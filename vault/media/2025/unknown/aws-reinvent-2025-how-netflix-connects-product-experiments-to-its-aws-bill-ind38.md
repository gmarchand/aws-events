---
clients:
- Netflix
- AWS
date: 2025-12-03
description: 'How do you measure the cost of innovation? At Netflix, a "winning" A/B
  test can create hidden cloud infrastructure costs that offset its business value.
  This session details our strategy for connecting product experiments to their infrastructure
  costs. We''ll share our framework for identifying an experiment''s impact on our
  cloud systems and show how we translate that impact into a projected AWS cost. Learn
  how this enables our teams to make smarter, more cost-aware product decisions at
  scale.


  L'
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- netflix
- cost-optimization
- ab-testing
- cloud
- finops
- reinvent
thematic: media
title: AWS re:Invent 2025 - How Netflix Connects Product Experiments to its AWS Bill
  (IND388)
url: https://www.youtube.com/watch?v=ulFeSnJlRvk
video_id: ulFeSnJlRvk
year: 2025
---

# AWS re:Invent 2025 - How Netflix Connects Product Experiments to its AWS Bill (IND388)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=ulFeSnJlRvk)
> 📅 2025-12-03 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[AWS]]

# How Netflix Connects Product Experiments to Its AWS Bill

## Introduction: The Hidden Cost of Innovation

Netflix operates at a scale where experimentation drives product evolution, with countless A/B tests running concurrently to refine the user experience. However, a critical blind spot exists in this culture of rapid iteration: a "winning" experiment that improves engagement or business metrics can simultaneously introduce significant, hidden infrastructure costs. These cloud expenses can quietly offset or even exceed the business value the experiment was designed to capture. This session, presented at AWS re:Invent 2025, details Netflix's strategy for closing this gap by directly linking product experiments to their underlying AWS cost implications, enabling smarter and more financially aware product decisions.

## The Framework for Measuring Experiment Cost

### Identifying Infrastructure Impact

Netflix has developed a systematic framework to identify how a given experiment alters the behavior of its cloud systems. Because experiments often introduce new code paths, additional API calls, expanded data processing, or heavier client-side rendering demands, each variant can shift consumption across compute, storage, network, and streaming resources in ways that are not immediately visible to product teams. The framework isolates these consumption deltas between control and treatment groups, attributing changes in resource utilization specifically to the experimental change rather than to broader traffic or seasonal patterns.

### Translating Impact into Projected AWS Cost

Once the infrastructure impact has been measured, Netflix translates that signal into a projected AWS cost figure. By mapping the observed resource changes to the unit economics of the relevant AWS services, the team produces a forward-looking dollar estimate of what scaling the winning variant to the full member base would actually cost. This projection becomes a first-class metric alongside traditional engagement and retention indicators, ensuring that the cost dimension is visible during decision-making rather than discovered after a feature has been rolled out globally.

## Enabling Cost-Aware Product Decisions at Scale

### Empowering Teams with Financial Visibility

The ultimate value of this approach lies in shifting how product teams reason about success. Rather than treating infrastructure as an invisible substrate, engineers and product managers at Netflix can now weigh the projected AWS cost of a feature against its business lift, sometimes choosing to refine an implementation, accept a smaller but more efficient win, or invest in optimization before launch. This transparency transforms cost from a centralized finance concern into a distributed engineering responsibility.

### Outcomes and Broader Lessons

By embedding cost projections into the experimentation platform, Netflix has institutionalized a discipline of measuring the true return on innovation. The session highlights how this practice prevents the gradual accumulation of expensive features that look successful in isolation but degrade overall margin, and it offers a replicable model for any organization running experiments at significant cloud scale. The core lesson is clear: connecting experiments to the AWS bill turns innovation into a measurable economic activity, allowing teams to optimize not just for what users want, but for what the business can sustainably deliver.