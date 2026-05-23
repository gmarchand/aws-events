---
clients:
- FanDuel
- FanDuel TV
- AWS
date: 2026-05-14
description: FanDuel TV has embarked on a journey to revolutionize its broadcast technologies
  by migrating comprehensive Media & Entertainment workloads to AWS, spanning live
  production, graphics, audio, and distribution. This session explores how organizational
  transformation—not just technology—unlocks cloud’s full potential. Learn how FanDuel
  adopted cross-functional “two-pizza teams” bridging broadcast and cloud expertise,
  breaking down traditional silos. Discover strategies for implementing DevOps, Infr
event: nab-2026
has_transcript: true
language: en
playlist: NAB 2026
tags:
- broadcast
- live-production
- cloud-migration
- aws
- fanduel
- transformation
- media-entertainment
thematic: media
title: 'Breaking Broadcast Silos: How FanDuel TV Transformed Live Production'
url: https://www.youtube.com/watch?v=rwiKLqsG_vc
video_id: rwiKLqsG_vc
year: 2026
---

# Breaking Broadcast Silos: How FanDuel TV Transformed Live Production

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=rwiKLqsG_vc)
> 📅 2026-05-14 | 🎤 nab-2026 | 🌐 en
> 🏢 Clients: [[FanDuel]] [[FanDuel TV]] [[AWS]]

# Breaking Broadcast Silos: How FanDuel TV Transformed Live Production

## Setting the Stage for Transformation

FanDuel TV operates as a uniquely complex media organization, functioning simultaneously as a broadcast provider, signal acquisition provider, and distribution partner. From its Los Angeles studios, the company broadcasts 70,000 horse races annually—each treated as an individual live event requiring full production capabilities despite running only two to three minutes—alongside studio shows like *Up and Adams* and *Run It Back*. The operation curates a "watch and wager" experience by interoperating with FanDuel's race book, sports book, and predictions apps, distributing content across OTT platforms, MVPD partners, cable, satellite, FAST channels, and social media.

Eric Gerard, Director of Engineering for TV Technologies at FanDuel, joined AWS's Ali and Principal ProServe Cloud Architect David Sabine to discuss how the company moved beyond traditional broadcast infrastructure. The catalyst was time-to-market pressure: when business stakeholders requested coverage of events like a WTT pingpong tournament with only days of notice, the existing on-premise infrastructure simply could not procure, deploy, and validate equipment quickly enough. AWS and its marketplace partners offered the repeatable, on-demand infrastructure necessary to meet these demands.

## Navigating Organizational and Cultural Change

### Overcoming Internal Resistance and Restructuring Teams

The transition surfaced significant organizational challenges beyond pure technology. Operations teams that had relied on twenty years of proven broadcast infrastructure were understandably skeptical about trusting cloud-based systems and uncertain about ownership models. Gerard initially explored a shared services arrangement with FanDuel Technology, the company's broader technology division, but discovered that competing product velocity and backlog priorities made this approach unworkable. Stealing engineering time from other parts of the business created friction rather than alignment.

This realization prompted Gerard to build a dedicated DevOps capability within broadcast itself, hiring cloud engineers, network engineers, and software engineers to support the cloud journey natively. While FanDuel had already been on AWS for two to three years prior to engaging with the AWS Live Cloud Production (LCP) program, deployments had been manual and brute-force, lacking CI/CD, Terraform, or Ansible automation. Building an internal team capable of true automation and software-defined operations became essential, since system integrators and AWS ProServe teams would eventually move on to other engagements.

### Empowering Broadcast Engineers as Cloud Builders

Gerard described broadcast engineers as "superheroes" who consistently absorb new technology faster than anyone else in the industry. By investing in AWS Solutions Architect and Terraform certifications, his team—including junior engineers and technicians—rapidly began writing infrastructure-as-code, often picking up skills faster than dedicated software engineers. The lesson for other organizations is clear: trust broadcast engineers, give them the opportunity, and they will flourish. Stepping back as a leader and letting the team build the control rooms and deploy the software themselves proved essential to genuine ownership and enthusiasm.

### The Power of Trusted Partner Voices

A recurring theme was the value of bringing in credible external voices at the right moments. Gerard recounted that messages he had been delivering internally for six months landed immediately when articulated by David Sabine to the same operations teams. The collaboration with Media.Monks provided strong delivery capability, but FanDuel needed deeper AWS expertise for nuanced, sport-specific deployment requirements. Gerard found that partner at the AWS booth at last year's NAB, illustrating that assembling the right blend of system integrators, AWS ProServe specialists, ISV partners, and internal staff is what ultimately produces success.

## Lessons Learned and the Path Forward

### Embracing Mistakes and Two-Way Doors

Gerard's strongest advice for broadcasters beginning similar journeys was to admit uncertainty openly, fail fast, and remain curious. He emphasized leaning into Amazon's leadership principles around two-way doors—reversible decisions that allow rapid pivoting—while avoiding one-way doors. Acknowledging being wrong out loud, he argued, is the single most important behavior for navigating a messy transformation. Transparency about what is known, what requires experimentation, and where critical decision points lie keeps internal teams, AWS, and partners aligned around shared success.

### Defining Success Through Creative Outcomes

Success at FanDuel is not defined by engineering metrics but by operations and production teams. Gerard's measure is whether producers and operators can sit down at a switcher or audio desk and produce shows of equal or better quality without noticing they are working in the cloud. Like-for-like A/B testing between on-premise and cloud productions validates this standard. The ultimate milestone is unplugging the on-premise facility entirely and running cloud productions daily without looking back, with a shadow period planned following NAB.

### Unlocking Innovation Beyond Lift-and-Shift

The transformation extends well beyond replicating existing capabilities. Cloud infrastructure unlocks SOC compliance that was difficult to achieve on-premise, where devices like TD panels could not run security agents like CrowdStrike. Reusable Terraform and Ansible deployments dramatically reduce facility costs and time-to-market. AI services open new product opportunities—real-time speech-to-text could feed the FanDuel sportsbook to surface personalized inventory and graphics to viewers during broadcasts, enabling true watch-and-wager interactivity.

Critically, because the rest of FanDuel and parent company Flutter operate on AWS, FanDuel TV's migration unifies the technology foundation across the enterprise. Following Flutter's "build once, reuse everywhere" principle, product managers from other Flutter brands like PokerStars and Paddy Power can now leverage the media system FanDuel TV has built. The shared services model that proved unworkable as a delivery mechanism has reemerged as a value-creation outcome, with the technology platform and organizational platform together enabling broader business innovation across the company.