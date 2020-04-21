# System Design from Scratch

## Chapter 1: Introduction to System Design

1.1 Before designing a system, below are the topics that we should be considering before designing any system.  
1.1. Features  
1.1.2. Define API's  
1.1.3. Availability  
1.1.4. Latency  
1.1.5. Scalability  
1.1.6. Durability  
1.1.7. Class Diagram  
1.1.8. Security and Privacy  
1.1.9. Cost effective 

### 1.1.1 Features  
Before designing a system, be clear about the features of the system. If you are appearing for an interview, ask the features to be included to the interviewer.  
For example:  

If you are to develop a chat application, you need to ask if there is only one to one chat or group chat. The level of security required and other features required.

### 1.1.2 Define API's
Once we define the features, we need to come up with the API's. How many API's are needed, when to call those API's and who will call the APIs.

### 1.1.3 Availability
Once we decide upon the API, we need to decide about the availability of the system. Particularly we need to decide upon how available the service should be.
For example: If a service goes down or a data center goes down, what should be the state of the system.

### 1.1.4 Latency
We need to decide upon how fast the system should be. If it is a chat application, the system should be very fast and responsive. Then we need to improve the latency of the system.
One way to improve the latency is by using cache system, CDN.
If it is a mail system, then it can be less responsive than our chat application.

### 1.1.5 Scalability
Once we decide on latency, we need to think about the scalability of the system. Especially on how the system will behave when there are 100 users, or 1000 users, or 1M users.

### 1.1.6 Durability
Now we should think about how durable the system should be. If the system you are designing is a code backup repository service, then the system should be highly durable and the associated security features needed for that data needs to be taken care.

### 1.1.7 Class Diagram
If you are needed to design a parking lot or an elevator system, you need to design the class and how multiple classes interact with each other.
Here the interviewer will be interested in OOP concepts and how effectively you use OOP concepts.

### 1.1.8 Security and Privacy
This is important when we are designing an authentication or credit card storage system.

### 1.1.9 Cost effective
Once we decide upon all the above features, we need to think how cost effective the system will be. Is there any alternative system available that are more cost effective?


### 1.2 Below are the topics to be known before designing a system
1.2.1. Vertical and Horizontal Scaling  
1.2.2. CAP Theorem  
1.2.3. ACID and BASE properties  
1.2.4. Partitioning or Sharding data  
1.2.5. consistent hashing  
1.2.6. Strong vs Eventual Consistency  
1.2.7. Optimistic vs pessimist locking  
1.2.8. Relational vs No SQL DB  
1.2.9. Caching  
1.2.10. Datacenters / Racks/ Hosts  
1.2.11. CPU/Memory/Network Bandwidth  
1.2.12. Random vs sequential read/write on disks  
1.2.13. http vs http2 vs web sockets  
1.2.14. TCP/IP Model  
1.2.15. IPv4 vs IPv6  
1.2.16. TCP vs UDP  
1.2.17. DNS lookup  
1.2.18. HTTPS vs TLS  
1.2.19. Certificate Authority  
1.2.20. Load Balancers  
1.2.21. CDN's  
1.2.22. Design Pattern and Object Oriented design  
1.2.23. Virtual Machines and containers  
1.2.24. Publisher-Subscriber  
1.2.25. Map reduce  
1.2.26. Multithreading, Concurrency, locks, Synchronization.  

### 1.2.1 Vertical and Horizontal Scaling  

If we want to serve more users, then we need to scale our system. We can do it in 2 ways :

1. Vertical Scaling: It refers to adding more memory, RAM, increase the processor speed all in a single host or a computer.

2. Horizontal Scaling: It refers to adding more hosts or computers as the number of users increases.

### 1.2.2 CAP Theorem  
CAP: Consistency, Availability and Partition Tolerance.  
* Consistency: It refers to the read is the most recent write.    
* Availability: It refers to, when user asks for a request, the system should be available to respond.  
* Partition Tolerance: The system should be able to function even if any one node or part of the system fails.  

CAP theorem says that it is only possible to achieve any 2 out of 3 things.  

### 1.2.3 ACID and BASE properties  
* ACID: Atomicity Consistency Isolation Durability
    Acid is for Relational Database.  
* BASE: Basically Available Soft-state Event, Base is for No SQL DB.  

### 1.2.4 Partitioning or Sharding data  

If we have huge amount of data, it is not possible to store all the data in a single DB system. Hence we need to store them in a different systems(nodes). Hence now Sharding of data comes to play. We need to choose to partition the data such that every node of DB is responsible for some of the data of that large amount of data

### 1.2.5 Consistent hashing
Consistent hashing is a way of organizing the key value pair for distributed data. So that when we want to scale the system, data changes due to additional keys will be minimum.

### 1.2.6 Strong vs Eventual Consistency

* Strong consistency refers to the read will have the latest write.
* Eventual consistency refers that the read will have some write, but eventually will have the latest write.
* Strong consistency is used in relational DB.
* No SQL DB can be configured with Strong or Eventual Consistency.

### 1.2.7 Optimistic vs pessimist locking

* In optimist locking, before committing any transaction we check and see if no other system is using the resource.
* In pessimist locking, we acquire lock before committing any transaction.

### 1.2.8 Relational vs No SQL DB

Relational DB will provide ACID properties, but No SQL DB provides high availability and is highly scalable.
Hence Depending on the system, we check and use which fits better.

### 1.2.9 Caching

Caching is frequently used in web-browser, it will store most frequently used data such as css files. Hence when you visit the website, it can be accessed quickly.

### 1.2.10 Datacenters / Racks/ Hosts
* Server: A server is a computer, that is used to serve the requests. Most of the time, a server will serve only one type of request. There are different types of servers like Web server, Proxy server, mail server.
* Racks: Racks is a collection of servers.
* Datacenter: A datacenter is a collection of multiple networking components like servers, routers, switches, firewalls inside a building. Datacenter can be a dedicated building or inside a room. To support these multiple servers and other networking components, they need to be kept cool, hence they need into kept in a AC room.
* Cluster: It is a collection of datacenter.
* Hosts: A host is a computer device; it is used to communicate to another hosts on the network.

### 1.2.11 CPU/Memory/Network Bandwidth

As all the above resources are costly and are limited, they should be effectively utilized. Many big companies, design their own datacenter to further reduce energy costs.

### 1.2.12 Random vs sequential read/write on disks
Sequential read and write are always faster than random read and writes on the disk.

### 1.2.13 http vs http2 vs web sockets

* http: It is a request, reply architecture between client and server.
* http2: It can do multiple requests over a single connection
* web-sockets: It is fully bidirectional communication between client and server.

### 10.2.14 TCP/IP Model
TCP/IP model is used for communicating between different computers or applications over the internet. Any device that is connected to open internet should agree to TCP/IP model.
It has 4 layers:
* Layer 4: Application Layer
* Layer 3: Transport Layer
* Layer 2: Internet Layer
* Layer 1: Link Layer
All the 4 layers performs different functions.

### 10.2.15 IPv4 vs IPv6

Internet Protocol addressing is a way that 2 computers communicate with each other over the internet. Each device that is connected to internet will have an IP address attached to it.
* IPv4: Internet Protocol version 4. It has 2³² ip address in total.
* IPv6: Internet Protocol version 6, as IPv4 address is running out, the technology is moving towards IPv6. It has 2¹²⁸ address.

### 10.2.16 TCP vs UDP

These 2 protocols are used to transfer packets over the internet.
* TCP: It stands for Transmission Control Protocol. It is connection oriented protocol. It guarantees delivery of the packet to the required recipient. Retransmission of lost packets can be done in TCP.
* UDP: It stands for User Datagram Protocol. It is a connection less protocol. The packet reaching to the destination cannot be guaranteed. It is faster than TCP.

### 10.2.17 DNS lookup
Domain Name Lookup service. When you type "harshityadav.in ", then the request goes to DNS which does the translation of the address into an IP address.

### 10.2.18 HTTPS vs TLS
TLS stands for Transport Layer Security, used to secure communication between client and server.
When TLS is used with HTTP, it will become HTTPS.

### 10.2.19 Certificate Authority
A certificate authority is an entity that issues digital certificates. A CA is tasked with identifying the website and ensuring safe data transfer between website and its clients.

### 10.2.20 Load Balancers
Once our application gets more number of visitors, we need to include more application servers to serve those customers. So we place those application servers behind a load-balancer. A load balancer is a server that will be the first point of contact of user request, based on some model it will distribute those requests evenly among the available application server such that no server is overloaded.
Load balancer server will also provide security for DDOS attacks, as those attacks will hit load balancer and application servers will be safe.

### 10.2.21 CDN's

CDN stands for content delivery network. It will help to improve the performance and latency by keeping the requested data near to the user.

### 10.2.22 Design Pattern and Object Oriented design

When developing/coding a system, it is important to follow coding standards. Design pattern will give an implementation idea for commonly occurring problems. Some of the design pattern to know are:

1. Singleton Design Pattern: Here only one instance of the class will be available.
2. Adapter Design Pattern: Here two incompatible elements can transfer data with adapter design pattern.
3. Proxy Design Pattern: It is used in place of another component that can be delivered later.
4. Factory Design Pattern: The concept is to create an object without exposing logic to the client.

Most of the system today will follow Object Oriented Design. This design helps to reuse the same component multiple times, easy to debug and fix the issues. And has many advantages over procedure oriented design.

### 10.2.23 Virtual Machines and containers

Virtual Machine is a software, that gives the user a feel that he is the owner of the hardware. But in reality that hardware will be shared by many users.
Containers: It is a way to run an application along with it's dependency in an isolated environment.

### 10.2.24 Publisher-Subscriber
Publisher Subscriber model is also called as Pub-Sub model in short. In this model, a publisher will broadcast the message without the knowledge of subscriber. A subscriber will be always listening to broadcast topic without the knowledge of who is publishing the message.

### 10.2.25 Map reduce
This concept is used to do distributed and parallel processing of big data.

### 10.2.26 Multithreading, Concurrency, locks, Synchronization.
These concepts are important in multithreading. In Java it comes built-in, while other languages like "c" need to depend upon platform for implementation.

## Topic 1: Microservices Architecture

Topic 1: Microservices Architecture

Before the introduction of Micro Architecture, there was a Monolithic Architecture.
A Monolithic Architecture is like a big box where all the software components are assembled in a tightly packed manner.
It means that all the components of a Monolithic Architecture are interconnected and inter dependent.
For example:
If you visit an online shopping website, they will be having:

1. Products service, where customers can look at the product.
2. Customer service, where customers can seek help to resolve any issues.
3. Cart service, where customers can buy the product.

So when you deploy the application, it will be deployed as a single instance that will be running all the time.
For scaling them, we shall run multiple instances of these application and keep them behind the load balancer.
The only advantage of these kind of application is the deployment will be easy and while scaling the application, you need to run multiple instances of the application which is easy.
But there are many disadvantages for this kind of architecture. Some of them are displayed below:

1. When you have a very large application, it will become difficult to modify and deploy the application without knowing all the dependencies.
2. The development and maintenance of the application will be difficult. As the application size is large, a simple bug fix will require complete analysis of the application.
3. The application memory consumption will be unfair. For example, a chat application will require less amount of CPU usage, but a payment checkout will require quick and immediate CPU resource. But in these kind of application, we cannot divide the CPU resources.
4. Single point of failure. Because all of the application are tightly dependent, if one of the application goes down, entire application will be effected. Hence it will make the application highly unstable.
5. Since all the modules are interdependent, adding new module or adding a new feature for existing module will become difficult.
Hence we shifted towards Microservices Architecture.

### What is a Microservices Architecture?
This architecture is a collection of small autonomous services that together form a complete application.
Here all applications are independent of each other. They communicate through API provided by the applications.
Below are some of the advantages of using Microservices Architecture:

1. Each Microservices can focus on one business logic
2. If any one of the service is down, it will not affect other services, as they are independent of each other.
3. Development and bug fixing is easy, because the developer will focus on only one module.
4. Instead of having a single database, each Microservices will be having its own database, avoiding single point of failure.

Below are some of the features of Microservices:
1. Decoupling: The modules can be easily build, scaled and deployed.
2. Autonomy: Teams can work independently
3. Continuous Delivery

As we have made all the modules as Microservices, each module will communicate with the API provided by other application.
Components involved in Microservice Architecture:

1. API gateway
2. Load Balancer
3. Database
4. Service discovery (Link)

Open-source tools for developing Microservices:
Operating System: CentOS
Container: Docker
Scheduler: Kubernates
Monitoring: Prometheus
Messaging: rabbitMQ
API: POSTMAN
Programming Language: Elixir

Below are some of the companies using Microservices:
Twitter
Netflix
Amazon
Paypal

### Topic 2: Data Sharding
Before going to data sharding, let us understand Single storage and why we moved to data sharding.
Before introduction of distributed systems, we had a single master storage. where in all the data will be dumped in to single DB and all the application traffic used to refer to that database.
But as the application traffic increased, and usually we have more reads than writes, it made more sense to add more database to accommodate more reads. Hence we do read replication. In this model, we take two to three copy of the original database and redirect the traffic to those databases. Usually in this model, the write will go the master (original database) and then the latest data will be copied to other database.
But in the above model, we have solved read delay but we introduced one potential issue. The issue is consistency, how to make use the read is the latest write? So how do we solve this?
We solve the above consist any issue by Data Sharding.
Data sharding is a way to break a large database into smaller DB's, in such a way that we maintain consistency in the database.

#### How do we do this?
Data sharding can be done in a very simple way. Consider we have 3 servers. We break the key into 3 different parts and assign each set of keys to different database.
For example, we have keys from A to Z. we divide the keys into 3 parts, and assign to the serevers below:
Server Key
Server 1 A to F
Server 2 G to N
Server 3 O to z
Hence we shard the data into multiple server, there by increasing the consistency. And each one of the databases will have their own replicated cluster.
Above method of Data Sharding is called as Index based partitioning