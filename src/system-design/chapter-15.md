# Design Google Drive

## Design Google Drive

<section class="chapter-video" aria-label="Video for Design Google Drive"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Design Google Drive</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In recent years, cloud storage services such as Google Drive, Dropbox, Microsoft OneDrive, and Apple iCloud have become very popular. In this chapter, you are asked to design Google Drive.</p>
<p>Let us take a moment to understand Google Drive before jumping into the design. Google Drive is a file storage and synchronization service that helps you store documents, photos, videos, and other files in the cloud. You can access your files from any computer, smartphone, and tablet. You can easily share those files with friends, family, and coworkers <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-1">[1]</a>. Figure 15-1 and 15-2 show what Google drive looks like on a browser and mobile application, respectively.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-211.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 211" height="675" loading="lazy" src="../../assets/system-design/figure-211.jpeg" width="1114"/></a></figure>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-212.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 212" height="717" loading="lazy" src="../../assets/system-design/figure-212.jpeg" width="320"/></a></figure>

## Step 1 - Understand the problem and establish design scope

<section class="chapter-video" aria-label="Video for Step 1 - Understand the problem and establish design scope"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 1 - Understand the problem and establish design scope</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Designing a Google drive is a big project, so it is important to ask questions to narrow down the scope.</p>
<p><strong>Candidate</strong>: What are the most important features? <strong>Interviewer</strong>: Upload and download files, file sync, and notifications.</p>
<p><strong>Candidate</strong>: Is this a mobile app, a web app, or both? <strong>Interviewer</strong>: Both.</p>
<p><strong>Candidate</strong>: What are the supported file formats? <strong>Interviewer</strong>: Any file type.</p>
<p><strong>Candidate</strong>: Do files need to be encrypted? <strong>Interview</strong>: Yes, files in the storage must be encrypted.</p>
<p><strong>Candidate</strong>: Is there a file size limit? <strong>Interview</strong>: Yes, files must be 10 GB or smaller.</p>
<p><strong>Candidate</strong>: How many users does the product have? <strong>Interviewer</strong>: 10M DAU.</p>
<p>In this chapter, we focus on the following features:</p>
<ul><li>Add files. The easiest way to add a file is to drag and drop a file into Google drive.</li><li>Download files.</li><li>Sync files across multiple devices. When a file is added to one device, it is automatically synced to other devices.</li><li>See file revisions.</li><li>Share files with your friends, family, and coworkers</li><li>Send a notification when a file is edited, deleted, or shared with you.</li></ul>
<p>Features not discussed in this chapter include:</p>
<ul><li>Google doc editing and collaboration. Google doc allows multiple people to edit the same document simultaneously. This is out of our design scope.</li></ul>
<p>Other than clarifying requirements, it is important to understand non-functional requirements:</p>
<ul><li>Reliability. Reliability is extremely important for a storage system. Data loss is unacceptable.</li><li>Fast sync speed. If file sync takes too much time, users will become impatient and abandon the product.</li><li>Bandwidth usage. If a product takes a lot of unnecessary network bandwidth, users will be unhappy, especially when they are on a mobile data plan.</li><li>Scalability. The system should be able to handle high volumes of traffic.</li><li>High availability. Users should still be able to use the system when some servers are offline, slowed down, or have unexpected network errors.</li></ul>

## Back of the envelope estimation

<section class="chapter-video" aria-label="Video for Back of the envelope estimation"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Back of the envelope estimation</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<ul><li>Assume the application has 50 million signed up users and 10 million DAU.</li><li>Users get 10 GB free space.</li><li>Assume users upload 2 files per day. The average file size is 500 KB.</li><li>1:1 read to write ratio.</li></ul>
<ul><li>Total space allocated: 50 million * 10 GB = 500 Petabyte</li><li>QPS for upload API: 10 million * 2 uploads / 24 hours / 3600 seconds = ~ 240</li><li>Peak QPS = QPS * 2 = 480</li></ul>

## Step 2 - Propose high-level design and get buy-in

<section class="chapter-video" aria-label="Video for Step 2 - Propose high-level design and get buy-in"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 2 - Propose high-level design and get buy-in</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Instead of showing the high-level design diagram from the beginning, we will use a slightly different approach. We will start with something simple: build everything in a single server. Then, gradually scale it up to support millions of users. By doing this exercise, it will refresh your memory about some important topics covered in the book.</p>
<p>Let us start with a single server setup as listed below:</p>
<ul><li>A web server to upload and download files.</li><li>A database to keep track of metadata like user data, login info, files info, etc.</li><li>A storage system to store files. We allocate 1TB of storage space to store files. We spend a few hours setting up an Apache web server, a MySql database, and a directory called <em>drive/</em> as the root directory to store uploaded files. Under <em>drive/</em> directory, there is a list of directories, known as namespaces. Each namespace contains all the uploaded files for that user. The filename on the server is kept the same as the original file name. Each file or folder can be uniquely identified by joining the namespace and the relative path.</li></ul>
<p>Figure 15-3 shows an example of how the <em>/drive</em> directory looks like on the left side and its expanded view on the right side.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-213.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 213" height="408" loading="lazy" src="../../assets/system-design/figure-213.jpeg" width="797"/></a></figure>

## APIs

<section class="chapter-video" aria-label="Video for APIs"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>APIs</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>What do the APIs look like? We primary need 3 APIs: upload a file, download a file, and get file revisions.</p>
<ol start="1"><li><strong>1. Upload a file to Google Drive</strong> Two types of uploads are supported:</li></ol>
<ul><li>Simple upload. Use this upload type when the file size is small.</li><li>Resumable upload. Use this upload type when the file size is large and there is high chance of network interruption.</li></ul>
<p>Here is an example of resumable upload API: <em>https://api.example.com/files/upload?uploadType=resumable</em></p>
<p>Params:</p>
<ul><li>uploadType=resumable</li><li>data: Local file to be uploaded.</li></ul>
<p>A resumable upload is achieved by the following 3 steps <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-2">[2]</a>:</p>
<ul><li>Send the initial request to retrieve the resumable URL.</li><li>Upload the data and monitor upload state.</li><li>If upload is disturbed, resume the upload.</li></ul>
<ol start="2"><li><strong>2. Download a file from Google Drive</strong> Example API: https://api.example.com/files/download</li></ol>
<p>Params:</p>
<ul><li>path: download file path. Example params: {</li></ul>
<p>"path": "/recipes/soup/best_soup.txt" }</p>
<ol start="3"><li><strong>3. Get file revisions</strong> Example API: https://api.example.com/files/list_revisions</li></ol>
<p>Params:</p>
<ul><li>path: The path to the file you want to get the revision history.</li><li>limit: The maximum number of revisions to return. Example params: {</li></ul>
<p>"path": "/recipes/soup/best_soup.txt", "limit": 20 }</p>
<p>All the APIs require user authentication and use HTTPS. Secure Sockets Layer (SSL) protects data transfer between the client and backend servers.</p>

## Move away from single server

<section class="chapter-video" aria-label="Video for Move away from single server"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Move away from single server</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>As more files are uploaded, eventually you get the space full alert as shown in Figure 15-4.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-214.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 214" height="303" loading="lazy" src="../../assets/system-design/figure-214.jpeg" width="777"/></a></figure>
<p>Only 10 MB of storage space is left! This is an emergency as users cannot upload files anymore. The first solution comes to mind is to shard the data, so it is stored on multiple storage servers. Figure 15-5 shows an example of sharding based on <em>user_id</em> .</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-215.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 215" height="481" loading="lazy" src="../../assets/system-design/figure-215.jpeg" width="673"/></a></figure>
<p>You pull an all-nighter to set up database sharding and monitor it closely. Everything works smoothly again. You have stopped the fire, but you are still worried about potential data losses in case of storage server outage. You ask around and your backend guru friend Frank told you that many leading companies like Netflix and Airbnb use Amazon S3 for storage. “Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance” <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-3">[3]</a>. You decide to do some research to see if it is a good fit.</p>
<p>After a lot of reading, you gain a good understanding of the S3 storage system and decide to store files in S3. Amazon S3 supports same-region and cross-region replication. A region is a geographic area where Amazon web services (AWS) have data centers. As shown in Figure 15-6, data can be replicated on the same-region (left side) and cross-region (right side). Redundant files are stored in multiple regions to guard against data loss and ensure availability. A bucket is like a folder in file systems.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-216.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 216" height="394" loading="lazy" src="../../assets/system-design/figure-216.jpeg" width="940"/></a></figure>
<p>After putting files in S3, you can finally have a good night's sleep without worrying about data losses. To stop similar problems from happening in the future, you decide to do further research on areas you can improve. Here are a few areas you find:</p>
<ul><li>Load balancer: Add a load balancer to distribute network traffic. A load balancer ensures</li></ul>
<p>evenly distributed traffic, and if a web server goes down, it will redistribute the traffic. • Web servers: After a load balancer is added, more web servers can be added/removed easily, depending on the traffic load. • Metadata database: Move the database out of the server to avoid single point of failure. In the meantime, set up data replication and sharding to meet the availability and scalability requirements. • File storage: Amazon S3 is used for file storage. To ensure availability and durability, files are replicated in two separate geographical regions.</p>
<p>After applying the above improvements, you have successfully decoupled web servers, metadata database, and file storage from a single server. The updated design is shown in Figure 15-7.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-217.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 217" height="834" loading="lazy" src="../../assets/system-design/figure-217.jpeg" width="590"/></a></figure>

## Sync conflicts

<section class="chapter-video" aria-label="Video for Sync conflicts"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Sync conflicts</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>For a large storage system like Google Drive, sync conflicts happen from time to time. When two users modify the same file or folder at the same time, a conflict happens. How can we resolve the conflict? Here is our strategy: the first version that gets processed wins, and the version that gets processed later receives a conflict. Figure 15-8 shows an example of a sync conflict.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-218.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 218" height="242" loading="lazy" src="../../assets/system-design/figure-218.jpeg" width="941"/></a></figure>
<p>In Figure 15-8, user 1 and user 2 tries to update the same file at the same time, but user 1’s file is processed by our system first. User 1’s update operation goes through, but, user 2 gets a sync conflict. How can we resolve the conflict for user 2? Our system presents both copies of the same file: user 2’s local copy and the latest version from the server (Figure 15-9). User 2 has the option to merge both files or override one version with the other.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-219.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 219" height="351" loading="lazy" src="../../assets/system-design/figure-219.jpeg" width="1320"/></a></figure>
<p>While multiple users are editing the same document at the same, it is challenging to keep the document synchronized. Interested readers should refer to the reference material <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-4">[4]</a> <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-5">[5]</a>.</p>

## High-level design

<section class="chapter-video" aria-label="Video for High-level design"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>High-level design</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Figure 15-10 illustrates the proposed high-level design. Let us examine each component of the system.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-220.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 220" height="695" loading="lazy" src="../../assets/system-design/figure-220.jpeg" width="875"/></a></figure>
<p><strong>User</strong>: A user uses the application either through a browser or mobile app.</p>
<p><strong>Block servers: </strong>Block servers upload blocks to cloud storage. Block storage, referred to as block-level storage, is a technology to store data files on cloud-based environments. A file can be split into several blocks, each with a unique hash value, stored in our metadata database. Each block is treated as an independent object and stored in our storage system (S3). To reconstruct a file, blocks are joined in a particular order. As for the block size, we use Dropbox as a reference: it sets the maximal size of a block to 4MB <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-6">[6]</a>.</p>
<p><strong>Cloud storage:</strong> A file is split into smaller blocks and stored in cloud storage.</p>
<p><strong>Cold storage: </strong>Cold storage is a computer system designed for storing inactive data, meaning files are not accessed for a long time.</p>
<p><strong>Load balancer</strong>: A load balancer evenly distributes requests among API servers.</p>
<p><strong>API servers: </strong>These are responsible for almost everything other than the uploading flow. API servers are used for user authentication, managing user profile, updating file metadata, etc.</p>
<p><strong>Metadata database: </strong>It stores metadata of users, files, blocks, versions, etc. Please note that files are stored in the cloud and the metadata database only contains metadata.</p>
<p><strong>Metadata cache</strong>: Some of the metadata are cached for fast retrieval. </p>
<p><strong>Notification service</strong>: It is a publisher/subscriber system that allows data to be transferred from notification service to clients as certain events happen. In our specific case, notification service notifies relevant clients when a file is added/edited/removed elsewhere so they can pull the latest changes.</p>
<p><strong>Offline backup queue</strong>: If a client is offline and cannot pull the latest file changes, the offline backup queue stores the info so changes will be synced when the client is online.</p>

<p>We have discussed the design of Google Drive at the high-level. Some of the components are complicated and worth careful examination; we will discuss these in detail in the deep dive.</p>

## Step 3 - Design deep dive

<section class="chapter-video" aria-label="Video for Step 3 - Design deep dive"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 3 - Design deep dive</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this section, we will take a close look at the following: block servers, metadata database, upload flow, download flow, notification service, save storage space and failure handling.</p>

## Block servers

<section class="chapter-video" aria-label="Video for Block servers"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Block servers</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>For large files that are updated regularly, sending the whole file on each update consumes a lot of bandwidth. Two optimizations are proposed to minimize the amount of network traffic being transmitted:</p>
<ul><li>Delta sync. When a file is modified, only modified blocks are synced instead of the whole file using a sync algorithm <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-7">[7]</a> <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-8">[8]</a>.</li><li>Compression. Applying compression on blocks can significantly reduce the data size. Thus, blocks are compressed using compression algorithms depending on file types. For example, gzip and bzip2 are used to compress text files. Different compression algorithms are needed to compress images and videos.</li></ul>
<p>In our system, block servers do the heavy lifting work for uploading files. Block servers process files passed from clients by splitting a file into blocks, compressing each block, and encrypting them. Instead of uploading the whole file to the storage system, only modified blocks are transferred.</p>
<p>Figure 15-11 shows how a block server works when a new file is added.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-221.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 221" height="545" loading="lazy" src="../../assets/system-design/figure-221.jpeg" width="940"/></a></figure>
<ul><li>A file is split into smaller blocks.</li><li>Each block is compressed using compression algorithms.</li><li>To ensure security, each block is encrypted before it is sent to cloud storage.</li><li>Blocks are uploaded to the cloud storage.</li></ul>
<p>Figure 15-12 illustrates delta sync, meaning only modified blocks are transferred to cloud storage. Highlighted blocks “block 2” and “block 5” represent changed blocks. Using delta sync, only those two blocks are uploaded to the cloud storage.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-222.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 222" height="690" loading="lazy" src="../../assets/system-design/figure-222.jpeg" width="792"/></a></figure>
<p>Block servers allow us to save network traffic by providing delta sync and compression.</p>

## High consistency requirement

<section class="chapter-video" aria-label="Video for High consistency requirement"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>High consistency requirement</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Our system requires strong consistency by default. It is unacceptable for a file to be shown differently by different clients at the same time. The system needs to provide strong consistency for metadata cache and database layers.</p>
<p>Memory caches adopt an eventual consistency model by default, which means different replicas might have different data. To achieve strong consistency, we must ensure the following:</p>
<ul><li>Data in cache replicas and the master is consistent.</li><li>Invalidate caches on database write to ensure cache and database hold the same value. Achieving strong consistency in a relational database is easy because it maintains the ACID (Atomicity, Consistency, Isolation, Durability) properties <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-9">[9]</a>. However, NoSQL databases do not support ACID properties by default. ACID properties must be programmatically incorporated in synchronization logic. In our design, we choose relational databases because the ACID is natively supported.</li></ul>

## Metadata database

<section class="chapter-video" aria-label="Video for Metadata database"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Metadata database</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Figure 15-13 shows the database schema design. Please note this is a highly simplified version as it only includes the most important tables and interesting fields.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-223.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 223" height="665" loading="lazy" src="../../assets/system-design/figure-223.jpeg" width="940"/></a></figure>
<p><strong>User</strong>: The user table contains basic information about the user such as username, email, profile photo, etc.</p>
<p><strong>Device</strong>: Device table stores device info. <em>Push_id</em> is used for sending and receiving mobile push notifications. Please note a user can have multiple devices.</p>
<p><strong>Namespace</strong>: A namespace is the root directory of a user.</p>
<p><strong>File: </strong>File table stores everything related to the latest file.</p>
<p><strong>File_version</strong>: It stores version history of a file. Existing rows are read-only to keep the integrity of the file revision history.</p>
<p><strong>Block</strong>: It stores everything related to a file block. A file of any version can be reconstructed by joining all the blocks in the correct order.</p>

## Upload flow

<section class="chapter-video" aria-label="Video for Upload flow"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Upload flow</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Let us discuss what happens when a client uploads a file. To better understand the flow, we draw the sequence diagram as shown in Figure 15-14.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-224.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 224" height="573" loading="lazy" src="../../assets/system-design/figure-224.jpeg" width="940"/></a></figure>
<p>In Figure 15-14, two requests are sent in parallel: add file metadata and upload the file to cloud storage. Both requests originate from client 1.</p>
<ul><li>Add file metadata.  1. Client 1 sends a request to add the metadata of the new file. 2. Store the new file metadata in metadata DB and change the file upload status to “pending.” 3. Notify the notification service that a new file is being added. 4. The notification service notifies relevant clients (client 2) that a file is being uploaded.</li></ul>
<ul><li>Upload files to cloud storage. 2.1 Client 1 uploads the content of the file to block servers. 2.2 Block servers chunk the files into blocks, compress, encrypt the blocks, and upload them to cloud storage. 2.3 Once the file is uploaded, cloud storage triggers upload completion callback. The request is sent to API servers. 2.4 File status changed to “uploaded” in Metadata DB. 2.5 Notify the notification service that a file status is changed to “uploaded.” 2.6 The notification service notifies relevant clients (client 2) that a file is fully uploaded. When a file is edited, the flow is similar, so we will not repeat it.</li></ul>

## Download flow

<section class="chapter-video" aria-label="Video for Download flow"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Download flow</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Download flow is triggered when a file is added or edited elsewhere. How does a client know if a file is added or edited by another client? There are two ways a client can know:</p>
<ul><li>If client A is online while a file is changed by another client, notification service will inform client A that changes are made somewhere so it needs to pull the latest data.</li></ul>
<ul><li>If client A is offline while a file is changed by another client, data will be saved to the cache. When the offline client is online again, it pulls the latest changes.</li></ul>
<p>Once a client knows a file is changed, it first requests metadata via API servers, then downloads blocks to construct the file. Figure 15-15 shows the detailed flow. Note, only the most important components are shown in the diagram due to space constraint.</p>
<figure class="source-figure"><a aria-label="Open diagram at full resolution" href="../../assets/system-design/figure-225.jpeg" rel="noopener" target="_blank"><img alt="Design Google Drive — original diagram 225" height="505" loading="lazy" src="../../assets/system-design/figure-225.jpeg" width="940"/></a></figure>
<ol start="1"><li>Notification service informs client 2 that a file is changed somewhere else.</li><li>Once client 2 knows that new updates are available, it sends a request to fetch metadata.</li><li>API servers call metadata DB to fetch metadata of the changes.</li><li>Metadata is returned to the API servers.</li><li>Client 2 gets the metadata.</li><li>Once the client receives the metadata, it sends requests to block servers to download blocks.</li><li>Block servers first download blocks from cloud storage.</li><li>Cloud storage returns blocks to the block servers.</li><li>Client 2 downloads all the new blocks to reconstruct the file.</li></ol>

## Notification service

<section class="chapter-video" aria-label="Video for Notification service"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Notification service</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>To maintain file consistency, any mutation of a file performed locally needs to be informed to other clients to reduce conflicts. Notification service is built to serve this purpose. At the high-level, notification service allows data to be transferred to clients as events happen. Here are a few options:</p>
<ul><li>Long polling. Dropbox uses long polling <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-10">[10]</a>.</li><li>WebSocket. WebSocket provides a persistent connection between the client and the server. Communication is bi-directional.</li></ul>
<p>Even though both options work well, we opt for long polling for the following two reasons:</p>
<ul><li>Communication for notification service is not bi-directional. The server sends information about file changes to the client, but not vice versa.</li><li>WebSocket is suited for real-time bi-directional communication such as a chat app. For</li></ul>
<p>Google Drive, notifications are sent infrequently with no burst of data.</p>
<p>With long polling, each client establishes a long poll connection to the notification service. If changes to a file are detected, the client will close the long poll connection. Closing the connection means a client must connect to the metadata server to download the latest changes. After a response is received or connection timeout is reached, a client immediately sends a new request to keep the connection open.</p>

## Save storage space

<section class="chapter-video" aria-label="Video for Save storage space"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Save storage space</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>To support file version history and ensure reliability, multiple versions of the same file are stored across multiple data centers. Storage space can be filled up quickly with frequent backups of all file revisions. Three techniques are proposed to reduce storage costs:</p>
<ul><li>De-duplicate data blocks. Eliminating redundant blocks at the account level is an easy way to save space. Two blocks are identical if they have the same hash value.</li><li>Adopt an intelligent data backup strategy. Two optimization strategies can be applied:</li><li>Set a limit: We can set a limit for the number of versions to store. If the limit is reached, the oldest version will be replaced with the new version.</li><li>Keep valuable versions only: Some files might be edited frequently. For example, saving every edited version for a heavily modified document could mean the file is saved over 1000 times within a short period. To avoid unnecessary copies, we could limit the number of saved versions. We give more weight to recent versions. Experimentation is helpful to figure out the optimal number of versions to save.</li><li>Moving infrequently used data to cold storage. Cold data is the data that has not been active for months or years. Cold storage like Amazon S3 glacier <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-11">[11]</a> is much cheaper than S3.</li></ul>

## Failure Handling

<section class="chapter-video" aria-label="Video for Failure Handling"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Failure Handling</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>Failures can occur in a large-scale system and we must adopt design strategies to address these failures. Your interviewer might be interested in hearing about how you handle the following system failures:</p>
<ul><li>Load balancer failure: If a load balancer fails, the secondary would become active and pick up the traffic. Load balancers usually monitor each other using a heartbeat, a periodic signal sent between load balancers. A load balancer is considered as failed if it has not sent a heartbeat for some time.</li><li>Block server failure: If a block server fails, other servers pick up unfinished or pending jobs.</li><li>Cloud storage failure: S3 buckets are replicated multiple times in different regions. If files are not available in one region, they can be fetched from different regions.</li><li>API server failure: It is a stateless service. If an API server fails, the traffic is redirected to other API servers by a load balancer.</li><li>Metadata cache failure: Metadata cache servers are replicated multiple times. If one node goes down, you can still access other nodes to fetch data. We will bring up a new cache server to replace the failed one.</li><li>Metadata DB failure.</li><li>Master down: If the master is down, promote one of the slaves to act as a new master and bring up a new slave node.</li><li>Slave down: If a slave is down, you can use another slave for read operations and</li></ul>
<p>bring another database server to replace the failed one.               • Notification service failure: Every online user keeps a long poll connection with the notification server. Thus, each notification server is connected with many users. According to the Dropbox talk in 2012 <a href="study:system-design/lessons/15-18-step-4-wrap-up/#reference-15-6">[6]</a>, over 1 million connections are open per machine. If a server goes down, all the long poll connections are lost so clients must reconnect to a different server. Even though one server can keep many open connections, it cannot reconnect all the lost connections at once. Reconnecting with all the lost clients is a relatively slow process.    • Offline backup queue failure: Queues are replicated multiple times. If one queue fails, consumers of the queue may need to re-subscribe to the backup queue.</p>

## Step 4 - Wrap up

<section class="chapter-video" aria-label="Video for Step 4 - Wrap up"><span class="video-play" aria-hidden="true">▷</span><div><span class="eyebrow">SECTION VIDEO</span><strong>Step 4 - Wrap up</strong><p>Video coming soon. Start with the reading below.</p></div><span class="video-coming">COMING SOON</span></section>

<p>In this chapter, we proposed a system design to support Google Drive. The combination of strong consistency, low network bandwidth and fast sync make the design interesting. Our design contains two flows: manage file metadata and file sync. Notification service is another important component of the system. It uses long polling to keep clients up to date with file changes.  </p>
<p>Like any system design interview questions, there is no perfect solution. Every company has its unique constraints and you must design a system to fit those constraints. Knowing the tradeoffs of your design and technology choices are important. If there are a few minutes left, you can talk about different design choices.</p>
<p>For example, we can upload files directly to cloud storage from the client instead of going through block servers. The advantage of this approach is that it makes file upload faster because a file only needs to be transferred once to the cloud storage. In our design, a file is transferred to block servers first, and then to the cloud storage. However, the new approach has a few drawbacks:</p>
<ul><li>First, the same chunking, compression, and encryption logic must be implemented on different platforms (iOS, Android, Web). It is error-prone and requires a lot of engineering effort. In our design, all those logics are implemented in a centralized place: block servers.</li><li>Second, as a client can easily be hacked or manipulated, implementing encrypting logic on the client side is not ideal.</li></ul>
<p>Another interesting evolution of the system is moving online/offline logic to a separate service. Let us call it presence service. By moving presence service out of notification servers, online/offline functionality can easily be integrated by other services.</p>
<p>Congratulations on getting this far! Now give yourself a pat on the back. Good job!</p>

<section class="lesson-references"><h3 id="references-15">References</h3><ol><li id="reference-15-1" value="1">Google Drive: <a href="https://www.google.com/drive/">https://www.google.com/drive/</a></li><li id="reference-15-2" value="2">Upload file data: <a href="https://developers.google.com/drive/api/v2/manage-uploads">https://developers.google.com/drive/api/v2/manage-uploads</a></li><li id="reference-15-3" value="3">Amazon S3: <a href="https://aws.amazon.com/s3">https://aws.amazon.com/s3</a></li><li id="reference-15-4" value="4">Differential Synchronization <a href="https://neil.fraser.name/writing/sync/">https://neil.fraser.name/writing/sync/</a></li><li id="reference-15-5" value="5">Differential Synchronization youtube talk <a href="https://www.youtube.com/watch?">https://www.youtube.com/watch?</a> v=S2Hp_1jqpY8</li><li id="reference-15-6" value="6">How We’ve Scaled Dropbox: <a href="https://youtu.be/PE4gwstWhmc">https://youtu.be/PE4gwstWhmc</a></li><li id="reference-15-7" value="7">Tridgell, A., &amp; Mackerras, P. (1996). The rsync algorithm.</li><li id="reference-15-8" value="8">Librsync. (n.d.). Retrieved April 18, 2015, from <a href="https://github.com/librsync/librsync">https://github.com/librsync/librsync</a></li><li id="reference-15-9" value="9">ACID:  <a href="https://en.wikipedia.org/wiki/ACID">https://en.wikipedia.org/wiki/ACID</a></li><li id="reference-15-10" value="10">Dropbox security white paper: <a href="https://www.dropbox.com/static/business/resources/Security_Whitepaper.pdf">https://www.dropbox.com/static/business/resources/Security_Whitepaper.pdf</a></li><li id="reference-15-11" value="11">Amazon S3 Glacier: <a href="https://aws.amazon.com/glacier/faqs/">https://aws.amazon.com/glacier/faqs/</a></li></ol></section>
