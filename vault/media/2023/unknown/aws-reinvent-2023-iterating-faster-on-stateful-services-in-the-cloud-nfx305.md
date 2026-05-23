---
clients:
- Netflix
- AWS
date: 2023-11-30
description: Netflix has historically coupled changing software with changing hardware
  through “immutable infrastructure,” but this is suboptimal for stateful services
  that need to iterate rapidly on software and configuration without losing their
  valuable state. In order to bring deploy times of kernel, base software, configuration,
  and user software changes down from months to minutes across stateful fleets, Netflix
  Compute and Data Platform teams have built the “Stateful Compute Platform.” In this
  session
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- cloud
- netflix
- stateful-services
- infrastructure
- devops
- reinvent
thematic: media
title: AWS re:Invent 2023 - Iterating faster on stateful services in the cloud (NFX305)
url: https://www.youtube.com/watch?v=v4nLdCHk9ag
video_id: v4nLdCHk9ag
year: 2023
---

# AWS re:Invent 2023 - Iterating faster on stateful services in the cloud (NFX305)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=v4nLdCHk9ag)
> 📅 2023-11-30 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[AWS]]

# Iterating Faster on Stateful Services in the Cloud at Netflix

## The Challenge of Immutable Infrastructure for Stateful Workloads

Netflix has long relied on the principle of immutable infrastructure, a pattern that tightly couples software changes to hardware changes. Whenever the kernel, base operating system, configuration, or user-level software needed to be updated, the corresponding instance was replaced entirely with a freshly provisioned one. While this approach has served stateless services well by providing predictability, reproducibility, and a clean separation between deployments, it creates significant friction for stateful services. Databases, caches, and other systems that hold valuable in-memory or on-disk state cannot simply be torn down and rebuilt without paying substantial costs in data movement, warm-up time, and operational risk. As a result, fleet-wide upgrades that should be routine were taking months to roll out across Netflix's stateful infrastructure, slowing the pace at which the platform teams could deliver security patches, performance improvements, and new capabilities.

## Building the Stateful Compute Platform

To overcome these limitations, Netflix's Compute and Data Platform teams collaborated to build what they call the Stateful Compute Platform. The central goal of this platform is to decouple software iteration from hardware lifecycle so that stateful fleets can be upgraded without losing the state they have painstakingly accumulated. By rethinking how software layers are composed and how state is managed during transitions, the team has compressed deployment timelines from months down to minutes, achieving an order-of-magnitude improvement in how quickly changes propagate across the fleet.

### Compositional Software Layers

A key technique behind this acceleration is compositional software. Rather than baking the kernel, base image, configuration, and application code into a single monolithic artifact that must be replaced as a unit, the platform treats these layers as independently deployable components. This means a kernel patch can be applied without rebuilding user software, and a configuration change can roll out without touching the underlying operating system. This separation dramatically reduces the blast radius of any given change and allows teams to iterate on each layer at its natural cadence.

### Advanced State Management

Equally important is the platform's approach to state management. Because the value of a stateful service lies in the data it holds, the platform provides mechanisms to preserve, hand off, or rapidly reconstruct state across software transitions. These techniques allow instances to be updated in place or replaced with minimal disruption to the data they serve, eliminating the historical tradeoff between deployment velocity and state preservation.

## Outcomes and Impact

The combination of compositional software and sophisticated state-handling primitives has fundamentally changed how Netflix operates its stateful fleets. Upgrades that once required quarter-long campaigns can now be completed in minutes, enabling faster security response, more aggressive performance tuning, and a tighter feedback loop between platform engineers and the services they support. The session ultimately demonstrates how rethinking the assumptions of immutable infrastructure for stateful contexts unlocks substantial gains in operational agility while preserving the reliability and state integrity that Netflix's services demand.