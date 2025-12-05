# AWS re:Invent 2024 - High-performance generative AI on Amazon EKS (KUB314)

[Video Link](https://www.youtube.com/watch?v=25tRVE2xq1I)

## Description

Generative AI models have opened up new possibilities in computing, but deploying them effectively can be challenging. Many are turning to open source tools on Kubernetes for solutions. Join this session to explore how Amazon EKS can address the infrastructure needs of generative AI, including GPU acceleration, scalability, and low-latency responses. Learn practical insights, see case studies of successful implementations, and discover best practices for using Amazon EKS to control costs while optimizing performance.

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

- Okay, good morning. Welcome to KUB314. We're gonna talk about how to
run Gen AI workloads on EKS. I assume many of you in the last couple days
have been to the keynotes. I think Peter was Monday
night, Matt was yesterday. I just heard there's a
machine learning keynote going on as we speak. So thank you for coming to this talk. And many of those keynotes, they're talking about machine learning, generative AI features
that are coming out. Graviton4, Trainium2 UltraServers, all of this cool stuff. And I think a lot of you in
this room are saying, yeah, that's great, but I can't use it unless it works with EKS and a lot of customers, some of the largest
foundational models out there, you see a lot of them were
trained on Kubernetes. And that's exactly what
we're gonna talk about today, is the work that EKS does to make running, Gen AI is in the title, but really any machine learning workloads easier to do on EKS. And I'm joined by Rama who's gonna talk a little bit about why EKS and Kubernetes has become a
good fit for ML workloads. And then special guest, we have Cas from Eli Lilly and Company who's gonna talk about how they've built their
machine learning platform on EKS and the success they've seen. Okay, super quick, why generative AI? What is generative AI? I know all of you probably know this, maybe some of you had a late night. It's the first talk,
I'll go super quick here. AI that can produce content that looks like human content in a lot of cases you can't
even tell the difference. And it's powered by
foundational models that have up to several hundred billion parameters probably by next year
approaching trillion parameters. And the real innovation with generative AI is that you can reduce the
time to build ML applications because you start with these
huge foundational models and then it takes only a little
bit of training to fine tune and do what you need to do
for your specific tasks. As far as use cases go,
really four main buckets that we've seen for
generative AI use cases, probably the one you're most familiar with is the enhancing customer experience. I think Andy came on stage yesterday and was talking about Rufus, the new agent that can help you shop on amazon.com. Boosting employee
productivity is another one. Another few announcements yesterday we had were code migration tools. I think we talked about
at Amazon how we've saved, I don't know, X number of developer hours moving from Java 11 to Java 17. I think we also announced a Windows modernization code migration. So that's a use case we see a lot. Content generation, image
generators are cool, video generators are cool. And I think the more interesting one is business operations. I've actually talked, I've had a lot of customer meetings
in the last couple days and a lot of you are already using Gen AI and some of the platforms you're building, whether it's doing log analysis to do faster troubleshooting, onboarding your developers
faster to the platforms building. So we're starting to see some use cases that are actually working. Some of the trends we've seen, more complex generative AI workflows, agents talking to agents, you know, moving to production
models require guardrails, other sets of capabilities. And I think the last one
is the most interesting, AWS, you've gone to the keynotes. AWS has a lot of different tools. Bedrock was talked a lot about yesterday. Amazon Queue, we have a lot of different layers of the stack. EKS is towards the bottom of that layer where you really need
the most flexibility, the most customization, the
highest levels of scalability. But I imagine in a large enterprise, you might be using a mix of EKS, Bedrock, Queue, other tools. If 2023 was the year of
gen AI, proof of concepts, POCs, we've seen 2024 be
the year of production. And moving to that production mindset really requires a
different way of thinking. You need to start thinking about how are we gonna make money or save costs? You know, we can't just run POCs forever. And you start to think about cost of inference at scale, latency at scale. You may just not want to pick the highest performing best model. You need to weigh that against
how much is it gonna cost me to run that in production? What is the latency, how is it gonna impact
the user experience? And then when you move to
production, you also need to think about things like security, compliance, ethical constraints. So there's a lot more
and a lot more effort that goes into building
a production application. And that's really the trend
we've started to see this year. So I'm gonna hand it off to Rama to talk about some of the
generative AI challenges and how EKS helps solve them. - Thanks Mike, hey folks, good morning. I'm Rama Ponnuswami, I drive worldwide, go to
market for AML on EKS. So talking a little bit about some of the common challenges that we see our customers face when they start to scale their gen AI workloads in production. It's sort of along three
different buckets, right? Like as Mike was saying,
there are different needs for your different teams
within a single organization. And one model is not gonna
fit all of them, right? So more than likely you'll
have to run multiple models, different ways of customizing those models to fit specific needs of different teams. So that comes with the added
burden of day two operations. How are you gonna manage the
versioning of those models? How are you gonna upgrade these models when new models show up? How do you build guardrails
against these models? And how do you manage access
to data for these models? Because customizing these
models is not gonna be easy. Customizing models requires
specific curated data that is domain specific and fits your particular specific use case where you want these models to be able to drive tasks specific
to that domain, right? And that also means that you are having to integrate multiple data
sources, having to manage access to all of this data all while maintaining your
data security requirements. And last but not least, all of this means that you are having to
manage massive scale of infrastructure, which gets trickier. We have seen a lot of our customers, when they start to scale
or hit critical scale in their production, they start to feel that delegating more of your infrastructure
control makes you less capable of controlling any of
these parameters, right? So we start to see customers
as they hit some critical scale and production of Gen
AI workloads, they want to have more control
over the infrastructure and start looking at options
like EKS where they can get that necessary control
to be able to customize all of their models and the ML environment that they want to operate in, and to be able to optimize on their cost to meet their ROI targets. So those are challenges at
the organizational level. Let's think a little bit
about what are the challenges of a data scientist or an ML engineer on their day-to-day operations. Data scientists don't really want to be managing infrastructure. All they require is a rarely
available infrastructure that they can just code deploy
their model and scale on, and they don't really want
to be doing boiler paid code or scripts that they need to run in order to manage the
lifecycle of their ML models. Instead, they want a
readily built platform that can help them with
all of those capabilities that they need to effectively deploy and scale their workloads
going further as well. And they want to be able
to meet these requirements in a more optimized
manner, in a repeatable way that they can just keep doing it over and over again instead of having to build something in a very
individualistic ad hoc manner each time they need to
build and scale a model. So to summarize in terms
of the key challenges or considerations, if you will, in terms of deploying generative AI in production, it's along three lines, right? You want to be able to move fast, you want to enable your data scientists and ML engineers to
build their models fast, deploy them fast, and be able to scale as they go forward as well. And the second thing is about how do you enable customization
of your models right? At scale. You want to be able to
customize multiple models to fit specific use cases within different teams
in your organization. And you also want to be able to ensure that these models will be able to scale, not just to meet the demands of today, but seamlessly scale to meet the demands of the future as well. And how do you ensure that you're able to continuously optimize on your costs as you're hitting higher
scales going forward? Scaling up your ML models as well. So this is really where
we see a lot of customers mention that EKS makes
a lot of sense for them, especially in environments where they need a lot more
control over infrastructure to meet data security concerns,
to meet cost optimization concerns because they need
to hit the ROI targets, so on and so forth as well. So let's sort of dissect, where does EKS provide these benefits? Why do we see a lot of our
customers start to leverage EKS for deploying the generative AI workloads? It's again, along those buckets of how does EKS enable you to move faster? It's twofold, right? The first is, in most cases where customers already have
standardized on Kubernetes as the way to do their
application development, they get to just extend
that existing platform and deploy ML models on top of it because they already built
foundational capabilities that they also need
for their ML workloads. The second reason is availability of open source tooling, right? ML space in general is fast moving and a lot of those
innovations are happening in the open source arena, right? And these open source tools,
most of them usually come with out of the box
Kubernetes integration. So with EKS customers can just integrate that ML specific OSS
solutions on top of it and enable their data
scientists to just move faster by providing them all end to end ML ops lifecycle capabilities, as we saw earlier, that's one of the key challenges. And in terms of scalability, Kubernetes and EKS as such provides
native integrations to all of AWS ML infrastructure services, enabling you to continue to scale seamlessly as
your demand increases for your ML models as well. In terms of customization, because you are getting control of your entire infrastructure
right up to the instance level with EKS, you are able to flexibly configure your environment to suit your specific unique needs, and you are not going to be restricted because of a certain
feature that we provide. And you know, we don't have restrictions in terms of how you can configure your ML environment within EKS. So that enables you to
customize it to your liking, to suit your specific unique requirements. And because you're able
to have multiple choices in terms of instances,
you are constantly able to choose the right infrastructure sizing, the right instances, and be able to optimize
on your cost continuously as you start to scale further with your ML workloads as well. So let's go a little deeper on how does flexibility
and cost optimization work on EKS for ML, it's really across three layers. The first is at the instant level because EKS supports all
of the EC2 instances, GPU, Nvidia based, GPU instances,
Trainium, Andreia, Intel based instances, so on and so forth. Any EC2 instance that is available on AWS, you can leverage it with EKS. So that lets you choose flexibly
which instances you want to use based on the workload and based on the
requirements of the workload. So this is not just
gonna be enough, right? Like ideally you don't want
to be making these choices manually each time a new workload comes into for scheduling. And that's really where the power ofKarpenter comes into the picture. With Karpenter, you can
effectively automate all of these choices by providing it the parameters under which you want to provision a specific instance and make it evaluate the incoming workload to choose the right instances for it. All of this gets automated by Karpenter and it's repeatedly
doing this on your behalf whenever a new workload gets scheduled. And on top of that, Karpenter makes provisioning much easier as well. So Karpenter, along with
our EKS optimized army comes with all of the inbuilt
dependencies that you need and you are able to
quickly spin up instances whenever your demand goes up and Karpenter gives you fast scaling, but more importantly,
it also scales back down whenever your demand is not going up. So you are able to cost optimize on that front and you are also able to leverage GPU sharing mechanisms. And with built-in multi-tenancy of EKS, you're able to effectively share your constrained GPU resources securely across multiple teams
in your organization, shooting up your utilization
of GPUs further as well. And on top of that, you get to integrate ML specific OSS solutions, the whole ocean of solutions available out there. You get to pick and choose the right tools for the right functionality that you need within your
organization to then integrate it with EKS and get all
the flexibility you need with the ML specific functionality your data scientists desire as well. In terms of, I wanted to quickly highlight very few customers. We have a lot of customers
running Gen A on EKS, but I wanted to pick a select few that have been able to
reap certain benefits by deploying generative
AI workloads on EKS. Vannevar Labs is a defense tech startup. They supply unconventional intelligence to national intelligence
agencies and defense departments. So they operate at the
highest level of secrecy and data security concerns. They were able to utilize EKS and Ray and Karpenter together to achieve 45% reduction
in their inference costs. And they were able to do
this by using mixed CPU and GPU instance types and being able to schedule CPU heavy workloads on GPU instances to utilize the under used
CPU, within the GPU instances. So overall, increasing
their GPU utilization by a huge margin. And we have recently
published a blog with them. If you're interested in learning about the specific configurations that they did to achieve this cost cut, please feel free to check it out in our AWS containers blog channel. The next is Informatica. They are another customer that have built an LLM
ops platform to train and fine tune multiple
LLM models on top of EKS. They were able to achieve
around 30% of cost saving compared to managed services
that they were using earlier. And they were able to achieve
enhanced configurability because they were sort of constrained by the managed services
customization ability that the managed services
was providing them. And Zoom is another
customer that has been able to create a similar LM ops platform where they do multimodal hosting and they're able to reliably and efficiently scale to meet their ongoing demand as well. Another key customer I wanted
to highlight is Hugging Face. If we have used the Hugging Face hub, the freemium pricing
one, the three tier one that basically runs on top of EPS today, the challenge that they initially, when they started out
building that platform was they had to build a platform that would enable inference of millions of models with dedicated
inference endpoints and a lot of different domain names had to be hosted there as well. And all of this needed to be provided with three tier pricing. So it was a challenge that they had to hyper optimize on their cost, on their infrastructure cost
in order to be able to afford to provide this as a
freemium price tier as well. So the solution they've
taken is to deploy it on EKS, multiple EKS clusters, 2000 plus nodes, and they're able to effectively pin pack a lot of parts within
very fewer instances. And they're also able to
use time sharing with GPUs where they swap models in and
out every few seconds as well. And with this, they're effectively able to provide this platform across the world for ML developers to collaborate on. So I mentioned something
earlier, customers that already have Kubernetes
as a standard platform for their application development. This sort of a snapshot of how those platforms look like, right? They build all of those
foundational capabilities already into this platform, like how to do logging, monitoring, disaster recovery, security at scale. All of those challenges have been solved. And customers, when it comes
to ML, they don't want to, again, solve these challenges
or reinvent the wheel, right? They just want to use all of
these foundational capabilities and extend it to run ML
workloads on top of this as well. So that's one key advantage. The second advantage is customers
are able to use Kubernetes as the standard layer across
all of their environments, be it on-prem, be it in the
edge, be it on cloud as well. So providing, using Kubernetes helps them unify these operations. And if you have been paying attention to the recent releases we did last Sunday, we released egress hybrid nodes as well, making this much easier
for customers to do with EKS hybrid notes, you
get to attach node on cloud, on premises, on edge into a single EKS managed
control plane if you desire and you get to offload all of the Kubernetes
control plane management and you get to have sort
of a logical mapping of your infrastructure across
all of these environments, providing you a better way to utilize your GPU resources wherever available and to cost optimize as
you go along as well. You can pick and choose
which workload gets deployed in which environment based
on the cost ROI benefits that you expect out of
those workloads as well. So in terms of what we
have seen customers do and when they try to
extend these platforms is, as I mentioned earlier on, integrate OSS solutions
on top of it, right? That lets Kubernetes do what it's good at, which is infrastructure orchestration. And you integrate OSS solutions on top, which provide you ML
specific functionality. For example, we've seen a lot of customers adopt VLLM together with EKS that provides you a lot of
functionality like memory and model optimization,
multimodal management, request batching, query queuing, so on and so forth for
inference infrastructure. So this can provide
you a readily available inference endpoint or an inference stack that you can make available to your data scientists
that they can just deploy a model and get an endpoint where they can run their inference out of. So in a sense, to summarize all of this, when customers use EKS for generative AI, what they've been able
to get is more control of their environment to
be able to customize it, to fit it to their specific needs, to be able to scale seamlessly
to meet future demands and be able to continuously cost optimize to meet their ROA targets. So with that, I will hand out to Mike to talk about the specific
features that EKS provides. - All right, thanks Rama. Okay, I'm gonna do a bit
of a rapid fire overview of a lot of the features we've launched in the last 12 to 18 months to make it easier to run AI ML generative AI workloads on EKS. First, this is more a concrete picture of what Rama was just talking about of all the tools out
there that you can use to get started, there's really two parts. The open source stack, very rarely are you starting from scratch. And Kubernetes Rama mentioned
Ray, VLLM, Jupyter Hub, all of these tools work with Kubernetes and it's really the flywheel effect that we like to talk about at Amazon because say you're gonna try to author a new machine learning tool,
you have a really good idea. If you want to get adoption of that, you're very likely gonna
make sure it works well on Kubernetes as one of your
first deployment targets. And a lot of these frameworks
tools out there do just that. They work well in Kubernetes. Certain ones of these we
choose to contribute to. We've made some some contributions to Ray and make sure it works well
with the neuron frameworks. And then at the other end
at EKS is we make sure that the infrastructure innovations and services at AWS that power this large
scale training inferencing work well with EKS. So CSI drivers, ECR, a lot of
those foundational services that you need to use with ML workloads, we make sure they work
really well with EKS. Okay, features, this one, we don't give enough love to I think the work we do for scalability of the control plane. We rarely ever do a what's
new post EKS is, you know, a little bit more performant. But I know for a fact we have customers that created EKS clusters six years ago when the service launched and they've just
continuously upgraded then from one dot 10 all the way up to one dot 30. And those clusters look nothing like they did when they
launched six years ago. So every time you create an EKS cluster, we're creating dedicated
infrastructure for you. EC2 instances, nat gateways, NLB, and we do a lot of work there. It's over time to
continuously add performance, whether it's newer instance
types, faster volumes, you know, better networking. And one of the projects we've done a lot of work on this year is
changing the way we manage at CD to really get to much higher scale. We have certain customers
that are asking us for 10,000, 20,000, 50,000 node clusters. And in order to make that happen, we've had to do some
pretty major refactoring to the way we manage at CD, which is the backend
database of Kubernetes. So likely next year, we'll
publish some more on that, but that's something
we've been working on. EFA is an example of a lower
level infrastructure innovation that AWS it's a OS
bypass hardware interface that allows high levels of
multi-node communication. We make that easy to use with EKS and Kubernetes with a device plugin. I think a couple notable
recent enhancements, EFA just added support for
cross subnet communication. You used to be limited to
a single subnet with EFA. Now you can do cross
subnet within the same AZ, you don't necessarily wanna
do training across AZs because that's expensive, but that helps with IP address exhaustion. And then the other thing
that helps with IP address exhaustion is oftentimes
your ML training workloads, they're sitting there just
crunching, doing a lot of math, they don't actually need
to talk to the internet. They only need to talk to each other, the other nodes in the cluster. So we recently added support
for EFA only ENI support, so you don't have to
add actual IP addresses to the EFA devices in your cluster. And that's now supported on EKS when you're running large
scale training jobs, you need a large scale storage backend to handle all of the data
that you're processing. And there's probably no
larger scale storage backend in the world than S3, S3 open source to technology called Mount Point last year that allows you to mount an
S3 bucket to an EC2 instance and use file system commands. And they get automatically
translated to S3 object commands. And we've made that easy to use, again with EKS via a CSI driver,
Kubernetes native interface. Recent notable enhancement
is the CSI driver added some more fine-grained
access controls. So you can lock down, you
know, which training pods in your cluster have
access to which buckets. Generative AI training
inferencing is not cheap, these instances are in high demand. They cost more than
standard CPU instances. AWS has done a lot of work
over the last five years to bring down, improve price performance, lower the cost Trainium. I think just yesterday
we announced Trainium2 and we'll continue to
innovate at the lowest levels of silicon to make sure
we give you the best price performance for Trainium workloads. And again, these are great, but for, for those of you in this room, it's not helpful unless it works with EKS. And in the last couple of months we've introduced accelerated armies for both Amazon Linux 2023, which is the newest general
purpose Linux distribution from Amazon, as well as Bottle Rocket, which is our container
optimized operating system. These work with all of the
various EKS compute options, self-managed node groups,
Karpenter management groups and probably again, one
of the underappreciated or under talked about things
we do here is the testing behind the scenes, the amount
of drivers, frameworks, libraries, Cuda toolkits,
like all of these things that go into an is complex. They change fast and we have
a pretty sophisticated testing framework where we're
running training jobs, inferencing jobs before
we release these ams. So you can just take them, run them and be confident that they're
gonna work for your workloads. Specifically for training workloads, I know we talk a lot about
Karpenter these days, but Manage Node Groups is our original managed compute
product that we launched, I think five years ago at re:Invent now. Now and Manage Node Groups
is actually a good fit for training workloads because often training
workloads are not dynamic. You just have a large
static pool of capacity that you need to run your training job. It's not going up and down often. So manage no groups is
a good fit for that. And EC2 launched a
feature a few months back called capacity block reservations. Again, I mentioned these
instance types are in high demand and capacity blocks is kind of like a hotel
reservation system, but for EC2 instances, so
up to eight weeks in advance you can book capacity for GPUs and you know you'll have
it at that specific time. Recently they just gave the ability to extend the reservation and that now natively works
with managed node groups. So particularly for training workloads, we think this is a nice enhancement. GPU instances do tend to fail more often than
than CPU instances. They're running complex math calculations. I know the EC2 team is doing
a ton of work, you know, at the data center level to try to increase the performance. Things like, I don't know, 1% changes in humidity in the data center can give a 10% increase in the
lifetime of a GPU instance, but they do fail on occasion and we've put a lot of effort this year into detecting those failures. So you don't have an instance
that goes bad and your cluster and is wasting money while it's not actually doing any work. So this actually rolled out for EKS auto mode just this last week, which I'll talk about it in a minute. It'll be rolling out for other
compute over the next week or two, but it's really two parts. It's the node health monitoring
agent, which is an agent it'll run as a Damon said in your cluster, look for all kinds of issues. We have six years of experience of running lots of Kubernetes clusters. We've seen every possible
way a node can fail. And we've taken that knowledge and built it into this node
health monitoring repair agent with a specific focus on GPU instances. And then on the auto repair side, managed node groups will get to the auto repair functionality where you can opt in to say, okay, EKS, you detected an issue. In some cases maybe you want
to recycle the instance. In other cases, maybe you want to reboot the instance depending
on the type of failure. And that'll be rolling out very soon. And then my last slide is on monitoring observability. I think it was at re:Invent last year. We launched version two of of
CloudWatch Container Insights, which it's a lot better than V1. If any of you had tried V1 a couple years back, had its challenges. The new version of
CloudWatch Container Insights is really, really nice. It's also more cost effective
for container workloads and a recent enhancement to
the Container Insights plugin. And you just run this as an
agent in your EKS cluster, is it now automatically
includes the monitoring plugins for both NVIDIA and neuron instance types. It'll scrape those metrics,
send them to CloudWatch, allow you to monitor how efficient your GP or resources are consumed,
do things like understand how workloads are running, you know, figure out how to tune hyper parameters. There's a lot of work
that the team did there to make sure that you have a simple out of the box check checkbox, GPU, Nvidia monitoring experience. So I highly recommend
you check this one out if you haven't seen it. Okay, I wanna talk
specifically about inference. I mentioned at the beginning, 2024 is the year of production. And production generally
means inferencing. If you have a live workload,
you're serving requests to your customers and
that brings challenges, especially with these, you
know, large language models. Running inference at scale
can be complex, you know, how do you, how do you serve
models that are cost effective, that have the performance you want? Latency, throughput, availability. All of these become concerns when you're running inferencing at scale. And how we're thinking
about inferencing at EKS is really there's those three
measurements on the left, the throughput, you know, how many tokens per second
your model is serving, the latency, which is the
time to the first token, and then cost, which is really
the GPU compute utilization, how much of the GPU you're actually using. And so a lot of these
features we're building and framework enhancements
we're doing are designed to help you achieve that trade off between throughput, latency and cost. There's never gonna be a perfect answer, but we want to give you
the tools to make it easy to do that trade off for yourself. Scaling to zero, scaling up quickly. Optimizing ML container images. This is something we're doing quite a bit of work in the container D project. You know, oftentimes
these ML images are tens, sometimes I've seen hundreds of gigabytes. And when you start your instance, so you don't wanna wait 15
minutes while the instance is costing you money and the
image is being downloaded. So we've done a lot of
work there to speed up that I just talked about
minimizing hardware failures. And then we're doing a lot of contributions in the open
source space to make sure that a lot of these popular
frameworks do work well on EKS and speaking of them, yeah, Ray VLLM, these are two of the, and
even in the last two days in customer conversations I've been in, I've heard these two projects
mentioned more than any others is the ones that customers are now using to serve inference workloads in production using things like the,
the device plugins, EFA, Nvidia neuron accelerated drivers, all of that is a very
common infrastructure stack that we're seeing customers
use for inference with EKS. Oh no, what happened? Okay, I dunno what's happening there. Anyway, we'll skip, Rama
already talked about Karpenter, but Karpenter really is the tool that, especially for inferencing, I mentioned Manage Node
Groups is good for training. Inferencing is generally a
much more dynamic workload. Karpenter is a good fit there because it can help you
more easily take advantage of the breadth and depth
of VC2 instance types. In some cases you may want
to use Graviton instances for inferencing, maybe
you don't necessarily need to use GPU instances. Karpenter in general, we're
seeing a lot of success with customers do for inference workloads, and hot off the press, some of you maybe saw announcements
over the last couple days, but we introduced what
we're calling auto mode the other day, and part of auto mode is integrating Karpenter into EKS, making it easier to use. Auto mode is really the new easy button for the Kubernetes data plane, the compute storage networking that you generally need
to run in your cluster now is included by default in EKS. And I'm specifically bringing
it up in this presentation because of the Karpenter angle. Karpenter's good for inferencing, it's now built in by default. Some of the, you know, the
three things on the right, compute optimization, cost efficiency, supporting diverse workloads, that's really built in Karpenter. That's what it's doing. The interesting innovation that we did with Auto Mode, if you haven't been to any of the presentations
yet, is we have this new operational model with EC2. Where previously you had
two ways of running compute in AWS you had the fully
managed lambda fargate model where computes running
in a AWS owned account or you had standard EC2
that was, you owned, this new model EC2 managed
instances they're calling is in the middle of that
or it's an EC2 instance in your account. But an AWS service like EKS actually owns the
lifecycle of that instance. So if you go to try to delete an E and I, delete the instance, you
get an error that says in use by a service and you
have to use that through EKS. And I bring it up because
I think especially in the top right here, the capabilities, a lot of the hard parts of getting started with machine learning workloads on EKS, which is figuring out
the right device drivers, the EFA plugin, configuring
instance storage. If you have local disc
instances, you know, customers used to have to
do these really complicated user data scripts to set up a raid zero
volume on the instance. A lot of that is now fully
automated with EKS auto mode. So we automatically configure Raid zero, we automatically configure
the device plugins, whether it's Nvidia or Neuron, we already include, you know, if you launch a GPU instance, we're gonna pick the right omni
that matches that instance. So just, there's a lot less work you have to think about. For training workloads, I'm not gonna quite say
automotive is a great fit yet, there's a 21 day max instance lifetime. A lot of times we talk to customers who are running training jobs that go for months in some cases. But I think for inference workloads, for production running models and production auto mode,
it could be a good fit. Just an example of a pretty common stack that we're seeing. And again, this is validated
in the last two days of conversations I've had with customers, but using Ray, VLLM and you know, you're using Karpenter, which is gonna spin up
a standard CPU instance to run the head pod and
the cube ray operator and then it's gonna spin up, for example, inferential instances to actually run your serving workloads. So this is a more and more
common pattern we're seeing for customers actually
running inference workloads in production with EKS. And then finally, just a
few more customer stories, H2O, Omi, Unitary, all of these customers, I believe these are all
either case studies, blogs you can go read about. They've all moved to Karpenter to do their inferencing workloads. I think H2O is an
interesting one they've done, they're using bottle rocket
to prefetch container images. We have a a nice blog out there that shows you how to do that. I mentioned the 15 minute time it takes, yes we can optimize that, but the fastest way is
actually just gonna preload the container image on
the instance itself, which you can do with Bottle
Rocket quite easily now. And other ones, yeah, just using Karpenter, reducing costs. We've seen a lot of these
customers have success moving to Karpenter to do
their inference workloads. Okay, I'll hand it off to Cas to talk about one of
those customers who is one of those customers who's
been successful with EKS. - Cool, thanks Mike. Hey everyone, I'm Cas Starak, I'm a product manager leader
at Eli Lilly and Company and I focus on research and AI products. And just gonna share a little
bit from a customer experience of building gen AI capabilities on EKS. And I thought to start, I could just talk a little
bit about the tech evolution at Lilly and maybe help
explain why someone from Eli Lilly is on an EKS
Gen AI track at re:Invent. I'll talk a little bit about
our platform development including EKS and then the Gen
AI scale up that's underway. So just a little bit
of historical context, the pictures here tell a
little bit of Lilly's history with technology on the
left, it's actually 1987 and some classic eighties
corporate executives, very excited about the
most recent delivery of some personal computer technology. And then on the right, some
of you might know what that is or you can see the text there, it's actually a Cray-2 supercomputer. And in 1989, Lilly was the first
non-governmental organization to purchase one of those in the US. And I just share that because after joining Lilly a year ago, I was pleasantly surprised
to learn about this history of early technology adoption and innovation that I
just, I didn't expect to find in 150 year old company. And there was, you know,
the software development and the data science and
everything else that came along with adopting those technologies. Now, unfortunately, it was not just a, you know, upward trajectory from there, similar to the so-called AI winters that, you know, that
industry has gone through. We had some of our own kind of technology innovation winters, and it really started around 2001 in what in terms we call Year X. And that was the year that the first Prozac
patents started dropping and going off patent. And at the time that was actually 1/3 of Lilly's profits. We had some other medicines
that went off patent. And you can imagine as sales
come down dramatically, there was a lot of examination of costs, bring down costs and
things that were, you know, quote, unquote non-core
like software development and some of that technology
innovation was very hard hit. And so there was this long period where I think some of
that early innovation started to atrophy a little bit. But you flash forward today
and it's completely flipped and there's a recognition
across the company that we really do need
to become a tech company to continue succeeding
as a medicines company, you know, for years and decades to come. And thankfully we've
been successful with some of our recent medicines, we
have a very strong pipeline and that's enabling us to invest and there's been significant investment and growth in those tech capabilities, software engineering capabilities, robotics automation, data
science, all types of AI. And there's, you know,
much more of that coming. And you know, one of
the things we're doing as we're going through this evolution and making these
investments is really trying to adopt, you know, most of the modern software
development practices. And part of that is, you know, a team was formed just a couple
years ago that I'm part of. This is the software
product engineering team. It's led by a former
Apple engineering leader Go Cole Rad Krishnan. And this team really focuses
on building scaled products and platforms that are
gonna be high reliability, high usage. And we try to take an approach that's really a kind
of software engineering center of excellence to help demonstrate and kind of spread those practices across the developers at Lilly. And a big part of is
this platform approach where we're thinking
about shared libraries, reusable components. We tend to leverage a lot
of open source capabilities and tools and doing things like building broad observability tools that can get used across the organization. And one of the platforms that's
been a really big investment for us is this CATS platform. And so this is a cloud applications and technology as a service. And what this is is a
comprehensive cloud application development and hosting solution. And so we built this on AWS and we use a series of open source and AWS managed services to support it. And this is a highly simplified diagram, but some of the key points,
you know, we use EKS for Kubernetes management, we use EC2 and Fargate for container execution and we have other AWS
services integrated into it, like S3 RDS, secret manager,
a whole slew of things. We also do GIT ops, CICD automation. So teams can go kind of seamlessly from commit to production. So kicks off with GitHub Actions, docker image push to ECR, Argo detects and then
automatically puts that into the right Kubernetes environment. And so, you know what
this means for developers, it's really been a newer way of developing we've shifted to the
cloud, they get, you know, a lot of speed and efficiency so they don't need to make a bunch of infrastructure
decisions, let alone build that infrastructure kind of laid out, you know, a menu for them to get started and then they obviously have the speed of that automated deployment. So that's been a big part of our kind of tech transformation
evolution to the cloud and it's gotten significant usage. It also brings security. So we have a lot of standardization and we kind of, you know, lay some tracks that we get people to follow. And so that gets them into robust, you know, security practices. We have vulnerability scanning, we've also provided observability
tools, so some of those with the Amazon services. We also use some open source
tools like Loki and Grafana. So that teams building on this,
they get a lot of logging, alerting, reporting,
visualization that can help them, you know, manage their
applications as they scale. And that last part's
really the biggest benefit is the scale and reliability. So, you know, once an
application is developed here, it can scale up to, you know,
all of Lilly's workforce, it can scale up globally and there's really no
additional work for the team and it maintains high
reliability when it does that. So as I've mentioned, we've
seen significant adoption over the last couple
years on this platform. We've got hundreds of developers using it. We've got growing number of applications, growing number of commits
increasing exponentially in, you know, global deployments across, you know, many, many countries. And one of the metrics I like, I sat in the intern end of summer readouts and it felt like almost
every intern mentioned CATS, using it and how it helped accelerate the development of whatever
their intern project was. So I think that's a good
measure of its effectiveness. And so you can imagine
some of the increase in usage of this, A lot of
it is coming from gen AI and we've been making
big investments there. And just to give you some context, really what Lilly's looking to do is lead our industry in terms of, you know, pharma peers in the adoption of an impact from gen AI. And we do think it's
fundamentally transformational to a lot of the work that we do and we've already been investing in it. So Lilly actually has
a history of using AI for drug discovery, small
and large molecule tools for generating its screening and there's actually a pretty
solid data science team that's been doing NLP work before all the LMS came out to do things like clinical summarization. So there's a history of
that that we're building on, but we're really going all in on gen AI and we're working with the
hyperscalers, we're getting, you know, out of box
solutions, we're working with smaller companies, startups for more, you know, organization or use case specific solutions. But then we're also doing a
lot of internal development and as part of this tech
transformation we're going through, we are looking where
does it make sense for us to have some of those
capabilities internally? And some of that is use
case and proof of concept, but really we try to focus
on what are scaled products and platforms that can serve the company. And one of the platforms
that we decided to build was a, you know, broadly usable developer facing gen AI platform to help accelerate that work at Lilly. And I can actually a little bit here. So we knew gen AI is
gonna be big, we want it to be reliable, we wanted
to be able to scale large number of users globally. So we decided to build it
on top of that CATS platform that I just walked you through. And we put together these main components and we started this development in 2023. We had our first production
release in December and we've been adding features and capabilities as we've
gone through the year. At the foundational level
it's a model library, so we want teams to be able to choose from the
latest and greatest LLMs and we're constantly
updating it, you know, we're big fans of the
anthropic line of models, but we also have Open AI, Gemini, hugging face, lama. You deploy pretty much any
model from hugging face if you get the legal approval. And we allow teams to
choose, you can host those as retail, we have open source, there can be fine tune models, you can host them locally
in our GPU cluster. And then on top of that we
built orchestration tools. So it started fairly simple and we use lang chain as our
main orchestration framework and we started fairly
simple with some tools for prompt engineering and model chaining. And we've added in, you know, more and more
complex orchestration tools and you can now support agentic workflows and multi-agent systems with it. And then we have tools for operations, scaling and maintenance. So we try to take care
of a lot of the scaling that the teams are gonna need so they don't need to worry about it. So our central team, you know, has an ops team thinking
about provisioning capacity. We recently worked with the
AWS team to help optimize some of our like cross regent inferences and our rate limiting capacity to help get better performance
at scale, lower latency. And so we're kind of doing
those things centrally so that other teams don't
have to worry about it as well as quality and monitoring. So we've created various
eval tools so that teams as they're scaling up
can monitor for drift or if they want to assess,
you know, the latest model, they can easily check
how performance changes. We also have data
integrations that, you know, where they're specific
to the Lilly environment. We're always trying to add new ones there and information retrieval tools. We started with a fairly kind of vanilla semantic search capability vector database and we've been adding in more complexity, we made elements of that tunable. So if teams wanna optimize things like, you know,
chunk size and overlap, they can get in there and do that. And then we started adding other things like contextual chunking and hybrid search and continuing to prove
the information retrieval. So again, teams don't need
to go out and build that. And we have it kind of optimize
to the Lilly environment and all of it's wrapped in this oversight in compliance and security layer. So we have full input output logging, cyber has visibility into that, into all of the configs, all of the users. We also have scanning and alerts, it's configurable by our cyber team. We use some AWS tools as well as some open
source tools to do this. And it helps give a lot of
reassurance to our cyber team and actually kind of points
this as a preferred platform. And so what that has
allowed us to do, again, we've been able to accelerate development so teams are able to
get started very quickly and get to POCs and MVPs quickly. They have optionality. So you heard the guys earlier
talk about the importance of, you know, different models
for different use cases. I think Andy talked about
it in his keynote yesterday. And so teams can easily
switch back and forth and figure out which model
is right for their use case. I mentioned, you know, quality
security compliance built in. And then because we've
built this, you know, on AWS on EKS, it's very scalable. So we've had use cases that
have gone from, you know, small early testing to deploy
globally without, you know, having major issues or downtime and not requiring a ton of work from the teams
actually doing the development. And so, you know, we
launched it originally into production in 2023 in December. So it's been, you know, less than a year and we've been impressed with the uptake and it's really impacting
every part of our business and we see this transformation happening. Just some examples,
probably my favorite one is this agentic discovery assistant. So there is a chem informatics agent. It has access to about 20 different tools. Some of those are chemin
informatics tools, some of them are internal databases with Lilly molecule information. They're external databases and we have an LM that's,
you know, answering questions or executing, you know,
user prompt workflows and choosing which of those tools to use. And it allows these very
powerful workflows to be executed that can aid our scientists
in early stage discovery. We have things in the
clinical trial space, so helping with how we
respond to regulators. We get thousands of questions and have to answer those from
regulators all over the world. It's a natural thing for LMs to help us do we have tools in our manufacturing space. So we have global manufacturing, there's a huge focus on our
manufacturing line uptime. And so we have this assistant that's been developed using this platform that uses structured and
unstructured data from like SOPs as well as equipment sensor data to help as our line operators
monitor and manage uptime. There's claims drafting tools and we're even developing
our first patient facing Q&A tool on the platform. So it's exciting to see that adoption. And then in terms of results, we've seen the acceleration, so we've heard it anecdotally from teams and then we've seen teams,
you know, in a little as a few weeks they're
able to get a POC out there or in a few months, actually have an MVP that's pushed into production because they have these
tools ready and available. We're able to meet quality
security compliance. It's really become a preferred
platform from our cyber team and you know, they
encourage folks to use this because we have all of that
visibility, logging and alerts and then it's enabled rapid scale up and we've seen a lot of adoption. So we have over 500 developers
at Lilly using the platform. There's thousands of end
users in over 30 countries and in a given month we
have billions of tokens that are processed by the platform. So the scale has been, you
know, what we were hoping to see and it's supporting this
tech at Lilly evolution. Obviously we're building
products on top of it that are impactful, but because
of the work we're doing, it's also this kind of
virtuous cycle of attracting and retaining, you know, talent
that wants to work on this. And it's kind of supporting that transformation I was talking about. And you know, lastly, just to
close, some lessons learned, I would say the main lesson is, you know, our kind of belief and intuition that having this platform approach, so using a scalable platform, you know, like EKS building this, you know, somewhat opinionated approach
to gen AI development. It's worked, we have developers using it, it's accelerating it,
we're seeing things scale, we're seeing things move into production. So I think that's probably
the biggest lesson learned. But some of the other
things along the way, if you build it, you know, some will come. So when you build a platform like this, you're gonna have the few early adopters that just naturally just start using it. Especially in a place like
Lilly, you'll have kind of that top of the curve
really capable, you know, fast moving developer teams but then there's you know, a whole distribution curve after that. And if you wanna get more
adoption, there's a lot of work around evangelizing, answering questions, getting support documentation out there, getting support teams, product mindset. So we've really treated it like a product. We have product manager or roadmap. We're really always trying
to gather voice of customer to make sure, you know, we might be very excited about building, you know, the latest
incremental improvement to the information retrieval pipeline. But our customers like, I just wish your QA environment
was a little more stable. And so making sure we don't
get too lost in the engineering and technology of it, but stay grounded with the customers has been important. And then expectations increased rapidly. So initially there was skepticism and it's like for some
developers at Lilly, this is like a new approach kind of channeling them
into a certain platform and putting some constraints around it. But the, you know, skepticism
quickly turned to like, oh I see, it's speeding it
up, it's making it easier. I get the approvals and
we're seeing adoption and then it turned to like, oh
now I want this, this, this, where's the documentation? What are your formal SLAs? So I'd say if you're taking this approach, make sure to think ahead of it. And if you're building the platform, keep up with the documentation, keep up with the support, you know, get ahead of okay communicating SLAs. 'cause especially in a place like Lilly, we have patient facing stuff,
we have manufacturing stuff, there's 24/7 expectations. And then lastly I mentioned
the cyber partnership and investing in that early
was pretty key I think to this platform success,
especially in a company like Lilly where there's a high bar around cyber or privacy legal and all of that. So with that I think I'll
turn it back over to Rama. - Thanks Cas, I appreciate
you taking the time to share those awesome insights with us. So something we have talked a lot about throughout this presentation
has been that customers want to integrate to us
as solutions on top of EKS to achieve the desire ML functionality. So a lot of our customers were asking us for guidance around how
to get started quickly integrating these solutions. What are the best practices
for integrating them? Can you provide us some templates and patterns that you're
seeing success with? So that's why we launched
the data on EKS project. It's an open source project where we publish different gen AI patterns that we have seen across our customers. We publish blueprints,
patterns, terraform templates that you can use to easily get started integrating some of the
popular OSS solutions that we see getting integrated with EKS for solving those ML specific challenges. So we have launched a
number of these patterns over the last year. We continue to create more
patterns as we see success with those patterns in in the real world. We have been placing special focus on releasing inference specific
patterns on top of EKS. Some of the things that we
have recently released are, Nvidia with VLLM, Racer with VLLM, Nvidia NIMS on EKS, so on and so forth. So check out our data on
EKS website where you'll see a lot of different patterns for inference and for training and fine tuning as well. With that, we have almost
come to the end of it. There are some interesting
sessions that are coming up with EKS, Amazon EKS
infrastructure as code gitops session on that as well. And there is an interesting
session from S&P Global that have implemented gen AI on EKS and how they're scaling to meet millions of inference requests per week using that setup as well. And we also have the Future of Kubernetes on AWS session coming up tomorrow that you can check out. You can continue your Amazon EKS learning through some of your
resources available out there through workshops, through
getting digital badges and best practices guides as well. With that, we come to
the end of the session. Thank you for listening to us patiently, and if you have any questions,
we'll be hanging out outside the room for some time. You can approach us and we can answer any
questions for you as well. Thank you. (people clapping)

## Subtitles with Timestamps

[00:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2s) - Okay, good morning.

[00:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3s) Welcome to KUB314.

[00:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=6s) We're gonna talk about how to
run Gen AI workloads on EKS.

[00:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=10s) I assume many of you

[00:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=12s) in the last couple days
have been to the keynotes.

[00:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=13s) I think Peter was Monday
night, Matt was yesterday.

[00:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=15s) I just heard there's a
machine learning keynote

[00:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=18s) going on as we speak.

[00:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=19s) So thank you for coming to this talk.

[00:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=21s) And many of those keynotes,

[00:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=22s) they're talking about machine learning,

[00:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=25s) generative AI features
that are coming out.

[00:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=27s) Graviton4, Trainium2 UltraServers,

[00:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=30s) all of this cool stuff.

[00:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=31s) And I think a lot of you in
this room are saying, yeah,

[00:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=33s) that's great, but I can't use it

[00:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=34s) unless it works with EKS

[00:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=35s) and a lot of customers,

[00:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=37s) some of the largest
foundational models out there,

[00:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=39s) you see a lot of them were
trained on Kubernetes.

[00:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=41s) And that's exactly what
we're gonna talk about today,

[00:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=43s) is the work that EKS does

[00:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=45s) to make running, Gen AI is in the title,

[00:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=48s) but really any machine learning workloads

[00:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=49s) easier to do on EKS.

[00:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=51s) And I'm joined by Rama who's gonna talk

[00:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=52s) a little bit about why EKS

[00:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=54s) and Kubernetes has become a
good fit for ML workloads.

[00:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=57s) And then special guest, we have Cas

[00:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=59s) from Eli Lilly and Company who's gonna talk

[01:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=62s) about how they've built their
machine learning platform

[01:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=64s) on EKS and the success they've seen.

[01:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=70s) Okay, super quick, why generative AI?

[01:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=73s) What is generative AI?

[01:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=75s) I know all of you probably know this,

[01:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=76s) maybe some of you had a late night.

[01:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=78s) It's the first talk,
I'll go super quick here.

[01:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=80s) AI that can produce content

[01:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=82s) that looks like human content

[01:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=84s) in a lot of cases you can't
even tell the difference.

[01:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=86s) And it's powered by
foundational models that have up

[01:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=89s) to several hundred billion parameters

[01:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=91s) probably by next year
approaching trillion parameters.

[01:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=94s) And the real innovation with generative AI

[01:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=96s) is that you can reduce the
time to build ML applications

[01:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=101s) because you start with these
huge foundational models

[01:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=103s) and then it takes only a little
bit of training to fine tune

[01:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=106s) and do what you need to do
for your specific tasks.

[01:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=110s) As far as use cases go,
really four main buckets

[01:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=113s) that we've seen for
generative AI use cases,

[01:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=115s) probably the one you're most familiar with

[01:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=117s) is the enhancing customer experience.

[02:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=120s) I think Andy came on stage yesterday

[02:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=122s) and was talking about Rufus, the new agent

[02:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=124s) that can help you shop on amazon.com.

[02:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=129s) Boosting employee
productivity is another one.

[02:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=131s) Another few announcements yesterday

[02:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=132s) we had were code migration tools.

[02:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=135s) I think we talked about
at Amazon how we've saved,

[02:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=138s) I don't know, X number of developer hours

[02:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=139s) moving from Java 11 to Java 17.

[02:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=142s) I think we also announced

[02:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=144s) a Windows modernization code migration.

[02:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=148s) So that's a use case we see a lot.

[02:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=150s) Content generation, image
generators are cool,

[02:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=153s) video generators are cool.

[02:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=155s) And I think the more interesting one

[02:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=156s) is business operations.

[02:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=157s) I've actually talked, I've had a lot

[02:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=159s) of customer meetings
in the last couple days

[02:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=160s) and a lot of you are already using Gen AI

[02:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=162s) and some of the platforms you're building,

[02:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=164s) whether it's doing log analysis

[02:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=166s) to do faster troubleshooting,

[02:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=168s) onboarding your developers
faster to the platforms building.

[02:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=171s) So we're starting to see some use cases

[02:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=173s) that are actually working.

[02:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=177s) Some of the trends we've seen,

[02:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=178s) more complex generative AI workflows,

[03:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=182s) agents talking to agents, you know,

[03:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=185s) moving to production
models require guardrails,

[03:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=186s) other sets of capabilities.

[03:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=188s) And I think the last one
is the most interesting,

[03:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=191s) AWS, you've gone to the keynotes.

[03:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=193s) AWS has a lot of different tools.

[03:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=195s) Bedrock was talked a lot about yesterday.

[03:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=196s) Amazon Queue, we have a lot

[03:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=198s) of different layers of the stack.

[03:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=200s) EKS is towards the bottom of that layer

[03:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=201s) where you really need
the most flexibility,

[03:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=204s) the most customization, the
highest levels of scalability.

[03:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=207s) But I imagine in a large enterprise,

[03:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=209s) you might be using a mix of EKS, Bedrock,

[03:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=212s) Queue, other tools.

[03:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=216s) If 2023 was the year of
gen AI, proof of concepts,

[03:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=221s) POCs, we've seen 2024 be
the year of production.

[03:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=224s) And moving to that production mindset

[03:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=227s) really requires a
different way of thinking.

[03:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=230s) You need to start thinking about

[03:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=233s) how are we gonna make money or save costs?

[03:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=234s) You know, we can't just run POCs forever.

[03:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=236s) And you start to think about cost

[03:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=238s) of inference at scale, latency at scale.

[04:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=242s) You may just not want to pick the highest

[04:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=245s) performing best model.

[04:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=246s) You need to weigh that against
how much is it gonna cost me

[04:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=248s) to run that in production?

[04:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=249s) What is the latency,

[04:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=250s) how is it gonna impact
the user experience?

[04:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=252s) And then when you move to
production, you also need

[04:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=255s) to think about things like security,

[04:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=257s) compliance, ethical constraints.

[04:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=260s) So there's a lot more
and a lot more effort

[04:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=263s) that goes into building
a production application.

[04:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=265s) And that's really the trend
we've started to see this year.

[04:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=268s) So I'm gonna hand it off to Rama

[04:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=270s) to talk about some of the
generative AI challenges

[04:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=273s) and how EKS helps solve them.

[04:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=278s) - Thanks Mike, hey folks, good morning.

[04:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=282s) I'm Rama Ponnuswami,

[04:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=283s) I drive worldwide, go to
market for AML on EKS.

[04:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=286s) So talking a little bit

[04:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=288s) about some of the common challenges

[04:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=291s) that we see our customers face

[04:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=292s) when they start to scale

[04:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=295s) their gen AI workloads in production.

[04:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=298s) It's sort of along three
different buckets, right?

[05:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=300s) Like as Mike was saying,
there are different needs

[05:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=303s) for your different teams
within a single organization.

[05:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=305s) And one model is not gonna
fit all of them, right?

[05:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=308s) So more than likely you'll
have to run multiple models,

[05:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=311s) different ways of customizing those models

[05:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=313s) to fit specific needs of different teams.

[05:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=316s) So that comes with the added
burden of day two operations.

[05:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=320s) How are you gonna manage the
versioning of those models?

[05:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=322s) How are you gonna upgrade these models

[05:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=323s) when new models show up?

[05:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=325s) How do you build guardrails
against these models?

[05:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=327s) And how do you manage access
to data for these models?

[05:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=331s) Because customizing these
models is not gonna be easy.

[05:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=334s) Customizing models requires
specific curated data

[05:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=338s) that is domain specific

[05:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=339s) and fits your particular specific use case

[05:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=342s) where you want these models to be able

[05:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=346s) to drive tasks specific
to that domain, right?

[05:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=351s) And that also means that you are having

[05:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=354s) to integrate multiple data
sources, having to manage access

[05:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=358s) to all of this data

[05:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=359s) all while maintaining your
data security requirements.

[06:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=362s) And last but not least, all of this means

[06:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=365s) that you are having to
manage massive scale

[06:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=368s) of infrastructure, which gets trickier.

[06:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=371s) We have seen a lot of our customers,

[06:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=372s) when they start to scale
or hit critical scale

[06:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=376s) in their production,

[06:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=377s) they start to feel that delegating more

[06:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=380s) of your infrastructure
control makes you less capable

[06:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=384s) of controlling any of
these parameters, right?

[06:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=388s) So we start to see customers
as they hit some critical scale

[06:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=390s) and production of Gen
AI workloads, they want

[06:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=393s) to have more control
over the infrastructure

[06:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=394s) and start looking at options
like EKS where they can get

[06:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=397s) that necessary control
to be able to customize

[06:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=401s) all of their models and the ML environment

[06:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=403s) that they want to operate in,

[06:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=404s) and to be able to optimize on their cost

[06:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=407s) to meet their ROI targets.

[06:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=409s) So those are challenges at
the organizational level.

[06:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=412s) Let's think a little bit
about what are the challenges

[06:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=415s) of a data scientist or an ML engineer

[06:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=417s) on their day-to-day operations.

[06:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=419s) Data scientists don't really want

[07:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=421s) to be managing infrastructure.

[07:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=422s) All they require is a rarely
available infrastructure

[07:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=425s) that they can just code deploy
their model and scale on,

[07:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=428s) and they don't really want
to be doing boiler paid code

[07:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=431s) or scripts that they need to run

[07:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=434s) in order to manage the
lifecycle of their ML models.

[07:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=436s) Instead, they want a
readily built platform

[07:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=438s) that can help them with
all of those capabilities

[07:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=441s) that they need to effectively deploy

[07:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=443s) and scale their workloads
going further as well.

[07:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=447s) And they want to be able
to meet these requirements

[07:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=451s) in a more optimized
manner, in a repeatable way

[07:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=455s) that they can just keep doing it

[07:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=456s) over and over again instead of having

[07:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=458s) to build something in a very
individualistic ad hoc manner

[07:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=461s) each time they need to
build and scale a model.

[07:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=463s) So to summarize in terms
of the key challenges

[07:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=467s) or considerations, if you will, in terms

[07:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=470s) of deploying generative AI in production,

[07:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=471s) it's along three lines, right?

[07:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=473s) You want to be able to move fast,

[07:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=474s) you want to enable your data scientists

[07:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=478s) and ML engineers to
build their models fast,

[08:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=480s) deploy them fast, and be able to scale

[08:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=482s) as they go forward as well.

[08:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=485s) And the second thing is about

[08:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=487s) how do you enable customization
of your models right?

[08:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=489s) At scale.

[08:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=491s) You want to be able to
customize multiple models

[08:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=492s) to fit specific use cases

[08:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=494s) within different teams
in your organization.

[08:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=497s) And you also want to be able to ensure

[08:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=500s) that these models will be able to scale,

[08:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=502s) not just to meet the demands of today,

[08:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=505s) but seamlessly scale

[08:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=507s) to meet the demands of the future as well.

[08:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=509s) And how do you ensure that you're able

[08:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=510s) to continuously optimize on your costs

[08:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=513s) as you're hitting higher
scales going forward?

[08:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=516s) Scaling up your ML models as well.

[08:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=520s) So this is really where
we see a lot of customers

[08:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=522s) mention that EKS makes
a lot of sense for them,

[08:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=525s) especially in environments

[08:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=526s) where they need a lot more
control over infrastructure

[08:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=529s) to meet data security concerns,
to meet cost optimization

[08:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=533s) concerns because they need
to hit the ROI targets,

[08:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=538s) so on and so forth as well.

[09:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=540s) So let's sort of dissect,

[09:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=541s) where does EKS provide these benefits?

[09:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=544s) Why do we see a lot of our
customers start to leverage EKS

[09:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=548s) for deploying the generative AI workloads?

[09:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=551s) It's again, along those buckets

[09:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=554s) of how does EKS enable you to move faster?

[09:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=557s) It's twofold, right?

[09:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=558s) The first is, in most cases

[09:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=560s) where customers already have
standardized on Kubernetes

[09:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=563s) as the way to do their
application development,

[09:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=565s) they get to just extend
that existing platform

[09:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=568s) and deploy ML models on top of it

[09:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=570s) because they already built
foundational capabilities

[09:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=572s) that they also need
for their ML workloads.

[09:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=578s) The second reason is availability

[09:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=582s) of open source tooling, right?

[09:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=583s) ML space in general is fast moving

[09:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=586s) and a lot of those
innovations are happening

[09:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=588s) in the open source arena, right?

[09:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=590s) And these open source tools,
most of them usually come

[09:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=593s) with out of the box
Kubernetes integration.

[09:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=595s) So with EKS customers can just integrate

[09:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=599s) that ML specific OSS
solutions on top of it

[10:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=602s) and enable their data
scientists to just move faster

[10:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=604s) by providing them all end to end ML ops

[10:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=607s) lifecycle capabilities, as we saw earlier,

[10:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=610s) that's one of the key challenges.

[10:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=613s) And in terms of scalability, Kubernetes

[10:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=615s) and EKS as such provides
native integrations

[10:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=618s) to all of AWS ML infrastructure services,

[10:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=620s) enabling you to continue

[10:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=622s) to scale seamlessly as
your demand increases

[10:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=625s) for your ML models as well.

[10:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=628s) In terms of customization,

[10:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=630s) because you are getting control

[10:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=632s) of your entire infrastructure
right up to the instance level

[10:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=635s) with EKS, you are able

[10:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=636s) to flexibly configure your environment

[10:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=640s) to suit your specific unique needs,

[10:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=642s) and you are not going to be restricted

[10:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=644s) because of a certain
feature that we provide.

[10:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=647s) And you know, we don't have restrictions

[10:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=649s) in terms of how you can configure

[10:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=651s) your ML environment within EKS.

[10:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=654s) So that enables you to
customize it to your liking,

[10:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=657s) to suit your specific unique requirements.

[11:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=660s) And because you're able
to have multiple choices

[11:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=663s) in terms of instances,
you are constantly able

[11:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=666s) to choose the right infrastructure sizing,

[11:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=669s) the right instances,

[11:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=671s) and be able to optimize
on your cost continuously

[11:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=675s) as you start to scale further

[11:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=677s) with your ML workloads as well.

[11:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=679s) So let's go a little deeper

[11:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=681s) on how does flexibility
and cost optimization

[11:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=684s) work on EKS for ML,

[11:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=685s) it's really across three layers.

[11:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=687s) The first is at the instant level

[11:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=690s) because EKS supports all
of the EC2 instances, GPU,

[11:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=694s) Nvidia based, GPU instances,
Trainium, Andreia,

[11:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=697s) Intel based instances, so on and so forth.

[11:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=700s) Any EC2 instance that is available on AWS,

[11:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=701s) you can leverage it with EKS.

[11:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=703s) So that lets you choose flexibly
which instances you want

[11:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=707s) to use based on the workload

[11:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=709s) and based on the
requirements of the workload.

[11:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=713s) So this is not just
gonna be enough, right?

[11:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=716s) Like ideally you don't want
to be making these choices

[11:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=717s) manually each time a new workload

[11:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=719s) comes into for scheduling.

[12:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=721s) And that's really where the power

[12:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=722s) ofKarpenter comes into the picture.

[12:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=724s) With Karpenter, you can
effectively automate

[12:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=727s) all of these choices by providing it

[12:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=729s) the parameters under which you want

[12:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=731s) to provision a specific instance

[12:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=732s) and make it evaluate the incoming workload

[12:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=736s) to choose the right instances for it.

[12:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=738s) All of this gets automated by Karpenter

[12:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=740s) and it's repeatedly
doing this on your behalf

[12:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=743s) whenever a new workload gets scheduled.

[12:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=747s) And on top of that, Karpenter makes

[12:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=749s) provisioning much easier as well.

[12:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=754s) So Karpenter, along with
our EKS optimized army

[12:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=757s) comes with all of the inbuilt
dependencies that you need

[12:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=762s) and you are able to
quickly spin up instances

[12:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=765s) whenever your demand goes up

[12:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=766s) and Karpenter gives you fast scaling,

[12:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=767s) but more importantly,
it also scales back down

[12:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=771s) whenever your demand is not going up.

[12:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=775s) So you are able to cost optimize

[12:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=776s) on that front and you are also able

[12:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=777s) to leverage GPU sharing mechanisms.

[13:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=783s) And with built-in multi-tenancy of EKS,

[13:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=786s) you're able to effectively share

[13:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=788s) your constrained GPU resources securely

[13:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=791s) across multiple teams
in your organization,

[13:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=793s) shooting up your utilization
of GPUs further as well.

[13:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=798s) And on top of that, you get to integrate

[13:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=800s) ML specific OSS solutions, the whole ocean

[13:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=804s) of solutions available out there.

[13:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=806s) You get to pick and choose the right tools

[13:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=808s) for the right functionality

[13:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=809s) that you need within your
organization to then integrate it

[13:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=813s) with EKS and get all
the flexibility you need

[13:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=815s) with the ML specific functionality

[13:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=816s) your data scientists desire as well.

[13:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=821s) In terms of, I wanted to quickly highlight

[13:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=822s) very few customers.

[13:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=825s) We have a lot of customers
running Gen A on EKS,

[13:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=828s) but I wanted to pick a select few

[13:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=829s) that have been able to
reap certain benefits

[13:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=832s) by deploying generative
AI workloads on EKS.

[13:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=836s) Vannevar Labs is a defense tech startup.

[13:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=838s) They supply unconventional intelligence

[14:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=840s) to national intelligence
agencies and defense departments.

[14:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=845s) So they operate at the
highest level of secrecy

[14:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=846s) and data security concerns.

[14:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=848s) They were able to utilize EKS

[14:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=851s) and Ray and Karpenter together

[14:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=853s) to achieve 45% reduction
in their inference costs.

[14:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=857s) And they were able to do
this by using mixed CPU

[14:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=860s) and GPU instance types

[14:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=862s) and being able to schedule

[14:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=864s) CPU heavy workloads on GPU instances

[14:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=868s) to utilize the under used
CPU, within the GPU instances.

[14:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=872s) So overall, increasing
their GPU utilization

[14:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=876s) by a huge margin.

[14:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=878s) And we have recently
published a blog with them.

[14:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=880s) If you're interested in learning

[14:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=882s) about the specific configurations

[14:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=883s) that they did to achieve this cost cut,

[14:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=885s) please feel free to check it out

[14:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=887s) in our AWS containers blog channel.

[14:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=890s) The next is Informatica.

[14:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=892s) They are another customer

[14:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=894s) that have built an LLM
ops platform to train

[14:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=896s) and fine tune multiple
LLM models on top of EKS.

[15:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=900s) They were able to achieve
around 30% of cost saving

[15:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=904s) compared to managed services
that they were using earlier.

[15:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=906s) And they were able to achieve
enhanced configurability

[15:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=910s) because they were sort of constrained

[15:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=912s) by the managed services
customization ability

[15:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=917s) that the managed services
was providing them.

[15:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=920s) And Zoom is another
customer that has been able

[15:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=922s) to create a similar LM ops platform

[15:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=924s) where they do multimodal hosting

[15:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=926s) and they're able to reliably

[15:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=928s) and efficiently scale

[15:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=929s) to meet their ongoing demand as well.

[15:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=935s) Another key customer I wanted
to highlight is Hugging Face.

[15:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=938s) If we have used the Hugging Face hub,

[15:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=939s) the freemium pricing
one, the three tier one

[15:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=943s) that basically runs on top of EPS today,

[15:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=945s) the challenge that they initially,

[15:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=947s) when they started out
building that platform

[15:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=949s) was they had to build a platform

[15:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=950s) that would enable inference of millions

[15:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=952s) of models with dedicated
inference endpoints

[15:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=959s) and a lot of different domain names

[16:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=962s) had to be hosted there as well.

[16:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=963s) And all of this needed to be provided

[16:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=965s) with three tier pricing.

[16:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=966s) So it was a challenge that they had

[16:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=969s) to hyper optimize on their cost,

[16:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=970s) on their infrastructure cost
in order to be able to afford

[16:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=973s) to provide this as a
freemium price tier as well.

[16:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=976s) So the solution they've
taken is to deploy it on EKS,

[16:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=978s) multiple EKS clusters, 2000 plus nodes,

[16:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=983s) and they're able to effectively pin pack

[16:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=986s) a lot of parts within
very fewer instances.

[16:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=989s) And they're also able to
use time sharing with GPUs

[16:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=992s) where they swap models in and
out every few seconds as well.

[16:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=997s) And with this, they're effectively able

[16:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=998s) to provide this platform across the world

[16:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1000s) for ML developers to collaborate on.

[16:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1005s) So I mentioned something
earlier, customers

[16:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1007s) that already have Kubernetes
as a standard platform

[16:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1011s) for their application development.

[16:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1013s) This sort of a snapshot

[16:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1015s) of how those platforms look like, right?

[16:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1017s) They build all of those
foundational capabilities

[17:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1020s) already into this platform,

[17:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1021s) like how to do logging, monitoring,

[17:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1024s) disaster recovery, security at scale.

[17:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1026s) All of those challenges have been solved.

[17:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1027s) And customers, when it comes
to ML, they don't want to,

[17:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1030s) again, solve these challenges
or reinvent the wheel, right?

[17:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1032s) They just want to use all of
these foundational capabilities

[17:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1035s) and extend it to run ML
workloads on top of this as well.

[17:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1039s) So that's one key advantage.

[17:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1041s) The second advantage is customers
are able to use Kubernetes

[17:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1044s) as the standard layer across
all of their environments,

[17:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1047s) be it on-prem, be it in the
edge, be it on cloud as well.

[17:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1052s) So providing, using Kubernetes

[17:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1053s) helps them unify these operations.

[17:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1055s) And if you have been paying attention

[17:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1057s) to the recent releases we did last Sunday,

[17:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1060s) we released egress hybrid nodes as well,

[17:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1063s) making this much easier
for customers to do

[17:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1064s) with EKS hybrid notes, you
get to attach node on cloud,

[17:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1067s) on premises, on edge

[17:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1069s) into a single EKS managed
control plane if you desire

[17:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1073s) and you get to offload

[17:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1075s) all of the Kubernetes
control plane management

[17:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1078s) and you get to have sort
of a logical mapping

[18:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1081s) of your infrastructure across
all of these environments,

[18:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1086s) providing you a better way to utilize

[18:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1088s) your GPU resources wherever available

[18:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1091s) and to cost optimize as
you go along as well.

[18:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1095s) You can pick and choose
which workload gets deployed

[18:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1097s) in which environment based
on the cost ROI benefits

[18:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1100s) that you expect out of
those workloads as well.

[18:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1104s) So in terms of what we
have seen customers do

[18:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1107s) and when they try to
extend these platforms is,

[18:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1111s) as I mentioned earlier on,

[18:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1112s) integrate OSS solutions
on top of it, right?

[18:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1114s) That lets Kubernetes do what it's good at,

[18:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1116s) which is infrastructure orchestration.

[18:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1119s) And you integrate OSS solutions on top,

[18:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1122s) which provide you ML
specific functionality.

[18:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1125s) For example, we've seen a lot of customers

[18:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1127s) adopt VLLM together with EKS

[18:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1130s) that provides you a lot of
functionality like memory

[18:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1134s) and model optimization,
multimodal management,

[18:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1136s) request batching, query queuing,

[18:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1139s) so on and so forth for
inference infrastructure.

[19:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1142s) So this can provide
you a readily available

[19:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1144s) inference endpoint or an inference stack

[19:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1147s) that you can make available

[19:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1148s) to your data scientists
that they can just deploy

[19:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1150s) a model and get an endpoint

[19:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1152s) where they can run their inference out of.

[19:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1154s) So in a sense, to summarize all of this,

[19:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1157s) when customers use EKS for generative AI,

[19:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1160s) what they've been able
to get is more control

[19:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1165s) of their environment to
be able to customize it,

[19:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1167s) to fit it to their specific needs,

[19:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1170s) to be able to scale seamlessly
to meet future demands

[19:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1173s) and be able to continuously cost optimize

[19:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1176s) to meet their ROA targets.

[19:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1178s) So with that, I will hand out to Mike

[19:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1181s) to talk about the specific
features that EKS provides.

[19:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1187s) - All right, thanks Rama.

[19:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1191s) Okay, I'm gonna do a bit
of a rapid fire overview

[19:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1194s) of a lot of the features we've launched

[19:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1196s) in the last 12 to 18 months

[19:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1198s) to make it easier to run AI ML

[20:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1202s) generative AI workloads on EKS.

[20:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1204s) First, this is more a concrete picture

[20:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1207s) of what Rama was just talking about

[20:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1207s) of all the tools out
there that you can use

[20:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1210s) to get started, there's really two parts.

[20:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1212s) The open source stack,

[20:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1214s) very rarely are you starting from scratch.

[20:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1216s) And Kubernetes Rama mentioned
Ray, VLLM, Jupyter Hub,

[20:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1221s) all of these tools work with Kubernetes

[20:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1223s) and it's really the flywheel effect

[20:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1224s) that we like to talk about at Amazon

[20:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1226s) because say you're gonna try to author

[20:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1228s) a new machine learning tool,
you have a really good idea.

[20:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1231s) If you want to get adoption of that,

[20:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1233s) you're very likely gonna
make sure it works well

[20:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1236s) on Kubernetes as one of your
first deployment targets.

[20:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1239s) And a lot of these frameworks
tools out there do just that.

[20:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1241s) They work well in Kubernetes.

[20:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1243s) Certain ones of these we
choose to contribute to.

[20:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1245s) We've made some some contributions to Ray

[20:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1248s) and make sure it works well
with the neuron frameworks.

[20:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1250s) And then at the other end
at EKS is we make sure

[20:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1253s) that the infrastructure innovations

[20:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1256s) and services at AWS

[20:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1258s) that power this large
scale training inferencing

[21:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1261s) work well with EKS.

[21:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1262s) So CSI drivers, ECR, a lot of
those foundational services

[21:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1266s) that you need to use with ML workloads,

[21:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1268s) we make sure they work
really well with EKS.

[21:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1272s) Okay, features, this one,

[21:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1276s) we don't give enough love

[21:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1277s) to I think the work we do

[21:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1279s) for scalability of the control plane.

[21:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1281s) We rarely ever do a what's
new post EKS is, you know,

[21:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1285s) a little bit more performant.

[21:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1286s) But I know for a fact we have customers

[21:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1287s) that created EKS clusters

[21:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1290s) six years ago when the service launched

[21:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1292s) and they've just
continuously upgraded then

[21:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1294s) from one dot 10

[21:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1296s) all the way up to one dot 30.

[21:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1298s) And those clusters look nothing

[21:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1299s) like they did when they
launched six years ago.

[21:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1301s) So every time you create an EKS cluster,

[21:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1303s) we're creating dedicated
infrastructure for you.

[21:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1306s) EC2 instances, nat gateways, NLB,

[21:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1311s) and we do a lot of work there.

[21:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1313s) It's over time to
continuously add performance,

[21:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1315s) whether it's newer instance
types, faster volumes,

[21:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1318s) you know, better networking.

[22:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1321s) And one of the projects we've done a lot

[22:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1323s) of work on this year is
changing the way we manage at CD

[22:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1325s) to really get to much higher scale.

[22:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1327s) We have certain customers
that are asking us for 10,000,

[22:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1332s) 20,000, 50,000 node clusters.

[22:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1333s) And in order to make that happen,

[22:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1334s) we've had to do some
pretty major refactoring

[22:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1336s) to the way we manage at CD,

[22:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1339s) which is the backend
database of Kubernetes.

[22:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1342s) So likely next year, we'll
publish some more on that,

[22:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1345s) but that's something
we've been working on.

[22:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1347s) EFA is an example of a lower
level infrastructure innovation

[22:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1352s) that AWS it's a OS
bypass hardware interface

[22:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1355s) that allows high levels of
multi-node communication.

[22:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1358s) We make that easy to use with EKS

[22:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1360s) and Kubernetes with a device plugin.

[22:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1364s) I think a couple notable
recent enhancements,

[22:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1367s) EFA just added support for
cross subnet communication.

[22:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1372s) You used to be limited to
a single subnet with EFA.

[22:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1375s) Now you can do cross
subnet within the same AZ,

[22:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1376s) you don't necessarily wanna
do training across AZs

[22:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1378s) because that's expensive,

[23:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1381s) but that helps with IP address exhaustion.

[23:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1383s) And then the other thing
that helps with IP address

[23:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1385s) exhaustion is oftentimes
your ML training workloads,

[23:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1387s) they're sitting there just
crunching, doing a lot of math,

[23:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1389s) they don't actually need
to talk to the internet.

[23:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1392s) They only need to talk to each other,

[23:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1393s) the other nodes in the cluster.

[23:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1395s) So we recently added support
for EFA only ENI support,

[23:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1399s) so you don't have to
add actual IP addresses

[23:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1400s) to the EFA devices in your cluster.

[23:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1404s) And that's now supported on EKS

[23:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1405s) when you're running large
scale training jobs,

[23:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1410s) you need a large scale storage backend

[23:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1413s) to handle all of the data
that you're processing.

[23:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1416s) And there's probably no
larger scale storage backend

[23:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1419s) in the world than S3, S3 open source

[23:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1422s) to technology called Mount Point last year

[23:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1426s) that allows you to mount an
S3 bucket to an EC2 instance

[23:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1430s) and use file system commands.

[23:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1433s) And they get automatically
translated to S3 object commands.

[23:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1436s) And we've made that easy to use, again

[23:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1438s) with EKS via a CSI driver,
Kubernetes native interface.

[24:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1441s) Recent notable enhancement
is the CSI driver

[24:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1445s) added some more fine-grained
access controls.

[24:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1448s) So you can lock down, you
know, which training pods

[24:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1451s) in your cluster have
access to which buckets.

[24:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1457s) Generative AI training
inferencing is not cheap,

[24:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1462s) these instances are in high demand.

[24:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1465s) They cost more than
standard CPU instances.

[24:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1467s) AWS has done a lot of work
over the last five years

[24:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1470s) to bring down, improve price performance,

[24:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1474s) lower the cost Trainium.

[24:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1478s) I think just yesterday
we announced Trainium2

[24:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1480s) and we'll continue to
innovate at the lowest levels

[24:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1483s) of silicon to make sure
we give you the best price

[24:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1486s) performance for Trainium workloads.

[24:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1488s) And again, these are great,

[24:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1489s) but for, for those of you in this room,

[24:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1491s) it's not helpful unless it works with EKS.

[24:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1493s) And in the last couple of months

[24:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1497s) we've introduced accelerated armies

[24:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1499s) for both Amazon Linux 2023,

[25:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1501s) which is the newest general
purpose Linux distribution

[25:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1505s) from Amazon, as well as Bottle Rocket,

[25:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1507s) which is our container
optimized operating system.

[25:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1510s) These work with all of the
various EKS compute options,

[25:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1514s) self-managed node groups,
Karpenter management groups

[25:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1517s) and probably again, one
of the underappreciated

[25:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1520s) or under talked about things
we do here is the testing

[25:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1522s) behind the scenes, the amount
of drivers, frameworks,

[25:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1527s) libraries, Cuda toolkits,
like all of these things

[25:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1531s) that go into an is complex.

[25:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1532s) They change fast and we have
a pretty sophisticated testing

[25:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1536s) framework where we're
running training jobs,

[25:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1538s) inferencing jobs before
we release these ams.

[25:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1539s) So you can just take them, run them

[25:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1541s) and be confident that they're
gonna work for your workloads.

[25:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1548s) Specifically for training workloads,

[25:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1549s) I know we talk a lot about
Karpenter these days,

[25:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1553s) but Manage Node Groups

[25:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1554s) is our original managed compute
product that we launched,

[25:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1558s) I think five years ago at re:Invent now.

[26:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1560s) Now and Manage Node Groups
is actually a good fit

[26:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1563s) for training workloads

[26:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1564s) because often training
workloads are not dynamic.

[26:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1565s) You just have a large
static pool of capacity

[26:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1567s) that you need to run your training job.

[26:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1569s) It's not going up and down often.

[26:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1570s) So manage no groups is
a good fit for that.

[26:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1573s) And EC2 launched a
feature a few months back

[26:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1576s) called capacity block reservations.

[26:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1578s) Again, I mentioned these
instance types are in high demand

[26:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1581s) and capacity blocks

[26:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1583s) is kind of like a hotel
reservation system,

[26:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1585s) but for EC2 instances, so
up to eight weeks in advance

[26:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1589s) you can book capacity for GPUs

[26:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1591s) and you know you'll have
it at that specific time.

[26:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1594s) Recently they just gave the ability

[26:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1596s) to extend the reservation

[26:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1598s) and that now natively works
with managed node groups.

[26:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1601s) So particularly for training workloads,

[26:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1603s) we think this is a nice enhancement.

[26:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1607s) GPU instances do tend

[26:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1611s) to fail more often than
than CPU instances.

[26:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1614s) They're running complex math calculations.

[26:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1616s) I know the EC2 team is doing
a ton of work, you know,

[27:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1620s) at the data center level

[27:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1621s) to try to increase the performance.

[27:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1623s) Things like, I don't know,

[27:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1626s) 1% changes in humidity in the data center

[27:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1627s) can give a 10% increase in the
lifetime of a GPU instance,

[27:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1631s) but they do fail on occasion

[27:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1634s) and we've put a lot of effort this year

[27:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1636s) into detecting those failures.

[27:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1638s) So you don't have an instance
that goes bad and your cluster

[27:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1641s) and is wasting money

[27:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1642s) while it's not actually doing any work.

[27:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1646s) So this actually rolled out

[27:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1647s) for EKS auto mode just this last week,

[27:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1650s) which I'll talk about it in a minute.

[27:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1651s) It'll be rolling out for other
compute over the next week

[27:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1654s) or two, but it's really two parts.

[27:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1655s) It's the node health monitoring
agent, which is an agent

[27:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1658s) it'll run as a Damon said in your cluster,

[27:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1660s) look for all kinds of issues.

[27:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1662s) We have six years of experience

[27:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1664s) of running lots of Kubernetes clusters.

[27:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1666s) We've seen every possible
way a node can fail.

[27:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1668s) And we've taken that knowledge

[27:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1670s) and built it into this node
health monitoring repair agent

[27:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1673s) with a specific focus on GPU instances.

[27:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1675s) And then on the auto repair side,

[27:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1677s) managed node groups

[27:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1679s) will get to the auto repair functionality

[28:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1681s) where you can opt in

[28:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1682s) to say, okay, EKS, you detected an issue.

[28:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1684s) In some cases maybe you want
to recycle the instance.

[28:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1687s) In other cases, maybe you want

[28:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1689s) to reboot the instance depending
on the type of failure.

[28:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1691s) And that'll be rolling out very soon.

[28:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1696s) And then my last slide

[28:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1698s) is on monitoring observability.

[28:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1701s) I think it was at re:Invent last year.

[28:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1703s) We launched version two of of
CloudWatch Container Insights,

[28:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1707s) which it's a lot better than V1.

[28:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1710s) If any of you had tried V1

[28:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1711s) a couple years back, had its challenges.

[28:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1714s) The new version of
CloudWatch Container Insights

[28:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1717s) is really, really nice.

[28:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1718s) It's also more cost effective
for container workloads

[28:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1721s) and a recent enhancement to
the Container Insights plugin.

[28:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1724s) And you just run this as an
agent in your EKS cluster,

[28:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1726s) is it now automatically
includes the monitoring plugins

[28:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1731s) for both NVIDIA and neuron instance types.

[28:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1732s) It'll scrape those metrics,
send them to CloudWatch,

[28:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1735s) allow you to monitor how efficient your GP

[28:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1738s) or resources are consumed,
do things like understand

[29:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1741s) how workloads are running, you know,

[29:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1743s) figure out how to tune hyper parameters.

[29:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1746s) There's a lot of work
that the team did there

[29:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1747s) to make sure that you have a simple

[29:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1751s) out of the box check checkbox, GPU,

[29:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1753s) Nvidia monitoring experience.

[29:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1756s) So I highly recommend
you check this one out

[29:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1758s) if you haven't seen it.

[29:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1759s) Okay, I wanna talk
specifically about inference.

[29:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1762s) I mentioned at the beginning,

[29:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1766s) 2024 is the year of production.

[29:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1768s) And production generally
means inferencing.

[29:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1770s) If you have a live workload,
you're serving requests

[29:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1774s) to your customers and
that brings challenges,

[29:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1778s) especially with these, you
know, large language models.

[29:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1782s) Running inference at scale
can be complex, you know,

[29:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1785s) how do you, how do you serve
models that are cost effective,

[29:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1789s) that have the performance you want?

[29:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1791s) Latency, throughput, availability.

[29:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1792s) All of these become concerns

[29:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1793s) when you're running inferencing at scale.

[29:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1798s) And how we're thinking
about inferencing at EKS

[30:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1802s) is really there's those three
measurements on the left,

[30:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1805s) the throughput, you know,

[30:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1807s) how many tokens per second
your model is serving,

[30:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1810s) the latency, which is the
time to the first token,

[30:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1813s) and then cost, which is really
the GPU compute utilization,

[30:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1817s) how much of the GPU you're actually using.

[30:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1818s) And so a lot of these
features we're building

[30:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1820s) and framework enhancements
we're doing are designed

[30:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1823s) to help you achieve that trade off

[30:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1824s) between throughput, latency and cost.

[30:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1827s) There's never gonna be a perfect answer,

[30:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1829s) but we want to give you
the tools to make it easy

[30:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1831s) to do that trade off for yourself.

[30:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1833s) Scaling to zero, scaling up quickly.

[30:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1836s) Optimizing ML container images.

[30:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1838s) This is something we're doing quite a bit

[30:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1840s) of work in the container D project.

[30:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1842s) You know, oftentimes
these ML images are tens,

[30:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1844s) sometimes I've seen hundreds of gigabytes.

[30:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1846s) And when you start your instance,

[30:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1850s) so you don't wanna wait 15
minutes while the instance

[30:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1852s) is costing you money and the
image is being downloaded.

[30:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1853s) So we've done a lot of
work there to speed up that

[30:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1856s) I just talked about
minimizing hardware failures.

[30:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1859s) And then we're doing a lot

[31:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1860s) of contributions in the open
source space to make sure

[31:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1864s) that a lot of these popular
frameworks do work well on EKS

[31:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1867s) and speaking of them, yeah, Ray VLLM,

[31:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1871s) these are two of the, and
even in the last two days

[31:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1873s) in customer conversations I've been in,

[31:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1875s) I've heard these two projects
mentioned more than any others

[31:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1878s) is the ones that customers are now using

[31:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1882s) to serve inference workloads in production

[31:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1883s) using things like the,
the device plugins, EFA,

[31:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1888s) Nvidia neuron accelerated drivers,

[31:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1891s) all of that is a very
common infrastructure stack

[31:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1892s) that we're seeing customers
use for inference with EKS.

[31:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1900s) Oh no, what happened?

[31:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1912s) Okay, I dunno what's happening there.

[31:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1914s) Anyway, we'll skip, Rama
already talked about Karpenter,

[31:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1917s) but Karpenter really is the tool

[32:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1920s) that, especially for inferencing,

[32:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1921s) I mentioned Manage Node
Groups is good for training.

[32:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1925s) Inferencing is generally a
much more dynamic workload.

[32:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1928s) Karpenter is a good fit there

[32:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1930s) because it can help you
more easily take advantage

[32:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1932s) of the breadth and depth
of VC2 instance types.

[32:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1936s) In some cases you may want
to use Graviton instances

[32:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1937s) for inferencing, maybe
you don't necessarily

[32:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1940s) need to use GPU instances.

[32:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1941s) Karpenter in general, we're
seeing a lot of success

[32:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1944s) with customers do for inference workloads,

[32:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1948s) and hot off the press, some of you

[32:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1950s) maybe saw announcements
over the last couple days,

[32:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1952s) but we introduced what
we're calling auto mode

[32:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1953s) the other day, and part of auto mode

[32:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1956s) is integrating Karpenter into EKS,

[32:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1958s) making it easier to use.

[32:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1962s) Auto mode is really the new easy button

[32:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1965s) for the Kubernetes data plane,

[32:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1968s) the compute storage networking

[32:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1969s) that you generally need
to run in your cluster

[32:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1970s) now is included by default in EKS.

[32:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1974s) And I'm specifically bringing
it up in this presentation

[32:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1975s) because of the Karpenter angle.

[32:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1977s) Karpenter's good for inferencing,

[32:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1979s) it's now built in by default.

[33:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1983s) Some of the, you know, the
three things on the right,

[33:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1986s) compute optimization, cost efficiency,

[33:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1988s) supporting diverse workloads,

[33:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1989s) that's really built in Karpenter.

[33:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1990s) That's what it's doing.

[33:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1992s) The interesting innovation that we did

[33:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1995s) with Auto Mode, if you haven't been to any

[33:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1997s) of the presentations
yet, is we have this new

[33:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=1999s) operational model with EC2.

[33:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2002s) Where previously you had
two ways of running compute

[33:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2006s) in AWS you had the fully
managed lambda fargate model

[33:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2009s) where computes running
in a AWS owned account

[33:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2012s) or you had standard EC2
that was, you owned,

[33:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2017s) this new model EC2 managed
instances they're calling

[33:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2018s) is in the middle of that
or it's an EC2 instance

[33:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2020s) in your account.

[33:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2022s) But an AWS service like EKS

[33:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2025s) actually owns the
lifecycle of that instance.

[33:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2027s) So if you go to try to delete an E and I,

[33:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2029s) delete the instance, you
get an error that says

[33:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2031s) in use by a service and you
have to use that through EKS.

[33:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2034s) And I bring it up because
I think especially

[34:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2040s) in the top right here, the capabilities,

[34:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2042s) a lot of the hard parts of getting started

[34:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2046s) with machine learning workloads on EKS,

[34:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2047s) which is figuring out
the right device drivers,

[34:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2051s) the EFA plugin, configuring
instance storage.

[34:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2056s) If you have local disc
instances, you know,

[34:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2058s) customers used to have to
do these really complicated

[34:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2060s) user data scripts

[34:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2061s) to set up a raid zero
volume on the instance.

[34:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2063s) A lot of that is now fully
automated with EKS auto mode.

[34:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2068s) So we automatically configure Raid zero,

[34:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2070s) we automatically configure
the device plugins,

[34:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2073s) whether it's Nvidia

[34:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2074s) or Neuron, we already include, you know,

[34:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2077s) if you launch a GPU instance,

[34:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2079s) we're gonna pick the right omni
that matches that instance.

[34:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2081s) So just, there's a lot less work

[34:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2082s) you have to think about.

[34:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2083s) For training workloads,

[34:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2084s) I'm not gonna quite say
automotive is a great fit yet,

[34:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2088s) there's a 21 day max instance lifetime.

[34:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2092s) A lot of times we talk to customers

[34:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2093s) who are running training jobs

[34:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2095s) that go for months in some cases.

[34:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2096s) But I think for inference workloads,

[34:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2097s) for production running models

[35:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2100s) and production auto mode,
it could be a good fit.

[35:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2105s) Just an example of a pretty common stack

[35:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2109s) that we're seeing.

[35:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2110s) And again, this is validated
in the last two days

[35:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2112s) of conversations I've had with customers,

[35:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2114s) but using Ray, VLLM

[35:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2117s) and you know, you're using Karpenter,

[35:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2120s) which is gonna spin up
a standard CPU instance

[35:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2123s) to run the head pod and
the cube ray operator

[35:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2126s) and then it's gonna spin up, for example,

[35:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2128s) inferential instances

[35:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2129s) to actually run your serving workloads.

[35:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2132s) So this is a more and more
common pattern we're seeing

[35:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2133s) for customers actually
running inference workloads

[35:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2136s) in production with EKS.

[35:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2139s) And then finally, just a
few more customer stories,

[35:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2143s) H2O, Omi, Unitary, all of these customers,

[35:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2147s) I believe these are all
either case studies,

[35:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2149s) blogs you can go read about.

[35:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2150s) They've all moved to Karpenter

[35:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2152s) to do their inferencing workloads.

[35:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2154s) I think H2O is an
interesting one they've done,

[35:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2156s) they're using bottle rocket
to prefetch container images.

[35:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2159s) We have a a nice blog out there

[36:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2162s) that shows you how to do that.

[36:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2163s) I mentioned the 15 minute time it takes,

[36:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2165s) yes we can optimize that,

[36:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2166s) but the fastest way is
actually just gonna preload

[36:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2169s) the container image on
the instance itself,

[36:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2172s) which you can do with Bottle
Rocket quite easily now.

[36:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2175s) And other ones, yeah,

[36:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2176s) just using Karpenter, reducing costs.

[36:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2178s) We've seen a lot of these
customers have success

[36:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2182s) moving to Karpenter to do
their inference workloads.

[36:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2184s) Okay, I'll hand it off to Cas

[36:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2186s) to talk about one of
those customers who is one

[36:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2190s) of those customers who's
been successful with EKS.

[36:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2193s) - Cool, thanks Mike.

[36:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2196s) Hey everyone, I'm Cas Starak,

[36:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2197s) I'm a product manager leader
at Eli Lilly and Company

[36:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2201s) and I focus on research and AI products.

[36:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2204s) And just gonna share a little
bit from a customer experience

[36:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2208s) of building gen AI capabilities on EKS.

[36:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2211s) And I thought to start,

[36:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2213s) I could just talk a little
bit about the tech evolution

[36:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2216s) at Lilly and maybe help
explain why someone

[36:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2218s) from Eli Lilly is on an EKS
Gen AI track at re:Invent.

[37:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2222s) I'll talk a little bit about
our platform development

[37:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2225s) including EKS and then the Gen
AI scale up that's underway.

[37:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2228s) So just a little bit
of historical context,

[37:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2232s) the pictures here tell a
little bit of Lilly's history

[37:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2235s) with technology on the
left, it's actually 1987

[37:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2239s) and some classic eighties
corporate executives,

[37:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2243s) very excited about the
most recent delivery

[37:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2245s) of some personal computer technology.

[37:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2248s) And then on the right, some
of you might know what that is

[37:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2251s) or you can see the text there,

[37:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2252s) it's actually a Cray-2 supercomputer.

[37:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2255s) And in 1989,

[37:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2257s) Lilly was the first
non-governmental organization

[37:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2261s) to purchase one of those in the US.

[37:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2262s) And I just share that

[37:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2264s) because after joining Lilly a year ago,

[37:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2266s) I was pleasantly surprised
to learn about this history

[37:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2269s) of early technology adoption

[37:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2271s) and innovation that I
just, I didn't expect

[37:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2274s) to find in 150 year old company.

[37:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2276s) And there was, you know,
the software development

[37:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2278s) and the data science and
everything else that came along

[38:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2281s) with adopting those technologies.

[38:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2283s) Now, unfortunately, it was not just

[38:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2285s) a, you know, upward trajectory from there,

[38:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2287s) similar to the so-called AI winters

[38:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2291s) that, you know, that
industry has gone through.

[38:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2292s) We had some of our own kind

[38:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2294s) of technology innovation winters,

[38:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2297s) and it really started around 2001

[38:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2300s) in what in terms we call Year X.

[38:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2303s) And that was the year

[38:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2304s) that the first Prozac
patents started dropping

[38:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2306s) and going off patent.

[38:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2308s) And at the time that was actually 1/3

[38:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2311s) of Lilly's profits.

[38:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2311s) We had some other medicines
that went off patent.

[38:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2314s) And you can imagine as sales
come down dramatically,

[38:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2316s) there was a lot of examination of costs,

[38:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2318s) bring down costs and
things that were, you know,

[38:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2320s) quote, unquote non-core
like software development

[38:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2323s) and some of that technology
innovation was very hard hit.

[38:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2327s) And so there was this long period

[38:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2328s) where I think some of
that early innovation

[38:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2331s) started to atrophy a little bit.

[38:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2333s) But you flash forward today
and it's completely flipped

[38:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2336s) and there's a recognition
across the company

[38:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2339s) that we really do need
to become a tech company

[39:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2342s) to continue succeeding
as a medicines company,

[39:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2345s) you know, for years and decades to come.

[39:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2347s) And thankfully we've
been successful with some

[39:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2350s) of our recent medicines, we
have a very strong pipeline

[39:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2353s) and that's enabling us to invest

[39:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2353s) and there's been significant investment

[39:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2356s) and growth in those tech capabilities,

[39:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2358s) software engineering capabilities,

[39:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2360s) robotics automation, data
science, all types of AI.

[39:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2365s) And there's, you know,
much more of that coming.

[39:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2367s) And you know, one of
the things we're doing

[39:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2369s) as we're going through this evolution

[39:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2371s) and making these
investments is really trying

[39:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2373s) to adopt, you know,

[39:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2375s) most of the modern software
development practices.

[39:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2376s) And part of that is, you know,

[39:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2378s) a team was formed just a couple
years ago that I'm part of.

[39:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2381s) This is the software
product engineering team.

[39:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2383s) It's led by a former
Apple engineering leader

[39:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2387s) Go Cole Rad Krishnan.

[39:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2389s) And this team really focuses
on building scaled products

[39:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2392s) and platforms that are
gonna be high reliability,

[39:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2394s) high usage.

[39:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2396s) And we try to take an approach

[39:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2398s) that's really a kind
of software engineering

[40:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2400s) center of excellence to help demonstrate

[40:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2402s) and kind of spread those practices

[40:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2403s) across the developers at Lilly.

[40:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2406s) And a big part of is
this platform approach

[40:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2408s) where we're thinking
about shared libraries,

[40:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2410s) reusable components.

[40:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2412s) We tend to leverage a lot
of open source capabilities

[40:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2415s) and tools and doing things

[40:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2417s) like building broad observability tools

[40:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2419s) that can get used across the organization.

[40:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2422s) And one of the platforms that's
been a really big investment

[40:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2426s) for us is this CATS platform.

[40:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2428s) And so this is a cloud applications

[40:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2430s) and technology as a service.

[40:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2431s) And what this is is a
comprehensive cloud application

[40:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2435s) development and hosting solution.

[40:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2437s) And so we built this on AWS

[40:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2440s) and we use a series of open source

[40:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2443s) and AWS managed services to support it.

[40:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2446s) And this is a highly simplified diagram,

[40:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2449s) but some of the key points,
you know, we use EKS

[40:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2452s) for Kubernetes management, we use EC2

[40:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2456s) and Fargate for container execution

[41:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2460s) and we have other AWS
services integrated into it,

[41:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2464s) like S3 RDS, secret manager,
a whole slew of things.

[41:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2470s) We also do GIT ops, CICD automation.

[41:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2472s) So teams can go kind of seamlessly

[41:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2474s) from commit to production.

[41:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2476s) So kicks off with GitHub Actions,

[41:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2479s) docker image push to ECR,

[41:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2482s) Argo detects and then
automatically puts that

[41:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2485s) into the right Kubernetes environment.

[41:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2487s) And so, you know what
this means for developers,

[41:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2489s) it's really been a newer way of developing

[41:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2493s) we've shifted to the
cloud, they get, you know,

[41:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2496s) a lot of speed and efficiency

[41:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2498s) so they don't need to make a bunch

[41:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2501s) of infrastructure
decisions, let alone build

[41:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2502s) that infrastructure kind of laid out,

[41:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2505s) you know, a menu for them to get started

[41:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2507s) and then they obviously have the speed

[41:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2508s) of that automated deployment.

[41:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2510s) So that's been a big part

[41:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2511s) of our kind of tech transformation
evolution to the cloud

[41:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2513s) and it's gotten significant usage.

[41:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2516s) It also brings security.

[41:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2517s) So we have a lot of standardization

[41:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2519s) and we kind of, you know, lay some tracks

[42:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2521s) that we get people to follow.

[42:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2523s) And so that gets them into robust,

[42:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2524s) you know, security practices.

[42:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2527s) We have vulnerability scanning,

[42:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2528s) we've also provided observability
tools, so some of those

[42:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2531s) with the Amazon services.

[42:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2532s) We also use some open source
tools like Loki and Grafana.

[42:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2537s) So that teams building on this,
they get a lot of logging,

[42:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2540s) alerting, reporting,
visualization that can help them,

[42:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2544s) you know, manage their
applications as they scale.

[42:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2547s) And that last part's
really the biggest benefit

[42:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2550s) is the scale and reliability.

[42:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2551s) So, you know, once an
application is developed here,

[42:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2553s) it can scale up to, you know,
all of Lilly's workforce,

[42:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2557s) it can scale up globally

[42:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2559s) and there's really no
additional work for the team

[42:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2562s) and it maintains high
reliability when it does that.

[42:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2565s) So as I've mentioned, we've
seen significant adoption

[42:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2567s) over the last couple
years on this platform.

[42:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2570s) We've got hundreds of developers using it.

[42:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2573s) We've got growing number of applications,

[42:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2575s) growing number of commits
increasing exponentially

[42:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2578s) in, you know, global deployments

[43:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2581s) across, you know, many, many countries.

[43:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2583s) And one of the metrics I like,

[43:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2585s) I sat in the intern end of summer readouts

[43:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2588s) and it felt like almost
every intern mentioned CATS,

[43:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2592s) using it and how it helped accelerate

[43:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2594s) the development of whatever
their intern project was.

[43:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2598s) So I think that's a good
measure of its effectiveness.

[43:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2601s) And so you can imagine
some of the increase

[43:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2604s) in usage of this, A lot of
it is coming from gen AI

[43:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2607s) and we've been making
big investments there.

[43:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2609s) And just to give you some context,

[43:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2611s) really what Lilly's looking to do

[43:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2613s) is lead our industry in terms of,

[43:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2617s) you know, pharma peers in the adoption

[43:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2619s) of an impact from gen AI.

[43:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2622s) And we do think it's
fundamentally transformational

[43:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2623s) to a lot of the work that we do

[43:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2625s) and we've already been investing in it.

[43:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2627s) So Lilly actually has
a history of using AI

[43:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2629s) for drug discovery, small
and large molecule tools

[43:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2633s) for generating its screening

[43:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2636s) and there's actually a pretty
solid data science team

[43:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2639s) that's been doing NLP work

[44:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2640s) before all the LMS came out

[44:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2642s) to do things like clinical summarization.

[44:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2643s) So there's a history of
that that we're building on,

[44:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2646s) but we're really going all in on gen AI

[44:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2648s) and we're working with the
hyperscalers, we're getting,

[44:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2652s) you know, out of box
solutions, we're working

[44:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2655s) with smaller companies, startups

[44:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2656s) for more, you know, organization

[44:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2658s) or use case specific solutions.

[44:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2659s) But then we're also doing a
lot of internal development

[44:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2662s) and as part of this tech
transformation we're going through,

[44:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2664s) we are looking where
does it make sense for us

[44:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2666s) to have some of those
capabilities internally?

[44:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2668s) And some of that is use
case and proof of concept,

[44:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2671s) but really we try to focus
on what are scaled products

[44:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2673s) and platforms that can serve the company.

[44:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2675s) And one of the platforms
that we decided to build

[44:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2678s) was a, you know, broadly usable

[44:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2680s) developer facing gen AI platform

[44:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2682s) to help accelerate that work at Lilly.

[44:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2685s) And I can actually a little bit here.

[44:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2687s) So we knew gen AI is
gonna be big, we want it

[44:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2690s) to be reliable, we wanted
to be able to scale

[44:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2692s) large number of users globally.

[44:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2694s) So we decided to build it
on top of that CATS platform

[44:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2697s) that I just walked you through.

[44:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2699s) And we put together these main components

[45:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2701s) and we started this development in 2023.

[45:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2704s) We had our first production
release in December

[45:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2706s) and we've been adding features

[45:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2708s) and capabilities as we've
gone through the year.

[45:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2709s) At the foundational level
it's a model library,

[45:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2712s) so we want teams to be able

[45:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2713s) to choose from the
latest and greatest LLMs

[45:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2716s) and we're constantly
updating it, you know,

[45:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2717s) we're big fans of the
anthropic line of models,

[45:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2721s) but we also have Open AI,

[45:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2724s) Gemini, hugging face, lama.

[45:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2727s) You deploy pretty much any
model from hugging face

[45:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2729s) if you get the legal approval.

[45:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2730s) And we allow teams to
choose, you can host those

[45:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2734s) as retail, we have open source,

[45:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2736s) there can be fine tune models,

[45:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2738s) you can host them locally
in our GPU cluster.

[45:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2740s) And then on top of that we
built orchestration tools.

[45:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2743s) So it started fairly simple

[45:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2746s) and we use lang chain as our
main orchestration framework

[45:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2748s) and we started fairly
simple with some tools

[45:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2751s) for prompt engineering and model chaining.

[45:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2752s) And we've added in,

[45:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2754s) you know, more and more
complex orchestration tools

[45:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2756s) and you can now support agentic workflows

[45:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2759s) and multi-agent systems with it.

[46:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2760s) And then we have tools for operations,

[46:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2762s) scaling and maintenance.

[46:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2763s) So we try to take care
of a lot of the scaling

[46:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2766s) that the teams are gonna need

[46:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2768s) so they don't need to worry about it.

[46:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2770s) So our central team, you know,

[46:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2772s) has an ops team thinking
about provisioning capacity.

[46:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2774s) We recently worked with the
AWS team to help optimize

[46:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2777s) some of our like cross regent inferences

[46:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2779s) and our rate limiting capacity

[46:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2782s) to help get better performance
at scale, lower latency.

[46:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2785s) And so we're kind of doing
those things centrally

[46:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2786s) so that other teams don't
have to worry about it

[46:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2789s) as well as quality and monitoring.

[46:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2792s) So we've created various
eval tools so that teams

[46:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2795s) as they're scaling up
can monitor for drift

[46:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2797s) or if they want to assess,
you know, the latest model,

[46:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2800s) they can easily check
how performance changes.

[46:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2802s) We also have data
integrations that, you know,

[46:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2806s) where they're specific
to the Lilly environment.

[46:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2807s) We're always trying to add new ones there

[46:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2809s) and information retrieval tools.

[46:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2811s) We started with a fairly kind of vanilla

[46:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2814s) semantic search capability vector database

[46:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2817s) and we've been adding in more complexity,

[47:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2820s) we made elements of that tunable.

[47:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2821s) So if teams wanna optimize

[47:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2824s) things like, you know,
chunk size and overlap,

[47:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2826s) they can get in there and do that.

[47:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2828s) And then we started adding other things

[47:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2829s) like contextual chunking and hybrid search

[47:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2832s) and continuing to prove
the information retrieval.

[47:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2835s) So again, teams don't need
to go out and build that.

[47:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2837s) And we have it kind of optimize
to the Lilly environment

[47:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2839s) and all of it's wrapped in this oversight

[47:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2841s) in compliance and security layer.

[47:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2843s) So we have full input output logging,

[47:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2846s) cyber has visibility into that,

[47:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2848s) into all of the configs, all of the users.

[47:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2850s) We also have scanning and alerts,

[47:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2853s) it's configurable by our cyber team.

[47:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2856s) We use some AWS tools

[47:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2858s) as well as some open
source tools to do this.

[47:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2860s) And it helps give a lot of
reassurance to our cyber team

[47:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2863s) and actually kind of points
this as a preferred platform.

[47:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2867s) And so what that has
allowed us to do, again,

[47:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2869s) we've been able to accelerate development

[47:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2872s) so teams are able to
get started very quickly

[47:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2873s) and get to POCs and MVPs quickly.

[47:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2876s) They have optionality.

[47:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2878s) So you heard the guys earlier
talk about the importance

[48:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2880s) of, you know, different models
for different use cases.

[48:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2882s) I think Andy talked about
it in his keynote yesterday.

[48:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2885s) And so teams can easily
switch back and forth

[48:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2888s) and figure out which model
is right for their use case.

[48:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2891s) I mentioned, you know, quality
security compliance built in.

[48:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2895s) And then because we've
built this, you know,

[48:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2896s) on AWS on EKS, it's very scalable.

[48:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2901s) So we've had use cases that
have gone from, you know,

[48:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2904s) small early testing to deploy
globally without, you know,

[48:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2907s) having major issues or downtime

[48:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2910s) and not requiring a ton

[48:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2912s) of work from the teams
actually doing the development.

[48:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2915s) And so, you know, we
launched it originally

[48:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2919s) into production in 2023 in December.

[48:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2921s) So it's been, you know, less than a year

[48:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2924s) and we've been impressed with the uptake

[48:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2926s) and it's really impacting
every part of our business

[48:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2929s) and we see this transformation happening.

[48:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2931s) Just some examples,
probably my favorite one

[48:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2933s) is this agentic discovery assistant.

[48:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2936s) So there is a chem informatics agent.

[48:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2938s) It has access to about 20 different tools.

[49:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2940s) Some of those are chemin
informatics tools,

[49:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2943s) some of them are internal databases

[49:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2944s) with Lilly molecule information.

[49:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2947s) They're external databases

[49:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2949s) and we have an LM that's,
you know, answering questions

[49:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2952s) or executing, you know,
user prompt workflows

[49:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2956s) and choosing which of those tools to use.

[49:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2958s) And it allows these very
powerful workflows to be executed

[49:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2962s) that can aid our scientists
in early stage discovery.

[49:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2966s) We have things in the
clinical trial space,

[49:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2968s) so helping with how we
respond to regulators.

[49:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2971s) We get thousands of questions

[49:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2972s) and have to answer those from
regulators all over the world.

[49:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2975s) It's a natural thing for LMs to help us do

[49:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2978s) we have tools in our manufacturing space.

[49:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2981s) So we have global manufacturing,

[49:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2983s) there's a huge focus on our
manufacturing line uptime.

[49:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2987s) And so we have this assistant

[49:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2988s) that's been developed using this platform

[49:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2991s) that uses structured and
unstructured data from like SOPs

[49:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2993s) as well as equipment sensor data to help

[49:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=2997s) as our line operators
monitor and manage uptime.

[50:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3001s) There's claims drafting tools

[50:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3003s) and we're even developing
our first patient facing

[50:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3007s) Q&A tool on the platform.

[50:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3009s) So it's exciting to see that adoption.

[50:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3012s) And then in terms of results,

[50:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3014s) we've seen the acceleration,

[50:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3017s) so we've heard it anecdotally from teams

[50:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3018s) and then we've seen teams,
you know, in a little

[50:21](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3021s) as a few weeks they're
able to get a POC out there

[50:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3022s) or in a few months, actually have an MVP

[50:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3024s) that's pushed into production

[50:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3025s) because they have these
tools ready and available.

[50:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3028s) We're able to meet quality
security compliance.

[50:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3030s) It's really become a preferred
platform from our cyber team

[50:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3034s) and you know, they
encourage folks to use this

[50:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3036s) because we have all of that
visibility, logging and alerts

[50:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3039s) and then it's enabled rapid scale up

[50:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3042s) and we've seen a lot of adoption.

[50:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3043s) So we have over 500 developers
at Lilly using the platform.

[50:47](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3047s) There's thousands of end
users in over 30 countries

[50:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3050s) and in a given month we
have billions of tokens

[50:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3054s) that are processed by the platform.

[50:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3056s) So the scale has been, you
know, what we were hoping to see

[50:59](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3059s) and it's supporting this
tech at Lilly evolution.

[51:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3061s) Obviously we're building
products on top of it

[51:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3063s) that are impactful, but because
of the work we're doing,

[51:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3067s) it's also this kind of
virtuous cycle of attracting

[51:10](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3070s) and retaining, you know, talent
that wants to work on this.

[51:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3073s) And it's kind of supporting

[51:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3074s) that transformation I was talking about.

[51:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3076s) And you know, lastly, just to
close, some lessons learned,

[51:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3079s) I would say the main lesson is, you know,

[51:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3083s) our kind of belief and intuition

[51:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3084s) that having this platform approach,

[51:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3087s) so using a scalable platform, you know,

[51:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3090s) like EKS building this, you know,

[51:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3093s) somewhat opinionated approach
to gen AI development.

[51:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3097s) It's worked, we have developers using it,

[51:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3099s) it's accelerating it,
we're seeing things scale,

[51:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3102s) we're seeing things move into production.

[51:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3102s) So I think that's probably
the biggest lesson learned.

[51:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3104s) But some of the other
things along the way,

[51:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3106s) if you build it, you know, some will come.

[51:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3108s) So when you build a platform like this,

[51:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3111s) you're gonna have the few early adopters

[51:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3112s) that just naturally just start using it.

[51:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3114s) Especially in a place like
Lilly, you'll have kind of

[51:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3117s) that top of the curve
really capable, you know,

[52:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3121s) fast moving developer teams

[52:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3122s) but then there's you know,

[52:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3123s) a whole distribution curve after that.

[52:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3124s) And if you wanna get more
adoption, there's a lot of work

[52:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3126s) around evangelizing, answering questions,

[52:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3129s) getting support documentation out there,

[52:12](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3132s) getting support teams, product mindset.

[52:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3135s) So we've really treated it like a product.

[52:16](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3136s) We have product manager or roadmap.

[52:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3138s) We're really always trying
to gather voice of customer

[52:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3140s) to make sure, you know,

[52:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3142s) we might be very excited about building,

[52:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3143s) you know, the latest
incremental improvement

[52:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3145s) to the information retrieval pipeline.

[52:27](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3147s) But our customers like,

[52:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3148s) I just wish your QA environment
was a little more stable.

[52:31](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3151s) And so making sure we don't
get too lost in the engineering

[52:33](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3153s) and technology of it, but stay grounded

[52:35](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3155s) with the customers has been important.

[52:37](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3157s) And then expectations increased rapidly.

[52:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3160s) So initially there was skepticism

[52:42](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3162s) and it's like for some
developers at Lilly,

[52:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3163s) this is like a new approach

[52:45](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3165s) kind of channeling them
into a certain platform

[52:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3168s) and putting some constraints around it.

[52:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3169s) But the, you know, skepticism
quickly turned to like,

[52:53](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3173s) oh I see, it's speeding it
up, it's making it easier.

[52:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3175s) I get the approvals and
we're seeing adoption

[52:56](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3176s) and then it turned to like, oh
now I want this, this, this,

[52:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3178s) where's the documentation?

[53:00](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3180s) What are your formal SLAs?

[53:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3182s) So I'd say if you're taking this approach,

[53:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3183s) make sure to think ahead of it.

[53:05](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3185s) And if you're building the platform,

[53:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3186s) keep up with the documentation,

[53:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3188s) keep up with the support, you know,

[53:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3189s) get ahead of okay communicating SLAs.

[53:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3191s) 'cause especially in a place like Lilly,

[53:14](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3194s) we have patient facing stuff,
we have manufacturing stuff,

[53:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3197s) there's 24/7 expectations.

[53:19](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3199s) And then lastly I mentioned
the cyber partnership

[53:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3202s) and investing in that early
was pretty key I think

[53:25](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3205s) to this platform success,
especially in a company like Lilly

[53:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3208s) where there's a high bar around cyber

[53:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3209s) or privacy legal and all of that.

[53:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3212s) So with that I think I'll
turn it back over to Rama.

[53:41](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3221s) - Thanks Cas, I appreciate
you taking the time

[53:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3224s) to share those awesome insights with us.

[53:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3226s) So something we have talked a lot about

[53:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3229s) throughout this presentation
has been that customers

[53:52](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3232s) want to integrate to us
as solutions on top of EKS

[53:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3234s) to achieve the desire ML functionality.

[53:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3237s) So a lot of our customers were asking us

[53:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3238s) for guidance around how
to get started quickly

[54:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3241s) integrating these solutions.

[54:03](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3243s) What are the best practices
for integrating them?

[54:06](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3246s) Can you provide us some templates

[54:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3247s) and patterns that you're
seeing success with?

[54:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3248s) So that's why we launched
the data on EKS project.

[54:11](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3251s) It's an open source project

[54:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3253s) where we publish different gen AI patterns

[54:15](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3255s) that we have seen across our customers.

[54:18](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3258s) We publish blueprints,
patterns, terraform templates

[54:22](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3262s) that you can use to easily get started

[54:24](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3264s) integrating some of the
popular OSS solutions

[54:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3268s) that we see getting integrated with EKS

[54:29](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3269s) for solving those ML specific challenges.

[54:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3274s) So we have launched a
number of these patterns

[54:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3278s) over the last year.

[54:39](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3279s) We continue to create more
patterns as we see success

[54:43](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3283s) with those patterns in in the real world.

[54:46](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3286s) We have been placing special focus

[54:49](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3289s) on releasing inference specific
patterns on top of EKS.

[54:51](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3291s) Some of the things that we
have recently released are,

[54:55](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3295s) Nvidia with VLLM, Racer with VLLM,

[54:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3298s) Nvidia NIMS on EKS, so on and so forth.

[55:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3302s) So check out our data on
EKS website where you'll see

[55:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3304s) a lot of different patterns for inference

[55:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3307s) and for training and fine tuning as well.

[55:09](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3309s) With that, we have almost
come to the end of it.

[55:13](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3313s) There are some interesting
sessions that are coming up

[55:17](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3317s) with EKS, Amazon EKS
infrastructure as code

[55:20](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3320s) gitops session on that as well.

[55:23](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3323s) And there is an interesting
session from S&P Global

[55:26](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3326s) that have implemented gen AI on EKS

[55:28](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3328s) and how they're scaling to meet

[55:30](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3330s) millions of inference requests per week

[55:32](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3332s) using that setup as well.

[55:34](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3334s) And we also have the Future of Kubernetes

[55:36](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3336s) on AWS session coming up tomorrow

[55:38](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3338s) that you can check out.

[55:40](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3340s) You can continue your Amazon EKS learning

[55:44](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3344s) through some of your
resources available out there

[55:48](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3348s) through workshops, through
getting digital badges

[55:50](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3350s) and best practices guides as well.

[55:54](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3354s) With that, we come to
the end of the session.

[55:57](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3357s) Thank you for listening to us patiently,

[55:58](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3358s) and if you have any questions,
we'll be hanging out

[56:01](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3361s) outside the room for some time.

[56:02](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3362s) You can approach us

[56:04](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3364s) and we can answer any
questions for you as well.

[56:07](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3367s) Thank you.

[56:08](https://www.youtube.com/watch?v=25tRVE2xq1I&t=3368s) (people clapping)

