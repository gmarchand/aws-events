---
clients:
- Netflix
- NVIDIA
- AWS
- AMD
- Intel
date: 2024-12-07
description: Netflix deploys various foundation models on standard CPUs and specialized
  accelerated computing chips from providers like NVIDIA, AWS, AMD, and Intel. Optimizing
  instance selection based on price and performance is crucial for rightsizing workloads,
  achieving cost efficiencies, and accurately forecasting infrastructure needs. In
  this session, hear Netflix’s approach to automating FM performance benchmarking
  using FMBench, an open source tool developed by AWS. Learn how FMBench simplifies
  deploy
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- ai
- llm
- foundation-models
- benchmarking
- aws
- netflix
- cloud
thematic: media
title: AWS re:Invent 2024 - How Netflix benchmarks FMs and LLMs across hardware chipsets
  (NFX307)
url: https://www.youtube.com/watch?v=zUjWhiRrp0Y
video_id: zUjWhiRrp0Y
year: 2024
---

# AWS re:Invent 2024 - How Netflix benchmarks FMs and LLMs across hardware chipsets (NFX307)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=zUjWhiRrp0Y)
> 📅 2024-12-07 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[NVIDIA]] [[AWS]] [[AMD]] [[Intel]]

# Benchmarking Foundation Models Across Hardware Chipsets at Netflix

## Overview of the Session

At AWS re:Invent 2024, Netflix presented its approach to systematically evaluating foundation models (FMs) and large language models (LLMs) across a diverse range of hardware accelerators. Because Netflix runs an expanding portfolio of generative AI and machine learning workloads supporting recommendations, content understanding, creative tooling, and operational use cases, the company must continuously match each model to the most appropriate compute platform. The session explored how Netflix uses FMBench, an open source benchmarking tool developed by AWS, to automate this evaluation process and drive data-informed infrastructure decisions on Amazon EC2.

## Why Benchmarking Matters for Netflix

### Balancing Cost, Performance, and Capacity Planning

Netflix deploys foundation models across both standard CPU instances and accelerated computing options that span chips from NVIDIA, AWS (Inferentia and Trainium), AMD, and Intel. Each generation of silicon delivers different trade-offs in latency, throughput, memory bandwidth, and price-per-token, and these characteristics shift dramatically depending on model size, quantization, batch configuration, and prompt length. Selecting the wrong instance can lead to overprovisioned clusters, missed latency targets, or runaway inference costs at Netflix's scale. Rightsizing workloads through rigorous benchmarking therefore directly affects cost efficiency, user-facing performance, and the accuracy of long-range capacity forecasts that the infrastructure team must provide to finance and engineering leadership.

### The Challenge of Manual Evaluation

Performing these comparisons by hand is impractical. Each new model release, chipset generation, or serving framework introduces fresh permutations to test, and consistent methodology is essential to make results comparable. Netflix needed a repeatable, automated, and reproducible workflow that could spin up instances, deploy models, drive realistic load patterns, and capture standardized metrics without bespoke engineering for every experiment.

## Using FMBench to Automate Benchmarking

### How FMBench Works

FMBench, the open source tool from AWS that Netflix adopted, simplifies the end-to-end benchmarking lifecycle. It provisions Amazon EC2 instances, deploys the target foundation model using a chosen serving stack, generates inference traffic according to configurable concurrency and payload profiles, and produces detailed reports. The tool supports a broad matrix of chipsets and serving runtimes, enabling apples-to-apples comparisons between, for example, an NVIDIA GPU-backed instance and an AWS Inferentia or Trainium instance running the same model. Configuration is driven by declarative files, which makes experiments easy to version, share, and rerun as new hardware or model variants become available.

### Metrics That Drive Decisions

The reporting layer captures the metrics Netflix cares about most: end-to-end and per-token latency, sustained throughput under varying concurrency, accuracy against reference outputs, and computed cost-per-million-tokens or cost-per-request. By presenting these dimensions side by side, FMBench allows engineers to identify the price-performance frontier for each workload class and to choose instances based on whether the constraint is interactive latency, batch throughput, or pure cost.

## Outcomes and Key Takeaways

### Data-Driven Infrastructure Choices

By integrating FMBench into its evaluation process, Netflix established a consistent, automated mechanism for selecting the right hardware for each foundation model deployment. The team can now respond quickly to new model releases and new EC2 instance types, validating performance claims with internal data rather than relying on vendor benchmarks alone. This enables more accurate capacity forecasting, reduces inference spend, and ensures that latency-sensitive features meet their service-level objectives.

### Broader Lessons for Practitioners

The session underscored that no single chipset wins across all workloads — optimal choice depends on model architecture, sequence lengths, throughput targets, and cost ceilings. Practitioners running generative AI on AWS were encouraged to adopt a systematic benchmarking discipline, leverage open source tooling like FMBench, and treat hardware selection as an ongoing optimization rather than a one-time decision. Netflix's experience demonstrated that disciplined measurement is the foundation for scaling foundation model deployments efficiently across a heterogeneous compute fleet.