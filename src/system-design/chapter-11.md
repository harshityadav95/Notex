# Design a news feed system

## Design a news feed system

<section class="chapter-video" aria-label="Video for Design a news feed system"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Design a news feed system</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this chapter, you are asked to design a news feed system. What is news feed? According to the Facebook help page, “News feed is the constantly updating list of stories in the middle of your home page. News Feed includes status updates, photos, videos, links, app activity, and likes from people, pages, and groups that you follow on Facebook” <a href="study:system-design/lessons/11-11-step-4-wrap-up/#reference-11-1">[1]</a>. This is a popular interview question. Similar questions commonly asked are: design Facebook news feed, Instagram feed, Twitter timeline, etc.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-137.jpeg" rel="noopener" target="_blank"><img alt="Design a news feed system — original diagram 137" height="784" loading="lazy" src="../../assets/system-design/figure-137.jpeg" width="637"/></a></figure>

## Step 1 - Understand the problem and establish design scope

<section class="chapter-video" aria-label="Video for Step 1 - Understand the problem and establish design scope"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 1 - Understand the problem and establish design scope</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>The first set of clarification questions are to understand what the interviewer has in mind when she asks you to design a news feed system. At the very least, you should figure out what features to support. Here is an example of candidate-interviewer interaction:</p>
<p><strong>Candidate</strong>: Is this a mobile app? Or a web app? Or both? <strong>Interviewer</strong>: Both</p>
<p><strong>Candidate</strong>: What are the important features? <strong>Interview: </strong>A user can publish a post and see her friends’ posts on the news feed page.</p>
<p><strong>Candidate</strong>: Is the news feed sorted by reverse chronological order or any particular order such as topic scores? For instance, posts from your close friends have higher scores. <strong>Interviewer</strong>: To keep things simple, let us assume the feed is sorted by reverse chronological order.</p>
<p><strong>Candidate</strong>: How many friends can a user have? <strong>Interviewer</strong>: 5000</p>
<p><strong>Candidate</strong>: What is the traffic volume? <strong>Interviewer</strong>: 10 million DAU</p>
<p><strong>Candidate</strong>: Can feed contain images, videos, or just text? <strong>Interviewer</strong>: It can contain media files, including both images and videos.</p>
<p>Now you have gathered the requirements, we focus on designing the system.</p>

## Step 2 - Propose high-level design and get buy-in

<section class="chapter-video" aria-label="Video for Step 2 - Propose high-level design and get buy-in"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 2 - Propose high-level design and get buy-in</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>The design is divided into two flows: feed publishing and news feed building.</p>
<ul><li>Feed publishing: when a user publishes a post, corresponding data is written into cache and database. A post is populated to her friends’ news feed.</li><li>Newsfeed building: for simplicity, let us assume the news feed is built by aggregating friends’ posts in reverse chronological order.</li></ul>

## Newsfeed APIs

<section class="chapter-video" aria-label="Video for Newsfeed APIs"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Newsfeed APIs</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>The news feed APIs are the primary ways for clients to communicate with servers. Those APIs are HTTP based that allow clients to perform actions, which include posting a status, retrieving news feed, adding friends, etc. We discuss two most important APIs: feed publishing API and news feed retrieval API.</p>
<p><strong>Feed publishing API</strong> To publish a post, a HTTP POST request will be sent to the server. The API is shown below:</p>
<p><em>POST /v1/me/feed</em> Params:</p>
<ul><li>content: content is the text of the post.</li><li>auth_token: it is used to authenticate API requests.</li></ul>
<p><strong>Newsfeed retrieval API</strong> The API to retrieve news feed is shown below:</p>
<p><em>GET /v1/me/feed</em> Params:</p>
<ul><li>auth_token: it is used to authenticate API requests.</li></ul>

## Feed publishing

<section class="chapter-video" aria-label="Video for Feed publishing"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Feed publishing</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Figure 11-2 shows the high-level design of the feed publishing flow.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-138.jpeg" rel="noopener" target="_blank"><img alt="Design a news feed system — original diagram 138" height="930" loading="lazy" src="../../assets/system-design/figure-138.jpeg" width="560"/></a></figure>
<ul><li>User: a user can view news feeds on a browser or mobile app. A user makes a post with content “Hello” through API: <em>/v1/me/feed?content=Hello&amp;auth_token={auth_token}</em></li><li>Load balancer: distribute traffic to web servers.</li><li>Web servers: web servers redirect traffic to different internal services.</li><li>Post service: persist post in the database and cache.</li><li>Fanout service: push new content to friends’ news feed. Newsfeed data is stored in the cache for fast retrieval.</li><li>Notification service: inform friends that new content is available and send out push notifications.</li></ul>

## Newsfeed building

<section class="chapter-video" aria-label="Video for Newsfeed building"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Newsfeed building</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this section, we discuss how news feed is built behind the scenes. Figure 11-3 shows the high-level design:</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-139.jpeg" rel="noopener" target="_blank"><img alt="Design a news feed system — original diagram 139" height="736" loading="lazy" src="../../assets/system-design/figure-139.jpeg" width="470"/></a></figure>
<ul><li>User: a user sends a request to retrieve her news feed. The request looks like this: / v1/me/feed.</li><li>Load balancer: load balancer redirects traffic to web servers.</li><li>Web servers: web servers route requests to newsfeed service.</li><li>Newsfeed service: news feed service fetches news feed from the cache.</li><li>Newsfeed cache: store news feed IDs needed to render the news feed.</li></ul>

## Step 3 - Design deep dive

<section class="chapter-video" aria-label="Video for Step 3 - Design deep dive"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 3 - Design deep dive</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>The high-level design briefly covered two flows: feed publishing and news feed building. Here, we discuss those topics in more depth.</p>

## Feed publishing deep dive

<section class="chapter-video" aria-label="Video for Feed publishing deep dive"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Feed publishing deep dive</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Figure 11-4 outlines the detailed design for feed publishing. We have discussed most of components in high-level design, and we will focus on two components: web servers and fanout service.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-140.jpeg" rel="noopener" target="_blank"><img alt="Design a news feed system — original diagram 140" height="1109" loading="lazy" src="../../assets/system-design/figure-140.jpeg" width="940"/></a></figure>
<p><strong>Web servers</strong> Besides communicating with clients, web servers enforce authentication and rate-limiting.</p>
<p>Only users signed in with valid <em>auth_token</em> are allowed to make posts. The system limits the number of posts a user can make within a certain period, vital to prevent spam and abusive content.</p>
<p><strong>Fanout service</strong> Fanout is the process of delivering a post to all friends. Two types of fanout models are: fanout on write (also called push model) and fanout on read (also called pull model). Both models have pros and cons. We explain their workflows and explore the best approach to support our system.</p>
<p><strong>Fanout on write. </strong>With this approach, news feed is pre-computed during write time. A new post is delivered to friends’ cache immediately after it is published.</p>
<p>Pros:</p>
<ul><li>The news feed is generated in real-time and can be pushed to friends immediately.</li><li>Fetching news feed is fast because the news feed is pre-computed during write time.</li></ul>
<p>Cons:</p>
<ul><li>If a user has many friends, fetching the friend list and generating news feeds for all of them are slow and time consuming. It is called hotkey problem.</li><li>For inactive users or those rarely log in, pre-computing news feeds waste computing resources.</li></ul>
<p><strong>Fanout on read</strong>. The news feed is generated during read time. This is an on-demand model. Recent posts are pulled when a user loads her home page.</p>
<p>Pros:</p>
<ul><li>For inactive users or those who rarely log in, fanout on read works better because it will not waste computing resources on them.</li><li>Data is not pushed to friends so there is no hotkey problem.</li></ul>
<p>Cons:</p>
<ul><li>Fetching the news feed is slow as the news feed is not pre-computed.</li></ul>
<p>We adopt a hybrid approach to get benefits of both approaches and avoid pitfalls in them. Since fetching the news feed fast is crucial, we use a push model for the majority of users. For celebrities or users who have many friends/followers, we let followers pull news content on-demand to avoid system overload. Consistent hashing is a useful technique to mitigate the hotkey problem as it helps to distribute requests/data more evenly.</p>
<p>Let us take a close look at the fanout service as shown in Figure 11-5.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-141.jpeg" rel="noopener" target="_blank"><img alt="Design a news feed system — original diagram 141" height="677" loading="lazy" src="../../assets/system-design/figure-141.jpeg" width="705"/></a></figure>
<p>The fanout service works as follows:</p>
<ol start="1"><li>Fetch friend IDs from the graph database. Graph databases are suited for managing friend relationship and friend recommendations. Interested readers wishing to learn more about this concept should refer to the reference material <a href="study:system-design/lessons/11-11-step-4-wrap-up/#reference-11-2">[2]</a>.</li><li>Get friends info from the user cache. The system then filters out friends based on user settings. For example, if you mute someone, her posts will not show up on your news feed even though you are still friends. Another reason why posts may not show is that a user could selectively share information with specific friends or hide it from other people.</li><li>Send friends list and new post ID to the message queue.</li><li>Fanout workers fetch data from the message queue and store news feed data in the news feed cache. You can think of the news feed cache as a <em>&lt;post_id, user_id&gt;</em> mapping table. Whenever a new post is made, it will be appended to the news feed table as shown in Figure 11-6. The memory consumption can become very large if we store the entire user and post objects in the cache. Thus, only IDs are stored. To keep the memory size small, we set a configurable limit. The chance of a user scrolling through thousands of posts in news feed is slim. Most users are only interested in the latest content, so the cache miss rate is low.</li><li>Store <em>&lt;post_id, user_id &gt;</em> in news feed cache. Figure 11-6 shows an example of what the news feed looks like in cache.</li></ol>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-142.jpeg" rel="noopener" target="_blank"><img alt="Design a news feed system — original diagram 142" height="440" loading="lazy" src="../../assets/system-design/figure-142.jpeg" width="396"/></a></figure>

## Newsfeed retrieval deep dive

<section class="chapter-video" aria-label="Video for Newsfeed retrieval deep dive"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Newsfeed retrieval deep dive</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Figure 11-7 illustrates the detailed design for news feed retrieval.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-143.jpeg" rel="noopener" target="_blank"><img alt="Design a news feed system — original diagram 143" height="847" loading="lazy" src="../../assets/system-design/figure-143.jpeg" width="800"/></a></figure>
<p>As shown in Figure 11-7, media content (images, videos, etc.) are stored in CDN for fast retrieval. Let us look at how a client retrieves news feed.</p>
<ol start="1"><li>A user sends a request to retrieve her news feed. The request looks like this: <em>/v1/me/feed</em></li><li>The load balancer redistributes requests to web servers.</li><li>Web servers call the news feed service to fetch news feeds.</li><li>News feed service gets a list post IDs from the news feed cache.</li><li>A user’s news feed is more than just a list of feed IDs. It contains username, profile picture, post content, post image, etc. Thus, the news feed service fetches the complete user and post objects from caches (user cache and post cache) to construct the fully hydrated news feed.</li><li>The fully hydrated news feed is returned in JSON format back to the client for rendering.</li></ol>

## Cache architecture

<section class="chapter-video" aria-label="Video for Cache architecture"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Cache architecture</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Cache is extremely important for a news feed system. We divide the cache tier into 5 layers as shown in Figure 11-8.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-144.jpeg" rel="noopener" target="_blank"><img alt="Design a news feed system — original diagram 144" height="546" loading="lazy" src="../../assets/system-design/figure-144.jpeg" width="940"/></a></figure>
<ul><li>News Feed: It stores IDs of news feeds.</li><li>Content: It stores every post data. Popular content is stored in hot cache.</li><li>Social Graph: It stores user relationship data.</li><li>Action: It stores info about whether a user liked a post, replied a post, or took other actions on a post.</li><li>Counters: It stores counters for like, reply, follower, following, etc.</li></ul>

## Step 4 - Wrap up

<section class="chapter-video" aria-label="Video for Step 4 - Wrap up"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 4 - Wrap up</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this chapter, we designed a news feed system. Our design contains two flows: feed publishing and news feed retrieval.</p>
<p>Like any system design interview questions, there is no perfect way to design a system. Every company has its unique constraints, and you must design a system to fit those constraints. Understanding the tradeoffs of your design and technology choices are important. If there are a few minutes left, you can talk about scalability issues. To avoid duplicated discussion, only high-level talking points are listed below.</p>
<p>Scaling the database:</p>
<ul><li>Vertical scaling vs Horizontal scaling</li><li>SQL vs NoSQL</li><li>Master-slave replication</li><li>Read replicas</li><li>Consistency models</li><li>Database sharding</li></ul>
<p>Other talking points:</p>
<ul><li>Keep web tier stateless</li><li>Cache data as much as you can</li><li>Support multiple data centers</li><li>Lose couple components with message queues</li><li>Monitor key metrics. For instance, QPS during peak hours and latency while users refreshing their news feed are interesting to monitor.</li></ul>
<p>Congratulations on getting this far! Now give yourself a pat on the back. Good job!</p>

<section class="lesson-references"><h3 id="references-11">References</h3><ol><li id="reference-11-1" value="1">How News Feed Works: <a href="https://www.facebook.com/help/327131014036297/">https://www.facebook.com/help/327131014036297/</a></li><li id="reference-11-2" value="2">Friend of Friend recommendations Neo4j and SQL Sever: <a href="http://geekswithblogs.net/brendonpage/archive/2015/10/26/friend-of-friendrecommendations-with-neo4j.aspx">http://geekswithblogs.net/brendonpage/archive/2015/10/26/friend-of-friendrecommendations-with-neo4j.aspx</a></li></ol></section>
