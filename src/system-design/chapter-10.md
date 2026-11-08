# Design a notification system

## Design a notification system

<section class="chapter-video" aria-label="Video for Design a notification system"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Design a notification system</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>A notification system has already become a very popular feature for many applications in recent years. A notification alerts a user with important information like breaking news, product updates, events, offerings, etc. It has become an indispensable part of our daily life. In this chapter, you are asked to design a notification system.</p>
<p>A notification is more than just mobile push notification. Three types of notification formats are: mobile push notification, SMS message, and Email. Figure 10-1 shows an example of each of these notifications.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-121.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 121" height="691" loading="lazy" src="../../assets/system-design/figure-121.jpeg" width="940"/></a></figure>

## Step 1 - Understand the problem and establish design scope

<section class="chapter-video" aria-label="Video for Step 1 - Understand the problem and establish design scope"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 1 - Understand the problem and establish design scope</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Building a scalable system that sends out millions of notifications a day is not an easy task. It requires a deep understanding of the notification ecosystem. The interview question is purposely designed to be open-ended and ambiguous, and it is your responsibility to ask questions to clarify the requirements.</p>
<p><strong>Candidate</strong>: What types of notifications does the system support? <strong>Interviewer</strong>: Push notification, SMS message, and email.</p>
<p><strong>Candidate: </strong>Is it a real-time system? <strong>Interviewer: </strong>Let us say it is a soft real-time system. We want a user to receive notifications as soon as possible. However, if the system is under a high workload, a slight delay is acceptable.</p>
<p><strong>Candidate: </strong>What are the supported devices? <strong>Interviewer: </strong>iOS devices, android devices, and laptop/desktop.</p>
<p><strong>Candidate: </strong>What triggers notifications? <strong>Interviewer: </strong>Notifications can be triggered by client applications. They can also be scheduled on the server-side.</p>
<p><strong>Candidate: </strong>Will users be able to opt-out? <strong>Interviewer: </strong>Yes, users who choose to opt-out will no longer receive notifications.</p>
<p><strong>Candidate: </strong>How many notifications are sent out each day? <strong>Interviewer: </strong>10 million mobile push notifications, 1 million SMS messages, and 5 million emails.</p>

## Step 2 - Propose high-level design and get buy-in

<section class="chapter-video" aria-label="Video for Step 2 - Propose high-level design and get buy-in"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 2 - Propose high-level design and get buy-in</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>This section shows the high-level design that supports various notification types: iOS push notification, Android push notification, SMS message, and Email. It is structured as follows:</p>
<ul><li>Different types of notifications</li><li>Contact info gathering flow</li><li>Notification sending/receiving flow</li></ul>

## Different types of notifications

<section class="chapter-video" aria-label="Video for Different types of notifications"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Different types of notifications</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>We start by looking at how each notification type works at a high level.</p>
<p><strong>iOS push notification</strong></p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-122.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 122" height="198" loading="lazy" src="../../assets/system-design/figure-122.jpeg" width="690"/></a></figure>
<p>We primary need three components to send an iOS push notification:</p>
<ul><li>Provider. A provider builds and sends notification requests to Apple Push Notification Service (APNS). To construct a push notification, the provider provides the following data:</li></ul>
<ul><li>Device token: This is a unique identifier used for sending push notifications.</li><li>Payload: This is a JSON dictionary that contains a notification’s payload. Here is an example:</li></ul>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-123.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 123" height="520" loading="lazy" src="../../assets/system-design/figure-123.jpeg" width="753"/></a></figure>
<ul><li>APNS: This is a remote service provided by Apple to propagate push notifications to iOS devices.</li><li>iOS Device: It is the end client, which receives push notifications.</li></ul>
<p><strong>Android push notification</strong> Android adopts a similar notification flow. Instead of using APNs, Firebase Cloud Messaging (FCM) is commonly used to send push notifications to android devices.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-124.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 124" height="216" loading="lazy" src="../../assets/system-design/figure-124.jpeg" width="752"/></a></figure>
<p><strong>SMS message</strong> For SMS messages, third party SMS services like Twilio <a href="study:system-design/lessons/10-11-step-4-wrap-up/#reference-10-1">[1]</a>, Nexmo <a href="study:system-design/lessons/10-11-step-4-wrap-up/#reference-10-2">[2]</a>, and many others are commonly used. Most of them are commercial services. </p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-125.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 125" height="256" loading="lazy" src="../../assets/system-design/figure-125.jpeg" width="772"/></a></figure>
<p><strong>Email</strong> Although companies can set up their own email servers, many of them opt for commercial email services. Sendgrid <a href="study:system-design/lessons/10-11-step-4-wrap-up/#reference-10-3">[3]</a> and Mailchimp <a href="study:system-design/lessons/10-11-step-4-wrap-up/#reference-10-4">[4]</a> are among the most popular email services, which offer a better delivery rate and data analytics.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-126.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 126" height="234" loading="lazy" src="../../assets/system-design/figure-126.jpeg" width="735"/></a></figure>
<p>Figure 10-6 shows the design after including all the third-party services.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-127.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 127" height="923" loading="lazy" src="../../assets/system-design/figure-127.jpeg" width="465"/></a></figure>

## Contact info gathering flow

<section class="chapter-video" aria-label="Video for Contact info gathering flow"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Contact info gathering flow</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>To send notifications, we need to gather mobile device tokens, phone numbers, or email addresses. As shown in Figure 10-7, when a user installs our app or signs up for the first time, API servers collect user contact info and store it in the database. </p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-128.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 128" height="282" loading="lazy" src="../../assets/system-design/figure-128.jpeg" width="940"/></a></figure>
<p>Figure 10-8 shows simplified database tables to store contact info. Email addresses and phone numbers are stored in the <em>user </em>table, whereas device tokens are stored in the <em>device </em>table. A user can have multiple devices, indicating that a push notification can be sent to all the user devices.</p>

<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-129.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 129" height="335" loading="lazy" src="../../assets/system-design/figure-129.jpeg" width="940"/></a></figure>

## Notification sending/receiving flow

<section class="chapter-video" aria-label="Video for Notification sending/receiving flow"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Notification sending/receiving flow</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>We will first present the initial design; then, propose some optimizations.</p>
<p><strong>High</strong><strong>-</strong><strong>level design</strong></p>
<p>Figure 10-9 shows the design, and each system component is explained below.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-130.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 130" height="739" loading="lazy" src="../../assets/system-design/figure-130.jpeg" width="940"/></a></figure>
<p><strong>Service 1 to N</strong>: A service can be a micro-service, a cron job, or a distributed system that triggers notification sending events. For example, a billing service sends emails to remind customers of their due payment or a shopping website tells customers that their packages will be delivered tomorrow via SMS messages.</p>
<p><strong>Notification system</strong>: The notification system is the centerpiece of sending/receiving notifications. Starting with something simple, only one notification server is used. It provides APIs for services 1 to N, and builds notification payloads for third party services.  </p>
<p><strong>Third-party services: </strong>Third party services are responsible for delivering notifications to users. While integrating with third-party services, we need to pay extra attention to extensibility. Good extensibility means a flexible system that can easily plugging or unplugging of a third-party service. Another important consideration is that a third-party service might be unavailable in new markets or in the future. For instance, FCM is unavailable in China. Thus, alternative third-party services such as Jpush, PushY, etc are used there.</p>
<p><strong>iOS, Android, SMS, Email</strong>: Users receive notifications on their devices.</p>
<p>Three problems are identified in this design:</p>
<ul><li>Single point of failure (SPOF): A single notification server means SPOF.</li><li>Hard to scale: The notification system handles everything related to push notifications in one server. It is challenging to scale databases, caches, and different notification processing components independently.</li><li>Performance bottleneck: Processing and sending notifications can be resource intensive. For example, constructing HTML pages and waiting for responses from third party services could take time. Handling everything in one system can result in the system overload, especially during peak hours.</li></ul>
<p><strong>High-level design (improved)</strong> After enumerating challenges in the initial design, we improve the design as listed below:</p>
<ul><li>Move the database and cache out of the notification server.</li><li>Add more notification servers and set up automatic horizontal scaling.</li><li>Introduce message queues to decouple the system components.</li></ul>
<p>Figure 10-10 shows the improved high-level design.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-131.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 131" height="589" loading="lazy" src="../../assets/system-design/figure-131.jpeg" width="881"/></a></figure>
<p>The best way to go through the above diagram is from left to right:</p>
<p><strong>Service 1 to N</strong>: They represent different services that send notifications via APIs provided by notification servers.</p>
<p><strong>Notification servers</strong>: They provide the following functionalities:</p>
<ul><li>Provide APIs for services to send notifications. Those APIs are only accessible internally or by verified clients to prevent spams.</li><li>Carry out basic validations to verify emails, phone numbers, etc.</li><li>Query the database or cache to fetch data needed to render a notification.</li><li>Put notification data to message queues for parallel processing.</li></ul>
<p>Here is an example of the API to send an email:</p>
<p><em>POST https://api.example.com/v/sms/send</em> Request body</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-132.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 132" height="540" loading="lazy" src="../../assets/system-design/figure-132.jpeg" width="582"/></a></figure>
<p><strong>Cache</strong>: User info, device info, notification templates are cached.</p>
<p><strong>DB</strong>: It stores data about user, notification, settings, etc.</p>
<p><strong>Message queues</strong>: They remove dependencies between components. Message queues serve as buffers when high volumes of notifications are to be sent out. Each notification type is assigned with a distinct message queue so an outage in one third-party service will not affect other notification types.</p>
<p><strong>Workers</strong>: Workers are a list of servers that pull notification events from message queues and send them to the corresponding third-party services.</p>
<p><strong>Third-party services</strong>: Already explained in the initial design.</p>
<p><strong>iOS, Android, SMS, Email</strong>: Already explained in the initial design.</p>
<p>Next, let us examine how every component works together to send a notification:</p>
<ol start="1"><li>A service calls APIs provided by notification servers to send notifications.</li><li>Notification servers fetch metadata such as user info, device token, and notification setting from the cache or database.</li><li>A notification event is sent to the corresponding queue for processing. For instance, an iOS push notification event is sent to the iOS PN queue.</li><li>Workers pull notification events from message queues.</li><li>Workers send notifications to third party services.</li><li>Third-party services send notifications to user devices.</li></ol>

## Step 3 - Design deep dive

<section class="chapter-video" aria-label="Video for Step 3 - Design deep dive"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 3 - Design deep dive</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In the high-level design, we discussed different types of notifications, contact info gathering flow, and notification sending/receiving flow. We will explore the following in deep dive:</p>
<ul><li>Reliability.</li><li>Additional component and considerations: notification template, notification settings, rate limiting, retry mechanism, security in push notifications, monitor queued notifications and event tracking.</li><li>Updated design.</li></ul>

## Reliability

<section class="chapter-video" aria-label="Video for Reliability"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Reliability</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>We must answer a few important reliability questions when designing a notification system in distributed environments.</p>
<p><strong>How to prevent data loss?</strong> One of the most important requirements in a notification system is that it cannot lose data. Notifications can usually be delayed or re-ordered, but never lost. To satisfy this requirement, the notification system persists notification data in a database and implements a retry mechanism. The notification log database is included for data persistence, as shown in Figure 10-11.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-133.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 133" height="382" loading="lazy" src="../../assets/system-design/figure-133.jpeg" width="597"/></a></figure>
<p><strong>Will recipients receive a notification exactly once?</strong> The short answer is no. Although notification is delivered exactly once most of the time, the distributed nature could result in duplicate notifications. To reduce the duplication occurrence, we introduce a dedupe mechanism and handle each failure case carefully. Here is a simple dedupe logic:</p>
<p>When a notification event first arrives, we check if it is seen before by checking the event ID. If it is seen before, it is discarded. Otherwise, we will send out the notification. For interested readers to explore why we cannot have exactly once delivery, refer to the reference material <a href="study:system-design/lessons/10-11-step-4-wrap-up/#reference-10-5">[5]</a>.</p>

## Additional components and considerations

<section class="chapter-video" aria-label="Video for Additional components and considerations"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Additional components and considerations</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>We have discussed how to collect user contact info, send, and receive a notification. A notification system is a lot more than that. Here we discuss additional components including template reusing, notification settings, event tracking, system monitoring, rate limiting, etc.</p>
<p><strong>Notification template</strong></p>
<p>A large notification system sends out millions of notifications per day, and many of these notifications follow a similar format. Notification templates are introduced to avoid building every notification from scratch. A notification template is a preformatted notification to create your unique notification by customizing parameters, styling, tracking links, etc. Here is an example template of push notifications.</p>
<p>BODY: You dreamed of it. We dared it. [ITEM NAME] is back — only until [DATE]. CTA: Order Now. Or, Save My [ITEM NAME]</p>
<p>The benefits of using notification templates include maintaining a consistent format, reducing the margin error, and saving time.</p>
<p><strong>Notification setting</strong> Users generally receive way too many notifications daily and they can easily feel overwhelmed. Thus, many websites and apps give users fine-grained control over notification settings. This information is stored in the notification setting table, with the following fields:</p>
<p>user_id   bigInt channel  varchar    # push notification, email or SMS opt_in   boolean    # opt-in to receive notification</p>
<p>Before any notification is sent to a user, we first check if a user is opted-in to receive this type of notification.</p>
<p><strong>Rate limiting</strong> To avoid overwhelming users with too many notifications, we can limit the number of notifications a user can receive. This is important because receivers could turn off notifications completely if we send too often.</p>
<p><strong>Retry mechanism</strong> When a third-party service fails to send a notification, the notification will be added to the message queue for retrying. If the problem persists, an alert will be sent out to developers.</p>
<p><strong>Security in push notifications</strong> For iOS or Android apps, appKey and appSecret are used to secure push notification APIs <a href="study:system-design/lessons/10-11-step-4-wrap-up/#reference-10-6">[6]</a>. Only authenticated or verified clients are allowed to send push notifications using our APIs. Interested users should refer to the reference material <a href="study:system-design/lessons/10-11-step-4-wrap-up/#reference-10-6">[6]</a>.</p>
<p><strong>Monitor queued notifications</strong> A key metric to monitor is the total number of queued notifications. If the number is large, the notification events are not processed fast enough by workers. To avoid delay in the notification delivery, more workers are needed. Figure 10-12 (credit to <a href="study:system-design/lessons/10-11-step-4-wrap-up/#reference-10-7">[7]</a>) shows an example of queued messages to be processed.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-134.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 134" height="226" loading="lazy" src="../../assets/system-design/figure-134.jpeg" width="633"/></a></figure>
<p>Figure 10-12</p>
<p><strong>Events tracking</strong> Notification metrics, such as open rate, click rate, and engagement are important in understanding customer behaviors. Analytics service implements events tracking. Integration between the notification system and the analytics service is usually required. Figure 10-13 shows an example of events that might be tracked for analytics purposes.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-135.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 135" height="497" loading="lazy" src="../../assets/system-design/figure-135.jpeg" width="853"/></a></figure>

## Updated design

<section class="chapter-video" aria-label="Video for Updated design"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Updated design</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Putting everything together, Figure 10-14 shows the updated notification system design.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-136.jpeg" rel="noopener" target="_blank"><img alt="Design a notification system — original diagram 136" height="622" loading="lazy" src="../../assets/system-design/figure-136.jpeg" width="940"/></a></figure>
<p>In this design, many new components are added in comparison with the previous design.</p>
<ul><li>The notification servers are equipped with two more critical features: authentication and rate-limiting.</li><li>We also add a retry mechanism to handle notification failures. If the system fails to send notifications, they are put back in the messaging queue and the workers will retry for a predefined number of times.</li><li>Furthermore, notification templates provide a consistent and efficient notification creation process.</li><li>Finally, monitoring and tracking systems are added for system health checks and future improvements.</li></ul>

## Step 4 - Wrap up

<section class="chapter-video" aria-label="Video for Step 4 - Wrap up"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 4 - Wrap up</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Notifications are indispensable because they keep us posted with important information. It could be a push notification about your favorite movie on Netflix, an email about discounts on new products, or a message about your online shopping payment confirmation.</p>
<p>In this chapter, we described the design of a scalable notification system that supports multiple notification formats: push notification, SMS message, and email. We adopted message queues to decouple system components. </p>
<p>Besides the high-level design, we dug deep into more components and optimizations.</p>
<ul><li>Reliability: We proposed a robust retry mechanism to minimize the failure rate.</li><li>Security: AppKey/appSecret pair is used to ensure only verified clients can send notifications.</li><li>Tracking and monitoring: These are implemented in any stage of a notification flow to capture important stats.</li><li>Respect user settings: Users may opt-out of receiving notifications. Our system checks user settings first before sending notifications.</li><li>Rate limiting: Users will appreciate a frequency capping on the number of notifications they receive.</li></ul>
<p>Congratulations on getting this far! Now give yourself a pat on the back. Good job!</p>

<section class="lesson-references"><h3 id="references-10">References</h3><ol><li id="reference-10-1" value="1">Twilio SMS:  <a href="https://www.twilio.com/sms">https://www.twilio.com/sms</a></li><li id="reference-10-2" value="2">Nexmo SMS: <a href="https://www.nexmo.com/products/sms">https://www.nexmo.com/products/sms</a></li><li id="reference-10-3" value="3">Sendgrid: <a href="https://sendgrid.com/">https://sendgrid.com/</a></li><li id="reference-10-4" value="4">Mailchimp: <a href="https://mailchimp.com/">https://mailchimp.com/</a></li><li id="reference-10-5" value="5">You Cannot Have Exactly-Once Delivery: <a href="https://bravenewgeek.com/you-cannot-haveexactly-once-delivery/">https://bravenewgeek.com/you-cannot-haveexactly-once-delivery/</a></li><li id="reference-10-6" value="6">Security in Push Notifications: <a href="https://cloud.ibm.com/docs/services/mobilepush?">https://cloud.ibm.com/docs/services/mobilepush?</a> topic=mobile-pushnotification-security-in-push-notifications</li><li id="reference-10-7" value="7">RadditMQ: <a href="https://bit.ly/2sotIa6">https://bit.ly/2sotIa6</a></li></ol></section>
