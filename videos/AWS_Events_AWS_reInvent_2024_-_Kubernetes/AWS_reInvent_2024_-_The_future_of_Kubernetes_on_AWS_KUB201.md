# AWS re:Invent 2024 - The future of Kubernetes on AWS (KUB201)

[Video Link](https://www.youtube.com/watch?v=_wwu0VKy3w4)

## Description

Kubernetes has become a standard way for organizations looking to modernize their application portfolios. AWS developed Amazon EKS to make Kubernetes more accessible to organizations of all sizes, helping them focus on what matters most for their businesses. In this session, join Amazon EKS product leadership to learn about the latest innovations and strategies for building Kubernetes platforms and applications faster. Discover how various organizations use Amazon EKS to run their most demanding applications in the cloud, on premises, and at the edge. Also hear Snowflake share insights on their next-generation AI and ML platform for model training and inference at scale.

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

- Good morning everybody. Welcome to Kub 201, the
future of Kubernetes on AWS. My name is Nathan Taber and I'm really excited to
talk to you this morning. I'm gonna be joined a little
bit later by Hyungtae Kim. So, our special guest speaker. I'm the head of product for
Kubernetes and registries at AWS, and let's get right into it. So, we're here because
there's a fundamental shift in how we use computers. So since mainframes and
integrated microcomputers, enterprise computing has
required significant investments in hardware and data center space. And in 2006, Amazon introduced
Amazon S3 and Amazon EC2. And these were the first
Amazon Web Services. They're part of the reason
why we're all here today. And they represented standard, publicly available
expressions of the storage and compute primitives
that are used by amazon.com to run, what was then and
I think still is today, one of the largest and most
highly trafficked websites in the world. And this is the cloud, a set of computing primitives you can use to run any application from
websites to data processing, to machine learning models. And over the nearly 20 years, AWS has grown to over 220 services, and we've spawned a
number of other clouds, including complex tooling used to manage applications and infrastructure. The cloud has fundamentally
changed our computing model, how we store, process
and retrieve information. We can now write and deploy applications across the world in minutes. We can instantiate entire data centers to train AI models so complex, that just a few years
ago, they would require multi-billion dollar
supercomputer investments. You can do things with a few
clicks in the AWS console, that not too long ago would've taken years of planning, investments and construction. So the cloud has fundamentally changed how we think about building applications. But with so many different
applications running in so many different places,
people have struggled with a consistent model of how to operate in and out of the cloud. And this is not a new problem, right? There have been many
solutions over the years that people have developed,
and that they've tried, but today the leading cloud
operating system is Kubernetes, and Kubernetes has become
incredibly popular. So, a super majority of
enterprises right now are using Kubernetes in production, or they're piloting its use. And this is largely because Kubernetes is actually useful, right? It's an incredibly useful tool. It has a simple set of APIs
for managing large groups of servers and coordinating
how your application runs across all of those servers. And I say simple because Kubernetes has about 1500 API methods or functions across about 55 core resources, and that's compared to
over 10,000 API functions for the AWS Python SDK, right? So relatively simple, but simplicity is just one core value
proposition of Kubernetes. (Nathan clears throat) Andy Jassy has said, "If you believe developers
will build applications from scratch using web services as primitive building blocks, then the operating system
becomes the internet". And within the internet though, there are multiple domains, so places outside of
the internet also exist. And this is where Kubernetes shines, with a set of primitive building blocks that you can use to work everywhere from your data center, to
AWS, to F16 fighter jets, and yes, they seriously did that. You can Google it. They have run Kubernetes
on F16 fighter jets. And finally, Kubernetes
is extensible because, believe it or not, 1500
functions is not enough to power a cloud. And this extensibility
is what allows customers to use Kubernetes in so many places. There are currently 195
open source projects that are managed under the Cloud Native
Computing Foundation, and there's hundreds
more landscape projects which run on, integrate
with, and extend Kubernetes. You can even write your own project, and I'm guessing that many people here have either seen that or
they've done it themselves. Okay. So point taken, Kubernetes is awesome. And actually the truth is, is that using Kubernetes is awesome. Kubernetes has an amazing
developer experience. Running Kubernetes is hard, and Kubectl Apply versus hundreds of lines of YAML, plugins, network
configuration, cluster upgrades, Kubernetes is generally
a hard system to operate, especially at scale, and
especially in multiple places. And so on AWS, we're in our seventh year of managed Kubernetes. We announced Amazon EKS right
here at ReInvent in 2017. And over the last seven years, we've gone deep into every
aspect of operating Kubernetes at what we think may be the
largest scale on the planet. We've taken a basic managed control plane and steadily added capabilities
for compute management, auxiliary software, security,
scalability, networking, observability, troubleshooting, we'd authored dozens of
new open source projects, we've given some of them away to the Cloud Native Computing Foundation, we've made fundamental changes
to how Kubernetes works, built a full suite of public
and internal integrations that help tie AWS and Kubernetes together, and we count ourselves as the home to many of the largest and
most sophisticated applications and machine learning models in existence that are built on Kubernetes. And we now run tens of
millions of clusters for customers every year. And this is growing quickly. If there's an Edge case,
our teams have seen it. We like to say this at AWS, that there's no compression
algorithm for experience. So over the next 45 minutes or so, I wanna talk about how AWS is innovating to help realize the vision of Kubernetes. And like I said, we're
lucky to be joined today by Hyungtae Kim, he's a
principal software engineer at Snowflake. Snowflake is an exabyte scale
data platform built on AWS, and I'm really excited to
hear a little bit later from Hyungtae about how
Snowflake is using EKS to scale machine learning
for their customers. So, yeah. So, your goal is to
deliver business value, not to operate an infrastructure system. Our customers only want
to touch what they need to touch when they need to touch it. So our goal is to take away that undifferentiated heavy lifting of operating these systems, and to deliver the fundamental components that you need to build a production-ready Kubernetes environment. So, what does that mean? What does a Kubernetes environment even look like these days? This is how we see it, right? There's several layers to the stack of actually taking Kubernetes and putting it into production. At the bottom layer, right? We have the infrastructure, and the infrastructure is the compute, the networking, the storage, the core fundamental
components that AWS builds and runs at scale for its customers. On the next layer, we have
the Kubernetes control plane. We handle scale,
availability, integrations and extensions around the
Kubernetes API server, at CD, all the other control plane components. And above that, you need
management tooling, right? Tools and components for
deployment, observability, governance, traffic and security. And then above that, even further, you have developer tooling, for those things like
internal developer platforms, job management, ML workflow management, things that people call ML ops these days, analytics platforms, right? And your applications, your code and your data all are containerized and they run all the way down this stack. And of course, off to the side, we have container registries because all of these things
are packaged as containers and then run down on this infrastructure. And so our goal with Kubernetes is to make it really easy for customers to go from applications and data into a full stack Kubernetes environment. So I'm gonna talk a little bit about that. Let's start with the registry, right? So everything starts with
a container registry. This is the place where your code and your data lands initially. Well, data may be landing
in places like RDS or S3, but application code is being packaged, it's being built with clients,
including Finch, Docker, there's a number of other
tools that are coming in. And we have Amazon ECR,
which is AWS's managed OCI, container registry, really
great registry product. We've been running ECR actually
longer than Amazon EKS. And you can build with any client, you can put that image into ECR, and then you can deploy that
out anywhere in AWS cloud. So you can deploy that
onto EKS, ECS, Lambda or anywhere else you want something to go. And so we've been enhancing
ECR over the last few years. ECR is a very active place
of investment for us. In this last year, we
actually have upgraded our image scanning on ECR because what we found is really important for customers is that
these images are secure, and you wanna run images
that have been scanned, that are signed that you know are running trusted code in production. And so previously we had
an image scanning library called Claire, and Claire was great, but it also didn't have
all of the libraries and all the vulnerability databases that our customers demanded. So in 2024, we integrated
with Amazon Inspector and introduced ECR basic
and enhanced image scanning. And so enhanced image scanning
is an upgrade project. We have basic, which runs on Inspector and then enhanced, which brings in over 50 vulnerability databases and 12 plus operating systems. And you can enable this
inside of every ECR registry and automatically scan images on push, or at any other schedule. The other thing that we've done in ECR is make it easier for customers
to centralize their estate of images in ECR before they pull them. And so essentially establishing
a delivery pipeline of container images all the
way down to the cluster. And one of the ways that we've done that was with ECR Pull Through Cache, or PTC, an authenticated Pull
Through Cache allows you to synchronize an upstream registry that comes from Docker hub,
from GitHub Container Registry or any other public registry source, and synchronize that image down into ECR. When you set that sync up, we automatically create
a private repository in ECR to house that image, all the different variants of it, and we periodically run with
that synchronization process to bring updated images down into ECR. They can there be scanned, and they can sit next
to the infrastructure that you need to pull. So this improves security, and it also improves image pull times to help your applications start faster. And like everything else,
it is available right now. And because of the work we've done on ECR and its footprint, Amazon ECR now has over 2 billion image
pulls every single day. And this is because
it's used with every way that customers run containers,
including on Kubernetes. Okay, so that's some of our innovations and things that we've done on
the container registry side. Let's go ahead and talk a little bit about the Kubernetes control plane. So one of the biggest challenges
that customers have faced with Kubernetes, is keeping
the control plane up to date. And on Amazon EKS, there
was a point in time where our performance on
keeping the control plane up to date, was honestly,
a little bit abysmal. So our high watermark for this
was 243 days behind upstream. And we've invested heavily
over the last two years in automation that has led us move from qualifying new
Kubernetes versions in weeks, down to qualifying new versions in days. And so in 2023, we put this
automation into practice and we launched four
versions of Amazon EKS in order to keep up to date. And so now we've slowed that down. We're now launching three versions a year, which is in pace with the
Kubernetes upstream release cycle. And we've had a consistent performance of about 40 to 35 days behind upstream. I don't think we're gonna
go much faster than this. There may be a time, but we typically wait for a new minor version of
Kubernetes to stabilize, typically to a .1 release
before we pull that down and make it a part of Amazon EKS. But honestly, I think next
year I may not show this graph because it's getting extremely boring, and that's the way that we like it. But as we've accelerated,
as we've brought in images and versions much faster into Amazon EKS, our customers have faced another problem, which is getting onto those
latest versions, right? So upgrading Kubernetes
can be a really big pain. And so what our customers
told us last year was that, look, it takes
us a little bit longer than 14 months, which is the
typical version release process in order to move to a new
version of Kubernetes. And so we listened to
that customer feedback and we introduced
Extended Version Support. Extended Version Support for Amazon EKS gives you an additional 12 months of full support for AWS for
any Kubernetes minor version. So what happens after 14 months in the community release cycle is that all support for that
version goes outta date. So the documentation is
removed from the website, the downloadable binaries are removed, bug tickets, bugs are not
just not worked on anymore, they're no longer accepted. And so effectively this version
is wiped out from existence, but on Amazon EKS, we've
invested in order to keep that running for an additional 12 months. So our teams will look at
new versions of Kubernetes and new CVEs that come down. We'll cherry pick appropriate patches and we'll patch all of the
systems running old versions of Kubernetes to keep them secure so that you can continue operating while you plan your move
to the next version. And so what's really nice
about Extended Version Support is that you choose when and
how much you want to use this. You can run into Extended Version Support on any minor version. You can upgrade back to
Standard Support at any time. You don't need to choose special versions of Kubernetes to hop between, you don't have to plan a strategy. You can adjust when you upgrade based on your business priorities. Also, at the same time, many customers were finding themselves running Extended Version
Support and saying, wait, this is a dev cluster. I actually don't care if you
guys upgrade it automatically. Can I make sure that this always just stays on Standard Support? And so a few months ago we
announced upgrade policies and upgrade policies
keep the control plane automatically updated
on standard versions. So you can set an upgrade policy
on any Kubernetes cluster, any EKS cluster, and
when you set that policy, we'll always keep that
control plane updated on the latest standard
version of Kubernetes. So this is a great solution
for dev and test clusters, or even canary staging clusters where you wanna see what the
impact of that upgrade is, and you never wanna worry about that falling into an
Extended Support mode. And that is available now. So having more time to
upgrade is part of the story, but also having more
confidence when you upgrade is the other part of the story for Kubernetes versions, right? And so our customers
wanted to be able to see what's gonna happen when
I upgrade this version? And so we introduced
Upgrade Insights last year, and Upgrade Insights effectively is a report card for your cluster. We run this continuously,
we give you 30 days of data, and we're looking at what API calls are coming into the API server, and we're looking at
all the future versions of Kubernetes that you're not running. So unfortunately, I did not
sort my list by version here, but you can see that I'm
running a 1.25 cluster in this example. And Upgrade Insights is
testing the API server and the calls that are
being made against it all the way up through version 1.32. So if I wanted to skip multiple versions, I can actually say, hey, I
want to go to 1.26 or 1.27, I can check my report card
against those versions and see if things are passing or failing. And what that looks like,
is I get a high level view, but then I can go directly in and say, okay, where am I getting that error? What's gonna fail out if I upgraded this control plane right now? And so in this case, I'm using a v1 beta 1 pod
disruption budget call, and in 1.25 that's replaced
with a v1 pod disruption budget. So if I upgraded this cluster
from 1.24 to 1.25 right now, I could expect that Kub State Metrics, and this is actually my
application, I named it "App", I know that that's not
very creative (laughs), but you can see that Kube State Metrics and App are the two things here that are making that API call. And so those are the things
that I need to go and fix before I upgrade my cluster. And so what we really like
about Upgrade Insights is that it allows us to
get down into the details and allows your teams
to understand precisely what's going on on the
cluster before you upgrade, to give you more confidence and to prevent failures during an upgrade. And like everything else,
this is available right now. This is inside of every EKS console. If you pop open the console, you'll find this in the
observability dashboard. And it's running on
every cluster by default. There's no cost to this, by the way. This is just available
for every single cluster. So obviously observability
is extremely useful when we're upgrading,
but observability is also a really important part
of operating a system like Kubernetes every single day. And one of the things that
our customers always have to do is to configure
observability on their clusters. And so this year we wanted
to make that a lot easier and we introduced enhanced
control plane observability. So this came out a few months ago, and what we did is we
added two major things. First, we added additional metrics for the cluster, Kube Controller Manager, and Kube Scheduler Metrics. And you can scrape these
in new Prometheus endpoints and export them to any
observability system. We also added new
pre-configured dashboards in the EKS console that
gives cluster administrators visual representation
of these key metrics, and that lets you rapidly assess, is your control plane healthy? Is it performing the way
that we expect it to perform? And so, these are really nice. You can see right here, they're prebuilt, they're in CloudWatch. You can deep dive into
any of these dashboards. And as part of this, we built this whole new
observability suite inside of EKS. And you can see my Cluster Insights tab is off to the right there. It's a little bit small. And we have the metrics, but we also, this is my favorite part,
we deeply integrated with CloudWatch Log Insights. So CloudWatch Log Insights has
been around for a long time, exporting CloudWatch logs, logs from EKS to CloudWatch has also been
around for a long time, but this is something that you had to go and you had to figure
out and run yourself. Now in the EKS dashboard, you have pre-configured log queries and you just press the button, Run Query, and you're gonna see a
list of the log query for certain common things that you may wanna look at on the cluster. So one of my favorites
here is Top Talkers. What this means is what are
the services on the cluster that are the most chatty
with the API server? So this is a great log
query to run for example, if you're seeing some
weird behavior anomalies in the API server, maybe
things aren't performing up to your expectations,
you're seeing that metric, you can go in and run
the Top Talkers query and you can say, hey, you know,
it looks like what is this? My v1 beta 1 ingresses, has made 1700 calls against the API server in the last 30 minutes,
so maybe I need to go look at some of these things,
I may see a spike here and I can get right down
into the root problem. So these dashboards are not meant to replace deeper observability tools, but they're meant to be a starting point for observability and
quick troubleshooting when you're doing cluster administration. And available now. Going a step deeper,
CloudWatch actually has done a huge amount of improvements
over the last year to make it easier for container
customers to use CloudWatch. So we now have Container Insights with enhanced observability
for Amazon EKS. So we put a subset of this
stuff in the EKS console that's available out of the box. And then clicking into CloudWatch, you actually have deeper
performance overviews that can look across one or more clusters. It can give you alarms,
utilization statuses, it gives you data that allows you to take more proactive action
against the performance of your clusters and your
cluster applications. And it gives you metrics and
visibility into cluster health. We recently added GPU Neuron
and Windows Support as well to these Container Insights. This is a really nice feature. I've been super impressed with the work that the CloudWatch team has done, and this is available now with
CloudWatch and Amazon EKS. This week at ReInvent, we actually did a really cool thing for network traffic as
well with CloudWatch. So we've had VPC flow logs for a long time with CloudWatch VPC, and CloudWatch just announced
Network Flow Monitor a few days ago. So this is a really cool new feature that gives you visibility
into the performance of the network traffic, between the boxes in the AWS data center. So a lot of times you may experience, if you're running it especially at scale, customers have problems where they may see network degradations or they're trying to
troubleshoot networking issues, and what CloudWatch
Network Flow Monitor does is it allows you to see exact data and places in the network path where you could see
performance degradations. Amazon EKS is integrated with Network Flow Monitor out of the box. We automatically annotate
the metadata that's traveling between the EC2 instances
inside of the cluster. So when you go into CloudWatch
Network Flow Monitor, you can understand the state
of that network traffic that's bound by the cluster, and whether that's communication
between cluster nodes or in and outta the cluster, and it's more easy to troubleshoot
performance degradations on the network layer. And like everything right
now, it's available right now. This is a new launch at ReInvent. We're really, really excited about it. One of the other things that we built for observability with our customers has been Split Cost Allocation Data. And so one of the biggest issues when you move to Kubernetes, if anyone's ever operated
in a VM world, right? We did these monolithic applications and you would do one application per VM, you would have really nice tagging, you'd get these beautiful
costs and usage dashboards, as an administrator,
you're running everything, it works really nicely,
as a finops administrator you get these really nice reports, and then one day the team says,
we're moving to Kubernetes. And you move to Kubernetes
and everything becomes a black box on the financial side, right? Because you have these shared clusters and multi-tenant microservices, and how do you understand
the exact cost of things? So there have been
tools including Kubecost that we've supported running with Amazon EKS for a number of years. But our customers told us they wanted this natively available in Amazon EKS. And so we partnered with
the AWS Cost and Usage team to introduce Split, (sneezes) excuse me, to introduce Split Cost Allocation Data. And what this does is
that we have a managed way that we are automatically collecting data for pod utilization on the cluster. We're putting that together
with your actual cost of running EC2 on the backend,
and we're building a new cost and usage report that gives
you fine-grained reporting. And this reporting can break
down against the pod level, against the deployment
level, the job level, namespaces and clusters. We automatically ingest
those true EC2 costs and we give you this native report to help you understand the actual cost of your applications. Cool. So, that's a lot on observability. The other thing that
we've done with add-ons, is when you run a cluster, right, just running the control
plane is not enough. You often need to bring
all these different types of operational tools into Amazon EKS. And a few years ago we launched add-ons, which helps you create clusters that have batteries included. And we've expanded the catalog of add-ons over the last year. We've added five or four new add-ons that are first party from Amazon EKS, including CloudWatch Container Insights, CSI Snapshot Controller,
the Pod Identity Agent and the Node Monitoring Agent. We've also enabled you to launch clusters without the core networking add-ons. Some customers told us that
they wanted to launch clusters, for example, without VPC CNI, so now you can configure
that at cluster launch in the add-ons API. And we've also launched over
40 marketplace add-ons to date. So we have the first party
add-ons that are coming from AWS, and then we've added a
marketplace integration where you can actually take more than 40 marketplace add-ons, you can choose which ones you
wanna run in your clusters, and with a single click, you can subscribe and launch those into
your Amazon EKS clusters. So made it really easy to
get tools like Datadog, Kubecost, New Relic, Splunk, et cetera, into your clusters with a single click. And when you install those
add-ons on the cluster, customers asked us to
make them more secure, and to improve the security posture of their clusters in general. So last year at ReInvent, we talked a lot about pod identity, which allows you to assign IEM roles down to specific pods. This year we took pod identity and we integrated it with EKS add-ons. So now in a single click,
when you set that add-on up, you can create and associate
a specific IEM role with that add-on, so that
everything on the cluster has a reduced scope of security and improved security blast radius. And it's available now. On the security side, we've
been continuously investing in security for EKS. So pod identity, bringing
pod identity to add-ons, we've had encryption at the cluster level for secrets for a number of years. You've been able to bring a KMS key to EKS and encrypt your secrets. We thought that that was good,
but it wasn't good enough. And so starting this year,
we now encrypt everything on the cluster with KMS v2 keys that we provide by default. And we don't just encrypt secrets, we encrypt every single object now. You can still bring your own CMK as well to encrypt on top of our KMS v2, but by default now everything
in Amazon EKS clusters is fully encrypted. In addition to encryption
and security controls, we've also improved our access
controls for Kubernetes. So Cedar is a new open source language that was built by AWS, and this is a language that allows you to write more expressive
and explicit policies for access control. And recently at KubeCon, we
announced expanding Cedar to Amazon EKS and Kubernetes. So using Cedar allows you to have features and functionality that are not
available in Kubernetes RBAC like denials, conditions and attribute and label based access controls. And so we're really excited about Cedar, it's a new open source
project that we're doing to bring Cedar and EKS together, and we think this will
be a really nice upgrade for customers to allow
better access control in and out of clusters. Additionally, on the networking side, one of the biggest
pushes from AWS is IPv6. I know you're seeing a lot of IPv6 talk, I think we've been talking about IPv6 for the last 20 years at least. And one of the things that
EKS has done this year is we've now checked the box on everything related to IPv6. So we've previously had single
stack pods and IPv6 clusters. We've had IPv6 management APIs. And now as of a few months ago, we now have IPv6 cluster endpoints. So if you have an IPv6 strategy and you're moving to
IPv6, you can adopt EKS and know that you have full IPv6 support in every part of the cluster. Additionally, on the networking
side, we've integrated with Amazon Application
Recovery Controller. So Route 53 launched
Application Recovery Controller last year, and what this allows you to do is to have a highly resilient setup where you can automatically shift traffic between AZs in the event of
a gray or a black AZ failure. So these could be failures
that we automatically detect and we shift traffic for you, or you can press this big
red emergency stop button at any time and shift traffic over. And so ARC is managed by Route
53, so it's managed centrally and a number of other AWS
services have integrated with ARC. And this allows us to safely shift traffic away and back to the AZ. So one of the things that
happens in an AZ gray failure, right, is we'll have one
component that could fail and could cause a performance degradation. And so then a lot of traffic
may evacuate outta the AZ, and that's fine, we'll go
and people get woken up, people get on calls, we
start to fix that issue. But as the AZ begins to recover,
something that we often see is what we call a thundering herd where everybody says,
oh, the AZ's recovering, let me shove all my traffic back into it. And usually during that AZ recovery phase is where things can be
a little bit delicate. And if you slam that AZ
with traffic right away, then you can have additional degradations and additional failovers. So very small problems can
cascade into very long problems, and short outages can
cascade into longer outages. So Amazon Application Recovery Controller, it doesn't just help you evacuate traffic and keep your applications running when you have an AZ outage issue, it also helps us slowly shift
your traffic back into the AZ so that that AZ doesn't fall over again and we can fully recover from
the incident a lot faster. And also available now. Part of our integration with AWS, we talked about integrations with AWS is allowing customers to have
full access to the cloud. And so our AWS controllers for Kubernetes is a project that we've been building over the last few years, that allows you to have
cloud native control and define AWS resources
directly from the Kubernetes API. Over the last year, we've
launched 20 new services in GA. We've rebuilt the pipelines
to rapidly build services out of Amazon SDKs, and we now
think that this is something that we're seeing more
and more customers use in order to manage their AWS resources alongside their Kubernetes resources. But as ACK has become more popular and we've had more service coverage, we've had customers tell us that, hey, it's really hard to orchestrate
all these things together because I may not just want a
single S3 bucket, for example, I may want a suite of
different capabilities. And so we've recently introduced
the Kube Resource Operator or KRO, and KRO allows you to actually abstract multiple
Kubernetes resources together and write abstractions and
publish them to clusters using Common Expression Language or CEL. And this is a really
simple YAML based language that lets you define a set of AWS and Kube resources together, and then publish that as an
abstraction to the cluster and program against that
abstraction using a CRD. So for example, you can define what a Kubernetes deployment looks like or what a web service
looks like at your company, and you can put that into the cluster as a controller using KRO, and then have your development
teams program against it. It's a really exciting project that's now available on GitHub and Alpha. We plan to develop this more
and more over the next year. Okay, so one thing about
AWS is that we are global. And a big announcement from EKS is that we are now covered in
every single global region, and we have a presence in
every single geographic reason, availability zone, and local zone. And so one of the things that
our customers we found is that they're running in
all these different modes. They're running from
Amazon EKS in the region, down to the local zone,
down to the outpost, down to EKS anywhere. And one of the things
that we are really excited to announce this week at ReInvent is Amazon EKS Hybrid Nodes. So our customers were running Amazon EKS, anywhere in the data center, and they told us that
they wanted something that was a little bit more managed. And so with Amazon EKS Hybrid Nodes, you can now use your existing on-premises or Edge Compute to connect that back to an Amazon EKS control plane
that's running in the region and manage everything consistently. So you can extend that control plane out to the data center and
out to your Edge compute and manage it in a consistent environment. And all the higher level
integrations from AWS, from observability to add-ons work seamlessly with Hybrid Nodes. And so the architecture
looks a little bit like this. I have my CLI tool, I
can install this manually or scripted across all
my on-premises nodes. And when that CLI is installed,
there's a small little agent that runs and the agent
bootstraps the Kubelet and other components onto that node and connects it up to
the Amazon EKS cluster. And so then in the cloud, that
node shows up in the console and also in the API server,
just like any other instance. You can see its attributes and you can start to
schedule workloads onto it. So we think Hybrid Nodes
is gonna be heavily adopted for people in enterprise
modernization, machine learning, financial services, media streaming, manufacturing, IT apps, all
sorts of different places. And we're really, really excited about how Hybrid Nodes is being used. And we've been talking
to customers all week about their plans to adopt Hybrid Nodes. But obviously we also
have the cloud, right? And one of the best parts
of AWS is the breadth and the depth of compute
options, that are offered at AWS. And one of the things that
we wanted to do for customers was to make it easier to
go from create cluster to run application. And so this week we're really excited to announce the launch of EKS Auto Mode. Auto Mode is a major evolution for how to run production ready
Kubernetes in the cloud. And it's also a fulfillment
of our vision for how Kubernetes should
operate in the cloud. So with Auto Mode, you can provision
application ready clusters, pre-configured with all the
capabilities that you need and best practice from AWS. Auto Mode reduces the time that it takes to launch new workloads,
allowing you to get new products or modernize applications
into production faster. And so, typically what
we'd see with customers when they were using
Kubernetes before Auto Mode, is they would choose how
to create the cluster, for example, using infrastructure as code, and then they would,
consider the type of compute that they needed to
run their applications. Do they want to use EC2 or Fargate? What instance types should be used? Then they'd think about
cluster capabilities, and then they'd have a number
of plugins and all this stuff, and they'd have to
provision all these things and wire these things together. With Auto Mode, all of
that is managed for you. So you get the managed control plane. When you put a cluster into Auto Mode, we automatically provision
and manage the capabilities within the cluster for compute,
networking and storage. We have EC2 managed
instances, which are secured and automatically managed instances that run in your account, and we automatically provision everything that's needed in order to run the cluster. So we automatically provision instances and we optimize instances, and keep everything updated
and healthy for you. And with Auto Mode, this
means that we can now have one click cluster creation in the Amazon EKS console and CLIs, and you can easily get started with a single click in the console. And like everything else,
this is available today. Really cool feature that
was launched as part of Auto Mode, is EKS Node
Health and Auto Repair, where we're automatically
looking at the health of nodes, especially GPU instances, and we're repairing
them and improving them. And this is something that's
available now with Auto Mode and we'll be looking to
expand health and auto repair to other functionalities in the future. Cool. So Auto Mode is generally available now, encourage you to check it out. So, one of the things that EKS
has been heavily adopted for is machine learning, from large language
foundational model training, robotics development, and
AI inference at scale, we've seen a lot of
customers use Amazon EKS. And we've been investing
in infrastructure features which simplify and accelerate
machine learning with EKS. So things from node health and auto repair to a set of accelerated AMIs, we are part of the recently
announced EC2 Ultra Servers. EC2 Ultra Servers works
natively with Amazon EKS, and also integrating deeply
with capacity block reservations for compute availability. We've been investing in our integrations for data management with
the S3 Mountpoint CSI Driver and the EFA Kubernetes device plugins for using elastic fabric
adapter networking for GPU instances. We've also been helping to streamline Kubernetes' machine learning by investing in native
OSS frameworks like Ray, and also bringing
accelerated instant support to Container Insights. So I'm really happy to talk more and more about machine learning on EKS, as we see this grow a lot more, and to go deeper into how
they're using machine learning, I'd like to welcome
Hyungtae Kim to the stage, principal software engineer at Snowflake. (audience applauds) - Yeah, thank you. Hello everyone. I'm Hyungtae Kim. I'm one of the engineering
leads for AI app platforms and infrastructure at Snowflake. Today I'm excited to share with you how we are powering AI
innovation at scale. You might be familiar with
our products like Cortex AI, which enables generative AI
capabilities for our customers, but what you may not be familiar with is the infrastructure story behind it all, specifically how we leverage
Kubernetes on top of EKS to build a robust foundation
for these AI services. In this section, I'll share our journey, the challenges that we
face, and the solutions that we implemented, while
building this infrastructure. Let me introduce you to Cortex AI, Snowflake's comprehensive Gen AI platform. What makes Cortex special is this ability to handle the full
spectrum of AI workloads, all powered by Kubernetes
and on AWS powered by EKS. On the inference side, we've built systems that can scale from zero to thousands of concurrent requests. Whether you're running
massive batch operations through familiar SQL interfaces, or powering real-time chat applications with sub-second latency requirements, our infrastructure adapts seamlessly. With our training infrastructure, we're not just running
models, we're building them. Our Arctic family of foundational models represents a significant investment in AI capabilities by requiring. We have models for enterprise use cases from search to document understanding, all requiring intensive
computational resources that EKS helps us manage efficiently. Beyond foundational models, we support sophisticated
fine tuning frameworks. This supports everything from
full parameter fine tuning to more efficient approaches like LoRa, enabling our customers
to customize their models for their specific needs while maintaining
performance and reliability. I'll share some of the real challenges we faced building Cortex because they'll probably
resonate with many of you. We encountered two major
themes that forced us to rethink our traditional
infrastructure approach, capacity management and system fragility. First there's capacity. We all know that GPUs
are scarce and expensive, especially high-end training
hardware like NVIDIA H100s, but what might surprise you is how does scarcity fundamentally
change our operations? Take cluster upgrades for example, the traditional blue-green
deployment approach would require us to temporarily
double our GPU capacity. Imagine spinning up hundreds
of P5s just for an upgrade. It's not just cost prohibitive, is often impossible due
to supply constraints. This forced us to innovate. We had to develop new patterns
for managing capacity, moving away from the just scale up mindset that worked so well for CPU resources, but the more interesting
challenge is fragility. AI workloads, especially
distributed training, have a unique all or
nothing characteristic. Imagine coordinating a
distributed training job across thousands of GPUs, and if just one GPU fails,
the entire job is compromised. Further exacerbating the problem, GPUs and their specialized
networking infrastructure have a higher failure rate
than traditional hardware. And here's the architecture
that powers Cortex. We call this our AI cluster, and it's designed to solve those challenges I just described. The fundamental idea is simple,
one cluster, one region, all AI workloads, but
what makes it powerful is how it intelligently manages resources across different workload types, from real-time inference to
large scale training jobs. Let me walk you through the key components that make this possible. We've organized them
into two main categories, capacity management and resilience. For capacity management, we built a custom capacity controller that access the brains of
our resource allocation. Think of it as an intelligent
traffic controller that knows which resource takes priority. For example, if a
real-time inference service needs more resources, it can intelligently preempt
lower priority training jobs. We paired this with the Volcano Scheduler, an open source scheduler
that handles gain scheduling, which is crucial for coordinating
distributed training jobs. On the resilience side, we
developed three key components. First is our node health service. Think of it as a proactive
diagnostic system. It runs intensive burden validation to ensure all the nodes are healthy. Second, we have a pod janitor. This might sound simple, but Kubernetes can get quite unhappy if we frequently terminate
workloads on top of nodes and it ensures clean termination and intelligent resubmission of pods. Lastly, we have the Invariant Enforcer. It enforces many properties of the cluster like network discovery and distribute training capabilities. Next, we'll dive into one of
our most crucial components, the capacity controller. Think of it as a brain that
orchestrates our GPU resources across different workload types. What you're seeing on screen
is an actual capacity bucket definition for our Cortex
inference workloads. Let me break down why this is interesting. Notice how it is marked as high priority. This means when these inference
services need resources, they get them first. The real magic happens in how we structure these capacity buckets. Each workload type, whether
it's real-time inference, batch processing, or model training, gets its own bucket with clear boundaries. In this example, you can
see we specified both P5 and P4 instance types, with
a minimum of three nodes and shared service stability and room to scale up to
200 nodes when needed. What makes the system
powerful is this ability to move nodes between
buckets intelligently. Think of it as a dynamic resource pools that can ship based on demand, but we can't just grab those randomly when we're dealing with
distributed training jobs that might be using hundreds of GPUs, we need to be surgical about
which nodes to take and when. And next, let's talk
about how we handle one of the trickiest challenges
in AI infrastructure, hardware reliability. GPUs are incredibly powerful, but they're sensitive pieces of hardware that can develop issues over time. Our node health service
is our automated guardian that ensures every GPU on our
fleet is performing optimally. Looking at the diagram,
you can see the lifecycle of a node in our system. When a new node joins our cluster, it starts in what we call
the probation period. It's there, but we won't
let it run workloads yet. We put this set nodes in probation through a comprehensive health check, that includes four critical areas, GPUs, networking, storage, and performance. What makes the system
particularly clever is how it handles multi-node scenarios. When something goes wrong
in a distributed work node, finding the problematic
node can be quite difficult, and you need to take
a systematic approach. We use pairwise testing to
isolate problematic nodes. And if a node fails this test, it is automatically
terminated through AWS APIs. If it succeeds, it joins active fleet. Post validation, if
any subsequent workload reports a potential failure, it is put back into validation. Next, let me share how EKS has accelerated our AI infrastructure. Instead of getting bogged down in the low level
complexities, we've been able to focus on what really matters, building innovative AI solutions. First is performance. Through close collaboration with AWS, we've been able to
optimize the performance of the elastic fiber adapter networking, which is crucial for distributed training. The out of box
compatibility of the systems is also valuable. The accelerated AMIs come
with compatible drivers for both GPUs and networking. The accelerated AMIs are also
compatible out of the box with the latest NVIDIA PyTorch images. Storage is also another area where EKS has simplified our operations. We've implemented a tiered approach. We use FSx for Lustre to provide high performance
distributed storage for model checkpoints and training data. EBS and EFS provides other
persistent similarities and S3 serves as a reliable
archive for data and models. This flexibility allows
us to optimize performance and cost for each specific use case. Last is in scalability and operations. Remember when GPU capacity challenges that I mentioned earlier? With AWS, we don't need to worry about maintaining our
own performance buffer because they handle no
remediation automatically. And for lower tier hardware, like 8 Tons, we can rely on the auto
scaling capabilities of EKS to manage those workloads. Coming full circle to the
two critical challenges, we started with, capacity
management and system fragility, our Snowflake AI cluster has transformed these challenges into strengths. Remember when I mentioned how AI workloads don't typically play well with traditional Kubernetes patterns? Well, we changed that story. In our online inference service
now can scale dynamically with demand, just like any
other Kubernetes workload. This is possible because
our capacity controller intelligently borrows resources from lower priority workloads when needed. We've also solved the thorny
problem of cluster upgrades. Instead of needing to double
our expensive GPU capacity for blue-green deployments, we can now orchestrate
upgrades by priority. We start with training workloads, then smoothly transition our latency sensitive inference services, maximizing uptime while
minimizing resource requirements. And the fragility challenge,
our no health service has dramatically reduced the
impact of hardware failures. When issues occur, and they still do with high performance hardware, they're automatically detected and migrated behind the scenes. And before I hand it back to Nate, let me share some of the
lessons from our AI journey building this infrastructure. These are the lessons I wish someone had told me when we started. First, embrace the impermeance
in your workload design. We learn sometimes the hard
way that treating disruptions as a feature, rather than a bug, leads to more resilient systems by keeping state and Kubernetes small and moving, offloading them to other features like
Ephemeral Vault, like S3, we can handle no failures
in capacity gracefully. It's about optimizing for
recovery, then preventing failure. Second, be strategic
about hardware management. Those GPU nodes are expensive. And when you find a set of
good ones, hold onto them, especially if you're on reservations. We save countless debugging hours by implementing rigorous
validation on node acquisition. Think of it as quality control
for your infrastructure. Third, automation isn't
optional, it's essential. Kubernetes can get into interesting states when you're frequently
terminating instances with active workloads. We build automated systems to monitor and remediate these issues, handling everything from stuck pods to cache synchronization problems. And lastly, here's a practical tip that saves us at least
one cluster rebuild, plan your network
infrastructure generously. The H 100 nodes consume a lot of IPs. We're on our eighth
iteration of our AI cluster in just 18 months. And every iteration we've learned
something new about scale. And the key lesson here is we've learned to treat our AI infrastructure like a living, breathing system. We need to constantly evolve, and look out for potential issues and be ready to fix that every time. And with that, I'll hand it back to Nate. (audience applauds) - Thanks Hyungtae. That was great. What Hyungtae and the team
at Snowflake have done is really, really impressive. Using EKS they've accelerated
the progress of Snowflake. They've taken a core system and evolved it into one of the best in class AI training and inference systems in the world. And they've helped their
customers manage data at scale all the much better. So, I wanna spend the next
few minutes that we have here talking about the future of Amazon EKS. So this is something
that we see across AWS, with sophisticated customers
that have engineering teams that are dedicated to
solving the hardest problems in distributed systems
and machine learning. And these technology companies, these pure technology companies, have a mission to solve
these hard problems. But we also have customers who need to solve similar problems, but they have a very
different focus, right? Using Kubernetes to innovate on behalf of their core businesses
for their customers. And this is a side effect of all these companies
becoming technology companies, advanced systems like AWS and Kubernetes, they can be engines for success
across your organization. But at the same time,
if your mission is not to build these systems,
but to solve problems that are not technology problems, it can be really difficult
to use these systems. And it's not that companies that are not pure technology companies are not smart people, it's just
they have a different focus. And so at a tech conference like ReInvent, it can seem like everybody
here is a technology company and this is what we're building for. But the reality is that
most companies in the world are not software technology companies. And most people are solving
other hard problems, and they want to take advantage
of this software technology. And so that leaves us with a problem because while we think that every company should use advanced technologies
to further their mission, lower costs and accelerate innovation, most companies shouldn't have to become pure software
technology companies to get these benefits. They should be able to
leverage the tools built by dedicated tech companies and software communities to
accelerate their innovation, lower cost, and improve
the quality of goods and services that they
produce for society. And so, the reason we all
love conferences like ReInvent is because they give a
glimpse into the future, the hope that you can have
this amazing new thing that's here right now, and it's finally actually
available to use. And this is our second problem, right? Systems like Kubernetes
we see as the future, but they can be hard to use. They require dedicated effort and expertise to install and operate. And then finally, in the cloud, running these things can require a lot of this time and expertise. And if you're using open
source technologies, sometimes even more so, so building and properly leveraging OSS can sometimes mean that you need people who understand how to build
and leverage that OSS, and really quickly they can go from, hey, I found a really cool
tool that we can install and use at our company, to, we're now a maintainer of that tool. And now, oh, we're a primary
maintainer of that tool. And now we own that tool, and we never intended to own that tool because that's not our business focus. And look, I don't want to say, discourage people in any way from using open source technology. In fact, I think open source technology is an amazing innovation. Like the idea of open
source software in general, and that I think that
all companies like AWS and our customers should
be contributing to OSS, but a problem that can happen is that at scale, OSS can become expensive. And so this is something that
we want to help customers with and make it a little bit easier. And so this is a balance, right? How do you keep control and flexibility all the
way from start to scale? How do you balance this trilema of systems where you want to have scale and control, you wanna have speeds of
changes and have scale? We see this trilema is
often you can pick two out of these three things. And we wanna optimize for customers at all of these levels, right? And so our mission with
EKS is to help kind of grow this triangle a little bit bigger. You'll still have to make
trade-offs and choices, but we wanna make it a
little bit more optimized and make those trade-offs a
little bit less painful, right? And so that's the goal that we have, is to go faster and
farther together with you. And our strength in AWS is secure, resilient, and scalable operations. Whether you're a software
technology company or you're in the majority of companies that do something extremely important, our mission is to help
accelerate your time to value with complex tools that don't require you to become an expert,
democratize innovation from AWS, our partners in the community, and lower the cost of entry turning CapEx into OpEx for all aspects of the stack. So a few years ago I showed a slide that looked really similar to this, right? This is our journey of Amazon EKS. We started from a hosted control plane, then we introduced managed data planes and with Auto Mode, right? We're making that even more managed now. And then also managed operational tools, also a part of Auto Mode. And while that mission has not changed and the overall strategy
of EKS has not changed, we found that the needs of our customers have evolved, right? You are all divinely unsatisfied. So let's zoom out a little bit, and there's a lot more
going on here, right? Like as we showed in the beginning, Kubernetes is a lot more than the cluster. So first of all, most folks don't just run
a single cluster anymore. They run a lot of clusters. People I speak to run
at least five, maybe 10, sometimes thousands, across
hundreds of accounts. And they want to knit them
those clusters together into a platform with
centralized management, observability, governance, access control, secrets management and deployments. And they wanna wrap that all
up in a beautiful package with templates, codified best practices, documentation, run books, everything that their developers and their data scientists
need to deploy applications to the exact places that they run best. Whether that's across a
fleet of accelerated TRN2 or NVIDIA GPU instances in the cloud, thousands of Edge locations, or they wanna manage all
of that seamlessly, right? They wanna manage that
seamlessly with the help of AWS. And so this is a little bit of a preview into where we're thinking is that this year we have integrated Hybrid, how do we start to bring in more of those platform components? How do we bring in an integrated
development experience? And so these are our investment priorities for the next few years, right? And this is exactly
what we're going to do. We're gonna provide optimized experiences for critical workload
patterns at any scale. We're gonna deepen AWS integrations and tooling for management and efficiency. And our goal is, as we do
this, to meet your workloads where they are, whether
those are in the cloud, across multiple regions, in local zones, on-premises in data
centers, or at the Edge. We also wanna simplify platform building. We want to make it easy to
have a production grade, Kubernetes based platform on AWS. And finally to accelerate the flywheel of innovation in the community, right? Open source is the engine that
powers so much of what we do, and we wanna make sure
that we are able to power that innovation, to have
new innovation be developed, to be a part of that, and
then also to bring that to customers so that they
consume it really easily without having to become deep experts in every single component
that they wanna run. And so for customers, we weren't gonna automate more things in and around the cluster, natively bring you the
latest AWS innovations through Kubernetes, and
ensure compatibility with and support for community projects, which make this Kubernetes
innovative and powerful. And for partners, because
we have so many partners that are either here
today or watching this, we wanna make it easier for you to build on EKS for your
products and services. We want to give you simple paths that allow you to enable EKS customers and to sell alongside
AWS to those customers, and provide ongoing guidance, support, and ideas to improve your
products in our partnership. So, this is a hard talk to give, right? Because it's the future, and it's hard to give a lot of detail about what we're doing, but also know that we're always thinking deeply about what we should do next. So it's a balance between
how much do we share and how much do we hold back knowing that it might change. Why would it change, right? It would change because our roadmap and our plans are completely based on what we hear from our customers, right? We build everything based
on customer feedback. If we don't have good data,
that customers really want what we're building and
we find it valuable, we simply won't build it. And as we start to build things, we talk to our customers about it, right? We experiment. And if our customers don't
find it valuable, we change it. We stop it and we go build
the thing that our customers are asking us to build. So we spent the whole front half of this presentation talking about all the new stuff that came out. Every single one of those has been driven by our customer asks. And for every slide that I showed, there's five other slides
that never made the cut because they're projects that
we considered and never built, 'cause as we talked to
customers about them, we found that maybe they
just weren't that useful, and we shouldn't go ahead and build them. And so, what this boils down to is that to understand the future of EKS, you have to know that you are
as big a part of the story as we are, and we're gonna
keep doing more things that make it easier to make Kubernetes a standard part of your stack. And Kubernetes turned
10 years old this year and 10 years from now, our mission is to make Kubernetes disappear. And so where are the
receipts on this, right? Well, we have our
containers public roadmap. And this is a place where we push things and we post things that
we're thinking about or working on, where you can
come and you can submit ideas and converse directly with the team. I went and counted this up 'cause I didn't wanna
put the slide up here and talk about this amazing thing and say, well, yeah, but no one ever uses it, to date, we've shipped over 400 EKS items on the roadmap since
we started it in 2018. And over 850 total items
that have hit this roadmap have been shipped across all
of our container services. So we encourage you to
visit this regularly. You can see what other people are saying. You can upvote, you can comment on things that you'd like to see
or submit your own ideas if you think we can do something better. So EKS issues are on here,
they're tagged as EKS, but you'll also see issues for other container services as we visit. And we encourage you to submit ideas and join the conversation there as well. If you wanna learn more about Amazon EKS, we have a number of great resources that the team has developed. We have the EKS Best Practices Guide, which was recently updated with best practices for machine learning. We also have the EKS workshop. You may have been able to attend an EKS workshop here at ReInvent. The EKS workshop is our master home for all of these workshops and events. So if you weren't able to make a workshop session at ReInvent, I highly encourage you and
your team to check this out. And then we have EKS blueprints, which is a set of best
practice codified examples for how you can deploy complete clusters, and now even platforms using Amazon EKS. And we have blueprints in both Terraform and the AWS CDK. So really appreciate
everybody coming today. And thank you for spending
some time to learn about what we're doing with EKS
from myself and Hyungtae. Thank you. (audience applauds)

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=0s) - Good morning everybody.

[00:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2s) Welcome to Kub 201, the
future of Kubernetes on AWS.

[00:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=6s) My name is Nathan Taber

[00:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=7s) and I'm really excited to
talk to you this morning.

[00:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=10s) I'm gonna be joined a little
bit later by Hyungtae Kim.

[00:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=12s) So, our special guest speaker.

[00:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=15s) I'm the head of product for
Kubernetes and registries

[00:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=17s) at AWS, and let's get right into it.

[00:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=20s) So, we're here because
there's a fundamental shift

[00:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=24s) in how we use computers.

[00:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=27s) So since mainframes and
integrated microcomputers,

[00:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=30s) enterprise computing has
required significant investments

[00:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=33s) in hardware and data center space.

[00:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=37s) And in 2006, Amazon introduced
Amazon S3 and Amazon EC2.

[00:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=42s) And these were the first
Amazon Web Services.

[00:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=44s) They're part of the reason
why we're all here today.

[00:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=47s) And they represented standard,

[00:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=48s) publicly available
expressions of the storage

[00:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=51s) and compute primitives
that are used by amazon.com

[00:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=54s) to run, what was then and
I think still is today,

[00:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=57s) one of the largest and most
highly trafficked websites

[01:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=60s) in the world.

[01:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=61s) And this is the cloud,

[01:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=62s) a set of computing primitives you can use

[01:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=64s) to run any application from
websites to data processing,

[01:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=68s) to machine learning models.

[01:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=70s) And over the nearly 20 years,

[01:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=72s) AWS has grown to over 220 services,

[01:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=75s) and we've spawned a
number of other clouds,

[01:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=77s) including complex tooling used

[01:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=79s) to manage applications and infrastructure.

[01:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=82s) The cloud has fundamentally
changed our computing model,

[01:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=85s) how we store, process
and retrieve information.

[01:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=88s) We can now write and deploy applications

[01:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=91s) across the world in minutes.

[01:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=92s) We can instantiate entire data centers

[01:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=95s) to train AI models so complex,

[01:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=97s) that just a few years
ago, they would require

[01:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=99s) multi-billion dollar
supercomputer investments.

[01:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=102s) You can do things with a few
clicks in the AWS console,

[01:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=105s) that not too long ago would've taken years

[01:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=106s) of planning, investments and construction.

[01:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=109s) So the cloud has fundamentally changed

[01:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=111s) how we think about building applications.

[01:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=113s) But with so many different
applications running

[01:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=116s) in so many different places,
people have struggled

[01:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=119s) with a consistent model of how to operate

[02:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=121s) in and out of the cloud.

[02:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=122s) And this is not a new problem, right?

[02:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=124s) There have been many
solutions over the years

[02:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=126s) that people have developed,
and that they've tried,

[02:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=129s) but today the leading cloud
operating system is Kubernetes,

[02:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=133s) and Kubernetes has become
incredibly popular.

[02:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=136s) So, a super majority of
enterprises right now

[02:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=139s) are using Kubernetes in production,

[02:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=142s) or they're piloting its use.

[02:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=144s) And this is largely because Kubernetes

[02:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=146s) is actually useful, right?

[02:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=148s) It's an incredibly useful tool.

[02:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=150s) It has a simple set of APIs
for managing large groups

[02:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=153s) of servers and coordinating
how your application runs

[02:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=156s) across all of those servers.

[02:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=157s) And I say simple because Kubernetes

[02:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=159s) has about 1500 API methods or functions

[02:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=163s) across about 55 core resources,

[02:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=165s) and that's compared to
over 10,000 API functions

[02:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=169s) for the AWS Python SDK, right?

[02:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=171s) So relatively simple, but simplicity

[02:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=174s) is just one core value
proposition of Kubernetes.

[02:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=177s) (Nathan clears throat)

[02:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=179s) Andy Jassy has said,

[03:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=180s) "If you believe developers
will build applications

[03:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=182s) from scratch using web services

[03:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=184s) as primitive building blocks,

[03:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=186s) then the operating system
becomes the internet".

[03:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=189s) And within the internet though,

[03:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=190s) there are multiple domains,

[03:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=191s) so places outside of
the internet also exist.

[03:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=195s) And this is where Kubernetes shines,

[03:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=196s) with a set of primitive building blocks

[03:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=198s) that you can use to work everywhere

[03:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=201s) from your data center, to
AWS, to F16 fighter jets,

[03:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=204s) and yes, they seriously did that.

[03:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=206s) You can Google it.

[03:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=207s) They have run Kubernetes
on F16 fighter jets.

[03:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=210s) And finally, Kubernetes
is extensible because,

[03:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=214s) believe it or not, 1500
functions is not enough

[03:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=218s) to power a cloud.

[03:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=219s) And this extensibility
is what allows customers

[03:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=224s) to use Kubernetes in so many places.

[03:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=226s) There are currently 195
open source projects

[03:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=231s) that are managed

[03:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=232s) under the Cloud Native
Computing Foundation,

[03:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=234s) and there's hundreds
more landscape projects

[03:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=237s) which run on, integrate
with, and extend Kubernetes.

[04:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=240s) You can even write your own project,

[04:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=242s) and I'm guessing that many people here

[04:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=244s) have either seen that or
they've done it themselves.

[04:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=247s) Okay.

[04:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=248s) So point taken, Kubernetes is awesome.

[04:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=251s) And actually the truth is,

[04:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=252s) is that using Kubernetes is awesome.

[04:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=254s) Kubernetes has an amazing
developer experience.

[04:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=257s) Running Kubernetes is hard,

[04:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=260s) and Kubectl Apply versus hundreds of lines

[04:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=263s) of YAML, plugins, network
configuration, cluster upgrades,

[04:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=267s) Kubernetes is generally
a hard system to operate,

[04:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=271s) especially at scale, and
especially in multiple places.

[04:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=275s) And so on AWS, we're in our seventh year

[04:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=277s) of managed Kubernetes.

[04:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=279s) We announced Amazon EKS right
here at ReInvent in 2017.

[04:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=283s) And over the last seven years,

[04:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=285s) we've gone deep into every
aspect of operating Kubernetes

[04:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=288s) at what we think may be the
largest scale on the planet.

[04:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=291s) We've taken a basic managed control plane

[04:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=293s) and steadily added capabilities
for compute management,

[04:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=297s) auxiliary software, security,
scalability, networking,

[05:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=301s) observability, troubleshooting,

[05:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=302s) we'd authored dozens of
new open source projects,

[05:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=305s) we've given some of them away

[05:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=306s) to the Cloud Native Computing Foundation,

[05:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=308s) we've made fundamental changes
to how Kubernetes works,

[05:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=312s) built a full suite of public
and internal integrations

[05:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=314s) that help tie AWS and Kubernetes together,

[05:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=317s) and we count ourselves as the home

[05:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=319s) to many of the largest and
most sophisticated applications

[05:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=322s) and machine learning models in existence

[05:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=324s) that are built on Kubernetes.

[05:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=327s) And we now run tens of
millions of clusters

[05:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=329s) for customers every year.

[05:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=331s) And this is growing quickly.

[05:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=332s) If there's an Edge case,
our teams have seen it.

[05:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=336s) We like to say this at AWS,

[05:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=337s) that there's no compression
algorithm for experience.

[05:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=341s) So over the next 45 minutes or so,

[05:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=343s) I wanna talk about how AWS is innovating

[05:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=345s) to help realize the vision of Kubernetes.

[05:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=348s) And like I said, we're
lucky to be joined today

[05:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=350s) by Hyungtae Kim, he's a
principal software engineer

[05:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=353s) at Snowflake.

[05:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=354s) Snowflake is an exabyte scale
data platform built on AWS,

[05:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=358s) and I'm really excited to
hear a little bit later

[06:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=360s) from Hyungtae about how
Snowflake is using EKS

[06:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=363s) to scale machine learning
for their customers.

[06:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=367s) So, yeah.

[06:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=369s) So, your goal is to
deliver business value,

[06:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=372s) not to operate an infrastructure system.

[06:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=375s) Our customers only want
to touch what they need

[06:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=377s) to touch when they need to touch it.

[06:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=379s) So our goal is to take away

[06:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=382s) that undifferentiated heavy lifting

[06:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=384s) of operating these systems,

[06:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=385s) and to deliver the fundamental components

[06:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=388s) that you need to build

[06:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=389s) a production-ready Kubernetes environment.

[06:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=391s) So, what does that mean?

[06:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=393s) What does a Kubernetes environment

[06:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=394s) even look like these days?

[06:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=396s) This is how we see it, right?

[06:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=398s) There's several layers to the stack

[06:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=400s) of actually taking Kubernetes

[06:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=402s) and putting it into production.

[06:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=403s) At the bottom layer, right?

[06:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=405s) We have the infrastructure,

[06:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=406s) and the infrastructure is the compute,

[06:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=409s) the networking, the storage,

[06:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=411s) the core fundamental
components that AWS builds

[06:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=413s) and runs at scale for its customers.

[06:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=415s) On the next layer, we have
the Kubernetes control plane.

[06:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=418s) We handle scale,
availability, integrations

[07:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=421s) and extensions around the
Kubernetes API server, at CD,

[07:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=424s) all the other control plane components.

[07:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=427s) And above that, you need
management tooling, right?

[07:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=430s) Tools and components for
deployment, observability,

[07:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=432s) governance, traffic and security.

[07:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=434s) And then above that, even further,

[07:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=436s) you have developer tooling,

[07:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=437s) for those things like
internal developer platforms,

[07:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=440s) job management, ML workflow management,

[07:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=442s) things that people call ML ops these days,

[07:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=444s) analytics platforms, right?

[07:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=446s) And your applications, your code

[07:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=447s) and your data all are containerized

[07:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=450s) and they run all the way down this stack.

[07:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=452s) And of course, off to the side,

[07:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=454s) we have container registries

[07:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=455s) because all of these things
are packaged as containers

[07:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=457s) and then run down on this infrastructure.

[07:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=460s) And so our goal with Kubernetes

[07:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=462s) is to make it really easy for customers

[07:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=464s) to go from applications and data

[07:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=467s) into a full stack Kubernetes environment.

[07:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=469s) So I'm gonna talk a little bit about that.

[07:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=471s) Let's start with the registry, right?

[07:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=473s) So everything starts with
a container registry.

[07:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=475s) This is the place where your code

[07:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=477s) and your data lands initially.

[07:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=479s) Well, data may be landing
in places like RDS or S3,

[08:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=482s) but application code is being packaged,

[08:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=484s) it's being built with clients,
including Finch, Docker,

[08:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=488s) there's a number of other
tools that are coming in.

[08:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=490s) And we have Amazon ECR,
which is AWS's managed OCI,

[08:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=494s) container registry, really
great registry product.

[08:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=497s) We've been running ECR actually
longer than Amazon EKS.

[08:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=501s) And you can build with any client,

[08:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=503s) you can put that image into ECR,

[08:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=505s) and then you can deploy that
out anywhere in AWS cloud.

[08:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=508s) So you can deploy that
onto EKS, ECS, Lambda

[08:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=511s) or anywhere else you want something to go.

[08:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=513s) And so we've been enhancing
ECR over the last few years.

[08:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=515s) ECR is a very active place
of investment for us.

[08:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=520s) In this last year, we
actually have upgraded

[08:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=522s) our image scanning on ECR

[08:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=524s) because what we found is really important

[08:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=525s) for customers is that
these images are secure,

[08:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=528s) and you wanna run images
that have been scanned,

[08:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=530s) that are signed that you know

[08:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=531s) are running trusted code in production.

[08:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=533s) And so previously we had
an image scanning library

[08:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=536s) called Claire, and Claire was great,

[08:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=538s) but it also didn't have
all of the libraries

[09:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=541s) and all the vulnerability databases

[09:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=543s) that our customers demanded.

[09:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=544s) So in 2024, we integrated
with Amazon Inspector

[09:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=549s) and introduced ECR basic
and enhanced image scanning.

[09:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=552s) And so enhanced image scanning
is an upgrade project.

[09:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=555s) We have basic, which runs on Inspector

[09:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=558s) and then enhanced, which brings in

[09:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=559s) over 50 vulnerability databases

[09:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=561s) and 12 plus operating systems.

[09:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=563s) And you can enable this
inside of every ECR registry

[09:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=567s) and automatically scan images on push,

[09:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=569s) or at any other schedule.

[09:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=572s) The other thing that we've done in ECR

[09:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=574s) is make it easier for customers
to centralize their estate

[09:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=577s) of images in ECR before they pull them.

[09:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=580s) And so essentially establishing
a delivery pipeline

[09:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=582s) of container images all the
way down to the cluster.

[09:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=585s) And one of the ways that we've done that

[09:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=586s) was with ECR Pull Through Cache, or PTC,

[09:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=589s) an authenticated Pull
Through Cache allows you

[09:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=591s) to synchronize an upstream registry

[09:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=594s) that comes from Docker hub,
from GitHub Container Registry

[09:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=597s) or any other public registry source,

[09:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=599s) and synchronize that image down into ECR.

[10:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=602s) When you set that sync up,

[10:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=603s) we automatically create
a private repository

[10:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=605s) in ECR to house that image,

[10:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=607s) all the different variants of it,

[10:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=609s) and we periodically run with
that synchronization process

[10:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=612s) to bring updated images down into ECR.

[10:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=615s) They can there be scanned,

[10:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=617s) and they can sit next
to the infrastructure

[10:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=618s) that you need to pull.

[10:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=619s) So this improves security,

[10:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=621s) and it also improves image pull times

[10:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=623s) to help your applications start faster.

[10:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=627s) And like everything else,
it is available right now.

[10:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=631s) And because of the work we've done on ECR

[10:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=633s) and its footprint, Amazon ECR now has

[10:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=636s) over 2 billion image
pulls every single day.

[10:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=639s) And this is because
it's used with every way

[10:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=641s) that customers run containers,
including on Kubernetes.

[10:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=645s) Okay, so that's some of our innovations

[10:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=647s) and things that we've done on
the container registry side.

[10:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=650s) Let's go ahead and talk a little bit

[10:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=651s) about the Kubernetes control plane.

[10:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=653s) So one of the biggest challenges
that customers have faced

[10:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=657s) with Kubernetes, is keeping
the control plane up to date.

[11:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=660s) And on Amazon EKS, there
was a point in time

[11:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=663s) where our performance on
keeping the control plane up

[11:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=665s) to date, was honestly,
a little bit abysmal.

[11:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=668s) So our high watermark for this
was 243 days behind upstream.

[11:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=672s) And we've invested heavily
over the last two years

[11:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=674s) in automation that has led us move

[11:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=677s) from qualifying new
Kubernetes versions in weeks,

[11:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=680s) down to qualifying new versions in days.

[11:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=682s) And so in 2023, we put this
automation into practice

[11:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=686s) and we launched four
versions of Amazon EKS

[11:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=689s) in order to keep up to date.

[11:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=691s) And so now we've slowed that down.

[11:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=693s) We're now launching three versions a year,

[11:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=695s) which is in pace with the
Kubernetes upstream release cycle.

[11:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=698s) And we've had a consistent performance

[11:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=700s) of about 40 to 35 days behind upstream.

[11:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=704s) I don't think we're gonna
go much faster than this.

[11:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=706s) There may be a time, but we typically wait

[11:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=708s) for a new minor version of
Kubernetes to stabilize,

[11:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=711s) typically to a .1 release
before we pull that down

[11:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=715s) and make it a part of Amazon EKS.

[11:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=717s) But honestly, I think next
year I may not show this graph

[12:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=720s) because it's getting extremely boring,

[12:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=722s) and that's the way that we like it.

[12:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=724s) But as we've accelerated,
as we've brought in images

[12:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=727s) and versions much faster into Amazon EKS,

[12:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=731s) our customers have faced another problem,

[12:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=733s) which is getting onto those
latest versions, right?

[12:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=736s) So upgrading Kubernetes
can be a really big pain.

[12:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=740s) And so what our customers
told us last year

[12:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=742s) was that, look, it takes
us a little bit longer

[12:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=744s) than 14 months, which is the
typical version release process

[12:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=748s) in order to move to a new
version of Kubernetes.

[12:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=750s) And so we listened to
that customer feedback

[12:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=752s) and we introduced
Extended Version Support.

[12:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=754s) Extended Version Support for Amazon EKS

[12:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=756s) gives you an additional 12 months

[12:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=758s) of full support for AWS for
any Kubernetes minor version.

[12:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=762s) So what happens after 14 months

[12:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=764s) in the community release cycle

[12:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=766s) is that all support for that
version goes outta date.

[12:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=769s) So the documentation is
removed from the website,

[12:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=772s) the downloadable binaries are removed,

[12:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=775s) bug tickets, bugs are not
just not worked on anymore,

[12:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=779s) they're no longer accepted.

[13:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=780s) And so effectively this version
is wiped out from existence,

[13:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=783s) but on Amazon EKS, we've
invested in order to keep

[13:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=786s) that running for an additional 12 months.

[13:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=788s) So our teams will look at
new versions of Kubernetes

[13:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=791s) and new CVEs that come down.

[13:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=793s) We'll cherry pick appropriate patches

[13:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=795s) and we'll patch all of the
systems running old versions

[13:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=797s) of Kubernetes to keep them secure

[13:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=799s) so that you can continue operating

[13:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=801s) while you plan your move
to the next version.

[13:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=804s) And so what's really nice
about Extended Version Support

[13:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=806s) is that you choose when and
how much you want to use this.

[13:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=809s) You can run into Extended Version Support

[13:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=812s) on any minor version.

[13:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=814s) You can upgrade back to
Standard Support at any time.

[13:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=817s) You don't need to choose special versions

[13:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=819s) of Kubernetes to hop between,

[13:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=821s) you don't have to plan a strategy.

[13:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=823s) You can adjust when you upgrade based

[13:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=825s) on your business priorities.

[13:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=826s) Also, at the same time,

[13:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=828s) many customers were finding themselves

[13:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=830s) running Extended Version
Support and saying,

[13:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=832s) wait, this is a dev cluster.

[13:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=835s) I actually don't care if you
guys upgrade it automatically.

[13:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=837s) Can I make sure that this always

[13:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=838s) just stays on Standard Support?

[14:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=840s) And so a few months ago we
announced upgrade policies

[14:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=843s) and upgrade policies
keep the control plane

[14:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=846s) automatically updated
on standard versions.

[14:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=848s) So you can set an upgrade policy
on any Kubernetes cluster,

[14:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=851s) any EKS cluster, and
when you set that policy,

[14:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=854s) we'll always keep that
control plane updated

[14:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=856s) on the latest standard
version of Kubernetes.

[14:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=858s) So this is a great solution
for dev and test clusters,

[14:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=862s) or even canary staging clusters

[14:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=864s) where you wanna see what the
impact of that upgrade is,

[14:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=866s) and you never wanna worry about

[14:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=867s) that falling into an
Extended Support mode.

[14:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=871s) And that is available now.

[14:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=874s) So having more time to
upgrade is part of the story,

[14:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=879s) but also having more
confidence when you upgrade

[14:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=881s) is the other part of the story

[14:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=882s) for Kubernetes versions, right?

[14:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=883s) And so our customers
wanted to be able to see

[14:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=886s) what's gonna happen when
I upgrade this version?

[14:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=888s) And so we introduced
Upgrade Insights last year,

[14:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=891s) and Upgrade Insights effectively

[14:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=893s) is a report card for your cluster.

[14:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=895s) We run this continuously,
we give you 30 days of data,

[14:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=899s) and we're looking at what API calls

[15:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=901s) are coming into the API server,

[15:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=903s) and we're looking at
all the future versions

[15:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=905s) of Kubernetes that you're not running.

[15:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=907s) So unfortunately, I did not
sort my list by version here,

[15:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=910s) but you can see that I'm
running a 1.25 cluster

[15:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=913s) in this example.

[15:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=915s) And Upgrade Insights is
testing the API server

[15:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=918s) and the calls that are
being made against it

[15:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=920s) all the way up through version 1.32.

[15:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=922s) So if I wanted to skip multiple versions,

[15:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=924s) I can actually say, hey, I
want to go to 1.26 or 1.27,

[15:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=929s) I can check my report card
against those versions

[15:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=931s) and see if things are passing or failing.

[15:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=934s) And what that looks like,
is I get a high level view,

[15:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=938s) but then I can go directly in and say,

[15:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=940s) okay, where am I getting that error?

[15:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=942s) What's gonna fail out if I upgraded

[15:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=944s) this control plane right now?

[15:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=945s) And so in this case,

[15:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=946s) I'm using a v1 beta 1 pod
disruption budget call,

[15:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=950s) and in 1.25 that's replaced
with a v1 pod disruption budget.

[15:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=954s) So if I upgraded this cluster
from 1.24 to 1.25 right now,

[15:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=959s) I could expect that Kub State Metrics,

[16:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=961s) and this is actually my
application, I named it "App",

[16:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=964s) I know that that's not
very creative (laughs),

[16:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=967s) but you can see that Kube State Metrics

[16:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=969s) and App are the two things here

[16:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=971s) that are making that API call.

[16:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=972s) And so those are the things
that I need to go and fix

[16:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=975s) before I upgrade my cluster.

[16:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=976s) And so what we really like
about Upgrade Insights

[16:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=979s) is that it allows us to
get down into the details

[16:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=981s) and allows your teams
to understand precisely

[16:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=984s) what's going on on the
cluster before you upgrade,

[16:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=986s) to give you more confidence

[16:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=988s) and to prevent failures during an upgrade.

[16:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=992s) And like everything else,
this is available right now.

[16:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=994s) This is inside of every EKS console.

[16:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=996s) If you pop open the console,

[16:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=998s) you'll find this in the
observability dashboard.

[16:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1000s) And it's running on
every cluster by default.

[16:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1002s) There's no cost to this, by the way.

[16:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1003s) This is just available
for every single cluster.

[16:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1008s) So obviously observability
is extremely useful

[16:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1011s) when we're upgrading,
but observability is also

[16:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1013s) a really important part
of operating a system

[16:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1015s) like Kubernetes every single day.

[16:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1017s) And one of the things that
our customers always have

[17:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1020s) to do is to configure
observability on their clusters.

[17:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1022s) And so this year we wanted
to make that a lot easier

[17:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1025s) and we introduced enhanced
control plane observability.

[17:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1029s) So this came out a few months ago,

[17:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1031s) and what we did is we
added two major things.

[17:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1034s) First, we added additional metrics

[17:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1036s) for the cluster, Kube Controller Manager,

[17:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1038s) and Kube Scheduler Metrics.

[17:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1040s) And you can scrape these
in new Prometheus endpoints

[17:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1042s) and export them to any
observability system.

[17:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1045s) We also added new
pre-configured dashboards

[17:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1048s) in the EKS console that
gives cluster administrators

[17:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1051s) visual representation
of these key metrics,

[17:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1054s) and that lets you rapidly assess,

[17:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1056s) is your control plane healthy?

[17:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1057s) Is it performing the way
that we expect it to perform?

[17:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1061s) And so, these are really nice.

[17:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1063s) You can see right here,

[17:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1064s) they're prebuilt, they're in CloudWatch.

[17:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1066s) You can deep dive into
any of these dashboards.

[17:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1069s) And as part of this,

[17:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1070s) we built this whole new
observability suite inside of EKS.

[17:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1072s) And you can see my Cluster Insights tab

[17:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1075s) is off to the right there.

[17:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1076s) It's a little bit small.

[17:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1078s) And we have the metrics, but we also,

[18:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1080s) this is my favorite part,
we deeply integrated

[18:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1082s) with CloudWatch Log Insights.

[18:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1084s) So CloudWatch Log Insights has
been around for a long time,

[18:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1087s) exporting CloudWatch logs, logs from EKS

[18:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1090s) to CloudWatch has also been
around for a long time,

[18:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1093s) but this is something that you had to go

[18:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1094s) and you had to figure
out and run yourself.

[18:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1096s) Now in the EKS dashboard,

[18:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1098s) you have pre-configured log queries

[18:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1100s) and you just press the button, Run Query,

[18:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1103s) and you're gonna see a
list of the log query

[18:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1107s) for certain common things

[18:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1109s) that you may wanna look at on the cluster.

[18:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1110s) So one of my favorites
here is Top Talkers.

[18:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1112s) What this means is what are
the services on the cluster

[18:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1116s) that are the most chatty
with the API server?

[18:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1118s) So this is a great log
query to run for example,

[18:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1121s) if you're seeing some
weird behavior anomalies

[18:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1124s) in the API server, maybe
things aren't performing up

[18:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1126s) to your expectations,
you're seeing that metric,

[18:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1128s) you can go in and run
the Top Talkers query

[18:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1131s) and you can say, hey, you know,
it looks like what is this?

[18:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1134s) My v1 beta 1 ingresses,

[18:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1136s) has made 1700 calls against the API server

[19:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1140s) in the last 30 minutes,
so maybe I need to go look

[19:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1142s) at some of these things,
I may see a spike here

[19:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1144s) and I can get right down
into the root problem.

[19:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1147s) So these dashboards are not meant

[19:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1148s) to replace deeper observability tools,

[19:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1151s) but they're meant to be a starting point

[19:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1152s) for observability and
quick troubleshooting

[19:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1154s) when you're doing cluster administration.

[19:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1158s) And available now.

[19:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1160s) Going a step deeper,
CloudWatch actually has done

[19:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1163s) a huge amount of improvements
over the last year

[19:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1165s) to make it easier for container
customers to use CloudWatch.

[19:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1168s) So we now have Container Insights

[19:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1171s) with enhanced observability
for Amazon EKS.

[19:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1174s) So we put a subset of this
stuff in the EKS console

[19:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1177s) that's available out of the box.

[19:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1178s) And then clicking into CloudWatch,

[19:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1180s) you actually have deeper
performance overviews

[19:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1183s) that can look across one or more clusters.

[19:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1185s) It can give you alarms,
utilization statuses,

[19:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1188s) it gives you data that allows you

[19:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1190s) to take more proactive action
against the performance

[19:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1192s) of your clusters and your
cluster applications.

[19:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1195s) And it gives you metrics and
visibility into cluster health.

[19:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1198s) We recently added GPU Neuron
and Windows Support as well

[20:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1202s) to these Container Insights.

[20:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1203s) This is a really nice feature.

[20:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1205s) I've been super impressed with the work

[20:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1206s) that the CloudWatch team has done,

[20:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1208s) and this is available now with
CloudWatch and Amazon EKS.

[20:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1213s) This week at ReInvent,

[20:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1214s) we actually did a really cool thing

[20:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1216s) for network traffic as
well with CloudWatch.

[20:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1218s) So we've had VPC flow logs for a long time

[20:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1222s) with CloudWatch VPC,

[20:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1224s) and CloudWatch just announced
Network Flow Monitor

[20:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1226s) a few days ago.

[20:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1227s) So this is a really cool new feature

[20:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1229s) that gives you visibility
into the performance

[20:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1231s) of the network traffic,

[20:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1232s) between the boxes in the AWS data center.

[20:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1235s) So a lot of times you may experience,

[20:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1237s) if you're running it especially at scale,

[20:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1239s) customers have problems

[20:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1240s) where they may see network degradations

[20:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1242s) or they're trying to
troubleshoot networking issues,

[20:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1245s) and what CloudWatch
Network Flow Monitor does

[20:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1247s) is it allows you to see exact data

[20:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1250s) and places in the network path

[20:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1252s) where you could see
performance degradations.

[20:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1254s) Amazon EKS is integrated

[20:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1256s) with Network Flow Monitor out of the box.

[20:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1258s) We automatically annotate
the metadata that's traveling

[21:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1261s) between the EC2 instances
inside of the cluster.

[21:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1264s) So when you go into CloudWatch
Network Flow Monitor,

[21:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1266s) you can understand the state
of that network traffic

[21:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1269s) that's bound by the cluster,

[21:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1271s) and whether that's communication
between cluster nodes

[21:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1273s) or in and outta the cluster,

[21:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1275s) and it's more easy to troubleshoot
performance degradations

[21:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1277s) on the network layer.

[21:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1280s) And like everything right
now, it's available right now.

[21:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1283s) This is a new launch at ReInvent.

[21:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1285s) We're really, really excited about it.

[21:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1287s) One of the other things that we built

[21:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1289s) for observability with our customers

[21:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1291s) has been Split Cost Allocation Data.

[21:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1293s) And so one of the biggest issues

[21:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1295s) when you move to Kubernetes,

[21:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1296s) if anyone's ever operated
in a VM world, right?

[21:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1299s) We did these monolithic applications

[21:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1301s) and you would do one application per VM,

[21:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1304s) you would have really nice tagging,

[21:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1306s) you'd get these beautiful
costs and usage dashboards,

[21:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1308s) as an administrator,
you're running everything,

[21:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1310s) it works really nicely,
as a finops administrator

[21:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1313s) you get these really nice reports,

[21:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1315s) and then one day the team says,
we're moving to Kubernetes.

[21:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1317s) And you move to Kubernetes
and everything becomes

[21:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1319s) a black box on the financial side, right?

[22:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1322s) Because you have these shared clusters

[22:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1323s) and multi-tenant microservices,

[22:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1324s) and how do you understand
the exact cost of things?

[22:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1327s) So there have been
tools including Kubecost

[22:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1330s) that we've supported running

[22:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1331s) with Amazon EKS for a number of years.

[22:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1333s) But our customers told us they wanted

[22:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1335s) this natively available in Amazon EKS.

[22:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1337s) And so we partnered with
the AWS Cost and Usage team

[22:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1340s) to introduce Split, (sneezes) excuse me,

[22:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1344s) to introduce Split Cost Allocation Data.

[22:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1346s) And what this does is
that we have a managed way

[22:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1349s) that we are automatically collecting data

[22:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1351s) for pod utilization on the cluster.

[22:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1353s) We're putting that together
with your actual cost

[22:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1356s) of running EC2 on the backend,
and we're building a new cost

[22:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1360s) and usage report that gives
you fine-grained reporting.

[22:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1362s) And this reporting can break
down against the pod level,

[22:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1365s) against the deployment
level, the job level,

[22:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1368s) namespaces and clusters.

[22:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1370s) We automatically ingest
those true EC2 costs

[22:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1373s) and we give you this native report

[22:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1374s) to help you understand the actual cost

[22:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1376s) of your applications.

[22:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1379s) Cool.

[23:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1381s) So, that's a lot on observability.

[23:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1384s) The other thing that
we've done with add-ons,

[23:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1387s) is when you run a cluster, right,

[23:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1389s) just running the control
plane is not enough.

[23:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1391s) You often need to bring
all these different types

[23:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1394s) of operational tools into Amazon EKS.

[23:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1396s) And a few years ago we launched add-ons,

[23:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1398s) which helps you create clusters

[23:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1400s) that have batteries included.

[23:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1402s) And we've expanded the catalog

[23:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1404s) of add-ons over the last year.

[23:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1406s) We've added five or four new add-ons

[23:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1408s) that are first party from Amazon EKS,

[23:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1411s) including CloudWatch Container Insights,

[23:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1413s) CSI Snapshot Controller,
the Pod Identity Agent

[23:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1416s) and the Node Monitoring Agent.

[23:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1417s) We've also enabled you to launch clusters

[23:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1420s) without the core networking add-ons.

[23:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1422s) Some customers told us that
they wanted to launch clusters,

[23:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1424s) for example, without VPC CNI,

[23:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1426s) so now you can configure
that at cluster launch

[23:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1429s) in the add-ons API.

[23:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1431s) And we've also launched over
40 marketplace add-ons to date.

[23:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1435s) So we have the first party
add-ons that are coming from AWS,

[23:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1438s) and then we've added a
marketplace integration

[24:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1440s) where you can actually take

[24:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1442s) more than 40 marketplace add-ons,

[24:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1444s) you can choose which ones you
wanna run in your clusters,

[24:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1447s) and with a single click, you can subscribe

[24:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1448s) and launch those into
your Amazon EKS clusters.

[24:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1450s) So made it really easy to
get tools like Datadog,

[24:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1454s) Kubecost, New Relic, Splunk, et cetera,

[24:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1456s) into your clusters with a single click.

[24:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1462s) And when you install those
add-ons on the cluster,

[24:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1465s) customers asked us to
make them more secure,

[24:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1467s) and to improve the security posture

[24:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1469s) of their clusters in general.

[24:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1470s) So last year at ReInvent, we talked a lot

[24:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1472s) about pod identity, which allows you

[24:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1474s) to assign IEM roles down to specific pods.

[24:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1477s) This year we took pod identity

[24:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1479s) and we integrated it with EKS add-ons.

[24:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1481s) So now in a single click,
when you set that add-on up,

[24:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1484s) you can create and associate
a specific IEM role

[24:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1487s) with that add-on, so that
everything on the cluster

[24:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1489s) has a reduced scope of security

[24:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1491s) and improved security blast radius.

[24:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1495s) And it's available now.

[24:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1497s) On the security side, we've
been continuously investing

[25:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1501s) in security for EKS.

[25:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1502s) So pod identity, bringing
pod identity to add-ons,

[25:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1506s) we've had encryption at the cluster level

[25:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1508s) for secrets for a number of years.

[25:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1510s) You've been able to bring a KMS key to EKS

[25:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1512s) and encrypt your secrets.

[25:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1514s) We thought that that was good,
but it wasn't good enough.

[25:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1516s) And so starting this year,
we now encrypt everything

[25:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1520s) on the cluster with KMS v2 keys

[25:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1522s) that we provide by default.

[25:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1524s) And we don't just encrypt secrets,

[25:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1526s) we encrypt every single object now.

[25:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1528s) You can still bring your own CMK as well

[25:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1530s) to encrypt on top of our KMS v2,

[25:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1532s) but by default now everything
in Amazon EKS clusters

[25:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1535s) is fully encrypted.

[25:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1540s) In addition to encryption
and security controls,

[25:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1542s) we've also improved our access
controls for Kubernetes.

[25:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1545s) So Cedar is a new open source language

[25:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1548s) that was built by AWS,

[25:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1550s) and this is a language that allows you

[25:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1552s) to write more expressive
and explicit policies

[25:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1556s) for access control.

[25:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1558s) And recently at KubeCon, we
announced expanding Cedar

[26:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1562s) to Amazon EKS and Kubernetes.

[26:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1563s) So using Cedar allows you to have features

[26:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1566s) and functionality that are not
available in Kubernetes RBAC

[26:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1569s) like denials, conditions and attribute

[26:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1572s) and label based access controls.

[26:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1574s) And so we're really excited about Cedar,

[26:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1575s) it's a new open source
project that we're doing

[26:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1577s) to bring Cedar and EKS together,

[26:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1579s) and we think this will
be a really nice upgrade

[26:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1581s) for customers to allow
better access control

[26:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1584s) in and out of clusters.

[26:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1587s) Additionally, on the networking side,

[26:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1590s) one of the biggest
pushes from AWS is IPv6.

[26:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1593s) I know you're seeing a lot of IPv6 talk,

[26:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1595s) I think we've been talking about IPv6

[26:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1597s) for the last 20 years at least.

[26:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1600s) And one of the things that
EKS has done this year

[26:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1602s) is we've now checked the box

[26:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1603s) on everything related to IPv6.

[26:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1605s) So we've previously had single
stack pods and IPv6 clusters.

[26:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1610s) We've had IPv6 management APIs.

[26:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1613s) And now as of a few months ago,

[26:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1614s) we now have IPv6 cluster endpoints.

[26:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1617s) So if you have an IPv6 strategy

[26:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1618s) and you're moving to
IPv6, you can adopt EKS

[27:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1621s) and know that you have full IPv6 support

[27:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1623s) in every part of the cluster.

[27:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1626s) Additionally, on the networking
side, we've integrated

[27:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1629s) with Amazon Application
Recovery Controller.

[27:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1632s) So Route 53 launched
Application Recovery Controller

[27:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1635s) last year, and what this allows you to do

[27:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1637s) is to have a highly resilient setup

[27:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1640s) where you can automatically shift traffic

[27:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1643s) between AZs in the event of
a gray or a black AZ failure.

[27:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1648s) So these could be failures
that we automatically detect

[27:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1651s) and we shift traffic for you,

[27:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1652s) or you can press this big
red emergency stop button

[27:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1655s) at any time and shift traffic over.

[27:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1658s) And so ARC is managed by Route
53, so it's managed centrally

[27:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1662s) and a number of other AWS
services have integrated with ARC.

[27:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1665s) And this allows us to safely shift traffic

[27:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1667s) away and back to the AZ.

[27:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1669s) So one of the things that
happens in an AZ gray failure,

[27:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1672s) right, is we'll have one
component that could fail

[27:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1674s) and could cause a performance degradation.

[27:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1676s) And so then a lot of traffic
may evacuate outta the AZ,

[27:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1679s) and that's fine, we'll go
and people get woken up,

[28:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1682s) people get on calls, we
start to fix that issue.

[28:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1684s) But as the AZ begins to recover,
something that we often see

[28:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1688s) is what we call a thundering herd

[28:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1689s) where everybody says,
oh, the AZ's recovering,

[28:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1691s) let me shove all my traffic back into it.

[28:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1694s) And usually during that AZ recovery phase

[28:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1696s) is where things can be
a little bit delicate.

[28:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1698s) And if you slam that AZ
with traffic right away,

[28:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1701s) then you can have additional degradations

[28:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1703s) and additional failovers.

[28:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1704s) So very small problems can
cascade into very long problems,

[28:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1708s) and short outages can
cascade into longer outages.

[28:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1710s) So Amazon Application Recovery Controller,

[28:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1714s) it doesn't just help you evacuate traffic

[28:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1716s) and keep your applications running

[28:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1718s) when you have an AZ outage issue,

[28:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1720s) it also helps us slowly shift
your traffic back into the AZ

[28:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1724s) so that that AZ doesn't fall over again

[28:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1726s) and we can fully recover from
the incident a lot faster.

[28:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1730s) And also available now.

[28:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1733s) Part of our integration with AWS,

[28:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1736s) we talked about integrations with AWS

[28:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1738s) is allowing customers to have
full access to the cloud.

[29:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1742s) And so our AWS controllers for Kubernetes

[29:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1745s) is a project that we've been building

[29:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1746s) over the last few years,

[29:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1748s) that allows you to have
cloud native control

[29:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1750s) and define AWS resources
directly from the Kubernetes API.

[29:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1754s) Over the last year, we've
launched 20 new services in GA.

[29:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1758s) We've rebuilt the pipelines
to rapidly build services out

[29:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1761s) of Amazon SDKs, and we now
think that this is something

[29:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1764s) that we're seeing more
and more customers use

[29:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1767s) in order to manage their AWS resources

[29:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1769s) alongside their Kubernetes resources.

[29:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1771s) But as ACK has become more popular

[29:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1773s) and we've had more service coverage,

[29:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1775s) we've had customers tell us that, hey,

[29:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1778s) it's really hard to orchestrate
all these things together

[29:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1780s) because I may not just want a
single S3 bucket, for example,

[29:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1784s) I may want a suite of
different capabilities.

[29:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1787s) And so we've recently introduced
the Kube Resource Operator

[29:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1790s) or KRO, and KRO allows you

[29:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1792s) to actually abstract multiple
Kubernetes resources together

[29:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1796s) and write abstractions and
publish them to clusters

[29:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1799s) using Common Expression Language or CEL.

[30:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1802s) And this is a really
simple YAML based language

[30:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1804s) that lets you define a set of AWS

[30:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1806s) and Kube resources together,

[30:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1808s) and then publish that as an
abstraction to the cluster

[30:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1811s) and program against that
abstraction using a CRD.

[30:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1814s) So for example, you can define

[30:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1816s) what a Kubernetes deployment looks like

[30:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1818s) or what a web service
looks like at your company,

[30:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1821s) and you can put that into the cluster

[30:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1822s) as a controller using KRO,

[30:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1824s) and then have your development
teams program against it.

[30:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1826s) It's a really exciting project

[30:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1828s) that's now available on GitHub and Alpha.

[30:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1830s) We plan to develop this more
and more over the next year.

[30:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1834s) Okay, so one thing about
AWS is that we are global.

[30:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1839s) And a big announcement from EKS is

[30:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1840s) that we are now covered in
every single global region,

[30:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1844s) and we have a presence in
every single geographic reason,

[30:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1848s) availability zone, and local zone.

[30:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1850s) And so one of the things that
our customers we found is

[30:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1853s) that they're running in
all these different modes.

[30:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1855s) They're running from
Amazon EKS in the region,

[30:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1857s) down to the local zone,
down to the outpost,

[31:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1860s) down to EKS anywhere.

[31:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1864s) And one of the things
that we are really excited

[31:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1866s) to announce this week at ReInvent

[31:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1867s) is Amazon EKS Hybrid Nodes.

[31:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1870s) So our customers were running Amazon EKS,

[31:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1872s) anywhere in the data center,

[31:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1874s) and they told us that
they wanted something

[31:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1876s) that was a little bit more managed.

[31:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1877s) And so with Amazon EKS Hybrid Nodes,

[31:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1879s) you can now use your existing on-premises

[31:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1882s) or Edge Compute to connect that back

[31:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1884s) to an Amazon EKS control plane
that's running in the region

[31:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1888s) and manage everything consistently.

[31:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1890s) So you can extend that control plane

[31:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1892s) out to the data center and
out to your Edge compute

[31:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1894s) and manage it in a consistent environment.

[31:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1897s) And all the higher level
integrations from AWS,

[31:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1899s) from observability to add-ons

[31:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1901s) work seamlessly with Hybrid Nodes.

[31:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1903s) And so the architecture
looks a little bit like this.

[31:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1906s) I have my CLI tool, I
can install this manually

[31:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1909s) or scripted across all
my on-premises nodes.

[31:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1911s) And when that CLI is installed,
there's a small little agent

[31:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1914s) that runs and the agent
bootstraps the Kubelet

[31:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1917s) and other components onto that node

[31:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1919s) and connects it up to
the Amazon EKS cluster.

[32:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1922s) And so then in the cloud, that
node shows up in the console

[32:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1925s) and also in the API server,
just like any other instance.

[32:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1930s) You can see its attributes

[32:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1931s) and you can start to
schedule workloads onto it.

[32:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1935s) So we think Hybrid Nodes
is gonna be heavily adopted

[32:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1938s) for people in enterprise
modernization, machine learning,

[32:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1941s) financial services, media streaming,

[32:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1943s) manufacturing, IT apps, all
sorts of different places.

[32:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1946s) And we're really, really excited about

[32:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1948s) how Hybrid Nodes is being used.

[32:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1951s) And we've been talking
to customers all week

[32:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1953s) about their plans to adopt Hybrid Nodes.

[32:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1956s) But obviously we also
have the cloud, right?

[32:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1958s) And one of the best parts
of AWS is the breadth

[32:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1961s) and the depth of compute
options, that are offered at AWS.

[32:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1965s) And one of the things that
we wanted to do for customers

[32:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1968s) was to make it easier to
go from create cluster

[32:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1971s) to run application.

[32:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1972s) And so this week we're really excited

[32:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1974s) to announce the launch of EKS Auto Mode.

[32:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1977s) Auto Mode is a major evolution for how

[32:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1979s) to run production ready
Kubernetes in the cloud.

[33:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1982s) And it's also a fulfillment
of our vision for

[33:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1984s) how Kubernetes should
operate in the cloud.

[33:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1986s) So with Auto Mode,

[33:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1987s) you can provision
application ready clusters,

[33:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1990s) pre-configured with all the
capabilities that you need

[33:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1993s) and best practice from AWS.

[33:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1995s) Auto Mode reduces the time that it takes

[33:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=1997s) to launch new workloads,
allowing you to get new products

[33:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2000s) or modernize applications
into production faster.

[33:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2003s) And so, typically what
we'd see with customers

[33:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2007s) when they were using
Kubernetes before Auto Mode,

[33:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2009s) is they would choose how
to create the cluster,

[33:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2012s) for example, using infrastructure as code,

[33:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2014s) and then they would,
consider the type of compute

[33:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2017s) that they needed to
run their applications.

[33:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2019s) Do they want to use EC2 or Fargate?

[33:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2022s) What instance types should be used?

[33:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2023s) Then they'd think about
cluster capabilities,

[33:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2026s) and then they'd have a number
of plugins and all this stuff,

[33:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2028s) and they'd have to
provision all these things

[33:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2029s) and wire these things together.

[33:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2031s) With Auto Mode, all of
that is managed for you.

[33:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2034s) So you get the managed control plane.

[33:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2036s) When you put a cluster into Auto Mode,

[33:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2038s) we automatically provision
and manage the capabilities

[34:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2041s) within the cluster for compute,
networking and storage.

[34:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2044s) We have EC2 managed
instances, which are secured

[34:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2048s) and automatically managed instances

[34:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2050s) that run in your account,

[34:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2051s) and we automatically provision everything

[34:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2055s) that's needed in order to run the cluster.

[34:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2057s) So we automatically provision instances

[34:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2059s) and we optimize instances,

[34:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2061s) and keep everything updated
and healthy for you.

[34:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2063s) And with Auto Mode, this
means that we can now

[34:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2065s) have one click cluster creation

[34:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2068s) in the Amazon EKS console and CLIs,

[34:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2071s) and you can easily get started

[34:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2073s) with a single click in the console.

[34:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2075s) And like everything else,
this is available today.

[34:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2078s) Really cool feature that
was launched as part

[34:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2080s) of Auto Mode, is EKS Node
Health and Auto Repair,

[34:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2083s) where we're automatically
looking at the health of nodes,

[34:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2085s) especially GPU instances,

[34:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2087s) and we're repairing
them and improving them.

[34:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2090s) And this is something that's
available now with Auto Mode

[34:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2093s) and we'll be looking to
expand health and auto repair

[34:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2095s) to other functionalities in the future.

[34:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2099s) Cool.

[35:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2100s) So Auto Mode is generally available now,

[35:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2102s) encourage you to check it out.

[35:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2105s) So, one of the things that EKS
has been heavily adopted for

[35:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2109s) is machine learning,

[35:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2110s) from large language
foundational model training,

[35:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2113s) robotics development, and
AI inference at scale,

[35:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2116s) we've seen a lot of
customers use Amazon EKS.

[35:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2119s) And we've been investing
in infrastructure features

[35:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2121s) which simplify and accelerate
machine learning with EKS.

[35:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2124s) So things from node health and auto repair

[35:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2127s) to a set of accelerated AMIs,

[35:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2130s) we are part of the recently
announced EC2 Ultra Servers.

[35:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2133s) EC2 Ultra Servers works
natively with Amazon EKS,

[35:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2136s) and also integrating deeply
with capacity block reservations

[35:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2139s) for compute availability.

[35:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2141s) We've been investing in our integrations

[35:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2144s) for data management with
the S3 Mountpoint CSI Driver

[35:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2147s) and the EFA Kubernetes device plugins

[35:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2150s) for using elastic fabric
adapter networking

[35:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2152s) for GPU instances.

[35:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2154s) We've also been helping

[35:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2155s) to streamline Kubernetes' machine learning

[35:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2157s) by investing in native
OSS frameworks like Ray,

[36:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2160s) and also bringing
accelerated instant support

[36:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2163s) to Container Insights.

[36:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2164s) So I'm really happy to talk more

[36:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2167s) and more about machine learning on EKS,

[36:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2169s) as we see this grow a lot more,

[36:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2171s) and to go deeper into how
they're using machine learning,

[36:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2174s) I'd like to welcome
Hyungtae Kim to the stage,

[36:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2176s) principal software engineer at Snowflake.

[36:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2179s) (audience applauds)

[36:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2181s) - Yeah, thank you.

[36:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2185s) Hello everyone.

[36:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2186s) I'm Hyungtae Kim.

[36:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2187s) I'm one of the engineering
leads for AI app platforms

[36:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2189s) and infrastructure at Snowflake.

[36:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2191s) Today I'm excited to share with you

[36:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2193s) how we are powering AI
innovation at scale.

[36:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2195s) You might be familiar with
our products like Cortex AI,

[36:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2198s) which enables generative AI
capabilities for our customers,

[36:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2202s) but what you may not be familiar with

[36:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2204s) is the infrastructure story behind it all,

[36:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2206s) specifically how we leverage
Kubernetes on top of EKS

[36:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2209s) to build a robust foundation
for these AI services.

[36:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2212s) In this section, I'll share our journey,

[36:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2214s) the challenges that we
face, and the solutions

[36:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2216s) that we implemented, while
building this infrastructure.

[37:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2221s) Let me introduce you to Cortex AI,

[37:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2223s) Snowflake's comprehensive Gen AI platform.

[37:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2225s) What makes Cortex special is this ability

[37:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2227s) to handle the full
spectrum of AI workloads,

[37:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2230s) all powered by Kubernetes
and on AWS powered by EKS.

[37:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2235s) On the inference side, we've built systems

[37:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2237s) that can scale from zero to thousands

[37:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2238s) of concurrent requests.

[37:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2240s) Whether you're running
massive batch operations

[37:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2242s) through familiar SQL interfaces,

[37:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2245s) or powering real-time chat applications

[37:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2247s) with sub-second latency requirements,

[37:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2249s) our infrastructure adapts seamlessly.

[37:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2251s) With our training infrastructure,

[37:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2253s) we're not just running
models, we're building them.

[37:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2256s) Our Arctic family of foundational models

[37:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2258s) represents a significant investment

[37:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2259s) in AI capabilities by requiring.

[37:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2264s) We have models for enterprise use cases

[37:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2267s) from search to document understanding,

[37:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2268s) all requiring intensive
computational resources

[37:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2271s) that EKS helps us manage efficiently.

[37:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2273s) Beyond foundational models,

[37:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2275s) we support sophisticated
fine tuning frameworks.

[37:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2278s) This supports everything from
full parameter fine tuning

[38:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2280s) to more efficient approaches like LoRa,

[38:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2282s) enabling our customers
to customize their models

[38:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2285s) for their specific needs

[38:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2286s) while maintaining
performance and reliability.

[38:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2290s) I'll share some of the real challenges

[38:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2292s) we faced building Cortex

[38:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2293s) because they'll probably
resonate with many of you.

[38:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2295s) We encountered two major
themes that forced us

[38:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2298s) to rethink our traditional
infrastructure approach,

[38:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2301s) capacity management and system fragility.

[38:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2304s) First there's capacity.

[38:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2306s) We all know that GPUs
are scarce and expensive,

[38:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2308s) especially high-end training
hardware like NVIDIA H100s,

[38:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2312s) but what might surprise you is

[38:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2314s) how does scarcity fundamentally
change our operations?

[38:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2317s) Take cluster upgrades for example,

[38:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2320s) the traditional blue-green
deployment approach

[38:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2322s) would require us to temporarily
double our GPU capacity.

[38:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2325s) Imagine spinning up hundreds
of P5s just for an upgrade.

[38:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2329s) It's not just cost prohibitive,

[38:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2330s) is often impossible due
to supply constraints.

[38:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2334s) This forced us to innovate.

[38:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2335s) We had to develop new patterns
for managing capacity,

[38:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2338s) moving away from the just scale up mindset

[39:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2340s) that worked so well for CPU resources,

[39:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2343s) but the more interesting
challenge is fragility.

[39:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2346s) AI workloads, especially
distributed training,

[39:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2348s) have a unique all or
nothing characteristic.

[39:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2351s) Imagine coordinating a
distributed training job

[39:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2353s) across thousands of GPUs,

[39:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2355s) and if just one GPU fails,
the entire job is compromised.

[39:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2359s) Further exacerbating the problem,

[39:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2361s) GPUs and their specialized
networking infrastructure

[39:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2364s) have a higher failure rate
than traditional hardware.

[39:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2371s) And here's the architecture
that powers Cortex.

[39:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2374s) We call this our AI cluster,

[39:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2375s) and it's designed to solve

[39:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2376s) those challenges I just described.

[39:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2378s) The fundamental idea is simple,
one cluster, one region,

[39:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2382s) all AI workloads, but
what makes it powerful

[39:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2384s) is how it intelligently manages resources

[39:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2386s) across different workload types,

[39:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2388s) from real-time inference to
large scale training jobs.

[39:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2391s) Let me walk you through the key components

[39:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2393s) that make this possible.

[39:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2395s) We've organized them
into two main categories,

[39:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2397s) capacity management and resilience.

[40:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2400s) For capacity management,

[40:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2401s) we built a custom capacity controller

[40:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2403s) that access the brains of
our resource allocation.

[40:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2405s) Think of it as an intelligent
traffic controller

[40:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2408s) that knows which resource takes priority.

[40:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2410s) For example, if a
real-time inference service

[40:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2412s) needs more resources,

[40:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2414s) it can intelligently preempt
lower priority training jobs.

[40:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2417s) We paired this with the Volcano Scheduler,

[40:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2419s) an open source scheduler
that handles gain scheduling,

[40:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2422s) which is crucial for coordinating
distributed training jobs.

[40:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2425s) On the resilience side, we
developed three key components.

[40:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2428s) First is our node health service.

[40:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2431s) Think of it as a proactive
diagnostic system.

[40:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2433s) It runs intensive burden validation

[40:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2435s) to ensure all the nodes are healthy.

[40:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2437s) Second, we have a pod janitor.

[40:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2440s) This might sound simple,

[40:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2442s) but Kubernetes can get quite unhappy

[40:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2444s) if we frequently terminate
workloads on top of nodes

[40:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2448s) and it ensures clean termination

[40:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2449s) and intelligent resubmission of pods.

[40:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2452s) Lastly, we have the Invariant Enforcer.

[40:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2455s) It enforces many properties

[40:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2457s) of the cluster like network discovery

[40:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2459s) and distribute training capabilities.

[41:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2464s) Next, we'll dive into one of
our most crucial components,

[41:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2467s) the capacity controller.

[41:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2468s) Think of it as a brain that
orchestrates our GPU resources

[41:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2471s) across different workload types.

[41:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2473s) What you're seeing on screen
is an actual capacity bucket

[41:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2476s) definition for our Cortex
inference workloads.

[41:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2479s) Let me break down why this is interesting.

[41:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2481s) Notice how it is marked as high priority.

[41:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2484s) This means when these inference
services need resources,

[41:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2486s) they get them first.

[41:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2488s) The real magic happens in

[41:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2489s) how we structure these capacity buckets.

[41:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2491s) Each workload type, whether
it's real-time inference,

[41:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2494s) batch processing, or model training,

[41:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2497s) gets its own bucket with clear boundaries.

[41:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2499s) In this example, you can
see we specified both P5

[41:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2502s) and P4 instance types, with
a minimum of three nodes

[41:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2505s) and shared service stability

[41:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2507s) and room to scale up to
200 nodes when needed.

[41:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2510s) What makes the system
powerful is this ability

[41:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2512s) to move nodes between
buckets intelligently.

[41:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2515s) Think of it as a dynamic resource pools

[41:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2516s) that can ship based on demand,

[41:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2518s) but we can't just grab those randomly

[42:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2520s) when we're dealing with
distributed training jobs

[42:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2523s) that might be using hundreds of GPUs,

[42:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2525s) we need to be surgical about
which nodes to take and when.

[42:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2531s) And next, let's talk
about how we handle one

[42:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2533s) of the trickiest challenges
in AI infrastructure,

[42:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2536s) hardware reliability.

[42:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2538s) GPUs are incredibly powerful,

[42:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2540s) but they're sensitive pieces of hardware

[42:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2542s) that can develop issues over time.

[42:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2544s) Our node health service
is our automated guardian

[42:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2546s) that ensures every GPU on our
fleet is performing optimally.

[42:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2549s) Looking at the diagram,
you can see the lifecycle

[42:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2552s) of a node in our system.

[42:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2553s) When a new node joins our cluster,

[42:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2555s) it starts in what we call
the probation period.

[42:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2558s) It's there, but we won't
let it run workloads yet.

[42:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2561s) We put this set nodes in probation

[42:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2563s) through a comprehensive health check,

[42:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2564s) that includes four critical areas, GPUs,

[42:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2567s) networking, storage, and performance.

[42:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2571s) What makes the system
particularly clever is

[42:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2573s) how it handles multi-node scenarios.

[42:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2575s) When something goes wrong
in a distributed work node,

[42:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2578s) finding the problematic
node can be quite difficult,

[43:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2581s) and you need to take
a systematic approach.

[43:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2583s) We use pairwise testing to
isolate problematic nodes.

[43:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2586s) And if a node fails this test,

[43:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2588s) it is automatically
terminated through AWS APIs.

[43:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2591s) If it succeeds, it joins active fleet.

[43:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2596s) Post validation, if
any subsequent workload

[43:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2599s) reports a potential failure,

[43:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2600s) it is put back into validation.

[43:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2605s) Next, let me share how EKS has accelerated

[43:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2608s) our AI infrastructure.

[43:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2609s) Instead of getting bogged down

[43:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2610s) in the low level
complexities, we've been able

[43:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2612s) to focus on what really matters,

[43:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2614s) building innovative AI solutions.

[43:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2617s) First is performance.

[43:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2619s) Through close collaboration with AWS,

[43:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2621s) we've been able to
optimize the performance

[43:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2624s) of the elastic fiber adapter networking,

[43:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2626s) which is crucial for distributed training.

[43:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2628s) The out of box
compatibility of the systems

[43:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2631s) is also valuable.

[43:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2632s) The accelerated AMIs come
with compatible drivers

[43:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2634s) for both GPUs and networking.

[43:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2636s) The accelerated AMIs are also
compatible out of the box

[44:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2640s) with the latest NVIDIA PyTorch images.

[44:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2644s) Storage is also another area

[44:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2646s) where EKS has simplified our operations.

[44:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2649s) We've implemented a tiered approach.

[44:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2651s) We use FSx for Lustre

[44:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2652s) to provide high performance
distributed storage

[44:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2655s) for model checkpoints and training data.

[44:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2658s) EBS and EFS provides other
persistent similarities

[44:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2662s) and S3 serves as a reliable
archive for data and models.

[44:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2666s) This flexibility allows
us to optimize performance

[44:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2669s) and cost for each specific use case.

[44:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2672s) Last is in scalability and operations.

[44:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2674s) Remember when GPU capacity challenges

[44:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2676s) that I mentioned earlier?

[44:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2678s) With AWS, we don't need to worry

[44:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2680s) about maintaining our
own performance buffer

[44:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2682s) because they handle no
remediation automatically.

[44:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2686s) And for lower tier hardware, like 8 Tons,

[44:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2688s) we can rely on the auto
scaling capabilities of EKS

[44:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2691s) to manage those workloads.

[44:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2696s) Coming full circle to the
two critical challenges,

[44:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2698s) we started with, capacity
management and system fragility,

[45:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2701s) our Snowflake AI cluster has transformed

[45:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2703s) these challenges into strengths.

[45:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2705s) Remember when I mentioned

[45:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2706s) how AI workloads don't typically play well

[45:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2708s) with traditional Kubernetes patterns?

[45:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2710s) Well, we changed that story.

[45:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2712s) In our online inference service
now can scale dynamically

[45:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2715s) with demand, just like any
other Kubernetes workload.

[45:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2718s) This is possible because
our capacity controller

[45:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2720s) intelligently borrows resources

[45:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2722s) from lower priority workloads when needed.

[45:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2725s) We've also solved the thorny
problem of cluster upgrades.

[45:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2729s) Instead of needing to double
our expensive GPU capacity

[45:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2732s) for blue-green deployments,

[45:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2734s) we can now orchestrate
upgrades by priority.

[45:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2736s) We start with training workloads,

[45:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2738s) then smoothly transition

[45:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2739s) our latency sensitive inference services,

[45:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2742s) maximizing uptime while
minimizing resource requirements.

[45:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2746s) And the fragility challenge,
our no health service

[45:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2748s) has dramatically reduced the
impact of hardware failures.

[45:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2751s) When issues occur, and they still do

[45:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2753s) with high performance hardware,

[45:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2755s) they're automatically detected

[45:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2756s) and migrated behind the scenes.

[46:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2761s) And before I hand it back to Nate,

[46:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2762s) let me share some of the
lessons from our AI journey

[46:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2765s) building this infrastructure.

[46:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2767s) These are the lessons I wish

[46:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2769s) someone had told me when we started.

[46:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2771s) First, embrace the impermeance
in your workload design.

[46:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2775s) We learn sometimes the hard
way that treating disruptions

[46:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2778s) as a feature, rather than a bug,

[46:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2781s) leads to more resilient systems

[46:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2783s) by keeping state and Kubernetes small

[46:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2787s) and moving, offloading them

[46:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2788s) to other features like
Ephemeral Vault, like S3,

[46:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2792s) we can handle no failures
in capacity gracefully.

[46:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2796s) It's about optimizing for
recovery, then preventing failure.

[46:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2800s) Second, be strategic
about hardware management.

[46:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2803s) Those GPU nodes are expensive.

[46:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2805s) And when you find a set of
good ones, hold onto them,

[46:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2808s) especially if you're on reservations.

[46:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2811s) We save countless debugging hours

[46:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2813s) by implementing rigorous
validation on node acquisition.

[46:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2816s) Think of it as quality control
for your infrastructure.

[46:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2819s) Third, automation isn't
optional, it's essential.

[47:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2823s) Kubernetes can get into interesting states

[47:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2825s) when you're frequently
terminating instances

[47:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2827s) with active workloads.

[47:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2828s) We build automated systems to monitor

[47:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2830s) and remediate these issues,

[47:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2832s) handling everything from stuck pods

[47:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2834s) to cache synchronization problems.

[47:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2838s) And lastly, here's a practical tip

[47:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2840s) that saves us at least
one cluster rebuild,

[47:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2843s) plan your network
infrastructure generously.

[47:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2845s) The H 100 nodes consume a lot of IPs.

[47:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2849s) We're on our eighth
iteration of our AI cluster

[47:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2851s) in just 18 months.

[47:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2856s) And every iteration we've learned
something new about scale.

[47:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2865s) And the key lesson here is we've learned

[47:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2868s) to treat our AI infrastructure

[47:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2870s) like a living, breathing system.

[47:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2871s) We need to constantly evolve,

[47:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2875s) and look out for potential issues

[47:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2878s) and be ready to fix that every time.

[48:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2880s) And with that, I'll hand it back to Nate.

[48:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2883s) (audience applauds)

[48:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2887s) - Thanks Hyungtae.

[48:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2890s) That was great.

[48:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2891s) What Hyungtae and the team
at Snowflake have done

[48:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2893s) is really, really impressive.

[48:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2895s) Using EKS they've accelerated
the progress of Snowflake.

[48:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2898s) They've taken a core system and evolved it

[48:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2901s) into one of the best in class AI training

[48:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2905s) and inference systems in the world.

[48:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2906s) And they've helped their
customers manage data

[48:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2908s) at scale all the much better.

[48:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2910s) So, I wanna spend the next
few minutes that we have here

[48:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2914s) talking about the future of Amazon EKS.

[48:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2918s) So this is something
that we see across AWS,

[48:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2922s) with sophisticated customers
that have engineering teams

[48:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2925s) that are dedicated to
solving the hardest problems

[48:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2928s) in distributed systems
and machine learning.

[48:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2931s) And these technology companies,

[48:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2934s) these pure technology companies,

[48:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2935s) have a mission to solve
these hard problems.

[48:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2938s) But we also have customers who need

[49:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2940s) to solve similar problems,

[49:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2942s) but they have a very
different focus, right?

[49:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2944s) Using Kubernetes to innovate on behalf

[49:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2946s) of their core businesses
for their customers.

[49:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2948s) And this is a side effect

[49:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2949s) of all these companies
becoming technology companies,

[49:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2952s) advanced systems like AWS and Kubernetes,

[49:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2956s) they can be engines for success
across your organization.

[49:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2959s) But at the same time,
if your mission is not

[49:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2961s) to build these systems,
but to solve problems

[49:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2963s) that are not technology problems,

[49:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2966s) it can be really difficult
to use these systems.

[49:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2968s) And it's not that companies

[49:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2970s) that are not pure technology companies

[49:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2972s) are not smart people, it's just
they have a different focus.

[49:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2975s) And so at a tech conference like ReInvent,

[49:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2978s) it can seem like everybody
here is a technology company

[49:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2980s) and this is what we're building for.

[49:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2982s) But the reality is that
most companies in the world

[49:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2986s) are not software technology companies.

[49:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2988s) And most people are solving
other hard problems,

[49:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2991s) and they want to take advantage
of this software technology.

[49:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2994s) And so that leaves us with a problem

[49:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2996s) because while we think that every company

[49:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=2998s) should use advanced technologies
to further their mission,

[50:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3001s) lower costs and accelerate innovation,

[50:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3003s) most companies shouldn't have

[50:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3005s) to become pure software
technology companies

[50:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3007s) to get these benefits.

[50:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3009s) They should be able to
leverage the tools built

[50:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3011s) by dedicated tech companies

[50:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3013s) and software communities to
accelerate their innovation,

[50:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3015s) lower cost, and improve
the quality of goods

[50:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3018s) and services that they
produce for society.

[50:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3021s) And so, the reason we all
love conferences like ReInvent

[50:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3024s) is because they give a
glimpse into the future,

[50:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3026s) the hope that you can have
this amazing new thing

[50:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3028s) that's here right now,

[50:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3030s) and it's finally actually
available to use.

[50:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3033s) And this is our second problem, right?

[50:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3034s) Systems like Kubernetes
we see as the future,

[50:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3037s) but they can be hard to use.

[50:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3039s) They require dedicated effort

[50:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3040s) and expertise to install and operate.

[50:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3043s) And then finally, in the cloud,

[50:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3047s) running these things can require a lot

[50:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3049s) of this time and expertise.

[50:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3051s) And if you're using open
source technologies,

[50:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3053s) sometimes even more so,

[50:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3054s) so building and properly leveraging OSS

[50:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3057s) can sometimes mean that you need people

[50:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3059s) who understand how to build
and leverage that OSS,

[51:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3062s) and really quickly they can go from, hey,

[51:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3064s) I found a really cool
tool that we can install

[51:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3066s) and use at our company, to,

[51:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3068s) we're now a maintainer of that tool.

[51:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3070s) And now, oh, we're a primary
maintainer of that tool.

[51:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3072s) And now we own that tool,

[51:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3073s) and we never intended to own that tool

[51:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3075s) because that's not our business focus.

[51:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3077s) And look, I don't want to say,

[51:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3078s) discourage people in any way

[51:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3081s) from using open source technology.

[51:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3083s) In fact, I think open source technology

[51:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3085s) is an amazing innovation.

[51:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3087s) Like the idea of open
source software in general,

[51:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3089s) and that I think that
all companies like AWS

[51:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3092s) and our customers should
be contributing to OSS,

[51:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3095s) but a problem that can happen is

[51:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3096s) that at scale, OSS can become expensive.

[51:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3099s) And so this is something that
we want to help customers with

[51:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3102s) and make it a little bit easier.

[51:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3104s) And so this is a balance, right?

[51:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3105s) How do you keep control

[51:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3107s) and flexibility all the
way from start to scale?

[51:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3109s) How do you balance this trilema of systems

[51:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3112s) where you want to have scale and control,

[51:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3114s) you wanna have speeds of
changes and have scale?

[51:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3117s) We see this trilema is
often you can pick two

[52:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3120s) out of these three things.

[52:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3123s) And we wanna optimize for customers

[52:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3125s) at all of these levels, right?

[52:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3127s) And so our mission with
EKS is to help kind

[52:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3130s) of grow this triangle a little bit bigger.

[52:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3132s) You'll still have to make
trade-offs and choices,

[52:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3134s) but we wanna make it a
little bit more optimized

[52:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3137s) and make those trade-offs a
little bit less painful, right?

[52:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3140s) And so that's the goal that we have,

[52:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3142s) is to go faster and
farther together with you.

[52:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3144s) And our strength in AWS is secure,

[52:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3147s) resilient, and scalable operations.

[52:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3148s) Whether you're a software
technology company

[52:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3151s) or you're in the majority of companies

[52:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3152s) that do something extremely important,

[52:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3155s) our mission is to help
accelerate your time to value

[52:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3157s) with complex tools that don't require you

[52:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3159s) to become an expert,
democratize innovation from AWS,

[52:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3163s) our partners in the community,

[52:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3165s) and lower the cost of entry turning CapEx

[52:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3168s) into OpEx for all aspects of the stack.

[52:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3171s) So a few years ago I showed a slide

[52:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3173s) that looked really similar to this, right?

[52:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3175s) This is our journey of Amazon EKS.

[52:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3177s) We started from a hosted control plane,

[53:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3181s) then we introduced managed data planes

[53:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3182s) and with Auto Mode, right?

[53:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3184s) We're making that even more managed now.

[53:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3186s) And then also managed operational tools,

[53:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3188s) also a part of Auto Mode.

[53:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3191s) And while that mission has not changed

[53:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3193s) and the overall strategy
of EKS has not changed,

[53:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3196s) we found that the needs

[53:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3197s) of our customers have evolved, right?

[53:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3200s) You are all divinely unsatisfied.

[53:22](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3202s) So let's zoom out a little bit,

[53:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3205s) and there's a lot more
going on here, right?

[53:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3207s) Like as we showed in the beginning,

[53:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3209s) Kubernetes is a lot more than the cluster.

[53:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3211s) So first of all,

[53:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3212s) most folks don't just run
a single cluster anymore.

[53:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3215s) They run a lot of clusters.

[53:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3216s) People I speak to run
at least five, maybe 10,

[53:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3220s) sometimes thousands, across
hundreds of accounts.

[53:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3223s) And they want to knit them
those clusters together

[53:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3225s) into a platform with
centralized management,

[53:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3228s) observability, governance, access control,

[53:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3230s) secrets management and deployments.

[53:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3232s) And they wanna wrap that all
up in a beautiful package

[53:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3234s) with templates, codified best practices,

[53:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3237s) documentation, run books,

[53:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3239s) everything that their developers

[54:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3240s) and their data scientists
need to deploy applications

[54:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3244s) to the exact places that they run best.

[54:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3246s) Whether that's across a
fleet of accelerated TRN2

[54:09](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3249s) or NVIDIA GPU instances in the cloud,

[54:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3251s) thousands of Edge locations,

[54:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3253s) or they wanna manage all
of that seamlessly, right?

[54:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3255s) They wanna manage that
seamlessly with the help of AWS.

[54:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3258s) And so this is a little bit of a preview

[54:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3260s) into where we're thinking is that

[54:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3261s) this year we have integrated Hybrid,

[54:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3263s) how do we start to bring in more

[54:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3265s) of those platform components?

[54:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3266s) How do we bring in an integrated
development experience?

[54:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3269s) And so these are our investment priorities

[54:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3271s) for the next few years, right?

[54:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3272s) And this is exactly
what we're going to do.

[54:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3274s) We're gonna provide optimized experiences

[54:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3276s) for critical workload
patterns at any scale.

[54:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3279s) We're gonna deepen AWS integrations

[54:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3281s) and tooling for management and efficiency.

[54:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3283s) And our goal is, as we do
this, to meet your workloads

[54:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3286s) where they are, whether
those are in the cloud,

[54:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3288s) across multiple regions, in local zones,

[54:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3290s) on-premises in data
centers, or at the Edge.

[54:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3293s) We also wanna simplify platform building.

[54:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3295s) We want to make it easy to
have a production grade,

[54:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3298s) Kubernetes based platform on AWS.

[55:01](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3301s) And finally to accelerate the flywheel

[55:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3303s) of innovation in the community, right?

[55:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3305s) Open source is the engine that
powers so much of what we do,

[55:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3308s) and we wanna make sure
that we are able to power

[55:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3310s) that innovation, to have
new innovation be developed,

[55:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3313s) to be a part of that, and
then also to bring that

[55:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3315s) to customers so that they
consume it really easily

[55:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3318s) without having to become deep experts

[55:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3320s) in every single component
that they wanna run.

[55:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3323s) And so for customers,

[55:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3324s) we weren't gonna automate more things

[55:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3326s) in and around the cluster,

[55:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3328s) natively bring you the
latest AWS innovations

[55:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3330s) through Kubernetes, and
ensure compatibility with

[55:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3333s) and support for community projects,

[55:35](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3335s) which make this Kubernetes
innovative and powerful.

[55:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3339s) And for partners, because
we have so many partners

[55:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3341s) that are either here
today or watching this,

[55:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3344s) we wanna make it easier for you

[55:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3345s) to build on EKS for your
products and services.

[55:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3348s) We want to give you simple paths

[55:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3350s) that allow you to enable EKS customers

[55:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3352s) and to sell alongside
AWS to those customers,

[55:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3355s) and provide ongoing guidance, support,

[55:58](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3358s) and ideas to improve your
products in our partnership.

[56:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3362s) So, this is a hard talk to give, right?

[56:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3366s) Because it's the future,

[56:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3367s) and it's hard to give a lot of detail

[56:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3370s) about what we're doing, but also know

[56:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3372s) that we're always thinking deeply

[56:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3373s) about what we should do next.

[56:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3375s) So it's a balance between
how much do we share

[56:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3377s) and how much do we hold back

[56:18](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3378s) knowing that it might change.

[56:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3380s) Why would it change, right?

[56:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3381s) It would change because our roadmap

[56:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3384s) and our plans are completely based on

[56:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3386s) what we hear from our customers, right?

[56:28](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3388s) We build everything based
on customer feedback.

[56:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3391s) If we don't have good data,
that customers really want

[56:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3394s) what we're building and
we find it valuable,

[56:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3396s) we simply won't build it.

[56:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3397s) And as we start to build things,

[56:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3399s) we talk to our customers about it, right?

[56:40](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3400s) We experiment.

[56:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3401s) And if our customers don't
find it valuable, we change it.

[56:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3404s) We stop it and we go build
the thing that our customers

[56:47](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3407s) are asking us to build.

[56:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3408s) So we spent the whole front half

[56:50](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3410s) of this presentation talking

[56:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3411s) about all the new stuff that came out.

[56:53](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3413s) Every single one of those has been driven

[56:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3414s) by our customer asks.

[56:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3416s) And for every slide that I showed,

[56:57](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3417s) there's five other slides
that never made the cut

[56:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3419s) because they're projects that
we considered and never built,

[57:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3422s) 'cause as we talked to
customers about them,

[57:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3424s) we found that maybe they
just weren't that useful,

[57:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3426s) and we shouldn't go ahead and build them.

[57:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3428s) And so, what this boils down to

[57:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3430s) is that to understand the future of EKS,

[57:12](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3432s) you have to know that you are
as big a part of the story

[57:15](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3435s) as we are, and we're gonna
keep doing more things

[57:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3437s) that make it easier to make Kubernetes

[57:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3439s) a standard part of your stack.

[57:21](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3441s) And Kubernetes turned
10 years old this year

[57:23](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3443s) and 10 years from now, our mission is

[57:25](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3445s) to make Kubernetes disappear.

[57:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3447s) And so where are the
receipts on this, right?

[57:30](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3450s) Well, we have our
containers public roadmap.

[57:33](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3453s) And this is a place where we push things

[57:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3456s) and we post things that
we're thinking about

[57:38](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3458s) or working on, where you can
come and you can submit ideas

[57:41](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3461s) and converse directly with the team.

[57:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3463s) I went and counted this up

[57:44](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3464s) 'cause I didn't wanna
put the slide up here

[57:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3465s) and talk about this amazing thing and say,

[57:48](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3468s) well, yeah, but no one ever uses it,

[57:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3469s) to date, we've shipped over 400 EKS items

[57:52](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3472s) on the roadmap since
we started it in 2018.

[57:55](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3475s) And over 850 total items
that have hit this roadmap

[57:59](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3479s) have been shipped across all
of our container services.

[58:02](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3482s) So we encourage you to
visit this regularly.

[58:04](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3484s) You can see what other people are saying.

[58:06](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3486s) You can upvote, you can comment on things

[58:08](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3488s) that you'd like to see
or submit your own ideas

[58:11](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3491s) if you think we can do something better.

[58:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3493s) So EKS issues are on here,
they're tagged as EKS,

[58:16](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3496s) but you'll also see issues

[58:17](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3497s) for other container services as we visit.

[58:19](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3499s) And we encourage you to submit ideas

[58:20](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3500s) and join the conversation there as well.

[58:24](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3504s) If you wanna learn more about Amazon EKS,

[58:26](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3506s) we have a number of great resources

[58:27](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3507s) that the team has developed.

[58:29](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3509s) We have the EKS Best Practices Guide,

[58:31](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3511s) which was recently updated

[58:32](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3512s) with best practices for machine learning.

[58:34](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3514s) We also have the EKS workshop.

[58:36](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3516s) You may have been able to attend

[58:37](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3517s) an EKS workshop here at ReInvent.

[58:39](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3519s) The EKS workshop is our master home

[58:42](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3522s) for all of these workshops and events.

[58:43](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3523s) So if you weren't able

[58:45](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3525s) to make a workshop session at ReInvent,

[58:46](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3526s) I highly encourage you and
your team to check this out.

[58:49](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3529s) And then we have EKS blueprints,

[58:51](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3531s) which is a set of best
practice codified examples

[58:54](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3534s) for how you can deploy complete clusters,

[58:56](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3536s) and now even platforms using Amazon EKS.

[59:00](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3540s) And we have blueprints in both Terraform

[59:03](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3543s) and the AWS CDK.

[59:05](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3545s) So really appreciate
everybody coming today.

[59:07](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3547s) And thank you for spending
some time to learn about

[59:10](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3550s) what we're doing with EKS
from myself and Hyungtae.

[59:13](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3553s) Thank you.

[59:14](https://www.youtube.com/watch?v=_wwu0VKy3w4&t=3554s) (audience applauds)

