# Design a key-value store

## Design a key-value store

<section class="chapter-video" aria-label="Video for Design a key-value store"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Design a key-value store</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>A key-value store, also referred to as a key-value database, is a non-relational database. Each unique identifier is stored as a key with its associated value. This data pairing is known as a “key-value” pair.</p>
<p>In a key-value pair, the key must be unique, and the value associated with the key can be accessed through the key. Keys can be plain text or hashed values. For performance reasons, a short key works better. What do keys look like? Here are a few examples:</p>
<ul><li>Plain text key: “last_logged_in_at”</li><li>Hashed key: 253DDEC4</li></ul>
<p>The value in a key-value pair can be strings, lists, objects, etc. The value is usually treated as an opaque object in key-value stores, such as Amazon dynamo <a href="study:system-design/lessons/06-15-summary/#reference-6-1">[1]</a>, Memcached <a href="study:system-design/lessons/06-15-summary/#reference-6-2">[2]</a>, Redis <a href="study:system-design/lessons/06-15-summary/#reference-6-3">[3]</a>, etc.</p>
<p>Here is a data snippet in a key-value store:</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-068.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 68" height="267" loading="lazy" src="../../assets/system-design/figure-068.jpeg" width="941"/></a></figure>
<p>In this chapter, you are asked to design a key-value store that supports the following operations:</p>
<p>- put(key, value)  // insert “value” associated with “key”</p>
<p>- get(key)  // get “value” associated with “key”</p>

## Understand the problem and establish design scope

<section class="chapter-video" aria-label="Video for Understand the problem and establish design scope"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Understand the problem and establish design scope</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>There is no perfect design. Each design achieves a specific balance regarding the tradeoffs of the read, write, and memory usage. Another tradeoff has to be made was between consistency and availability. In this chapter, we design a key-value store that comprises of the following characteristics:</p>
<ul><li>The size of a key-value pair is small: less than 10 KB.</li><li>Ability to store big data.</li><li>High availability: The system responds quickly, even during failures.</li><li>High scalability: The system can be scaled to support large data set.</li><li>Automatic scaling: The addition/deletion of servers should be automatic based on traffic.</li><li>Tunable consistency.</li><li>Low latency.</li></ul>

## Single server key-value store

<section class="chapter-video" aria-label="Video for Single server key-value store"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Single server key-value store</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Developing a key-value store that resides in a single server is easy. An intuitive approach is to store key-value pairs in a hash table, which keeps everything in memory. Even though memory access is fast, fitting everything in memory may be impossible due to the space constraint. Two optimizations can be done to fit more data in a single server:</p>
<ul><li>Data compression</li><li>Store only frequently used data in memory and the rest on disk</li></ul>
<p>Even with these optimizations, a single server can reach its capacity very quickly. A distributed key-value store is required to support big data.</p>

## Distributed key-value store

<section class="chapter-video" aria-label="Video for Distributed key-value store"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Distributed key-value store</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>A distributed key-value store is also called a distributed hash table, which distributes keyvalue pairs across many servers. When designing a distributed system, it is important to understand CAP (<strong>C</strong>onsistency, <strong>A</strong>vailability, <strong>P</strong>artition Tolerance) theorem.</p>

## CAP theorem

<section class="chapter-video" aria-label="Video for CAP theorem"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>CAP theorem</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>CAP theorem states it is impossible for a distributed system to simultaneously provide more than two of these three guarantees: consistency, availability, and partition tolerance. Let us establish a few definitions.</p>
<p><strong>Consistency</strong>: consistency means all clients see the same data at the same time no matter which node they connect to.</p>
<p><strong>Availability: </strong>availability means any client which requests data gets a response even if some of the nodes are down.</p>
<p><strong>Partition Tolerance: </strong>a partition indicates a communication break between two nodes. Partition tolerance means the system continues to operate despite network partitions.</p>
<p>CAP theorem states that one of the three properties must be sacrificed to support 2 of the 3 properties as shown in Figure 6-1.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-069.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 69" height="657" loading="lazy" src="../../assets/system-design/figure-069.jpeg" width="657"/></a></figure>
<p>Nowadays, key-value stores are classified based on the two CAP characteristics they support:</p>
<p><strong>CP (consistency and partition tolerance) systems</strong>: a CP key-value store supports consistency and partition tolerance while sacrificing availability.</p>
<p><strong>AP (availability and partition tolerance) systems</strong>: an AP key-value store supports availability and partition tolerance while sacrificing consistency.</p>
<p><strong>CA (consistency and availability) systems</strong>: a CA key-value store supports consistency and availability while sacrificing partition tolerance. Since network failure is unavoidable, a distributed system must tolerate network partition. Thus, a CA system cannot exist in real-world applications.</p>

<p>What you read above is mostly the definition part. To make it easier to understand, let us take a look at some concrete examples. In distributed systems, data is usually replicated multiple times. Assume data are replicated on three replica nodes, <em>n1</em>, <em>n2</em> and <em>n3</em> as shown in Figure 6- 2.</p>
<p><strong>Ideal situation</strong> In the ideal world, network partition never occurs. Data written to <em>n1</em> is automatically replicated to <em>n2</em> and <em>n3</em>. Both consistency and availability are achieved.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-070.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 70" height="873" loading="lazy" src="../../assets/system-design/figure-070.jpeg" width="933"/></a></figure>
<p><strong>Real-world distributed systems</strong> In a distributed system, partitions cannot be avoided, and when a partition occurs, we must choose between consistency and availability. In Figure 6-3, <em>n3</em> goes down and cannot communicate with <em>n1</em> and <em>n2</em>. If clients write data to <em>n1</em> or <em>n2</em>, data cannot be propagated to n3. If data is written to <em>n3</em> but not propagated to <em>n1</em> and <em>n2</em> yet, <em>n1</em> and <em>n2</em> would have stale data.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-071.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 71" height="873" loading="lazy" src="../../assets/system-design/figure-071.jpeg" width="933"/></a></figure>
<p>If we choose consistency over availability (CP system), we must block all write operations to <em>n1</em> and <em>n2</em> to avoid data inconsistency among these three servers, which makes the system unavailable. Bank systems usually have extremely high consistent requirements. For example, it is crucial for a bank system to display the most up-to-date balance info. If inconsistency occurs due to a network partition, the bank system returns an error before the inconsistency is resolved.</p>
<p>However, if we choose availability over consistency (AP system), the system keeps accepting reads, even though it might return stale data. For writes, <em>n1</em> and <em>n2</em> will keep accepting writes, and data will be synced to <em>n3</em> when the network partition is resolved.</p>
<p>Choosing the right CAP guarantees that fit your use case is an important step in building a distributed key-value store. You can discuss this with your interviewer and design the system accordingly.</p>

## System components

<section class="chapter-video" aria-label="Video for System components"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>System components</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this section, we will discuss the following core components and techniques used to build a key-value store:</p>
<ul><li>Data partition</li><li>Data replication</li><li>Consistency</li><li>Inconsistency resolution</li><li>Handling failures</li><li>System architecture diagram</li><li>Write path</li><li>Read path</li></ul>
<p>The content below is largely based on three popular key-value store systems: Dynamo <a href="study:system-design/lessons/06-15-summary/#reference-6-4">[4]</a>, Cassandra <a href="study:system-design/lessons/06-15-summary/#reference-6-5">[5]</a>, and BigTable <a href="study:system-design/lessons/06-15-summary/#reference-6-6">[6]</a>.</p>

## Data partition

<section class="chapter-video" aria-label="Video for Data partition"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Data partition</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>For large applications, it is infeasible to fit the complete data set in a single server. The simplest way to accomplish this is to split the data into smaller partitions and store them in multiple servers. There are two challenges while partitioning the data:</p>
<ul><li>Distribute data across multiple servers evenly.</li><li>Minimize data movement when nodes are added or removed.</li></ul>
<p>Consistent hashing discussed in Chapter 5 is a great technique to solve these problems. Let us revisit how consistent hashing works at a high-level.</p>
<ul><li>First, servers are placed on a hash ring. In Figure 6-4, eight servers, represented by <em>s0,</em> <em>s1, ..., s7</em>, are placed on the hash ring.</li><li>Next, a key is hashed onto the same ring, and it is stored on the first server encountered while moving in the clockwise direction. For instance, <em>key0</em> is stored in <em>s1</em> using this logic.</li></ul>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-072.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 72" height="1143" loading="lazy" src="../../assets/system-design/figure-072.jpeg" width="1059"/></a></figure>
<p>Using consistent hashing to partition data has the following advantages:</p>
<p><strong>Automatic scaling: </strong>servers could be added and removed automatically depending on the load.</p>

<p><strong>Heterogeneity:</strong> the number of virtual nodes for a server is proportional to the server capacity. For example, servers with higher capacity are assigned with more virtual nodes.</p>

## Data replication

<section class="chapter-video" aria-label="Video for Data replication"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Data replication</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>To achieve high availability and reliability, data must be replicated asynchronously over <em>N</em> servers, where <em>N</em> is a configurable parameter. These <em>N </em>servers are chosen using the following logic: after a key is mapped to a position on the hash ring, walk clockwise from that position and choose the first <em>N</em> servers on the ring to store data copies. In Figure 6-5 (<em>N = 3</em>), <em>key0</em> is replicated at <em>s1, s2,</em> and <em>s3</em>.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-073.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 73" height="741" loading="lazy" src="../../assets/system-design/figure-073.jpeg" width="675"/></a></figure>
<p>With virtual nodes, the first <em>N</em> nodes on the ring may be owned by fewer than <em>N</em> physical servers. To avoid this issue, we only choose unique servers while performing the clockwise walk logic.</p>
<p>Nodes in the same data center often fail at the same time due to power outages, network issues, natural disasters, etc. For better reliability, replicas are placed in distinct data centers, and data centers are connected through high-speed networks.</p>

## Consistency

<section class="chapter-video" aria-label="Video for Consistency"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Consistency</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Since data is replicated at multiple nodes, it must be synchronized across replicas. Quorum consensus can guarantee consistency for both read and write operations. Let us establish a few definitions first.</p>
<p><strong>N</strong> = The number of replicas</p>
<p><strong>W</strong> = A write quorum of size <em>W</em>. For a write operation to be considered as successful, write operation must be acknowledged from <em>W</em> replicas.</p>
<p><strong>R</strong> = A read quorum of size <em>R</em>. For a read operation to be considered as successful, read operation must wait for responses from at least <em>R </em>replicas.</p>
<p>Consider the following example shown in Figure 6-6 with <em>N = 3</em>.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-074.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 74" height="633" loading="lazy" src="../../assets/system-design/figure-074.jpeg" width="639"/></a></figure>
<p><em>W = 1</em> does not mean data is written on one server. For instance, with the configuration in Figure 6-6, data is replicated at <em>s0</em>, <em>s1,</em> and <em>s2</em>. <em>W = 1</em> means that the coordinator must receive at least one acknowledgment before the write operation is considered as successful. For instance, if we get an acknowledgment from <em>s1</em>, we no longer need to wait for acknowledgements from <em>s0</em> and <em>s2</em>. A coordinator acts as a proxy between the client and the nodes.</p>
<p>The configuration of <em>W, R</em> and <em>N</em> is a typical tradeoff between latency and consistency. If <em>W =</em> <em>1</em> or <em>R = 1</em>, an operation is returned quickly because a coordinator only needs to wait for a response from any of the replicas. If <em>W</em> or <em>R &gt; 1</em>, the system offers better consistency; however, the query will be slower because the coordinator must wait for the response from the slowest replica.</p>
<p>If <em>W + R &gt; N</em>, strong consistency is guaranteed because there must be at least one overlapping node that has the latest data to ensure consistency.</p>

<p>How to configure <em>N, W</em>, and <em>R </em>to fit our use cases? Here are some of the possible setups:</p>
<p>If <em>R = 1</em> and <em>W = N</em>, the system is optimized for a fast read.</p>
<p>If <em>W = 1 and R = N</em>, the system is optimized for fast write.</p>
<p>If <em>W + R &gt; N</em>, strong consistency is guaranteed (Usually <em>N = 3, W = R = 2</em>).</p>
<p>If <em>W + R &lt;= N</em>, strong consistency is not guaranteed.</p>
<p>Depending on the requirement, we can tune the values of <em>W, R, N</em> to achieve the desired level of consistency.</p>
<p><strong>Consistency models</strong> Consistency model is other important factor to consider when designing a key-value store. A consistency model defines the degree of data consistency, and a wide spectrum of possible consistency models exist:</p>
<ul><li>Strong consistency: any read operation returns a value corresponding to the result of the most updated write data item. A client never sees out-of-date data.</li><li>Weak consistency: subsequent read operations may not see the most updated value.</li><li>Eventual consistency: this is a specific form of weak consistency. Given enough time, all updates are propagated, and all replicas are consistent.</li></ul>
<p>Strong consistency is usually achieved by forcing a replica not to accept new reads/writes until every replica has agreed on current write. This approach is not ideal for highly available systems because it could block new operations. Dynamo and Cassandra adopt eventual consistency, which is our recommended consistency model for our key-value store. From concurrent writes, eventual consistency allows inconsistent values to enter the system and force the client to read the values to reconcile. The next section explains how reconciliation works with versioning.</p>

## Inconsistency resolution: versioning

<section class="chapter-video" aria-label="Video for Inconsistency resolution: versioning"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Inconsistency resolution: versioning</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Replication gives high availability but causes inconsistencies among replicas. Versioning and vector locks are used to solve inconsistency problems. Versioning means treating each data modification as a new immutable version of data. Before we talk about versioning, let us use an example to explain how inconsistency happens:</p>
<p>As shown in Figure 6-7, both replica nodes <em>n1</em> and <em>n2</em> have the same value. Let us call this value the original <em>value. Server 1</em> and <em>server 2</em> get the same value for <em>get(“name”)</em> operation.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-075.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 75" height="492" loading="lazy" src="../../assets/system-design/figure-075.jpeg" width="780"/></a></figure>
<p>Next, <em>server 1</em> changes the name to “johnSanFrancisco”, and <em>server 2</em> changes the name to “johnNewYork” as shown in Figure 6-8. These two changes are performed simultaneously. Now, we have conflicting values, called versions <em>v1</em> and <em>v2</em>.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-076.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 76" height="407" loading="lazy" src="../../assets/system-design/figure-076.jpeg" width="798"/></a></figure>
<p>In this example, the original value could be ignored because the modifications were based on it. However, there is no clear way to resolve the conflict of the last two versions. To resolve this issue, we need a versioning system that can detect conflicts and reconcile conflicts. A vector clock is a common technique to solve this problem. Let us examine how vector clocks work.</p>
<p>A vector clock is a <em>[server, version] </em>pair associated with a data item. It can be used to check if one version precedes, succeeds, or in conflict with others.</p>
<p>Assume a vector clock is represented by <em>D([S1, v1], [S2, v2], ..., [Sn, vn])</em>, where <em>D</em> is a data item, <em>v1</em> is a version counter, and <em>s1</em> is a server number, etc. If data item <em>D</em> is written to server <em>Si</em>, the system must perform one of the following tasks.</p>
<ul><li>Increment <em>vi</em> if <em>[Si, vi]</em> exists.</li><li>Otherwise, create a new entry <em>[Si, 1]</em>.</li></ul>
<p>The above abstract logic is explained with a concrete example as shown in Figure 6-9.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-077.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 77" height="892" loading="lazy" src="../../assets/system-design/figure-077.jpeg" width="805"/></a></figure>
<ol start="1"><li>A client writes a data item <em>D1</em> to the system, and the write is handled by server <em>Sx</em>, which now has the vector clock <em>D1[(Sx, 1)]</em>.</li><li>Another client reads the latest <em>D1</em>, updates it to <em>D2</em>, and writes it back. <em>D2</em> descends from <em>D1</em> so it overwrites <em>D1</em>. Assume the write is handled by the same server <em>Sx</em>, which now has vector clock <em>D2([Sx, 2])</em>.</li><li>Another client reads the latest <em>D2</em>, updates it to <em>D3</em>, and writes it back. Assume the write is handled by server <em>Sy</em>, which now has vector clock <em>D3([Sx, 2], [Sy, 1]))</em>.</li><li>Another client reads the latest <em>D2</em>, updates it to <em>D4</em>, and writes it back. Assume the write</li></ol>
<p>is handled by server <em>Sz</em>, which now has <em>D4([Sx, 2], [Sz, 1]))</em>. 5. When another client reads <em>D3</em> and <em>D4</em>, it discovers a conflict, which is caused by data item <em>D2</em> being modified by both <em>Sy</em> and <em>Sz</em>. The conflict is resolved by the client and updated data is sent to the server. Assume the write is handled by <em>Sx</em>, which now has <em>D5([Sx, 3], [Sy, 1], [Sz, 1])</em>. We will explain how to detect conflict shortly.</p>
<p>Using vector clocks, it is easy to tell that a version <em>X</em> is an ancestor (i.e. no conflict) of version <em>Y</em> if the version counters for each participant in the vector clock of <em>Y</em> is greater than or equal to the ones in version <em>X</em>. For example, the vector clock <em>D([s0, 1], [s1, 1])]</em> is an ancestor of <em>D([s0, 1], [s1, 2])</em>. Therefore, no conflict is recorded.</p>
<p>Similarly, you can tell that a version <em>X</em> is a sibling (i.e., a conflict exists) of <em>Y</em> if there is any participant in <em>Y</em>'s vector clock who has a counter that is less than its corresponding counter in <em>X</em>. For example, the following two vector clocks indicate there is a conflict: <em>D([s0, 1], [s1,</em> <em>2])</em> and <em>D([s0, 2], [s1, 1]).</em></p>
<p>Even though vector clocks can resolve conflicts, there are two notable downsides. First, vector clocks add complexity to the client because it needs to implement conflict resolution logic.</p>
<p>Second, the <em>[server: version]</em> pairs in the vector clock could grow rapidly. To fix this problem, we set a threshold for the length, and if it exceeds the limit, the oldest pairs are removed. This can lead to inefficiencies in reconciliation because the descendant relationship cannot be determined accurately. However, based on Dynamo paper <a href="study:system-design/lessons/06-15-summary/#reference-6-4">[4]</a>, Amazon has not yet encountered this problem in production; therefore, it is probably an acceptable solution for most companies.</p>

## Handling failures

<section class="chapter-video" aria-label="Video for Handling failures"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Handling failures</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>As with any large system at scale, failures are not only inevitable but common. Handling failure scenarios is very important. In this section, we first introduce techniques to detect failures. Then, we go over common failure resolution strategies.</p>
<p><strong>Failure detection</strong> In a distributed system, it is insufficient to believe that a server is down because another server says so. Usually, it requires at least two independent sources of information to mark a server down.</p>
<p>As shown in Figure 6-10, all-to-all multicasting is a straightforward solution. However, this is inefficient when many servers are in the system.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-078.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 78" height="657" loading="lazy" src="../../assets/system-design/figure-078.jpeg" width="610"/></a></figure>
<p>A better solution is to use decentralized failure detection methods like gossip protocol. Gossip protocol works as follows:</p>
<ul><li>Each node maintains a node membership list, which contains member IDs and heartbeat counters.</li><li>Each node periodically increments its heartbeat counter.</li><li>Each node periodically sends heartbeats to a set of random nodes, which in turn propagate to another set of nodes.</li><li>Once nodes receive heartbeats, membership list is updated to the latest info.</li><li>If the heartbeat has not increased for more than predefined periods, the member is considered as offline.</li></ul>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-079.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 79" height="402" loading="lazy" src="../../assets/system-design/figure-079.jpeg" width="941"/></a></figure>
<p>As shown in Figure 6-11:</p>
<ul><li>Node <em>s0</em> maintains a node membership list shown on the left side.</li><li>Node <em>s0</em> notices that node s2’s (member ID = 2) heartbeat counter has not increased for a long time.</li><li>Node <em>s0</em> sends heartbeats that include <em>s2</em>’s info to a set of random nodes. Once other nodes confirm that <em>s2</em>’s heartbeat counter has not been updated for a long time, node <em>s2</em> is marked down, and this information is propagated to other nodes.</li></ul>
<p><strong>Handling temporary failures</strong> After failures have been detected through the gossip protocol, the system needs to deploy certain mechanisms to ensure availability. In the strict quorum approach, read and write operations could be blocked as illustrated in the quorum consensus section.</p>
<p>A technique called “sloppy quorum” <a href="study:system-design/lessons/06-15-summary/#reference-6-4">[4]</a> is used to improve availability. Instead of enforcing the quorum requirement, the system chooses the first <em>W</em> healthy servers for writes and first <em>R</em> healthy servers for reads on the hash ring. Offline servers are ignored.</p>
<p>If a server is unavailable due to network or server failures, another server will process requests temporarily. When the down server is up, changes will be pushed back to achieve data consistency. This process is called hinted handoff. Since <em>s2</em> is unavailable in Figure 6- 12, reads and writes will be handled by <em>s3</em> temporarily. When <em>s2</em> comes back online, <em>s3</em> will hand the data back to <em>s2</em>.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-080.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 80" height="1143" loading="lazy" src="../../assets/system-design/figure-080.jpeg" width="1143"/></a></figure>
<p><strong>Handling permanent failures</strong></p>
<p>Hinted handoff is used to handle temporary failures. What if a replica is permanently unavailable? To handle such a situation, we implement an anti-entropy protocol to keep replicas in sync. Anti-entropy involves comparing each piece of data on replicas and updating each replica to the newest version. A Merkle tree is used for inconsistency detection and minimizing the amount of data transferred.</p>
<p>Quoted from Wikipedia <a href="study:system-design/lessons/06-15-summary/#reference-6-7">[7]</a>: “A hash tree or Merkle tree is a tree in which every non-leaf node is labeled with the hash of the labels or values (in case of leaves) of its child nodes. Hash trees allow efficient and secure verification of the contents of large data structures”.</p>
<p>Assuming key space is from 1 to 12, the following steps show how to build a Merkle tree. Highlighted boxes indicate inconsistency.</p>
<p>Step 1: Divide key space into buckets (4 in our example) as shown in Figure 6-13.  A bucket is used as the root level node to maintain a limited depth of the tree.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-081.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 81" height="528" loading="lazy" src="../../assets/system-design/figure-081.jpeg" width="1353"/></a></figure>
<p>Step 2: Once the buckets are created, hash each key in a bucket using a uniform hashing method (Figure 6-14).</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-082.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 82" height="200" loading="lazy" src="../../assets/system-design/figure-082.jpeg" width="940"/></a></figure>
<p>Step 3: Create a single hash node per bucket (Figure 6-15).</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-083.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 83" height="276" loading="lazy" src="../../assets/system-design/figure-083.jpeg" width="940"/></a></figure>
<p>Step 4: Build the tree upwards till root by calculating hashes of children (Figure 6-16).</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-084.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 84" height="490" loading="lazy" src="../../assets/system-design/figure-084.jpeg" width="940"/></a></figure>
<p>To compare two Merkle trees, start by comparing the root hashes. If root hashes match, both servers have the same data. If root hashes disagree, then the left child hashes are compared followed by right child hashes. You can traverse the tree to find which buckets are not synchronized and synchronize those buckets only.</p>
<p>Using Merkle trees, the amount of data needed to be synchronized is proportional to the differences between the two replicas, and not the amount of data they contain. In real-world systems, the bucket size is quite big. For instance, a possible configuration is one million buckets per one billion keys, so each bucket only contains 1000 keys.</p>
<p><strong>Handling data center outage</strong> Data center outage could happen due to power outage, network outage, natural disaster, etc. To build a system capable of handling data center outage, it is important to replicate data across multiple data centers. Even if a data center is completely offline, users can still access data through the other data centers.</p>

## System architecture diagram

<section class="chapter-video" aria-label="Video for System architecture diagram"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>System architecture diagram</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Now that we have discussed different technical considerations in designing a key-value store, we can shift our focus on the architecture diagram, shown in Figure 6-17.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-085.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 85" height="570" loading="lazy" src="../../assets/system-design/figure-085.jpeg" width="941"/></a></figure>
<p>Main features of the architecture are listed as follows:</p>
<ul><li>Clients communicate with the key-value store through simple APIs: <em>get(key)</em> and <em>put(key,</em> <em>value)</em>.</li><li>A coordinator is a node that acts as a proxy between the client and the key-value store.</li><li>Nodes are distributed on a ring using consistent hashing.</li><li>The system is completely decentralized so adding and moving nodes can be automatic.</li><li>Data is replicated at multiple nodes.</li><li>There is no single point of failure as every node has the same set of responsibilities. As the design is decentralized, each node performs many tasks as presented in Figure 6-18.</li></ul>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-086.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 86" height="705" loading="lazy" src="../../assets/system-design/figure-086.jpeg" width="658"/></a></figure>

## Write path

<section class="chapter-video" aria-label="Video for Write path"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Write path</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Figure 6-19 explains what happens after a write request is directed to a specific node. Please note the proposed designs for write/read paths are primary based on the architecture of Cassandra <a href="study:system-design/lessons/06-15-summary/#reference-6-8">[8]</a>.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-087.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 87" height="499" loading="lazy" src="../../assets/system-design/figure-087.jpeg" width="940"/></a></figure>
<ol start="1"><li>The write request is persisted on a commit log file.</li><li>Data is saved in the memory cache.</li></ol>
<ol start="3"><li>When the memory cache is full or reaches a predefined threshold, data is flushed to SSTable <a href="study:system-design/lessons/06-15-summary/#reference-6-9">[9]</a> on disk. Note: A sorted-string table (SSTable) is a sorted list of &lt;key, value&gt; pairs. For readers interested in learning more about SStable, refer to the reference material <a href="study:system-design/lessons/06-15-summary/#reference-6-9">[9]</a>.</li></ol>

## Read path

<section class="chapter-video" aria-label="Video for Read path"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Read path</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>After a read request is directed to a specific node, it first checks if data is in the memory cache. If so, the data is returned to the client as shown in Figure 6-20.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-088.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 88" height="478" loading="lazy" src="../../assets/system-design/figure-088.jpeg" width="940"/></a></figure>
<p>If the data is not in memory, it will be retrieved from the disk instead. We need an efficient way to find out which SSTable contains the key. Bloom filter <a href="study:system-design/lessons/06-15-summary/#reference-6-10">[10]</a> is commonly used to solve this problem.</p>
<p>The read path is shown in Figure 6-21 when data is not in memory.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-089.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 89" height="472" loading="lazy" src="../../assets/system-design/figure-089.jpeg" width="940"/></a></figure>
<ol start="1"><li>The system first checks if data is in memory. If not, go to step 2.</li><li>If data is not in memory, the system checks the bloom filter.</li></ol>
<ol start="3"><li>The bloom filter is used to figure out which SSTables might contain the key.</li><li>SSTables return the result of the data set.</li><li>The result of the data set is returned to the client.</li></ol>

## Summary

<section class="chapter-video" aria-label="Video for Summary"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Summary</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>This chapter covers many concepts and techniques. To refresh your memory, the following table summarizes features and corresponding techniques used for a distributed key-value store.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-090.jpeg" rel="noopener" target="_blank"><img alt="Design a key-value store — original diagram 90" height="1056" loading="lazy" src="../../assets/system-design/figure-090.jpeg" width="1355"/></a></figure>

<section class="lesson-references"><h3 id="references-6">References</h3><ol><li id="reference-6-1" value="1">Amazon DynamoDB: <a href="https://aws.amazon.com/dynamodb/">https://aws.amazon.com/dynamodb/</a></li><li id="reference-6-2" value="2">memcached: <a href="https://memcached.org/">https://memcached.org/</a></li><li id="reference-6-3" value="3">Redis: <a href="https://redis.io/">https://redis.io/</a></li><li id="reference-6-4" value="4">Dynamo: Amazon’s Highly Available Key-value Store: <a href="https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf">https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf</a></li><li id="reference-6-5" value="5">Cassandra: <a href="https://cassandra.apache.org/">https://cassandra.apache.org/</a></li><li id="reference-6-6" value="6">Bigtable: A Distributed Storage System for Structured Data: <a href="https://static.googleusercontent.com/media/research.google.com/en//archive/bigtableosdi06.pdf">https://static.googleusercontent.com/media/research.google.com/en//archive/bigtableosdi06.pdf</a></li><li id="reference-6-7" value="7">Merkle tree: <a href="https://en.wikipedia.org/wiki/Merkle_tree">https://en.wikipedia.org/wiki/Merkle_tree</a></li><li id="reference-6-8" value="8">Cassandra architecture: <a href="https://cassandra.apache.org/doc/latest/architecture/">https://cassandra.apache.org/doc/latest/architecture/</a></li><li id="reference-6-9" value="9">SStable: <a href="https://www.igvita.com/2012/02/06/sstable-and-log-structured-storage-leveldb/">https://www.igvita.com/2012/02/06/sstable-and-log-structured-storage-leveldb/</a></li><li id="reference-6-10" value="10">Bloom filter <a href="https://en.wikipedia.org/wiki/Bloom_filter">https://en.wikipedia.org/wiki/Bloom_filter</a></li></ol></section>
