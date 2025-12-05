# AWS re:Invent 2024 - Simplify Kubernetes workloads with Karpenter & Amazon EKS Auto Mode (KUB312)

[Video Link](https://www.youtube.com/watch?v=JwzP8I8tdaY)

## Description

Kubernetes makes building and running complex applications simpler, but using Kubernetes comes with a unique set of challenges, such as security, networking, interoperability, storage, and scaling. Amazon EKS eliminates the need to install, operate, and maintain your own Kubernetes control planes, alleviating many challenges, but responding quickly to new workload requirements while balancing cost and performance can be difficult. In this session, learn how Karpenter and newly launched Amazon EKS Auto Mode simplify managing your Amazon EKS cluster, from cluster creation and running your application to day 2 operations and everything in between.

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

- All right, welcome everyone. I know this is Tuesday afternoon, you have a lot of choices on the sessions. First of all, thanks for
coming to this session. Little bit of Easter egg, for those of you who have
been watching the catalog, you'd noticed the title
of our session changed. So you signed up for Karpenter, you are getting Karpenter, and then some. My name is Raj. I'm a Principal Solutions Architect for Containers and Serverless at AWS. I've been at AWS for six years and I have helped many
customers migrate to Kubernetes and Serverless. Today, I'm gonna co-present
with Sheetal Joshi. - Hello, I'm Sheetal Joshi. I'm a principal SA for
Containers here at AWS, predominantly working with the EKS and the Kubernetes customers and I'm very excited to
co-present with Raj here, today. - Excellent.
- There you go. - Let's get started. Okay, today we're going to talk about how do customers adopt Amazon EKS? And then, of course this is a Karpenter and EKS Auto Mode session. So we'll talk about how do customers scale their applications? And then, we're gonna
talk about some challenges and how to solve them
with Karpenter and beyond. And at the end, we are also
going to share some resources for you to learn more. So if we go back six years, we released Amazon EKS. Kubernetes is awesome. I've been working in
Kubernetes for a long time, but our customers told us that self-managing the control
plan is difficult. So that's why Amazon EKS was born. So, EKS is a stable and
secure way to run Kubernetes and we run fully upstream and certified conformant Kubernetes. All right, so at this point
you are like EKS is great. I want to get started with EKS. So how do you do that today? First, you create your cluster and what that does is it creates a control plan in AWS account where we make it scalable, highly available, and secure. Next, you want to deploy your workload but not so fast. Before you deploy your workload, you also need to install some
add-on and controllers, right? So generally, you create
a managed node group, two or more EC2 instances, and then you install add-ons like ingress controller
or storage controller and some of the other ones. Okay, at this point you installed all those add-ons and controllers and then you deploy your application. So, you create a managed node
group and then you deploy and the pod gets deployed there. But of course, this is a scaling session so we have to talk about autoscaling. So, we're like, you know what? This app we made is going great. At this point you install
something like Cluster Autoscaler and then your pods scale
across multiple instances. Cluster Autoscaler is great, however, Cluster Autoscaler
has some challenges. With Cluster Autoscaler, you need to create node groups, either managed or self-managed. And in those node groups, you have to specify what instance families it should be using as
well as their priority. Also, with Cluster Autoscaler, you need to create Autoscaling Group. Now, Autoscaling group comes, autoscaling group is great, but it comes with some challenges. So for each node group you have to have a separate autoscaling group. If you want your workload to spread it across
multiple availability zones, you need to create multiple
autoscaling groups, et cetera. And finally, the AMI selection
and refresh is cumbersome. For those of you who are running Cluster Autoscaler in production, you know you have to
manage the launch template, anytime an AMI is changed,
you have to go change it, run recycle commands, all that stuff. For that reason we created Karpenter. So how does Karpenter work? So first, the pod scales using
horizontal Pod Autoscaler. Then the pods go pending and with Cluster Autoscaler
it has the Cluster Autoscaler Autoscaling group, but Karpenter bypasses all of that and it interacts directly with EC2 Fleet. Because it is bypassing all those hops. Karpenter is faster. Also, when we created Karpenter we wanted it to be Kubernetes native and as Kubernetes
enthusiasts, we love YAML. So you can control the behavior of Karpenter using two YAML files, NodePool and EC2NodeClass. Okay, so let's go back to our process. So instead of Cluster Autoscaler, you install the Karpenter, add-on. Okay, and then your application scale. And now, you do not need to
have any managed node group. Your instances are coming up faster, things are good. Even though scaling is the
bread-and-butter of Karpenter. Karpenter does way more than scaling. Karpenter does cost
optimization out of the box. Karpenter supports diverse workloads including machine learning
and generative AI. And Karpenter, also helps
with upgrade and patching. For that reason, Karpenter is the total data plan implementation. Karpenter is made with love at AWS, but we donated it to the
open-source community and it is one of the CNC projects now under SIG autoscaling. And we are very proud to
see how Karpenter is growing and how customers like you are contributing to the Karpenter. Okay, so let's start this point. We're like, okay, Raj, Karpenter is great, how do we get started with this? So, we see the journey in
our customers like this. First, you evaluate the
features of Karpenter, then you implement it, then you do Day 2 operations, and maybe finally,
there is some evolution. And throughout this talk, we are going to follow the same process. All right, so let's start
with the evaluation phase. For your containers to run,
it requires different things, CPU, memory, storage, et cetera. And, how does it map to
different EC2 instances? There are many different EC2
instances that we provide you. The larger the size,
the larger CPU you get, and then the instance family
determines CPU to memory ratio. And, we give you a lot of flexibility. We have over 800 different
instance types to choose from, such as GPUs like P4d, or the latest generation
custom silicon instances like INF2 or TRN. So first question is, how do I control which EC2s
does Karpenter spin up? Well, remember we talked
about the node pool YAML? So this is a sample node pool YAML. Using this node pool YAML, you can control how Karpenter behaves. For example, on the top we are saying, instance family should
be within c5, m5 and r5. And I'm showing off a little bit here, Not only you can use the operator in, but you can also use not in. So you are like okay,
use those instance types but do not spin up anything
which is nano, micro, small or medium whatever,
depending on your workload. And, we realize it's not easy to choose from 800
different instance types. So all these fields, if you're
thinking, Raj, this is great but this is a lot. So you can keep this all empty and AWS will automatically choose the appropriate instance type for you based on your deployment
pods resource requests. And, we always have those
sneaky SRE teams who are like, or the sneaky app developers like myself, who I was before. It's like I need lot
of CPU, lot of memory, and for that reason you can also limit how many EC2 instances this
node pool can provision. So in the bottom, you could see we have the
limit of CPU of a hundred. So this node pool will keep
on provisioning EC2 instances 'til the aggregate amount
of CPU, which is a hundred. I'm just showing CPU but
this also works with memory. You can also control things
like availability zone. For example, you can say, hey, split
it up within US 2a, 2b, or any specific AZ. Unlike autoscaling group, you do not need to create different node pools for this. Also, you can control
the architecture type, you can use x86 or Arm, like Graviton, based on your workload. And finally, a lot of you
want to mix in spot instances. In the bottom, I'm showing that capacity-type
spot comma on demand. If you specify both spot and on demand, Karpenter will always prioritize spot, but it is intelligent enough to know when the spot capacity is low, it will automatically fall back and create on demand instances. And we all know, for those of us who have given Solutions Architect Associate
Certification exams, you know the question always comes, what is one thing you need
to keep in mind with spot? It can go away with
two-minutes warnings, right? Karpenter handles that two-minute warnings and you do not have to
do anything yourself. It will spin up a backup
spot instances for you and cordon and drain
the terminating instance and move the pods in a rolling deployment fashion. You do not need to install and manage node termination handler. It has built-in spot interruption handler. Okay, moving forward, for those of you who have used real-world production
workload in Kubernetes, you also need to have
scheduling constraints. With Karpenter, you can use
different scheduling constraints like node selectors, node affinity, taints and tolerations, and topology spread. So this is of course, used
a lot in your project. So let's take a deeper look at this. So let's say, on the left,
I'm showing a node pool and this node pool spins up a
spot instance of capacity-type and also architecture-type AMD64, whichever instance this
node pool provisions, Karpenter will attach
all these key value pairs as labels to the nodes. So for example, Karpenter
will put capacity-type, colon spot, Kubernetes.io
slash architecture colon, AMD64, et cetera. What does that mean? So on the right, I'm showing a sample
pod specification file, you can use those key value pairs to schedule the pod in specific instances. So in this case, if you deploy this, if the EC2 was already running into, the pods will get scheduled there. If there was no EC2 running, Karpenter will spin up a spot instance to satisfy the scheduling requirements. Karpenter will also attach
well-known labels to your nodes. You do not need to do anything special. For example, the zone, instance type, operating system, et cetera. So you can use all these fields in your pod specification
file for scheduling. Okay, you might ask those,
that's a good start, how about user-defined labels? Karpenter supports that, as well. So in this example on the left, I'm showing how to use
user-defined annotation, taints and labels in your node pool. And on the right, you
can reuse those labels, taints and annotations
to schedule your pod. This is a very, very popular
way to schedule parts for different applications, right? You can have different node
pools with different labels and the different teams can
use those different labels to schedule their workloads. Which brings us to a good question. How many different node
pools should you define? Well, you have different options. The easiest one is a single node pool. So you put everything in
a single node pool YAML and then each team, whatever they need, they use those fields to specify and then schedule those pods. The most popular one that
I see with my customers is multiple node pools, where each team has their
own separate node pool. One of the big reasons is, maybe one team is running
expensive GPU EC2s, and remember the limit-fields
for that node pool, you can limit them to a certain
amount of CPU or memory. Maybe, there is a noisy neighbor, they need more CPU and memory than others. They need different types of instances. So you can separate the teams
using separate node pools. Another advanced strategy
is weighted node pools where you can prioritize
one node pool before others. When will you use it? If you want to prioritize
reserved instances or savings plan ahead
of other instance types. So pretty sure this part
is a little confusing. So let me give you an example. In this example, I'm
showing two node pools. The top one has the
weight 60 on the bottom and see the instance types are c and r. I'm assuming you have
reserved instance contract for those two instance types. So anytime a pod goes pending, it will use the first node pool, and it'll keep on spinning up instances 'til it reaches the limit, right? Let's say you have
reserve instance contract for certain number of EC2s. So it'll keep on spinning up EC2 instances 'til the CPU or memory reaches thousand and then the other node
pool will take over. Oops, let me go back. Then the other node pool will take over and then it'll keep on provisioning different instance types. All right, remember I talked about Karpenter can optimize
cost out of the box. So at this point your cluster
is running with Karpenter. Proper instance types are chosen, however, over time your cluster may
end up looking like this. For worker nodes, the fast worker node nicely utilized and bin packed, the last three, not so much. With Karpenter, you can specify the consolidation policy when empty or underutilized and Karpenter will automatically
bin pack your pods, terminate the unnecessary instances and saves you a lot of money. However, one feedback we
got from our customers is this is great, but Karpenter
runs this simulation and this consolidation
every 10 seconds or so. So this could be lot of nodes
coming up and coming down. So for that reason we
introduced another knob for you to control this behavior. This is included in Karpenter version one. The field is consolidated after. So see on the bottom, I'm showing consolidated after one hour. So even if you're EC2
instances looking like this, it will wait one more hour
before it consolidates because you know your workloads the best. If you know some new
workloads gonna come in after five minutes. So you are telling Karpenter, hey don't touch these EC2 instances, don't consolidate yet. Let's wait for a little bit of time. So let's say one hour passes, no new pod gets added or removed, only after that Karpenter will consolidate and terminate the unused instances. Not only Karpenter can consolidate to the existing instances, Karpenter can also replace
and right-size instances. So in this case, the
second and third instance, m5.xlarge, even if you bin pack those
two pods in one m5.xlarge, there is still an inefficiency. Karpenter is smart enough, in this case it will
terminate both these m5.xlarge and spin up a m5.large,
so half the instance size and save you a lot of money. And all this happens out of the box. Now, one question I get
is, Raj, this is great but you know a lot of critical workloads running in the middle of the day, and I don't want Karpenter to disrupt all these EC2 instances. For that reason, we
released disruption budget with Karpenter version one. Using this disruption budget, you can specifically control the behavior of this disruption. So let's go through this. In this YAML, so this is part of node pool YAML, the first block says, nodes zero. So that means zero nodes can be disrupted during the schedule Monday
to Friday from nine o'clock for duration eight hours. So nine o'clock to five o'clock, for the reason, drifted and underutilized. So even if Karpenter can
consolidate those nodes, it will not touch them Monday
to Friday working hours. What if they're empty? You are like, you know, empty nodes, I don't care, nothing can be disrupted. So a hundred percent of those
nodes could be disrupted. Doesn't matter whether it's
working hours or weekends. Now, the last one says, outside of those working hours, so 10% of the nodes could be disrupted for the reasons, drifted and unutilized. So remember, this is all cumulative. So if I put all this together, that means 0% of the nodes could be disrupted during working hours. A hundred percent of the
nodes could be disrupted for when they're empty even during working hours and for the nodes outside
of the working hours for the reasons, drifted
and underutilized, only 10% of the nodes could
be disrupted at a time. So I talked about drift. What is drift? So Karpenter is Kubernetes native, and the Kubernetes core principle is, to reconcile between the desired state and the current state. And, Karpenter is no different. So let's say in this case, in the node pool you have a
reserved instances contract, you are using m5.large. So all the EC2s that this
node pool spun up is m5.large. Let's say you go and change this m5.large to c5.large. So in this case, the desired
configuration in the node pool will deviate from the running instance, which is m5.large. So Karpenter will automatically cordon and drain the running m5.large
spin up a c5.large instance and move over your pods. Okay, so at this point we
learned about NodePool. NodePool controls the instance family, availability zone,
budgets, all that stuff. But how about AMI subnet security group? That's what EC2NodeClass does. So for example, you can select which subnets are eligible to launch your EC2. You can attach certain
security groups to EC2, in this case, the name, my security group. You can select the AMI for EC2 and you can have other
things like user data, attach tags, define EBS, and more. So, AMI is the important one. So let's take a look. So you can use AMI selector
to select from different AMIs. Amazon provides you EKS
optimized AMI out of the box. So to use them, in the EC2NodeClass, you could use something like, alias at the bottle rocket, at the latest. So any EC2 that this Karpenter provisions will run with EKS optimized
AMI or bottle rocket with the latest version. Similarly, another example
could be Amazon Linux 2 at the latest. The supported family values
in alias are al2, al2023, bottle rocket, Windows
2019 and Windows 2022. Now, you may say latest is great, but what if I want to pin my work nodes to a specific version, and I want to test out the new version, then only go to the latest version. You can do that, as well. So as part of the Karpenter V1, you can pin your work nodes to a specific AMI version, like this. So for this case I'm saying alias bottle rocket at the rate v1.20.5. So all the EC2s that this
node class will provision will be of this version of bottle rocket. Similarly, Amazon Linux 2
with the with the version of 2024, July 29th. What about custom AMI? Karpenter supports custom AMI, as well. A lot of my customers uses custom AMI. You can select custom AMI using tag, name, owner, as well as ID. If multiple AMIs are found
satisfying these conditions, Karpenter will use the latest one. If no AMI is found, no nodes will be provisioned, right? So this part is a little scary. You don't want to, you want to avoid this and you can, once you deploy EC2NodeClass, you can check the status
fields for this AMI field and it will show if the
conditions are selecting any AMIs. Okay? So if you have been following the theme, AWS is customer-obsessed. So, we went from okay
customers self-managing the control plan. So we created EKS, then we were like, okay, EKS is good, how can we make your lives better? Okay, so we created Karpenter. Now, what about after Karpenter? So to talk about that, I'm gonna invite my
co-presenter, Sheetal, on stage. - Thank you, Raj. That was a great deep-dive into Karpenter and it was cool to see
how those like, you know, in reality that consolidation and the optimization was
working, that was really cool. So you work with a lot
of customers, right? Karpenter and no Karpenter. So what are some of the challenges that you hear from your customers who are actually running
Karpenter or Cluster Autoscaler? - Yeah, one challenge I hear is, okay, Raj Karpenter is great but there are so many fields in that YAML file, how do I
select those fields, right? Like, what do I select so that the EC2 instances are
optimized and right-sized? So likewise, Sheetal, you
work with a lot of customers, what challenges do you
see in your conversations? - Well, these applications
are not lone wolf, right? So they actually depend on
the core cluster capabilities such as what we call as add-ons. Whether it is part networking
or the service discovery or the load-balancing capabilities. Along with that, any of
the user defined add-ons that customers really require to meet their business,
like you know, requirements and most importantly, the last one here is
upgrading the clusters and keeping your Kubernetes cluster safe, is the biggest, biggest
challenge for, I think, most of you who are actually
attending this session, right? Which actually requires
a dedicated expertise and the continuous time investment which kind of slows down the innovation that customers are really looking for. So this is great. I think some of you might already be thinking
like Raj talked about all of the Karpenter details and seems like it addresses the challenges that we just talked about, but what do you think are the challenges beyond Karpenter, Raj? - Yeah, it'll be good like to have some best practice recommendations to run the add-ons, controller, and something
that's like built-in. What about you, Sheetal? - Yeah, I think these
management of the add-ons and their versions and the lifecycle of these controllers is a big challenge as well, right? Karpenter doesn't address
any of those needs and it's a controller by itself. So just managing the Karpenter with all of the best practices is a big challenge for our customers and yet again, I think
you touched upon it, but ease-of-use and out
of the box capabilities, how do I get started quickly? I think that's one of the major questions that our customers always ask. - Great. Seems like you
have answers for this and something up your sleeve so I'll leave you to it on the stage. - Thank you so much, Raj. So without further due, let me introduce you to
Amazon EKS Auto Mode. So what is it? Amazon EKS Auto Mode, I think, if you are following the news, AWS news, blog post, it's everywhere. So technically, Amazon EKS
mode is gonna streamline your Kubernetes cluster
infrastructure management. So, let's dive deep in the next 20 minutes of what actually EKS Auto Mode is and how does it simplify
application deployment onto Kubernetes clusters. So the first one, when you
use Amazon EKS Auto Mode, it kind of brings in
that increased agility and accelerates the innovations by offloading cluster operations to AWS. And, how do we do this? With the introduction of
the Amazon EKS Auto Mode, EKS is taking on more responsibility under the shared responsibility model beyond the Kubernetes control plane that we have always managed to the Kubernetes data plane, as well. So the next one, it basically improves the performance and maintains the application availability by dynamically scaling
the compute resources that your applications depend on. And along with that,
it's secure by default. So what do we mean by secure by default? EKS Auto Mode automatically updates your worker notes and also applies the
security fixes automatically. So the last one, it
continuously optimizes the cost with automatic capacity
planning and dynamic scaling. So, how does it do it? So as you can see here,
you create a cluster, it's still the same API,
that doesn't change, it's still Amazon EKS, and when you create a cluster, it includes all of the core capabilities that are basically required for production-ready clusters, right? So you create a cluster, you get managed control plane, the API server and the HCD instances. Along with that, all of these
core capabilities included alongside. And next, when you
deploy your applications, it automatically provisions
cluster infrastructures. So in how does it do? Amazon EKS Auto Mode is built on the principles of Karpenter. So it keeps watching for the applications and when you deploy your applications, it launches the nodes
looking at the requirements that are specified within
application manifest, it's dynamically scaled resources as the application scale changes and it continuously optimizes for cost. As you saw, all of the
optimization principles and the consolidation principles that Raj talked about, still apply here. And the last one, it
automatically updates the notes and the core cluster capabilities. So let's go back to this slide that Raj talked about, a few seconds ago. So here, how did you deploy
applications before today? Right? As you can see there
are multiple steps involved. The step one, you provision control plane, you provision compute, and then you install more add-ons, right? And you monitor your cluster
for the resource usage and then you manually optimize and update. And starting today, with the EKS Auto Mode deploying applications
becomes much simpler and all of those steps
are drastically reduced. So first, you still create a cluster, you provision a control plane and as you can see here EKS Auto Mode, and when you do that, you get a managed control
plane alongside of it. The controllers that provide
these managed capabilities which are compute, network, and storage, you get automatically out of the box. As you can see here, all of these controllers now run on an Amazon EKS account in Amazon EKS managed VPCs, you do not have to worry about, you know, provisioning the compute and running these controllers. We automatically take
care of the lifecycle of these controllers as and when update your
control plane as well. So the next, now the cluster is ready for you to deploy applications onto. So let's go ahead and
launch some applications. As you can see here, basically EKS Auto Mode
automatically launch the nodes and also you will see that
node basically comes up with all of the node agents, or the Kubernetes agents
that are really required for these application pods to function. One important distinction. So we do call it as easy to
manage instances here, right? So this is a special feature
that we are actually announcing with the launch of the Auto Mode itself, and it is available
internally for the consumption of services like Amazon EKS. And, you will also see, that these are still EC2 instances which run inside of the customer account. So when you create a cluster, you provide us special AIM policies and the permissions to
manage the lifecycle of these in instances that are running in your account. So let's double-click, and see how does it look, what do we mean by this
Amazon EC2 managed instances. So Amazon EKS with Auto
Mode still gonna continue to make available of these
specialized armies, right? And with Auto Mode, we do
actually release new Auto Mode managed armies and Auto Mode supports
bottle rocket OS by default. And, the armies that you see here, are a variant of the
upstream bottle rocket army that is available. And on the right-hand-side, the EC2 instance which is
now an Amazon EC2 instance, you will have to understand the components that are
inside of it, right? With the launch of the
Amazon EKS Auto Mode, we are kind of shifting our
operational model a bit here. So, as you can see, all of these node agents and the Kubernetes agents such as whether it is core DNS, or Q proxy, or a CNI, along with the pod identity, and the node monitoring
and the CSI node agents all are gonna run as the
system de -processes. When you create a cluster, when you run cube cut you will get pods, or a nodes, you will not see anything
within inside of your cluster, it's just an empty cluster. So moving on, another way to understand EKS Auto Mode is understanding the shared
responsibility model, or looking at it from a
shared responsibility model. So this is what the shared
responsibility model looked like previously. Here as you can see,
AWS remains responsible for all of the global infrastructure along with the foundation services and EKS was responsible for
the Kubernetes control plane, the API server, and the HCD instances, and customers remained responsible
for their applications, the availability of their applications, the security monitoring and also the VPC infrastructure
and cluster configurations. And, along with that,
you remain responsible for managing the lifecycle
of these instances along with all of the
cluster capabilities. And now, with EKS Auto
Mode, as you can see, Amazon EKS has shifted its
responsibility drastically, it shifts responsibility
beyond EKS control plane to also provide the complete management of these cluster EC2 instances and also the cluster capabilities. You, as customers, remain responsible for your application containers, the availability of those and monitoring, hence, allowing you to focus on your innovation rather
than worrying about the cluster infrastructure. With that, you still
will have the flexibility to bring in your own VPC infrastructures or the cluster configurations
such as those RBAs that you configure to provide
the multi-tenancy requirements and any of the add-ons from the CNC of like, we have like,
you know, so many add-ons that are available tools. So if you're using any of those, you will still be able to
run those EKS Auto Mode. With this, we take on more
of the undifferentiated heavy-lifting, including patching, monitoring, health and repair of the underlying EC2 instances. So let's get like, you know, dive deep into the
cluster capabilities here, just classifying the cluster capabilities. The first one, compute. As I said, EKS Auto Mode is built on the principles of the Karpenter. So all of the benefits that you get within open-source Karpenter, you will be able to get those with EKS Auto Mode, as well. We run a patch version of
that Karpenter controller, whenever you provision a cluster, a Karpenter controller is
already installed, right? So the benefits such
as compute autoscaling and also the continuous right-sizing, you get it automatically. Bottle rocket OS is what is supported and bottle rocket OS, for
those of you do not know, it's a container optimized OS, which is secured by default
with read-only file system. And one important thing to note here, is the third one, which is health,
monitoring, and auto repair. So, I actually highlighted
that node repair agent that is running on the
Amazon EC2 instance, the managed EC2 instance now, right? So it is actually looking
for the health status and sending the signals
back to the Auto Mode and Auto Mode node when
the node is unhealthy and it's gonna replace that
node with the healthy node. Moving on to the storage, when you create a cluster
with Auto Mode enabled, you get block store controller that's already installed
by default, as well. And the final one, the networking. I think networking is like,
you know, a big challenge for most of you here in the audience and with the launch of EKS Auto Mode, we are gonna simplify
a lot of those things. All of these controllers, come with the best practices included in the opinionated default. The first one pod networking
which is gonna be completely managed, which is VPC CNI, by default. So we are making a lot of change. So with Auto Mode for those of you know, today VPC CNI supports a lot
of configuration options, which is kind of a challenging, right? Customers come to us and
say what do I configure? I do not understand. So, by default we are gonna configure VPC CNI in a prefix delegation mode and if we do not see a contagious block of IPs it's gonna fall back
to the secondary IP mode. And along with the part networking, network policies are gonna be supported out of the box, as well. You will get fully-managed
in cluster service, load balancing the Kubernetes
service load balancing, and also if you want to
expose these applications outside of the cluster,
you'll be able to do so. And the last one, which
is the cluster DNS, there is a little bit of distinctions that I would like you to know. With the launch of the EKS Auto Mode, the core DNS now runs on every node. So by automatically providing
you the auto-scaling capabilities of this
core ENS out of the box. So, if you are wondering
why I should use Auto Mode or why should I create a
cluster with Auto Mode enabled, just to summarize the benefits. First, easier and faster to get started, and it provides the fully-managed cluster capabilities, as well, and secure by default by providing OS patching out of the box and
it is automatically upgraded. So, what do we mean by that here? And I'm gonna talk about in detail towards the end of this session that, whenever you update a control plane, all of the Kubernetes data plane nodes, along with the core cluster capabilities are gonna be upgraded
automatically, as well. If your workload run on Kubernetes, that should run on Auto Mode. And most importantly, we are not gonna be abstracting any of the EC2 instance
capabilities away from you. You will still have access to nearly all of the EC2 instance types
that you are used to today. If you are using a different categories you will be able to do so along with the GPUs and
the instance capabilities, and they will also have access
to the silicone innovations that is happening here at AWS, whether it is a Nitro or AWS Graviton which provides the price performance along with energy efficiencies, as well. You will be able to continue to purchase the EC2 instance types however you purchase today, whether it is on demand instances or if you use savings plan, you will be able to use those with Auto Mode as well. And, if you are cost like, you know, very cost sensitive and you
allow the cost efficiencies that SPOT provides,
you'll be able to do that with Auto Mode as well. So if you're wondering,
how do I get started? With the launch of the Auto Mode, we did a little bit facelift to the console AWS EKS
cluster creation, as well. Now, you get a quick
configuration options, with, you can now launch EKS
clusters with a single click. Auto Mode is available for 129 and above, and also an easy toggle options when you go to the console you'll be able to say whether you want to use Auto Mode or not. It comes with all of the
built in best practices. So what do we really mean
by built-in best practices? When you create a
cluster with mode enabled by default, we actually install or deploy two built-in node pools called as general purpose and system. It's again the Karpenter APIs, it supports all of the constructs that Raj talked about as well. And if you are using the
existing cluster create, whether it's an API, or whether it is a console,
you will be able to do that mode as well. Or, if you're wondering do
I have Terraform support? Yes, with the launch, you
will be able to create or use Terraform with Auto Mode, as well, or if you allow eksctl just to get started you'll be able to do so as well. And one of the important distinctions with Auto Mode is you will be able to, you know, enable Auto Mode in
an existing cluster as well. Like, you can bring in
your existing cluster and enable Auto Mode as you can see is just an easy toggle option and start to offload that
operational responsibility to EKS. So let's get into the
details of compute portions of the management aspect. So what you see here is out of the box we too provide built-in node pools. First one, is general purpose. So what's the use case of general purpose and why did we really do this? We wanted to provide you
the simplified getting started experience. Along with that, we wanted
you to provide support for launching any of the
general purpose workloads and it comes with a mix
of on-demand instance type and support for Graviton, as well as x86. So this is how it's gonna look like. As you can see here, we have the consolidation
turned on by default and the capacity types is on demand and also it comes with a mix
of CMR instance categories and later instance generation than four, the default node expiry
is set to 336 hours which is 14 days. Along with that, the
support for AMD64, as well. So the next one is a system NodePool and why system NodePool? General purpose workloads are great but we do also understand there
are a lot of other add-ons that you would want to run that you your applications depend on. So system NodePool comes
with the critical add-ons, no schedule-only, and you'll be able to leverage and use all of the other
AWS existing add-ons family to run on EKS Auto Mode by leveraging the system NodePool. It supports both AMD and ARM. So as you can see,
there is a special taint that is added on to the system node pool. Well, these best practices are great opinion defaults are actually encouraging, but how about the flexibility? If you're already running
self-managed Karpenter, or if you have a varied use cases where you're thinking about
I need the flexibility and for that you will be able to define your own user-defined
node pools, as well. So some typical use cases to define these user-defined node pools. Again, accelerated instances,
whether it is a GPU or a neuro family if you want to use, you'll be able to define those using the user-defined node pools and if you're a spot lover you
can create your own node pool to use the spot instances, as well. And you want to isolate
compute for different purposes and teams operation and also tenant isolation due
to noisy neighbor, as well. These are some of the classic
use case when you want to create your user defined
node pools, as well. One of the important distinction here, the general purpose node pool
and the system node pools are non-editable. Even if you go ahead and edit those, we are immediately gonna reconcile it back to the defaults that we provide. As an example, here, I am creating a separate node pool for my ai-ml team. As you can see, you can
provide the value inf2 and EKS Auto Mode is intelligent enough when you say a family of inf2, it's gonna actually provision the nodes with all of the capabilities included. What do I really mean by that is? The drivers, the Kubernetes
plugins are gonna come embedded. Along with that, you will
still have access to all of the disruption controls, you can still configure those budgets, reasons, the expires, the
limits, and the weight that Rajdeep talked about. EKSNodeClass. Rajdeep introduced you to EC2NodeClass and with the launch of the Auto Mode we are introducing a new kind class called as EKSNodeClass. What is this node class, right? So in the node class
basically, you kind of provide, the security groups, as well as the subnets out of the box. Just like you get the node pools, you also get one default node class which actually defaults
to the cluster subnets and the node security group
that you have provided when you created a cluster. And this is referenced by
both general purpose node pool as well as the system node pool
through the class reference. One important distinction here is EKSNodeClass becomes very simple. There is no AMI selectors because we are gonna be managing the lifecycle of these EC2
instances for you, completely, and we are gonna be owning those you are no longer required
to specify any of the AMIs. Enhance security, with again, the bottle rocket OS supports. If you want to bring in
your own security group and the subnets, you'll be able to do so, by creating a user-defined EKSNodeClass. It includes the network
configurations such as the source NAT setting and
also the network policies. You can also specify the formal storage that's gonna be used
by these EC2 instances. So this is how you define
the user-defined node class. Here, I'm defining a
user-defined node class called a team-ai-ml, which is gonna be used by the node pool that I created previously. Again, the strategies for
defining multiple node pools still apply to EKS auto node, as well. If you want to get started quickly and looking for that simplified
getting-started experience, you can use the general purpose node pool, or the system node pool, you can use multiple node pools as well, along with those general
purpose node pool. The general purpose in
the system node pool come with a default weight of zero. And if you want to
prioritize your workloads to be handled by your own node pool, you can configure the weights accordingly. So this is great. One of the important, I think, benefits of using Auto Mode is the
simplified day two operations and also reduced
operational overhead, right? So let's just understand how does EKS Auto Mode
handle the automatic updates of the core capabilities, as
well as, the data plane nodes? It's important to understand the shared responsibility
model here, right? I think since yesterday I
have got so many questions. So does it mean Auto Mode is automatically upgrade my control plane? That's, kind of, looks scary to me. It's not. You still, kind of, are responsible for updating your control plane and all of the best practices before you update your
control plane still applies. We highly encourage you to do the testing in
your lower environments, run our upgrade insights
checks to make sure that your applications
are are still gonna work with the latest version of the Kubernetes. So when we release a new
version of the Kubernetes, we also publish the recommended
optimized bottle rocket AMI for each of the version. And when that latest AMI is
actually, basically released, that's when the action is gonna happen. So before we see how
the node update works, let's take a look at the
other distinction factor, which is automatic updates
of the cluster capabilities with EKS Auto Mode. Here, right? As you can see, Karpenter v1.0 is running and also the EBS storage
controller, that is 1.34. And Amazon EKS checks
the controller version and it determines if any of this controller requires an update. Here, the other two controllers did not require any update but however, the network controller, we released a new version of it. Amazon EKS Auto Mode goes ahead and updates only the required controller. Not all the controller
updates are always necessary and when it updates these controllers it is important to note that these controller
updates are not blocking. What do we really mean by that? Just like today, when we are updating, like, we do manage the
updates of the control plane, the API server and the HCD, your application still continues to run. And similarly, while we are
updating these controllers, your application should
continue to run, as well. So the next one, how does
the data plane updates work? It is completely zero touch. You do not have to do anything. Amazon EKS Mode respect
the disruption budget. It sees that the control
plane is now updated and it is updated to 1.31. So it goes ahead. It replaces the old worker
nodes with the latest AMI. Here, you see the old one was replaced with the 1.31 AMI, as well. And it does that, so, by respecting all of
the disruption budgets, whether it is the node
pool disruption budgets, or whether it is your
manifest PO disruption budgets that you have configured, it's done in a rolling deployment fashion. And one thing to note, by default, the general purpose node pool
comes with a 14-days expiry. However, you can configure
your user-defined node pools expiry up to 21 days. So it force updates on the 21 day if not already updated, as well. So the final thing, how does security updates are
hand handled with Auto Mode? Similar concept here, Karpenter drift detection comes into play. Amazon EKS publishes the latest AMI, which includes the waste patches. That might also include
patching of these agents that are running on the node too. IT district, it again respects
the disruption budget. It goes ahead and replaces these worker nodes in a rolling
deployment fashion. As you saw, the old one were replaced with the latest AMI version, as well, against force update of 21 days
still applies here, as well. So, if you have not
started using Auto Mode or if you haven't created
a cluster with Auto Mode, I highly encourage you to
get started using Auto Mode. Whether, you are new to Kubernetes or EKS, or you would want to accelerate
your modernization journey, EKS Auto Mode is for you, or you want to offload that
operational overhead to EKS. Again, do not wait, start to use EKS Auto Mode in production. Auto mode is generally available in all of the commercial region. We will be soon launching
the support for China, as well as Claude 2. With that, I'm gonna welcome
back Raj back onto the stage for closing thoughts. - All right, so seems like EKS Auto Mode helps all of you to get started faster, but as a someone who is
enthusiastic about Karpenter, what's happening with
open-source Karpenter, Sheetal? - We love Karpenter. We develop that with love here at AWS. We are committed to develop
Karpenter in the open. It's not going to go anywhere. As you heard, B repeatedly say, Amazon EKS Auto Mode is built on the principles of Karpenter. So any feature that is made
available in the Karpenter, it's gonna be made available
in Auto Mode, as well. - That's great to hear. So as you could see, you have a lot of
flexibility at the same time, if you are someone who is like, okay, how do I get started with EKS? Faster and simpler. EKS
Auto Mode is the answer. You can create the cluster, you get bunch of
capabilities out of the box. We manage, and upgrade the add-ons, like Karpenter storage and Ingress and a lot of other features
that Sheetal talked about. As always, either you use
EKS, EKS Auto, or Karpenter, it's running fully upstream
Kubernetes conformant version. With that, I know this
is a lot of information and this is just the beginning. We have lot more information available throughout different sessions. Sheetal, here, is running
two builder sessions, one tomorrow, one day after. You can also learn a
bunch about EKS Auto Mode, you can read the launch blog. She just released a launch
blog right before this talk. As well as, we have guidance on if you're using cluster autoscaler today, how to migrate to Karpenter v1. With that, we are gonna be here
for a little bit of question and answer, before we start the Q and A, you wanna move one more forward, Sheetal. Don't forget to complete
the session survey, if you like this session or if you have not, give us some feedback, we take them seriously. - Thank you so much for
attending this session. - Thank you.
(audience clapping)

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1s) - All right, welcome everyone.

[00:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3s) I know this is Tuesday afternoon,

[00:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=5s) you have a lot of choices on the sessions.

[00:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=7s) First of all, thanks for
coming to this session.

[00:10](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=10s) Little bit of Easter egg,

[00:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=11s) for those of you who have
been watching the catalog,

[00:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=14s) you'd noticed the title
of our session changed.

[00:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=17s) So you signed up for Karpenter,

[00:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=19s) you are getting Karpenter, and then some.

[00:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=22s) My name is Raj.

[00:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=23s) I'm a Principal Solutions Architect

[00:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=25s) for Containers and Serverless at AWS.

[00:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=28s) I've been at AWS for six years

[00:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=30s) and I have helped many
customers migrate to

[00:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=32s) Kubernetes and Serverless.

[00:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=35s) Today, I'm gonna co-present
with Sheetal Joshi.

[00:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=38s) - Hello, I'm Sheetal Joshi.

[00:39](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=39s) I'm a principal SA for
Containers here at AWS,

[00:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=42s) predominantly working with the EKS

[00:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=44s) and the Kubernetes customers

[00:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=45s) and I'm very excited to
co-present with Raj here, today.

[00:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=48s) - Excellent.
- There you go.

[00:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=50s) - Let's get started.

[00:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=53s) Okay,

[00:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=55s) today we're going to talk about

[00:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=56s) how do customers adopt Amazon EKS?

[01:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=60s) And then, of course this is a Karpenter

[01:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=62s) and EKS Auto Mode session.

[01:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=63s) So we'll talk about

[01:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=64s) how do customers scale their applications?

[01:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=68s) And then, we're gonna
talk about some challenges

[01:10](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=70s) and how to solve them
with Karpenter and beyond.

[01:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=74s) And at the end, we are also
going to share some resources

[01:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=78s) for you to learn more.

[01:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=80s) So if we go back six years,

[01:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=82s) we released Amazon EKS.

[01:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=86s) Kubernetes is awesome.

[01:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=87s) I've been working in
Kubernetes for a long time,

[01:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=89s) but our customers told us that

[01:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=91s) self-managing the control
plan is difficult.

[01:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=95s) So that's why Amazon EKS was born.

[01:39](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=99s) So, EKS is a stable and
secure way to run Kubernetes

[01:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=104s) and we run fully upstream

[01:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=106s) and certified conformant Kubernetes.

[01:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=110s) All right, so at this point
you are like EKS is great.

[01:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=113s) I want to get started with EKS.

[01:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=115s) So how do you do that today?

[01:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=117s) First, you create your cluster

[02:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=120s) and what that does is

[02:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=122s) it creates a control plan in AWS account

[02:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=125s) where we make it scalable,

[02:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=128s) highly available, and secure.

[02:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=132s) Next, you want to deploy your workload

[02:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=136s) but not so fast.

[02:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=138s) Before you deploy your workload,

[02:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=140s) you also need to install some
add-on and controllers, right?

[02:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=145s) So generally, you create
a managed node group,

[02:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=148s) two or more EC2 instances,

[02:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=151s) and then you install add-ons

[02:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=154s) like ingress controller
or storage controller

[02:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=158s) and some of the other ones.

[02:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=161s) Okay, at this point you installed

[02:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=163s) all those add-ons and controllers

[02:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=165s) and then you deploy your application.

[02:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=168s) So, you create a managed node
group and then you deploy

[02:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=172s) and the pod gets deployed there.

[02:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=176s) But of course, this is a scaling session

[02:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=178s) so we have to talk about autoscaling.

[03:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=180s) So, we're like, you know what?

[03:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=182s) This app we made is going great.

[03:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=185s) At this point you install
something like Cluster Autoscaler

[03:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=191s) and then your pods scale
across multiple instances.

[03:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=197s) Cluster Autoscaler is great,

[03:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=199s) however, Cluster Autoscaler
has some challenges.

[03:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=203s) With Cluster Autoscaler,

[03:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=204s) you need to create node groups,

[03:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=207s) either managed or self-managed.

[03:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=210s) And in those node groups,

[03:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=211s) you have to specify what instance families

[03:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=215s) it should be using as
well as their priority.

[03:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=220s) Also, with Cluster Autoscaler,

[03:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=221s) you need to create Autoscaling Group.

[03:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=225s) Now, Autoscaling group comes,

[03:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=227s) autoscaling group is great,

[03:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=228s) but it comes with some challenges.

[03:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=230s) So for each node group you have

[03:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=232s) to have a separate autoscaling group.

[03:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=234s) If you want your workload

[03:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=235s) to spread it across
multiple availability zones,

[03:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=238s) you need to create multiple
autoscaling groups, et cetera.

[04:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=242s) And finally, the AMI selection
and refresh is cumbersome.

[04:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=248s) For those of you who are running

[04:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=249s) Cluster Autoscaler in production,

[04:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=252s) you know you have to
manage the launch template,

[04:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=254s) anytime an AMI is changed,
you have to go change it,

[04:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=257s) run recycle commands, all that stuff.

[04:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=261s) For that reason we created Karpenter.

[04:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=266s) So how does Karpenter work?

[04:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=268s) So first, the pod scales using
horizontal Pod Autoscaler.

[04:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=273s) Then the pods go pending

[04:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=275s) and with Cluster Autoscaler
it has the Cluster Autoscaler

[04:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=277s) Autoscaling group,

[04:39](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=279s) but Karpenter bypasses all of that

[04:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=283s) and it interacts directly with EC2 Fleet.

[04:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=287s) Because it is bypassing all those hops.

[04:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=291s) Karpenter is faster.

[04:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=295s) Also, when we created Karpenter

[04:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=298s) we wanted it to be Kubernetes native

[05:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=300s) and as Kubernetes
enthusiasts, we love YAML.

[05:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=304s) So you can control the behavior

[05:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=306s) of Karpenter using two YAML files,

[05:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=309s) NodePool and EC2NodeClass.

[05:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=314s) Okay, so let's go back to our process.

[05:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=317s) So instead of Cluster Autoscaler,

[05:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=319s) you install the Karpenter, add-on.

[05:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=323s) Okay, and then your application scale.

[05:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=325s) And now, you do not need to
have any managed node group.

[05:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=330s) Your instances are coming up faster,

[05:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=333s) things are good.

[05:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=336s) Even though scaling is the
bread-and-butter of Karpenter.

[05:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=340s) Karpenter does way more than scaling.

[05:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=345s) Karpenter does cost
optimization out of the box.

[05:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=350s) Karpenter supports diverse workloads

[05:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=352s) including machine learning
and generative AI.

[05:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=356s) And Karpenter, also helps
with upgrade and patching.

[06:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=361s) For that reason, Karpenter is the total

[06:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=365s) data plan implementation.

[06:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=369s) Karpenter is made with love at AWS,

[06:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=371s) but we donated it to the
open-source community

[06:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=374s) and it is one of the CNC projects now

[06:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=376s) under SIG autoscaling.

[06:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=378s) And we are very proud to
see how Karpenter is growing

[06:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=381s) and how customers like you

[06:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=383s) are contributing to the Karpenter.

[06:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=387s) Okay, so let's start this point.

[06:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=388s) We're like, okay, Raj,

[06:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=390s) Karpenter is great,

[06:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=391s) how do we get started with this?

[06:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=394s) So, we see the journey in
our customers like this.

[06:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=397s) First, you evaluate the
features of Karpenter,

[06:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=400s) then you implement it,

[06:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=402s) then you do Day 2 operations,

[06:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=404s) and maybe finally,
there is some evolution.

[06:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=408s) And throughout this talk,

[06:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=410s) we are going to follow the same process.

[06:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=414s) All right, so let's start
with the evaluation phase.

[06:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=419s) For your containers to run,
it requires different things,

[07:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=424s) CPU, memory, storage, et cetera.

[07:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=428s) And, how does it map to
different EC2 instances?

[07:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=433s) There are many different EC2
instances that we provide you.

[07:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=437s) The larger the size,
the larger CPU you get,

[07:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=441s) and then the instance family
determines CPU to memory ratio.

[07:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=447s) And, we give you a lot of flexibility.

[07:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=450s) We have over 800 different
instance types to choose from,

[07:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=455s) such as GPUs like P4d,

[07:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=457s) or the latest generation
custom silicon instances like

[07:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=461s) INF2 or TRN.

[07:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=465s) So first question is,

[07:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=467s) how do I control which EC2s
does Karpenter spin up?

[07:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=473s) Well, remember we talked
about the node pool YAML?

[07:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=477s) So this is a sample node pool YAML.

[08:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=480s) Using this node pool YAML,

[08:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=482s) you can control how Karpenter behaves.

[08:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=485s) For example, on the top we are saying,

[08:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=489s) instance family should
be within c5, m5 and r5.

[08:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=496s) And I'm showing off a little bit here,

[08:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=498s) Not only you can use the operator in,

[08:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=500s) but you can also use not in.

[08:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=504s) So you are like okay,
use those instance types

[08:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=506s) but do not spin up anything
which is nano, micro,

[08:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=509s) small or medium whatever,
depending on your workload.

[08:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=513s) And, we realize it's not easy

[08:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=517s) to choose from 800
different instance types.

[08:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=521s) So all these fields, if you're
thinking, Raj, this is great

[08:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=524s) but this is a lot.

[08:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=525s) So you can keep this all empty

[08:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=527s) and AWS will automatically choose

[08:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=530s) the appropriate instance type for you

[08:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=532s) based on your deployment
pods resource requests.

[08:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=538s) And, we always have those
sneaky SRE teams who are like,

[09:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=542s) or the sneaky app developers like myself,

[09:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=544s) who I was before.

[09:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=545s) It's like I need lot
of CPU, lot of memory,

[09:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=548s) and for that reason you can also limit

[09:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=551s) how many EC2 instances this
node pool can provision.

[09:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=555s) So in the bottom,

[09:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=556s) you could see we have the
limit of CPU of a hundred.

[09:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=560s) So this node pool will keep
on provisioning EC2 instances

[09:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=564s) 'til the aggregate amount
of CPU, which is a hundred.

[09:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=569s) I'm just showing CPU but
this also works with memory.

[09:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=575s) You can also control things
like availability zone.

[09:39](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=579s) For example,

[09:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=580s) you can say, hey, split
it up within US 2a, 2b,

[09:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=584s) or any specific AZ.

[09:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=588s) Unlike autoscaling group, you do not need

[09:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=590s) to create different node pools for this.

[09:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=594s) Also, you can control
the architecture type,

[09:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=596s) you can use x86 or Arm, like Graviton,

[10:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=601s) based on your workload.

[10:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=603s) And finally, a lot of you
want to mix in spot instances.

[10:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=608s) In the bottom,

[10:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=609s) I'm showing that capacity-type
spot comma on demand.

[10:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=614s) If you specify both spot and on demand,

[10:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=618s) Karpenter will always prioritize spot,

[10:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=622s) but it is intelligent enough to know

[10:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=624s) when the spot capacity is low,

[10:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=626s) it will automatically fall back

[10:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=628s) and create on demand instances.

[10:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=631s) And we all know,

[10:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=632s) for those of us who have given

[10:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=633s) Solutions Architect Associate
Certification exams,

[10:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=635s) you know the question always comes,

[10:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=637s) what is one thing you need
to keep in mind with spot?

[10:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=640s) It can go away with
two-minutes warnings, right?

[10:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=644s) Karpenter handles that two-minute warnings

[10:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=648s) and you do not have to
do anything yourself.

[10:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=650s) It will spin up a backup
spot instances for you

[10:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=655s) and cordon and drain
the terminating instance

[10:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=658s) and move the pods

[11:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=660s) in a rolling deployment fashion.

[11:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=663s) You do not need to install and manage

[11:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=667s) node termination handler.

[11:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=669s) It has built-in spot interruption handler.

[11:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=674s) Okay, moving forward,

[11:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=677s) for those of you who have

[11:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=679s) used real-world production
workload in Kubernetes,

[11:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=683s) you also need to have
scheduling constraints.

[11:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=687s) With Karpenter, you can use
different scheduling constraints

[11:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=691s) like node selectors,

[11:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=693s) node affinity,

[11:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=695s) taints and tolerations,

[11:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=696s) and topology spread.

[11:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=700s) So this is of course, used
a lot in your project.

[11:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=703s) So let's take a deeper look at this.

[11:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=707s) So let's say, on the left,
I'm showing a node pool

[11:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=710s) and this node pool spins up a
spot instance of capacity-type

[11:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=715s) and also architecture-type AMD64,

[12:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=720s) whichever instance this
node pool provisions,

[12:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=723s) Karpenter will attach
all these key value pairs

[12:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=729s) as labels to the nodes.

[12:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=731s) So for example, Karpenter
will put capacity-type,

[12:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=735s) colon spot, Kubernetes.io
slash architecture colon,

[12:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=740s) AMD64, et cetera.

[12:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=742s) What does that mean?

[12:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=744s) So on the right,

[12:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=745s) I'm showing a sample
pod specification file,

[12:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=750s) you can use those key value pairs

[12:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=753s) to schedule the pod in specific instances.

[12:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=758s) So in this case, if you deploy this,

[12:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=760s) if the EC2 was already running into,

[12:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=762s) the pods will get scheduled there.

[12:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=765s) If there was no EC2 running,

[12:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=766s) Karpenter will spin up a spot instance

[12:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=770s) to satisfy the scheduling requirements.

[12:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=775s) Karpenter will also attach
well-known labels to your nodes.

[12:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=779s) You do not need to do anything special.

[13:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=781s) For example, the zone, instance type,

[13:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=785s) operating system, et cetera.

[13:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=787s) So you can use all these fields

[13:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=789s) in your pod specification
file for scheduling.

[13:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=794s) Okay, you might ask those,
that's a good start,

[13:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=798s) how about user-defined labels?

[13:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=802s) Karpenter supports that, as well.

[13:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=804s) So in this example on the left,

[13:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=806s) I'm showing how to use
user-defined annotation,

[13:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=810s) taints and labels in your node pool.

[13:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=813s) And on the right, you
can reuse those labels,

[13:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=818s) taints and annotations
to schedule your pod.

[13:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=823s) This is a very, very popular
way to schedule parts

[13:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=826s) for different applications, right?

[13:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=829s) You can have different node
pools with different labels

[13:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=834s) and the different teams can
use those different labels

[13:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=837s) to schedule their workloads.

[14:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=840s) Which brings us to a good question.

[14:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=844s) How many different node
pools should you define?

[14:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=848s) Well, you have different options.

[14:10](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=850s) The easiest one is a single node pool.

[14:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=852s) So you put everything in
a single node pool YAML

[14:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=855s) and then each team, whatever they need,

[14:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=858s) they use those fields to specify

[14:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=863s) and then schedule those pods.

[14:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=866s) The most popular one that
I see with my customers

[14:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=869s) is multiple node pools,

[14:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=871s) where each team has their
own separate node pool.

[14:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=876s) One of the big reasons is,

[14:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=878s) maybe one team is running
expensive GPU EC2s,

[14:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=882s) and remember the limit-fields
for that node pool,

[14:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=886s) you can limit them to a certain
amount of CPU or memory.

[14:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=891s) Maybe, there is a noisy neighbor,

[14:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=893s) they need more CPU and memory than others.

[14:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=896s) They need different types of instances.

[14:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=899s) So you can separate the teams
using separate node pools.

[15:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=905s) Another advanced strategy
is weighted node pools

[15:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=909s) where you can prioritize
one node pool before others.

[15:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=916s) When will you use it?

[15:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=918s) If you want to prioritize
reserved instances

[15:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=920s) or savings plan ahead
of other instance types.

[15:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=924s) So pretty sure this part
is a little confusing.

[15:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=927s) So let me give you an example.

[15:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=930s) In this example, I'm
showing two node pools.

[15:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=935s) The top one has the
weight 60 on the bottom

[15:39](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=939s) and see the instance types are c and r.

[15:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=943s) I'm assuming you have
reserved instance contract

[15:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=946s) for those two instance types.

[15:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=949s) So anytime a pod goes pending,

[15:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=952s) it will use the first node pool,

[15:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=955s) and it'll keep on spinning up instances

[15:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=959s) 'til it reaches the limit, right?

[16:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=961s) Let's say you have
reserve instance contract

[16:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=964s) for certain number of EC2s.

[16:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=966s) So it'll keep on spinning up EC2 instances

[16:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=969s) 'til the CPU or memory reaches thousand

[16:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=972s) and then the other node
pool will take over.

[16:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=975s) Oops, let me go back.

[16:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=976s) Then the other node pool will take over

[16:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=978s) and then it'll keep on provisioning

[16:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=981s) different instance types.

[16:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=984s) All right, remember I talked about

[16:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=987s) Karpenter can optimize
cost out of the box.

[16:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=991s) So at this point your cluster
is running with Karpenter.

[16:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=995s) Proper instance types are chosen,

[16:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=998s) however,

[16:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1000s) over time your cluster may
end up looking like this.

[16:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1005s) For worker nodes,

[16:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1006s) the fast worker node

[16:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1008s) nicely utilized and bin packed,

[16:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1011s) the last three, not so much.

[16:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1014s) With Karpenter,

[16:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1016s) you can specify the consolidation policy

[17:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1020s) when empty or underutilized

[17:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1023s) and Karpenter will automatically
bin pack your pods,

[17:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1028s) terminate the unnecessary instances

[17:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1031s) and saves you a lot of money.

[17:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1035s) However, one feedback we
got from our customers is

[17:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1039s) this is great, but Karpenter
runs this simulation

[17:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1043s) and this consolidation
every 10 seconds or so.

[17:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1047s) So this could be lot of nodes
coming up and coming down.

[17:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1051s) So for that reason we
introduced another knob

[17:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1055s) for you to control this behavior.

[17:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1058s) This is included in Karpenter version one.

[17:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1062s) The field is consolidated after.

[17:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1065s) So see on the bottom,

[17:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1066s) I'm showing consolidated after one hour.

[17:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1069s) So even if you're EC2
instances looking like this,

[17:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1073s) it will wait one more hour
before it consolidates

[17:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1078s) because you know your workloads the best.

[18:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1081s) If you know some new
workloads gonna come in

[18:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1083s) after five minutes.

[18:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1084s) So you are telling Karpenter,

[18:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1086s) hey don't touch these EC2 instances,

[18:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1089s) don't consolidate yet.

[18:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1091s) Let's wait for a little bit of time.

[18:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1094s) So let's say one hour passes,

[18:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1096s) no new pod gets added or removed,

[18:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1099s) only after that Karpenter will consolidate

[18:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1103s) and terminate the unused instances.

[18:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1108s) Not only Karpenter can consolidate

[18:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1110s) to the existing instances,

[18:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1113s) Karpenter can also replace
and right-size instances.

[18:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1118s) So in this case, the
second and third instance,

[18:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1120s) m5.xlarge,

[18:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1122s) even if you bin pack those
two pods in one m5.xlarge,

[18:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1127s) there is still an inefficiency.

[18:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1131s) Karpenter is smart enough,

[18:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1132s) in this case it will
terminate both these m5.xlarge

[18:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1138s) and spin up a m5.large,
so half the instance size

[19:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1143s) and save you a lot of money.

[19:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1145s) And all this happens out of the box.

[19:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1149s) Now, one question I get
is, Raj, this is great

[19:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1153s) but you know a lot of critical workloads

[19:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1155s) running in the middle of the day,

[19:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1157s) and I don't want Karpenter

[19:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1158s) to disrupt all these EC2 instances.

[19:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1162s) For that reason, we
released disruption budget

[19:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1166s) with Karpenter version one.

[19:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1169s) Using this disruption budget,

[19:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1172s) you can specifically control

[19:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1174s) the behavior of this disruption.

[19:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1177s) So let's go through this.

[19:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1180s) In this YAML,

[19:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1181s) so this is part of node pool YAML,

[19:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1183s) the first block says, nodes zero.

[19:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1187s) So that means zero nodes can be disrupted

[19:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1191s) during the schedule Monday
to Friday from nine o'clock

[19:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1196s) for duration eight hours.

[19:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1198s) So nine o'clock to five o'clock,

[20:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1200s) for the reason, drifted and underutilized.

[20:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1204s) So even if Karpenter can
consolidate those nodes,

[20:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1209s) it will not touch them Monday
to Friday working hours.

[20:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1214s) What if they're empty?

[20:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1216s) You are like, you know, empty nodes,

[20:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1217s) I don't care, nothing can be disrupted.

[20:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1220s) So a hundred percent of those
nodes could be disrupted.

[20:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1225s) Doesn't matter whether it's
working hours or weekends.

[20:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1229s) Now, the last one says,

[20:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1232s) outside of those working hours,

[20:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1234s) so 10% of the nodes could be disrupted

[20:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1238s) for the reasons, drifted and unutilized.

[20:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1243s) So remember, this is all cumulative.

[20:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1245s) So if I put all this together,

[20:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1247s) that means 0% of the nodes

[20:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1249s) could be disrupted during working hours.

[20:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1251s) A hundred percent of the
nodes could be disrupted

[20:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1254s) for when they're empty

[20:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1256s) even during working hours

[20:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1258s) and for the nodes outside
of the working hours

[21:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1261s) for the reasons, drifted
and underutilized,

[21:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1263s) only 10% of the nodes could
be disrupted at a time.

[21:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1268s) So I talked about drift.

[21:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1271s) What is drift?

[21:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1273s) So Karpenter is Kubernetes native,

[21:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1275s) and the Kubernetes core principle is,

[21:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1278s) to reconcile between the desired state

[21:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1280s) and the current state.

[21:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1282s) And, Karpenter is no different.

[21:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1286s) So let's say in this case,

[21:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1287s) in the node pool you have a
reserved instances contract,

[21:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1290s) you are using m5.large.

[21:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1292s) So all the EC2s that this
node pool spun up is m5.large.

[21:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1297s) Let's say you go and change this m5.large

[21:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1301s) to c5.large.

[21:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1304s) So in this case, the desired
configuration in the node pool

[21:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1308s) will deviate from the running instance,

[21:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1311s) which is m5.large.

[21:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1313s) So Karpenter will automatically cordon

[21:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1316s) and drain the running m5.large
spin up a c5.large instance

[22:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1322s) and move over your pods.

[22:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1326s) Okay, so at this point we
learned about NodePool.

[22:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1332s) NodePool controls the instance family,

[22:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1335s) availability zone,
budgets, all that stuff.

[22:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1338s) But how about AMI subnet security group?

[22:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1342s) That's what EC2NodeClass does.

[22:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1345s) So for example,

[22:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1346s) you can select which subnets are eligible

[22:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1349s) to launch your EC2.

[22:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1351s) You can attach certain
security groups to EC2,

[22:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1354s) in this case, the name, my security group.

[22:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1357s) You can select the AMI for EC2

[22:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1361s) and you can have other
things like user data,

[22:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1364s) attach tags, define EBS, and more.

[22:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1369s) So, AMI is the important one.

[22:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1371s) So let's take a look.

[22:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1373s) So you can use AMI selector
to select from different AMIs.

[22:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1379s) Amazon provides you EKS
optimized AMI out of the box.

[23:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1383s) So to use them, in the EC2NodeClass,

[23:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1387s) you could use something like,

[23:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1389s) alias at the bottle rocket, at the latest.

[23:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1393s) So any EC2 that this Karpenter provisions

[23:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1396s) will run with EKS optimized
AMI or bottle rocket

[23:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1400s) with the latest version.

[23:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1402s) Similarly, another example
could be Amazon Linux 2

[23:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1406s) at the latest.

[23:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1408s) The supported family values
in alias are al2, al2023,

[23:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1413s) bottle rocket, Windows
2019 and Windows 2022.

[23:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1418s) Now, you may say latest is great,

[23:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1422s) but what if I want to pin my work nodes

[23:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1425s) to a specific version,

[23:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1427s) and I want to test out the new version,

[23:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1428s) then only go to the latest version.

[23:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1431s) You can do that, as well.

[23:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1433s) So as part of the Karpenter V1,

[23:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1435s) you can pin your work nodes

[23:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1438s) to a specific AMI version, like this.

[24:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1440s) So for this case I'm saying

[24:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1443s) alias bottle rocket at the rate v1.20.5.

[24:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1449s) So all the EC2s that this
node class will provision

[24:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1453s) will be of this version of bottle rocket.

[24:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1457s) Similarly, Amazon Linux 2
with the with the version

[24:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1460s) of 2024, July 29th.

[24:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1464s) What about custom AMI?

[24:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1466s) Karpenter supports custom AMI, as well.

[24:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1468s) A lot of my customers uses custom AMI.

[24:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1471s) You can select custom AMI

[24:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1473s) using tag, name,

[24:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1476s) owner, as well as ID.

[24:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1481s) If multiple AMIs are found
satisfying these conditions,

[24:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1485s) Karpenter will use the latest one.

[24:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1488s) If no AMI is found,

[24:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1490s) no nodes will be provisioned, right?

[24:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1492s) So this part is a little scary.

[24:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1493s) You don't want to, you want to avoid this

[24:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1496s) and you can,

[24:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1497s) once you deploy EC2NodeClass,

[25:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1500s) you can check the status
fields for this AMI field

[25:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1504s) and it will show if the
conditions are selecting any AMIs.

[25:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1509s) Okay?

[25:10](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1510s) So if you have been following the theme,

[25:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1512s) AWS is customer-obsessed.

[25:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1515s) So, we went from okay
customers self-managing

[25:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1518s) the control plan.

[25:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1519s) So we created EKS,

[25:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1521s) then we were like, okay, EKS is good,

[25:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1523s) how can we make your lives better?

[25:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1525s) Okay, so we created Karpenter.

[25:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1528s) Now, what about after Karpenter?

[25:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1531s) So to talk about that,

[25:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1533s) I'm gonna invite my
co-presenter, Sheetal, on stage.

[25:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1538s) - Thank you, Raj.

[25:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1540s) That was a great deep-dive into Karpenter

[25:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1543s) and it was cool to see
how those like, you know,

[25:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1546s) in reality that consolidation

[25:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1547s) and the optimization was
working, that was really cool.

[25:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1552s) So you work with a lot
of customers, right?

[25:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1554s) Karpenter and no Karpenter.

[25:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1556s) So what are some of the challenges

[25:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1558s) that you hear from your customers

[25:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1559s) who are actually running
Karpenter or Cluster Autoscaler?

[26:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1563s) - Yeah, one challenge I hear is,

[26:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1566s) okay, Raj Karpenter is great

[26:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1568s) but there are so many fields in

[26:10](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1570s) that YAML file, how do I
select those fields, right?

[26:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1574s) Like, what do I select

[26:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1575s) so that the EC2 instances are
optimized and right-sized?

[26:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1579s) So likewise, Sheetal, you
work with a lot of customers,

[26:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1581s) what challenges do you
see in your conversations?

[26:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1584s) - Well, these applications
are not lone wolf, right?

[26:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1587s) So they actually depend on
the core cluster capabilities

[26:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1591s) such as what we call as add-ons.

[26:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1592s) Whether it is part networking
or the service discovery

[26:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1595s) or the load-balancing capabilities.

[26:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1597s) Along with that, any of
the user defined add-ons

[26:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1600s) that customers really require

[26:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1602s) to meet their business,
like you know, requirements

[26:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1605s) and most importantly,

[26:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1607s) the last one here is
upgrading the clusters

[26:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1611s) and keeping your Kubernetes cluster safe,

[26:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1614s) is the biggest, biggest
challenge for, I think,

[26:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1616s) most of you who are actually
attending this session, right?

[26:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1619s) Which actually requires
a dedicated expertise

[27:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1622s) and the continuous time investment

[27:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1624s) which kind of slows down the innovation

[27:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1627s) that customers are really looking for.

[27:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1631s) So this is great.

[27:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1632s) I think some of you

[27:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1633s) might already be thinking
like Raj talked about

[27:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1636s) all of the Karpenter details

[27:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1637s) and seems like it addresses the challenges

[27:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1639s) that we just talked about,

[27:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1641s) but what do you think are the challenges

[27:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1642s) beyond Karpenter, Raj?

[27:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1644s) - Yeah, it'll be good like

[27:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1645s) to have some best practice recommendations

[27:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1648s) to run the add-ons,

[27:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1650s) controller, and something
that's like built-in.

[27:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1653s) What about you, Sheetal?

[27:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1655s) - Yeah, I think these
management of the add-ons

[27:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1657s) and their versions

[27:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1658s) and the lifecycle of these controllers

[27:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1660s) is a big challenge as well, right?

[27:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1662s) Karpenter doesn't address
any of those needs

[27:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1664s) and it's a controller by itself.

[27:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1666s) So just managing the Karpenter

[27:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1668s) with all of the best practices

[27:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1669s) is a big challenge for our customers

[27:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1671s) and yet again, I think
you touched upon it,

[27:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1673s) but ease-of-use and out
of the box capabilities,

[27:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1676s) how do I get started quickly?

[27:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1677s) I think that's one of the major questions

[28:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1680s) that our customers always ask.

[28:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1682s) - Great. Seems like you
have answers for this

[28:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1684s) and something up your sleeve

[28:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1685s) so I'll leave you to it on the stage.

[28:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1687s) - Thank you so much, Raj.

[28:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1688s) So without further due,

[28:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1691s) let me introduce you to
Amazon EKS Auto Mode.

[28:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1694s) So what is it?

[28:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1695s) Amazon EKS Auto Mode,

[28:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1697s) I think, if you are following the news,

[28:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1699s) AWS news, blog post, it's everywhere.

[28:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1702s) So technically, Amazon EKS
mode is gonna streamline

[28:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1706s) your Kubernetes cluster
infrastructure management.

[28:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1709s) So, let's dive deep in the next 20 minutes

[28:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1711s) of what actually EKS Auto Mode is

[28:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1714s) and how does it simplify
application deployment

[28:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1717s) onto Kubernetes clusters.

[28:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1718s) So the first one, when you
use Amazon EKS Auto Mode,

[28:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1723s) it kind of brings in
that increased agility

[28:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1726s) and accelerates the innovations

[28:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1728s) by offloading cluster operations to AWS.

[28:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1730s) And, how do we do this?

[28:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1732s) With the introduction of
the Amazon EKS Auto Mode,

[28:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1734s) EKS is taking on more responsibility

[28:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1738s) under the shared responsibility model

[29:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1740s) beyond the Kubernetes control plane

[29:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1742s) that we have always managed

[29:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1744s) to the Kubernetes data plane, as well.

[29:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1747s) So the next one,

[29:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1748s) it basically improves the performance

[29:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1752s) and maintains the application availability

[29:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1754s) by dynamically scaling
the compute resources

[29:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1757s) that your applications depend on.

[29:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1759s) And along with that,
it's secure by default.

[29:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1762s) So what do we mean by secure by default?

[29:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1765s) EKS Auto Mode automatically updates

[29:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1768s) your worker notes

[29:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1770s) and also applies the
security fixes automatically.

[29:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1775s) So the last one, it
continuously optimizes the cost

[29:39](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1779s) with automatic capacity
planning and dynamic scaling.

[29:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1782s) So, how does it do it?

[29:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1785s) So as you can see here,
you create a cluster,

[29:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1788s) it's still the same API,
that doesn't change,

[29:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1790s) it's still Amazon EKS,

[29:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1792s) and when you create a cluster,

[29:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1793s) it includes all of the core capabilities

[29:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1796s) that are basically required

[29:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1797s) for production-ready clusters, right?

[29:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1799s) So you create a cluster,

[30:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1801s) you get managed control plane,

[30:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1803s) the API server and the HCD instances.

[30:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1805s) Along with that, all of these
core capabilities included

[30:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1808s) alongside.

[30:10](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1810s) And next, when you
deploy your applications,

[30:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1812s) it automatically provisions
cluster infrastructures.

[30:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1816s) So in how does it do?

[30:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1818s) Amazon EKS Auto Mode is built

[30:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1820s) on the principles of Karpenter.

[30:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1822s) So it keeps watching for the applications

[30:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1825s) and when you deploy your applications,

[30:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1827s) it launches the nodes
looking at the requirements

[30:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1830s) that are specified within
application manifest,

[30:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1832s) it's dynamically scaled resources

[30:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1835s) as the application scale changes

[30:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1837s) and it continuously optimizes for cost.

[30:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1840s) As you saw, all of the
optimization principles

[30:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1842s) and the consolidation principles

[30:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1844s) that Raj talked about, still apply here.

[30:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1847s) And the last one, it
automatically updates the notes

[30:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1850s) and the core cluster capabilities.

[30:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1854s) So let's go back to this slide

[30:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1856s) that Raj talked about, a few seconds ago.

[31:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1860s) So here, how did you deploy
applications before today?

[31:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1863s) Right? As you can see there
are multiple steps involved.

[31:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1866s) The step one, you provision control plane,

[31:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1869s) you provision compute,

[31:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1871s) and then you install more add-ons, right?

[31:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1873s) And you monitor your cluster
for the resource usage

[31:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1877s) and then you manually optimize and update.

[31:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1881s) And starting today, with the EKS Auto Mode

[31:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1884s) deploying applications
becomes much simpler

[31:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1886s) and all of those steps
are drastically reduced.

[31:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1890s) So first, you still create a cluster,

[31:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1892s) you provision a control plane

[31:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1893s) and as you can see here EKS Auto Mode,

[31:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1896s) and when you do that,

[31:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1897s) you get a managed control
plane alongside of it.

[31:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1900s) The controllers that provide
these managed capabilities

[31:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1904s) which are compute, network,

[31:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1906s) and storage,

[31:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1907s) you get automatically out of the box.

[31:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1910s) As you can see here,

[31:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1911s) all of these controllers

[31:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1912s) now run on an Amazon EKS account

[31:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1916s) in Amazon EKS managed VPCs,

[31:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1919s) you do not have to worry about,

[32:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1921s) you know, provisioning the compute

[32:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1923s) and running these controllers.

[32:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1925s) We automatically take
care of the lifecycle

[32:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1927s) of these controllers

[32:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1929s) as and when update your
control plane as well.

[32:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1932s) So the next, now the cluster is ready

[32:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1935s) for you to deploy applications onto.

[32:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1938s) So let's go ahead and
launch some applications.

[32:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1940s) As you can see here,

[32:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1942s) basically EKS Auto Mode
automatically launch the nodes

[32:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1946s) and also you will see that
node basically comes up

[32:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1949s) with all of the node agents,

[32:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1952s) or the Kubernetes agents
that are really required

[32:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1954s) for these application pods to function.

[32:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1957s) One important distinction.

[32:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1958s) So we do call it as easy to
manage instances here, right?

[32:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1962s) So this is a special feature
that we are actually announcing

[32:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1966s) with the launch of the Auto Mode itself,

[32:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1968s) and it is available
internally for the consumption

[32:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1971s) of services like Amazon EKS.

[32:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1972s) And, you will also see,

[32:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1975s) that these are still EC2 instances

[32:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1978s) which run inside of the customer account.

[33:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1981s) So when you create a cluster,

[33:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1982s) you provide us special AIM policies

[33:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1985s) and the permissions to
manage the lifecycle

[33:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1987s) of these in instances

[33:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1989s) that are running in your account.

[33:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1991s) So let's double-click,

[33:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1993s) and see how does it look,

[33:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1995s) what do we mean by this
Amazon EC2 managed instances.

[33:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=1998s) So Amazon EKS with Auto
Mode still gonna continue

[33:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2002s) to make available of these
specialized armies, right?

[33:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2007s) And with Auto Mode, we do
actually release new Auto Mode

[33:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2012s) managed armies

[33:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2013s) and Auto Mode supports
bottle rocket OS by default.

[33:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2018s) And, the armies that you see here,

[33:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2020s) are a variant of the
upstream bottle rocket army

[33:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2023s) that is available.

[33:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2024s) And on the right-hand-side,

[33:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2025s) the EC2 instance which is
now an Amazon EC2 instance,

[33:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2029s) you will have to understand

[33:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2031s) the components that are
inside of it, right?

[33:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2034s) With the launch of the
Amazon EKS Auto Mode,

[33:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2036s) we are kind of shifting our
operational model a bit here.

[34:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2040s) So, as you can see,

[34:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2041s) all of these node agents

[34:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2043s) and the Kubernetes agents

[34:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2044s) such as whether it is core DNS,

[34:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2048s) or Q proxy, or a CNI,

[34:10](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2050s) along with the pod identity,

[34:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2052s) and the node monitoring
and the CSI node agents

[34:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2055s) all are gonna run as the
system de -processes.

[34:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2058s) When you create a cluster,

[34:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2059s) when you run cube cut you will get pods,

[34:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2061s) or a nodes,

[34:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2062s) you will not see anything
within inside of your cluster,

[34:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2065s) it's just an empty cluster.

[34:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2068s) So moving on,

[34:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2070s) another way to understand EKS Auto Mode

[34:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2073s) is understanding the shared
responsibility model,

[34:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2076s) or looking at it from a
shared responsibility model.

[34:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2078s) So this is what the shared
responsibility model looked like

[34:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2082s) previously.

[34:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2083s) Here as you can see,
AWS remains responsible

[34:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2086s) for all of the global infrastructure along

[34:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2089s) with the foundation services

[34:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2091s) and EKS was responsible for
the Kubernetes control plane,

[34:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2095s) the API server, and the HCD instances,

[34:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2097s) and customers remained responsible
for their applications,

[35:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2102s) the availability of their applications,

[35:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2103s) the security monitoring

[35:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2106s) and also the VPC infrastructure
and cluster configurations.

[35:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2109s) And, along with that,
you remain responsible

[35:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2111s) for managing the lifecycle
of these instances

[35:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2114s) along with all of the
cluster capabilities.

[35:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2117s) And now, with EKS Auto
Mode, as you can see,

[35:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2121s) Amazon EKS has shifted its
responsibility drastically,

[35:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2125s) it shifts responsibility
beyond EKS control plane

[35:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2128s) to also provide the complete management

[35:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2131s) of these cluster EC2 instances

[35:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2133s) and also the cluster capabilities.

[35:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2135s) You, as customers, remain responsible

[35:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2138s) for your application containers,

[35:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2140s) the availability of those and monitoring,

[35:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2143s) hence, allowing you to focus on

[35:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2145s) your innovation rather
than worrying about the

[35:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2148s) cluster infrastructure.

[35:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2149s) With that, you still
will have the flexibility

[35:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2152s) to bring in your own VPC infrastructures

[35:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2155s) or the cluster configurations
such as those RBAs

[35:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2157s) that you configure to provide
the multi-tenancy requirements

[36:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2160s) and any of the add-ons from the CNC

[36:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2162s) of like, we have like,
you know, so many add-ons

[36:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2164s) that are available tools.

[36:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2166s) So if you're using any of those,

[36:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2167s) you will still be able to
run those EKS Auto Mode.

[36:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2171s) With this, we take on more
of the undifferentiated

[36:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2174s) heavy-lifting, including patching,

[36:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2175s) monitoring, health and repair of the

[36:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2178s) underlying EC2 instances.

[36:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2182s) So let's get like, you know,

[36:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2184s) dive deep into the
cluster capabilities here,

[36:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2187s) just classifying the cluster capabilities.

[36:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2191s) The first one, compute.

[36:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2193s) As I said, EKS Auto Mode is built

[36:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2196s) on the principles of the Karpenter.

[36:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2197s) So all of the benefits that you get within

[36:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2200s) open-source Karpenter,

[36:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2202s) you will be able to get those

[36:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2204s) with EKS Auto Mode, as well.

[36:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2206s) We run a patch version of
that Karpenter controller,

[36:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2210s) whenever you provision a cluster,

[36:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2212s) a Karpenter controller is
already installed, right?

[36:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2215s) So the benefits such
as compute autoscaling

[36:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2218s) and also the continuous right-sizing,

[37:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2220s) you get it automatically.

[37:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2222s) Bottle rocket OS is what is supported

[37:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2225s) and bottle rocket OS, for
those of you do not know,

[37:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2228s) it's a container optimized OS,

[37:10](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2230s) which is secured by default
with read-only file system.

[37:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2234s) And one important thing to note here,

[37:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2236s) is the third one,

[37:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2237s) which is health,
monitoring, and auto repair.

[37:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2239s) So, I actually highlighted
that node repair agent

[37:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2243s) that is running on the
Amazon EC2 instance,

[37:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2246s) the managed EC2 instance now, right?

[37:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2248s) So it is actually looking
for the health status

[37:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2251s) and sending the signals
back to the Auto Mode

[37:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2253s) and Auto Mode node when
the node is unhealthy

[37:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2256s) and it's gonna replace that
node with the healthy node.

[37:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2260s) Moving on to the storage,

[37:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2262s) when you create a cluster
with Auto Mode enabled,

[37:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2264s) you get block store controller

[37:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2267s) that's already installed
by default, as well.

[37:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2269s) And the final one, the networking.

[37:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2272s) I think networking is like,
you know, a big challenge

[37:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2274s) for most of you here in the audience

[37:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2277s) and with the launch of EKS Auto Mode,

[37:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2278s) we are gonna simplify
a lot of those things.

[38:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2281s) All of these controllers,

[38:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2282s) come with the best practices included

[38:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2284s) in the opinionated default.

[38:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2285s) The first one pod networking
which is gonna be completely

[38:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2289s) managed, which is VPC CNI, by default.

[38:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2292s) So we are making a lot of change.

[38:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2294s) So with Auto Mode for those of you know,

[38:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2297s) today VPC CNI supports a lot
of configuration options,

[38:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2300s) which is kind of a challenging, right?

[38:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2302s) Customers come to us and
say what do I configure?

[38:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2304s) I do not understand.

[38:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2305s) So, by default we are gonna configure

[38:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2307s) VPC CNI in a prefix delegation mode

[38:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2309s) and if we do not see a contagious block

[38:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2311s) of IPs it's gonna fall back
to the secondary IP mode.

[38:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2314s) And along with the part networking,

[38:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2316s) network policies are gonna be

[38:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2318s) supported out of the box, as well.

[38:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2320s) You will get fully-managed
in cluster service,

[38:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2323s) load balancing the Kubernetes
service load balancing,

[38:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2325s) and also if you want to
expose these applications

[38:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2328s) outside of the cluster,
you'll be able to do so.

[38:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2331s) And the last one, which
is the cluster DNS,

[38:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2333s) there is a little bit of distinctions

[38:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2335s) that I would like you to know.

[38:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2336s) With the launch of the EKS Auto Mode,

[38:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2339s) the core DNS now runs on every node.

[39:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2341s) So by automatically providing
you the auto-scaling

[39:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2345s) capabilities of this
core ENS out of the box.

[39:10](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2350s) So, if you are wondering
why I should use Auto Mode

[39:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2354s) or why should I create a
cluster with Auto Mode enabled,

[39:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2357s) just to summarize the benefits.

[39:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2359s) First, easier and faster to get started,

[39:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2362s) and it provides the fully-managed

[39:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2364s) cluster capabilities, as well,

[39:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2366s) and secure by default by providing

[39:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2368s) OS patching out of the box and
it is automatically upgraded.

[39:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2372s) So, what do we mean by that here?

[39:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2374s) And I'm gonna talk about in detail

[39:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2376s) towards the end of this session

[39:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2378s) that, whenever you update a control plane,

[39:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2380s) all of the Kubernetes data plane nodes,

[39:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2383s) along with the core cluster capabilities

[39:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2384s) are gonna be upgraded
automatically, as well.

[39:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2387s) If your workload run on Kubernetes,

[39:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2389s) that should run on Auto Mode.

[39:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2392s) And most importantly,

[39:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2393s) we are not gonna be abstracting

[39:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2395s) any of the EC2 instance
capabilities away from you.

[39:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2398s) You will still have access to nearly all

[40:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2400s) of the EC2 instance types
that you are used to today.

[40:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2405s) If you are using a different categories

[40:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2407s) you will be able to do so

[40:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2408s) along with the GPUs and
the instance capabilities,

[40:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2413s) and they will also have access
to the silicone innovations

[40:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2416s) that is happening here at AWS,

[40:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2418s) whether it is a Nitro or AWS Graviton

[40:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2421s) which provides the price performance along

[40:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2424s) with energy efficiencies, as well.

[40:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2426s) You will be able to continue

[40:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2427s) to purchase the EC2 instance types

[40:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2429s) however you purchase today,

[40:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2431s) whether it is on demand instances

[40:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2433s) or if you use savings plan,

[40:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2435s) you will be able to use those

[40:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2436s) with Auto Mode as well.

[40:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2438s) And, if you are cost like, you know,

[40:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2442s) very cost sensitive and you
allow the cost efficiencies

[40:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2445s) that SPOT provides,
you'll be able to do that

[40:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2448s) with Auto Mode as well.

[40:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2450s) So if you're wondering,
how do I get started?

[40:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2453s) With the launch of the Auto Mode,

[40:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2455s) we did a little bit facelift

[40:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2457s) to the console AWS EKS
cluster creation, as well.

[41:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2462s) Now, you get a quick
configuration options,

[41:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2464s) with, you can now launch EKS
clusters with a single click.

[41:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2468s) Auto Mode is available for 129 and above,

[41:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2473s) and also an easy toggle options

[41:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2474s) when you go to the console

[41:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2475s) you'll be able to say whether you want

[41:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2476s) to use Auto Mode or not.

[41:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2478s) It comes with all of the
built in best practices.

[41:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2481s) So what do we really mean
by built-in best practices?

[41:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2485s) When you create a
cluster with mode enabled

[41:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2486s) by default, we actually install or deploy

[41:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2491s) two built-in node pools called

[41:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2493s) as general purpose and system.

[41:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2495s) It's again the Karpenter APIs,

[41:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2496s) it supports all of the constructs

[41:39](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2499s) that Raj talked about as well.

[41:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2502s) And if you are using the
existing cluster create,

[41:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2505s) whether it's an API,

[41:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2506s) or whether it is a console,
you will be able to do

[41:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2509s) that mode as well.

[41:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2511s) Or, if you're wondering do
I have Terraform support?

[41:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2513s) Yes, with the launch, you
will be able to create

[41:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2516s) or use Terraform with Auto Mode, as well,

[41:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2519s) or if you allow eksctl just to get started

[42:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2522s) you'll be able to do so as well.

[42:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2525s) And one of the important distinctions

[42:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2526s) with Auto Mode is you will be able to,

[42:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2529s) you know, enable Auto Mode in
an existing cluster as well.

[42:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2532s) Like, you can bring in
your existing cluster

[42:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2535s) and enable Auto Mode as you can see

[42:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2537s) is just an easy toggle option

[42:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2539s) and start to offload that
operational responsibility to EKS.

[42:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2545s) So let's get into the
details of compute portions

[42:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2548s) of the management aspect.

[42:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2550s) So what you see here is out of the box

[42:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2552s) we too provide built-in node pools.

[42:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2555s) First one, is general purpose.

[42:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2556s) So what's the use case of general purpose

[42:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2558s) and why did we really do this?

[42:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2560s) We wanted to provide you
the simplified getting

[42:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2562s) started experience.

[42:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2564s) Along with that, we wanted
you to provide support for

[42:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2567s) launching any of the
general purpose workloads

[42:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2570s) and it comes with a mix
of on-demand instance type

[42:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2573s) and support for Graviton, as well as x86.

[42:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2576s) So this is how it's gonna look like.

[42:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2578s) As you can see here,

[43:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2580s) we have the consolidation
turned on by default

[43:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2583s) and the capacity types is on demand

[43:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2587s) and also it comes with a mix
of CMR instance categories

[43:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2591s) and later instance generation than four,

[43:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2595s) the default node expiry
is set to 336 hours

[43:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2600s) which is 14 days.

[43:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2601s) Along with that, the
support for AMD64, as well.

[43:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2606s) So the next one is a system NodePool

[43:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2608s) and why system NodePool?

[43:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2611s) General purpose workloads are great

[43:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2612s) but we do also understand there
are a lot of other add-ons

[43:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2615s) that you would want to run

[43:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2617s) that you your applications depend on.

[43:39](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2619s) So system NodePool comes
with the critical add-ons,

[43:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2622s) no schedule-only,

[43:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2623s) and you'll be able to leverage

[43:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2625s) and use all of the other
AWS existing add-ons family

[43:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2629s) to run on EKS Auto Mode

[43:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2631s) by leveraging the system NodePool.

[43:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2633s) It supports both AMD and ARM.

[43:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2637s) So as you can see,
there is a special taint

[43:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2639s) that is added on to the system node pool.

[44:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2642s) Well, these best practices are great

[44:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2644s) opinion defaults are actually encouraging,

[44:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2647s) but how about the flexibility?

[44:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2649s) If you're already running
self-managed Karpenter,

[44:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2652s) or if you have a varied use cases

[44:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2653s) where you're thinking about
I need the flexibility

[44:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2656s) and for that you will be able to

[44:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2658s) define your own user-defined
node pools, as well.

[44:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2661s) So some typical use cases

[44:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2663s) to define these user-defined node pools.

[44:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2666s) Again, accelerated instances,
whether it is a GPU

[44:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2669s) or a neuro family if you want to use,

[44:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2671s) you'll be able to define those

[44:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2672s) using the user-defined node pools

[44:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2674s) and if you're a spot lover you
can create your own node pool

[44:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2677s) to use the spot instances, as well.

[44:39](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2679s) And you want to isolate
compute for different purposes

[44:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2683s) and teams operation

[44:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2684s) and also tenant isolation due
to noisy neighbor, as well.

[44:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2688s) These are some of the classic
use case when you want

[44:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2690s) to create your user defined
node pools, as well.

[44:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2693s) One of the important distinction here,

[44:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2695s) the general purpose node pool
and the system node pools

[44:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2697s) are non-editable.

[44:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2698s) Even if you go ahead and edit those,

[45:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2700s) we are immediately gonna reconcile it back

[45:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2703s) to the defaults that we provide.

[45:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2706s) As an example, here,

[45:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2707s) I am creating a separate node pool

[45:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2709s) for my ai-ml team.

[45:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2711s) As you can see, you can
provide the value inf2

[45:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2714s) and EKS Auto Mode is intelligent enough

[45:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2717s) when you say a family of inf2,

[45:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2719s) it's gonna actually provision the nodes

[45:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2721s) with all of the capabilities included.

[45:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2724s) What do I really mean by that is?

[45:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2725s) The drivers, the Kubernetes
plugins are gonna come embedded.

[45:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2731s) Along with that, you will
still have access to all

[45:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2734s) of the disruption controls,

[45:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2735s) you can still configure those budgets,

[45:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2737s) reasons, the expires, the
limits, and the weight

[45:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2740s) that Rajdeep talked about.

[45:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2744s) EKSNodeClass.

[45:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2746s) Rajdeep introduced you to EC2NodeClass

[45:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2749s) and with the launch of the Auto Mode

[45:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2750s) we are introducing a new kind class

[45:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2753s) called as EKSNodeClass.

[45:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2754s) What is this node class, right?

[45:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2757s) So in the node class
basically, you kind of provide,

[46:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2760s) the security groups,

[46:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2761s) as well as the subnets out of the box.

[46:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2764s) Just like you get the node pools,

[46:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2766s) you also get one default node class

[46:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2769s) which actually defaults
to the cluster subnets

[46:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2772s) and the node security group
that you have provided

[46:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2775s) when you created a cluster.

[46:17](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2777s) And this is referenced by
both general purpose node pool

[46:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2780s) as well as the system node pool
through the class reference.

[46:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2784s) One important distinction here is

[46:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2787s) EKSNodeClass becomes very simple.

[46:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2790s) There is no AMI selectors

[46:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2791s) because we are gonna be managing

[46:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2793s) the lifecycle of these EC2
instances for you, completely,

[46:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2796s) and we are gonna be owning those

[46:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2798s) you are no longer required
to specify any of the AMIs.

[46:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2802s) Enhance security,

[46:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2802s) with again, the bottle rocket OS supports.

[46:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2805s) If you want to bring in
your own security group

[46:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2808s) and the subnets,

[46:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2809s) you'll be able to do so,

[46:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2810s) by creating a user-defined EKSNodeClass.

[46:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2813s) It includes the network
configurations such as

[46:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2816s) the source NAT setting and
also the network policies.

[46:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2819s) You can also specify the formal storage

[47:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2821s) that's gonna be used
by these EC2 instances.

[47:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2826s) So this is how you define
the user-defined node class.

[47:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2829s) Here, I'm defining a
user-defined node class called a

[47:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2831s) team-ai-ml,

[47:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2832s) which is gonna be used by the node pool

[47:14](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2834s) that I created previously.

[47:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2838s) Again, the strategies for
defining multiple node pools

[47:20](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2840s) still apply to EKS auto node, as well.

[47:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2843s) If you want to get started quickly

[47:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2846s) and looking for that simplified
getting-started experience,

[47:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2849s) you can use the general purpose node pool,

[47:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2851s) or the system node pool,

[47:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2852s) you can use multiple node pools as well,

[47:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2855s) along with those general
purpose node pool.

[47:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2857s) The general purpose in
the system node pool

[47:39](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2859s) come with a default weight of zero.

[47:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2861s) And if you want to
prioritize your workloads

[47:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2863s) to be handled by your own node pool,

[47:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2865s) you can configure the weights accordingly.

[47:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2869s) So this is great.

[47:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2871s) One of the important, I think, benefits

[47:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2873s) of using Auto Mode is the
simplified day two operations

[47:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2878s) and also reduced
operational overhead, right?

[48:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2880s) So let's just understand

[48:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2882s) how does EKS Auto Mode
handle the automatic updates

[48:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2885s) of the core capabilities, as
well as, the data plane nodes?

[48:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2889s) It's important to understand

[48:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2891s) the shared responsibility
model here, right?

[48:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2893s) I think since yesterday I
have got so many questions.

[48:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2896s) So does it mean Auto Mode is automatically

[48:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2899s) upgrade my control plane?

[48:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2901s) That's, kind of, looks scary to me.

[48:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2903s) It's not.

[48:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2904s) You still, kind of, are responsible

[48:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2907s) for updating your control plane

[48:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2909s) and all of the best practices

[48:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2911s) before you update your
control plane still applies.

[48:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2914s) We highly encourage

[48:36](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2916s) you to do the testing in
your lower environments,

[48:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2918s) run our upgrade insights
checks to make sure

[48:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2921s) that your applications
are are still gonna work

[48:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2925s) with the latest version of the Kubernetes.

[48:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2927s) So when we release a new
version of the Kubernetes,

[48:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2930s) we also publish the recommended
optimized bottle rocket AMI

[48:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2934s) for each of the version.

[48:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2936s) And when that latest AMI is
actually, basically released,

[49:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2940s) that's when the action is gonna happen.

[49:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2942s) So before we see how
the node update works,

[49:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2945s) let's take a look at the
other distinction factor,

[49:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2948s) which is automatic updates
of the cluster capabilities

[49:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2951s) with EKS Auto Mode.

[49:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2953s) Here, right?

[49:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2953s) As you can see, Karpenter v1.0 is running

[49:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2956s) and also the EBS storage
controller, that is 1.34.

[49:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2961s) And Amazon EKS checks
the controller version

[49:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2964s) and it determines if any

[49:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2965s) of this controller requires an update.

[49:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2968s) Here, the other two controllers

[49:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2970s) did not require any update but

[49:32](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2972s) however, the network controller,

[49:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2975s) we released a new version of it.

[49:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2977s) Amazon EKS Auto Mode goes ahead

[49:39](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2979s) and updates only the required controller.

[49:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2981s) Not all the controller
updates are always necessary

[49:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2985s) and when it updates these controllers

[49:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2988s) it is important to note

[49:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2990s) that these controller
updates are not blocking.

[49:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2992s) What do we really mean by that?

[49:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2994s) Just like today, when we are updating,

[49:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=2997s) like, we do manage the
updates of the control plane,

[50:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3000s) the API server and the HCD,

[50:01](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3001s) your application still continues to run.

[50:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3003s) And similarly, while we are
updating these controllers,

[50:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3006s) your application should
continue to run, as well.

[50:10](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3010s) So the next one, how does
the data plane updates work?

[50:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3015s) It is completely zero touch.

[50:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3016s) You do not have to do anything.

[50:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3018s) Amazon EKS Mode respect
the disruption budget.

[50:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3022s) It sees that the control
plane is now updated

[50:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3025s) and it is updated to 1.31.

[50:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3027s) So it goes ahead.

[50:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3028s) It replaces the old worker
nodes with the latest AMI.

[50:33](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3033s) Here, you see the old one was replaced

[50:35](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3035s) with the 1.31 AMI, as well.

[50:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3037s) And it does that,

[50:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3038s) so, by respecting all of
the disruption budgets,

[50:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3041s) whether it is the node
pool disruption budgets,

[50:43](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3043s) or whether it is your
manifest PO disruption budgets

[50:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3047s) that you have configured,

[50:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3048s) it's done in a rolling deployment fashion.

[50:50](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3050s) And one thing to note, by default,

[50:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3052s) the general purpose node pool
comes with a 14-days expiry.

[50:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3056s) However, you can configure
your user-defined node pools

[51:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3060s) expiry up to 21 days.

[51:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3062s) So it force updates on the 21 day

[51:05](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3065s) if not already updated, as well.

[51:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3068s) So the final thing,

[51:10](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3070s) how does security updates are
hand handled with Auto Mode?

[51:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3073s) Similar concept here,

[51:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3075s) Karpenter drift detection comes into play.

[51:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3079s) Amazon EKS publishes the latest AMI,

[51:22](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3082s) which includes the waste patches.

[51:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3084s) That might also include
patching of these agents

[51:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3086s) that are running on the node too.

[51:28](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3088s) IT district, it again respects
the disruption budget.

[51:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3091s) It goes ahead and replaces these

[51:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3094s) worker nodes in a rolling
deployment fashion.

[51:37](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3097s) As you saw, the old one were replaced

[51:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3100s) with the latest AMI version, as well,

[51:42](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3102s) against force update of 21 days
still applies here, as well.

[51:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3106s) So, if you have not
started using Auto Mode

[51:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3109s) or if you haven't created
a cluster with Auto Mode,

[51:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3111s) I highly encourage you to
get started using Auto Mode.

[51:55](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3115s) Whether, you are new to Kubernetes or EKS,

[51:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3118s) or you would want to accelerate
your modernization journey,

[52:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3123s) EKS Auto Mode is for you,

[52:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3124s) or you want to offload that
operational overhead to EKS.

[52:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3129s) Again, do not wait,

[52:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3131s) start to use EKS Auto Mode in production.

[52:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3135s) Auto mode is generally available in all

[52:16](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3136s) of the commercial region.

[52:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3138s) We will be soon launching
the support for China,

[52:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3141s) as well as Claude 2.

[52:23](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3143s) With that, I'm gonna welcome
back Raj back onto the stage

[52:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3147s) for closing thoughts.

[52:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3151s) - All right, so seems like EKS Auto Mode

[52:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3154s) helps all of you to get started faster,

[52:38](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3158s) but as a someone who is
enthusiastic about Karpenter,

[52:41](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3161s) what's happening with
open-source Karpenter, Sheetal?

[52:44](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3164s) - We love Karpenter.

[52:46](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3166s) We develop that with love here at AWS.

[52:48](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3168s) We are committed to develop
Karpenter in the open.

[52:52](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3172s) It's not going to go anywhere.

[52:54](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3174s) As you heard, B repeatedly say,

[52:56](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3176s) Amazon EKS Auto Mode

[52:58](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3178s) is built on the principles of Karpenter.

[53:00](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3180s) So any feature that is made
available in the Karpenter,

[53:03](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3183s) it's gonna be made available
in Auto Mode, as well.

[53:06](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3186s) - That's great to hear.

[53:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3188s) So as you could see,

[53:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3189s) you have a lot of
flexibility at the same time,

[53:12](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3192s) if you are someone who is like, okay,

[53:13](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3193s) how do I get started with EKS?

[53:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3195s) Faster and simpler. EKS
Auto Mode is the answer.

[53:19](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3199s) You can create the cluster,

[53:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3201s) you get bunch of
capabilities out of the box.

[53:25](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3205s) We manage, and upgrade the add-ons,

[53:29](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3209s) like Karpenter storage and Ingress

[53:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3211s) and a lot of other features
that Sheetal talked about.

[53:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3214s) As always, either you use
EKS, EKS Auto, or Karpenter,

[53:40](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3220s) it's running fully upstream
Kubernetes conformant version.

[53:45](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3225s) With that, I know this
is a lot of information

[53:47](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3227s) and this is just the beginning.

[53:49](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3229s) We have lot more information available

[53:51](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3231s) throughout different sessions.

[53:53](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3233s) Sheetal, here, is running
two builder sessions,

[53:57](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3237s) one tomorrow, one day after.

[53:59](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3239s) You can also learn a
bunch about EKS Auto Mode,

[54:02](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3242s) you can read the launch blog.

[54:04](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3244s) She just released a launch
blog right before this talk.

[54:07](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3247s) As well as,

[54:08](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3248s) we have guidance on

[54:09](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3249s) if you're using cluster autoscaler today,

[54:11](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3251s) how to migrate to Karpenter v1.

[54:15](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3255s) With that, we are gonna be here
for a little bit of question

[54:18](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3258s) and answer, before we start the Q and A,

[54:21](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3261s) you wanna move one more forward, Sheetal.

[54:24](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3264s) Don't forget to complete
the session survey,

[54:26](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3266s) if you like this session

[54:27](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3267s) or if you have not, give us some feedback,

[54:30](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3270s) we take them seriously.

[54:31](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3271s) - Thank you so much for
attending this session.

[54:34](https://www.youtube.com/watch?v=JwzP8I8tdaY&t=3274s) - Thank you.
(audience clapping)

