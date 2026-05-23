---
clients:
- Netflix
- AWS
date: 2021-12-17
description: Netflix is poised to become the world’s most prolific visual effects
  and animated content studio. To enable their artists around the world, they built
  Netflix Workstations, a secure way to access remote desktops and stream creative
  applications from any data center to any device. Artists can now access high-performing
  virtual workstations on AWS with the freedom to create no matter where they are.
  This session reviews the technologies Netflix used, such as NICE DCV, Amazon EC2
  G4 instances, Spin
event: unknown
has_transcript: true
language: en
playlist: ''
tags:
- streaming
- cloud
- remote-desktop
- vfx
- animation
- aws
- netflix
thematic: media
title: 'AWS re:Invent 2021 - Create from anywhere: The Netflix Workstations story'
url: https://www.youtube.com/watch?v=sEDM4I3Yqbo
video_id: sEDM4I3Yqbo
year: 2021
---

# AWS re:Invent 2021 - Create from anywhere: The Netflix Workstations story

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=sEDM4I3Yqbo)
> 📅 2021-12-17 | 🎤 unknown | 🌐 en
> 🏢 Clients: [[Netflix]] [[AWS]]

# Create from Anywhere: The Netflix Workstations Story

## Empowering a Global Creative Workforce

Netflix is rapidly expanding its position as one of the world's most prolific producers of visual effects and animated content, a trajectory that demands a creative infrastructure capable of supporting artists distributed across continents. To meet this challenge, Netflix built Netflix Workstations, a platform that delivers secure, high-performance remote desktops and streams creative applications from any data center to any device. The solution frees artists from the constraints of physical studio locations, allowing them to produce world-class content from wherever they happen to be working.

## Architecture and Core Technologies

### Streaming Pixels Securely with NICE DCV and EC2 G4 Instances

At the heart of the Workstations platform is NICE DCV, the high-performance remote display protocol that streams pixels from cloud-hosted workstations to artists' endpoints with the responsiveness required for demanding creative software. These desktops run on Amazon EC2 G4 instances, which provide the GPU acceleration necessary for visual effects and animation workloads such as compositing, modeling, and rendering. By centralizing the workstation in AWS rather than shipping powerful hardware to every artist, Netflix preserves the security of pre-release content while still delivering an experience comparable to a physical on-premises workstation.

### Orchestration and Configuration Management

To deploy and manage these workstations at scale, Netflix relies on Spinnaker for continuous delivery and orchestration of the underlying cloud resources, paired with Salt for configuration management of the workstation images and the applications running on them. This combination allows the team to roll out updates, manage software versions across thousands of artists, and maintain consistent, reproducible environments. The result is an operational model where new workstations can be provisioned on demand and kept current with minimal manual intervention.

### A Device- and Location-Agnostic Experience

Because the heavy compute lives in AWS, artists can connect from a wide range of endpoints without sacrificing performance, and Netflix can place workstations in regions close to where its talent lives and works. This geographic flexibility was particularly important for enabling remote and hybrid work patterns and for onboarding production partners and contractors quickly, without the lead time traditionally required to ship and configure dedicated hardware.

## Outcomes and the Road Ahead

The Workstations platform has given Netflix a measurable advantage in scaling its creative pipeline: artists are productive faster, content remains protected within Netflix's controlled cloud environment, and the studio can flex capacity up or down in line with project demand. Looking forward, Netflix sees the Workstations foundation extending well beyond visual effects and animation, with the potential to support a broader range of creative and technical workflows across the company. The session closes with a vision of cloud-based workstations as a general-purpose capability that will continue to reshape how globally distributed teams collaborate on high-end content production.