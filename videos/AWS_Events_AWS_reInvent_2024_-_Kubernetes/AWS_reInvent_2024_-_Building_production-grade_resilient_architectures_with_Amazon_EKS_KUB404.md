# AWS re:Invent 2024 - Building production-grade resilient architectures with Amazon EKS (KUB404)

[Video Link](https://www.youtube.com/watch?v=g9USwIPr7Xs)

## Description

Platform teams need to effectively manage thousands of clusters to meet the demands of growing organizations. In this session, learn how to manage and upgrade clusters at scale without compromising security, resiliency, performance, and cost. See how you can use open source tools like ACK, Argo CD, and Backstage to build and maintain Amazon EKS clusters at scale, as well as provide a single pane of glass as an inventory of Amazon EKS clusters across your entire AWS organization. Explore architecture techniques to ensure workload resiliency with enhanced observability, enabling rapid issue identification across Amazon EKS clusters.

Learn more:
AWS re:Invent: https://go.aws/reinvent.
More AWS events: https://go.aws/3kss9CP 

Subscribe:
More AWS videos: http://bit.ly/2O3zS75
More AWS events videos: http://bit.ly/316g9t4

About AWS:
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts. AWS is the world's most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWSreInvent  #AWSreInvent2024

## Transcript

- So this talk is
building production-grade resilient architectures with Amazon EKS. In short is building Amazon
EKS cluster with resiliency. My name is Carlos Santana. I don't play the guitar. I always have to make that joke. (audience laughing) So you can go to the House
of Blues here in Las Vegas, and here's some Carlos Santana music. But I'm a senior specialist
solutions architect in containers that includes EKS and ECS. And with me is Niall. He's a principal specialist
solutions architect in containers, both on EKS
and ECS, pretty much, right? But for today, we're going to
be talking about Kubernetes running on AWS using EKS. So the agenda for today, we had a lot of topics to choose from. We one hour of a session, we had to choose some
aspects that come together in a story around platform
engineering on top of EKS so we choose to talk about management, observability, and governance. So that's what pretty much
what we're going to talk today. Talking about platforms. Everybody starts building their platforms and builders, right? These are the folks that are in charge of the cloud resources
in the organization. And what builds a platform
is building for teams. They're organized by teams. And then you have your applications that you run to run on AWS and then you have your infrastructure. So pretty much, it boils
down to three aspects. You have teams, you have applications that you have to put those
applications somewhere in the infrastructure. Talking about platforms, the idea is that these platform
engineers build abstractions and they accelerate how they
build these applications on AWS providing cloud infrastructure
as easy as possible with autonomy to those teams. This is a stat that by
July, last July of 2024, there's more clusters being managed by AWS in this terms of EKS. 33% growth year over year. So the amount of clusters
that folks are configuring, deploying, and managing and upgrading, it's increasing year by year. So there's a stat that's in there. And what are the challenges that platform teams have when they come into managing this cluster. So today, we're going to
look into three areas. One is this life cycle of
the cluster from deployment to upgrade on how to develop a
consistent ecosystem process. The next one is enforcing best
practices across all clusters by not monitoring them
and also the applications. But for today, we're going to concentrate more of the clusters and the system wise software
that runs on those clusters. And last, providing guardrails
to support the teams that need these clusters and giving them the right
amount of autonomy, right? They need a cluster, they're developers, but they need guardrails. So let's start with the
first topic of management. And this is how it looks like. We generally see customers
with a repo Git resource. Some kind of infrastructure
as code tooling, like Terraform, CloudFormation. I heard somebody here in the
audience talking about CDK. Pulumi and others infrastructure as code that the state lives in
a object store like S3. And then they will deploy a cluster. Then they will use the same
infrastructure as code tooling to deploy Kubernetes resources, saving the state of these
Kubernetes resources in the same location at,
for example, the S3 bucket. For Kubernetes resources,
this might be pragmatic, but for simple cluster
management, not a problem at all. And then, things starts growing. Then you as a platform engineer,
you start getting requests as that teams need another EKS cluster. So you copy paste, right? That pipeline move it on,
and you get a second cluster and create a new pipeline. Then it gets to this level. So raise your hand if
you have an organization that it looks like this. Having a lot of pipelines,
deploying a lot of EKS clusters. It grows, the growth continues. This becomes unmanageable. Too many versions of the pipeline because you're copy pasting to track which clusters is up-to-date. These without thinking what is inside of each cluster, right? The resources and application. It's not uncommon to see many
pipelines in our organization. So this is a lot of snowflakes, right? Each one individually, you can say that it's an cluster, but you look closer, they have a different version. So what are the application
they have inside? And each one has an old version of a variation of a pipeline. So what are the key challenges to restate in terms of management? When you have unmanaged
growth of clusters, what are the some key challenges? Enforcing standards across
your fleet of clusters. So now we're talking
about fleet of clusters becomes hard to automate
those deployments. When you have automation, how do you configure a
single source of truth for all of them? Out of management becomes
something that gets out of control with so much open source projects. The team cannot be an expert
on every add-on out there that you put in your clusters. And lastly, workload management. How to match the best
instance type, in case of EC2 to a workload? And also do cost
optimization on top of it. So this is something that
we see from the field. Me and Niall, we work on
the field with customers, probably some of you. And we work with customers
that are trying to configure and deploy EKS clusters and
building kind of like a pattern or how do we serve these teams
that are in the organization. So we see a lot of ways of clusters that are provisioning organizations. Templates as a service,
this is in the website. It's used by many platform teams initially since it's a low barrier to entry, like the platform team will
be, I create a template, give it to the dev team, and then they will create a cluster. But this becomes hard to manage a scale. Development teams guess what? Not to upgrade their clusters. If you are in the platform
team dealing with EKS clusters, you know that you need
upgrade them, patch them, and release new updates. It just give them that
template to the dev team. They will just run it once and then never go back to
upgrade those clusters. Platform teams taking more
ownership, providing a service. So let's take a look at what we advertise. So the first one is customers
cluster as a service, giving a cluster to a team, but the platform team
managing the cluster itself, making sure that they're the
ones upgrading the cluster, upgrading the add-ons. Another one is namespace as a service. So namespace as a service is something that the team would have a discussion or maybe a form that asks the team, like, how many resources do you
need in that namespace? So the platform teams
can set resource quotas and Kubernetes that are
APIs that you can configure or maybe limit ranges or
default for request and limits. And that way, you get a namespace created by this platform team. And then the team can
deploy inside of them. And the last one is maybe the
team, the only team that needs to provide to the platform team is give me an application,
I'll give you a ripple. And they don't know that their application is running on Kubernetes. They only care about what
getting their application on Git. And then the platform
team stays care of taking that application, building the containers and deploying the application, so the team gets isolated from that infrastructure management and the team only focus on their app. So we take that last one
is very, very familiar to some of you, who here is using GitOps? Okay. So you can relate to what are
the benefits of using GitOps and how I can manage the methodology we can build a platform on top of it. By using the iterative configuration,. it reduces complexity, right? When using Git, we can track changes and enhance level of visibility, right? So we can even roll back. When you have security standards that are put automatically
increase the security. So this is something that
we have seen in the field with some teams that once
the security teams know that they can use GitOps
to have their software or policies automatically
on all EKS clusters that actually start learning GitOps. And that's something that
I learned from the field. And when you want to be sure that if someone makes a mistake, makes a mistake making a change somewhere, it can automatically reconcile
that change back, right? Roll it back automatically. So in GitOps, it always
reconciles the desired state to the current state. That's if you have automatic syncing. There's different ways
of configuring GitOps. So you can have manually or automatic, it depends on your organization and the environment that
you're working with. If we're going to deploy and upgrade an EKS cluster with GitOps, let's take a look at what it
looks like, bill of materials. At high level, there are three major areas to consider when you are
configured in EKS cluster for your organization. There's many more as some of
you already working with EKS. But for this instance, we contemplate talking
about three of them. The first one is control plane. This is the thing that like
configuration of the EKS service that you can configure with the AWS API. Things like do you want encryption
on your FCD, for example? Or you want to configure
cluster access management, which is a recent feature of Amazon EKS that some of you were
maybe using the config map. Now you don't have to use the config map. You can use cluster access management and that you can configure
through, like I said, the address API of EKS. Next one is pod identity. Maybe you were using
(indistinct), things like that that configures the service
account with an annotation. Now we have a better or a new approach of doing
it with pod identity. That that configuration, you actually do it at the
address API on the EKS service that you can associate a service
account with the IAM role. And most important is upgrading
the version of Kubernetes, like going from EKS 1.30 to 1.31, upgrading the minor release. That's something that is
available at the control plane. And that's a lot of considerations to take as I mentioned a few, that you will have for that bill of materials
that at some point, you'll be configuring that cluster or many cluster at the same time at that level of configuration. And then it can be like
one unit of change. The next one is the data plane of workers. In Kubernetes, they're called worker nodes where you have, for example,
your tuple, your container ID. And now with Karpenter, we
have much better control on how we configure the EC2
instances using Kubernetes API. So when I meet Kubernetes, API, it's usually your helm
chart or YAML files. And we see a lot of organizations already have their Karpenter helm chart that they can create their
classes and more importantly, the no pools based on themes
that they can configure. And those helm charts usually
are deployed through GitOps. That's a better management
that allows the team to configure the no pools
that can match the workloads that when they deploy
the pods, for example, that request the EC2 instance. And the last one is the add-ons. And this can be add-ons
that were provide by AWS, the EKS add-ons and other type of add-ons that are systemwide software that you deploy on your Kubernetes
cluster, usually package as a helm chart that come from open source or can come from a AWS partner and vendor. So if we are going to rely on GitOps for tooling for fleet
management, we can have a process that will constantly try to
reconcile the source of truth with the actual state of the cluster. That bill of materials that we discuss, we can express as Kubernetes files and Git in different... Specialists have visibility and control over the
definition of the dependencies. So we have here like
applications, infrastructure, policy and security all configured in YAML files in this
respect for this slide, we're just going to name it
cluster YAML for simplicity of the workshop, of this presentation. So once you have your
configuration that you have as like I said, the different areas of that building materials, you're changing the control plane, you're changing something about Karpenter or you're changing something about add-on, you have that in Git. And we can have a GitHub
agent reconciling. Our Gits agent in here. This is an icon of Argo CD. This is a CNCF open source project that many customers actually
use their other GitOps tools that reconcile these resources
into the Kubernetes cluster. On this cluster, we can have
cluster Kubernetes controllers like ACK. Have ACK there. ACK stands for AWS Controls
for Kubernetes, a tool that is open source and
is fully supported by AWS. This is the EKS team providing
this open source project. So if you have any issues or you have feature requests,
you can just open a Git. In the Git repo, you can open
an issue and request that and the team will look into it. And also we have a channel
in the Kubernetes Slack. So for example, now that we have ACK, ACK could be something
that can configure we Git, that will get you an Amazon EKS cluster. So this is the first layer
that I was talking about, about the control plane. Then we have a kind of inception of like deploying Argo CD again inside the Kubernetes cluster. And that Argo CD is deployed
there to have some isolation. That way, that Argo CD can only care or handle that Kubernetes cluster. And as an agent, that it
sits down configuring that. Then the Argo CD is the one
managing that EKS cluster. So it would deploy the add-ons. For example, if you have
open source Karpenter, we deploy a Karpenter that
will give you those notes for your workloads. And if your workloads needs
access to an AWS resource, for example, an S3 bucket,
you can have ACK install inside that cluster to deploy the S3 bucket that your application needs. So this is a typical architecture
that is used by folks that are using GitOps to
configure both the control plane, Karpenter for the data
plane and then the add-ons. And this way, they can do
everything defined in Git as as YAML files
declarative configuration. So let's talk about now a little bit more about resiliency, right? So now we can build a
cluster, we can use GitOps, we can use open source
tools, we can use AWS APIs, we can use open source tools like ACK. So we have a lot of clusters, but without velocity, as you heard before, many organizations have multiple clusters for different reasons. It could be for different
regions, different teams, different AWS accounts. Without velocity, they fall behind, cannot upgrade everything serially. It will take forever to make one change if they have to upgrade
everything serially across. Some organizations have
hundreds of EKS clusters. Upgrading in batches, however, it needs safe cars in place to ensure resiliency and availability. So this is kind of like the
misconception that people think that they can set the desire configuration and suddenly, every cluster
around the world gets updated automatically at once. That's not something
that is best practice. It doesn't give you high resiliency. So consistency of components
and versions help and scale. So this is how EKS team presented last year in reinvent 2023, we have massive amount of EKS cluster, like I mentioned in the stat. Year over year is growing, the number of clusters that we manage. For example, when there's a patch released for the Cube API server. Cube API server is a component that runs on the control plane
that AWS takes care of that, that you don't have to worry about. But we have to patch it. If there's an upstream, what I mean upstream is the
upstream kubernetes project. There's a patch that needs to be rolled out across all
our e cluster around the world. That's something that
we take very seriously. But like again, we have velocity and resiliency both
together on that balance. So grouping clusters in cells
help manage the blast radius. We have the bake time between waves, we call them like one wave of a number of cells that get upgraded. And this time, that is the bake or soak time that you people refer to, decreases as the amount
of cells increases. And we have different levels
of tests that are done between every wave of
waiting for that soak. And every cell could be
about a dozen clusters. And there's a YouTube video
about this talk online. So applying this pattern to your own EKS clusters
in your AWS accounts in your organizations. We can have some type of fleet management that we can have updates be rolled out across your organization,
but in the resilient way. So how this looks like, obviously, depends on your organization. And in this example, what could be a cell? A cell could be one units of work, it could be one cluster for example. And to explain this concepts, we're going to use like
one cell is one cluster. So how many cells you can do in one wave? Well, it matters managing
the velocity and resiliency. As you progress, the
confidence tends to increase. So for example, as you roll out one of the add-ons,
like I mentioned, right? Or you're changing a Karpenter
class, a configuration that is used across all your e clusters, you have more confidence as you start patching those clusters. And then you diminish the amount of time that you wait for those. And you can pick up more
cells as you upgrade. So in this example, we have waves sandbox. That is the one cluster
that the platform team uses for testing their change. If you are doing platform engineering, usually, you call them a sandbox. And you can have waves on
one single environment. In this case, we're showing
different environments. So we have dev and then you do staging. So in staging, you do more clusters. In production, you can have
not update all clusters in production as you increase
that, but you can divide how many clusters you have
in production to update. So in this case, we have
prod one and prod two. Maybe they're divided between regions or maybe they're divided
by address accounts, it really depends on your organization. But the idea is as you
dynamically increase the number of cells on a wave, you
decrease the amount of time that you wait for that. So in practice, let's take
a concrete example of this. So we already talk about
the cluster that TAML that defines your bills of materials. If you need to change
something, for example, upgrading an EKS cluster,
you will push that into Git. Then you have a rollout. And then this rollout could be a pipeline, a custom pipeline that you write. It could be a process
that you follow manually or it could be a combination of pipelines and manual process that you use something like a ticketing system to
follow the change management. But we're using a tool like
GitHub, we can use Argo CD to orchestrate that rollout with Argo CD. So we would take wave one,
you would do your checks. So before upgrading, you
can automate the checks to see like, can I do the upgrade or not? And then, once the check pass, then you actually do the update. After the update, you will have your test. And this test could be
related to the specific change that you do or it could be a test that you always do regardless, what is the change that you did. So the change could be
at the control level, a control plane level, it could
be at the data plane level, like a change in Karpenter
configuration of Karpenter, or it could be one of the add-ons
for example the BPCC and I or any open source project
that you have as an add-on. Then we have the soak time. And the soak time is the amount of time that you're going to wait. And in here, you're
going to start monitoring of if things are happening,
like give it enough time to monitor that the system is healthy to move to the next wave. What's the next wave? Wave number two. In this case, we increase
the amount of clusters by known number of cells when we do the same exact same test again, right? We check and we test and we soak. And the amount of time
that you wait it decreases. And it continues. And then that you're
orchestrating with Argo CD. So let's take a look at
if you are using Argo CD or could use another tool, but in this case, Argos are
going to take a concrete example 'cause people like to
see concrete example. So this is using Argo CD and we're going to look at what it means to check or the precinct. So Argo CD has a system that you can configure
precinct hooks that you can, it's a Kubernetes resource
with a specific annotation and things that you can do here is gates. A checking that, for example, using Amazon EKS upgrade insights, there's an API that you can
call to see what are the things that you need to do or if
everything's green to go ahead and continue with the upgrade. If not, you will stop. The other one could be set up. Something that you need to set up before you actually do the upgrade. Could be a migration to
a database, for example, if it's for a workload. Or it could be something
to configure secrets that they need to be there, or it could be another add-on
that needs to be healthy before you continue with the
upgrade of this next add-on. And the prereqs could be CRDs. CRDs that need to be installed. So you always have the
same precinct hooks. Doesn't matter if it's a upgrade
or maybe it's a deployment. So people use the same hooks. Then it goes to the actual
deployment, which is Argo CD to do the dynamic upgrades. And then this is where Argo CD
talks to the Kubernetes APIs and you leverage that. And Niall is going to talk
more about those hooks. And but then after the hook,
we have to do our tests that we mentioned, right? So Argo CD also has a posting hook that you can do some
validation on the environment, like some functional
tests to see the health of the add-ons are correct, maybe the EKS upgrades are correct. Maybe going back to Argo insights. You can also do AC tasks
like launch a pipeline for example or something in Jenkins. Or it could be Argo workflows
if using Argo workflow, which is a CI/CD pipeline or workflow orchestrator that
you can run inside Kubernetes or just notifications
that everything went well. And with that, I'm going
to pass it to Niall to talk about the next two
stages of observe and govern. - All right, good morning, everyone. So thanks, Carlos. He's, I think, hit his CNCF
bingo card for the morning so far in the first section, but I get to talk about the
slightly less interesting stuff. But still, we're gonna
switch gears a little bit now that we've gone through Carlos's section around how we provision
and upgrade these clusters using our nice and get driven process. We'll switch gears to coral areas and we'll start with observability here. So I don't think there
exists an AWS presentation that has the word "observability" without having the slide in
it, but it's a catchy quote. So I threw in here. At the end of the day, regardless of whether we have one cluster or 100 clusters, things are gonna break. We need a strategy to
find issues, detect them, help us remediate them. And if we can't do that
as a platform team, then we can't operate a service that our developers can rely on. So both in this section
and the next section, we don't have time to
do observability 101. Instead, what we're gonna
do is focus on specifically some areas that we've seen
come up again and again with customers that they struggle with these particular areas
when they're operating clusters at maybe a larger scale. And that could even be when
you start to reach 10 clusters, these issues can start to
manifest pretty quickly. But we'll go through this one
by one and just take a look. So the first area is gonna be
roles and responsibilities. So Carlos already mentioned at
the start of the presentation that at least most of the
customers that we talk to when they start to manage
lots of EKS clusters, they tend to be
organizationally structured around a platform team
and an application team. Is that necessary? No, but it tends to be what
we're seeing in the field as an effective way to scale your use of EKS across lots of clusters. Now the platform team is typically not just a
cluster factory, right? The name suggests they
typically offer more in terms of some sort
of shared capabilities that the development teams could rely on in the observability sphere. That could be managing the observability infrastructure itself. But they can also, in some cases, maybe even pre-provision dashboards and alerts as they
onboard application teams to get them up and running quicker. By the end of the day, the
platform team is responsible for keeping those clusters up and running. They're not building the clusters and throwing them over the wall. That's a kind of the opposite
of what we're looking for. We want them to provide a
service to the development teams where the developers or customers, right? That's how we think about. That's whole idea of platform as a product and we need an observability strategy that reflects how we do that. So in order for the application
teams to trust the service and the trust is a critical part here, and we'll talk a bit
about that later as well. The platform team needs to be monitoring the signals coming from
the clusters constantly as the application teams are monitoring their workload signals. The platform team is working
hard to monitor dashboards and alerts with their
instrumentation coming back from the clusters and
providing that reliable service that the app teams are depending on. So, and many of you have probably already gone down this journey. You know, it's not unusual for us to see customers start off just by investing heavily
in dashboards, right? Dashboards are easy, they look great. You get your telemetry into your system. You install in dashboards and
you're doing observability and everything's great,
you can find your problems, but obviously, this doesn't scale very effectively pretty quickly, right? As soon as you start to
monitor a handful of clusters, you're not gonna be sitting, staring a dashboards waiting
for a bomb to happen. You need something that scales a bit more effectively than that. So pretty quickly, you
know, folks will migrate to something along the lines of relying significantly
more on proactive alerting. As a platform team, again, for that aspect
of trust, we don't want, ideally, our customers to even
notice if there's a problem. If something breaks some of our clusters, we want to know about
it and hopefully fix it before they even know that it's there. We definitely don't wanna be
relying on them telling us that it's broken because
that is just fundamentally how that trust starts to erode in the platform team and the platform. And this starts to dovetail
into a topic which we talk about all the time, which is platform adoption. If the trust erodes
between the platform team and the application teams,
then you quickly run into an issue where
they're not gonna wanna use your platform and you
need to keep that trust by having these proactive alerts and having a very proactive approach to keeping those clusters up and running regardless
of where on that spectrum that Carlos showed you land. Even if you're just
vending a cluster to them and the patterns that
we're talking about here, it's your responsibility to keep those up. So you need a solid system here. Alerts also, just having
alerts by themselves, you know, end up in a couple of
different holes here. Alert fatigue is an
old term at this point. Everyone knows it. So having the right alerts
is obviously very important, but also having an alert by itself doesn't tell you to fix the problem. And to scale your support
organization, you need to have run books tied
effectively to your alerts so that you can scale your platform team and that folks can fix
the problem at two o'clock in the morning when they get an alert and aren't scrambling through
through documentation. Also something that
input in the slide here, but as we increasingly start to see automated remediation
start to become more and more of a pattern. I know I was at CubeCon
a couple of weeks ago and I think the thing I saw the most on the vendor floor was ops remediation vendors we're now pretty
heavy in the expo. If you don't have runbooks to find, then you're not gonna be able to automate these processes eventually. So this is something which
people have been doing for a long time, but as we start to see this automation trend
increase, if you have runbook, increasingly there are tools coming up that can take those runbook and potentially apply them
automatically for you. So you've now got a new motivation to have these runbooks
actually defined ahead of time. And finally taking this. So far, we've talked about
things which probably aren't directly related to, you know, necessarily managing all our clusters, but this nice continuous delivery flow that Carlos gave us earlier, from my perspective, it's
basically a prerequisite to have this feedback loop in your process to make this work, right? This is how, as Carlos said, the EKS service team operates
is as they're rolling out through those cells and
through those waves, the proactive alerts become something that is telling them whether or not their process should
continue or not, right? They're not sitting watching
dashboards as you can imagine. So the other thing obviously,
as we go through here, Carlos talked about tests. So it's not unusual for us
to talk to platform teams who have maybe built a way to test and upgrade in their sandbox cluster. Maybe they've got a small cluster they use for functional tests. And that will uncover
uncover several issues. But as you progress through
your waves, when you start to reach staging and deployment, at the end of the day, it's no mystery. You're gonna uncover issues
that you just can't find in dev. And you can continue to
iterate on your tests and continue to find
those problems earlier on. But at the end of the day,
the soak period isn't useful unless you're monitoring something and you're alerting on things. I ideally in an automated way that will effectively sort
of act as a circuit breaker for your process, right? So this robust set of alerts
really just ends up being a mechanism we can use to cancel a rollout as it's going through if we
start to run into problems. So this sort of feeds back into that whole continuous
delivery process. This is probably the
question I get asked a lot, which I wish I had a better answer for. I wish I had a list for you
of what you should monitor and what the alert thresholds would be. If anyone has one, please send me it. But at the end of the day, a
lot of you folks are, you know, running Kubernetes already. You know how many components
you can install in a cluster, you know how many different workloads you can have running in a cluster. It can be pretty difficult
to figure out, you know, a set of things that we can
just tell you monitor this stuff and you're, you're gonna be good. Some of these things, there are some great stuff
online you can use as benchmarks, but I think instead of
trying to give you a list, really, what we wanna talk
about here is just emphasizing the breadth of what you have to monitor to effectively do this. To have trust in your process that it will short circuit your deployment if something goes wrong. This can be anything
from did the error rate on your Kubernetes control plane increase after your upgrade? Are your nodes coming up healthy? Did core DNS latency increase? Core DNS is still a problem in 2024. And if we can, can we understand if our
customers workloads are degrading if we've done an upgrade? Right? Did the error rate on developers team, or sorry, application A, B,
C in experience more latency or experience higher error rate. And if we can especially get
that sort of information, we understand not just
the health of the cluster that we're providing, but
the health of the experience that we're giving to our developers. Now, something which recently
launched, which is related to this would be that we did
in the last couple weeks launch the improved EKS cluster
control plane monitoring, where you can now get a whole bunch of extra metrics outta the control plane, which is something you
should definitely check out. We'll throw a link in some
of the related resources at the end of the session,
but that gives you a whole set of metrics that you
didn't previously have, as well as extra mechanisms
built into the console around things like
looking at your audit logs and stuff like that to identify issues. So that's been a great recent launch, which you can start to leverage. Now, not strictly observability, but we're gonna throw under this umbrella is maybe switching,
switching off a little bit, which is cluster inventory. So this is less around,
you know, finding issues and troubleshooting
issues and more around, how do I get a picture of all the clusters in my organization? Especially as it starts to scale and especially as it starts
to scale across regions, but accounts and whole
AWS organizations, right? It can be tricky to navigate
between all the console screens and sort of keep track of what's going going
on in aggregate view, there's lots of ways
that you can solve this. We see people doing it with vendor tools. We see them using Grafana
and observability tooling. One thing that we started to see is folks using developer
portals like Backstage. So I'm a big fan of Backstage if you've seen it myself before, but we have seen some customers, especially Kubernetes native customers, starting to use the ability to ingest information
about their EKS clusters into developer portals,
whether it's an open source one like Backstage or vendor products that kind of provide the equivalent. So you get that cross-account,
cross-region view of all the clusters that you have there. I think this is probably a better option than some of the other
approaches that we see, like building your own portal from scratch as a custom web app. Which a lot of people were doing with developer portals before Backstage. But this is something that I
think we're, we're starting to see some of our more
advanced Kubernetes users take advantage of, as
well as an aggregate list of all our clusters, especially
tools like Backstage, which are super flexible,
gives us the opportunity to customize and start
to aggregate information not just from EKS but
from related systems. So we could start with basic stuff, right? Maybe our account ID, our
AWS region, EKS version, the add-on versions, just
basic stuff we can pull from the API and maybe some of the places, but then we can start to
add in extra information like a cost tab where we
maybe pull the information from Cube cost or open cost. Maybe we start to provide
feedback on policy violations and findings in Backstage and
pull that to the same place. Maybe we show the SLOs for the
cluster so dev teams can see what the historical availability
of their cluster has been. Right? Again, not a monitoring tool,
but just a heads up display of how has this cluster
been performing that users or managers or somebody
else can just take a look at to get a heads up view. And then if there's information that we don't wanna rebuild
all of our other tools in developer portal site Backstage, we then start to provide
out links to all the places that we need to go, right? We're trying to get rid of
that big bookmark folder that you have where especially
if you've got 100 clusters, you're gonna have a
pretty bad time in Chrome trying to keep track of all this stuff. So we provide deep links
into all the places for a given cluster so it
becomes not just a single pane, but also a launching point
often to all the other systems that you need to actually
run your cluster. And it gives you just that
basis for being able to navigate through across your fleet. The last thing that we
find this useful for is relationships. So it's not unusual for developer portals to let you express relationships between whatever they call
items in their catalog. And in the stage case,
it would be entities. We can start to model things like what workloads
depend on a given cluster. Then the team ownership
we already have modeled typically in our Backstage. At this point, we can then start to model which clusters are dependent on each
other by understanding which workloads depend on each other. And we can start to build up this graph of metadata about our
clusters, our workloads, and our organizations that are not, we're not talking about
pods and deployments, we're talking organizationally about how these things fit
together so we can start to understand the impact or blast radius of changes potentially if we needed to figure something out. Or what would the impact be if this cluster in the
picture here went down in terms of not just the
workloads and the teams, but in terms of maybe downstream clusters where the workloads are interlinked. And we can start to do that
by building up this graph. And this can all be done
automatically, right? We don't need to do this manually. Just last week, we open sourced
a new plugin for Backstage where you can now ingest
AWS infrastructure straight into the Backstage
catalog through AWS config. And that means that there
were some existing plugins, which that you do parts of this before that were a little bit patchy in terms of a specific AWS services. Now anything that lives in config, you can pull straight into
Backstage including EKS clusters and then map them through
in terms of dependencies, using things like tags to build up this graph
completely automatically and start to get an idea
of how this fits together. So in a similar vein, Carlos talked at the
beginning about Guardrails. So talk about governments a little bit. One of the themes that
Carlos discussed earlier was consistency, right? When we start to talk to customers that have 100 EKS clusters,
you can't necessarily, well, it's harder to manage those if you don't have a
measure of consistency. So what Carlos talked
about earlier gave us that consistency at the
EKS cluster layer, right? We're getting all of our clusters up, we're getting our nodes up, we're getting our add-ons installed, but unfortunately, we've
got some pesky developers actually putting stuff in the clusters. And depending on your organization, you may or may not have control
over what that looks like, depending on the spectrum
that Carlos talked about of where you end up from vending a cluster all the way through to
a platform abstraction. That gives you more or less control there. So really, in any of those cases, governance really becomes
a key for achieving that consistency as we scale, especially as we're trying
to balance autonomy, right? Between more autonomous dev
teams that have opportunities to do more in their clusters versus maybe a more guardrailed approach where we are helping developers figure out what we should be putting in our clusters. Now again, this is not gonna be a policy as code 100 session. Instead we wanna talk
a little bit more about how we're seeing people
apply this specifically for problems at scale. But just as a quick primer,
obviously for everyone, policy as codes, engines like
OPA gatekeeper by Kyverno are exceptionally popular tools that you can get from
the open source world that will allow you to essentially express policies as codes. For example, Kyverno
typically is a YAML file, and those will often, you can enforce them in
different ways, right? So a pretty open one would
be you apply the policy and the cluster, a set of controllers are reconciling against
changes that are made. And you can flag a policy
report of everything that violates the policy
that needs to be addressed. A little bit of a harsher approach is that you can use things
like admission control to simply block app changes to the cluster that don't apply your policies correctly. Now, certain organizations
are willing to apply that and others are not, again,
on that autonomy scale, that gives us a nice way to
just stop things going in full stop that we don't wanna be there. But oftentimes, development teams will say that it slows them down. And in many cases, it can, right? So you've gotta balance
about which one of these that you're going to apply
effectively to your organization and the nature of how you're
building your platform. But specifically what do we see as some friction points
similar to observability where policies start to
come into the picture. So similar to what to alert on, we have what policies should I write? And this is potentially
even more of a blurry area because I don't know
what your policies are. There's certain natures
of policies that we have that are probably why we
consider a solid baseline, right? Those ones around say security, are you running read only file systems in your house, in your pods? Are you locking down,
adding extra capabilities and running as a root user? All those, I would say boring things that are kinda like your
foundational set of policies that you should really
be putting in place. Probably some basics around
things like are you tagging or labeling all of your pods correctly so you can do chargebacks
for cost as you scale up because you need to keep
your costs under control. Where we start to see this
specifically come into play for larger fleets of clusters. Firstly, keeping rollouts on track. So I've talked to so many customers where they're call them a Kubernetes team or a platform team, are
unable to upgrade clusters because of what developers
have deployed to them, right? As Carlos said about giving folks infrastructures code templates and them never upgrading their clusters, deprecated APIs, deprecated
CRDs, pod disruption budgets that basically get your node
rollout stuck in the mud. This is where we immediately
get into the discussion of policy as code. And you have to be able to
provide guardrails for people so that your cluster
rollout stays on track. You're not gonna be able to
go to every developer team and tell them that they
have to operate their CRDs. If you're running hundreds, 200 clusters, you're gonna spend all
of your time doing that. You have to start to
push that process left and keep them on the rails. And I know it sounds obvious, but my hope here would be that if you are in a similar position or you think you might
be in a similar position, this is a problem that a
lot of customers are having. And the solution is
unfortunately this, right? There's no magic technical
solution to this problem. A lot of it is organizational
as it probably comes across. Policies give us a way to implement an approach to solve this. But this is a recurring problem
that we see people having and you just have to plan for it. So if you are having that problem and are struggling to get
people to get on board with how to fix it, this is
really what we're seeing. The other aspect is availability. We've talked to customers where
they say they can't upgrade the clusters because in
the development clusters, their application teams have
only deployed with one replica. And when they upgrade the
cluster, the teams complain that the cluster went down
and the platform's not stable. This can even go up to
staging and production if they haven't used
pods disruption budgets. And obviously this impacts more than our upgrades
hurting your cluster. If there was other issues, you know, with the cluster itself,
it will also manifest. But if we're going with this
process of regular upgrades, we wanna keep things rolling, we're constantly changing stuff,
we want flexibility there. If these things are not in
place, again, that trust, even if it's just the perception of trust eroding in your platform, you're gonna run into issues
again with adoption teams complaining and it's not necessarily fair, but using policies has
to be one of these tools that you leverage not
just for the resiliency of keeping your apps
running, but for making sure that you can apply these updates
regularly without getting negative feedback on the
platform that you've built and the process that you've
spent all your time building that Carlos talked about earlier. In terms of managing policies. I mean, Carlos has already done all the hard work for us here, right? We've already got our ship and process that can take whatever
artifacts that we want and push them out. When you start to get up to scale, what we're really trying to do here is manage consistency,
again, across our clusters, but we have to be able to handle variation and we have to be able
to handle exceptions. So to get that consistency, one pattern that we see often is
just, it doesn't matter what cluster it is,
you have one helm chart of all your policies and
it goes everywhere, right? That's your baseline. Starting to patch work, deploying one policy to one
cluster and one to another, we'll work early on. But as you start to get
up to a larger scale, you're gonna need to just start to say, I'm throwing everything everywhere. And then start to be able to apply options within your helm chart, save
values files that allow you to enable or disable certain policies. Maybe you have different policies in your web services cluster than you have in your
data cluster, for example. So that could be one sort of
maybe bar that you use there. And then we just roll that out with our GitHub-driven process
to all of our clusters. It's just something else that we deploy. In terms of exceptions, so tools like Kyverno have exceptions as a first class process. You need to be able to handle this, right? So it could even just be as simple as you have that third party software that just won't run if it's not run as a root user or something like that. You know, we all have one. So being able to handle
exceptions is something that you need to be able to do eventually, but we want to be able to do
in a way where we can continue to have this single
artifact that we deploy out. So making sure to plan for exceptions, depending on the tooling that
you're using, is something that we wanna make sure we plan for. Now I talked about
earlier around, you know, the different ways that you can run these policies, code frameworks. The simplest being we're just
gonna assess the resources in the cluster and maybe create a report. So Kyverno, for example, will drop in something
like a cluster, you know, a policy report into your cluster when it does its assessment. At first, you can
probably just take a look into the clusters to
see what's not running. But once you start to really
scale out your EKS fleet, you're gonna need something
a little bit more aggregate in order to effectively
police these violations of your policies. So Kyverno, as an example,
has the related project of the policy reporter,
which you can install in your cluster, aggregate
all your findings into a system like S3 or
Elastic Search or Security Hub. And that gives you that single pane where you can aggregate all
those violations in one place. So we have an example
blog post for both OPA and Gatekeeper, which this
screenshot was derived from where we're shipping all
of our kernel findings straight into security hub, now we can search them, we can
search by account, by region, by cluster, maybe by workload if all the right metadata is there. And then we can rely on
whatever other features we want from security hub, say
remediation workflows and all that sort of stuff is things that we can build off
of to effectively start to actually not just
detect these violations, but have a system around remediating. So with that, we're at
the point of the talk where we're gonna start to wrap up. So really, this reflects the
three themes at the start of the talk that Carlos talked about. Applying Git GitOps
effectively is something that we're really
starting to see as a trend from these customers that are building out larger fleets of EKS clusters. GitOps, whether it's
a prerequisite or not, is really the trend that we're seeing around technology and things
like ROCD in some cases flux and also piggyback on top of GitOps with Kubernetes-driven
infrastructure provisioning, whether it's ACK cross-plane
and technology like that. Investing in proactive monitoring, right? Of being alert driven, not just so that you can detect problems, but you can, so you can feed it back into that GitOps process so that you can have
this largely hands off and you have confidence in the
system that you're building and the process that you're using to keep your customers,
sorry, your clusters updated. And finally, we wanna use
governance as our key to scaling. There are some problems
that we keep seeing over and over again as customers
try to manage EKS clusters and start to scale up their adoption. That policies are effectively the key to, and you know, planning for that and, you know, committing to that being the solution is
something that, you know, we have to talk to customers
about pretty regularly. Related sessions this week. So this has been pretty high level, right? We've been talking themes and concepts. Carlos has put together a workshop, which is being run twice this week, once tomorrow and once on Wednesday. This will also be available on GitHub and the link is in a
link which will be coming in a couple slides, but
that will actually give you hands-on experience in what
we've talked about today - In the three areas of
like you have experience of managing multi-clusters
with GitOps using Argo CD. In the workshop, we have an
example of using Terraform. A lot of folks use Terraform. So the pattern shows you
how to manage Terraform for AWS APIs and then Git
Argo CD for the GitOps. So a lot of folks have difficulties how to put those two tools together. So we have an example of that and then going into management
of observability of like, a lot of platform teams worry about the applications observability, which is just like net good, but forget about like monitoring the observability of the add-ons. Like how is the open
source Karpenter's doing? How Accordion is acting,
BCC and I subnets. That's observability that
the platform teams owns. So they have to be aware of that. And that ends with, you know, some learnings about policy management. Would you be using Kyverno? So we'll be using the Kyverno and Kyverno reporting,
configuring actually this example of the security hub. So you have hands on screens on that. So get there early if you can. - And it will be available
on, it's already available. - Yeah, and it's available. Everything is on GitHub open source. So you can start looking at
it, taking extracts of it to apply it to your own organization. - Next, there is Cube 301. So this is a talk with Adobe
and some folks from AWS on how they've built
scalable platforms with EKS. They've previously done
some talks at CubeCon, and some other stuff, CNCF-related talks around how they do this and you know, they're applying
some of the principles that Carlos talked about
around pre-flight checks and post-flight checks and
all that kinda stuff, right? So definitely a talk I
think is worth seeing because you'll see
again some of the themes around platform building but also, how Adobe is doing in practice. So definitely recommend that one. And then finally there is some chalk talks that are getting done on
playing off things like infrastructures, code, GitOps,
CI/CD, the different options that you have, pros and cons and what maybe you should be considering for your organization
that you can catch again a couple times this week, which
will also be great Sessions, Oh. (indistinct). In terms of extra
resources, so EKS workshop, hands-on labs if you
haven't already done it. We're continuing to evolve that with the new launches as they come out. We're running that a
couple of times this week, but we didn't include
on the extra sessions. But if you want to run this yourself, you can run it self-service. We can also run this as what
we call an immersion day. Talk to your account team. You can have specialists come in, help deliver this to your
teams and learn EKS hands-on. It's very modular. We can tailor it to your organization depending on what it's you wanna learn. So definitely worth taking a
look if you haven't already. Best practices guide. So many of you'll probably
already be familiar with the EKS Best Practice Guide. It's been around for a while, but recently we did take what
is this great set of knowledge for day two operations and it's now officially part
of the EKS documentation. So all the same great knowledge,
but it matches the docs and it's all in the same place now. So it could be easier to find. And finally, who doesn't love a badge? Get your badge put on
LinkedIn, that kind of stuff. I don't have mine yet, do you? - [Carlos] Huh? - Do you have your EKS badge? - Yes.
- Oh, okay. I need to catch up. (audience laughing) This is a link to a GitHub well, page. You'll find all the Kubernetes
sessions in this GitHub. There'll be a directory for
each Kubernetes session. It'll mostly be links to resources. We're not necessarily putting code here, a bunch of links to stuff
that you can look at related to each session. So that link should
take you to our folder, but that repository, you can pretty easily
find your way around it. We've added some links in
there to some of the stuff that we've talked about,
some of the extra sessions. - Yeah, the main rig me
has all the Cube track that we are part of. Like EKS group track. - Yep. - And there's other workshops if Niall mentioned Backstage. There's also some workshops that you're going to get hands
on experience with Backstage. I think is Cube 308. Cube today is if you want
to get hands on doing EKS and Backstage and there's other ones of gen AI on Backstage. - [Niall] Yes.

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=0s) - So this talk is
building production-grade

[00:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3s) resilient architectures with Amazon EKS.

[00:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=7s) In short is building Amazon
EKS cluster with resiliency.

[00:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=10s) My name is Carlos Santana.

[00:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=12s) I don't play the guitar.

[00:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=13s) I always have to make that joke.

[00:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=15s) (audience laughing)

[00:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=16s) So you can go to the House
of Blues here in Las Vegas,

[00:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=18s) and here's some Carlos Santana music.

[00:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=20s) But I'm a senior specialist
solutions architect

[00:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=23s) in containers that includes EKS and ECS.

[00:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=26s) And with me is Niall.

[00:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=30s) He's a principal specialist
solutions architect

[00:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=33s) in containers, both on EKS
and ECS, pretty much, right?

[00:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=37s) But for today, we're going to
be talking about Kubernetes

[00:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=41s) running on AWS using EKS.

[00:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=44s) So the agenda for today,

[00:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=46s) we had a lot of topics to choose from.

[00:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=48s) We one hour of a session,

[00:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=51s) we had to choose some
aspects that come together

[00:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=54s) in a story around platform
engineering on top of EKS

[00:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=57s) so we choose to talk about management,

[01:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=60s) observability, and governance.

[01:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=65s) So that's what pretty much
what we're going to talk today.

[01:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=68s) Talking about platforms.

[01:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=70s) Everybody starts building

[01:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=71s) their platforms and builders, right?

[01:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=73s) These are the folks that are in charge

[01:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=75s) of the cloud resources
in the organization.

[01:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=77s) And what builds a platform
is building for teams.

[01:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=81s) They're organized by teams.

[01:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=82s) And then you have your applications

[01:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=84s) that you run to run on AWS

[01:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=86s) and then you have your infrastructure.

[01:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=88s) So pretty much, it boils
down to three aspects.

[01:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=90s) You have teams, you have applications

[01:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=92s) that you have to put those
applications somewhere

[01:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=95s) in the infrastructure.

[01:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=97s) Talking about platforms, the idea

[01:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=100s) is that these platform
engineers build abstractions

[01:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=102s) and they accelerate how they
build these applications on AWS

[01:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=107s) providing cloud infrastructure
as easy as possible

[01:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=110s) with autonomy to those teams.

[01:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=114s) This is a stat that by
July, last July of 2024,

[01:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=119s) there's more clusters being managed by AWS

[02:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=123s) in this terms of EKS.

[02:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=125s) 33% growth year over year.

[02:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=127s) So the amount of clusters
that folks are configuring,

[02:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=131s) deploying, and managing and upgrading,

[02:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=133s) it's increasing year by year.

[02:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=135s) So there's a stat that's in there.

[02:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=138s) And what are the challenges

[02:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=139s) that platform teams have when they come

[02:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=141s) into managing this cluster.

[02:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=144s) So today, we're going to
look into three areas.

[02:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=147s) One is this life cycle of
the cluster from deployment

[02:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=151s) to upgrade on how to develop a
consistent ecosystem process.

[02:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=155s) The next one is enforcing best
practices across all clusters

[02:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=158s) by not monitoring them
and also the applications.

[02:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=161s) But for today, we're going to concentrate

[02:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=163s) more of the clusters

[02:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=165s) and the system wise software
that runs on those clusters.

[02:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=168s) And last, providing guardrails
to support the teams

[02:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=171s) that need these clusters

[02:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=173s) and giving them the right
amount of autonomy, right?

[02:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=176s) They need a cluster, they're developers,

[02:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=178s) but they need guardrails.

[03:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=183s) So let's start with the
first topic of management.

[03:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=187s) And this is how it looks like.

[03:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=189s) We generally see customers
with a repo Git resource.

[03:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=193s) Some kind of infrastructure
as code tooling,

[03:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=195s) like Terraform, CloudFormation.

[03:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=197s) I heard somebody here in the
audience talking about CDK.

[03:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=200s) Pulumi and others infrastructure as code

[03:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=203s) that the state lives in
a object store like S3.

[03:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=207s) And then they will deploy a cluster.

[03:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=211s) Then they will use the same
infrastructure as code tooling

[03:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=215s) to deploy Kubernetes resources,

[03:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=216s) saving the state of these
Kubernetes resources

[03:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=221s) in the same location at,
for example, the S3 bucket.

[03:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=224s) For Kubernetes resources,
this might be pragmatic,

[03:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=226s) but for simple cluster
management, not a problem at all.

[03:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=232s) And then, things starts growing.

[03:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=235s) Then you as a platform engineer,
you start getting requests

[03:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=238s) as that teams need another EKS cluster.

[04:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=243s) So you copy paste, right?

[04:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=244s) That pipeline move it on,
and you get a second cluster

[04:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=248s) and create a new pipeline.

[04:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=252s) Then it gets to this level.

[04:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=253s) So raise your hand if
you have an organization

[04:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=256s) that it looks like this.

[04:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=257s) Having a lot of pipelines,
deploying a lot of EKS clusters.

[04:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=261s) It grows, the growth continues.

[04:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=263s) This becomes unmanageable.

[04:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=265s) Too many versions of the pipeline

[04:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=267s) because you're copy pasting

[04:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=269s) to track which clusters is up-to-date.

[04:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=272s) These without thinking what is inside

[04:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=275s) of each cluster, right?

[04:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=276s) The resources and application.

[04:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=278s) It's not uncommon to see many
pipelines in our organization.

[04:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=282s) So this is a lot of snowflakes, right?

[04:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=284s) Each one individually, you can say

[04:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=287s) that it's an cluster, but you look closer,

[04:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=290s) they have a different version.

[04:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=291s) So what are the application
they have inside?

[04:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=293s) And each one has an old version

[04:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=295s) of a variation of a pipeline.

[05:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=301s) So what are the key challenges

[05:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=302s) to restate in terms of management?

[05:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=304s) When you have unmanaged
growth of clusters,

[05:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=307s) what are the some key challenges?

[05:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=308s) Enforcing standards across
your fleet of clusters.

[05:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=312s) So now we're talking
about fleet of clusters

[05:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=314s) becomes hard to automate
those deployments.

[05:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=319s) When you have automation,

[05:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=320s) how do you configure a
single source of truth

[05:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=323s) for all of them?

[05:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=324s) Out of management becomes
something that gets out of control

[05:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=327s) with so much open source projects.

[05:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=329s) The team cannot be an expert
on every add-on out there

[05:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=332s) that you put in your clusters.

[05:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=334s) And lastly, workload management.

[05:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=336s) How to match the best
instance type, in case of EC2

[05:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=340s) to a workload?

[05:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=341s) And also do cost
optimization on top of it.

[05:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=349s) So this is something that
we see from the field.

[05:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=351s) Me and Niall, we work on
the field with customers,

[05:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=354s) probably some of you.

[05:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=355s) And we work with customers
that are trying to configure

[05:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=358s) and deploy EKS clusters and
building kind of like a pattern

[06:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=362s) or how do we serve these teams
that are in the organization.

[06:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=367s) So we see a lot of ways of clusters

[06:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=369s) that are provisioning organizations.

[06:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=371s) Templates as a service,
this is in the website.

[06:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=374s) It's used by many platform teams initially

[06:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=377s) since it's a low barrier to entry,

[06:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=378s) like the platform team will
be, I create a template,

[06:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=382s) give it to the dev team,

[06:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=384s) and then they will create a cluster.

[06:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=386s) But this becomes hard to manage a scale.

[06:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=388s) Development teams guess what?

[06:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=390s) Not to upgrade their clusters.

[06:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=394s) If you are in the platform
team dealing with EKS clusters,

[06:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=396s) you know that you need
upgrade them, patch them,

[06:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=398s) and release new updates.

[06:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=400s) It just give them that
template to the dev team.

[06:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=402s) They will just run it once

[06:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=404s) and then never go back to
upgrade those clusters.

[06:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=408s) Platform teams taking more
ownership, providing a service.

[06:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=411s) So let's take a look at what we advertise.

[06:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=414s) So the first one is customers
cluster as a service,

[06:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=419s) giving a cluster to a team,

[07:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=421s) but the platform team
managing the cluster itself,

[07:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=424s) making sure that they're the
ones upgrading the cluster,

[07:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=427s) upgrading the add-ons.

[07:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=428s) Another one is namespace as a service.

[07:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=430s) So namespace as a service is something

[07:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=432s) that the team would have a discussion

[07:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=435s) or maybe a form that asks the team, like,

[07:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=437s) how many resources do you
need in that namespace?

[07:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=439s) So the platform teams
can set resource quotas

[07:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=442s) and Kubernetes that are
APIs that you can configure

[07:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=447s) or maybe limit ranges or
default for request and limits.

[07:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=451s) And that way, you get a namespace

[07:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=453s) created by this platform team.

[07:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=455s) And then the team can
deploy inside of them.

[07:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=458s) And the last one is maybe the
team, the only team that needs

[07:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=462s) to provide to the platform team

[07:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=463s) is give me an application,
I'll give you a ripple.

[07:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=466s) And they don't know that their application

[07:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=468s) is running on Kubernetes.

[07:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=469s) They only care about what
getting their application on Git.

[07:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=473s) And then the platform
team stays care of taking

[07:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=475s) that application, building the containers

[07:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=477s) and deploying the application,

[07:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=478s) so the team gets isolated

[08:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=480s) from that infrastructure management

[08:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=482s) and the team only focus on their app.

[08:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=487s) So we take that last one
is very, very familiar

[08:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=491s) to some of you, who here is using GitOps?

[08:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=496s) Okay.

[08:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=496s) So you can relate to what are
the benefits of using GitOps

[08:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=500s) and how I can manage the methodology

[08:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=501s) we can build a platform on top of it.

[08:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=504s) By using the iterative configuration,.

[08:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=506s) it reduces complexity, right?

[08:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=508s) When using Git, we can track changes

[08:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=511s) and enhance level of visibility, right?

[08:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=513s) So we can even roll back.

[08:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=516s) When you have security standards

[08:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=518s) that are put automatically
increase the security.

[08:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=520s) So this is something that
we have seen in the field

[08:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=524s) with some teams that once
the security teams know

[08:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=528s) that they can use GitOps
to have their software

[08:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=533s) or policies automatically
on all EKS clusters

[08:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=537s) that actually start learning GitOps.

[08:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=538s) And that's something that
I learned from the field.

[09:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=541s) And when you want to be sure

[09:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=543s) that if someone makes a mistake,

[09:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=545s) makes a mistake making a change somewhere,

[09:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=548s) it can automatically reconcile
that change back, right?

[09:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=551s) Roll it back automatically.

[09:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=553s) So in GitOps, it always
reconciles the desired state

[09:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=556s) to the current state.

[09:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=558s) That's if you have automatic syncing.

[09:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=562s) There's different ways
of configuring GitOps.

[09:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=564s) So you can have manually or automatic,

[09:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=565s) it depends on your organization

[09:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=567s) and the environment that
you're working with.

[09:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=572s) If we're going to deploy

[09:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=573s) and upgrade an EKS cluster with GitOps,

[09:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=576s) let's take a look at what it
looks like, bill of materials.

[09:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=581s) At high level, there are three major areas

[09:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=585s) to consider when you are
configured in EKS cluster

[09:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=587s) for your organization.

[09:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=589s) There's many more as some of
you already working with EKS.

[09:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=594s) But for this instance,

[09:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=595s) we contemplate talking
about three of them.

[09:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=598s) The first one is control plane.

[10:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=601s) This is the thing that like
configuration of the EKS service

[10:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=606s) that you can configure with the AWS API.

[10:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=608s) Things like do you want encryption
on your FCD, for example?

[10:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=612s) Or you want to configure
cluster access management,

[10:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=615s) which is a recent feature of Amazon EKS

[10:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=620s) that some of you were
maybe using the config map.

[10:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=622s) Now you don't have to use the config map.

[10:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=624s) You can use cluster access management

[10:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=625s) and that you can configure
through, like I said,

[10:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=628s) the address API of EKS.

[10:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=631s) Next one is pod identity.

[10:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=633s) Maybe you were using
(indistinct), things like that

[10:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=636s) that configures the service
account with an annotation.

[10:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=639s) Now we have a better

[10:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=641s) or a new approach of doing
it with pod identity.

[10:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=644s) That that configuration,

[10:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=645s) you actually do it at the
address API on the EKS service

[10:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=649s) that you can associate a service
account with the IAM role.

[10:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=655s) And most important is upgrading
the version of Kubernetes,

[10:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=658s) like going from EKS 1.30 to 1.31,

[11:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=663s) upgrading the minor release.

[11:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=665s) That's something that is
available at the control plane.

[11:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=668s) And that's a lot of considerations to take

[11:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=670s) as I mentioned a few, that you will have

[11:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=672s) for that bill of materials
that at some point,

[11:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=674s) you'll be configuring that cluster

[11:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=676s) or many cluster at the same time

[11:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=678s) at that level of configuration.

[11:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=679s) And then it can be like
one unit of change.

[11:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=683s) The next one is the data plane of workers.

[11:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=688s) In Kubernetes, they're called worker nodes

[11:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=690s) where you have, for example,
your tuple, your container ID.

[11:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=694s) And now with Karpenter, we
have much better control

[11:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=697s) on how we configure the EC2
instances using Kubernetes API.

[11:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=702s) So when I meet Kubernetes, API,

[11:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=704s) it's usually your helm
chart or YAML files.

[11:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=707s) And we see a lot of organizations

[11:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=709s) already have their Karpenter helm chart

[11:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=712s) that they can create their
classes and more importantly,

[11:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=717s) the no pools based on themes
that they can configure.

[12:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=720s) And those helm charts usually
are deployed through GitOps.

[12:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=723s) That's a better management
that allows the team

[12:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=726s) to configure the no pools
that can match the workloads

[12:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=728s) that when they deploy
the pods, for example,

[12:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=730s) that request the EC2 instance.

[12:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=733s) And the last one is the add-ons.

[12:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=736s) And this can be add-ons
that were provide by AWS,

[12:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=738s) the EKS add-ons and other type of add-ons

[12:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=741s) that are systemwide software

[12:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=742s) that you deploy on your Kubernetes
cluster, usually package

[12:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=745s) as a helm chart that come from open source

[12:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=748s) or can come from a AWS partner and vendor.

[12:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=755s) So if we are going to rely on GitOps

[12:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=757s) for tooling for fleet
management, we can have a process

[12:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=761s) that will constantly try to
reconcile the source of truth

[12:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=764s) with the actual state of the cluster.

[12:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=768s) That bill of materials that we discuss,

[12:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=771s) we can express as Kubernetes files

[12:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=775s) and Git in different...

[12:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=778s) Specialists have visibility

[12:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=779s) and control over the
definition of the dependencies.

[13:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=783s) So we have here like
applications, infrastructure,

[13:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=787s) policy and security all configured

[13:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=789s) in YAML files in this
respect for this slide,

[13:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=793s) we're just going to name it
cluster YAML for simplicity

[13:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=797s) of the workshop, of this presentation.

[13:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=802s) So once you have your
configuration that you have

[13:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=806s) as like I said, the different areas

[13:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=808s) of that building materials,

[13:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=809s) you're changing the control plane,

[13:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=810s) you're changing something about Karpenter

[13:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=812s) or you're changing something about add-on,

[13:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=814s) you have that in Git.

[13:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=815s) And we can have a GitHub
agent reconciling.

[13:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=819s) Our Gits agent in here.

[13:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=821s) This is an icon of Argo CD.

[13:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=823s) This is a CNCF open source project

[13:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=826s) that many customers actually
use their other GitOps tools

[13:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=831s) that reconcile these resources
into the Kubernetes cluster.

[13:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=835s) On this cluster, we can have
cluster Kubernetes controllers

[14:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=840s) like ACK.

[14:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=842s) Have ACK there.

[14:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=843s) ACK stands for AWS Controls
for Kubernetes, a tool

[14:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=847s) that is open source and
is fully supported by AWS.

[14:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=850s) This is the EKS team providing
this open source project.

[14:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=854s) So if you have any issues

[14:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=856s) or you have feature requests,
you can just open a Git.

[14:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=859s) In the Git repo, you can open
an issue and request that

[14:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=862s) and the team will look into it.

[14:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=863s) And also we have a channel
in the Kubernetes Slack.

[14:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=868s) So for example, now that we have ACK,

[14:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=871s) ACK could be something
that can configure we Git,

[14:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=873s) that will get you an Amazon EKS cluster.

[14:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=876s) So this is the first layer
that I was talking about,

[14:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=878s) about the control plane.

[14:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=881s) Then we have a kind of inception

[14:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=883s) of like deploying Argo CD again

[14:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=886s) inside the Kubernetes cluster.

[14:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=888s) And that Argo CD is deployed
there to have some isolation.

[14:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=893s) That way, that Argo CD can only care

[14:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=895s) or handle that Kubernetes cluster.

[14:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=899s) And as an agent, that it
sits down configuring that.

[15:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=904s) Then the Argo CD is the one
managing that EKS cluster.

[15:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=907s) So it would deploy the add-ons.

[15:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=909s) For example, if you have
open source Karpenter,

[15:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=912s) we deploy a Karpenter that
will give you those notes

[15:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=915s) for your workloads.

[15:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=917s) And if your workloads needs
access to an AWS resource,

[15:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=921s) for example, an S3 bucket,
you can have ACK install

[15:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=925s) inside that cluster to deploy

[15:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=928s) the S3 bucket that your application needs.

[15:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=930s) So this is a typical architecture
that is used by folks

[15:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=935s) that are using GitOps to
configure both the control plane,

[15:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=939s) Karpenter for the data
plane and then the add-ons.

[15:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=943s) And this way, they can do
everything defined in Git

[15:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=948s) as as YAML files
declarative configuration.

[15:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=954s) So let's talk about now a little bit more

[15:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=957s) about resiliency, right?

[15:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=958s) So now we can build a
cluster, we can use GitOps,

[16:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=961s) we can use open source
tools, we can use AWS APIs,

[16:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=965s) we can use open source tools like ACK.

[16:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=968s) So we have a lot of clusters,

[16:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=969s) but without velocity, as you heard before,

[16:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=974s) many organizations have multiple clusters

[16:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=976s) for different reasons.

[16:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=977s) It could be for different
regions, different teams,

[16:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=981s) different AWS accounts.

[16:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=983s) Without velocity, they fall behind,

[16:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=984s) cannot upgrade everything serially.

[16:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=987s) It will take forever to make one change

[16:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=990s) if they have to upgrade
everything serially across.

[16:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=993s) Some organizations have
hundreds of EKS clusters.

[16:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=996s) Upgrading in batches,

[16:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=998s) however, it needs safe cars in place

[16:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1001s) to ensure resiliency and availability.

[16:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1003s) So this is kind of like the
misconception that people think

[16:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1005s) that they can set the desire configuration

[16:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1008s) and suddenly, every cluster
around the world gets updated

[16:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1013s) automatically at once.

[16:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1014s) That's not something
that is best practice.

[16:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1017s) It doesn't give you high resiliency.

[17:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1020s) So consistency of components
and versions help and scale.

[17:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1026s) So this is how EKS team

[17:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1028s) presented last year in reinvent 2023,

[17:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1031s) we have massive amount of EKS cluster,

[17:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1033s) like I mentioned in the stat.

[17:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1035s) Year over year is growing,

[17:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1036s) the number of clusters that we manage.

[17:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1038s) For example, when there's a patch released

[17:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1041s) for the Cube API server.

[17:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1043s) Cube API server is a component

[17:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1044s) that runs on the control plane
that AWS takes care of that,

[17:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1047s) that you don't have to worry about.

[17:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1049s) But we have to patch it.

[17:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1050s) If there's an upstream,

[17:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1051s) what I mean upstream is the
upstream kubernetes project.

[17:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1055s) There's a patch that needs

[17:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1057s) to be rolled out across all
our e cluster around the world.

[17:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1061s) That's something that
we take very seriously.

[17:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1063s) But like again, we have velocity

[17:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1065s) and resiliency both
together on that balance.

[17:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1070s) So grouping clusters in cells
help manage the blast radius.

[17:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1074s) We have the bake time between waves,

[17:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1077s) we call them like one wave of a number

[18:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1080s) of cells that get upgraded.

[18:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1081s) And this time, that is the bake

[18:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1083s) or soak time that you people refer to,

[18:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1087s) decreases as the amount
of cells increases.

[18:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1091s) And we have different levels
of tests that are done

[18:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1096s) between every wave of
waiting for that soak.

[18:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1100s) And every cell could be
about a dozen clusters.

[18:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1103s) And there's a YouTube video
about this talk online.

[18:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1111s) So applying this pattern

[18:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1113s) to your own EKS clusters
in your AWS accounts

[18:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1117s) in your organizations.

[18:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1119s) We can have some type of fleet management

[18:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1121s) that we can have updates be rolled out

[18:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1124s) across your organization,
but in the resilient way.

[18:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1128s) So how this looks like,

[18:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1129s) obviously, depends on your organization.

[18:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1131s) And in this example, what could be a cell?

[18:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1135s) A cell could be one units of work,

[18:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1138s) it could be one cluster for example.

[19:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1141s) And to explain this concepts,

[19:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1143s) we're going to use like
one cell is one cluster.

[19:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1147s) So how many cells you can do in one wave?

[19:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1150s) Well, it matters managing
the velocity and resiliency.

[19:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1155s) As you progress, the
confidence tends to increase.

[19:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1160s) So for example, as you roll out

[19:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1163s) one of the add-ons,
like I mentioned, right?

[19:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1165s) Or you're changing a Karpenter
class, a configuration

[19:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1169s) that is used across all your e clusters,

[19:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1173s) you have more confidence

[19:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1174s) as you start patching those clusters.

[19:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1177s) And then you diminish the amount of time

[19:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1179s) that you wait for those.

[19:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1180s) And you can pick up more
cells as you upgrade.

[19:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1183s) So in this example, we have waves sandbox.

[19:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1187s) That is the one cluster
that the platform team uses

[19:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1190s) for testing their change.

[19:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1192s) If you are doing platform engineering,

[19:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1194s) usually, you call them a sandbox.

[19:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1196s) And you can have waves on
one single environment.

[19:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1199s) In this case, we're showing
different environments.

[20:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1201s) So we have dev and then you do staging.

[20:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1203s) So in staging, you do more clusters.

[20:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1206s) In production, you can have
not update all clusters

[20:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1210s) in production as you increase
that, but you can divide

[20:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1213s) how many clusters you have
in production to update.

[20:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1216s) So in this case, we have
prod one and prod two.

[20:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1219s) Maybe they're divided between regions

[20:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1223s) or maybe they're divided
by address accounts,

[20:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1225s) it really depends on your organization.

[20:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1228s) But the idea is as you
dynamically increase the number

[20:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1231s) of cells on a wave, you
decrease the amount of time

[20:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1234s) that you wait for that.

[20:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1236s) So in practice, let's take
a concrete example of this.

[20:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1241s) So we already talk about
the cluster that TAML

[20:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1243s) that defines your bills of materials.

[20:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1246s) If you need to change
something, for example,

[20:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1248s) upgrading an EKS cluster,
you will push that into Git.

[20:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1252s) Then you have a rollout.

[20:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1254s) And then this rollout could be a pipeline,

[20:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1257s) a custom pipeline that you write.

[20:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1259s) It could be a process
that you follow manually

[21:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1261s) or it could be a combination of pipelines

[21:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1264s) and manual process that you use something

[21:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1267s) like a ticketing system to
follow the change management.

[21:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1270s) But we're using a tool like
GitHub, we can use Argo CD

[21:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1274s) to orchestrate that rollout with Argo CD.

[21:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1279s) So we would take wave one,
you would do your checks.

[21:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1282s) So before upgrading, you
can automate the checks

[21:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1287s) to see like, can I do the upgrade or not?

[21:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1291s) And then, once the check pass,

[21:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1293s) then you actually do the update.

[21:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1296s) After the update, you will have your test.

[21:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1298s) And this test could be
related to the specific change

[21:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1302s) that you do or it could be a test

[21:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1304s) that you always do regardless,

[21:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1306s) what is the change that you did.

[21:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1308s) So the change could be
at the control level,

[21:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1311s) a control plane level, it could
be at the data plane level,

[21:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1313s) like a change in Karpenter
configuration of Karpenter,

[21:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1316s) or it could be one of the add-ons
for example the BPCC and I

[21:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1319s) or any open source project
that you have as an add-on.

[22:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1324s) Then we have the soak time.

[22:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1326s) And the soak time is the amount of time

[22:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1328s) that you're going to wait.

[22:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1330s) And in here, you're
going to start monitoring

[22:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1332s) of if things are happening,
like give it enough time

[22:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1337s) to monitor that the system is healthy

[22:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1340s) to move to the next wave.

[22:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1341s) What's the next wave?

[22:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1342s) Wave number two.

[22:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1343s) In this case, we increase
the amount of clusters

[22:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1347s) by known number of cells when we do

[22:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1349s) the same exact same test again, right?

[22:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1351s) We check and we test and we soak.

[22:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1353s) And the amount of time
that you wait it decreases.

[22:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1357s) And it continues.

[22:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1358s) And then that you're
orchestrating with Argo CD.

[22:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1362s) So let's take a look at
if you are using Argo CD

[22:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1365s) or could use another tool,

[22:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1366s) but in this case, Argos are
going to take a concrete example

[22:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1369s) 'cause people like to
see concrete example.

[22:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1371s) So this is using Argo CD

[22:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1373s) and we're going to look at what it means

[22:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1375s) to check or the precinct.

[22:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1376s) So Argo CD has a system

[22:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1378s) that you can configure
precinct hooks that you can,

[23:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1382s) it's a Kubernetes resource
with a specific annotation

[23:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1385s) and things that you can do here is gates.

[23:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1388s) A checking that, for example,

[23:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1390s) using Amazon EKS upgrade insights,

[23:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1393s) there's an API that you can
call to see what are the things

[23:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1396s) that you need to do or if
everything's green to go ahead

[23:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1399s) and continue with the upgrade.

[23:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1401s) If not, you will stop.

[23:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1402s) The other one could be set up.

[23:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1404s) Something that you need to set up

[23:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1405s) before you actually do the upgrade.

[23:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1407s) Could be a migration to
a database, for example,

[23:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1410s) if it's for a workload.

[23:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1411s) Or it could be something
to configure secrets

[23:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1415s) that they need to be there,

[23:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1416s) or it could be another add-on
that needs to be healthy

[23:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1419s) before you continue with the
upgrade of this next add-on.

[23:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1422s) And the prereqs could be CRDs.

[23:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1425s) CRDs that need to be installed.

[23:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1426s) So you always have the
same precinct hooks.

[23:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1429s) Doesn't matter if it's a upgrade
or maybe it's a deployment.

[23:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1432s) So people use the same hooks.

[23:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1435s) Then it goes to the actual
deployment, which is Argo CD

[23:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1438s) to do the dynamic upgrades.

[24:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1440s) And then this is where Argo CD
talks to the Kubernetes APIs

[24:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1443s) and you leverage that.

[24:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1445s) And Niall is going to talk
more about those hooks.

[24:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1448s) And but then after the hook,
we have to do our tests

[24:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1452s) that we mentioned, right?

[24:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1453s) So Argo CD also has a posting hook

[24:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1456s) that you can do some
validation on the environment,

[24:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1458s) like some functional
tests to see the health

[24:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1461s) of the add-ons are correct,

[24:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1463s) maybe the EKS upgrades are correct.

[24:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1464s) Maybe going back to Argo insights.

[24:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1467s) You can also do AC tasks
like launch a pipeline

[24:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1470s) for example or something in Jenkins.

[24:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1472s) Or it could be Argo workflows
if using Argo workflow,

[24:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1474s) which is a CI/CD pipeline

[24:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1476s) or workflow orchestrator that
you can run inside Kubernetes

[24:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1479s) or just notifications
that everything went well.

[24:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1483s) And with that, I'm going
to pass it to Niall

[24:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1485s) to talk about the next two
stages of observe and govern.

[24:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1491s) - All right, good morning, everyone.

[24:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1493s) So thanks, Carlos.

[24:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1495s) He's, I think, hit his CNCF
bingo card for the morning

[24:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1498s) so far in the first section,

[24:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1499s) but I get to talk about the
slightly less interesting stuff.

[25:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1502s) But still, we're gonna
switch gears a little bit now

[25:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1506s) that we've gone through Carlos's section

[25:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1507s) around how we provision
and upgrade these clusters

[25:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1510s) using our nice and get driven process.

[25:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1512s) We'll switch gears to coral areas

[25:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1514s) and we'll start with observability here.

[25:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1515s) So I don't think there
exists an AWS presentation

[25:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1520s) that has the word "observability"

[25:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1522s) without having the slide in
it, but it's a catchy quote.

[25:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1524s) So I threw in here.

[25:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1526s) At the end of the day,

[25:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1527s) regardless of whether we have one cluster

[25:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1528s) or 100 clusters, things are gonna break.

[25:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1531s) We need a strategy to
find issues, detect them,

[25:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1535s) help us remediate them.

[25:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1536s) And if we can't do that
as a platform team,

[25:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1537s) then we can't operate a service

[25:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1539s) that our developers can rely on.

[25:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1542s) So both in this section
and the next section,

[25:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1546s) we don't have time to
do observability 101.

[25:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1549s) Instead, what we're gonna
do is focus on specifically

[25:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1551s) some areas that we've seen
come up again and again

[25:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1554s) with customers that they struggle

[25:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1557s) with these particular areas
when they're operating clusters

[26:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1560s) at maybe a larger scale.

[26:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1562s) And that could even be when
you start to reach 10 clusters,

[26:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1564s) these issues can start to
manifest pretty quickly.

[26:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1567s) But we'll go through this one
by one and just take a look.

[26:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1570s) So the first area is gonna be
roles and responsibilities.

[26:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1573s) So Carlos already mentioned at
the start of the presentation

[26:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1576s) that at least most of the
customers that we talk to

[26:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1579s) when they start to manage
lots of EKS clusters,

[26:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1582s) they tend to be
organizationally structured

[26:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1584s) around a platform team
and an application team.

[26:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1587s) Is that necessary?

[26:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1588s) No, but it tends to be what
we're seeing in the field

[26:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1591s) as an effective way to scale your use

[26:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1593s) of EKS across lots of clusters.

[26:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1596s) Now the platform team

[26:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1599s) is typically not just a
cluster factory, right?

[26:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1602s) The name suggests they
typically offer more

[26:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1605s) in terms of some sort
of shared capabilities

[26:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1607s) that the development teams could rely on

[26:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1610s) in the observability sphere.

[26:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1611s) That could be managing

[26:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1613s) the observability infrastructure itself.

[26:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1615s) But they can also, in some cases,

[26:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1616s) maybe even pre-provision dashboards

[26:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1618s) and alerts as they
onboard application teams

[27:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1620s) to get them up and running quicker.

[27:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1623s) By the end of the day, the
platform team is responsible

[27:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1625s) for keeping those clusters up and running.

[27:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1627s) They're not building the clusters

[27:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1629s) and throwing them over the wall.

[27:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1630s) That's a kind of the opposite
of what we're looking for.

[27:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1632s) We want them to provide a
service to the development teams

[27:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1635s) where the developers or customers, right?

[27:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1638s) That's how we think about.

[27:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1639s) That's whole idea of platform as a product

[27:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1641s) and we need an observability strategy

[27:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1643s) that reflects how we do that.

[27:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1644s) So in order for the application
teams to trust the service

[27:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1649s) and the trust is a critical part here,

[27:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1650s) and we'll talk a bit
about that later as well.

[27:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1654s) The platform team needs to be monitoring

[27:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1656s) the signals coming from
the clusters constantly

[27:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1658s) as the application teams

[27:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1660s) are monitoring their workload signals.

[27:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1662s) The platform team is working
hard to monitor dashboards

[27:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1666s) and alerts with their
instrumentation coming back

[27:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1667s) from the clusters and
providing that reliable service

[27:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1670s) that the app teams are depending on.

[27:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1674s) So, and many of you have probably

[27:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1676s) already gone down this journey.

[27:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1678s) You know, it's not unusual for us

[28:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1680s) to see customers start off

[28:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1681s) just by investing heavily
in dashboards, right?

[28:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1683s) Dashboards are easy, they look great.

[28:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1686s) You get your telemetry into your system.

[28:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1689s) You install in dashboards and
you're doing observability

[28:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1691s) and everything's great,
you can find your problems,

[28:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1693s) but obviously, this doesn't scale

[28:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1695s) very effectively pretty quickly, right?

[28:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1698s) As soon as you start to
monitor a handful of clusters,

[28:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1701s) you're not gonna be sitting,

[28:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1703s) staring a dashboards waiting
for a bomb to happen.

[28:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1704s) You need something that scales

[28:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1705s) a bit more effectively than that.

[28:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1706s) So pretty quickly, you
know, folks will migrate

[28:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1710s) to something along the lines

[28:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1711s) of relying significantly
more on proactive alerting.

[28:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1714s) As a platform team,

[28:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1715s) again, for that aspect
of trust, we don't want,

[28:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1720s) ideally, our customers to even
notice if there's a problem.

[28:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1722s) If something breaks some of our clusters,

[28:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1723s) we want to know about
it and hopefully fix it

[28:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1725s) before they even know that it's there.

[28:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1727s) We definitely don't wanna be
relying on them telling us

[28:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1729s) that it's broken because
that is just fundamentally

[28:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1732s) how that trust starts to erode

[28:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1734s) in the platform team and the platform.

[28:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1735s) And this starts to dovetail
into a topic which we talk about

[28:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1738s) all the time, which is platform adoption.

[29:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1740s) If the trust erodes
between the platform team

[29:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1743s) and the application teams,
then you quickly run

[29:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1744s) into an issue where
they're not gonna wanna use

[29:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1747s) your platform and you
need to keep that trust

[29:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1748s) by having these proactive alerts

[29:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1750s) and having a very proactive approach

[29:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1752s) to keeping those clusters

[29:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1753s) up and running regardless
of where on that spectrum

[29:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1755s) that Carlos showed you land.

[29:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1756s) Even if you're just
vending a cluster to them

[29:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1758s) and the patterns that
we're talking about here,

[29:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1760s) it's your responsibility to keep those up.

[29:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1762s) So you need a solid system here.

[29:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1765s) Alerts also, just having
alerts by themselves, you know,

[29:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1770s) end up in a couple of
different holes here.

[29:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1772s) Alert fatigue is an
old term at this point.

[29:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1774s) Everyone knows it.

[29:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1776s) So having the right alerts
is obviously very important,

[29:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1780s) but also having an alert by itself

[29:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1782s) doesn't tell you to fix the problem.

[29:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1783s) And to scale your support
organization, you need

[29:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1786s) to have run books tied
effectively to your alerts

[29:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1788s) so that you can scale your platform team

[29:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1790s) and that folks can fix
the problem at two o'clock

[29:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1792s) in the morning when they get an alert

[29:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1793s) and aren't scrambling through
through documentation.

[29:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1796s) Also something that
input in the slide here,

[29:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1798s) but as we increasingly start

[29:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1799s) to see automated remediation
start to become more

[30:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1802s) and more of a pattern.

[30:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1804s) I know I was at CubeCon
a couple of weeks ago

[30:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1806s) and I think the thing I saw the most

[30:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1808s) on the vendor floor was ops remediation

[30:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1812s) vendors we're now pretty
heavy in the expo.

[30:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1815s) If you don't have runbooks to find,

[30:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1816s) then you're not gonna be able

[30:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1817s) to automate these processes eventually.

[30:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1819s) So this is something which
people have been doing

[30:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1821s) for a long time, but as we start

[30:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1822s) to see this automation trend
increase, if you have runbook,

[30:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1825s) increasingly there are tools coming up

[30:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1827s) that can take those runbook

[30:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1829s) and potentially apply them
automatically for you.

[30:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1830s) So you've now got a new motivation

[30:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1832s) to have these runbooks
actually defined ahead of time.

[30:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1837s) And finally taking this.

[30:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1838s) So far, we've talked about
things which probably

[30:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1840s) aren't directly related to, you know,

[30:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1841s) necessarily managing all our clusters,

[30:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1843s) but this nice continuous delivery flow

[30:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1847s) that Carlos gave us earlier,

[30:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1848s) from my perspective, it's
basically a prerequisite

[30:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1851s) to have this feedback loop in your process

[30:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1854s) to make this work, right?

[30:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1855s) This is how, as Carlos said,

[30:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1857s) the EKS service team operates
is as they're rolling out

[31:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1861s) through those cells and
through those waves,

[31:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1862s) the proactive alerts become something

[31:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1864s) that is telling them whether or not

[31:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1866s) their process should
continue or not, right?

[31:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1869s) They're not sitting watching
dashboards as you can imagine.

[31:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1871s) So the other thing obviously,
as we go through here,

[31:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1875s) Carlos talked about tests.

[31:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1877s) So it's not unusual for us
to talk to platform teams

[31:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1880s) who have maybe built a way to test

[31:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1882s) and upgrade in their sandbox cluster.

[31:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1885s) Maybe they've got a small cluster they use

[31:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1887s) for functional tests.

[31:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1888s) And that will uncover
uncover several issues.

[31:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1891s) But as you progress through
your waves, when you start

[31:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1893s) to reach staging and deployment,

[31:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1894s) at the end of the day, it's no mystery.

[31:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1896s) You're gonna uncover issues
that you just can't find in dev.

[31:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1899s) And you can continue to
iterate on your tests

[31:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1902s) and continue to find
those problems earlier on.

[31:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1904s) But at the end of the day,
the soak period isn't useful

[31:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1907s) unless you're monitoring something

[31:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1909s) and you're alerting on things.

[31:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1910s) I ideally in an automated way

[31:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1913s) that will effectively sort
of act as a circuit breaker

[31:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1915s) for your process, right?

[31:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1916s) So this robust set of alerts
really just ends up being

[32:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1920s) a mechanism we can use to cancel a rollout

[32:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1924s) as it's going through if we
start to run into problems.

[32:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1926s) So this sort of feeds back

[32:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1927s) into that whole continuous
delivery process.

[32:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1933s) This is probably the
question I get asked a lot,

[32:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1935s) which I wish I had a better answer for.

[32:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1937s) I wish I had a list for you
of what you should monitor

[32:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1940s) and what the alert thresholds would be.

[32:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1943s) If anyone has one, please send me it.

[32:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1946s) But at the end of the day, a
lot of you folks are, you know,

[32:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1948s) running Kubernetes already.

[32:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1949s) You know how many components
you can install in a cluster,

[32:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1952s) you know how many different workloads

[32:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1954s) you can have running in a cluster.

[32:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1955s) It can be pretty difficult
to figure out, you know,

[32:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1958s) a set of things that we can
just tell you monitor this stuff

[32:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1960s) and you're, you're gonna be good.

[32:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1962s) Some of these things,

[32:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1963s) there are some great stuff
online you can use as benchmarks,

[32:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1967s) but I think instead of
trying to give you a list,

[32:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1970s) really, what we wanna talk
about here is just emphasizing

[32:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1971s) the breadth of what you have to monitor

[32:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1973s) to effectively do this.

[32:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1974s) To have trust in your process

[32:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1975s) that it will short circuit your deployment

[32:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1977s) if something goes wrong.

[32:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1979s) This can be anything
from did the error rate

[33:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1981s) on your Kubernetes control plane

[33:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1984s) increase after your upgrade?

[33:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1986s) Are your nodes coming up healthy?

[33:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1987s) Did core DNS latency increase?

[33:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1989s) Core DNS is still a problem in 2024.

[33:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1991s) And if we can,

[33:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1994s) can we understand if our
customers workloads are degrading

[33:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1997s) if we've done an upgrade?

[33:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1997s) Right?

[33:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=1998s) Did the error rate on developers team,

[33:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2001s) or sorry, application A, B,
C in experience more latency

[33:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2005s) or experience higher error rate.

[33:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2006s) And if we can especially get
that sort of information,

[33:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2008s) we understand not just
the health of the cluster

[33:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2010s) that we're providing, but
the health of the experience

[33:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2012s) that we're giving to our developers.

[33:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2014s) Now, something which recently
launched, which is related

[33:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2018s) to this would be that we did
in the last couple weeks launch

[33:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2021s) the improved EKS cluster
control plane monitoring,

[33:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2025s) where you can now get a whole bunch

[33:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2027s) of extra metrics outta the control plane,

[33:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2029s) which is something you
should definitely check out.

[33:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2030s) We'll throw a link in some
of the related resources

[33:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2033s) at the end of the session,
but that gives you a whole set

[33:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2036s) of metrics that you
didn't previously have,

[33:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2037s) as well as extra mechanisms
built into the console

[34:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2041s) around things like
looking at your audit logs

[34:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2043s) and stuff like that to identify issues.

[34:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2045s) So that's been a great recent launch,

[34:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2046s) which you can start to leverage.

[34:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2049s) Now, not strictly observability,

[34:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2052s) but we're gonna throw under this umbrella

[34:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2053s) is maybe switching,
switching off a little bit,

[34:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2055s) which is cluster inventory.

[34:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2057s) So this is less around,
you know, finding issues

[34:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2060s) and troubleshooting
issues and more around,

[34:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2062s) how do I get a picture of all the clusters

[34:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2064s) in my organization?

[34:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2065s) Especially as it starts to scale

[34:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2066s) and especially as it starts
to scale across regions,

[34:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2070s) but accounts and whole
AWS organizations, right?

[34:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2072s) It can be tricky to navigate
between all the console screens

[34:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2075s) and sort of keep track

[34:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2076s) of what's going going
on in aggregate view,

[34:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2079s) there's lots of ways
that you can solve this.

[34:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2080s) We see people doing it with vendor tools.

[34:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2082s) We see them using Grafana
and observability tooling.

[34:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2085s) One thing that we started to see

[34:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2087s) is folks using developer
portals like Backstage.

[34:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2089s) So I'm a big fan of Backstage

[34:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2092s) if you've seen it myself before,

[34:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2094s) but we have seen some customers,

[34:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2096s) especially Kubernetes native customers,

[34:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2098s) starting to use the ability

[35:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2100s) to ingest information
about their EKS clusters

[35:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2102s) into developer portals,
whether it's an open source one

[35:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2105s) like Backstage or vendor products

[35:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2107s) that kind of provide the equivalent.

[35:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2109s) So you get that cross-account,
cross-region view

[35:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2112s) of all the clusters that you have there.

[35:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2114s) I think this is probably a better option

[35:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2117s) than some of the other
approaches that we see,

[35:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2119s) like building your own portal from scratch

[35:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2120s) as a custom web app.

[35:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2121s) Which a lot of people were doing

[35:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2122s) with developer portals before Backstage.

[35:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2124s) But this is something that I
think we're, we're starting

[35:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2126s) to see some of our more
advanced Kubernetes users

[35:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2130s) take advantage of, as
well as an aggregate list

[35:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2133s) of all our clusters, especially
tools like Backstage,

[35:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2135s) which are super flexible,
gives us the opportunity

[35:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2137s) to customize and start
to aggregate information

[35:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2140s) not just from EKS but
from related systems.

[35:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2143s) So we could start with basic stuff, right?

[35:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2145s) Maybe our account ID, our
AWS region, EKS version,

[35:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2149s) the add-on versions, just
basic stuff we can pull

[35:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2151s) from the API and maybe some of the places,

[35:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2153s) but then we can start to
add in extra information

[35:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2155s) like a cost tab where we
maybe pull the information

[35:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2158s) from Cube cost or open cost.

[36:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2160s) Maybe we start to provide
feedback on policy violations

[36:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2164s) and findings in Backstage and
pull that to the same place.

[36:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2167s) Maybe we show the SLOs for the
cluster so dev teams can see

[36:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2171s) what the historical availability
of their cluster has been.

[36:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2174s) Right?

[36:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2175s) Again, not a monitoring tool,
but just a heads up display

[36:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2177s) of how has this cluster
been performing that users

[36:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2181s) or managers or somebody
else can just take a look at

[36:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2184s) to get a heads up view.

[36:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2185s) And then if there's information

[36:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2187s) that we don't wanna rebuild
all of our other tools

[36:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2190s) in developer portal site Backstage,

[36:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2192s) we then start to provide
out links to all the places

[36:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2194s) that we need to go, right?

[36:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2195s) We're trying to get rid of
that big bookmark folder

[36:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2197s) that you have where especially
if you've got 100 clusters,

[36:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2201s) you're gonna have a
pretty bad time in Chrome

[36:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2203s) trying to keep track of all this stuff.

[36:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2206s) So we provide deep links
into all the places

[36:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2207s) for a given cluster so it
becomes not just a single pane,

[36:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2210s) but also a launching point
often to all the other systems

[36:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2213s) that you need to actually
run your cluster.

[36:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2215s) And it gives you just that
basis for being able to navigate

[36:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2218s) through across your fleet.

[37:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2222s) The last thing that we
find this useful for

[37:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2224s) is relationships.

[37:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2226s) So it's not unusual for developer portals

[37:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2228s) to let you express relationships

[37:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2230s) between whatever they call
items in their catalog.

[37:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2233s) And in the stage case,
it would be entities.

[37:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2236s) We can start to model things

[37:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2238s) like what workloads
depend on a given cluster.

[37:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2241s) Then the team ownership
we already have modeled

[37:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2244s) typically in our Backstage.

[37:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2246s) At this point,

[37:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2248s) we can then start to model which clusters

[37:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2249s) are dependent on each
other by understanding

[37:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2251s) which workloads depend on each other.

[37:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2252s) And we can start to build up this graph

[37:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2255s) of metadata about our
clusters, our workloads,

[37:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2257s) and our organizations that are not,

[37:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2259s) we're not talking about
pods and deployments,

[37:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2261s) we're talking organizationally about

[37:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2264s) how these things fit
together so we can start

[37:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2265s) to understand the impact

[37:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2267s) or blast radius of changes potentially

[37:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2269s) if we needed to figure something out.

[37:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2270s) Or what would the impact be

[37:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2273s) if this cluster in the
picture here went down

[37:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2275s) in terms of not just the
workloads and the teams,

[37:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2277s) but in terms of maybe downstream clusters

[38:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2280s) where the workloads are interlinked.

[38:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2282s) And we can start to do that
by building up this graph.

[38:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2284s) And this can all be done
automatically, right?

[38:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2286s) We don't need to do this manually.

[38:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2289s) Just last week, we open sourced
a new plugin for Backstage

[38:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2292s) where you can now ingest
AWS infrastructure

[38:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2295s) straight into the Backstage
catalog through AWS config.

[38:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2299s) And that means that there
were some existing plugins,

[38:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2301s) which that you do parts of this before

[38:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2303s) that were a little bit patchy

[38:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2305s) in terms of a specific AWS services.

[38:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2307s) Now anything that lives in config,

[38:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2308s) you can pull straight into
Backstage including EKS clusters

[38:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2311s) and then map them through
in terms of dependencies,

[38:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2313s) using things like tags

[38:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2314s) to build up this graph
completely automatically

[38:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2317s) and start to get an idea
of how this fits together.

[38:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2322s) So in a similar vein,

[38:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2325s) Carlos talked at the
beginning about Guardrails.

[38:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2327s) So talk about governments a little bit.

[38:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2332s) One of the themes that
Carlos discussed earlier

[38:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2334s) was consistency, right?

[38:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2335s) When we start to talk to customers

[38:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2336s) that have 100 EKS clusters,
you can't necessarily,

[39:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2340s) well, it's harder to manage those

[39:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2342s) if you don't have a
measure of consistency.

[39:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2344s) So what Carlos talked
about earlier gave us

[39:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2346s) that consistency at the
EKS cluster layer, right?

[39:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2350s) We're getting all of our clusters up,

[39:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2351s) we're getting our nodes up,

[39:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2352s) we're getting our add-ons installed,

[39:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2354s) but unfortunately, we've
got some pesky developers

[39:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2357s) actually putting stuff in the clusters.

[39:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2358s) And depending on your organization,

[39:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2360s) you may or may not have control
over what that looks like,

[39:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2364s) depending on the spectrum
that Carlos talked about

[39:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2366s) of where you end up from vending a cluster

[39:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2368s) all the way through to
a platform abstraction.

[39:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2370s) That gives you more or less control there.

[39:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2372s) So really, in any of those cases,

[39:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2375s) governance really becomes
a key for achieving

[39:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2378s) that consistency as we scale,

[39:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2380s) especially as we're trying
to balance autonomy, right?

[39:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2382s) Between more autonomous dev
teams that have opportunities

[39:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2385s) to do more in their clusters

[39:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2387s) versus maybe a more guardrailed approach

[39:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2390s) where we are helping developers figure out

[39:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2392s) what we should be putting in our clusters.

[39:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2396s) Now again, this is not gonna be

[39:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2398s) a policy as code 100 session.

[40:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2402s) Instead we wanna talk
a little bit more about

[40:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2404s) how we're seeing people
apply this specifically

[40:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2407s) for problems at scale.

[40:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2409s) But just as a quick primer,
obviously for everyone,

[40:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2412s) policy as codes, engines like
OPA gatekeeper by Kyverno

[40:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2414s) are exceptionally popular tools

[40:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2418s) that you can get from
the open source world

[40:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2420s) that will allow you

[40:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2421s) to essentially express policies as codes.

[40:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2424s) For example, Kyverno
typically is a YAML file,

[40:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2427s) and those will often,

[40:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2428s) you can enforce them in
different ways, right?

[40:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2430s) So a pretty open one would
be you apply the policy

[40:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2433s) and the cluster, a set of controllers

[40:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2435s) are reconciling against
changes that are made.

[40:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2437s) And you can flag a policy
report of everything

[40:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2439s) that violates the policy
that needs to be addressed.

[40:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2443s) A little bit of a harsher approach

[40:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2445s) is that you can use things
like admission control

[40:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2447s) to simply block app changes to the cluster

[40:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2451s) that don't apply your policies correctly.

[40:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2454s) Now, certain organizations
are willing to apply that

[40:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2456s) and others are not, again,
on that autonomy scale,

[41:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2460s) that gives us a nice way to
just stop things going in

[41:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2462s) full stop that we don't wanna be there.

[41:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2464s) But oftentimes, development teams will say

[41:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2467s) that it slows them down.

[41:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2468s) And in many cases, it can, right?

[41:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2470s) So you've gotta balance
about which one of these

[41:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2472s) that you're going to apply
effectively to your organization

[41:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2475s) and the nature of how you're
building your platform.

[41:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2479s) But specifically what do we see

[41:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2480s) as some friction points
similar to observability

[41:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2483s) where policies start to
come into the picture.

[41:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2484s) So similar to what to alert on,

[41:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2487s) we have what policies should I write?

[41:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2490s) And this is potentially
even more of a blurry area

[41:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2493s) because I don't know
what your policies are.

[41:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2495s) There's certain natures
of policies that we have

[41:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2498s) that are probably why we
consider a solid baseline, right?

[41:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2501s) Those ones around say security,

[41:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2503s) are you running read only file systems

[41:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2505s) in your house, in your pods?

[41:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2506s) Are you locking down,
adding extra capabilities

[41:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2509s) and running as a root user?

[41:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2510s) All those, I would say boring things

[41:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2512s) that are kinda like your
foundational set of policies

[41:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2515s) that you should really
be putting in place.

[41:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2517s) Probably some basics around
things like are you tagging

[42:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2520s) or labeling all of your pods correctly

[42:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2522s) so you can do chargebacks
for cost as you scale up

[42:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2524s) because you need to keep
your costs under control.

[42:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2528s) Where we start to see this
specifically come into play

[42:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2530s) for larger fleets of clusters.

[42:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2531s) Firstly, keeping rollouts on track.

[42:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2534s) So I've talked to so many customers

[42:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2536s) where they're call them a Kubernetes team

[42:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2538s) or a platform team, are
unable to upgrade clusters

[42:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2540s) because of what developers
have deployed to them, right?

[42:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2544s) As Carlos said about giving folks

[42:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2547s) infrastructures code templates

[42:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2549s) and them never upgrading their clusters,

[42:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2551s) deprecated APIs, deprecated
CRDs, pod disruption budgets

[42:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2556s) that basically get your node
rollout stuck in the mud.

[42:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2560s) This is where we immediately
get into the discussion

[42:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2563s) of policy as code.

[42:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2564s) And you have to be able to
provide guardrails for people

[42:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2567s) so that your cluster
rollout stays on track.

[42:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2570s) You're not gonna be able to
go to every developer team

[42:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2573s) and tell them that they
have to operate their CRDs.

[42:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2575s) If you're running hundreds, 200 clusters,

[42:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2578s) you're gonna spend all
of your time doing that.

[43:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2580s) You have to start to
push that process left

[43:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2582s) and keep them on the rails.

[43:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2583s) And I know it sounds obvious,

[43:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2586s) but my hope here would be that

[43:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2587s) if you are in a similar position

[43:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2589s) or you think you might
be in a similar position,

[43:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2591s) this is a problem that a
lot of customers are having.

[43:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2594s) And the solution is
unfortunately this, right?

[43:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2597s) There's no magic technical
solution to this problem.

[43:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2600s) A lot of it is organizational
as it probably comes across.

[43:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2603s) Policies give us a way to implement

[43:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2605s) an approach to solve this.

[43:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2607s) But this is a recurring problem
that we see people having

[43:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2609s) and you just have to plan for it.

[43:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2610s) So if you are having that problem

[43:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2612s) and are struggling to get
people to get on board

[43:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2614s) with how to fix it, this is
really what we're seeing.

[43:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2618s) The other aspect is availability.

[43:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2619s) We've talked to customers where
they say they can't upgrade

[43:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2622s) the clusters because in
the development clusters,

[43:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2625s) their application teams have
only deployed with one replica.

[43:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2627s) And when they upgrade the
cluster, the teams complain

[43:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2631s) that the cluster went down
and the platform's not stable.

[43:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2635s) This can even go up to
staging and production

[43:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2637s) if they haven't used
pods disruption budgets.

[43:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2639s) And obviously this impacts

[43:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2639s) more than our upgrades
hurting your cluster.

[44:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2644s) If there was other issues, you know,

[44:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2646s) with the cluster itself,
it will also manifest.

[44:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2648s) But if we're going with this
process of regular upgrades,

[44:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2651s) we wanna keep things rolling,

[44:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2653s) we're constantly changing stuff,
we want flexibility there.

[44:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2656s) If these things are not in
place, again, that trust,

[44:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2659s) even if it's just the perception

[44:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2661s) of trust eroding in your platform,

[44:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2663s) you're gonna run into issues
again with adoption teams

[44:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2666s) complaining and it's not necessarily fair,

[44:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2669s) but using policies has
to be one of these tools

[44:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2672s) that you leverage not
just for the resiliency

[44:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2674s) of keeping your apps
running, but for making sure

[44:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2677s) that you can apply these updates
regularly without getting

[44:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2680s) negative feedback on the
platform that you've built

[44:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2682s) and the process that you've
spent all your time building

[44:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2685s) that Carlos talked about earlier.

[44:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2690s) In terms of managing policies.

[44:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2693s) I mean, Carlos has already done

[44:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2695s) all the hard work for us here, right?

[44:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2696s) We've already got our ship and process

[44:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2699s) that can take whatever
artifacts that we want

[45:01](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2701s) and push them out.

[45:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2702s) When you start to get up to scale,

[45:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2704s) what we're really trying to do here

[45:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2705s) is manage consistency,
again, across our clusters,

[45:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2709s) but we have to be able to handle variation

[45:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2711s) and we have to be able
to handle exceptions.

[45:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2712s) So to get that consistency, one pattern

[45:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2715s) that we see often is
just, it doesn't matter

[45:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2717s) what cluster it is,
you have one helm chart

[45:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2719s) of all your policies and
it goes everywhere, right?

[45:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2722s) That's your baseline.

[45:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2723s) Starting to patch work,

[45:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2724s) deploying one policy to one
cluster and one to another,

[45:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2727s) we'll work early on.

[45:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2728s) But as you start to get
up to a larger scale,

[45:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2732s) you're gonna need to just start to say,

[45:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2734s) I'm throwing everything everywhere.

[45:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2735s) And then start to be able to apply options

[45:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2737s) within your helm chart, save
values files that allow you

[45:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2740s) to enable or disable certain policies.

[45:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2741s) Maybe you have different policies

[45:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2743s) in your web services cluster

[45:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2745s) than you have in your
data cluster, for example.

[45:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2748s) So that could be one sort of
maybe bar that you use there.

[45:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2753s) And then we just roll that out

[45:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2754s) with our GitHub-driven process
to all of our clusters.

[45:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2756s) It's just something else that we deploy.

[45:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2758s) In terms of exceptions,

[45:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2759s) so tools like Kyverno have exceptions

[46:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2762s) as a first class process.

[46:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2764s) You need to be able to handle this, right?

[46:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2765s) So it could even just be as simple

[46:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2767s) as you have that third party software

[46:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2769s) that just won't run if it's not run

[46:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2770s) as a root user or something like that.

[46:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2772s) You know, we all have one.

[46:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2774s) So being able to handle
exceptions is something

[46:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2777s) that you need to be able to do eventually,

[46:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2779s) but we want to be able to do
in a way where we can continue

[46:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2781s) to have this single
artifact that we deploy out.

[46:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2783s) So making sure to plan for exceptions,

[46:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2785s) depending on the tooling that
you're using, is something

[46:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2787s) that we wanna make sure we plan for.

[46:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2792s) Now I talked about
earlier around, you know,

[46:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2795s) the different ways that you can run

[46:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2796s) these policies, code frameworks.

[46:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2797s) The simplest being we're just
gonna assess the resources

[46:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2800s) in the cluster and maybe create a report.

[46:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2802s) So Kyverno, for example,

[46:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2804s) will drop in something
like a cluster, you know,

[46:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2806s) a policy report into your cluster

[46:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2808s) when it does its assessment.

[46:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2810s) At first, you can
probably just take a look

[46:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2811s) into the clusters to
see what's not running.

[46:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2814s) But once you start to really
scale out your EKS fleet,

[46:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2817s) you're gonna need something
a little bit more aggregate

[46:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2819s) in order to effectively
police these violations

[47:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2822s) of your policies.

[47:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2823s) So Kyverno, as an example,
has the related project

[47:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2827s) of the policy reporter,
which you can install

[47:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2829s) in your cluster, aggregate
all your findings

[47:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2832s) into a system like S3 or
Elastic Search or Security Hub.

[47:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2835s) And that gives you that single pane

[47:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2837s) where you can aggregate all
those violations in one place.

[47:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2840s) So we have an example
blog post for both OPA

[47:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2844s) and Gatekeeper, which this
screenshot was derived from

[47:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2848s) where we're shipping all
of our kernel findings

[47:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2850s) straight into security hub,

[47:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2851s) now we can search them, we can
search by account, by region,

[47:36](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2856s) by cluster, maybe by workload

[47:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2857s) if all the right metadata is there.

[47:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2858s) And then we can rely on
whatever other features we want

[47:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2861s) from security hub, say
remediation workflows

[47:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2864s) and all that sort of stuff is things

[47:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2866s) that we can build off
of to effectively start

[47:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2868s) to actually not just
detect these violations,

[47:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2870s) but have a system around remediating.

[47:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2875s) So with that, we're at
the point of the talk

[47:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2877s) where we're gonna start to wrap up.

[47:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2878s) So really, this reflects the
three themes at the start

[48:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2883s) of the talk that Carlos talked about.

[48:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2887s) Applying Git GitOps
effectively is something

[48:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2889s) that we're really
starting to see as a trend

[48:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2891s) from these customers that are building out

[48:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2893s) larger fleets of EKS clusters.

[48:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2895s) GitOps, whether it's
a prerequisite or not,

[48:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2898s) is really the trend that we're seeing

[48:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2900s) around technology and things
like ROCD in some cases flux

[48:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2904s) and also piggyback on top of GitOps

[48:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2907s) with Kubernetes-driven
infrastructure provisioning,

[48:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2908s) whether it's ACK cross-plane
and technology like that.

[48:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2912s) Investing in proactive monitoring, right?

[48:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2914s) Of being alert driven,

[48:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2915s) not just so that you can detect problems,

[48:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2917s) but you can, so you can feed it back

[48:38](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2918s) into that GitOps process

[48:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2920s) so that you can have
this largely hands off

[48:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2923s) and you have confidence in the
system that you're building

[48:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2925s) and the process that you're using

[48:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2927s) to keep your customers,
sorry, your clusters updated.

[48:49](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2929s) And finally, we wanna use
governance as our key to scaling.

[48:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2933s) There are some problems
that we keep seeing

[48:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2935s) over and over again as customers
try to manage EKS clusters

[48:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2938s) and start to scale up their adoption.

[49:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2940s) That policies are effectively the key to,

[49:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2942s) and you know, planning for that

[49:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2944s) and, you know, committing to that

[49:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2947s) being the solution is
something that, you know,

[49:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2949s) we have to talk to customers
about pretty regularly.

[49:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2954s) Related sessions this week.

[49:17](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2957s) So this has been pretty high level, right?

[49:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2958s) We've been talking themes and concepts.

[49:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2960s) Carlos has put together a workshop,

[49:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2962s) which is being run twice this week,

[49:24](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2964s) once tomorrow and once on Wednesday.

[49:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2967s) This will also be available on GitHub

[49:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2969s) and the link is in a
link which will be coming

[49:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2972s) in a couple slides, but
that will actually give you

[49:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2974s) hands-on experience in what
we've talked about today

[49:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2977s) - In the three areas of
like you have experience

[49:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2980s) of managing multi-clusters
with GitOps using Argo CD.

[49:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2984s) In the workshop, we have an
example of using Terraform.

[49:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2988s) A lot of folks use Terraform.

[49:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2990s) So the pattern shows you
how to manage Terraform

[49:53](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2993s) for AWS APIs and then Git
Argo CD for the GitOps.

[49:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2996s) So a lot of folks have difficulties

[49:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=2999s) how to put those two tools together.

[50:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3000s) So we have an example of that

[50:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3002s) and then going into management
of observability of like,

[50:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3007s) a lot of platform teams worry about

[50:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3009s) the applications observability,

[50:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3011s) which is just like net good,

[50:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3014s) but forget about like monitoring

[50:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3016s) the observability of the add-ons.

[50:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3018s) Like how is the open
source Karpenter's doing?

[50:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3021s) How Accordion is acting,
BCC and I subnets.

[50:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3025s) That's observability that
the platform teams owns.

[50:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3027s) So they have to be aware of that.

[50:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3029s) And that ends with, you know,

[50:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3032s) some learnings about policy management.

[50:34](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3034s) Would you be using Kyverno?

[50:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3035s) So we'll be using the Kyverno

[50:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3037s) and Kyverno reporting,
configuring actually this example

[50:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3040s) of the security hub.

[50:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3042s) So you have hands on screens on that.

[50:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3044s) So get there early if you can.

[50:47](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3047s) - And it will be available
on, it's already available.

[50:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3048s) - Yeah, and it's available.

[50:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3050s) Everything is on GitHub open source.

[50:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3052s) So you can start looking at
it, taking extracts of it

[50:55](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3055s) to apply it to your own organization.

[50:59](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3059s) - Next, there is Cube 301.

[51:03](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3063s) So this is a talk with Adobe
and some folks from AWS

[51:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3066s) on how they've built
scalable platforms with EKS.

[51:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3068s) They've previously done
some talks at CubeCon,

[51:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3072s) and some other stuff, CNCF-related talks

[51:14](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3074s) around how they do this

[51:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3076s) and you know, they're applying
some of the principles

[51:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3078s) that Carlos talked about
around pre-flight checks

[51:21](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3081s) and post-flight checks and
all that kinda stuff, right?

[51:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3083s) So definitely a talk I
think is worth seeing

[51:26](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3086s) because you'll see
again some of the themes

[51:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3088s) around platform building but also,

[51:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3089s) how Adobe is doing in practice.

[51:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3091s) So definitely recommend that one.

[51:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3092s) And then finally there is some chalk talks

[51:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3095s) that are getting done on
playing off things like

[51:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3100s) infrastructures, code, GitOps,
CI/CD, the different options

[51:43](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3103s) that you have, pros and cons

[51:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3105s) and what maybe you should be considering

[51:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3106s) for your organization
that you can catch again

[51:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3108s) a couple times this week, which
will also be great Sessions,

[51:56](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3116s) Oh. (indistinct).

[52:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3122s) In terms of extra
resources, so EKS workshop,

[52:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3126s) hands-on labs if you
haven't already done it.

[52:08](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3128s) We're continuing to evolve that

[52:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3129s) with the new launches as they come out.

[52:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3131s) We're running that a
couple of times this week,

[52:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3132s) but we didn't include
on the extra sessions.

[52:15](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3135s) But if you want to run this yourself,

[52:18](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3138s) you can run it self-service.

[52:19](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3139s) We can also run this as what
we call an immersion day.

[52:22](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3142s) Talk to your account team.

[52:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3143s) You can have specialists come in,

[52:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3145s) help deliver this to your
teams and learn EKS hands-on.

[52:29](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3149s) It's very modular.

[52:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3150s) We can tailor it to your organization

[52:32](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3152s) depending on what it's you wanna learn.

[52:33](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3153s) So definitely worth taking a
look if you haven't already.

[52:41](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3161s) Best practices guide.

[52:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3162s) So many of you'll probably
already be familiar

[52:44](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3164s) with the EKS Best Practice Guide.

[52:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3165s) It's been around for a while,

[52:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3166s) but recently we did take what
is this great set of knowledge

[52:50](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3170s) for day two operations

[52:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3171s) and it's now officially part
of the EKS documentation.

[52:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3174s) So all the same great knowledge,
but it matches the docs

[52:58](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3178s) and it's all in the same place now.

[53:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3180s) So it could be easier to find.

[53:02](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3182s) And finally, who doesn't love a badge?

[53:04](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3184s) Get your badge put on
LinkedIn, that kind of stuff.

[53:07](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3187s) I don't have mine yet, do you?

[53:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3189s) - [Carlos] Huh?

[53:10](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3190s) - Do you have your EKS badge?

[53:11](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3191s) - Yes.
- Oh, okay.

[53:12](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3192s) I need to catch up.

[53:13](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3193s) (audience laughing)

[53:16](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3196s) This is a link to a GitHub well, page.

[53:20](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3200s) You'll find all the Kubernetes
sessions in this GitHub.

[53:23](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3203s) There'll be a directory for
each Kubernetes session.

[53:25](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3205s) It'll mostly be links to resources.

[53:27](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3207s) We're not necessarily putting code here,

[53:28](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3208s) a bunch of links to stuff
that you can look at

[53:30](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3210s) related to each session.

[53:31](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3211s) So that link should
take you to our folder,

[53:35](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3215s) but that repository,

[53:37](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3217s) you can pretty easily
find your way around it.

[53:39](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3219s) We've added some links in
there to some of the stuff

[53:40](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3220s) that we've talked about,
some of the extra sessions.

[53:42](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3222s) - Yeah, the main rig me
has all the Cube track

[53:45](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3225s) that we are part of.

[53:46](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3226s) Like EKS group track.

[53:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3228s) - Yep.

[53:48](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3228s) - And there's other workshops

[53:51](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3231s) if Niall mentioned Backstage.

[53:52](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3232s) There's also some workshops

[53:54](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3234s) that you're going to get hands
on experience with Backstage.

[53:57](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3237s) I think is Cube 308.

[54:00](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3240s) Cube today is if you want
to get hands on doing EKS

[54:05](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3245s) and Backstage and there's other ones

[54:06](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3246s) of gen AI on Backstage.

[54:09](https://www.youtube.com/watch?v=g9USwIPr7Xs&t=3249s) - [Niall] Yes.

