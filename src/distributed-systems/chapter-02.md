# Communication

## Overview: Communication

<section class="chapter-video" aria-label="Video for Overview: Communication"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>Overview: Communication</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-29"></div>

<div class="source-page" id="source-page-31"></div>

<p><em>“The network is reliable.”</em></p>

<p>– Fallacies of distributed computing, L. Peter Deutsch</p>

<p>Communication between processes over the network, or<em> </em><em>inter</em><em>process</em><em> </em><em>communication</em> (IPC), is at the heart of distributed systems — it’s what makes distributed systems distributed. In order for</p>

<p>processes to communicate, they need to agree on a set of rules that determine how data is processed and formatted. Network protocols specify such rules.</p>

<p>The protocols are arranged in a stack<sup>6</sup>, where each layer builds on the abstraction provided by the layer below, and lower layers are closer to the hardware. When a process sends data to another through the network stack, the data moves from the top layer to the bottom one and vice-versa at the other end, as shown in Figure 1.3:</p>

<ul><li>The<em> link layer</em> consists of network protocols that operate on local network links, like Ethernet or Wi-Fi, and provides an interface to the underlying network hardware. Switches operate at this layer and forward Ethernet packets based on their destination MAC address<sup>7</sup>.</li><li>The<em> internet layer</em> routes packets from one machine to another across the network. The Internet Protocol (IP) is the core protocol of this layer, which delivers packets on a best-effort ba-</li></ul>

<p class="source-footnote">6“Internet protocol suite,”<a href="https://en.wikipedia.org/wiki/Internet_protocol_suite"> https://en.wikipedia.org/wiki/Internet_protocol_s</a> <a href="https://en.wikipedia.org/wiki/Internet_protocol_suite">uite</a></p>

<p class="source-footnote"><a href="https://en.wikipedia.org/wiki/Internet_protocol_suite">7</a>“MAC address,”<a href="https://en.wikipedia.org/wiki/MAC_address"> https://en.wikipedia.org/wiki/MAC_address</a></p>

<div class="source-page" id="source-page-32"></div>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-003.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-003.png" alt="Figure 1.3: Internet protocol suite" width="3072" height="1480" loading="lazy"></a></figure>

<p class="source-caption">Figure 1.3: Internet protocol suite</p>

<p>sis (i.e., packets can be dropped, duplicated, or corrupted). Routers operate at this layer and forward IP packets to the next router along the path to their final destination. • The<em> transport layer</em> transmits data between two processes. To enable multiple processes hosted on the same machine to communicate at the same time, port numbers are used to ad-dress the processes on either end. The most important protocol in this layer is the Transmission Control Protocol (TCP), which creates a reliable communication channel on top of IP. • Finally, the<em> </em><em>application</em><em> </em><em>layer</em> defines high-level communication protocols, like HTTP or DNS. Typically your applications will target this level of abstraction.</p>

<p>Even though each protocol builds on top of another, sometimes the abstractions leak. If you don’t have a good grasp of how the lower layers work, you will have a hard time troubleshooting network-ing issues that will inevitably arise. More importantly, having an appreciation of the complexity of what happens when you make a network call will make you a better systems builder.</p>

<p>Chapter 2 describes how to build a reliable communication channel (TCP) on top of an unreliable one (IP), which can drop or duplicate data or deliver it out of order. Building reliable abstractions on top of unreliable ones is a common pattern we will encounter again in the rest of the book.</p>

<div class="source-page" id="source-page-33"></div>

<p>Chapter 3 describes how to build a secure channel (TLS) on top of a reliable one (TCP). Security is a core concern of any system, and in this chapter, we will get a taste of what it takes to secure a network connection from prying eyes and malicious agents.</p>

<p>Chapter 4 dives into how the phone book of the internet (DNS) works, which allows nodes to discover others using names. At its heart, DNS is a distributed, hierarchical, and eventually consistent key-value store. By studying it, we will get the first taste of eventual consistency<sup>8</sup><sup> </sup>and the challenges it introduces.</p>

<p>Chapter 5 concludes this part by discussing how loosely coupled services communicate with each other through APIs by describing the implementation of a RESTful HTTP API built upon the protocols introduced earlier.</p>

<p class="source-footnote">8We will learn more about consistency models in chapter 10.</p>

## Reliable links

<section class="chapter-video" aria-label="Video for Reliable links"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>Reliable links</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-35"></div>

<p>At the internet layer, the communication between two nodes happens by routing packets to their destination from one router to the next. Two ingredients are required for this: a way to address nodes and a mechanism to route packets across routers.</p>

<p>Addressing is handled by the IP protocol. For example, IPv6 provides a 128-bit address space, allowing 2<sup>128</sup><sup> </sup>addresses. To decide where to send a packet, a router needs to consult a local routing table. The table maps a destination address to the address of the next router along the path to that destination. The responsibility of building and communicating the routing tables across routers lies with the Border Gateway Protocol (BGP<sup>1</sup>).</p>

<p>Now, IP doesn’t guarantee that data sent over the internet will arrive at its destination. For example, if a router becomes overloaded, it might start dropping packets. This is where TCP<sup>2</sup><sup> </sup>comes in, a transport-layer protocol that exposes a reliable communication channel between two processes on top of IP. TCP guarantees that a stream of bytes arrives in order without gaps, duplication, or corruption. TCP also implements a set of stability patterns to</p>

<p class="source-footnote">1“RFC 4271: A Border Gateway Protocol 4 (BGP-4),”<a href="https://datatracker.ietf.org/doc/html/rfc4271"> https://datatracker.ietf.o</a> <a href="https://datatracker.ietf.org/doc/html/rfc4271">rg/doc/html/rfc4271</a></p>

<p class="source-footnote"><a href="https://datatracker.ietf.org/doc/html/rfc4271">2</a>“RFC 793: Transmission Control Protocol,”<a href="https://tools.ietf.org/html/rfc793"> https://tools.ietf.org/html/rfc793</a></p>

<div class="source-page" id="source-page-36"></div>

<p>avoid overwhelming the network and the receiver.</p>

<h3 id="section-2-1-reliability"><strong>2.1</strong> <strong>Reliability</strong></h3>

<p>To create the illusion of a reliable channel, TCP partitions a byte stream into discrete packets called segments. The segments are sequentially numbered, which allows the receiver to detect holes and duplicates. Every segment sent needs to be acknowledged by the receiver. When that doesn’t happen, a timer fires on the sending side and the segment is retransmitted. To ensure that the data hasn’t been corrupted in transit, the receiver uses a checksum to verify the integrity of a delivered segment.</p>

<h3 id="section-2-2-connection-lifecycle"><strong>2.2</strong> <strong>Connection lifecycle</strong></h3>

<p>A connection needs to be opened before any data can be transmitted on a TCP channel. The operating system manages the connection state on both ends through a<em> socket</em>. The socket keeps track of the state changes of the connection during its lifetime. At a high level, there are three states the connection can be in:</p>

<ul><li>The opening state in which the connection is being created.</li><li>The established state in which the connection is open and data is being transferred.</li><li>The closing state in which the connection is being closed.</li></ul>

<p>In reality, this is a simplification, as there are more states<sup>3</sup><sup> </sup>than the three above.</p>

<p>A server must be listening for connection requests from clients before a connection is established. TCP uses a three-way handshake to create a new connection, as shown in Figure 2.1:</p>

<p>1. The sender picks a random sequence number<em> x</em> and sends a SYN segment to the receiver.</p>

<p class="source-footnote">3“TCP State Diagram,”<a href="https://en.wikipedia.org/wiki/Transmission_Control_Protocol#/media/File:Tcp_state_diagram_fixed_new.svg"> https://en.wikipedia.org/wiki/Transmission_Control</a> <a href="https://en.wikipedia.org/wiki/Transmission_Control_Protocol#/media/File:Tcp_state_diagram_fixed_new.svg">_Protocol#/media/File:Tcp_state_diagram_fixed_new.svg</a></p>

<div class="source-page" id="source-page-37"></div>

<p>2. The receiver increments<em> x</em>, chooses a random sequence number<em> y</em>, and sends back a SYN/ACK segment. 3. The sender increments both sequence numbers and replies with an ACK segment and the first bytes of application data.</p>

<p>The sequence numbers are used by TCP to ensure the data is delivered in order and without holes.</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-004.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-004.png" alt="Figure 2.1: Three-way handshake" width="1672" height="1235" loading="lazy"></a></figure>

<p class="source-caption">Figure 2.1: Three-way handshake</p>

<p>The handshake introduces a full round-trip in which no application data is sent. So until the connection has been opened, the bandwidth is essentially zero. The lower the round trip time is, the faster the connection can be established. Therefore, putting servers closer to the clients helps reduce this cold-start penalty.</p>

<p>After the data transmission is complete, the connection needs to be closed to release all resources on both ends. This termination phase involves multiple round-trips. If it’s likely that another transmission will occur soon, it makes sense to keep the connection open to avoid paying the cold-start tax again.</p>

<p>Moreover, closing a socket doesn’t dispose of it immediately as it</p>

<div class="source-page" id="source-page-38"></div>

<p>transitions to a waiting state (<em>TIME_WAIT</em>) that lasts several minutes and discards any segments received during the wait. The wait prevents delayed segments from a closed connection from being considered part of a new connection. But if many connections open and close quickly, the number of sockets in the waiting state will continue to increase until it reaches the maximum number of sockets that can be open, causing new connection attempts to fail. This is another reason why processes typically maintain connection pools to avoid recreating connections repeatedly.</p>

<h3 id="section-2-3-flow-control"><strong>2.3</strong> <strong>Flow control</strong></h3>

<p>Flow control is a backoff mechanism that TCP implements to prevent the sender from overwhelming the receiver. The receiver stores incoming TCP segments waiting to be processed by the application into a receive buffer, as shown in Figure 2.2.</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-005.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-005.png" alt="Figure 2.2: The receive buffer stores data that hasn’t yet been pro- cessed by the destination process." width="1956" height="1289" loading="lazy"></a></figure>

<p class="source-caption">Figure 2.2: The receive buffer stores data that hasn’t yet been processed by the destination process.</p>

<p>The receiver also communicates the size of the buffer to the sender whenever it acknowledges a segment, as shown in Figure 2.3.</p>

<div class="source-page" id="source-page-39"></div>

<p>Assuming it’s respecting the protocol, the sender avoids sending more data than can fit in the receiver’s buffer.</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-006.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-006.png" alt="Figure 2.3: The size of the receive buffer is communicated in the headers of acknowledgment segments." width="1672" height="1234" loading="lazy"></a></figure>

<p class="source-caption">Figure 2.3: The size of the receive buffer is communicated in the headers of acknowledgment segments.</p>

<p>This mechanism is not too dissimilar to rate-limiting at the service level, a mechanism that rejects a request when a specific quota is exceeded (see section 28.3). But, rather than rate-limiting on an API key or IP address, TCP is rate-limiting on a connection level.</p>

<h3 id="section-2-4-congestion-control"><strong>2.4</strong> <strong>Congestion control</strong></h3>

<p>TCP guards not only against overwhelming the receiver, but also against flooding the underlying network. The sender maintains a so-called<em> </em><em>congestion</em><em> </em><em>window</em>, which represents the total number of outstanding segments that can be sent without an acknowledgment from the other side. The smaller the congestion window is, the fewer bytes can be in flight at any given time, and the less bandwidth is utilized.</p>

<div class="source-page" id="source-page-40"></div>

<p>When a new connection is established, the size of the congestion window is set to a system default. Then, for every segment acknowledged, the window increases its size exponentially until it reaches an upper limit. This means we can’t use the network’s full capacity right after a connection is established. The shorter the round-trip time (RTT), the quicker the sender can start utilizing the underlying network’s bandwidth, as shown in Figure 2.4.</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-007.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-007.png" alt="Figure 2.4: The shorter the RTT, the quicker the sender can start utilizing the underlying network’s bandwidth." width="1624" height="1187" loading="lazy"></a></figure>

<p class="source-caption">Figure 2.4: The shorter the RTT, the quicker the sender can start utilizing the underlying network’s bandwidth.</p>

<p>What happens if a segment is lost? When the sender detects a missed acknowledgment through a timeout, a mechanism called <em>congestion</em><em> </em><em>avoidance</em> kicks in, and the congestion window size is reduced. From there onwards, the passing of time increases the window size<sup>4</sup><sup> </sup>by a certain amount, and timeouts decrease it by another.</p>

<p>As mentioned earlier, the size of the congestion window defines the maximum number of bytes that can be sent without receiving</p>

<p class="source-footnote">4“CUBIC: A New TCP-Friendly High-Speed TCP Variant,”<a href="https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.153.3152&amp;rep=rep1&amp;type=pdf"> https://citeseerx.is</a> <a href="https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.153.3152&amp;rep=rep1&amp;type=pdf">t.psu.edu/viewdoc/download?doi=10.1.1.153.3152&amp;rep=rep1&amp;type=pdf</a></p>

<div class="source-page" id="source-page-41"></div>

<p>an acknowledgment. Because the sender needs to wait for a full round trip to get an acknowledgment, we can derive the maximum theoretical bandwidth by dividing the size of the congestion window by the round trip time:</p>

<p>Bandwidth = <sup>WinSize</sup></p>

<p>RTT</p>

<p>The equation<sup>5</sup><sup> </sup>shows that bandwidth is a function of latency. TCP will try very hard to optimize the window size since it can’t do anything about the round-trip time. However, that doesn’t always yield the optimal configuration. Due to the way congestion control works, the shorter the round-trip time, the better the underlying network’s bandwidth is utilized. This is more reason to put servers geographically close to the clients.</p>

<h3 id="section-2-5-custom-protocols"><strong>2.5</strong> <strong>Custom protocols</strong></h3>

<p>TCP’s reliability and stability come at the price of lower bandwidth and higher latencies than the underlying network can deliver. If we drop the stability and reliability mechanisms that TCP provides, what we get is a simple protocol named<em> </em><em>User</em> <em>Datagram</em><em> </em><em>Protocol</em><sup>6</sup><sup> </sup>(UDP) — a connectionless transport layer protocol that can be used as an alternative to TCP.</p>

<p>Unlike TCP, UDP does not expose the abstraction of a byte stream to its clients. As a result, clients can only send discrete packets with a limited size called<em> </em><em>datagrams</em>. UDP doesn’t offer any reliability as datagrams don’t have sequence numbers and are not acknowledged. UDP doesn’t implement flow and congestion control either. Overall, UDP is a lean and bare-bones protocol. It’s used to bootstrap custom protocols, which provide some, but not all, of the stability and reliability guarantees that TCP does<sup>7</sup>.</p>

<p class="source-footnote">5“Bandwidth-delay product,” <a href="https://en.wikipedia.org/wiki/Bandwidth-delay_product">https://en.wikipedia.org/wiki/Bandwidth-</a> <a href="https://en.wikipedia.org/wiki/Bandwidth-delay_product">delay_product</a></p>

<p class="source-footnote"><a href="https://en.wikipedia.org/wiki/Bandwidth-delay_product">6</a>“RFC 768: User Datagram Protocol,”<a href="https://datatracker.ietf.org/doc/html/rfc768"> https://datatracker.ietf.org/doc/html/</a> <a href="https://datatracker.ietf.org/doc/html/rfc768">rfc768</a></p>

<p class="source-footnote"><a href="https://datatracker.ietf.org/doc/html/rfc768">7</a>As we will later see, HTTP 3 is based on UDP to avoid some of TCP’s short-comings.</p>

<div class="source-page" id="source-page-42"></div>

<p>For example, in multiplayer games, clients sample gamepad events several times per second and send them to a server that keeps track of the global game state. Similarly, the server samples the game state several times per second and sends these snapshots back to the clients. If a snapshot is lost in transmission, there is no value in retransmitting it as the game evolves in real-time; by the time the retransmitted snapshot would get to the destination, it would be obsolete. This is a use case where UDP shines; in contrast, TCP would attempt to redeliver the missing data and degrade the game’s experience.</p>

## Secure links

<section class="chapter-video" aria-label="Video for Secure links"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>Secure links</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-43"></div>

<p>We now know how to reliably send bytes from one process to another over the network. The problem is that these bytes are sent in the clear, and a middleman could intercept the communication. To protect against that, we can use the<em> Transport Layer Security</em><sup>1</sup><sup> </sup>(TLS) protocol. TLS runs on top of TCP and encrypts the communication channel so that application layer protocols, like HTTP, can leverage it to communicate securely. In a nutshell, TLS provides <em>encryption</em>,<em> authentication</em>, and<em> integrity</em>.</p>

<h3 id="section-3-1-encryption"><strong>3.1</strong> <strong>Encryption</strong></h3>

<p>Encryption guarantees that the data transmitted between a client and a server is obfuscated and can only be read by the communicating processes.</p>

<p>When the TLS connection is first opened, the client and the server negotiate a shared encryption secret using<em> </em><em>asymmetric</em><em> </em><em>encryption</em>. First, each party generates a key pair consisting of a private and public key. The processes can then create a shared secret by exchanging their public keys. This is possible thanks to some math-</p>

<p class="source-footnote">1“RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3,” <a href="https://datatracker.ietf.org/doc/html/rfc8446">https:</a> <a href="https://datatracker.ietf.org/doc/html/rfc8446">//datatracker.ietf.org/doc/html/rfc8446</a></p>

<div class="source-page" id="source-page-44"></div>

<p>ematical properties<sup>2</sup><sup> </sup>of the key pairs. The beauty of this approach is that the shared secret is never communicated over the wire.</p>

<p>Although asymmetric encryption is slow and expensive, it’s only used to create the shared encryption key. After that,<em> symmetric en</em><em>cryption</em> is used, which is fast and cheap. The shared key is periodically renegotiated to minimize the amount of data that can be deciphered if the shared key is broken.</p>

<p>Encrypting in-flight data has a CPU penalty, but it’s negligible since modern processors have dedicated cryptographic instructions. Therefore, TLS should be used for all communications, even those not going through the public internet.</p>

<h3 id="section-3-2-authentication"><strong>3.2</strong> <strong>Authentication</strong></h3>

<p>Although we have a way to obfuscate data transmitted across the wire, the client still needs to authenticate the server to verify it’s who it claims to be. Similarly, the server might want to authenticate the identity of the client.</p>

<p>TLS implements authentication using digital signatures based on asymmetric cryptography. The server generates a key pair with a private and a public key and shares its public key with the client. When the server sends a message to the client, it signs it with its private key. The client uses the server’s public key to verify that the digital signature was actually signed with the private key. This is possible thanks to mathematical properties<sup>3</sup><sup> </sup>of the key pair.</p>

<p>The problem with this approach is that the client has no idea whether the public key shared by the server is authentic. Hence, the protocol uses certificates to prove the ownership of a public key. A certificate includes information about the owning entity, expiration date, public key, and a digital signature of the thirdparty entity that issued the certificate. The certificate’s issuing</p>

<p class="source-footnote">2“A (Relatively Easy To Understand) Primer on Elliptic Curve Cryptography,” <a href="https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/">https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-</a> <a href="https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/">curve-cryptography/</a></p>

<p class="source-footnote"><a href="https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/">3</a>“Digital signature,”<a href="https://en.wikipedia.org/wiki/Digital_signature"> https://en.wikipedia.org/wiki/Digital_signature</a></p>

<div class="source-page" id="source-page-45"></div>

<p>entity is called a<em> certificate authority</em> (CA), which is also represented with a certificate. This creates a chain of certificates that ends with a certificate issued by a root CA, as shown in Figure 3.1, which self-signs its certificate.</p>

<p>For a TLS certificate to be trusted by a device, the certificate, or one of its ancestors, must be present in the trusted store of the client. Trusted root CAs, such as Let’s Encrypt<sup>4</sup>, are typically included in the client’s trusted store by default by the operating system vendor.</p>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-008.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-008.png" alt="Figure 3.1: A certificate chain ends with a self-signed certificate issued by a root CA." width="760" height="1788" loading="lazy"></a></figure>

<p class="source-caption">Figure 3.1: A certificate chain ends with a self-signed certificate issued by a root CA.</p>

<p>When a TLS connection is opened, the server sends the full certificate chain to the client, starting with the server’s certificate and</p>

<p class="source-footnote">4“Let’s Encrypt: A nonprofit Certificate Authority,”<a href="https://letsencrypt.org/"> https://letsencrypt.org/</a></p>

<div class="source-page" id="source-page-46"></div>

<p>ending with the root CA. The client verifies the server’s certificate by scanning the certificate chain until it finds a certificate that it trusts. Then, the certificates are verified in reverse order from that point in the chain. The verification checks several things, like the certificate’s expiration date and whether the digital signature was actually signed by the issuing CA. If the verification reaches the last certificate in the path (the server’s own certificate) without errors, the path is verified, and the server is authenticated.</p>

<p>One of the most common mistakes when using TLS is letting a certificate expire. When that happens, the client won’t be able to verify the server’s identity, and opening a connection to the remote process will fail. This can bring an entire application down as clients can no longer connect with it. For this reason, automation to monitor and auto-renew certificates close to expiration is well worth the investment.</p>

<h3 id="section-3-3-integrity"><strong>3.3</strong> <strong>Integrity</strong></h3>

<p>Even if the data is obfuscated, a middleman could still tamper with it; for example, random bits within the messages could be swapped. To protect against tampering, TLS verifies the integrity of the data by calculating a message digest. A secure hash function is used to create a message authentication code<sup>5</sup><sup> </sup>(HMAC). When a process receives a message, it recomputes the digest of the message and checks whether it matches the digest included in the message. If not, then the message has either been corrupted during transmission or has been tampered with. In this case, the message is dropped.</p>

<p>The TLS HMAC protects against data corruption as well, not just tampering. You might be wondering how data can be corrupted if TCP is supposed to guarantee its integrity. While TCP does use a checksum to protect against data corruption, it’s not 100% reliable<sup>6</sup>:</p>

<p class="source-footnote">5“RFC 2104: HMAC: Keyed-Hashing for Message Authentication,”<a href="https://datatracker.ietf.org/doc/html/rfc2104"> https://da</a> <a href="https://datatracker.ietf.org/doc/html/rfc2104">tatracker.ietf.org/doc/html/rfc2104</a></p>

<p class="source-footnote"><a href="https://datatracker.ietf.org/doc/html/rfc2104">6</a>“When the CRC and TCP checksum disagree,”<a href="https://dl.acm.org/doi/10.1145/347057.347561"> https://dl.acm.org/doi/10.11</a> <a href="https://dl.acm.org/doi/10.1145/347057.347561">45/347057.347561</a></p>

<div class="source-page" id="source-page-47"></div>

<p>it fails to detect errors for roughly 1 in 16 million to 10 billion packets. With packets of 1 KB, this is expected to happen once per 16 GB to 10 TB transmitted.</p>

<h3 id="section-3-4-handshake"><strong>3.4</strong> <strong>Handshake</strong></h3>

<p>When a new TLS connection is established, a handshake between the client and server occurs during which:</p>

<p>1. The parties agree on the cipher suite to use. A cipher suite specifies the different algorithms that the client and the server intend to use to create a secure channel, like the:</p>

<ul><li>key exchange algorithm used to generate shared secrets;</li><li>signature algorithm used to sign certificates;</li><li>symmetric encryption algorithm used to encrypt the application data;</li><li>HMAC algorithm used to guarantee the integrity and authenticity of the application data. 2. The parties use the key exchange algorithm to create a shared secret. The symmetric encryption algorithm uses the shared secret to encrypt communication on the secure channel going forward. 3. The client verifies the certificate provided by the server. The verification process confirms that the server is who it says it is. If the verification is successful, the client can start sending encrypted application data to the server. The server can optionally also verify the client certificate if one is available.</li></ul>

<p>These operations don’t necessarily happen in this order, as modern implementations use several optimizations to reduce round trips. For example, the handshake typically requires 2 round trips with TLS 1.2 and just one with TLS 1.3. The bottom line is that creating a new connection is not free: yet another reason to put your servers geographically closer to the clients and reuse connections when possible.</p>

## Discovery

<section class="chapter-video" aria-label="Video for Discovery"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>Discovery</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-49"></div>

<p>So far, we have explored how to create a reliable and secure channel between two processes running on different machines. However, to create a new connection with a remote process, we must first discover its IP address somehow. The most common way of doing that is via the phone book of the internet: the<em> Domain Name</em> <em>System</em><sup>1</sup><sup> </sup>(DNS) — a distributed, hierarchical, and eventually consistent key-value store.</p>

<p>In this chapter, we will look at how DNS resolution<sup>2</sup><sup> </sup>works in a browser, but the process is similar for other types of clients. When you enter a URL in your browser, the first step is to resolve the hostname’s IP address, which is then used to open a new TLS connection. For example, let’s take a look at how the DNS resolution works when you type<em> www.example.com</em> into your browser (see Figure 4.1).</p>

<p>1. The browser checks its local cache to see whether it has resolved the hostname before. If so, it returns the cached IP address; otherwise, it routes the request to a DNS resolver,</p>

<p class="source-footnote">1“RFC 1035: Domain Names - Implementation and Specification,” <a href="https://datatracker.ietf.org/doc/html/rfc1035">https://da</a> <a href="https://datatracker.ietf.org/doc/html/rfc1035">tatracker.ietf.org/doc/html/rfc1035</a></p>

<p class="source-footnote"><a href="https://datatracker.ietf.org/doc/html/rfc1035">2</a>“A deep dive into DNS,”<a href="https://www.youtube.com/watch?v=drWd9HIhJdU"> https://www.youtube.com/watch?v=drWd9HIhJ</a> <a href="https://www.youtube.com/watch?v=drWd9HIhJdU">dU</a></p>

<div class="source-page" id="source-page-50"></div>

<p>a server typically hosted by your Internet Service Provider (ISP).</p>

<p>2. The resolver is responsible for iteratively resolving the hostname for its clients. The reason why it’s iterative will become obvious in a moment. The resolver first checks its local cache for a cached entry, and if one is found, it’s returned to the client. If not, the query is sent to a root name server (root NS).</p>

<p>3. The root name server maps the<em> top-level domain</em> (TLD) of the request, i.e.,<em> .com</em>, to the address of the name server responsible for it.</p>

<p>4. The resolver sends a resolution request for<em> example.com</em> to the TLD name server.</p>

<p>5. The TLD name server maps the<em> example.com</em> domain name to the address of the<em> authoritative name server</em> responsible for the domain.</p>

<p>6. Finally, the resolver queries the authoritative name server for <em>www.example.com</em>, which returns the IP address of the<em> </em><em>www</em> hostname.</p>

<p>If the query included a subdomain of <em>example.com</em>, like <em>news.example.com</em>, the authoritative name server would have returned the address of the name server responsible for the subdomain, and an additional request would be required.</p>

<p>The original DNS protocol sent plain-text messages primarily over UDP for efficiency reasons. However, because this allows anyone monitoring the transmission to snoop, the industry has mostly moved to secure alternatives, such as DNS on top of TLS<sup>3</sup>.</p>

<p>The resolution process involves several round trips in the worst case, but its beauty is that the address of a root name server is all that’s needed to resolve a hostname. That said, the resolution would be slow if every request had to go through several name</p>

<p class="source-footnote">3“RFC 7858: Specification for DNS over Transport Layer Security (TLS),”<a href="https://en.wikipedia.org/wiki/DNS_over_TLS"> https:</a> <a href="https://en.wikipedia.org/wiki/DNS_over_TLS">//en.wikipedia.org/wiki/DNS_over_TLS</a></p>

<div class="source-page" id="source-page-51"></div>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-009.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-009.png" alt="Figure 4.1: DNS resolution process" width="2451" height="1773" loading="lazy"></a></figure>

<p class="source-caption">Figure 4.1: DNS resolution process</p>

<p>server lookups. Not only that, but think of the scale required for the name servers to handle the global resolution load. So caching is used to speed up the resolution process since the mapping of domain names to IP addresses doesn’t change often — the browser, operating system, and DNS resolver all use caches internally.</p>

<p>How do these caches know when to expire a record? Every DNS record has a<em> time to live</em> (TTL) that informs the cache how long the entry is valid for. But there is no guarantee that clients play nicely and enforce the TTL. So don’t be surprised when you change a DNS entry and find out that a small number of clients are still trying to connect to the old address long after the TTL has expired.</p>

<p>Setting a TTL requires making a tradeoff. If you use a long TTL, many clients won’t see a change for a long time. But if you set it too short, you increase the load on the name servers and the average response time of requests because clients will have to resolve the hostname more often.</p>

<p>If your name server becomes unavailable for any reason, then the</p>

<div class="source-page" id="source-page-52"></div>

<p>smaller the record’s TTL is, the higher the number of clients impacted will be. DNS can easily become a single point of failure — if your DNS name server is down and clients can’t find the IP ad-dress of your application, they won’t be able to connect it. This can lead to massive outages<sup>4</sup>.</p>

<p>This brings us to an interesting observation. DNS could be a lot more robust to failures if DNS caches would serve stale entries when they can’t reach a name server, rather than treating TTLs as time bombs. Since entries rarely change, serving a stale entry is arguably a lot more robust than not serving any entry at all. The principle that a system should continue to function even when a dependency is impaired is also referred to as “static stability”; we will talk more about it in the resiliency part of the book.</p>

<p class="source-footnote">4“DDoS attack on Dyn,”<a href="https://en.wikipedia.org/wiki/2016_Dyn_cyberattack"> https://en.wikipedia.org/wiki/2016_Dyn_cyberatta</a> <a href="https://en.wikipedia.org/wiki/2016_Dyn_cyberattack">ck</a></p>

## APIs

<section class="chapter-video" aria-label="Video for APIs"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">CHAPTER VIDEO</span><strong>APIs</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<div class="source-page" id="source-page-53"></div>

<p>Now that we know how a client can discover the IP address of a server and create a reliable and secure communication link with it, we want the client to invoke operations offered by the server. To that end, the server uses an adapter — which defines its application programming interface (API) — to translate messages received from the communication link to interface calls implemented by its business logic (see Figure 1.2).</p>

<p>The communication style between a client and a server can be<em> di</em><em>rect</em> or<em> indirect</em>, depending on whether the client communicates directly with the server or indirectly through a broker. Direct communication requires that both processes are up and running for the communication to succeed. However, sometimes this guarantee is either not needed or very hard to achieve, in which case indirect communication is a better fit. An example of indirect communication is<em> </em><em>messaging</em>. In this model, the sender and the receiver don’t communicate directly, but they exchange messages through a message channel (the broker). The sender sends messages to the channel, and on the other side, the receiver reads messages from it. Later in chapter 23, we will see how message channels are implemented and how to best use them.</p>

<p>In this chapter, we will focus our attention on a direct communi-</p>

<div class="source-page" id="source-page-54"></div>

<p>cation style called<em> request-response</em>, in which a client sends a<em> request</em> <em>message</em> to the server, and the server replies with a<em> response message</em>. This is similar to a function call but across process boundaries and over the network.</p>

<p>The request and response messages contain data that is serialized in a language-agnostic format. The choice of format determines a message’s serialization and deserialization speed, whether it’s human-readable, and how hard it is to evolve it over time. A<em> tex</em><em>tual</em> format like JSON<sup>1</sup><sup> </sup>is self-describing and human-readable, at the expense of increased verbosity and parsing overhead. On the other hand, a binary format like Protocol Buffers<sup>2</sup><sup> </sup>is leaner and more performant than a textual one at the expense of human read-ability.</p>

<p>When a client sends a request to a server, it can block and wait for the response to arrive, making the communication<em> synchronous</em>. Alternatively, it can ask the outbound adapter to invoke a callback when it receives the response, making the communication<em> </em><em>asyn</em><em>chronous</em>.</p>

<p>Synchronous communication is inefficient, as it blocks threads that could be used to do something else. Some languages, like JavaScript, C#, and Go, can completely hide callbacks through language primitives such as async/await<sup>3</sup>. These primitives make writing asynchronous code as straightforward as writing synchronous code.</p>

<p>Commonly used IPC technologies for request-response interactions are HTTP and gRPC<sup>4</sup>. Typically, internal APIs used for server-to-server communications within an organization are implemented with a high-performance RPC framework like gRPC. In contrast, external APIs available to the public tend to be based</p>

<p class="source-footnote">1“ECMA-404: The JSON data interchange syntax,”<a href="https://www.ecma-international.org/publications-and-standards/standards/ecma-404/"> https://www.ecma-intern</a> <a href="https://www.ecma-international.org/publications-and-standards/standards/ecma-404/">ational.org/publications-and-standards/standards/ecma-404/</a></p>

<p class="source-footnote"><a href="https://www.ecma-international.org/publications-and-standards/standards/ecma-404/">2</a>“Protocol Buffers: a language-neutral, platform-neutral extensible mechanism for serializing structured data,”<a href="https://developers.google.com/protocol-buffers"> https://developers.google.com/protocol-buffers</a></p>

<p class="source-footnote">3“Asynchronous programming with async and await,”<a href="https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/"> https://docs.microsoft</a> <a href="https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/">.com/en-us/dotnet/csharp/programming-guide/concepts/async/</a></p>

<p class="source-footnote"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/">4</a>“gRPC: A high performance, open source universal RPC framework,” <a href="https://grpc.io/">https:</a> <a href="https://grpc.io/">//grpc.io/</a></p>

<div class="source-page" id="source-page-55"></div>

<p>on HTTP, since web browsers can easily make HTTP requests via JavaScript code.</p>

<p>A popular set of design principles for designing elegant and scalable HTTP APIs is representational state transfer (REST<sup>5</sup>), and an API based on these principles is said to be RESTful. For example, these principles include that:</p>

<ul><li>requests are stateless, and therefore each request contains all the necessary information required to process it;</li><li>responses are implicitly or explicitly labeled as cacheable or non-cacheable. If a response is cacheable, the client can reuse the response for a later, equivalent request.</li></ul>

<p>Given the ubiquity of RESTful HTTP APIs, we will walk through the process of creating an HTTP API in the rest of the chapter.</p>

<h3 id="section-5-1-http"><strong>5.1</strong> <strong>HTTP</strong></h3>

<p><em>HTTP</em><sup>6</sup><sup> </sup>is a request-response protocol used to encode and transport information between a client and a server. In an<em> HTTP transaction</em>, the client sends a<em> request message</em> to the server’s API endpoint, and the server replies back with a<em> response message</em>, as shown in Figure 5.1.</p>

<p>In HTTP 1.1, a message is a textual block of data that contains a start line, a set of headers, and an optional body:</p>

<ul><li>In a request message, the<em> start line</em> indicates what the request is for, and in a response message, it indicates whether the request was successful or not.</li><li>The<em> headers</em> are key-value pairs with metadata that describes the message.</li><li>The message<em> body</em> is a container for data.</li></ul>

<p>HTTP is a stateless protocol, which means that everything needed by a server to process a request needs to be specified within the</p>

<p class="source-footnote">5“Representational State Transfer,”<a href="https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm"> https://www.ics.uci.edu/~fielding/pubs</a> <a href="https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm">/dissertation/rest_arch_style.htm</a></p>

<p class="source-footnote"><a href="https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm">6</a>“Hypertext Transfer Protocol,”<a href="https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol"> https://en.wikipedia.org/wiki/Hypertext_T</a> <a href="https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol">ransfer_Protocol</a></p>

<div class="source-page" id="source-page-56"></div>

<figure class="source-figure"><a href="../../assets/distributed-systems/figure-010.png" target="_blank" rel="noopener" aria-label="Open diagram at full resolution"><img src="../../assets/distributed-systems/figure-010.png" alt="Figure 5.1: An example HTTP transaction between a browser and a web server" width="1550" height="1549" loading="lazy"></a></figure>

<p class="source-caption">Figure 5.1: An example HTTP transaction between a browser and a web server</p>

<p>request itself, without context from previous requests. HTTP uses TCP for the reliability guarantees discussed in chapter 2. When it runs on top of TLS, it’s also referred to as HTTPS.</p>

<p>HTTP 1.1 keeps a connection to a server open by default to avoid needing to create a new one for the next transaction. However, a new request can’t be issued until the response to the previous one has been received (aka<em> </em><em>head-of-line</em><em> </em><em>blocking</em> or HOL blocking); in other words, the transactions have to be serialized. For example, a browser that needs to fetch several images to render an HTML page has to download them one at a time, which can be very inefficient.</p>

<p>Although HTTP 1.1 technically allows some type of requests to be</p>

<div class="source-page" id="source-page-57"></div>

<p>pipelined<sup>7</sup>, it still suffers from HOL blocking as a single slow response will block all the responses after it. With HTTP 1.1, the typical way to improve the throughput of outgoing requests is by creating multiple connections. However, this comes with a price because connections consume resources like memory and sockets.</p>

<p>HTTP 2<sup>8</sup><sup> </sup>was designed from the ground up to address the main limitations of HTTP 1.1. It uses a binary protocol rather than a textual one, allowing it to multiplex multiple concurrent requestresponse transactions (streams) on the same connection. In early 2020 about half of the most-visited websites on the internet were using the new HTTP 2 standard.</p>

<p>HTTP 3<sup>9</sup><sup> </sup>is the latest iteration of the HTTP standard, which is based on UDP and implements its own transport protocol to address some of TCP’s shortcomings<sup>10</sup>. For example, with HTTP 2, a packet loss over the TCP connection blocks all streams (HOL), but with HTTP 3 a packet loss interrupts only one stream, not all of them.</p>

<p>This book uses the HTTP 1.1 standard for illustration purposes since its plain text format is easier to display. Moreover, HTTP 1.1 is still widely used.</p>

<h3 id="section-5-2-resources"><strong>5.2</strong> <strong>Resources</strong></h3>

<p>Suppose we would like to implement a service to manage the product catalog of an e-commerce application. The service must allow customers to browse the catalog and administrators to create, update, or delete products. Although that sounds simple, in order to expose this service via HTTP, we first need to understand how to model APIs with HTTP.</p>

<p class="source-footnote">7“HTTP pipelining,”<a href="https://en.wikipedia.org/wiki/HTTP_pipelining"> https://en.wikipedia.org/wiki/HTTP_pipelining</a> 8“RFC 7540: Hypertext Transfer Protocol Version 2 (HTTP/2),”<a href="https://tools.ietf.org/html/rfc7540"> https://tools.ie</a> <a href="https://tools.ietf.org/html/rfc7540">tf.org/html/rfc7540</a></p>

<p class="source-footnote"><a href="https://tools.ietf.org/html/rfc7540">9</a>“HTTP/3 is next Generation HTTP. Is it QUIC enough?,”<a href="https://www.youtube.com/watch?v=rlN4F1oyaRM"> https://www.yout</a> <a href="https://www.youtube.com/watch?v=rlN4F1oyaRM">ube.com/watch?v=rlN4F1oyaRM</a></p>

<p class="source-footnote"><a href="https://www.youtube.com/watch?v=rlN4F1oyaRM">10</a>“Comparing HTTP/3 vs. HTTP/2 Performance,”<a href="https://blog.cloudflare.com/http-3-vs-http-2/"> </a><a href="https://blog.cloudflare.com/http-3-vs-http-2/">https://blog.cloudflare.co</a> <a href="https://blog.cloudflare.com/http-3-vs-http-2/">m/http-3-vs-http-2/</a></p>

<div class="source-page" id="source-page-58"></div>

<p>An HTTP server hosts resources, where a<em> </em><em>resource</em> can be a physical or abstract entity, like a document, an image, or a collection of other resources. A URL identifies a resource by describing its location on the server.</p>

<p>In our catalog service, the collection of products is a type of resource, which could be accessed with a URL like<a href="https://www.example.com/products?sort=price"><em> https://www.exam</em></a> <a href="https://www.example.com/products?sort=price"><em>ple.com/products?sort=price</em></a>, where:</p>

<ul><li><em> </em><em>https</em> is the protocol;</li><li><em> </em><em>www.example.com</em> is the hostname;</li><li><em> </em><em>products</em> is the name of the resource;</li><li><em> </em><em>?sort=price</em> is the query string, which contains additional parameters that affect how the service handles the request; in this case, the sort order of the list of products returned in the response.</li></ul>

<p>The URL without the query string is also referred to as the API’s <em>/products</em> endpoint.</p>

<p>URLs can also model relationships between resources. For example, since a product is a resource that belongs to the collection of products, the product with the unique identifier 42 could have the following relative URL:<em> </em><em>/products/42</em>. And if the product also has a list of reviews associated with it, we could append its resource name to the product’s URL, i.e.,<em> /products/42/reviews</em>. However, the API becomes more complex as the nesting of resources increases, so it’s a balancing act.</p>

<p>Naming resources is only one part of the equation; we also have to serialize the resources on the wire when they are transmitted in the body of request and response messages. When a client sends a request to get a resource, it adds specific headers to the message to describe the preferred representation for the resource. The server uses these headers to pick the most appropriate representation<sup>11</sup></p>

<p>for the response. Generally, in HTTP APIs, JSON is used to represent non-binary resources. For example, this is how the representation of<em> /products/42</em> might look:</p>

<p class="source-footnote">11“HTTP Content negotiation,” <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation">https://developer.mozilla.org/en-US/docs/</a> <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation">Web/HTTP/Content_negotiation</a></p>

<div class="source-page" id="source-page-59"></div>

<pre><code>{
  &quot;id&quot;: 42,
  &quot;category&quot;: &quot;Laptop&quot;,
  &quot;price&quot;: 999
}</code></pre>

<h3 id="section-5-3-request-methods"><strong>5.3</strong> <strong>Request methods</strong></h3>

<p>HTTP requests can create, read, update, and delete (CRUD) resources using request<em> methods</em>. When a client makes a request to a server for a particular resource, it specifies which method to use. You can think of a request method as the verb or action to use on a resource.</p>

<p>The most commonly used methods are<em> </em><em>POST</em>,<em> </em><em>GET</em>,<em> </em><em>PUT</em>, and <em>DELETE</em>. For example, the API of our catalog service could be defined as follows:</p>

<ul><li><em> </em><em>POST /products</em> — Create a new product and return the URL of the new resource.</li><li><em> </em><em>GET /products</em> — Retrieve a list of products. The query string can be used to filter, paginate, and sort the collection.</li><li><em> </em><em>GET /products/42</em> — Retrieve product 42.</li><li><em> </em><em>PUT /products/42</em> — Update product 42.</li><li><em> </em><em>DELETE /products/42</em> — Delete product 42.</li></ul>

<p>Request methods can be categorized based on whether they are safe and whether they are idempotent. A<em> safe</em> method should not have any visible side effects and can safely be cached. An<em> </em><em>idem</em><em>potent</em> method can be executed multiple times, and the end result should be the same as if it was executed just a single time. Idempotency is a crucial aspect of APIs, and we will talk more about it later in section 5.7.</p>

<table><thead><tr><th>Method</th><th>Safe</th><th>Idempotent</th></tr></thead><tbody><tr><td>POST</td><td>No</td><td>No</td></tr><tr><td>GET</td><td>Yes</td><td>Yes</td></tr><tr><td>PUT</td><td>No</td><td>Yes</td></tr></tbody></table>

<div class="source-page" id="source-page-60"></div>

<table><thead><tr><th>Method</th><th>Safe</th><th>Idempotent</th></tr></thead><tbody><tr><td>DELETE</td><td>No</td><td>Yes</td></tr></tbody></table>

<h3 id="section-5-4-response-status-codes"><strong>5.4</strong> <strong>Response status codes</strong></h3>

<p>After the server has received a request, it needs to process it and send a response back to the client. The HTTP response contains a <em>status code</em><sup>12</sup><sup> </sup>to communicate to the client whether the request succeeded or not. Different status code ranges have different meanings.</p>

<p>Status codes between 200 and 299 are used to communicate success. For example,<em> 200 (OK)</em> means that the request succeeded, and the body of the response contains the requested resource.</p>

<p>Status codes between 300 and 399 are used for redirection. For example,<em> 301 (Moved Permanently)</em> means that the requested resource has been moved to a different URL specified in the response message<em> Location</em> header.</p>

<p>Status codes between 400 and 499 are reserved for client errors. A request that fails with a client error will usually return the same error if it’s retried since the error is caused by an issue with the client, not the server. Because of that, it shouldn’t be retried. Some common client errors are:</p>

<ul><li><em> </em><em>400</em><em> </em><em>(Bad</em><em> </em><em>Request)</em> — Validating the client-side input has failed.</li><li><em> </em><em>401 (Unauthorized)</em> — The client isn’t authenticated.</li><li><em> </em><em>403 (Forbidden)</em> — The client is authenticated, but it’s not allowed to access the resource.</li><li><em> </em><em>404 (Not Found)</em> — The server couldn’t find the requested resource.</li></ul>

<p>Status codes between 500 and 599 are reserved for server errors. A request that fails with a server error can be retried as the issue that</p>

<p class="source-footnote">12“HTTP Status Codes,”<a href="https://httpstatuses.com/"> https://httpstatuses.com/</a></p>

<div class="source-page" id="source-page-61"></div>

<p>caused it to fail might be temporary. These are some typical server status codes:</p>

<ul><li><em> </em><em>500</em><em> </em><em>(Internal</em><em> </em><em>Server</em><em> </em><em>Error)</em> — The server encountered an unexpected error that prevented it from handling the request.</li><li><em> </em><em>502</em><em> </em><em>(Bad</em><em> </em><em>Gateway)</em> — The server, while acting as a gateway or proxy, received an invalid response from a downstream server it accessed while attempting to handle the request.<sup>13</sup></li></ul>

<ul><li><em> </em><em>503 (Service Unavailable)</em> — The server is currently unable to handle the request due to a temporary overload or scheduled maintenance.</li></ul>

<h3 id="section-5-5-openapi"><strong>5.5</strong> <strong>OpenAPI</strong></h3>

<p>Now that we understand how to model an API with HTTP, we can write an adapter that handles HTTP requests by calling the business logic of the catalog service. For example, suppose the service is defined by the following interface:</p>

<pre><code>interface CatalogService
{
  List&lt;Product&gt; GetProducts(...);
  Product GetProduct(...);
  void AddProduct(...);
  void DeleteProduct(...);
  void UpdateProduct(...)
}</code></pre>

<p>So when the HTTP adapter receives a<em> </em><em>GET</em><em> </em><em>/products</em> request to retrieve the list of all products, it will invoke the<em> </em><em>GetProducts(...)</em> method and convert the result into an HTTP response. Although this is a simple example, you can see how the adapter connects the IPC mechanism (HTTP) to the business logic.</p>

<p>We can generate a skeleton of the HTTP adapter by defining the</p>

<p class="source-footnote">13In this book, we will sometimes classify service dependencies as upstream or downstream depending on the direction of the dependency relationship. For example, if service A makes requests to service B, then service B is a downstream dependency of A, and A is an upstream dependency of B. Since there is no consensus in the industry for these terms, other texts might use a different convention.</p>

<div class="source-page" id="source-page-62"></div>

<p>API of the service with an<em> </em><em>interface</em><em> </em><em>definition</em><em> </em><em>language</em> (IDL). An IDL is a language-independent definition of the API that can be used to generate boilerplate code for the server-side adapter and client-side software development kits (SDKs) in your languages of choice.</p>

<p>The OpenAPI<sup>14</sup><sup> </sup>specification, which evolved from the Swagger project, is one of the most popular IDLs for RESTful HTTP APIs. With it, we can formally describe the API in a YAML document, including the available endpoints, supported request methods, and response status codes for each endpoint, and the schema of the resources’ JSON representation.</p>

<p>For example, this is how part of the<em> /products</em> endpoint of the catalog service’s API could be defined:</p>

<pre><code>openapi: 3.0.0
info:
  version: &quot;1.0.0&quot;
  title: Catalog Service API
paths:
  /products:
    get:
      summary: List products
      parameters:
        - in: query
          name: sort
          required: false
          schema:
            type: string
      responses:
        &quot;200&quot;:
          description: list of products in catalog
          content:
            application/json:
              schema:</code></pre>

<p class="source-footnote">14“OpenAPI Specification,”<a href="https://swagger.io/specification/"> https://swagger.io/specification/</a></p>

<div class="source-page" id="source-page-63"></div>

<pre><code>                type: array
                items:
                  $ref: &quot;#/components/schemas/ProductItem&quot;
        &quot;400&quot;:
          description: bad input
components:
  schemas:
    ProductItem:
      type: object
      required:
        - id
        - name
        - category
      properties:
        id:
          type: number
        name:
          type: string
        category:
          type: string</code></pre>

<p>Although this is a very simple example and we won’t go deeper into OpenAPI, it should give you an idea of its expressiveness. With this definition, we can then run a tool to generate the API’s documentation, boilerplate adapters, and client SDKs.</p>

<h3 id="section-5-6-evolution"><strong>5.6</strong> <strong>Evolution</strong></h3>

<p>An API starts out as a well-designed interface<sup>15</sup>. Slowly but surely, it will have to change to adapt to new use cases. The last thing we want to do when evolving an API is to introduce a breaking change that requires all clients to be modified at once, some of which we might have no control over.</p>

<p>There are two types of changes that can break compatibility, one</p>

<p class="source-footnote">15Or at least it should.</p>

<div class="source-page" id="source-page-64"></div>

<p>at the endpoint level and another at the message level. For example, if we were to change the<em> </em><em>/products</em> endpoint to<em> </em><em>/new-products</em>, it would obviously break clients that haven’t been updated to support the new endpoint. The same applies when making a previously optional query parameter mandatory.</p>

<p>Changing the schema of request or response messages in a backward-incompatible way can also wreak havoc. For example, changing the type of the<em> </em><em>category</em> property in the<em> </em><em>Product</em> schema from string to number is a breaking change that would cause the old deserialization logic to blow up in clients. Similar arguments<sup>16</sup></p>

<p>can be made for messages represented with other serialization formats, like Protocol Buffers.</p>

<p>REST APIs should be versioned to support breaking changes, e.g., by prefixing a version number in the URLs (<em>/v1/products/</em>). However, as a general rule of thumb, APIs should evolve in a backward-compatible way unless there is a very good reason. Although backward-compatible APIs tend not to be particularly elegant, they are practical.</p>

<h3 id="section-5-7-idempotency"><strong>5.7</strong> <strong>Idempotency</strong></h3>

<p>When an API request times out, the client has no idea whether the server actually received the request or not. For example, the server could have processed the request and crashed right before sending a response back to the client.</p>

<p>An effective way for clients to deal with transient failures such as these is to retry the request one or more times until they get a response back. Some HTTP request methods (e.g., PUT, DELETE) are considered inherently idempotent as the effect of executing multiple identical requests is identical to executing only one request<sup>17</sup>. For example, if the server processes the same PUT request</p>

<p class="source-footnote">16“Schema evolution in Avro, Protocol Buffers and Thrift,”<a href="https://martin.kleppmann.com/2012/12/05/schema-evolution-in-avro-protocol-buffers-thrift.html"> https://martin.klepp</a> <a href="https://martin.kleppmann.com/2012/12/05/schema-evolution-in-avro-protocol-buffers-thrift.html">mann.com/2012/12/05/schema-evolution-in-avro-protocol-buffers-thrift.html</a></p>

<p class="source-footnote"><a href="https://martin.kleppmann.com/2012/12/05/schema-evolution-in-avro-protocol-buffers-thrift.html">17</a>“Idempotent Methods,”<a href="https://datatracker.ietf.org/doc/html/rfc7231#section-4.2.2"> https://datatracker.ietf.org/doc/html/rfc7231#secti</a> <a href="https://datatracker.ietf.org/doc/html/rfc7231#section-4.2.2">on-4.2.2</a></p>

<div class="source-page" id="source-page-65"></div>

<p>for the same resource twice in a row, the end effect would be the same as if the PUT request was executed only once.</p>

<p>But what about requests that are not inherently idempotent? For example, suppose a client issues a POST request to add a new product to the catalog service. If the request times out, the client has no way of knowing whether the request succeeded or not. If the request succeeds, retrying it will create two identical products, which is not what the client intended.</p>

<p>In order to deal with this case, the client might have to implement some kind of reconciliation logic that checks for duplicate products and removes them when the request is retried. You can see how this introduces a lot of complexity for the client. Instead of pushing this complexity to the client, a better solution would be for the server to create the product only once by making the POST request idempotent, so that no matter how many times that specific request is retried, it will appear as if it only executed once.</p>

<p>For the server to detect that a request is a duplicate, it needs to be decorated with an idempotency key — a unique identifier (e.g., a UUID). The identifier could be part of a header, like<em> </em><em>Idempotency-</em> <em>Key</em> in Stripe’s API<sup>18</sup>. For the server to detect duplicates, it needs to remember all the request identifiers it has seen by storing them in a database. When a request comes in, the server checks the database to see if the request ID is already present. If it’s not there, it adds the request identifier to the database and executes the request. Request identifiers don’t have to be stored indefinitely, and they can be purged after some time.</p>

<p>Now here comes the tricky part. Suppose the server adds the request identifier to the database and crashes before executing the request. In that case, any future retry won’t have any effect because the server will think it has already executed it. So what we really want is for the request to be handled atomically: either the server processes the request successfully and adds the request identifier to the database, or it fails to process it without storing the request</p>

<p class="source-footnote">18“Designing robust and predictable APIs with idempotency,”<a href="https://stripe.com/blog/idempotency"> https://stripe.c</a> <a href="https://stripe.com/blog/idempotency">om/blog/idempotency</a></p>

<div class="source-page" id="source-page-66"></div>

<p>identifier.</p>

<p>If the request identifiers and the resources managed by the server are stored in the same database, we can guarantee atomicity with ACID transactions<sup>19</sup>. In other words, we can wrap the product creation and request identifier log within the same database transaction in the POST handler. However, if the handler needs to make external calls to other services to handle the request, the implementation becomes a lot more challenging<sup>20</sup>, since it requires some form of coordination. Later, in chapter 13.2, we will learn how to do just that.</p>

<p>Now, assuming the server can detect a duplicate request, how should it be handled? In our example, the server could respond to the client with a status code that signals that the product already exists. But then the client would have to deal with this case differently than if it had received a successful response for the first POST request (<em>201 Created</em>). So ideally, the server should return the same response that it would have returned for the very first request.</p>

<p>So far, we have only considered a single client. Now, imagine the following scenario:</p>

<p>1. Client A sends a request to create a new product. Although the request succeeds, the client doesn’t receive a timely response. 2. Client B deletes the newly created product. 3. Client A retries the original creation request.</p>

<p>How should the server deal with the request in step 3? From client’s A perspective, it would be less surprising<sup>21</sup><sup> </sup>to receive the original creation response than some strange error mentioning that the resource created with that specific request identifier has been deleted. When in doubt, it’s helpful to follow the principle</p>

<p class="source-footnote">19“Using Atomic Transactions to Power an Idempotent API,”<a href="https://brandur.org/http-transactions"> https://brandur.</a> <a href="https://brandur.org/http-transactions">org/http-transactions</a></p>

<p class="source-footnote"><a href="https://brandur.org/http-transactions">20</a>“Implementing Stripe-like Idempotency Keys in Postgres,” <a href="https://brandur.org/idempotency-keys">https://brandur.</a> <a href="https://brandur.org/idempotency-keys">org/idempotency-keys</a></p>

<p class="source-footnote"><a href="https://brandur.org/idempotency-keys">21</a>“Making retries safe with idempotent APIs,”<a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/"> https://aws.amazon.com/build</a> <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">ers-library/making-retries-safe-with-idempotent-APIs/</a></p>

<div class="source-page" id="source-page-67"></div>

<p>of least astonishment.</p>

<p>To summarize, an idempotent API makes it a lot easier to implement clients that are robust to failures, since they can assume that requests can be retried on failure without worrying about all the possible edge cases.</p>

<div class="source-page" id="source-page-69"></div>

<p>Communicating over networks is what makes a system distributed. It’s all too easy to ignore the “leaking” complexity that goes into it, since modern programming languages and frameworks make it look like invoking a remote API is no different from calling a local function. I know I did at first and eventually learned this lesson after spending days investigating weird degradations that ultimately turned out to be caused by exhausted socket pools or routers dropping packets.</p>

<p>Since then, I spend a great deal of time thinking of everything that can go wrong when a remote request is made: socket pools can be exhausted, TLS certificates can expire, DNS servers can become unavailable, routers can become congested and drop packets, non-idempotent requests can result in unexpected states, and the list goes on. The only universal truth is that the fastest, safest, most secure, and reliable network call is the one you don’t have to make. And I hope that by reading about TCP, TLS, UDP, DNS, and HTTP, you also have (re)discovered a profound respect for the challenges of building networked applications.</p>
