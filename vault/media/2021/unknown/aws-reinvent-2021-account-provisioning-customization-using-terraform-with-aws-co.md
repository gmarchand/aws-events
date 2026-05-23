---
clients:
- AWS
- Terraform
date: 2021-12-17
description: If you create AWS accounts on a regular basis and need to  make sure
  that those accounts meet all of your users’ needs while also  meeting your business
  and security policies, infrastructure-as-code (IaC)  tools are essential for automation,
  including the popular IaC solution  Terraform. Join this session to learn about
  the newly launched AWS Control  Tower Account Factory for Terraform (AFT), which
  enables you to provision AWS  Control Tower managed accounts through Terraform IaC
  pipelines. Lea
event: unknown
has_transcript: true
language: en
playlist: ''
tags:
- aws
- terraform
- cloud
- automation
- security
- iac
- devops
thematic: media
title: AWS re:Invent 2021 - Account provisioning & customization using Terraform with
  AWS Control Tower
url: https://www.youtube.com/watch?v=8Ot5wn7kxI0
video_id: 8Ot5wn7kxI0
year: 2021
---

# AWS re:Invent 2021 - Account provisioning & customization using Terraform with AWS Control Tower

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=8Ot5wn7kxI0)
> 📅 2021-12-17 | 🎤 unknown | 🌐 en
> 🏢 Clients: [[AWS]] [[Terraform]]

# Account Provisioning and Customization Using Terraform with AWS Control Tower

## Session Overview

This AWS re:Invent 2021 session addresses a common challenge faced by organizations that regularly create AWS accounts: ensuring each new account satisfies user requirements while simultaneously enforcing business and security policies. The session positions infrastructure-as-code (IaC) as the essential mechanism for automating this process at scale and focuses specifically on integrating Terraform, one of the most widely adopted IaC tools, with AWS Control Tower. The central announcement of the talk is the newly launched AWS Control Tower Account Factory for Terraform (AFT), which extends the account provisioning capabilities of Control Tower into Terraform-driven workflows.

## Account Factory for Terraform

### Purpose and Capabilities

AWS Control Tower Account Factory for Terraform enables organizations to provision Control Tower managed accounts directly through Terraform infrastructure-as-code pipelines. Rather than provisioning accounts manually or through separate tooling, AFT allows teams to treat account creation as a versioned, reviewable, and repeatable IaC artifact. This approach brings the standard benefits of IaC—auditability, consistency, and automation—to the foundational task of establishing new AWS accounts within a multi-account environment governed by Control Tower.

### Pipeline-Driven Provisioning and Customization

The session demonstrates how a Terraform IaC pipeline can drive one-click account creation, after which the pipeline automatically triggers additional customizations to enhance the newly provisioned account. These customizations allow organizations to layer their specific guardrails, baseline configurations, networking, identity integrations, and security controls onto each account as it is created, ensuring that every new account emerges from the pipeline already aligned with organizational standards. By combining Control Tower's governance model with Terraform's declarative configuration, AFT closes the gap between account creation and account readiness, reducing the manual effort traditionally required to bring a new account into compliance with internal policies.

## Key Takeaways

The session ultimately positions AFT as a strategic capability for organizations standardizing on Terraform: it eliminates bespoke scripting around account vending, enforces governance from the moment an account is created, and provides a single, pipeline-based workflow for both provisioning and post-creation customization. Teams responsible for landing zones, platform engineering, and cloud governance are the primary beneficiaries, gaining a sanctioned path to scale account creation without sacrificing the consistency and security posture that Control Tower is designed to enforce.