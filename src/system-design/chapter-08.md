# Design a URL shortener

## Design a URL shortener

<section class="chapter-video" aria-label="Video for Design a URL shortener"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Design a URL shortener</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this chapter, we will tackle an interesting and classic system design interview question: designing a URL shortening service like tinyurl.</p>

## Step 1 - Understand the problem and establish design scope

<section class="chapter-video" aria-label="Video for Step 1 - Understand the problem and establish design scope"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 1 - Understand the problem and establish design scope</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>System design interview questions are intentionally left open-ended. To design a well-crafted system, it is critical to ask clarification questions.</p>
<p><strong>Candidate</strong>: Can you give an example of how a URL shortener work? <strong>Interviewer</strong>: Assume URL https://www.systeminterview.com/q=chatsystem&amp;c=loggedin&amp;v=v3&amp;l=long is the original URL. Your service creates an alias with shorter length: https://tinyurl.com/ y7keocwj. If you click the alias, it redirects you to the original URL.</p>
<p><strong>Candidate</strong>: What is the traffic volume? <strong>Interviewer</strong>: 100 million URLs are generated per day.</p>
<p><strong>Candidate</strong>: How long is the shortened URL? <strong>Interviewer</strong>: As short as possible.</p>
<p><strong>Candidate</strong>: What characters are allowed in the shortened URL? <strong>Interviewer</strong>: Shortened URL can be a combination of numbers (0-9) and characters (a-z, A- Z).</p>
<p><strong>Candidate</strong>: Can shortened URLs be deleted or updated? <strong>Interviewer</strong>: For simplicity, let us assume shortened URLs cannot be deleted or updated.</p>
<p>Here are the basic use cases:</p>
<p>1.URL shortening: given a long URL =&gt; return a much shorter URL 2.URL redirecting: given a shorter URL =&gt; redirect to the original URL 3.High availability, scalability, and fault tolerance considerations</p>

## Back of the envelope estimation

<section class="chapter-video" aria-label="Video for Back of the envelope estimation"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Back of the envelope estimation</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<ul><li>Write operation: 100 million URLs are generated per day.</li><li>Write operation per second: 100 million / 24 /3600 = 1160</li><li>Read operation: Assuming ratio of read operation to write operation is 10:1, read operation per second: 1160 * 10 = 11,600</li><li>Assuming the URL shortener service will run for 10 years, this means we must support 100 million * 365 * 10 = 365 billion records.</li><li>Assume average URL length is 100.</li></ul>
<ul><li>Storage requirement over 10 years: 365 billion * 100 bytes * 10 years = 365 TB</li></ul>
<p>It is important for you to walk through the assumptions and calculations with your interviewer so that both of you are on the same page.</p>

## Step 2 - Propose high-level design and get buy-in

<section class="chapter-video" aria-label="Video for Step 2 - Propose high-level design and get buy-in"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 2 - Propose high-level design and get buy-in</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this section, we discuss the API endpoints, URL redirecting, and URL shortening flows.</p>

## API Endpoints

<section class="chapter-video" aria-label="Video for API Endpoints"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>API Endpoints</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>API endpoints facilitate the communication between clients and servers. We will design the APIs REST-style. If you are unfamiliar with restful API, you can consult external materials, such as the one in the reference material <a href="study:system-design/lessons/08-13-step-4-wrap-up/#reference-8-1">[1]</a>. A URL shortener primary needs two API endpoints. 1.URL shortening. To create a new short URL, a client sends a POST request, which contains one parameter: the original long URL. The API looks like this:</p>
<p><em>POST api/v1/data/shorten</em></p>
<ul><li>request parameter: {longUrl: longURLString}</li><li>return shortURL</li></ul>
<p>2.URL redirecting. To redirect a short URL to the corresponding long URL, a client sends a GET request. The API looks like this:</p>
<p><em>GET api/v1/shortUrl</em></p>
<ul><li>Return longURL for HTTP redirection</li></ul>

## URL redirecting

<section class="chapter-video" aria-label="Video for URL redirecting"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>URL redirecting</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Figure 8-1 shows what happens when you enter a tinyurl onto the browser. Once the server receives a tinyurl request, it changes the short URL to the long URL with 301 redirect.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-098.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 98" height="466" loading="lazy" src="../../assets/system-design/figure-098.jpeg" width="940"/></a></figure>
<p>The detailed communication between clients and servers is shown in Figure 8-2.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-099.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 99" height="702" loading="lazy" src="../../assets/system-design/figure-099.jpeg" width="652"/></a></figure>
<p>One thing worth discussing here is 301 redirect vs 302 redirect.</p>
<p><strong>301 redirect</strong>. A 301 redirect shows that the requested URL is “permanently” moved to the long URL. Since it is permanently redirected, the browser caches the response, and subsequent requests for the same URL will not be sent to the URL shortening service. Instead, requests are redirected to the long URL server directly.</p>
<p><strong>302 redirect</strong>. A 302 redirect means that the URL is “temporarily” moved to the long URL, meaning that subsequent requests for the same URL will be sent to the URL shortening service first. Then, they are redirected to the long URL server.</p>
<p>Each redirection method has its pros and cons. If the priority is to reduce the server load, using 301 redirect makes sense as only the first request of the same URL is sent to URL shortening servers. However, if analytics is important, 302 redirect is a better choice as it can track click rate and source of the click more easily.</p>
<p>The most intuitive way to implement URL redirecting is to use hash tables. Assuming the hash table stores <em>&lt;shortURL, longURL&gt;</em> pairs, URL redirecting can be implemented by the following:</p>
<ul><li>Get longURL: longURL = hashTable.get(shortURL)</li><li>Once you get the longURL, perform the URL redirect.</li></ul>

## URL shortening

<section class="chapter-video" aria-label="Video for URL shortening"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>URL shortening</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Let us assume the short URL looks like this: www.tinyurl.com/<strong>{hashValue}</strong>. To support the URL shortening use case, we must find a hash function <em>fx</em> that maps a long URL to the <em>hashValue</em>, as shown in Figure 8-3.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-100.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 100" height="406" loading="lazy" src="../../assets/system-design/figure-100.jpeg" width="487"/></a></figure>
<p>The hash function must satisfy the following requirements:</p>
<ul><li>Each <em>longURL</em> must be hashed to one <em>hashValue</em>.</li><li>Each <em>hashValue</em> can be mapped back to the <em>longURL</em>.</li></ul>
<p>Detailed design for the hash function is discussed in deep dive.</p>

## Step 3 - Design deep dive

<section class="chapter-video" aria-label="Video for Step 3 - Design deep dive"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 3 - Design deep dive</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Up until now, we have discussed the high-level design of URL shortening and URL redirecting. In this section, we dive deep into the following: data model, hash function, URL shortening and URL redirecting.</p>

## Data model

<section class="chapter-video" aria-label="Video for Data model"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Data model</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In the high-level design, everything is stored in a hash table. This is a good starting point; however, this approach is not feasible for real-world systems as memory resources are limited and expensive. A better option is to store <em>&lt;shortURL, longURL&gt;</em> mapping in a relational database. Figure 8-4 shows a simple database table design. The simplified version of the table contains 3 columns: <em>id</em>, <em>shortURL, longURL</em>.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-101.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 101" height="435" loading="lazy" src="../../assets/system-design/figure-101.jpeg" width="476"/></a></figure>

## Hash function

<section class="chapter-video" aria-label="Video for Hash function"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Hash function</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Hash function is used to hash a long URL to a short URL, also known as <em>hashValue</em>.</p>
<p><strong>Hash value length</strong> The <em>hashValue</em> consists of characters from [0-9, a-z, A-Z], containing 10 + 26 + 26 = 62 possible characters. To figure out the length of <em>hashValue</em>, find the smallest <em>n</em> such that <em>62^n</em> <em>≥ 365 billion</em>. The system must support up to 365 billion URLs based on the back of the envelope estimation. Table 8-1 shows the length of <em>hashValue</em> and the corresponding maximal number of URLs it can support.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-102.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 102" height="835" loading="lazy" src="../../assets/system-design/figure-102.jpeg" width="1265"/></a></figure>
<p>When <em>n = 7, 62 ^ n = ~3.5 trillion</em>, 3.5 trillion is more than enough to hold 365 billion URLs, so the length of <em>hashValue</em> is 7.</p>
<p>We will explore two types of hash functions for a URL shortener. The first one is “hash + collision resolution”, and the second one is “base 62 conversion.” Let us look at them one by one.</p>
<p><strong>Hash + collision resolution</strong> To shorten a long URL, we should implement a hash function that hashes a long URL to a 7character string. A straightforward solution is to use well-known hash functions like CRC32, MD5, or SHA-1. The following table compares the hash results after applying different hash functions on this URL: https://en.wikipedia.org/wiki/Systems_design.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-103.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 103" height="287" loading="lazy" src="../../assets/system-design/figure-103.jpeg" width="722"/></a></figure>
<p>As shown in Table 8-2, even the shortest hash value (from CRC32) is too long (more than 7 characters). How can we make it shorter?</p>
<p>The first approach is to collect the first 7 characters of a hash value; however, this method can lead to hash collisions. To resolve hash collisions, we can recursively append a new predefined string until no more collision is discovered. This process is explained in Figure 8-</p>
<p>5.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-104.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 104" height="600" loading="lazy" src="../../assets/system-design/figure-104.jpeg" width="940"/></a></figure>
<p>This method can eliminate collision; however, it is expensive to query the database to check if a shortURL exists for every request. A technique called bloom filters <a href="study:system-design/lessons/08-13-step-4-wrap-up/#reference-8-2">[2]</a> can improve performance. A bloom filter is a space-efficient probabilistic technique to test if an element is a member of a set. Refer to the reference material <a href="study:system-design/lessons/08-13-step-4-wrap-up/#reference-8-2">[2]</a> for more details.</p>
<p><strong>Base 62 conversion</strong> Base conversion is another approach commonly used for URL shorteners. Base conversion helps to convert the same number between its different number representation systems. Base 62 conversion is used as there are 62 possible characters for <em>hashValue</em>. Let us use an example to explain how the conversion works: convert 1115710 to base 62 representation</p>
<p>(1115710 represents 11157 in a base 10 system).</p>
<ul><li>From its name, base 62 is a way of using 62 characters for encoding. The mappings are: <em>0-0, ..., 9-9, 10-a, 11-b, ..., 35-z, 36-A, ..., 61-Z, where</em> ‘a’ stands for 10, ‘Z’ stands for 61, etc.</li></ul>
<ul><li>1115710 = 2 x 62<sup>2</sup> + 55 x 62<sup>1 </sup>+ 59 x 62<sup>0</sup> = [2, 55, 59] -&gt; [2, T, X] in base 62</li></ul>
<p>representation. Figure 8-6 shows the conversation process.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-105.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 105" height="417" loading="lazy" src="../../assets/system-design/figure-105.jpeg" width="816"/></a></figure>
<ul><li>Thus, the short URL is https://tinyurl.com /<strong>2TX</strong></li></ul>
<p><strong>Comparison of the two approaches</strong> Table 8-3 shows the differences of the two approaches.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-106.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 106" height="782" loading="lazy" src="../../assets/system-design/figure-106.jpeg" width="1277"/></a></figure>

## URL shortening deep dive

<section class="chapter-video" aria-label="Video for URL shortening deep dive"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>URL shortening deep dive</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>As one of the core pieces of the system, we want the URL shortening flow to be logically simple and functional. Base 62 conversion is used in our design. We build the following diagram (Figure 8-7) to demonstrate the flow.  </p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-107.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 107" height="659" loading="lazy" src="../../assets/system-design/figure-107.jpeg" width="802"/></a></figure>
<ol start="1"><li>longURL is the input.</li><li>The system checks if the longURL is in the database.</li><li>If it is, it means the longURL was converted to shortURL before. In this case, fetch the shortURL from the database and return it to the client.</li><li>If not, the longURL is new. A new unique ID (primary key) Is generated by the unique ID generator.</li><li>Convert the ID to shortURL with base 62 conversion.</li><li>Create a new database row with the ID, shortURL, and longURL. To make the flow easier to understand, let us look at a concrete example.</li></ol>
<ul><li>Assuming the input longURL is: https://en.wikipedia.org/wiki/Systems_design</li><li>Unique ID generator returns ID: 2009215674938.</li><li>Convert the ID to shortURL using the base 62 conversion. ID (2009215674938) is converted to “zn9edcu”.</li><li>Save ID, shortURL, and longURL to the database as shown in Table 8-4.</li></ul>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-108.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 108" height="267" loading="lazy" src="../../assets/system-design/figure-108.jpeg" width="1274"/></a></figure>
<p>The distributed unique ID generator is worth mentioning. Its primary function is to generate globally unique IDs, which are used for creating shortURLs. In a highly distributed environment, implementing a unique ID generator is challenging. Luckily, we have already discussed a few solutions in “Chapter 7: Design A Unique ID Generator in Distributed Systems”. You can refer back to it to refresh your memory.</p>


## URL redirecting deep dive

<section class="chapter-video" aria-label="Video for URL redirecting deep dive"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>URL redirecting deep dive</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Figure 8-8 shows the detailed design of the URL redirecting. As there are more reads than writes, <em>&lt;shortURL, longURL&gt; </em>mapping is stored in a cache to improve performance.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-109.jpeg" rel="noopener" target="_blank"><img alt="Design a URL shortener — original diagram 109" height="317" loading="lazy" src="../../assets/system-design/figure-109.jpeg" width="941"/></a></figure>
<p>The flow of URL redirecting is summarized as follows:</p>
<ol start="1"><li>A user clicks a short URL link: https://tinyurl.com/zn9edcu</li><li>The load balancer forwards the request to web servers.</li><li>If a shortURL is already in the cache, return the longURL directly.</li><li>If a shortURL is not in the cache, fetch the longURL from the database. If it is not in the database, it is likely a user entered an invalid shortURL.</li><li>The longURL is returned to the user.</li></ol>

## Step 4 - Wrap up

<section class="chapter-video" aria-label="Video for Step 4 - Wrap up"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 4 - Wrap up</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this chapter, we talked about the API design, data model, hash function, URL shortening, and URL redirecting.</p>
<p>If there is extra time at the end of the interview, here are a few additional talking points.</p>
<ul><li>Rate limiter: A potential security problem we could face is that malicious users send an overwhelmingly large number of URL shortening requests. Rate limiter helps to filter out requests based on IP address or other filtering rules. If you want to refresh your memory about rate limiting, refer to “Chapter 4: Design a rate limiter”.</li><li>Web server scaling: Since the web tier is stateless, it is easy to scale the web tier by adding or removing web servers.</li><li>Database scaling: Database replication and sharding are common techniques.</li><li>Analytics: Data is increasingly important for business success. Integrating an analytics solution to the URL shortener could help to answer important questions like how many people click on a link? When do they click the link? etc.</li><li>Availability, consistency, and reliability. These concepts are at the core of any large system’s success. We discussed them in detail in Chapter 1, please refresh your memory on these topics.</li></ul>
<p>Congratulations on getting this far! Now give yourself a pat on the back. Good job!</p>

<section class="lesson-references"><h3 id="references-8">References</h3><ol><li id="reference-8-1" value="1">A RESTful Tutorial: <a href="https://www.restapitutorial.com/index.html">https://www.restapitutorial.com/index.html</a></li><li id="reference-8-2" value="2">Bloom filter: <a href="https://en.wikipedia.org/wiki/Bloom_filter">https://en.wikipedia.org/wiki/Bloom_filter</a></li></ol></section>
