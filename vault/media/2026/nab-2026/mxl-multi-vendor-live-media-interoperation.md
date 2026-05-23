---
clients:
- AWS
- Amazon EC2
- Amazon
date: 2026-05-13
description: Cloud-based live production often forces broadcasters to choose between
  vendor lock-in or complex integration challenges. The Media eXchange Layer (MXL)
  is an open-source SDK enabling interoperable ultra-low latency exchange of live
  uncompressed video, audio, and metadata between different software media functions.
  This demo showcases MXL v1.0 exchanging live media between multiple AWS Partners
  hosted on three Amazon EC2 g6 instances using both shared memory within an instance
  and Amazon Elastic
event: nab-2026
has_transcript: true
language: en
playlist: NAB 2026
tags:
- live
- cloud
- interoperability
- open-source
- broadcast
- low-latency
- sdk
thematic: media
title: 'MXL: Multi-vendor live media interoperation'
url: https://www.youtube.com/watch?v=d1NZtPafHpw
video_id: d1NZtPafHpw
year: 2026
---

# MXL: Multi-vendor live media interoperation

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=d1NZtPafHpw)
> 📅 2026-05-13 | 🎤 nab-2026 | 🌐 en
> 🏢 Clients: [[AWS]] [[Amazon EC2]] [[Amazon]]

# MXL: Multi-Vendor Live Media Interoperation

## Overview

Cloud-based live production has historically forced broadcasters into a difficult trade-off between vendor lock-in and the complexity of integrating disparate systems. The Media eXchange Layer (MXL) addresses this longstanding challenge by providing an open-source SDK that enables interoperable, ultra-low latency exchange of live uncompressed video, audio, and metadata between media software functions developed by different vendors. By standardizing the way live media flows between components, MXL empowers broadcasters to assemble best-of-breed workflows without sacrificing performance or flexibility.

## Demonstrating MXL v1.0 on AWS

The demonstration showcases MXL version 1.0 in action, exchanging live media across multiple AWS Partner solutions running on three Amazon EC2 g6 instances. This multi-instance, multi-vendor setup illustrates how MXL functions in realistic production environments where workloads are distributed across compute resources and supplied by different software providers. The scenario highlights MXL's role as a connective tissue that allows independently developed media functions to interoperate seamlessly.

### Transport Mechanisms: Shared Memory and EFA RDMA

A central technical highlight is MXL's dual-transport approach for moving uncompressed media efficiently. Within a single EC2 instance, MXL leverages shared memory to pass video, audio, and metadata between media functions with minimal overhead, enabling extremely low latency communication. Between instances, MXL uses Amazon Elastic Fabric Adapter (EFA) with RDMA transport to extend that same low-latency, high-throughput exchange across the network. Together, these mechanisms deliver the performance characteristics required for broadcast-quality live production while preserving the modular, distributed architecture that cloud workflows demand.

### Broadcast Performance Without Vendor Lock-In

The outcome of the demonstration is a clear illustration that broadcasters no longer need to compromise. MXL delivers the broadcast-grade performance traditionally associated with proprietary, tightly integrated systems while keeping workflows open to multiple vendors. This means production teams retain the freedom to choose the tools that best fit each stage of their pipeline, adapt their workflows over time, and modernize their live operations in the cloud without being constrained by single-vendor ecosystems.