# Foundations

## Introduction

<section class="chapter-video" aria-label="Video for Introduction"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>Introduction</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-19"></div>

<p><em>“A</em><em> </em><em>distributed</em><em> </em><em>system</em><em> </em><em>is</em><em> </em><em>one</em><em> </em><em>in</em><em> </em><em>which</em><em> </em><em>the</em><em> </em><em>failure</em><em> </em><em>of</em><em> </em><em>a</em><em> </em><em>com</em><em>puter</em><em> </em><em>you</em><em> </em><em>didn’t</em><em> </em><em>even</em><em> </em><em>know</em><em> </em><em>existed</em><em> </em><em>can</em><em> </em><em>render</em><em> </em><em>your</em><em> </em><em>own</em> <em>computer unusable.”</em></p>

<p>– Leslie Lamport</p>

<p>Loosely speaking, a distributed system is a group of nodes that cooperate by exchanging messages over communication links to achieve some task. A node can generically refer to a physical machine, like a phone, or a software process, like a browser.</p>

<p>Why do we bother building distributed systems in the first place?</p>

<p>Some applications are inherently distributed. For example, the web is a distributed system you are very familiar with. You access it with a browser, which runs on your phone, tablet, desktop, or Xbox. Together with other billions of devices worldwide, it forms a distributed system.</p>

<p>Another reason for building distributed systems is that some applications require high availability and need to be resilient to single-node failures. For example, Dropbox replicates your data across multiple nodes so that the loss of a single one doesn’t cause your data to be lost.</p>

<div class="source-page" id="source-page-20"></div>

<p>Some applications need to tackle workloads that are just too big to fit on a single node, no matter how powerful. For example, Google receives tens of thousands of search requests per second from all over the globe. There is no way a single node could handle that.</p>

<p>And finally, some applications have performance requirements that would be physically impossible to achieve with a single node. Netflix can seamlessly stream movies to your TV at high resolution because it has a data center close to you.</p>

<p>This book tackles the fundamental challenges that need to be solved to design, build, and operate distributed systems.</p>

<h3 id="section-1-1-communication"><strong>1.1</strong> <strong>Communication</strong></h3>

<p>The first challenge derives from the need for nodes to communicate with each other over the network. For example, when your browser wants to load a website, it resolves the server’s IP address from the URL and sends an HTTP request to it. In turn, the server returns a response with the page’s content.</p>

<p>How are the request and response messages represented on the wire? What happens when there is a temporary network outage, or some faulty network switch flips a few bits in the messages? How does the server guarantee that no intermediary can snoop on the communication?</p>

<p>Although it would be convenient to assume that some networking library is going to abstract all communication concerns away, in practice, it’s not that simple because abstractions leak<sup>1</sup>, and you need to understand how the network stack works when that happens.</p>

<p class="source-footnote">1“The Law of Leaky Abstractions,” <a href="https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/">https://www.joelonsoftware.com/2002/</a> <a href="https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/">11/11/the-law-of-leaky-abstractions/</a></p>

<div class="source-page" id="source-page-21"></div>

<h3 id="section-1-2-coordination"><strong>1.2</strong> <strong>Coordination</strong></h3>

<p>Another hard challenge of building distributed systems is that some form of coordination is required to make individual nodes work in unison towards a shared objective. This is particularly challenging to do in the presence of failures. The “two generals” problem is a famous thought experiment that showcases this.</p>

<p>Suppose two generals (nodes), each commanding their own army, need to agree on a time to jointly attack a city. There is some distance between the armies (network), and the only way to communicate is via messengers, who can be captured by the enemy (network failure). Under these assumptions, is there a way for the generals to agree on a time?</p>

<p>Well, general 1 could send a message with a proposed time to general 2. But since the messenger could be captured, general 1 wouldn’t know whether the message was actually delivered. You could argue that general 2 could send a messenger with a response to confirm it received the original message. However, just like before, general 2 wouldn’t know whether the response was actually delivered and another confirmation would be required. As it turns out, no matter how many rounds of confirmation are made, neither general can be certain that the other army will attack the city at the same time. As you can see, this problem is much harder to solve than it originally appeared.</p>

<p>Because coordination is such a key topic, the second part of the book is dedicated to understanding the fundamental distributed algorithms used to implement it.</p>

<h3 id="section-1-3-scalability"><strong>1.3</strong> <strong>Scalability</strong></h3>

<p>The performance of an application represents how efficiently it can handle<em> </em><em>load</em>. Intuitively, load is anything that consumes the system’s resources such as CPU, memory, and network bandwidth. Since the nature of load depends on the application’s use cases and architecture, there are different ways to measure it. For example,</p>

<div class="source-page" id="source-page-22"></div>

<p>the number of concurrent users or the ratio of writes to reads are different forms of load.</p>

<p>For the type of applications discussed in this book, performance is generally measured in terms of throughput and response time. <em>Throughput</em> is the number of requests processed per second by</p>

<p>the application, while<em> response time</em> is the time elapsed in seconds between sending a request to the application and receiving a response.</p>

<p>As load increases, the application will eventually reach its<em> </em><em>capac</em><em>ity</em>, i.e., the maximum load it can withstand, when a resource is exhausted. The performance either plateaus or worsens at that point, as shown in Figure 1.1. If the load on the system continues to grow, it will eventually hit a point where most operations fail or time out.</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-001.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-001.png" alt="Figure 1.1: The system throughput on the y axis is the subset of client requests (x axis) that can be handled without errors and with low response times, also referred to as its goodput." width="1138" height="957" loading="lazy"></a></figure>

<p class="source-caption">Figure 1.1: The system throughput on the y axis is the subset of client requests (x axis) that can be handled without errors and with low response times, also referred to as its goodput.</p>

<div class="source-page" id="source-page-23"></div>

<p>The capacity of a distributed system depends on its architecture, its implementation, and an intricate web of physical limitations like the nodes’ memory size and clock cycle and the bandwidth and latency of network links. For an application to be scalable, a load increase should not degrade the application’s performance. This requires increasing the capacity of the application at will.</p>

<p>A quick and easy way is to buy more expensive hardware with better performance, which is also referred to as<em> scaling up</em>. Unfortunately, this approach is bound to hit a brick wall sooner or later when such hardware just doesn’t exist. The alternative is<em> </em><em>scaling</em> <em>out</em> by adding more commodity machines to the system and having them work together.</p>

<p>Although procuring additional machines at will may have been daunting a few decades ago, the rise of cloud providers has made that trivial. In 2006 Amazon launched Amazon Web Services (AWS), which included the ability to rent virtual machines with its Elastic Compute Cloud (EC2<sup>2</sup>) service. Since then, the number of cloud providers and cloud services has only grown, democratizing the ability to create scalable applications.</p>

<p>In Part III of this book, we will explore the core architectural patterns and building blocks of scalable cloud-native applications.</p>

<h3 id="section-1-4-resiliency"><strong>1.4</strong> <strong>Resiliency</strong></h3>

<p>A distributed system is resilient when it can continue to do its job even when failures happen. And at scale, anything that can go wrong will go wrong. Every component has a probability of failing — nodes can crash, network links can be severed, etc. No matter</p>

<p>how small that probability is, the more components there are and the more operations the system performs, the higher the number of failures will be. And it gets worse because a failure of one component can increase the probability that another one will fail if the components are not well isolated.</p>

<p class="source-footnote">2“Amazon EC2,”<a href="https://aws.amazon.com/ec2/"> https://aws.amazon.com/ec2/</a></p>

<div class="source-page" id="source-page-24"></div>

<p>Failures that are left unchecked can impact the system’s<em> </em><em>availabil</em><em>ity</em><sup>3</sup>, i.e., the percentage of time the system is available for use. It’s a ratio defined as the amount of time the application can serve requests (<em>uptime</em>) divided by the total time measured (<em>uptime</em> plus <em>downtime</em>, i.e., the time the application can’t serve requests).</p>

<p>Availability is often described with nines, a shorthand way of expressing percentages of availability. Three nines are typically considered acceptable by users, and anything above four is considered to be highly available.</p>

<table><thead><tr><th>Availability%</th><th>Downtimeperday</th></tr></thead><tbody><tr><td>90%(“onenine”)</td><td>240h
ours
.</td></tr><tr><td>99%(“twonines”)</td><td>1440minutes
.</td></tr><tr><td>999%(“th reenines”)
.</td><td>144minutes
.</td></tr><tr><td>9999%(“fournines”)
.</td><td>864seconds
.</td></tr><tr><td>99999%(“fivenines”)
.</td><td>864milliseconds</td></tr></tbody></table>

<p>If the system isn’t resilient to failures, its availability will inevitably drop. Because of that, a distributed system needs to embrace failures and be prepared to withstand them using techniques such as redundancy, fault isolation, and self-healing mechanisms, which we will discuss in Part IV,<em> Resiliency</em>.</p>

<h3 id="section-1-5-maintainability"><strong>1.5</strong> <strong>Maintainability</strong></h3>

<p>It’s a well-known fact that the majority of the cost of software is spent after its initial development in maintenance activities, such as fixing bugs, adding new features, and operating it. Thus, we should aspire to make our systems easy to modify, extend and operate so that they are easy to maintain.</p>

<p>Any change is a potential incident waiting to happen. Good testing — in the form of unit, integration, and end-to-end tests — is a</p>

<p class="source-footnote">3“AWS Well-Architected Framework, Availability,”<a href="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html"> https://docs.aws.amazon.</a> <a href="https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html">com/wellarchitected/latest/reliability-pillar/availability.html</a></p>

<div class="source-page" id="source-page-25"></div>

<p>minimum requirement to modify or extend a system without worrying it will break. And once a change has been merged into the codebase, it needs to be released to production safely without affecting the system’s availability.</p>

<p>Also, operators need to monitor the system’s health, investigate degradations and restore the service when it can’t self-heal. This requires altering the system’s behavior without code changes, e.g., toggling a feature flag or scaling out a service with a configuration change.</p>

<p>Historically, developers, testers, and operators were part of different teams, but the rise of microservices and DevOps has changed that. Nowadays, the same team that designs and implements a system is also responsible for testing and operating it. That’s a good thing since there is no better way to discover where a system falls short than being on call for it. Part V will explore best practices for testing and operating distributed systems.</p>

<h3 id="section-1-6-anatomy-of-a-distributed-system"><strong>1.6</strong> <strong>Anatomy of a distributed system</strong></h3>

<p>Distributed systems come in all shapes and sizes. In this book, we are mainly concerned with backend applications that run on commodity machines and implement some kind of business service. So you could say a distributed system is a group of machines that communicate over network links. However, from a run-time point of view, a distributed system is a group of software processes that communicate via<em> </em><em>inter-process</em><em> </em><em>communication</em> (IPC) mechanisms like HTTP. And from an implementation perspective, a distributed system is a group of loosely-coupled components (services) that communicate via APIs. All these are valid and useful architectural points of view. In the rest of the book, we will switch between them depending on which one is more appropriate to discuss a particular topic.</p>

<p>A<em> </em><em>service</em> implements one specific part of the overall system’s capabilities. At the core of a service sits the business logic, which exposes interfaces to communicate with the outside world. Some</p>

<div class="source-page" id="source-page-26"></div>

<p>interfaces define the operations that the service offers to its users. In contrast, others define the operations that the service can invoke on other services, like data stores, message brokers, etc.</p>

<p>Since processes can’t call each other’s interfaces directly,<em> </em><em>adapters</em> are needed to connect IPC mechanisms to service interfaces. An inbound adapter is part of the service’s<em> </em><em>Application</em><em> </em><em>Programming</em> <em>Interface</em> (API); it handles the requests received from an IPC mechanism, like HTTP, by invoking operations defined in the service interfaces. In contrast, outbound adapters grant the business logic access to external services, like data stores. This architectural style is also referred to as the ports and adapters architecture<sup>4</sup>. The idea is that the business logic doesn’t depend on technical details; instead, the technical details depend on the business logic (dependency inversion principle<sup>5</sup>). This concept is illustrated in Figure 1.2.</p>

<p>Going forward, we will refer to a process running a service as a <em>server</em>, and a process sending requests to a server as a<em> client</em>. Sometimes, a process will be both a client and a server. For simplicity, we will assume that an individual instance of a service runs entirely within a single server process. Similarly, we will also assume that a process has a single thread. These assumptions will allow us to neglect some implementation details that would only complicate the discussion without adding much value.</p>

<p class="source-footnote">4“Ports And Adapters Architecture,”<a href="http://wiki.c2.com/?PortsAndAdaptersArchitecture"> http://wiki.c2.com/?PortsAndAdapter</a> <a href="http://wiki.c2.com/?PortsAndAdaptersArchitecture">sArchitecture</a></p>

<p class="source-footnote"><a href="http://wiki.c2.com/?PortsAndAdaptersArchitecture">5</a>“Dependency inversion principle,”<a href="https://en.wikipedia.org/wiki/Dependency_inversion_principle"> https://en.wikipedia.org/wiki/Depend</a> <a href="https://en.wikipedia.org/wiki/Dependency_inversion_principle">ency_inversion_principle</a></p>

<div class="source-page" id="source-page-27"></div>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-002.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-002.png" alt="Figure 1.2: In this example, the business logic uses the reposi- tory interface, implemented by the PostgreSQL adapter, to access the database. In contrast, the HTTP adapter handles incoming re- quests by calling operations defined in the service interface." width="2118" height="1627" loading="lazy"></a></figure>

<p class="source-caption">Figure 1.2: In this example, the business logic uses the repository interface, implemented by the PostgreSQL adapter, to access the database. In contrast, the HTTP adapter handles incoming requests by calling operations defined in the service interface.</p>
