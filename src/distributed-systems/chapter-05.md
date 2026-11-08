# Resiliency

## Overview: Resiliency

<section class="chapter-video" aria-label="Video for Overview: Resiliency"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>Overview: Resiliency</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-247"></div>

<div class="source-page" id="source-page-249"></div>

<p><em>“Anything that can go wrong will go wrong.”</em></p>

<p>– Murphy’s law</p>

<p>In the last part, we discussed the three fundamental scalability patterns: functional decomposition, data partitioning, and replication. They all have one thing in common: they increase the number of moving parts (machines, services, processes, etc.) in our applications. But since every part has a probability of failing, the more moving parts there are, the higher the chance that any of them will fail. Eventually, anything that can go wrong will go wrong <sup>8</sup>; power outages, hardware faults, software crashes, memory leaks — you name it.</p>

<p>Remember when we talked about availability and “nines” in chapter 1? Well, to guarantee just two nines, an application can only be unavailable for up to 15 minutes a day. That’s very little time to take any manual action when something goes wrong. And if we strive for three nines, we only have 43 minutes per<em> </em><em>month</em> available. Clearly, the more nines we want, the faster our systems need to detect, react to, and repair faults as they occur. In this part, we will discuss a variety of resiliency best practices and patterns to achieve that.</p>

<p>To build fault-tolerant applications, we first need to have an idea of what can go wrong. In chapter 24, we will explore some of the most common root causes of failures.</p>

<p class="source-footnote">8Also known as Murphy’s law</p>

<div class="source-page" id="source-page-250"></div>

<p>Chapter 25 describes how to use redundancy, the replication of functionality or state, to increase the availability of a system. As we will learn, redundancy is only helpful when the redundant nodes can’t fail for the same reason at the same time, i.e., when failures are not correlated.</p>

<p>Chapter 26 discusses how to isolate correlated failures by partitioning resources and then describes two very powerful forms of partitioning: shuffle sharding and cellular architectures.</p>

<p>Chapter 27 dives into more tactical resiliency patterns for tolerating failures of downstream dependencies that you can apply to existing systems with few changes, like timeouts and retries.</p>

<p>Chapter 28 discusses resiliency patterns, like load shedding and rate-limiting, for protecting systems against overload from upstream dependencies.</p>

## Common failure causes

<section class="chapter-video" aria-label="Video for Common failure causes"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>Common failure causes</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-251"></div>

<p>We say that a system has a<em> </em><em>failure</em><sup>1</sup><sup> </sup>when it no longer provides a service to its users that meets its specification. A failure is caused by a<em> fault</em>: a failure of an internal component or an external dependency the system depends on. Some faults can be tolerated and have no user-visible impact at all, while others lead to failures.</p>

<p>To build fault-tolerant applications, we first need to have an idea of what can go wrong. In the next few sections, we will explore some of the most common root causes of failures. By the end of it, you will likely wonder how to tolerate all these different types of faults. The answers will follow in the next few chapters.</p>

<h3 id="section-24-1-hardware-faults"><strong>24.1</strong> <strong>Hardware faults</strong></h3>

<p>Any physical part of a machine can fail. HDDs, memory modules, power supplies, motherboards, SSDs, NICs, or CPUs, can all stop working for various reasons. In some cases, hardware faults can cause data corruption as well. If that wasn’t enough, entire data centers can go down because of power cuts or natural disasters.</p>

<p class="source-footnote">1“A Conceptual Framework for System Fault Tolerance,”<a href="https://resources.sei.cmu.edu/asset_files/TechnicalReport/1992_005_001_16112.pdf"> https://resources.sei.</a> <a href="https://resources.sei.cmu.edu/asset_files/TechnicalReport/1992_005_001_16112.pdf">cmu.edu/asset_files/TechnicalReport/1992_005_001_16112.pdf</a></p>

<div class="source-page" id="source-page-252"></div>

<p>As we will discuss later, we can address many of these infrastructure faults with redundancy. You would think that these faults are the main cause for distributed applications failing, but in reality, they often fail for very mundane reasons.</p>

<h3 id="section-24-2-incorrect-error-handling"><strong>24.2</strong> <strong>Incorrect error handling</strong></h3>

<p>A study from 2014<sup>2</sup><sup> </sup>of user-reported failures from five popular distributed data stores found that the majority of catastrophic failures were the result of incorrect handling of non-fatal errors.</p>

<p>In most cases, the bugs in the error handling could have been detected with simple tests. For example, some handlers completely ignored errors. Others caught an overly generic exception, like<em> Ex</em><em>ception</em> in Java, and aborted the entire process for no good reason. And some other handlers were only partially implemented and even contained “FIXME” and “TODO” comments.</p>

<p>In hindsight, this is perhaps not too surprising, given that error handling tends to be an afterthought.<sup>3</sup><sup> </sup>Later, in chapter 29, we will take a closer look at best practices for testing large distributed applications.</p>

<h3 id="section-24-3-configuration-changes"><strong>24.3</strong> <strong>Configuration changes</strong></h3>

<p>Configuration changes are one of the leading root causes for catastrophic failures<sup>4</sup>. It’s not just misconfigurations that cause problems, but also valid configuration changes to enable rarely-used features that no longer work as expected (or never did).</p>

<p>What makes configuration changes particularly dangerous is that their effects can be delayed<sup>5</sup>. If an application reads a configura-</p>

<p class="source-footnote">2“Simple Testing Can Prevent Most Critical Failures: An Analysis of Production Failures in Distributed Data-Intensive Systems,”<a href="https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-yuan.pdf"> https://www.usenix.org/syste</a> <a href="https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-yuan.pdf">m/files/conference/osdi14/osdi14-paper-yuan.pdf</a></p>

<p class="source-footnote"><a href="https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-yuan.pdf">3</a>This is the reason the Go language puts so much emphasis on error handling. 4“A List of Post-mortems: Config Errors,”<a href="https://github.com/danluu/post-mortems#config-errors"> https://github.com/danluu/post-</a> <a href="https://github.com/danluu/post-mortems#config-errors">mortems#config-errors</a></p>

<p class="source-footnote"><a href="https://github.com/danluu/post-mortems#config-errors">5</a>“Early Detection of Configuration Errors to Reduce Failure Damage,” <a href="https://www.usenix.org/system/files/conference/osdi16/osdi16-xu.pdf">https:</a> <a href="https://www.usenix.org/system/files/conference/osdi16/osdi16-xu.pdf">//www.usenix.org/system/files/conference/osdi16/osdi16-xu.pdf</a></p>

<div class="source-page" id="source-page-253"></div>

<p>tion value only when it’s actually needed, an invalid value might take effect only hours or days after it has changed and thus escape early detection.</p>

<p>This is why configuration changes should be version-controlled, tested, and released just like code changes, and their validation should happen preventively when the change happens. In chapter 30, we will discuss safe release practices for code and configuration changes in the context of continuous deployments.</p>

<h3 id="section-24-4-single-points-of-failure"><strong>24.4</strong> <strong>Single points of failure</strong></h3>

<p>A single point of failure (SPOF) is a component whose failure brings the entire system down with it. In practice, systems can have multiple SPOFs.</p>

<p>Humans make for great SPOFs, and if you put them in a position where they can cause a catastrophic failure on their own, you can bet they eventually will. For example, human failures often happen when someone needs to manually execute a series of operational steps in a specific order without making any mistakes. On the other hand, computers are great at executing instructions, which is why automation should be leveraged whenever possible.</p>

<p>Another common SPOF is DNS<sup>6</sup>. If clients can’t resolve the domain name for an application, they won’t be able to connect to it. There are many reasons why that can happen, ranging from domain names expiring<sup>7</sup><sup> </sup>to entire root level domains going down<sup>8</sup>.</p>

<p>Similarly, the TLS certificate used by an application for its HTTP endpoints is also a SPOF<sup>9</sup>. If the certificate expires, clients won’t be able to open a secure connection with the application.</p>

<p class="source-footnote">6“It’s always DNS,”<a href="https://twitter.com/ahidalgosre/status/1315345619926609920?lang=en-GB"> https://twitter.com/ahidalgosre/status/1315345619926</a> <a href="https://twitter.com/ahidalgosre/status/1315345619926609920?lang=en-GB">609920?lang=en-GB</a> <a href="https://twitter.com/ahidalgosre/status/1315345619926609920?lang=en-GB">7</a>“Foursquare Goes Dark Too. Unintentionally.,”<a href="https://techcrunch.com/2010/03/27/foursquare-offline"> https://techcrunch.com/201</a> <a href="https://techcrunch.com/2010/03/27/foursquare-offline">0/03/27/foursquare-offline</a> <a href="https://techcrunch.com/2010/03/27/foursquare-offline">8</a>“Stop using .IO Domain Names for Production Traffic,”<a href="https://hackernoon.com/stop-using-io-domain-names-for-production-traffic-b6aa17eeac20"> https://hackernoon.c</a> <a href="https://hackernoon.com/stop-using-io-domain-names-for-production-traffic-b6aa17eeac20">om/stop-using-io-domain-names-for-production-traffic-b6aa17eeac20</a></p>

<p class="source-footnote"><a href="https://hackernoon.com/stop-using-io-domain-names-for-production-traffic-b6aa17eeac20">9</a>“Microsoft Teams goes down after Microsoft forgot to renew a certificate,” <a href="https://www.theverge.com/2020/2/3/21120248/microsoft-teams-down-outage-certificate-issue-status">ht</a> <a href="https://www.theverge.com/2020/2/3/21120248/microsoft-teams-down-outage-certificate-issue-status">tps://www.theverge.com/2020/2/3/21120248/microsoft-teams-down-outage-</a> <a href="https://www.theverge.com/2020/2/3/21120248/microsoft-teams-down-outage-certificate-issue-status">certificate-issue-status</a></p>

<div class="source-page" id="source-page-254"></div>

<p>Ideally, SPOFs should be identified when the system is designed. The best way to detect them is to examine every system component and ask what would happen if it were to fail. Some SPOFs can be architected away, e.g., by introducing redundancy, while others can’t. In that case, the only option left is to reduce the SPOF’s blast radius, i.e., the damage the SPOF inflicts on the system when it fails. Many of the resiliency patterns we will discuss later reduce the blast radius of failures.</p>

<h3 id="section-24-5-network-faults"><strong>24.5</strong> <strong>Network faults</strong></h3>

<p>When a client sends a request to a server, it expects to receive a response from it a while later. In the best case, it receives the response shortly after sending the request. If that doesn’t happen, the client has two options: continue to wait or fail the request with a time-out exception or error.</p>

<p>As discussed in chapter 7, when the concepts of failure detection and timeouts were introduced, there are many reasons for not getting a prompt response. For example, the server could be very slow or have crashed while processing the request; or maybe the network could be losing a small percentage of packets, causing lots of retransmissions and delays.</p>

<p>Slow network calls are the silent killers<sup>10</sup><sup> </sup>of distributed systems. Because the client doesn’t know whether the response will eventually arrive, it can spend a long time waiting before giving up, if it gives up at all, causing performance degradations that are challenging to debug. This kind of fault is also referred to as a<em> </em><em>gray</em> <em>failure</em><sup>11</sup>: a failure that is so subtle that it can’t be detected quickly or accurately. Because of their nature, gray failures can easily bring an entire system down to its knees.</p>

<p>In the next section, we will explore another common cause of gray failures.</p>

<p class="source-footnote">10“Fallacies of distributed computing,”<a href="https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing"> https://en.wikipedia.org/wiki/Fallacie</a> <a href="https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing">s_of_distributed_computing</a></p>

<p class="source-footnote"><a href="https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing">11</a>“Gray Failure: The Achilles’ Heel of Cloud-Scale Systems,”<a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/paper-1.pdf"> https://www.mi</a> <a href="https://www.microsoft.com/en-us/research/wp-content/uploads/2017/06/paper-1.pdf">crosoft.com/en-us/research/wp-content/uploads/2017/06/paper-1.pdf</a></p>

<div class="source-page" id="source-page-255"></div>

<h3 id="section-24-6-resource-leaks"><strong>24.6</strong> <strong>Resource leaks</strong></h3>

<p>From an observer’s point of view, a very slow process is not very different from one that isn’t running at all — neither can perform useful work. Resource leaks are one of the most common causes of slow processes.</p>

<p>Memory is arguably the most well-known resource affected by leaks. A memory leak causes a steady increase in memory consumption over time. Even languages with garbage collection are vulnerable to leaks: if a reference to an object that is no longer needed is kept somewhere, the garbage collector won’t be able to delete it. When a leak has consumed so much memory that there is very little left, the operating system will start to swap memory pages to disk aggressively. Also, the garbage collector will kick in more frequently, trying to release memory. All of this consumes CPU cycles and makes the process slower. Eventually, when there is no more physical memory left, and there is no more space in the swap file, the process won’t be able to allocate memory, and most operations will fail.</p>

<p>Memory is just one of the many resources that can leak. Take thread pools, for example: if a thread acquired from a pool makes a synchronous blocking HTTP call without a timeout and the call never returns, the thread won’t be returned to the pool. And since the pool has a limited maximum size, it will eventually run out of threads if it keeps losing them.</p>

<p>You might think that making<em> </em><em>asynchronous</em> calls rather than synchronous ones would help in the previous case. However, modern HTTP clients use socket pools to avoid recreating TCP connections and paying a performance fee, as discussed in chapter 2. If a request is made without a timeout, the connection is never returned to the pool. As the pool has a limited maximum size, eventually, there won’t be any connections left.</p>

<p>On top of that, your code isn’t the only thing accessing memory, threads, and sockets. The libraries your application depends on use the same resources, and they can hit the same issues we just</p>

<div class="source-page" id="source-page-256"></div>

<p>discussed.</p>

<h3 id="section-24-7-load-pressure"><strong>24.7</strong> <strong>Load pressure</strong></h3>

<p>Every system has a limit of how much load it can withstand, i.e., its capacity. So when the load directed to the system continues to increase, it’s bound to hit that limit sooner or later. But an organic increase in load, that gives the system the time to scale out accordingly and increase its capacity, is one thing, and a sudden and unexpected flood is another.</p>

<p>For example, consider the number of requests received by an application in a period of time. The rate and the type of incoming requests can change over time, and sometimes suddenly, for a variety of reasons:</p>

<ul><li>The requests might have a seasonality. So, for example, depending on the hour of the day, the application is hit by users in different countries.</li><li>Some requests are much more expensive than others and abuse the system in unexpected ways, like scrapers slurping in data at super-human speed.</li><li>Some requests are malicious, like those of DDoS attacks that try to saturate the application’s bandwidth to deny legitimate users access to it.</li></ul>

<p>While some load surges can be handled by automation that adds capacity (e.g., autoscaling), others require the system to reject requests to shield it from overloading, using the patterns we will discuss in chapter 28.</p>

<h3 id="section-24-8-cascading-failures"><strong>24.8</strong> <strong>Cascading failures</strong></h3>

<p>You would think that if a system has hundreds of processes, it shouldn’t make much of a difference if a small percentage are slow or unreachable. The thing about faults is that they have the potential to spread virally and cascade from one process to the other until the whole system crumbles to its knees. This happens when</p>

<div class="source-page" id="source-page-257"></div>

<p>system components depend on each other, and a failure in one increases the probability of failure in others.</p>

<p>For example, suppose multiple clients are querying two database replicas, A and B, behind a load balancer. Each replica handles about 50 transactions per second (see Figure 24.1).</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-062.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-062.png" alt="Figure 24.1: Two replicas behind a load balancer; each is handling half the load." width="1101" height="844" loading="lazy"></a></figure>

<p class="source-caption">Figure 24.1: Two replicas behind a load balancer; each is handling half the load.</p>

<p>Suddenly, replica B becomes unavailable because of a network fault. The load balancer detects that B is unavailable and removes it from the pool. Because of that, replica A has to pick up the slack for B and serve twice the requests per unit time it was serving before (see Figure 24.2).</p>

<p>If replica A struggles to keep up with the incoming requests, the clients will experience increasingly more timeouts and start to retry requests, adding more load to the system. Eventually, replica A will be under so much load that most requests will time out, forcing the load balancer to remove it from the pool. In other words, the original network fault that caused replica B to become unavailable cascaded into a fault at replica A.</p>

<p>Suppose now that replica B becomes available again and the load balancer puts it back in the pool. Because it’s the only replica in the pool, it will be flooded with requests, causing it to overload and eventually be removed again.</p>

<div class="source-page" id="source-page-258"></div>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-063.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-063.png" alt="Figure 24.2: When replica B becomes unavailable, A will be hit with more load, which can strain it beyond its capacity." width="969" height="857" loading="lazy"></a></figure>

<p class="source-caption">Figure 24.2: When replica B becomes unavailable, A will be hit with more load, which can strain it beyond its capacity.</p>

<p>You can see how even after the network fault is gone, the application continues to struggle because of a feedback loop that causes the load to jump from one replica to another. Failures with this characteristic are also referred to as metastable<sup>12</sup>.</p>

<p>A big enough corrective action is usually needed to break the loop, like temporarily blocking traffic from getting to the replicas in the first place. Unfortunately, these failures are very hard to mitigate once they have started, and the best way to prevent them is to stop faults from spreading from one component to another in the first place.</p>

<h3 id="section-24-9-managing-risk"><strong>24.9</strong> <strong>Managing risk</strong></h3>

<p>As it should be evident by now, a distributed application needs to accept that faults are inevitable and be prepared to detect, react to, and repair them as they occur.</p>

<p>At this point, you might feel overwhelmed by the sheer amount of things that can go wrong. But just because a specific fault has</p>

<p class="source-footnote">12“Metastable Failures in Distributed Systems,” <a href="https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf">https://sigops.org/s/confere</a> <a href="https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf">nces/hotos/2021/papers/hotos21-s11-bronson.pdf</a></p>

<div class="source-page" id="source-page-259"></div>

<p>a chance of happening, it doesn’t mean we have to do something about it. We first have to consider the probability it will manifest and the impact it will cause to the system’s users when it does. By multiplying the two factors together, we get a risk score<sup>13</sup><sup> </sup>that we can use to prioritize which faults to address (see Figure 24.3) first. For example, a fault that is very likely to happen, and has a large impact, should be tackled head on; on the other hand, a fault with a low likelihood and low impact can wait.</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-064.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-064.png" alt="Figure 24.3: Risk matrix" width="2264" height="1724" loading="lazy"></a></figure>

<p class="source-caption">Figure 24.3: Risk matrix</p>

<p>Once we decide that we need to do something about a specific fault, we can try to reduce its probability and/or reduce its impact. This will be the main focus of the next chapters.</p>

<p class="source-footnote">13“Risk matrix,”<a href="https://en.wikipedia.org/wiki/Risk_matrix"> https://en.wikipedia.org/wiki/Risk_matrix</a></p>

## Redundancy

<section class="chapter-video" aria-label="Video for Redundancy"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>Redundancy</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-261"></div>

<p>Redundancy, the replication of functionality or state, is arguably the first line of defense against failures. When functionality or state is replicated over multiple nodes and a node fails, the others can take over. Moreover, as discussed in Part III, replication is also a core pattern that enables our applications to scale out horizontally.</p>

<p>Redundancy is the main reason why distributed applications can achieve better availability than single-node applications. But only some forms of redundancy actually improve availability. Marc Brooker lists four prerequisites<sup>1</sup>:</p>

<p>1. The complexity added by introducing redundancy mustn’t cost more availability than it adds. 2. The system must reliably detect which of the redundant components are healthy and which are unhealthy. 3. The system must be able to run in degraded mode. 4. The system must be able to return to fully redundant mode.</p>

<p>Let’s see how these prerequisites apply to a concrete example. Hardware faults such as disk, memory, and network failures can cause a node to crash, degrade or become otherwise unavailable. In a stateless service, a load balancer can mask these faults using</p>

<p class="source-footnote">1“When Redundancy Actually Helps,” <a href="https://brooker.co.za/blog/2019/06/20/redundancy.html">https://brooker.co.za/blog/2019/06</a> <a href="https://brooker.co.za/blog/2019/06/20/redundancy.html">/20/redundancy.html</a></p>

<div class="source-page" id="source-page-262"></div>

<p>a pool of redundant nodes. Although the load balancer increases the system’s complexity and, therefore, the number of ways the system can fail, the benefits in terms of scalability and availability almost always outweigh the risks it introduces (e.g., the load balancer failing).</p>

<p>The load balancer needs to detect which nodes are healthy and which aren’t to take the faulty ones out of the pool. It does that with health checks, as we learned in chapter 18. Health checks are critical to achieving high availability; if there are ten servers in the pool and one is unresponsive for some reason, then 10% of requests will fail, causing the availability to drop. Therefore, the longer it takes for the load balancer to detect the unresponsive server, the longer the failures will be visible to the clients.</p>

<p>Now, when the load balancer takes one or more unhealthy servers out of the pool, the assumption is that the others have enough capacity left to handle the increase in load. In other words, the system must be able to run in degraded mode. However, that by itself is not enough; new servers also need to be added to the pool to replace the ones that have been removed. Otherwise, there eventually won’t be enough servers left to cope with the load.</p>

<p>In stateful services, masking a node failure is a lot more complex since it involves replicating state. We have discussed replication at length in the previous chapters, and it shouldn’t come as a surprise by now that meeting the above requisites is a lot more challenging for a stateful service than for a stateless one.</p>

<h3 id="section-25-1-correlation"><strong>25.1</strong> <strong>Correlation</strong></h3>

<p>Redundancy is only helpful when the redundant nodes can’t fail for the same reason at the same time, i.e., when failures are not correlated. For example, if a faulty memory module causes a server to crash, it’s unlikely other servers will fail simultaneously for the same reason since they are running on different machines. However, if the servers are hosted in the same data center, and a fiber cut or an electrical storm causes a data-center-wide outage, the en-</p>

<div class="source-page" id="source-page-263"></div>

<p>tire application becomes unavailable no matter how many servers there are. In other words, the failures caused by a data center outage are correlated and limit the application’s availability. So if we want to increase the availability, we have to reduce the correlation between failures by using more than one data center.</p>

<p>Cloud providers such as AWS and Azure replicate their entire stack in multiple regions for that very reason. Each region comprises multiple data centers called Availability Zones (AZs) that are cross-connected with high-speed network links. AZs are far enough from each other to minimize the risk of correlated failures (e.g., power cuts) but still close enough to have low network latency, which is bounded by the speed of light. In fact, the latency is low enough by design to support synchronous replication protocols without a significant latency penalty.</p>

<p>With AZs, we can create applications that are resilient to data center outages. For example, a stateless service could have instances running in multiple AZs behind a shared load balancer so that if an AZ becomes unavailable, it doesn’t impact the availability of the service. On the other hand, stateful services require the use of a replication protocol to keep their state in sync across AZs. But since latencies are low enough between AZs, the replication protocol can be partially synchronous, like Raft, or even fully synchronous, like chain replication.</p>

<p>Taking it to the extreme, a catastrophic event could destroy an entire region with all of its AZs. To tolerate that, we can duplicate the entire application stack in multiple regions. To distribute the traffic to different data centers located in different regions, we can use<em> global DNS load balancing</em>. Unlike earlier, the application’s state needs to be replicated asynchronously across regions<sup>2</sup><sup> </sup>given the high network latency between regions (see Figure 25.1).</p>

<p>That said, the chance of an entire region being destroyed is extremely low. Before embarking on the effort of making your application resilient against region failures, you should have very good</p>

<p class="source-footnote">2“Active-Active for Multi-Regional Resiliency,” <a href="https://netflixtechblog.com/active-active-for-multi-regional-resiliency-c47719f6685b">https://netflixtechblog.com/</a> <a href="https://netflixtechblog.com/active-active-for-multi-regional-resiliency-c47719f6685b">active-active-for-multi-regional-resiliency-c47719f6685b</a></p>

<div class="source-page" id="source-page-264"></div>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-065.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-065.png" alt="Figure 25.1: A simplistic multi-region architecture" width="2300" height="2765" loading="lazy"></a></figure>

<p class="source-caption">Figure 25.1: A simplistic multi-region architecture</p>

<p>reasons for it. It’s more likely your application will be forced to have a presence in multiple regions for legal compliance reasons. For example, there are laws mandating that the data of European customers has to be processed and stored within Europe<sup>3</sup>.</p>

<p class="source-footnote">3“The CJEU judgment in the Schrems II case,”<a href="https://www.europarl.europa.eu/RegData/etudes/ATAG/2020/652073/EPRS_ATA(2020)652073_EN.pdf"> https://www.europarl.europa.</a> <a href="https://www.europarl.europa.eu/RegData/etudes/ATAG/2020/652073/EPRS_ATA(2020)652073_EN.pdf">eu/RegData/etudes/ATAG/2020/652073/EPRS_ATA(2020)652073_EN.pdf</a></p>

## Fault isolation

<section class="chapter-video" aria-label="Video for Fault isolation"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>Fault isolation</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-265"></div>

<p>So far, we have discussed how to address infrastructure faults with redundancy, but there are other kinds of failures that we can’t tolerate with redundancy alone because of their high degree of correlation.</p>

<p>For example, suppose a specific user sends malformed requests (deliberately or not) that cause the servers handling them to crash because of a bug. Since the bug is in the code, it doesn’t matter how many DCs and regions our application is deployed to; if the user’s requests can land anywhere, they can affect all DCs and regions. Due to their nature, these requests are sometimes referred to as poison pills.</p>

<p>Similarly, if the requests of a specific user require a lot more resources than others, they can degrade the performance for every other user (aka noisy neighbor effect).</p>

<p>The main issue in the previous examples is that the blast radius of poison pills and noisy neighbors is the entire application. To reduce it, we can partition the application’s stack by user so that the requests of a specific user can only ever affect the partition it was assigned to.<sup>1</sup><sup> </sup>That way, even if a user is degrading a partition,</p>

<p class="source-footnote">1We discussed partitioning in chapter 16 from a scalability point of view.</p>

<div class="source-page" id="source-page-266"></div>

<p>the issue is isolated from the rest of the system.</p>

<p>For example, suppose we have 6 instances of a stateless service behind a load balancer, divided into 3 partitions (see Figure 26.1). In this case, a noisy or poisonous user can only ever impact 33 percent of users. And as the number of partitions increases, the blast radius decreases further.</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-066.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-066.png" alt="Figure 26.1: Service instances partitioned into 3 partitions" width="1726" height="1125" loading="lazy"></a></figure>

<p class="source-caption">Figure 26.1: Service instances partitioned into 3 partitions</p>

<p>The use of partitions for fault isolation is also referred to as the <em>bulkhead pattern</em>, named after the compartments of a ship’s hull. If one compartment is damaged and fills up with water, the leak is isolated to that partition and doesn’t spread to the rest of the ship.</p>

<h3 id="section-26-1-shuffle-sharding"><strong>26.1</strong> <strong>Shuffle sharding</strong></h3>

<p>The problem with partitioning is that users who are unlucky enough to land on a degraded partition are impacted as well. For stateless services, there is a very simple, yet powerful, variation of partitioning called shuffle sharding<sup>2</sup><sup> </sup>that can help mitigate that.</p>

<p>The idea is to introduce<em> virtual partitions</em> composed of random (but</p>

<p class="source-footnote">2“Shuffle Sharding: Massive and Magical Fault Isolation,”<a href="https://aws.amazon.com/blogs/architecture/shuffle-sharding-massive-and-magical-fault-isolation/"> https://aws.amazon</a> <a href="https://aws.amazon.com/blogs/architecture/shuffle-sharding-massive-and-magical-fault-isolation/">.com/blogs/architecture/shuffle-sharding-massive-and-magical-fault-isolation/</a></p>

<div class="source-page" id="source-page-267"></div>

<p>permanent) subsets of service instances. This makes it much more unlikely for two users to be allocated to the same partition as each other.</p>

<p>Let’s go back to our previous example of a stateless service with 6 instances. How many combinations of virtual partitions with 2 instances can we build out of 6 instances? If you recall the combinations formula from your high school statistics class, the answer is 15:</p>

<p>n! r!(n−r)! <sup>=</sup><sup> </sup><sup>6!</sup></p>

<p>2!4! <sup>= 15</sup></p>

<p>There are now 15 partitions for a user to be assigned to, while before, we had only 3, which makes it a lot less likely for two users to end up in the same partition. The caveat is that virtual partitions partially overlap (see Figure 26.2). But by combining shuffle sharding with a load balancer that removes faulty instances, and clients that retry failed requests, we can build a system with much better fault isolation than one with physical partitions alone.</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-067.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-067.png" alt="Figure 26.2: Virtual partitions are far less likely to fully overlap with each other." width="1734" height="1117" loading="lazy"></a></figure>

<p class="source-caption">Figure 26.2: Virtual partitions are far less likely to fully overlap with each other.</p>

<div class="source-page" id="source-page-268"></div>

<h3 id="section-26-2-cellular-architecture"><strong>26.2</strong> <strong>Cellular architecture</strong></h3>

<p>In the previous examples, we discussed partitioning in the context of stateless services. We can take it up a notch and partition the entire application stack, including its dependencies (load balancers, compute services, storage services, etc.), by user<sup>3</sup><sup> </sup>into<em> cells</em><sup>4</sup>. Each cell is completely independent of others, and a gateway service is responsible for routing requests to the right cells.</p>

<p>We have already seen an example of a “cellular” architecture when discussing Azure Storage in Chapter 17. In Azure Storage, a cell is a storage cluster, and accounts are partitioned across storage clusters (see Figure 26.3).</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-068.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-068.png" alt="Figure 26.3: Each storage cluster (stamp) is a cell in Azure Storage." width="1707" height="1887" loading="lazy"></a></figure>

<p class="source-caption">Figure 26.3: Each storage cluster (stamp) is a cell in Azure Storage.</p>

<p class="source-footnote">3Partitioning by user is just an example; we could partition just as well by physical location, workload, or any other dimension that makes sense for the application.</p>

<p class="source-footnote">4“New Relic case: Huge scale, small clusters: Using Cells to scale in the Cloud,” <a href="https://www.youtube.com/watch?v=eMikCXiBlOA">https://www.youtube.com/watch?v=eMikCXiBlOA</a></p>

<div class="source-page" id="source-page-269"></div>

<p>An unexpected benefit of cellular architectures comes from setting limits to the maximum capacity of a cell. That way, when the system needs to scale out, a new cell is added rather than scaling out existing ones. Since a cell has a maximum size, we can thoroughly test and benchmark it at that size, knowing that we won’t have any surprises in the future and hit some unexpected brick wall.</p>

## Downstream resiliency

<section class="chapter-video" aria-label="Video for Downstream resiliency"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>Downstream resiliency</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-271"></div>

<p>Now that we have discussed how to reduce the impact of faults at the architectural level with redundancy and partitioning, we will dive into tactical resiliency patterns that stop faults from propagating from one component or service to another. In this chapter, we will discuss patterns that protect a service from failures of downstream dependencies.</p>

<h3 id="section-27-1-timeout"><strong>27.1</strong> <strong>Timeout</strong></h3>

<p>When a network call is made, it’s best practice to configure a time-out to fail the call if no response is received within a certain amount of time. If the call is made without a timeout, there is a chance it will never return, and as mentioned in chapter 24, network calls that don’t return lead to resource leaks. Thus, the role of timeouts is to detect connectivity faults and stop them from cascading from one component to another. In general, timeouts are a must-have for operations that can potentially never return, like acquiring a mutex.</p>

<p>Unfortunately, some network APIs don’t have a way to set a time-out in the first place, while others have no timeout configured by default. For example, JavaScript’s<em> XMLHttpRequest</em> is<em> the</em> web API</p>

<div class="source-page" id="source-page-272"></div>

<p>to retrieve data from a server asynchronously, and its default time-out is zero<sup>1</sup>, which means there is no timeout:</p>

<pre><code>var xhr = new XMLHttpRequest();
xhr.open(&quot;GET&quot;, &quot;/api&quot;, true);
// No timeout by default, so it needs to be set explicitly!
xhr.timeout = 10000; // 10K milliseconds
xhr.onload = function () {
  // Request finished
};
xhr.ontimeout = function (e) {
  // Request timed out
};
xhr.send(null);</code></pre>

<p>The<em> </em><em>fetch</em> web API is a modern replacement for<em> </em><em>XMLHttpRequest</em> that uses Promises. When the fetch API was initially introduced, there was no way to set a timeout at all<sup>2</sup>. Browsers have only later added support for timeouts through the Abort API<sup>3</sup>. Things aren’t much rosier for Python; the popular<em> requests</em> library uses a default timeout of infinity<sup>4</sup>. And Go’s<em> HTTP package</em> doesn’t use timeouts<sup>5</sup></p>

<p>by default.</p>

<p>Modern HTTP clients for Java and .NET do a better job and usually, come with default timeouts. For example, .NET Core<em> </em><em>HttpClient</em> has a default timeout of 100 seconds<sup>6</sup>. It’s lax but arguably better than not having a timeout at all.</p>

<p>As a rule of thumb, always set timeouts when making network calls, and be wary of third-party libraries that make network calls</p>

<p class="source-footnote">1“Web APIs: XMLHttpRequest.timeout,” <a href="https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/timeout">https://developer.mozilla.org/en-</a> <a href="https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/timeout">US/docs/Web/API/XMLHttpRequest/timeout</a></p>

<p class="source-footnote"><a href="https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/timeout">2</a>“Add a timeout option, to prevent hanging,”<a href="https://github.com/whatwg/fetch/issues/951"> https://github.com/whatwg/fe</a> <a href="https://github.com/whatwg/fetch/issues/951">tch/issues/951</a></p>

<p class="source-footnote"><a href="https://github.com/whatwg/fetch/issues/951">3</a>“Web APIs: AbortController,” <a href="https://developer.mozilla.org/en-US/docs/Web/API/AbortController">https://developer.mozilla.org/en-US/docs/</a> <a href="https://developer.mozilla.org/en-US/docs/Web/API/AbortController">Web/API/AbortController</a></p>

<p class="source-footnote"><a href="https://developer.mozilla.org/en-US/docs/Web/API/AbortController">4</a>“Requests Quickstart: Timeouts,”<a href="https://requests.readthedocs.io/en/master/user/quickstart/#timeouts"> https://requests.readthedocs.io/en/maste</a> <a href="https://requests.readthedocs.io/en/master/user/quickstart/#timeouts">r/user/quickstart/#timeouts</a></p>

<p class="source-footnote"><a href="https://requests.readthedocs.io/en/master/user/quickstart/#timeouts">5</a>“net/http: make default configs have better timeouts,”<a href="https://github.com/golang/go/issues/24138"> https://github.com/g</a> <a href="https://github.com/golang/go/issues/24138">olang/go/issues/24138</a></p>

<p class="source-footnote"><a href="https://github.com/golang/go/issues/24138">6</a>“HttpClient.Timeout Property,” <a href="https://docs.microsoft.com/en-us/dotnet/api/system.net.http.httpclient.timeout?view=net-6.0#remarks">https://docs.microsoft.com/en-us/dotnet/</a> <a href="https://docs.microsoft.com/en-us/dotnet/api/system.net.http.httpclient.timeout?view=net-6.0#remarks">api/system.net.http.httpclient.timeout?view=net-6.0#remarks</a></p>

<div class="source-page" id="source-page-273"></div>

<p>but don’t expose settings for timeouts.</p>

<p>But how do we determine a good timeout duration? One way is to base it on the desired false timeout rate<sup>7</sup>. For example, suppose we have a service calling another, and we are willing to accept that 0.1% of downstream requests that would have eventually returned a response time out (i.e., 0.1% false timeout rate). To accomplish that, we can configure the timeout based on the 99.9th percentile of the downstream service’s response time.</p>

<p>We also want to have good monitoring in place to measure the entire lifecycle of a network call, like the duration of the call, the status code received, and whether a timeout was triggered. We will talk more about monitoring later in the book, but the point I want to make here is that we have to measure what happens at the integration points of our systems, or we are going to have a hard time debugging production issues.</p>

<p>Ideally, a network call should be wrapped within a library function that sets a timeout and monitors the request so that we don’t have to remember to do this for each call. Alternatively, we can also use a reverse proxy co-located on the same machine, which intercepts remote calls made by our process. The proxy can enforce timeouts and monitor calls, relieving our process ofthis responsibility. We talked about this in section 18.3 when discussing the sidecar pattern and the service mesh.</p>

<h3 id="section-27-2-retry"><strong>27.2</strong> <strong>Retry</strong></h3>

<p>We know by now that a client should configure a timeout when making a network request. But what should it do when the request fails or times out? The client has two options at that point: it can either fail fast or retry the request. If a short-lived connectivity issue caused the failure or timeout, then retrying after some <em>backoff time</em> has a high probability of succeeding. However, if the downstream service is overwhelmed, retrying immediately after</p>

<p class="source-footnote">7“Timeouts, retries, and backoff with jitter,”<a href="https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/"> https://aws.amazon.com/builder</a> <a href="https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/">s-library/timeouts-retries-and-backoff-with-jitter/</a></p>

<div class="source-page" id="source-page-274"></div>

<p>will only worsen matters. This is why retrying needs to be slowed down with increasingly longer delays between the individual retries until either a maximum number of retries is reached or enough time has passed since the initial request.</p>

<h4 id="section-27-2-1-exponential-backoff"><strong>27.2.1</strong> <strong>Exponential backoff</strong></h4>

<p>To set the delay between retries, we can use a<em> </em><em>capped</em><em> </em><em>exponential</em> <em>function</em>, where the delay is derived by multiplying the initial backoff duration by a constant that increases exponentially after each attempt, up to some maximum value (the cap):</p>

<p>delay = min(cap, initial-backoff ⋅2<sup>attempt</sup>)</p>

<p>For example, if the cap is set to 8 seconds, and the initial backoff duration is 2 seconds, then the first retry delay is 2 seconds, the second is 4 seconds, the third is 8 seconds, and any further delay will be capped to 8 seconds.</p>

<p>Although exponential backoff does reduce the pressure on the downstream dependency, it still has a problem. When the downstream service is temporarily degraded, multiple clients will likely see their requests failing around the same time. This will cause clients to retry simultaneously, hitting the downstream service with load spikes that further degrade it, as shown in Figure 27.1.</p>

<p>To avoid this herding behavior, we can introduce random jitter<sup>8</sup></p>

<p>into the delay calculation. This spreads retries out over time, smoothing out the load to the downstream service:</p>

<p>delay = random(0, min(cap, initial-backoff ⋅2<sup>attempt</sup>))</p>

<p>Actively waiting and retrying failed network requests isn’t the only way to implement retries. In batch applications that don’t have strict real-time requirements, a process can park a failed</p>

<p class="source-footnote">8“Exponential Backoff And Jitter,”<a href="https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/"> https://aws.amazon.com/blogs/architect</a> <a href="https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/">ure/exponential-backoff-and-jitter/</a></p>

<div class="source-page" id="source-page-275"></div>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-069.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-069.png" alt="Figure 27.1: Retry storm" width="1507" height="920" loading="lazy"></a></figure>

<p class="source-caption">Figure 27.1: Retry storm</p>

<p>request into a<em> </em><em>retry</em><em> </em><em>queue</em>. The same process, or possibly another, can read from the same queue later and retry the failed requests.</p>

<p>Just because a network call can be retried doesn’t mean it should be. If the error is not short-lived, for example, because the process is not authorized to access the remote endpoint, it makes no sense to retry the request since it will fail again. In this case, the process should fail fast and cancel the call right away. And as discussed in chapter 5.7, we should also understand the consequences of retrying a network call that isn’t idempotent and whose side effects can affect the application’s correctness.</p>

<h4 id="section-27-2-2-retry-amplification"><strong>27.2.2</strong> <strong>Retry amplification</strong></h4>

<p>Suppose that handling a user request requires going through a chain of three services. The user’s client calls service A, which calls service B, which in turn calls service C. If the intermediate request from service B to service C fails, should B retry the request or not? Well, if B does retry it, A will perceive a longer execution time for its request, making it more likely to hit A’s timeout. If that happens, A retries the request, making it more likely for the client to hit its timeout and retry.</p>

<div class="source-page" id="source-page-276"></div>

<p>Having retries at multiple levels of the dependency chain can amplify the total number of retries — the deeper a service is in the chain, the higher the load it will be exposed to due to retry amplification (see Figure 27.2).</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-070.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-070.png" alt="Figure 27.2: Retry amplification in action" width="2338" height="543" loading="lazy"></a></figure>

<p class="source-caption">Figure 27.2: Retry amplification in action</p>

<p>And if the pressure gets bad enough, this behavior can easily overload downstream services. That’s why, when we have long dependency chains, we should consider retrying at a single level of the chain and failing fast in all the others.</p>

<h3 id="section-27-3-circuit-breaker"><strong>27.3</strong> <strong>Circuit breaker</strong></h3>

<p>Suppose a service uses timeouts to detect whether a downstream dependency is unavailable and retries to mitigate transient failures. If the failures aren’t transient and the downstream dependency remains unresponsive, what should it do then? If the service keeps retrying failed requests, it will necessarily become slower for its clients. In turn, this slowness can spread to the rest of the system.</p>

<p>To deal with non-transient failures, we need a mechanism that detects long-term degradations of downstream dependencies and stops new requests from being sent downstream in the first place. After all, the fastest network call is the one we don’t have to make. The mechanism in question is the<em> </em><em>circuit</em><em> </em><em>breaker</em>, inspired by the same functionality implemented in electrical circuits.</p>

<p>The goal of the circuit breaker is to allow a sub-system to fail without slowing down the caller. To protect the system, calls to the failing sub-system are temporarily blocked. Later, when the subsystem recovers and failures stop, the circuit breaker allows calls</p>

<div class="source-page" id="source-page-277"></div>

<p>to go through again.</p>

<p>Unlike retries, circuit breakers prevent network calls entirely, making the pattern particularly useful for non-transient faults. In other words, retries are helpful when the expectation is that the next call will succeed, while circuit breakers are helpful when the expectation is that the next call will fail.</p>

<p>A circuit breaker can be implemented as a state machine with three states: open, closed, and half-open (see Figure 27.3).</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-071.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-071.png" alt="Figure 27.3: Circuit breaker state machine" width="1531" height="1122" loading="lazy"></a></figure>

<p class="source-caption">Figure 27.3: Circuit breaker state machine</p>

<p>In the closed state, the circuit breaker merely acts as a pass-through for network calls. In this state, the circuit breaker tracks the number of failures, like errors and timeouts. If the number goes over a certain threshold within a predefined time interval, the circuit breaker trips and opens the circuit.</p>

<p>When the circuit is open, network calls aren’t attempted and fail immediately. As an open circuit breaker can have business implications, we need to consider what should happen when a downstream dependency is down. If the dependency is non-critical, we want our service to degrade gracefully rather than to stop entirely. Think of an airplane that loses one of its non-critical sub-systems in flight; it shouldn’t crash but rather gracefully degrade to a state</p>

<div class="source-page" id="source-page-278"></div>

<p>where the plane can still fly and land. Another example is Amazon’s front page; if the recommendation service is unavailable, the page renders without recommendations. It’s a better outcome than failing to render the whole page entirely.</p>

<p>After some time has passed, the circuit breaker gives the downstream dependency another chance and transitions to the half-open state. In the half-open state, the next call is allowed to pass through to the downstream service. If the call succeeds, the circuit breaker transitions to the closed state; if the call fails instead, it transitions back to the open state.</p>

<p>You might think that’s all there is to understand how a circuit breaker works, but the devil is in the details. For example, how many failures are enough to consider a downstream dependency down? How long should the circuit breaker wait to transition from the open to the half-open state? It really depends on the specific context; only by using data about past failures can we make an informed decision.</p>

## Upstream resiliency

<section class="chapter-video" aria-label="Video for Upstream resiliency"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>Upstream resiliency</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-279"></div>

<p>The previous chapter discussed patterns that protect services against downstream failures, like failures to reach an external dependency. In this chapter, we will shift gears and discuss mechanisms to protect against upstream pressure.<sup>1</sup></p>

<h3 id="section-28-1-load-shedding"><strong>28.1</strong> <strong>Load shedding</strong></h3>

<p>A server has very little control over how many requests it receives at any given time. The operating system has a connection queue per port with a limited capacity that, when reached, causes new connection attempts to be rejected immediately. But typically, under extreme load, the server crawls to a halt before that limit is reached as it runs out of resources like memory, threads, sockets, or files. This causes the response time to increase until eventually, the server becomes unavailable to the outside world.</p>

<p>When a server operates at capacity, it should reject excess requests<sup>2</sup></p>

<p>so that it can dedicate its resources to the requests it’s already processing. For example, the server could use a counter to measure</p>

<p class="source-footnote">1We have already met a mechanism to protect against upstream pressure when we discussed health checks in the context of load balancers in chapter 18.</p>

<p class="source-footnote">2“Using load shedding to avoid overload,”<a href="https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload"> https://aws.amazon.com/builders-</a> <a href="https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload">library/using-load-shedding-to-avoid-overload</a></p>

<div class="source-page" id="source-page-280"></div>

<p>the number of concurrent requests being processed that is incremented when a new request comes in and decreased when a response is sent. The server can then infer whether it’s overloaded by comparing the counter with a threshold that approximates the server’s capacity.</p>

<p>When the server detects that it’s overloaded, it can reject incoming requests by failing fast and returning a response with status code <em>503 (Service Unavailable)</em>. This technique is also referred to as<em> load</em> <em>shedding</em>. The server doesn’t necessarily have to reject arbitrary requests; for example, if different requests have different priorities, the server could reject only low-priority ones. Alternatively, the server could reject the oldest requests first since those will be the first ones to time out and be retried, so handling them might be a waste of time.</p>

<p>Unfortunately, rejecting a request doesn’t completely shield the server from the cost of handling it. Depending on how the rejection is implemented, the server might still have to pay the price of opening a TLS connection and reading the request just to reject it. Hence, load shedding can only help so much, and if load keeps increasing, the cost of rejecting requests will eventually take over and degrade the server.</p>

<h3 id="section-28-2-load-leveling"><strong>28.2</strong> <strong>Load leveling</strong></h3>

<p>There is an alternative to load shedding, which can be exploited when clients don’t expect a prompt response. The idea is to introduce a messaging channel between the clients and the service. The channel decouples the load directed to the service from its capacity, allowing it to process requests at its own pace.</p>

<p>This pattern is referred to as load leveling and it’s well suited to fending off short-lived spikes, which the channel smooths out (see Figure 28.1). But if the service doesn’t catch up eventually, a large backlog will build up, which comes with its own problems, as discussed in chapter 23.</p>

<p>Load-shedding and load leveling don’t address an increase in load</p>

<div class="source-page" id="source-page-281"></div>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-072.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-072.png" alt="Figure 28.1: The channel smooths out the load for the consuming service." width="2345" height="1115" loading="lazy"></a></figure>

<p class="source-caption">Figure 28.1: The channel smooths out the load for the consuming service.</p>

<p>directly but rather protect a service from getting overloaded. To handle more load, the service needs to be scaled out. This is why these protection mechanisms are typically combined with autoscaling<sup>3</sup>, which detects that the service is running hot and automatically increases its scale to handle the additional load.</p>

<h3 id="section-28-3-rate-limiting"><strong>28.3</strong> <strong>Rate-limiting</strong></h3>

<p>Rate-limiting, or throttling, is a mechanism that rejects a request when a specific quota is exceeded. A service can have multiple quotas, e.g., for the number of requests or bytes received within a time interval. Quotas are typically applied to specific users, API keys, or IP addresses.</p>

<p>For example, if a service with a quota of 10 requests per second per API key receives on average 12 requests per second from a specific API key, it will, on average, reject 2 requests per second from that API key.</p>

<p>When a service rate-limits a request, it needs to return a response with a particular error code so that the sender knows that it failed because a quota has been exhausted. For services with HTTP APIs,</p>

<p class="source-footnote">3“Autoscaling,”<a href="https://en.wikipedia.org/wiki/Autoscaling"> https://en.wikipedia.org/wiki/Autoscaling</a></p>

<div class="source-page" id="source-page-282"></div>

<p>the most common way to do that is by returning a response with status code<em> 429 (Too Many Requests)</em>. The response should include additional details about which quota has been exhausted and by how much; it can also include a<em> Retry-After</em> header indicating how long to wait before making a new request:</p>

<p>If the client application plays by the rules, it will stop hammering the service for some time, shielding the service from non-malicious users monopolizing it by mistake. In addition, this protects against bugs in the clients that cause a client to hit a downstream service for one reason or another repeatedly.</p>

<p>Rate-limiting is also used to enforce pricing tiers; if users want to use more resources, they should also be willing to pay more. This is how you can offload your service’s cost to your users: have them pay proportionally to their usage and enforce pricing tiers with quotas.</p>

<p>You would think that rate-limiting also offers strong protection against a DDoS attack, but it only partially protects a service from it. Nothing forbids throttled clients from continuing to hammer a service after getting<em> </em><em>429s</em>. Rate-limited requests aren’t free either — for example, to rate-limit a request by API key, the service has</p>

<p>to pay the price of opening a TLS connection, and at the very least, download part of the request to read the key. Although rate limiting doesn’t fully protect against DDoS attacks, it does help reduce their impact.</p>

<p>Economies of scale are the only true protection against DDoS at-tacks. If you run multiple services behind one large gateway service, no matter which of the services behind it are attacked, the gateway service will be able to withstand the attack by rejecting the traffic upstream. The beauty of this approach is that the cost of running the gateway is amortized across all the services that are using it.</p>

<p>Although rate-limiting has some similarities with load shedding, they are different concepts. Load shedding rejects traffic based on the local state of a process, like the number of requests concurrently processed by it; rate-limiting instead sheds traffic based on</p>

<div class="source-page" id="source-page-283"></div>

<p>the global state of the system, like the total number of requests concurrently processed for a specific API key across all service instances. And because there is a global state involved, some form of coordination is required.</p>

<h4 id="section-28-3-1-single-process-implementation"><strong>28.3.1</strong> <strong>Single-process implementation</strong></h4>

<p>The distributed implementation of rate-limiting is interesting in its own right, and it’s well worth spending some time discussing it. We will start with a single-process implementation first and then extend it to a distributed one.</p>

<p>Suppose we want to enforce a quota of 2 requests per minute, per API key. A naive approach would be to use a doubly-linked list per API key, where each list stores the timestamps of the last N requests received. Whenever a new request comes in, an entry is appended to the list with its corresponding timestamp. Then, periodically, entries older than a minute are purged from the list.</p>

<p>By keeping track of the list’s length, the process can rate-limit incoming requests by comparing it with the quota. The problem with this approach is that it requires a list per API key, which quickly becomes expensive in terms of memory as it grows with the number of requests received.</p>

<p>To reduce memory consumption, we need to come up with a way to reduce the storage requirements. One way to do this is by dividing time into buckets of fixed duration, for example of 1 minute, and keeping track of how many requests have been seen within each bucket (see Figure 28.2).</p>

<p>A bucket contains a numerical counter. When a new request comes in, its timestamp is used to determine the bucket it belongs to. For example, if a request arrives at 12.00.18, the counter of the bucket for minute “12.00” is incremented by 1 (see Figure 28.3).</p>

<p>With bucketing, we can compress the information about the number of requests seen in a way that doesn’t grow with the number of requests. Now that we have a memory-friendly representation, how can we use it to implement rate-limiting? The idea is to use a</p>

<div class="source-page" id="source-page-284"></div>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-073.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-073.png" alt="Figure 28.2: Buckets divide time into 1-minute intervals, which keep track of the number of requests seen." width="1692" height="884" loading="lazy"></a></figure>

<p class="source-caption">Figure 28.2: Buckets divide time into 1-minute intervals, which keep track of the number of requests seen.</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-074.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-074.png" alt="Figure 28.3: When a new request comes in, its timestamp is used to determine the bucket it belongs to." width="1715" height="941" loading="lazy"></a></figure>

<p class="source-caption">Figure 28.3: When a new request comes in, its timestamp is used to determine the bucket it belongs to.</p>

<p>sliding window that moves across the buckets in real time, keeping track of the number of requests within it.</p>

<p>The sliding window represents the interval of time used to decide whether to rate-limit or not. The window’s length depends on the time unit used to define the quota, which in our case is 1 minute. But there is a caveat: a sliding window can overlap with multiple</p>

<div class="source-page" id="source-page-285"></div>

<p>buckets. To derive the number of requests under the sliding window, we have to compute a weighted sum of the bucket’s counters, where each bucket’s weight is proportional to its overlap with the sliding window (see Figure 28.4).</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-075.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-075.png" alt="Figure 28.4: A bucket’s weight is proportional to its overlap with the sliding window." width="1692" height="840" loading="lazy"></a></figure>

<p class="source-caption">Figure 28.4: A bucket’s weight is proportional to its overlap with the sliding window.</p>

<p>Although this is an approximation, it’s a reasonably good one for our purposes. And it can be made more accurate by increasing the granularity of the buckets. So, for example, we can reduce the approximation error using 30-second buckets rather than 1-minute ones.</p>

<p>We only have to store as many buckets as the sliding window can overlap with at any given time. For example, with a 1-minute window and a 1-minute bucket length, the sliding window can overlap with at most 2 buckets. Thus, there is no point in storing the third oldest bucket, the fourth oldest one, etc.</p>

<p>To summarize, this approach requires two counters per API key, which is much more efficient in terms of memory than the naive implementation storing a list of requests per API key.</p>

<h4 id="section-28-3-2-distributed-implementation"><strong>28.3.2</strong> <strong>Distributed implementation</strong></h4>

<p>When more than one process accepts requests, the local state is no longer good enough, as the quota needs to be enforced on the total</p>

<div class="source-page" id="source-page-286"></div>

<p>number of requests per API key across all service instances. This requires a shared data store to keep track of the number of requests seen.</p>

<p>As discussed earlier, we need to store two integers per API key, one for each bucket. When a new request comes in, the process receiving it could fetch the current bucket, update it and write it back to the data store. But that wouldn’t work because two processes could update the same bucket concurrently, which would result in a lost update. The fetch, update, and write operations need to be packaged into a single transaction to avoid any race conditions.</p>

<p>Although this approach is functionally correct, it’s costly. There are two issues here: transactions are slow, and executing one per request would be very expensive as the data store would have to scale linearly with the number of requests. Also, because the data store is a hard dependency, the service will become unavailable if it can’t reach it.</p>

<p>Let’s address these issues. Rather than using transactions, we can use a single atomic<em> get-and-increment</em> operation that most data stores provide. Alternatively, the same can be emulated with a<em> </em><em>compare-and-swap</em>. These atomic operations have much better performance than transactions.</p>

<p>Now, rather than updating the data store on each request, the process can batch bucket updates in memory for some time and flush them asynchronously to the data store at the end of it (see Figure 28.5). This reduces the shared state’s accuracy, but it’s a good trade-off as it reduces the load on the data store and the number of requests sent to it.</p>

<p>What happens if the data store is down? Remember the CAP theorem’s essence: when there is a network fault, we can either sacrifice consistency and keep our system up or maintain consistency and stop serving requests. In our case, temporarily rejecting requests just because the data store used for rate-limiting is not reachable could damage the business. Instead, it’s safer to keep serving re-</p>

<div class="source-page" id="source-page-287"></div>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-076.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-076.png" alt="Figure 28.5: Servers batch bucket updates in memory for some time, and flush them asynchronously to the data store at the end of it." width="1870" height="877" loading="lazy"></a></figure>

<p class="source-caption">Figure 28.5: Servers batch bucket updates in memory for some time, and flush them asynchronously to the data store at the end of it.</p>

<p>quests based on the last state read from the store.<sup>4</sup></p>

<h3 id="section-28-4-constant-work"><strong>28.4</strong> <strong>Constant work</strong></h3>

<p>When overload, configuration changes, or faults force an application to behave differently from usual, we say the application has a multi-modal behavior. Some of these<em> </em><em>modes</em> might trigger rare bugs, conflict with mechanisms that assume the happy path, and more generally make life harder for operators, since their mental model of how the application behaves is no longer valid. Thus, as a general rule of thumb, we should strive to minimize the number of modes.</p>

<p>For example, simple key-value stores are favored over relational databases in data planes because they tend to have predictable performance<sup>5</sup>. A relational database has many operational modes due to hidden optimizations, which can change how specific queries perform from one execution to another. Instead, dumb key-value stores behave predictably for a given query, which guarantees that</p>

<p class="source-footnote">4This is another application of the concept of<em> static stability</em>, first introduced in chapter 22.</p>

<p class="source-footnote">5“Some opinionated thoughts on SQL databases,”<a href="https://blog.nelhage.com/post/some-opinionated-sql-takes/"> https://blog.nelhage.com/p</a> <a href="https://blog.nelhage.com/post/some-opinionated-sql-takes/">ost/some-opinionated-sql-takes/</a></p>

<div class="source-page" id="source-page-288"></div>

<p>there won’t be any surprises.</p>

<p>A common reason for a system to change behavior is overload, which can cause the system to become slower and degrade at the worst possible time. Ideally, the worst- and average-case behavior shouldn’t differ. One way to achieve that is by exploiting the <em>constant work pattern</em>, which keeps the work per unit time constant.</p>

<p>The idea is to have the system perform the same amount of work<sup>6</sup></p>

<p>under high load as under average load. And, if there is any variation under stress, it should be because the system is performing better, not worse. Such a system is also said to be<em> antifragile</em>. This is a different property from resiliency; a resilient system keeps operating under extreme load, while an antifragile one performs better.</p>

<p>We have already seen one application of the constant work pattern when discussing the propagation of configuration changes from the control plane to the data plane in chapter 22. For example, suppose we have a configuration store (control plane) that stores a bag of settings for each user, like the quotas used by the API gateway (data plane) to rate-limit requests. When a setting changes for a specific user, the control plane needs to broadcast it to the data plane. However, as each change is a separate independent unit of work, the data plane needs to perform work proportional to the number of changes.</p>

<p>If you don’t see how this could be a problem, imagine that a large number of settings are updated for the majority of users at the same time (e.g., quotas changed due to a business decision). This could cause an unexpectedly large number of individual update messages to be sent to every data plane instance, which could struggle to handle them.</p>

<p>The workaround to this problem is simple but powerful. The control plane can periodically dump the settings of all users to a file in a scalable and highly available file store like Azure Storage or AWS S3. The dump includes the configuration settings of all users, even the ones for which there were no changes. Data plane instances</p>

<p class="source-footnote">6“Reliability, constant work, and a good cup of coffee,”<a href="https://aws.amazon.com/builders-library/reliability-and-constant-work/"> https://aws.amazon.c</a> <a href="https://aws.amazon.com/builders-library/reliability-and-constant-work/">om/builders-library/reliability-and-constant-work/</a></p>

<div class="source-page" id="source-page-289"></div>

<p>can then periodically read the dump in bulk and refresh their local view of the system’s configuration. Thus, no matter how many settings change, the control plane periodically writes a file to the data store, and the data plane periodically reads it.</p>

<p>We can take this pattern to the extreme and pre-allocate empty configuration slots for the maximum number of supported users. This guarantees that as the number of users grows, the work required to propagate changes remains stable. Additionally, doing so allows to stress-test the system and understand its behavior, knowing that it will behave the same under all circumstances. Although this limits the number of users, a limit exists regardless of whether the constant work pattern is used or not. This approach is typically used in cellular architectures (see 26.2), where a single cell has a well-defined maximum size and the system is scaled out by creating new cells.</p>

<p>The beauty of using the constant work pattern is that the data plane periodically performs the same amount of work in bulk, no matter how many configuration settings have changed. This makes updating settings reliable and predictable. Also, periodically writing and reading a large file is much simpler to implement correctly than a complex mechanism that only sends what changed.</p>

<p>Another advantage of this approach is that it’s robust against a whole variety of faults thanks to its self-healing properties. If the configuration dump gets corrupted for whatever reason, no harm is done since the next update will fix it. And if a faulty update was pushed to all users by mistake, reverting it is as simple as creating a new dump and waiting it out. In contrast, the solution that sends individual updates is much harder to implement correctly, as the data plane needs complex logic to handle and heal from corrupted updates.</p>

<p>To sum up, performing constant work is more expensive than doing just the necessary work. Still, it’s often worth considering it, given the increase in reliability and reduction in complexity it enables.</p>

<div class="source-page" id="source-page-291"></div>

<p>As the number of components or operations in a system increases, so does the number of failures, and eventually, anything that can happen will happen. In my team, we humorously refer to this as “cruel math.”</p>

<p>If you talk to an engineer responsible for a production system, you will quickly realize that they tend to be more worried about minimizing and tolerating failures than how to further scale out their systems. The reason for that is that once you have an architecture that scales to handle your current load, you will be mostly concerned with tolerating faults until you eventually reach the next scalability bottleneck.</p>

<p>What you should take away from this part is that failures are inevitable since, no matter how hard you try, it’s just impossible to build an infallible system. When you can’t design away some failure modes (e.g., with constant work), the best you can do is to reduce their blast radius and stop the cracks from propagating from one component to the other.</p>
