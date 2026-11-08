# Design a unique ID generator in distributed systems

## Design a unique ID generator in distributed systems

<section class="chapter-video" aria-label="Video for Design a unique ID generator in distributed systems"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Design a unique ID generator in distributed systems</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this chapter, you are asked to design a unique ID generator in distributed systems. Your first thought might be to use a primary key with the <em>auto_increment</em> attribute in a traditional database. However, <em>auto_increment</em> does not work in a distributed environment because a single database server is not large enough and generating unique IDs across multiple databases with minimal delay is challenging.</p>
<p>Here are a few examples of unique IDs:</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-091.jpeg" rel="noopener" target="_blank"><img alt="Design a unique ID generator in distributed systems — original diagram 91" height="757" loading="lazy" src="../../assets/system-design/figure-091.jpeg" width="603"/></a></figure>

## Step 1 - Understand the problem and establish design scope

<section class="chapter-video" aria-label="Video for Step 1 - Understand the problem and establish design scope"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 1 - Understand the problem and establish design scope</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Asking clarification questions is the first step to tackle any system design interview question. Here is an example of candidate-interviewer interaction:</p>
<p><strong>Candidate</strong>: What are the characteristics of unique IDs? <strong>Interviewer</strong>: IDs must be unique and sortable.</p>
<p><strong>Candidate</strong>: For each new record, does ID increment by 1? <strong>Interviewer</strong>: The ID increments by time but not necessarily only increments by 1. IDs created in the evening are larger than those created in the morning on the same day.</p>
<p><strong>Candidate</strong>: Do IDs only contain numerical values? <strong>Interviewer</strong>: Yes, that is correct.</p>
<p><strong>Candidate</strong>: What is the ID length requirement? <strong>Interviewer</strong>: IDs should fit into 64-bit.</p>
<p><strong>Candidate</strong>: What is the scale of the system? <strong>Interviewer</strong>: The system should be able to generate 10,000 IDs per second.</p>
<p>Above are some of the sample questions that you can ask your interviewer. It is important to understand the requirements and clarify ambiguities. For this interview question, the requirements are listed as follows:</p>
<ul><li>IDs must be unique.</li><li>IDs are numerical values only.</li><li>IDs fit into 64-bit.</li><li>IDs are ordered by date.</li><li>Ability to generate over 10,000 unique IDs per second.</li></ul>

## Step 2 - Propose high-level design and get buy-in

<section class="chapter-video" aria-label="Video for Step 2 - Propose high-level design and get buy-in"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 2 - Propose high-level design and get buy-in</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Multiple options can be used to generate unique IDs in distributed systems. The options we considered are:</p>
<ul><li>Multi-master replication</li><li>Universally unique identifier (UUID)</li><li>Ticket server</li><li>Twitter snowflake approach</li></ul>
<p>Let us look at each of them, how they work, and the pros/cons of each option.</p>

## Multi-master replication

<section class="chapter-video" aria-label="Video for Multi-master replication"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Multi-master replication</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>As shown in Figure 7-2, the first approach is multi-master replication.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-092.jpeg" rel="noopener" target="_blank"><img alt="Design a unique ID generator in distributed systems — original diagram 92" height="402" loading="lazy" src="../../assets/system-design/figure-092.jpeg" width="715"/></a></figure>
<p>This approach uses the databases’ <em>auto_increment</em> feature. Instead of increasing the next ID by 1, we increase it by <em>k, </em>where <em>k</em> is the number of database servers in use. As illustrated in Figure 7-2, next ID to be generated is equal to the previous ID in the same server plus 2. This solves some scalability issues because IDs can scale with the number of database servers. However, this strategy has some major drawbacks:</p>
<ul><li>Hard to scale with multiple data centers</li><li>IDs do not go up with time across multiple servers.</li><li>It does not scale well when a server is added or removed.</li></ul>

## UUID

<section class="chapter-video" aria-label="Video for UUID"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>UUID</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>A UUID is another easy way to obtain unique IDs. UUID is a 128-bit number used to identify information in computer systems. UUID has a very low probability of getting collusion. Quoted from Wikipedia, “after generating 1 billion UUIDs every second for approximately 100 years would the probability of creating a single duplicate reach 50%” <a href="study:system-design/lessons/07-09-step-4-wrap-up/#reference-7-1">[1]</a>.</p>
<p>Here is an example of UUID: <em>09c93e62-50b4-468d-bf8a-c07e1040bfb2</em>. UUIDs can be generated independently without coordination between servers. Figure 7-3 presents the UUIDs design.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-093.jpeg" rel="noopener" target="_blank"><img alt="Design a unique ID generator in distributed systems — original diagram 93" height="284" loading="lazy" src="../../assets/system-design/figure-093.jpeg" width="940"/></a></figure>
<p>In this design, each web server contains an ID generator, and a web server is responsible for generating IDs independently.</p>
<p>Pros:</p>
<ul><li>Generating UUID is simple. No coordination between servers is needed so there will not be any synchronization issues.</li><li>The system is easy to scale because each web server is responsible for generating IDs they consume. ID generator can easily scale with web servers. Cons:</li></ul>
<ul><li>IDs are 128 bits long, but our requirement is 64 bits.</li><li>IDs do not go up with time.</li><li>IDs could be non-numeric.</li></ul>

## Ticket Server

<section class="chapter-video" aria-label="Video for Ticket Server"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Ticket Server</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Ticket servers are another interesting way to generate unique IDs. Flicker developed ticket servers to generate distributed primary keys <a href="study:system-design/lessons/07-09-step-4-wrap-up/#reference-7-2">[2]</a>. It is worth mentioning how the system works.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-094.jpeg" rel="noopener" target="_blank"><img alt="Design a unique ID generator in distributed systems — original diagram 94" height="393" loading="lazy" src="../../assets/system-design/figure-094.jpeg" width="940"/></a></figure>
<p>The idea is to use a centralized <em>auto_increment</em> feature in a single database server (Ticket Server). To learn more about this, refer to flicker’s engineering blog article <a href="study:system-design/lessons/07-09-step-4-wrap-up/#reference-7-2">[2]</a>.</p>
<p>Pros:</p>
<ul><li>Numeric IDs.</li><li>It is easy to implement, and it works for small to medium-scale applications.</li></ul>
<p>Cons:</p>
<ul><li>Single point of failure. Single ticket server means if the ticket server goes down, all systems that depend on it will face issues. To avoid a single point of failure, we can set up multiple ticket servers. However, this will introduce new challenges such as data synchronization.</li></ul>

## Twitter snowflake approach

<section class="chapter-video" aria-label="Video for Twitter snowflake approach"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Twitter snowflake approach</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Approaches mentioned above give us some ideas about how different ID generation systems work. However, none of them meet our specific requirements; thus, we need another approach. Twitter’s unique ID generation system called “snowflake” <a href="study:system-design/lessons/07-09-step-4-wrap-up/#reference-7-3">[3]</a> is inspiring and can satisfy our requirements.</p>
<p>Divide and conquer is our friend. Instead of generating an ID directly, we divide an ID into different sections. Figure 7-5 shows the layout of a 64-bit ID.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-095.jpeg" rel="noopener" target="_blank"><img alt="Design a unique ID generator in distributed systems — original diagram 95" height="150" loading="lazy" src="../../assets/system-design/figure-095.jpeg" width="940"/></a></figure>
<p>Each section is explained below.</p>
<ul><li>Sign bit: 1 bit. It will always be 0. This is reserved for future uses. It can potentially be used to distinguish between signed and unsigned numbers.</li><li>Timestamp: 41 bits. Milliseconds since the epoch or custom epoch. We use Twitter snowflake default epoch 1288834974657, equivalent to Nov 04, 2010, 01:42:54 UTC.</li><li>Datacenter ID: 5 bits, which gives us <em>2 ^ 5 = 32</em> datacenters.</li><li>Machine ID: 5 bits, which gives us <em>2 ^ 5 = 32</em> machines per datacenter.</li><li>Sequence number: 12 bits. For every ID generated on that machine/process, the sequence number is incremented by 1. The number is reset to 0 every millisecond.</li></ul>

## Step 3 - Design deep dive

<section class="chapter-video" aria-label="Video for Step 3 - Design deep dive"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 3 - Design deep dive</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In the high-level design, we discussed various options to design a unique ID generator in distributed systems. We settle on an approach that is based on the Twitter snowflake ID generator. Let us dive deep into the design. To refresh our memory, the design diagram is relisted below.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-096.jpeg" rel="noopener" target="_blank"><img alt="Design a unique ID generator in distributed systems — original diagram 96" height="150" loading="lazy" src="../../assets/system-design/figure-096.jpeg" width="940"/></a></figure>
<p>Datacenter IDs and machine IDs are chosen at the startup time, generally fixed once the system is up running. Any changes in datacenter IDs and machine IDs require careful review since an accidental change in those values can lead to ID conflicts. Timestamp and sequence numbers are generated when the ID generator is running.</p>
<p><strong>Timestamp</strong> The most important 41 bits make up the timestamp section. As timestamps grow with time, IDs are sortable by time. Figure 7-7 shows an example of how binary representation is converted to UTC. You can also convert UTC back to binary representation using a similar method.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-097.jpeg" rel="noopener" target="_blank"><img alt="Design a unique ID generator in distributed systems — original diagram 97" height="808" loading="lazy" src="../../assets/system-design/figure-097.jpeg" width="940"/></a></figure>
<p>The maximum timestamp that can be represented in 41 bits is</p>
<p><em>2 ^ 41 - 1 = 2199023255551</em> milliseconds (ms), which gives us: ~ 69 years =</p>
<p><em>2199023255551 ms / 1000 seconds / 365 days / 24 hours/ 3600 seconds</em>. This means the ID generator will work for 69 years and having a custom epoch time close to today’s date delays the overflow time. After 69 years, we will need a new epoch time or adopt other techniques to migrate IDs.</p>
<p><strong>Sequence number</strong> Sequence number is 12 bits, which give us 2 ^ 12 = 4096 combinations. This field is 0 unless more than one ID is generated in a millisecond on the same server. In theory, a machine can support a maximum of 4096 new IDs per millisecond.</p>

## Step 4 - Wrap up

<section class="chapter-video" aria-label="Video for Step 4 - Wrap up"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 4 - Wrap up</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this chapter, we discussed different approaches to design a unique ID generator: multi-master replication, UUID, ticket server, and Twitter snowflake-like unique ID generator. We settle on snowflake as it supports all our use cases and is scalable in a distributed environment.</p>
<p>If there is extra time at the end of the interview, here are a few additional talking points:</p>
<ul><li>Clock synchronization. In our design, we assume ID generation servers have the same clock. This assumption might not be true when a server is running on multiple cores. The same challenge exists in multi-machine scenarios. Solutions to clock synchronization are out of the scope of this book; however, it is important to understand the problem exists. Network Time Protocol is the most popular solution to this problem. For interested readers, refer to the reference material <a href="study:system-design/lessons/07-09-step-4-wrap-up/#reference-7-4">[4]</a>.</li><li>Section length tuning. For example, fewer sequence numbers but more timestamp bits are effective for low concurrency and long-term applications.</li><li>High availability. Since an ID generator is a mission-critical system, it must be highly available.</li></ul>
<p>Congratulations on getting this far! Now give yourself a pat on the back. Good job!</p>

<section class="lesson-references"><h3 id="references-7">References</h3><ol><li id="reference-7-1" value="1">Universally unique identifier: <a href="https://en.wikipedia.org/wiki/Universally_unique_identifier">https://en.wikipedia.org/wiki/Universally_unique_identifier</a></li><li id="reference-7-2" value="2">Ticket Servers: Distributed Unique Primary Keys on the Cheap: <a href="https://code.flickr.net/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-thecheap/">https://code.flickr.net/2010/02/08/ticket-servers-distributed-unique-primary-keys-on-thecheap/</a></li><li id="reference-7-3" value="3">Announcing Snowflake: <a href="https://blog.twitter.com/engineering/en_us/a/2010/announcingsnowflake.html">https://blog.twitter.com/engineering/en_us/a/2010/announcingsnowflake.html</a></li><li id="reference-7-4" value="4">Network time protocol: <a href="https://en.wikipedia.org/wiki/Network_Time_Protocol">https://en.wikipedia.org/wiki/Network_Time_Protocol</a></li></ol></section>
