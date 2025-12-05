# AWS re:Invent 2024 - Securing Kubernetes workloads in Amazon EKS (KUB315)

[Video Link](https://www.youtube.com/watch?v=yuXF-NXaelI)

## Description

Kubernetes clusters can be complex environments with multiple components and configurations. Securing your software supply chain, control plane, worker nodes, and pod security policies is essential to prevent unauthorized access, resource exploitation, and data breaches. In this session, learn about features that can help you secure your Amazon EKS clusters. Get guidance on how security and platform administrators can protect information, systems, and assets that are reliant on Amazon EKS while delivering business value to their customers. This session covers security guidance specific to Amazon EKS, Amazon ECR, AWS Identity and Access Management (IAM), and network security.

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

- Hey everyone, my name is Micah Hausler. You are at Kube 315:
Securing Kubernetes Workloads in Amazon EKS. I'm a principal software engineer at AWS. I work on Kubernetes, Kubernetes security, I've contribute to upstream Kubernetes, I'm on the Kubernetes security committee, so we take in security
reports and evaluate them, and then issue fixes Kubernetes. - And I'm George John. I'm a product manager
with Amazon EKS team. I'm very excited to be here, and thank you all for taking
the time to join us today. - Am I on? Sure. - Oh, okay.
- [Micah] Great. - So for today's session, we thought we'll take
a different approach. We are gonna look at how you
can secure your workloads running in Amazon EKS from
a few different layers. So first, we'll take a
look at the big picture. We look at the controls that are available to you at a cluster level. So we look at what are, how you can secure
access into the cluster, we look at how you can assign permissions to applications running in the cluster so it can access AWS resources outside. So things like S3 Bucket, DynamoDB, how you can securely set that up, and finally, in the
first section, we look at how you can use the various AWS services in the security space, and how those integrate with Amazon EKS. And then we'll dive a little bit deeper, we'll go into the infrastructure layer. So by infrastructure here, I'm referring to the EC2 instances, the working notes that you run in the cluster. And we'll also look at the,
some of the networking VPC, and what are the controls and
mechanisms available for you to secure the infrastructure layer. And then finally, we'll jump
into the application layer. We'll talk about the best
practices, some of the controls to secure your images and pods that make up your application. So one thing I wanna call out
is that, in today's session, our focus is really on
EKS and AWS controls and capabilities that
are available to you. But at the end of the session,
we'll share a resource, namely the EKS Best Practices Guide that talks about the
Kubernetes capabilities and tools that are available so that you get the full picture in terms of how you can secure or cluster. So with that, let's get started. So over the last few years, we have seen a massive uptick
in adoption of Kubernetes. As per the 2023 Cloud Native
Computing Foundation's annual survey, 84% of the
respondents are using Kubernetes, either in production, or evaluating it. And this is something we
are seeing at Amazon EKS. Every year, we have customers
running tens of millions of clusters, and this number keeps growing. And when we launched
EKS over six years ago, it was really in response
to customer feedback that managing Kubernetes at scale is hard. You know, customers were spending
a lot of time monitoring, scaling, managing the
Kubernetes control plane, and they want something, they
want a native to integrate with various AWS services. And since then, EKS has emerged as a
most trusted way for you to run Kubernetes in AWS. Now we remove the
undifferentiated heavy lifting of not just managing the
Kubernetes control plane, but VARIOUS aspects of the cluster. For AWS and EKS, security
is the highest priority. Now when we, as always,
operating securely in the cloud is a shared responsibility. AWS takes responsibility for
the security of the cloud, and you as a customer takes responsibility for security in the cloud. So here you can see at the bottom, three layers are all
managed by AWS and EKS. So things like the Kubernetes
clusters control plane, the infrastructure it runs on,
the regions, the local zones, some of the foundational services, the control plane leverages, like the compute storage networking, and the actual Kubernetes
bits, like the API server that runs in the control
plane, that CD database. All that is our responsibility. We patch, we scale, we manage, we make sure it's available and resilient. And the layers about it are
really the EC2 instances and the worker nodes that run in your VPC. Things like, whether the operating system that runs on the EC2,
whether it's patched, whether it's monitored,
whether you're looking at the health of it. Some of the cluster
capabilities like auto scaling, and even the Kubernetes
pieces that, the binaries that run on the worker
node, like the kubelet, or the container runtime. All that is your responsibility. But AWS and EKS offers
you various tools like, there are multiple capabilities
like security groups on pods, subnets, private
endpoint access, EKS add-ons, EKS-optimized AMI's, all of
which will make it easy for you to secure your data plane, your VPC, and the things that run there, but at the end of the day,
it's still your responsibility. Now that we have covered
some of the basics, let's jump into the first layer. So first we look at, like I said, the cluster level controls. When we launched EKS, we wanted to offer a Kubernetes native wave for authenticating into the cluster. So what we did is, we have this config map called AWS-AUTH, where you can define the
mapping of IM principals to Kubernetes permissions. Now this approach had some trade-offs. You know, on one hand it is good because you can use IAM, you don't need to maintain a separate identity provider, and you get all the benefits of IAM, like multi-factor authentication, the auditing with
CloudTrail logs, and so on. But on the other hand, now you had to deal with different set of APIs
to create an EKS cluster with all the permissions. For example, you would use EKS
APIs to create the cluster, and then you have to
move to Kubernetes APIs to provision the mapping
and set up the config map. This meant that automating, or using infrastructure as code
tools to bootstrap a cluster with the required permissions is hard. Another challenge with the
config map experience was, it was a little bit brittle. Like if you make a typo in the config map, or you don't follow
the exact format there, you could accidentally
lock your users out. And there were behaviors like, when you create the IAM
identity that is used to create the EKS cluster, automatically gets super user access. Now this was something which, was behavior which many
customers didn't like. So to address these, soon
after re:Invent last year, so Mike and I were on stage
last year, we talked about it as something that's coming out. It came out as a feature
soon after re:Invent, called Cluster Access Management. What Cluster Access Management does is that it kind of unifies the APIs. So no longer you're switching between EKS and Kubernetes APIs. Instead, you can just use EKS
APIs to create the cluster, set up the permissions, you
have cluster ready to go. And it simplified the configuration, so users and other AWS
services that needed access to the EKS, the whole setup
was much more simpler now. And finally, it gave you granular control. So, if you remember the
scenario I mentioned before, now with Cluster Access
management, you are able to revoke the permissions
granted automatically to the IAM principal
that creates a cluster. There is a link to the blog at the bottom. If you are interested in
learning more about it, please take a look. We strongly encourage you to take a look at Cluster
Access Management. For EKS, that is the future,
that is where we are heading. All the new features, all the
capabilities will be built on Cluster Access Management. And if you have an existing cluster that's using the older
AWS-AUTH config map, we strongly encourage you to move. There is a simple, easy way
to migrate from one to the... From config map to
Cluster Access Management. Let's look at the actual
flow behind the scenes. So first, you would be integrating with... Or interfacing with IAM to
create the IAM principal, whether it's a role or user. And then you would be
interfacing with the new APIs that were introduced
as part of the feature. The same functionality is
also available on the console. So you can either use EKS
console, or you can use the APIs, and then you would be
creating two main entities. First one is access entry. So access entry would
associate with the IAM identity you created in the previous step, and then you create an access policy and define, use access policy
to specify the permissions that the access entry has. So once the first two steps are done, you have pretty much set up the feature. The Cluster Access Management feature. And then let's say you
have a user who's trying to access the API server. What happens is implicitly,
AWS STS is called, either by IAM Authenticator,
or the CLI get token operation. And when the request
lands in the control plane on the API server, we have a web hook which intercepts the request,
looks at the STS token, tries to find the user identity
associated with the token, and then if it doesn't
matching with the access entry, if that succeeds,
authentication is complete. The next is authorization. For authorization, there
is a series of authorizers that we look at, and then
if the user identity maps with the access entry and access policy, the authorization is also allowed, and then the request can flow In. Cluster access management
is available both through APIs and console, so
you have the flexibility there. Alright, so the first
part I talked about is how can you set up
access into the cluster? Now we will move on to, you have an application
running in the cluster, most likely you might need
to access an AWS resource, and you could have a
Kubernetes application that need to access S3 bucket. It could be DynamoDB table,
it could be any AWS resource. How do you make sure you
assign the right permissions to the application? So one option we had previously,
and it's still available, is called IAM Roles For Service Account. In short, it's called IRSA. So we launched IRSA in 2019. IRSA enabled you to grant
granular AWS permissions to pods. So you could have multiple pods belonging to multiple applications all running on the same EC2 instance, but have effectively
different set of permissions. Now this was launched
in 2019, like I said, and our goal was to make sure IRSA works across the different
Kubernetes deployment models we support in AWS. So we wanted IRSA to work
with EKS, manage those in the cloud, EKS Anywhere, self-managed, Kubernetes clusters on EC2
instance, Red Hat, OpenShift, service for AWS. ROSA in short. So we build IRSA by not
taking a direct dependency on any of the EKS APIs. We leveraged some of the
foundational services like IAM, but that had some trade-offs. One was, now that we are
depending on IAM for IRSA, you had to create an
IAM, or OIDC provider. Now this was a privilege operation. We heard from some customers,
especially customers in regulated regulated industries, that the cluster administrator
doesn't have IAM permissions. So now it means that the
cluster administrator has to reach out to identity... Sorry, IAM administrator. There's a lot of back
and forth to set up IRSA, which was not really user friendly. The other one was the scoping. So when you create, when you use a role, or when you create a role for use in IRSA, you typically have to bound that role, or specify, what are the clusters that can assume this role? Now it means that if you wanna use a role in a new cluster later on, you
have to go back to IAM role, keep updating the trust policy, or if you wanna rework
a role from a cluster, you have to go back to
the roles trust policy and keep playing with it. And finally, there are some
limitations in terms of how many clusters can a role be used with. And to address these,
at re:Invent last year, we launched the feature
called Pod Identity. So Pod Identity simplifies trust. Pod Identity enables you to create a role that can be assumed by
EKS service as a whole. So previously, when you create a role, you specify the clusters
that it could assume, and now with Pod Identity,
you can just specify that AWS service can assume it. So it doesn't matter which
cluster you're using, but you also have the ability
if you wanna lock it down to a few clusters, you
have that ability as well. It offers new capabilities like attribute based access control by supporting IAM role session tags, so it enables reuse of policies
and roles across clusters. And finally, you are able
to now create clusters with all the required
permissions in one go. And there is a link to
a blog at the bottom if you are interested in
learning more about Pod Identity. So one thing I wanna emphasize is that, like I said, Cluster Access
Management is the future for the previous talk, the
first part of this talk, I said AWS-AUTH config map is older way, but here, IRSA is not the older way. We will support both. We have no plans to deprecate IRSA. IRSA would continue to exist
along with Pod Identity. Pod Identity is purpose
built for EKS managed service in the cloud. It doesn't work with EKS Anywhere, or self-managed Kubernetes
clusters on EC2. So it's all about giving you more options. Depending on your use case and needs, you can pick the solution
that best fits your needs. Alright, let's look at the flow. For Pod Identity, a prerequisite is that you need to run
the Pod Identity agent, as a (indistinct). So it needs to be run, be
running on all worker nodes. So here, let's take a
very simple scenario. Let's say you wanna deploy an application to your cluster that needs
to access an S3 bucket. It could be any AWS resource, I'm just using S3 as
a simple example here. The first thing is, you
would be interfacing with, or using IAM to create an IAM role. An IAM role has two
parts: a permission policy and a trust policy. A permission policy is
where you're specifying, this can access S3. So in our case, we want the application to be able to access S3, the permission policy
would have the permissions for it to access S3. And then you have the trust policy. This is where Pod Identity
is different from IRSA. The trust policy for
Pod Identity specifies that this role can be
assumed by EKS's service. So we have a new service
principal we introduced, and that's a one time step. It doesn't matter
whether this role is used on cluster A or B, or a C in
the future, it will just work, and it's a one time step you have to do. And after that, what you do is you create, use the Pod Identity APIs. Again, you can use the
console if you want, but there is a operation called Create Pod Identity Association, which is how you map the IAM role that you previously created
with the service account. So one good thing here is
that that service account, the Kubernetes service
account, need not exist at that point in time. It can be something you
create in the future. The good thing about that is, if you are a cluster administrator, you wanna set up the cluster
with all the permissions, so when the app dev teams comes in later, that cluster is ready to go for them, you can pre-create the
Pod Identity Association with all the mappings ahead of time. Now these are the two things you do to set up Pod Identity. The feature. And then let's say later on, you have app dev team is
deploying their application, a pod is spun up. When we detect that this
pod has a service account associated with it, which
was previously mapped through the Pod Identity
Association, we have a web hook that intercepts a request,
and will mutate the pod spec. And we'll add couple of
environment variables, well known environment
variables to the pod spec. So when AWS SDK comes up, it knows these environment variables. It would mount these, it would fetch the service account token that's mounted to the pod. It'll make a call to
the Pod Identity agent, pass the token, the service account token. And then the Pod Identity agent
would then call assumed role for Pod Identity, which is a
new API we introduced as part of the Pod Identity API. And this API would then validate
the service account token that was passed. If it is validated, it returns
a temporary AWS credential, which is then injected into the pod. And then the application
can use that AWS credential to access S3. All right, so what's new in Pod Identity since the launch at re:Invent last year? Pod Identity is now available
in all commercial AWS regions, and China, as well as
the US GovCloud regions. We open source the agent itself. So when we launched, it was
only available as an EKS add-on. We got feedback from customers
that they wanna deploy it as a helm shot, or wanna
bake it into their own AMI and create a custom AMI. So the agent is now open sourced. And the last one is, we introduced
support for Pod Identity and EKS add-ons. So add-ons are operational software that you can run in the cluster. And these software
usually needs permissions, AWS permissions to access AWS resources. Previously, the only way
you could set that up was through IRSA, but now Pod
Identity is also available, which greatly simplifies
the add-on setup experience. Alright, so now let's move
on to some of the controls that are available for you to
identify an alert on issues. The first thing is looking
at the access, the requests that are coming into
the API server itself. So when you create an EKS cluster, you get a cluster endpoint, which is basically the API server that's running in the control plane. All the requests coming into
the API server are logged in the control plane audit log, and they are made available in CloudWatch. This is an opt-in, or
something you have to enable. But once you enable control plane logging, the logs will automatically
flow to CloudWatch. Now it being in CloudWatch means that you can use things
like CloudWatch log inside to further analyze it. At the end of the presentation, we'll share the security best practices. Within that, there's a section
called Detective Controls, and there are some pre-built
CloudWatch log insights (indistinct) we have found to be useful. So that is something you
wanna probably take a look at after the presentation. The other benefit of it
being in CloudWatch is that you can set up alarms. So if you wanna detect
increase in 403 forbidden or unauthorized access, you're now able to kind of alert yourself
to those situations. Alright, so next one is, so previously we looked
at, looking at the requests that are coming into the API
server endpoint of the cluster. This is about looking at the requests that are coming into the EKS API. So here, EKS API is, the EKS
service APIs that you use to create cluster delete,
cluster update, cluster, all of those EKS APIs, not Kubernetes APIs. All of those are logged in CloudTrail, and along with CloudTrail
logs and CloudTrail insights, you're able to analyze them. And finally, we have Amazon detective. So all VPC flow logs, if you wanna analyze or visualize them, you
can use Amazon detective, which is integrated with EKS. Next is encryption. So with some of the
native AWS storage options like EBS, EFS, FSx for luster, is supported in EKS. You can encrypt at rest with
either AWS managed keys, or you can bring your own keys. Along with that, some of the
secret sensitive information that's stored in the Kubernetes
cluster is typically stored in the Kubernetes secretS object. EKS gives you the ability to
encrypt a secret subject either with a key that is the AWS
Key Management Service office, or you can bring your own key to KMS, and then use that to encrypt it. And with the keys being in
KMS, you get the ability, you get the benefit of automatic
rotation offered by KMS. So what are some of the
other cluster scoped controls that are available to you? The first one is the
Kubernetes cluster endpoint. So here by, when I say
Kubernetes cluster endpoint, I'm referring to the API server endpoint that's available in every cluster. By default, it's in a public mode, meaning that any traffic
originating from your VPC, if it has to reach out to the API server. Let's say your worker
nodes need to reach out to the API server. The traffic leaves the VPC, it remains an Amazon network, and then comes back to the API server. But if you, let's say you wanna
make it completely private so that traffic always remains in VPC, you have the option to
configure the endpoint to be in a private mode. The next one is the other
API, which is the EKS APIs. So today, again, if you have a need where any traffic originating
from your VPC should hit the EKS APIs through a private endpoint, or in a private manner, there
is AWS private link that, this feature I think we
launched a year or so ago. So you can leverage AWS
private link with EKS service to kind of get that private connectivity. The next one is use manage
components whenever you can. So EKS add-ons, EKS Optimized
Amazon Machine Images, or AMIs. These are something we
take responsibility for. We always are looking for issues. If there are vulnerabilities,
it is on us to go patch it, and make a new version available. And then there are APIs
that you can leverage to apply those to your cluster. So when possible, you
leverage managed components. The last one here is using security hub for scanning your cluster. Security hubs has, I think
around eight predefined checks to look at the security
state of your cluster. So, you know, that is
something you can also look to get an idea of how your cluster is from a security standpoint. Alright, with that, let me invite Micah. - Thanks George. So next, the next section is around infrastructure
scoped security controls. So, as George talked about, we kind of are separating
cluster from from infrastructure. So by infrastructure, we really mean where does your containers run? And the first thing that
we're really excited to talk about is EKS Auto Mode. This was just launched yesterday, so you're getting the fresh stuff. EKS Auto Mode is a new
feature of EKS that helps you to automate your entire
Kubernetes cluster infrastructure. So with Auto Mode, AWS
takes responsibility for creating and deploying nodes. You only have to create your pods. What this really allows you
to do is improve performance, and optimize resources. Using Carpenter, which
is an open source project that we created, we manage
that completely for you, and we will create the
nodes that are required for the pods you define. If you define a pod that
requires X amount of memory, Y amount of CPU in a specific AWS zone, we'll create it there. Similarly, as you scale up a,
say a Kubernetes deployment and add more replicas, we
will create the best type of EC2 node for you. Similarly, we will also consolidate and find the best type of nodes for the workloads that you have running. This really simplifies the
management of your cluster. You don't have to think
about creating a node group, which zones do you wanna create it in? You just have to use the Kubernetes API to create a configuration
for EKS Auto Mode. And also this really reduces the operational overhead required. You don't have to think about
updating the machine images that AWS is responsible for creating and making available to
you, you just use the nodes. Nodes have a max lifetime of 21 days, so even if you have a workload that's running more than 21 days, that node will get
recycled, and gracefully, your application will get recreated onto another node that's the
latest Amazon machine image, with the latest security patches, and so it's always up to date. This really helps you
increase your own agility, and accelerate your own innovation because you're not having
to spend time trying to keep all your nodes up to date. You really get to offload all of these offer operations to AWS. This also just really helps
you improve the performance and availability of your application. As I said before, it's graceful restarts. Graceful migration of of nodes. So you don't have to think about what sort of scaling policies you have to apply to an auto scaling group. This will do it for you. And finally, this really
does help you optimize costs by automating the capacity
planning and dynamic scaling. You don't have to go say,
okay, what kind of node, what's the best type of node
that I need for my workload? We'll determine that based on the requests in your Kubernetes pod. So this, as George shared earlier, we have a shared responsibility model. And with EKS Auto Mode,
this changes a little bit. In the previous example, if you're using EKS managed noDE groups, there's more of the
responsibility that's on you. In this model, all that's on you is really
maintaining the security of your containers, and
your VPC infrastructure, and any add-ons that you install on top. There's a number of add-ons that are automatically
included with EKS Auto Mode. Things like the kubelet, the
container networking interface, the kube proxy, and some CSI drivers. Those are automatically maintained by us. But other add-ons, those are still on you, but there's just a whole lot
less that you have to manage. Another aspect to talk about in terms of the cluster security is really about cluster network security. So you have applications
running on containers and pods in your cluster, right? There's two main configurations
that you have here. The first is to take advantage of Kubernetes networking policy. So this is part of
Kubernetes as the interface, and then powered by the AWS VPC container
network interface or CNI plugin. You can define rules in the
Kubernetes API that say, I wanna let pods in this
network namespace talk to pods in this other network namespace. You get very granular
control over pod labels, or even at the pod label level, and L seven. So, what host name, or what TCP port. That is enforced on the host. So it's using EBPF in the EKS VPC CNI. Other, if you're using
a different CNI plugin with a different enforcement layer that might be using a
different technology. But that's enforced on the host. The other method is with security groups. So these are the same security
groups you know and love, with EC2, but they can be
applied to your Kubernetes pods. So each pod in Kubernetes that uses an elastic network interface, or an ENI that gets attached
to your EC2 instance, and EC2 security group per
pod attaches a security group to that pod's network interface. So this lets you use an off host mechanism that can't be modified on
the host to control what app, what network calls a pod can make. And included is a link where
you can read more about that. As George mentioned, there's
some detective controls that you can do with CloudTrail. Another form of detective controls more around the infrastructure
layer are around GuardDuty. So GuardDuty has some
really great integrations with Amazon EKS. The first integration that
we built with GuardDuty was for audit log protection. So Kubernetes has an audit log,
Kubernetes is an API server. It emits an audit log for every request that's made against it. So audit log includes things
like if you create a pod, it tells you the pod name,
which user created the pod, other metadata about the pod. And all this goes to a central log. You can turn it on,
send it to your account, but with GuardDuty, you
can also have that log sent to GuardDuty for your cluster. GuardDuty uses machine
learning, it also uses quite a bit of like
rules that we've observed from known attack patterns. And I interface, we interface
with the GuardDuty team a lot to say, here's new things
that are coming in Kubernetes, here's new things we should
look for configurate, either misconfiguration,
or attack patterns. And so GuardDuty will send you an alert if it detects either a
mis-configuration, if you, say you accidentally configure anonymous, so unauthenticated users to
the Kubernetes API as admin. I've seen it before,
it's awful, don't do it. But if you did it, you would get an alert from GuardDuty saying, hey, this happened, you should go remediate this. And same for a bunch of
other known attack patterns. So that's a really, really
great protection mechanism. You can enable at your
account level to say, I want this for all my clusters. Second is Amazon GuardDuty's
Detective controls is with runtime protection. So Amazon GuardDuty also
has an agent based mode where they will deploy
through EKS add-ons, an agent onto every host, to
look for known attack patterns, whether that's through
file to file changes, or other known heuristics
on the node to look for malicious attack patterns
that wouldn't show up in the Kubernetes audit log, but could be seen in,
say, the Linux audit log. So that's another great control. Again, you can turn that on at the account level, or at
the AWS organizational level for your account, to just make
it enabled on all clusters. A few other infrastructure
scope security controls that we just recommend for
customers, are to restrict and minimize access to your
instances using AWS SSM. So if you're used to spinning
up a VM, if you ever pointed and clicked through the AWS
console your first time, you probably used SSH right? Everyone's sort of familiar with SSH. Generating SSH keys, get your
(indistinct) on your instance, and then opening a port
on your security group, and getting an IP address, and, right? Connecting to your host. That is... When you've done that, I
would not be surprised, and you can be ashamed, it's okay, to have set the incoming
security group rule to allow anywhere in the world, because I don't wanna go look up my IP. What if I'm at home, and my IP changes? Or if I'm at office and I
have a floating IP, right? You might set it to the whole world. That's not great, but you
might've done it right? You don't wanna do that in production. And so with AWS systems
manager, you can turn off SSH, and enable SSM to access your hosts, and the SSM agent connects
back to the SSM service. And with SSM session manager,
you can log into your instance through SSM without
needing that open port. So it's a great security control that's not necessarily unique to EKS, but just a best practice
that we really recommend, because it really can save you from having mis-configured an open port to the world. You just don't need to do
that for something like SSH. There's all kinds of internet bots and everything scanning, you know, the global IP space looking for, what's listening on port 22? And you don't wanna be hit there. Additionally, we recommend
using a container optimized OS. So we have the Amazon EKS optimized AMIs, those are using Amazon Linux. And then we also have Bottle Rocket, which using the same
kernel with Amazon Linux, but using a more hardened container, only container first OS. EKS Auto Mode actually uses
Bottle Rocket under the hood. But bottle rocket is a
much more locked down OS that doesn't have, it's
not a general purpose OS, it doesn't have a package manager. So you can't keep packages up to date, you don't have to keep
packages up to date. You get a new... You create a new instance
when you need a new package, or to get a security patch. And then finally, we also recommend just verifying your
configuration of your cluster using the CIS benchmark. We have an EKS specific CIS benchmark that lets you verify the
configuration of your cluster, making sure you have things like, if you don't want public access
to your cluster turned on, you can have that turned off. Making sure that you
have all the other APIs that we've talked about, like
Cluster Access Management, making sure that you're no
longer using config map mode. You can use the CIS benchmark
with open source tools like Kube-Bench to validate
your configuration here. And finally, the final
section here is really to zoom in to the application
scope security controls of your cluster. So, as we mentioned, pod
security is kind of one of those things that you need
to pay attention to, right? So one of the best mechanisms
for this is really using either entry Kubernetes
Pod Security Standards, or some out external pod security, so policy-as-code solution. There's open source
solutions like Kyverno, or Open Policy Agent Gatekeeper, or others out there that
help you enforce some of your security standards as code. Some of the best, just to
hit some highlights here, there's a whole slew of them. Again, we'll have a link later to the EKS Security Best
Practices Guide with these. But a few ones we just
really wanna call out because these are just so critical, is limit the privilegeD containers. And I'm specifically using
the word "limit" here, because sometimes people think they should never have
privileged containers. And if you're not familiar
with privileged containers, if you ever run docker command line, you have a dash dash privilege flag. When you run privilege, that
gives a container access to all kinds of Linux devices, and privilege escalations on the host, so that can do management of the host. Sometimes that's necessary. So when we say limit, we don't mean eliminate
privileged containers. For example, the AWS VPC CNI needs to set up network namespaces so that pods can have their
own network on a host. That needs to be privileged. There are things like the, or the CSI, the Container
Storage Interface agents for EBS, or for EFS, or several of the other
Amazon integrations. Those might need to be
privileged, and that's okay. But what we do encourage
you to do is limit that. So if you have an application
that's serving web traffic, probably does not need to be privileged, so don't make that privileged. Similarly, if you have an application that's running on your
cluster, that is, again, take this web serving traffic example, that's never gonna talk
to the Kubernetes API, disable service account token mounts. By default, Kubernetes
mounts a token into every pod so that it can talk to the
API server and authenticate. It doesn't have any
permissions by default, but it's there as an
authentication mechanism. If you don't need it, turn it off, right? Similarly, restrict use of host path. It's just one of those things that, if you don't need, turn it off. There's all kinds of CVEs in the past, whether that's in container
D in Kubernetes itself, or runC, the container runtime agent, that have centered around host mounts. So if you don't need them, turn them off. And then finally, just as you
build your container images, when you define that, whether
it's in your docker file, or however you're defining
your container image, or actually, not in your docker file, but actually in your pod
configuration, if your pod, say again, we'll take
the web traffic example. If the the pod never has to write, or the application in your
pod never has to write to the file system,
consider switching that to a read-only file
system in your container. That eliminates a whole
slew of attack vectors that your application could
potentially be vulnerable to, and you just don't even
have to worry about. Another aspect that we like to think about is just image security. So your images that
you're running are pulling from somewhere, probably Amazon
ECR, maybe somewhere else. We highly, highly recommend scanning these for vulnerabilities regularly. So with Amazon ECR, you can use the native
Amazon Inspector integration and get scans of your image and reports if there are secure security
vulnerabilities found in your application, whether
that's in the system packages, or there's some support for
language packages as well. Also, when you're using
ECR, if you don't need ECR to be coming from outside
of your VPC, you can use ECR with private link. You can lock down so that
your image can only come over private link. That's a great, great control
that we've seen customers use. And finally, similar to
the read-only file system, this is more of a thing that you have to configure in your container
definition when you build it, but configure your image
to use a non root user. It's sort of a default if
you're ever, use a docker file when you build, it just
uses the root user. If you're listening, if you, again, if you have a web container
that's listening on whatever port it is, it
doesn't necessarily need to be running as root. And so you can change
that to a non root user. That, again, just reduces
the permissions that that Linux process has when
it runs in your cluster, so that it has much less likelihood of, if there's a security
event, of having permissions to escalate and do things
that you don't want it to do. The next part I wanna
talk about is something that we're pretty excited about. So this is pretty new. So Kubernetes has built in authorization. If you've ever used Kubernetes, you've probably configured RBAC, or role-based access control. And you've probably written an
RBAC policy to allow some pod to manage things in your cluster, or maybe a human to manage
things in your cluster, right? If you've ever written an RBAC pol- How? Quick show of hands. How many of you have ever
written an RBAC policy? Okay, good, good. We got a lot of people here. Okay, so if you've ever
written an RBAC policy, you've probably come into some
of the limitations of this. It's worked great in
Kubernetes for the last, like eight years or so. But the more and more that
we've heard from customers, we're seeing some of the
limitations of RBAC come into play. If you've ever written
an RBAC policy, you know that it's allow only. You can't do a denial. So if you wanna allow, say
you're a platform team, you wanna allow a developer
or group of developers to manage some deployments in the cluster, but you don't want them
to manage deployments or daemon sets in the
kube system namespace. That's becomes really painful
as a platform administrator because you have to create a
RBAC policy in every namespace for those developers. If you create a Kubernetes cluster role, you have to give it
either every permission on every namespace, or just
specifically named namespaces. There's no conditions. That becomes really painful. So there's no conditions
and there's no denials. Cedar is a access control language and runtime evaluation
engine that's open source, built by AWS. It was launched several
years ago at re:Invent. There's also a managed service for this, Amazon Verified Permissions. But Cedar can be used for, actually even your own applications. You can define what kind
of actions can be permitted by who, and on what resources. So over the last few months, we've built and then open sourced a new prototype for re-imagined Kubernetes
authorization using Cedar. And it's on GitHub, so
you can see the link here. You can actually download
it and try it out. We're gonna show a demo here in a second, but I wanna show just kind of
quickly what this looks like. So if you've never seen
Cedar code, that's okay. Cedar is very, very easy to read. Cedar policies have basically three or... Well, three parts we'll call 'em. You have effect. So in this policy, this
is a contrived policy that doesn't do anything
'cause there's not, it's not actually used, but
just to show you kind of what can be done with Cedar. There's an effect, so a permit or forbid. This is a permit policy. Then you have the main
section of the policy where you have principal,
action, and resource. You define what principal
this policy applies to, you can define what
action, or set of actions that this policy applies to. So I'm saying here,
principal is a custom user. Not a specific one, but just
that's the type of principal. The action is in the
list of "get" or "list". So it can be either a
get or a list action. And then the resources,
some custom resource type that I've allowed. But it's now has something
that you can't do in Kubernetes RBAC. It has a condition. We have this when clause. We're only gonna allow
this policy to take effect when a principal is in a specific group. And so we have a custom
group type we've defined, and an identifier for that group. So maybe it's a name. And then one other part
to this condition is that the resource has some field on it, and that field must equal cool value. And then finally, there's a
syntactic sugar called an... That's another condition on Cedar policies called an "unless" clause, that negate when this policy applies. It makes it a bit simpler
than having to write, and, or, not, equals
to in your when clause. You can just add an unless clause as well. So we're gonna, this
policy will all take effect with the when, unless resource dot co- My kind attribute equals "secret". So if that attribute equals "secret", this whole policy doesn't apply. So that's just a really
quick walkthrough of Cedar. Now we're gonna do a really quick demo of what this looks like. Alright, so I wanna
show you a few policies that I've written here ahead of time. So, and then we're gonna walk through and kind of see how this works. So the first policy I've written
is a authorization policy. It allows a principal
that's a Kubernetes user to do an action. And so that act, the actions
that it can do are create, and these are just Kubernetes
verbs, create, list, watch, update, patch, and delete. And then the resources it can act on are Kubernetes resources. So if you've ever, again, if you've ever written an RBAC policy, there's non-resource URLs like metrics, liveness checks, and
then there's resources. So any secret pod, config map,
CRD, those are all resources. So we're gonna say, okay,
this acts on resources. But this only applies
when the principal name is sample user. The resource being acted
on is a namespace resource. So this excludes resources
that don't have a namespace like node, validating
admission configuration, a number of other Kubernetes types. The namespace name is default. The API group is empty,
which is the core API group where pods, config maps and
everything live and Kubernetes. And the API resource is config map. So we're gonna allow the sample user to basically do all these
verbs on config map. So that's our authorization policy. This looks sort of similar
to what you could actually do almost all of this in RBAC, right? It's permit, so it's not a forbid, and all of these expressions
could be modeled in RBAC. Now we're gonna do something
a little bit different. So we're gonna add a second
policy that's a forbid clause. We're gonna forbid users that are in the group requires labels. So Kubernetes users are in groups. They are forbidden from
listing and watching any Kubernetes resource, unless the request has a label selector. So if you've ever listed
Kubernetes resources like pods, or any other resource, you
can do with Kube Cuddle. Kube cuddle dash L for a label selector. Key equals value. You can specify keys and values. So in this example, we're
gonna forbid all requests, unless there's a label
selector where key owner equals the requester's name. This is something you can't do in RBAC. This is attribute based access control. So we've now restricted some of those verbs that we saw above. The next policy is not just
Kubernetes authorization, but Kubernetes admission. So Kubernetes admission is
another part of Kubernetes where you can restrict
mutations to resources. So creates, deletes, updates. So again, we're gonna apply this to users in the requires label group. They are forbidden from creating, updating or deleting any resource, period. Unless that resource has metadata. That metadata, so if you've ever configured
a Kubernetes resource, it has metadata object in
the object meta and labels. And one of those labels is
"owner is principal name". So you can no longer,
we're gonna forbid users and requires labels from
creating any, or updating, or deleting any resource
unless they're the owner of it. And then finally, we're gonna
do a similar forbid on update, but we're gonna prevent overriding. So when you get an admission
request for an update, you get two resources. You get the new state and the old state. We don't wanna let someone
overwrite a resource that they didn't already own. So we're gonna forbid, if the old object metadata
didn't have owner is name, we're gonna forbid that. Okay? So that's our policy. So I've already created this in a local Kubernetes
and docker kind cluster, and we're gonna walk through
what that actually looks like. Okay, so I have a kube config
here that I've written, that is a sample user. And I'm using the Kubernetes
client call Kube cuddle off, who am I? And this is just gonna return
back, "What user are you?" What groups are you in? So I'm the sample user, I'm
in the group sample group, requires labels that we saw in our policy, and a system authenticated. I wanna as admin, so I'm the
admin of the the cluster, not as that other kube config. I wanna create a config map
just for display purposes here. Okay, so I created a config
map called "other config". It is gonna have the,
just the key and value foo bar, right? It doesn't need any data. We're gonna label that
config map we just created with the owner, some user. So not our sample user,
just some other user. Now we're gonna just get config maps that exist and show their labels. So there's three. There's kube root CA that's already there. That's created
automatically by Kubernetes, it doesn't have any labels. We have this other config
owned by some user. We have this test config
owned by the name default. Okay? So none of these are
owned by our sample user. As our sample user, if we
try to kube cuddle get CM or config map, we're
gonna get a forbidden. And we're not only gonna get
a forbid, we're gonna see what policy denied that request. So you can see here that the policy label
enforcement policy one on line 21 column one forbid this request. So I now know, okay, I'm forbidden, and I know which policy
forbid me from doing this. If I wanna try to label, so
I wanna update an existing, that other config, and add
the stage equals test label, I'm gonna get forbidden from
that because I don't own it. If I want to create a config
map as my sample user, and I try to do that, again from literal where K one equals V one, but I don't have any label
on this config map I'm trying to create, again, I'm gonna get denied. This is a admission denial. You can see admission webhook denied this. So, so far this is pretty effective. So what if we, how do we actually
do something as this user? Okay, so here's a sample config map. I have it locally in a file
called "sample-config". Notice that it has a label, and the label is owner equals sample user. It just has some dummy
data of stage equal test. So what happens if we
actually try to create this as the sample user? Okay, let's try it. It succeeds. This is great, right? This is what we actually want. And then as the sample user,
if we wanna list config maps, so get config maps with a label selector, remember we tried it before
without a label selector. We do it with a label
selector, it succeeds, but we can only see the one we own. We can't see any else. So that's our short demo here. The few things to note
about Cedar is that Cedar is really at this point a prototype. We wanna hear more from you. If you would like this
integrated in into EKS, we would love to hear about it. You can go ahead, download it, try it out. It's all open source. And yeah, again, we would love to hear what you like, what you don't like, what you'd like to see about this. But for now, this is
an open source project that we're really excited about, and wanna get more
information on from you. Finally, a few resources. As we mentioned throughout the talk, we have an EKS best practices guide. This is on the AWS documentation. There's a QR code here. So you can really read more
about these best practices that we've mentioned here, as well as just Kubernetes specific ones that aren't specific to AWS or EKS, but just Kubernetes in general. We have the EKS workshop,
which is a great guided tour of, if you're new to
Kubernetes, new to EKS, and you wanna learn how
to create an EKS cluster, it's a great guided tour
of creating a cluster, configuring it, installing
applications on it, like monitoring stacks, and other add-ons. It's really, really helpful. And then also we have EKS
blueprints that we provide. These are sample
configurations for Terraform and AWS CDK to help
you get up and running, and started very quickly with EKS. Finally, we also have a public roadmap. So if you go to GitHub
on the AWS organization, the containers roadmap,
there's a link here. You can see a list of
feature requests by by users, or issues that we've opened to say, hey, this is something we're thinking about, we want user feedback on,
you can upvote features that you want in EKS there, or
tell us about your use case. We want to hear about it. There's one for Cedar
integration into EKS. So if you want, if you like
that, if you want that, plus one that, but you can
also subscribe to updates. So you'll get notified when
features are in development, or when they actually ship. We use this actually. Our product managers use this
all the time to gauge, okay, what's the most popular issue? You could all go see it. You can sort by plus ones to see what's the most requested feature for EKS? And with that, thank you,
appreciate your time today. George and I'll be
available after the talk for Q and A outside. Thank you, and have a
great week at re:Invent. - Thank you. (crowd clapping)

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1s) - Hey everyone, my name is Micah Hausler.

[00:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=4s) You are at Kube 315:
Securing Kubernetes Workloads

[00:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=7s) in Amazon EKS.

[00:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=8s) I'm a principal software engineer at AWS.

[00:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=11s) I work on Kubernetes, Kubernetes security,

[00:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=14s) I've contribute to upstream Kubernetes,

[00:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=17s) I'm on the Kubernetes security committee,

[00:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=19s) so we take in security
reports and evaluate them,

[00:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=22s) and then issue fixes Kubernetes.

[00:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=24s) - And I'm George John.

[00:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=25s) I'm a product manager
with Amazon EKS team.

[00:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=29s) I'm very excited to be here,

[00:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=30s) and thank you all for taking
the time to join us today.

[00:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=35s) - Am I on?

[00:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=37s) Sure.

[00:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=38s) - Oh, okay.
- [Micah] Great.

[00:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=40s) - So for today's session,

[00:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=41s) we thought we'll take
a different approach.

[00:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=44s) We are gonna look at how you
can secure your workloads

[00:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=47s) running in Amazon EKS from
a few different layers.

[00:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=50s) So first, we'll take a
look at the big picture.

[00:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=52s) We look at the controls that are available

[00:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=54s) to you at a cluster level.

[00:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=56s) So we look at what are,

[00:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=57s) how you can secure
access into the cluster,

[01:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=60s) we look at how you can assign permissions

[01:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=62s) to applications running in the cluster

[01:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=64s) so it can access AWS resources outside.

[01:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=66s) So things like S3 Bucket, DynamoDB,

[01:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=69s) how you can securely set that up,

[01:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=71s) and finally, in the
first section, we look at

[01:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=72s) how you can use the various AWS services

[01:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=75s) in the security space,

[01:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=76s) and how those integrate with Amazon EKS.

[01:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=80s) And then we'll dive a little bit deeper,

[01:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=83s) we'll go into the infrastructure layer.

[01:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=85s) So by infrastructure here, I'm referring

[01:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=87s) to the EC2 instances, the working notes

[01:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=90s) that you run in the cluster.

[01:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=93s) And we'll also look at the,
some of the networking VPC,

[01:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=95s) and what are the controls and
mechanisms available for you

[01:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=97s) to secure the infrastructure layer.

[01:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=100s) And then finally, we'll jump
into the application layer.

[01:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=102s) We'll talk about the best
practices, some of the controls

[01:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=105s) to secure your images and pods

[01:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=107s) that make up your application.

[01:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=110s) So one thing I wanna call out
is that, in today's session,

[01:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=112s) our focus is really on
EKS and AWS controls

[01:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=116s) and capabilities that
are available to you.

[01:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=118s) But at the end of the session,
we'll share a resource,

[02:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=120s) namely the EKS Best Practices Guide

[02:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=123s) that talks about the
Kubernetes capabilities

[02:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=125s) and tools that are available so

[02:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=127s) that you get the full picture in terms of

[02:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=129s) how you can secure or cluster.

[02:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=132s) So with that, let's get started.

[02:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=135s) So over the last few years,

[02:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=137s) we have seen a massive uptick
in adoption of Kubernetes.

[02:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=141s) As per the 2023 Cloud Native
Computing Foundation's

[02:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=144s) annual survey, 84% of the
respondents are using Kubernetes,

[02:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=148s) either in production, or evaluating it.

[02:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=152s) And this is something we
are seeing at Amazon EKS.

[02:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=154s) Every year, we have customers
running tens of millions

[02:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=158s) of clusters,

[02:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=159s) and this number keeps growing.

[02:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=162s) And when we launched
EKS over six years ago,

[02:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=166s) it was really in response
to customer feedback

[02:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=168s) that managing Kubernetes at scale is hard.

[02:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=171s) You know, customers were spending
a lot of time monitoring,

[02:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=174s) scaling, managing the
Kubernetes control plane,

[02:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=177s) and they want something, they
want a native to integrate

[02:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=179s) with various AWS services.

[03:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=183s) And since then,

[03:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=187s) EKS has emerged as a
most trusted way for you

[03:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=190s) to run Kubernetes in AWS.

[03:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=193s) Now we remove the
undifferentiated heavy lifting

[03:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=195s) of not just managing the
Kubernetes control plane,

[03:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=198s) but VARIOUS aspects of the cluster.

[03:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=202s) For AWS and EKS, security
is the highest priority.

[03:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=207s) Now when we, as always,
operating securely in the cloud

[03:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=211s) is a shared responsibility.

[03:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=214s) AWS takes responsibility for
the security of the cloud,

[03:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=217s) and you as a customer takes responsibility

[03:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=219s) for security in the cloud.

[03:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=221s) So here you can see at the bottom,

[03:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=223s) three layers are all
managed by AWS and EKS.

[03:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=227s) So things like the Kubernetes
clusters control plane,

[03:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=230s) the infrastructure it runs on,
the regions, the local zones,

[03:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=233s) some of the foundational services,

[03:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=235s) the control plane leverages,

[03:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=236s) like the compute storage networking,

[03:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=238s) and the actual Kubernetes
bits, like the API server

[04:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=241s) that runs in the control
plane, that CD database.

[04:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=244s) All that is our responsibility.

[04:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=246s) We patch, we scale, we manage,

[04:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=248s) we make sure it's available and resilient.

[04:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=250s) And the layers about it are
really the EC2 instances

[04:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=253s) and the worker nodes that run in your VPC.

[04:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=256s) Things like, whether the operating system

[04:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=259s) that runs on the EC2,
whether it's patched,

[04:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=261s) whether it's monitored,
whether you're looking

[04:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=262s) at the health of it.

[04:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=264s) Some of the cluster
capabilities like auto scaling,

[04:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=266s) and even the Kubernetes
pieces that, the binaries

[04:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=268s) that run on the worker
node, like the kubelet,

[04:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=271s) or the container runtime.

[04:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=272s) All that is your responsibility.

[04:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=275s) But AWS and EKS offers
you various tools like,

[04:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=278s) there are multiple capabilities
like security groups

[04:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=280s) on pods, subnets, private
endpoint access, EKS add-ons,

[04:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=284s) EKS-optimized AMI's, all of
which will make it easy for you

[04:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=287s) to secure your data plane, your VPC,

[04:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=290s) and the things that run there,

[04:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=291s) but at the end of the day,
it's still your responsibility.

[04:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=295s) Now that we have covered
some of the basics,

[04:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=296s) let's jump into the first layer.

[04:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=298s) So first we look at, like I said,

[04:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=299s) the cluster level controls.

[05:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=302s) When we launched EKS, we wanted

[05:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=305s) to offer a Kubernetes native wave

[05:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=307s) for authenticating into the cluster.

[05:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=310s) So what we did is,

[05:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=311s) we have this config map called AWS-AUTH,

[05:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=314s) where you can define the
mapping of IM principals

[05:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=316s) to Kubernetes permissions.

[05:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=319s) Now this approach had some trade-offs.

[05:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=321s) You know, on one hand it is good

[05:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=323s) because you can use IAM, you don't need

[05:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=325s) to maintain a separate identity provider,

[05:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=327s) and you get all the benefits of IAM,

[05:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=329s) like multi-factor authentication,

[05:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=331s) the auditing with
CloudTrail logs, and so on.

[05:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=335s) But on the other hand, now you had to deal

[05:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=337s) with different set of APIs
to create an EKS cluster

[05:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=340s) with all the permissions.

[05:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=342s) For example, you would use EKS
APIs to create the cluster,

[05:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=346s) and then you have to
move to Kubernetes APIs

[05:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=348s) to provision the mapping
and set up the config map.

[05:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=351s) This meant that automating,

[05:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=353s) or using infrastructure as code
tools to bootstrap a cluster

[05:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=357s) with the required permissions is hard.

[05:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=359s) Another challenge with the
config map experience was,

[06:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=363s) it was a little bit brittle.

[06:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=364s) Like if you make a typo in the config map,

[06:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=367s) or you don't follow
the exact format there,

[06:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=370s) you could accidentally
lock your users out.

[06:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=372s) And there were behaviors like,

[06:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=374s) when you create the IAM
identity that is used

[06:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=377s) to create the EKS cluster,

[06:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=379s) automatically gets super user access.

[06:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=381s) Now this was something which,

[06:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=382s) was behavior which many
customers didn't like.

[06:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=385s) So to address these, soon
after re:Invent last year,

[06:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=389s) so Mike and I were on stage
last year, we talked about it

[06:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=391s) as something that's coming out.

[06:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=393s) It came out as a feature
soon after re:Invent,

[06:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=396s) called Cluster Access Management.

[06:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=398s) What Cluster Access Management does is

[06:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=399s) that it kind of unifies the APIs.

[06:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=401s) So no longer you're switching

[06:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=403s) between EKS and Kubernetes APIs.

[06:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=404s) Instead, you can just use EKS
APIs to create the cluster,

[06:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=407s) set up the permissions, you
have cluster ready to go.

[06:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=410s) And it simplified the configuration,

[06:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=412s) so users and other AWS
services that needed access

[06:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=415s) to the EKS, the whole setup
was much more simpler now.

[06:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=419s) And finally, it gave you granular control.

[07:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=422s) So, if you remember the
scenario I mentioned before,

[07:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=424s) now with Cluster Access
management, you are able

[07:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=426s) to revoke the permissions
granted automatically

[07:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=429s) to the IAM principal
that creates a cluster.

[07:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=434s) There is a link to the blog at the bottom.

[07:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=436s) If you are interested in
learning more about it,

[07:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=438s) please take a look.

[07:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=439s) We strongly encourage you

[07:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=441s) to take a look at Cluster
Access Management.

[07:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=444s) For EKS, that is the future,
that is where we are heading.

[07:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=446s) All the new features, all the
capabilities will be built

[07:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=448s) on Cluster Access Management.

[07:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=450s) And if you have an existing cluster

[07:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=452s) that's using the older
AWS-AUTH config map,

[07:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=455s) we strongly encourage you to move.

[07:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=457s) There is a simple, easy way
to migrate from one to the...

[07:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=461s) From config map to
Cluster Access Management.

[07:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=467s) Let's look at the actual
flow behind the scenes.

[07:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=470s) So first, you would be integrating with...

[07:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=472s) Or interfacing with IAM to
create the IAM principal,

[07:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=475s) whether it's a role or user.

[07:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=477s) And then you would be
interfacing with the new APIs

[08:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=481s) that were introduced
as part of the feature.

[08:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=483s) The same functionality is
also available on the console.

[08:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=486s) So you can either use EKS
console, or you can use the APIs,

[08:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=489s) and then you would be
creating two main entities.

[08:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=491s) First one is access entry.

[08:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=493s) So access entry would
associate with the IAM identity

[08:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=496s) you created in the previous step,

[08:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=498s) and then you create an access policy

[08:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=500s) and define, use access policy
to specify the permissions

[08:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=503s) that the access entry has.

[08:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=506s) So once the first two steps are done,

[08:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=507s) you have pretty much set up the feature.

[08:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=509s) The Cluster Access Management feature.

[08:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=511s) And then let's say you
have a user who's trying

[08:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=513s) to access the API server.

[08:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=516s) What happens is implicitly,
AWS STS is called,

[08:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=519s) either by IAM Authenticator,
or the CLI get token operation.

[08:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=523s) And when the request
lands in the control plane

[08:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=525s) on the API server, we have a web hook

[08:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=527s) which intercepts the request,
looks at the STS token,

[08:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=530s) tries to find the user identity
associated with the token,

[08:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=534s) and then if it doesn't
matching with the access entry,

[08:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=536s) if that succeeds,
authentication is complete.

[08:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=539s) The next is authorization.

[09:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=541s) For authorization, there
is a series of authorizers

[09:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=543s) that we look at, and then
if the user identity maps

[09:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=546s) with the access entry and access policy,

[09:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=549s) the authorization is also allowed,

[09:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=551s) and then the request can flow In.

[09:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=556s) Cluster access management
is available both

[09:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=558s) through APIs and console, so
you have the flexibility there.

[09:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=564s) Alright, so the first
part I talked about is

[09:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=566s) how can you set up
access into the cluster?

[09:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=569s) Now we will move on to,

[09:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=570s) you have an application
running in the cluster,

[09:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=572s) most likely you might need
to access an AWS resource,

[09:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=575s) and you could have a
Kubernetes application

[09:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=577s) that need to access S3 bucket.

[09:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=579s) It could be DynamoDB table,
it could be any AWS resource.

[09:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=581s) How do you make sure you
assign the right permissions

[09:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=583s) to the application?

[09:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=586s) So one option we had previously,
and it's still available,

[09:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=589s) is called IAM Roles For Service Account.

[09:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=592s) In short, it's called IRSA.

[09:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=594s) So we launched IRSA in 2019.

[09:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=596s) IRSA enabled you to grant
granular AWS permissions to pods.

[10:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=601s) So you could have multiple pods belonging

[10:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=603s) to multiple applications all running

[10:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=605s) on the same EC2 instance,

[10:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=606s) but have effectively
different set of permissions.

[10:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=609s) Now this was launched
in 2019, like I said,

[10:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=612s) and our goal was to make sure IRSA works

[10:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=615s) across the different
Kubernetes deployment models

[10:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=617s) we support in AWS.

[10:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=619s) So we wanted IRSA to work
with EKS, manage those

[10:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=622s) in the cloud, EKS Anywhere, self-managed,

[10:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=625s) Kubernetes clusters on EC2
instance, Red Hat, OpenShift,

[10:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=629s) service for AWS.

[10:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=630s) ROSA in short.

[10:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=631s) So we build IRSA by not
taking a direct dependency

[10:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=635s) on any of the EKS APIs.

[10:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=636s) We leveraged some of the
foundational services like IAM,

[10:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=639s) but that had some trade-offs.

[10:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=641s) One was, now that we are
depending on IAM for IRSA,

[10:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=645s) you had to create an
IAM, or OIDC provider.

[10:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=649s) Now this was a privilege operation.

[10:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=651s) We heard from some customers,
especially customers

[10:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=653s) in regulated regulated industries,

[10:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=655s) that the cluster administrator
doesn't have IAM permissions.

[10:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=659s) So now it means that the
cluster administrator has

[11:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=663s) to reach out to identity...

[11:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=664s) Sorry, IAM administrator.

[11:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=666s) There's a lot of back
and forth to set up IRSA,

[11:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=668s) which was not really user friendly.

[11:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=671s) The other one was the scoping.

[11:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=673s) So when you create, when you use a role,

[11:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=674s) or when you create a role for use in IRSA,

[11:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=678s) you typically have to bound that role,

[11:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=679s) or specify, what are the clusters

[11:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=681s) that can assume this role?

[11:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=683s) Now it means that if you wanna use a role

[11:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=685s) in a new cluster later on, you
have to go back to IAM role,

[11:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=688s) keep updating the trust policy,

[11:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=690s) or if you wanna rework
a role from a cluster,

[11:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=693s) you have to go back to
the roles trust policy

[11:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=694s) and keep playing with it.

[11:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=696s) And finally, there are some
limitations in terms of

[11:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=698s) how many clusters can a role be used with.

[11:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=702s) And to address these,
at re:Invent last year,

[11:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=705s) we launched the feature
called Pod Identity.

[11:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=707s) So Pod Identity simplifies trust.

[11:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=710s) Pod Identity enables you to create a role

[11:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=713s) that can be assumed by
EKS service as a whole.

[11:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=717s) So previously, when you create a role,

[11:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=719s) you specify the clusters
that it could assume,

[12:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=722s) and now with Pod Identity,
you can just specify

[12:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=723s) that AWS service can assume it.

[12:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=726s) So it doesn't matter which
cluster you're using,

[12:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=728s) but you also have the ability
if you wanna lock it down

[12:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=730s) to a few clusters, you
have that ability as well.

[12:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=733s) It offers new capabilities

[12:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=736s) like attribute based access control

[12:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=738s) by supporting IAM role session tags,

[12:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=741s) so it enables reuse of policies
and roles across clusters.

[12:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=744s) And finally, you are able
to now create clusters

[12:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=747s) with all the required
permissions in one go.

[12:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=751s) And there is a link to
a blog at the bottom

[12:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=753s) if you are interested in
learning more about Pod Identity.

[12:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=756s) So one thing I wanna emphasize is that,

[12:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=758s) like I said, Cluster Access
Management is the future

[12:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=761s) for the previous talk, the
first part of this talk,

[12:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=764s) I said AWS-AUTH config map is older way,

[12:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=767s) but here, IRSA is not the older way.

[12:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=769s) We will support both.

[12:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=770s) We have no plans to deprecate IRSA.

[12:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=773s) IRSA would continue to exist
along with Pod Identity.

[12:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=776s) Pod Identity is purpose
built for EKS managed service

[12:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=779s) in the cloud.

[13:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=780s) It doesn't work with EKS Anywhere,

[13:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=782s) or self-managed Kubernetes
clusters on EC2.

[13:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=786s) So it's all about giving you more options.

[13:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=788s) Depending on your use case and needs,

[13:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=790s) you can pick the solution
that best fits your needs.

[13:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=795s) Alright, let's look at the flow.

[13:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=797s) For Pod Identity, a prerequisite is

[13:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=798s) that you need to run
the Pod Identity agent,

[13:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=801s) as a (indistinct).

[13:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=802s) So it needs to be run, be
running on all worker nodes.

[13:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=805s) So here, let's take a
very simple scenario.

[13:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=807s) Let's say you wanna deploy an application

[13:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=810s) to your cluster that needs
to access an S3 bucket.

[13:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=812s) It could be any AWS resource,

[13:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=813s) I'm just using S3 as
a simple example here.

[13:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=816s) The first thing is, you
would be interfacing with,

[13:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=818s) or using IAM to create an IAM role.

[13:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=821s) An IAM role has two
parts: a permission policy

[13:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=823s) and a trust policy.

[13:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=825s) A permission policy is
where you're specifying,

[13:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=827s) this can access S3.

[13:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=829s) So in our case, we want the application

[13:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=830s) to be able to access S3,

[13:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=832s) the permission policy
would have the permissions

[13:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=833s) for it to access S3.

[13:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=835s) And then you have the trust policy.

[13:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=836s) This is where Pod Identity
is different from IRSA.

[13:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=839s) The trust policy for
Pod Identity specifies

[14:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=842s) that this role can be
assumed by EKS's service.

[14:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=845s) So we have a new service
principal we introduced,

[14:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=847s) and that's a one time step.

[14:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=848s) It doesn't matter
whether this role is used

[14:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=850s) on cluster A or B, or a C in
the future, it will just work,

[14:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=854s) and it's a one time step you have to do.

[14:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=856s) And after that, what you do is you create,

[14:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=858s) use the Pod Identity APIs.

[14:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=861s) Again, you can use the
console if you want,

[14:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=863s) but there is a operation called

[14:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=865s) Create Pod Identity Association,

[14:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=867s) which is how you map the IAM role

[14:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=869s) that you previously created
with the service account.

[14:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=873s) So one good thing here is
that that service account,

[14:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=875s) the Kubernetes service
account, need not exist

[14:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=877s) at that point in time.

[14:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=879s) It can be something you
create in the future.

[14:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=881s) The good thing about that is,

[14:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=882s) if you are a cluster administrator,

[14:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=883s) you wanna set up the cluster
with all the permissions,

[14:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=886s) so when the app dev teams comes in later,

[14:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=888s) that cluster is ready to go for them,

[14:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=890s) you can pre-create the
Pod Identity Association

[14:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=892s) with all the mappings ahead of time.

[14:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=896s) Now these are the two things you do

[14:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=898s) to set up Pod Identity.

[15:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=901s) The feature.

[15:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=902s) And then let's say later on,

[15:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=903s) you have app dev team is
deploying their application,

[15:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=906s) a pod is spun up.

[15:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=908s) When we detect that this
pod has a service account

[15:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=912s) associated with it, which
was previously mapped

[15:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=914s) through the Pod Identity
Association, we have a web hook

[15:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=917s) that intercepts a request,
and will mutate the pod spec.

[15:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=920s) And we'll add couple of
environment variables,

[15:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=923s) well known environment
variables to the pod spec.

[15:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=925s) So when AWS SDK comes up,

[15:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=928s) it knows these environment variables.

[15:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=930s) It would mount these,

[15:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=932s) it would fetch the service account token

[15:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=934s) that's mounted to the pod.

[15:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=936s) It'll make a call to
the Pod Identity agent,

[15:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=938s) pass the token, the service account token.

[15:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=940s) And then the Pod Identity agent
would then call assumed role

[15:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=944s) for Pod Identity, which is a
new API we introduced as part

[15:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=946s) of the Pod Identity API.

[15:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=948s) And this API would then validate
the service account token

[15:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=951s) that was passed.

[15:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=952s) If it is validated, it returns
a temporary AWS credential,

[15:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=955s) which is then injected into the pod.

[15:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=959s) And then the application
can use that AWS credential

[16:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=961s) to access S3.

[16:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=966s) All right, so what's new in Pod Identity

[16:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=968s) since the launch at re:Invent last year?

[16:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=971s) Pod Identity is now available
in all commercial AWS regions,

[16:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=975s) and China, as well as
the US GovCloud regions.

[16:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=978s) We open source the agent itself.

[16:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=980s) So when we launched, it was
only available as an EKS add-on.

[16:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=984s) We got feedback from customers
that they wanna deploy it

[16:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=986s) as a helm shot, or wanna
bake it into their own AMI

[16:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=989s) and create a custom AMI.

[16:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=990s) So the agent is now open sourced.

[16:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=993s) And the last one is, we introduced
support for Pod Identity

[16:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=996s) and EKS add-ons.

[16:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=998s) So add-ons are operational software

[16:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=999s) that you can run in the cluster.

[16:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1001s) And these software
usually needs permissions,

[16:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1004s) AWS permissions to access AWS resources.

[16:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1006s) Previously, the only way
you could set that up was

[16:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1008s) through IRSA, but now Pod
Identity is also available,

[16:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1011s) which greatly simplifies
the add-on setup experience.

[16:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1018s) Alright, so now let's move
on to some of the controls

[17:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1021s) that are available for you to
identify an alert on issues.

[17:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1024s) The first thing is looking
at the access, the requests

[17:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1027s) that are coming into
the API server itself.

[17:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1029s) So when you create an EKS cluster,

[17:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1031s) you get a cluster endpoint,

[17:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1033s) which is basically the API server

[17:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1035s) that's running in the control plane.

[17:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1037s) All the requests coming into
the API server are logged

[17:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1040s) in the control plane audit log,

[17:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1042s) and they are made available in CloudWatch.

[17:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1045s) This is an opt-in, or
something you have to enable.

[17:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1048s) But once you enable control plane logging,

[17:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1051s) the logs will automatically
flow to CloudWatch.

[17:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1053s) Now it being in CloudWatch means

[17:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1055s) that you can use things
like CloudWatch log inside

[17:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1057s) to further analyze it.

[17:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1059s) At the end of the presentation,

[17:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1061s) we'll share the security best practices.

[17:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1063s) Within that, there's a section
called Detective Controls,

[17:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1065s) and there are some pre-built
CloudWatch log insights

[17:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1067s) (indistinct) we have found to be useful.

[17:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1068s) So that is something you
wanna probably take a look at

[17:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1071s) after the presentation.

[17:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1074s) The other benefit of it
being in CloudWatch is

[17:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1076s) that you can set up alarms.

[17:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1077s) So if you wanna detect
increase in 403 forbidden

[18:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1082s) or unauthorized access, you're now able

[18:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1084s) to kind of alert yourself
to those situations.

[18:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1089s) Alright, so next one is,

[18:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1090s) so previously we looked
at, looking at the requests

[18:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1092s) that are coming into the API
server endpoint of the cluster.

[18:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1095s) This is about looking at the requests

[18:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1097s) that are coming into the EKS API.

[18:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1099s) So here, EKS API is, the EKS
service APIs that you use

[18:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1103s) to create cluster delete,
cluster update, cluster, all

[18:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1106s) of those EKS APIs, not Kubernetes APIs.

[18:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1109s) All of those are logged in CloudTrail,

[18:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1110s) and along with CloudTrail
logs and CloudTrail insights,

[18:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1113s) you're able to analyze them.

[18:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1115s) And finally, we have Amazon detective.

[18:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1117s) So all VPC flow logs, if you wanna analyze

[18:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1120s) or visualize them, you
can use Amazon detective,

[18:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1122s) which is integrated with EKS.

[18:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1127s) Next is encryption.

[18:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1129s) So with some of the
native AWS storage options

[18:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1132s) like EBS, EFS, FSx for luster,

[18:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1135s) is supported in EKS.

[18:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1138s) You can encrypt at rest with
either AWS managed keys,

[19:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1142s) or you can bring your own keys.

[19:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1144s) Along with that, some of the
secret sensitive information

[19:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1148s) that's stored in the Kubernetes
cluster is typically stored

[19:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1150s) in the Kubernetes secretS object.

[19:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1152s) EKS gives you the ability to
encrypt a secret subject either

[19:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1156s) with a key that is the AWS
Key Management Service office,

[19:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1160s) or you can bring your own key to KMS,

[19:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1162s) and then use that to encrypt it.

[19:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1164s) And with the keys being in
KMS, you get the ability,

[19:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1167s) you get the benefit of automatic
rotation offered by KMS.

[19:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1174s) So what are some of the
other cluster scoped controls

[19:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1176s) that are available to you?

[19:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1177s) The first one is the
Kubernetes cluster endpoint.

[19:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1180s) So here by, when I say
Kubernetes cluster endpoint,

[19:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1182s) I'm referring to the API server endpoint

[19:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1184s) that's available in every cluster.

[19:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1186s) By default, it's in a public mode, meaning

[19:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1188s) that any traffic
originating from your VPC,

[19:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1191s) if it has to reach out to the API server.

[19:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1192s) Let's say your worker
nodes need to reach out

[19:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1194s) to the API server.

[19:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1195s) The traffic leaves the VPC,

[19:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1197s) it remains an Amazon network,

[19:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1198s) and then comes back to the API server.

[20:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1200s) But if you, let's say you wanna
make it completely private

[20:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1202s) so that traffic always remains in VPC,

[20:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1204s) you have the option to
configure the endpoint

[20:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1207s) to be in a private mode.

[20:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1209s) The next one is the other
API, which is the EKS APIs.

[20:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1214s) So today, again, if you have a need

[20:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1216s) where any traffic originating
from your VPC should hit

[20:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1219s) the EKS APIs through a private endpoint,

[20:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1223s) or in a private manner, there
is AWS private link that,

[20:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1226s) this feature I think we
launched a year or so ago.

[20:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1229s) So you can leverage AWS
private link with EKS service

[20:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1232s) to kind of get that private connectivity.

[20:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1236s) The next one is use manage
components whenever you can.

[20:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1239s) So EKS add-ons, EKS Optimized
Amazon Machine Images,

[20:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1244s) or AMIs.

[20:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1244s) These are something we
take responsibility for.

[20:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1247s) We always are looking for issues.

[20:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1250s) If there are vulnerabilities,
it is on us to go patch it,

[20:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1253s) and make a new version available.

[20:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1255s) And then there are APIs
that you can leverage

[20:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1257s) to apply those to your cluster.

[20:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1258s) So when possible, you
leverage managed components.

[21:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1261s) The last one here is using security hub

[21:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1263s) for scanning your cluster.

[21:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1265s) Security hubs has, I think
around eight predefined checks

[21:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1270s) to look at the security
state of your cluster.

[21:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1273s) So, you know, that is
something you can also look

[21:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1275s) to get an idea of how your cluster is

[21:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1277s) from a security standpoint.

[21:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1281s) Alright, with that, let me invite Micah.

[21:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1283s) - Thanks George.

[21:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1285s) So next, the next section is

[21:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1287s) around infrastructure
scoped security controls.

[21:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1289s) So, as George talked about,

[21:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1291s) we kind of are separating
cluster from from infrastructure.

[21:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1294s) So by infrastructure, we really mean

[21:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1296s) where does your containers run?

[21:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1299s) And the first thing that
we're really excited

[21:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1301s) to talk about is EKS Auto Mode.

[21:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1303s) This was just launched yesterday,

[21:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1304s) so you're getting the fresh stuff.

[21:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1307s) EKS Auto Mode is a new
feature of EKS that helps you

[21:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1311s) to automate your entire
Kubernetes cluster infrastructure.

[21:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1316s) So with Auto Mode, AWS
takes responsibility

[22:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1321s) for creating and deploying nodes.

[22:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1323s) You only have to create your pods.

[22:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1326s) What this really allows you
to do is improve performance,

[22:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1329s) and optimize resources.

[22:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1332s) Using Carpenter, which
is an open source project

[22:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1334s) that we created, we manage
that completely for you,

[22:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1337s) and we will create the
nodes that are required

[22:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1340s) for the pods you define.

[22:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1341s) If you define a pod that
requires X amount of memory,

[22:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1344s) Y amount of CPU in a specific AWS zone,

[22:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1347s) we'll create it there.

[22:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1348s) Similarly, as you scale up a,
say a Kubernetes deployment

[22:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1352s) and add more replicas, we
will create the best type

[22:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1356s) of EC2 node for you.

[22:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1358s) Similarly, we will also consolidate

[22:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1360s) and find the best type of nodes

[22:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1362s) for the workloads that you have running.

[22:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1365s) This really simplifies the
management of your cluster.

[22:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1367s) You don't have to think
about creating a node group,

[22:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1370s) which zones do you wanna create it in?

[22:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1371s) You just have to use the Kubernetes API

[22:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1373s) to create a configuration
for EKS Auto Mode.

[22:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1377s) And also this really reduces

[22:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1379s) the operational overhead required.

[23:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1381s) You don't have to think about
updating the machine images

[23:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1384s) that AWS is responsible for creating

[23:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1387s) and making available to
you, you just use the nodes.

[23:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1390s) Nodes have a max lifetime of 21 days,

[23:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1393s) so even if you have a workload

[23:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1396s) that's running more than 21 days,

[23:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1398s) that node will get
recycled, and gracefully,

[23:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1401s) your application will get recreated

[23:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1402s) onto another node that's the
latest Amazon machine image,

[23:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1406s) with the latest security patches,

[23:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1407s) and so it's always up to date.

[23:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1412s) This really helps you
increase your own agility,

[23:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1415s) and accelerate your own innovation

[23:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1417s) because you're not having
to spend time trying

[23:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1419s) to keep all your nodes up to date.

[23:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1422s) You really get to offload all

[23:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1423s) of these offer operations to AWS.

[23:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1427s) This also just really helps
you improve the performance

[23:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1431s) and availability of your application.

[23:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1433s) As I said before, it's graceful restarts.

[23:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1435s) Graceful migration of of nodes.

[23:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1437s) So you don't have to think about what sort

[24:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1442s) of scaling policies you have to apply

[24:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1443s) to an auto scaling group.

[24:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1444s) This will do it for you.

[24:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1447s) And finally, this really
does help you optimize costs

[24:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1450s) by automating the capacity
planning and dynamic scaling.

[24:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1453s) You don't have to go say,
okay, what kind of node,

[24:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1455s) what's the best type of node
that I need for my workload?

[24:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1458s) We'll determine that based on the requests

[24:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1460s) in your Kubernetes pod.

[24:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1464s) So this, as George shared earlier,

[24:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1467s) we have a shared responsibility model.

[24:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1469s) And with EKS Auto Mode,
this changes a little bit.

[24:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1473s) In the previous example, if you're using

[24:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1476s) EKS managed noDE groups,

[24:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1480s) there's more of the
responsibility that's on you.

[24:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1484s) In this model,

[24:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1486s) all that's on you is really
maintaining the security

[24:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1488s) of your containers, and
your VPC infrastructure,

[24:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1491s) and any add-ons that you install on top.

[24:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1493s) There's a number of add-ons

[24:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1494s) that are automatically
included with EKS Auto Mode.

[24:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1497s) Things like the kubelet, the
container networking interface,

[25:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1501s) the kube proxy, and some CSI drivers.

[25:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1506s) Those are automatically maintained by us.

[25:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1507s) But other add-ons, those are still on you,

[25:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1512s) but there's just a whole lot
less that you have to manage.

[25:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1517s) Another aspect to talk about in terms

[25:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1520s) of the cluster security is really

[25:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1522s) about cluster network security.

[25:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1524s) So you have applications
running on containers

[25:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1526s) and pods in your cluster, right?

[25:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1528s) There's two main configurations
that you have here.

[25:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1532s) The first is to take advantage

[25:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1534s) of Kubernetes networking policy.

[25:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1535s) So this is part of
Kubernetes as the interface,

[25:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1539s) and then powered

[25:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1539s) by the AWS VPC container
network interface or CNI plugin.

[25:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1546s) You can define rules in the
Kubernetes API that say,

[25:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1550s) I wanna let pods in this
network namespace talk

[25:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1554s) to pods in this other network namespace.

[25:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1556s) You get very granular
control over pod labels,

[25:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1559s) or even at the pod label level,

[26:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1562s) and L seven.

[26:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1564s) So, what host name, or what TCP port.

[26:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1569s) That is enforced on the host.

[26:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1571s) So it's using EBPF in the EKS VPC CNI.

[26:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1576s) Other, if you're using
a different CNI plugin

[26:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1578s) with a different enforcement layer

[26:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1580s) that might be using a
different technology.

[26:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1583s) But that's enforced on the host.

[26:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1586s) The other method is with security groups.

[26:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1588s) So these are the same security
groups you know and love,

[26:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1590s) with EC2, but they can be
applied to your Kubernetes pods.

[26:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1594s) So each pod in Kubernetes

[26:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1596s) that uses an elastic network interface,

[26:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1598s) or an ENI that gets attached
to your EC2 instance,

[26:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1602s) and EC2 security group per
pod attaches a security group

[26:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1605s) to that pod's network interface.

[26:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1607s) So this lets you use an off host mechanism

[26:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1611s) that can't be modified on
the host to control what app,

[26:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1616s) what network calls a pod can make.

[27:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1620s) And included is a link where
you can read more about that.

[27:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1626s) As George mentioned, there's
some detective controls

[27:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1628s) that you can do with CloudTrail.

[27:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1632s) Another form of detective controls more

[27:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1634s) around the infrastructure
layer are around GuardDuty.

[27:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1639s) So GuardDuty has some
really great integrations

[27:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1642s) with Amazon EKS.

[27:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1643s) The first integration that
we built with GuardDuty was

[27:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1647s) for audit log protection.

[27:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1648s) So Kubernetes has an audit log,
Kubernetes is an API server.

[27:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1652s) It emits an audit log for every request

[27:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1653s) that's made against it.

[27:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1655s) So audit log includes things
like if you create a pod,

[27:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1657s) it tells you the pod name,
which user created the pod,

[27:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1660s) other metadata about the pod.

[27:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1663s) And all this goes to a central log.

[27:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1665s) You can turn it on,
send it to your account,

[27:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1667s) but with GuardDuty, you
can also have that log sent

[27:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1669s) to GuardDuty for your cluster.

[27:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1671s) GuardDuty uses machine
learning, it also uses

[27:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1677s) quite a bit of like
rules that we've observed

[27:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1679s) from known attack patterns.

[28:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1681s) And I interface, we interface
with the GuardDuty team a lot

[28:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1685s) to say, here's new things
that are coming in Kubernetes,

[28:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1688s) here's new things we should
look for configurate,

[28:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1690s) either misconfiguration,
or attack patterns.

[28:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1692s) And so GuardDuty will send you an alert

[28:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1694s) if it detects either a
mis-configuration, if you,

[28:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1698s) say you accidentally configure anonymous,

[28:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1701s) so unauthenticated users to
the Kubernetes API as admin.

[28:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1705s) I've seen it before,
it's awful, don't do it.

[28:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1708s) But if you did it, you would get an alert

[28:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1709s) from GuardDuty saying, hey, this happened,

[28:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1712s) you should go remediate this.

[28:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1714s) And same for a bunch of
other known attack patterns.

[28:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1717s) So that's a really, really
great protection mechanism.

[28:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1721s) You can enable at your
account level to say,

[28:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1722s) I want this for all my clusters.

[28:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1724s) Second is Amazon GuardDuty's
Detective controls is

[28:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1728s) with runtime protection.

[28:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1729s) So Amazon GuardDuty also
has an agent based mode

[28:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1734s) where they will deploy
through EKS add-ons,

[28:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1737s) an agent onto every host, to
look for known attack patterns,

[29:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1741s) whether that's through
file to file changes,

[29:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1745s) or other known heuristics
on the node to look

[29:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1750s) for malicious attack patterns
that wouldn't show up

[29:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1752s) in the Kubernetes audit log,

[29:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1754s) but could be seen in,
say, the Linux audit log.

[29:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1759s) So that's another great control.

[29:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1761s) Again, you can turn that on

[29:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1762s) at the account level, or at
the AWS organizational level

[29:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1768s) for your account, to just make
it enabled on all clusters.

[29:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1773s) A few other infrastructure
scope security controls

[29:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1776s) that we just recommend for
customers, are to restrict

[29:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1780s) and minimize access to your
instances using AWS SSM.

[29:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1784s) So if you're used to spinning
up a VM, if you ever pointed

[29:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1788s) and clicked through the AWS
console your first time,

[29:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1790s) you probably used SSH right?

[29:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1792s) Everyone's sort of familiar with SSH.

[29:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1794s) Generating SSH keys, get your
(indistinct) on your instance,

[29:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1798s) and then opening a port
on your security group,

[30:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1800s) and getting an IP address, and, right?

[30:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1802s) Connecting to your host.

[30:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1805s) That is...

[30:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1806s) When you've done that, I
would not be surprised,

[30:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1808s) and you can be ashamed, it's okay,

[30:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1811s) to have set the incoming
security group rule

[30:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1813s) to allow anywhere in the world,

[30:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1815s) because I don't wanna go look up my IP.

[30:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1817s) What if I'm at home, and my IP changes?

[30:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1818s) Or if I'm at office and I
have a floating IP, right?

[30:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1821s) You might set it to the whole world.

[30:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1823s) That's not great, but you
might've done it right?

[30:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1825s) You don't wanna do that in production.

[30:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1826s) And so with AWS systems
manager, you can turn off SSH,

[30:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1831s) and enable SSM to access your hosts,

[30:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1834s) and the SSM agent connects
back to the SSM service.

[30:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1838s) And with SSM session manager,
you can log into your instance

[30:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1841s) through SSM without
needing that open port.

[30:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1844s) So it's a great security control

[30:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1846s) that's not necessarily unique to EKS,

[30:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1848s) but just a best practice
that we really recommend,

[30:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1850s) because it really can save you from having

[30:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1853s) mis-configured an open port to the world.

[30:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1855s) You just don't need to do
that for something like SSH.

[30:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1858s) There's all kinds of internet bots

[31:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1860s) and everything scanning, you know,

[31:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1861s) the global IP space looking for,

[31:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1862s) what's listening on port 22?

[31:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1864s) And you don't wanna be hit there.

[31:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1867s) Additionally, we recommend
using a container optimized OS.

[31:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1870s) So we have the Amazon EKS optimized AMIs,

[31:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1873s) those are using Amazon Linux.

[31:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1876s) And then we also have Bottle Rocket,

[31:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1877s) which using the same
kernel with Amazon Linux,

[31:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1879s) but using a more hardened container,

[31:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1881s) only container first OS.

[31:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1883s) EKS Auto Mode actually uses
Bottle Rocket under the hood.

[31:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1887s) But bottle rocket is a
much more locked down OS

[31:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1890s) that doesn't have, it's
not a general purpose OS,

[31:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1893s) it doesn't have a package manager.

[31:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1895s) So you can't keep packages up to date,

[31:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1897s) you don't have to keep
packages up to date.

[31:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1898s) You get a new...

[31:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1899s) You create a new instance
when you need a new package,

[31:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1903s) or to get a security patch.

[31:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1905s) And then finally, we also recommend

[31:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1908s) just verifying your
configuration of your cluster

[31:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1911s) using the CIS benchmark.

[31:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1912s) We have an EKS specific CIS benchmark

[31:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1915s) that lets you verify the
configuration of your cluster,

[31:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1918s) making sure you have things like,

[32:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1920s) if you don't want public access
to your cluster turned on,

[32:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1923s) you can have that turned off.

[32:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1925s) Making sure that you
have all the other APIs

[32:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1930s) that we've talked about, like
Cluster Access Management,

[32:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1932s) making sure that you're no
longer using config map mode.

[32:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1937s) You can use the CIS benchmark
with open source tools

[32:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1939s) like Kube-Bench to validate
your configuration here.

[32:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1944s) And finally, the final
section here is really

[32:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1946s) to zoom in to the application
scope security controls

[32:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1949s) of your cluster.

[32:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1951s) So, as we mentioned, pod
security is kind of one

[32:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1955s) of those things that you need
to pay attention to, right?

[32:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1957s) So one of the best mechanisms
for this is really using

[32:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1961s) either entry Kubernetes
Pod Security Standards,

[32:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1965s) or some out external pod security,

[32:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1968s) so policy-as-code solution.

[32:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1971s) There's open source
solutions like Kyverno,

[32:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1974s) or Open Policy Agent Gatekeeper,

[32:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1976s) or others out there that
help you enforce some

[32:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1979s) of your security standards as code.

[33:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1982s) Some of the best, just to
hit some highlights here,

[33:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1985s) there's a whole slew of them.

[33:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1986s) Again, we'll have a link later

[33:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1988s) to the EKS Security Best
Practices Guide with these.

[33:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1991s) But a few ones we just
really wanna call out

[33:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1993s) because these are just so critical,

[33:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1994s) is limit the privilegeD containers.

[33:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1996s) And I'm specifically using
the word "limit" here,

[33:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=1999s) because sometimes people think

[33:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2001s) they should never have
privileged containers.

[33:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2003s) And if you're not familiar
with privileged containers,

[33:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2004s) if you ever run docker command line,

[33:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2008s) you have a dash dash privilege flag.

[33:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2010s) When you run privilege, that
gives a container access

[33:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2012s) to all kinds of Linux devices,

[33:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2014s) and privilege escalations on the host,

[33:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2016s) so that can do management of the host.

[33:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2019s) Sometimes that's necessary.

[33:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2020s) So when we say limit,

[33:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2021s) we don't mean eliminate
privileged containers.

[33:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2024s) For example, the AWS VPC CNI needs

[33:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2028s) to set up network namespaces so

[33:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2030s) that pods can have their
own network on a host.

[33:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2033s) That needs to be privileged.

[33:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2034s) There are things like the,

[33:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2036s) or the CSI, the Container
Storage Interface agents

[33:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2039s) for EBS, or for EFS,

[34:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2043s) or several of the other
Amazon integrations.

[34:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2045s) Those might need to be
privileged, and that's okay.

[34:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2048s) But what we do encourage
you to do is limit that.

[34:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2051s) So if you have an application
that's serving web traffic,

[34:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2053s) probably does not need to be privileged,

[34:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2055s) so don't make that privileged.

[34:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2058s) Similarly, if you have an application

[34:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2059s) that's running on your
cluster, that is, again,

[34:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2062s) take this web serving traffic example,

[34:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2065s) that's never gonna talk
to the Kubernetes API,

[34:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2068s) disable service account token mounts.

[34:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2069s) By default, Kubernetes
mounts a token into every pod

[34:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2073s) so that it can talk to the
API server and authenticate.

[34:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2076s) It doesn't have any
permissions by default,

[34:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2078s) but it's there as an
authentication mechanism.

[34:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2080s) If you don't need it, turn it off, right?

[34:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2083s) Similarly, restrict use of host path.

[34:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2085s) It's just one of those things that,

[34:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2087s) if you don't need, turn it off.

[34:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2088s) There's all kinds of CVEs in the past,

[34:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2091s) whether that's in container
D in Kubernetes itself,

[34:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2095s) or runC, the container runtime agent,

[34:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2099s) that have centered around host mounts.

[35:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2101s) So if you don't need them, turn them off.

[35:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2104s) And then finally, just as you
build your container images,

[35:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2108s) when you define that, whether
it's in your docker file,

[35:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2110s) or however you're defining
your container image,

[35:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2113s) or actually, not in your docker file,

[35:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2115s) but actually in your pod
configuration, if your pod,

[35:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2118s) say again, we'll take
the web traffic example.

[35:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2120s) If the the pod never has to write,

[35:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2122s) or the application in your
pod never has to write

[35:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2124s) to the file system,
consider switching that

[35:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2126s) to a read-only file
system in your container.

[35:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2130s) That eliminates a whole
slew of attack vectors

[35:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2133s) that your application could
potentially be vulnerable to,

[35:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2136s) and you just don't even
have to worry about.

[35:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2140s) Another aspect that we like

[35:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2141s) to think about is just image security.

[35:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2143s) So your images that
you're running are pulling

[35:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2145s) from somewhere, probably Amazon
ECR, maybe somewhere else.

[35:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2150s) We highly, highly recommend scanning these

[35:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2152s) for vulnerabilities regularly.

[35:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2155s) So with Amazon ECR,

[35:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2156s) you can use the native
Amazon Inspector integration

[35:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2159s) and get scans of your image and reports

[36:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2163s) if there are secure security
vulnerabilities found

[36:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2165s) in your application, whether
that's in the system packages,

[36:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2170s) or there's some support for
language packages as well.

[36:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2175s) Also, when you're using
ECR, if you don't need ECR

[36:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2179s) to be coming from outside
of your VPC, you can use ECR

[36:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2182s) with private link.

[36:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2183s) You can lock down so that
your image can only come

[36:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2185s) over private link.

[36:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2186s) That's a great, great control
that we've seen customers use.

[36:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2190s) And finally, similar to
the read-only file system,

[36:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2193s) this is more of a thing that you have

[36:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2195s) to configure in your container
definition when you build it,

[36:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2199s) but configure your image
to use a non root user.

[36:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2202s) It's sort of a default if
you're ever, use a docker file

[36:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2205s) when you build, it just
uses the root user.

[36:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2208s) If you're listening, if you, again,

[36:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2209s) if you have a web container
that's listening on

[36:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2212s) whatever port it is, it
doesn't necessarily need

[36:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2214s) to be running as root.

[36:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2215s) And so you can change
that to a non root user.

[36:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2218s) That, again, just reduces
the permissions that

[37:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2220s) that Linux process has when
it runs in your cluster,

[37:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2223s) so that it has much less likelihood of,

[37:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2226s) if there's a security
event, of having permissions

[37:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2229s) to escalate and do things
that you don't want it to do.

[37:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2235s) The next part I wanna
talk about is something

[37:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2236s) that we're pretty excited about.

[37:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2237s) So this is pretty new.

[37:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2239s) So Kubernetes has built in authorization.

[37:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2241s) If you've ever used Kubernetes,

[37:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2242s) you've probably configured RBAC,

[37:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2244s) or role-based access control.

[37:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2246s) And you've probably written an
RBAC policy to allow some pod

[37:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2250s) to manage things in your cluster,

[37:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2252s) or maybe a human to manage
things in your cluster, right?

[37:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2255s) If you've ever written an RBAC pol-

[37:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2256s) How?

[37:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2257s) Quick show of hands.

[37:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2258s) How many of you have ever
written an RBAC policy?

[37:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2260s) Okay, good, good.

[37:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2260s) We got a lot of people here.

[37:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2261s) Okay, so if you've ever
written an RBAC policy,

[37:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2263s) you've probably come into some
of the limitations of this.

[37:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2266s) It's worked great in
Kubernetes for the last,

[37:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2270s) like eight years or so.

[37:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2272s) But the more and more that
we've heard from customers,

[37:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2274s) we're seeing some of the
limitations of RBAC come into play.

[37:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2277s) If you've ever written
an RBAC policy, you know

[37:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2279s) that it's allow only.

[38:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2281s) You can't do a denial.

[38:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2282s) So if you wanna allow, say
you're a platform team,

[38:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2286s) you wanna allow a developer
or group of developers

[38:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2289s) to manage some deployments in the cluster,

[38:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2290s) but you don't want them
to manage deployments

[38:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2293s) or daemon sets in the
kube system namespace.

[38:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2297s) That's becomes really painful
as a platform administrator

[38:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2301s) because you have to create a
RBAC policy in every namespace

[38:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2305s) for those developers.

[38:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2308s) If you create a Kubernetes cluster role,

[38:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2311s) you have to give it
either every permission

[38:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2313s) on every namespace, or just
specifically named namespaces.

[38:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2316s) There's no conditions.

[38:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2317s) That becomes really painful.

[38:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2320s) So there's no conditions
and there's no denials.

[38:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2322s) Cedar is a access control language

[38:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2325s) and runtime evaluation
engine that's open source,

[38:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2330s) built by AWS.

[38:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2331s) It was launched several
years ago at re:Invent.

[38:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2334s) There's also a managed service for this,

[38:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2336s) Amazon Verified Permissions.

[38:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2338s) But Cedar can be used for,

[39:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2342s) actually even your own applications.

[39:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2345s) You can define what kind
of actions can be permitted

[39:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2348s) by who, and on what resources.

[39:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2351s) So over the last few months, we've built

[39:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2353s) and then open sourced a new prototype

[39:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2357s) for re-imagined Kubernetes
authorization using Cedar.

[39:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2361s) And it's on GitHub, so
you can see the link here.

[39:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2363s) You can actually download
it and try it out.

[39:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2366s) We're gonna show a demo here in a second,

[39:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2368s) but I wanna show just kind of
quickly what this looks like.

[39:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2371s) So if you've never seen
Cedar code, that's okay.

[39:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2373s) Cedar is very, very easy to read.

[39:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2376s) Cedar policies have basically three or...

[39:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2380s) Well, three parts we'll call 'em.

[39:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2382s) You have effect.

[39:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2383s) So in this policy, this
is a contrived policy

[39:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2385s) that doesn't do anything
'cause there's not,

[39:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2388s) it's not actually used, but
just to show you kind of

[39:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2391s) what can be done with Cedar.

[39:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2392s) There's an effect, so a permit or forbid.

[39:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2394s) This is a permit policy.

[39:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2395s) Then you have the main
section of the policy

[39:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2398s) where you have principal,
action, and resource.

[40:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2400s) You define what principal
this policy applies to,

[40:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2406s) you can define what
action, or set of actions

[40:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2409s) that this policy applies to.

[40:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2410s) So I'm saying here,
principal is a custom user.

[40:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2414s) Not a specific one, but just
that's the type of principal.

[40:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2417s) The action is in the
list of "get" or "list".

[40:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2420s) So it can be either a
get or a list action.

[40:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2423s) And then the resources,
some custom resource type

[40:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2426s) that I've allowed.

[40:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2427s) But it's now has something
that you can't do

[40:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2429s) in Kubernetes RBAC.

[40:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2430s) It has a condition.

[40:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2431s) We have this when clause.

[40:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2432s) We're only gonna allow
this policy to take effect

[40:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2434s) when a principal is in a specific group.

[40:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2438s) And so we have a custom
group type we've defined,

[40:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2441s) and an identifier for that group.

[40:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2443s) So maybe it's a name.

[40:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2445s) And then one other part
to this condition is

[40:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2447s) that the resource has some field on it,

[40:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2450s) and that field must equal cool value.

[40:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2453s) And then finally, there's a
syntactic sugar called an...

[40:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2456s) That's another condition on Cedar policies

[40:59](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2459s) called an "unless" clause,

[41:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2460s) that negate when this policy applies.

[41:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2463s) It makes it a bit simpler
than having to write,

[41:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2465s) and, or, not, equals
to in your when clause.

[41:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2468s) You can just add an unless clause as well.

[41:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2471s) So we're gonna, this
policy will all take effect

[41:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2474s) with the when, unless resource dot co-

[41:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2478s) My kind attribute equals "secret".

[41:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2480s) So if that attribute equals "secret",

[41:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2482s) this whole policy doesn't apply.

[41:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2484s) So that's just a really
quick walkthrough of Cedar.

[41:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2486s) Now we're gonna do a really quick demo

[41:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2488s) of what this looks like.

[41:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2493s) Alright, so I wanna
show you a few policies

[41:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2497s) that I've written here ahead of time.

[41:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2499s) So, and then we're gonna walk through

[41:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2501s) and kind of see how this works.

[41:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2504s) So the first policy I've written
is a authorization policy.

[41:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2508s) It allows a principal
that's a Kubernetes user

[41:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2512s) to do an action.

[41:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2513s) And so that act, the actions
that it can do are create,

[41:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2517s) and these are just Kubernetes
verbs, create, list, watch,

[42:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2520s) update, patch, and delete.

[42:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2522s) And then the resources it can act on

[42:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2524s) are Kubernetes resources.

[42:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2526s) So if you've ever, again,

[42:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2527s) if you've ever written an RBAC policy,

[42:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2529s) there's non-resource URLs like metrics,

[42:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2532s) liveness checks, and
then there's resources.

[42:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2534s) So any secret pod, config map,
CRD, those are all resources.

[42:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2538s) So we're gonna say, okay,
this acts on resources.

[42:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2541s) But this only applies
when the principal name

[42:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2544s) is sample user.

[42:26](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2546s) The resource being acted
on is a namespace resource.

[42:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2550s) So this excludes resources
that don't have a namespace

[42:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2553s) like node, validating
admission configuration,

[42:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2556s) a number of other Kubernetes types.

[42:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2558s) The namespace name is default.

[42:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2561s) The API group is empty,
which is the core API group

[42:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2563s) where pods, config maps and
everything live and Kubernetes.

[42:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2567s) And the API resource is config map.

[42:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2570s) So we're gonna allow the sample user

[42:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2571s) to basically do all these
verbs on config map.

[42:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2575s) So that's our authorization policy.

[42:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2577s) This looks sort of similar
to what you could actually do

[43:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2580s) almost all of this in RBAC, right?

[43:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2581s) It's permit, so it's not a forbid,

[43:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2584s) and all of these expressions
could be modeled in RBAC.

[43:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2588s) Now we're gonna do something
a little bit different.

[43:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2590s) So we're gonna add a second
policy that's a forbid clause.

[43:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2594s) We're gonna forbid users that are

[43:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2596s) in the group requires labels.

[43:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2598s) So Kubernetes users are in groups.

[43:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2601s) They are forbidden from
listing and watching

[43:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2604s) any Kubernetes resource,

[43:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2607s) unless the request has a label selector.

[43:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2610s) So if you've ever listed
Kubernetes resources like pods,

[43:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2613s) or any other resource, you
can do with Kube Cuddle.

[43:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2617s) Kube cuddle dash L for a label selector.

[43:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2619s) Key equals value.

[43:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2620s) You can specify keys and values.

[43:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2622s) So in this example, we're
gonna forbid all requests,

[43:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2625s) unless there's a label
selector where key owner

[43:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2629s) equals the requester's name.

[43:52](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2632s) This is something you can't do in RBAC.

[43:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2633s) This is attribute based access control.

[43:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2636s) So we've now restricted some

[43:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2638s) of those verbs that we saw above.

[44:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2640s) The next policy is not just
Kubernetes authorization,

[44:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2644s) but Kubernetes admission.

[44:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2645s) So Kubernetes admission is
another part of Kubernetes

[44:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2648s) where you can restrict
mutations to resources.

[44:11](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2651s) So creates, deletes, updates.

[44:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2655s) So again, we're gonna apply this

[44:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2656s) to users in the requires label group.

[44:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2659s) They are forbidden from creating, updating

[44:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2661s) or deleting any resource, period.

[44:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2665s) Unless that resource has metadata.

[44:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2669s) That metadata,

[44:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2670s) so if you've ever configured
a Kubernetes resource,

[44:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2672s) it has metadata object in
the object meta and labels.

[44:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2676s) And one of those labels is
"owner is principal name".

[44:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2680s) So you can no longer,
we're gonna forbid users

[44:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2683s) and requires labels from
creating any, or updating,

[44:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2686s) or deleting any resource
unless they're the owner of it.

[44:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2690s) And then finally, we're gonna
do a similar forbid on update,

[44:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2695s) but we're gonna prevent overriding.

[44:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2697s) So when you get an admission
request for an update,

[45:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2700s) you get two resources.

[45:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2701s) You get the new state and the old state.

[45:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2704s) We don't wanna let someone
overwrite a resource

[45:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2706s) that they didn't already own.

[45:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2708s) So we're gonna forbid,

[45:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2708s) if the old object metadata
didn't have owner is name,

[45:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2712s) we're gonna forbid that.

[45:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2714s) Okay?

[45:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2715s) So that's our policy.

[45:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2716s) So I've already created this

[45:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2717s) in a local Kubernetes
and docker kind cluster,

[45:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2721s) and we're gonna walk through
what that actually looks like.

[45:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2728s) Okay, so I have a kube config
here that I've written,

[45:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2732s) that is a sample user.

[45:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2734s) And I'm using the Kubernetes
client call Kube cuddle off,

[45:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2738s) who am I?

[45:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2739s) And this is just gonna return
back, "What user are you?"

[45:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2742s) What groups are you in?

[45:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2743s) So I'm the sample user, I'm
in the group sample group,

[45:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2746s) requires labels that we saw in our policy,

[45:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2748s) and a system authenticated.

[45:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2751s) I wanna as admin, so I'm the
admin of the the cluster,

[45:56](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2756s) not as that other kube config.

[45:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2758s) I wanna create a config map
just for display purposes here.

[46:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2761s) Okay, so I created a config
map called "other config".

[46:04](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2764s) It is gonna have the,
just the key and value

[46:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2767s) foo bar, right?

[46:09](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2769s) It doesn't need any data.

[46:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2770s) We're gonna label that
config map we just created

[46:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2774s) with the owner, some user.

[46:15](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2775s) So not our sample user,
just some other user.

[46:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2778s) Now we're gonna just get config maps

[46:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2780s) that exist and show their labels.

[46:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2781s) So there's three.

[46:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2782s) There's kube root CA that's already there.

[46:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2784s) That's created
automatically by Kubernetes,

[46:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2787s) it doesn't have any labels.

[46:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2788s) We have this other config
owned by some user.

[46:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2790s) We have this test config
owned by the name default.

[46:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2794s) Okay?

[46:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2795s) So none of these are
owned by our sample user.

[46:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2798s) As our sample user, if we
try to kube cuddle get CM

[46:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2801s) or config map, we're
gonna get a forbidden.

[46:44](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2804s) And we're not only gonna get
a forbid, we're gonna see

[46:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2807s) what policy denied that request.

[46:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2809s) So you can see here

[46:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2811s) that the policy label
enforcement policy one

[46:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2813s) on line 21 column one forbid this request.

[46:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2818s) So I now know, okay, I'm forbidden,

[47:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2820s) and I know which policy
forbid me from doing this.

[47:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2823s) If I wanna try to label, so
I wanna update an existing,

[47:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2827s) that other config, and add
the stage equals test label,

[47:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2832s) I'm gonna get forbidden from
that because I don't own it.

[47:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2837s) If I want to create a config
map as my sample user,

[47:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2841s) and I try to do that, again from literal

[47:23](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2843s) where K one equals V one,

[47:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2845s) but I don't have any label
on this config map I'm trying

[47:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2847s) to create, again, I'm gonna get denied.

[47:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2850s) This is a admission denial.

[47:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2852s) You can see admission webhook denied this.

[47:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2855s) So, so far this is pretty effective.

[47:39](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2859s) So what if we, how do we actually
do something as this user?

[47:41](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2861s) Okay, so here's a sample config map.

[47:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2863s) I have it locally in a file
called "sample-config".

[47:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2867s) Notice that it has a label,

[47:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2869s) and the label is owner equals sample user.

[47:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2871s) It just has some dummy
data of stage equal test.

[47:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2874s) So what happens if we
actually try to create this

[47:57](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2877s) as the sample user?

[47:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2878s) Okay, let's try it.

[48:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2880s) It succeeds.

[48:01](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2881s) This is great, right?

[48:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2882s) This is what we actually want.

[48:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2885s) And then as the sample user,
if we wanna list config maps,

[48:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2888s) so get config maps with a label selector,

[48:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2890s) remember we tried it before
without a label selector.

[48:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2892s) We do it with a label
selector, it succeeds,

[48:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2894s) but we can only see the one we own.

[48:16](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2896s) We can't see any else.

[48:19](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2899s) So that's our short demo here.

[48:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2902s) The few things to note
about Cedar is that Cedar

[48:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2908s) is really at this point a prototype.

[48:31](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2911s) We wanna hear more from you.

[48:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2912s) If you would like this
integrated in into EKS,

[48:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2914s) we would love to hear about it.

[48:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2916s) You can go ahead, download it, try it out.

[48:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2918s) It's all open source.

[48:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2920s) And yeah, again, we would love to hear

[48:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2923s) what you like, what you don't like,

[48:46](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2926s) what you'd like to see about this.

[48:47](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2927s) But for now, this is
an open source project

[48:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2929s) that we're really excited about,

[48:50](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2930s) and wanna get more
information on from you.

[48:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2933s) Finally, a few resources.

[48:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2935s) As we mentioned throughout the talk,

[48:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2938s) we have an EKS best practices guide.

[49:00](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2940s) This is on the AWS documentation.

[49:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2942s) There's a QR code here.

[49:03](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2943s) So you can really read more
about these best practices

[49:06](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2946s) that we've mentioned here,

[49:08](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2948s) as well as just Kubernetes specific ones

[49:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2950s) that aren't specific to AWS or EKS,

[49:12](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2952s) but just Kubernetes in general.

[49:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2954s) We have the EKS workshop,
which is a great guided tour

[49:17](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2957s) of, if you're new to
Kubernetes, new to EKS,

[49:20](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2960s) and you wanna learn how
to create an EKS cluster,

[49:22](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2962s) it's a great guided tour
of creating a cluster,

[49:25](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2965s) configuring it, installing
applications on it,

[49:28](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2968s) like monitoring stacks, and other add-ons.

[49:32](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2972s) It's really, really helpful.

[49:33](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2973s) And then also we have EKS
blueprints that we provide.

[49:37](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2977s) These are sample
configurations for Terraform

[49:40](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2980s) and AWS CDK to help
you get up and running,

[49:43](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2983s) and started very quickly with EKS.

[49:49](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2989s) Finally, we also have a public roadmap.

[49:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2991s) So if you go to GitHub
on the AWS organization,

[49:55](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2995s) the containers roadmap,
there's a link here.

[49:58](https://www.youtube.com/watch?v=yuXF-NXaelI&t=2998s) You can see a list of
feature requests by by users,

[50:02](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3002s) or issues that we've opened to say, hey,

[50:05](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3005s) this is something we're thinking about,

[50:07](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3007s) we want user feedback on,
you can upvote features

[50:10](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3010s) that you want in EKS there, or
tell us about your use case.

[50:13](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3013s) We want to hear about it.

[50:14](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3014s) There's one for Cedar
integration into EKS.

[50:18](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3018s) So if you want, if you like
that, if you want that,

[50:21](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3021s) plus one that, but you can
also subscribe to updates.

[50:24](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3024s) So you'll get notified when
features are in development,

[50:27](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3027s) or when they actually ship.

[50:29](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3029s) We use this actually.

[50:30](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3030s) Our product managers use this
all the time to gauge, okay,

[50:34](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3034s) what's the most popular issue?

[50:35](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3035s) You could all go see it.

[50:36](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3036s) You can sort by plus ones to see

[50:38](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3038s) what's the most requested feature for EKS?

[50:42](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3042s) And with that, thank you,
appreciate your time today.

[50:45](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3045s) George and I'll be
available after the talk

[50:48](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3048s) for Q and A outside.

[50:51](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3051s) Thank you, and have a
great week at re:Invent.

[50:53](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3053s) - Thank you.

[50:54](https://www.youtube.com/watch?v=yuXF-NXaelI&t=3054s) (crowd clapping)

