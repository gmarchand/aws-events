# AWS re:Invent 2024 - Amazon EKS for edge and hybrid use cases (KUB310)

[Video Link](https://www.youtube.com/watch?v=QMzor8haEOM)

## Description

Some workloads need to run on premises, at the edge, or in a hybrid scenario due to low latency, data dependencies, data sovereignty, and other regulatory reasons, especially in industries such as manufacturing, healthcare, telecommunications, and financial services. Data-dependent workloads may have to wait for data to be in AWS services before they can be fully migrated. In this session, explore production-ready architectures using Amazon EKS Anywhere and Amazon EKS Hybrid Nodes to run container workloads on premises and support modernizing VMware-based workloads.

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

- Welcome to the session. This is "KUB310, Amazon EKS for edge and hybrid use cases." My name is Eric Chapman. I'm a Senior Product Manager
on the Amazon EKS team focused on hybrid and edge. And I'm here today with my
colleague Gokul Chandra, who's a Container Specialist
Solutions Architect, focused on bringing our EKS
hybrid and edge solutions to customers in the telco vertical. Today, we're gonna dive deep on how the Amazon Elastic
Kubernetes Service, or EKS, can help alleviate some of the challenges faced by customers running
with a hybrid strategy; that is deploying workloads at the edge and on-premises, as well as running on AWS. We're gonna start by laying out some of the common challenges faced by customers running
across environments. We'll lay out how
standardization can help, and why more and more customers
continue to turn Kubernetes as their standard platform, and what challenges
remain once they do so. We'll lay out what we're
doing on the Amazon EKS team to help make it simpler, more
efficient, and more consistent to deploy Kubernetes
across your environments. We'll review architectures
and best practices for each of our EKS hybrid solutions. And we'll close with how
you can learn more about EKS during re:Invent and thereafter. Let's start with a scenario that brings in many of the reasons that our customers opt for a hybrid approach to begin with, and the challenges that
arise once they do. Say you're a platform engineering manager at an enterprise with
multiple business lines. You've standardized your cloud
operations on Kubernetes, running EKS on AWS; and many of your applications
are cloud native, integrating with AWS services for networking, storage and databases. However, you still have a large suite of applications that run on-prem and will continue to run
on-prem for the near future. Some of these are tightly integrated with legacy technologies
that are gonna be difficult to extract and pull into the cloud. Others require compute running in close physical proximity to end systems, or need to run at the edge
for high performance latency. Other applications still handle highly sensitive customer data and face strict data
residency requirements. These applications run
on different systems with different operational models and different skillset requirements, leading to unscalable
silos across your teams. Instead of focusing on
improving platform performance or adding capabilities for your platform that can help your
development teams innovate, your team spends too much time manually patching and
maintaining underlying systems just to maintain platform
stability and business continuity. You know that if you could offload some of the undifferentiated
overhead work, operational work that your team does, you could free your teams
to focus on innovating in ways that help improve
developer experiences and ultimately improve experiences
for your end customers. With your applications
running on different systems with various integrations, there are multiple technology stacks that you need to support. Supporting multiple technology stacks, such technology sprawl leads
to several other challenges. For one, it hinders your
ability to innovate rapidly for your development teams, and it limits the ROI of
each individual improvement, as improvements to one technology stack aren't inherited by the others. The difficulty in making changes quickly arises from a proliferation
of manual processes, out-of-date versions, and strict coupling
with other dependencies. Furthermore, each technology stack requires different skillsets that don't necessarily
translate across environments and you've had to expand your team just to maintain your
platform in steady state. You think that if you could standardize on a single platform, you'd unlock your team's
ability to innovate. With the explosion of popularity, and popularity of Kubernetes in the cloud, we see more and more customers that are running across
on-prem and cloud environments standardizing on Kubernetes, integrating with consistent
tooling wherever they run. Say you chose Kubernetes as your container management
platform in the cloud to ensure high availability and scalability of your
mission-critical applications. The open and extensible
nature of Kubernetes stimulated the development of
a healthy ecosystem of tooling and innovative practices like GitOps that your teams can readily adopt. And as Kubernetes is an
open source standard, you could run it across your environments wherever your applications need to run. In fact, let's say many
of your application teams running on-prem have
adopted Kubernetes already. And while you've seen some of the benefits of such standardization, operational overhead continues to hinder your team's ability to innovate. While your development resources
have become more fungible across your environments
given this standardization, there remains a very steep learning curve for those tasked with administering your Kubernetes clusters. Maybe you underestimated the complexity of managing the Kubernetes
control planes themselves, keeping your clusters healthy, rotating certificates on a timely basis, and making sure DHCP
IP leases don't expire. It's also been more challenging
than you've expected to continually scale up and
scale down your control planes as your workloads scale
across your fleet of clusters. These are many of the same challenges that led you to choose EKS in the cloud, and many reasons that
customers running across clouds opt for managed Kubernetes solutions. EKS manages tens of millions
of clusters on an annual basis and we continue to see rapid adoption with 33% year over year growth in the number of clusters managed. Our goal on the AWS Kubernetes team is to make the operational
aspects of running Kubernetes an afterthought for our customers
wherever they need to run. And since the introduction of
EKS on AWS Outposts in 2019, one point of focus for the EKS team is on how we could bring
EKS into hybrid environments to provide the benefits
of a managed service and to enable you to establish
operational consistency across your environments. I'm sure many of you know
but for those that don't, AWS Outposts is AWS managed infrastructure that extends AWS services into your data center or colo facility, including EC2 for compute, S3 and EBS for storage and VPC for networking. EKS has been available on Outposts since Outposts' general
availability in 2019. And given the availability of these other AWS services on Outpost and Kubernetes control plane managed for you in the cloud by EKS, running EKS nodes on Outpost is gonna provide the most
consistent experience with running EKS nodes in region, and the tightest integration with AWS. We've seen Outpost customers adopt EKS for use cases like
general purpose automation and use cases that require
local data processing such as banking or real money gaming, just to name a few use cases. Customers love the operational
consistency that they get when they run EKS on Outpost as compared to running EKS in the region. Now at any given point, many
customers aren't in a position to refresh their
on-premises infrastructure. And so, to meet customers where they are, in 2021, we launched Amazon EKS Anywhere. EKS Anywhere provides AWS supported Kubernetes management software that simplifies the
infrastructure provisioning and lifecycle management process for clusters running on
customer managed hardware and virtualized and
bare-metal environments. EKSA is a fully customer managed solution with infrastructure providers,
Kubernetes' components, and operating systems
tested and supported by AWS. An EKSA subscription also
comes with AWS support for a curated set of add-on packages that extend core Kubernetes functionality for load balancing, ingress
monitoring and more. EKSA is especially popular with customers that have stricter requirements around their on-premises networking or need to operate in
locations with disconnected, disrupted, intermittent and
limited network connectivity. Such use cases include telco applications that need to run on bare-metal
at the far network edge, financial services apps that face stricter networking and regulatory requirements, and applications run by
travel and hospitality firms, operating cruise ships that may not have internet connectivity for
days or weeks at a time. We've enhanced EKS
Anywhere for compatibility with key telco ISV solutions. And in a couple of slides here, Gokul is gonna run us
through the architecture that one of our large telco customers uses to run their 5G O-RAN workload on EKSA. So customers really love
that they could continue to run on their own hardware
when they choose EKSA, take advantage of the investment they've already made on-prem. And customers really love
that with EKS on Outpost, they get the Kubernetes control plane managed for them in the cloud by EKS. In speaking with dozens
and dozens of customers, it became clear to us that
there is a need for a solution that would enable customers to continue to run on their existing hardware without requiring them to
manage the control plane. And that's why we're so excited on Sunday to announce the general
availability of EKS Hybrid Nodes. A new EKS feature that enables you to run Kubernetes nodes
on your existing hardware and attach it to the EKS control
plane running in the cloud. EKS Hybrid Nodes creates a more consistent operating experience between running EKS in the
cloud and running on-prem. And with Hybrid Nodes, we take on the operational responsibility for managing the Kubernetes control plane while allowing you to continue running your workloads on-prem, taking advantage of that on-prem hardware investment you've already made. Now you can conserve
your on-premises capacity strictly for your application workloads. And like with EKS in the cloud, you don't have to worry about scaling up and down your
Kubernetes control planes. That's all managed for you by EKS. EKS Hybrid Nodes is the
best choice for customers whose on-prem or edge
locations can network with AWS, and we think it's going
to be the best choice and the sweet spot for
most hybrid customers. We expect that Hybrid
Nodes will be especially popular for distributed edge use cases like media streaming and manufacturing, as well as general
enterprise modernization. And many of the same use cases customers use EKS on Outpost for today. EKS Hybrid Nodes, or EKS clusters with Hybrid Nodes rather, can also run cloud nodes
in a single cluster, opening the door for AI and ML use cases that use GPUs on-prem and in the cloud to bolster their training capacity or for inference bursting. I'm extremely excited to talk to you more about EKS Hybrid Nodes and I hope you're excited to
learn more about the details. But before we get there, I'm
gonna hand it off to Gokul who's gonna dive deeper for us on EKS on Outposts and EKS Anywhere. - Thank you, Eric. So let's talk about how AWS Outposts today can supercharge your
on-premises infrastructure with Amazon EKS. So, customers usually deploy Kubernetes clusters and pods on premises in order to reduce the latency and also enhance the security. And there are multiple other use cases where the hybrid capacity is not a requirement but a mandate. So whether extending your cluster to your on-premises
environment from the cloud or even managing your
hybrid compute capacity or hybrid computing platform design, so AWS Outpost covers you
for all those use cases. When it comes to deploying Amazon EKS clusters on AWS Outpost, we support two deployment options here. The first one is the extended clusters where you can start by creating the EKS cloud-based control plane in the same way that you do with the regional-based clusters. Then you deploy the cluster nodes, which are the Kubernetes nodes, which host your actual workloads
within the hybrid model like on the AWS Outpost
rack that is shipped and connected back to the region
from your own data center. And this is called the
extended cluster approach. But with this approach, what
you will be getting here is the same managed
Kubernetes control plane, which is completely managed by AWS, and an integrated experience
with other ecosystem of services that are
available today in the region. So the second model is the local clusters. So this is aimed at specific use cases where we have listened to our customers, where some of our customers
have their environments or deployment setting where they can have the unreliable network connectivity. Means they might have disruptions
because of so many reasons because of the placement
of the data centers in the penultimate regions of a metro or even in an isolated environment where they have issues with the continuous network availability, where it is required for the
AWS Outposts with EKS to run. So this is where we introduced the second deployment option called local clusters, which enables customers to still continue their Kubernetes-based operations even during the course of disconnects. So with this model, what EKS does is, it deploys a local control
plane, the EKS control plane, on your AWS Outpost rack itself. And during the course of
disconnect to the region for the EKS control plane
that we manage in the region, still the customers can continue to manage the Kubernetes-based operations without having any kind of
disruptions to their workloads. So this is aimed at
specific use cases as said, while local clusters can provide
this extended functionality where customers can still
continue to run their workloads without any kind of disruptions. Extended clusters, the first option, remains the recommended
option from the AWS end because it provides a more integrated and a managed experience to the customers, where the Kubernetes control plane is completely managed by AWS. And also, there are multiple
ecosystem of services that are available within the cloud where customers can directly use them to enhance their overall portfolio or their overall workload portfolio too. So, let us see how the
architecture is laid out for the extended clusters
that we have just discussed. So customers start by
ordering an Outpost rack. And this AWS Outpost rack will be shipped to customers' own data center that gets connected back to the region using a service link approach. And service link in turn
uses a direct connect service that is offered by AWS. And this connectivity
provides a high throughput secure connectivity back to the region from your Outpost environment. Then customers can create the VPC, the networking. Like when it comes to networking, the networks are created
in a similar fashion what they do today with
the region-based approach. They can create a VPC with
multiple subnets spanning across multiple availability
zones within the region. Now the difference that
makes like with AWS Outposts is that with AWS Outposts registered to your own account and placed within your data center, the same VPC that has been
created within the region can be extended to this Outpost rack. Means you can create multiple
subnets within the same VPC, selecting your Outposts
as the availability zone. So this enables the
extendability of the network from the cloud to your own data center using the constructs
that we enable seamlessly with AWS Outposts. So once you have this
networking layout established, you can create the EKS
control plane the same way that you do with the
cloud-based clusters today. So here, it's important to note that the EKS control plane is
created in the region, and the control plane anchors
to the region-based subnets using Cross-Account ENI architecture where the EKS control plane
is completely managed by AWS. So this gets anchored to the
subnets within the same VPC that you have extended to
the Outpost infrastructure. And once you have the control
plane deployed the same way as you do with any other
regional based clusters today, then you have an extended approach like with everything
that gets from the cloud to your Outpost environment. So here, once you have this whole infrastructure with EKS control plane, then you start by creating
self-managed node groups within the same Outpost subnets that you have extended to
your own infrastructure that is positioned
within your data centers. So it's important to note that that EKS control plane can be created with the
region-based subnets, but your actual Kubernetes nodes will be running within the subnets that are positioned in
the Outpost environment. So the self-managed node group, which is a Kubernetes node group which constitutes multiple nodes, technically these are the EC2 instances because AWS Outpost rack
has multiple services that are offered today as
part of the AWS portfolio where you can run your EC2 instances which are your Kubernetes
nodes technically on your own environment
like without having to rely on the region-based EC2 services. So this enables the customers to deploy your actual workloads running
on the Kubernetes nodes, which are positioned on the Outpost rack, which in turn is positioned
within your own data center. So, usually when you
deploy the applications within this Outpost environment, definitely you might
have another environment or portfolio with full set of applications that you have already been running within your own data center environments. So we provide a construct
called local gateway where local gateway access the gateway to enable the communication
between the applications that are running on this EKS environment to talk to your own
applications running on any other data center infrastructure
that you already have. So it enables seamless connectivity so that you can stitch the
application connectivity that is running on Outposts with your own infrastructure components that are running within your data center. Now so far, we have discussed how customers can leverage AWS Outposts, that is, AWS provided
and managed hardware; and deploy EKS clusters on them so that you can extend
your application portfolio from cloud to your own data center. But what if customers want
to run the applications on their own hardware? Technically the COTS-based
hardware that they have procured. Or many customers have made
significant investments in their data center hardware where they already have this hardware sitting in their own data centers. Or the second thing important
aspect to discuss here about the requirements may be is like, what if a customer wants
to deploy the clusters in a completely isolated environment? When we say completely isolated, they don't want to have a
region-based connectivity or they don't want any
internet connectivity going out of their environments. That is where EKS Anywhere
comes into picture. So EKS Anywhere enables
customers to deploy Kubernetes clusters on their
own COTS-based hardware or existing virtualized environments that they are already managing
such as VMware, CloudStack. So this enables to deploy
clusters with the same consistency as you see with the
region-based KS clusters. So this is about EKS Anywhere. Now let us see how EKS Anywhere
architecture looks like. So it's a complete stack of components that form up the full
stack of EKS Anywhere as a consistent Kubernetes
platform that is provided by AWS. So the first one is the
infrastructure providers, right? Even before going here, we have to emphasize on the fact that EKS Anywhere is designed based on the Cluster API foundations. So Cluster API is a Kubernetes
sub-project that standardizes and simplifies the cluster
lifecycle management. So EKS Anywhere inherits a
lot of different architectural patterns from Cluster API,
in short called as CAPI, across the community. So, the infrastructure providers means EKS Anywhere can be deployed on all these options that we show here. So it can be deployed
on bare-metal servers where you can completely
use your bare-metal servers to deploy the EKS Anywhere
clusters on top of them. Especially with bare-metal approach, we not only support deploying clusters but we have also taken the
undifferentiated heavy lifting of imaging and managing the service to using a Tinkerbell component. So Tinkerbell is a open source project where AWS heavily contributed
to this particular project to make it Kubernetes native
or cloud native in general. And the second set of
infrastructure providers are your virtualized environments. What it means is that, if you already have
your VMware environments or CloudStack environments, you can use this existing
virtualized layer which manages the virtual machines and you can deploy EKS
Anywhere on top of them. Where we provide the full set of capabilities for the customers to have an end-to-end experience with a seamless automated
approach of creating clusters on top of your virtualized environments. And also, we do support
our partner environments such as Nutanix. And also we do have a
full set of capabilities to deploy EKS Anywhere clusters on Snow, which is our edge-based device like which is provided by AWS. So these are the infrastructure providers where EKS Anywhere can be deployed on. The next layer is the
Kubernetes distribution. So the Kubernetes distribution that is being used with EKS Anywhere is called the EKS Distro, which is the EKS
distribution of Kubernetes. And one important thing
to note here is that this is the same Kubernetes distribution that is used across the board. Means it is now powering millions
of clusters in the region where already customers are
using it at a production scale. So what exactly this distribution provides or enables users is to
just like rely on AWS, where AWS holds the responsibility in maintaining the security patching and also building the base images for coming up with this distribution so that you're ready to go
deploying these clusters without having to worry
about spending cycles on the security patching, CVE analysis, vulnerability analysis and all. So this is the EKS distribution which is called the EKS Distro. Next comes the layer of
cluster lifecycle management and cluster operations, and also the CNI, which is the Container
Networking Interface, which provides the baseline connectivity for your pods and services that run on top of your Kubernetes environment. So, EKS Anywhere comes packaged
with a set of controllers that enables seamless operations to create, delete, upgrade,
update, add, delete nodes. And all these operations
are provided by the set of controllers that comes
packaged with EKS Anywhere. And, on the other hand, the packaged or the main CNI, or I mean the supported CNI
with EKS Anywhere, is Cilium. So there is a very big
differentiation factor here. If the people here are familiar with how EKS works in the region, we have AWS VPC CNI that provides flat networking
model within the region. But with EKS Anywhere, as said, this is a completely and isolated option that runs within your own data center. We cannot use AWS VPC CNI, as similar to the other
option we have just discussed; that is the EKS on Outposts. Still EKS on Outposts
uses the VPC construct. So we use VPC CNI for Kubernetes. But with EKS Anywhere, because it's completely out of AWS control and it is positioned within
the customer's own data center, on your own hardware, and you will be utilizing
your own network there, so that is where we package Cilium as the go-to CNI with EKS Anywhere. Next comes the layer of the
operations and tooling, right? See, just creating EKS clusters
or Kubernetes environments is not alone enough to
run your full-fledged application portfolio. You need certain set of tools or tooling that has to be deployed on
your Kubernetes environments to carry out multiple
activities that are required for your end applications to
be available for the end users. So, for example, it can
be the load balances, it can be the ingress, it can be your image registries. So all these tooling are needed. And what we heard from
our customers is, like, if they're consuming this directly from the upstream communities, they have to rely on the
community-based support. Or the second model is,
if any of these components are available through our partner network or from some enterprise vendor, they have to go to that
particular enterprise vendor to get the support for
these particular components. So that is where we came up with something called Curated Packages where we enable customers to
use some pre-curated packages which are like designed
and also defined by AWS, where AWS holds the responsibility of managing these components too on your Kubernetes environments. For example, let us take
Harbor, Emissary, MetalLB; all these are very well-known open source community based projects. So whenever you use Curated Packages, you don't have to worry
about maintaining them and also maintaining
the version capabilities and also compatibility with the specific Kubernetes version that
you are running on. And AWS provides the full-fledged support in managing these particular add-ons on top of the EKS environments. So that is the value that we have provided with Curated Packages. And another important aspect here is that, so from the security perspective, if you are using a specific
add-on on Kubernetes and if it has some kind
of security vulnerability, today, if you're consuming it directly from open source or upstream, you have to wait on the community to enable you with a patched version. But that is not the case
with Curated Packages that are available with EKS Anywhere, where AWS holds the responsibility and also provides the full-fledged support for any of these add-ons that are available in the portfolio. And AWS is responsible for managing the code of all these add-ons too. So that is the Curated Package layer that comes with EKS Anywhere. Next, you can create and
manage EKS clusters today in a few different ways, right? So the first model is eksctl CLI. So, we provide a
comprehensive CLI mechanism. And here it's very important to note, like if people are familiar here with how EKS clusters
in the region operate, we have a consistent API endpoint, where it acts as a vending
machine for Kubernetes clusters. And you can directly
call this API endpoint with AWS CLI or infrastructure
as a code tooling, which in turn triggers the creation of EKS clusters in the region. But that is not the case
with EKS Anywhere, right? Because it's sitting
in your own data center and it's operated by the customer. So that is where we provide
the same consistent experience using a comprehensive set of CLI options that are available with eksctl CLI. So eksctl CLI used to be our approach of creating clusters within
the region from start. And eksctl CLI, we added an
extension called Anywhere which provides the capabilities to operate and manage clusters within
your own environments. So the same set of tooling but we integrated or extended the approach to even control the clusters
and manage the clusters on-premises on your own hardware. The second option is Terraform, right? If you're a fan of the infrastructure as a code like tooling, we provide a custom
Terraform operator provider, for creating and managing
EKS Anywhere clusters. The third approach, which
is our recommended approach, where we briefly discussed about how EKS Anywhere inherits
a lot of different architectural patterns from CAPI. So we recommend this approach where you can completely
manage your clusters with a GitOps-based fashion, having the whole cluster configuration stored in a Git repository. And with EKS Anywhere, one of the packages
include Flux Controller. Flux Controller is a prominent
GitOps-based controller that is available in the community. And we started supporting it and we contribute to the Flux Controller so that it gets packaged with EKS Anywhere and you can use a GitOps-based approach for your infrastructure. Again, reiterating over this point, we are not talking about the GitOps-based approach for managing your applications, but managing the infrastructure itself can be done using GitOps. So these are the three different ways that you can use for
creating the clusters. Next comes the region-based connectivity. As we alluded to multiple
different deployment options and also we discussed about how EKS Anywhere is completely different and it can be air-gapped and isolated without having to rely on the
region-based connectivity, still, if the customer
is interested in using any of the managed
services within the cloud, they can have optional
connectivity back to the region. So there are common use cases that we have seen among customers, right? For example, if they want to use a central single-pane observability
dashboard mechanism for thousands of EKS clusters today, so they can use the
Amazon-managed Prometheus, Amazon-managed Grafana that
is available in the region, so they can still have the optional cloud-based connectivity
with EKS Anywhere. Now, the deployment topologies. So, EKS Anywhere supports two different deployment topologies, right? And as the standardized
CAPI procedure involves having a workload and
a management cluster, the same approach is
available with EKS Anywhere where you can use a single
cluster-based option where customers are free to use the single deployment option, managing singleton clusters, which will be provisioned
with all the controllers on top of this cluster, which can manage the cluster itself. For example, when I say
managing the cluster itself, if you want to add nodes, delete
nodes, upgrade the cluster, all the controllers are
available on the same cluster. The second approach is
the management cluster and workload cluster approach, right? What it does is, you will have a central management cluster with a full set of controllers that are responsible
for creating, updating and managing the lifecycle
of the clusters, or deployed. And using this management
cluster as the endpoint, you can create and operate a
fleet of workload clusters. So the workload clusters are the clusters where the end user workloads are deployed. As you can see, a clear-cut
differentiation here between the management cluster
and the workload cluster, you see that the controllers
that are deployed on the management cluster are absent on the workload clusters, providing the resources that are required for your end applications, not consuming any resources for the cluster lifecycle
operations itself. So this is how you can manage
a fleet of workload clusters with a management cluster. We usually recommend customers having more than three EKS Anywhere
clusters to have this approach. So it provides a very concrete governance when managing the clusters and also the single-pane observability of the whole cluster portfolio within your data center environment. Now, the declarative options and the cellular cluster management, which is very important for
customers running hundreds of Kubernetes clusters in their
environments today, right? So, the interface that you use to create your EKS Anywhere clusters is a very simple YAML-based configuration. This is the configuration file where you define the
cluster specifications that include the name, the network name, and also the number of control plane nodes that it has to create, and the worker node configurations. Everything goes into this
YAML-based configuration. And as we just discussed,
the GitOps-based approach paired with the management
cluster topology, you can have a cellular
management approach where you can use a
specific management cluster to operate a fleet of workload clusters in a GitOps approach, where the management
cluster access the sync and then it realizes
all the configurations that you have provided
through a Git source to create and operate
multiple workload clusters. Lastly, the deployment options, right? So, when we reached out to customers, each customer has their
unique set of requirements when creating a Kubernetes cluster. We cannot always force them
to create a multi-node cluster because there might be conditions where they're resource-constrained. So that is where we support
different deployment options. The first one being
the multi-node approach where each node will be
acting as a control plane or a data plane node. Or the second one is the colocated master and the worker nodes where you can have three nodes with masters, high available masters; and also the worker node can
be running on the same machine. The third option is a single-node approach where you can run the entire
EKS Anywhere environment or EKS Anywhere cluster on
a single bare-metal node. So these are different deployment options we support with EKS Anywhere today. And particularly, we want to emphasize or introduce you to a specific use case where EKS Anywhere enabled a
Japanese-based telco customer to deploy their nationwide open radio access network
architecture across Japan, almost serving 90 million subscribers. And this particular
topology where EKS Anywhere is used as the container
access service option constitutes almost 15,000
different cell sites with more than 35,000 bare-metal servers, like including all the sites
that we have seen just now. So, with this particular approach, NTT DOCOMO is able to stretch
their cloud-based pattern from the region to the
penultimate regions, including the cell towers and cell sites. So, how exactly EKS Anywhere
enable the NTT DOCOMO? So NTT DOCOMO, as any other telco operator
in the market today, has a stretched topology. Means they have AWS regions, regional data centers, edge sites, and also cell sites. So what is the differentiation
factor here, right? So region, region is a cloud-based model. And then coming to regional sites, regional sites are standard data centers which have enough capacity
to host multi-node clusters. And edge sites are
resource-constraint environments where they cannot operate
a lot of different options like when it comes to
having a set of hardware. And when coming to the cell sites, these are the most edge
sites in a cell topology where they can only host
single-node clusters because the cell sites can only host a specific set of hardware
under them, like or in them. So this is the stretch topology that is usually seen
with our telco customers. And connecting these particular topologies was made easy for NTT DOCOMO with our Direct Connect
approach that we already have where they can connect the
region to until the cell site with the direct connectivity approach or Direct Connect service that
we have in the AWS portfolio that provides consistent,
reliable and secure connectivity from the region to even the
edge site or applications and also for the infrastructure. So the connectivity is not
just for the infrastructure, but the same backbone can be
used for the applications too. So with cellular management
of EKS Anywhere clusters that what we have seen earlier, NTT DOCOMO is able to create and manage multiple workload clusters with a management cluster
sitting in the regional site. And there are different
topologies that they have used because regional sites
have enough capacity to host multi-node clusters. They use a workload cluster
sitting in the regional site to create and operate
multiple workload clusters. And the regional data
center is used to host the management cluster
that can operate and deploy multiple workload clusters
in the edge sites. So this stretch topology and also the cellular cluster management enabled DOCOMO to deploy
their full-fledged container access service platform starting from the region
to the edge sites. In the region, the EKS
service is always available. And NTT DOCOMO is one
of the first customer where it paired up with NEC, which is their core and RAN provider, the ISP vendor that
provides the core and RAN, to certify their workloads
on graviton in the region. So they're hosting the 5G
core in the region and RAN which constitutes the
DU, the Distributed Unit, and the centralized unit on
the EKS Anywhere environments stretching from regional
sites to the edge sites. So with this particular approach, NTT DOCOMO was able to deploy
different set of applications starting from the cloud to the region. For example, the edge sites will comprise of the distributed unit
and the centralized unit. The RAN intelligent controllers are deployed in the regional sites, and the main 5G core components
are deployed in the region. So, let us end the EKS Anywhere topic like with a few best practices, right? So whatever deployment we choose, we provide a set of
deployment best practices. So the same applies for EKS Anywhere too, even if it is managed within
your own data centers. The first one is using the GitOps-based cluster management approach where you can store the
whole cluster configuration as a code in the GitOps repository and can sync the cluster
management and creation. And the second one is
using the curated packages where you can use the
AWS-provided Curated Packages to manage all your add-ons that gets deployed on
EKS Anywhere clusters. The cluster upgrades with EKS Anywhere, the CLI and also the
GitOps-based approach, we support different
types of upgrade patterns. It can be rolling upgrades
or in place upgrades where you can just upgrade
the Kubernetes version running on top of your hardware or a full-fledged rolling upgrade, which also patches the OS that is running on top of your hardware. So you can use the existing mechanisms to upgrade your clusters. The LDAP and also OIDC for
security based authentication, you can integrate EKS Anywhere with your existing LDAP infrastructure that is available within
your data center environment. Lastly, as the Cilium is the package CNI that is available with EKS Anywhere, you can use the eBPF security that is available with
the network policies that is provided by Cilium to
protect your East/West traffic that is within your cluster so that you can use a
full-fledged capabilities that are provided by Cilium to secure your workload communication, between port to port or
service to port communications. So now, let me hand it over back to Eric, who will be introducing the
newest deployment option, the EKS Hybrid Nodes. - Thanks, Gokul. All right, so years of running EKS on Outposts and EKS Anywhere and learning from our customers gave us the conviction that managing the
Kubernetes control planes for clusters running on
customer-managed hardware would represent a meaningful step toward alleviating the
undifferentiated heavy lift of running Kubernetes on-premises. With EKS Hybrid Nodes, you attach on-premises
and edge infrastructure running in your environment to the EKS control plane
running in the cloud, enabling you to retain
your workloads on-prem while offloading control plane management responsibility to Amazon. You'll continue using Amazon EKS features like EKS add-ons, EKS Pod Identities, cluster access management,
cluster insights, and extended Kubernetes version support. And now, you can rely on AWS' expertise in managing, securing, scaling
up Kubernetes control planes to reduce your operational overhead, conserve your on-prem capacity by hosting your Kubernetes
control plane in the cloud, and establish operational consistency across your on-prem
and cloud environments. So, how does it work? With EKS Hybrid Nodes, your EKS control plane continues
to run in the AWS region with the same APIs, tooling and features that you're accustomed to
when you run EKS in the cloud. Your on-premises worker nodes are physical or virtual
machines that you manage. With this bring-your-own
infrastructure approach, EKS is not calling
infrastructure provider APIs to provision node capacity on your behalf. Instead, with Hybrid Nodes, you'll reuse the tooling and systems that you've established
on-prem to provision capacity. So to enable your on-prem and edge devices to connect to the EKS
control plane in the cloud, we've adapted the tooling that we use to initialize the EKS
optimized Amazon Linux AMIs so as to accommodate
the connection of nodes running on customer-managed hardware to the EKS control plane. The resulting hybrid node
CLI utility called nodeadm installs the components
needed for your on-prem hosts to run as Kubernetes nodes and connect, authenticate to the EKS control plane, including the kubelet, containerd, and the AWS IAM Authenticator. Running the nodeadm init command bootstraps your nodes by configuring the installed artifacts to join your EKS control
plane in the cloud. All right, let's take a brief detour to learn a little bit more about nodeadm before coming back to
wrap up our overview. So you'll run nodeadm on each
of your on-premises hosts to simplify the installation,
configuration, registration, upgrading and uninstallation
of your Hybrid Nodes. We enhanced nodeadm to work
with arbitrary infrastructure and select operating systems. And we integrated it
with AWS Systems Manager and AWS IAM Roles Anywhere to streamline the process of authenticating your on-prem nodes to the Kubernetes cluster, the EKS control plane
running in the cloud. To automate the initialization of your Hybrid Nodes to your EKS cluster, we recommend including nodeadm in your golden operating system images configured to run at host startup for your ISOs, OVAs or
other image formats. Now coming back to our overview, to join your cluster, your EKS Hybrid Nodes assume
an EKS Hybrid Nodes IAM role that you'll create on your AWS account. This is similar to the EKS
nodes IAM role you use today. For your EKS Hybrid Nodes
to assume this role, they'll obtain temporary credentials either using an AWS systems
manager hybrid activation or AWS IAM Roles Anywhere. Systems Manager is a simpler solution and we generally recommend it for Hybrid Nodes authentication. Unless you already have
public key infrastructure with your own private
certificate authority and certificates established on-prem, in which case IAM Roles
Anywhere is a good choice. You'll also need consistent
private connectivity from your on-prem or edge
environment into the AWS region. We expect that AWS Direct Connect, AWS Site-to-Site VPN or a customer-managed VPN solution will be the most common technologies that our customers use to
establish this connection. Direct Connect is often preferred when consistent high
performance latency is required. Although AWS Site-to-Site
VPN doesn't require the installation of
physical networking hardware and can be a good choice,
a cost-effective choice, for deployments that don't require as much network consistency. So how are responsibilities shared between AWS and EKS
Hybrid Nodes customers? AWS, of course, continues to manage the AWS services that run in the region, including the EKS control plane, your identity and observability services and the ECR container registry. A subset of EKS add-ons
are supported by Amazon as compatible with Hybrid Nodes, including kube-proxy, CoreDNS, the ADOT and CloudWatch
observability agents, the Pod Identity agent, and the CSI snapshot controller. You'll be responsible for
managing the components that run on-prem in your environment, including your on-prem
storage solution, networking, and the operating systems
that run your Hybrid Nodes. AWS supports the integration of the Cilium and Calico CNI drivers when
you run them with Hybrid Nodes. And AWS supports the basic features of those drivers with Hybrid Nodes, including for overlay networking,
IP address management, and dynamic PodIP advertising using the Border Gateway Protocol, or BGP. AWS supports select operating
systems with Hybrid Nodes and supports the integration
of those operating systems but you'll retain responsibility for managing the operating system, patching it, and maintaining it. EKS Hybrid Nodes is compatible
with Ubuntu and RHEL for bare-metal and
virtualized environments, and with Amazon Linux 2023 for virtualized environments alone. Now let's run through how traffic routes across your environment
between the EKS control plane and your on-prem nodes and pods. Without configuring your EKS
cluster for Hybrid Nodes, your control plane wouldn't
know how to reach the node and PodIP addresses running
in your environment. To account for this, when you create a Hybrid
Nodes-enabled EKS cluster, you pass in a RemoteNodeNetwork CIDR range and a remote pod network CIDR range. The RemoteNodeNetwork CIDR is used for kubectl exec,
logs, and port forwarding; and the remote pod network CIDR is used if your control
plane needs to reach webhooks running in your environment. These new parameters alert
the EKS control plane that these IP addresses can be reached by forwarding traffic
into your cluster VPC. These CIDR ranges can't
overlap with each other, they can't overlap with
the cluster VPC CIDR range, and they can't overlap
with the EKS service CIDR. As of today, only new
EKS clusters are capable of handling this remote
networking configuration. And as such, today, only new
clusters can run Hybrid Nodes, although we plan to enable
existing EKS clusters to run Hybrid Nodes in the future. So traffic routes from your
control plane into your VPC over the Elastic Network
Interfaces or ENIs, that EKS creates on your subnets when you create your cluster. This is the same mechanism that EKS uses for control plane to cloud
node communication today. And in order for data to
make it into your data center and into your environment
once it's in your VPC, you need to add rules to
your VPC routing table for traffic out to your node and pod CIDRs set to transit over a gateway that you'll create and
attach on your account. This will typically either
be a virtual private gateway, which is better suited
for small and medium-sized deployments and simpler network typologies or an AWS transit gateway, which is generally recommended for larger, more complex networks. So the data then flows out of your gateway over your private connection that's either your Direct
Connect or your Site-to-Site VPN and into your environment. The firewall rules
protecting your data center, your edge location, need to enable
bi-directional communication between the EKS control
plane running in the cloud and your Hybrid Nodes running on-prem. And you'll also need
to add forwarding rules to your on-prem routing table for your hybrid node and pod CIDRs. As pods are ephemeral, their IP addresses
change fairly frequently. So it's recommended that
you dynamically advertise PodIP addresses to your on-prem router if you're making your
pods routable using BGP, which is supported for
both Cilium and Calico. You also need to ensure that those ENI, those EKS cluster ENI security groups allow for bi-directional communication between the control plane
and your on-prem environment. We're really excited to see how
you all use EKS Hybrid Nodes and where you derive the most value. One of our beta customers, Darktrace, highlighted the cross-environment
operational consistency that the solution provides. Darktrace offers an AI-based
cybersecurity platform that learns patterns
specific to each customer to provide for robust threat
protection and response. Darktrace uses Kubernetes
on-prem to provide their teams with a consistent deployment environment, taking advantage of Kubernetes
tooling for observability application scaling and disaster recovery. And instead of creating
cross-site clusters and administering their
control plane themselves, Darktrace decided to use EKS Hybrid Nodes to unify Kubernetes management with EKS, driving higher scalability,
availability and efficiency. Now, let's touch on some EKS
Hybrid Nodes best practices. To automate node bootstrap, include nodeadm in your
golden operating system images and optionally set it
to run at host startup as a systemd service. To limit latency between the control plane and your environment,
create your EKS cluster in the region that's closest
to your hybrid location, to your data center or
to your edge location. For best performance, we
recommend minimum bandwidth of 100 megabits per second. and maximum roundtrip
latency of 200 milliseconds. Although these parameters
really depend on your use case, how you're using Hybrid Nodes. And it's very much recommended that you perform your own network testing. Factors like image size and
how many nodes you're running very much impact latency, so work closely with
your networking teams. Next, leverage AWS services
by utilizing compatible EKS add-ons for monitoring,
logging and identity management. And one thing I didn't
mention about nodeadm is that it creates a label
on each of your Hybrid Nodes. That's compute-type equals hybrid. You can use this label to target workloads at or away from your Hybrid Nodes when you're using mixed mode clusters that include both Hybrid
Nodes and cloud nodes in a single cluster. And lastly, and most important,
probably most importantly, throughout the process of getting
started with Hybrid Nodes, work very closely with your
networking and security teams to ensure your firewall rules
and your security groups allow the bi-directional
communication that's required from your on-prem or edge
locations into the AWS region for the control plane
and other AWS services that you might want to
integrate with Hybrid Nodes. All right, before we go, let's touch on a simple decision tree for how you could decide
which EKS hybrid solution best meets your needs,
best suits your use case. So you have to ask yourself
a couple of questions. First, do I already have
AWS Outposts running on-prem or am I considering an
infrastructure refresh? If the answer to this question is yes, then running EKS on Outpost is gonna provide the most
consistent experience with running EKS nodes in the cloud and the tightest integration with AWS. If your answer is no, ask yourself, do I need an air-gapped environment? Do I need an air-gap solution? If you don't, then EKS Hybrid Nodes is gonna provide you with the most value by offloading responsibility for control plane management to AWS while allowing you to continue to run on your existing hardware. If you do need an air-gapped solution, then EKS Anywhere is gonna
be the best choice for you. Now, how can you learn more about EKS through the rest of
re:Invent and thereafter? First, go and attend these
other amazing sessions on the Kubernetes track. At KUB402, you're gonna learn
about various architectures for building and deploying
workloads on Amazon EKS with Amazon ECR and automations. KUB320 is gonna focus on how organizations build petabyte scale data
processing pipelines on EKS. And at KUB201, you'll hear from Amazon
Kubernetes product leadership about the latest
innovations and strategies for building platforms and applications with Kubernetes faster. We also encourage you to attend sessions on the hybrid and edge
track such as HYB301. And if you're interested in a session that you can't attend in person, footage for most sessions
will be available on YouTube within a couple of days of
those sessions taking place, specifically for breakout sessions. After re:Invent, you can continue
your EKS learning journey by taking the EKS workshop, working through the EKS
best practices guide. Please take a look at the EKS
Hybrid Nodes documentation. The team spent a ton of work on it and there's a ton of
great content out there. You can also review session materials for AWS re:Invent sessions
at this QR code and URL here. This slide deck materials for this session are gonna be available at this QR code and at this GitHub URL. Give you a second to take
photos if you want to. All right, so thank you very
much for attending the session. I hope you got a lot out of it, I hope you learned a thing or two. As you continue your journey modernizing your on-prem infrastructure, please don't hesitate to
reach out to me or Gokul. Our email addresses are
up on the screen here. And we also encourage
you to please complete the session survey in
the mobile application. It helps us see how we're doing and how we can do better
for future sessions.

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=0s) - Welcome to the session.

[00:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=1s) This is "KUB310,

[00:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=2s) Amazon EKS for edge and hybrid use cases."

[00:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=6s) My name is Eric Chapman.

[00:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=7s) I'm a Senior Product Manager
on the Amazon EKS team

[00:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=11s) focused on hybrid and edge.

[00:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=12s) And I'm here today with my
colleague Gokul Chandra,

[00:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=15s) who's a Container Specialist
Solutions Architect,

[00:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=18s) focused on bringing our EKS
hybrid and edge solutions

[00:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=21s) to customers in the telco vertical.

[00:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=24s) Today, we're gonna dive deep

[00:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=25s) on how the Amazon Elastic
Kubernetes Service, or EKS,

[00:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=30s) can help alleviate some of the challenges

[00:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=31s) faced by customers running
with a hybrid strategy;

[00:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=34s) that is deploying workloads at the edge

[00:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=37s) and on-premises,

[00:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=38s) as well as running on AWS.

[00:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=41s) We're gonna start by laying out

[00:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=42s) some of the common challenges

[00:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=44s) faced by customers running
across environments.

[00:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=47s) We'll lay out how
standardization can help,

[00:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=49s) and why more and more customers
continue to turn Kubernetes

[00:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=52s) as their standard platform,

[00:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=53s) and what challenges
remain once they do so.

[00:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=56s) We'll lay out what we're
doing on the Amazon EKS team

[00:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=59s) to help make it simpler, more
efficient, and more consistent

[01:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=63s) to deploy Kubernetes
across your environments.

[01:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=66s) We'll review architectures
and best practices

[01:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=68s) for each of our EKS hybrid solutions.

[01:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=71s) And we'll close with how
you can learn more about EKS

[01:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=74s) during re:Invent and thereafter.

[01:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=78s) Let's start with a scenario that brings in

[01:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=80s) many of the reasons that our customers opt

[01:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=82s) for a hybrid approach to begin with,

[01:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=84s) and the challenges that
arise once they do.

[01:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=87s) Say you're a platform engineering manager

[01:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=90s) at an enterprise with
multiple business lines.

[01:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=93s) You've standardized your cloud
operations on Kubernetes,

[01:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=96s) running EKS on AWS;

[01:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=99s) and many of your applications
are cloud native,

[01:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=101s) integrating with AWS services

[01:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=103s) for networking, storage and databases.

[01:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=106s) However, you still have a large suite

[01:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=107s) of applications that run on-prem

[01:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=109s) and will continue to run
on-prem for the near future.

[01:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=112s) Some of these are tightly integrated

[01:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=114s) with legacy technologies
that are gonna be difficult

[01:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=116s) to extract and pull into the cloud.

[01:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=118s) Others require compute running in close

[02:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=120s) physical proximity to end systems,

[02:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=123s) or need to run at the edge
for high performance latency.

[02:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=126s) Other applications still handle

[02:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=128s) highly sensitive customer data

[02:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=130s) and face strict data
residency requirements.

[02:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=133s) These applications run
on different systems

[02:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=135s) with different operational models

[02:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=138s) and different skillset requirements,

[02:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=139s) leading to unscalable
silos across your teams.

[02:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=143s) Instead of focusing on
improving platform performance

[02:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=146s) or adding capabilities for your platform

[02:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=148s) that can help your
development teams innovate,

[02:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=151s) your team spends too much time

[02:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=153s) manually patching and
maintaining underlying systems

[02:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=156s) just to maintain platform
stability and business continuity.

[02:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=160s) You know that if you could offload

[02:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=161s) some of the undifferentiated
overhead work,

[02:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=164s) operational work that your team does,

[02:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=166s) you could free your teams
to focus on innovating

[02:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=169s) in ways that help improve
developer experiences

[02:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=172s) and ultimately improve experiences
for your end customers.

[02:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=176s) With your applications
running on different systems

[02:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=179s) with various integrations,

[03:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=180s) there are multiple technology stacks

[03:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=182s) that you need to support.

[03:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=184s) Supporting multiple technology stacks,

[03:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=185s) such technology sprawl leads
to several other challenges.

[03:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=190s) For one, it hinders your
ability to innovate rapidly

[03:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=193s) for your development teams,

[03:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=194s) and it limits the ROI of
each individual improvement,

[03:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=199s) as improvements to one technology stack

[03:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=202s) aren't inherited by the others.

[03:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=204s) The difficulty in making changes quickly

[03:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=206s) arises from a proliferation
of manual processes,

[03:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=209s) out-of-date versions,

[03:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=211s) and strict coupling
with other dependencies.

[03:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=214s) Furthermore, each technology stack

[03:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=216s) requires different skillsets

[03:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=218s) that don't necessarily
translate across environments

[03:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=220s) and you've had to expand your team

[03:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=222s) just to maintain your
platform in steady state.

[03:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=225s) You think that if you could standardize

[03:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=226s) on a single platform,

[03:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=228s) you'd unlock your team's
ability to innovate.

[03:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=231s) With the explosion of popularity,

[03:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=233s) and popularity of Kubernetes in the cloud,

[03:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=235s) we see more and more customers

[03:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=237s) that are running across
on-prem and cloud environments

[04:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=240s) standardizing on Kubernetes,

[04:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=242s) integrating with consistent
tooling wherever they run.

[04:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=246s) Say you chose Kubernetes

[04:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=247s) as your container management
platform in the cloud

[04:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=250s) to ensure high availability

[04:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=251s) and scalability of your
mission-critical applications.

[04:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=255s) The open and extensible
nature of Kubernetes

[04:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=258s) stimulated the development of
a healthy ecosystem of tooling

[04:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=262s) and innovative practices like GitOps

[04:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=264s) that your teams can readily adopt.

[04:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=265s) And as Kubernetes is an
open source standard,

[04:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=268s) you could run it across your environments

[04:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=270s) wherever your applications need to run.

[04:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=272s) In fact, let's say many
of your application teams

[04:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=274s) running on-prem have
adopted Kubernetes already.

[04:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=277s) And while you've seen some of the benefits

[04:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=279s) of such standardization,

[04:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=281s) operational overhead continues to hinder

[04:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=283s) your team's ability to innovate.

[04:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=285s) While your development resources
have become more fungible

[04:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=288s) across your environments
given this standardization,

[04:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=291s) there remains a very steep learning curve

[04:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=294s) for those tasked with administering

[04:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=295s) your Kubernetes clusters.

[04:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=297s) Maybe you underestimated the complexity

[05:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=300s) of managing the Kubernetes
control planes themselves,

[05:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=302s) keeping your clusters healthy,

[05:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=304s) rotating certificates on a timely basis,

[05:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=306s) and making sure DHCP
IP leases don't expire.

[05:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=309s) It's also been more challenging
than you've expected

[05:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=312s) to continually scale up and
scale down your control planes

[05:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=315s) as your workloads scale
across your fleet of clusters.

[05:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=319s) These are many of the same challenges

[05:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=320s) that led you to choose EKS in the cloud,

[05:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=323s) and many reasons that
customers running across clouds

[05:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=326s) opt for managed Kubernetes solutions.

[05:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=329s) EKS manages tens of millions
of clusters on an annual basis

[05:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=334s) and we continue to see rapid adoption

[05:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=337s) with 33% year over year growth

[05:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=339s) in the number of clusters managed.

[05:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=341s) Our goal on the AWS Kubernetes team

[05:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=345s) is to make the operational
aspects of running Kubernetes

[05:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=348s) an afterthought for our customers
wherever they need to run.

[05:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=351s) And since the introduction of
EKS on AWS Outposts in 2019,

[05:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=357s) one point of focus for the EKS team

[05:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=359s) is on how we could bring
EKS into hybrid environments

[06:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=362s) to provide the benefits
of a managed service

[06:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=364s) and to enable you to establish
operational consistency

[06:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=367s) across your environments.

[06:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=370s) I'm sure many of you know
but for those that don't,

[06:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=372s) AWS Outposts is AWS managed infrastructure

[06:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=375s) that extends AWS services

[06:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=378s) into your data center or colo facility,

[06:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=380s) including EC2 for compute,

[06:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=382s) S3 and EBS for storage

[06:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=384s) and VPC for networking.

[06:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=386s) EKS has been available on Outposts

[06:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=390s) since Outposts' general
availability in 2019.

[06:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=393s) And given the availability of these other

[06:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=395s) AWS services on Outpost

[06:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=397s) and Kubernetes control plane

[06:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=398s) managed for you in the cloud by EKS,

[06:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=401s) running EKS nodes on Outpost

[06:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=403s) is gonna provide the most
consistent experience

[06:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=405s) with running EKS nodes in region,

[06:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=407s) and the tightest integration with AWS.

[06:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=411s) We've seen Outpost customers adopt EKS

[06:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=415s) for use cases like
general purpose automation

[06:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=417s) and use cases that require
local data processing

[07:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=420s) such as banking or real money gaming,

[07:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=422s) just to name a few use cases.

[07:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=425s) Customers love the operational
consistency that they get

[07:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=429s) when they run EKS on Outpost

[07:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=430s) as compared to running EKS in the region.

[07:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=433s) Now at any given point, many
customers aren't in a position

[07:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=436s) to refresh their
on-premises infrastructure.

[07:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=439s) And so, to meet customers where they are,

[07:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=441s) in 2021, we launched Amazon EKS Anywhere.

[07:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=445s) EKS Anywhere provides AWS supported

[07:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=448s) Kubernetes management software

[07:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=450s) that simplifies the
infrastructure provisioning

[07:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=452s) and lifecycle management process

[07:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=454s) for clusters running on
customer managed hardware

[07:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=457s) and virtualized and
bare-metal environments.

[07:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=460s) EKSA is a fully customer managed solution

[07:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=463s) with infrastructure providers,
Kubernetes' components,

[07:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=466s) and operating systems
tested and supported by AWS.

[07:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=471s) An EKSA subscription also
comes with AWS support

[07:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=475s) for a curated set of add-on packages

[07:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=478s) that extend core Kubernetes functionality

[08:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=480s) for load balancing, ingress
monitoring and more.

[08:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=484s) EKSA is especially popular with customers

[08:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=488s) that have stricter requirements

[08:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=489s) around their on-premises networking

[08:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=492s) or need to operate in
locations with disconnected,

[08:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=494s) disrupted, intermittent and
limited network connectivity.

[08:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=499s) Such use cases include telco applications

[08:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=502s) that need to run on bare-metal
at the far network edge,

[08:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=506s) financial services apps that face stricter

[08:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=509s) networking and regulatory requirements,

[08:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=511s) and applications run by
travel and hospitality firms,

[08:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=514s) operating cruise ships that may not have

[08:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=516s) internet connectivity for
days or weeks at a time.

[08:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=520s) We've enhanced EKS
Anywhere for compatibility

[08:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=523s) with key telco ISV solutions.

[08:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=526s) And in a couple of slides here,

[08:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=528s) Gokul is gonna run us
through the architecture

[08:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=530s) that one of our large telco customers uses

[08:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=533s) to run their 5G O-RAN workload on EKSA.

[08:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=537s) So customers really love
that they could continue

[08:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=539s) to run on their own hardware
when they choose EKSA,

[09:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=544s) take advantage of the investment

[09:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=545s) they've already made on-prem.

[09:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=547s) And customers really love
that with EKS on Outpost,

[09:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=550s) they get the Kubernetes control plane

[09:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=551s) managed for them in the cloud by EKS.

[09:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=554s) In speaking with dozens
and dozens of customers,

[09:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=556s) it became clear to us that
there is a need for a solution

[09:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=559s) that would enable customers to continue

[09:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=561s) to run on their existing hardware

[09:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=563s) without requiring them to
manage the control plane.

[09:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=566s) And that's why we're so excited on Sunday

[09:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=568s) to announce the general
availability of EKS Hybrid Nodes.

[09:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=572s) A new EKS feature that enables you

[09:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=574s) to run Kubernetes nodes
on your existing hardware

[09:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=577s) and attach it to the EKS control
plane running in the cloud.

[09:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=580s) EKS Hybrid Nodes creates a more

[09:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=582s) consistent operating experience

[09:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=584s) between running EKS in the
cloud and running on-prem.

[09:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=587s) And with Hybrid Nodes,

[09:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=589s) we take on the operational responsibility

[09:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=592s) for managing the Kubernetes control plane

[09:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=594s) while allowing you to continue

[09:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=595s) running your workloads on-prem,

[09:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=597s) taking advantage of that on-prem

[09:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=598s) hardware investment you've already made.

[10:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=601s) Now you can conserve
your on-premises capacity

[10:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=604s) strictly for your application workloads.

[10:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=606s) And like with EKS in the cloud,

[10:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=607s) you don't have to worry about scaling

[10:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=609s) up and down your
Kubernetes control planes.

[10:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=611s) That's all managed for you by EKS.

[10:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=613s) EKS Hybrid Nodes is the
best choice for customers

[10:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=617s) whose on-prem or edge
locations can network with AWS,

[10:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=621s) and we think it's going
to be the best choice

[10:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=623s) and the sweet spot for
most hybrid customers.

[10:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=627s) We expect that Hybrid
Nodes will be especially

[10:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=629s) popular for distributed edge use cases

[10:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=632s) like media streaming and manufacturing,

[10:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=634s) as well as general
enterprise modernization.

[10:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=637s) And many of the same use cases customers

[10:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=639s) use EKS on Outpost for today.

[10:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=642s) EKS Hybrid Nodes,

[10:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=643s) or EKS clusters with Hybrid Nodes rather,

[10:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=646s) can also run cloud nodes
in a single cluster,

[10:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=649s) opening the door for AI and ML use cases

[10:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=652s) that use GPUs on-prem and in the cloud

[10:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=655s) to bolster their training capacity

[10:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=657s) or for inference bursting.

[10:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=659s) I'm extremely excited to talk to you

[11:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=661s) more about EKS Hybrid Nodes

[11:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=662s) and I hope you're excited to
learn more about the details.

[11:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=664s) But before we get there, I'm
gonna hand it off to Gokul

[11:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=667s) who's gonna dive deeper for us

[11:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=668s) on EKS on Outposts and EKS Anywhere.

[11:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=673s) - Thank you, Eric.

[11:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=674s) So let's talk about how AWS Outposts today

[11:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=679s) can supercharge your
on-premises infrastructure

[11:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=682s) with Amazon EKS.

[11:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=683s) So, customers usually deploy

[11:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=685s) Kubernetes clusters and pods on premises

[11:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=689s) in order to reduce the latency

[11:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=692s) and also enhance the security.

[11:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=694s) And there are multiple other use cases

[11:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=697s) where the hybrid capacity

[11:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=700s) is not a requirement but a mandate.

[11:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=703s) So whether extending your cluster

[11:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=705s) to your on-premises
environment from the cloud

[11:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=708s) or even managing your
hybrid compute capacity

[11:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=712s) or hybrid computing platform design,

[11:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=714s) so AWS Outpost covers you
for all those use cases.

[11:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=718s) When it comes to deploying

[12:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=721s) Amazon EKS clusters on AWS Outpost,

[12:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=723s) we support two deployment options here.

[12:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=726s) The first one is the extended clusters

[12:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=728s) where you can start by creating the EKS

[12:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=732s) cloud-based control plane

[12:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=733s) in the same way that you do

[12:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=735s) with the regional-based clusters.

[12:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=737s) Then you deploy the cluster nodes,

[12:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=739s) which are the Kubernetes nodes,

[12:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=741s) which host your actual workloads
within the hybrid model

[12:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=745s) like on the AWS Outpost
rack that is shipped

[12:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=748s) and connected back to the region
from your own data center.

[12:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=751s) And this is called the
extended cluster approach.

[12:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=754s) But with this approach, what
you will be getting here

[12:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=757s) is the same managed
Kubernetes control plane,

[12:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=760s) which is completely managed by AWS,

[12:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=763s) and an integrated experience
with other ecosystem

[12:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=766s) of services that are
available today in the region.

[12:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=769s) So the second model is the local clusters.

[12:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=772s) So this is aimed at specific use cases

[12:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=774s) where we have listened to our customers,

[12:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=777s) where some of our customers
have their environments

[13:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=780s) or deployment setting where they can have

[13:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=784s) the unreliable network connectivity.

[13:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=787s) Means they might have disruptions
because of so many reasons

[13:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=790s) because of the placement
of the data centers

[13:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=793s) in the penultimate regions of a metro

[13:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=796s) or even in an isolated environment

[13:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=799s) where they have issues with the continuous

[13:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=802s) network availability,

[13:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=804s) where it is required for the
AWS Outposts with EKS to run.

[13:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=808s) So this is where we introduced the second

[13:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=810s) deployment option called local clusters,

[13:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=813s) which enables customers to still continue

[13:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=817s) their Kubernetes-based operations

[13:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=819s) even during the course of disconnects.

[13:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=821s) So with this model, what EKS does is,

[13:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=824s) it deploys a local control
plane, the EKS control plane,

[13:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=828s) on your AWS Outpost rack itself.

[13:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=830s) And during the course of
disconnect to the region

[13:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=834s) for the EKS control plane
that we manage in the region,

[13:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=837s) still the customers can continue

[13:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=839s) to manage the Kubernetes-based operations

[14:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=842s) without having any kind of
disruptions to their workloads.

[14:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=846s) So this is aimed at
specific use cases as said,

[14:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=849s) while local clusters can provide
this extended functionality

[14:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=854s) where customers can still
continue to run their workloads

[14:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=859s) without any kind of disruptions.

[14:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=861s) Extended clusters, the first option,

[14:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=864s) remains the recommended
option from the AWS end

[14:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=866s) because it provides a more integrated

[14:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=869s) and a managed experience to the customers,

[14:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=872s) where the Kubernetes control plane

[14:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=874s) is completely managed by AWS.

[14:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=876s) And also, there are multiple
ecosystem of services

[14:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=880s) that are available within the cloud

[14:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=882s) where customers can directly use them

[14:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=884s) to enhance their overall portfolio

[14:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=887s) or their overall workload portfolio too.

[14:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=891s) So, let us see how the
architecture is laid out

[14:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=895s) for the extended clusters
that we have just discussed.

[14:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=898s) So customers start by
ordering an Outpost rack.

[15:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=903s) And this AWS Outpost rack will be shipped

[15:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=905s) to customers' own data center

[15:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=907s) that gets connected back to the region

[15:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=910s) using a service link approach.

[15:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=912s) And service link in turn
uses a direct connect service

[15:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=915s) that is offered by AWS.

[15:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=917s) And this connectivity
provides a high throughput

[15:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=920s) secure connectivity back to the region

[15:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=922s) from your Outpost environment.

[15:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=925s) Then customers can create

[15:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=928s) the VPC, the networking.

[15:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=930s) Like when it comes to networking,

[15:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=931s) the networks are created
in a similar fashion

[15:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=934s) what they do today with
the region-based approach.

[15:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=937s) They can create a VPC with
multiple subnets spanning across

[15:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=941s) multiple availability
zones within the region.

[15:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=944s) Now the difference that
makes like with AWS Outposts

[15:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=948s) is that with AWS Outposts

[15:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=951s) registered to your own account

[15:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=952s) and placed within your data center,

[15:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=955s) the same VPC that has been
created within the region

[15:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=959s) can be extended to this Outpost rack.

[16:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=961s) Means you can create multiple
subnets within the same VPC,

[16:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=966s) selecting your Outposts
as the availability zone.

[16:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=969s) So this enables the
extendability of the network

[16:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=973s) from the cloud to your own data center

[16:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=976s) using the constructs
that we enable seamlessly

[16:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=978s) with AWS Outposts.

[16:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=980s) So once you have this
networking layout established,

[16:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=984s) you can create the EKS
control plane the same way

[16:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=987s) that you do with the
cloud-based clusters today.

[16:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=990s) So here, it's important to note that

[16:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=993s) the EKS control plane is
created in the region,

[16:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=997s) and the control plane anchors
to the region-based subnets

[16:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=1001s) using Cross-Account ENI architecture

[16:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=1004s) where the EKS control plane
is completely managed by AWS.

[16:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=1008s) So this gets anchored to the
subnets within the same VPC

[16:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=1012s) that you have extended to
the Outpost infrastructure.

[16:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=1015s) And once you have the control
plane deployed the same way

[16:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=1018s) as you do with any other
regional based clusters today,

[17:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=1021s) then you have an extended approach

[17:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=1024s) like with everything
that gets from the cloud

[17:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=1028s) to your Outpost environment.

[17:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=1030s) So here,

[17:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=1033s) once you have this whole infrastructure

[17:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=1036s) with EKS control plane,

[17:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=1038s) then you start by creating
self-managed node groups

[17:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=1042s) within the same Outpost subnets

[17:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=1045s) that you have extended to
your own infrastructure

[17:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=1048s) that is positioned
within your data centers.

[17:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=1050s) So it's important to note that

[17:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=1053s) that EKS control plane

[17:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=1054s) can be created with the
region-based subnets,

[17:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=1057s) but your actual Kubernetes nodes

[17:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=1060s) will be running within the subnets

[17:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=1062s) that are positioned in
the Outpost environment.

[17:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=1066s) So the self-managed node group,

[17:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=1068s) which is a Kubernetes node group

[17:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=1071s) which constitutes multiple nodes,

[17:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=1074s) technically these are the EC2 instances

[17:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=1076s) because AWS Outpost rack
has multiple services

[17:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=1079s) that are offered today as
part of the AWS portfolio

[18:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=1083s) where you can run your EC2 instances

[18:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=1085s) which are your Kubernetes
nodes technically

[18:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=1088s) on your own environment
like without having to rely

[18:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=1091s) on the region-based EC2 services.

[18:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=1094s) So this enables the customers to deploy

[18:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=1098s) your actual workloads running
on the Kubernetes nodes,

[18:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=1101s) which are positioned on the Outpost rack,

[18:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=1104s) which in turn is positioned
within your own data center.

[18:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=1109s) So, usually when you
deploy the applications

[18:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=1115s) within this Outpost environment,

[18:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=1117s) definitely you might
have another environment

[18:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=1120s) or portfolio with full set of applications

[18:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=1122s) that you have already been running

[18:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=1125s) within your own data center environments.

[18:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=1127s) So we provide a construct
called local gateway

[18:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=1130s) where local gateway access the gateway

[18:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=1133s) to enable the communication
between the applications

[18:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=1136s) that are running on this EKS environment

[18:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=1139s) to talk to your own
applications running on

[19:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=1141s) any other data center infrastructure
that you already have.

[19:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=1145s) So it enables seamless connectivity

[19:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=1149s) so that you can stitch the
application connectivity

[19:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=1152s) that is running on Outposts

[19:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=1154s) with your own infrastructure components

[19:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=1156s) that are running within your data center.

[19:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=1160s) Now so far, we have discussed

[19:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=1164s) how customers can leverage AWS Outposts,

[19:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=1167s) that is, AWS provided
and managed hardware;

[19:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=1171s) and deploy EKS clusters on them

[19:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=1173s) so that you can extend
your application portfolio

[19:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=1177s) from cloud to your own data center.

[19:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=1179s) But what if customers want
to run the applications

[19:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=1183s) on their own hardware?

[19:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=1185s) Technically the COTS-based
hardware that they have procured.

[19:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=1188s) Or many customers have made
significant investments

[19:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=1192s) in their data center hardware

[19:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=1194s) where they already have this hardware

[19:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=1196s) sitting in their own data centers.

[19:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=1198s) Or the second thing important
aspect to discuss here

[20:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=1202s) about the requirements may be is like,

[20:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=1205s) what if a customer wants
to deploy the clusters

[20:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=1208s) in a completely isolated environment?

[20:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=1210s) When we say completely isolated,

[20:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=1212s) they don't want to have a
region-based connectivity

[20:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=1215s) or they don't want any
internet connectivity

[20:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=1218s) going out of their environments.

[20:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=1220s) That is where EKS Anywhere
comes into picture.

[20:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=1223s) So EKS Anywhere enables
customers to deploy

[20:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=1227s) Kubernetes clusters on their
own COTS-based hardware

[20:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=1232s) or existing virtualized environments

[20:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=1235s) that they are already managing
such as VMware, CloudStack.

[20:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=1239s) So this enables to deploy
clusters with the same consistency

[20:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=1244s) as you see with the
region-based KS clusters.

[20:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=1248s) So this is about EKS Anywhere.

[20:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=1251s) Now let us see how EKS Anywhere
architecture looks like.

[20:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=1255s) So it's a complete stack of components

[20:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=1258s) that form up the full
stack of EKS Anywhere

[21:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=1261s) as a consistent Kubernetes
platform that is provided by AWS.

[21:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=1267s) So the first one is the
infrastructure providers, right?

[21:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=1270s) Even before going here,

[21:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=1272s) we have to emphasize on the fact that

[21:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=1274s) EKS Anywhere is designed

[21:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=1276s) based on the Cluster API foundations.

[21:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=1279s) So Cluster API is a Kubernetes
sub-project that standardizes

[21:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=1284s) and simplifies the cluster
lifecycle management.

[21:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=1287s) So EKS Anywhere inherits a
lot of different architectural

[21:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=1292s) patterns from Cluster API,
in short called as CAPI,

[21:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=1296s) across the community.

[21:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=1298s) So, the infrastructure providers means

[21:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=1302s) EKS Anywhere can be deployed

[21:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=1303s) on all these options that we show here.

[21:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=1306s) So it can be deployed
on bare-metal servers

[21:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=1308s) where you can completely
use your bare-metal servers

[21:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=1311s) to deploy the EKS Anywhere
clusters on top of them.

[21:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=1315s) Especially with bare-metal approach,

[21:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=1317s) we not only support deploying clusters

[22:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=1320s) but we have also taken the
undifferentiated heavy lifting

[22:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=1323s) of imaging and managing the service

[22:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=1326s) to using a Tinkerbell component.

[22:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=1328s) So Tinkerbell is a open source project

[22:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=1332s) where AWS heavily contributed
to this particular project

[22:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=1335s) to make it Kubernetes native
or cloud native in general.

[22:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=1338s) And the second set of
infrastructure providers

[22:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=1342s) are your virtualized environments.

[22:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=1344s) What it means is that,

[22:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=1346s) if you already have
your VMware environments

[22:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=1350s) or CloudStack environments,

[22:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=1351s) you can use this existing
virtualized layer

[22:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=1355s) which manages the virtual machines

[22:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=1357s) and you can deploy EKS
Anywhere on top of them.

[22:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=1360s) Where we provide the full set

[22:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=1363s) of capabilities for the customers

[22:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=1365s) to have an end-to-end experience

[22:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=1367s) with a seamless automated
approach of creating clusters

[22:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=1370s) on top of your virtualized environments.

[22:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=1372s) And also, we do support
our partner environments

[22:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=1376s) such as Nutanix.

[22:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=1378s) And also we do have a
full set of capabilities

[23:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=1381s) to deploy EKS Anywhere clusters on Snow,

[23:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=1384s) which is our edge-based device

[23:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=1387s) like which is provided by AWS.

[23:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=1389s) So these are the infrastructure providers

[23:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=1392s) where EKS Anywhere can be deployed on.

[23:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=1395s) The next layer is the
Kubernetes distribution.

[23:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=1398s) So the Kubernetes distribution

[23:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=1399s) that is being used with EKS Anywhere

[23:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=1401s) is called the EKS Distro,

[23:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=1404s) which is the EKS
distribution of Kubernetes.

[23:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=1407s) And one important thing
to note here is that

[23:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=1409s) this is the same Kubernetes distribution

[23:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=1412s) that is used across the board.

[23:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=1415s) Means it is now powering millions
of clusters in the region

[23:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=1420s) where already customers are
using it at a production scale.

[23:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=1424s) So what exactly this distribution provides

[23:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=1427s) or enables users is to
just like rely on AWS,

[23:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=1431s) where AWS holds the responsibility

[23:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=1433s) in maintaining the security patching

[23:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=1435s) and also building the base images

[23:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=1437s) for coming up with this distribution

[24:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=1440s) so that you're ready to go
deploying these clusters

[24:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=1443s) without having to worry
about spending cycles

[24:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=1446s) on the security patching, CVE analysis,

[24:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=1449s) vulnerability analysis and all.

[24:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=1451s) So this is the EKS distribution

[24:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=1453s) which is called the EKS Distro.

[24:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=1456s) Next comes the layer of
cluster lifecycle management

[24:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=1459s) and cluster operations,

[24:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=1461s) and also the CNI,

[24:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=1462s) which is the Container
Networking Interface,

[24:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=1464s) which provides the baseline connectivity

[24:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=1466s) for your pods and services that run

[24:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=1468s) on top of your Kubernetes environment.

[24:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=1471s) So, EKS Anywhere comes packaged
with a set of controllers

[24:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=1477s) that enables seamless operations

[24:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=1479s) to create, delete, upgrade,
update, add, delete nodes.

[24:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=1486s) And all these operations
are provided by the set

[24:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=1488s) of controllers that comes
packaged with EKS Anywhere.

[24:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=1492s) And, on the other hand,

[24:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=1494s) the packaged or the main CNI,

[24:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=1498s) or I mean the supported CNI
with EKS Anywhere, is Cilium.

[25:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=1503s) So there is a very big
differentiation factor here.

[25:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=1506s) If the people here are familiar

[25:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=1508s) with how EKS works in the region,

[25:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=1511s) we have AWS VPC CNI

[25:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=1513s) that provides flat networking
model within the region.

[25:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=1516s) But with EKS Anywhere, as said,

[25:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=1519s) this is a completely and isolated option

[25:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=1521s) that runs within your own data center.

[25:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=1523s) We cannot use AWS VPC CNI,

[25:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=1526s) as similar to the other
option we have just discussed;

[25:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=1529s) that is the EKS on Outposts.

[25:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=1531s) Still EKS on Outposts
uses the VPC construct.

[25:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=1535s) So we use VPC CNI for Kubernetes.

[25:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=1537s) But with EKS Anywhere,

[25:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=1538s) because it's completely out of AWS control

[25:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=1542s) and it is positioned within
the customer's own data center,

[25:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=1545s) on your own hardware,

[25:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=1546s) and you will be utilizing
your own network there,

[25:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=1549s) so that is where we package Cilium

[25:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=1552s) as the go-to CNI with EKS Anywhere.

[25:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=1556s) Next comes the layer of the
operations and tooling, right?

[26:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=1560s) See, just creating EKS clusters
or Kubernetes environments

[26:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=1563s) is not alone enough to
run your full-fledged

[26:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=1567s) application portfolio.

[26:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=1569s) You need certain set of tools or tooling

[26:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=1572s) that has to be deployed on
your Kubernetes environments

[26:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=1576s) to carry out multiple
activities that are required

[26:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=1580s) for your end applications to
be available for the end users.

[26:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=1583s) So, for example, it can
be the load balances,

[26:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=1587s) it can be the ingress,

[26:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=1589s) it can be your image registries.

[26:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=1592s) So all these tooling are needed.

[26:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=1594s) And what we heard from
our customers is, like,

[26:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=1597s) if they're consuming this directly

[26:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=1599s) from the upstream communities,

[26:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=1601s) they have to rely on the
community-based support.

[26:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=1605s) Or the second model is,
if any of these components

[26:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=1608s) are available through our partner network

[26:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=1610s) or from some enterprise vendor,

[26:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=1613s) they have to go to that
particular enterprise vendor

[26:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=1616s) to get the support for
these particular components.

[26:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=1619s) So that is where we came up with something

[27:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=1621s) called Curated Packages

[27:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=1623s) where we enable customers to
use some pre-curated packages

[27:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=1629s) which are like designed
and also defined by AWS,

[27:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=1634s) where AWS holds the responsibility

[27:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=1636s) of managing these components too

[27:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=1638s) on your Kubernetes environments.

[27:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=1640s) For example, let us take
Harbor, Emissary, MetalLB;

[27:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=1643s) all these are very well-known

[27:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=1645s) open source community based projects.

[27:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=1647s) So whenever you use Curated Packages,

[27:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=1650s) you don't have to worry
about maintaining them

[27:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=1653s) and also maintaining
the version capabilities

[27:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=1656s) and also compatibility with the specific

[27:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=1658s) Kubernetes version that
you are running on.

[27:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=1660s) And AWS provides the full-fledged support

[27:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=1663s) in managing these particular add-ons

[27:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=1665s) on top of the EKS environments.

[27:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=1668s) So that is the value that we have provided

[27:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=1670s) with Curated Packages.

[27:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=1672s) And another important aspect here is that,

[27:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=1674s) so from the security perspective,

[27:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=1677s) if you are using a specific
add-on on Kubernetes

[28:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=1680s) and if it has some kind
of security vulnerability,

[28:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=1683s) today, if you're consuming it directly

[28:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=1685s) from open source or upstream,

[28:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=1687s) you have to wait on the community

[28:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=1690s) to enable you with a patched version.

[28:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=1692s) But that is not the case
with Curated Packages

[28:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=1695s) that are available with EKS Anywhere,

[28:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=1697s) where AWS holds the responsibility

[28:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=1699s) and also provides the full-fledged support

[28:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=1704s) for any of these add-ons

[28:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=1706s) that are available in the portfolio.

[28:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=1707s) And AWS is responsible for managing

[28:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=1710s) the code of all these add-ons too.

[28:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=1713s) So that is the Curated Package layer

[28:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=1716s) that comes with EKS Anywhere.

[28:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=1719s) Next, you can create and
manage EKS clusters today

[28:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=1723s) in a few different ways, right?

[28:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=1725s) So the first model is eksctl CLI.

[28:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=1728s) So, we provide a
comprehensive CLI mechanism.

[28:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=1731s) And here it's very important to note,

[28:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=1733s) like if people are familiar here

[28:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=1735s) with how EKS clusters
in the region operate,

[28:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=1739s) we have a consistent API endpoint,

[29:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=1741s) where it acts as a vending
machine for Kubernetes clusters.

[29:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=1745s) And you can directly
call this API endpoint

[29:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=1747s) with AWS CLI or infrastructure
as a code tooling,

[29:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=1750s) which in turn triggers the creation

[29:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=1753s) of EKS clusters in the region.

[29:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=1755s) But that is not the case
with EKS Anywhere, right?

[29:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=1757s) Because it's sitting
in your own data center

[29:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=1760s) and it's operated by the customer.

[29:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=1762s) So that is where we provide
the same consistent experience

[29:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=1767s) using a comprehensive set of CLI options

[29:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=1769s) that are available with eksctl CLI.

[29:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=1772s) So eksctl CLI used to be our approach

[29:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=1776s) of creating clusters within
the region from start.

[29:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=1779s) And eksctl CLI, we added an
extension called Anywhere

[29:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=1783s) which provides the capabilities to operate

[29:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=1787s) and manage clusters within
your own environments.

[29:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=1789s) So the same set of tooling

[29:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=1791s) but we integrated or extended the approach

[29:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=1794s) to even control the clusters
and manage the clusters

[29:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=1797s) on-premises on your own hardware.

[29:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=1799s) The second option is Terraform, right?

[30:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=1800s) If you're a fan of the infrastructure

[30:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=1802s) as a code like tooling,

[30:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=1804s) we provide a custom
Terraform operator provider,

[30:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=1809s) for creating and managing
EKS Anywhere clusters.

[30:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=1812s) The third approach, which
is our recommended approach,

[30:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=1815s) where we briefly discussed about

[30:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=1817s) how EKS Anywhere inherits
a lot of different

[30:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=1821s) architectural patterns from CAPI.

[30:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=1823s) So we recommend this approach

[30:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=1825s) where you can completely
manage your clusters

[30:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=1828s) with a GitOps-based fashion,

[30:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=1830s) having the whole cluster configuration

[30:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=1833s) stored in a Git repository.

[30:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=1835s) And with EKS Anywhere,

[30:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=1836s) one of the packages
include Flux Controller.

[30:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=1839s) Flux Controller is a prominent
GitOps-based controller

[30:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=1844s) that is available in the community.

[30:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=1845s) And we started supporting it

[30:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=1847s) and we contribute to the Flux Controller

[30:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=1849s) so that it gets packaged with EKS Anywhere

[30:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=1851s) and you can use a GitOps-based approach

[30:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=1854s) for your infrastructure.

[30:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=1856s) Again, reiterating over this point,

[30:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=1858s) we are not talking about the GitOps-based

[31:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=1860s) approach for managing your applications,

[31:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=1862s) but managing the infrastructure itself

[31:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=1864s) can be done using GitOps.

[31:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=1866s) So these are the three different ways

[31:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=1868s) that you can use for
creating the clusters.

[31:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=1871s) Next comes the region-based connectivity.

[31:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=1874s) As we alluded to multiple
different deployment options

[31:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=1879s) and also we discussed about

[31:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=1881s) how EKS Anywhere is completely different

[31:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=1883s) and it can be air-gapped and isolated

[31:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=1886s) without having to rely on the
region-based connectivity,

[31:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=1890s) still, if the customer
is interested in using

[31:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=1894s) any of the managed
services within the cloud,

[31:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=1897s) they can have optional
connectivity back to the region.

[31:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=1901s) So there are common use cases

[31:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=1902s) that we have seen among customers, right?

[31:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=1904s) For example, if they want to use a central

[31:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=1907s) single-pane observability
dashboard mechanism

[31:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=1910s) for thousands of EKS clusters today,

[31:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=1912s) so they can use the
Amazon-managed Prometheus,

[31:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=1916s) Amazon-managed Grafana that
is available in the region,

[31:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=1919s) so they can still have the optional

[32:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=1921s) cloud-based connectivity
with EKS Anywhere.

[32:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=1925s) Now, the deployment topologies.

[32:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=1927s) So, EKS Anywhere supports two different

[32:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=1931s) deployment topologies, right?

[32:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=1933s) And as the standardized
CAPI procedure involves

[32:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=1937s) having a workload and
a management cluster,

[32:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=1940s) the same approach is
available with EKS Anywhere

[32:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=1944s) where you can use a single
cluster-based option

[32:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=1948s) where customers are free to use

[32:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=1950s) the single deployment option,

[32:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=1952s) managing singleton clusters,

[32:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=1954s) which will be provisioned
with all the controllers

[32:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=1957s) on top of this cluster,

[32:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=1958s) which can manage the cluster itself.

[32:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=1961s) For example, when I say
managing the cluster itself,

[32:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=1964s) if you want to add nodes, delete
nodes, upgrade the cluster,

[32:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=1967s) all the controllers are
available on the same cluster.

[32:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=1971s) The second approach is
the management cluster

[32:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=1974s) and workload cluster approach, right?

[32:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=1976s) What it does is,

[32:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=1978s) you will have a central management cluster

[33:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=1980s) with a full set of controllers

[33:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=1983s) that are responsible
for creating, updating

[33:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=1986s) and managing the lifecycle
of the clusters, or deployed.

[33:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=1990s) And using this management
cluster as the endpoint,

[33:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=1993s) you can create and operate a
fleet of workload clusters.

[33:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=1997s) So the workload clusters are the clusters

[33:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=2000s) where the end user workloads are deployed.

[33:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=2003s) As you can see, a clear-cut
differentiation here

[33:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=2005s) between the management cluster
and the workload cluster,

[33:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=2008s) you see that the controllers
that are deployed

[33:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=2010s) on the management cluster

[33:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=2011s) are absent on the workload clusters,

[33:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=2014s) providing the resources that are required

[33:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=2017s) for your end applications,

[33:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=2018s) not consuming any resources

[33:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=2020s) for the cluster lifecycle
operations itself.

[33:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=2023s) So this is how you can manage
a fleet of workload clusters

[33:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=2027s) with a management cluster.

[33:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=2028s) We usually recommend customers having more

[33:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=2030s) than three EKS Anywhere
clusters to have this approach.

[33:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=2034s) So it provides a very concrete governance

[33:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=2037s) when managing the clusters

[33:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=2039s) and also the single-pane observability

[34:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=2041s) of the whole cluster portfolio

[34:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=2043s) within your data center environment.

[34:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=2046s) Now, the declarative options

[34:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=2048s) and the cellular cluster management,

[34:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=2050s) which is very important for
customers running hundreds

[34:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=2053s) of Kubernetes clusters in their
environments today, right?

[34:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=2057s) So,

[34:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=2059s) the interface that you use

[34:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=2061s) to create your EKS Anywhere clusters

[34:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=2063s) is a very simple YAML-based configuration.

[34:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=2067s) This is the configuration file

[34:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=2069s) where you define the
cluster specifications

[34:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=2071s) that include the name, the network name,

[34:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=2074s) and also the number of control plane nodes

[34:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=2076s) that it has to create,

[34:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=2077s) and the worker node configurations.

[34:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=2079s) Everything goes into this
YAML-based configuration.

[34:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=2082s) And as we just discussed,
the GitOps-based approach

[34:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=2086s) paired with the management
cluster topology,

[34:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=2089s) you can have a cellular
management approach

[34:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=2091s) where you can use a
specific management cluster

[34:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=2097s) to operate a fleet of workload clusters

[35:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=2100s) in a GitOps approach,

[35:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=2101s) where the management
cluster access the sync

[35:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=2105s) and then it realizes
all the configurations

[35:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=2108s) that you have provided
through a Git source

[35:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=2110s) to create and operate
multiple workload clusters.

[35:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=2114s) Lastly, the deployment options, right?

[35:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=2115s) So, when we reached out to customers,

[35:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=2119s) each customer has their
unique set of requirements

[35:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=2121s) when creating a Kubernetes cluster.

[35:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=2123s) We cannot always force them
to create a multi-node cluster

[35:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=2127s) because there might be conditions

[35:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=2129s) where they're resource-constrained.

[35:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=2131s) So that is where we support
different deployment options.

[35:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=2133s) The first one being
the multi-node approach

[35:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=2137s) where each node will be
acting as a control plane

[35:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=2140s) or a data plane node.

[35:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=2141s) Or the second one is the colocated

[35:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=2143s) master and the worker nodes

[35:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=2145s) where you can have three nodes

[35:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=2147s) with masters, high available masters;

[35:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=2150s) and also the worker node can
be running on the same machine.

[35:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=2153s) The third option is a single-node approach

[35:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=2156s) where you can run the entire
EKS Anywhere environment

[36:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=2160s) or EKS Anywhere cluster on
a single bare-metal node.

[36:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=2163s) So these are different deployment options

[36:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=2165s) we support with EKS Anywhere today.

[36:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=2168s) And particularly, we want to emphasize

[36:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=2171s) or introduce you to a specific use case

[36:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=2175s) where EKS Anywhere enabled a
Japanese-based telco customer

[36:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=2180s) to deploy their nationwide

[36:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=2184s) open radio access network
architecture across Japan,

[36:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=2188s) almost serving 90 million subscribers.

[36:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=2191s) And this particular
topology where EKS Anywhere

[36:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=2194s) is used as the container
access service option

[36:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=2198s) constitutes almost 15,000
different cell sites

[36:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=2202s) with more than 35,000 bare-metal servers,

[36:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=2205s) like including all the sites
that we have seen just now.

[36:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=2208s) So, with this particular approach,

[36:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=2211s) NTT DOCOMO is able to stretch
their cloud-based pattern

[36:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=2217s) from the region to the
penultimate regions,

[36:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=2219s) including the cell towers and cell sites.

[37:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=2222s) So,

[37:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=2225s) how exactly EKS Anywhere
enable the NTT DOCOMO?

[37:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=2228s) So NTT DOCOMO,

[37:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=2230s) as any other telco operator
in the market today,

[37:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=2234s) has a stretched topology.

[37:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=2235s) Means they have AWS regions,

[37:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=2239s) regional data centers,

[37:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=2241s) edge sites, and also cell sites.

[37:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=2243s) So what is the differentiation
factor here, right?

[37:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=2246s) So region, region is a cloud-based model.

[37:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=2249s) And then coming to regional sites,

[37:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=2251s) regional sites are standard data centers

[37:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=2255s) which have enough capacity
to host multi-node clusters.

[37:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=2259s) And edge sites are
resource-constraint environments

[37:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=2262s) where they cannot operate
a lot of different options

[37:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=2266s) like when it comes to
having a set of hardware.

[37:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=2269s) And when coming to the cell sites,

[37:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=2271s) these are the most edge
sites in a cell topology

[37:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=2275s) where they can only host
single-node clusters

[37:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=2278s) because the cell sites can only host

[38:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=2281s) a specific set of hardware
under them, like or in them.

[38:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=2284s) So this is the stretch topology

[38:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=2286s) that is usually seen
with our telco customers.

[38:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=2290s) And connecting these particular topologies

[38:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=2293s) was made easy for NTT DOCOMO

[38:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=2296s) with our Direct Connect
approach that we already have

[38:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=2300s) where they can connect the
region to until the cell site

[38:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=2304s) with the direct connectivity approach

[38:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=2306s) or Direct Connect service that
we have in the AWS portfolio

[38:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=2309s) that provides consistent,
reliable and secure connectivity

[38:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=2313s) from the region to even the
edge site or applications

[38:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=2317s) and also for the infrastructure.

[38:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=2319s) So the connectivity is not
just for the infrastructure,

[38:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=2322s) but the same backbone can be
used for the applications too.

[38:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=2325s) So with cellular management
of EKS Anywhere clusters

[38:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=2330s) that what we have seen earlier,

[38:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=2332s) NTT DOCOMO is able to create

[38:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=2335s) and manage multiple workload clusters

[38:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=2338s) with a management cluster
sitting in the regional site.

[39:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=2341s) And there are different
topologies that they have used

[39:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=2344s) because regional sites
have enough capacity

[39:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=2348s) to host multi-node clusters.

[39:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=2349s) They use a workload cluster
sitting in the regional site

[39:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=2354s) to create and operate
multiple workload clusters.

[39:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=2357s) And the regional data
center is used to host

[39:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=2360s) the management cluster
that can operate and deploy

[39:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=2364s) multiple workload clusters
in the edge sites.

[39:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=2366s) So this stretch topology

[39:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=2369s) and also the cellular cluster management

[39:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=2371s) enabled DOCOMO to deploy
their full-fledged

[39:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=2375s) container access service platform

[39:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=2377s) starting from the region
to the edge sites.

[39:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=2380s) In the region, the EKS
service is always available.

[39:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=2384s) And NTT DOCOMO is one
of the first customer

[39:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=2388s) where it paired up with NEC,

[39:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=2390s) which is their core and RAN provider,

[39:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=2393s) the ISP vendor that
provides the core and RAN,

[39:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=2396s) to certify their workloads
on graviton in the region.

[40:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=2401s) So they're hosting the 5G
core in the region and RAN

[40:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=2404s) which constitutes the
DU, the Distributed Unit,

[40:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=2407s) and the centralized unit on
the EKS Anywhere environments

[40:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=2412s) stretching from regional
sites to the edge sites.

[40:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=2415s) So with this particular approach,

[40:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=2418s) NTT DOCOMO was able to deploy
different set of applications

[40:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=2422s) starting from the cloud to the region.

[40:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=2425s) For example, the edge sites will comprise

[40:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=2428s) of the distributed unit
and the centralized unit.

[40:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=2431s) The RAN intelligent controllers

[40:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=2433s) are deployed in the regional sites,

[40:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=2434s) and the main 5G core components
are deployed in the region.

[40:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=2438s) So, let us end the EKS Anywhere topic

[40:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=2442s) like with a few best practices, right?

[40:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=2444s) So whatever deployment we choose,

[40:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=2447s) we provide a set of
deployment best practices.

[40:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=2450s) So the same applies for EKS Anywhere too,

[40:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=2452s) even if it is managed within
your own data centers.

[40:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=2455s) The first one is using the GitOps-based

[40:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=2458s) cluster management approach

[41:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=2460s) where you can store the
whole cluster configuration

[41:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=2464s) as a code in the GitOps repository

[41:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=2466s) and can sync the cluster
management and creation.

[41:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=2469s) And the second one is
using the curated packages

[41:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=2472s) where you can use the
AWS-provided Curated Packages

[41:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=2476s) to manage all your add-ons

[41:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=2478s) that gets deployed on
EKS Anywhere clusters.

[41:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=2481s) The cluster upgrades with EKS Anywhere,

[41:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=2484s) the CLI and also the
GitOps-based approach,

[41:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=2487s) we support different
types of upgrade patterns.

[41:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=2490s) It can be rolling upgrades
or in place upgrades

[41:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=2494s) where you can just upgrade
the Kubernetes version

[41:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=2496s) running on top of your hardware

[41:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=2498s) or a full-fledged rolling upgrade,

[41:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=2500s) which also patches the OS

[41:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=2502s) that is running on top of your hardware.

[41:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=2504s) So you can use the existing mechanisms

[41:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=2507s) to upgrade your clusters.

[41:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=2509s) The LDAP and also OIDC for
security based authentication,

[41:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=2513s) you can integrate EKS Anywhere

[41:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=2515s) with your existing LDAP infrastructure

[41:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=2517s) that is available within
your data center environment.

[42:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=2520s) Lastly, as the Cilium is the package CNI

[42:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=2523s) that is available with EKS Anywhere,

[42:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=2525s) you can use the eBPF security

[42:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=2527s) that is available with
the network policies

[42:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=2530s) that is provided by Cilium to
protect your East/West traffic

[42:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=2534s) that is within your cluster

[42:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=2536s) so that you can use a
full-fledged capabilities

[42:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=2539s) that are provided by Cilium

[42:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=2541s) to secure your workload communication,

[42:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=2543s) between port to port or
service to port communications.

[42:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=2547s) So now, let me hand it over back to Eric,

[42:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=2550s) who will be introducing the
newest deployment option,

[42:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=2552s) the EKS Hybrid Nodes.

[42:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=2555s) - Thanks, Gokul.

[42:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=2558s) All right, so years of running

[42:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=2560s) EKS on Outposts and EKS Anywhere

[42:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=2563s) and learning from our customers

[42:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=2564s) gave us the conviction

[42:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=2565s) that managing the
Kubernetes control planes

[42:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=2567s) for clusters running on
customer-managed hardware

[42:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=2570s) would represent a meaningful step

[42:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=2572s) toward alleviating the
undifferentiated heavy lift

[42:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=2575s) of running Kubernetes on-premises.

[42:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=2577s) With EKS Hybrid Nodes,

[42:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=2579s) you attach on-premises
and edge infrastructure

[43:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=2581s) running in your environment

[43:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=2583s) to the EKS control plane
running in the cloud,

[43:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=2585s) enabling you to retain
your workloads on-prem

[43:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=2588s) while offloading control plane

[43:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=2589s) management responsibility to Amazon.

[43:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=2592s) You'll continue using Amazon EKS features

[43:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=2595s) like EKS add-ons, EKS Pod Identities,

[43:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=2598s) cluster access management,
cluster insights,

[43:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=2601s) and extended Kubernetes version support.

[43:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=2603s) And now, you can rely on AWS' expertise

[43:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=2607s) in managing, securing, scaling
up Kubernetes control planes

[43:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=2610s) to reduce your operational overhead,

[43:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=2612s) conserve your on-prem capacity

[43:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=2614s) by hosting your Kubernetes
control plane in the cloud,

[43:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=2618s) and establish operational consistency

[43:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=2620s) across your on-prem
and cloud environments.

[43:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=2624s) So, how does it work?

[43:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=2625s) With EKS Hybrid Nodes,

[43:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=2627s) your EKS control plane continues
to run in the AWS region

[43:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=2631s) with the same APIs, tooling and features

[43:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=2634s) that you're accustomed to
when you run EKS in the cloud.

[43:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=2637s) Your on-premises worker nodes

[43:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=2639s) are physical or virtual
machines that you manage.

[44:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=2642s) With this bring-your-own
infrastructure approach,

[44:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=2644s) EKS is not calling
infrastructure provider APIs

[44:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=2648s) to provision node capacity on your behalf.

[44:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=2650s) Instead, with Hybrid Nodes,

[44:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=2652s) you'll reuse the tooling and systems

[44:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=2653s) that you've established
on-prem to provision capacity.

[44:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=2657s) So to enable your on-prem and edge devices

[44:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=2659s) to connect to the EKS
control plane in the cloud,

[44:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=2662s) we've adapted the tooling that we use

[44:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=2664s) to initialize the EKS
optimized Amazon Linux AMIs

[44:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=2668s) so as to accommodate
the connection of nodes

[44:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=2670s) running on customer-managed hardware

[44:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=2672s) to the EKS control plane.

[44:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=2674s) The resulting hybrid node
CLI utility called nodeadm

[44:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=2678s) installs the components
needed for your on-prem hosts

[44:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=2682s) to run as Kubernetes nodes and connect,

[44:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=2685s) authenticate to the EKS control plane,

[44:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=2687s) including the kubelet, containerd,

[44:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=2689s) and the AWS IAM Authenticator.

[44:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=2692s) Running the nodeadm init command

[44:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=2695s) bootstraps your nodes

[44:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=2696s) by configuring the installed artifacts

[44:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=2698s) to join your EKS control
plane in the cloud.

[45:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=2701s) All right, let's take a brief detour

[45:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=2702s) to learn a little bit more about nodeadm

[45:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=2704s) before coming back to
wrap up our overview.

[45:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=2707s) So you'll run nodeadm on each
of your on-premises hosts

[45:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=2710s) to simplify the installation,
configuration, registration,

[45:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=2715s) upgrading and uninstallation
of your Hybrid Nodes.

[45:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=2718s) We enhanced nodeadm to work
with arbitrary infrastructure

[45:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=2722s) and select operating systems.

[45:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=2724s) And we integrated it
with AWS Systems Manager

[45:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=2727s) and AWS IAM Roles Anywhere

[45:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=2729s) to streamline the process

[45:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=2731s) of authenticating your on-prem nodes

[45:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=2733s) to the Kubernetes cluster,

[45:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=2734s) the EKS control plane
running in the cloud.

[45:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=2737s) To automate the initialization

[45:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=2740s) of your Hybrid Nodes to your EKS cluster,

[45:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=2743s) we recommend including nodeadm

[45:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=2745s) in your golden operating system images

[45:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=2748s) configured to run at host startup

[45:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=2750s) for your ISOs, OVAs or
other image formats.

[45:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=2755s) Now coming back to our overview,

[45:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=2757s) to join your cluster,

[45:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=2758s) your EKS Hybrid Nodes assume
an EKS Hybrid Nodes IAM role

[46:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=2762s) that you'll create on your AWS account.

[46:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=2765s) This is similar to the EKS
nodes IAM role you use today.

[46:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=2769s) For your EKS Hybrid Nodes
to assume this role,

[46:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=2773s) they'll obtain temporary credentials

[46:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=2774s) either using an AWS systems
manager hybrid activation

[46:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=2778s) or AWS IAM Roles Anywhere.

[46:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=2780s) Systems Manager is a simpler solution

[46:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=2783s) and we generally recommend it

[46:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=2784s) for Hybrid Nodes authentication.

[46:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=2786s) Unless you already have
public key infrastructure

[46:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=2789s) with your own private
certificate authority

[46:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=2791s) and certificates established on-prem,

[46:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=2793s) in which case IAM Roles
Anywhere is a good choice.

[46:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=2797s) You'll also need consistent
private connectivity

[46:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=2800s) from your on-prem or edge
environment into the AWS region.

[46:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=2805s) We expect that AWS Direct Connect,

[46:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=2808s) AWS Site-to-Site VPN

[46:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=2810s) or a customer-managed VPN solution

[46:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=2813s) will be the most common technologies

[46:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=2815s) that our customers use to
establish this connection.

[46:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=2819s) Direct Connect is often preferred

[47:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=2821s) when consistent high
performance latency is required.

[47:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=2823s) Although AWS Site-to-Site
VPN doesn't require

[47:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=2826s) the installation of
physical networking hardware

[47:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=2829s) and can be a good choice,
a cost-effective choice,

[47:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=2832s) for deployments that don't require

[47:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=2834s) as much network consistency.

[47:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=2837s) So how are responsibilities shared

[47:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=2839s) between AWS and EKS
Hybrid Nodes customers?

[47:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=2844s) AWS, of course, continues to manage

[47:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=2845s) the AWS services that run in the region,

[47:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=2848s) including the EKS control plane,

[47:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=2850s) your identity and observability services

[47:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=2852s) and the ECR container registry.

[47:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=2855s) A subset of EKS add-ons
are supported by Amazon

[47:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=2859s) as compatible with Hybrid Nodes,

[47:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=2862s) including kube-proxy, CoreDNS,

[47:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=2864s) the ADOT and CloudWatch
observability agents,

[47:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=2868s) the Pod Identity agent,

[47:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=2869s) and the CSI snapshot controller.

[47:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=2872s) You'll be responsible for
managing the components

[47:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=2875s) that run on-prem in your environment,

[47:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=2877s) including your on-prem
storage solution, networking,

[48:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=2880s) and the operating systems
that run your Hybrid Nodes.

[48:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=2883s) AWS supports the integration of the Cilium

[48:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=2886s) and Calico CNI drivers when
you run them with Hybrid Nodes.

[48:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=2890s) And AWS supports the basic features

[48:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=2893s) of those drivers with Hybrid Nodes,

[48:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=2895s) including for overlay networking,
IP address management,

[48:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=2899s) and dynamic PodIP advertising

[48:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=2902s) using the Border Gateway Protocol, or BGP.

[48:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=2906s) AWS supports select operating
systems with Hybrid Nodes

[48:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=2909s) and supports the integration
of those operating systems

[48:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=2913s) but you'll retain responsibility

[48:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=2914s) for managing the operating system,

[48:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=2916s) patching it, and maintaining it.

[48:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=2919s) EKS Hybrid Nodes is compatible
with Ubuntu and RHEL

[48:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=2923s) for bare-metal and
virtualized environments,

[48:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=2925s) and with Amazon Linux 2023

[48:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=2927s) for virtualized environments alone.

[48:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=2930s) Now let's run through how traffic routes

[48:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=2932s) across your environment
between the EKS control plane

[48:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=2936s) and your on-prem nodes and pods.

[48:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=2939s) Without configuring your EKS
cluster for Hybrid Nodes,

[49:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=2943s) your control plane wouldn't
know how to reach the node

[49:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=2945s) and PodIP addresses running
in your environment.

[49:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=2948s) To account for this,

[49:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=2949s) when you create a Hybrid
Nodes-enabled EKS cluster,

[49:15](https://www.youtube.com/watch?v=QMzor8haEOM&t=2955s) you pass in a RemoteNodeNetwork CIDR range

[49:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=2958s) and a remote pod network CIDR range.

[49:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=2960s) The RemoteNodeNetwork CIDR

[49:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=2962s) is used for kubectl exec,
logs, and port forwarding;

[49:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=2965s) and the remote pod network CIDR

[49:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=2967s) is used if your control
plane needs to reach

[49:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=2969s) webhooks running in your environment.

[49:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=2971s) These new parameters alert
the EKS control plane

[49:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=2974s) that these IP addresses can be reached

[49:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=2976s) by forwarding traffic
into your cluster VPC.

[49:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=2980s) These CIDR ranges can't
overlap with each other,

[49:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=2983s) they can't overlap with
the cluster VPC CIDR range,

[49:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=2985s) and they can't overlap
with the EKS service CIDR.

[49:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=2989s) As of today, only new
EKS clusters are capable

[49:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=2992s) of handling this remote
networking configuration.

[49:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=2995s) And as such, today, only new
clusters can run Hybrid Nodes,

[49:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=2999s) although we plan to enable
existing EKS clusters

[50:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=3002s) to run Hybrid Nodes in the future.

[50:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=3006s) So traffic routes from your
control plane into your VPC

[50:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=3009s) over the Elastic Network
Interfaces or ENIs,

[50:14](https://www.youtube.com/watch?v=QMzor8haEOM&t=3014s) that EKS creates on your subnets

[50:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=3016s) when you create your cluster.

[50:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=3018s) This is the same mechanism that EKS uses

[50:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=3021s) for control plane to cloud
node communication today.

[50:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=3025s) And in order for data to
make it into your data center

[50:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=3028s) and into your environment
once it's in your VPC,

[50:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=3031s) you need to add rules to
your VPC routing table

[50:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=3034s) for traffic out to your node and pod CIDRs

[50:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=3037s) set to transit over a gateway

[50:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=3038s) that you'll create and
attach on your account.

[50:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=3041s) This will typically either
be a virtual private gateway,

[50:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=3044s) which is better suited
for small and medium-sized

[50:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=3047s) deployments and simpler network typologies

[50:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=3049s) or an AWS transit gateway,

[50:51](https://www.youtube.com/watch?v=QMzor8haEOM&t=3051s) which is generally recommended

[50:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=3052s) for larger, more complex networks.

[50:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=3055s) So the data then flows out of your gateway

[50:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=3057s) over your private connection

[50:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=3058s) that's either your Direct
Connect or your Site-to-Site VPN

[51:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=3061s) and into your environment.

[51:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=3063s) The firewall rules
protecting your data center,

[51:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=3066s) your edge location,

[51:07](https://www.youtube.com/watch?v=QMzor8haEOM&t=3067s) need to enable
bi-directional communication

[51:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=3069s) between the EKS control
plane running in the cloud

[51:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=3073s) and your Hybrid Nodes running on-prem.

[51:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=3076s) And you'll also need
to add forwarding rules

[51:18](https://www.youtube.com/watch?v=QMzor8haEOM&t=3078s) to your on-prem routing table

[51:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=3080s) for your hybrid node and pod CIDRs.

[51:23](https://www.youtube.com/watch?v=QMzor8haEOM&t=3083s) As pods are ephemeral,

[51:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=3085s) their IP addresses
change fairly frequently.

[51:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=3087s) So it's recommended that
you dynamically advertise

[51:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=3090s) PodIP addresses to your on-prem router

[51:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=3093s) if you're making your
pods routable using BGP,

[51:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=3096s) which is supported for
both Cilium and Calico.

[51:39](https://www.youtube.com/watch?v=QMzor8haEOM&t=3099s) You also need to ensure that those ENI,

[51:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=3101s) those EKS cluster ENI security groups

[51:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=3104s) allow for bi-directional communication

[51:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=3106s) between the control plane
and your on-prem environment.

[51:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=3113s) We're really excited to see how
you all use EKS Hybrid Nodes

[51:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=3116s) and where you derive the most value.

[51:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=3118s) One of our beta customers, Darktrace,

[52:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=3120s) highlighted the cross-environment
operational consistency

[52:03](https://www.youtube.com/watch?v=QMzor8haEOM&t=3123s) that the solution provides.

[52:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=3125s) Darktrace offers an AI-based
cybersecurity platform

[52:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=3129s) that learns patterns
specific to each customer

[52:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=3132s) to provide for robust threat
protection and response.

[52:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=3136s) Darktrace uses Kubernetes
on-prem to provide their teams

[52:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=3139s) with a consistent deployment environment,

[52:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=3141s) taking advantage of Kubernetes
tooling for observability

[52:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=3145s) application scaling and disaster recovery.

[52:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=3149s) And instead of creating
cross-site clusters

[52:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=3151s) and administering their
control plane themselves,

[52:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=3154s) Darktrace decided to use EKS Hybrid Nodes

[52:36](https://www.youtube.com/watch?v=QMzor8haEOM&t=3156s) to unify Kubernetes management with EKS,

[52:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=3160s) driving higher scalability,
availability and efficiency.

[52:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=3165s) Now, let's touch on some EKS
Hybrid Nodes best practices.

[52:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=3169s) To automate node bootstrap,

[52:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=3170s) include nodeadm in your
golden operating system images

[52:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=3174s) and optionally set it
to run at host startup

[52:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=3176s) as a systemd service.

[52:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=3178s) To limit latency between the control plane

[52:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=3179s) and your environment,
create your EKS cluster

[53:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=3182s) in the region that's closest
to your hybrid location,

[53:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=3185s) to your data center or
to your edge location.

[53:09](https://www.youtube.com/watch?v=QMzor8haEOM&t=3189s) For best performance, we
recommend minimum bandwidth

[53:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=3192s) of 100 megabits per second.

[53:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=3193s) and maximum roundtrip
latency of 200 milliseconds.

[53:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=3197s) Although these parameters
really depend on your use case,

[53:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=3201s) how you're using Hybrid Nodes.

[53:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=3202s) And it's very much recommended

[53:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=3204s) that you perform your own network testing.

[53:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=3206s) Factors like image size and
how many nodes you're running

[53:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=3208s) very much impact latency,

[53:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=3210s) so work closely with
your networking teams.

[53:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=3212s) Next, leverage AWS services
by utilizing compatible

[53:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=3217s) EKS add-ons for monitoring,
logging and identity management.

[53:42](https://www.youtube.com/watch?v=QMzor8haEOM&t=3222s) And one thing I didn't
mention about nodeadm

[53:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=3225s) is that it creates a label
on each of your Hybrid Nodes.

[53:48](https://www.youtube.com/watch?v=QMzor8haEOM&t=3228s) That's compute-type equals hybrid.

[53:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=3230s) You can use this label to target workloads

[53:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=3232s) at or away from your Hybrid Nodes

[53:54](https://www.youtube.com/watch?v=QMzor8haEOM&t=3234s) when you're using mixed mode clusters

[53:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=3236s) that include both Hybrid
Nodes and cloud nodes

[53:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=3239s) in a single cluster.

[54:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=3241s) And lastly, and most important,
probably most importantly,

[54:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=3244s) throughout the process of getting
started with Hybrid Nodes,

[54:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=3246s) work very closely with your
networking and security teams

[54:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=3250s) to ensure your firewall rules
and your security groups

[54:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=3253s) allow the bi-directional
communication that's required

[54:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=3256s) from your on-prem or edge
locations into the AWS region

[54:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=3260s) for the control plane
and other AWS services

[54:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=3262s) that you might want to
integrate with Hybrid Nodes.

[54:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=3266s) All right, before we go,

[54:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=3267s) let's touch on a simple decision tree

[54:29](https://www.youtube.com/watch?v=QMzor8haEOM&t=3269s) for how you could decide
which EKS hybrid solution

[54:32](https://www.youtube.com/watch?v=QMzor8haEOM&t=3272s) best meets your needs,
best suits your use case.

[54:35](https://www.youtube.com/watch?v=QMzor8haEOM&t=3275s) So you have to ask yourself
a couple of questions.

[54:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=3277s) First, do I already have
AWS Outposts running on-prem

[54:41](https://www.youtube.com/watch?v=QMzor8haEOM&t=3281s) or am I considering an
infrastructure refresh?

[54:44](https://www.youtube.com/watch?v=QMzor8haEOM&t=3284s) If the answer to this question is yes,

[54:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=3285s) then running EKS on Outpost

[54:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=3287s) is gonna provide the most
consistent experience

[54:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=3290s) with running EKS nodes in the cloud

[54:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=3292s) and the tightest integration with AWS.

[54:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=3295s) If your answer is no, ask yourself,

[54:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=3297s) do I need an air-gapped environment?

[54:58](https://www.youtube.com/watch?v=QMzor8haEOM&t=3298s) Do I need an air-gap solution?

[55:00](https://www.youtube.com/watch?v=QMzor8haEOM&t=3300s) If you don't, then EKS Hybrid Nodes

[55:02](https://www.youtube.com/watch?v=QMzor8haEOM&t=3302s) is gonna provide you with the most value

[55:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=3304s) by offloading responsibility

[55:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=3306s) for control plane management to AWS

[55:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=3308s) while allowing you to continue to run

[55:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=3310s) on your existing hardware.

[55:11](https://www.youtube.com/watch?v=QMzor8haEOM&t=3311s) If you do need an air-gapped solution,

[55:13](https://www.youtube.com/watch?v=QMzor8haEOM&t=3313s) then EKS Anywhere is gonna
be the best choice for you.

[55:17](https://www.youtube.com/watch?v=QMzor8haEOM&t=3317s) Now, how can you learn more about EKS

[55:20](https://www.youtube.com/watch?v=QMzor8haEOM&t=3320s) through the rest of
re:Invent and thereafter?

[55:22](https://www.youtube.com/watch?v=QMzor8haEOM&t=3322s) First, go and attend these
other amazing sessions

[55:25](https://www.youtube.com/watch?v=QMzor8haEOM&t=3325s) on the Kubernetes track.

[55:26](https://www.youtube.com/watch?v=QMzor8haEOM&t=3326s) At KUB402, you're gonna learn
about various architectures

[55:30](https://www.youtube.com/watch?v=QMzor8haEOM&t=3330s) for building and deploying
workloads on Amazon EKS

[55:34](https://www.youtube.com/watch?v=QMzor8haEOM&t=3334s) with Amazon ECR and automations.

[55:37](https://www.youtube.com/watch?v=QMzor8haEOM&t=3337s) KUB320 is gonna focus on how organizations

[55:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=3340s) build petabyte scale data
processing pipelines on EKS.

[55:45](https://www.youtube.com/watch?v=QMzor8haEOM&t=3345s) And at KUB201,

[55:47](https://www.youtube.com/watch?v=QMzor8haEOM&t=3347s) you'll hear from Amazon
Kubernetes product leadership

[55:50](https://www.youtube.com/watch?v=QMzor8haEOM&t=3350s) about the latest
innovations and strategies

[55:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=3353s) for building platforms and applications

[55:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=3355s) with Kubernetes faster.

[55:57](https://www.youtube.com/watch?v=QMzor8haEOM&t=3357s) We also encourage you to attend sessions

[55:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=3359s) on the hybrid and edge
track such as HYB301.

[56:05](https://www.youtube.com/watch?v=QMzor8haEOM&t=3365s) And if you're interested in a session

[56:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=3366s) that you can't attend in person,

[56:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=3368s) footage for most sessions
will be available on YouTube

[56:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=3370s) within a couple of days of
those sessions taking place,

[56:12](https://www.youtube.com/watch?v=QMzor8haEOM&t=3372s) specifically for breakout sessions.

[56:16](https://www.youtube.com/watch?v=QMzor8haEOM&t=3376s) After re:Invent, you can continue
your EKS learning journey

[56:19](https://www.youtube.com/watch?v=QMzor8haEOM&t=3379s) by taking the EKS workshop,

[56:21](https://www.youtube.com/watch?v=QMzor8haEOM&t=3381s) working through the EKS
best practices guide.

[56:24](https://www.youtube.com/watch?v=QMzor8haEOM&t=3384s) Please take a look at the EKS
Hybrid Nodes documentation.

[56:27](https://www.youtube.com/watch?v=QMzor8haEOM&t=3387s) The team spent a ton of work on it

[56:28](https://www.youtube.com/watch?v=QMzor8haEOM&t=3388s) and there's a ton of
great content out there.

[56:31](https://www.youtube.com/watch?v=QMzor8haEOM&t=3391s) You can also review session materials

[56:33](https://www.youtube.com/watch?v=QMzor8haEOM&t=3393s) for AWS re:Invent sessions
at this QR code and URL here.

[56:38](https://www.youtube.com/watch?v=QMzor8haEOM&t=3398s) This slide deck materials for this session

[56:40](https://www.youtube.com/watch?v=QMzor8haEOM&t=3400s) are gonna be available at this QR code

[56:43](https://www.youtube.com/watch?v=QMzor8haEOM&t=3403s) and at this GitHub URL.

[56:46](https://www.youtube.com/watch?v=QMzor8haEOM&t=3406s) Give you a second to take
photos if you want to.

[56:49](https://www.youtube.com/watch?v=QMzor8haEOM&t=3409s) All right, so thank you very
much for attending the session.

[56:52](https://www.youtube.com/watch?v=QMzor8haEOM&t=3412s) I hope you got a lot out of it,

[56:53](https://www.youtube.com/watch?v=QMzor8haEOM&t=3413s) I hope you learned a thing or two.

[56:55](https://www.youtube.com/watch?v=QMzor8haEOM&t=3415s) As you continue your journey

[56:56](https://www.youtube.com/watch?v=QMzor8haEOM&t=3416s) modernizing your on-prem infrastructure,

[56:59](https://www.youtube.com/watch?v=QMzor8haEOM&t=3419s) please don't hesitate to
reach out to me or Gokul.

[57:01](https://www.youtube.com/watch?v=QMzor8haEOM&t=3421s) Our email addresses are
up on the screen here.

[57:04](https://www.youtube.com/watch?v=QMzor8haEOM&t=3424s) And we also encourage
you to please complete

[57:06](https://www.youtube.com/watch?v=QMzor8haEOM&t=3426s) the session survey in
the mobile application.

[57:08](https://www.youtube.com/watch?v=QMzor8haEOM&t=3428s) It helps us see how we're doing

[57:10](https://www.youtube.com/watch?v=QMzor8haEOM&t=3430s) and how we can do better
for future sessions.

