---
clients:
- AWS Elemental MediaTailor
- AWS
date: 2025-09-29
description: Customers want to monetize live video while offering digital video recorder
  (DVR) features and reducing impact on viewers. This demo showcases server-guided
  ad insertion (SGAI) using HLS Interstitials with AWS Elemental MediaTailor in a
  live streaming environment with extended DVR functionality. Visitors can observe
  how pre-roll ads play once while preserving underlying content, and how timeline
  scrubbing to mid-roll positions triggers ad requests and delivery. The demo illustrates
  how SGAI opti
event: ibc-2025-demo-showcase
has_transcript: true
language: en
playlist: IBC 2025 Demo Showcase
tags:
- hls
- live
- dvr
- ad-insertion
- mediatailor
- aws
- streaming
thematic: media
title: HLS Interstitials with live DVR functionality with AWS Elemental MediaTailor
url: https://www.youtube.com/watch?v=p46_bVg73oQ
video_id: p46_bVg73oQ
year: 2025
---

# HLS Interstitials with live DVR functionality with AWS Elemental MediaTailor

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=p46_bVg73oQ)
> 📅 2025-09-29 | 🎤 ibc-2025-demo-showcase | 🌐 en
> 🏢 Clients: [[AWS Elemental MediaTailor]] [[AWS]]

# HLS Interstitials with Live DVR Functionality Using AWS Elemental MediaTailor

## Overview of Server-Guided Ad Insertion in Live Streaming

This demonstration explores how broadcasters and streaming providers can monetize live video content while preserving a high-quality viewer experience and supporting digital video recorder (DVR) capabilities. The featured technology combines HLS Interstitials with AWS Elemental MediaTailor to deliver server-guided ad insertion (SGAI) within a live streaming environment that offers an extended DVR window. By leveraging this approach, content providers gain greater control over how and when advertisements appear, while viewers retain the flexibility to navigate through previously aired content without disruption.

The core challenge addressed by this solution centers on balancing monetization needs with viewer satisfaction. Traditional ad insertion methods often interrupt the underlying stream or replace content in ways that compromise the DVR experience. SGAI with HLS Interstitials resolves these issues by treating ads as discrete, server-guided events that the player can manage intelligently, leaving the primary content intact and available for replay.

## Demonstration of Ad Insertion Behaviors

### Pre-Roll Ad Playback and Content Preservation

The demo first showcases pre-roll ad behavior, where an advertisement plays once at the start of the viewing session before transitioning into the live stream. Critically, this pre-roll insertion does not alter the underlying content timeline. Viewers who continue watching are not subjected to repeated pre-roll exposure, and the live content beneath the ad remains fully preserved within the DVR window. This design ensures that monetization opportunities at the session start do not compromise the integrity of the recorded stream.

### Mid-Roll Ad Triggering Through Timeline Scrubbing

The demonstration then highlights mid-roll ad behavior tied to DVR navigation. When a viewer scrubs along the timeline to a mid-roll position, the player triggers an ad request, and MediaTailor dynamically delivers and inserts the appropriate advertisement at that moment. This capability allows ad placements to remain relevant and well-targeted even when viewers consume content asynchronously through DVR functionality. The seamless transition between scrubbed positions and inserted ads illustrates how SGAI maintains a smooth playback experience without breaking the live stream's structural continuity.

### Monetization, Control, and Measurement Benefits

By combining HLS Interstitials with MediaTailor's server-guided approach, the solution delivers three key advantages: optimized monetization through additional and more flexible ad opportunities, precise control over ad placement that respects content boundaries and viewer context, and improved measurement capabilities that give content owners better insight into ad performance. The extended DVR window further amplifies these benefits by enabling monetization across a broader window of viewing activity rather than only during real-time playback.

## Conclusion

The demonstration establishes that AWS Elemental MediaTailor, paired with HLS Interstitials and SGAI, offers a robust framework for monetizing live streams while supporting modern DVR experiences. Content providers can deliver pre-roll and mid-roll ads with confidence that the underlying content remains intact, viewer navigation is respected, and ad placements are both timely and measurable. This approach represents a practical path forward for streaming services seeking to balance revenue generation with viewer-friendly playback features.