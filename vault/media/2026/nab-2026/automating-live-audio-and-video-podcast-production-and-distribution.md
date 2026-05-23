---
clients:
- AWS
- AWS Elemental
date: 2026-05-13
description: Podcast studios are often operated by on-air talent who expect one-touch,
  start and stop simplicity to manage their production workflows without technical
  crews offering support. This demonstration will use the production of the live Three
  Big Questions with AWS podcast to show an automated multi-camera production, with
  live streaming and fast-turnaround post-recording workflows. Attendees will see
  vertical video dynamically produced by AWS Elemental Inference and lower third graphics
  powered by
event: nab-2026
has_transcript: true
language: en
playlist: NAB 2026
tags:
- podcast
- automation
- live
- audio
- video
- production
- workflow
thematic: media
title: Automating live audio and video podcast production and distribution
url: https://www.youtube.com/watch?v=lJJiMtOWRlg
video_id: lJJiMtOWRlg
year: 2026
---

# Automating live audio and video podcast production and distribution

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=lJJiMtOWRlg)
> 📅 2026-05-13 | 🎤 nab-2026 | 🌐 en
> 🏢 Clients: [[AWS]] [[AWS Elemental]]

# Automating Live Audio and Video Podcast Production and Distribution on AWS

## Overview of the Automated Podcast Workflow

This demonstration showcases how AWS services can transform podcast production into a fully automated pipeline, eliminating the need for dedicated technical crews and allowing on-air talent to focus exclusively on content creation. Using the live production of *Three Big Questions with AWS* as a working example, the session illustrates how a podcast studio can be operated with one-touch simplicity, where talent simply starts and stops recording while sophisticated automation handles every aspect of multi-camera capture, live streaming, post-production, and multi-platform distribution. The architecture is built around the principle that production complexity should be invisible to the people in front of the microphones and cameras.

## Production and Live Streaming Capabilities

### Multi-Camera Capture and Intelligent Vertical Video Generation

The studio operates as a multi-camera environment where the live program is captured and streamed simultaneously. A key innovation is the dynamic creation of vertical video formats powered by AWS Elemental Inference, which intelligently reframes horizontal multi-camera footage into vertical compositions optimized for mobile and social platforms. This eliminates the traditional need to operate separate camera setups or manually crop footage for different aspect ratios, allowing a single production to serve audiences across landscape and vertical viewing experiences without additional human intervention.

### Generative AI for Graphics and Metadata

Lower-third graphics, typically a manual production task requiring an operator to trigger name and title overlays at the right moments, are generated automatically through an Amazon Bedrock-based generative AI workflow. This same generative AI capability extends to producing descriptive metadata and summaries that travel with the finished podcast assets, ensuring that distribution-ready files arrive at partner platforms with rich, contextually appropriate information already attached.

## Post-Production and Multi-Platform Distribution

### Fast-Turnaround Packaging Following Media Lake Guidance

Once a recording session ends, automated post-production workflows assemble finished on-demand versions of the podcast, packaging both the video and audio along with their associated metadata. These workflows follow the Guidance for a Media Lake on AWS, providing a structured and scalable foundation for storing, processing, and routing media assets through the production lifecycle without manual file handling.

### Delivery to Podcast and Broadcast Partners

The completed assets flow automatically to multiple distribution endpoints tailored for each medium. Video and on-demand podcast versions are delivered to partners such as ART19 and Triton Digital, while audio versions are routed through RCS Works and Radio.Cloud for traditional radio broadcast. This multi-destination distribution happens without operator involvement, demonstrating an end-to-end pipeline in which a single recording session yields polished, platform-specific outputs across streaming, on-demand, social, and broadcast channels.

## Outcome and Significance

The result is a production model that fundamentally shifts the economics and accessibility of podcast creation. By orchestrating AWS Elemental services, Amazon Bedrock, and media lake architecture into a cohesive automated pipeline, talent-operated studios can produce broadcast-quality, multi-format content at scale. The demonstration confirms that combining cloud media services with generative AI removes the historical dependency on technical production crews, enabling creators to deliver consistently across audio, video, vertical, and radio formats while automation manages the underlying complexity end-to-end.