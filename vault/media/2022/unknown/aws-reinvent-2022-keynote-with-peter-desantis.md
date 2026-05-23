---
clients:
- AWS
- Scuderia Ferrari
date: 2022-11-29
description: "Peter DeSantis, Senior Vice President, AWS Utility Computing, dives
  deep on how AWS refuses to compromise in the tug of war between low cost, high performance
  and security. He will give an update on the Graviton line of chips and the AWS Nitro
  system, as well as machine learning infrastructure and serverless computing. \n\nLearn
  more about AWS at https://go.aws/3UhdMh1.\nASL (ASL American Sign Language) is available
  at https://youtu.be/aSzlVsd9wDA.\n\nGuest Speaker: \n43:26 Jock Clear of Scuderia
  Ferr"
event: unknown
has_transcript: true
language: en
playlist: ''
tags:
- aws
- reinvent
- keynote
- graviton
- nitro
- machine-learning
- cloud
thematic: media
title: AWS re:Invent 2022 - Keynote with Peter DeSantis
url: https://www.youtube.com/watch?v=R11YgBEZzqE
video_id: R11YgBEZzqE
year: 2022
---

# AWS re:Invent 2022 - Keynote with Peter DeSantis

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=R11YgBEZzqE)
> 📅 2022-11-29 | 🎤 unknown | 🌐 en
> 🏢 Clients: [[AWS]] [[Scuderia Ferrari]]

# AWS re:Invent 2022 Keynote with Peter DeSantis: Engineering Without Compromise

Peter DeSantis, Senior Vice President of AWS Utility Computing, delivered a deeply technical keynote centered on AWS's commitment to refusing trade-offs between cost, performance, and security. The session traversed innovations across silicon, networking, machine learning infrastructure, and serverless computing, illustrating how foundational engineering investments compound into superior customer outcomes.

## Performance Through Custom Silicon and Networking

### The Nitro System and Graviton Evolution

DeSantis opened by reaffirming the AWS Nitro System as the architectural foundation enabling high performance and strong security simultaneously. He introduced AWS Nitro v5, the latest generation offering substantially greater compute power, memory bandwidth, and PCIe throughput, which directly translates into faster networking and storage for EC2 customers. Building on Nitro v5, AWS launched the C7gn EC2 instance, designed for network-intensive workloads and powered by the new Nitro card alongside Graviton processors. To address high-performance computing specifically, AWS announced Graviton3E, a variant tuned for vector and floating-point performance, and the HPC7g EC2 instance built around it, targeting tightly coupled scientific simulations.

### Reinventing the Network with SRD

A significant portion of the keynote focused on the Scalable Reliable Datagram (SRD) protocol, originally developed for the Elastic Fabric Adapter to support HPC workloads. DeSantis explained the limitations of traditional TCP in modern data centers, where its assumptions about congestion and ordering create latency variability that hurts demanding applications. SRD takes a different approach by spraying packets across many network paths and handling reordering and reliability above the transport layer, dramatically reducing tail latency.

AWS extended SRD beyond HPC into core services. All new EBS io2 volumes now run on SRD, delivering more consistent and lower-latency block storage. The Elastic Network Adapter also gained SRD support through the launch of ENA Express, which transparently brings SRD's performance benefits to standard TCP applications without requiring code changes, improving throughput and tail latency for ordinary EC2 workloads.

## Machine Learning Infrastructure at Scale

### Training Foundational Models

DeSantis devoted substantial attention to the challenges of training foundational models, whose parameter counts have exploded to hundreds of billions. He walked through the engineering realities of distributed training, including the need to scale across thousands of accelerators, the mathematics of gradient averaging across nodes, and the bandwidth-intensive requirement of sharing parameters during each training step. These workloads demand both raw compute and exceptional networking, since communication overhead can dominate training time at scale.

To address these demands, AWS launched Trn1n instances for EC2, a network-optimized variant of the Trainium-based Trn1 platform with 1,600 Gbps of networking. This positions AWS to support the largest model training jobs with high cost-efficiency relative to GPU alternatives.

### A Perspective from Scuderia Ferrari

Jock Clear of Scuderia Ferrari joined as guest speaker to discuss how Formula 1 racing parallels cloud engineering, emphasizing the relentless pursuit of marginal gains, the role of simulation and data, and how computational infrastructure has become inseparable from competitive performance on the track.

## Rethinking Serverless Computing

### Isolation, Firecracker, and Cold Starts

The final segment addressed serverless computing and the underlying technology that makes AWS Lambda viable at scale. DeSantis explored process isolation models, contrasting traditional containers with the stronger boundaries required for multi-tenant execution, and detailed how Firecracker, the lightweight virtualization technology AWS open-sourced, provides VM-level isolation with container-like startup characteristics.

He then turned to the persistent challenge of cold start latency, which has long been a friction point for latency-sensitive Lambda workloads, particularly those built on JVM-based runtimes with lengthy initialization phases. To solve this, AWS announced AWS Lambda SnapStart, which captures a snapshot of an initialized function and restores it on demand rather than executing initialization on each cold invocation.

### Making Snapshots Fast

DeSantis went beyond the announcement to explain how AWS makes SnapStart practical. Naively loading a multi-hundred-megabyte snapshot would not deliver the desired latency, so AWS employs efficient snapshot handling techniques and predictive snapshot loading, which anticipates the memory pages a function will need and prefetches them. This combination yields cold start improvements of up to ten times for supported workloads without requiring developers to redesign their applications.

## Closing Themes

DeSantis closed by reinforcing the keynote's central thesis: that the apparent trade-offs between cost, performance, and security are not fundamental laws but engineering challenges to be overcome through deep, vertically integrated investment. The launches spanning Nitro v5, Graviton3E, C7gn and HPC7g instances, ENA Express, EBS on SRD, Trn1n instances, and Lambda SnapStart collectively demonstrate how AWS continues to push every layer of the stack to eliminate compromises customers have historically been forced to accept.