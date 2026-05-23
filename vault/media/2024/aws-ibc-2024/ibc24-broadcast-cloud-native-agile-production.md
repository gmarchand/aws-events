---
clients: []
date: 2024-09-10
description: 'Fast-turnaround workflows for news, sports, and entertainment shows
  today face challenges such as vendor lock-in and inflexible or costly solutions.
  This has made it difficult to realize the business benefits of moving these workflows
  to the cloud.


  Cloud Native Agile Production (CNAP) is a cloud-native, open, and interoperable
  way of creating fast-turnaround content in the cloud. The system utilizes chunked
  media held in an open-source Time-addressable Media Store (TAMS) that ingests live
  feeds'
event: aws-ibc-2024
has_transcript: true
language: en
playlist: AWS IBC 2024
tags:
- cloud-native
- broadcast
- production
- workflows
- news
- sports
- cloud-migration
thematic: media
title: IBC24 - Broadcast - Cloud Native Agile Production
url: https://www.youtube.com/watch?v=wjGZstStGuk
video_id: wjGZstStGuk
year: 2024
---

# IBC24 - Broadcast - Cloud Native Agile Production

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=wjGZstStGuk)
> 📅 2024-09-10 | 🎤 aws-ibc-2024 | 🌐 en

# Cloud Native Agile Production (CNAP) at IBC24

## Overview and Industry Challenge

Fast-turnaround production workflows in news, sports, and entertainment have long struggled with vendor lock-in, inflexible tooling, and prohibitive costs that have hindered the migration of these processes to the cloud. While broadcasters have widely embraced cloud computing for storage, distribution, and post-production, the agile, time-sensitive nature of live and near-live content creation has remained tethered to traditional on-premises infrastructure. The Cloud Native Agile Production (CNAP) initiative directly addresses these obstacles by offering an open, interoperable, and cloud-native architecture purpose-built for rapid content creation.

## The CNAP Architecture

### Time-Addressable Media Store as the Foundation

At the core of CNAP lies the Time-addressable Media Store (TAMS), an open-source system that fundamentally rethinks how media is held and accessed in the cloud. Rather than treating media files as monolithic assets that must be copied, moved, and duplicated between systems, TAMS ingests live feeds and breaks them into chunked media elements arranged on a scalable timeline. Each chunk receives a unique identifier, allowing any tool, team, or workflow to reference precisely the segment it needs without ever creating a copy. This chunked, addressable approach removes the redundant data duplication that has historically plagued cloud production workflows and made them economically unattractive.

### Metadata-Only Operations and Interoperability

A defining characteristic of CNAP is its ability to perform metadata-only operations. Edits, rearrangements, and references can all be executed by pointing to existing media chunks rather than copying or re-encoding content, dramatically reducing storage costs, processing overhead, and turnaround times. Because the architecture is open and interoperable, multiple platforms, applications, and teams can collaborate on the same source material concurrently, eliminating the silos that traditionally form between ingest, editing, and playout systems.

### End-to-End Demonstrated Workflow

The IBC24 demonstration showcased a complete CNAP pipeline running from initial live ingest through to on-air playback. Content captured into TAMS was manipulated in parallel by two distinct editing environments: a lightweight browser-based editor suitable for journalists and remote contributors, and a virtual workstation-based editing system offering the depth required by professional craft editors. Both tools operated against the same chunked media without duplicating assets. The finished material was then handed off to a live vision mixer for gallery playback, completing the journey from camera to broadcast entirely within a cloud-native, open framework.

## Outcomes and Significance

By combining the open-source TAMS with chunked media addressing and metadata-only operations, CNAP delivers the business benefits that cloud migration has long promised but rarely achieved for fast-turnaround production: vendor independence, cost efficiency, and the ability to scale workflows elastically across teams and geographies. The IBC24 showcase positions CNAP as a credible blueprint for broadcasters seeking to modernize news, sports, and entertainment production without sacrificing the agility that live content demands.