# AWS re:Invent 2024 - Networking strategies for Kubernetes (KUB406)

[Video Link](https://www.youtube.com/watch?v=8fes5sP0rs0)

## Description

This deep-dive session explores networking considerations that Amazon EKS cluster operators must navigate. Examine pod communication, service discovery, and policy enforcement in depth, and hear about advanced strategies for load balancing and application networking. Leave this session armed with the technical knowledge and best practices needed to successfully deploy and manage resilient, secure workloads on Amazon EKS using services like Amazon VPC, Elastic Load Balancing (ELB), and Amazon VPC Lattice. Join this session to learn more about Kubernetes networking on AWS.

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

- Hello, everybody, and
welcome to the session. My name is Federica Ciuffo. I'm Italian, but I live
in Spain, in Madrid. So happy to see you
all here today with us. And today with me is also Sai Vennam. - Hey, everyone. Sai here. I'm a container specialist at AWS. I'm based out of Austin, Texas, but originally I'm from India and excited to talk to you guys about networking strategies
for Kubernetes today. This is a 400-level talk, but I'll just give you a quick heads-up that we're gonna start at
smaller levels of complexity and kind of build up as we
get to the end of the session. Let's go ahead and get started. - Yeah, and actually we
have built the agenda with all the interactions
that we have with customer during this 2024 as we are
both container specialists, so we have a lot of conversation around Kubernetes networking. And so we wanted to highlight the most interesting customer interaction that we had during the year and also the, you know,
most-asked questions. And to make this, what, session, a little bit more interactive. We have translated
those customer questions and topics into requirements
of an application. This will be the rental store application, and today, well, we will
take, do a little bit of role play, Sai and I. So I will be a cloud architect who is responsible of
architecting the clouds and also Kubernetes clusters
to run this application, while Sai- - Yeah, I'm gonna be the
cluster operator, right? So I can say that with most of the people that I've talked to at sessions today, I'm guessing a lot of
you in the audience today are on a platform team at your company operating Kubernetes clusters, and I hope to kind of
emulate that role today. So Federica's gonna give me requirements. She's gonna come from a position of being a really
well-versed cloud architect, and she's gonna be giving me demands that I have to fulfill
as the platform team. So that's kind of the back and
forth we're gonna try to do. - Yeah, so we'll put our hats on. - All right. - And so we, Sai, we have
different requirements for our application. The first thing that I want to do is actually to simplify your life and make it easier to
simplify cluster operations, so let's streamline that
as much as possible, as well as our application
is an external application, so our customer will be able to actually access it externally. So we will see how to do that together. And we also need some,
let's say we want to improve their resiliency in general,
in particular of the network, but also based on the
findings that we find, we also want to be able to
observe this architecture and this application
at each time in a more, in a way that doesn't really
burden my application teams, which are, well, spending a
lot of time into observing but without a really
clear way of how to do so with many microservices. We also have some requirements
from security teams, so we need to enforce that. And we want to be able to
take a different approach as to tackle those
disruptions within the cluster when we make new updates, for example. For example, we have to update the cluster each three months and things like this. So all of these operations
that can be disruptive, right now, we are doing it with the in-place upgrades, et cetera, but we want to have a
deeper look into something that could be a little
bit less disruptive, like blue-greens in that sense. But before diving deeper into that, I think, Sai, I already
sent you the application, so if we can take a look. - Yeah, let's take a look at the application really quickly here. So I'm gonna switch this
to my computer here, and as a heads-up, okay, that's, the wrong screen is being shared there. So give us just one second.
Let's see what's going on here. - Yeah, so in the meantime, let's review what we want to do in that sense. But well, let me review
how we are gonna deploy the application where actually we live while Sai reviews where
he has the application. So in that sense, our organization has
different business units, and each business unit
has a dedicated account. Also, we have some
on-premises data centers that we need to take into consideration. And everything is actually
connected with Transit Gateway. There is also, well, some direct connects and et cetera for the environment. So I think we got the application, right? - Yes, we got it. Perfect timing, all right, excellent. So let me make this a little bit bigger. So we were saying that
we had the local version of the application up and running. So Federica's team has
basically built containers on their local machines, and to do so, they've built a version of this retail store sample application that runs locally without
running on the cloud. And let's just see what that looks like by running a quick command here
to start up the application. All right, we're gonna set
the MySQL password, pass, and then do a docker-compose up. And I think this is a great way to work with containers locally. You can see what it did there was download the container images, and what it's doing is it's starting up the application now locally, and in a few seconds
here, it's fully started. And let's actually go
to our local host here to access the application. Boom, there we go. This is our beautiful retail
store sample application running locally. But while this is great for development, it kind of enables iterative
development very quickly with containers on your local machine, we need a way to run
this in the cloud, right? So that's kind of the next step here. - Yeah, exactly, and
actually what we will need is to have a replica of this application in each and every VPC in the environment that is dedicated to the retail account. The application that Sai just showed is made up of different
decoupled components, and we have some
infrastructure dependencies. We have seen the MySQL there. And so let's go right into it. The first thing that we want
to do is to simplify your life, and actually thinking about
the Kubernetes architecture, there are a lot of networking components that we need to configure
and take into consideration, not only the control plane and the different components
that talk to each other, but also how are we gonna bring together control plane and data plane. Within the data plane also, some very core networking components that we need to take into consideration, and our cluster needs to
be configured with that to be able to use those. For example, we have
kube-proxy, CoreDNS, the CNI, so a lot of things, and
we want to simplify that, and this is actually
where Amazon EKS can help. And so, Sai, do you want
to take this one and so- - Yeah, absolutely. So let's talk a little
bit about Amazon EKS. And you guys might be wondering, "Sai, this is a networking talk. Why are we talking about EKS?" Believe me, I'm getting to it. So Amazon EKS is really
just managed Kubernetes. It's not our special
version of Kubernetes. It's open source, upstream,
conformant Kubernetes that we help manage for you. Now, when we first launched
Amazon EKS, you know, about six years ago now, the
focus was on helping customers by managing the control plane. So you kind of saw there
with that very neat animation the capabilities that
we're managing for you with the control plane. But we're taking this a step further, and I think all of you know what I'm about to talk about here, but it was an announcement
that we released just earlier this week. Now Amazon EKS is helping customers manage parts of the data plane as well. So essentially what Auto
Mode enables customers to do is have EKS clusters that are ready for production use cases out of the box. All of these components
that you as platform teams, me as a platform operator
had to manage on my own are now managed for you. And the scope and the purview
of Auto Mode is, you know, is continuing to increase. You can check out the road map. A lot of it is public on GitHub. And so critically, so
where Auto Mode fits in with networking is that a number of key networking components are managed for you in Auto Mode. Let's dive into these really quickly. For one, the VPC CNI is
gonna be managed for you now. So this is the, you know,
the one that's by default set up with every EKS cluster but no longer managed by
you in your data plane. We handle it for you. That means when you
upgrade your control plane, those add-ons are
upgraded for you as well. This means less cognitive overload of managing different
components of your data plane. In addition, CoreDNS out of
the box as well as kube-proxy, these are all gonna be
kind of managed for you. In fact, there's actually
one more thing here that's gonna be managed for you, the application Load
Balancer Controller as well, which would be coming out of the box with all EKS Auto Mode clusters. So put all of that together, and essentially what
you have is Amazon EKS managing more capabilities for you in the control plane and data plane. But Federica, you've looked
into a little bit about CNIs. Can you explain your requirements
and why you wanna use this CNI versus maybe some other ones? - Yeah, exactly, so we are going to, for the Amazon VPC CNI actually, because it simplifies a bit how can we do Kubernetes within AWS. Effectively, the Amazon VPC
CNI, it's deeply integrated with the underlying
network that is Amazon VPC, and thus it assigns IPs
from Amazon VPC to pods. And this is great for
us because it enables us to take advantage of all the
good things of Amazon VPC. Like for example, we can do security. We can do also observability
with VPC flow logs. Also the CNI is highly customizable. That is, we can really fit the CNI and change all the specs to our needs. And this is great for us. Also, we need to consider
there are other alternate CNIs that are compatible with
EKS but not supported. What does that mean? That it is recommended to have support from the vendor of the CNI of your choice. But we are gonna stick with this CNI, and actually I love how the all of these, well, Amazon EKS, then on top of that, Auto Mode helps your life and
your team to really streamline and take that heavy
lifting out of your team and lets AWS handle this. - Yeah, I'm glad that you're
okay with using the VPC CNI, 'cause that makes my life easier. It's integrated into the AWS
ecosystem as a platform team, less things for me to
worry about managing. - And actually you mentioned
before about load balancer, Load Balancer Controller. So this is actually tied
to our next requirement, and our next requirement,
I want my customers to be able to access my application. Now, great what Sai just showed us that he was running locally,
but this is not what we need. So we need something more. And when we are thinking about
how to access application from outside the cluster
to our backend pods, we always need some Kubernetes objects, that is, ingress and service resources, ingress resources
operating at the Layer 7, application layer, and
service resources operating at the network transport layer. But we need something more. We need some infrastructure
piece that help us to let that, let's say, traffic from
outside the classroom inside the classroom. And that piece usually is
a proxy, a load balancer. So in AWS, there is a native way to do so by using the AWS Load Balancer Controller. And I'm very excited
about the capabilities of AWS Load Balancer Controller, because again, I want to
simplify my team's work with operating with Kubernetes on AWS. The AWS Load Balancer
Controller automatically deploys an application load balancer
with ingress resources, and a service, with service resources, it automatically deploys
a network load balancer, so native AWS load
balancers that actually have all the ability and reliability,
scalability, et cetera, but in particular, not only
supporting in Auto Mode, as we were saying before,
but in particular, I want to dive deeper
into what it can do for us at Layer 7, because if you think about it, we are actually using an
application load balancer. The application load balancer itself is a Layer 7 load balancer. So what does this mean? So all the capabilities,
all the Layer 7 processing happens at a load balancer layer, that is, can be offloaded from, you know, the configuration that
your application teams and my application teams need
to do to the load balancer. For example, certificates,
it can be offloaded to the load balancer, and
then it can also be managed by AWS certificate management,
so a certificate manager that it is actually deeply integrated with AWS Load Balancer Controller itself. And we can take advantage
of all those integration between the AWS Load Balancer and the security and
natural suite within AWS. And this is great for us
because it simplifies our life. Additionally, there is
another way you could, you know, deploy or
handle ingress traffic, that is, use a third-party
ingress controller. You can see here that now the processing, the layers in processing and features shifts from being a responsibility
of the load balancer to being the responsibility
of the controller itself. And this is key because, for example, where before we could offload
the SSR certificate management to the load balancer, now
we need to supply that to the ingress controller. And this is essentially very different. Another thing that is different and adds a little bit more management is that you are handling
only ingress resources. So if you need to handle
service resources, you will need an additional controller, a service controller. With EKS, this used to
be very transparent to do with the in-tree load balancer controller or service controller, but
that has not gone away. It's still there, but we are only pushing, let's say, updates. There are essential
security updates to it. So what it is actually recommended again for handling the service
deployment of load balancers is again, the AWS Load
Balancer Controller. Funny enough, if you're
using an ingress controller, you will still need the AWS
Load Balancer Controller to deploy the load balancer that is in front of the ingress
controller of your choice. So Sai, I am, we have gone
through the differences and so what we can do with the
AWS Load Balancer Controller, third-party controllers, but can we see it in
action with my application? That would be amazing. - Let's do it. So we're gonna get into
our first kind of real demo that Docker composed one,
not a real demo really, but here we're gonna jump
into actually exposing an application using an
application load balancer that's Layer 7-based load balancing. And just very quickly I wanna say here that I love this diagram because you can kind of see how, you know, when you create an ingress resource, obviously it gives you more
advanced path-based routing that operates at the Layer 7 level. You can create those with
custom ingress controllers or the AWS Load Balancer Controller. And at the Layer 4 level, if
you wanna get a load balance for each individual service, you can do so with the
network load balancers that are also kind of, you can create with the AWS Load Balancer Controller. All right, so let's go
ahead and get into this. So in my EKS cluster here,
we've basically deployed all of, oh, I can tell the internet connection's already a little bit, we're
gonna get all the pods in the cluster, but in this cluster, we've already deployed the containers for the retail sample
application that we have today. And critically, you can see here that we've also deployed the
AWS Load Balancer Controller. By the way, if you were
to run this command in an Auto Mode cluster,
you wouldn't see those pods, 'cause those, the Load Balancer Controller is managed for you. But since I'm running on a
standard cluster, not Auto Mode, this is something that
I had to install myself. And then obviously when
I upgrade the cluster, I would also have to handle upgrading the Load Balancer Controller itself. Okay, once that controller is installed, essentially what Kubernetes
is now able to do is anytime an ingress resource is created or a service with the type load balancer, the controller kicks in. It says, "Oh, I know what to do now," and in the backend, it's
gonna start creating resources for us in AWS, and it's
deeply integrated, right? A lot of things happening,
especially if you're doing, you know, custom domains
and you have certs and that kind of thing. There's a lot going on in the
backend with Route 53 and ACM, you know, certificate
authority and all of that that the Load Balancer
Controller will handle for you. So I did create an ingress resource, so I'm gonna run get
Ingress in all namespaces, and there we go. We can see fairly straightforward here that we have an ingress,
it has an address. We'll copy it and access
it, but before I do that, I do wanna quickly show you
what's in that ingress yaml. And this is really
critical here to understand how specifying an ingress works, because you can kind of
see a few things here. Notably, there's annotations, and these tell the application
load balancer controller, ALB, that we're creating for this ingress something that's internet
facing, not internal only. So we want public
internet access for this. We want the target type to be IP mode, and the other option is instance mode. I won't get into this in in
too much depth right now, but I'll share some resources
for how you can dive deeper into the reason why we
provide both options. In addition, a health check
path so that the target group knows whether it's healthy or not. And then the other critical piece here is the service it's
actually routing to, right? So if I do a quick get
svc in the UI namespace, what I'll see is the UI
service here, port 80, and that's essentially
what we're routing to with that ingress. Okay, last thing I wanna call out here, 'cause I've gotten this
question a lot this week, the question is, with Auto Mode, do you have to do anything special to use the AWS managed version of the Load Balancer Controller versus the one that's just
running in your cluster with non-Auto Mode clusters? And by the way, since
you can add Auto Mode to your existing
clusters, this is critical for how you're gonna migrate to the AWS managed
version of the controller. Essentially, you'll notice here there's an ingress class name. So when you wanna use the
Auto Mode managed version of the controller,
essentially what you'll do is you'll create a new ingress class that specifies that you
want ingress resources to be handled by that controller instead. This makes it really seamless
for you to migrate clusters to Auto Mode because you
simply need to install that new ingress class and then
switch the kind of ingresses that you have to the new ingress class. And then you can, you know, remove the load balancer
controller from your cluster. You no longer need to manage it. Okay, now that we've seen all that, I'm gonna pray a little
bit to the demo gods of the internet is all work, actually, that loaded perfectly
fast, thank you. (chuckles) So you can see here that the application running in the cloud in Kubernetes fronted by an ingress resource, so application load balancing. All right, guys, I promise
you we are starting at a lower level of complexity,
and we're gonna bump it up as we kind of go through the presentation. So with this demo, I'm gonna
pass it back to you, Federica, and let's get into some more fun stuff. - PowerPoint, yeah,
and actually thank you, because this is our first requirements. Again, we wanted to
start simple for my teams that are adopting Kubernetes
clusters with Amazon EKS, and there are a lot of things
that you can also do with, you know, adding certificates
to this domain and et cetera. So thank you, Sai, for
showing us how we can, how could we can do this, but
we have other requirements. So let's see this. So with my teams, we
have a lot of problems when it comes to network resiliency, because as long as we
are already following all the best practices, spreading pods across availability zones with topology spread constraints,
we are also deploying a lot of reliability built-in mechanism within the applications. But for us, it is really difficult to test disaster recovery scenarios. So one thing that can help us to do that is actually the new
integration of Amazon EKS with ARC, Amazon Recovery Controller. And this makes easy for us to test and recover from a recovery scenario because we don't have to wait for the health checks
on the services to fail. But actually our controller will signals that the AZ is down, and so the targets, the endpoints that are
in the affected zone will automatically be
deregistered from the service. And this is great for us.
- So Federica, I've gotta ask, so I don't
know what ARC is just yet, so you gotta tell me, why do we need ARC when the whole reason
we're using Kubernetes is because when pods are unhealthy, they automatically stop
getting traffic routed to them? So what's the point of using ARC? - The problem is that
there is a delay to it, so we need to wait for
those health checks to fail, and then the targets will be deregistered. That will be a lot of problems. So ARC shorten that time because automatically in AWS API, they signals that as soon as
there is an AZ, let's say, failure, and this is automatically done. It is true that my team responsibility will also be to make that
application resilient. - Okay, so essentially while
Kubernetes could detect that the pods are unhealthy
and stop routing traffic to it, it takes a little while because
essentially the health check has to fail, the readiness probes, the health probes, and then it happens, so this could impact your customers. But here, you know, essentially
we're improving availability by making it a little bit faster where the second there's an AZ issue, we'll just zonal shift
that traffic, right? - Correct.
- Awesome. - And also it's very interesting for us, the thing that we can
test those scenarios, even if there isn't a real AZ failure, so. About testing those scenarios, I mentioned that my teams
actually have built a lot on the application to ensure reliability. And it has been a long work because first we need to observe where bottlenecks or
potential failures are. Then you need to implement
within the application. Then there is application
aid that is using an application coding
language, programming language, another with another programming language. So it's kind of a mess for us. And I was looking from an
architectural perspective for a way for us to unify those operation and take that burden away
from my application teams. So maybe in the ecosystem, the most-used way to do so
is adopting service meshes. And real quick, what's a service mesh? So in the most common
architecture for service mesh, you take a proxy, you put it next to your application containers. You do that for each application container within the cluster, and
you create basically a new layer that is made
off of all of those proxies, and you push to that layer
the advanced network security and network observability responsibility. Thus you are decopying that from the application business logic that still will be
handled by the developers. Too, those other things
that are now unified with only one programming language because you will be
using that actually proxy for each and every application. So it makes my life easier, makes my application life easier, and it is very powerful. If you look at the capabilities and what service meshes bring to us, all of the things that we
want to do are actually there. We want to be able to
observe, for example, tracing requests, understand
what bottlenecks are, and then we want to be able to implement those reliability features,
not within the application but within the service mesh. Also security feature to it
where I have a lot of requests from my security team around, for example, mutual TLS and securing
the workloads, et cetera. So that's a really big ask, although service meshes also
come with some challenges. - Right, Federica, I love the fact that you covered all the advantages, but you're kind of leaving out the part of me as the
operator having to manage all the challenges of
running a service mesh. And you know, traditionally
the kind of service meshes we're talking about
here, things like Istio that work off of the sidecar model, right? And so the challenges, well, some of them are gonna be things like resource
efficiency issues, right? So when sidecars are not being
utilized to max efficiency, or you know, the fact that
sidecars need to scale up with every pod as they scale
up, this can be challenging. In addition, just installing the sidecars into a cluster is not so easy. It requires the pods be restarted because every time you add the sidecar, the pod needs to go
through a restart cycle. That's not great either. In addition, additional points of failure, security boundaries, these are all things that as the platform team I
need to be thinking about. And of course, I do wanna implement organizational best
practices at the same time because as the platform
team, I've been told all service-to-service
communication has to be encrypted, has to go over mutual TLS,
so we need some solution. So I like the idea of using a service mesh because you know, Federica's
team doesn't have to instrument each single application
with all of the things that we need for observability security. We can add it as a layer on top, which removes complexity from her team. Adds a little bit to mine, but I think we have an approach
to this, Istio Ambient Mesh. So essentially Istio Ambient Mesh, what it's gonna do is enable us to get the same advantages of Istio in a traditional sidecar model but without the sidecars,
and the way it does this is by essentially encrypting traffic between services into a ztunnel proxy. This particular protocol that it uses, it's an Istio-specific term called HBONE, HTTP-Based Overlay Network Environment. So when you break that apart,
it's not that complicated. It's an environment that
overlays on top of your network, and it's based on HTTP. And the interesting thing about this is that essentially what it'll do is make it so that all of the traffic going between your services
now goes through this ztunnel. That enables us to have
mutual TLS out of the box. No pods need to be restarted. The traffic goes from
working at a network layer, working in your network, to going through the ztunnel, right? So that happens as kind
of a switch that flips, and to show that, I want
to actually jump to a demo. And by the way, I know that you saw a bit about waypoint proxies as well. I'll get to that in a second. That's for Layer 7 capabilities. We're gonna focus on Layer 4. That's IP addresses,
Layer 4 authorization. Think IPs and ports rather than fully qualified domain names, PATs, domains, that kind of thing. Okay, so let's take a look
at my cluster environment. I'm gonna use K9s, and
if you don't use this, I highly recommend it. It's a great way to step
through your clusters, see what's running, that kind of thing. And in this cluster,
oh, yeah, the internet's a little bit slow here, but there we go. We can see that I've
already installed Istio. Now, this is a non-disruptive
activity, by the way. It's kinda like a Helm chart. You just install into the cluster. These pods get started, and you can see that it comes with some
observability tools like Grafana, Prometheus, Kiali, Jaeger, and the control plane for Istio as well, as well as an ingress gateway for how traffic gets routed
through Istio instead. Okay, and you can see that, yeah, these pods haven't been restarted actually in the last 26 days. And so real quick, let's take a look. There's a helpful command
that istioctl exposes for us called ztunnel-config workloads. And this is all the
workloads in our cluster, and we can see that right
now, that protocol is TCP, and that essentially telling us it's not going over the HBONE protocol. We don't have that mutual
TLS enabled just yet. And to enable that, we simply need to, this is really cool in my opinion, label the default namespace
with this annotation, just with this label rather. We set the data plane mode
to ambient, and that's it. Now the traffic is gonna start going through the HBONE proxy. So we'll run that istioctl command again, and there we go. Now all those workloads
that were TCP before are now going over the HBONE protocol. Can ignore these. There are some admin
control plane-type services. Those don't need to be changed. But for our actual application workloads, they're going over HBONE, and let me just get
the services real quick so I can access it. I'm gonna grab the one for
the Istio ingress gateway. Apologize, it's a little hard to read, but I'm just gonna grab the Istio piece. And so remember, our
applications weren't restarted. I need to do a couple of
cache list reloads here just to hit the application
here, but there we go. We access our application. Pod-to-pod communication is
happening with mutual TLS. No downtime, no pod restarts. We have Ambient Mesh
enabled in our cluster. But when we think about Istio, we don't just use Istio for mutual TLS. That seems like a bit of an overkill. We get a lot of other advantages
with Istio as well, right? So observability is one
of the critical ones. So I would love to show you how to enable observability
capabilities as well. So very quickly, just jumping
back to the slides here, with ztunnel, we have this
mutual TLS out of the box. We have Layer 4 authorization policies that we can implement as well. Istio is great for the
Layer 7 capabilities, right, so more advanced traffic
routing and that kind of thing. So with a waypoint, essentially what we do is we have traffic that now goes through the separate waypoint that's
running on the cluster, and this is what's gonna
give Istio the ability to do Layer 7 capabilities
and really rich observability. In fact, we're also gonna do a demo of chaos engineering here in a minute. Another popular use case for why you would want this waypoint for Layer 7 capabilities
is canary deployments. Let's say you have a new
feature that you wanna roll out to a subset of your users,
maybe users on Firefox or users on a mobile phone. All of that becomes just a flip that we can switch at the network layer. The app teams don't need to
necessarily change any code. We can do that at the network
layer, that overlay layer. It's really powerful stuff. Let's take a look at what that looks like. We're gonna jump back to my machine here, and to enable the waypoint, let me make this a little bit
easier for you all to see. Okay, to apply the waypoint,
essentially what I'll do is run this istioctl helper command that applies the waypoint
in the default namespace, and that's it. Again, no pods are restarting because this just starts a new pod, and we'll get deployments in the cluster, and we can see that we seven seconds ago started this new waypoint, and now we should have
observability in our application. I'm just gonna refresh this a couple times to make sure we have some logs, metrics kind of flowing
through the application and that kind of thing. Maybe we'll add a pocket
watch to our card, and we'll hit the checkout button. Okay, awesome. That should be enough. Now we're gonna go back
to our command line and run handy istioctl dashboard kiali. Kiali is an open source
kind of observability tool helping us see exactly
how our application looks. Let's make sure we're
looking at like the last, you know, three hours of data. Okay, that's really hard to read. That's not very interesting to me. So let me start cleaning this up a bit. So I'm gonna hide unknown
nodes. I want an app graph. I'm gonna go here. Oh,
already looking better. I'm gonna go here, I'm going to enable some of these things here. I'm gonna get rid of service nodes. I'm gonna do traffic
animations, waypoint proxies. And there we go, so you can already see a lot more that we can see here. Let's disable TCP traffic, 'cause I don't wanna see like
Prometheus stuff going on. And boom, there we go. We can now see kind of a visual layout of our application architecture. I didn't complete a checkout, so that's why this line is black, because we don't have
mutual TLS for this pod, 'cause I didn't actually
do a checkout process. But you can see right here
that it's showing traffic for the other pods that were activated when I was clicking around
in that sample application. Click into one of these, and
you can see that, you know, the traffic from UI to carts
has mutual TLS enabled. So pretty cool stuff, in my opinion. In fact, I can even jump
into things like carts and see exactly what
application is talking to what, and I might notice here
that hey, one of my services is talking to a service that it shouldn't, and I could use Istio to
implement an authorization or network policy to prevent
access between services that maybe shouldn't be
talking to one another, right, limiting blast radius, implementing better security practices. Okay, so what did we see here? We saw with Istio Ambient Mesh, without ever restarting any of our pods, any of our applications, we
got Layer 4 capabilities, mutual TLS enabled,
and we were able to get some great observability
out of this as well. I mentioned I wanted to do a
chaos engineering demo for you. So let's talk about that real quick. So in the gateway that I
deployed into this cluster, which is really straightforward,
I'm basically, you know, it's kind of like that ingress resource that I showed earlier. It's just the Istio way of doing it. I've exposed the UI service, and for that UI service,
let's insert a fault. So about 75% of the time, it's gonna fail. And I haven't applied this yet, so let's just make sure I'm
still hitting the application. Yep, all is good. But now
let's apply this new gateway. It should say configured
to virtualservice. There we go, configured. And now 75% of the time
this should fail. Boom. All right, so we hit that fault already. This is really chaos
engineering at its finest. It's seeing how your application
would respond to failures. So we could also do things like maybe implement a
retry policy on failure and see if our application
responds correctly. Let's keep hitting this a few times, 'cause 25% of the time it should work. Wow, that's crazy. Six, I
should not go gambling today. All right, that's seven times
for it to actually work. And we can already see
that there's some issues with the like cache
invalidation that's going on. So I feel like we already
uncovered a bug, right? So maybe when there's a fault we should deal with the
cache a little better so users don't end up seeing
a page like this, really- - [Federica] Something for
my teams to think about. - [Sai] Exactly, exactly. So
what do you think, Federica? Oops, we don't need that. Let's jump to the slides. - Yeah.
- Yeah. - I think this is exactly
what we are looking for, actually, Sai, so thank
you for showing that. I love the fact that really easily we can have mutant TLS in the cluster. That's a very big ask from
security teams, et cetera. So definitely also like all the things that we can do in terms of observability and implementing new
things that will enhance the reliability of our
applications with Istio Ambient. But I also want to put
you on the spot here. So is there any limitation that we should be aware
about for Istio Ambient? - So there is a limitation here. When we first started
implementing Ambient Mesh with this sample, this application, what we saw was that one of the services didn't mesh well with Ambient
mode, no pun intended. Essentially what we saw
was that one of the pods uses the MySQL protocol to
access our persistence layer, and that protocol didn't
play nicely with the ztunnel. It's like, well, what do we do here? Well, there's a really
great thing that we can do, which shows kind of the
flexibility of Ambient Mesh. Essentially what we did, and
I'll pull up K9s again here, my terminal UI, and dig into
that catalog deployment. And I did cheat here a little bit, and you'll notice that in this pod, we have two containers running. And just to show you what
that second container is, it's an Envoy proxy. There we go, so
essentially what we've done for just this catalog
service is enable a sidecar. And so yes, for this
pod, I had to restart it. And you might have noticed when I ran that ztunnel config
workloads command first, there was one service that was already on the HBONE protocol. That was my little cheat. So beforehand, I had
set up that pod already with the sidecar, and so that really shows how flexible Ambient Mesh
can be for certain workloads that don't work on that HBONE
protocol, that ztunnel proxy. Essentially what you do is in
the deployment configuration for just that one catalog service, right, that catalog service, we add this label,
sidecar injection is true. And so for that one pod we have a sidecar, and in fact in Kiali, it showed it as well that for that one pod we
had a sidecar enabled. And you know, I think we can even show that really quickly here, going here. Okay, let's reset this
back to what it was before. All right, here we go, so
looking at the catalog, that little icon right there, that tells us that it had a sidecar in it. So okay, awesome. We saw how, you know,
for certain workloads that maybe don't work great
with that ztunnel proxy, we can just stick a sidecar
on it and get going. - Amazing, thank you. And this
is exactly what we look for. And also I like that for
my teams, including you, we can go from a no service mesh state to a, let's say, secure
layer service mesh state to a fully fledged one
without needing to adopt the full Layer 7 capabilities right away. So that's amazing as well. And also I wanted to circle,
go back a little bit. We talked a lot about ingresses before, and actually, ingresses, well, are great, but those are limited. Ingresses are limited. To do advanced network staff with ingress, you need to do a lot of annotations, customer resource definitions. So, and actually the Kubernetes ecosystem is not adding new features to ingresses. So this will be the
same also going forward. The evolution, though, of ingress, that is the Kubernetes Gateway API has all those capabilities, and all the new features are added to the Kubernetes Gateway API. The Gateway API tries to solve all of the challenges that
you had with ingresses and takes all the lessons
learned from service meshes. And funny enough, this
Gateway API is the one that we are using for the
Layer 7, Istio Ambient. So the ecosystem in general
is going for a rapid adoption towards the Kubernetes Gateway API. Finally we have one API
that everybody can use so that we don't have,
when we want to move from, for example, service mesh to the other or an ingress specification to the other, we needed to, like, for example, for the ingress controllers,
many different annotations. The migration to one ingress controller to the other was very difficult. Now with the Gateway API,
since we have the same spec, this will be easier. So other things that you
can do with the Gateway API, first of all, you can
do all that you could do with the ingress API obviously. So you can handle ingress
traffic, but you can also handle, and you can obviously do more, all of that you could
do with the annotations, now it's embedded within the API again. Then you can do service-to-service
with the Gamma project. And now in the last KubeCon,
we also have seen applications of the Kubernetes Gateway
API for egress traffic. So that's amazing because we have one API to handle all these use cases and scenario and to unify Kubernetes
networking, really. Another thing that I, specific topic that you can also tackle
with Kubernetes Gateway API that I wanted to dive deeper is actually blue-green
scenarios across clusters. So for example, as I explained before, my teams are spending a
lot of time in, you know, doing cluster upgrades, for example, and we are doing the
in-place upgrades right now, but we wanted to explore
how it would look like to do blue-greens, for example,
for better reliability. We want to be able to roll back if needed. We want to do canary
deployments to the new versions, so all of these things, and
looking at the ecosystem, we said, "Okay, we need
to do multicluster then. Which are the options for us?" We have adopted the Istio Ambient, but multicluster is still not
supported for Istio Ambient. And in general, thinking about how you approach multicluster, with Istio or a service mesh in general, well, there are multiple considerations that we need to do as architects. For example, we need to think about how we are gonna set up the control plane. Are we gonna externalize the control plane to manage the clusters? Are we gonna set it up in
a high-availability mode? Other things that we need to consider is to then we need to share API permissions across the clusters. Then there is encryption
and tenancy boundaries. Then again, we also need to take care of trust between meshes. So if it was difficult
before to, you know, start with service meshes,
adding multiple clusters to the mesh adds a very big
layer of complexity to it. So I told you that this can be also done with a Kubernetes Gateway API. So different approach is using
the Kubernetes Gateway API, and you do that coupling
it with another set of APIs to APIs in general that are the multicluster services API, ServiceInput and ServiceExport
that enable you to do that, let's say, multicluster that
we need but in an easier way, with a Kubernetes native way. And within AWS, we do implement
the Kubernetes Gateway API and the multicluster services API with Amazon VPC Lattice as infrastructure. So like, for example, we
have seen before the ingress, with the ingress controller
that implemented load balancers, now we see the Kubernetes
Gateway API with its controller that implements Amazon
VPC Lattice resources. And real quick, what
Amazon VPC Lattice is, so first of all, Amazon VPC
Lattice is a network service just like Transit Gateway,
just like VPC Peering, but it operates at a different layer, the Layer 7 of the OSI model, unlike Transit Gateway,
unlike VPC Peering. And it enabled us to connect
applications across VPCs and accounts without the
need of those services just by using Amazon VPC Lattice. It also implements an AWS
native approach to security. And another nice thing is
that not only can we have traffic across multiple clusters using the Kubernetes Gateway API and Amazon VPC Lattice, but
also with Amazon VPC Lattice, you could have a single URL that sends some part of
the traffic to, let's say, a service within Amazon EC2 and a service that is
either in Kubernetes, or for example, ECS or Lambda. And this is very compelling to us because we also have some,
well, legacy workloads still running on institute that
we would like to modernize. And there is effectively many challenges, but network is one of them. So these simplifies for that a lot for us. - Yeah, absolutely, we're really excited about the Gateway API. It's really this thing
that the whole community and cloud providers are
kind of centering around. Of course, the Gateway
API is an open source upstream Kubernetes thing, right, like the evolution of ingress. And so cloud providers,
especially like AWS, are creating controllers like
the Gateway API controller that Federica covered on the past slide to be able to implement some
of those resources in AWS, and VPC Lattice really hooks
into that really nicely with that Gateway API controller. So instead of creating ingresses and kind of ingress APIs and services, it's kind of a new approach
with gateways and HTTP routes. And I think we're really
gonna see the community and customers kind of
move to this new approach because of the number of
advantages that it offers, that one that I'll say
is, you know, being able to route to targets
outside of the cluster, whether it's another cluster or maybe Lambda, maybe
ECS, whatever you have, and in addition kind of
all of the capabilities that Federica had covered here that become available as well. So today I wanna quickly summarize what we talked about, right? So we started with simplifying
cluster operations. We talked about our choice with Amazon EKS to run our container-based applications. We talked about how it uses VPC CNI for pod-to-pod networking
kind of integrated into the platform, and
especially with Auto Mode. You know, even for a lot of
the demos that I showed today, that would've been streamlined because I would no longer have to manage some of those components like
the Load Balancer Controller, VPC CNI, CoreDNS, they're managed for me. And when we upgrade clusters, those are also upgraded for us. And of course that means,
you know, with Auto Mode, there's other components
that are managed as well, things like Karpenter. You don't have to worry about
dedicated compute to run that, those resources either, no
dedicated node for Karpenter, no dedicated nodes for
your networking components. Kind of moving on here,
we talked a little bit about exposing applications
externally, right, using the Load Balancer Controller. We talked about creating ALBs,
application load balancers, at the Layer 7 using the
Load Balancer Controller. And at the Layer 4 level,
we talked about creating individual NLBs by creating
services of type load balancer. Kind of further moving down here, we talked a bit about
using Istio Ambient Mesh, enabling us to have Layer 4 and Layer 7 authorization policies, Layer 7 advanced routing,
mutual TLS out of the box without disrupting applications and as well as that interoperability with using sidecars when you need them for specific workloads. And lastly, we kind of talked
a bit about VPC Lattice and the new Gateway API,
the Kubernetes Gateway API, how it's enabling customers to move and evolve to this new
version of networking and how VPC Lattice being a VPC capability in Amazon helps support that. Okay, a lot of you might be wondering how can you continue to
learn these things at home? Well, by the way, that first demo I did, that ingress demo that I did, was actually based on EKS Workshop. So that same environment that I showed you with VS Code in the cloud, you can spin that up for yourself. So I highly recommend
going through EKS Workshop to learn at your own pace. In fact, I can very
quickly just show one thing for you on eksworkshop.com. Some of the things that you'll notice here in the Fundamentals section, if we go to Exposing applications, the same thing that we
showed with ingress, you can actually set up an
environment for yourself and go through it yourself. We talk about things like the
multiple ingress patterns, so what happens when you create
multiple ingress resources but you want them fronted by a single ALB. We also talk about IP
mode versus instance mode for load balancers as well. So EKS Workshop, a great way, self-paced, to kind of learn everything about EKS. And I really, truly believe that, because there's quite
a bit of content here, and we're constantly updating it. One thing I'll say is that
if you don't wanna spin it up in your own account,
you can also reach out to your AWS account manager
to request an EKS Workshop. And in that QR code, there's
gonna be a form as well that you can fill out,
and we'll reach out to you to help get you set up
with an EKS Workshop. Also, EKS's Best Practices Guide, now integrated into the AWS Docs, a great place to learn about
best practices for networking. I know Federica and her
team spent a lot of time making a ton of updates to
the best practices guide so that it's always kind of the latest kind of optimized setup for
networking that we recommend. And you can get a badge as well if you kind of go through
one of our courses. All right, that's all
we have for you today. Thank you so much for
attending our session. - Thank you.
(audience applauding)

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=0s) - Hello, everybody, and
welcome to the session.

[00:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3s) My name is Federica Ciuffo.

[00:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=5s) I'm Italian, but I live
in Spain, in Madrid.

[00:08](https://www.youtube.com/watch?v=8fes5sP0rs0&t=8s) So happy to see you
all here today with us.

[00:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=12s) And today with me is also Sai Vennam.

[00:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=16s) - Hey, everyone. Sai here.

[00:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=17s) I'm a container specialist at AWS.

[00:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=19s) I'm based out of Austin, Texas,

[00:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=21s) but originally I'm from India

[00:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=23s) and excited to talk to you guys

[00:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=25s) about networking strategies
for Kubernetes today.

[00:28](https://www.youtube.com/watch?v=8fes5sP0rs0&t=28s) This is a 400-level talk,

[00:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=30s) but I'll just give you a quick heads-up

[00:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=32s) that we're gonna start at
smaller levels of complexity

[00:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=35s) and kind of build up as we
get to the end of the session.

[00:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=38s) Let's go ahead and get started.

[00:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=39s) - Yeah, and actually we
have built the agenda

[00:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=42s) with all the interactions
that we have with customer

[00:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=45s) during this 2024 as we are
both container specialists,

[00:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=48s) so we have a lot of conversation

[00:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=50s) around Kubernetes networking.

[00:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=52s) And so we wanted to highlight

[00:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=55s) the most interesting customer interaction

[00:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=58s) that we had during the year

[01:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=60s) and also the, you know,
most-asked questions.

[01:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=63s) And to make this, what, session,

[01:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=66s) a little bit more interactive.

[01:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=67s) We have translated
those customer questions

[01:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=71s) and topics into requirements
of an application.

[01:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=76s) This will be the rental store application,

[01:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=79s) and today, well, we will
take, do a little bit

[01:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=83s) of role play, Sai and I.

[01:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=85s) So I will be a cloud architect

[01:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=87s) who is responsible of
architecting the clouds

[01:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=91s) and also Kubernetes clusters
to run this application,

[01:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=95s) while Sai-

[01:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=96s) - Yeah, I'm gonna be the
cluster operator, right?

[01:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=98s) So I can say that with most of the people

[01:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=101s) that I've talked to at sessions today,

[01:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=103s) I'm guessing a lot of
you in the audience today

[01:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=105s) are on a platform team at your company

[01:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=108s) operating Kubernetes clusters,

[01:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=109s) and I hope to kind of
emulate that role today.

[01:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=112s) So Federica's gonna give me requirements.

[01:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=114s) She's gonna come from a position

[01:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=115s) of being a really
well-versed cloud architect,

[02:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=120s) and she's gonna be giving me demands

[02:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=121s) that I have to fulfill
as the platform team.

[02:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=124s) So that's kind of the back and
forth we're gonna try to do.

[02:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=126s) - Yeah, so we'll put our hats on.

[02:08](https://www.youtube.com/watch?v=8fes5sP0rs0&t=128s) - All right.

[02:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=129s) - And so we, Sai, we have
different requirements

[02:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=132s) for our application.

[02:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=135s) The first thing that I want to do

[02:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=138s) is actually to simplify your life

[02:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=141s) and make it easier to
simplify cluster operations,

[02:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=145s) so let's streamline that
as much as possible,

[02:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=149s) as well as our application
is an external application,

[02:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=152s) so our customer will be able

[02:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=153s) to actually access it externally.

[02:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=158s) So we will see how to do that together.

[02:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=161s) And we also need some,
let's say we want to improve

[02:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=167s) their resiliency in general,
in particular of the network,

[02:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=171s) but also based on the
findings that we find,

[02:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=175s) we also want to be able to
observe this architecture

[03:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=180s) and this application
at each time in a more,

[03:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=184s) in a way that doesn't really
burden my application teams,

[03:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=187s) which are, well, spending a
lot of time into observing

[03:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=192s) but without a really
clear way of how to do so

[03:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=195s) with many microservices.

[03:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=197s) We also have some requirements
from security teams,

[03:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=200s) so we need to enforce that.

[03:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=202s) And we want to be able to
take a different approach

[03:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=207s) as to tackle those
disruptions within the cluster

[03:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=213s) when we make new updates, for example.

[03:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=216s) For example, we have to update the cluster

[03:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=219s) each three months and things like this.

[03:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=220s) So all of these operations
that can be disruptive,

[03:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=224s) right now, we are doing it

[03:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=226s) with the in-place upgrades, et cetera,

[03:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=228s) but we want to have a
deeper look into something

[03:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=232s) that could be a little
bit less disruptive,

[03:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=234s) like blue-greens in that sense.

[03:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=237s) But before diving deeper into that,

[04:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=240s) I think, Sai, I already
sent you the application,

[04:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=244s) so if we can take a look.

[04:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=246s) - Yeah, let's take a look

[04:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=247s) at the application really quickly here.

[04:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=249s) So I'm gonna switch this
to my computer here,

[04:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=253s) and as a heads-up, okay, that's,

[04:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=256s) the wrong screen is being shared there.

[04:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=258s) So give us just one second.
Let's see what's going on here.

[04:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=262s) - Yeah, so in the meantime, let's review

[04:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=266s) what we want to do in that sense.

[04:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=269s) But well, let me review
how we are gonna deploy

[04:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=275s) the application where actually we live

[04:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=277s) while Sai reviews where
he has the application.

[04:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=281s) So in that sense,

[04:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=286s) our organization has
different business units,

[04:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=292s) and each business unit
has a dedicated account.

[04:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=298s) Also, we have some
on-premises data centers

[05:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=301s) that we need to take into consideration.

[05:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=303s) And everything is actually
connected with Transit Gateway.

[05:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=309s) There is also, well, some direct connects

[05:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=314s) and et cetera for the environment.

[05:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=316s) So I think we got the application, right?

[05:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=322s) - Yes, we got it.

[05:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=323s) Perfect timing, all right, excellent.

[05:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=325s) So let me make this a little bit bigger.

[05:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=327s) So we were saying that
we had the local version

[05:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=330s) of the application up and running.

[05:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=331s) So Federica's team has
basically built containers

[05:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=334s) on their local machines, and to do so,

[05:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=338s) they've built a version

[05:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=339s) of this retail store sample application

[05:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=341s) that runs locally without
running on the cloud.

[05:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=344s) And let's just see what that looks like

[05:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=346s) by running a quick command here
to start up the application.

[05:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=351s) All right, we're gonna set
the MySQL password, pass,

[05:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=356s) and then do a docker-compose up.

[05:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=359s) And I think this is a great way

[06:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=361s) to work with containers locally.

[06:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=363s) You can see what it did there

[06:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=364s) was download the container images,

[06:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=366s) and what it's doing is it's starting up

[06:08](https://www.youtube.com/watch?v=8fes5sP0rs0&t=368s) the application now locally,

[06:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=370s) and in a few seconds
here, it's fully started.

[06:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=373s) And let's actually go
to our local host here

[06:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=376s) to access the application.

[06:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=378s) Boom, there we go.

[06:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=379s) This is our beautiful retail
store sample application

[06:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=383s) running locally.

[06:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=384s) But while this is great for development,

[06:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=387s) it kind of enables iterative
development very quickly

[06:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=390s) with containers on your local machine,

[06:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=392s) we need a way to run
this in the cloud, right?

[06:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=394s) So that's kind of the next step here.

[06:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=396s) - Yeah, exactly, and
actually what we will need

[06:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=399s) is to have a replica of this application

[06:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=402s) in each and every VPC in the environment

[06:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=405s) that is dedicated to the retail account.

[06:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=408s) The application that Sai just showed

[06:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=410s) is made up of different
decoupled components,

[06:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=413s) and we have some
infrastructure dependencies.

[06:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=415s) We have seen the MySQL there.

[06:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=417s) And so let's go right into it.

[07:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=421s) The first thing that we want
to do is to simplify your life,

[07:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=425s) and actually thinking about
the Kubernetes architecture,

[07:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=430s) there are a lot of networking components

[07:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=432s) that we need to configure
and take into consideration,

[07:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=437s) not only the control plane

[07:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=439s) and the different components
that talk to each other,

[07:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=442s) but also how are we gonna bring together

[07:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=445s) control plane and data plane.

[07:28](https://www.youtube.com/watch?v=8fes5sP0rs0&t=448s) Within the data plane also,

[07:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=449s) some very core networking components

[07:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=452s) that we need to take into consideration,

[07:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=454s) and our cluster needs to
be configured with that

[07:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=458s) to be able to use those.

[07:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=459s) For example, we have
kube-proxy, CoreDNS, the CNI,

[07:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=464s) so a lot of things, and
we want to simplify that,

[07:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=467s) and this is actually
where Amazon EKS can help.

[07:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=472s) And so, Sai, do you want
to take this one and so-

[07:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=475s) - Yeah, absolutely.

[07:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=476s) So let's talk a little
bit about Amazon EKS.

[07:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=478s) And you guys might be wondering,

[08:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=480s) "Sai, this is a networking talk.

[08:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=481s) Why are we talking about EKS?"

[08:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=483s) Believe me, I'm getting to it.

[08:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=485s) So Amazon EKS is really
just managed Kubernetes.

[08:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=489s) It's not our special
version of Kubernetes.

[08:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=492s) It's open source, upstream,
conformant Kubernetes

[08:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=495s) that we help manage for you.

[08:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=497s) Now, when we first launched
Amazon EKS, you know,

[08:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=501s) about six years ago now, the
focus was on helping customers

[08:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=505s) by managing the control plane.

[08:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=507s) So you kind of saw there
with that very neat animation

[08:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=510s) the capabilities that
we're managing for you

[08:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=513s) with the control plane.

[08:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=514s) But we're taking this a step further,

[08:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=516s) and I think all of you know

[08:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=517s) what I'm about to talk about here,

[08:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=519s) but it was an announcement
that we released

[08:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=521s) just earlier this week.

[08:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=523s) Now Amazon EKS is helping customers manage

[08:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=527s) parts of the data plane as well.

[08:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=529s) So essentially what Auto
Mode enables customers to do

[08:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=532s) is have EKS clusters that are ready

[08:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=535s) for production use cases out of the box.

[08:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=538s) All of these components
that you as platform teams,

[09:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=541s) me as a platform operator
had to manage on my own

[09:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=545s) are now managed for you.

[09:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=546s) And the scope and the purview
of Auto Mode is, you know,

[09:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=550s) is continuing to increase.

[09:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=551s) You can check out the road map.

[09:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=553s) A lot of it is public on GitHub.

[09:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=557s) And so critically, so
where Auto Mode fits in

[09:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=560s) with networking is that a number

[09:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=562s) of key networking components

[09:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=564s) are managed for you in Auto Mode.

[09:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=566s) Let's dive into these really quickly.

[09:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=569s) For one, the VPC CNI is
gonna be managed for you now.

[09:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=574s) So this is the, you know,
the one that's by default

[09:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=577s) set up with every EKS cluster

[09:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=578s) but no longer managed by
you in your data plane.

[09:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=582s) We handle it for you.

[09:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=584s) That means when you
upgrade your control plane,

[09:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=586s) those add-ons are
upgraded for you as well.

[09:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=589s) This means less cognitive overload

[09:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=590s) of managing different
components of your data plane.

[09:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=593s) In addition, CoreDNS out of
the box as well as kube-proxy,

[09:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=598s) these are all gonna be
kind of managed for you.

[10:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=601s) In fact, there's actually
one more thing here

[10:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=602s) that's gonna be managed for you,

[10:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=604s) the application Load
Balancer Controller as well,

[10:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=607s) which would be coming out of the box

[10:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=610s) with all EKS Auto Mode clusters.

[10:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=613s) So put all of that together,

[10:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=615s) and essentially what
you have is Amazon EKS

[10:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=618s) managing more capabilities for you

[10:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=621s) in the control plane and data plane.

[10:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=623s) But Federica, you've looked
into a little bit about CNIs.

[10:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=627s) Can you explain your requirements
and why you wanna use

[10:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=630s) this CNI versus maybe some other ones?

[10:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=633s) - Yeah, exactly, so we are going to,

[10:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=636s) for the Amazon VPC CNI actually,

[10:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=639s) because it simplifies a bit

[10:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=641s) how can we do Kubernetes within AWS.

[10:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=646s) Effectively, the Amazon VPC
CNI, it's deeply integrated

[10:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=650s) with the underlying
network that is Amazon VPC,

[10:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=653s) and thus it assigns IPs
from Amazon VPC to pods.

[10:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=659s) And this is great for
us because it enables us

[11:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=662s) to take advantage of all the
good things of Amazon VPC.

[11:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=666s) Like for example, we can do security.

[11:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=669s) We can do also observability
with VPC flow logs.

[11:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=672s) Also the CNI is highly customizable.

[11:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=677s) That is, we can really fit the CNI

[11:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=681s) and change all the specs to our needs.

[11:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=684s) And this is great for us.

[11:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=686s) Also, we need to consider
there are other alternate CNIs

[11:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=690s) that are compatible with
EKS but not supported.

[11:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=694s) What does that mean?

[11:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=695s) That it is recommended to have support

[11:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=699s) from the vendor of the CNI of your choice.

[11:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=703s) But we are gonna stick with this CNI,

[11:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=705s) and actually I love how the all of these,

[11:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=709s) well, Amazon EKS, then on top of that,

[11:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=712s) Auto Mode helps your life and
your team to really streamline

[11:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=716s) and take that heavy
lifting out of your team

[12:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=721s) and lets AWS handle this.

[12:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=725s) - Yeah, I'm glad that you're
okay with using the VPC CNI,

[12:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=727s) 'cause that makes my life easier.

[12:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=729s) It's integrated into the AWS
ecosystem as a platform team,

[12:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=732s) less things for me to
worry about managing.

[12:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=734s) - And actually you mentioned
before about load balancer,

[12:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=738s) Load Balancer Controller.

[12:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=740s) So this is actually tied
to our next requirement,

[12:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=744s) and our next requirement,
I want my customers

[12:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=747s) to be able to access my application.

[12:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=750s) Now, great what Sai just showed us

[12:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=753s) that he was running locally,
but this is not what we need.

[12:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=756s) So we need something more.

[12:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=758s) And when we are thinking about
how to access application

[12:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=762s) from outside the cluster
to our backend pods,

[12:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=766s) we always need some Kubernetes objects,

[12:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=770s) that is, ingress and service resources,

[12:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=774s) ingress resources
operating at the Layer 7,

[12:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=776s) application layer, and
service resources operating

[13:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=781s) at the network transport layer.

[13:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=783s) But we need something more.

[13:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=785s) We need some infrastructure
piece that help us to let that,

[13:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=791s) let's say, traffic from
outside the classroom

[13:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=794s) inside the classroom.

[13:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=795s) And that piece usually is
a proxy, a load balancer.

[13:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=799s) So in AWS, there is a native way to do so

[13:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=803s) by using the AWS Load Balancer Controller.

[13:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=806s) And I'm very excited
about the capabilities

[13:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=810s) of AWS Load Balancer Controller,

[13:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=812s) because again, I want to
simplify my team's work

[13:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=815s) with operating with Kubernetes on AWS.

[13:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=818s) The AWS Load Balancer
Controller automatically deploys

[13:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=822s) an application load balancer
with ingress resources,

[13:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=825s) and a service, with service resources,

[13:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=827s) it automatically deploys
a network load balancer,

[13:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=830s) so native AWS load
balancers that actually have

[13:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=836s) all the ability and reliability,
scalability, et cetera,

[13:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=839s) but in particular, not only
supporting in Auto Mode,

[14:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=842s) as we were saying before,
but in particular,

[14:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=845s) I want to dive deeper
into what it can do for us

[14:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=850s) at Layer 7, because if you think about it,

[14:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=854s) we are actually using an
application load balancer.

[14:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=858s) The application load balancer itself

[14:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=861s) is a Layer 7 load balancer.

[14:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=863s) So what does this mean?

[14:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=865s) So all the capabilities,
all the Layer 7 processing

[14:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=869s) happens at a load balancer layer,

[14:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=873s) that is, can be offloaded from, you know,

[14:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=877s) the configuration that
your application teams

[14:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=879s) and my application teams need
to do to the load balancer.

[14:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=882s) For example, certificates,
it can be offloaded

[14:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=887s) to the load balancer, and
then it can also be managed

[14:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=891s) by AWS certificate management,
so a certificate manager

[14:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=896s) that it is actually deeply integrated

[14:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=899s) with AWS Load Balancer Controller itself.

[15:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=902s) And we can take advantage
of all those integration

[15:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=905s) between the AWS Load Balancer

[15:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=909s) and the security and
natural suite within AWS.

[15:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=912s) And this is great for us
because it simplifies our life.

[15:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=916s) Additionally, there is
another way you could,

[15:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=920s) you know, deploy or
handle ingress traffic,

[15:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=923s) that is, use a third-party
ingress controller.

[15:28](https://www.youtube.com/watch?v=8fes5sP0rs0&t=928s) You can see here that now the processing,

[15:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=931s) the layers in processing and features

[15:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=934s) shifts from being a responsibility
of the load balancer

[15:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=939s) to being the responsibility
of the controller itself.

[15:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=943s) And this is key because, for example,

[15:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=945s) where before we could offload
the SSR certificate management

[15:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=949s) to the load balancer, now
we need to supply that

[15:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=952s) to the ingress controller.

[15:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=953s) And this is essentially very different.

[15:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=956s) Another thing that is different

[15:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=959s) and adds a little bit more management

[16:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=961s) is that you are handling
only ingress resources.

[16:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=966s) So if you need to handle
service resources,

[16:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=969s) you will need an additional controller,

[16:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=972s) a service controller.

[16:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=974s) With EKS, this used to
be very transparent to do

[16:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=979s) with the in-tree load balancer controller

[16:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=981s) or service controller, but
that has not gone away.

[16:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=986s) It's still there, but we are only pushing,

[16:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=990s) let's say, updates.

[16:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=992s) There are essential
security updates to it.

[16:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=994s) So what it is actually recommended again

[16:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=998s) for handling the service
deployment of load balancers

[16:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1003s) is again, the AWS Load
Balancer Controller.

[16:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1006s) Funny enough, if you're
using an ingress controller,

[16:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1008s) you will still need the AWS
Load Balancer Controller

[16:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1012s) to deploy the load balancer

[16:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1013s) that is in front of the ingress
controller of your choice.

[16:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1017s) So Sai, I am, we have gone
through the differences

[17:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1022s) and so what we can do with the
AWS Load Balancer Controller,

[17:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1025s) third-party controllers,

[17:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1027s) but can we see it in
action with my application?

[17:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1031s) That would be amazing.

[17:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1032s) - Let's do it.

[17:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1033s) So we're gonna get into
our first kind of real demo

[17:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1036s) that Docker composed one,
not a real demo really,

[17:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1039s) but here we're gonna jump
into actually exposing

[17:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1041s) an application using an
application load balancer

[17:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1045s) that's Layer 7-based load balancing.

[17:28](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1048s) And just very quickly I wanna say here

[17:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1049s) that I love this diagram

[17:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1051s) because you can kind of see how, you know,

[17:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1053s) when you create an ingress resource,

[17:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1054s) obviously it gives you more
advanced path-based routing

[17:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1057s) that operates at the Layer 7 level.

[17:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1060s) You can create those with
custom ingress controllers

[17:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1062s) or the AWS Load Balancer Controller.

[17:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1065s) And at the Layer 4 level, if
you wanna get a load balance

[17:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1069s) for each individual service,

[17:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1071s) you can do so with the
network load balancers

[17:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1074s) that are also kind of, you can create

[17:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1076s) with the AWS Load Balancer Controller.

[17:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1079s) All right, so let's go
ahead and get into this.

[18:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1082s) So in my EKS cluster here,
we've basically deployed all of,

[18:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1087s) oh, I can tell the internet connection's

[18:08](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1088s) already a little bit, we're
gonna get all the pods

[18:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1092s) in the cluster, but in this cluster,

[18:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1093s) we've already deployed the containers

[18:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1096s) for the retail sample
application that we have today.

[18:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1101s) And critically, you can see here

[18:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1102s) that we've also deployed the
AWS Load Balancer Controller.

[18:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1107s) By the way, if you were
to run this command

[18:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1109s) in an Auto Mode cluster,
you wouldn't see those pods,

[18:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1113s) 'cause those, the Load Balancer Controller

[18:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1115s) is managed for you.

[18:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1116s) But since I'm running on a
standard cluster, not Auto Mode,

[18:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1120s) this is something that
I had to install myself.

[18:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1122s) And then obviously when
I upgrade the cluster,

[18:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1124s) I would also have to handle upgrading

[18:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1126s) the Load Balancer Controller itself.

[18:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1130s) Okay, once that controller is installed,

[18:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1132s) essentially what Kubernetes
is now able to do

[18:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1135s) is anytime an ingress resource is created

[18:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1138s) or a service with the type load balancer,

[19:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1141s) the controller kicks in.

[19:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1142s) It says, "Oh, I know what to do now,"

[19:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1144s) and in the backend, it's
gonna start creating resources

[19:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1146s) for us in AWS, and it's
deeply integrated, right?

[19:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1149s) A lot of things happening,
especially if you're doing,

[19:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1151s) you know, custom domains
and you have certs

[19:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1153s) and that kind of thing.

[19:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1155s) There's a lot going on in the
backend with Route 53 and ACM,

[19:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1158s) you know, certificate
authority and all of that

[19:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1161s) that the Load Balancer
Controller will handle for you.

[19:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1164s) So I did create an ingress resource,

[19:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1167s) so I'm gonna run get
Ingress in all namespaces,

[19:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1171s) and there we go.

[19:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1171s) We can see fairly straightforward here

[19:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1173s) that we have an ingress,
it has an address.

[19:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1176s) We'll copy it and access
it, but before I do that,

[19:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1178s) I do wanna quickly show you
what's in that ingress yaml.

[19:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1182s) And this is really
critical here to understand

[19:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1184s) how specifying an ingress works,

[19:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1187s) because you can kind of
see a few things here.

[19:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1189s) Notably, there's annotations,

[19:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1192s) and these tell the application
load balancer controller,

[19:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1195s) ALB, that we're creating for this ingress

[19:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1199s) something that's internet
facing, not internal only.

[20:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1201s) So we want public
internet access for this.

[20:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1203s) We want the target type to be IP mode,

[20:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1206s) and the other option is instance mode.

[20:08](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1208s) I won't get into this in in
too much depth right now,

[20:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1211s) but I'll share some resources
for how you can dive deeper

[20:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1214s) into the reason why we
provide both options.

[20:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1218s) In addition, a health check
path so that the target group

[20:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1221s) knows whether it's healthy or not.

[20:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1223s) And then the other critical piece here

[20:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1225s) is the service it's
actually routing to, right?

[20:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1227s) So if I do a quick get
svc in the UI namespace,

[20:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1232s) what I'll see is the UI
service here, port 80,

[20:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1238s) and that's essentially
what we're routing to

[20:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1239s) with that ingress.

[20:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1240s) Okay, last thing I wanna call out here,

[20:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1242s) 'cause I've gotten this
question a lot this week,

[20:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1244s) the question is, with Auto Mode,

[20:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1246s) do you have to do anything special

[20:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1248s) to use the AWS managed version

[20:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1251s) of the Load Balancer Controller

[20:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1252s) versus the one that's just
running in your cluster

[20:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1255s) with non-Auto Mode clusters?

[20:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1257s) And by the way, since
you can add Auto Mode

[21:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1260s) to your existing
clusters, this is critical

[21:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1262s) for how you're gonna migrate

[21:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1263s) to the AWS managed
version of the controller.

[21:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1266s) Essentially, you'll notice here

[21:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1267s) there's an ingress class name.

[21:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1269s) So when you wanna use the
Auto Mode managed version

[21:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1272s) of the controller,
essentially what you'll do

[21:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1274s) is you'll create a new ingress class

[21:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1276s) that specifies that you
want ingress resources

[21:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1279s) to be handled by that controller instead.

[21:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1281s) This makes it really seamless
for you to migrate clusters

[21:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1283s) to Auto Mode because you
simply need to install

[21:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1286s) that new ingress class and then
switch the kind of ingresses

[21:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1291s) that you have to the new ingress class.

[21:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1294s) And then you can, you know,

[21:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1296s) remove the load balancer
controller from your cluster.

[21:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1299s) You no longer need to manage it.

[21:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1300s) Okay, now that we've seen all that,

[21:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1303s) I'm gonna pray a little
bit to the demo gods

[21:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1305s) of the internet is all work, actually,

[21:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1306s) that loaded perfectly
fast, thank you. (chuckles)

[21:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1309s) So you can see here that the application

[21:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1311s) running in the cloud in Kubernetes

[21:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1313s) fronted by an ingress resource,

[21:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1316s) so application load balancing.

[21:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1318s) All right, guys, I promise
you we are starting

[22:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1320s) at a lower level of complexity,
and we're gonna bump it up

[22:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1322s) as we kind of go through the presentation.

[22:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1324s) So with this demo, I'm gonna
pass it back to you, Federica,

[22:08](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1328s) and let's get into some more fun stuff.

[22:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1331s) - PowerPoint, yeah,
and actually thank you,

[22:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1335s) because this is our first requirements.

[22:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1337s) Again, we wanted to
start simple for my teams

[22:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1340s) that are adopting Kubernetes
clusters with Amazon EKS,

[22:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1344s) and there are a lot of things
that you can also do with,

[22:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1347s) you know, adding certificates
to this domain and et cetera.

[22:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1350s) So thank you, Sai, for
showing us how we can,

[22:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1354s) how could we can do this, but
we have other requirements.

[22:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1359s) So let's see this.

[22:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1362s) So with my teams, we
have a lot of problems

[22:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1368s) when it comes to network resiliency,

[22:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1370s) because as long as we
are already following

[22:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1373s) all the best practices,

[22:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1375s) spreading pods across availability zones

[22:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1378s) with topology spread constraints,
we are also deploying

[23:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1382s) a lot of reliability built-in mechanism

[23:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1385s) within the applications.

[23:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1387s) But for us, it is really difficult

[23:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1389s) to test disaster recovery scenarios.

[23:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1393s) So one thing that can help us to do that

[23:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1396s) is actually the new
integration of Amazon EKS

[23:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1400s) with ARC, Amazon Recovery Controller.

[23:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1403s) And this makes easy for us to test

[23:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1406s) and recover from a recovery scenario

[23:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1409s) because we don't have to wait

[23:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1412s) for the health checks
on the services to fail.

[23:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1415s) But actually our controller will signals

[23:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1420s) that the AZ is down, and so the targets,

[23:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1424s) the endpoints that are
in the affected zone

[23:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1427s) will automatically be
deregistered from the service.

[23:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1431s) And this is great for us.
- So Federica,

[23:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1433s) I've gotta ask, so I don't
know what ARC is just yet,

[23:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1436s) so you gotta tell me, why do we need ARC

[23:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1438s) when the whole reason
we're using Kubernetes

[24:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1440s) is because when pods are unhealthy,

[24:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1443s) they automatically stop
getting traffic routed to them?

[24:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1445s) So what's the point of using ARC?

[24:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1447s) - The problem is that
there is a delay to it,

[24:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1450s) so we need to wait for
those health checks to fail,

[24:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1452s) and then the targets will be deregistered.

[24:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1455s) That will be a lot of problems.

[24:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1457s) So ARC shorten that time

[24:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1461s) because automatically in AWS API,

[24:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1463s) they signals that as soon as
there is an AZ, let's say,

[24:28](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1468s) failure, and this is automatically done.

[24:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1471s) It is true that my team responsibility

[24:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1474s) will also be to make that
application resilient.

[24:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1478s) - Okay, so essentially while
Kubernetes could detect

[24:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1481s) that the pods are unhealthy
and stop routing traffic to it,

[24:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1484s) it takes a little while because
essentially the health check

[24:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1487s) has to fail, the readiness probes,

[24:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1488s) the health probes, and then it happens,

[24:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1490s) so this could impact your customers.

[24:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1492s) But here, you know, essentially
we're improving availability

[24:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1496s) by making it a little bit faster

[24:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1497s) where the second there's an AZ issue,

[24:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1499s) we'll just zonal shift
that traffic, right?

[25:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1502s) - Correct.
- Awesome.

[25:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1503s) - And also it's very interesting for us,

[25:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1505s) the thing that we can
test those scenarios,

[25:08](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1508s) even if there isn't a real AZ failure, so.

[25:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1514s) About testing those scenarios,

[25:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1515s) I mentioned that my teams
actually have built a lot

[25:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1520s) on the application to ensure reliability.

[25:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1523s) And it has been a long work

[25:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1525s) because first we need to observe

[25:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1527s) where bottlenecks or
potential failures are.

[25:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1530s) Then you need to implement
within the application.

[25:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1533s) Then there is application
aid that is using

[25:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1535s) an application coding
language, programming language,

[25:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1539s) another with another programming language.

[25:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1541s) So it's kind of a mess for us.

[25:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1543s) And I was looking from an
architectural perspective

[25:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1546s) for a way for us to unify those operation

[25:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1549s) and take that burden away
from my application teams.

[25:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1554s) So maybe in the ecosystem,

[25:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1557s) the most-used way to do so
is adopting service meshes.

[26:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1562s) And real quick, what's a service mesh?

[26:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1564s) So in the most common
architecture for service mesh,

[26:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1569s) you take a proxy, you put it

[26:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1571s) next to your application containers.

[26:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1575s) You do that for each application container

[26:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1577s) within the cluster, and
you create basically

[26:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1580s) a new layer that is made
off of all of those proxies,

[26:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1584s) and you push to that layer
the advanced network security

[26:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1591s) and network observability responsibility.

[26:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1595s) Thus you are decopying that

[26:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1597s) from the application business logic

[26:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1598s) that still will be
handled by the developers.

[26:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1603s) Too, those other things
that are now unified

[26:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1606s) with only one programming language

[26:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1608s) because you will be
using that actually proxy

[26:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1612s) for each and every application.

[26:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1613s) So it makes my life easier,

[26:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1615s) makes my application life easier,

[26:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1618s) and it is very powerful.

[27:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1620s) If you look at the capabilities

[27:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1622s) and what service meshes bring to us,

[27:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1625s) all of the things that we
want to do are actually there.

[27:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1629s) We want to be able to
observe, for example,

[27:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1632s) tracing requests, understand
what bottlenecks are,

[27:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1635s) and then we want to be able to implement

[27:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1638s) those reliability features,
not within the application

[27:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1641s) but within the service mesh.

[27:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1643s) Also security feature to it
where I have a lot of requests

[27:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1646s) from my security team around, for example,

[27:28](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1648s) mutual TLS and securing
the workloads, et cetera.

[27:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1653s) So that's a really big ask,

[27:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1655s) although service meshes also
come with some challenges.

[27:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1660s) - Right, Federica, I love the fact

[27:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1662s) that you covered all the advantages,

[27:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1663s) but you're kind of leaving out

[27:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1666s) the part of me as the
operator having to manage

[27:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1669s) all the challenges of
running a service mesh.

[27:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1672s) And you know, traditionally
the kind of service meshes

[27:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1675s) we're talking about
here, things like Istio

[27:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1677s) that work off of the sidecar model, right?

[27:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1679s) And so the challenges, well, some of them

[28:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1681s) are gonna be things like resource
efficiency issues, right?

[28:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1685s) So when sidecars are not being
utilized to max efficiency,

[28:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1689s) or you know, the fact that
sidecars need to scale up

[28:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1692s) with every pod as they scale
up, this can be challenging.

[28:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1695s) In addition, just installing the sidecars

[28:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1698s) into a cluster is not so easy.

[28:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1700s) It requires the pods be restarted

[28:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1702s) because every time you add the sidecar,

[28:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1703s) the pod needs to go
through a restart cycle.

[28:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1706s) That's not great either.

[28:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1707s) In addition, additional points of failure,

[28:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1710s) security boundaries, these are all things

[28:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1711s) that as the platform team I
need to be thinking about.

[28:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1715s) And of course, I do wanna implement

[28:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1717s) organizational best
practices at the same time

[28:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1719s) because as the platform
team, I've been told

[28:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1721s) all service-to-service
communication has to be encrypted,

[28:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1725s) has to go over mutual TLS,
so we need some solution.

[28:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1729s) So I like the idea of using a service mesh

[28:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1732s) because you know, Federica's
team doesn't have to instrument

[28:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1735s) each single application
with all of the things

[28:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1737s) that we need for observability security.

[28:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1739s) We can add it as a layer on top,

[29:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1741s) which removes complexity from her team.

[29:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1743s) Adds a little bit to mine,

[29:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1744s) but I think we have an approach
to this, Istio Ambient Mesh.

[29:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1750s) So essentially Istio Ambient Mesh,

[29:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1752s) what it's gonna do is enable us

[29:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1754s) to get the same advantages of Istio

[29:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1758s) in a traditional sidecar model

[29:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1760s) but without the sidecars,
and the way it does this

[29:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1764s) is by essentially encrypting traffic

[29:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1766s) between services into a ztunnel proxy.

[29:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1771s) This particular protocol that it uses,

[29:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1773s) it's an Istio-specific term called HBONE,

[29:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1777s) HTTP-Based Overlay Network Environment.

[29:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1781s) So when you break that apart,
it's not that complicated.

[29:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1783s) It's an environment that
overlays on top of your network,

[29:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1786s) and it's based on HTTP.

[29:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1788s) And the interesting thing about this

[29:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1789s) is that essentially what it'll do

[29:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1791s) is make it so that all of the traffic

[29:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1793s) going between your services
now goes through this ztunnel.

[29:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1797s) That enables us to have
mutual TLS out of the box.

[30:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1803s) No pods need to be restarted.

[30:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1805s) The traffic goes from
working at a network layer,

[30:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1810s) working in your network,

[30:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1812s) to going through the ztunnel, right?

[30:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1814s) So that happens as kind
of a switch that flips,

[30:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1817s) and to show that, I want
to actually jump to a demo.

[30:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1820s) And by the way, I know that you saw a bit

[30:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1822s) about waypoint proxies as well.

[30:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1824s) I'll get to that in a second.

[30:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1825s) That's for Layer 7 capabilities.

[30:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1826s) We're gonna focus on Layer 4.

[30:28](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1828s) That's IP addresses,
Layer 4 authorization.

[30:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1831s) Think IPs and ports

[30:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1832s) rather than fully qualified domain names,

[30:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1834s) PATs, domains, that kind of thing.

[30:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1836s) Okay, so let's take a look
at my cluster environment.

[30:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1840s) I'm gonna use K9s, and
if you don't use this,

[30:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1843s) I highly recommend it.

[30:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1844s) It's a great way to step
through your clusters,

[30:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1846s) see what's running, that kind of thing.

[30:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1848s) And in this cluster,
oh, yeah, the internet's

[30:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1852s) a little bit slow here, but there we go.

[30:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1854s) We can see that I've
already installed Istio.

[30:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1856s) Now, this is a non-disruptive
activity, by the way.

[30:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1859s) It's kinda like a Helm chart.

[30:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1859s) You just install into the cluster.

[31:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1861s) These pods get started, and you can see

[31:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1863s) that it comes with some
observability tools

[31:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1865s) like Grafana, Prometheus, Kiali, Jaeger,

[31:08](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1868s) and the control plane for Istio as well,

[31:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1870s) as well as an ingress gateway

[31:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1871s) for how traffic gets routed
through Istio instead.

[31:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1875s) Okay, and you can see that, yeah,

[31:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1876s) these pods haven't been restarted

[31:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1878s) actually in the last 26 days.

[31:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1882s) And so real quick, let's take a look.

[31:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1884s) There's a helpful command
that istioctl exposes for us

[31:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1887s) called ztunnel-config workloads.

[31:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1890s) And this is all the
workloads in our cluster,

[31:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1892s) and we can see that right
now, that protocol is TCP,

[31:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1896s) and that essentially telling us

[31:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1898s) it's not going over the HBONE protocol.

[31:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1900s) We don't have that mutual
TLS enabled just yet.

[31:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1904s) And to enable that, we simply need to,

[31:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1907s) this is really cool in my opinion,

[31:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1909s) label the default namespace
with this annotation,

[31:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1913s) just with this label rather.

[31:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1915s) We set the data plane mode
to ambient, and that's it.

[32:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1920s) Now the traffic is gonna start going

[32:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1922s) through the HBONE proxy.

[32:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1924s) So we'll run that istioctl command again,

[32:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1926s) and there we go.

[32:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1927s) Now all those workloads
that were TCP before

[32:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1930s) are now going over the HBONE protocol.

[32:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1932s) Can ignore these.

[32:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1933s) There are some admin
control plane-type services.

[32:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1936s) Those don't need to be changed.

[32:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1937s) But for our actual application workloads,

[32:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1939s) they're going over HBONE,

[32:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1941s) and let me just get
the services real quick

[32:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1943s) so I can access it.

[32:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1944s) I'm gonna grab the one for
the Istio ingress gateway.

[32:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1947s) Apologize, it's a little hard to read,

[32:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1949s) but I'm just gonna grab the Istio piece.

[32:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1951s) And so remember, our
applications weren't restarted.

[32:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1953s) I need to do a couple of
cache list reloads here

[32:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1955s) just to hit the application
here, but there we go.

[32:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1958s) We access our application.

[32:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1960s) Pod-to-pod communication is
happening with mutual TLS.

[32:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1963s) No downtime, no pod restarts.

[32:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1966s) We have Ambient Mesh
enabled in our cluster.

[32:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1968s) But when we think about Istio,

[32:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1971s) we don't just use Istio for mutual TLS.

[32:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1974s) That seems like a bit of an overkill.

[32:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1977s) We get a lot of other advantages
with Istio as well, right?

[32:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1979s) So observability is one
of the critical ones.

[33:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1982s) So I would love to show you

[33:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1984s) how to enable observability
capabilities as well.

[33:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1987s) So very quickly, just jumping
back to the slides here,

[33:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1991s) with ztunnel, we have this
mutual TLS out of the box.

[33:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1994s) We have Layer 4 authorization policies

[33:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1996s) that we can implement as well.

[33:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=1997s) Istio is great for the
Layer 7 capabilities, right,

[33:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2000s) so more advanced traffic
routing and that kind of thing.

[33:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2003s) So with a waypoint, essentially what we do

[33:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2006s) is we have traffic that now goes through

[33:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2010s) the separate waypoint that's
running on the cluster,

[33:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2012s) and this is what's gonna
give Istio the ability

[33:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2015s) to do Layer 7 capabilities
and really rich observability.

[33:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2018s) In fact, we're also gonna do a demo

[33:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2020s) of chaos engineering here in a minute.

[33:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2022s) Another popular use case

[33:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2024s) for why you would want this waypoint

[33:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2026s) for Layer 7 capabilities
is canary deployments.

[33:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2029s) Let's say you have a new
feature that you wanna roll out

[33:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2031s) to a subset of your users,
maybe users on Firefox

[33:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2034s) or users on a mobile phone.

[33:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2036s) All of that becomes just a flip

[33:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2038s) that we can switch at the network layer.

[34:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2040s) The app teams don't need to
necessarily change any code.

[34:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2043s) We can do that at the network
layer, that overlay layer.

[34:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2046s) It's really powerful stuff.

[34:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2047s) Let's take a look at what that looks like.

[34:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2049s) We're gonna jump back to my machine here,

[34:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2053s) and to enable the waypoint,

[34:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2055s) let me make this a little bit
easier for you all to see.

[34:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2058s) Okay, to apply the waypoint,
essentially what I'll do

[34:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2062s) is run this istioctl helper command

[34:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2065s) that applies the waypoint
in the default namespace,

[34:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2069s) and that's it.

[34:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2070s) Again, no pods are restarting

[34:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2071s) because this just starts a new pod,

[34:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2074s) and we'll get deployments in the cluster,

[34:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2076s) and we can see that we seven seconds ago

[34:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2078s) started this new waypoint,

[34:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2080s) and now we should have
observability in our application.

[34:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2084s) I'm just gonna refresh this a couple times

[34:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2085s) to make sure we have some logs,

[34:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2089s) metrics kind of flowing
through the application

[34:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2091s) and that kind of thing.

[34:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2092s) Maybe we'll add a pocket
watch to our card,

[34:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2094s) and we'll hit the checkout button.

[34:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2097s) Okay, awesome. That should be enough.

[35:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2100s) Now we're gonna go back
to our command line

[35:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2102s) and run handy istioctl dashboard kiali.

[35:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2106s) Kiali is an open source
kind of observability tool

[35:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2109s) helping us see exactly
how our application looks.

[35:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2112s) Let's make sure we're
looking at like the last,

[35:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2114s) you know, three hours of data.

[35:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2116s) Okay, that's really hard to read.

[35:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2118s) That's not very interesting to me.

[35:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2120s) So let me start cleaning this up a bit.

[35:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2121s) So I'm gonna hide unknown
nodes. I want an app graph.

[35:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2126s) I'm gonna go here. Oh,
already looking better.

[35:28](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2128s) I'm gonna go here, I'm going to enable

[35:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2130s) some of these things here.

[35:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2132s) I'm gonna get rid of service nodes.

[35:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2134s) I'm gonna do traffic
animations, waypoint proxies.

[35:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2139s) And there we go, so you can already see

[35:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2141s) a lot more that we can see here.

[35:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2143s) Let's disable TCP traffic,

[35:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2145s) 'cause I don't wanna see like
Prometheus stuff going on.

[35:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2148s) And boom, there we go.

[35:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2151s) We can now see kind of a visual layout

[35:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2153s) of our application architecture.

[35:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2156s) I didn't complete a checkout,

[35:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2158s) so that's why this line is black,

[35:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2159s) because we don't have
mutual TLS for this pod,

[36:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2163s) 'cause I didn't actually
do a checkout process.

[36:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2165s) But you can see right here
that it's showing traffic

[36:08](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2168s) for the other pods that were activated

[36:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2171s) when I was clicking around
in that sample application.

[36:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2174s) Click into one of these, and
you can see that, you know,

[36:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2176s) the traffic from UI to carts
has mutual TLS enabled.

[36:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2181s) So pretty cool stuff, in my opinion.

[36:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2183s) In fact, I can even jump
into things like carts

[36:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2185s) and see exactly what
application is talking to what,

[36:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2189s) and I might notice here
that hey, one of my services

[36:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2192s) is talking to a service that it shouldn't,

[36:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2193s) and I could use Istio to
implement an authorization

[36:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2196s) or network policy to prevent
access between services

[36:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2199s) that maybe shouldn't be
talking to one another, right,

[36:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2202s) limiting blast radius,

[36:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2204s) implementing better security practices.

[36:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2207s) Okay, so what did we see here?

[36:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2208s) We saw with Istio Ambient Mesh,

[36:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2211s) without ever restarting any of our pods,

[36:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2213s) any of our applications, we
got Layer 4 capabilities,

[36:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2215s) mutual TLS enabled,
and we were able to get

[36:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2218s) some great observability
out of this as well.

[37:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2221s) I mentioned I wanted to do a
chaos engineering demo for you.

[37:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2224s) So let's talk about that real quick.

[37:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2226s) So in the gateway that I
deployed into this cluster,

[37:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2229s) which is really straightforward,
I'm basically, you know,

[37:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2231s) it's kind of like that ingress resource

[37:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2233s) that I showed earlier.

[37:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2234s) It's just the Istio way of doing it.

[37:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2236s) I've exposed the UI service,

[37:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2238s) and for that UI service,
let's insert a fault.

[37:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2242s) So about 75% of the time, it's gonna fail.

[37:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2246s) And I haven't applied this yet,

[37:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2247s) so let's just make sure I'm
still hitting the application.

[37:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2250s) Yep, all is good. But now
let's apply this new gateway.

[37:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2256s) It should say configured
to virtualservice.

[37:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2258s) There we go, configured.

[37:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2261s) And now 75% of the time
this should fail. Boom.

[37:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2263s) All right, so we hit that fault already.

[37:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2266s) This is really chaos
engineering at its finest.

[37:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2268s) It's seeing how your application
would respond to failures.

[37:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2272s) So we could also do things

[37:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2273s) like maybe implement a
retry policy on failure

[37:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2275s) and see if our application
responds correctly.

[37:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2277s) Let's keep hitting this a few times,

[37:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2278s) 'cause 25% of the time it should work.

[38:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2281s) Wow, that's crazy. Six, I
should not go gambling today.

[38:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2284s) All right, that's seven times
for it to actually work.

[38:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2287s) And we can already see
that there's some issues

[38:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2289s) with the like cache
invalidation that's going on.

[38:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2291s) So I feel like we already
uncovered a bug, right?

[38:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2295s) So maybe when there's a fault

[38:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2297s) we should deal with the
cache a little better

[38:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2299s) so users don't end up seeing
a page like this, really-

[38:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2303s) - [Federica] Something for
my teams to think about.

[38:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2305s) - [Sai] Exactly, exactly. So
what do you think, Federica?

[38:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2309s) Oops, we don't need that.

[38:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2310s) Let's jump to the slides.

[38:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2314s) - Yeah.
- Yeah.

[38:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2315s) - I think this is exactly
what we are looking for,

[38:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2317s) actually, Sai, so thank
you for showing that.

[38:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2319s) I love the fact that really easily

[38:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2322s) we can have mutant TLS in the cluster.

[38:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2324s) That's a very big ask from
security teams, et cetera.

[38:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2328s) So definitely also like all the things

[38:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2331s) that we can do in terms of observability

[38:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2334s) and implementing new
things that will enhance

[38:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2338s) the reliability of our
applications with Istio Ambient.

[39:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2341s) But I also want to put
you on the spot here.

[39:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2344s) So is there any limitation

[39:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2346s) that we should be aware
about for Istio Ambient?

[39:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2350s) - So there is a limitation here.

[39:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2351s) When we first started
implementing Ambient Mesh

[39:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2354s) with this sample, this application,

[39:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2357s) what we saw was that one of the services

[39:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2359s) didn't mesh well with Ambient
mode, no pun intended.

[39:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2364s) Essentially what we saw
was that one of the pods

[39:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2367s) uses the MySQL protocol to
access our persistence layer,

[39:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2371s) and that protocol didn't
play nicely with the ztunnel.

[39:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2374s) It's like, well, what do we do here?

[39:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2376s) Well, there's a really
great thing that we can do,

[39:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2379s) which shows kind of the
flexibility of Ambient Mesh.

[39:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2381s) Essentially what we did, and
I'll pull up K9s again here,

[39:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2386s) my terminal UI, and dig into
that catalog deployment.

[39:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2391s) And I did cheat here a little bit,

[39:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2394s) and you'll notice that in this pod,

[39:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2396s) we have two containers running.

[39:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2399s) And just to show you what
that second container is,

[40:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2404s) it's an Envoy proxy.

[40:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2406s) There we go, so
essentially what we've done

[40:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2409s) for just this catalog
service is enable a sidecar.

[40:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2414s) And so yes, for this
pod, I had to restart it.

[40:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2417s) And you might have noticed when I ran

[40:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2418s) that ztunnel config
workloads command first,

[40:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2421s) there was one service that was already

[40:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2423s) on the HBONE protocol.

[40:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2424s) That was my little cheat.

[40:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2425s) So beforehand, I had
set up that pod already

[40:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2430s) with the sidecar, and so that really shows

[40:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2432s) how flexible Ambient Mesh
can be for certain workloads

[40:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2436s) that don't work on that HBONE
protocol, that ztunnel proxy.

[40:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2440s) Essentially what you do is in
the deployment configuration

[40:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2444s) for just that one catalog service,

[40:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2446s) right, that catalog service,

[40:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2448s) we add this label,
sidecar injection is true.

[40:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2451s) And so for that one pod we have a sidecar,

[40:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2454s) and in fact in Kiali, it showed it as well

[40:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2457s) that for that one pod we
had a sidecar enabled.

[41:01](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2461s) And you know, I think we can even show

[41:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2463s) that really quickly here, going here.

[41:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2469s) Okay, let's reset this
back to what it was before.

[41:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2476s) All right, here we go, so
looking at the catalog,

[41:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2478s) that little icon right there,

[41:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2480s) that tells us that it had a sidecar in it.

[41:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2483s) So okay, awesome.

[41:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2485s) We saw how, you know,
for certain workloads

[41:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2487s) that maybe don't work great
with that ztunnel proxy,

[41:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2491s) we can just stick a sidecar
on it and get going.

[41:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2494s) - Amazing, thank you. And this
is exactly what we look for.

[41:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2498s) And also I like that for
my teams, including you,

[41:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2503s) we can go from a no service mesh state

[41:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2507s) to a, let's say, secure
layer service mesh state

[41:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2510s) to a fully fledged one
without needing to adopt

[41:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2513s) the full Layer 7 capabilities right away.

[41:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2518s) So that's amazing as well.

[41:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2519s) And also I wanted to circle,
go back a little bit.

[42:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2522s) We talked a lot about ingresses before,

[42:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2527s) and actually, ingresses, well, are great,

[42:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2530s) but those are limited.

[42:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2533s) Ingresses are limited.

[42:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2534s) To do advanced network staff with ingress,

[42:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2537s) you need to do a lot of annotations,

[42:19](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2539s) customer resource definitions.

[42:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2541s) So, and actually the Kubernetes ecosystem

[42:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2546s) is not adding new features to ingresses.

[42:28](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2548s) So this will be the
same also going forward.

[42:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2553s) The evolution, though, of ingress,

[42:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2556s) that is the Kubernetes Gateway API

[42:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2558s) has all those capabilities,

[42:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2561s) and all the new features are added

[42:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2562s) to the Kubernetes Gateway API.

[42:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2565s) The Gateway API tries to solve

[42:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2569s) all of the challenges that
you had with ingresses

[42:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2572s) and takes all the lessons
learned from service meshes.

[42:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2576s) And funny enough, this
Gateway API is the one

[42:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2579s) that we are using for the
Layer 7, Istio Ambient.

[43:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2582s) So the ecosystem in general
is going for a rapid adoption

[43:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2587s) towards the Kubernetes Gateway API.

[43:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2590s) Finally we have one API
that everybody can use

[43:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2594s) so that we don't have,
when we want to move from,

[43:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2596s) for example, service mesh to the other

[43:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2598s) or an ingress specification to the other,

[43:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2601s) we needed to, like, for example,

[43:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2603s) for the ingress controllers,
many different annotations.

[43:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2607s) The migration to one ingress controller

[43:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2609s) to the other was very difficult.

[43:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2610s) Now with the Gateway API,
since we have the same spec,

[43:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2613s) this will be easier.

[43:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2615s) So other things that you
can do with the Gateway API,

[43:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2620s) first of all, you can
do all that you could do

[43:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2622s) with the ingress API obviously.

[43:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2624s) So you can handle ingress
traffic, but you can also handle,

[43:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2628s) and you can obviously do more,

[43:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2630s) all of that you could
do with the annotations,

[43:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2633s) now it's embedded within the API again.

[43:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2637s) Then you can do service-to-service
with the Gamma project.

[44:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2642s) And now in the last KubeCon,
we also have seen applications

[44:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2645s) of the Kubernetes Gateway
API for egress traffic.

[44:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2649s) So that's amazing because we have one API

[44:12](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2652s) to handle all these use cases and scenario

[44:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2656s) and to unify Kubernetes
networking, really.

[44:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2660s) Another thing that I, specific topic

[44:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2663s) that you can also tackle
with Kubernetes Gateway API

[44:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2666s) that I wanted to dive deeper

[44:28](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2668s) is actually blue-green
scenarios across clusters.

[44:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2673s) So for example, as I explained before,

[44:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2677s) my teams are spending a
lot of time in, you know,

[44:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2681s) doing cluster upgrades, for example,

[44:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2683s) and we are doing the
in-place upgrades right now,

[44:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2686s) but we wanted to explore
how it would look like

[44:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2689s) to do blue-greens, for example,
for better reliability.

[44:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2694s) We want to be able to roll back if needed.

[44:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2696s) We want to do canary
deployments to the new versions,

[44:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2699s) so all of these things, and
looking at the ecosystem,

[45:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2704s) we said, "Okay, we need
to do multicluster then.

[45:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2707s) Which are the options for us?"

[45:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2711s) We have adopted the Istio Ambient,

[45:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2714s) but multicluster is still not
supported for Istio Ambient.

[45:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2718s) And in general, thinking about

[45:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2720s) how you approach multicluster,

[45:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2722s) with Istio or a service mesh in general,

[45:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2727s) well, there are multiple considerations

[45:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2729s) that we need to do as architects.

[45:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2732s) For example, we need to think about

[45:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2735s) how we are gonna set up the control plane.

[45:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2739s) Are we gonna externalize the control plane

[45:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2741s) to manage the clusters?

[45:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2743s) Are we gonna set it up in
a high-availability mode?

[45:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2747s) Other things that we need to consider

[45:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2748s) is to then we need to share

[45:50](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2750s) API permissions across the clusters.

[45:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2753s) Then there is encryption
and tenancy boundaries.

[45:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2757s) Then again, we also need to take care

[46:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2760s) of trust between meshes.

[46:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2762s) So if it was difficult
before to, you know,

[46:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2766s) start with service meshes,
adding multiple clusters

[46:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2769s) to the mesh adds a very big
layer of complexity to it.

[46:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2774s) So I told you that this can be also done

[46:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2780s) with a Kubernetes Gateway API.

[46:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2781s) So different approach is using
the Kubernetes Gateway API,

[46:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2785s) and you do that coupling
it with another set

[46:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2789s) of APIs to APIs in general

[46:32](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2792s) that are the multicluster services API,

[46:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2794s) ServiceInput and ServiceExport
that enable you to do that,

[46:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2799s) let's say, multicluster that
we need but in an easier way,

[46:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2804s) with a Kubernetes native way.

[46:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2808s) And within AWS, we do implement
the Kubernetes Gateway API

[46:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2813s) and the multicluster services API

[46:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2817s) with Amazon VPC Lattice as infrastructure.

[47:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2820s) So like, for example, we
have seen before the ingress,

[47:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2823s) with the ingress controller
that implemented load balancers,

[47:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2827s) now we see the Kubernetes
Gateway API with its controller

[47:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2831s) that implements Amazon
VPC Lattice resources.

[47:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2834s) And real quick, what
Amazon VPC Lattice is,

[47:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2838s) so first of all, Amazon VPC
Lattice is a network service

[47:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2844s) just like Transit Gateway,
just like VPC Peering,

[47:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2849s) but it operates at a different layer,

[47:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2853s) the Layer 7 of the OSI model,

[47:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2855s) unlike Transit Gateway,
unlike VPC Peering.

[47:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2859s) And it enabled us to connect
applications across VPCs

[47:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2865s) and accounts without the
need of those services

[47:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2869s) just by using Amazon VPC Lattice.

[47:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2873s) It also implements an AWS
native approach to security.

[47:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2878s) And another nice thing is
that not only can we have

[48:05](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2885s) traffic across multiple clusters

[48:08](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2888s) using the Kubernetes Gateway API

[48:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2890s) and Amazon VPC Lattice, but
also with Amazon VPC Lattice,

[48:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2893s) you could have a single URL

[48:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2896s) that sends some part of
the traffic to, let's say,

[48:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2898s) a service within Amazon EC2

[48:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2900s) and a service that is
either in Kubernetes,

[48:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2904s) or for example, ECS or Lambda.

[48:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2907s) And this is very compelling to us

[48:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2909s) because we also have some,
well, legacy workloads

[48:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2914s) still running on institute that
we would like to modernize.

[48:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2917s) And there is effectively many challenges,

[48:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2920s) but network is one of them.

[48:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2922s) So these simplifies for that a lot for us.

[48:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2925s) - Yeah, absolutely, we're really excited

[48:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2927s) about the Gateway API.

[48:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2928s) It's really this thing
that the whole community

[48:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2931s) and cloud providers are
kind of centering around.

[48:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2934s) Of course, the Gateway
API is an open source

[48:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2936s) upstream Kubernetes thing, right,

[48:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2938s) like the evolution of ingress.

[49:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2940s) And so cloud providers,
especially like AWS,

[49:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2943s) are creating controllers like
the Gateway API controller

[49:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2947s) that Federica covered on the past slide

[49:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2949s) to be able to implement some
of those resources in AWS,

[49:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2953s) and VPC Lattice really hooks
into that really nicely

[49:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2957s) with that Gateway API controller.

[49:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2958s) So instead of creating ingresses

[49:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2961s) and kind of ingress APIs and services,

[49:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2963s) it's kind of a new approach
with gateways and HTTP routes.

[49:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2967s) And I think we're really
gonna see the community

[49:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2969s) and customers kind of
move to this new approach

[49:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2971s) because of the number of
advantages that it offers,

[49:33](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2973s) that one that I'll say
is, you know, being able

[49:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2975s) to route to targets
outside of the cluster,

[49:38](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2978s) whether it's another cluster

[49:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2979s) or maybe Lambda, maybe
ECS, whatever you have,

[49:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2983s) and in addition kind of
all of the capabilities

[49:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2986s) that Federica had covered here

[49:47](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2987s) that become available as well.

[49:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2989s) So today I wanna quickly summarize

[49:52](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2992s) what we talked about, right?

[49:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2993s) So we started with simplifying
cluster operations.

[49:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=2997s) We talked about our choice with Amazon EKS

[50:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3000s) to run our container-based applications.

[50:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3002s) We talked about how it uses VPC CNI

[50:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3004s) for pod-to-pod networking
kind of integrated

[50:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3006s) into the platform, and
especially with Auto Mode.

[50:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3010s) You know, even for a lot of
the demos that I showed today,

[50:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3013s) that would've been streamlined

[50:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3014s) because I would no longer have to manage

[50:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3015s) some of those components like
the Load Balancer Controller,

[50:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3018s) VPC CNI, CoreDNS, they're managed for me.

[50:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3021s) And when we upgrade clusters,

[50:23](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3023s) those are also upgraded for us.

[50:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3025s) And of course that means,
you know, with Auto Mode,

[50:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3027s) there's other components
that are managed as well,

[50:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3029s) things like Karpenter.

[50:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3030s) You don't have to worry about
dedicated compute to run that,

[50:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3034s) those resources either, no
dedicated node for Karpenter,

[50:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3036s) no dedicated nodes for
your networking components.

[50:40](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3040s) Kind of moving on here,
we talked a little bit

[50:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3043s) about exposing applications
externally, right,

[50:46](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3046s) using the Load Balancer Controller.

[50:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3048s) We talked about creating ALBs,
application load balancers,

[50:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3051s) at the Layer 7 using the
Load Balancer Controller.

[50:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3055s) And at the Layer 4 level,
we talked about creating

[50:57](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3057s) individual NLBs by creating
services of type load balancer.

[51:03](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3063s) Kind of further moving down here,

[51:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3066s) we talked a bit about
using Istio Ambient Mesh,

[51:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3069s) enabling us to have Layer 4

[51:11](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3071s) and Layer 7 authorization policies,

[51:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3073s) Layer 7 advanced routing,
mutual TLS out of the box

[51:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3077s) without disrupting applications

[51:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3080s) and as well as that interoperability

[51:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3082s) with using sidecars when you need them

[51:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3084s) for specific workloads.

[51:26](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3086s) And lastly, we kind of talked
a bit about VPC Lattice

[51:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3091s) and the new Gateway API,
the Kubernetes Gateway API,

[51:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3094s) how it's enabling customers to move

[51:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3097s) and evolve to this new
version of networking

[51:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3099s) and how VPC Lattice being a VPC capability

[51:43](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3103s) in Amazon helps support that.

[51:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3105s) Okay, a lot of you might be wondering

[51:48](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3108s) how can you continue to
learn these things at home?

[51:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3111s) Well, by the way, that first demo I did,

[51:53](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3113s) that ingress demo that I did,

[51:55](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3115s) was actually based on EKS Workshop.

[51:58](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3118s) So that same environment that I showed you

[52:00](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3120s) with VS Code in the cloud,

[52:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3122s) you can spin that up for yourself.

[52:04](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3124s) So I highly recommend
going through EKS Workshop

[52:07](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3127s) to learn at your own pace.

[52:09](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3129s) In fact, I can very
quickly just show one thing

[52:13](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3133s) for you on eksworkshop.com.

[52:16](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3136s) Some of the things that you'll notice here

[52:18](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3138s) in the Fundamentals section,

[52:20](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3140s) if we go to Exposing applications,

[52:22](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3142s) the same thing that we
showed with ingress,

[52:25](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3145s) you can actually set up an
environment for yourself

[52:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3147s) and go through it yourself.

[52:29](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3149s) We talk about things like the
multiple ingress patterns,

[52:31](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3151s) so what happens when you create
multiple ingress resources

[52:34](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3154s) but you want them fronted by a single ALB.

[52:37](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3157s) We also talk about IP
mode versus instance mode

[52:41](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3161s) for load balancers as well.

[52:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3162s) So EKS Workshop, a great way, self-paced,

[52:45](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3165s) to kind of learn everything about EKS.

[52:49](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3169s) And I really, truly believe that,

[52:51](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3171s) because there's quite
a bit of content here,

[52:54](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3174s) and we're constantly updating it.

[52:56](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3176s) One thing I'll say is that
if you don't wanna spin it up

[52:59](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3179s) in your own account,
you can also reach out

[53:02](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3182s) to your AWS account manager
to request an EKS Workshop.

[53:06](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3186s) And in that QR code, there's
gonna be a form as well

[53:08](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3188s) that you can fill out,
and we'll reach out to you

[53:10](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3190s) to help get you set up
with an EKS Workshop.

[53:14](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3194s) Also, EKS's Best Practices Guide,

[53:15](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3195s) now integrated into the AWS Docs,

[53:17](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3197s) a great place to learn about
best practices for networking.

[53:21](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3201s) I know Federica and her
team spent a lot of time

[53:24](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3204s) making a ton of updates to
the best practices guide

[53:27](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3207s) so that it's always kind of the latest

[53:30](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3210s) kind of optimized setup for
networking that we recommend.

[53:35](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3215s) And you can get a badge as well

[53:36](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3216s) if you kind of go through
one of our courses.

[53:39](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3219s) All right, that's all
we have for you today.

[53:42](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3222s) Thank you so much for
attending our session.

[53:44](https://www.youtube.com/watch?v=8fes5sP0rs0&t=3224s) - Thank you.
(audience applauding)

