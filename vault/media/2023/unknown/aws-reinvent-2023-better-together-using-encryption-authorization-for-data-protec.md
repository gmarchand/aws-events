---
clients:
- AWS
date: 2023-12-05
description: Encryption and authorization are fundamental to any data protection strategy.
  On premises, these are typically siloed concerns. In AWS, they are deeply aware
  of each other to provide you with more robust, flexible, and granular data protection
  controls that are greater than the sum of their parts. In this session, follow along
  as our representative application evolves, layering in increasingly sophisticated
  controls that protect the embedded data. Deeply explore specific AWS Key Management
  Servi
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- encryption
- authorization
- data-protection
- security
- cloud
thematic: media
title: 'AWS re:Invent 2023 - Better together: Using encryption & authorization for
  data protection (SEC333)'
url: https://www.youtube.com/watch?v=T4_rqwfngfU
video_id: T4_rqwfngfU
year: 2023
---

# AWS re:Invent 2023 - Better together: Using encryption & authorization for data protection (SEC333)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=T4_rqwfngfU)
> 📅 2023-12-05 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]]

# Better Together: Using Encryption and Authorization for Data Protection

## Overview of the Session

At AWS re:Invent 2023, session SEC333 explored how encryption and authorization, traditionally treated as separate disciplines in on-premises environments, work in concert within AWS to deliver data protection controls that exceed the capabilities of either mechanism in isolation. The presentation centered on the premise that AWS Key Management Service (AWS KMS), AWS Identity and Access Management (IAM), and the AWS Nitro System are intentionally designed to be aware of one another, enabling more granular, flexible, and robust safeguards for sensitive data than siloed approaches can achieve.

To make these concepts tangible, the speakers structured the talk around a representative application that evolved throughout the session. With each iteration, they layered in progressively more sophisticated security controls, allowing the audience to observe how encryption and authorization mechanisms reinforce one another as protections become increasingly stringent.

## Core Technical Themes

### Integrating KMS and IAM for Defense in Depth

A central theme of the session was the deep integration between AWS KMS and IAM. Rather than treating key management and access control as independent layers, AWS allows policy authors to combine them so that a request to access encrypted data must satisfy both identity-based permissions and key-based authorization. The speakers walked through specific KMS key policies, IAM policies, and grants, demonstrating how features such as encryption context, condition keys, and key policy statements can be used to tightly scope which principals can decrypt which data under which circumstances. This combination produces a defense-in-depth posture in which compromising a single credential or policy is insufficient to expose protected information.

### Advancing Protection with the Nitro System

The session also examined how the AWS Nitro System extends data protection beyond traditional encryption-at-rest and access-control patterns. By leveraging Nitro Enclaves and the cryptographic attestation capabilities they provide, applications can prove the integrity of the workload requesting access to a key before KMS authorizes a decryption operation. The presenters showed how attestation-based condition keys in KMS policies allow organizations to restrict the use of sensitive keys to specific, verified enclave images, ensuring that even privileged operators or compromised host operating systems cannot access plaintext data. This pattern was presented as a powerful tool for handling highly sensitive workloads such as those involving regulated data or secrets processing.

### Practical Patterns and Policy Design

Throughout the evolution of the example application, the speakers emphasized practical patterns that attendees could apply directly to their own environments. They highlighted the importance of using encryption context as a form of authenticated metadata that ties cryptographic operations to business logic, and they demonstrated how condition keys can enforce that encryption context at policy evaluation time. The discussion also covered how to structure key policies, resource policies, and IAM policies cohesively so that intent is expressed clearly and least privilege is preserved as systems scale.

## Key Takeaways and Outcomes

The principal outcome of the session was a clear demonstration that encryption and authorization in AWS are most effective when designed together rather than as separate concerns. Attendees left with concrete guidance on raising their security bar by combining KMS features, IAM controls, and Nitro-based attestation into cohesive protection strategies. The recommended approach involves starting with foundational encryption and access controls, then incrementally adding context-aware policies and, where warranted by sensitivity, enclave-based attestation to ensure that only verified workloads can operate on protected data. By following this layered evolution, organizations can build applications whose data protection guarantees are substantially stronger than the sum of their individual security mechanisms.