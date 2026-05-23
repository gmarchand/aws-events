---
clients:
- AWS
- AWS Elemental MediaConvert
date: 2022-06-07
description: 'AWS Elemental MediaConvert has a feature called Automated ABR Configuration
  which automatically customizes the ABR (Adaptive Bit Rate) encoding configuration
  for each source video. Automated ABR Configuration simplifies the set up of transcoding,
  optimizes video quality, and reduces ABR package size. It chooses the ideal rendition
  for the ABR ladder based on a content classification analysis performed during the
  encoding process.


  To learn more, please visit https://aws.amazon.com/mediaconvert/ '
event: aws-at-nab-demos-2022
has_transcript: true
language: en
playlist: AWS at NAB Demos 2022
tags:
- transcoding
- abr
- mediaconvert
- aws
- encoding
- video-quality
- file-based
thematic: media
title: File-based transcoding using Automated ABR Configuration with AWS Elemental
  MediaConvert
url: https://www.youtube.com/watch?v=QMs7fFKHPQw
video_id: QMs7fFKHPQw
year: 2022
---

# File-based transcoding using Automated ABR Configuration with AWS Elemental MediaConvert

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=QMs7fFKHPQw)
> 📅 2022-06-07 | 🎤 aws-at-nab-demos-2022 | 🌐 en
> 🏢 Clients: [[AWS]] [[AWS Elemental MediaConvert]]

# File-Based Transcoding with Automated ABR Configuration in AWS Elemental MediaConvert

## Overview of Automated ABR Configuration

AWS Elemental MediaConvert offers a powerful feature called Automated ABR Configuration that streamlines the creation of adaptive bit rate streaming packages for video-on-demand content. Rather than requiring engineers to manually define each rendition in an ABR ladder, this capability automatically tailors the encoding configuration to the unique characteristics of every source video. By analyzing the content during the encoding process, MediaConvert determines the optimal set of renditions to include, ensuring that each output is purpose-built for the material it represents.

This approach addresses a long-standing challenge in video workflows, where a single static ABR ladder is applied uniformly across diverse content types regardless of complexity, motion, or visual detail. With Automated ABR Configuration, the system intelligently adapts to each asset, removing guesswork from the transcoding setup and delivering more consistent results across a content library.

## Key Benefits and Outcomes

### Simplified Setup and Operational Efficiency

Automated ABR Configuration significantly reduces the operational burden of configuring transcoding jobs. Instead of manually tuning bitrates, resolutions, and rendition counts for different content categories, operators can rely on MediaConvert to make these decisions automatically. This simplification accelerates job setup, lowers the likelihood of misconfiguration, and frees engineering teams to focus on higher-value tasks rather than repetitive encoding parameter tuning.

### Optimized Video Quality

Because the feature performs a content classification analysis during encoding, it selects renditions that are genuinely appropriate for the source material. High-complexity content such as fast-action sports or visually intricate scenes receives a rendition ladder suited to preserving detail, while simpler content avoids unnecessary high-bitrate outputs. The result is consistently strong perceptual quality across the entire library, tailored to what each piece of content actually demands.

### Reduced ABR Package Size

By eliminating renditions that would not meaningfully improve the viewing experience, Automated ABR Configuration produces leaner ABR packages. Smaller package sizes translate directly into reduced storage costs, lower content delivery network egress charges, and more efficient distribution to end users. This efficiency benefits both publishers managing large catalogs and viewers consuming content on bandwidth-constrained connections.

## Practical Application and Further Resources

The feature is designed for file-based, video-on-demand transcoding workflows where source assets vary widely in nature and a one-size-fits-all encoding ladder is suboptimal. Teams adopting this capability gain a workflow that is easier to maintain, more cost-effective to operate, and better aligned with modern streaming quality expectations. Additional technical detail, configuration guidance, and architectural background are available through the AWS Elemental MediaConvert product page and the AWS Media blog post introducing Automated ABR Configuration.