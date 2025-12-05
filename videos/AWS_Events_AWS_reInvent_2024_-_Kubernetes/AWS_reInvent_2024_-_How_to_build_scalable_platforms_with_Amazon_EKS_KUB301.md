# AWS re:Invent 2024 - How to build scalable platforms with Amazon EKS (KUB301)

[Video Link](https://www.youtube.com/watch?v=WkPrmHKZsq4)

## Description

A wide range of companies, from the most innovative startups to the world’s leading enterprises, are running their internal platforms on Amazon EKS, helping them to accelerate developer velocity and increase the pace of innovation. In this session, learn about best practices that AWS has developed over years of helping thousands of customers build and scale their internal platforms on Amazon EKS.

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

- I'm Nirmal Mehta. I'm a principal specialist
solution architect, and you're in KUB301 session: How to build scalable
platforms with Amazon EKS. If you're not in the right session, don't know what EKS is,
you'll learn it here. Stick around, you'll learn some things. Like I mentioned, I'm Nirmal. I'm gonna be joined today
with Isaac and John. They'll introduce themselves when they come up a little bit later, and we're here to talk to you about this lovely picture. That's it. This is the only slide
in our presentation. So who here... I can barely see, so... Oh, I'm gonna do this. Who here is a platform engineer? Awesome. Who here is building a platform currently? Why do we need platforms? (audience member faintly speaking) That's right. So, controlling governance, adapting to new things. Who thinks their platform
looks like this picture? A nice field of dreams. We talk to a lot of customers that are building
platforms like yourselves, and one thing that is a reoccurring theme is they get abandoned. They're not adopted. Who here has that problem right now? You've built this awesome, nice platform and the developers are a little
bit hesitant to adopt it. That's what this talk is about today. We're gonna give you guidance around how to think about the platforms
you're building on EKS and the best practices
on how to keep it going so that they're not abandoned. But before we get to that,
why do we need platforms? We need platforms because
we need to respond to the ever changing
technology needs and demands. You know, we've gone through
massive technology shifts, internet, smart phones,
the scale, you know, the number of objects, the storage, the number of applications,
the number of nodes even, number of servers. We need platforms to be able to adapt to those technology shifts and what our developers need
to run their applications. You're probably going through
something like that right now. Who's had to have a
meeting with an ML team and like all of a sudden, you gotta integrate machine learning into your application or your platform and support those workloads, right? So as the internet grew, we started to need to have automation. So we went from supporting websites with maybe tens of machines
and we could handcraft. We adopted things like Chef
and Puppet to start automating and having some governance
over those servers. But we never got all the
way with that automation. And now with these massive applications, we started breaking
them into microservices, started using containerization, and that started to solve
some of this control loop, this governance and automation but it came with some additional issues such as an increase in
complexity, dependencies, and just needing something
to manage that complexity. So that's why we started
building these platforms. And we said to ourselves, "If you build it, they will come. The developers will come." Who knows of the "Field of Dreams" movie? All right. So in that movie, a farmer gets visited by a ghost of a baseball
player in the past and is told if he builds
this baseball stadium in his field, all these legendary
baseball players will come. And I think, I was a platform engineer
before I came over to AWS, and I had that same attitude. Oh, my platform's awesome. It has the best features, it's got the coolest stuff, uses docker and containers. Isn't that cool? And I sat there and I had to, and I thought all these developers, there's no way they wouldn't want to come and use my shiny Kubernetes platform. And I sat there and I sat there and then I
realized, no one's showing up. No one's showing up to my field of dreams. So why do we keep doing this? We focus, we think it's just about
the features of the platform and the platforms are abandoned because they don't have
the right features. But it's not that. It must be something else. When we're talking to customers and we start digging into why
those platforms don't succeed, we realize that what really
attracts development teams and your users to a platform is trust. Platforms are abandoned when
they fail to establish trust. Distrust of the platform to
evolve to the meeting needs that leads to shadow IT, distrust in delivering the
services and capabilities that the developer needs, and distrust that the
system will break frequently and in non-known ways. We know it's trust because we know developers will still choose a previous platform that they have a prediction and know the bottlenecks
and know the edges. And they continue to use
those older platforms. So we know that it's trust because they trust that. They're used to it, even if it's ganky, for
lack of a better term. So, what is trust? Trust is three parts. Logic. If you believe that I
have rigor in my logic, then you're more likely
to trust me, right? And hopefully, you will
demonstrate some logic today in this presentation. If you sense that I'm authentic, then I'm more likely to be trusted. And if you sense that I
care about your needs, then you're more likely to trust me. So how does this translate
into a platform perspective? Authenticity, or, yeah, authenticity translates into a collaborative
shared responsibility, showing we collectively
care about the outcomes. You know, you build
you own product mindset for the platform. Logic turns into transparency. Say what you're gonna do and
do what you're gonna say. Commitment to transparency
and collaboration. And then empathy turns into reliability. I care about supporting your services and making sure they run well. And I'm here for your needs, your developer needs. So I want to have you keep that in the back of your mind as Isaac and John do the
rest of the presentation around these three concepts of trust in how to build a scalable platform. Where we see a lot of
friction is how do we keep that trust level high, but
also meet the demands of scale? There's a tension there. We can move fast, scale out, but maybe we reduce reliability or not meet the needs immediately. That erodes the trust. So the challenge in building
these scalable platforms is figuring out a way to meet the scale of the ever evolving technology demands and also keep the trust level high. So I wanna just take a step back. We were talking, preparing
for this presentation and John told me, "Look, at the end of the day, all my developers care
about is getting their code into production as fast as possible." We can talk about all these other things. An example in the past is, you know, you might have a monolithic pipeline and the development team is used to that. So they, you know, they're used to doing that
three to four month deployment in this monolithic app. Now they've broken it
down into microservices, but they don't trust the new platform to be able to handle
deploying these microservices. They don't know the friction or it's a higher friction. So they tend to cram all
those new microservices and the new things they're trying to do into existing pipelines,
that monolithic pipeline, because they know what
the bottlenecks are, what the pain points are and they know what the friction is and they know that that might be the way to get to code in production
as fast as possible in their mind. So I want you to keep that
in the back of your head when we're going through
the rest of these details of how to build these platforms
in the best practices, how to keep that trust level high while also meeting that scale. So Isaac, can you come up and
tell me how we can do that? - Absolutely. Thank you, Nirmal. So let's dive into what we always do when we think about platform
engineering and our plans. We always turn to automation. Almost every single year
for as long as I remember, I've been doing platforms
for a very, very long time. We're gonna automate things, we're gonna automate more things. And this year, what are we gonna do? We're gonna automate again. And next year, I guarantee
on your product roadmap for your platform, more automation. We started off with Puppet, moved to Chef, moved to Ansible, now to Terraform. We are constantly automating. But why isn't that we actually get to this point of automation? And if you think about
like other industries, when was the last time any of
you have ever been in a bank? I've not been in a bank. I can't even remember the
last time I was in a bank. They've automated. It started in the eighties with an ATM, an automated teller machine. It's in the name. So other industries have figured this out, but somehow we, as platform engineers and software developers, still haven't figured it out. Why is it that we're still
automating every year, year after year after year? And I guarantee you,
we're not gonna get it if we continue doing the
exact same things over and over again. So let's dive into this. Now, one of the things that
Nirmal talked about is scale. What changes in our world more
than anywhere else is scale. The number of developers,
the number of services. For those who have been
with AWS for a long time, we started off with EC2 and S3. We now have over 250 different services. We launched a whole bunch of
new services here at re:Invent. Every single year, our scale grows dramatically and we have to adapt to those changes. So as we grow and we scale, what do we do? We break down things into smaller chunks. And I don't mean just microservices, we think about humans, organizations. So we break down our large platform teams into smaller teams. We might have a networking team and they'll have their own set of pipeline and abstractions you see
here, authentication. All of that gets put
into in a stored state. And they deal with networking, right? We also have an infrastructure team. They're gonna be focused on
standing up EC2 instances, maybe your Kubernetes clusters, right? All of that other baseline
foundational infrastructure that you need to actually
run your application. We also will have an observability team. They're gonna be focused on, obviously, bringing up
observability for your applications for the infrastructure,
for the networking. And then they have their own pipeline. Compliance will also have
their own pipeline as well. They'll have their set
of authentication tools and if we're lucky, they'll be using a lot
of the similar tools. But unfortunately, what ends up happening is
everybody sets up their own sets of tools, right? And then finally, finally we can get to
deploying our application. This is the... When we refer to the platform, when most people think about
is just this one pipeline, the CI/CD pipeline that we all talk about. That's when we talk about platforms, that's what most people think about. And they don't think about anything left of that dash line, right? But that isn't all. You don't deploy an application
without any dependencies. You now have to get things
like databases, right? You need to get S3 buckets, ElastiCache. You have a lot of dependencies that your application needs to depend on. Well, that's a whole nother pipeline. But to make things matter, to make things more complex, there's actually one pipeline that actually nobody really
talks about but exists. It is a continuous compliance pipeline that runs behind the scenes and makes sure that everything is
continuously in compliance. Now up until this point, everybody here has been storing
all of their configuration, everything inside of Git, and then they deploy the pipeline and everything seems to work. That moment that you push
that deployment pipeline, you push the button and it works. But how do we come up with drift? Well, drift happens because of things like the
continuous compliance pipeline that runs in the background. It's secret. The developers don't
know anything about that. So what they think is,
"I've put something in Git, but then there's
something else changing it in the background." It'd also be a human being
actually making changes in the background. So this thing that we've talked about, Git as a source of truth
is actually not the source of truth. We had one developer, one customer tell us, "Git is not the source of truth; it is the source of hope," because of so much drift
between our pipelines and what we expect our intended outcome and then the actual outcome, right? And immediately, we start to break trust. All this trust that we build, we go look, put stuff in Git. You'll trust that what you put in Git, will match what's in production. That doesn't actually happen. So immediately, we start to
break trust with developers. And that's a really important
thing as Nirmal touched on to being able to gain
adoption of your system. So let's go back to this. So let's get back to this diagram and what's complicating things? Why can we not actually automate between all of these pipelines? And the answer is human interaction. Now again, we're gonna
launch a lot of new services, a lot of new features that your developers or you, as a platform
engineers, are gonna want to integrate into your platform. So what is it gonna take? Well, let's simplify this a little bit. Let's just assume we need a new resource. Well, in order to get that resource into your application or
be able to provision it, it needs to interact with
the infrastructure layer. Well, the infrastructure
layer needs to go back to the developers. And now we're setting up
meetings, adding Jira tickets, and we're constantly in meetings, just communicating our requirements. Here's what we need,
here's what we needed. Justification, setting up calendars. This thing, this little feature that
you might need now turned into weeks of meetings. Well, we also need to
run it by compliance. We're not gonna just ship
something into production. There we go. More, more meetings. App developers are now
talking to compliance. Now the network team, you need
to have access to it somehow. Network team's involved. More meetings, more
meetings, more meetings, and more meetings. So the example I gave about
an ATM machine, right? There's no humans involved. And so what slows us down and what makes it impossible
for us to automate is pipelines that we're running in the
interaction between us, the way that we communicate
with each other, is actually just through meetings. We're never gonna automate that, in this way. It's only just gonna lead
to more and more meetings, more and more Jira tickets, and more and more waiting and delays. We know that some customers, when we launch new features here at AWS, it takes some over a year
to actually adopt them due to all of these
meetings and Jira tickets and waiting for people to do the work. And so what we know is that anything, any improvements outside of the bottleneck are just an illusion. So all these other little things that we're automating around, hey, we're gonna automate
this little piece, is not actually getting to the core of what actually needs to
be automated in order for us to be productive as platform engineers. It doesn't build trust because we're constantly just in meetings, talking to each other,
justifying our needs. So this is the core of
platform engineering. Why is this a new thing? Why wasn't this here before? We're finally at the breaking point, finally at the breaking
point of these pipelines. We're finally at the breaking
point of all these meetings because we reach a large scale. So how do we get around this? Well, we can just borrow what
the banking industry has done, is just use APIs. The answer is actually rather simple. Getting there is a lot harder. So how do we think about using APIs? Well, instead of thinking about pipelines, things like networking
or blue-green deployments or you know, getting a
pipeline to get an RDS database or an S3 bucket, we think of these things in terms of capability and what your capabilities and what your platform
instead should be doing is exposing this
capability through an API. Right? APIs are declarative, right? And can be controlled by the
software behind it, right? When you think about a pipeline, you hit that pipeline button, that's it. It runs once. And hopefully, it doesn't break, but then you start to
lose control that way. So we gain control by
moving things behind an API and then we can actually
start automating things. And the way that teams communicate with each other is no
longer through meetings. It's through APIs, which
is a well-established form. So how do we, as platform
engineers, get there, right? So in this diagram here, we've moved all of those disparate APIs, authentication abstraction
into a single layer, right? One facade that encapsulates or abstracts out all of
those complex moving parts behind the scenes so that
your developers can ship fast and ship things into
production as fast as possible. All right. So let's go back into our diagram. We still have the same teams. Those teams didn't go anywhere. But we're now thinking in
terms of software development. We're thinking in terms of APIs and we're building into this platform. And now we've moved more into
a product mindset, right? So the requests that used to come in and require all of these meetings, we're now prioritizing
through a product manager. And this product manager is making sure that we're getting to the
features that we need to as quickly as possible, or the most important features. But there's one challenge
with this, right? So we've solved some of the problems here in terms of removing
some of the bottlenecks of communication between teams, but we still have a bottleneck. And this bottleneck is you
will always have more requests, feature requests from your developers than what your product or your platform engineering
team can ever handle. And so what are they gonna do when you can't get to all
of those feature requests? Are they gonna sit
around and and just wait? No, they're gonna work around you. And many of us know this as Shadow Ops or you know, these rogue teams
that go build this platform or go end up using a different service without you knowing, work around you because they
can't actually use the platform and based on their needs. But this isn't what we want. We don't want them working
around this, right? This is another form of
us breaking trust, right? This is developers not
breaking trust with us as platform engineers, right? Eroding trust. It constantly happens. It's all little by little
breaking this trust. What we really want them
to do is we want them to extend our platform, right? But we can't get them
to extend our platform if everything that we do is proprietary and we're writing our own code and building our own documentation, which sometimes we don't
even get to, right? So how do we cultivate this
kind of culture, right? This is exactly what
Nirmal was talking about, collaboration. How do we collaborate with each other? Right, and for those
who have read the book, "Team Topologies," this is one of the major
concepts in the book is, we as platform engineers
and where we are today, we started off in facilitation. The idea of SRE and DevOps was, hey, I will embed a human
being into your team and they will help you actually
launch your application. And now for the most part,
most people are starting to move into this acts as a service, database as a service, platform as a service, Kubernetes as a service, right? All of these containers
as a service, right? And that'll get you to the
next level of scalability. But where we need to
move to is collaboration. So what can we look to to help us collaborate? What other forms in the world, just like in the banking
example, we used APIs. What other form of
software can we leverage to actually help us collaborate? So for many here, I'm sure you all use open
source software, right? Those communities in open source have exhibited
transparency, collaboration. They earn trust. That's how they get to be so big. There's a huge community. So if we inherit an open
source framework, right, for our platform, we get to bring along all of that with us: transparency, collaboration, the trust. So what if we use Kubernetes
as this framework? Now up until this point, I assume many of you have used Kubernetes to deploy containers. And think of it as a container
orchestration system. From this point on, I'm not gonna talk about
orchestrating containers. I'm gonna talk about
strictly as a platform. Even if you never use Kubernetes
to deploy a container ever, you can still use it as
your platform layer, right? And why would we want to do that? That seems kind of crazy. But why would we wanna do that? Because it has every foundational aspect of what a platform needs and has an API handler and has RBAC built in, has a mutating admission controller that helps us actually
control what gets in and out and able to make changes on
the way into the platform, which is important. As we keep going, we can build in web hook
controllers, schema validation, have other controllers here that actually integrate with Kubernetes so that we can add our own business logic and our own compliance. But most importantly
here is we have one place to store state. If you go back to those pipelines, every single one of those
pipelines stored state in their own different way. And if you're using Terraform, every time you run a pipeline, it creates a new state file, right? That's a different state
stored somewhere else. And there's no way to really query it. If I wanna understand what is
the state of my application, I have to go to four or five
different state stores, right? And that makes it really
hard to build trust with a developer when they can't actually see
what's happened in the past. So ETCD serves as our single state store. And instead of capabilities, Kubernetes calls them controllers, right? But in the end of the
day, every single time that you add a controller or a CRD into your Kubernetes cluster, what are you effectively doing? You're adding a new
capability to that platform. So if you're using a secrets controller or an API controller, that
is actually what's happened. You're enabling some new
behavior or new feature. So how do we extend this further? Okay, you're already doing it. For those who are
already using Kubernetes, you in fact are already doing this, right? So this isn't necessarily something new, it's just thinking about
it in a different way. The other reason why we want to use something like
Kubernetes is the notion of abstractions. Abstractions help hide away complexity. When we think about an API, in fact, that is what's happening, right? We are hiding away that
complexity behind an API. Again, going back to that
banking example and APIs, it's not like the bank is asking you if you want to take money from one account and put it into another. They're not asking you
to tell them the process of how to do that. They just go, "Hey, what do you need?" And the API will handle it. So how do we do this here in Kubernetes? Everybody's very familiar with
the deployments abstraction. The deployment abstraction
is actually an abstraction over a replica set, which
is an abstraction over pods, which is an abstraction over containers. Now, the beauty of Kubernetes is that if you need a new set of functionality, let's say blue-green, would you throw all of this away? Now, you wouldn't throw this away. Instead you would add blue-green and leverage all of the
abstractions underneath. And so what we call this in software development world
is composability, right? We're able to actually
compose a whole bunch of different pieces of functionality and bring it into one, right? And for those who use Argo, there's ability to have blue-green and that's actually all they do. They take replica sets, pods, containers, and build their own blue-green
abstraction over top of it. All right, so let's extend
this a little bit further. All right, because remember, developers don't care
about any of this stuff. They care about their application, they care about their application
getting into production as quickly as possible, right? So let's build more abstractions. So within Kubernetes, we can build a new abstraction
called an application, right? That's what they care about. Now, the term application
can mean something for me in my organization, which will be different than for you all in your organization. So this is just an example. So an application might need an ingress, you might need an S3 bucket and S3 bucket, of
course, needs IM policies and we're building these
other abstractions as well and connecting the dots. We have ticketing, usually we use Jira tickets
or ServiceNow tickets to enforce compliance. So our compliance abstraction is there. But that's not all. We need an environment to deploy to. Are we deploying to dev stage? And that environment needs
an account, a VPC, a subnet. You might need a Kubernetes cluster. And all of these abstractions
can live inside of Kubernetes. So if we tie this all
together, what do we have? We have an application that
points to an environment that also points to a
ticketing system to help us with compliance and track changes. We have that application
that has ingress, buckets, also its own ticketing system to make sure that we're
enforcing compliance. And this is what a developer
really cares about. It's just this application,
this little box, not really so much
everything underneath it. And so if we recall the pipelines that we had at the very early on, all that communication, all those meetings starts to go away when we start thinking about
Kubernetes as a platform and start thinking about composability. We're able to just combine
different components without having to jump
into these meetings. We've moved away from pipelines and that's what Kubernetes
helps us to do, right? It simplifies this. Developers care about
applications not infrastructure. And there's also one other thing here too. You remember that continuous
compliance pipeline, that secret pipeline
that runs in the back? You notice that we don't
have this for Kubernetes? And the reason we don't
have this for Kubernetes is because we have this
continuous control loop. That control loop in that continuous compliant is built into the very foundational
fabric of Kubernetes, right? So the more we leverage Kubernetes
for our platforms, right, the more trust we have because everything is there,
the more transparency we have. In fact, actually, when you
query something in Kubernetes, you have, here's my intended state, here's my actual state,
all in one API call. And every single API
call, it returns your spec and then the actual status, right? The other reason why we
wanna leverage Kubernetes is it has a large
controller ecosystem, right? You're not doing this on your own. You're leveraging that community that already has a lot of trust, that already has a lot of transparency. There's a number of
open source controllers that you can use to add functionality. I talked about Argo. You don't need to build your
own blue-green functionality in automation, use Argo and bring that in and now you have additional
deployment semantics within inside of your platform. We also just recently launched K-R-O, kro, that helps you build these abstractions on top of ACK, right? Which also represents objects in AWS in a Kubernetes friendly way, right? So there's a huge controller
ecosystem out there that allows you to develop without or to develop these abstractions
without you having to code. But of course, at some point,
you may hit a limitation of what's available and
you will need to code or you create your own custom controllers and you can do that as well. And now you can start mixing
and matching and composing. All right. But most importantly, what does this enable
for your organization? It enables our teams and our human beings to collaborate differently. Again, we're moving away
from the notion of pipelines and interacting through
words and Jira tickets, to now putting everything into code and taking each other's components and building something new. So you'll notice on the left hand side, we have app team architects, on the left hand side of this API, where we have database
architects, security compliance, all writing all of their requirements, again, not into tickets but into a declarative language, right? And Kubernetes allows us to do this. Now the great thing about
Kubernetes allowing us to do this, right? It's great. You don't have to actually have very many
worker nodes for this, but you do need a scalable control plane because we are now
putting a lot of pressure on the control plane as a platform, not just as a component, not just as a container
orchestration system. And this is where EKS comes in. We have worked over the last seven years to make EKS the most scalable, managed Kubernetes control
plane on the planet. So if you just use EKS, you're delegating all of that to AWS and now you can just focus
on building your platform without actually having to
create a bunch of worker nodes and manage yet another set of APIs in containers somewhere else. We'll do that for you. The other great thing is, of
course, we already mentioned, you're not on your own, right? We're inviting people to
the other side of the table behind the curtain. You now get to bring your app developers and your other teams to the left side, but also the community. And lastly, you can now, because you're moving away if you're doing platform engineering and moving away from proprietary code that you're writing on your own or your proprietary platform, you can now have us help you. We have blueprints, we have CNOE, which is our a opinionated
platform community out there, all putting out a bunch of configuration, a bunch of open source tools to help you build your platform with us. We have specialists that can come in and help you build your tool because if you're building
it with open source, well, we know how that works. We can see it. That's what the transparency is there. So you're not on your own anymore when you're thinking about platform. You're not, you're collaborating, you're thinking beyond the
walls of platform engineering, and this is what's gonna help you scale. This is the foundation of
building that trust, right? We're gonna get... We have to get to the point
that we're bringing developers and other people behind the curtain of this platform engineering team. Alright, so let's walk through
what this would look like in practice. So we go back to Git, here in number one, developers are actually pushing
Git configuration into Git. Two, we have Argo, or a controller monitoring Git to make sure that we have those changes. Argo or any CI/CD system
that you have in there, we'll then push it to the API server. At this point, by the way, we actually haven't applied
anything into Kubernetes. There's no changes being made. We have to go first through
the admission controller and make sure that these
changes are valid changes, they're good changes,
they're compliant changes. That gets pushed into ETCD,
our single state store. This is for, again, for S3 buckets. RDS, this could be for
your applications, right? All of those abstractions we talked about now have their representation in that CD. That gets put into a tenant name space. We have controllers sitting
there and listening, reconciling, noticing those changes, going out, reaching out to any API. Now, of course, I talked
a lot about the AWS API, but you can use this to
manage other resources, other observability resources. Anything that has an API, we now are communicating with
it and making those changes. Number seven here is
getting the status back from those changes. So now we have our intent and
our status in the same place and we're updating that in that CD. And as we go back down to eight, we have our presentation layer, a single presentation layer that represents our
networking, our observability, our applications, our history. Everything a developer
needs to get their job done and get their application into production, they can see it in a
single presentation layer. And in this example, I'm using Backstage, you could build your own one, you can use another open
source tool or use a vendor. But it makes it super simple
now that we have everything behind a single API that
happens to be Kubernetes but at its core, it's an API. Getting back to that automation. So some of the key takeaways. Build your community and collaborate. Do not think of yourself
as just this platform team that is a finite set of resources. Think about open source, think about AWS, we're here to help, right? Build a bigger community. Another one is have a product mindset. You still need to make sure that you're being empathetic
to your developers, you're listening to them, and you're building
exactly what they need. Abstract away complexity with APIs. This is key, right? When we think about pipelines, what we're really doing is
exposing that complexity, all of those steps
directly to the developer, which is not very helpful. And lastly, leverage open
source for transparency and reduce your undifferentiated
lifting by leveraging EKS to manage that control plate for you. Now up until this point, Nirmal has been talking about high level. I've been talking a
little bit lower level, but it's still rather abstract. Next, I'd like to invite
John Weber from Adobe to talk about how to make
this an actual reality. He's done this in real life. So, come on stage here, John. Take on over. - Thank you sir. - Thank you. (audience claps) - Welcome to KUB301, how to stop meetings. Thanks so much, Isaac. I'm really excited to share Adobe's story
with you here today. I don't know how things
work at your company, but at at Adobe, it could be really hard to get a service out the door. It takes on order a
month for a new developer to get up and running with
a new Greenfield service. Not only do they need to write the code, but they probably have
to create some tickets to get access to observability
systems or production and wait for humans to go ahead and respond to those tickets. And meanwhile, they actually
have to write the code, they have to deploy the code, they have to test integrations. And then the humans,
where the tickets went to, come back and say, "I have no idea what
you're asking me for." And between bartering of
what the developer needs, you have to think about
production readiness. All the monitoring tools,
are they all set up? Do you have alerts? What is your backup strategy? And are you ready with
your incident response when something goes wrong? Because it will. I'm part of the developer platforms group and our motto is very simple: help developers write
better software faster. How do you make this landscape do that so developers can actually
achieve that outcome? I'm a fan of abstraction and platforms where you need to simplify and in many cases, oversimplify
for your developers. I'm also a fan of our
cloud providers like AWS, who could manage all this
stuff better than I ever could. Where do all of these
principles intersect? I want to turn your attention to the bottom box labeled, Ethos. At some point in my career, I've probably run every
customer-facing product that Adobe has to offer. And one of my core challenges
was around consistency. As I like to say, Adobe is
inconsistently inconsistent. We would've some technical
alignment around strategy, hey, we should use a public
cloud provider like AWS. But then each engineering
team would go off and make their implementation unique. When every team is able to do that, how do you prevent sprawl? And worst of all, a terrible
customer experience, which is the last thing
that any of us want. So at Adobe, we decided to create Ethos and we needed to make a few big bets. Some of them we got right, containers and docker. Some of them we got wrong, Mesos. And so we also needed to give some level of flexibility to our customers. Some of them wanted
just a turnkey solution where they didn't care about any of the underlying infrastructure and that was CaaS or
container as a service. We also realized that Kubernetes was where
the industry was headed and some teams wanted
to consume native APIs and choose their own
adventure, as I like to say. And that was our platform as
a service offering or PaaS. So building on a scalable
technology foundation like Kubernetes enable
us to have future pivots, say towards GitOps powered by Argo. Like Nirmal said, I believe developers literally
care about one thing: "How do I get my code to
production as quickly as possible? So what are my users interested in and what am I interested in, given we're all part of
the big Adobe family? So Ethos exposes these capabilities, so developers don't have to
think about any of this stuff. They don't need to think about how would I run cloud
infrastructure at scale? They don't need to think
about how I build a CI/CD, a robust CI/CD pipeline. They certainly don't want
to think about security and compliance. And of course cost is always top of mind with finite resources like GPUs. And in cases where we
can provide insights, we also want to think how
can we absorb that pain from the developer and take action on their behalf. Folks, we are a product team. You may not be able to
go to Adobe's website and purchase Ethos or your
favorite e-commerce store, but if you are a customer or a user of Adobe's
products, you use Ethos. And because I'm a product team, I need to be very much
aligned with my stakeholders to build trust and respect with them. The first group is our internal customers, our developers. Yes, these folks are customers. One of my early career failures was, I refuse to call these
folks customers, right? They're colleagues, they're coworkers. I was completely wrong. If you don't consider your
developers your customers and don't build a level of respect and empathy with them, you will fail. You will fail. So what do your customers need? Clear documentation. A UX makes sense. Low barriers to entry, because they don't want to use
a system that's hard to use. External customers. Adobe is the dial tone and the fabric for everything that we provide. We're here to achieve and
enable high quality features and value for all of our end users. AWS. Is AWS able to satisfy the needs of Adobe? Conversely, am I giving the
right level of feedback to AWS so they can hide and abstract all the way to that ugly complexity
that I don't want to see? Adobe very much has a soft culture. We love to give a blank canvas
to our users and unlock them and say, "Hey, go build some
magic powered by Adobe." We also do that with our developers. And as you can see, when you hand a blank
canvas over your developers, things could go wrong. So what we had to do is we had to build a grassroots ground game to get them onboard and on site. We started with a platform
champions program. If you get boots on the ground
within each development team, if you have advocates and promoters for what you're trying to achieve, and most importantly, if
they have skin in the game, you're gonna build an incredibly strong and vibrant community. We also have embraced
an inner source model. You will never have enough resources to do all of the things the
business is asking you to do. So you need to not only
scale your technology, but you need to scale how you operate. We have a very well-defined
open contribution model to Ethos within Adobe. You need to listen to your customers. And we do this through CABs. We sit down with our users regularly and we listen to their pain points and they say, "Hey, you're making my job or my life so much easier." Or they're telling us, "Man, what did you just build for us?" Tough love is okay. Feedback is a gift. This is what we've been able to achieve. This year, we received
six times the number of contributions outside
of our organization. 25,000 contributions to Ethos are outside of the Ethos team. 25,000. We have about 1,500
contributors within Adobe as part of this journey. This is up from 230 last year. Imagine if you had 1,500 extra developers willingly contributing to your code base. It's really amazing. In order to be successful, you need to build a
culture of accountability. I believe engineers
acting as product owners, and I mean this in the agile sense, so no offense to my product
manager friends out there, but every engineering manager needs to be a customer advocate. They should understand and have a vision for what they're building
and how it should function. They should be having
continuous conversations with the people that
they're delivering value to. To quote the great Werner
Vogels, "You build, you run." Guess who gets to be on
call at 2:00 AM on a Tuesday when things break? Yep. The people who write the software. And when things go wrong, your developers need to understand and have empathy and share
some of the pain and burden that your customers are going through. Amazingly, people are highly motivated to fix systemic issues if they continue to get
woken up every night. Go figure. The developers, the people consuming
the amazing capabilities that we're building, need to understand the cloud is not free. This stuff costs real money. So we built granular
dashboards and cost attribution and then we send those teams a bill. And because I care about Adobe's money and they care about Adobe's money, we had to take a pivot and think about how we could
absorb some of that pain. And we did that through the automatic
resource configurator or ARC. Raise your hands. Who believes developers
get container sizing right the first time they deploy production? Anyone? No, okay. That's what I thought. ARC's a really simple system that we built with the
Adobe research team. When engineers request
capacity on an Ethos cluster, we deploy the pod along with
an open policy agent or OPA and we evaluate and give us hooks to be able
to change their pod spec. Now we deploy workload on a worker that has available capacity and then we record utilization
metrics through Prometheus and then we store those in a long-term time series
database like Cortex. Then ARC begins to look at the utilization and then recommends container sizing to the developer via an
automatic pull request. And once the dev accepts the
PR and says, "You know what? I may have gotten this wrong," GitOps will do its magic and take over once that gets merged and we go ahead and have
container sizing solved. Like any service provider, I need to have an enforceable
contract with my users. I need to set targets, measure them, and hold myself accountable
to the results and outcomes. I do this by embracing
service level indicators and service level objectives. By defining my core capabilities, can I deploy? Can I scale? Do I have network connectivity? And then I measure and
evaluate my performance on a continuous basis. I also fully embrace DKS. Folks, there's no glory running
Kubernetes on an EC2 node. Right? You have much better things to do. Everybody should be striving
towards declaring bankruptcy, infrastructure bankruptcy and
giving this all to Amazon. And when stuff goes wrong and it will, can your team write a high quality RCA? And not only that, would you be comfortable
publishing externally? You need to set that bar really high. Imagine being customer of service where you could, on demand,
check my homework in real time to make sure you're getting
what I promised you. We've been able to do that at Adobe. Here's a sample dashboard that's available to anyone in the company. And in this example,
we're assessing the health of the egress capability
for our Ethos cluster. Am I delivering on the
promise that I've made to ensure outgoing network connectivity for the Kubernetes clusters
that our team manages? I also care about my customer's
reliability and uptime. I know that getting observability,
working is really hard. Agents, collectors, metrics,
traces, logs, events, and so on and so forth. So we've rallied around open SLO. Folks, this stuff is solved in many cases. You don't need to make your lives harder and figure out how to build
this stuff on your own, like we initially thought we had to. So all of our applications on
Ethos are auto instrumented wherever possible. We do need to take a maybe
a few inputs from a user, like what their target should be. But then our tooling takes over and with the magic on open SLO, we're able to calculate
error budgets automatically for all of our applications on Ethos. So where are we investing and what are those returns
on that investment? The main KPI that I look at around operational scaling is
our cluster-to-operator ratio. And since we've pivoted to EKS and declared infrastructure bankruptcy, I'm happy to tell you that we've scaled our
operator-to-cluster ratio from 10 to one to 30 to one. We're also looking to retire
our homegrown solution and embrace GitOps and Argo. And this is way more flexible with newer use cases like generative AI. And lastly, we need to reduce friction. Having less places for
your developers to go means that they'll be happier
and they will work faster. We've done that by
moving all of our portals into one and embracing Backstage. So what are the outcomes of this work? What does this scoreboard show at the end of the fourth quarter? And are we winning? We are winning. Developers are able to deploy
a full greenfield stack in just a few days rather
than waiting an entire month. There are less meetings too, by the way. And included in that Greenfield stack is our observability platform, which I'm happy to say has
driven the time it's taken to detect an incident by over 75%. Cost will continue to be a major theme as we go forward into
the era of generative AI. And when you're dealing
with finite resources and expensive ones like GPUs, with Ethos, we were able to
nail our cost efficiency targets early this year. Finally, building Ethos in
our internal Adobe platform has made developers much happier because all they care about is, "How do I get to production
as quickly as possible?" And so if you have happy
developers, what does that mean? It means that they're more
productive developers, which means you're gonna
have happier customers. Thanks for listening. Let me hand it back to Nirmal. He'll take us home. - Thank you.
(audience claps) Alright, so you've learned, you've seen why building a
platform on EKS is important and helps you build a
trustable and scalable system to adapt to ever-changing needs, but you don't need to do it yourself. Check out CNOE. CNOE is our cloud native
operations excellence, open source, open community. It's... We talk to a lot of customers and customers like Adobe
got together and they said, instead of all of us trying to figure out, out of the CNCF landscape, which tool we want for observability, which one we want for deployments, let's just create an
opinionated architecture and then build the tools, an open source tool, to be able to deploy these
platforms with these opinions. So that's what CNOE is. Check it out. You can leverage it and
accelerate your platform today. So how do we build attractive platforms? Focus on trust, increase transparency,
collaboration, and empathy through reliability. Consider your platform as a product that's continuously evolving. Survey, interview your developers, interview the people that you think should
be using your platform and ask them why they're not coming to it. Abstract the complexity through the controllers
on EKS or Kubernetes and extend your community
beyond just your organization to include developers, other stakeholders, AWS, and the open source community. You're not alone. Thanks for coming to our session today. Here's some other sessions
that are going on in the track, the Kubernetes track, that are related. Some of them have already occurred and the videos will be on
YouTube if they're breakouts. Check out the CNOE workshop
on Thursday, tomorrow, if you want to get hands on
on building an IDP using CNOE. And there was some new
announcements with new features at KUB201. So you want to check out that talk on some of the new features
that we're launching in Kubernetes and where
we're going with EKS. Check out the EKS training. So if you're new to
Kubernetes, new to EKS, we have a free EKS badge and training. And for our session today,
please check out this QR code with all the links and resources to help you accelerate
your platform building. Happy platforming and I hope y'all had a good time. (Nirmal chuckles)
(audience claps)

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1s) - I'm Nirmal Mehta.

[00:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1s) I'm a principal specialist
solution architect,

[00:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3s) and you're in KUB301 session:

[00:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=6s) How to build scalable
platforms with Amazon EKS.

[00:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=10s) If you're not in the right session,

[00:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=12s) don't know what EKS is,
you'll learn it here.

[00:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=14s) Stick around, you'll learn some things.

[00:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=19s) Like I mentioned, I'm Nirmal.

[00:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=21s) I'm gonna be joined today
with Isaac and John.

[00:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=25s) They'll introduce themselves

[00:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=26s) when they come up a little bit later,

[00:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=28s) and we're here to talk to you

[00:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=30s) about this lovely picture.

[00:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=33s) That's it.

[00:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=34s) This is the only slide
in our presentation.

[00:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=37s) So who here...

[00:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=38s) I can barely see, so...

[00:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=40s) Oh, I'm gonna do this.

[00:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=41s) Who here is a platform engineer?

[00:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=45s) Awesome.

[00:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=46s) Who here is building a platform currently?

[00:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=51s) Why do we need platforms?

[00:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=56s) (audience member faintly speaking)

[01:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=69s) That's right.

[01:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=69s) So, controlling governance,

[01:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=72s) adapting to new things.

[01:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=75s) Who thinks their platform
looks like this picture?

[01:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=78s) A nice field of dreams.

[01:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=83s) We talk to a lot of customers

[01:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=84s) that are building
platforms like yourselves,

[01:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=87s) and one thing that is a reoccurring theme

[01:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=91s) is they get abandoned.

[01:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=95s) They're not adopted.

[01:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=97s) Who here has that problem right now?

[01:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=100s) You've built this awesome, nice platform

[01:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=103s) and the developers are a little
bit hesitant to adopt it.

[01:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=109s) That's what this talk is about today.

[01:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=112s) We're gonna give you guidance around how

[01:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=114s) to think about the platforms
you're building on EKS

[01:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=118s) and the best practices
on how to keep it going

[02:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=122s) so that they're not abandoned.

[02:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=125s) But before we get to that,
why do we need platforms?

[02:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=129s) We need platforms because
we need to respond

[02:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=132s) to the ever changing
technology needs and demands.

[02:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=138s) You know, we've gone through
massive technology shifts,

[02:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=142s) internet, smart phones,
the scale, you know,

[02:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=147s) the number of objects, the storage,

[02:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=149s) the number of applications,
the number of nodes even,

[02:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=153s) number of servers.

[02:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=155s) We need platforms to be able to adapt

[02:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=158s) to those technology shifts

[02:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=159s) and what our developers need
to run their applications.

[02:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=163s) You're probably going through
something like that right now.

[02:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=165s) Who's had to have a
meeting with an ML team

[02:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=169s) and like all of a sudden,

[02:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=170s) you gotta integrate machine learning

[02:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=172s) into your application or your platform

[02:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=174s) and support those workloads, right?

[03:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=180s) So as the internet grew,

[03:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=183s) we started to need to have automation.

[03:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=187s) So we went from supporting websites

[03:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=189s) with maybe tens of machines
and we could handcraft.

[03:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=193s) We adopted things like Chef
and Puppet to start automating

[03:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=197s) and having some governance
over those servers.

[03:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=200s) But we never got all the
way with that automation.

[03:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=206s) And now with these massive applications,

[03:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=209s) we started breaking
them into microservices,

[03:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=211s) started using containerization,

[03:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=214s) and that started to solve
some of this control loop,

[03:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=216s) this governance and automation

[03:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=218s) but it came with some additional issues

[03:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=221s) such as an increase in
complexity, dependencies,

[03:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=225s) and just needing something
to manage that complexity.

[03:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=229s) So that's why we started
building these platforms.

[03:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=233s) And we said to ourselves,

[03:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=234s) "If you build it, they will come.

[03:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=236s) The developers will come."

[03:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=239s) Who knows of the "Field of Dreams" movie?

[04:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=243s) All right.

[04:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=244s) So in that movie, a farmer gets visited

[04:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=248s) by a ghost of a baseball
player in the past

[04:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=252s) and is told if he builds
this baseball stadium

[04:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=255s) in his field,

[04:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=257s) all these legendary
baseball players will come.

[04:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=261s) And I think,

[04:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=262s) I was a platform engineer
before I came over to AWS,

[04:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=266s) and I had that same attitude.

[04:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=267s) Oh,

[04:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=269s) my platform's awesome.

[04:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=271s) It has the best features,

[04:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=273s) it's got the coolest stuff,

[04:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=275s) uses docker and containers.

[04:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=276s) Isn't that cool?

[04:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=278s) And I sat there and I had to,

[04:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=280s) and I thought all these developers,

[04:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=282s) there's no way they wouldn't want to come

[04:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=284s) and use my shiny Kubernetes platform.

[04:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=288s) And I sat there

[04:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=289s) and I sat there and then I
realized, no one's showing up.

[04:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=292s) No one's showing up to my field of dreams.

[04:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=294s) So why do we keep doing this?

[04:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=296s) We focus,

[04:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=297s) we think it's just about
the features of the platform

[05:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=304s) and the platforms are abandoned

[05:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=307s) because they don't have
the right features.

[05:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=309s) But it's not that.

[05:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=311s) It must be something else.

[05:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=315s) When we're talking to customers

[05:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=316s) and we start digging into why
those platforms don't succeed,

[05:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=321s) we realize that what really
attracts development teams

[05:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=325s) and your users to a platform is trust.

[05:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=329s) Platforms are abandoned when
they fail to establish trust.

[05:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=334s) Distrust of the platform to
evolve to the meeting needs

[05:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=339s) that leads to shadow IT,

[05:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=342s) distrust in delivering the
services and capabilities

[05:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=346s) that the developer needs,

[05:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=349s) and distrust that the
system will break frequently

[05:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=352s) and in non-known ways.

[05:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=357s) We know it's trust

[05:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=358s) because we know developers

[05:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=359s) will still choose a previous platform

[06:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=363s) that they have a prediction

[06:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=364s) and know the bottlenecks
and know the edges.

[06:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=369s) And they continue to use
those older platforms.

[06:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=372s) So we know that it's trust

[06:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=373s) because they trust that.

[06:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=375s) They're used to it,

[06:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=376s) even if it's ganky, for
lack of a better term.

[06:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=382s) So,

[06:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=384s) what is trust?

[06:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=386s) Trust is three parts.

[06:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=388s) Logic.

[06:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=389s) If you believe that I
have rigor in my logic,

[06:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=392s) then you're more likely
to trust me, right?

[06:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=394s) And hopefully, you will
demonstrate some logic today

[06:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=396s) in this presentation.

[06:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=398s) If you sense that I'm authentic,

[06:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=402s) then I'm more likely to be trusted.

[06:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=405s) And if you sense that I
care about your needs,

[06:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=409s) then you're more likely to trust me.

[06:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=412s) So how does this translate
into a platform perspective?

[06:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=418s) Authenticity,

[06:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=419s) or, yeah,

[07:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=420s) authenticity translates

[07:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=422s) into a collaborative
shared responsibility,

[07:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=426s) showing we collectively
care about the outcomes.

[07:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=428s) You know, you build
you own product mindset

[07:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=432s) for the platform.

[07:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=434s) Logic turns into transparency.

[07:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=436s) Say what you're gonna do and
do what you're gonna say.

[07:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=440s) Commitment to transparency
and collaboration.

[07:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=444s) And then empathy turns into reliability.

[07:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=448s) I care about supporting your services

[07:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=451s) and making sure they run well.

[07:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=453s) And I'm here for your needs,

[07:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=455s) your developer needs.

[07:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=458s) So I want to have you keep that

[07:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=460s) in the back of your mind

[07:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=461s) as Isaac and John do the
rest of the presentation

[07:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=465s) around these three concepts of trust

[07:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=468s) in how to build a scalable platform.

[07:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=472s) Where we see a lot of
friction is how do we keep

[07:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=476s) that trust level high, but
also meet the demands of scale?

[08:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=481s) There's a tension there.

[08:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=482s) We can move fast, scale out,

[08:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=486s) but maybe we reduce reliability

[08:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=489s) or not meet the needs immediately.

[08:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=493s) That erodes the trust.

[08:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=494s) So the challenge in building
these scalable platforms

[08:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=499s) is figuring out a way to meet the scale

[08:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=502s) of the ever evolving technology demands

[08:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=504s) and also keep the trust level high.

[08:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=508s) So I wanna just take a step back.

[08:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=512s) We were talking, preparing
for this presentation

[08:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=514s) and John told me,

[08:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=516s) "Look, at the end of the day,

[08:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=518s) all my developers care
about is getting their code

[08:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=522s) into production as fast as possible."

[08:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=524s) We can talk about all these other things.

[08:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=528s) An example in the past is, you know,

[08:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=531s) you might have a monolithic pipeline

[08:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=533s) and the development team is used to that.

[08:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=535s) So they, you know,

[08:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=536s) they're used to doing that
three to four month deployment

[08:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=538s) in this monolithic app.

[09:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=540s) Now they've broken it
down into microservices,

[09:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=543s) but they don't trust the new platform

[09:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=545s) to be able to handle
deploying these microservices.

[09:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=549s) They don't know the friction

[09:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=550s) or it's a higher friction.

[09:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=552s) So they tend to cram all
those new microservices

[09:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=556s) and the new things they're trying to do

[09:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=557s) into existing pipelines,
that monolithic pipeline,

[09:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=561s) because they know what
the bottlenecks are,

[09:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=563s) what the pain points are

[09:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=564s) and they know what the friction is

[09:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=566s) and they know that that might be the way

[09:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=568s) to get to code in production
as fast as possible

[09:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=571s) in their mind.

[09:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=573s) So I want you to keep that
in the back of your head

[09:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=577s) when we're going through
the rest of these details

[09:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=579s) of how to build these platforms
in the best practices,

[09:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=582s) how to keep that trust level high

[09:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=585s) while also meeting that scale.

[09:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=587s) So Isaac, can you come up and
tell me how we can do that?

[09:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=593s) - Absolutely.

[09:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=594s) Thank you, Nirmal.

[09:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=597s) So let's dive into what we always do

[10:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=602s) when we think about platform
engineering and our plans.

[10:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=606s) We always turn to automation.

[10:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=608s) Almost every single year
for as long as I remember,

[10:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=611s) I've been doing platforms
for a very, very long time.

[10:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=613s) We're gonna automate things,

[10:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=615s) we're gonna automate more things.

[10:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=616s) And this year, what are we gonna do?

[10:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=617s) We're gonna automate again.

[10:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=619s) And next year, I guarantee
on your product roadmap

[10:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=622s) for your platform, more automation.

[10:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=625s) We started off with Puppet, moved to Chef,

[10:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=628s) moved to Ansible, now to Terraform.

[10:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=630s) We are constantly automating.

[10:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=632s) But why isn't that we actually get

[10:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=634s) to this point of automation?

[10:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=636s) And if you think about
like other industries,

[10:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=639s) when was the last time any of
you have ever been in a bank?

[10:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=642s) I've not been in a bank.

[10:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=643s) I can't even remember the
last time I was in a bank.

[10:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=645s) They've automated.

[10:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=646s) It started in the eighties with an ATM,

[10:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=648s) an automated teller machine.

[10:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=649s) It's in the name.

[10:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=650s) So other industries have figured this out,

[10:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=652s) but somehow we, as platform engineers

[10:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=655s) and software developers,

[10:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=657s) still haven't figured it out.

[10:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=658s) Why is it that we're still
automating every year,

[11:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=661s) year after year after year?

[11:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=663s) And I guarantee you,
we're not gonna get it

[11:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=665s) if we continue doing the
exact same things over

[11:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=666s) and over again.

[11:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=668s) So let's dive into this.

[11:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=669s) Now, one of the things that
Nirmal talked about is scale.

[11:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=674s) What changes in our world more
than anywhere else is scale.

[11:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=677s) The number of developers,
the number of services.

[11:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=680s) For those who have been
with AWS for a long time,

[11:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=682s) we started off with EC2 and S3.

[11:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=685s) We now have over 250 different services.

[11:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=688s) We launched a whole bunch of
new services here at re:Invent.

[11:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=691s) Every single year,

[11:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=693s) our scale grows dramatically

[11:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=695s) and we have to adapt to those changes.

[11:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=697s) So as we grow and we scale, what do we do?

[11:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=699s) We break down things into smaller chunks.

[11:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=702s) And I don't mean just microservices,

[11:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=703s) we think about humans, organizations.

[11:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=706s) So we break down our large platform teams

[11:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=708s) into smaller teams.

[11:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=709s) We might have a networking team

[11:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=710s) and they'll have their own set of pipeline

[11:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=712s) and abstractions you see
here, authentication.

[11:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=716s) All of that gets put
into in a stored state.

[11:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=719s) And they deal with networking, right?

[12:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=721s) We also have an infrastructure team.

[12:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=724s) They're gonna be focused on
standing up EC2 instances,

[12:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=727s) maybe your Kubernetes clusters, right?

[12:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=729s) All of that other baseline
foundational infrastructure

[12:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=733s) that you need to actually
run your application.

[12:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=737s) We also will have an observability team.

[12:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=739s) They're gonna be focused on,

[12:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=740s) obviously, bringing up
observability for your applications

[12:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=743s) for the infrastructure,
for the networking.

[12:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=744s) And then they have their own pipeline.

[12:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=747s) Compliance will also have
their own pipeline as well.

[12:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=750s) They'll have their set
of authentication tools

[12:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=753s) and if we're lucky,

[12:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=754s) they'll be using a lot
of the similar tools.

[12:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=756s) But unfortunately,

[12:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=757s) what ends up happening is
everybody sets up their own sets

[12:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=759s) of tools, right?

[12:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=761s) And then finally,

[12:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=762s) finally we can get to
deploying our application.

[12:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=765s) This is the...

[12:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=766s) When we refer to the platform,

[12:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=767s) when most people think about
is just this one pipeline,

[12:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=770s) the CI/CD pipeline that we all talk about.

[12:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=773s) That's when we talk about platforms,

[12:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=774s) that's what most people think about.

[12:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=776s) And they don't think about anything left

[12:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=778s) of that dash line, right?

[13:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=781s) But that isn't all.

[13:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=781s) You don't deploy an application
without any dependencies.

[13:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=784s) You now have to get things
like databases, right?

[13:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=787s) You need to get S3 buckets, ElastiCache.

[13:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=791s) You have a lot of dependencies

[13:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=792s) that your application needs to depend on.

[13:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=794s) Well, that's a whole nother pipeline.

[13:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=797s) But to make things matter,

[13:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=798s) to make things more complex,

[13:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=800s) there's actually one pipeline

[13:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=801s) that actually nobody really
talks about but exists.

[13:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=805s) It is a continuous compliance pipeline

[13:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=807s) that runs behind the scenes and makes sure

[13:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=809s) that everything is
continuously in compliance.

[13:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=812s) Now up until this point,

[13:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=813s) everybody here has been storing
all of their configuration,

[13:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=816s) everything inside of Git,

[13:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=818s) and then they deploy the pipeline

[13:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=820s) and everything seems to work.

[13:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=821s) That moment that you push
that deployment pipeline,

[13:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=823s) you push the button and it works.

[13:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=825s) But how do we come up with drift?

[13:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=829s) Well, drift happens

[13:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=830s) because of things like the
continuous compliance pipeline

[13:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=832s) that runs in the background.

[13:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=833s) It's secret.

[13:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=834s) The developers don't
know anything about that.

[13:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=836s) So what they think is,
"I've put something in Git,

[13:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=839s) but then there's
something else changing it

[14:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=841s) in the background."

[14:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=842s) It'd also be a human being
actually making changes

[14:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=844s) in the background.

[14:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=846s) So this thing that we've talked about,

[14:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=847s) Git as a source of truth
is actually not the source

[14:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=850s) of truth.

[14:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=851s) We had one developer,

[14:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=852s) one customer tell us,

[14:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=853s) "Git is not the source of truth;

[14:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=854s) it is the source of hope,"

[14:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=856s) because of so much drift
between our pipelines

[14:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=859s) and what we expect our intended outcome

[14:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=862s) and then the actual outcome, right?

[14:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=865s) And immediately, we start to break trust.

[14:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=867s) All this trust that we build, we go look,

[14:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=869s) put stuff in Git.

[14:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=871s) You'll trust that what you put in Git,

[14:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=872s) will match what's in production.

[14:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=874s) That doesn't actually happen.

[14:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=875s) So immediately, we start to
break trust with developers.

[14:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=878s) And that's a really important
thing as Nirmal touched on

[14:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=880s) to being able to gain
adoption of your system.

[14:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=883s) So let's go back to this.

[14:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=884s) So let's get back to this diagram

[14:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=886s) and what's complicating things?

[14:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=887s) Why can we not actually automate

[14:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=889s) between all of these pipelines?

[14:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=892s) And the answer is human interaction.

[14:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=895s) Now again, we're gonna
launch a lot of new services,

[14:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=897s) a lot of new features that your developers

[14:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=899s) or you, as a platform
engineers, are gonna want

[15:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=901s) to integrate into your platform.

[15:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=903s) So what is it gonna take?

[15:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=904s) Well, let's simplify this a little bit.

[15:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=906s) Let's just assume we need a new resource.

[15:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=909s) Well, in order to get that resource

[15:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=911s) into your application or
be able to provision it,

[15:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=915s) it needs to interact with
the infrastructure layer.

[15:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=917s) Well, the infrastructure
layer needs to go back

[15:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=919s) to the developers.

[15:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=920s) And now we're setting up
meetings, adding Jira tickets,

[15:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=922s) and we're constantly in meetings,

[15:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=923s) just communicating our requirements.

[15:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=927s) Here's what we need,
here's what we needed.

[15:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=928s) Justification,

[15:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=930s) setting up calendars.

[15:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=932s) This thing,

[15:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=933s) this little feature that
you might need now turned

[15:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=934s) into weeks of meetings.

[15:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=936s) Well, we also need to
run it by compliance.

[15:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=938s) We're not gonna just ship
something into production.

[15:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=941s) There we go.

[15:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=941s) More, more meetings.

[15:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=943s) App developers are now
talking to compliance.

[15:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=945s) Now the network team, you need
to have access to it somehow.

[15:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=947s) Network team's involved.

[15:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=948s) More meetings, more
meetings, more meetings,

[15:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=950s) and more meetings.

[15:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=951s) So the example I gave about
an ATM machine, right?

[15:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=955s) There's no humans involved.

[15:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=957s) And so what slows us down

[15:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=958s) and what makes it impossible
for us to automate is pipelines

[16:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=962s) that we're running in the
interaction between us,

[16:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=964s) the way that we communicate
with each other,

[16:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=967s) is actually just through meetings.

[16:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=969s) We're never gonna automate that,

[16:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=971s) in this way.

[16:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=972s) It's only just gonna lead
to more and more meetings,

[16:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=974s) more and more Jira tickets,

[16:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=975s) and more and more waiting and delays.

[16:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=977s) We know that some customers,

[16:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=978s) when we launch new features here at AWS,

[16:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=980s) it takes some over a year
to actually adopt them

[16:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=983s) due to all of these
meetings and Jira tickets

[16:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=986s) and waiting for people to do the work.

[16:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=989s) And so what we know is that anything,

[16:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=992s) any improvements outside

[16:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=994s) of the bottleneck are just an illusion.

[16:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=996s) So all these other little things

[16:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=998s) that we're automating around,

[16:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=999s) hey, we're gonna automate
this little piece,

[16:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1000s) is not actually getting to the core

[16:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1003s) of what actually needs to
be automated in order for us

[16:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1005s) to be productive as platform engineers.

[16:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1009s) It doesn't build trust

[16:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1010s) because we're constantly just in meetings,

[16:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1012s) talking to each other,
justifying our needs.

[16:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1015s) So this is the core of
platform engineering.

[16:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1018s) Why is this a new thing?

[17:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1020s) Why wasn't this here before?

[17:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1022s) We're finally at the breaking point,

[17:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1024s) finally at the breaking
point of these pipelines.

[17:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1025s) We're finally at the breaking
point of all these meetings

[17:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1027s) because we reach a large scale.

[17:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1029s) So how do we get around this?

[17:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1031s) Well, we can just borrow what
the banking industry has done,

[17:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1034s) is just use APIs.

[17:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1035s) The answer is actually rather simple.

[17:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1038s) Getting there is a lot harder.

[17:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1040s) So how do we think about using APIs?

[17:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1041s) Well, instead of thinking about pipelines,

[17:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1043s) things like networking
or blue-green deployments

[17:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1046s) or you know, getting a
pipeline to get an RDS database

[17:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1051s) or an S3 bucket,

[17:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1052s) we think of these things

[17:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1053s) in terms of capability

[17:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1054s) and what your capabilities

[17:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1056s) and what your platform
instead should be doing

[17:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1058s) is exposing this
capability through an API.

[17:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1061s) Right?

[17:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1061s) APIs are declarative, right?

[17:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1065s) And can be controlled by the
software behind it, right?

[17:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1067s) When you think about a pipeline,

[17:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1068s) you hit that pipeline button,

[17:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1070s) that's it.

[17:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1071s) It runs once.

[17:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1072s) And hopefully, it doesn't break,

[17:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1075s) but then you start to
lose control that way.

[17:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1077s) So we gain control by
moving things behind an API

[17:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1079s) and then we can actually
start automating things.

[18:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1081s) And the way that teams communicate

[18:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1083s) with each other is no
longer through meetings.

[18:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1086s) It's through APIs, which
is a well-established form.

[18:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1089s) So how do we, as platform
engineers, get there, right?

[18:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1092s) So in this diagram here,

[18:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1094s) we've moved all of those disparate APIs,

[18:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1097s) authentication abstraction
into a single layer, right?

[18:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1100s) One facade that encapsulates

[18:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1102s) or abstracts out all of
those complex moving parts

[18:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1105s) behind the scenes so that
your developers can ship fast

[18:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1108s) and ship things into
production as fast as possible.

[18:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1112s) All right.

[18:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1113s) So let's go back into our diagram.

[18:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1114s) We still have the same teams.

[18:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1116s) Those teams didn't go anywhere.

[18:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1118s) But we're now thinking in
terms of software development.

[18:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1120s) We're thinking in terms of APIs

[18:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1121s) and we're building into this platform.

[18:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1124s) And now we've moved more into
a product mindset, right?

[18:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1128s) So the requests that used to come in

[18:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1130s) and require all of these meetings,

[18:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1131s) we're now prioritizing
through a product manager.

[18:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1135s) And this product manager is making sure

[18:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1136s) that we're getting to the
features that we need to

[18:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1138s) as quickly as possible,

[18:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1139s) or the most important features.

[19:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1141s) But there's one challenge
with this, right?

[19:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1143s) So we've solved some of the problems here

[19:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1145s) in terms of removing
some of the bottlenecks

[19:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1147s) of communication between teams,

[19:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1149s) but we still have a bottleneck.

[19:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1151s) And this bottleneck is you
will always have more requests,

[19:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1155s) feature requests from your developers

[19:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1157s) than what your product

[19:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1158s) or your platform engineering
team can ever handle.

[19:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1162s) And so what are they gonna do

[19:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1163s) when you can't get to all
of those feature requests?

[19:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1167s) Are they gonna sit
around and and just wait?

[19:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1169s) No, they're gonna work around you.

[19:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1171s) And many of us know this as Shadow Ops

[19:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1173s) or you know, these rogue teams
that go build this platform

[19:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1175s) or go end up using a different service

[19:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1178s) without you knowing,

[19:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1179s) work around you because they
can't actually use the platform

[19:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1182s) and based on their needs.

[19:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1185s) But this isn't what we want.

[19:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1186s) We don't want them working
around this, right?

[19:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1188s) This is another form of
us breaking trust, right?

[19:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1191s) This is developers not
breaking trust with us

[19:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1192s) as platform engineers, right?

[19:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1194s) Eroding trust.

[19:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1195s) It constantly happens.

[19:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1196s) It's all little by little
breaking this trust.

[19:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1198s) What we really want them
to do is we want them

[20:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1201s) to extend our platform, right?

[20:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1203s) But we can't get them
to extend our platform

[20:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1205s) if everything that we do is proprietary

[20:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1207s) and we're writing our own code

[20:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1209s) and building our own documentation,

[20:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1210s) which sometimes we don't
even get to, right?

[20:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1213s) So how do we cultivate this
kind of culture, right?

[20:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1217s) This is exactly what
Nirmal was talking about,

[20:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1219s) collaboration.

[20:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1220s) How do we collaborate with each other?

[20:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1224s) Right, and for those
who have read the book,

[20:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1226s) "Team Topologies,"

[20:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1227s) this is one of the major
concepts in the book is,

[20:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1230s) we as platform engineers
and where we are today,

[20:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1233s) we started off in facilitation.

[20:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1235s) The idea of SRE and DevOps was,

[20:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1237s) hey, I will embed a human
being into your team

[20:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1240s) and they will help you actually
launch your application.

[20:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1243s) And now for the most part,
most people are starting

[20:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1245s) to move into this acts as a service,

[20:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1248s) database as a service,

[20:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1249s) platform as a service,

[20:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1250s) Kubernetes as a service, right?

[20:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1251s) All of these containers
as a service, right?

[20:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1254s) And that'll get you to the
next level of scalability.

[20:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1258s) But where we need to
move to is collaboration.

[21:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1260s) So what can we look to

[21:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1262s) to help us collaborate?

[21:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1263s) What other forms in the world,

[21:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1264s) just like in the banking
example, we used APIs.

[21:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1267s) What other form of
software can we leverage

[21:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1270s) to actually help us collaborate?

[21:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1273s) So for many here,

[21:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1275s) I'm sure you all use open
source software, right?

[21:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1277s) Those communities in open source

[21:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1280s) have exhibited
transparency, collaboration.

[21:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1284s) They earn trust.

[21:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1285s) That's how they get to be so big.

[21:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1286s) There's a huge community.

[21:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1287s) So if we inherit an open
source framework, right,

[21:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1291s) for our platform,

[21:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1293s) we get to bring along all of that with us:

[21:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1295s) transparency, collaboration, the trust.

[21:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1298s) So what if we use Kubernetes
as this framework?

[21:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1300s) Now up until this point,

[21:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1301s) I assume many of you have used Kubernetes

[21:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1303s) to deploy containers.

[21:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1305s) And think of it as a container
orchestration system.

[21:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1308s) From this point on,

[21:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1309s) I'm not gonna talk about
orchestrating containers.

[21:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1312s) I'm gonna talk about
strictly as a platform.

[21:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1314s) Even if you never use Kubernetes
to deploy a container ever,

[21:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1319s) you can still use it as
your platform layer, right?

[22:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1322s) And why would we want to do that?

[22:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1323s) That seems kind of crazy.

[22:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1324s) But why would we wanna do that?

[22:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1325s) Because it has every foundational aspect

[22:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1328s) of what a platform needs

[22:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1329s) and has an API handler

[22:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1331s) and has RBAC built in,

[22:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1333s) has a mutating admission controller

[22:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1335s) that helps us actually
control what gets in and out

[22:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1337s) and able to make changes on
the way into the platform,

[22:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1339s) which is important.

[22:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1341s) As we keep going,

[22:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1342s) we can build in web hook
controllers, schema validation,

[22:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1346s) have other controllers here

[22:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1347s) that actually integrate with Kubernetes

[22:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1350s) so that we can add our own business logic

[22:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1352s) and our own compliance.

[22:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1353s) But most importantly
here is we have one place

[22:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1357s) to store state.

[22:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1358s) If you go back to those pipelines,

[22:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1360s) every single one of those
pipelines stored state

[22:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1363s) in their own different way.

[22:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1364s) And if you're using Terraform,

[22:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1366s) every time you run a pipeline,

[22:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1368s) it creates a new state file, right?

[22:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1370s) That's a different state
stored somewhere else.

[22:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1373s) And there's no way to really query it.

[22:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1374s) If I wanna understand what is
the state of my application,

[22:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1377s) I have to go to four or five
different state stores, right?

[23:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1380s) And that makes it really
hard to build trust

[23:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1382s) with a developer

[23:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1383s) when they can't actually see
what's happened in the past.

[23:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1387s) So ETCD serves as our single state store.

[23:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1389s) And instead of capabilities,

[23:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1392s) Kubernetes calls them controllers, right?

[23:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1394s) But in the end of the
day, every single time

[23:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1396s) that you add a controller or a CRD

[23:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1398s) into your Kubernetes cluster,

[23:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1399s) what are you effectively doing?

[23:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1401s) You're adding a new
capability to that platform.

[23:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1404s) So if you're using a secrets controller

[23:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1406s) or an API controller, that
is actually what's happened.

[23:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1410s) You're enabling some new
behavior or new feature.

[23:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1413s) So how do we extend this further?

[23:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1414s) Okay, you're already doing it.

[23:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1416s) For those who are
already using Kubernetes,

[23:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1417s) you in fact are already doing this, right?

[23:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1420s) So this isn't necessarily something new,

[23:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1422s) it's just thinking about
it in a different way.

[23:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1426s) The other reason why we want

[23:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1427s) to use something like
Kubernetes is the notion

[23:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1429s) of abstractions.

[23:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1430s) Abstractions help hide away complexity.

[23:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1433s) When we think about an API,

[23:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1435s) in fact, that is what's happening, right?

[23:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1437s) We are hiding away that
complexity behind an API.

[24:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1441s) Again, going back to that
banking example and APIs,

[24:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1446s) it's not like the bank is asking you

[24:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1447s) if you want to take money from one account

[24:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1449s) and put it into another.

[24:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1451s) They're not asking you
to tell them the process

[24:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1453s) of how to do that.

[24:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1454s) They just go, "Hey, what do you need?"

[24:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1455s) And the API will handle it.

[24:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1457s) So how do we do this here in Kubernetes?

[24:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1458s) Everybody's very familiar with
the deployments abstraction.

[24:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1461s) The deployment abstraction
is actually an abstraction

[24:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1463s) over a replica set, which
is an abstraction over pods,

[24:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1467s) which is an abstraction over containers.

[24:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1469s) Now, the beauty of Kubernetes is that

[24:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1472s) if you need a new set of functionality,

[24:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1475s) let's say blue-green,

[24:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1476s) would you throw all of this away?

[24:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1479s) Now, you wouldn't throw this away.

[24:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1482s) Instead you would add blue-green

[24:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1483s) and leverage all of the
abstractions underneath.

[24:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1486s) And so what we call this

[24:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1487s) in software development world
is composability, right?

[24:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1490s) We're able to actually
compose a whole bunch

[24:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1492s) of different pieces of functionality

[24:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1494s) and bring it into one, right?

[24:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1496s) And for those who use Argo,

[24:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1497s) there's ability to have blue-green

[25:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1500s) and that's actually all they do.

[25:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1501s) They take replica sets, pods, containers,

[25:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1503s) and build their own blue-green
abstraction over top of it.

[25:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1506s) All right, so let's extend
this a little bit further.

[25:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1509s) All right, because remember,

[25:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1510s) developers don't care
about any of this stuff.

[25:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1512s) They care about their application,

[25:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1514s) they care about their application
getting into production

[25:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1516s) as quickly as possible, right?

[25:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1518s) So let's build more abstractions.

[25:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1520s) So within Kubernetes,

[25:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1521s) we can build a new abstraction
called an application, right?

[25:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1524s) That's what they care about.

[25:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1525s) Now, the term application
can mean something

[25:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1527s) for me in my organization,

[25:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1529s) which will be different than for you all

[25:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1531s) in your organization.

[25:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1532s) So this is just an example.

[25:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1534s) So an application might need an ingress,

[25:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1537s) you might need an S3 bucket

[25:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1539s) and S3 bucket, of
course, needs IM policies

[25:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1541s) and we're building these
other abstractions as well

[25:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1544s) and connecting the dots.

[25:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1546s) We have ticketing,

[25:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1548s) usually we use Jira tickets
or ServiceNow tickets

[25:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1550s) to enforce compliance.

[25:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1551s) So our compliance abstraction is there.

[25:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1554s) But that's not all.

[25:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1555s) We need an environment to deploy to.

[25:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1557s) Are we deploying to dev stage?

[25:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1559s) And that environment needs
an account, a VPC, a subnet.

[26:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1562s) You might need a Kubernetes cluster.

[26:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1564s) And all of these abstractions
can live inside of Kubernetes.

[26:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1568s) So if we tie this all
together, what do we have?

[26:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1571s) We have an application that
points to an environment

[26:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1574s) that also points to a
ticketing system to help us

[26:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1576s) with compliance and track changes.

[26:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1578s) We have that application
that has ingress, buckets,

[26:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1581s) also its own ticketing system

[26:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1583s) to make sure that we're
enforcing compliance.

[26:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1585s) And this is what a developer
really cares about.

[26:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1588s) It's just this application,
this little box,

[26:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1590s) not really so much
everything underneath it.

[26:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1593s) And so if we recall the pipelines

[26:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1594s) that we had at the very early on,

[26:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1596s) all that communication,

[26:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1597s) all those meetings starts to go away

[26:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1600s) when we start thinking about
Kubernetes as a platform

[26:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1602s) and start thinking about composability.

[26:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1604s) We're able to just combine
different components

[26:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1606s) without having to jump
into these meetings.

[26:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1609s) We've moved away from pipelines

[26:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1611s) and that's what Kubernetes
helps us to do, right?

[26:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1614s) It simplifies this.

[26:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1618s) Developers care about
applications not infrastructure.

[27:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1621s) And there's also one other thing here too.

[27:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1624s) You remember that continuous
compliance pipeline,

[27:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1626s) that secret pipeline
that runs in the back?

[27:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1629s) You notice that we don't
have this for Kubernetes?

[27:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1632s) And the reason we don't
have this for Kubernetes is

[27:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1634s) because we have this
continuous control loop.

[27:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1636s) That control loop

[27:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1638s) in that continuous compliant is built

[27:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1640s) into the very foundational
fabric of Kubernetes, right?

[27:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1644s) So the more we leverage Kubernetes
for our platforms, right,

[27:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1647s) the more trust we have

[27:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1648s) because everything is there,
the more transparency we have.

[27:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1650s) In fact, actually, when you
query something in Kubernetes,

[27:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1652s) you have,

[27:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1653s) here's my intended state,

[27:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1654s) here's my actual state,
all in one API call.

[27:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1658s) And every single API
call, it returns your spec

[27:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1660s) and then the actual status, right?

[27:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1665s) The other reason why we
wanna leverage Kubernetes

[27:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1666s) is it has a large
controller ecosystem, right?

[27:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1669s) You're not doing this on your own.

[27:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1671s) You're leveraging that community

[27:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1673s) that already has a lot of trust,

[27:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1674s) that already has a lot of transparency.

[27:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1676s) There's a number of
open source controllers

[27:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1679s) that you can use to add functionality.

[28:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1681s) I talked about Argo.

[28:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1682s) You don't need to build your
own blue-green functionality

[28:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1684s) in automation,

[28:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1685s) use Argo and bring that in

[28:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1686s) and now you have additional
deployment semantics

[28:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1689s) within inside of your platform.

[28:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1691s) We also just recently launched K-R-O, kro,

[28:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1694s) that helps you build these abstractions

[28:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1696s) on top of ACK, right?

[28:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1697s) Which also represents objects in AWS

[28:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1701s) in a Kubernetes friendly way, right?

[28:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1703s) So there's a huge controller
ecosystem out there

[28:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1705s) that allows you to develop without

[28:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1707s) or to develop these abstractions
without you having to code.

[28:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1710s) But of course, at some point,
you may hit a limitation

[28:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1713s) of what's available and
you will need to code

[28:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1716s) or you create your own custom controllers

[28:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1717s) and you can do that as well.

[28:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1719s) And now you can start mixing
and matching and composing.

[28:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1723s) All right.

[28:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1724s) But most importantly,

[28:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1725s) what does this enable
for your organization?

[28:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1728s) It enables our teams and our human beings

[28:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1731s) to collaborate differently.

[28:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1733s) Again, we're moving away
from the notion of pipelines

[28:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1736s) and interacting through
words and Jira tickets,

[29:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1740s) to now putting everything into code

[29:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1742s) and taking each other's components

[29:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1744s) and building something new.

[29:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1746s) So you'll notice on the left hand side,

[29:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1747s) we have app team architects,

[29:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1749s) on the left hand side of this API,

[29:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1752s) where we have database
architects, security compliance,

[29:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1755s) all writing all of their requirements,

[29:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1759s) again, not into tickets

[29:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1761s) but into a declarative language, right?

[29:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1765s) And Kubernetes allows us to do this.

[29:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1768s) Now the great thing about
Kubernetes allowing us

[29:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1771s) to do this, right?

[29:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1772s) It's great.

[29:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1773s) You don't have

[29:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1773s) to actually have very many
worker nodes for this,

[29:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1775s) but you do need a scalable control plane

[29:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1777s) because we are now
putting a lot of pressure

[29:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1779s) on the control plane as a platform,

[29:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1781s) not just as a component,

[29:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1783s) not just as a container
orchestration system.

[29:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1786s) And this is where EKS comes in.

[29:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1788s) We have worked over the last seven years

[29:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1790s) to make EKS the most scalable,

[29:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1792s) managed Kubernetes control
plane on the planet.

[29:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1796s) So if you just use EKS,

[29:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1799s) you're delegating all of that to AWS

[30:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1802s) and now you can just focus
on building your platform

[30:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1805s) without actually having to
create a bunch of worker nodes

[30:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1807s) and manage yet another set of APIs

[30:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1810s) in containers somewhere else.

[30:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1811s) We'll do that for you.

[30:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1814s) The other great thing is, of
course, we already mentioned,

[30:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1816s) you're not on your own, right?

[30:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1818s) We're inviting people to
the other side of the table

[30:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1820s) behind the curtain.

[30:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1822s) You now get to bring your app developers

[30:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1824s) and your other teams to the left side,

[30:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1826s) but also the community.

[30:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1827s) And lastly, you can now,

[30:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1829s) because you're moving away

[30:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1830s) if you're doing platform engineering

[30:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1832s) and moving away from proprietary code

[30:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1834s) that you're writing on your own

[30:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1836s) or your proprietary platform,

[30:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1838s) you can now have us help you.

[30:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1840s) We have blueprints, we have CNOE,

[30:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1842s) which is our a opinionated
platform community out there,

[30:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1847s) all putting out a bunch of configuration,

[30:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1849s) a bunch of open source tools

[30:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1852s) to help you build your platform with us.

[30:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1854s) We have specialists that can come in

[30:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1855s) and help you build your tool

[30:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1857s) because if you're building
it with open source,

[30:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1859s) well, we know how that works.

[31:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1860s) We can see it.

[31:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1861s) That's what the transparency is there.

[31:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1863s) So you're not on your own anymore

[31:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1864s) when you're thinking about platform.

[31:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1866s) You're not,

[31:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1866s) you're collaborating,

[31:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1868s) you're thinking beyond the
walls of platform engineering,

[31:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1870s) and this is what's gonna help you scale.

[31:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1873s) This is the foundation of
building that trust, right?

[31:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1876s) We're gonna get...

[31:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1877s) We have to get to the point
that we're bringing developers

[31:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1879s) and other people behind the curtain

[31:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1881s) of this platform engineering team.

[31:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1884s) Alright, so let's walk through
what this would look like

[31:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1887s) in practice.

[31:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1888s) So we go back to Git, here in number one,

[31:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1890s) developers are actually pushing
Git configuration into Git.

[31:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1897s) Two, we have Argo,

[31:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1898s) or a controller monitoring Git

[31:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1900s) to make sure that we have those changes.

[31:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1903s) Argo or any CI/CD system
that you have in there,

[31:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1906s) we'll then push it to the API server.

[31:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1907s) At this point, by the way,

[31:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1908s) we actually haven't applied
anything into Kubernetes.

[31:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1911s) There's no changes being made.

[31:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1912s) We have to go first through
the admission controller

[31:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1914s) and make sure that these
changes are valid changes,

[31:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1917s) they're good changes,
they're compliant changes.

[31:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1919s) That gets pushed into ETCD,
our single state store.

[32:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1922s) This is for,

[32:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1924s) again, for S3 buckets.

[32:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1925s) RDS, this could be for
your applications, right?

[32:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1928s) All of those abstractions we talked about

[32:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1930s) now have their representation in that CD.

[32:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1934s) That gets put into a tenant name space.

[32:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1937s) We have controllers sitting
there and listening,

[32:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1939s) reconciling,

[32:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1940s) noticing those changes,

[32:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1942s) going out, reaching out to any API.

[32:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1944s) Now, of course, I talked
a lot about the AWS API,

[32:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1946s) but you can use this to
manage other resources,

[32:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1948s) other observability resources.

[32:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1951s) Anything that has an API,

[32:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1953s) we now are communicating with
it and making those changes.

[32:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1957s) Number seven here is
getting the status back

[32:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1959s) from those changes.

[32:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1960s) So now we have our intent and
our status in the same place

[32:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1964s) and we're updating that in that CD.

[32:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1966s) And as we go back down to eight,

[32:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1968s) we have our presentation layer,

[32:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1970s) a single presentation layer

[32:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1971s) that represents our
networking, our observability,

[32:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1974s) our applications, our history.

[32:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1976s) Everything a developer
needs to get their job done

[32:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1979s) and get their application into production,

[33:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1981s) they can see it in a
single presentation layer.

[33:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1983s) And in this example, I'm using Backstage,

[33:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1985s) you could build your own one,

[33:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1986s) you can use another open
source tool or use a vendor.

[33:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1989s) But it makes it super simple
now that we have everything

[33:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1992s) behind a single API that
happens to be Kubernetes

[33:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1996s) but at its core, it's an API.

[33:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=1998s) Getting back to that automation.

[33:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2001s) So some of the key takeaways.

[33:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2003s) Build your community and collaborate.

[33:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2005s) Do not think of yourself
as just this platform team

[33:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2008s) that is a finite set of resources.

[33:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2010s) Think about open source, think about AWS,

[33:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2013s) we're here to help, right?

[33:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2015s) Build a bigger community.

[33:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2017s) Another one is have a product mindset.

[33:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2018s) You still need to make sure

[33:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2019s) that you're being empathetic
to your developers,

[33:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2021s) you're listening to them,

[33:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2023s) and you're building
exactly what they need.

[33:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2026s) Abstract away complexity with APIs.

[33:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2029s) This is key, right?

[33:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2030s) When we think about pipelines,

[33:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2031s) what we're really doing is
exposing that complexity,

[33:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2034s) all of those steps
directly to the developer,

[33:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2036s) which is not very helpful.

[34:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2041s) And lastly, leverage open
source for transparency

[34:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2044s) and reduce your undifferentiated
lifting by leveraging EKS

[34:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2048s) to manage that control plate for you.

[34:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2050s) Now up until this point,

[34:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2052s) Nirmal has been talking about high level.

[34:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2054s) I've been talking a
little bit lower level,

[34:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2056s) but it's still rather abstract.

[34:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2057s) Next, I'd like to invite
John Weber from Adobe

[34:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2060s) to talk about how to make
this an actual reality.

[34:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2062s) He's done this in real life.

[34:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2063s) So, come on stage here, John.

[34:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2066s) Take on over.

[34:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2067s) - Thank you sir.

[34:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2068s) - Thank you.

[34:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2069s) (audience claps)

[34:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2070s) - Welcome to KUB301, how to stop meetings.

[34:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2077s) Thanks so much, Isaac.

[34:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2078s) I'm really excited

[34:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2079s) to share Adobe's story
with you here today.

[34:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2083s) I don't know how things
work at your company,

[34:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2085s) but at at Adobe, it could be really hard

[34:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2087s) to get a service out the door.

[34:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2089s) It takes on order a
month for a new developer

[34:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2092s) to get up and running with
a new Greenfield service.

[34:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2095s) Not only do they need to write the code,

[34:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2098s) but they probably have
to create some tickets

[35:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2100s) to get access to observability
systems or production

[35:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2103s) and wait for humans to go ahead

[35:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2105s) and respond to those tickets.

[35:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2107s) And meanwhile, they actually
have to write the code,

[35:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2109s) they have to deploy the code,

[35:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2110s) they have to test integrations.

[35:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2112s) And then the humans,
where the tickets went to,

[35:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2114s) come back and say,

[35:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2115s) "I have no idea what
you're asking me for."

[35:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2118s) And between bartering of
what the developer needs,

[35:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2122s) you have to think about
production readiness.

[35:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2124s) All the monitoring tools,
are they all set up?

[35:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2126s) Do you have alerts?

[35:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2127s) What is your backup strategy?

[35:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2129s) And are you ready with
your incident response

[35:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2132s) when something goes wrong?

[35:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2133s) Because it will.

[35:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2135s) I'm part of the developer platforms group

[35:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2137s) and our motto is very simple:

[35:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2140s) help developers write
better software faster.

[35:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2144s) How do you make this landscape do that

[35:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2146s) so developers can actually
achieve that outcome?

[35:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2149s) I'm a fan of abstraction and platforms

[35:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2153s) where you need to simplify

[35:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2154s) and in many cases, oversimplify
for your developers.

[35:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2159s) I'm also a fan of our
cloud providers like AWS,

[36:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2161s) who could manage all this
stuff better than I ever could.

[36:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2165s) Where do all of these
principles intersect?

[36:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2168s) I want to turn your attention

[36:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2169s) to the bottom box labeled, Ethos.

[36:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2173s) At some point in my career,

[36:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2175s) I've probably run every
customer-facing product

[36:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2178s) that Adobe has to offer.

[36:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2180s) And one of my core challenges
was around consistency.

[36:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2184s) As I like to say, Adobe is
inconsistently inconsistent.

[36:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2190s) We would've some technical
alignment around strategy,

[36:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2192s) hey, we should use a public
cloud provider like AWS.

[36:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2196s) But then each engineering
team would go off

[36:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2198s) and make their implementation unique.

[36:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2201s) When every team is able to do that,

[36:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2203s) how do you prevent sprawl?

[36:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2204s) And worst of all, a terrible
customer experience,

[36:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2208s) which is the last thing
that any of us want.

[36:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2211s) So at Adobe, we decided to create Ethos

[36:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2214s) and we needed to make a few big bets.

[36:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2216s) Some of them we got right,

[36:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2217s) containers and docker.

[36:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2219s) Some of them we got wrong, Mesos.

[37:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2222s) And so we also needed to give some level

[37:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2225s) of flexibility to our customers.

[37:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2227s) Some of them wanted
just a turnkey solution

[37:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2229s) where they didn't care about any

[37:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2231s) of the underlying infrastructure

[37:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2233s) and that was CaaS or
container as a service.

[37:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2237s) We also realized

[37:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2237s) that Kubernetes was where
the industry was headed

[37:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2240s) and some teams wanted
to consume native APIs

[37:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2244s) and choose their own
adventure, as I like to say.

[37:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2247s) And that was our platform as
a service offering or PaaS.

[37:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2251s) So building on a scalable
technology foundation

[37:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2254s) like Kubernetes enable
us to have future pivots,

[37:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2257s) say towards GitOps powered by Argo.

[37:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2262s) Like Nirmal said,

[37:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2264s) I believe developers literally
care about one thing:

[37:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2269s) "How do I get my code to
production as quickly as possible?

[37:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2274s) So what are my users interested in

[37:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2277s) and what am I interested in,

[37:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2279s) given we're all part of
the big Adobe family?

[38:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2282s) So Ethos exposes these capabilities,

[38:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2284s) so developers don't have to
think about any of this stuff.

[38:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2288s) They don't need to think

[38:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2288s) about how would I run cloud
infrastructure at scale?

[38:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2292s) They don't need to think
about how I build a CI/CD,

[38:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2294s) a robust CI/CD pipeline.

[38:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2296s) They certainly don't want
to think about security

[38:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2298s) and compliance.

[38:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2300s) And of course cost is always top of mind

[38:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2304s) with finite resources like GPUs.

[38:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2307s) And in cases where we
can provide insights,

[38:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2309s) we also want to think how
can we absorb that pain

[38:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2311s) from the developer

[38:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2312s) and take action on their behalf.

[38:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2316s) Folks, we are a product team.

[38:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2319s) You may not be able to
go to Adobe's website

[38:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2321s) and purchase Ethos or your
favorite e-commerce store,

[38:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2325s) but if you are a customer

[38:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2326s) or a user of Adobe's
products, you use Ethos.

[38:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2330s) And because I'm a product team,

[38:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2332s) I need to be very much
aligned with my stakeholders

[38:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2336s) to build trust and respect with them.

[38:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2339s) The first group is our internal customers,

[39:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2341s) our developers.

[39:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2343s) Yes, these folks are customers.

[39:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2347s) One of my early career failures was,

[39:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2349s) I refuse to call these
folks customers, right?

[39:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2351s) They're colleagues, they're coworkers.

[39:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2353s) I was completely wrong.

[39:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2356s) If you don't consider your
developers your customers

[39:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2359s) and don't build a level of respect

[39:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2361s) and empathy with them, you will fail.

[39:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2364s) You will fail.

[39:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2367s) So what do your customers need?

[39:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2369s) Clear documentation.

[39:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2371s) A UX makes sense.

[39:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2373s) Low barriers to entry,

[39:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2374s) because they don't want to use
a system that's hard to use.

[39:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2378s) External customers.

[39:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2380s) Adobe is the dial tone and the fabric

[39:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2382s) for everything that we provide.

[39:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2385s) We're here to achieve and
enable high quality features

[39:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2390s) and value for all of our end users.

[39:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2393s) AWS.

[39:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2395s) Is AWS able to satisfy the needs of Adobe?

[40:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2401s) Conversely, am I giving the
right level of feedback to AWS

[40:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2405s) so they can hide and abstract all the way

[40:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2407s) to that ugly complexity
that I don't want to see?

[40:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2413s) Adobe very much has a soft culture.

[40:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2416s) We love to give a blank canvas
to our users and unlock them

[40:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2420s) and say, "Hey, go build some
magic powered by Adobe."

[40:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2424s) We also do that with our developers.

[40:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2426s) And as you can see,

[40:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2427s) when you hand a blank
canvas over your developers,

[40:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2430s) things could go wrong.

[40:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2432s) So what we had to do is we had

[40:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2433s) to build a grassroots ground game

[40:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2436s) to get them onboard and on site.

[40:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2438s) We started with a platform
champions program.

[40:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2442s) If you get boots on the ground
within each development team,

[40:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2446s) if you have advocates and promoters

[40:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2449s) for what you're trying to achieve,

[40:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2451s) and most importantly, if
they have skin in the game,

[40:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2454s) you're gonna build an incredibly strong

[40:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2457s) and vibrant community.

[41:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2461s) We also have embraced
an inner source model.

[41:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2463s) You will never have enough resources

[41:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2466s) to do all of the things the
business is asking you to do.

[41:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2470s) So you need to not only
scale your technology,

[41:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2472s) but you need to scale how you operate.

[41:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2475s) We have a very well-defined
open contribution model

[41:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2479s) to Ethos within Adobe.

[41:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2482s) You need to listen to your customers.

[41:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2484s) And we do this through CABs.

[41:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2486s) We sit down with our users regularly

[41:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2489s) and we listen to their pain points

[41:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2490s) and they say, "Hey, you're making my job

[41:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2492s) or my life so much easier."

[41:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2494s) Or they're telling us,

[41:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2495s) "Man, what did you just build for us?"

[41:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2498s) Tough love is okay.

[41:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2499s) Feedback is a gift.

[41:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2504s) This is what we've been able to achieve.

[41:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2506s) This year, we received
six times the number

[41:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2509s) of contributions outside
of our organization.

[41:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2514s) 25,000 contributions to Ethos are outside

[41:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2518s) of the Ethos team.

[41:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2519s) 25,000.

[42:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2526s) We have about 1,500
contributors within Adobe

[42:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2530s) as part of this journey.

[42:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2533s) This is up from 230 last year.

[42:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2535s) Imagine if you had 1,500 extra developers

[42:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2538s) willingly contributing to your code base.

[42:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2542s) It's really amazing.

[42:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2545s) In order to be successful,

[42:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2547s) you need to build a
culture of accountability.

[42:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2551s) I believe engineers
acting as product owners,

[42:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2554s) and I mean this in the agile sense,

[42:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2557s) so no offense to my product
manager friends out there,

[42:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2560s) but every engineering manager needs

[42:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2562s) to be a customer advocate.

[42:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2565s) They should understand and have a vision

[42:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2567s) for what they're building
and how it should function.

[42:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2571s) They should be having
continuous conversations

[42:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2574s) with the people that
they're delivering value to.

[42:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2578s) To quote the great Werner
Vogels, "You build, you run."

[43:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2584s) Guess who gets to be on
call at 2:00 AM on a Tuesday

[43:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2587s) when things break?

[43:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2589s) Yep.

[43:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2589s) The people who write the software.

[43:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2592s) And when things go wrong,

[43:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2594s) your developers need to understand

[43:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2596s) and have empathy and share
some of the pain and burden

[43:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2599s) that your customers are going through.

[43:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2601s) Amazingly, people are highly motivated

[43:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2604s) to fix systemic issues

[43:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2606s) if they continue to get
woken up every night.

[43:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2608s) Go figure.

[43:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2612s) The developers,

[43:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2612s) the people consuming
the amazing capabilities

[43:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2615s) that we're building,

[43:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2617s) need to understand the cloud is not free.

[43:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2619s) This stuff costs real money.

[43:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2622s) So we built granular
dashboards and cost attribution

[43:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2626s) and then we send those teams a bill.

[43:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2630s) And because I care about Adobe's money

[43:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2633s) and they care about Adobe's money,

[43:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2636s) we had to take a pivot

[43:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2637s) and think about how we could
absorb some of that pain.

[44:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2641s) And we did that

[44:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2642s) through the automatic
resource configurator or ARC.

[44:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2647s) Raise your hands.

[44:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2648s) Who believes developers
get container sizing right

[44:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2651s) the first time they deploy production?

[44:13](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2653s) Anyone?

[44:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2654s) No, okay.

[44:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2655s) That's what I thought.

[44:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2657s) ARC's a really simple system

[44:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2658s) that we built with the
Adobe research team.

[44:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2661s) When engineers request
capacity on an Ethos cluster,

[44:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2665s) we deploy the pod along with
an open policy agent or OPA

[44:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2669s) and we evaluate

[44:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2670s) and give us hooks to be able
to change their pod spec.

[44:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2673s) Now we deploy workload

[44:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2675s) on a worker that has available capacity

[44:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2677s) and then we record utilization
metrics through Prometheus

[44:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2681s) and then we store those

[44:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2682s) in a long-term time series
database like Cortex.

[44:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2685s) Then ARC begins to look at the utilization

[44:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2688s) and then recommends container sizing

[44:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2691s) to the developer via an
automatic pull request.

[44:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2695s) And once the dev accepts the
PR and says, "You know what?

[44:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2697s) I may have gotten this wrong,"

[44:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2699s) GitOps will do its magic and take over

[45:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2702s) once that gets merged

[45:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2704s) and we go ahead and have
container sizing solved.

[45:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2710s) Like any service provider,

[45:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2712s) I need to have an enforceable
contract with my users.

[45:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2716s) I need to set targets, measure them,

[45:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2719s) and hold myself accountable
to the results and outcomes.

[45:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2724s) I do this by embracing
service level indicators

[45:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2726s) and service level objectives.

[45:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2729s) By defining my core capabilities,

[45:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2732s) can I deploy?

[45:34](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2734s) Can I scale?

[45:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2736s) Do I have network connectivity?

[45:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2737s) And then I measure and
evaluate my performance

[45:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2740s) on a continuous basis.

[45:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2743s) I also fully embrace DKS.

[45:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2745s) Folks, there's no glory running
Kubernetes on an EC2 node.

[45:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2751s) Right?

[45:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2752s) You have much better things to do.

[45:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2754s) Everybody should be striving
towards declaring bankruptcy,

[45:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2758s) infrastructure bankruptcy and
giving this all to Amazon.

[46:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2762s) And when stuff goes wrong and it will,

[46:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2765s) can your team write a high quality RCA?

[46:08](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2768s) And not only that,

[46:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2769s) would you be comfortable
publishing externally?

[46:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2772s) You need to set that bar really high.

[46:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2776s) Imagine being customer of service

[46:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2778s) where you could, on demand,
check my homework in real time

[46:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2783s) to make sure you're getting
what I promised you.

[46:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2786s) We've been able to do that at Adobe.

[46:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2788s) Here's a sample dashboard that's available

[46:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2791s) to anyone in the company.

[46:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2793s) And in this example,
we're assessing the health

[46:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2795s) of the egress capability
for our Ethos cluster.

[46:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2798s) Am I delivering on the
promise that I've made

[46:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2801s) to ensure outgoing network connectivity

[46:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2805s) for the Kubernetes clusters
that our team manages?

[46:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2810s) I also care about my customer's
reliability and uptime.

[46:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2815s) I know that getting observability,
working is really hard.

[46:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2819s) Agents, collectors, metrics,
traces, logs, events,

[47:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2824s) and so on and so forth.

[47:06](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2826s) So we've rallied around open SLO.

[47:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2829s) Folks, this stuff is solved in many cases.

[47:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2832s) You don't need to make your lives harder

[47:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2834s) and figure out how to build
this stuff on your own,

[47:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2837s) like we initially thought we had to.

[47:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2839s) So all of our applications on
Ethos are auto instrumented

[47:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2843s) wherever possible.

[47:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2844s) We do need to take a maybe
a few inputs from a user,

[47:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2847s) like what their target should be.

[47:29](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2849s) But then our tooling takes over

[47:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2851s) and with the magic on open SLO,

[47:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2852s) we're able to calculate
error budgets automatically

[47:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2856s) for all of our applications on Ethos.

[47:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2861s) So where are we investing

[47:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2863s) and what are those returns
on that investment?

[47:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2867s) The main KPI that I look at

[47:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2868s) around operational scaling is
our cluster-to-operator ratio.

[47:54](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2874s) And since we've pivoted to EKS

[47:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2876s) and declared infrastructure bankruptcy,

[47:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2878s) I'm happy to tell you

[48:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2880s) that we've scaled our
operator-to-cluster ratio

[48:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2883s) from 10 to one

[48:04](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2884s) to 30 to one.

[48:07](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2887s) We're also looking to retire
our homegrown solution

[48:10](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2890s) and embrace GitOps and Argo.

[48:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2892s) And this is way more flexible

[48:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2894s) with newer use cases like generative AI.

[48:16](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2896s) And lastly, we need to reduce friction.

[48:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2899s) Having less places for
your developers to go

[48:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2903s) means that they'll be happier
and they will work faster.

[48:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2908s) We've done that by
moving all of our portals

[48:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2910s) into one and embracing Backstage.

[48:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2916s) So what are the outcomes of this work?

[48:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2919s) What does this scoreboard show

[48:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2921s) at the end of the fourth quarter?

[48:43](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2923s) And are we winning?

[48:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2926s) We are winning.

[48:48](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2928s) Developers are able to deploy
a full greenfield stack

[48:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2932s) in just a few days rather
than waiting an entire month.

[48:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2935s) There are less meetings too, by the way.

[48:58](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2938s) And included in that Greenfield stack

[49:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2940s) is our observability platform,

[49:01](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2941s) which I'm happy to say has
driven the time it's taken

[49:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2945s) to detect an incident by over 75%.

[49:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2949s) Cost will continue to be a major theme

[49:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2952s) as we go forward into
the era of generative AI.

[49:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2955s) And when you're dealing
with finite resources

[49:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2958s) and expensive ones like GPUs,

[49:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2960s) with Ethos, we were able to
nail our cost efficiency targets

[49:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2963s) early this year.

[49:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2965s) Finally, building Ethos in
our internal Adobe platform

[49:30](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2970s) has made developers much happier

[49:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2973s) because all they care about is,

[49:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2975s) "How do I get to production
as quickly as possible?"

[49:39](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2979s) And so if you have happy
developers, what does that mean?

[49:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2982s) It means that they're more
productive developers,

[49:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2985s) which means you're gonna
have happier customers.

[49:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2989s) Thanks for listening.

[49:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2990s) Let me hand it back to Nirmal.

[49:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2991s) He'll take us home.

[49:55](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2995s) - Thank you.
(audience claps)

[49:59](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=2999s) Alright, so you've learned,

[50:02](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3002s) you've seen why building a
platform on EKS is important

[50:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3005s) and helps you build a
trustable and scalable system

[50:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3011s) to adapt to ever-changing needs,

[50:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3014s) but you don't need to do it yourself.

[50:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3017s) Check out CNOE.

[50:18](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3018s) CNOE is our cloud native
operations excellence,

[50:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3021s) open source, open community.

[50:23](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3023s) It's...

[50:25](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3025s) We talk to a lot of customers

[50:27](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3027s) and customers like Adobe
got together and they said,

[50:31](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3031s) instead of all of us trying to figure out,

[50:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3033s) out of the CNCF landscape,

[50:35](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3035s) which tool we want for observability,

[50:38](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3038s) which one we want for deployments,

[50:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3040s) let's just create an
opinionated architecture

[50:44](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3044s) and then build the tools,

[50:46](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3046s) an open source tool,

[50:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3047s) to be able to deploy these
platforms with these opinions.

[50:49](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3049s) So that's what CNOE is.

[50:51](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3051s) Check it out.

[50:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3052s) You can leverage it and
accelerate your platform today.

[50:57](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3057s) So how do we build attractive platforms?

[51:03](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3063s) Focus on trust,

[51:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3065s) increase transparency,
collaboration, and empathy

[51:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3069s) through reliability.

[51:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3071s) Consider your platform as a product

[51:14](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3074s) that's continuously evolving.

[51:17](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3077s) Survey, interview your developers,

[51:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3079s) interview the people

[51:20](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3080s) that you think should
be using your platform

[51:22](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3082s) and ask them why they're not coming to it.

[51:26](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3086s) Abstract the complexity

[51:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3088s) through the controllers
on EKS or Kubernetes

[51:32](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3092s) and extend your community
beyond just your organization

[51:37](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3097s) to include developers, other stakeholders,

[51:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3100s) AWS, and the open source community.

[51:42](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3102s) You're not alone.

[51:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3105s) Thanks for coming to our session today.

[51:47](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3107s) Here's some other sessions
that are going on in the track,

[51:50](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3110s) the Kubernetes track, that are related.

[51:52](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3112s) Some of them have already occurred

[51:53](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3113s) and the videos will be on
YouTube if they're breakouts.

[51:56](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3116s) Check out the CNOE workshop
on Thursday, tomorrow,

[52:00](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3120s) if you want to get hands on
on building an IDP using CNOE.

[52:05](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3125s) And there was some new
announcements with new features

[52:09](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3129s) at KUB201.

[52:11](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3131s) So you want to check out that talk

[52:12](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3132s) on some of the new features
that we're launching

[52:15](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3135s) in Kubernetes and where
we're going with EKS.

[52:19](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3139s) Check out the EKS training.

[52:21](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3141s) So if you're new to
Kubernetes, new to EKS,

[52:24](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3144s) we have a free EKS badge and training.

[52:28](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3148s) And for our session today,
please check out this QR code

[52:33](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3153s) with all the links and resources

[52:36](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3156s) to help you accelerate
your platform building.

[52:40](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3160s) Happy platforming

[52:41](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3161s) and I hope y'all had a good time.

[52:45](https://www.youtube.com/watch?v=WkPrmHKZsq4&t=3165s) (Nirmal chuckles)
(audience claps)

