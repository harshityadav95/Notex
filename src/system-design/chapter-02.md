# Back-of-the-envelope estimation

## Back-of-the-envelope estimation

<section class="chapter-video" aria-label="Video for Back-of-the-envelope estimation"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Back-of-the-envelope estimation</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In a system design interview, sometimes you are asked to estimate system capacity or performance requirements using a back-of-the-envelope estimation. According to Jeff Dean, Google Senior Fellow, “back-of-the-envelope calculations are estimates you create using a combination of thought experiments and common performance numbers to get a good feel for which designs will meet your requirements” <a href="study:system-design/lessons/02-06-tips/#reference-2-1">[1]</a>.</p>
<p>You need to have a good sense of scalability basics to effectively carry out back-of-theenvelope estimation. The following concepts should be well understood: power of two <a href="study:system-design/lessons/02-06-tips/#reference-2-2">[2]</a>, latency numbers every programmer should know, and availability numbers.</p>

## Power of two

<section class="chapter-video" aria-label="Video for Power of two"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Power of two</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Although data volume can become enormous when dealing with distributed systems, calculation all boils down to the basics. To obtain correct calculations, it is critical to know the data volume unit using the power of 2. A byte is a sequence of 8 bits. An ASCII character uses one byte of memory (8 bits). Below is a table explaining the data volume unit (Table 2- 1).</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-026.jpeg" rel="noopener" target="_blank"><img alt="Back-of-the-envelope estimation — original diagram 26" height="742" loading="lazy" src="../../assets/system-design/figure-026.jpeg" width="1272"/></a></figure>

## Latency numbers every programmer should know

<section class="chapter-video" aria-label="Video for Latency numbers every programmer should know"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Latency numbers every programmer should know</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Dr. Dean from Google reveals the length of typical computer operations in 2010 <a href="study:system-design/lessons/02-06-tips/#reference-2-1">[1]</a>. Some numbers are outdated as computers become faster and more powerful. However, those numbers should still be able to give us an idea of the fastness and slowness of different computer operations.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-027.jpeg" rel="noopener" target="_blank"><img alt="Back-of-the-envelope estimation — original diagram 27" height="1403" loading="lazy" src="../../assets/system-design/figure-027.jpeg" width="1266"/></a></figure>
<p>Notes ----------ns = nanosecond, μs = microsecond, ms = millisecond 1 ns = 10^-9 seconds 1 μs= 10^-6 seconds = 1,000 ns 1 ms = 10^-3 seconds = 1,000 μs = 1,000,000 ns</p>
<p>A Google software engineer built a tool to visualize Dr. Dean’s numbers. The tool also takes the time factor into consideration. Figures 2-1 shows the visualized latency numbers as of 2020 (source of figures: reference material <a href="study:system-design/lessons/02-06-tips/#reference-2-3">[3]</a>).</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-028.jpeg" rel="noopener" target="_blank"><img alt="Back-of-the-envelope estimation — original diagram 28" height="903" loading="lazy" src="../../assets/system-design/figure-028.jpeg" width="940"/></a></figure>
<p>By analyzing the numbers in Figure 2-1, we get the following conclusions:</p>
<ul><li>Memory is fast but the disk is slow.</li><li>Avoid disk seeks if possible.</li><li>Simple compression algorithms are fast.</li><li>Compress data before sending it over the internet if possible.</li><li>Data centers are usually in different regions, and it takes time to send data between them.</li></ul>

## Availability numbers

<section class="chapter-video" aria-label="Video for Availability numbers"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Availability numbers</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>High availability is the ability of a system to be continuously operational for a desirably long period of time. High availability is measured as a percentage, with 100% means a service that has 0 downtime. Most services fall between 99% and 100%.</p>
<p>A service level agreement (SLA) is a commonly used term for service providers. This is an agreement between you (the service provider) and your customer, and this agreement formally defines the level of uptime your service will deliver. Cloud providers Amazon <a href="study:system-design/lessons/02-06-tips/#reference-2-4">[4]</a>, Google <a href="study:system-design/lessons/02-06-tips/#reference-2-5">[5]</a> and Microsoft <a href="study:system-design/lessons/02-06-tips/#reference-2-6">[6]</a> set their SLAs at 99.9% or above. Uptime is traditionally measured in nines. The more the nines, the better. As shown in Table 2-3, the number of nines correlate to the expected system downtime.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-029.jpeg" rel="noopener" target="_blank"><img alt="Back-of-the-envelope estimation — original diagram 29" height="642" loading="lazy" src="../../assets/system-design/figure-029.jpeg" width="1266"/></a></figure>

## Example: Estimate Twitter QPS and storage requirements

<section class="chapter-video" aria-label="Video for Example: Estimate Twitter QPS and storage requirements"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Example: Estimate Twitter QPS and storage requirements</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Please note the following numbers are for this exercise only as they are not real numbers from Twitter.</p>
<p>Assumptions:</p>
<ul><li>300 million monthly active users.</li><li>50% of users use Twitter daily.</li><li>Users post 2 tweets per day on average.</li><li>10% of tweets contain media.</li><li>Data is stored for 5 years.</li></ul>
<p>Estimations: Query per second (QPS) estimate:</p>
<ul><li>Daily active users (DAU) = 300 million * 50% = 150 million</li><li>Tweets QPS = 150 million * 2 tweets / 24 hour / 3600 seconds = ~3500</li><li>Peek QPS = 2 * QPS = ~7000</li></ul>
<p>We will only estimate media storage here.</p>
<ul><li>Average tweet size:</li><li>tweet_id   64 bytes</li><li>text           140 bytes</li><li>media       1 MB</li><li>Media storage: 150 million * 2 * 10% * 1 MB = 30 TB per day</li><li>5-year media storage: 30 TB * 365 * 5 = ~55 PB</li></ul>

## Tips

<section class="chapter-video" aria-label="Video for Tips"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Tips</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Back-of-the-envelope estimation is all about the process. Solving the problem is more important than obtaining results. Interviewers may test your problem-solving skills. Here are a few tips to follow:</p>
<ul><li>Rounding and Approximation. It is difficult to perform complicated math operations during the interview. For example, what is the result of “99987 / 9.1”? There is no need to spend valuable time to solve complicated math problems. Precision is not expected. Use round numbers and approximation to your advantage. The division question can be simplified as follows: “100,000 / 10”.</li><li>Write down your assumptions. It is a good idea to write down your assumptions to be referenced later.</li><li>Label your units. When you write down “5”, does it mean 5 KB or 5 MB? You might confuse yourself with this. Write down the units because “5 MB” helps to remove ambiguity.</li><li>Commonly asked back-of-the-envelope estimations: QPS, peak QPS, storage, cache, number of servers, etc. You can practice these calculations when preparing for an interview. Practice makes perfect.</li></ul>
<p>Congratulations on getting this far! Now give yourself a pat on the back. Good job!</p>

<section class="lesson-references"><h3 id="references-2">References</h3><ol><li id="reference-2-1" value="1">J. Dean.Google Pro Tip: Use Back-Of-The-Envelope-Calculations To Choose The Best Design: <a href="http://highscalability.com/blog/2011/1/26/google-pro-tip-use-back-of-the-envelopecalculations-to-choo.html">http://highscalability.com/blog/2011/1/26/google-pro-tip-use-back-of-the-envelopecalculations-to-choo.html</a></li><li id="reference-2-2" value="2">System design primer: <a href="https://github.com/donnemartin/system-design-primer">https://github.com/donnemartin/system-design-primer</a></li><li id="reference-2-3" value="3">Latency Numbers Every Programmer Should Know: <a href="https://colin-scott.github.io/personal_website/research/interactive_latency.html">https://colin-scott.github.io/personal_website/research/interactive_latency.html</a></li><li id="reference-2-4" value="4">Amazon Compute Service Level Agreement: <a href="https://aws.amazon.com/compute/sla/">https://aws.amazon.com/compute/sla/</a></li><li id="reference-2-5" value="5">Compute Engine Service Level Agreement (SLA): <a href="https://cloud.google.com/compute/sla">https://cloud.google.com/compute/sla</a></li><li id="reference-2-6" value="6">SLA summary for Azure services: <a href="https://azure.microsoft.com/enus/support/legal/sla/summary/">https://azure.microsoft.com/enus/support/legal/sla/summary/</a></li></ol></section>
