---
clients:
- Riot Games
- AWS
date: 2024-12-10
description: Discover how Riot Games, the studio behind League of Legends and VALORANT,
  revolutionized their game server infrastructure with AWS. Explore how they used
  AWS auto scaling to significantly cut their game server fleet costs while boosting
  their ability to rapidly respond to shifts in player demand, which helped them take
  creative risks in updating their games. Learn how they developed a flexible Game
  Provisioning Platform that can automatically spin up game servers tailored to the
  unique requirem
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- gaming
- aws
- cloud
- auto-scaling
- infrastructure
- game-servers
- scalability
thematic: media
title: 'AWS re:Invent 2024 - Effortless game launches: How League of Legends runs
  at scale on AWS (GAM307)'
url: https://www.youtube.com/watch?v=iNYmyuFVMCo
video_id: iNYmyuFVMCo
year: 2024
---

# AWS re:Invent 2024 - Effortless game launches: How League of Legends runs at scale on AWS (GAM307)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=iNYmyuFVMCo)
> 📅 2024-12-10 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Riot Games]] [[AWS]]

# Effortless Game Launches: How League of Legends Runs at Scale on AWS

## Overview of Riot Games' Infrastructure Transformation

Riot Games, the studio behind globally popular titles such as League of Legends and VALORANT, undertook a significant transformation of its game server infrastructure in partnership with AWS. The session at AWS re:Invent 2024 explored how Riot reimagined the way it provisions, scales, and manages the backend systems that power live multiplayer experiences for millions of concurrent players around the world. By leveraging AWS auto scaling capabilities and building a purpose-driven internal platform, Riot achieved meaningful cost reductions while gaining the operational agility needed to support creative experimentation across its growing portfolio of games.

## Scaling Game Servers with AWS

### Reducing Costs Through Elastic Auto Scaling

A central theme of the discussion was how Riot adopted AWS auto scaling to right-size its game server fleets in response to fluctuating player demand. Historically, supporting always-on multiplayer titles required provisioning capacity for peak concurrency, which left substantial resources idle during off-peak hours. By dynamically expanding and contracting fleets in lockstep with real-time player activity, Riot significantly lowered its game server infrastructure costs. Just as importantly, this elasticity gave the studio confidence to take creative risks, knowing that infrastructure could absorb unexpected surges driven by major patches, new game modes, or marketing moments without overprovisioning year-round.

### Responding Rapidly to Player Demand

Beyond cost savings, the elasticity unlocked through AWS allowed Riot's operations teams to react quickly when player behavior changed. Whether responding to viral content, regional engagement spikes, or seasonal events, the company gained the ability to scale capacity within minutes rather than relying on slow, manual capacity planning cycles. This responsiveness directly translates into better player experiences, with reduced matchmaking times and stable session quality even during demand peaks.

## Building a Flexible Game Provisioning Platform

### Standardizing Across Diverse Titles

Riot developed an internal Game Provisioning Platform designed to abstract away the unique infrastructure needs of each title. Because League of Legends, VALORANT, and other Riot games each have distinct technical requirements—ranging from tick rates and session lengths to regional distribution patterns—a one-size-fits-all approach was not viable. The platform instead exposes flexible primitives that game teams configure to spin up game servers tailored to their specific gameplay characteristics, all while reusing a shared, well-tested foundation built on AWS services.

### Accelerating Innovation and Experimentation

The provisioning platform proved especially valuable for accelerating the rollout of new content. Riot's teams can now deploy experimental game modes, limited-time events, and entirely new titles much faster than before, because the underlying infrastructure work is largely automated. This shortens the path from creative idea to live player experience, enabling the studio to test concepts, gather feedback, and iterate with confidence. The result is a healthier innovation pipeline in which infrastructure is no longer a bottleneck to creative ambition.

## Outcomes and Key Takeaways

The collaboration between Riot Games and AWS produced clear, measurable outcomes: substantially lower game server fleet costs, faster response to shifts in player demand, and a reusable provisioning platform that supports the unique needs of multiple titles. The broader lesson for studios and platform teams is that combining cloud-native auto scaling with a thoughtfully designed internal abstraction layer can simultaneously deliver financial efficiency and creative flexibility. For Riot, this foundation positions the company to launch new games, modes, and experiences with greater speed and confidence while continuing to deliver reliable performance to its global player community.