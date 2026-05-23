---
clients:
- AWS
- Prime Video
- NASCAR
date: 2025-12-07
description: Explore the innovative NASCAR fuel estimation technology developed by
  AWS PACE Prototyping Team for Prime Video's race broadcasts. This initiative aimed
  to bring broadcast innovation through our new fuel tool to the inaugural race series
  on Prime Video. We'll demonstrate how the solution processes streaming telemetry
  data from the cars (which contains no direct fuel information) and applies both
  mathematical and machine learning models to 3-second intervals of the data to estimate
  fuel levels. D
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- machine-learning
- nascar
- prime-video
- sports
- broadcast
- analytics
thematic: media
title: 'AWS re:Invent 2025 - Powering Prime Video''s NASCAR Coverage: ML Fuel Analytics
  in Action (SPF303)'
url: https://www.youtube.com/watch?v=Abk9GMdn2Ig
video_id: Abk9GMdn2Ig
year: 2025
---

# AWS re:Invent 2025 - Powering Prime Video's NASCAR Coverage: ML Fuel Analytics in Action (SPF303)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=Abk9GMdn2Ig)
> 📅 2025-12-07 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Prime Video]] [[NASCAR]]

# Powering Prime Video's NASCAR Coverage: ML Fuel Analytics in Action

## Overview of the Broadcast Innovation Initiative

The AWS Professional Services Acceleration and Customer Engagement (PACE) Prototyping Team partnered with Prime Video to deliver a groundbreaking fuel estimation capability for the inaugural NASCAR race series broadcast on the platform. Because fuel strategy plays a decisive role in race outcomes—often determining when drivers pit, how aggressively they push, and ultimately who wins—giving broadcasters real-time visibility into fuel levels promised to elevate the storytelling and analytical depth of every race. This session explored how the team translated that ambition into a production-ready system capable of operating under the demanding conditions of live motorsport coverage.

## Technical Approach and Solution Architecture

### Working Around the Absence of Direct Fuel Telemetry

The central technical challenge stemmed from the fact that the streaming telemetry feeds coming from each car contained no direct measurement of fuel quantity. To overcome this gap, the team designed a pipeline that ingests telemetry continuously and processes it in three-second intervals, applying a hybrid of mathematical modeling and machine learning to infer fuel consumption rates and remaining fuel levels. By fusing physics-based calculations with a trained ML model for consumption rate, the solution produced reliable fuel estimates from indirect signals such as throttle behavior, speed, and other car performance metrics.

### Real-Time Visualization for Broadcasters

Once the system computes fuel metrics, it surfaces them through visualizations engineered for broadcast use. Producers and on-air analysts can monitor fuel status across the field in real time, allowing them to anticipate pit stops, identify drivers running short, and weave strategic narratives into the live coverage. This transforms what was previously hidden race information into compelling, viewer-facing insight.

### Validation Without Ground Truth

Because no authoritative ground truth fuel data exists for live races, the team adopted a rigorous validation strategy that involved running the system through multiple live races prior to the Prime Video debut. These shadow runs allowed engineers to refine the consumption rate model, tune mathematical parameters, and confirm that both accuracy and latency met broadcast-grade standards before the series went live.

## Outcomes and Impact

The completed solution achieved strong accuracy and low-latency performance suitable for live television production, demonstrating that AWS-built ML pipelines can meet the rigorous demands of professional sports broadcasting. The collaboration delivered a tangible enhancement to Prime Video's NASCAR coverage, equipping commentators with strategic insight that deepens fan engagement, and it stands as a reference example of how prototyping teams can rapidly turn novel data science problems into production systems that influence live viewer experiences.