---
clients:
- CloudFront
date: 2026-05-13
description: "Content providers and streaming platforms struggle to secure video delivery
  while maintaining performance at scale. Traditional authentication methods add latency,
  create bottlenecks at origin servers, and lack fine-grained access controls for
  different content types, devices, or geographic regions. \n\nThis demonstration
  shows how CBOR Web Tokens (CWT) and Common Access Tokens (CAT) deliver secure token-based
  authentication and authorization with CloudFront Functions at CloudFront Edge Locations."
event: nab-2026
has_transcript: true
language: en
playlist: NAB 2026
tags:
- streaming
- security
- authentication
- cwt
- cdn
- access-tokens
- video-delivery
thematic: media
title: Secure streaming delivery using Common Access Tokens and CBOR Web Tokens
url: https://www.youtube.com/watch?v=WHnS97Qz-4Y
video_id: WHnS97Qz-4Y
year: 2026
---

# Secure streaming delivery using Common Access Tokens and CBOR Web Tokens

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=WHnS97Qz-4Y)
> 📅 2026-05-13 | 🎤 nab-2026 | 🌐 en
> 🏢 Clients: [[CloudFront]]

# Secure Streaming Delivery Using Common Access Tokens and CBOR Web Tokens

## Overview of the Challenge and Solution

Content providers and streaming platforms face a persistent tension between securing video delivery and maintaining performance at scale. Traditional authentication mechanisms introduce latency, concentrate load on origin servers, and offer limited flexibility when access policies need to vary by content type, device, or geography. As streaming audiences grow globally, these limitations translate directly into degraded viewer experiences and rising infrastructure costs.

This demonstration presents a modern approach that addresses these issues by combining CBOR Web Tokens (CWT) and Common Access Tokens (CAT) with CloudFront Functions executed at CloudFront edge locations. The result is a lightweight, high-performance authentication and authorization layer that operates close to viewers, enforcing fine-grained access policies without burdening origin infrastructure.

## Token Technologies and Their Advantages

### Compact Binary Tokens with CWT

CBOR Web Tokens provide a compact, binary alternative to traditional JSON Web Tokens. By using Concise Binary Object Representation (CBOR) encoding instead of verbose JSON, CWTs reduce token size and parsing overhead, which is particularly valuable in latency-sensitive streaming workflows. The tokens leverage CBOR Object Signing and Encryption (COSE) to deliver cryptographic integrity and confidentiality, ensuring that authentication credentials remain trustworthy as they traverse the delivery path.

### Fine-Grained Authorization with CAT

Common Access Tokens build on the CWT foundation by adding richer authorization semantics tailored to streaming use cases. CAT supports constraints such as URL pattern matching, IP-based restrictions, and HTTP method limitations, allowing operators to express nuanced access policies within the token itself. This expressiveness enables differentiated treatment of various content types, devices, and regions without requiring custom logic at the origin.

### Edge Execution with CloudFront Functions

Validating these tokens directly at CloudFront edge locations through CloudFront Functions delivers sub-millisecond execution times. Because authorization decisions happen at the edge, requests are accepted or rejected before reaching the origin, dramatically reducing origin load while keeping enforcement geographically close to viewers.

## Outcomes and Benefits

The combined approach yields enhanced security without sacrificing performance. Streaming platforms gain flexible, policy-driven access control that scales globally, origin servers experience reduced traffic and load because unauthorized requests are filtered at the edge, and viewers benefit from low-latency playback experiences. By adopting CWT and CAT with CloudFront Functions, content providers can implement robust, future-ready authentication mechanisms that meet the demands of modern, large-scale video delivery.