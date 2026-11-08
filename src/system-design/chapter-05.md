# Design consistent hashing

## Design consistent hashing

<section class="chapter-video" aria-label="Video for Design consistent hashing"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Design consistent hashing</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>To achieve horizontal scaling, it is important to distribute requests/data efficiently and evenly across servers. Consistent hashing is a commonly used technique to achieve this goal. But first, let us take an in-depth look at the problem.</p>

## The rehashing problem

<section class="chapter-video" aria-label="Video for The rehashing problem"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>The rehashing problem</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>If you have <em>n</em> cache servers, a common way to balance the load is to use the following hash method:</p>
<p><em>serverIndex = hash(key) % N</em>, where <em>N</em> is the size of the server pool.</p>
<p>Let us use an example to illustrate how it works. As shown in Table 5-1, we have 4 servers and 8 string keys with their hashes.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-051.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 51" height="695" loading="lazy" src="../../assets/system-design/figure-051.jpeg" width="940"/></a></figure>
<p>To fetch the server where a key is stored, we perform the modular operation <em>f(key) % 4</em>. For instance, <em>hash(key0) % 4 = 1</em> means a client must contact server 1 to fetch the cached data. Figure 5-1 shows the distribution of keys based on Table 5-1.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-052.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 52" height="666" loading="lazy" src="../../assets/system-design/figure-052.jpeg" width="1110"/></a></figure>
<p>This approach works well when the size of the server pool is fixed, and the data distribution is even. However, problems arise when new servers are added, or existing servers are removed. For example, if server 1 goes offline, the size of the server pool becomes 3. Using the same hash function, we get the same hash value for a key. But applying modular operation gives us different server indexes because the number of servers is reduced by 1. We get the results as shown in Table 5-2 by applying <em>hash % 3</em>:</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-053.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 53" height="651" loading="lazy" src="../../assets/system-design/figure-053.jpeg" width="890"/></a></figure>
<p>Figure 5-2 shows the new distribution of keys based on Table 5-2.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-054.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 54" height="783" loading="lazy" src="../../assets/system-design/figure-054.jpeg" width="1110"/></a></figure>
<p>As shown in Figure 5-2, most keys are redistributed, not just the ones originally stored in the offline server (server 1). This means that when server 1 goes offline, most cache clients will connect to the wrong servers to fetch data. This causes a storm of cache misses. Consistent hashing is an effective technique to mitigate this problem.</p>

## Consistent hashing

<section class="chapter-video" aria-label="Video for Consistent hashing"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Consistent hashing</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Quoted from Wikipedia: "Consistent hashing is a special kind of hashing such that when a hash table is re-sized and consistent hashing is used, only k/n keys need to be remapped on average, where k is the number of keys, and n is the number of slots. In contrast, in most traditional hash tables, a change in the number of array slots causes nearly all keys to be remapped <a href="study:system-design/lessons/05-13-wrap-up/#reference-5-1">[1]</a>”.</p>

## Hash space and hash ring

<section class="chapter-video" aria-label="Video for Hash space and hash ring"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Hash space and hash ring</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Now we understand the definition of consistent hashing, let us find out how it works. Assume SHA-1 is used as the hash function f, and the output range of the hash function is: <em>x0, x1, x2,</em> <em>x3, ..., xn</em>. In cryptography, SHA-1’s hash space goes from 0 to 2^160 - 1. That means <em>x0</em> corresponds to 0, <em>xn</em> corresponds to 2^160 – 1, and all the other hash values in the middle fall between 0 and 2^160 - 1. Figure 5-3 shows the hash space.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-055.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 55" height="163" loading="lazy" src="../../assets/system-design/figure-055.jpeg" width="940"/></a></figure>
<p>By collecting both ends, we get a hash ring as shown in Figure 5-4:</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-056.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 56" height="456" loading="lazy" src="../../assets/system-design/figure-056.jpeg" width="325"/></a></figure>

## Hash servers

<section class="chapter-video" aria-label="Video for Hash servers"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Hash servers</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Using the same hash function f, we map servers based on server IP or name onto the ring. Figure 5-5 shows that 4 servers are mapped on the hash ring.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-057.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 57" height="642" loading="lazy" src="../../assets/system-design/figure-057.jpeg" width="940"/></a></figure>

## Hash keys

<section class="chapter-video" aria-label="Video for Hash keys"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Hash keys</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>One thing worth mentioning is that hash function used here is different from the one in “the rehashing problem,” and there is no modular operation. As shown in Figure 5-6, 4 cache keys (key0, key1, key2, and key3) are hashed onto the hash ring</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-058.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 58" height="589" loading="lazy" src="../../assets/system-design/figure-058.jpeg" width="940"/></a></figure>

## Server lookup

<section class="chapter-video" aria-label="Video for Server lookup"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Server lookup</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>To determine which server a key is stored on, we go clockwise from the key position on the ring until a server is found. Figure 5-7 explains this process. Going clockwise, <em>key0</em> is stored on <em>server 0</em>; <em>key1</em> is stored on <em>server 1</em>; <em>key2</em> is stored on <em>server 2</em> and <em>key3</em> is stored on <em>server</em> <em>3</em>.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-059.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 59" height="495" loading="lazy" src="../../assets/system-design/figure-059.jpeg" width="742"/></a></figure>

## Add a server

<section class="chapter-video" aria-label="Video for Add a server"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Add a server</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Using the logic described above, adding a new server will only require redistribution of a fraction of keys.</p>
<p>In Figure 5-8, after a new <em>server 4</em> is added, only <em>key0</em> needs to be redistributed. <em>k1, k2, </em>and <em>k3 </em>remain on the same servers. Let us take a close look at the logic. Before <em>server 4 </em>is added, <em>key0</em> is stored on <em>server 0</em>. Now, <em>key0</em> will be stored on <em>server 4</em> because <em>server 4</em> is the first server it encounters by going clockwise from <em>key0</em>’s position on the ring. The other keys are not redistributed based on consistent hashing algorithm.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-060.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 60" height="695" loading="lazy" src="../../assets/system-design/figure-060.jpeg" width="940"/></a></figure>

## Remove a server

<section class="chapter-video" aria-label="Video for Remove a server"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Remove a server</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>When a server is removed, only a small fraction of keys require redistribution with consistent hashing. In Figure 5-9, when <em>server 1</em> is removed, only <em>key1</em> must be remapped to <em>server 2</em>. The rest of the keys are unaffected.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-061.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 61" height="676" loading="lazy" src="../../assets/system-design/figure-061.jpeg" width="940"/></a></figure>

## Two issues in the basic approach

<section class="chapter-video" aria-label="Video for Two issues in the basic approach"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Two issues in the basic approach</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>The consistent hashing algorithm was introduced by Karger et al. at MIT <a href="study:system-design/lessons/05-13-wrap-up/#reference-5-1">[1]</a>. The basic steps are:</p>
<ul><li>Map servers and keys on to the ring using a uniformly distributed hash function.</li><li>To find out which server a key is mapped to, go clockwise from the key position until the first server on the ring is found.</li></ul>
<p>Two problems are identified with this approach. First, it is impossible to keep the same size of partitions on the ring for all servers considering a server can be added or removed. A partition is the hash space between adjacent servers. It is possible that the size of the partitions on the ring assigned to each server is very small or fairly large. In Figure 5-10, if <em>s1</em> is removed, <em>s2’s</em> partition (highlighted with the bidirectional arrows) is twice as large as <em>s0</em> and <em>s3’s</em> partition.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-062.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 62" height="551" loading="lazy" src="../../assets/system-design/figure-062.jpeg" width="940"/></a></figure>
<p>Second, it is possible to have a non-uniform key distribution on the ring. For instance, if servers are mapped to positions listed in Figure 5-11, most of the keys are stored on <em>server 2</em>. However, <em>server 1</em> and <em>server 3</em> have no data.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-063.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 63" height="610" loading="lazy" src="../../assets/system-design/figure-063.jpeg" width="940"/></a></figure>
<p>A technique called virtual nodes or replicas is used to solve these problems.</p>

## Virtual nodes

<section class="chapter-video" aria-label="Video for Virtual nodes"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Virtual nodes</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>A virtual node refers to the real node, and each server is represented by multiple virtual nodes on the ring. In Figure 5-12, both <em>server 0</em> and <em>server 1 </em>have 3 virtual nodes. The 3 is arbitrarily chosen; and in real-world systems, the number of virtual nodes is much larger. Instead of using <em>s0</em>, we have <em>s0_0, s0_1</em>, and s0_2 to represent <em>server 0</em> on the ring. Similarly, <em>s1_0, s1_1</em>, and <em>s1_2</em> represent server 1 on the ring. With virtual nodes, each server is responsible for multiple partitions. Partitions (edges) with label <em>s0</em> are managed by server 0. On the other hand, partitions with label <em>s1</em> are managed by <em>server 1</em>.</p>

<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-064.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 64" height="705" loading="lazy" src="../../assets/system-design/figure-064.jpeg" width="940"/></a></figure>
<p>To find which server a key is stored on, we go clockwise from the key’s location and find the first virtual node encountered on the ring. In Figure 5-13, to find out which server <em>k0</em> is stored on, we go clockwise from <em>k0</em>’s location and find virtual node <em>s1_1</em>, which refers to <em>server 1</em>.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-065.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 65" height="611" loading="lazy" src="../../assets/system-design/figure-065.jpeg" width="940"/></a></figure>
<p>As the number of virtual nodes increases, the distribution of keys becomes more balanced. This is because the standard deviation gets smaller with more virtual nodes, leading to balanced data distribution. Standard deviation measures how data are spread out. The outcome of an experiment carried out by online research <a href="study:system-design/lessons/05-13-wrap-up/#reference-5-2">[2]</a> shows that with one or two hundred virtual nodes, the standard deviation is between 5% (200 virtual nodes) and 10% (100 virtual nodes) of the mean. The standard deviation will be smaller when we increase the number of virtual nodes. However, more spaces are needed to store data about virtual nodes. This is a tradeoff, and we can tune the number of virtual nodes to fit our system requirements.</p>

## Find affected keys

<section class="chapter-video" aria-label="Video for Find affected keys"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Find affected keys</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>When a server is added or removed, a fraction of data needs to be redistributed. How can we find the affected range to redistribute the keys?</p>
<p>In Figure 5-14, <em>server 4</em> is added onto the ring. The affected range starts from <em>s4</em> (newly added node) and moves anticlockwise around the ring until a server is found (<em>s3</em>). Thus, keys located between <em>s3</em> and <em>s4</em> need to be redistributed to <em>s4</em>.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-066.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 66" height="695" loading="lazy" src="../../assets/system-design/figure-066.jpeg" width="940"/></a></figure>
<p>When a server (<em>s1</em>) is removed as shown in Figure 5-15, the affected range starts from <em>s1</em> (removed node) and moves anticlockwise around the ring until a server is found (<em>s0</em>). Thus, keys located between <em>s0</em> and <em>s1</em> must be redistributed to <em>s2</em>.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-067.jpeg" rel="noopener" target="_blank"><img alt="Design consistent hashing — original diagram 67" height="844" loading="lazy" src="../../assets/system-design/figure-067.jpeg" width="1174"/></a></figure>

## Wrap up

<section class="chapter-video" aria-label="Video for Wrap up"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Wrap up</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this chapter, we had an in-depth discussion about consistent hashing, including why it is needed and how it works. The benefits of consistent hashing include:</p>
<ul><li>Minimized keys are redistributed when servers are added or removed.</li><li>It is easy to scale horizontally because data are more evenly distributed.</li><li>Mitigate hotspot key problem. Excessive access to a specific shard could cause server overload. Imagine data for Katy Perry, Justin Bieber, and Lady Gaga all end up on the same shard. Consistent hashing helps to mitigate the problem by distributing the data more evenly.</li></ul>
<p>Consistent hashing is widely used in real-world systems, including some notable ones:</p>
<ul><li>Partitioning component of Amazon’s Dynamo database <a href="study:system-design/lessons/05-13-wrap-up/#reference-5-3">[3]</a></li><li>Data partitioning across the cluster in Apache Cassandra <a href="study:system-design/lessons/05-13-wrap-up/#reference-5-4">[4]</a></li><li>Discord chat application <a href="study:system-design/lessons/05-13-wrap-up/#reference-5-5">[5]</a></li><li>Akamai content delivery network <a href="study:system-design/lessons/05-13-wrap-up/#reference-5-6">[6]</a></li><li>Maglev network load balancer <a href="study:system-design/lessons/05-13-wrap-up/#reference-5-7">[7]</a></li></ul>
<p>Congratulations on getting this far! Now give yourself a pat on the back. Good job!</p>

<section class="lesson-references"><h3 id="references-5">References</h3><ol><li id="reference-5-1" value="1">Consistent hashing: <a href="https://en.wikipedia.org/wiki/Consistent_hashing">https://en.wikipedia.org/wiki/Consistent_hashing</a></li><li id="reference-5-2" value="2">Consistent Hashing: <a href="https://tom-e-white.com/2007/11/consistent-hashing.html">https://tom-e-white.com/2007/11/consistent-hashing.html</a></li><li id="reference-5-3" value="3">Dynamo: Amazon’s Highly Available Key-value Store: <a href="https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf">https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf</a></li><li id="reference-5-4" value="4">Cassandra - A Decentralized Structured Storage System: <a href="http://www.cs.cornell.edu/Projects/ladis2009/papers/Lakshman-ladis2009.PDF">http://www.cs.cornell.edu/Projects/ladis2009/papers/Lakshman-ladis2009.PDF</a></li><li id="reference-5-5" value="5">How Discord Scaled Elixir to 5,000,000 Concurrent Users: <a href="https://blog.discord.com/scaling-elixir-f9b8e1e7c29b">https://blog.discord.com/scaling-elixir-f9b8e1e7c29b</a></li><li id="reference-5-6" value="6">CS168: The Modern Algorithmic Toolbox Lecture #1: Introduction and Consistent Hashing: <a href="http://theory.stanford.edu/~tim/s16/l/l1.pdf">http://theory.stanford.edu/~tim/s16/l/l1.pdf</a></li><li id="reference-5-7" value="7">Maglev: A Fast and Reliable Software Network Load Balancer: <a href="https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44824.pdf">https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/44824.pdf</a></li></ol></section>
