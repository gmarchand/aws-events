---
clients:
- Netflix
- Amazon
- AWS
date: 2021-12-17
description: "In this session, learn about the challenges of scalable distributed
  training of media machine learning models on multi-GPU nodes used by Netflix and
  how the Amazon FSx solution is used to resolve the data loader performance bottlenecks
  of the training system. See the impressive results in terms of performance and throughput
  improvements on multi-node GPUs and the scalability of Amazon FSx. \n\nLearn more
  about re:Invent 2021 at https://bit.ly/3IvOLtK\n \nSubscribe: \nMore AWS videos
  http://bit.ly/2O3"
event: unknown
has_transcript: true
language: en
playlist: ''
tags:
- machine-learning
- distributed-training
- aws
- fsx
- netflix
- gpu
- cloud
thematic: media
title: AWS re:Invent 2021 - Large-scale distributed training of media ML models with
  Amazon FSx
url: https://www.youtube.com/watch?v=Ayt0PTaoovI
video_id: Ayt0PTaoovI
year: 2021
---

# AWS re:Invent 2021 - Large-scale distributed training of media ML models with Amazon FSx

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=Ayt0PTaoovI)
> 📅 2021-12-17 | 🎤 unknown | 🌐 en
> 🏢 Clients: [[Netflix]] [[Amazon]] [[AWS]]

# Large-Scale Distributed Training of Media ML Models with Amazon FSx

## Overview of the Challenge

Netflix operates at a scale where machine learning models must process vast amounts of media content, including video, audio, and image data, to power recommendations, content understanding, and production workflows. Training these media-focused ML models requires multi-GPU compute nodes capable of handling enormous datasets, but the performance of distributed training systems is often constrained not by compute capacity itself but by the speed at which data can be delivered to the GPUs. This session examines how Netflix encountered and addressed these bottlenecks by leveraging Amazon FSx as the storage backbone for its large-scale training infrastructure.

## Identifying Data Loader Bottlenecks in Distributed Training

### The Nature of Media ML Workloads

Media ML training differs significantly from text or tabular workloads because each training sample can be substantial in size, often consisting of high-resolution video frames or audio segments. When training jobs scale across many GPUs and nodes, the data loader pipeline must continuously feed these large samples to keep expensive GPU resources fully utilized. Netflix observed that as they expanded the number of GPUs participating in a single training job, the data loaders increasingly became the limiting factor, leaving GPUs idle while waiting for input batches. This idle time directly translates into longer training cycles, higher costs, and slower iteration on model development.

### Storage Performance as the Critical Variable

The team determined that the underlying storage layer was central to the data loader bottleneck. Conventional object storage approaches introduced latency and throughput ceilings that could not sustain the aggregate read demand of multi-node GPU clusters. To keep training efficient at scale, the storage system needed to deliver high throughput, low latency, and consistent performance across many concurrent readers.

## Adopting Amazon FSx as the Solution

### Why FSx Fit the Use Case

Amazon FSx, particularly in its high-performance file system configuration, provided the throughput and parallelism required for Netflix's distributed training workloads. By presenting a POSIX-compliant file system optimized for high-performance computing patterns, FSx allowed the existing data loader code to read training samples efficiently without major architectural changes. The service's ability to scale throughput linearly with capacity made it well suited to the bursty, parallel access patterns characteristic of multi-GPU training.

### Performance and Throughput Results

After integrating FSx into the training pipeline, Netflix observed substantial improvements in both per-node and aggregate throughput. GPU utilization rose markedly because data loaders could keep pace with the compute, and training jobs that previously stalled while scaling out were able to maintain near-linear scaling efficiency across additional nodes. The result was faster training times, better hardware utilization, and the ability to experiment with larger models and datasets without storage becoming the limiting factor.

## Scalability and Broader Implications

### Scaling Across Multi-Node GPU Clusters

A key takeaway from the deployment is that FSx scales gracefully as the number of GPU nodes increases. Whereas earlier configurations showed diminishing returns when adding compute capacity, the FSx-backed pipeline preserved throughput per GPU even at high node counts. This scalability is essential for Netflix's continued investment in larger, more sophisticated media models that demand ever-greater training resources.

### Lessons for Distributed ML Practitioners

The session underscores that compute is rarely the sole determinant of training efficiency in modern ML systems. Storage architecture, data loader design, and the interplay between them are equally critical, especially for media workloads with large sample sizes. Choosing a managed high-performance file system such as Amazon FSx can eliminate a major class of bottlenecks and allow ML teams to focus on model quality rather than infrastructure tuning. Netflix's experience illustrates that aligning the storage layer with the demands of distributed GPU training delivers measurable gains in performance, cost efficiency, and developer productivity.