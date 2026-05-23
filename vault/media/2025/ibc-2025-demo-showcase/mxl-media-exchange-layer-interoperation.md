---
clients: []
date: 2025-09-29
description: Broadcasters seek customizable and dynamic live video workflows with
  cost-effective scalability and enhanced operational efficiency, security, and reliability.
  For the highest tiers of live content, they want to combine the best tools for the
  job with uncompressed quality and ultra-low latency. The Media Exchange Layer (MXL)
  is an open-source framework that enables real-time exchange of uncompressed video,
  audio, and metadata between professional media software media functions, as part
  of the EB
event: ibc-2025-demo-showcase
has_transcript: true
language: en
playlist: IBC 2025 Demo Showcase
tags:
- mxl
- live
- broadcast
- interoperability
- low-latency
- uncompressed
- workflows
thematic: media
title: MXL (Media Exchange Layer) interoperation
url: https://www.youtube.com/watch?v=ezje5CJdTuE
video_id: ezje5CJdTuE
year: 2025
---

# MXL (Media Exchange Layer) interoperation

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=ezje5CJdTuE)
> 📅 2025-09-29 | 🎤 ibc-2025-demo-showcase | 🌐 en

# MXL Interoperation: Enabling Cloud-Native Live Broadcast Workflows

## Overview and Industry Context

Broadcasters today face mounting pressure to modernize their live video workflows while preserving the uncompromising quality standards demanded by premium content. They require customizable, dynamic pipelines that scale cost-effectively, operate with enhanced efficiency, and meet stringent security and reliability requirements. For the highest tiers of live broadcasting, this challenge intensifies because operators must combine best-of-breed tools from multiple vendors while maintaining uncompressed quality and ultra-low latency throughout the chain.

The Media Exchange Layer (MXL) addresses this challenge as an open-source framework designed to enable real-time exchange of uncompressed video, audio, and metadata between professional media software functions. MXL forms a core component of the European Broadcasting Union's Dynamic Media Facility (DMF) reference architecture, which provides a blueprint for transitioning traditional broadcast infrastructure toward cloud-native, software-defined operations.

## Multi-Vendor Interoperability Demonstration

### Partner Integration on AWS Infrastructure

The demonstration showcases how multiple broadcast software AWS Partners interoperate seamlessly through MXL, exchanging uncompressed media in real time. Grass Valley, Matrox, TVU Networks, and Riedel each contribute software media functions that communicate with one another using the shared MXL framework, illustrating that broadcasters no longer need to choose a single vendor ecosystem to build complex live workflows. Instead, they can compose pipelines from specialized tools that excel at specific tasks, knowing those tools can pass uncompressed signals between each other without quality loss or latency penalties.

The workflow runs on Amazon EC2 G6 instances powered by NVIDIA L4 Tensor Core GPUs, providing the GPU-accelerated compute necessary to handle uncompressed video processing at scale. This combination demonstrates that even the most demanding live broadcast operations, traditionally tied to dedicated on-premises hardware, can now be executed effectively in the cloud.

### Secure Container Deployment

To support flexible, repeatable deployment of these software media functions, the demonstration leverages Amazon Elastic Container Registry (ECR) for storing, managing, and deploying container instances. ECR provides the secure foundation that broadcasters need when running mission-critical workloads, ensuring that software functions from different partners can be versioned, distributed, and instantiated reliably across the cloud environment.

## Implications for Cloud-Native Broadcasting

By proving that complex multi-vendor live broadcast workflows can transition to cloud-native architectures without sacrificing the uncompressed quality and ultra-low latency that premium content requires, this demonstration marks a significant step toward the Dynamic Media Facility vision. Broadcasters gain the ability to compose dynamic, scalable workflows on demand, drawing from a growing ecosystem of interoperable software media functions while benefiting from the elasticity, security, and operational efficiency of AWS infrastructure.