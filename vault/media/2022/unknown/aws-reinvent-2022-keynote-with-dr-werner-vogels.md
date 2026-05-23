---
clients:
- Amazon
- AWS
date: 2022-12-02
description: "Dr. Werner Vogels, Amazon.com VP and CTO, talks about the benefits of
  building asynchronous, loosely coupled systems and how event-driven architecture
  enables global scale. He then explains how the cloud is enabling customers to build
  more immersive experiences using 3D and how simulation is empowering customers to
  experiment and innovate in new ways. \n\nLearn more about AWS at https://go.aws/3Vv2JC7.\nASL
  (ASL American Sign Language) is available at https://youtu.be/NSUKeKtDX1I\n\nGuest
  speakers:\n4"
event: unknown
has_transcript: true
language: en
playlist: ''
tags:
- aws
- cloud
- keynote
- event-driven
- architecture
- simulation
- 3d
thematic: media
title: AWS re:Invent 2022 - Keynote with Dr. Werner Vogels
url: https://www.youtube.com/watch?v=RfvL_423a-I
video_id: RfvL_423a-I
year: 2022
---

# AWS re:Invent 2022 - Keynote with Dr. Werner Vogels

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=RfvL_423a-I)
> 📅 2022-12-02 | 🎤 unknown | 🌐 en
> 🏢 Clients: [[Amazon]] [[AWS]]

# AWS re:Invent 2022 Keynote with Dr. Werner Vogels

## Embracing Asynchrony as a Foundational Principle

Dr. Werner Vogels, Amazon.com's VP and CTO, opened his re:Invent 2022 keynote by arguing that the natural world operates asynchronously, and software systems should reflect that reality. He emphasized that synchronous, tightly coupled architectures impose artificial constraints that limit scale, resilience, and evolution. By contrast, loosely coupled systems allow individual components to fail, evolve, and scale independently, producing software that more accurately mirrors how real-world processes unfold.

To illustrate the longevity of these principles, Vogels published Amazon's 1998 Distributed Computing Manifesto, a foundational document that shaped how Amazon decomposed its monolith into services. He pointed to Amazon S3 as a canonical example of a service built on asynchronous, loosely coupled internals, and explained how workflows and a culture of "listen, learn, improve" have allowed AWS to refine these patterns over decades. Building on this theme, he announced **AWS Step Functions Distributed Map**, a new capability enabling massive parallel processing across millions of objects within a single workflow.

### Event-Driven Architectures and Composability

Vogels then expanded the discussion to event-driven architectures, framing events as the natural currency of asynchronous systems. He argued that events are inherently composable, allowing developers to assemble sophisticated business logic from independent, reusable building blocks. To make event-driven development more approachable, he introduced **AWS Application Composer**, a visual tool for designing and building serverless applications, and **Amazon EventBridge Pipes**, which simplifies point-to-point integrations between event producers and consumers with built-in filtering and transformation.

Angela Timofte of Trustpilot joined Vogels on stage to share how Trustpilot adopted event-driven architecture to handle massive review volumes while empowering autonomous teams. She described the cultural and technical journey of decoupling services through events, demonstrating how this approach enabled the company to scale globally while maintaining agility. Vogels reinforced that event-driven architectures are the key to achieving global scale, since they allow systems to absorb spikes, route around failures, and evolve continuously.

### Patterns, Tooling, and Developer Productivity

Recognizing that successful distributed systems rely on well-understood patterns, Vogels highlighted the Amazon Builders' Library as a resource where AWS engineers share hard-won lessons. He then unveiled **Amazon CodeCatalyst**, a unified software development service that integrates project planning, source control, CI/CD pipelines, and collaboration features into a single environment. CodeCatalyst is designed to reduce the friction of starting and operating modern cloud projects, accelerating teams that adopt event-driven approaches.

## Building Multidimensional and Immersive Experiences

Shifting focus, Vogels declared that the world is multidimensional and that 3D experiences are poised to become as pervasive as video is today. He explained how cloud computing now makes it economical to capture, process, and stream rich 3D content at scale. Techniques such as photogrammetry and Neural Radiance Fields (NeRF) are dramatically lowering the barrier to creating photorealistic 3D models from ordinary photographs, while open standards like the Open 3D Engine (O3DE) provide a foundation for interoperable tooling.

He showcased how Matterport uses **AWS IoT TwinMaker** to build digital twins of physical spaces, and how spatial intelligence is enabling new categories of applications. Zoox served as an example of how 3D simulation underpins autonomous vehicle development. Nathan Thomas of Epic Games then took the stage to demonstrate **RealityScan**, a mobile application built with AWS that allows anyone to scan real-world objects into high-fidelity 3D assets, illustrating how cloud-powered 3D capture is becoming accessible to consumers.

### Simulation as a Tool for Experimentation

Vogels presented simulation as one of the most transformative uses of cloud-scale compute, arguing that it allows organizations to experiment safely and innovate faster than physical testing permits. He introduced the **AWS Ambit Scenario Designer** for generating rich virtual environments and demonstrated **AWS SimSpace Weaver**, a managed service for running large-scale spatial simulations across multiple instances. The demo showed how cities, crowds, and complex systems can be modeled at a scale previously reserved for the largest research labs.

### Looking Toward a Quantum Future

Closing the keynote, Vogels turned to the future and focused on quantum simulation, explaining how classical cloud resources can simulate quantum systems to advance research in chemistry, materials science, and cryptography. He framed quantum simulation as an immediate, practical bridge to the quantum era, allowing researchers to develop and validate algorithms today. Vogels concluded by urging builders to embrace asynchrony, event-driven design, immersive 3D, and simulation as the foundations for the next generation of cloud-native systems.