---
clients:
- Amazon Aurora
- AWS
date: 2023-12-03
description: With an innovative architecture that decouples compute from storage and
  advanced features like Global Database and low-latency read replicas, Amazon Aurora
  reimagines what it means to be a relational database. Aurora is a modern database
  service offering unparalleled performance and high availability at scale with full
  open source MySQL and PostgreSQL compatibility. In this session, dive deep into
  the most exciting new features Aurora offers, including Aurora I/O-Optimized, Aurora
  zero-ETL integ
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- aurora
- database
- cloud
- reinvent
- storage
thematic: media
title: AWS re:Invent 2023 - Deep dive into Amazon Aurora and its innovations (DAT408)
url: https://www.youtube.com/watch?v=je6GCOZ22lI
video_id: je6GCOZ22lI
year: 2023
---

# AWS re:Invent 2023 - Deep dive into Amazon Aurora and its innovations (DAT408)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=je6GCOZ22lI)
> 📅 2023-12-03 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Amazon Aurora]] [[AWS]]

# Deep Dive into Amazon Aurora and Its Innovations

## Reimagining the Relational Database

Amazon Aurora represents a fundamental rethinking of what a relational database can be in the cloud era. By decoupling compute from storage, Aurora delivers a managed service that combines the familiarity and compatibility of open source MySQL and PostgreSQL with the performance, scalability, and durability that cloud-native architectures make possible. This separation allows the storage layer to operate as a distributed, self-healing system spanning multiple Availability Zones, while the compute layer scales independently to meet the demands of modern applications. The result is a database that offers unparalleled availability and throughput without forcing customers to abandon the standards and tooling they already rely on.

## Architecture and Core Capabilities

### Decoupled Compute and Storage Foundation

At the heart of Aurora's design is a purpose-built distributed storage system that replicates data six ways across three Availability Zones. Rather than shipping full database pages over the network, Aurora sends only redo log records to storage, dramatically reducing I/O overhead and enabling faster commits, quicker recovery, and more efficient replication. This architecture allows Aurora to support up to fifteen low-latency read replicas that share the same underlying storage volume, eliminating the replication lag and duplication of storage costs that traditional architectures impose. Compute instances can be added, removed, or failed over in seconds because there is no need to copy data between nodes.

### Global Database and High Availability

Aurora Global Database extends this architecture across AWS Regions, enabling cross-region replication with typical lag measured in the low hundreds of milliseconds. This capability supports both disaster recovery scenarios with aggressive recovery point and recovery time objectives, as well as globally distributed applications that need to serve low-latency reads close to users. Combined with multi-AZ failover within a Region, Global Database gives customers a comprehensive resilience story that would be difficult and expensive to engineer on traditional database platforms.

## Innovations Driving the Next Generation of Aurora

### Aurora I/O-Optimized for Predictable Pricing

Aurora I/O-Optimized introduces a configuration that includes I/O charges in the base price of compute and storage, providing predictable costs for I/O-intensive workloads. Customers running workloads where I/O charges represented a significant share of their bill can realize meaningful savings while also benefiting from improved throughput and lower latency. This option complements the standard Aurora pricing model, allowing customers to choose the configuration that best matches their workload economics.

### Zero-ETL Integration with Amazon Redshift

Aurora's zero-ETL integration with Amazon Redshift removes the traditional friction between transactional and analytical systems. Data written to Aurora becomes available in Redshift within seconds, without customers needing to build, maintain, or operate extract-transform-load pipelines. This integration enables near real-time analytics on operational data, accelerating use cases such as personalization, fraud detection, and operational dashboards while reducing the engineering effort and cost associated with custom data movement infrastructure.

### Aurora Serverless v2

Aurora Serverless v2 delivers fine-grained, instantaneous scaling of database capacity in response to workload demand. Capacity scales in small increments up to hundreds of thousands of transactions per second, and applications can move between provisioned and serverless configurations without disruption. Serverless v2 is well suited to variable, unpredictable, or multi-tenant workloads, allowing customers to pay only for the capacity they actually consume while maintaining the full feature set of Aurora, including read replicas, Global Database, and Multi-AZ deployments.

### pgvector and Generative AI Workloads

The addition of the pgvector extension to Aurora PostgreSQL transforms Aurora into a viable foundation for generative AI applications. With pgvector, developers can store vector embeddings alongside their relational data and perform similarity searches directly in the database. This enables retrieval-augmented generation patterns, semantic search, and recommendation systems without introducing a separate specialized vector database. By unifying operational data and embeddings in a single managed service, Aurora reduces architectural complexity and allows generative AI capabilities to be added to existing applications with minimal disruption.

## Outcomes and Takeaways

The session reinforces that Aurora continues to evolve along three clear directions: deeper cost and performance optimization through options like I/O-Optimized and Serverless v2, tighter integration with the broader AWS data ecosystem through zero-ETL with Redshift, and expansion into emerging workloads such as generative AI through pgvector. Customers evaluating Aurora should consider matching their workload patterns to the appropriate pricing and capacity model, leveraging zero-ETL to simplify analytics pipelines, and exploring vector capabilities to consolidate AI workloads onto their existing relational platform. Together, these innovations position Aurora as a database service that not only matches the capabilities of traditional engines but extends well beyond them to meet the requirements of modern, data-intensive, and intelligent applications.