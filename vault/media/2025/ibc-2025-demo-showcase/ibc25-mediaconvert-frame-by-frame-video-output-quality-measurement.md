---
clients:
- AWS Elemental MediaConvert
- AWS
date: 2025-09-29
description: Content providers need frame-level video quality insights to optimize
  their encoding workflows and troubleshoot quality of experience (QoE) issues. AWS
  Elemental MediaConvert now provides detailed video quality metrics for every frame
  in your output. This demo showcases a visualization tool that displays MediaConvert
  frame-by-frame quality data directly in a video player. Use it to validate that
  your adaptive bitrate (ABR) streams meet quality objectives and optimize the balance
  between video qu
event: ibc-2025-demo-showcase
has_transcript: true
language: en
playlist: IBC 2025 Demo Showcase
tags:
- encoding
- video-quality
- mediaconvert
- aws
- qoe
- metrics
- broadcast
thematic: media
title: IBC25   MediaConvert   frame by frame video output quality measurement
url: https://www.youtube.com/watch?v=QpgNcuDlXiE
video_id: QpgNcuDlXiE
year: 2025
---

# IBC25   MediaConvert   frame by frame video output quality measurement

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=QpgNcuDlXiE)
> 📅 2025-09-29 | 🎤 ibc-2025-demo-showcase | 🌐 en
> 🏢 Clients: [[AWS Elemental MediaConvert]] [[AWS]]

# Frame-by-Frame Video Quality Measurement in AWS Elemental MediaConvert

## Overview of the New Capability

AWS Elemental MediaConvert has introduced a powerful new feature that delivers detailed video quality metrics for every individual frame in encoded outputs. This advancement addresses a critical need among content providers who require granular, frame-level visibility into their encoding workflows. By exposing quality data at this level of precision, MediaConvert empowers media engineers to optimize their adaptive bitrate (ABR) streams, troubleshoot quality of experience (QoE) issues, and make data-driven decisions about encoding configurations.

The capability transforms how content owners validate their video pipelines. Rather than relying on aggregate scores or sampled measurements, teams can now examine the precise quality characteristics of each frame, identifying problem segments and ensuring that every portion of the stream meets defined quality thresholds.

## How the Visualization Tool Works

### Integrating Quality Metrics with Playback

The demonstration centers on a visualization tool that overlays MediaConvert's frame-by-frame quality data directly within a video player. As the content plays, the tool surfaces the corresponding quality metrics in real time, allowing viewers to correlate visual artifacts or quality variations with the underlying numerical data. This tight coupling between playback and metrics provides an intuitive way to inspect encoder behavior across the entire duration of an asset.

By presenting quality measurements alongside the actual video, engineers can immediately identify scenes where the encoder struggled, where bitrate allocation may have been suboptimal, or where compression artifacts appeared. This contextual presentation transforms raw metric data into actionable insights that would otherwise require extensive manual correlation.

### Validating ABR Streams and Optimizing Efficiency

A primary use case for the tool is validating that adaptive bitrate ladder renditions consistently meet predefined quality objectives. Content providers configure ABR streams to balance bandwidth consumption against viewer experience, and the visualization tool reveals whether each rendition delivers the expected quality across all frames. When deviations occur, engineers can pinpoint the exact frames responsible and adjust encoding parameters accordingly.

Beyond validation, the tool supports ongoing optimization of the trade-off between video quality and data efficiency. Teams can experiment with different encoding settings and immediately observe the frame-level impact, enabling them to reduce bitrate where quality permits while preserving fidelity in demanding scenes. This data-driven approach helps reduce delivery costs without compromising the viewer experience.

## Business Impact for Content Providers

The introduction of frame-level quality metrics in MediaConvert positions content providers to deliver more consistent streaming experiences while controlling encoding and distribution costs. Granular insight into encoder performance shortens troubleshooting cycles for QoE issues, accelerates iteration on encoding profiles, and provides the evidence needed to justify configuration changes. Ultimately, the combination of MediaConvert's detailed metrics and the demonstrated visualization workflow gives media organizations a robust framework for continuously improving video quality across their entire ABR delivery pipeline.