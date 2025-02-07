[Basics](#basics)

[Load balancer](#load-balancer)
[Proxies](#proxies)
[CDN Content delivery network](#cdn-content-delivery-network)
[DNS Domain Name System](#dns-domain-name-system)
[Network Communications](#network-communications)
[Client-Server Communications](#client-server-communications)

[Caching](#caching)
[Storage](#storage)
[Database](#database)
[Stateless and Stateful Services](#stateless-and-stateful-services)
[Data Structures Behind Databases](#data-structures-behind-databases)
[Databases Replication](#databases-replication)
[Databases Partitioning](#databases-partitioning)
[Consistent hashing](#38-consistent-hashing)
[Indexing](#indexing)

[Paging and filtering](#paging-and-filtering)
[Bloom filter](#bloom-filter)
[Quorum](#quorum)
[Master-Slave](#master-slave)

[Data Flow](#data-flow)
[Message Queue](#message-queue)
[Batch processing](#batch-processing)
[Stream Processing](#stream-processing)
[Patterns](#patterns)

[Throughput and Latency](#throughput-and-latency)
[CAP Consistency, Availability, Partition tolenrance](#cap-consistency-availability-partition-tolenrance)
[PACELC Partition, Availability, Consistency, Else, Latency, and Consistency](#pacelc-partition-availability-consistency-else-latency-and-consistency)
[Resiliency](#resiliency)
[Availability patterns](#availability-patterns)
[Consistency patterns](#consistency-patterns)

[Rate limiting](#rate-limiting)
[Logging and monitoring](#logging-and-monitoring)
[Security](#security)
[Asynchronism](#asynchronism)
[Application Layer](#application-layer)
[Microservice](#microservices)

## What you need to know for the following system design concepts:

- what it is?
- how to use it?
- advantages?
- use cases?
- example tools if any?

### Basics

#### **System Design Interview Course**

- **Project:** Enroll in a comprehensive system design course.
- **Resources:** [System Design Primer](https://github.com/donnemartin/system-design-primer)

#### **Study Guide**

- **Project:** Compile a study guide with key topics, resources, and practice problems.
- **Resources:** [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview)

### Load balancer

Load balancers distribute incoming client requests to computing resources such as application servers and databases. In each case, the load balancer returns the response from the computing resource to the appropriate client. Load balancers are effective at:

- Preventing requests from going to unhealthy servers
- Preventing overloading resources
- Helping to eliminate a single point of failure

Load balancers can be implemented with hardware (expensive) or with software such as HAProxy.

Additional benefits include:

- **SSL termination** - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
  - Removes the need to install [X.509 certificates](https://en.wikipedia.org/wiki/X.509) on each server
- **Session persistence** - Issue cookies and route a specific client's requests to same instance if the web apps do not keep track of sessions

To protect against failures, it's common to set up multiple load balancers, either in [active-passive](#active-passive) or [active-active](#active-active) mode.

Load balancers can route traffic based on various metrics, including:

- Random
- Least loaded
- Session/cookies
- [Layer 4](#layer-4-load-balancing)
- [Layer 7](#layer-7-load-balancing)
- [Load balancing algorithms](https://aws.amazon.com/what-is/load-balancing/)

#### Layer 4 load balancing

Layer 4 load balancers look at info at the [transport layer](#communication) to decide how to distribute requests. Generally, this involves the source, destination IP addresses, and ports in the header, but not the contents of the packet. Layer 4 load balancers forward network packets to and from the upstream server, performing [Network Address Translation (NAT)](https://www.geeksforgeeks.org/network-address-translation-nat/).

#### Layer 7 load balancing

Layer 7 load balancers look at the [application layer](#communication) to decide how to distribute requests. This can involve contents of the header, message, and cookies. Layer 7 load balancers terminate network traffic, reads the message, makes a load-balancing decision, then opens a connection to the selected server. For example, a layer 7 load balancer can direct video traffic to servers that host videos while directing more sensitive user billing traffic to security-hardened servers.

At the cost of flexibility, layer 4 load balancing requires less time and computing resources than Layer 7, although the performance impact can be minimal on modern commodity hardware.

#### Disadvantage(s): load balancer

- The load balancer can become a performance bottleneck if it does not have enough resources or if it is not configured properly.
- Introducing a load balancer to help eliminate a single point of failure results in increased complexity.
- A single load balancer is a single point of failure, configuring multiple load balancers further increases complexity.

#### Load balancer vs reverse proxy

- Deploying a load balancer is useful when you have multiple servers. Often, load balancers route traffic to a set of servers serving the same function.
- Reverse proxies can be useful even with just one web server or application server, opening up the benefits described in the previous section.
- Solutions such as NGINX and HAProxy can support both layer 7 reverse proxying and load balancing.

### Proxies

A reverse proxy is a web server that centralizes internal services and provides unified interfaces to the public. Requests from clients are forwarded to a server that can fulfill it before the reverse proxy returns the server's response to the client.

Additional benefits include:

- **Increased security** - Hide information about backend servers, blacklist IPs, limit number of connections per client
- **Increased scalability and flexibility** - Clients only see the reverse proxy's IP, allowing you to scale servers or change their configuration
- **SSL termination** - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
  - Removes the need to install [X.509 certificates](https://en.wikipedia.org/wiki/X.509) on each server
- **Compression** - Compress server responses
- **Caching** - Return the response for cached requests
- **Static content** - Serve static content directly
  - HTML/CSS/JS
  - Photos
  - Videos
  - Etc

#### Disadvantage(s): reverse proxy

- Introducing a reverse proxy results in increased complexity.
- A single reverse proxy is a single point of failure, configuring multiple reverse proxies a failover further increases complexity.

### CDN Content delivery network

A content delivery network (CDN) is a globally distributed network of proxy servers, serving content from locations closer to the user. Generally, static files such as HTML/CSS/JS, photos, and videos are served from CDN, although some CDNs such as Amazon's CloudFront support dynamic content. The site's DNS resolution will tell clients which server to contact.

Serving content from CDNs can significantly improve performance in two ways:

- Users receive content from data centers close to them
- Your servers do not have to serve requests that the CDN fulfills

#### Push CDNs

Push CDNs receive new content whenever changes occur on your server. You take full responsibility for providing content, uploading directly to the CDN and rewriting URLs to point to the CDN. You can configure when content expires and when it is updated. Content is uploaded only when it is new or changed, minimizing traffic, but maximizing storage.

Sites with a small amount of traffic or sites with content that isn't often updated work well with push CDNs. Content is placed on the CDNs once, instead of being re-pulled at regular intervals.

#### Pull CDNs

Pull CDNs grab new content from your server when the first user requests the content. You leave the content on your server and rewrite URLs to point to the CDN. This results in a slower request until the content is cached on the CDN.

A [time-to-live (TTL)](https://en.wikipedia.org/wiki/Time_to_live) determines how long content is cached. Pull CDNs minimize storage space on the CDN, but can create redundant traffic if files expire and are pulled before they have actually changed.

Sites with heavy traffic work well with pull CDNs, as traffic is spread out more evenly with only recently-requested content remaining on the CDN.

#### Disadvantage(s): CDN

- CDN costs could be significant depending on traffic, although this should be weighed with additional costs you would incur not using a CDN.
- Content might be stale if it is updated before the TTL expires it.
- CDNs require changing URLs for static content to point to the CDN.

### DNS Domain Name System

A Domain Name System (DNS) translates a domain name such as www.example.com to an IP address.

DNS is hierarchical, with a few authoritative servers at the top level. Your router or ISP provides information about which DNS server(s) to contact when doing a lookup. Lower level DNS servers cache mappings, which could become stale due to DNS propagation delays. DNS results can also be cached by your browser or OS for a certain period of time, determined by the `time to live (TTL)`

- **NS record (name server)** - Specifies the DNS servers for your domain/subdomain.
- **MX record (mail exchange)** - Specifies the mail servers for accepting messages.
- **A record (address)** - Points a name to an IP address.
- **CNAME (canonical)** - Points a name to another name or `CNAME` (example.com to www.example.com) or to an `A` record.

Services such as **`CloudFlare`** and **`AWS Route 53`** provide managed DNS services. Some DNS services can route traffic through various methods:

#### Disadvantage(s): DNS

- Accessing a DNS server introduces a slight delay, although mitigated by caching described above.
- DNS server management could be complex and is generally managed by governments, ISPs, and large companies.
- DNS services have recently come under DDoS attack, preventing users from accessing websites such as Twitter without knowing Twitter's IP address(es).

### Network Communications

#### Hypertext transfer protocol (HTTP)

HTTP is a method for encoding and transporting data between a client and a server. It is a request/response protocol: clients issue requests and servers issue responses with relevant content and completion status info about the request. HTTP is self-contained, allowing requests and responses to flow through many intermediate routers and servers that perform load balancing, caching, encryption, and compression.

A basic HTTP request consists of a verb (method) and a resource (endpoint). Below are common HTTP verbs:

| Verb   | Description                                               | Idempotent\* | Safe | Cacheable                               |
| ------ | --------------------------------------------------------- | ------------ | ---- | --------------------------------------- |
| GET    | Reads a resource                                          | Yes          | Yes  | Yes                                     |
| POST   | Creates a resource or trigger a process that handles data | No           | No   | Yes if response contains freshness info |
| PUT    | Creates or replace a resource                             | Yes          | No   | No                                      |
| PATCH  | Partially updates a resource                              | No           | No   | Yes if response contains freshness info |
| DELETE | Deletes a resource                                        | Yes          | No   | No                                      |

\*Can be called many times without different outcomes.

HTTP is an application layer protocol relying on lower-level protocols such as **TCP** and **UDP**.

#### Transmission control protocol (TCP)

TCP is a connection-oriented protocol over an IP network. Connection is established and terminated using a handshake. All packets sent are guaranteed to reach the destination in the original order and without corruption through:

- Sequence numbers and checksum fields for each packet
- Acknowledgement packets and automatic retransmission

If the sender does not receive a correct response, it will resend the packets. If there are multiple timeouts, the connection is dropped. TCP also implements `flow control` and `congestion control`. These guarantees cause delays and generally result in less efficient transmission than UDP.

To ensure high throughput, web servers can keep a large number of TCP connections open, resulting in high memory usage. It can be expensive to have a large number of open connections between web server threads and say, a `memcached` server. `Connection pooling` can help in addition to switching to UDP where applicable.

TCP is useful for applications that require high reliability but are less time critical. Some examples include web servers, database info, SMTP, FTP, and SSH.

Use TCP over UDP when:

- You need all of the data to arrive intact
- You want to automatically make a best estimate use of the network throughput

#### User datagram protocol (UDP)

UDP is connectionless. Datagrams (analogous to packets) are guaranteed only at the datagram level. Datagrams might reach their destination out of order or not at all. UDP does not support congestion control. Without the guarantees that TCP support, UDP is generally more efficient.

UDP can broadcast, sending datagrams to all devices on the subnet. This is useful with `DHCP` because the client has not yet received an IP address, thus preventing a way for TCP to stream without the IP address.

UDP is less reliable but works well in real time use cases such as VoIP, video chat, streaming, and realtime multiplayer games.

Use UDP over TCP when:

- You need the lowest latency
- Late data is worse than loss of data
- You want to implement your own error correction

#### Remote procedure call (RPC)

In an RPC, a client causes a procedure to execute on a different address space, usually a remote server. The procedure is coded as if it were a local procedure call, abstracting away the details of how to communicate with the server from the client program. Remote calls are usually slower and less reliable than local calls so it is helpful to distinguish RPC calls from local calls. Popular RPC frameworks include Protobuf, and Apache Avro.

RPC is a request-response protocol:

- **Client program** - Calls the client stub procedure. The parameters are pushed onto the stack like a local procedure call.
- **Client stub procedure** - Marshals (packs) procedure id and arguments into a request message.
- **Client communication module** - OS sends the message from the client to the server.
- **Server communication module** - OS passes the incoming packets to the server stub procedure.
- **Server stub procedure** - Unmarshalls the results, calls the server procedure matching the procedure id and passes the given arguments.
- The server response repeats the steps above in reverse order.

Sample RPC calls:

```
GET /someoperation?data=anId

POST /anotheroperation
{
  "data":"anId";
  "anotherdata": "another value"
}
```

RPC is focused on exposing behaviors. RPCs are often used for performance reasons with internal communications, as you can hand-craft native calls to better fit your use cases.

Choose a native library (aka SDK) when:

- You know your target platform.
- You want to control how your "logic" is accessed.
- You want to control how error control happens off your library.
- Performance and end user experience is your primary concern.

HTTP APIs following **REST** tend to be used more often for public APIs.

##### Disadvantage(s): RPC

- RPC clients become tightly coupled to the service implementation.
- A new API must be defined for every new operation or use case.
- It can be difficult to debug RPC.
- You might not be able to leverage existing technologies out of the box. For example, it might require additional effort to ensure RPC calls are properly cached on caching servers such as Squid.

#### Representational state transfer (REST)

REST is an architectural style enforcing a client/server model where the client acts on a set of resources managed by the server. The server provides a representation of resources and actions that can either manipulate or get a new representation of resources. All communication must be stateless and cacheable.

There are four qualities of a RESTful interface:

- **Identify resources (URI in HTTP)** - use the same URI regardless of any operation.
- **Change with representations (Verbs in HTTP)** - use verbs, headers, and body.
- **Self-descriptive error message (status response in HTTP)** - Use status codes, don't reinvent the wheel.
- **HATEOAS (HTML interface for HTTP)** - your web service should be fully accessible in a browser.

Sample REST calls:

```
GET /someresources/anId

PUT /someresources/anId
{"anotherdata": "another value"}
```

REST is focused on exposing data. It minimizes the coupling between client/server and is often used for public HTTP APIs. REST uses a more generic and uniform method of exposing resources through URIs, representation through headers, and actions through verbs such as GET, POST, PUT, DELETE, and PATCH. Being stateless, REST is great for horizontal scaling and partitioning.

##### Disadvantage(s): REST

- With REST being focused on exposing data, it might not be a good fit if resources are not naturally organized or accessed in a simple hierarchy. For example, returning all updated records from the past hour matching a particular set of events is not easily expressed as a path. With REST, it is likely to be implemented with a combination of URI path, query parameters, and possibly the request body.
- REST typically relies on a few verbs (GET, POST, PUT, DELETE, and PATCH) which sometimes doesn't fit your use case. For example, moving expired documents to the archive folder might not cleanly fit within these verbs.
- Fetching complicated resources with nested hierarchies requires multiple round trips between the client and server to render single views, e.g. fetching content of a blog entry and the comments on that entry. For mobile applications operating in variable network conditions, these multiple roundtrips are highly undesirable.
- Over time, more fields might be added to an API response and older clients will receive all new data fields, even those that they do not need, as a result, it bloats the payload size and leads to larger latencies.

#### RPC and REST calls comparison

| Operation                       | RPC                                                                                       | REST                                                         |
| ------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Signup                          | **POST** /signup                                                                          | **POST** /persons                                            |
| Resign                          | **POST** /resign<br/>{<br/>"personid": "1234"<br/>}                                       | **DELETE** /persons/1234                                     |
| Read a person                   | **GET** /readPerson?personid=1234                                                         | **GET** /persons/1234                                        |
| Read a person’s items list      | **GET** /readUsersItemsList?personid=1234                                                 | **GET** /persons/1234/items                                  |
| Add an item to a person’s items | **POST** /addItemToUsersItemsList<br/>{<br/>"personid": "1234";<br/>"itemid": "456"<br/>} | **POST** /persons/1234/items<br/>{<br/>"itemid": "456"<br/>} |
| Update an item                  | **POST** /modifyItem<br/>{<br/>"itemid": "456";<br/>"key": "value"<br/>}                  | **PUT** /items/456<br/>{<br/>"key": "value"<br/>}            |
| Delete an item                  | **POST** /removeItem<br/>{<br/>"itemid": "456"<br/>}                                      | **DELETE** /items/456                                        |

### Client-Server Communications

#### 69. **REST API**

- client to server communication

#### 70. **GraphQL**

- client to server communication

#### 71. **Websocket**

- client to server communication

#### 72. **gRPC**

- server to server communication
- client to server communication (web gRPC)

#### 73. **polling**

- network monitoring
- server monitoring
- database monitoring

**strategies**

- fix interval polling
- event-driven polling
- Asynchronous Polling
- grouped Polling
- Threshold-Based Polling
- Exponential Backoff

#### 74. **Server sent event (SSE)**

- a type of server push technology that establishes a long-lasting connection between the client and the server.

### Caching

Caching improves page load times and can reduce the load on your servers and databases. In this model, the dispatcher will first lookup if the request has been made before and try to find the previous result to return, in order to save the actual execution.

Databases often benefit from a uniform distribution of reads and writes across its partitions. Popular items can skew the distribution, causing bottlenecks. Putting a cache in front of a database can help absorb uneven loads and spikes in traffic.

#### Client caching

Caches can be located on the client side (OS or browser), [server side](#reverse-proxy-web-server), or in a distinct cache layer.

#### CDN caching

[CDNs](#content-delivery-network) are considered a type of cache.

#### Web server caching

[Reverse proxies](#reverse-proxy-web-server) and caches such as Varnish can serve static and dynamic content directly. Web servers can also cache requests, returning responses without having to contact application servers.

#### Database caching

Your database usually includes some level of caching in a default configuration, optimized for a generic use case. Tweaking these settings for specific usage patterns can further boost performance.

#### Application caching

In-memory caches such as Memcached and Redis are key-value stores between your application and your data storage. Since the data is held in RAM, it is much faster than typical databases where data is stored on disk. RAM is more limited than disk, so cache invalidation algorithms such as least recently used (LRU) can help invalidate 'cold' entries and keep 'hot' data in RAM.

Redis has the following additional features:

- Persistence option
- Built-in data structures such as sorted sets and lists

There are multiple levels you can cache that fall into two general categories: **database queries** and **objects**:

- Row level
- Query-level
- Fully-formed serializable objects
- Fully-rendered HTML

Generally, you should try to avoid file-based caching, as it makes cloning and auto-scaling more difficult.

#### Caching at the database query level

Whenever you query the database, hash the query as a key and store the result to the cache. This approach suffers from expiration issues:

- Hard to delete a cached result with complex queries
- If one piece of data changes such as a table cell, you need to delete all cached queries that might include the changed cell

#### Caching at the object level

See your data as an object, similar to what you do with your application code. Have your application assemble the dataset from the database into a class instance or a data structure(s):

- Remove the object from cache if its underlying data has changed
- Allows for asynchronous processing: workers assemble objects by consuming the latest cached object

Suggestions of what to cache:

- User sessions
- Fully rendered web pages
- Activity streams
- User graph data

#### When to update the cache

Since you can only store a limited amount of data in cache, you'll need to determine which cache update strategy works best for your use case.

#### Cache-aside (Caching Strategy)

The application is responsible for reading and writing from storage. The cache does not interact with storage directly. The application does the following:

- Look for entry in cache, resulting in a cache miss
- Load entry from the database
- Add entry to cache
- Return entry

```python
def get_user(self, user_id):
    user = cache.get("user.{0}", user_id)
    if user is None:
        user = db.query("SELECT * FROM users WHERE user_id = {0}", user_id)
        if user is not None:
            key = "user.{0}".format(user_id)
            cache.set(key, json.dumps(user))
    return user
```

Memcached is generally used in this manner.

Subsequent reads of data added to cache are fast. Cache-aside is also referred to as lazy loading. Only requested data is cached, which avoids filling up the cache with data that isn't requested.

##### Disadvantage(s): cache-aside

- Each cache miss results in three trips, which can cause a noticeable delay.
- Data can become stale if it is updated in the database. This issue is mitigated by setting a time-to-live (TTL) which forces an update of the cache entry, or by using write-through.
- When a node fails, it is replaced by a new, empty node, increasing latency.

#### Write-through (Caching Strategy)

The application uses the cache as the main data store, reading and writing data to it, while the cache is responsible for reading and writing to the database:

- Application adds/updates entry in cache
- Cache synchronously writes entry to data store
- Return

Application code:

```python
set_user(12345, {"foo":"bar"})
```

Cache code:

```python
def set_user(user_id, values):
    user = db.query("UPDATE Users WHERE id = {0}", user_id, values)
    cache.set(user_id, user)
```

Write-through is a slow overall operation due to the write operation, but subsequent reads of just written data are fast. Users are generally more tolerant of latency when updating data than reading data. Data in the cache is not stale.

##### Disadvantage(s): write through

- When a new node is created due to failure or scaling, the new node will not cache entries until the entry is updated in the database. Cache-aside in conjunction with write through can mitigate this issue.
- Most data written might never be read, which can be minimized with a TTL.

#### Write-behind (write-back) (Caching Strategy)

In write-behind, the application does the following:

- Add/update entry in cache
- Asynchronously write entry to the data store, improving write performance

##### Disadvantage(s): write-behind

- There could be data loss if the cache goes down prior to its contents hitting the data store.
- It is more complex to implement write-behind than it is to implement cache-aside or write-through.

#### Refresh-ahead (Caching Strategy)

You can configure the cache to automatically refresh any recently accessed cache entry prior to its expiration.

Refresh-ahead can result in reduced latency vs read-through if the cache can accurately predict which items are likely to be needed in the future.

##### Disadvantage(s): refresh-ahead

- Not accurately predicting which items are likely to be needed in the future can result in reduced performance than without refresh-ahead.

#### Caching Scaling (Caching Strategy)

- **Project:** Scale a caching solution for a high-traffic application.

#### Caching TTL (Caching Strategy)

- **Project:** Implement TTL for cache entries to manage freshness.

#### Disadvantage(s): cache

- Need to maintain consistency between caches and the source of truth such as the database through Cache invalidation.
- Cache invalidation is a difficult problem, there is additional complexity associated with when to update the cache.
- Need to make application changes such as adding Redis or memcached.

### Storage

#### 23. **Introduction to Storage**

- **Project:** Overview of different storage systems with hands-on examples.
- **Resources:** [Introduction to Storage](https://www.ibm.com/docs/en/baw/19.x?topic=architecture-storage-overview)

#### 24. **SQL Database**

- **Project:** Design and implement a relational database.
- **Resources:** [MySQL Tutorial](https://dev.mysql.com/doc/mysql-getting-started/en/)

#### 25. **Introduction to NoSQL Databases**

- **Project:** Compare and contrast different NoSQL databases.
- **Resources:** [NoSQL Databases Explained](https://www.mongodb.com/nosql-explained)

#### 26. **Key-value Database**

- **Project:** Implement a key-value store.
- **Resources:** [Redis Documentation](https://redis.io/documentation)

#### 27. **Document Database**

- **Project:** Design a document database for a sample application.
- **Resources:** [MongoDB Documentation](https://docs.mongodb.com/)

#### 28. **Full-text Search Database**

- **Project:** Implement full-text search using Elasticsearch.
- **Resources:** [Elasticsearch Guide](https://www.elastic.co/guide/index.html)

#### 29. **OLTP or OLAP?**

- **Project:** Set up and compare an OLTP system with an OLAP system.
- **Resources:** [OLTP vs OLAP](https://www.ibm.com/cloud/blog/oltp-vs-olap)

#### 30. **Blob/Object Storage**

- **Project:** Use AWS S3 for storing and retrieving large objects.
- **Resources:** [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)

### Database

#### Relational database management system (RDBMS)

A relational database like SQL is a collection of data items organized in tables.

**ACID** is a set of properties of relational database transactions.

- **Atomicity** - Each transaction is all or nothing
- **Consistency** - Any transaction will bring the database from one valid state to another
- **Isolation** - Executing transactions concurrently has the same results as if the transactions were executed serially
- **Durability** - Once a transaction has been committed, it will remain so

There are many techniques to scale a relational database: **master-slave replication**, **master-master replication**, **federation**, **sharding**, **denormalization**, and **SQL tuning**.

##### Master-slave replication

The master serves reads and writes, replicating writes to one or more slaves, which serve only reads. Slaves can also replicate to additional slaves in a tree-like fashion. If the master goes offline, the system can continue to operate in read-only mode until a slave is promoted to a master or a new master is provisioned.

###### Disadvantage(s): master-slave replication

- Additional logic is needed to promote a slave to a master.
- See [Disadvantage(s): replication](#disadvantages-replication) for points related to **both** master-slave and master-master.

##### Master-master replication

Both masters serve reads and writes and coordinate with each other on writes. If either master goes down, the system can continue to operate with both reads and writes.

###### Disadvantage(s): master-master replication

- You'll need a load balancer or you'll need to make changes to your application logic to determine where to write.
- Most master-master systems are either loosely consistent (violating ACID) or have increased write latency due to synchronization.
- Conflict resolution comes more into play as more write nodes are added and as latency increases.
- See [Disadvantage(s): replication](#disadvantages-replication) for points related to **both** master-slave and master-master.

##### Disadvantage(s): replication

- There is a potential for loss of data if the master fails before any newly written data can be replicated to other nodes.
- Writes are replayed to the read replicas. If there are a lot of writes, the read replicas can get bogged down with replaying writes and can't do as many reads.
- The more read slaves, the more you have to replicate, which leads to greater replication lag.
- On some systems, writing to the master can spawn multiple threads to write in parallel, whereas read replicas only support writing sequentially with a single thread.
- Replication adds more hardware and additional complexity.

##### Federation

Federation (or functional partitioning) splits up databases by function. For example, instead of a single, monolithic database, you could have three databases: **forums**, **users**, and **products**, resulting in less read and write traffic to each database and therefore less replication lag. Smaller databases result in more data that can fit in memory, which in turn results in more cache hits due to improved cache locality. With no single central master serializing writes you can write in parallel, increasing throughput.

###### Disadvantage(s): federation

- Federation is not effective if your schema requires huge functions or tables.
- You'll need to update your application logic to determine which database to read and write.
- Joining data from two databases is more complex with a server link.
- Federation adds more hardware and additional complexity.

##### Sharding

Sharding distributes data across different databases such that each database can only manage a subset of the data. Taking a users database as an example, as the number of users increases, more shards are added to the cluster.

Similar to the advantages of [federation](#federation), sharding results in less read and write traffic, less replication, and more cache hits. Index size is also reduced, which generally improves performance with faster queries. If one shard goes down, the other shards are still operational, although you'll want to add some form of replication to avoid data loss. Like federation, there is no single central master serializing writes, allowing you to write in parallel with increased throughput.

Common ways to shard a table of users is either through the user's last name initial or the user's geographic location.

###### Disadvantage(s): sharding

- You'll need to update your application logic to work with shards, which could result in complex SQL queries.
- Data distribution can become lopsided in a shard. For example, a set of power users on a shard could result in increased load to that shard compared to others.
  - Rebalancing adds additional complexity. A sharding function based on consistent hashing can reduce the amount of transferred data.
- Joining data from multiple shards is more complex.
- Sharding adds more hardware and additional complexity.

##### Denormalization

Denormalization attempts to improve read performance at the expense of some write performance. Redundant copies of the data are written in multiple tables to avoid expensive joins. Some RDBMS such as PostgreSQL and Oracle support materialized views which handle the work of storing redundant information and keeping redundant copies consistent.

Once data becomes distributed with techniques such as [federation](#federation) and [sharding](#sharding), managing joins across data centers further increases complexity. Denormalization might circumvent the need for such complex joins.

In most systems, reads can heavily outnumber writes 100:1 or even 1000:1. A read resulting in a complex database join can be very expensive, spending a significant amount of time on disk operations.

###### Disadvantage(s): denormalization

- Data is duplicated.
- Constraints can help redundant copies of information stay in sync, which increases complexity of the database design.
- A denormalized database under heavy write load might perform worse than its normalized counterpart.

##### SQL tuning

SQL tuning is a broad topic and many books have been written as reference.

It's important to **benchmark** and **profile** to simulate and uncover bottlenecks.

- **Benchmark** - Simulate high-load situations with tools such as ab.
- **Profile** - Enable tools such as the slow query log to help track performance issues.

Benchmarking and profiling might point you to the following optimizations.

###### Tighten up the schema

- MySQL dumps to disk in contiguous blocks for fast access.
- Use `CHAR` instead of `VARCHAR` for fixed-length fields.
  - `CHAR` effectively allows for fast, random access, whereas with `VARCHAR`, you must find the end of a string before moving onto the next one.
- Use `TEXT` for large blocks of text such as blog posts. `TEXT` also allows for boolean searches. Using a `TEXT` field results in storing a pointer on disk that is used to locate the text block.
- Use `INT` for larger numbers up to 2^32 or 4 billion.
- Use `DECIMAL` for currency to avoid floating point representation errors.
- Avoid storing large `BLOBS`, store the location of where to get the object instead.
- `VARCHAR(255)` is the largest number of characters that can be counted in an 8 bit number, often maximizing the use of a byte in some RDBMS.
- Set the `NOT NULL` constraint where applicable to improve search performance.

##### Indexing

**Use good indices**

- Columns that you are querying (`SELECT`, `GROUP BY`, `ORDER BY`, `JOIN`) could be faster with indices.
- Indices are usually represented as self-balancing `B-tree` that keeps data sorted and allows searches, sequential access, insertions, and deletions in logarithmic time.
- Placing an index can keep the data in memory, requiring more space.
- Writes could also be slower since the index also needs to be updated.
- When loading large amounts of data, it might be faster to disable indices, load the data, then rebuild the indices.

##### Avoid expensive joins

- [Denormalize](#denormalization) where performance demands it.

##### Partition tables

- Break up a table by putting hot spots in a separate table to help keep it in memory.

##### Tune the query cache

- In some cases, the `query cache` could lead to `performance issues`.

#### NoSQL

NoSQL is a collection of data items represented in a **key-value store**, **document store**, **wide column store**, or a **graph database**. Data is denormalized, and joins are generally done in the application code. Most NoSQL stores lack true ACID transactions and favor [eventual consistency](#eventual-consistency).

**BASE** is often used to describe the properties of NoSQL databases. In comparison with the [CAP Theorem](#cap-theorem), BASE chooses availability over consistency.

- **Basically available** - the system guarantees availability.
- **Soft state** - the state of the system may change over time, even without input.
- **Eventual consistency** - the system will become consistent over a period of time, given that the system doesn't receive input during that period.

In addition to choosing between [SQL or NoSQL](#sql-or-nosql), it is helpful to understand which type of NoSQL database best fits your use case(s). We'll review **key-value stores**, **document stores**, **wide column stores**, and **graph databases** in the next section.

##### Key-value store

> Abstraction: hash table

A key-value store generally allows for O(1) reads and writes and is often backed by memory or SSD. Data stores can maintain keys in `lexicographic order`, allowing efficient retrieval of key ranges. Key-value stores can allow for storing of metadata with a value.

Key-value stores provide high performance and are often used for simple data models or for rapidly-changing data, such as an in-memory cache layer. Since they offer only a limited set of operations, complexity is shifted to the application layer if additional operations are needed.

A key-value store is the basis for more complex systems such as a document store, and in some cases, a graph database.

##### Document store

> Abstraction: key-value store with documents stored as values

A document store is centered around documents (XML, JSON, binary, etc), where a document stores all information for a given object. Document stores provide APIs or a query language to query based on the internal structure of the document itself. _Note, many key-value stores include features for working with a value's metadata, blurring the lines between these two storage types._

Based on the underlying implementation, documents are organized by collections, tags, metadata, or directories. Although documents can be organized or grouped together, documents may have fields that are completely different from each other.

Some document stores like `MongoDB` and `CouchDB` also provide a SQL-like language to perform complex queries. `DynamoDB` supports both key-values and documents.

Document stores provide high flexibility and are often used for working with occasionally changing data.

##### Wide column store

> Abstraction: nested map `ColumnFamily<RowKey, Columns<ColKey, Value, Timestamp>>`

A wide column store's basic unit of data is a column (name/value pair). A column can be grouped in column families (analogous to a SQL table). Super column families further group column families. You can access each column independently with a row key, and columns with the same row key form a row. Each value contains a timestamp for versioning and for conflict resolution.

Google introduced `Bigtable` as the first wide column store, which influenced the open-source `HBase` often-used in the Hadoop ecosystem, and `Cassandra` from Facebook. Stores such as BigTable, HBase, and Cassandra maintain keys in lexicographic order, allowing efficient retrieval of selective key ranges.

Wide column stores offer high availability and high scalability. They are often used for very large data sets.

##### Graph database

> Abstraction: graph

In a graph database, each node is a record and each arc is a relationship between two nodes. Graph databases are optimized to represent complex relationships with many foreign keys or many-to-many relationships.

Graphs databases offer high performance for data models with complex relationships, such as a social network. They are relatively new and are not yet widely-used; it might be more difficult to find development tools and resources. Many graphs can only be accessed with [REST APIs](#representational-state-transfer-rest).

#### SQL or NoSQL

Reasons for **SQL**:

- Structured data
- Strict schema
- Relational data
- Need for complex joins
- Transactions
- Clear patterns for scaling
- More established: developers, community, code, tools, etc
- Lookups by index are very fast

Reasons for **NoSQL**:

- Semi-structured data
- Dynamic or flexible schema
- Non-relational data
- No need for complex joins
- Store many TB (or PB) of data
- Very data intensive workload
- Very high throughput for IOPS

Sample data well-suited for NoSQL:

- Rapid ingest of clickstream and log data
- Leaderboard or scoring data
- Temporary data, such as a shopping cart
- Frequently accessed ('hot') tables
- Metadata/lookup tables

#### Horizontal scaling and Vertical scalling

Load balancers can also help with horizontal scaling, improving performance and availability. Scaling out using commodity machines is more cost efficient and results in higher availability than scaling up a single server on more expensive hardware, called **Vertical Scaling**. It is also easier to hire for talent working on commodity hardware than it is for specialized enterprise systems.

[Difference between horizontal and vertical scalling](https://www.geeksforgeeks.org/horizontal-and-vertical-scaling-in-databases/)

#### Disadvantage(s): horizontal scaling

- Scaling horizontally introduces complexity and involves cloning servers
  - Servers should be stateless: they should not contain any user-related data like sessions or profile pictures
  - Sessions can be stored in a centralized data store such as a [database](#database) (SQL, NoSQL) or a persistent [cache](#cache) (Redis, Memcached)
- Downstream servers such as caches and databases need to handle more simultaneous connections as upstream servers scale out

### Stateless and Stateful Services

- **Project:** Convert a stateful service to stateless and compare.
- **Resources:** [Stateless vs Stateful Architecture](https://www.redhat.com/en/topics/cloud-native-apps/stateful-vs-stateless)

### Data Structures Behind Databases

- [Data Structures in SQL](https://www.dbvis.com/thetable/a-comprehensive-guide-to-data-structures-in-sql/#:~:text=Depending%20on%20how%20the%20data,are%20linked%20to%20one%20another.)

### Databases Replication

#### 31. **How to Scale Databases**

- **Project:** Implement scaling strategies for a database.
- **Resources:** [Database Scaling Techniques](https://docs.microsoft.com/en-us/azure/architecture/best-practices/data-partitioning)

#### 32. **Database Replication: Fundamentals and Algorithms**

- **Project:** Set up database replication and analyze different algorithms.
- **Resources:** [PostgreSQL Replication](https://www.postgresql.org/docs/current/high-availability.html)

#### 33. **Implementing Database Replication: Practical Guide and Failover Strategies**

- **Project:** Practical guide to implement replication with failover.
- **Resources:** MySQL Replication

#### 34. **Data Replication Tutorial**

- **Project:** Hands-on tutorial for data replication.
- **Resources:** [MongoDB Replication](https://docs.mongodb.com/manual/replication/)

#### 35. **Change Data Capture**

- **Project:** Implement CDC for a database system.

### Databases Partitioning

#### 36. **Database Partitioning**

- **Project:** Implement partitioning for a database.
- Database Partitioning Techniques

#### 37. **Advanced Database Partitioning Techniques and Key Selection**

- **Project:** Explore advanced partitioning and key selection strategies.
- Advanced Partitioning in cassandra, mongo, etc.

#### 38. **Consistent Hashing**

- **Project:** Implement consistent hashing for distributed systems.
- Consistent Hashing Algorithm

#### 39. **Database Partition Tutorial**

- **Project:** Step-by-step tutorial on database partitioning.
- Partitioning in PostgreSQL

### Indexing

### Paging and filtering

### Bloom filter

- A bloom filter is a probabilistic data structure that is based on hashing. It is extremely space efficient and is typically used to add elements to a set and test if an element is in a set. Though, the elements themselves are not added to a set. Instead a hash of the elements is added to the set.
- The advantages of the bloom filter are the following:
  - constant time complexity
  - constant space complexity
  - operations are parallelizable
  - no false negatives
  - enables privacy by not storing actual items
- The limitations of the bloom filter are the following:
  - bloom filter doesn’t support the delete operation
  - false positives rate can’t be reduced to zero
  - bloom filter on disk requires random access due to random indices generated by hash functions

### Quorum

- Quorum, within distributed systems, denotes the minimum number of nodes or processes required to reach a consensus on a specific action or decision to validate it. This consensus is essential for maintaining system coherence and ensuring effective operation, even in the presence of failures or network partitions.
- benefits of Quorum in system design are consistency, high availability, scalability,data integrity, fault tolerance
- Usecases of Quorum:
  - Quorum is used in distributed databases to ensure that read and write operations are consistent across multiple nodes. By requiring a quorum of nodes to agree on each operation, distributed databases can maintain data consistency even in the presence of network partitions or node failures.
  - Quorum is a fundamental concept in consensus algorithms like Paxos and Raft. These algorithms use a quorum of nodes to agree on the order of operations, ensuring that all nodes in the system reach a consistent state.
  - Quorum is used in distributed file systems to ensure that file operations are consistent across multiple nodes. By requiring a quorum of nodes to agree on each operation, distributed file systems can maintain data consistency and availability.
  - Quorum is used in configuration management systems to ensure that configuration changes are applied consistently across multiple nodes. By requiring a quorum of nodes to agree on each change, configuration management systems can prevent conflicts and ensure that changes are applied correctly.
  - Quorum can be used in load balancing algorithms to ensure that requests are distributed evenly across a cluster of servers. By requiring a quorum of servers to agree on the load balancing decision, load balancers can ensure that requests are routed efficiently and reliably.

### Master-Slave

- Master-Slave Architecture is a design in computing where one central unit, called the master, controls and directs the operation of multiple subordinate units, known as slaves. In this setup, the master node governs and delegates tasks to the slave nodes, which execute the assigned tasks and report back to the master. This architecture is commonly used in distributed systems to manage resources efficiently and streamline data processing.

### Data flow

#### 46. **Overview**

- **Project:** Design a data flow diagram for a complex system.

#### 47. **Push vs Pull**

- **Project:** Implement both push and pull data models.

### Message Queue

#### 48. **Message Queues in System Design**

- **Project:** Set up a message queue for a microservices architecture.

#### 49. **Message Queue Use Cases and Patterns**

- **Project:** Implement common message queue patterns.

#### 50. **Redis-queue Tutorial**

- **Project:** Tutorial to implement message queues using Redis.

#### 51. **Log-based message queues**

- **Project:** Implement a log-based message queue system.

#### 52. **Introduction to Kafka**

- **Project:** Set up and use Kafka for stream processing.

#### 53. **Kafka Exercise**

- **Project:** Hands-on exercise to create a Kafka producer and consumer.

### Batch Processing

#### 54. **Overview**

- **Project:** Design a batch processing system for ETL.

#### 55. **Batch processing In System Design**

- **Project:** Implement batch processing for a data pipeline.

#### 56. **MapReduce**

- **Project:** Implement a MapReduce job for data processing.

#### 57. **Dataflow Engines**

- **Project:** Use a dataflow engine for batch processing.

#### 58. **Why use Batch Processing**

- **Project:** Case study on the benefits of batch processing.

### Stream Processing

#### 59. **Stream processing**

- **Project:** Implement a stream processing application.

#### 60. **Batch and stream**

- **Project:** Compare batch and stream processing with practical examples.

#### 61. **Lambda Architecture**

- **Project:** Implement Lambda Architecture for a real-time analytics system.

#### 62. **Kappa Architecture**

- **Project:** Implement Kappa Architecture for stream processing.

### Patterns

#### 63. **A Database Per Microservice**

- **Project:** Design a microservices architecture with individual databases.

#### 64. **Cache, Always**

- **Project:** Implement caching in a microservices architecture.

#### 65. **Change Data Capture + ElasticSearch**

- **Project:** Sync data to Elasticsearch using Change Data Capture.

#### 66. **The Two-Stage Processing Pattern**

- **Project:** Implement a two-stage data processing pipeline.

### Throughput and Latency

#### 75. **Latency**

- time taken to send one package

#### 76. **Throughput**

- number of data arrived withing one second

### CAP Consistency, Availability, Partition tolenrance

In a distributed computer system, you can only support two of the following guarantees:

- **Consistency** - Every read receives the most recent write or an error
- **Availability** - Every request receives a response, without guarantee that it contains the most recent version of the information. Redundancy, failover mechanisms, distributed systems, and geographic distribution.

- **Partition Tolerance** - The system continues to operate despite arbitrary partitioning due to network failures

_Networks aren't reliable, so you'll need to support partition tolerance. You'll need to make a software tradeoff between consistency and availability._

#### CP - consistency and partition tolerance

Waiting for a response from the partitioned node might result in a timeout error. CP is a good choice if your business needs require atomic reads and writes.

#### AP - availability and partition tolerance

Responses return the most readily available version of the data available on any node, which might not be the latest. Writes might take some time to propagate when the partition is resolved.

AP is a good choice if the business needs to allow for [eventual consistency](#eventual-consistency) or when the system needs to continue working despite external errors.

### PACELC Partition, Availability, Consistency, Else, Latency, and Consistency

- The theorem states that in the event of a network partition, a distributed system must choose between availability and consistency; otherwise, it must choose between latency and consistency.
- Assists in choosing the right distributed database system based on availability and latency requirements.
- Helps data scientists and technology professionals make decisions related to application performance and user experience
- Provides a framework for evaluating trade-offs between different technologies and configurations to achieve optimal data processing and analytics performance
- CAP Theorem focuses on the trade-offs between consistency, availability, and partition tolerance in distributed systems, while PACELC Theorem extends this concept by also considering latency trade-offs in non-partition scenarios.

### Resiliency

### Consistency patterns

With multiple copies of the same data, we are faced with options on how to synchronize them so clients have a consistent view of the data. Recall the definition of consistency from the [CAP theorem](#cap-theorem) - Every read receives the most recent write or an error.

#### Weak consistency

After a write, reads may or may not see it. A best effort approach is taken.

This approach is seen in systems such as memcached. Weak consistency works well in real time use cases such as VoIP, video chat, and realtime multiplayer games. For example, if you are on a phone call and lose reception for a few seconds, when you regain connection you do not hear what was spoken during connection loss.

#### Eventual consistency

After a write, reads will eventually see it (typically within milliseconds). Data is replicated asynchronously.

This approach is seen in systems such as DNS and email. Eventual consistency works well in highly available systems.

#### Strong consistency

After a write, reads will see it. Data is replicated synchronously.

This approach is seen in file systems and RDBMSes. Strong consistency works well in systems that need transactions.

### Availability patterns

There are two complementary patterns to support high availability: **fail-over** and **replication**.

#### Fail-over

##### Active-passive

With active-passive fail-over, heartbeats are sent between the active and the passive server on standby. If the heartbeat is interrupted, the passive server takes over the active's IP address and resumes service.

The length of downtime is determined by whether the passive server is already running in 'hot' standby or whether it needs to start up from 'cold' standby. Only the active server handles traffic.

Active-passive failover can also be referred to as master-slave failover.

##### Active-active

In active-active, both servers are managing traffic, spreading the load between them.

If the servers are public-facing, the DNS would need to know about the public IPs of both servers. If the servers are internal-facing, application logic would need to know about both servers.

Active-active failover can also be referred to as master-master failover.

#### Disadvantage(s): failover

- Fail-over adds more hardware and additional complexity.
- There is a potential for loss of data if the active system fails before any newly written data can be replicated to the passive.

#### Replication

##### Master-slave and master-master

This topic is further discussed in the [Database](#database) section:

- [Master-slave replication](#master-slave-replication)
- [Master-master replication](#master-master-replication)

#### Availability in numbers

Availability is often quantified by uptime (or downtime) as a percentage of time the service is available. Availability is generally measured in number of 9s--a service with 99.99% availability is described as having four 9s.

##### 99.9% availability - three 9s

| Duration           | Acceptable downtime |
| ------------------ | ------------------- |
| Downtime per year  | 8h 45min 57s        |
| Downtime per month | 43m 49.7s           |
| Downtime per week  | 10m 4.8s            |
| Downtime per day   | 1m 26.4s            |

##### 99.99% availability - four 9s

| Duration           | Acceptable downtime |
| ------------------ | ------------------- |
| Downtime per year  | 52min 35.7s         |
| Downtime per month | 4m 23s              |
| Downtime per week  | 1m 5s               |
| Downtime per day   | 8.6s                |

##### Availability in parallel vs in sequence

If a service consists of multiple components prone to failure, the service's overall availability depends on whether the components are in sequence or in parallel.

**In sequence**

Overall availability decreases when two components with availability < 100% are in sequence:

```
Availability (Total) = Availability (Foo) * Availability (Bar)
```

If both `Foo` and `Bar` each had 99.9% availability, their total availability in sequence would be 99.8%.

**In parallel**

Overall availability increases when two components with availability < 100% are in parallel:

```
Availability (Total) = 1 - (1 - Availability (Foo)) * (1 - Availability (Bar))
```

If both `Foo` and `Bar` each had 99.9% availability, their total availability in parallel would be 99.9999%.

### Rate limiting

### Logging and monitoring

### Security

Security is a broad topic. Unless you have considerable experience, a security background, or are applying for a position that requires knowledge of security, you probably won't need to know more than the basics:

- Encrypt in transit and at rest.
- Sanitize all user inputs or any input parameters exposed to user to prevent `XSS for Cross-site_scripting` and `SQL injection`.
- Use parameterized queries to prevent SQL injection.
- Use the principle of `least privilege`.

### Asynchronism

Asynchronous workflows help reduce request times for expensive operations that would otherwise be performed in-line. They can also help by doing time-consuming work in advance, such as periodic aggregation of data.

#### Message queues

Message queues receive, hold, and deliver messages. If an operation is too slow to perform inline, you can use a message queue with the following workflow:

- An application publishes a job to the queue, then notifies the user of job status
- A worker picks up the job from the queue, processes it, then signals the job is complete

The user is not blocked and the job is processed in the background. During this time, the client might optionally do a small amount of processing to make it seem like the task has completed. For example, if posting a tweet, the tweet could be instantly posted to your timeline, but it could take some time before your tweet is actually delivered to all of your followers.

**Redis** is useful as a simple message broker but messages can be lost.

**RabbitMQ** is popular but requires you to adapt to the 'AMQP' protocol and manage your own nodes.

**Amazon SQS** is hosted but can have high latency and has the possibility of messages being delivered twice.

#### Task queues

Tasks queues receive tasks and their related data, runs them, then delivers their results. They can support scheduling and can be used to run computationally-intensive jobs in the background.

**Celery** has support for scheduling and primarily has python support.

#### Back pressure

If queues start to grow significantly, the queue size can become larger than memory, resulting in cache misses, disk reads, and even slower performance. Back pressure can help by limiting the queue size, thereby maintaining a high throughput rate and good response times for jobs already in the queue. Once the queue fills up, clients get a server busy or HTTP 503 status code to try again later. Clients can retry the request at a later time, perhaps with `exponential backoff`.

### Application layer

<p align="center">
  <img src="./../support_images/application_layer.png">
</p>

Separating out the web layer from the application layer (also known as platform layer) allows you to scale and configure both layers independently. Adding a new API results in adding application servers without necessarily adding additional web servers. The **single responsibility principle** advocates for small and autonomous services that work together. Small teams with small services can plan more aggressively for rapid growth.

Workers in the application layer also help enable [asynchronism](#asynchronism).

#### Disadvantage(s): application layer

- Adding an application layer with loosely coupled services requires a different approach from an architectural, operations, and process viewpoint (vs a monolithic system).
- Microservices can add complexity in terms of deployments and operations.

### Microservices

Related to this discussion are microservices, which can be described as a suite of independently deployable, small, modular services. Each service runs a unique process and communicates through a well-defined, lightweight mechanism to serve a business goal.

Pinterest, for example, could have the following microservices: user profile, follower, feed, search, photo upload, etc.
