---
clients:
- Netflix
- AWS
date: 2023-12-04
description: As big data and ML became more prevalent and impactful, the scalability,
  reliability, and usability of the orchestrating ecosystem have become increasingly
  important for Netflix. To better serve various business needs, Netflix has developed
  a new workflow orchestrator called Maestro, which greatly improves the usability
  and scalability of the orchestration system and boosts the productivity of the engineers
  working with data. Maestro provides support to run super-large-scale workflows,
  consistin
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- reinvent
- netflix
- ml
- data
- workflow-orchestration
- cloud
thematic: media
title: 'AWS re:Invent 2023 - Netflix Maestro: Orchestrating scaled data & ML workflows
  in the cloud (NFX308)'
url: https://www.youtube.com/watch?v=kPYPgR0Gzrs
video_id: kPYPgR0Gzrs
year: 2023
---

# AWS re:Invent 2023 - Netflix Maestro: Orchestrating scaled data & ML workflows in the cloud (NFX308)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=kPYPgR0Gzrs)
> 📅 2023-12-04 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[AWS]]

# Netflix Maestro: Orchestrating Scaled Data and ML Workflows in the Cloud

## Overview and Motivation

Netflix's data platform supports an expansive ecosystem of analytics, machine learning, and content decision-making workflows that drive nearly every aspect of the streaming business. As big data and machine learning have grown more central to Netflix's operations, the orchestration layer that coordinates these workloads has faced mounting pressure to scale, remain reliable, and stay accessible to a diverse set of users ranging from data engineers and scientists to content analysts. The previous orchestration tooling at Netflix struggled to keep pace with the volume of jobs, the complexity of dependency graphs, and the heterogeneity of user personas. To address these challenges, Netflix engineered Maestro, a new workflow orchestrator purpose-built to improve usability, scalability, and engineering productivity across the company's data and ML platforms.

## Maestro's Design and Capabilities

### Architecture and Scalability

Maestro is designed to run extremely large-scale workflows that can encompass hundreds of thousands of jobs organized into nested, hierarchical structures. Rather than treating each workflow as a flat directed acyclic graph, Maestro embraces composition, allowing teams to build sub-workflows and reusable components that can be combined into larger pipelines. This nested model enables Netflix to express deeply complex data and ML pipelines while keeping individual workflow definitions manageable. The system runs in the cloud and is engineered for horizontal scalability, fault tolerance, and consistent execution semantics so that orchestration itself never becomes a bottleneck for the business.

### Lineage, Signals, and Event-Driven Triggering

A defining feature of Maestro is its ability to maintain lineage information that connects event signals, workflows, and the data tables they produce or consume. This lineage tracking gives engineers and scientists visibility into how datasets are generated and how downstream pipelines depend on upstream sources. Maestro also supports event-driven and signal-based triggering, allowing workflows to start automatically when upstream data becomes available rather than relying purely on time-based schedules. The result is a more reactive, data-aware orchestration model that reduces wasted compute and shortens the time between data arrival and downstream insight.

### Usability and Developer Productivity

Beyond raw scalability, Maestro emphasizes developer experience. The platform provides interfaces and abstractions that let users define and operate workflows without needing deep knowledge of orchestration internals, while still offering the flexibility advanced users require for ML and data engineering tasks. By unifying support for batch data pipelines and machine learning workflows under a single orchestrator, Netflix has reduced the cognitive overhead of moving between systems and improved the productivity of teams working across the data lifecycle.

## Outcomes and Takeaways

By rebuilding its orchestration foundation around Maestro, Netflix has positioned its data and ML platforms to handle continued growth in workload size and complexity while improving the daily experience of the engineers who depend on them. The combination of nested workflow composition, lineage tracking between signals, workflows, and tables, and event-driven execution illustrates how purpose-built orchestration can serve as critical infrastructure for modern, large-scale data organizations. The session highlights Maestro as both a practical solution to Netflix's specific scaling challenges and a broader example of how enterprises can rethink workflow orchestration to better support the convergence of data engineering and machine learning in the cloud.