# Design a rate limiter

## Design a rate limiter

<section class="chapter-video" aria-label="Video for Design a rate limiter"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Design a rate limiter</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In a network system, a rate limiter is used to control the rate of traffic sent by a client or a service. In the HTTP world, a rate limiter limits the number of client requests allowed to be sent over a specified period. If the API request count exceeds the threshold defined by the rate limiter, all the excess calls are blocked. Here are a few examples:</p>
<ul><li>A user can write no more than 2 posts per second.</li><li>You can create a maximum of 10 accounts per day from the same IP address.</li><li>You can claim rewards no more than 5 times per week from the same device.</li></ul>
<p>In this chapter, you are asked to design a rate limiter. Before starting the design, we first look at the benefits of using an API rate limiter:</p>
<ul><li>Prevent resource starvation caused by Denial of Service (DoS) attack <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-1">[1]</a>. Almost all APIs published by large tech companies enforce some form of rate limiting. For example, Twitter limits the number of tweets to 300 per 3 hours <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-2">[2]</a>. Google docs APIs have the following default limit: 300 per user per 60 seconds for read requests <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-3">[3]</a>. A rate limiter prevents DoS attacks, either intentional or unintentional, by blocking the excess calls.</li><li>Reduce cost. Limiting excess requests means fewer servers and allocating more resources to high priority APIs. Rate limiting is extremely important for companies that use paid third party APIs. For example, you are charged on a per-call basis for the following external APIs: check credit, make a payment, retrieve health records, etc. Limiting the number of calls is essential to reduce costs.</li><li>Prevent servers from being overloaded. To reduce server load, a rate limiter is used to filter out excess requests caused by bots or users’ misbehavior.</li></ul>

## Step 1 - Understand the problem and establish design scope

<section class="chapter-video" aria-label="Video for Step 1 - Understand the problem and establish design scope"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 1 - Understand the problem and establish design scope</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Rate limiting can be implemented using different algorithms, each with its pros and cons. The interactions between an interviewer and a candidate help to clarify the type of rate limiters we are trying to build.</p>
<p><strong>Candidate</strong>: What kind of rate limiter are we going to design? Is it a client-side rate limiter or server-side API rate limiter? <strong>Interviewer</strong>: Great question. We focus on the server-side API rate limiter.</p>
<p><strong>Candidate</strong>: Does the rate limiter throttle API requests based on IP, the user ID, or other properties? <strong>Interviewer</strong>: The rate limiter should be flexible enough to support different sets of throttle rules.</p>
<p><strong>Candidate</strong>: What is the scale of the system? Is it built for a startup or a big company with a large user base? <strong>Interviewer</strong>: The system must be able to handle a large number of requests.</p>
<p><strong>Candidate</strong>: Will the system work in a distributed environment? <strong>Interviewer</strong>: Yes.</p>
<p><strong>Candidate</strong>: Is the rate limiter a separate service or should it be implemented in application code? <strong>Interviewer</strong>: It is a design decision up to you.</p>
<p><strong>Candidate</strong>: Do we need to inform users who are throttled? <strong>Interviewer</strong>: Yes.</p>
<p><strong>Requirements</strong> Here is a summary of the requirements for the system:</p>
<ul><li>Accurately limit excessive requests.</li><li>Low latency. The rate limiter should not slow down HTTP response time.</li><li>Use as little memory as possible.</li><li>Distributed rate limiting. The rate limiter can be shared across multiple servers or processes.</li><li>Exception handling. Show clear exceptions to users when their requests are throttled.</li><li>High fault tolerance. If there are any problems with the rate limiter (for example, a cache server goes offline), it does not affect the entire system.</li></ul>

## Step 2 - Propose high-level design and get buy-in

<section class="chapter-video" aria-label="Video for Step 2 - Propose high-level design and get buy-in"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 2 - Propose high-level design and get buy-in</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Let us keep things simple and use a basic client and server model for communication.</p>

## Where to put the rate limiter?

<section class="chapter-video" aria-label="Video for Where to put the rate limiter?"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Where to put the rate limiter?</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Intuitively, you can implement a rate limiter at either the client or server-side. </p>
<ul><li>Client-side implementation. Generally speaking, client is an unreliable place to enforce rate limiting because client requests can easily be forged by malicious actors. Moreover, we might not have control over the client implementation.</li><li>Server-side implementation. Figure 4-1 shows a rate limiter that is placed on the server-side.</li></ul>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-034.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 34" height="218" loading="lazy" src="../../assets/system-design/figure-034.jpeg" width="877"/></a></figure>
<p>Besides the client and server-side implementations, there is an alternative way. Instead of putting a rate limiter at the API servers, we create a rate limiter middleware, which throttles requests to your APIs as shown in Figure 4-2.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-035.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 35" height="356" loading="lazy" src="../../assets/system-design/figure-035.jpeg" width="859"/></a></figure>
<p>Let us use an example in Figure 4-3 to illustrate how rate limiting works in this design. Assume our API allows 2 requests per second, and a client sends 3 requests to the server within a second. The first two requests are routed to API servers. However, the rate limiter middleware throttles the third request and returns a HTTP status code 429. The HTTP 429 response status code indicates a user has sent too many requests.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-036.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 36" height="338" loading="lazy" src="../../assets/system-design/figure-036.jpeg" width="852"/></a></figure>
<p>Cloud microservices <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-4">[4]</a> have become widely popular and rate limiting is usually implemented within a component called API gateway. API gateway is a fully managed service that supports rate limiting, SSL termination, authentication, IP whitelisting, servicing static content, etc. For now, we only need to know that the API gateway is a middleware that supports rate limiting.</p>
<p>While designing a rate limiter, an important question to ask ourselves is: where should the rater limiter be implemented, on the server-side or in a gateway? There is no absolute answer. It depends on your company’s current technology stack, engineering resources, priorities, goals, etc. Here are a few general guidelines:</p>
<ul><li>Evaluate your current technology stack, such as programming language, cache service, etc. Make sure your current programming language is efficient to implement rate limiting on the server-side.</li><li>Identify the rate limiting algorithm that fits your business needs. When you implement everything on the server-side, you have full control of the algorithm. However, your choice might be limited if you use a third-party gateway.</li><li>If you have already used microservice architecture and included an API gateway in the design to perform authentication, IP whitelisting, etc., you may add a rate limiter to the API gateway.</li><li>Building your own rate limiting service takes time. If you do not have enough engineering resources to implement a rate limiter, a commercial API gateway is a better option.</li></ul>

## Algorithms for rate limiting

<section class="chapter-video" aria-label="Video for Algorithms for rate limiting"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Algorithms for rate limiting</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Rate limiting can be implemented using different algorithms, and each of them has distinct pros and cons. Even though this chapter does not focus on algorithms, understanding them at high-level helps to choose the right algorithm or combination of algorithms to fit our use cases. Here is a list of popular algorithms:</p>
<ul><li>Token bucket</li><li>Leaking bucket</li><li>Fixed window counter</li><li>Sliding window log</li><li>Sliding window counter</li></ul>
<p><strong>Token bucket algorithm</strong> The token bucket algorithm is widely used for rate limiting. It is simple, well understood and commonly used by internet companies. Both Amazon <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-5">[5]</a> and Stripe <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-6">[6]</a> use this algorithm to throttle their API requests.</p>

<p>The token bucket algorithm work as follows:</p>
<ul><li>A token bucket is a container that has pre-defined capacity. Tokens are put in the bucket at preset rates periodically. Once the bucket is full, no more tokens are added. As shown in Figure 4-4, the token bucket capacity is 4. The refiller puts 2 tokens into the bucket every second. Once the bucket is full, extra tokens will overflow.</li></ul>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-037.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 37" height="858" loading="lazy" src="../../assets/system-design/figure-037.jpeg" width="753"/></a></figure>
<ul><li>Each request consumes one token. When a request arrives, we check if there are enough tokens in the bucket. Figure 4-5 explains how it works.</li></ul>
<ul><li>If there are enough tokens, we take one token out for each request, and the request goes through.</li><li>If there are not enough tokens, the request is dropped.</li></ul>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-038.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 38" height="739" loading="lazy" src="../../assets/system-design/figure-038.jpeg" width="805"/></a></figure>
<p>Figure 4-6 illustrates how token consumption, refill, and rate limiting logic work. In this example, the token bucket size is 4, and the refill rate is 4 per 1 minute.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-039.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 39" height="832" loading="lazy" src="../../assets/system-design/figure-039.jpeg" width="741"/></a></figure>
<p>The token bucket algorithm takes two parameters:</p>
<ul><li>Bucket size: the maximum number of tokens allowed in the bucket</li><li>Refill rate: number of tokens put into the bucket every second How many buckets do we need? This varies, and it depends on the rate-limiting rules. Here are a few examples.</li></ul>
<ul><li>It is usually necessary to have different buckets for different API endpoints. For instance, if a user is allowed to make 1 post per second, add 150 friends per day, and like 5 posts per second, 3 buckets are required for each user.</li><li>If we need to throttle requests based on IP addresses, each IP address requires a bucket.</li><li>If the system allows a maximum of 10,000 requests per second, it makes sense to have a global bucket shared by all requests. Pros:</li></ul>
<ul><li>The algorithm is easy to implement.</li><li>Memory efficient.</li><li>Token bucket allows a burst of traffic for short periods. A request can go through as long as there are tokens left. Cons:</li></ul>
<ul><li>Two parameters in the algorithm are bucket size and token refill rate. However, it might</li></ul>
<p>be challenging to tune them properly.</p>
<p><strong>Leaking bucket algorithm</strong> The leaking bucket algorithm is similar to the token bucket except that requests are processed at a fixed rate. It is usually implemented with a first-in-first-out (FIFO) queue. The algorithm works as follows:</p>
<ul><li>When a request arrives, the system checks if the queue is full. If it is not full, the request is added to the queue.</li><li>Otherwise, the request is dropped.</li><li>Requests are pulled from the queue and processed at regular intervals.</li></ul>
<p>Figure 4-7 explains how the algorithm works.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-040.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 40" height="331" loading="lazy" src="../../assets/system-design/figure-040.jpeg" width="940"/></a></figure>
<p>Leaking bucket algorithm takes the following two parameters:</p>
<ul><li>Bucket size: it is equal to the queue size. The queue holds the requests to be processed at a fixed rate.</li><li>Outflow rate: it defines how many requests can be processed at a fixed rate, usually in seconds. Shopify, an ecommerce company, uses leaky buckets for rate-limiting <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-7">[7]</a>.</li></ul>
<p>Pros:</p>
<ul><li>Memory efficient given the limited queue size.</li><li>Requests are processed at a fixed rate therefore it is suitable for use cases that a stable outflow rate is needed.</li></ul>
<p>Cons:</p>
<ul><li>A burst of traffic fills up the queue with old requests, and if they are not processed in time, recent requests will be rate limited.</li><li>There are two parameters in the algorithm. It might not be easy to tune them properly.</li></ul>
<p><strong>Fixed window counter algorithm</strong> Fixed window counter algorithm works as follows:</p>
<ul><li>The algorithm divides the timeline into fix-sized time windows and assign a counter for each window.</li><li>Each request increments the counter by one.</li><li>Once the counter reaches the pre-defined threshold, new requests are dropped until a new time window starts.</li></ul>
<p>Let us use a concrete example to see how it works. In Figure 4-8, the time unit is 1 second and the system allows a maximum of 3 requests per second. In each second window, if more than 3 requests are received, extra requests are dropped as shown in Figure 4-8.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-041.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 41" height="552" loading="lazy" src="../../assets/system-design/figure-041.jpeg" width="940"/></a></figure>
<p>A major problem with this algorithm is that a burst of traffic at the edges of time windows could cause more requests than allowed quota to go through. Consider the following case:</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-042.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 42" height="452" loading="lazy" src="../../assets/system-design/figure-042.jpeg" width="940"/></a></figure>
<p>In Figure 4-9, the system allows a maximum of 5 requests per minute, and the available quota resets at the human-friendly round minute. As seen, there are five requests between 2:00:00 and 2:01:00 and five more requests between 2:01:00 and 2:02:00. For the one-minute window between 2:00:30 and 2:01:30, 10 requests go through. That is twice as many as allowed requests.</p>
<p>Pros:</p>
<ul><li>Memory efficient.</li></ul>
<ul><li>Easy to understand.</li><li>Resetting available quota at the end of a unit time window fits certain use cases.</li></ul>
<p>Cons:</p>
<ul><li>Spike in traffic at the edges of a window could cause more requests than the allowed quota to go through.</li></ul>
<p><strong>Sliding window log algorithm</strong> As discussed previously, the fixed window counter algorithm has a major issue: it allows more requests to go through at the edges of a window. The sliding window log algorithm fixes the issue. It works as follows:</p>
<ul><li>The algorithm keeps track of request timestamps. Timestamp data is usually kept in cache, such as sorted sets of Redis <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-8">[8]</a>.</li><li>When a new request comes in, remove all the outdated timestamps. Outdated timestamps are defined as those older than the start of the current time window.</li><li>Add timestamp of the new request to the log.</li><li>If the log size is the same or lower than the allowed count, a request is accepted. Otherwise, it is rejected.</li></ul>
<p>We explain the algorithm with an example as revealed in Figure 4-10.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-043.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 43" height="689" loading="lazy" src="../../assets/system-design/figure-043.jpeg" width="770"/></a></figure>
<p>In this example, the rate limiter allows 2 requests per minute. Usually, Linux timestamps are stored in the log. However, human-readable representation of time is used in our example for better readability.</p>
<ul><li>The log is empty when a new request arrives at 1:00:01. Thus, the request is allowed.</li></ul>
<ul><li>A new request arrives at 1:00:30, the timestamp 1:00:30 is inserted into the log. After the insertion, the log size is 2, not larger than the allowed count. Thus, the request is allowed.</li><li>A new request arrives at 1:00:50, and the timestamp is inserted into the log. After the insertion, the log size is 3, larger than the allowed size 2. Therefore, this request is rejected even though the timestamp remains in the log.</li><li>A new request arrives at 1:01:40. Requests in the range [1:00:40,1:01:40) are within the latest time frame, but requests sent before 1:00:40 are outdated. Two outdated timestamps, 1:00:01 and 1:00:30, are removed from the log. After the remove operation, the log size becomes 2; therefore, the request is accepted.</li></ul>
<p>Pros:</p>
<ul><li>Rate limiting implemented by this algorithm is very accurate. In any rolling window, requests will not exceed the rate limit.</li></ul>
<p>Cons:</p>
<ul><li>The algorithm consumes a lot of memory because even if a request is rejected, its timestamp might still be stored in memory.</li></ul>
<p><strong>Sliding window counter algorithm</strong> The sliding window counter algorithm is a hybrid approach that combines the fixed window counter and sliding window log. The algorithm can be implemented by two different approaches. We will explain one implementation in this section and provide reference for the other implementation at the end of the section. Figure 4-11 illustrates how this algorithm works.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-044.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 44" height="552" loading="lazy" src="../../assets/system-design/figure-044.jpeg" width="941"/></a></figure>
<p>Assume the rate limiter allows a maximum of 7 requests per minute, and there are 5 requests in the previous minute and 3 in the current minute. For a new request that arrives at a 30% position in the current minute, the number of requests in the rolling window is calculated using the following formula:</p>
<ul><li>Requests in current window <strong>+ </strong>requests in the previous window<strong> * </strong>overlap percentage of the rolling window and previous window</li></ul>
<ul><li>Using this formula, we get 3 + 5 * 0.7% = 6.5 request. Depending on the use case, the number can either be rounded up or down. In our example, it is rounded down to 6.</li></ul>
<p>Since the rate limiter allows a maximum of 7 requests per minute, the current request can go through. However, the limit will be reached after receiving one more request.</p>
<p>Due to the space limitation, we will not discuss the other implementation here. Interested readers should refer to the reference material <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-9">[9]</a>. This algorithm is not perfect. It has pros and cons.</p>
<p>Pros</p>
<ul><li>It smooths out spikes in traffic because the rate is based on the average rate of the previous window.</li><li>Memory efficient.</li></ul>
<p>Cons</p>
<ul><li>It only works for not-so-strict look back window. It is an approximation of the actual rate because it assumes requests in the previous window are evenly distributed. However, this problem may not be as bad as it seems. According to experiments done by Cloudflare <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-10">[10]</a>, only 0.003% of requests are wrongly allowed or rate limited among 400 million requests.</li></ul>

## High-level architecture

<section class="chapter-video" aria-label="Video for High-level architecture"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>High-level architecture</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>The basic idea of rate limiting algorithms is simple. At the high-level, we need a counter to keep track of how many requests are sent from the same user, IP address, etc. If the counter is larger than the limit, the request is disallowed.</p>
<p>Where shall we store counters? Using the database is not a good idea due to slowness of disk access. In-memory cache is chosen because it is fast and supports time-based expiration strategy. For instance, Redis <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-11">[11]</a> is a popular option to implement rate limiting. It is an inmemory store that offers two commands: INCR and EXPIRE.</p>
<ul><li>INCR: It increases the stored counter by 1.</li><li>EXPIRE: It sets a timeout for the counter. If the timeout expires, the counter is automatically deleted.</li></ul>
<p>Figure 4-12 shows the high-level architecture for rate limiting, and this works as follows:</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-045.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 45" height="401" loading="lazy" src="../../assets/system-design/figure-045.jpeg" width="940"/></a></figure>
<ul><li>The client sends a request to rate limiting middleware.</li><li>Rate limiting middleware fetches the counter from the corresponding bucket in Redis and</li></ul>
<p>checks if the limit is reached or not.</p>
<ul><li>If the limit is reached, the request is rejected.</li><li>If the limit is not reached, the request is sent to API servers. Meanwhile, the system increments the counter and saves it back to Redis.</li></ul>

## Step 3 - Design deep dive

<section class="chapter-video" aria-label="Video for Step 3 - Design deep dive"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 3 - Design deep dive</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>The high-level design in Figure 4-12 does not answer the following questions:</p>
<ul><li>How are rate limiting rules created? Where are the rules stored?</li><li>How to handle requests that are rate limited?</li></ul>
<p>In this section, we will first answer the questions regarding rate limiting rules and then go over the strategies to handle rate-limited requests. Finally, we will discuss rate limiting in distributed environment, a detailed design, performance optimization and monitoring.</p>

## Rate limiting rules

<section class="chapter-video" aria-label="Video for Rate limiting rules"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Rate limiting rules</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Lyft open-sourced their rate-limiting component <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-12">[12]</a>. We will peek inside of the component and look at some examples of rate limiting rules:</p>
<p>domain: messaging descriptors:</p>
<p> - key: message_type    Value: marketing     rate_limit:</p>
<p>     unit: day      requests_per_unit: 5</p>
<p>In the above example, the system is configured to allow a maximum of 5 marketing messages per day. Here is another example:</p>
<p>domain: auth descriptors:</p>
<p> - key: auth_type    Value: login     rate_limit:</p>
<p>     unit: minute      requests_per_unit: 5</p>
<p>This rule shows that clients are not allowed to login more than 5 times in 1 minute. Rules are generally written in configuration files and saved on disk.</p>

## Exceeding the rate limit

<section class="chapter-video" aria-label="Video for Exceeding the rate limit"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Exceeding the rate limit</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In case a request is rate limited, APIs return a HTTP response code 429 (too many requests) to the client. Depending on the use cases, we may enqueue the rate-limited requests to be processed later. For example, if some orders are rate limited due to system overload, we may keep those orders to be processed later.</p>
<p><strong>Rate limiter headers</strong> How does a client know whether it is being throttled? And how does a client know the number of allowed remaining requests before being throttled? The answer lies in HTTP response headers. The rate limiter returns the following HTTP headers to clients:</p>
<p><em>X-Ratelimit-Remaining</em>: The remaining number of allowed requests within the window.</p>
<p><em>X-Ratelimit-Limit: </em>It indicates how many calls the client can make per time window.</p>
<p><em>X-Ratelimit-Retry-After:</em> The number of seconds to wait until you can make a request again without being throttled.</p>
<p>When a user has sent too many requests, a 429 too many requests error and <em>X-Ratelimit-</em></p>
<p><em>Retry-After </em>header are returned to the client.</p>

## Detailed design

<section class="chapter-video" aria-label="Video for Detailed design"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Detailed design</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Figure 4-13 presents a detailed design of the system.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-046.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 46" height="770" loading="lazy" src="../../assets/system-design/figure-046.jpeg" width="940"/></a></figure>
<ul><li>Rules are stored on the disk. Workers frequently pull rules from the disk and store them in the cache.</li><li>When a client sends a request to the server, the request is sent to the rate limiter middleware first.</li><li>Rate limiter middleware loads rules from the cache. It fetches counters and last request timestamp from Redis cache. Based on the response, the rate limiter decides:</li></ul>
<ul><li>if the request is not rate limited, it is forwarded to API servers.</li><li>if the request is rate limited, the rate limiter returns 429 too many requests error to the client. In the meantime, the request is either dropped or forwarded to the queue.</li></ul>

## Rate limiter in a distributed environment

<section class="chapter-video" aria-label="Video for Rate limiter in a distributed environment"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Rate limiter in a distributed environment</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Building a rate limiter that works in a single server environment is not difficult. However, scaling the system to support multiple servers and concurrent threads is a different story. There are two challenges:</p>
<ul><li>Race condition</li><li>Synchronization issue</li></ul>
<p><strong>Race condition</strong> As discussed earlier, rate limiter works as follows at the high-level:</p>
<ul><li>Read the <em>counter</em> value from Redis.</li><li>Check if ( <em>counter + 1</em> ) exceeds the threshold.</li><li>If not, increment the counter value by 1 in Redis.</li></ul>
<p>Race conditions can happen in a highly concurrent environment as shown in Figure 4-14.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-047.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 47" height="536" loading="lazy" src="../../assets/system-design/figure-047.jpeg" width="941"/></a></figure>
<p>Assume the <em>counter</em> value in Redis is 3. If two requests concurrently read the <em>counter</em> value before either of them writes the value back, each will increment the <em>counter</em> by one and write it back without checking the other thread. Both requests (threads) believe they have the correct <em>counter</em> value 4. However, the correct <em>counter</em> value should be 5.</p>
<p>Locks are the most obvious solution for solving race condition. However, locks will significantly slow down the system. Two strategies are commonly used to solve the problem: Lua script <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-13">[13]</a> and sorted sets data structure in Redis <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-8">[8]</a>. For readers interested in these strategies, refer to the corresponding reference materials <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-8">[8]</a> <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-13">[13]</a>.</p>
<p><strong>Synchronization issue</strong> Synchronization is another important factor to consider in a distributed environment. To support millions of users, one rate limiter server might not be enough to handle the traffic. When multiple rate limiter servers are used, synchronization is required. For example, on the left side of Figure 4-15, client 1 sends requests to rate limiter 1, and client 2 sends requests to rate limiter 2. As the web tier is stateless, clients can send requests to a different rate limiter as shown on the right side of Figure 4-15. If no synchronization happens, rate limiter 1 does not contain any data about client 2. Thus, the rate limiter cannot work properly. </p>

<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-048.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 48" height="333" loading="lazy" src="../../assets/system-design/figure-048.jpeg" width="940"/></a></figure>
<p>One possible solution is to use sticky sessions that allow a client to send traffic to the same rate limiter. This solution is not advisable because it is neither scalable nor flexible. A better approach is to use centralized data stores like Redis. The design is shown in Figure 4-16.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-049.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 49" height="383" loading="lazy" src="../../assets/system-design/figure-049.jpeg" width="848"/></a></figure>

## Performance optimization

<section class="chapter-video" aria-label="Video for Performance optimization"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Performance optimization</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Performance optimization is a common topic in system design interviews. We will cover two areas to improve.</p>
<p>First, multi-data center setup is crucial for a rate limiter because latency is high for users located far away from the data center. Most cloud service providers build many edge server locations around the world. For example, as of 5/20 2020, Cloudflare has 194 geographically distributed edge servers <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-14">[14]</a>. Traffic is automatically routed to the closest edge server to reduce latency.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-050.jpeg" rel="noopener" target="_blank"><img alt="Design a rate limiter — original diagram 50" height="525" loading="lazy" src="../../assets/system-design/figure-050.jpeg" width="787"/></a></figure>
<p>Second, synchronize data with an eventual consistency model. If you are unclear about the eventual consistency model, refer to the “Consistency” section in “Chapter 6: Design a Keyvalue Store.”</p>

## Monitoring

<section class="chapter-video" aria-label="Video for Monitoring"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Monitoring</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>After the rate limiter is put in place, it is important to gather analytics data to check whether the rate limiter is effective. Primarily, we want to make sure:</p>
<ul><li>The rate limiting algorithm is effective.</li><li>The rate limiting rules are effective.</li></ul>
<p>For example, if rate limiting rules are too strict, many valid requests are dropped. In this case, we want to relax the rules a little bit. In another example, we notice our rate limiter becomes ineffective when there is a sudden increase in traffic like flash sales. In this scenario, we may replace the algorithm to support burst traffic. Token bucket is a good fit here. </p>

## Step 4 - Wrap up

<section class="chapter-video" aria-label="Video for Step 4 - Wrap up"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 4 - Wrap up</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this chapter, we discussed different algorithms of rate limiting and their pros/cons. Algorithms discussed include:</p>
<ul><li>Token bucket</li><li>Leaking bucket</li><li>Fixed window</li><li>Sliding window log</li><li>Sliding window counter</li></ul>
<p>Then, we discussed the system architecture, rate limiter in a distributed environment, performance optimization and monitoring. Similar to any system design interview questions, there are additional talking points you can mention if time allows:</p>
<ul><li>Hard vs soft rate limiting.</li><li>Hard: The number of requests cannot exceed the threshold.</li><li>Soft:  Requests can exceed the threshold for a short period.</li><li>Rate limiting at different levels. In this chapter, we only talked about rate limiting at the application level (HTTP: layer 7). It is possible to apply rate limiting at other layers. For example, you can apply rate limiting by IP addresses using Iptables <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-15">[15]</a> (IP: layer 3). Note: The Open Systems Interconnection model (OSI model) has 7 layers <a href="study:system-design/lessons/04-14-step-4-wrap-up/#reference-4-16">[16]</a>:  Layer 1: Physical layer, Layer 2: Data link layer, Layer 3: Network layer, Layer 4: Transport layer, Layer 5: Session layer, Layer 6: Presentation layer, Layer 7: Application layer.</li><li>Avoid being rate limited. Design your client with best practices:</li><li>Use client cache to avoid making frequent API calls.</li><li>Understand the limit and do not send too many requests in a short time frame.</li><li>Include code to catch exceptions or errors so your client can gracefully recover from exceptions.</li><li>Add sufficient back off time to retry logic. Congratulations on getting this far! Now give yourself a pat on the back. Good job!</li></ul>

<section class="lesson-references"><h3 id="references-4">References</h3><ol><li id="reference-4-1" value="1">Rate-limiting strategies and techniques: <a href="https://cloud.google.com/solutions/rate-limitingstrategies-techniques">https://cloud.google.com/solutions/rate-limitingstrategies-techniques</a></li><li id="reference-4-2" value="2">Twitter rate limits: <a href="https://developer.twitter.com/en/docs/basics/rate-limits">https://developer.twitter.com/en/docs/basics/rate-limits</a></li><li id="reference-4-3" value="3">Google docs usage limits: <a href="https://developers.google.com/docs/api/limits">https://developers.google.com/docs/api/limits</a></li><li id="reference-4-4" value="4">IBM microservices: <a href="https://www.ibm.com/cloud/learn/microservices">https://www.ibm.com/cloud/learn/microservices</a></li><li id="reference-4-5" value="5">Throttle API requests for better throughput: <a href="https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-requestthrottling.html">https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-requestthrottling.html</a></li><li id="reference-4-6" value="6">Stripe rate limiters: <a href="https://stripe.com/blog/rate-limiters">https://stripe.com/blog/rate-limiters</a></li><li id="reference-4-7" value="7">Shopify REST Admin API rate limits: <a href="https://help.shopify.com/en/api/reference/restadmin-api-rate-limits">https://help.shopify.com/en/api/reference/restadmin-api-rate-limits</a></li><li id="reference-4-8" value="8">Better Rate Limiting With Redis Sorted Sets: <a href="https://engineering.classdojo.com/blog/2015/02/06/rolling-rate-limiter/">https://engineering.classdojo.com/blog/2015/02/06/rolling-rate-limiter/</a></li><li id="reference-4-9" value="9">System Design — Rate limiter and Data modelling: <a href="https://medium.com/@saisandeepmopuri/system-design-rate-limiter-and-data-modelling-">https://medium.com/@saisandeepmopuri/system-design-rate-limiter-and-data-modelling-</a> 9304b0d18250</li><li id="reference-4-10" value="10">How we built rate limiting capable of scaling to millions of domains: <a href="https://blog.cloudflare.com/counting-things-a-lot-of-different-things/">https://blog.cloudflare.com/counting-things-a-lot-of-different-things/</a></li><li id="reference-4-11" value="11">Redis website: <a href="https://redis.io/">https://redis.io/</a></li><li id="reference-4-12" value="12">Lyft rate limiting: <a href="https://github.com/lyft/ratelimit">https://github.com/lyft/ratelimit</a></li><li id="reference-4-13" value="13">Scaling your API with rate limiters: <a href="https://gist.github.com/ptarjan/e38f45f2dfe601419ca3af937fff574d#request-rate-limiter">https://gist.github.com/ptarjan/e38f45f2dfe601419ca3af937fff574d#request-rate-limiter</a></li><li id="reference-4-14" value="14">What is edge computing: <a href="https://www.cloudflare.com/learning/serverless/glossary/whatis-edge-computing/">https://www.cloudflare.com/learning/serverless/glossary/whatis-edge-computing/</a></li><li id="reference-4-15" value="15">Rate Limit Requests with Iptables: <a href="https://blog.programster.org/rate-limit-requests-withiptables">https://blog.programster.org/rate-limit-requests-withiptables</a></li><li id="reference-4-16" value="16">OSI model: <a href="https://en.wikipedia.org/wiki/OSI_model#Layer_architecture">https://en.wikipedia.org/wiki/OSI_model#Layer_architecture</a></li></ol></section>
