# AWS re:Invent 2024 - Amazon EKS as data platform for analytics (KUB405)

[Video Link](https://www.youtube.com/watch?v=AAwa5gc1XNA)

## Description

As running analytics workloads on Amazon EKS continues to rise, data engineers need self-service tools to create infrastructure for running analytics jobs. This session offers practical insights into how leading organizations are modernizing their data platforms, transitioning from traditional infrastructure as code pipelines to infrastructure as Kubernetes APIs. Using open source technologies like AWS Controllers for Kubernetes (ACK), data platform teams can help data engineers create on-demand namespaces and clusters fully equipped to run analytics jobs, thereby streamlining their workflow.

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

- All right. Welcome, my name is Roland Barcia. I'm the worldwide director for our specialist technology team. I have the honor to be presenting
with much smarter people, Christina and Victor. They will introduce themselves
when they start speaking for the interest of time. So let's get going, 'cause we have a lot of
material to get through. This is a 400-level session,
so we wanna go deep very fast. I'm gonna kick it off, and
kind of set some context before I hand it off to Christina. And we're gonna talk a little
bit about data to start. Obviously, in a conference,
where we're talking a lot about generative AI, LLMs, Bedrock, et cetera, data has become probably
one of the key commodities that we have. And there's lots of it, lots
of different data formats, lots of different users
or personas of data. It's no longer just analysts anymore. Its developers use data,
end users use data, internal folks use data, and people need to make
decisions fast and quickly. And so when we talk about data, we wanna think about personas, because we're at AWS,
we're customer-obsessed, and we gotta think about data from a perspective of who uses it. And so we're gonna get a little bit deeper into things like data processing
with Spark as an example. But we want to think about
things like your external users. So you have data that you expose as part of your business to your users. Oftentimes you have
historical data, batch data, things that people look
at monthly, weekly, that have a known pattern. And more and more, we have
a need to make decisions real-time with data. This is probably where we see a lot of generative AI use, right? Where people are using prompt engineering and things to do ad hoc queries, ad hoc answers to questions,
and things like that. Internally, we have personas
that wanna make use of data to make decisions about
anything and everything from how do I run a
system more efficiently? How do I scale it better? What are some security
audits that I'm seeing? And observability tools
kind of help out there. And then we have to process
lots and lots of data, right? So we're gonna get into things like Spark, and it's cluster technology, and things like Hadoop in the past. And then emerging technologies like Flink that have kind of brought
together, you know, how do I process streaming data, as well as batch data together
to make these decisions. And so let's talk a little bit
about platform engineering. A lot of our customers have
standardized on Kubernetes. They use EKS, Elastic Kubernetes Service. Some great announcements this week in other sessions in the track, like Auto Mode and things like that. But oftentimes when you are a startup, maybe you have just a development team and you do platform engineering as part of that development team. But over time, as you grow, the emergence of platform engineering has come about with Kubernetes. And a lot of those concerns really focused in the first generation
around web applications, microservices, event-driven architectures. And this emergence, I always call it a
little bit of a collision between personas and goals, right? Where developers wanted freedom, they want to use their
favorite open-source tools, their technologies, they want autonomy. I wanna build a new
app, I wanna deploy it, I wanna get it out quickly. And then you have platform teams that are worried about things
like the security systems, scalability, cost, performance. And so the first generation
of these, you know, platform teams are really
thinking about web applications, microservices, transactional systems. And platform engineering
has really emerged as a way to kind of meet in the middle between providing this autonomy and still automating things like standards in a developer-like way. There's lots of talks on
overall platform engineering. I have one on Thursday
in the serverless track from the developer persona point of view, the users of the platform. And so you can come to that
session when I get into it. But when we're talking
about platform engineering, one of the things that
customers often struggles, where is that line between the developers and the people that use the
platform, and the platform team? Do I vend out clusters? Do I vend out code as a service? Do I make it easy for developers
to just check in code? And so these are the
first generation problems. It's all been solved, right? But probably not. There's still probably lots of debate here on where the line stands, and that's because of the workloads. And so we get now into the
age of data and lots of data, and data scientists and engineers have started building
things with Notebooks, using SQL data processing. They're building stateful applications. They're building
applications with streaming and events workflows. They're using Notebooks
with Python or R to build applications and Notebooks
that are doing generative AI, or ML, or any type of data processing. They're building data
lakes and data meshes, and applications that sit in front of them to kind of federate the data. And the platform team all of a sudden has to worry about things like, what's the optimal storage to use? Do I give them GPUs? We have cool Inferentia2 and Trainium2 announced this morning that we kind of heard
about as well, right? And so, and we have new
types of DevOps, MLOps, data pipelines, the lifecycle of an LLM, the lifecycle of MyData. So these are now new concerns
in this next generation. And so I'm not gonna go into
all of these in exhaust, but there's a lot of goals
for platform engineering and data workloads, right? So how do I get the right
resources, developers? I wanna get the right
type of machine type, the right type of GPUs,
the right storage type for their workloads, for their Notebook, for their data processing. They want the right security,
the right isolation. They don't want a data
job running over here to interfere with a
transactional system over there. And I wanna do it at the
best price point possible. And of course, just like
developers, data scientists, data engineers are very
opinionated about their favorite, you know, PyTorch framework, TensorFlow, all the different types
of frameworks out there for doing data applications. And so how do I support that autonomy with this new generation of applications that are very data intensive? Lots of different challenges
with stateful workloads, right? We're talking about
things like how do I use thousands of nodes or
even the opposite problem, really large images that
take a while to start up to warm up the data. And some of the things in Kubernetes, we're really optimizing
the first generation to spin up compute very fast and detect if there's a
failure of every pass, and kill the pod, bring up a new pod. And sometimes these data workloads need to do things like check mark or checkpoint where they
are in data processing. They have these new concerns
with stateful applications. Sometimes the scalers are too fast, there's different network configurations. Do models have gravity? Does data have gravity? Even people are finding in some cases that data is cheaper to
move closer to the compute. And so you know, there is all
fluctuation of these patterns, and platform teams have to adjust to that. And so these are some of
the challenges we'll see, Christina and Victor are gonna
go into real world examples of how they implemented this. Just very quickly. You know, there's different
options for folks. By all means you can do Spark, EMR in a serverless way
using serverless paradigm if you are doing things
more native to AWS, and you get some default
services, lots of advantages. A lot of our customers choose
Kubernetes to standardize. We have one of the best
Kubernetes services out there in EKS, and there's
different ways to run Spark, because of the ecosystem you have. You can use an operator
run Spark on your own. We of course have Amazon
EMR that runs on EKS as well as an option to
give you kind of the best of both world between
management and flexibility, and the best open-source frameworks. So Kubernetes and data, right? When we talk about it, there's lots of different
patterns early on, started with storage and
custom resource definitions, moved on to event-based
applications with Kafka that gives you events,
event streaming, messaging. Then we get to spark with
the architecture moving from this type Hadoop workloads in memory intensive parallel processing. Then we get into Apache
Flink, which is like, I need both real-time data
and I need batch data, and I need to do processing
across them both, we get into I need GPUs and other types of specialized
hardware to run intensive, maybe training models et cetera. And specialized schedulers
in supporting things like Notebook as a service. So we have an evolution
of Kubernetes for data. We have a project, you take
a picture really quickly, data on EKS. If you can come to us afterwards, lots of different blueprints
and best practices to help you provision different patterns, like running Spark on EKS,
or running Flink on EKS, or running Kafka on EKS. So we have different types of scripts that kind of help you get started. And on the last point,
and we talk about data, there's really a life cycle. So we talked about the support that a data platform needs to have. So for example, how does the
data get into your environment, into your system ingest? And you need to support
different types of tools, Kafka-based things. You can do managed
services like Amazon MSK or run Kafka and Kubernetes. We have native options
like Kinesis, et cetera. And then we have workflow tools that kind of help stage the data, whether it be things like
Step Function, or Airflow, or Argo Workflows,
different batch schedulers to have some instances come
up and more stateful patterns, and we already talked
about data processing. Then we get into the data processing tier, and we get into things
like batch scheduling, doing kind of all the
processing you need overnight. And then you wanna get your
data out and consume it. You might do some transformations, might do some SQL against it,
different catalog the data, and make the data available as an API. So this is the lifecycle of the data. And so with that I'm gonna
now, we're gonna go deeper, I'm gonna hand it to Christina. Christina, gave you a minute back. - Thank you, Roland. Hi, everyone. Next I'm gonna cover three
things that you can do. So you can optimize your
analytics platform on Kubernetes for growth. So you're set to bring in
analytics workloads fast into AWS, as well as grow into different regions. My name is Christina Andonov,
I am a solutions architect, and I help you, our customers, building analytics
platforms on Kubernetes. And as Roland mentioned, one reason that you might
be here in this room is that you're already running
your business applications on Kubernetes. You feel comfortable using it, scaling it, and now the analytics
workloads are coming in. So when we engage with
customers like that, this is where we usually find them, having two separate teams,
building two separate platforms centered around the same compute. And the reason for that is not
that much the compute itself as it is the traffic
pattern of the workload that lends on that compute. See for business application, the traffic pattern is much
like the weather in California. For the most part, you get
highs of 80s, lows of 60s, and with minor exceptions,
it is very predictable. The traffic pattern for
the analytics workloads, well, that's more like the
weather in the Caribbean during the hurricane season. And when that flood of jobs
arrives at your clusters, that data platform team's
responsibility is to make sure that these clusters can scale
in a very short period of time so they can ingest the jobs are optimized, so they can process the jobs fast and can do all that cost efficiently. So next, let's go over some best practices of what you can do to
optimize these clusters. And when I mentioned best practices, because I'm assuming
you're already running your business applications on Kubernetes, I'll just go over the
delta of best practices between your business platform
and your data platform. We're gonna build a cluster with best practices from the ground up. We're gonna split the build
in three logical layers where layer one will be building a vanilla yet production-ready cluster
optimized for analytics. Layer two will be installing
various open-source tools to make that cluster
purpose-built cluster. And layer three will be
onboarding your tenants on that cluster. And actually before you
even create the cluster, you have to set up the networking to make sure the network will
scale and you have enough IPs, because you might have
heard that with IPv4, IP exhaustion is a thing,
and your natural inclination might be to use an overlay network. But overlay network will inevitably add a little bit of latency, which is counterproductive to
what we wanna achieve here. So instead of an overlay network, what you can do is use this special range of non-routable IPs. And in this case, in this example, two CIDR blocks that will give you 130 IPs to use for the nodes and the pods. Here is where I usually get the question, but how about IPv6? And yes, yes, IPv6 will make
all of our exhaustion problems go away eventually. Kubernetes supports IPv6
since two years ago. Spark supports IPv6 since last
year, version 3.4 or later. But chances are something,
somewhere along your stack, or that your cluster talks to, might not yet be supporting IPv6. So it's definitely an option, but if you choose to use
it, please test it truly. Either way you go about here, I'll consider you have enough IPs, and then we can proceed
with creating the cluster, and start to put the
add-ons onto the cluster. The first add-on that
goes in is the VPC CNI. And the VPC CNI comes
with this default setting, WARM_ENI_TARGET=1. What does that even mean? Well what it means is that
when instances come up, they have an ENI, and that ENI holds a set of pre-warmed IPs. One of those IPs goes to the worker node, and then a spot comes up, they get assigned IPs
from those pre-warmed IPs. Now if that instance
were to be a c5.2xlarge, that ENI will hold 15 IPs. But for analytics, we tend
to use much larger instances, such as c5.18xlarge, and that
instance comes with two ENIs, and they hold 50 IPs each. That is 100 IPs. Well for analytics, our pods
tend to be larger as well, which means you are not gonna schedule nearly as 100 pods on this instance, and all these IPs, most
of them will go wasted. And that pool of 130 we just
said, that might not be enough. So what you can do here is set
MAX_ENI to 1 for the VPC CNI. And then the second
option here, maxPods: 30. That is setting on the cubelet, you can set it to a static number like 30, or you can check our data
and it has blueprints. We have different patterns
where we set that option automatically based on
how large the instances for different flavors of Linux. Last thing for the VPC CNI, VPC
CNI tends to be very chatty, and who it likes to talk to,
its best friend, the EC2 API. See for each and every of those IPs, usually the VPC CNI makes
a call to the EC2 API. And if you're trying to
bring up one instance, that's not a problem. But if you're trying
to bring 100 instances at a time, well, guess what? You're gonna throttle the API. So what you can do here is set up this enable prefix delegation. What enable prefix delegation does, it packages 16s of those IPs in one query, and it queries the EC2 API, that will reduce the queries
to the EC2 API fold 16. All right, VPC CNI set. Next I have a riddle for you. Do you know why CoreDNS gets
invited to all the parties? 'Cause it resolves everything. Well most of the time. For analytics, usually, CoreDNS
has to scale up proactively as a lot of instances are coming up. And in the past, you had to
use this open-source project called Cluster Proportional Autoscaler in order to scale CoreDNS. And I have good news for you. In May, we announced
many scaling for CoreDNS. That means if you are
on version 1.25 of EKS and CoreDNS 1.9, and you have upgraded one time to those versions
or later since May, this feature is already available for you, and all you have to do is
just set, just enable it, and then CoreDNS will
proactively scale for you. You should also install
open-source project called NodeLocal DNS. NodeLocal DNS is a
DaemonSet that you install, it runs on every single node,
and it caches the queries, so it alleviates the
queries that go to CoreDNS. And one last thing here,
let's talk a little bit about how CoreDNS resolves external domains. If we give it a domain
like s3.amazonaws.com, it will go to its configuration, and there's this setting called ndots:5, it's gonna see ndots:5. And what that means is CoreDNS
will look at that domain, say, oh, this domain has two dots, and two is less than five. So this must be internal
to my cluster domain. So what I'm gonna do is I'm gonna go here and append every single
option in the search line, and that will resolve of
in five unnecessary queries before I go externally and
check where that domain is. One thing you can do here
is, first and foremost, please do not change
ndots of 5 to CoreDNS, but you can set ndots
to 2 on the pods only. What that will do is it's gonna
take a look at the domain, it's gonna say, "Oh, it has two dots, and I'm gonna resolve it right away." It's gonna resolve in one query. And that will alleviate the
pressure on the CoreDNS pods, and that's how CoreDNS can keep
its party celebrity status. Next, for your business applications, we're gonna scale some compute here. So for business applications, you tend to use this open-source project where a lot of our customers tend to use this open-source project
called Cluster Autoscaler. Cluster Autoscaler scales up instances based on CPU and memory. And then what it does,
how it scales instances, it usually takes on average like between two and three minutes
to bring an instance up. We see data platform teams
are the first to switch to another open-source
project called Karpenter. Karpenter came out from
AWS, we open-sourced it, and we donated it to seek
auto-scaling last year. And this year, we graduated it to GA. So now it's V1, it is stable,
you can go ahead and use it. And the difference here
with Karpenter is that one Karpenter is fully
aware of AWS pricing. So not only it's gonna pick an instance that is gonna fit the pod's
memory and CPU speaking, but it's gonna pick the most
cost efficient instance. Also, Karpenter is very
quick on how it scales those instances up much, much quicker. We usually see scaling the instance up in less than a minute. Before we dive into the
Karpenter configuration, let's talk a little bit
about how Spark jobs work. Usually when a data engineer
submits a Spark job, a driver pod comes up, and that driver pod is
responsible for managing the job. That driver pod is responsible
for scheduling the executors, and if any of the
executors get interrupted, the driver pod knows about
it, it schedules another one, and it finishes the job. If the driver pod gets interrupted, the whole job has to start over. What that means for Karpenter is that we can install the driver pod to on-demand instances,
and executors are ideal for our deeply discounted spot capacity. As it comes to Karpenter, you can actually set one NodePool, and provide both capacity
types in the NodePool, and then use either annotations
or labels, or taints, and toleration to land
each workload respectively. Okay, great. Now we set the compute to scale, next on the menu, we have storage. And when I say storage, I
mean Spark shuffle storage. See we have these instance
types with d in the name before the dot. What that d means is that that instance comes with a SSD drive
built-in into the instance. That will be the fastest
storage you get, hands down. So we recommend utilizing that, those instances and that storage. Now some instances come with one, some instances come with
more than one SSD drives. And to take full advantage
of the whole capacity, you should set these drives
to RAID0 using Karpenter. It's as simple instance
source policy RAID0. I don't know if you've used this before, but this used to be a user-data script that does some calculations. So this is awesome. Not only this is awesome, but you don't have to set the host pod for the executors anymore. Executors will have direct
access to that storage. Well you still might wanna
limit how much of that storage they'll use in the Spark
configuration, but that's about it. So for short running
jobs, this is perfect, but for long running jobs, if that instance gets interrupted, well the driver pods know about it, and it's gonna bring other executors up, but now we lost the checkpoints. So these two executors have to start over. So if you have longer running jobs, maybe a better option would
be to use EBS volumes. And in Spark configuration,
we can do that, we can make the driver pod
aware of the EBS volumes with this configuration. And that way if the
instance gets interrupted, another one comes up, the driver pod knows where the EBS volumes are, it attaches them to the new executors, and the new executors take off from where the interrupted ones left off, because they have the
checkpoint data in EBS. Last thing about storage here is that these two options
are not mutually exclusive. You can use, you can provide
both of them to your end users, and they can pick and
choose which one to use depending on the job they're running. As I mentioned, Karpenter
brings instances up very quick. The next thing that needs to happen is that instance has
to download the images and to run the pods. And good rule of thumb here is to have from the
moment I want an instance to the moment I have
my pods up and running is to have that process under a minute. So a few optimizations you can do here. First and foremost, get
those images the closest to your instances as possible. If you are storing them in ECR, make sure they're in the region with cross-regional replication. If you're storing them
in a different repo, we support pull through cache for ECR, use pull through cache,
put them in the region. Set a VPC endpoint, so those images get downloaded
through the network, and we don't have to go out and back in. And if that's not enough, and that's might not be enough
to get it under a minute, if your images are pretty
large, meaning 5 to 10 gigs, what you can do is you
can take large files out of your images such as JAR
files and other libraries. You can store them in S3 express zone 1. And then have the images lean, and when they download, use S3-Mountpoint to mount this S3 bucket as
a drive to your executors. Okay, so now we get it under a minute. And last one, in this first layer, please monitor, set up your monitoring before you put this in production. I know most of you monitor, Spark and the open-source
softwares that you're using, they come with metrics. I want you to monitor three
additional things here. The first thing is please monitor the Kubernetes control plane. We do expose the
Kubernetes control metrics. Check out the EKS best practices guide, and make sure you monitor that. Make sure you monitor the AWS APIs. We do provide in CloudWatch metrics. And as I mentioned earlier,
if you're using VPC CNI, you might throttle the EC2 API. Make sure you have access
to those throttle metrics, out CloudWatch as a data
source to your Grafana, or to your monitoring vendor, and watch those throttle metrics. Same thing for the EBS API. And last one, make sure
you monitor the network. See for example, CoreDNS
is using UDP protocol, which means if your
contract table on the Linux, the connection tracking
table gets filled up, those CoreDNS packages
are gonna get dropped. And you wanna know about it
from the CoreDNS metrics, you need to monitor the network again, EKS best practices guide
for monitoring the network, check it out. And that concludes the first layer. So now we have a cluster that can scale, will be performant enough,
and cost efficient. Next we're gonna add
various open-source software on this cluster to make
it purpose-built cluster. The most common open-source projects that we see customer use are Apache Flink and Apache Spark. Usually the question is, do I put them together
in the same cluster, or do I split them in their own cluster? And the answer to that
is, well, it depends. If you have smaller clusters, or clusters up to let's say 2-300 nodes, yeah, you can run them
on the same cluster. But if your clusters start
growing beyond that point, it will be good to start
thinking about separating them. The rest of the talk will be focused mostly on Apache Spark here. For Apache Spark, we recommend, if you're running the open-source version to use the Spark Operator. Earlier this year, the
maintainers of data on EKS worked with the community and
got the Spark Operator donated to the Kubeflow community. And since then, we have
seen tremendous bug fixes, active maintainers. So use Apache Spark. Another one here that is optional, like see the Kubernetes
scheduler, you can schedule jobs on first in, first out basis. But if you're coming from
like a Hadoop and YARN world, you might want your priority
cues or gang scheduling. And to use that, we recommend using this other open-source project
called Apache YuniKorn that works really well with Spark. And last but not least, you will need some workflow
engine for your jobs. Most common one we see is Apache Airflow. You can install it, and self-manage it, or you can use our managed offerings. We also see a fair
amount of Argo Workflows, even lately, Step Functions
to do the workflow here. And that concludes the second layer. Next, let's talk a little bit about your tenant isolation
strategy before we move on to onboarding your tenants. See, for some customers
use one team per cluster, but we see the majority
of the customers actually using multi-tenant cluster and
using namespace as a service. And if you're using a
namespace as a service, in that third layer for your users, you have to create some construct
like namespace, Spark API, even Jupyter Notebook, and
a few other things in there. So let's take a look at this in a little bit of a
different perspective, and the perspective is the following. Who creates the automation for each layer, and who consumes the
automation for each layer? So for layer one, usually
we see data platform teams. They're tool of choices,
generally Terraform. so they will create the Terraform, and they will also consume that Terraform. Layer two is very similar, they'll create a Terraform
and some other tooling, but they will install this
open-source softwares, and they'll manage them. Layer three however becomes things look a
little bit different. And what looks different is
that the data engineers usually have to go through a ticketing system, or if they have access to
use that Terraform platform, they're not very well-versed, so they have to open the tickets for help. And one of the reasons for those tickets is actually these AWS resources. 'Cause the rest, we have some tooling, you can put them on the helm chart, you can use like some other tooling. But if you have to create
AWS roles, policies, S3 buckets, RDS instances,
any resources in AWS with permissions, the data
engineers have to open a ticket, a security has to approve this ticket, somebody from the data
platform team will pick it up, copy-paste some Terraform,
create this construct, and the compliance team has to audit it. Instead of using this process, you can optimize it by
providing your users with a proper interface, which
we think is should be an API, and you can use the
Kubernetes API to do so. And you can install this
open-source project on Kubernetes to extend its API in order
to do, create IM policies, S3 buckets, and so on. So ACK is an open-source project that AWS open-source a while back. Recently, this year, the EKS
service team took ownership of all of the controllers for ACK. And currently, we're at 50 GA controllers. That means we have coverage
for 50 AWS services. And what GA means for you is that this is covered by your
enterprise support. So using ACK, you can
extend the Kubernetes API, and you can create APIs
to onboard your tenants, and you can do the full
namespace vending for them. If you're using one team per cluster, we see that those customers
are trying to expand this to the whole three layers. But in general, this is where the majority of the customers are, and they're really happy with this. You know, in the beginning when I started, and I said, here's where
we find the customers having two separate teams,
supporting two separate platform, centers around the same compute. And if you are an executive
in the room, you are probably, well, is this a good thing? Is it a bad thing? What should I do about it? Should I put them together? Should I, what do I do? I'll tell you what to do. So you don't wanna limit
the organizational growth, you wanna be able to, the number
of platform teams you have is somewhat irrelevant. What you want to do is you
want to standardize on tools and practices so you
can foster that growth as it comes to your organization. A word on Terraform here. So when you start splitting
your platform teams, let's say you end up
with 10 platform teams and you standardize on Terraform, you're gonna end up with 10
different code bases guaranteed. So you wanna standardize
not only on the tool, but how the tool is used. Again, as I mentioned, we wanna
utilize the Kubernetes API as one of those toolings, so we can provide APIs to our engineers. So the three things that you should do in order to set your
analytics platform to scale are use the best practices
that we just talked about, so you can optimize, optimize,
optimize those clusters for scalability, performance, and cost. Foster organizational growth, not by limiting the number
of platform teams you have, but by standardizing on
tools, best practices, and processes in your organization. And delight your end
users with the interface that they can use to
onboard onto the platform. Now all these are great in theory, and it would be just theory
if it wasn't for you, our customers, to put them in practice. So I'm delighted to say we have our customer here, AppsFlyer, and Victor will tell us how
they not only put all of these into practice and a lot more,
but they did it at scale. - Thank you. Thank you, Christina. Super excited to be here. Hello, everybody. Roland spoke about different
options to run Spark workloads. What if I can tell you
that only one decision can change your data organization. It can boost your performance,
enrich your observability, save costs, and empower your developers. Sounds fictional, right? Well I'm here today to tell you about the decision we made one year ago. My name is Victor, I'm
working for AppsFlyer for the past six years, I'm
leading the data platform group responsible for the real-time
and analytics data platforms. I have vast experience in AWS
ecosystem and data processing, and one of the biggest
benefits at AppsFlyer is that I can do it at scale. Did you know there are more
than 7 billion smartphones? On average, there are
more than 60 app installed on each phone. If you will show me your
phone and application, I will definitely recognize an app which has AppsFlyer SDK on it. AppsFlyer is helping app owners to optimize their advertising campaign and find the right audience for that app. We expose digital analytics
and handle a massive amount of data each day to make it happen. Now let's jump right into
the analytics workloads, and see how we run it at AppsFlyer. First, let's talk a bit about Spark. Spark is an open-source analytic engine for large scale data processing. You will find it almost
in every organization that handles data at scale. Let's review some of
its key characteristics. Spark is usually being
used as batch processing for consuming and
producing downstream data. Depending on the job, it will
require different CPU, memory, and IO performance. Processing time is very important, and the right compute
and scaling strategies are a key factor. And Spark jobs are usually
stateless in nature. However, if interrupted, they will require data reprocessing, which might affect your SLA. Now let's talk about the challenges at AppsFlyer with Spark jobs, we process more than 100 petabyte daily. We run thousands of very different
jobs at any given moment. Our compute is widely distributed
from Intel to Graviton, CPU, memory, and
storage-optimized instances. Basically you name it, we have it. We're very dynamic according
to our data trends. We process millions of events per second, and our traffic can scale
up and down very rapidly, and we must be very efficient
with our scaling strategies. And finally, we're very
strict with our SLA. As a data company, we must make sure we process our data in time, otherwise it will affect our business. So we decided that the
best course of action in handling those challenges
is moving our workloads from our original EC2 instances managed by configuration management and internal tools to EKS. Why EKS? Let's deep dive. There are several areas
where EKS ecosystem excels when it comes to analytics processing. I'm going to mention three
and show you the value. We're going to talk about
Karpenter for scaling and compute optimizations. Observability, which can be enriched and give you valuable
insights about your data. And enablement, how we
empower our data engineers. Remember this slide, it
perfectly shows the ingress, consume, and downstream. Let's focus on this area, the data lake. And let me show you as an example how our main data processing
compaction runs on EKS. Compacted data is the result of merging small fragmented data files into larger, more organized files. To optimize storage
efficiency and performance, this is usually the first
entry point for your data lake. We run it hourly, have around 150 jobs with different runtimes, and we process around
60 tera each iteration. I will start with Karpenter, which help us tackle our challenges and achieve our goals
for compute, scaling, and cost performance. Take a look how our old
EC2 base spark cluster looked like before we
switched to EKS and Karpenter. It was managed by configuration
management tools and EnOS. The yellow line represents utilization, and the purple represents
the cluster size. You can see that the scaling
mechanism is not effective. When our utilization drops, the node scale down cannot keep up. Karpenter solves it. it picks the right compute
per our configuration and scales up and down efficiently according to our utilization. In each iteration we scale
up approximately to 60 node, and back down when we end the processing. If we look at the utilization of the node, we will see that we peak at around 80%, which is our sweet spot and
stay stable in old capacity. We start to scale down only
when utilization drops. Data processing is very expensive
in term of compute power. By doing this, we minimize our idle time, and eliminate resource
waste and unnecessary costs. In a 24-hour cycle, we're
doing it more than 1,600 times, both for creation and termination. And remember this is only
our compaction workload. We have hundreds of other
different processing workloads, so we can only imagine how our
termination and creation node looks like on a daily basis. Let's look at the instant spread. Karpenter's strategy is
speaking the most stable and cost effective node
at any given moment. We use Graviton Gen 3
and fall back to Gen 2 when there is no capacity. We use spot instances only. And take a look at the bare metal node. Full control of the machine resources, direct hardware access,
no hypervisor overhead, very high performance. It is 15% of our NodePool. When was the last time anyone manually picked bare metal nodes for stateless or dynamic applications like Spark? It also gives us the option
to use new gen instances, and we can provision them
as soon as they get out. We also distribute a node across multiple availability zones. Karpenter's make sure that we provision on the most cost effective zone. Zone A was the winner that day. It had 20% more nodes compared to zone B. We also ensure that our job pods run within the same availability zone, eliminating cross AZ data
transfer and its associated costs. But not all was well that day. We had many spot interruption
during those 24 hours. In some cases, dozens in one hour, which should be devastating
to our SLA, right? However, due to the effective
termination handling by Karpenter, we can hook spot
termination signal to Spark, which gives us the option to
migrate the intermediate stage of data within two minutes. This approach eliminates the need for reprocessing in the
event of node failure. It makes spot termination nearly
seamless to our workloads, keeping us well within our SLA, and the longest job during those 24 hours was only 33 minutes. I've shown you some nice results. Now let's see how you can
achieve near the same performance with a few simple configuration changes. For scaling, we use Amazon Linux 2024, optimized for fast boot
time and kernel performance. This allows us to provision
nodes in under 10 seconds. For decommission, we adjust
our node distribution budget according to our processing trends. We set times when we can
decommission more aggressively to reduce the idle time, and less aggressive when we
are usually at peak utilization to maintain high performance. This configuration is being used for Spark to be aware of no termination
and enable Spark shuffling. And to ensure we can
migrate within two minutes, we utilize local storage
for optimal performance. To enhance resiliency and cost efficiency, we configure each Spark job to run within the same availability zone. Again, eliminating cross AZ traffic and its associated costs. And this section defines the
use of Graviton instances with local storage for
optimal performance. Now, I must say that we
try placing specific nodes, but no matter how many variations we try, Karpenter automatic selection
consistently outperform in terms of cost efficiency. We're done with tuning. Now let's talk about what we
can do with observability. We saw how Karpenter helps us
manage and scale our compute. Now let's see how combining
the metrics from Karpenter, Kubernetes, and Spark helps
us get some valuable insights from our platform. How many of you know
what is the percentage of each data processing flow? In compaction, we know exactly what is the ratio of every processing, and when it starts and ends
in each processing cycle. Here you can see that
clicks take around 28% of the workload, and start
at the middle of each cycle. This allows us to see the distribution and weight of each dataset
at any given moment. Moreover, we can see daily,
weekly, and monthly trends, and understand our system
and business implications. Look at this metric. We can see that click
processing was reduced by 8% compared to last week. And a different dataset
was increased by 35, which might be a bit concerning, right? By examining our Datadog query, we can see that this information
can be easily obtained by combining metrics from
Kubernetes and Spark. But what happens when
we add Karpenter metrics for price estimation? Karpenter sends us cost
per instance and AZ, and by adding to Spark and Kubernetes, we can calculate how much
each data processing cost. So we get the price for
processing our data per minute in near real-time. This is huge, both for
engineering and business purposes. You can tell how your
co-deployment affects the cost, and take decision according to the trends. You can even set a better pricing for the service you
provide for your customers. You can even take it one step further by integrating this
into your data lineage. Allowing you to determine the total cost of your entire data processing pipeline, you can decide what can be
optimized and what is redundant. Combining your observability metrics gives you a comprehensive
view of your data flows, and allows you to take
data-driven decisions about your data. Well, all those metrics and
performance I showed you worth nothing if only platform engineers know how to use it and tune it. And I showed you only
a few of the options. We encourage and give our
data engineers full autonomy and control over their
applications and platforms. We of course provide best
practice defaults and policy, but they can change in overall
depending on their needs. Everything is being done
through our source code. We created a detailed Git structure, which defines the action of the repo. Deployment units, both for
infrastructure application and third-party integrations. And environments, which
segregates between development, staging, and production. Each has its own Git or flow. This approach allows us to
manage the infrastructure of Kubernetes and application components from a single interface
enabling automated workflows and validation for
executions and deployment. It protects us from configuration drift, ensure we maintain the current state, and allows us to spin up
and modify application and the infrastructure within minutes. And finally, this removes the dependencies of our platform engineers. It raises the velocity and
autonomy of the data engineers, and contributes to the knowledge of both. So at the beginning, I presented that one decision
change our data organization. As you notice, this decision
was moving Spark workloads from EC2 to EKS. Now let me show you the value. This is a young version of me. Compared to our old EC2
Intel by Spark clusters, by using EKS, Karpenter, and Graviton, we reduced our cost by 60%. We improved our SLA by 35%, and significantly enriched
our observability. And the cherry on top, we
reduced the operational overhead of our platform engineers, and raise their overall
happiness along the way. Thank you. (audience applauding) - All right. So excellent presentation, thank you both. If you take anything away, right? Optimize and monitor EKS for
analytics and best practices. Align tools and practices to
foster organizational growth. So we saw the layers that
Christina talked about, so you can be happy like Victor. And provide APIs. Remember, developers, data engineers, data scientists are your
customers of the platform. If they can't build, if you
can't provide them APIs, all you're gonna have is
a platform not being used. So enable APIs to empower data engineers to work independently. Autonomy, while you're still providing the automations for control. We have a happy union together. So thank you. Thank you, everyone, for joining. Don't forget for session
resources like data on EKS, you can click and scan the QR code there. Thank you for coming, everyone, and enjoy the rest of the conference. (audience applauding)

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=0s) - All right.

[00:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1s) Welcome, my name is Roland Barcia.

[00:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3s) I'm the worldwide director

[00:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=5s) for our specialist technology team.

[00:08](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=8s) I have the honor to be presenting
with much smarter people,

[00:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=12s) Christina and Victor.

[00:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=13s) They will introduce themselves
when they start speaking

[00:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=16s) for the interest of time.

[00:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=17s) So let's get going,

[00:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=18s) 'cause we have a lot of
material to get through.

[00:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=20s) This is a 400-level session,
so we wanna go deep very fast.

[00:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=23s) I'm gonna kick it off, and
kind of set some context

[00:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=26s) before I hand it off to Christina.

[00:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=29s) And we're gonna talk a little
bit about data to start.

[00:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=32s) Obviously, in a conference,
where we're talking a lot about

[00:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=36s) generative AI, LLMs, Bedrock, et cetera,

[00:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=40s) data has become probably
one of the key commodities

[00:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=43s) that we have.

[00:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=44s) And there's lots of it, lots
of different data formats,

[00:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=47s) lots of different users
or personas of data.

[00:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=50s) It's no longer just analysts anymore.

[00:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=52s) Its developers use data,
end users use data,

[00:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=56s) internal folks use data,

[00:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=57s) and people need to make
decisions fast and quickly.

[01:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=60s) And so when we talk about data,

[01:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=63s) we wanna think about personas,

[01:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=65s) because we're at AWS,
we're customer-obsessed,

[01:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=69s) and we gotta think about data

[01:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=70s) from a perspective of who uses it.

[01:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=73s) And so we're gonna get a little bit deeper

[01:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=75s) into things like data processing
with Spark as an example.

[01:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=79s) But we want to think about
things like your external users.

[01:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=82s) So you have data that you expose

[01:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=85s) as part of your business to your users.

[01:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=87s) Oftentimes you have
historical data, batch data,

[01:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=91s) things that people look
at monthly, weekly,

[01:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=94s) that have a known pattern.

[01:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=95s) And more and more, we have
a need to make decisions

[01:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=98s) real-time with data.

[01:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=100s) This is probably where we see a lot

[01:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=101s) of generative AI use, right?

[01:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=103s) Where people are using prompt engineering

[01:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=105s) and things to do ad hoc queries,

[01:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=107s) ad hoc answers to questions,
and things like that.

[01:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=111s) Internally, we have personas
that wanna make use of data

[01:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=114s) to make decisions about
anything and everything

[01:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=117s) from how do I run a
system more efficiently?

[02:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=121s) How do I scale it better?

[02:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=123s) What are some security
audits that I'm seeing?

[02:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=125s) And observability tools
kind of help out there.

[02:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=129s) And then we have to process
lots and lots of data, right?

[02:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=133s) So we're gonna get into things like Spark,

[02:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=135s) and it's cluster technology,

[02:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=137s) and things like Hadoop in the past.

[02:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=139s) And then emerging technologies like Flink

[02:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=142s) that have kind of brought
together, you know,

[02:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=143s) how do I process streaming data,

[02:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=145s) as well as batch data together
to make these decisions.

[02:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=150s) And so let's talk a little bit
about platform engineering.

[02:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=154s) A lot of our customers have
standardized on Kubernetes.

[02:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=159s) They use EKS, Elastic Kubernetes Service.

[02:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=162s) Some great announcements this week

[02:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=163s) in other sessions in the track,

[02:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=164s) like Auto Mode and things like that.

[02:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=167s) But oftentimes when you are a startup,

[02:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=169s) maybe you have just a development team

[02:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=172s) and you do platform engineering

[02:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=173s) as part of that development team.

[02:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=174s) But over time, as you grow,

[02:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=176s) the emergence of platform engineering

[02:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=178s) has come about with Kubernetes.

[03:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=181s) And a lot of those concerns really focused

[03:04](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=184s) in the first generation
around web applications,

[03:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=187s) microservices, event-driven architectures.

[03:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=190s) And this emergence,

[03:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=192s) I always call it a
little bit of a collision

[03:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=195s) between personas and goals, right?

[03:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=197s) Where developers wanted freedom,

[03:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=200s) they want to use their
favorite open-source tools,

[03:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=202s) their technologies, they want autonomy.

[03:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=204s) I wanna build a new
app, I wanna deploy it,

[03:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=205s) I wanna get it out quickly.

[03:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=207s) And then you have platform teams

[03:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=208s) that are worried about things
like the security systems,

[03:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=212s) scalability, cost, performance.

[03:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=214s) And so the first generation
of these, you know,

[03:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=217s) platform teams are really
thinking about web applications,

[03:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=221s) microservices, transactional systems.

[03:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=224s) And platform engineering
has really emerged

[03:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=226s) as a way to kind of meet in the middle

[03:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=230s) between providing this autonomy

[03:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=233s) and still automating things like standards

[03:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=235s) in a developer-like way.

[03:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=237s) There's lots of talks on
overall platform engineering.

[04:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=241s) I have one on Thursday
in the serverless track

[04:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=243s) from the developer persona point of view,

[04:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=245s) the users of the platform.

[04:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=247s) And so you can come to that
session when I get into it.

[04:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=249s) But when we're talking
about platform engineering,

[04:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=251s) one of the things that
customers often struggles,

[04:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=253s) where is that line between the developers

[04:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=257s) and the people that use the
platform, and the platform team?

[04:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=261s) Do I vend out clusters?

[04:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=263s) Do I vend out code as a service?

[04:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=265s) Do I make it easy for developers
to just check in code?

[04:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=268s) And so these are the
first generation problems.

[04:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=270s) It's all been solved, right?

[04:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=272s) But probably not.

[04:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=274s) There's still probably lots of debate here

[04:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=276s) on where the line stands,

[04:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=277s) and that's because of the workloads.

[04:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=280s) And so we get now into the
age of data and lots of data,

[04:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=285s) and data scientists and engineers

[04:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=287s) have started building
things with Notebooks,

[04:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=290s) using SQL data processing.

[04:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=292s) They're building stateful applications.

[04:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=294s) They're building
applications with streaming

[04:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=296s) and events workflows.

[04:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=298s) They're using Notebooks
with Python or R to build

[05:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=302s) applications and Notebooks
that are doing generative AI,

[05:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=305s) or ML, or any type of data processing.

[05:08](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=308s) They're building data
lakes and data meshes,

[05:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=310s) and applications that sit in front of them

[05:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=312s) to kind of federate the data.

[05:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=314s) And the platform team all of a sudden

[05:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=316s) has to worry about things like,

[05:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=318s) what's the optimal storage to use?

[05:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=320s) Do I give them GPUs?

[05:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=321s) We have cool Inferentia2 and Trainium2

[05:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=323s) announced this morning

[05:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=324s) that we kind of heard
about as well, right?

[05:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=326s) And so, and we have new
types of DevOps, MLOps,

[05:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=330s) data pipelines, the lifecycle of an LLM,

[05:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=333s) the lifecycle of MyData.

[05:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=335s) So these are now new concerns
in this next generation.

[05:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=339s) And so I'm not gonna go into
all of these in exhaust,

[05:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=343s) but there's a lot of goals
for platform engineering

[05:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=346s) and data workloads, right?

[05:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=347s) So how do I get the right
resources, developers?

[05:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=352s) I wanna get the right
type of machine type,

[05:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=354s) the right type of GPUs,
the right storage type

[05:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=357s) for their workloads, for their Notebook,

[05:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=359s) for their data processing.

[06:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=361s) They want the right security,
the right isolation.

[06:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=363s) They don't want a data
job running over here

[06:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=365s) to interfere with a
transactional system over there.

[06:08](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=368s) And I wanna do it at the
best price point possible.

[06:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=371s) And of course, just like
developers, data scientists,

[06:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=374s) data engineers are very
opinionated about their favorite,

[06:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=378s) you know, PyTorch framework, TensorFlow,

[06:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=380s) all the different types
of frameworks out there

[06:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=383s) for doing data applications.

[06:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=385s) And so how do I support that autonomy

[06:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=388s) with this new generation of applications

[06:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=390s) that are very data intensive?

[06:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=393s) Lots of different challenges
with stateful workloads, right?

[06:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=396s) We're talking about
things like how do I use

[06:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=399s) thousands of nodes or
even the opposite problem,

[06:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=402s) really large images that
take a while to start up

[06:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=406s) to warm up the data.

[06:48](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=408s) And some of the things in Kubernetes,

[06:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=410s) we're really optimizing
the first generation

[06:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=412s) to spin up compute very fast

[06:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=414s) and detect if there's a
failure of every pass,

[06:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=416s) and kill the pod, bring up a new pod.

[06:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=419s) And sometimes these data workloads

[07:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=420s) need to do things like check mark

[07:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=422s) or checkpoint where they
are in data processing.

[07:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=425s) They have these new concerns
with stateful applications.

[07:08](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=428s) Sometimes the scalers are too fast,

[07:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=430s) there's different network configurations.

[07:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=433s) Do models have gravity?

[07:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=434s) Does data have gravity?

[07:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=435s) Even people are finding in some cases

[07:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=438s) that data is cheaper to
move closer to the compute.

[07:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=441s) And so you know, there is all
fluctuation of these patterns,

[07:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=446s) and platform teams have to adjust to that.

[07:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=448s) And so these are some of
the challenges we'll see,

[07:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=451s) Christina and Victor are gonna
go into real world examples

[07:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=453s) of how they implemented this.

[07:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=456s) Just very quickly.

[07:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=458s) You know, there's different
options for folks.

[07:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=461s) By all means you can do Spark,

[07:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=464s) EMR in a serverless way
using serverless paradigm

[07:48](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=468s) if you are doing things
more native to AWS,

[07:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=471s) and you get some default
services, lots of advantages.

[07:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=474s) A lot of our customers choose
Kubernetes to standardize.

[07:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=478s) We have one of the best
Kubernetes services

[08:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=480s) out there in EKS, and there's
different ways to run Spark,

[08:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=483s) because of the ecosystem you have.

[08:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=485s) You can use an operator
run Spark on your own.

[08:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=487s) We of course have Amazon
EMR that runs on EKS

[08:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=490s) as well as an option to
give you kind of the best

[08:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=493s) of both world between
management and flexibility,

[08:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=495s) and the best open-source frameworks.

[08:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=499s) So Kubernetes and data, right?

[08:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=502s) When we talk about it,

[08:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=503s) there's lots of different
patterns early on,

[08:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=505s) started with storage and
custom resource definitions,

[08:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=509s) moved on to event-based
applications with Kafka

[08:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=513s) that gives you events,
event streaming, messaging.

[08:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=516s) Then we get to spark with
the architecture moving

[08:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=519s) from this type Hadoop workloads

[08:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=521s) in memory intensive parallel processing.

[08:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=524s) Then we get into Apache
Flink, which is like,

[08:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=526s) I need both real-time data
and I need batch data,

[08:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=529s) and I need to do processing
across them both,

[08:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=532s) we get into I need GPUs

[08:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=533s) and other types of specialized
hardware to run intensive,

[08:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=537s) maybe training models et cetera.

[08:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=539s) And specialized schedulers
in supporting things

[09:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=541s) like Notebook as a service.

[09:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=543s) So we have an evolution
of Kubernetes for data.

[09:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=546s) We have a project, you take
a picture really quickly,

[09:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=550s) data on EKS.

[09:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=552s) If you can come to us afterwards,

[09:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=554s) lots of different blueprints
and best practices

[09:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=557s) to help you provision different patterns,

[09:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=559s) like running Spark on EKS,
or running Flink on EKS,

[09:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=563s) or running Kafka on EKS.

[09:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=564s) So we have different types of scripts

[09:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=566s) that kind of help you get started.

[09:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=569s) And on the last point,
and we talk about data,

[09:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=572s) there's really a life cycle.

[09:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=574s) So we talked about the support

[09:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=576s) that a data platform needs to have.

[09:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=578s) So for example, how does the
data get into your environment,

[09:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=581s) into your system ingest?

[09:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=583s) And you need to support
different types of tools,

[09:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=586s) Kafka-based things.

[09:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=587s) You can do managed
services like Amazon MSK

[09:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=590s) or run Kafka and Kubernetes.

[09:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=591s) We have native options
like Kinesis, et cetera.

[09:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=594s) And then we have workflow tools

[09:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=595s) that kind of help stage the data,

[09:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=597s) whether it be things like
Step Function, or Airflow,

[10:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=600s) or Argo Workflows,
different batch schedulers

[10:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=603s) to have some instances come
up and more stateful patterns,

[10:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=607s) and we already talked
about data processing.

[10:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=610s) Then we get into the data processing tier,

[10:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=612s) and we get into things
like batch scheduling,

[10:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=615s) doing kind of all the
processing you need overnight.

[10:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=618s) And then you wanna get your
data out and consume it.

[10:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=621s) You might do some transformations,

[10:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=623s) might do some SQL against it,
different catalog the data,

[10:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=627s) and make the data available as an API.

[10:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=629s) So this is the lifecycle of the data.

[10:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=631s) And so with that I'm gonna
now, we're gonna go deeper,

[10:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=634s) I'm gonna hand it to Christina.

[10:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=636s) Christina, gave you a minute back.

[10:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=638s) - Thank you, Roland.

[10:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=641s) Hi, everyone.

[10:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=642s) Next I'm gonna cover three
things that you can do.

[10:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=646s) So you can optimize your
analytics platform on Kubernetes

[10:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=650s) for growth.

[10:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=651s) So you're set to bring in
analytics workloads fast into AWS,

[10:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=657s) as well as grow into different regions.

[11:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=661s) My name is Christina Andonov,
I am a solutions architect,

[11:04](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=664s) and I help you, our customers,

[11:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=667s) building analytics
platforms on Kubernetes.

[11:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=670s) And as Roland mentioned,

[11:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=671s) one reason that you might
be here in this room

[11:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=674s) is that you're already running
your business applications

[11:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=677s) on Kubernetes.

[11:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=678s) You feel comfortable using it, scaling it,

[11:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=681s) and now the analytics
workloads are coming in.

[11:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=685s) So when we engage with
customers like that,

[11:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=689s) this is where we usually find them,

[11:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=691s) having two separate teams,
building two separate platforms

[11:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=697s) centered around the same compute.

[11:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=699s) And the reason for that is not
that much the compute itself

[11:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=703s) as it is the traffic
pattern of the workload

[11:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=706s) that lends on that compute.

[11:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=709s) See for business application,

[11:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=711s) the traffic pattern is much
like the weather in California.

[11:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=715s) For the most part, you get
highs of 80s, lows of 60s,

[11:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=718s) and with minor exceptions,
it is very predictable.

[12:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=723s) The traffic pattern for
the analytics workloads,

[12:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=727s) well, that's more like the
weather in the Caribbean

[12:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=731s) during the hurricane season.

[12:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=733s) And when that flood of jobs
arrives at your clusters,

[12:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=738s) that data platform team's
responsibility is to make sure

[12:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=742s) that these clusters can scale
in a very short period of time

[12:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=747s) so they can ingest the jobs are optimized,

[12:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=750s) so they can process the jobs fast

[12:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=753s) and can do all that cost efficiently.

[12:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=758s) So next, let's go over some best practices

[12:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=762s) of what you can do to
optimize these clusters.

[12:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=766s) And when I mentioned best practices,

[12:48](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=768s) because I'm assuming
you're already running

[12:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=771s) your business applications on Kubernetes,

[12:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=773s) I'll just go over the
delta of best practices

[12:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=776s) between your business platform
and your data platform.

[13:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=781s) We're gonna build a cluster

[13:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=782s) with best practices from the ground up.

[13:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=785s) We're gonna split the build
in three logical layers

[13:08](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=788s) where layer one will be building a vanilla

[13:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=792s) yet production-ready cluster
optimized for analytics.

[13:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=796s) Layer two will be installing
various open-source tools

[13:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=799s) to make that cluster
purpose-built cluster.

[13:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=803s) And layer three will be
onboarding your tenants

[13:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=806s) on that cluster.

[13:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=808s) And actually before you
even create the cluster,

[13:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=810s) you have to set up the networking

[13:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=813s) to make sure the network will
scale and you have enough IPs,

[13:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=816s) because you might have
heard that with IPv4,

[13:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=820s) IP exhaustion is a thing,
and your natural inclination

[13:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=825s) might be to use an overlay network.

[13:48](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=828s) But overlay network will inevitably

[13:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=831s) add a little bit of latency,

[13:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=833s) which is counterproductive to
what we wanna achieve here.

[13:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=837s) So instead of an overlay network,

[13:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=838s) what you can do is use this special range

[14:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=842s) of non-routable IPs.

[14:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=845s) And in this case, in this example,

[14:08](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=848s) two CIDR blocks that will give you 130 IPs

[14:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=853s) to use for the nodes and the pods.

[14:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=857s) Here is where I usually get the question,

[14:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=859s) but how about IPv6?

[14:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=861s) And yes, yes, IPv6 will make
all of our exhaustion problems

[14:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=867s) go away eventually.

[14:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=870s) Kubernetes supports IPv6
since two years ago.

[14:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=875s) Spark supports IPv6 since last
year, version 3.4 or later.

[14:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=880s) But chances are something,
somewhere along your stack,

[14:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=885s) or that your cluster talks to,

[14:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=887s) might not yet be supporting IPv6.

[14:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=889s) So it's definitely an option,

[14:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=891s) but if you choose to use
it, please test it truly.

[14:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=895s) Either way you go about here,

[14:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=897s) I'll consider you have enough IPs,

[14:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=899s) and then we can proceed
with creating the cluster,

[15:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=902s) and start to put the
add-ons onto the cluster.

[15:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=906s) The first add-on that
goes in is the VPC CNI.

[15:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=909s) And the VPC CNI comes
with this default setting,

[15:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=914s) WARM_ENI_TARGET=1.

[15:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=916s) What does that even mean?

[15:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=917s) Well what it means is that
when instances come up,

[15:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=922s) they have an ENI, and that ENI holds a set

[15:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=926s) of pre-warmed IPs.

[15:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=929s) One of those IPs goes to the worker node,

[15:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=932s) and then a spot comes up,

[15:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=934s) they get assigned IPs
from those pre-warmed IPs.

[15:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=938s) Now if that instance
were to be a c5.2xlarge,

[15:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=943s) that ENI will hold 15 IPs.

[15:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=945s) But for analytics, we tend
to use much larger instances,

[15:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=949s) such as c5.18xlarge, and that
instance comes with two ENIs,

[15:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=956s) and they hold 50 IPs each.

[15:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=959s) That is 100 IPs.

[16:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=961s) Well for analytics, our pods
tend to be larger as well,

[16:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=965s) which means you are not gonna schedule

[16:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=967s) nearly as 100 pods on this instance,

[16:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=970s) and all these IPs, most
of them will go wasted.

[16:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=974s) And that pool of 130 we just
said, that might not be enough.

[16:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=979s) So what you can do here is set
MAX_ENI to 1 for the VPC CNI.

[16:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=986s) And then the second
option here, maxPods: 30.

[16:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=990s) That is setting on the cubelet,

[16:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=994s) you can set it to a static number like 30,

[16:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=998s) or you can check our data
and it has blueprints.

[16:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1001s) We have different patterns
where we set that option

[16:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1006s) automatically based on
how large the instances

[16:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1009s) for different flavors of Linux.

[16:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1012s) Last thing for the VPC CNI, VPC
CNI tends to be very chatty,

[16:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1017s) and who it likes to talk to,
its best friend, the EC2 API.

[17:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1023s) See for each and every of those IPs,

[17:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1025s) usually the VPC CNI makes
a call to the EC2 API.

[17:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1029s) And if you're trying to
bring up one instance,

[17:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1031s) that's not a problem.

[17:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1032s) But if you're trying
to bring 100 instances

[17:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1035s) at a time, well, guess what?

[17:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1037s) You're gonna throttle the API.

[17:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1040s) So what you can do here

[17:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1041s) is set up this enable prefix delegation.

[17:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1045s) What enable prefix delegation does,

[17:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1047s) it packages 16s of those IPs in one query,

[17:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1051s) and it queries the EC2 API,

[17:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1054s) that will reduce the queries
to the EC2 API fold 16.

[17:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1059s) All right, VPC CNI set.

[17:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1063s) Next I have a riddle for you.

[17:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1066s) Do you know why CoreDNS gets
invited to all the parties?

[17:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1071s) 'Cause it resolves everything.

[17:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1073s) Well most of the time.

[17:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1075s) For analytics, usually, CoreDNS
has to scale up proactively

[18:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1080s) as a lot of instances are coming up.

[18:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1083s) And in the past, you had to
use this open-source project

[18:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1086s) called Cluster Proportional Autoscaler

[18:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1089s) in order to scale CoreDNS.

[18:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1091s) And I have good news for you.

[18:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1093s) In May, we announced
many scaling for CoreDNS.

[18:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1098s) That means if you are
on version 1.25 of EKS

[18:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1102s) and CoreDNS 1.9, and you have upgraded

[18:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1107s) one time to those versions
or later since May,

[18:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1111s) this feature is already available for you,

[18:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1113s) and all you have to do is
just set, just enable it,

[18:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1117s) and then CoreDNS will
proactively scale for you.

[18:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1123s) You should also install
open-source project

[18:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1126s) called NodeLocal DNS.

[18:48](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1128s) NodeLocal DNS is a
DaemonSet that you install,

[18:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1131s) it runs on every single node,
and it caches the queries,

[18:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1134s) so it alleviates the
queries that go to CoreDNS.

[18:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1138s) And one last thing here,
let's talk a little bit about

[19:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1141s) how CoreDNS resolves external domains.

[19:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1146s) If we give it a domain
like s3.amazonaws.com,

[19:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1151s) it will go to its configuration,

[19:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1153s) and there's this setting called ndots:5,

[19:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1156s) it's gonna see ndots:5.

[19:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1157s) And what that means is CoreDNS
will look at that domain,

[19:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1160s) say, oh, this domain has two dots,

[19:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1162s) and two is less than five.

[19:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1163s) So this must be internal
to my cluster domain.

[19:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1168s) So what I'm gonna do is I'm gonna go here

[19:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1170s) and append every single
option in the search line,

[19:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1175s) and that will resolve of
in five unnecessary queries

[19:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1179s) before I go externally and
check where that domain is.

[19:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1187s) One thing you can do here
is, first and foremost,

[19:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1189s) please do not change
ndots of 5 to CoreDNS,

[19:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1193s) but you can set ndots
to 2 on the pods only.

[19:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1198s) What that will do is it's gonna
take a look at the domain,

[20:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1202s) it's gonna say, "Oh, it has two dots,

[20:04](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1204s) and I'm gonna resolve it right away."

[20:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1206s) It's gonna resolve in one query.

[20:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1209s) And that will alleviate the
pressure on the CoreDNS pods,

[20:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1213s) and that's how CoreDNS can keep
its party celebrity status.

[20:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1221s) Next, for your business applications,

[20:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1226s) we're gonna scale some compute here.

[20:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1227s) So for business applications,

[20:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1229s) you tend to use this open-source project

[20:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1231s) where a lot of our customers tend to use

[20:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1233s) this open-source project
called Cluster Autoscaler.

[20:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1236s) Cluster Autoscaler scales up instances

[20:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1240s) based on CPU and memory.

[20:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1244s) And then what it does,
how it scales instances,

[20:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1246s) it usually takes on average like

[20:48](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1248s) between two and three minutes
to bring an instance up.

[20:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1251s) We see data platform teams
are the first to switch

[20:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1256s) to another open-source
project called Karpenter.

[20:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1258s) Karpenter came out from
AWS, we open-sourced it,

[21:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1263s) and we donated it to seek
auto-scaling last year.

[21:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1267s) And this year, we graduated it to GA.

[21:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1270s) So now it's V1, it is stable,
you can go ahead and use it.

[21:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1274s) And the difference here
with Karpenter is that

[21:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1278s) one Karpenter is fully
aware of AWS pricing.

[21:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1281s) So not only it's gonna pick an instance

[21:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1284s) that is gonna fit the pod's
memory and CPU speaking,

[21:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1288s) but it's gonna pick the most
cost efficient instance.

[21:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1293s) Also, Karpenter is very
quick on how it scales

[21:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1296s) those instances up much, much quicker.

[21:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1298s) We usually see scaling the instance up

[21:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1300s) in less than a minute.

[21:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1303s) Before we dive into the
Karpenter configuration,

[21:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1307s) let's talk a little bit
about how Spark jobs work.

[21:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1310s) Usually when a data engineer
submits a Spark job,

[21:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1314s) a driver pod comes up,

[21:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1316s) and that driver pod is
responsible for managing the job.

[22:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1320s) That driver pod is responsible
for scheduling the executors,

[22:04](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1324s) and if any of the
executors get interrupted,

[22:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1326s) the driver pod knows about
it, it schedules another one,

[22:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1329s) and it finishes the job.

[22:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1331s) If the driver pod gets interrupted,

[22:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1333s) the whole job has to start over.

[22:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1337s) What that means for Karpenter

[22:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1339s) is that we can install the driver pod

[22:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1343s) to on-demand instances,
and executors are ideal

[22:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1348s) for our deeply discounted spot capacity.

[22:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1352s) As it comes to Karpenter,

[22:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1353s) you can actually set one NodePool,

[22:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1355s) and provide both capacity
types in the NodePool,

[22:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1360s) and then use either annotations
or labels, or taints,

[22:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1363s) and toleration to land
each workload respectively.

[22:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1369s) Okay, great.

[22:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1371s) Now we set the compute to scale,

[22:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1374s) next on the menu, we have storage.

[22:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1377s) And when I say storage, I
mean Spark shuffle storage.

[23:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1381s) See we have these instance
types with d in the name

[23:04](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1384s) before the dot.

[23:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1386s) What that d means is that that instance

[23:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1389s) comes with a SSD drive
built-in into the instance.

[23:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1395s) That will be the fastest
storage you get, hands down.

[23:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1401s) So we recommend utilizing that,

[23:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1404s) those instances and that storage.

[23:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1406s) Now some instances come with one,

[23:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1409s) some instances come with
more than one SSD drives.

[23:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1412s) And to take full advantage
of the whole capacity,

[23:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1417s) you should set these drives
to RAID0 using Karpenter.

[23:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1423s) It's as simple instance
source policy RAID0.

[23:48](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1428s) I don't know if you've used this before,

[23:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1430s) but this used to be a user-data script

[23:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1432s) that does some calculations.

[23:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1434s) So this is awesome.

[23:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1436s) Not only this is awesome,

[23:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1437s) but you don't have to set the host pod

[24:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1440s) for the executors anymore.

[24:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1442s) Executors will have direct
access to that storage.

[24:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1446s) Well you still might wanna
limit how much of that storage

[24:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1450s) they'll use in the Spark
configuration, but that's about it.

[24:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1454s) So for short running
jobs, this is perfect,

[24:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1457s) but for long running jobs,

[24:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1459s) if that instance gets interrupted,

[24:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1462s) well the driver pods know about it,

[24:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1464s) and it's gonna bring other executors up,

[24:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1467s) but now we lost the checkpoints.

[24:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1471s) So these two executors have to start over.

[24:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1474s) So if you have longer running jobs,

[24:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1477s) maybe a better option would
be to use EBS volumes.

[24:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1482s) And in Spark configuration,
we can do that,

[24:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1485s) we can make the driver pod
aware of the EBS volumes

[24:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1489s) with this configuration.

[24:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1491s) And that way if the
instance gets interrupted,

[24:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1493s) another one comes up, the driver pod knows

[24:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1496s) where the EBS volumes are,

[24:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1498s) it attaches them to the new executors,

[25:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1500s) and the new executors take off

[25:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1503s) from where the interrupted ones left off,

[25:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1506s) because they have the
checkpoint data in EBS.

[25:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1510s) Last thing about storage here

[25:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1512s) is that these two options
are not mutually exclusive.

[25:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1515s) You can use, you can provide
both of them to your end users,

[25:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1519s) and they can pick and
choose which one to use

[25:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1521s) depending on the job they're running.

[25:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1526s) As I mentioned, Karpenter
brings instances up very quick.

[25:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1531s) The next thing that needs to happen

[25:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1533s) is that instance has
to download the images

[25:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1538s) and to run the pods.

[25:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1540s) And good rule of thumb here

[25:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1542s) is to have from the
moment I want an instance

[25:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1544s) to the moment I have
my pods up and running

[25:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1547s) is to have that process under a minute.

[25:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1551s) So a few optimizations you can do here.

[25:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1553s) First and foremost, get
those images the closest

[25:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1556s) to your instances as possible.

[25:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1559s) If you are storing them in ECR,

[26:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1561s) make sure they're in the region

[26:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1562s) with cross-regional replication.

[26:04](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1564s) If you're storing them
in a different repo,

[26:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1567s) we support pull through cache for ECR,

[26:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1570s) use pull through cache,
put them in the region.

[26:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1573s) Set a VPC endpoint,

[26:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1575s) so those images get downloaded
through the network,

[26:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1578s) and we don't have to go out and back in.

[26:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1581s) And if that's not enough,

[26:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1583s) and that's might not be enough
to get it under a minute,

[26:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1586s) if your images are pretty
large, meaning 5 to 10 gigs,

[26:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1590s) what you can do is you
can take large files out

[26:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1595s) of your images such as JAR
files and other libraries.

[26:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1598s) You can store them in S3 express zone 1.

[26:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1602s) And then have the images lean,

[26:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1604s) and when they download, use S3-Mountpoint

[26:48](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1608s) to mount this S3 bucket as
a drive to your executors.

[26:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1614s) Okay, so now we get it under a minute.

[26:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1616s) And last one, in this first layer,

[27:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1620s) please monitor, set up your monitoring

[27:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1623s) before you put this in production.

[27:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1625s) I know most of you monitor,

[27:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1627s) Spark and the open-source
softwares that you're using,

[27:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1631s) they come with metrics.

[27:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1633s) I want you to monitor three
additional things here.

[27:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1635s) The first thing is please monitor

[27:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1637s) the Kubernetes control plane.

[27:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1639s) We do expose the
Kubernetes control metrics.

[27:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1642s) Check out the EKS best practices guide,

[27:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1645s) and make sure you monitor that.

[27:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1647s) Make sure you monitor the AWS APIs.

[27:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1650s) We do provide in CloudWatch metrics.

[27:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1653s) And as I mentioned earlier,
if you're using VPC CNI,

[27:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1657s) you might throttle the EC2 API.

[27:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1660s) Make sure you have access
to those throttle metrics,

[27:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1663s) out CloudWatch as a data
source to your Grafana,

[27:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1667s) or to your monitoring vendor,

[27:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1669s) and watch those throttle metrics.

[27:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1671s) Same thing for the EBS API.

[27:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1673s) And last one, make sure
you monitor the network.

[27:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1677s) See for example, CoreDNS
is using UDP protocol,

[28:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1682s) which means if your
contract table on the Linux,

[28:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1686s) the connection tracking
table gets filled up,

[28:08](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1688s) those CoreDNS packages
are gonna get dropped.

[28:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1690s) And you wanna know about it
from the CoreDNS metrics,

[28:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1693s) you need to monitor the network again,

[28:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1696s) EKS best practices guide
for monitoring the network,

[28:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1699s) check it out.

[28:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1700s) And that concludes the first layer.

[28:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1704s) So now we have a cluster that can scale,

[28:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1707s) will be performant enough,
and cost efficient.

[28:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1712s) Next we're gonna add
various open-source software

[28:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1715s) on this cluster to make
it purpose-built cluster.

[28:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1719s) The most common open-source projects

[28:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1722s) that we see customer use are Apache Flink

[28:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1726s) and Apache Spark.

[28:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1729s) Usually the question is,

[28:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1731s) do I put them together
in the same cluster,

[28:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1733s) or do I split them in their own cluster?

[28:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1736s) And the answer to that
is, well, it depends.

[28:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1739s) If you have smaller clusters,

[29:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1742s) or clusters up to let's say 2-300 nodes,

[29:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1746s) yeah, you can run them
on the same cluster.

[29:08](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1748s) But if your clusters start
growing beyond that point,

[29:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1752s) it will be good to start
thinking about separating them.

[29:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1755s) The rest of the talk will be focused

[29:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1757s) mostly on Apache Spark here.

[29:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1760s) For Apache Spark, we recommend,

[29:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1762s) if you're running the open-source version

[29:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1764s) to use the Spark Operator.

[29:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1766s) Earlier this year, the
maintainers of data on EKS

[29:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1769s) worked with the community and
got the Spark Operator donated

[29:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1772s) to the Kubeflow community.

[29:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1775s) And since then, we have
seen tremendous bug fixes,

[29:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1779s) active maintainers.

[29:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1780s) So use Apache Spark.

[29:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1783s) Another one here that is optional,

[29:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1786s) like see the Kubernetes
scheduler, you can schedule jobs

[29:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1790s) on first in, first out basis.

[29:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1792s) But if you're coming from
like a Hadoop and YARN world,

[29:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1796s) you might want your priority
cues or gang scheduling.

[30:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1800s) And to use that, we recommend using this

[30:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1802s) other open-source project
called Apache YuniKorn

[30:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1805s) that works really well with Spark.

[30:08](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1808s) And last but not least,

[30:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1809s) you will need some workflow
engine for your jobs.

[30:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1813s) Most common one we see is Apache Airflow.

[30:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1816s) You can install it, and self-manage it,

[30:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1819s) or you can use our managed offerings.

[30:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1821s) We also see a fair
amount of Argo Workflows,

[30:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1824s) even lately, Step Functions
to do the workflow here.

[30:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1829s) And that concludes the second layer.

[30:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1832s) Next, let's talk a little bit about

[30:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1836s) your tenant isolation
strategy before we move on

[30:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1839s) to onboarding your tenants.

[30:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1842s) See, for some customers
use one team per cluster,

[30:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1847s) but we see the majority
of the customers actually

[30:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1850s) using multi-tenant cluster and
using namespace as a service.

[30:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1856s) And if you're using a
namespace as a service,

[30:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1858s) in that third layer for your users,

[31:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1861s) you have to create some construct
like namespace, Spark API,

[31:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1866s) even Jupyter Notebook, and
a few other things in there.

[31:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1869s) So let's take a look at this

[31:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1872s) in a little bit of a
different perspective,

[31:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1874s) and the perspective is the following.

[31:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1876s) Who creates the automation for each layer,

[31:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1879s) and who consumes the
automation for each layer?

[31:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1883s) So for layer one, usually
we see data platform teams.

[31:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1887s) They're tool of choices,
generally Terraform.

[31:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1889s) so they will create the Terraform,

[31:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1891s) and they will also consume that Terraform.

[31:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1895s) Layer two is very similar,

[31:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1897s) they'll create a Terraform
and some other tooling,

[31:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1899s) but they will install this
open-source softwares,

[31:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1903s) and they'll manage them.

[31:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1905s) Layer three however

[31:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1907s) becomes things look a
little bit different.

[31:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1910s) And what looks different is
that the data engineers usually

[31:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1914s) have to go through a ticketing system,

[31:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1916s) or if they have access to
use that Terraform platform,

[32:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1921s) they're not very well-versed,

[32:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1923s) so they have to open the tickets for help.

[32:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1927s) And one of the reasons for those tickets

[32:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1930s) is actually these AWS resources.

[32:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1933s) 'Cause the rest, we have some tooling,

[32:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1936s) you can put them on the helm chart,

[32:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1937s) you can use like some other tooling.

[32:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1939s) But if you have to create
AWS roles, policies,

[32:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1944s) S3 buckets, RDS instances,
any resources in AWS

[32:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1948s) with permissions, the data
engineers have to open a ticket,

[32:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1951s) a security has to approve this ticket,

[32:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1953s) somebody from the data
platform team will pick it up,

[32:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1956s) copy-paste some Terraform,
create this construct,

[32:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1961s) and the compliance team has to audit it.

[32:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1965s) Instead of using this process,

[32:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1969s) you can optimize it by
providing your users

[32:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1973s) with a proper interface, which
we think is should be an API,

[32:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1979s) and you can use the
Kubernetes API to do so.

[33:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1982s) And you can install this
open-source project on Kubernetes

[33:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1985s) to extend its API in order
to do, create IM policies,

[33:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1991s) S3 buckets, and so on.

[33:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1993s) So ACK is an open-source project

[33:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1995s) that AWS open-source a while back.

[33:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=1999s) Recently, this year, the EKS
service team took ownership

[33:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2005s) of all of the controllers for ACK.

[33:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2009s) And currently, we're at 50 GA controllers.

[33:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2013s) That means we have coverage
for 50 AWS services.

[33:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2018s) And what GA means for you is that

[33:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2022s) this is covered by your
enterprise support.

[33:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2027s) So using ACK, you can
extend the Kubernetes API,

[33:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2031s) and you can create APIs
to onboard your tenants,

[33:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2036s) and you can do the full
namespace vending for them.

[34:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2041s) If you're using one team per cluster,

[34:04](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2044s) we see that those customers
are trying to expand this

[34:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2050s) to the whole three layers.

[34:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2053s) But in general, this is where

[34:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2056s) the majority of the customers are,

[34:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2058s) and they're really happy with this.

[34:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2063s) You know, in the beginning when I started,

[34:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2065s) and I said, here's where
we find the customers

[34:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2069s) having two separate teams,
supporting two separate platform,

[34:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2072s) centers around the same compute.

[34:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2074s) And if you are an executive
in the room, you are probably,

[34:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2078s) well, is this a good thing?

[34:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2079s) Is it a bad thing?

[34:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2080s) What should I do about it?

[34:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2081s) Should I put them together?

[34:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2082s) Should I, what do I do?

[34:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2084s) I'll tell you what to do.

[34:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2086s) So you don't wanna limit
the organizational growth,

[34:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2090s) you wanna be able to, the number
of platform teams you have

[34:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2095s) is somewhat irrelevant.

[34:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2097s) What you want to do is you
want to standardize on tools

[35:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2102s) and practices so you
can foster that growth

[35:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2106s) as it comes to your organization.

[35:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2110s) A word on Terraform here.

[35:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2111s) So when you start splitting
your platform teams,

[35:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2114s) let's say you end up
with 10 platform teams

[35:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2117s) and you standardize on Terraform,

[35:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2119s) you're gonna end up with 10
different code bases guaranteed.

[35:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2125s) So you wanna standardize
not only on the tool,

[35:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2127s) but how the tool is used.

[35:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2131s) Again, as I mentioned, we wanna
utilize the Kubernetes API

[35:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2135s) as one of those toolings,

[35:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2137s) so we can provide APIs to our engineers.

[35:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2143s) So the three things that you should do

[35:48](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2148s) in order to set your
analytics platform to scale

[35:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2152s) are use the best practices
that we just talked about,

[35:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2156s) so you can optimize, optimize,
optimize those clusters

[35:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2159s) for scalability, performance, and cost.

[36:04](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2164s) Foster organizational growth,

[36:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2166s) not by limiting the number
of platform teams you have,

[36:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2170s) but by standardizing on
tools, best practices,

[36:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2174s) and processes in your organization.

[36:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2177s) And delight your end
users with the interface

[36:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2180s) that they can use to
onboard onto the platform.

[36:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2186s) Now all these are great in theory,

[36:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2190s) and it would be just theory
if it wasn't for you,

[36:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2194s) our customers, to put them in practice.

[36:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2198s) So I'm delighted to say

[36:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2200s) we have our customer here, AppsFlyer,

[36:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2204s) and Victor will tell us how
they not only put all of these

[36:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2210s) into practice and a lot more,
but they did it at scale.

[36:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2214s) - Thank you.

[36:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2216s) Thank you, Christina.

[36:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2218s) Super excited to be here.

[36:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2219s) Hello, everybody.

[37:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2223s) Roland spoke about different
options to run Spark workloads.

[37:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2230s) What if I can tell you
that only one decision

[37:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2233s) can change your data organization.

[37:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2237s) It can boost your performance,
enrich your observability,

[37:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2242s) save costs, and empower your developers.

[37:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2248s) Sounds fictional, right?

[37:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2250s) Well I'm here today to tell you

[37:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2252s) about the decision we made one year ago.

[37:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2256s) My name is Victor, I'm
working for AppsFlyer

[37:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2258s) for the past six years, I'm
leading the data platform group

[37:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2262s) responsible for the real-time
and analytics data platforms.

[37:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2266s) I have vast experience in AWS
ecosystem and data processing,

[37:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2271s) and one of the biggest
benefits at AppsFlyer

[37:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2274s) is that I can do it at scale.

[37:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2278s) Did you know there are more
than 7 billion smartphones?

[38:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2282s) On average, there are
more than 60 app installed

[38:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2285s) on each phone.

[38:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2287s) If you will show me your
phone and application,

[38:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2289s) I will definitely recognize an app

[38:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2292s) which has AppsFlyer SDK on it.

[38:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2296s) AppsFlyer is helping app owners

[38:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2299s) to optimize their advertising campaign

[38:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2301s) and find the right audience for that app.

[38:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2305s) We expose digital analytics
and handle a massive amount

[38:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2308s) of data each day to make it happen.

[38:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2311s) Now let's jump right into
the analytics workloads,

[38:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2315s) and see how we run it at AppsFlyer.

[38:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2319s) First, let's talk a bit about Spark.

[38:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2322s) Spark is an open-source analytic engine

[38:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2325s) for large scale data processing.

[38:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2327s) You will find it almost
in every organization

[38:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2329s) that handles data at scale.

[38:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2331s) Let's review some of
its key characteristics.

[38:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2336s) Spark is usually being
used as batch processing

[38:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2338s) for consuming and
producing downstream data.

[39:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2343s) Depending on the job, it will
require different CPU, memory,

[39:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2347s) and IO performance.

[39:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2350s) Processing time is very important,

[39:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2354s) and the right compute
and scaling strategies

[39:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2357s) are a key factor.

[39:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2361s) And Spark jobs are usually
stateless in nature.

[39:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2366s) However, if interrupted,

[39:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2369s) they will require data reprocessing,

[39:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2371s) which might affect your SLA.

[39:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2375s) Now let's talk about the challenges

[39:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2377s) at AppsFlyer with Spark jobs,

[39:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2380s) we process more than 100 petabyte daily.

[39:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2385s) We run thousands of very different
jobs at any given moment.

[39:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2391s) Our compute is widely distributed
from Intel to Graviton,

[39:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2397s) CPU, memory, and
storage-optimized instances.

[40:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2400s) Basically you name it, we have it.

[40:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2405s) We're very dynamic according
to our data trends.

[40:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2409s) We process millions of events per second,

[40:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2413s) and our traffic can scale
up and down very rapidly,

[40:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2419s) and we must be very efficient
with our scaling strategies.

[40:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2424s) And finally, we're very
strict with our SLA.

[40:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2429s) As a data company, we must make sure

[40:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2431s) we process our data in time,

[40:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2433s) otherwise it will affect our business.

[40:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2437s) So we decided that the
best course of action

[40:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2442s) in handling those challenges
is moving our workloads

[40:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2445s) from our original EC2 instances

[40:48](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2448s) managed by configuration management

[40:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2449s) and internal tools to EKS.

[40:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2453s) Why EKS?

[40:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2454s) Let's deep dive.

[40:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2457s) There are several areas
where EKS ecosystem excels

[41:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2460s) when it comes to analytics processing.

[41:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2463s) I'm going to mention three
and show you the value.

[41:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2467s) We're going to talk about
Karpenter for scaling

[41:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2469s) and compute optimizations.

[41:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2472s) Observability, which can be enriched

[41:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2475s) and give you valuable
insights about your data.

[41:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2479s) And enablement, how we
empower our data engineers.

[41:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2487s) Remember this slide, it
perfectly shows the ingress,

[41:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2491s) consume, and downstream.

[41:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2497s) Let's focus on this area, the data lake.

[41:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2501s) And let me show you as an example

[41:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2503s) how our main data processing
compaction runs on EKS.

[41:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2510s) Compacted data is the result

[41:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2512s) of merging small fragmented data files

[41:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2515s) into larger, more organized files.

[41:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2518s) To optimize storage
efficiency and performance,

[42:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2521s) this is usually the first
entry point for your data lake.

[42:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2525s) We run it hourly, have around 150 jobs

[42:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2529s) with different runtimes,

[42:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2532s) and we process around
60 tera each iteration.

[42:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2536s) I will start with Karpenter,

[42:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2539s) which help us tackle our challenges

[42:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2541s) and achieve our goals
for compute, scaling,

[42:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2545s) and cost performance.

[42:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2549s) Take a look how our old
EC2 base spark cluster

[42:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2553s) looked like before we
switched to EKS and Karpenter.

[42:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2557s) It was managed by configuration
management tools and EnOS.

[42:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2563s) The yellow line represents utilization,

[42:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2567s) and the purple represents
the cluster size.

[42:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2570s) You can see that the scaling
mechanism is not effective.

[42:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2573s) When our utilization drops,

[42:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2575s) the node scale down cannot keep up.

[42:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2579s) Karpenter solves it.

[43:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2581s) it picks the right compute
per our configuration

[43:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2583s) and scales up and down efficiently

[43:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2586s) according to our utilization.

[43:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2589s) In each iteration we scale
up approximately to 60 node,

[43:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2593s) and back down when we end the processing.

[43:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2596s) If we look at the utilization of the node,

[43:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2598s) we will see that we peak at around 80%,

[43:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2602s) which is our sweet spot and
stay stable in old capacity.

[43:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2607s) We start to scale down only
when utilization drops.

[43:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2614s) Data processing is very expensive
in term of compute power.

[43:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2618s) By doing this, we minimize our idle time,

[43:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2622s) and eliminate resource
waste and unnecessary costs.

[43:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2627s) In a 24-hour cycle, we're
doing it more than 1,600 times,

[43:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2632s) both for creation and termination.

[43:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2635s) And remember this is only
our compaction workload.

[43:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2638s) We have hundreds of other
different processing workloads,

[44:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2642s) so we can only imagine how our
termination and creation node

[44:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2647s) looks like on a daily basis.

[44:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2652s) Let's look at the instant spread.

[44:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2654s) Karpenter's strategy is
speaking the most stable

[44:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2658s) and cost effective node
at any given moment.

[44:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2662s) We use Graviton Gen 3
and fall back to Gen 2

[44:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2665s) when there is no capacity.

[44:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2668s) We use spot instances only.

[44:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2672s) And take a look at the bare metal node.

[44:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2676s) Full control of the machine resources,

[44:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2681s) direct hardware access,
no hypervisor overhead,

[44:45](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2685s) very high performance.

[44:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2687s) It is 15% of our NodePool.

[44:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2691s) When was the last time anyone manually

[44:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2694s) picked bare metal nodes for stateless

[44:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2697s) or dynamic applications like Spark?

[45:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2701s) It also gives us the option
to use new gen instances,

[45:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2705s) and we can provision them
as soon as they get out.

[45:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2712s) We also distribute a node

[45:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2713s) across multiple availability zones.

[45:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2716s) Karpenter's make sure that we provision

[45:18](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2718s) on the most cost effective zone.

[45:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2721s) Zone A was the winner that day.

[45:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2723s) It had 20% more nodes compared to zone B.

[45:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2727s) We also ensure that our job pods

[45:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2729s) run within the same availability zone,

[45:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2731s) eliminating cross AZ data
transfer and its associated costs.

[45:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2738s) But not all was well that day.

[45:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2741s) We had many spot interruption
during those 24 hours.

[45:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2746s) In some cases, dozens in one hour,

[45:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2750s) which should be devastating
to our SLA, right?

[45:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2755s) However, due to the effective
termination handling

[45:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2758s) by Karpenter, we can hook spot
termination signal to Spark,

[46:03](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2763s) which gives us the option to
migrate the intermediate stage

[46:06](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2766s) of data within two minutes.

[46:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2769s) This approach eliminates the need

[46:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2771s) for reprocessing in the
event of node failure.

[46:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2776s) It makes spot termination nearly
seamless to our workloads,

[46:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2780s) keeping us well within our SLA,

[46:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2783s) and the longest job during those 24 hours

[46:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2786s) was only 33 minutes.

[46:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2792s) I've shown you some nice results.

[46:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2794s) Now let's see how you can
achieve near the same performance

[46:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2798s) with a few simple configuration changes.

[46:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2802s) For scaling, we use Amazon Linux 2024,

[46:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2806s) optimized for fast boot
time and kernel performance.

[46:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2810s) This allows us to provision
nodes in under 10 seconds.

[46:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2815s) For decommission, we adjust
our node distribution budget

[46:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2819s) according to our processing trends.

[47:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2822s) We set times when we can
decommission more aggressively

[47:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2825s) to reduce the idle time,

[47:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2827s) and less aggressive when we
are usually at peak utilization

[47:11](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2831s) to maintain high performance.

[47:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2835s) This configuration is being used for Spark

[47:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2837s) to be aware of no termination
and enable Spark shuffling.

[47:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2841s) And to ensure we can
migrate within two minutes,

[47:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2844s) we utilize local storage
for optimal performance.

[47:29](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2849s) To enhance resiliency and cost efficiency,

[47:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2852s) we configure each Spark job

[47:34](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2854s) to run within the same availability zone.

[47:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2858s) Again, eliminating cross AZ traffic

[47:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2861s) and its associated costs.

[47:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2864s) And this section defines the
use of Graviton instances

[47:48](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2868s) with local storage for
optimal performance.

[47:51](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2871s) Now, I must say that we
try placing specific nodes,

[47:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2874s) but no matter how many variations we try,

[47:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2877s) Karpenter automatic selection
consistently outperform

[48:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2881s) in terms of cost efficiency.

[48:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2885s) We're done with tuning.

[48:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2887s) Now let's talk about what we
can do with observability.

[48:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2892s) We saw how Karpenter helps us
manage and scale our compute.

[48:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2896s) Now let's see how combining
the metrics from Karpenter,

[48:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2900s) Kubernetes, and Spark helps
us get some valuable insights

[48:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2904s) from our platform.

[48:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2908s) How many of you know
what is the percentage

[48:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2912s) of each data processing flow?

[48:36](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2916s) In compaction, we know exactly

[48:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2918s) what is the ratio of every processing,

[48:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2920s) and when it starts and ends
in each processing cycle.

[48:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2926s) Here you can see that
clicks take around 28%

[48:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2930s) of the workload, and start
at the middle of each cycle.

[48:54](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2934s) This allows us to see the distribution

[48:57](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2937s) and weight of each dataset
at any given moment.

[49:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2942s) Moreover, we can see daily,
weekly, and monthly trends,

[49:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2947s) and understand our system
and business implications.

[49:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2952s) Look at this metric.

[49:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2953s) We can see that click
processing was reduced

[49:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2955s) by 8% compared to last week.

[49:19](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2959s) And a different dataset
was increased by 35,

[49:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2963s) which might be a bit concerning, right?

[49:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2967s) By examining our Datadog query,

[49:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2970s) we can see that this information
can be easily obtained

[49:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2973s) by combining metrics from
Kubernetes and Spark.

[49:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2979s) But what happens when
we add Karpenter metrics

[49:43](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2983s) for price estimation?

[49:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2986s) Karpenter sends us cost
per instance and AZ,

[49:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2990s) and by adding to Spark and Kubernetes,

[49:53](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2993s) we can calculate how much
each data processing cost.

[49:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=2998s) So we get the price for
processing our data per minute

[50:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3002s) in near real-time.

[50:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3005s) This is huge, both for
engineering and business purposes.

[50:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3009s) You can tell how your
co-deployment affects the cost,

[50:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3013s) and take decision according to the trends.

[50:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3015s) You can even set a better pricing

[50:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3017s) for the service you
provide for your customers.

[50:23](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3023s) You can even take it one step further

[50:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3026s) by integrating this
into your data lineage.

[50:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3031s) Allowing you to determine the total cost

[50:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3033s) of your entire data processing pipeline,

[50:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3037s) you can decide what can be
optimized and what is redundant.

[50:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3042s) Combining your observability metrics

[50:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3044s) gives you a comprehensive
view of your data flows,

[50:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3047s) and allows you to take
data-driven decisions

[50:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3050s) about your data.

[50:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3055s) Well, all those metrics and
performance I showed you

[50:58](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3058s) worth nothing if only platform engineers

[51:01](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3061s) know how to use it and tune it.

[51:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3065s) And I showed you only
a few of the options.

[51:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3069s) We encourage and give our
data engineers full autonomy

[51:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3073s) and control over their
applications and platforms.

[51:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3077s) We of course provide best
practice defaults and policy,

[51:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3080s) but they can change in overall
depending on their needs.

[51:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3084s) Everything is being done
through our source code.

[51:28](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3088s) We created a detailed Git structure,

[51:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3090s) which defines the action of the repo.

[51:32](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3092s) Deployment units, both for
infrastructure application

[51:37](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3097s) and third-party integrations.

[51:39](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3099s) And environments, which
segregates between development,

[51:42](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3102s) staging, and production.

[51:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3104s) Each has its own Git or flow.

[51:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3107s) This approach allows us to
manage the infrastructure

[51:50](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3110s) of Kubernetes and application components

[51:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3112s) from a single interface
enabling automated workflows

[51:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3116s) and validation for
executions and deployment.

[52:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3120s) It protects us from configuration drift,

[52:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3122s) ensure we maintain the current state,

[52:04](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3124s) and allows us to spin up
and modify application

[52:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3127s) and the infrastructure within minutes.

[52:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3132s) And finally, this removes the dependencies

[52:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3137s) of our platform engineers.

[52:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3140s) It raises the velocity and
autonomy of the data engineers,

[52:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3144s) and contributes to the knowledge of both.

[52:30](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3150s) So at the beginning,

[52:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3151s) I presented that one decision
change our data organization.

[52:35](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3155s) As you notice, this decision
was moving Spark workloads

[52:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3158s) from EC2 to EKS.

[52:40](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3160s) Now let me show you the value.

[52:46](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3166s) This is a young version of me.

[52:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3169s) Compared to our old EC2
Intel by Spark clusters,

[52:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3172s) by using EKS, Karpenter, and Graviton,

[52:56](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3176s) we reduced our cost by 60%.

[53:00](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3180s) We improved our SLA by 35%,

[53:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3185s) and significantly enriched
our observability.

[53:12](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3192s) And the cherry on top, we
reduced the operational overhead

[53:15](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3195s) of our platform engineers,

[53:17](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3197s) and raise their overall
happiness along the way.

[53:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3200s) Thank you.

[53:21](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3201s) (audience applauding)

[53:25](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3205s) - All right.

[53:27](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3207s) So excellent presentation, thank you both.

[53:31](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3211s) If you take anything away, right?

[53:33](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3213s) Optimize and monitor EKS for
analytics and best practices.

[53:38](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3218s) Align tools and practices to
foster organizational growth.

[53:41](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3221s) So we saw the layers that
Christina talked about,

[53:44](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3224s) so you can be happy like Victor.

[53:47](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3227s) And provide APIs.

[53:49](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3229s) Remember, developers, data engineers,

[53:52](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3232s) data scientists are your
customers of the platform.

[53:55](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3235s) If they can't build, if you
can't provide them APIs,

[53:59](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3239s) all you're gonna have is
a platform not being used.

[54:02](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3242s) So enable APIs to empower data engineers

[54:05](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3245s) to work independently.

[54:07](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3247s) Autonomy, while you're still providing

[54:09](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3249s) the automations for control.

[54:10](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3250s) We have a happy union together.

[54:13](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3253s) So thank you.

[54:14](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3254s) Thank you, everyone, for joining.

[54:16](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3256s) Don't forget for session
resources like data on EKS,

[54:20](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3260s) you can click and scan the QR code there.

[54:22](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3262s) Thank you for coming, everyone,

[54:24](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3264s) and enjoy the rest of the conference.

[54:26](https://www.youtube.com/watch?v=AAwa5gc1XNA&t=3266s) (audience applauding)

