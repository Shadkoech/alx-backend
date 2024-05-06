# Queuing System in JavaScript

## Overview
This project focuses on implementing a queuing system in JavaScript using Redis and Node.js. It covers various aspects such as setting up Redis, using Redis clients, handling async operations, building basic Express apps, and creating job queues with Kue.

## Redis
Redis ( Remote Dictionary Server) is an open-source, in-memory data structure store used as a database, cache, and message broker. It supports various data structures such as strings, hashes, lists, sets, sorted sets, bitmaps, hyperloglogs, and geospatial indexes. Redis is known for its high performance, scalability, and versatility, making it popular in various use cases, including caching, real-time analytics, messaging, and job queues.
- Redis is used by giants like Twitter, GitHub, and Snapchat.
- In the context of this queuing system project, Redis plays a crucial role as the backend data store and message broker. 

## Learning objectives
Going through this project equips one to be able to:
- Set up a Redis server on your machine
- Perform simple operations with the Redis client
- Use Redis clients with Node.js for basic and advanced operations
- Store hash values in Redis and deal with async operations
- Implement a queuing system using Kue
- Build basic Express applications interacting with a Redis server and queue


## Tasks
### Overview
1. `Install a Redis Instance:` Download, compile, and start a Redis server. Verify its functionality and set up a key-value pair.
2. `Node Redis Client:` Implement a Node.js script to connect to the Redis server using the node_redis library. Handle connection errors and successes.
3. `Node Redis Client and Basic Operations:`` Expand the previous script to perform basic Redis operations like setting and retrieving values.
4. `Node Redis Client and Async Operations:` Modify the script to handle async operations using promisify and async/await.
5. `Node Redis Client Publisher and Subscriber:` Create separate scripts for publisher and subscriber functionalities, demonstrating communication via Redis channels.
6. `Create the Job Creator:` Implement a script to create jobs using Kue and interact with the Redis server.
7. `Create the Job Processor:` Develop a script to process jobs created by the Job Creator, demonstrating background job processing.
8. `Track Progress and Errors with Kue:` Enhance the Job Creator and Processor scripts to track job progress and handle errors effectively.
9. `Writing the Job Creation Function:` Write a function to create and manage jobs efficiently, validating inputs and handling errors.
10. `Writing the Test for Job Creation:` Implement tests to validate the functionality of the job creation function, ensuring correctness and reliability.
11. `In Stock?:` Develop an Express server to manage product listings and reservation functionalities using Redis for data storage.
