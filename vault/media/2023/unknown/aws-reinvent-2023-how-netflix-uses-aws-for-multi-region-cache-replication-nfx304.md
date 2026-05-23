---
clients:
- Netflix
- AWS
- Amazon SQS
- Apache Kafka
date: 2023-12-06
description: EVCache is a critical tier 0 microservice hosted on AWS that empowers
  Netflix with low latency, high-availability caching, and in-memory database solutions.
  To ensure global accessibility of EVCache data, regardless of the AWS Region it
  is written to, Netflix developed Cross-Region Replication (CRR), a large-scale distributed
  system. This session delves into CRR’s design and architecture, showcasing the effective
  utilization of services like Amazon SQS, Apache Kafka, load balancers, auto scaling
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- netflix
- caching
- multi-region
- replication
- microservices
- cloud
thematic: media
title: AWS re:Invent 2023 - How Netflix uses AWS for multi-Region cache replication
  (NFX304)
url: https://www.youtube.com/watch?v=85TiFrDhCR4
video_id: 85TiFrDhCR4
year: 2023
---

# AWS re:Invent 2023 - How Netflix uses AWS for multi-Region cache replication (NFX304)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=85TiFrDhCR4)
> 📅 2023-12-06 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[AWS]] [[Amazon SQS]] [[Apache Kafka]]

# How Netflix Uses AWS for Multi-Region Cache Replication

## Overview of EVCache and Its Role at Netflix

EVCache stands as a tier 0 microservice within Netflix's infrastructure, providing the low-latency, high-availability caching and in-memory database capabilities that underpin the streaming experience for millions of users worldwide. Hosted entirely on AWS, this service has become indispensable to Netflix's operations, serving as a foundational layer that other critical services depend upon. Given its central role, ensuring that data stored in EVCache remains accessible globally—regardless of which AWS Region originally received the write—became an engineering priority that drove the development of a sophisticated replication system.

To address this challenge, Netflix engineered Cross-Region Replication (CRR), a large-scale distributed system designed to propagate cache data across AWS Regions while maintaining the performance characteristics that Netflix's applications require. The session explores how Netflix designed and operates this system at remarkable scale, achieving roughly 30 million cross-region requests per second while keeping P90 latencies under two seconds.

## Architecture and AWS Services Powering Cross-Region Replication

### Distributed System Design with AWS Building Blocks

The CRR architecture leverages a thoughtful combination of AWS managed services and open-source technologies to achieve its scale and reliability goals. Amazon SQS plays a central role in the message-passing pipeline, providing durable, decoupled queuing that allows replication events to flow reliably between regions even when downstream components experience variability. Apache Kafka complements this by handling high-throughput event streaming where ordering and replay capabilities are valuable, giving Netflix flexibility to choose the right messaging primitive for each stage of the replication flow.

Load balancers distribute the heavy replication traffic across fleets of consumers, while EC2 auto scaling ensures that compute capacity expands and contracts in response to fluctuating workloads. This elasticity proves essential given Netflix's globally varying traffic patterns, allowing the system to handle peak loads without overprovisioning during quieter periods. Amazon EC2 instances host the worker components that read replication messages, transform them as needed, and write the data into EVCache clusters in destination regions.

### Achieving Scale and Performance Targets

The combination of these services enables CRR to sustain approximately 30 million requests per second across regions, a throughput level that places it among the largest replication systems in production. Equally important, Netflix has tuned the architecture so that P90 latencies remain under two seconds, meaning the vast majority of replicated writes become visible in destination regions quickly enough to support Netflix's consistency expectations. Achieving both high throughput and low latency simultaneously required careful attention to batching strategies, parallelism, queue sizing, and the placement of components relative to the data they process.

## Key Outcomes and Engineering Lessons

The CRR system demonstrates how thoughtful composition of AWS services—queues, streaming platforms, load balancers, auto scaling groups, and compute—can yield a globally distributed replication tier that meets demanding performance and availability requirements. By offloading much of the operational burden to managed services like SQS while retaining flexibility through Kafka and EC2, Netflix struck a balance between development velocity and fine-grained control over the replication path.

The result is a system that gives Netflix application teams confidence that data written to EVCache in one region will be available in others within a tight latency envelope, simplifying the design of multi-region applications and supporting Netflix's broader resilience strategy. The session ultimately illustrates a reusable pattern for organizations facing similar cross-region data distribution challenges, showing that extreme scale is achievable through disciplined architectural choices built on AWS primitives.