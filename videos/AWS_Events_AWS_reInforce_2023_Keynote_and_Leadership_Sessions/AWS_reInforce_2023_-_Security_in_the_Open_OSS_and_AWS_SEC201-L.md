# AWS re:Inforce 2023 - Security in the Open: OSS and AWS (SEC201-L)

[Video Link](https://www.youtube.com/watch?v=kMY8gGmWfAI)

## Description

Open source software (OSS) provides many foundational elements of the AWS Cloud and in the modern IT world. AWS is committed to raising standards for open source security by developing key security-related technologies with community support and by contributing code, resources, and talent to the broader open source ecosystem. 

In this session, Mark Ryland, Director, Office of the CISO, AWS, and David Nalley, Director, Open Source Strategy & Marketing, AWS, assess the latest AWS work in OSS, including the open development of critical security-related technologies such as AWS libcrypto, s2n, post-quantum crypto, Amazon Corretto, Firecracker, and Bottlerocket. You will discover what AWS teams are doing to improve the security of the upstream OSS supply chain through contributions to the Open Source Security Foundation (OpenSSF) and more.

Learn more about AWS re:Inforce at https://go.aws/3N9286k.

Subscribe: 
More AWS videos - http://bit.ly/2O3zS75 
More AWS events videos - http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers — including the fastest-growing startups, largest enterprises, and leading government agencies — are using AWS to lower costs, become more agile, and innovate faster.

#reInforce2023 #CloudSecurity #AWS #AmazonWebServices #CloudComputing

## Transcript

The past 12 to 18 months, like, no point in my previous
20 years involvement in open source
has really driven home just how pervasive and ubiquitous
open source has become. Open source is truly everywhere. And I know that it's in my watches. I know that it's in the cars
that I drive. It's the washing machine
in my house, and of course all over the software
on the computers that we operate. I've known that, frankly,
for 20 years. I knew that open source
was everywhere, that it was important. And of course, open source
is important to AWS. We build tools atop it. We build services atop it. Our customers love it. And so we've got a vested
interest in the broader security of open source in
the landscape that we operate in. But as I said, the past 12
to 18 months have been really
a huge change in people recognizing just
how ubiquitous it is. And so Synopsis, who provide
the Black Duck software composition analysis tool, they're telling us
that 96% of codebases that they see contain open source. 96%. I've always known that open source
has been ubiquitous, but 96%? So I want to spend some time
talking about open source, how AWS thinks about it. I want to say that it's not
just important, but talk a little bit about
why it's important and how we engage
in open source communities. I think the why is important, because it probably applies
to most companies, and I want to explain
our commitment and our strategy. AWS has this long history
of benefiting from open source. AWS would not look like it
does today without open source. If you'll remember EC2, it was
built atop the Xen hypervisor. S3 was originally built
atop Apache Tomcat. They were the foundational layers
that allowed us to innovate quickly and deliver value
to our customers. And we think that open source
is much better in terms of being able to provide
those foundational layers that allow us to innovate
and deliver value. No one wants to reinvent the wheel
and write another web server. We have a number of very good
open source web servers that allow us to not have to spend
the time to re-implement that. Of course, that means that we
need to have a very healthy, a very sustainable open source
foundation to build atop. And healthy means a couple
of different things, right? We obviously, we want secure code. We want well tested code
that operates well. We also want the communities
that are building that code to be sustainable
and to be healthy. We don't want the one person
in Nebraska holding up the entire Internet. And so when we look at--when
we're looking at how we pay attention
to open source, we recognize that it's important
to our business, it's important to our builders, and we build, obviously,
plenty of things on top of it. But it's not just important to AWS. It's important to our customers. Many of our customers tell us
that they have open source first mandates in their business. Meaning that when they're choosing
a new technology platform, that they are defaulting to
open source if one is available. And so with customers repeatedly
choosing open source, asking us to help
with their open source workloads, and whether that's
a database server, whether it's AIML platforms
or container orchestration engines, we have to make sure
that those workloads run really well on top of AWS
and for our customers in general. Open source also
is important to the world. It has become a common foundation
that we're all dependent upon, which means that we have
somewhat of a shared destiny, because we're all
depending upon open source, because open source
is ubiquitous. We have a lot of conversations. Mark and I get to speak
to customers frequently, and customers
are continuously asking us, “Tell us how you think
about open source. How are you securing
your supply chain?” We're having lots of software supply
chain security conversations today, and that really comes down
to two questions. The first is how are you
consuming open source safely? What constraints are you
putting in to make sure that open source is being consumed
in a responsible manner? And then also, how are you
taking care of the software development process to ensure that all of these things
that you're ingesting are secure? And people are lumping
both of those things into our software supply
chain security conversations. And so we want to talk a little bit
about that as well and show you some of the things
that AWS is doing, may not be a perfect fit
for other folks, but at least it'll be
very transparent in how we handle open source
and how we think about that process. Mark, do you want to talk about
some of those conversations? Yeah, good morning, everyone.
It's great to be here. This presentation is very broadly about how AWS works
with the open source community to make it stronger,
healthier and more secure. But we thought it would make sense
to at least briefly talk about how we consume open source
and that conversation, although a brief part
of this overall talk, we could do a whole hour
just on this topic, will at least give you some thoughts
about both how we operate, but thoughts about
how you as well could operate. There's not one perfect way
to do this, but we think we have some
learnings we'd like to share. So just briefly, in terms of
secure consumption, we very much take a federated
approach to this topic, as we do with many other topics. We don't highly centralize
really anything at AWS, but we still have central teams
that support certain core functions to make sure that the teams
that have sort of direct or immediate responsibility
are doing their job well. And for us, open source consumption
begins in the engineering teams that need--that decide
to use open source. So the consumers of open source
take that core responsibility for the software artifacts
they're using, whether they develop them themselves or whether they import something
from the outside world, it's their responsibility to do that
in a safe, sane and secure fashion, with the support of a bunch
of other teams. But still, the core responsibility
exists in that initial consumer. And in order to make sure that we
have ownership of these artifacts once they're brought in, we place that responsibility on sort
of that initial consuming team. They can hand it off later,
perhaps, if that makes sense. But some team has to really own
the health and maintenance of that
core library or what have you, and that's the builder team. They need a lot of support
to do that well, and that's where
our Builder Experience team, which is a central team, comes in. This is the team that runs
the core code repositories, build servers, build pipelines, as well as all
the deployment capabilities and a lot of centralized testing
that runs on every single code check in everything from unit tests
and so forth. But security tests and code scans,
static code analysis, software composition analysis, all these tools are run
in a central service fashion by the builder experience team. So that means that any other
organization that wants to use this open,
say, an open source library, the first thing they're going to do is they're going to look to see,
“Hey, is anybody else using this?” Just like they would want to reuse
code that's internal only, they're going to want to reuse
open source code as well, because that means someone's taken
initial responsibility for vetting, maintaining and updating that system. And so this is where that
other team would go, would go to the central code
repository and tools, find that capability or that library or that source code and progress
from there, again, with that sort of federated
ownership and control. And then finally,
we have a security team, a central security engineering team,
especially on the proactive, what we call proactive security
or Apse, which does run a lot of the central
tooling to make sure that we're, again, using and consuming
and deploying systems and code in a very safe fashion
across the board, including the open source components. And so the Central Security
engineering team not only runs a lot
of the security checks in that central builder environment and maintains both proprietary
and third party and open source security
scanning tools and so forth. They run, for example,
this is a little off the topic, but a canary service. So when you write your code,
you also write security and variant types of checks,
which then the security team has a service which runs
those constantly to make sure that certain security invariants
of your service in production are constantly
doing the right thing, returning the right result,
the expected result from any call, typically around authorization, but lots of other security invariants
that you want to maintain. You build essentially tests
that run constantly against
the production environment. Kind of helping hold this
all together is our open source
program office. They provide kind of
the general interface to sort of the correct
and proper and healthy interaction with the outside world,
along with David's team as well. They're the ones that are doing
things like making sure that we have good relationships
with the right outside builders, sponsoring and funding things
that make sense. We'll talk more about security
related funding later in the talk, and in general, creating
that healthy interface between AWS and the broader
open source community to make sure
those lines of communication, those relationships are there
to support the overall health of this of this environment, and again, using open source
in a secure fashion. And we'll talk in a minute
about working upstream. So another aspect of all of this
is if we do see need to make changes or improvements
or security fixes or what have you, a key part of what
we're going to be doing is making sure that those
get pushed upstream as well. So, after a little detour,
if you will, although a very important one
on consumption, we'll go back to sort of how we think about--how we interact with
the broader world in open source. And we'll focus on these
three pillars: work upstream. That means when you're working
with something where you're not the kind
of primary creator, make sure that you are interacting
with that original source in a way that is responsible and contributing
to the common good there. Release tools, and effectively
this is be the upstream in many cases when you have things that the rest
of the community can benefit from, put them out there
so others can benefit. And then we'll talk also
about financial support as well. We'll start with the work upstream. So if we think if we take this
kind of long term and community oriented approach to working in
the open source world, we can benefit not only ourselves
but the broader community. And we've been doing this
for a long time and increasingly more
and more over the years. I'll dive into a few of these. We'll dive into a few of these
examples in more detail, but just to cover a few in a more
kind of quick and anecdotal way, I want to call out Xen project. This was, as David mentioned, EC2, one of our first
and most foundational services originally launched
on the Xen hypervisor. This is back in the days when
Intel processors didn't have support
for hardware virtualization, and people may remember some funky
things that were done in those days. Xen was really pioneering with
this notion of Paravirtualization. Raise your hand if you
remember Paravirtualization. It's kind of dead, and it needs to be
dead, because it had some issues. But it did an amazing job, and we worked very closely
in that world of Xen to make sure that we were deeply
involved with improvements, patches and so forth. Now we've been gradually
deprecating our use of Xen, as probably many of you know, and moving to KVM based,
the nitro hypervisor. We're still active
in the Xen community, and one of the last kind of
major contributions we made to Xen was in the spectrum meltdown era, when we realized that a lot of
shared state at the processor level could lead to certain kinds
of side channel issues. And Paravirtualization,
in particular, was very problematic in that regard. It was very problematic that
the kind of shared state between the kernels and drivers
in the paravirtualized instances, that you could have problems
of the type that are manifested
in Specter meltdown. So we actually created
an internal technology to create a kind of shim layer, so that the operating system
that's being hypervised thinks
it's being paravirtualized, but actually there's an HVM
hardware virtualization layer sort of under the covers. So you're essentially creating
a sort of fake copy of some Xen internals
on the VM side and then actual HVM capability
between the guest and the hypervisor. This is a technology we call Vixen,
and we did push this upstream, and so now any consumer
of--it was modified slightly, but it did become
kind of the standard now, so that Xen users
can run old-fashioned, never updated operating systems
that expect Paravirtualization, but actually are using
harbor primitives to do that. There's many other great
examples here before we get into
some of these others. The one other one I want to call out
very recently in the KVM world, those of you who are familiar
with operating system and hypervisor security,
you might be familiar with something that Microsoft calls
virtualization based security. So for the Windows operating system
and the Hyper-V hypervisor, they've developed some technology that they can sort of
take parts of Windows and run it in a separate--kind of
like a separate VM. It's not exactly a separate VM, but it's a hypervisor
protected memory space, and that is designed to protect
against certain kinds of cross process attacks,
essentially, that might cause trouble with the things like the local
security authority in Windows LSA, which maintains all of your passwords
and clear text in memory, for example. Now the problem is that that's
a proprietary Microsoft technology. They released some information
about how they did that, but it's definitely not open source. We developed a VBS capability
for KVM, which we just recently
started pushing upstream. So anyone who uses the Linux--is
in the Linux ecosystem, using the KVM hypervisor, will be able to run these sort
of advanced and proprietary Windows features and do that
on an open source basis. So we're very excited about that. Let's move on to some specifics here,
and we'll start with OpenJDK. So we've had a long history
with Java. We're a big Java shop. Continue to be. And back now, five years ago,
2017 timeframe, began to see a future in which we really felt the need to take a lot more ownership
for Java and our use of Java. And in the 2017,
2018 time frame realized we're not the only large enterprise that is a little bit concerned
about the future of OpenJDK. There was a change of ownership,
as you may recall, in the industry. I won't name any names,
of the Java environment, and there was a general concern that the open version might need
some additional love and care and really become more
of a full community effort. So we joined in that effort. We created our own Java distribution,
we call Corretto, and since then we've really invested
heavily in the OpenJDK world, and we release our Corretto capabilities
and runtime to the world for free. You're welcome to use it. It's fully supported by
our support organization and by our engineering processes. I won't go through all the different
things on the timeline for the sake of time. You can download the slides,
but basically it's just the point we're making is that we've decided
to really help the community jointly own the destiny
and the quality and the features
of OpenJDK going forward and making some very,
very deep investments in that. And I'll hand off to David
for some more topics. I just want to call out Corretto has done amazing things
for our customers and for the users. Specifically, we just saw New Relic
tell us that Corretto is the most
widely consumed OpenJDK distribution,
which is mind boggling, but it tells me that customers
are actually finding value in what we're providing. So I'm super excited about that. But I'm a little more excited
about Rust. And how many folks know what Rust is? Okay, so Rust is a new programming
language, and I say new, it's been around-- David, does the world need
another programming language? The answer is— Yes, and more security tools. Yes, it actually does. And he'll explain why. So Rust is a new programming language,
and I use the term new relatively. It's certainly newer than C and Java, and it has come about offering
the performance of C, but with a number
of additional assurances. So the biggest value from a security
perspective that we see with Rust is thread safety
and memory safety. And we're going to talk a little more
about memory safety in a little while. But when we were looking at
operating things at scale, Mark said we're a large Java shop, and we started paying attention
to Rust in 2017. In 2018, we shipped Firecracker,
which was written primarily in Rust, and that is an open source
operating system that's really permitting
serverless technology. So if you're running AWS Lambda,
Firecracker is there, we've released that as an open source
project for people to consume. And that was the first visible notice
that we gave the world that we were
paying attention to Rust. We had been using it for some
internal things already prior to that. More recently, we launched a new
Linux distribution called Bottlerocket, and Bottlerocket is heavily
Rust language focused and is designed to provide
a really thin, small security surface
for running containers. And so we've also made
that open source. Folks can download
and make use of that already. In 2019, we announced that we were
sponsoring the Rust Project. In 2020, we started hiring
a number of Rust maintainers, because we recognized that Rust
was going to be important to how AWS was going to develop in the future. So we started building up a team
of folks who were already invested in the Rust programming language, who had already made
substantial contributions and had leadership positions there. Shortly after that, we helped found,
with a number of other stakeholders in the community,
the Rust Foundation. And today, EC2 looks at Rust
as its language of choice for security sensitive applications
such as nitro enclaves. And so we think that that Rust
is incredibly important to what's going to be the future
of a number of different workloads inside AWS. And we're working,
we're heavily working. We've got two teams who are focused
on upstream contributions into the Rust programming language, because we think that there is
so much benefit not just for AWS in how we build our tools
and our services, but for the rest of the world, because we get into things
like memory safety. But Mark and I, we just talked
about programming languages, and I won't talk about a third, because maybe the world does finally
have enough programming languages. I want to talk a little further up
the stack with Kubernetes. And Kubernetes is really
a workload orchestration that the primary workload
is containers, and it has become
incredibly successful. And it's become successful
by a number of different measures, the number of people contributing. There are literally thousands
of people who work on every
single release of Kubernetes. The number of workloads that now
assume that Kubernetes is going to be the underlying layer
that they're operating on. And I can't tell you the number
of new tools that I look at that presuppose
that they're going to be operating in a Kubernetes environment. We obviously recognized this
when our customers were telling us that Kubernetes was important. We have the EKS service and
obviously provide managed Kubernetes. But we recognized a need really early
on that we needed
to get involved in Kubernetes and the rest of that Cloud Native
Computing Foundation arena. And so we've been getting involved
in places like Container D, etcd, Nerd Cuddle,
all of the surrounding technologies that help make Kubernetes
so useful and so helpful, because Kubernetes
is not just one thing. It's essentially using a driver
model, allowing people to plug
in different things, like different network controllers,
different scheduling technology. And that is one of the reasons
that it's been so successful is that ability to plug in things. But that means lots of help
is needed on the outside. So etcd, Container D, etcetera, are contributing technologies
to that success. And we have heavily invested there, taken leadership positions
in technical steering committees, in the governing board
and a number of other places. And also released some of our own
tooling, where we recognized gaps that
our customers are pointing out to us. So Carpenter was recently
released recently, a year ago, was recently shown and provides
a lot of value for our customers in trying to scale things
on Kubernetes. But we also recognize that Kubernetes
does not exist on code contributions alone. So we've done a couple
of other things. One is, despite how popular
Kubernetes is and how fast it's innovating, that's creating some upgrade
fatigue with customers. And so they don't want to upgrade
every six months. They've asked us for help, and we,
along with others in the community, are working on figuring out
a longer support time frame for that, because customers want to be able
to actually operate something, not just be
in an infinite upgrade loop. We're also, though, realizing that
there needs to be infrastructure to actually test Kubernetes
in advance. And so we committed millions
of dollars in cloud credits every year for continuous integration
for the types of testing that ensure that when you deploy
a new version of Kubernetes, that hopefully it will be pain free. We've been doing that,
as well as helping with their release infrastructure now and getting involved there
to make sure that, you know, again, the project does not sustain
itself on code alone. But that's not the only thing
we should be doing, right? We talked a little bit
about adding features. Mark talked about adding features
to KVM, improving security on Xen,
and that's important. And I think that AWS has an
obligation or responsibility to release the security
improvements that it has. And, Mark, do you want to start
talking about that? Yeah. So in many ways,
again, as a shortcut, you could say work upstream
is one thing. Be upstream is another thing. Of course there's an overlap
and a dynamic quality to that. But in this case, what we're saying is we have developed technology
from scratch that we realize is very useful
for--I say from scratch. I'm sure there's open source
libraries inside of those, but basically significant
major projects that we then want to release
to allow others to benefit from, even when they're not using our
cloud platform or any of our tools. And so we want to talk about a few
of those in this session as well. We'll dive into, I think,
three of those, but I'll call out a few that don't have their own separate
slides in this overview slide. So a launch from August of last year, Open Cybersecurity Schema
framework, OCSF. This is actually a set
of supporting open source tools, but the core release
is actually of a standard which allows security tools
to interoperate in a much more seamless way. When we would talk to customers and working with a lot of partners
in the security space, what we heard over and over again
was my security teams spend too much time
on data munging and data cleansing. They're doing this kind of
repetitive stuff. They're writing tools
or they're doing manual things. They're cutting and pasting between
multiple open windows on a screen. Just crazy stuff to try to get
security tools to actually work together and to do that basic kind of function
you need to do often, which is I need to do sort of a join
across two data sets. And it was often very, very hard,
if not impossible. So what we realized was
if we could create a standard for how tools communicate with one another,
there'd be a huge benefit to that. So now we launched this last August
actually at Blackhat with about 20 other partners
all signing up to support OCSF. Now I think there's up to 60
or 70 companies who are all committed
to either emitting or consuming OCSF records
from their security products. And that will make it much easier
going forward for security teams to manage the data that's flowing
in and out of these tools. We also use the OCSF format
as the native format of the Security Lake product that we just launched
I think a week ago and was in the keynote yesterday. So any tool that can emit OCSF
can natively feed their data into our security lake. And that was not an accident,
by the way, that we worked on both a standard and a service together
that supports the standard. So that's a really, I think, a really
interesting and impactful one. David already mentioned Bottlerocket. Bottlerocket you can think
of as a secure Linux distribution
focused on container security. So for example, it has a read
only file system. There's no reason why file systems
need to be updated at the OS level, if the only thing it's doing
is running containers that are running virtualized
file systems on top. So and it has many other such attributes
of very locked down, very secure Linux foundation for running
container environments. Firecracker we already mentioned. Firecracker implements a technology
that are called microVMs. So again, we don't trust container
boundaries as a security boundary. In general, there's very bad track
record of containers being fully secure in terms of the ability
to escape from a container. They really weren't designed
for that, so there's no blame there. So we strongly believe in using
harbor based virtualization whenever you have
a multi-tenanted or any workload where you need strong isolation. The problem is that VMs typically,
a typical virtual machine takes a while to boot: seconds, maybe a minute,
because they're big and complicated. So Firecracker implements
a microVM technology in which a full KVM virtual machine
can be booted and executing user space code
in less than one eighth of a second. So 125 milliseconds is
the design goal for Firecracker. We've met that consistently
over time, and that means
that you can now launch VMs as quick as you can launch
a container essentially or close enough
that you can use that as a very foundational
property of your container based or function
as a service workload. So we use Firecracker underneath Lambda
and underneath our Fargate service, but we also release it to the world. And there's a lot of other vendors
now who use Firecracker in their container
runtime environments, and we're really excited
for the success of that. I think you were going to call one
of these out before I move on. Yeah, I’ve got a favorite. I do have a favorite on this slide,
and it's trusted language extensions. So PostgreSQL, the open source
database, has a wonderfully vibrant
extension community, and that allows Postgres to change
from a relational database to a vector database to something
focused on geospatial and a host of other things. There are literally hundreds
of extensions to PostgreSQL, the database itself. And we recognized
from some of our own pain, and while it didn't directly
impact our customers because of defense in depth,
we saw that a number of folks were calling out the extension space
as an attack surface that would allow them to do nefarious
things to PostgreSQL databases, true in hosted environments
as well as self-managed. And so we created trusted
language extensions and released that as open source. We did that at re:Invent last year. And I'm excited about this, because not only does it
solve a problem for us, and we could have
just solved that problem, but we released this
because we recognized that everyone should have a more
secure and a more safe PostgreSQL. So the trusted language extensions are probably my favorite
thing on this slide, because it's something that
we've seen a significant problem, identified that problem, and then worked to not just
shut down the specific issues, but to create a safer environment
to run those extensions in. I'm super excited. I'm really excited by seeing how many people are adopting
trusted language extensions as the environment in PostgreSQL
that have nothing to do with AWS. That's awesome. That's a great story. So we'll dive into a couple of these. Open quantum safe
is called out here, OQS, and we'll talk about that
in the context of S2 and some other crypto stuff. And then Cedar and maybe I think
we have one other example here in terms of our decision
to work in the open with core technologies
that we develop. So you can imagine you run a cloud
platform, encryption super important. It's one of the fundamental
properties of data isolation, data security that customers rely on,
that we rely on. So you really want to be constantly
on the cutting edge of cryptography and of encryption technologies
across the board. Customers, obviously, they're running
applications on top of our stack. They want super-efficient systems with minimum CPU
and memory utilization, but they want state
of the art technology underneath. So we've been on a journey now
for a number of years to develop technology in this space and to open source
the technology we develop, because we believe it can benefit
the broader community. I'll start with s2n. s2n was one of our first forays
into this general space. It originally stood
for signal to noise. I'm not sure if we even spell
that out anymore, we call it s2n. But you can think of s2n
as a very stripped down, very minimalistic,
very feature poor, intentionally, implementation of the TLS protocol. Feature poor meaning that TLS
has a ton of features that most people never use, and but to implement those features
takes a lot of code and therefore introduces
the possibility of more bugs. The wakeup call for us and I think
for a lot of people in the industry was the Heartbleed zero day. Remember the Heartbleed one? Raise your hand if you had a bad day
on the Heartbleed day. We did, too, although we were able
to patch a massive global fleet of load
balancers in less than 24 hours, we still had literally
hundreds of thousands of hosts that had to be patched
in our ELB service. But that was a wakeup call,
because we looked at like, okay, what's the root cause here? Well, it's a bug in OpenSSL. And okay, software has bugs,
but it was a pretty painful one. But what about OpenSSL? Oh, it's 300,000 lines of C code. It's old, it's Crufty. It's got--I mean, God bless
the community for keeping it up. And we now we've been financially
supporting them ever since, and it's done a ton of good
for the industry, but it's not what we felt
really good about in terms of relying on
as a core technology for very fundamental security
properties of our cloud. So since then we've been kind of
on a journey to both implement a replacement
and substitute that in and use it as well
as release that to the world. s2n was one of the first steps there. So it's, again, just implements
the TLS part of the protocol, still uses OpenSSL
for the cryptography parts of the handshake and the encryption. That was some years ago. s2n is an interesting example too,
because this was before Rust was kind of up and running
and popular, so it's written in C. However, it's written
in a very strange and idiomatic C that looks just like Rust, because you can't do
any direct memory access. It requires all these kind
of indirections. And we have formal tests and proofs
that show that if any developer does a check in that's not using
the proper memory handling functions that are inside of s2n, sorry,
your code will get rejected. So still using the C language,
but using it in a very carefully crafted and memory safe fashion. A couple of other really
interesting facts about s2n. First of all, it's a project
that had, I think at the start, maybe a little bit more now,
about 20,000 lines of code, 80,000 lines of tests. So it's a very, very test centric,
test heavy project. And it was the first test,
first release to the wild, as far as I know, at least of any significant
piece of code, in which formal verification
was part of the build and the test and release process. So all the people we hire, and you've probably heard
in many talks from AWS, a group we call the Automated
Reasoning team or these formal verification
capabilities, a branch of computer science
that has been a bit obscure. It's been around for a long time. It's not obscure anymore,
at least as far as we're concerned. We're using more and more we're using
the tools and techniques of formal verification
to prove the correctness of code. In s2n, if you go to
the GitHub repository and you look at the build instructions
and you download and try to build it, you're going to actually download
a bunch of formal proofs about the correctness
of various parts of that code. Again, it doesn't mean the code
is bug free necessarily, but it's a much higher standard than
we've traditionally done for a lot of these systems. So that was a big and important foray
into this space, but we didn't want to stop there. So subsequently we've also
open sourced our own libcrypto, so now we're giving you
an open source reimplementation of the core cryptographic primitives
you need for your network, as well as other use cases that are traditionally done
in the OpenSSL library. I won't go on and on about libcrypto,
but it's out there. One of the key things we're doing
with libcrypto is we're taking on the burden
of FIPS validation. That's one of the kind of things that people often expect
of their cryptographic libraries. They want that third
party validation. And interestingly,
even around the world, we still hear people are very happy
with FIPS validation, even though it's technically
a US government standard. And but it's hard for an open source
team to do that. It's expensive, it's time consuming,
it's frustrating, it takes a long time. It's almost you almost kind of
require commercial interest and commercial commitment to really
kind of go through the trouble, which many companies do. But we're doing that on behalf
of the open source users of s2n and of libcrypto We're taking that that through
FIPS validation, and we'll keep that up to date
as time goes on, which is kind of the hard part. Often you get it through and then you
kind of like relax and move on, and then your code gets out of date. And so you get into this bad cycle. So we're doing that with libcrypto. And the final thing I want to call
out that's just briefly referenced in this slide, and we could spend
a whole hour on it is Post-quantum cryptography. So we've made a lot of investments
in PQC. Again, the nutshell version,
which I'm sure most of you know is nobody has a sufficiently coherent
quantum computer today to crack asymmetric cryptography. But all the experts say
that if we can invent one, and we don't usually like to bet
against engineering teams, once problems go from theory
to engineering, the engineers are often very good
at succeeding at very hard problems. And so it's not unlikely that in
the future, not too distant future, there will be a sufficiently
powerful quantum computer that could crack today's
asymmetric cryptography. Now, the good news is often
not mentioned, which is symmetric cryptography does not suffer much
from quantum computers. So if you're using AS256
for encrypting something that you write
to disk as EBS and S3 and Dynamo and all our storage services do, quantum computers would speed up
brute forcing of that, cracking that crypto by a factor
of 100, 1,000, doesn't matter. So much power is required to crack
those that that's essentially irrelevant, at least as far as we know,
according to today's experts. But asymmetric cryptography,
totally different. It's much, much--very susceptible
to being cracked by a quantum computer
using brute force techniques. And therefore, we have to get ahead
of this problem before it becomes a problem. So we've made a lot of investments
in post-quantum cryptography. We have production systems today
in production using hybrid key exchange, which means that it encrypts
the inner keys of a TLS session with both elliptic curve
and post-quantum so that if one is cracked
or the other, you still have
basically defense in depth. So a lot of really interesting
technology going on there. But again, the key thing is
we're doing this in the open, so that anyone can benefit
from all the investments and the work
that we're doing in this space. Speaking of formal verification, and because that's one of the key sub
themes of this open source release, which we just made a month or so ago, we've introduced to the world
a new--another new language. Hey, we need new languages. We really felt we did need
a new language in this case. We looked long and hard
at existing authorization languages. So this is a kind of a narrow
but very important part of the security world is how do I encode permissions
about access to systems? If I could step back for those of you
who, like me, have worked in sort of identity
and access management over the years, as an industry, we've done a pretty
good job on the identity side, right? We have a pretty good story
about SAML and OIDC and blah, blah, blah. That allows me to come across into
a system with some sort of validated, cryptographically validated user
with a set of claims. Okay, now I show up at a system. Now what happens? Somebody has to make
an authorization decision, like what rights does
that person have in the system that they're accessing? There the industry has done
a terrible job of standardization. We tried years ago with something
called XACML, if you know what that is, boy, we could go have a cup of coffee
and talk about that. Failed miserably. And if you think about today's
IT systems, on premises especially, you have these
ACL models everywhere SharePoint ACLs, Exchange,
different file systems, everything has
an access control model that's all completely disjoint,
completely heterogeneous, and it's not a good story
in terms of wanting to understand and answer those basic questions. Who has access to what? Like that is the holy grail
of access management systems? Who has access to what? Today, super hard to answer
that question. It's easier in the cloud, by the way, because you have a common identity
management system for all the APIs. Still not super easy to answer,
and we're getting there, but at least there's a possibility, because of the unification
on the access side. But long digression, but we decided
that our existing IAM system works great,
but was it the right language to expose for a broader
set of use cases? We decided not. I can go into lots
of great details why not. We looked at existing open source
or standards technologies. They didn't really meet
the requirements, so we invented
a new one called Cedar. And one of the many great things
about Cedar, which I won't go into, but one of the most
interesting things is it was built
by a joint engineering team that included both experts
in access management, but also formal
verification scientists who built both the language
for formal verification as well as the implementation,
the runtime and the libraries. Those are also formally verified, because you really want correctness
when it comes to access decisions. So this is a really cool technology, and there's some
great blogs on Cedar, if you want to dig
into the gory details. It includes another technology
called differential testing, which is a very interesting
sort of probabilistic fuzzing, if you will, because even
with formal verification, you still want to do
some testing to make sure that your tools
are all working properly. So enough on Cedar, but it's
a very exciting release, and we hope the world adopts this
and uses it everywhere because even though there'll
still be some challenges in terms of unification, having a common access language
would be a huge win, and we're working hard
to make that true. Yeah. You know, Mark,
I was one of the naysayers who said that there was
no need for Cedar, because we have other
access languages out there. And when this project
came up internally, I was one of the folks who said,
“Why are we reinventing the wheel? This doesn't make sense.” But the formal verification
of both the engine, the access engine,
and the policy itself really sold me that this was something new
that actually needed to exist. I'm excited about Cedar. I'm excited about the attention
that it's getting as well, because people seem
genuinely excited about this, and those people
are not even AWS customers. They're recognizing that this is
a gap that we have
in the security space. So I want to talk a little bit
about Snapchange, which was another open source
release we made last month. And Snapchange came out of a team
inside AWS called Find and Fix
or our F2 team. And to explain a little bit
about what F2 does, the F2 team has a mandate
that they are to go look at what AWS and our customers
are using the most and then to audit it
to find problems, specifically security problems
in the most commonly used open source tools that AWS
and our customers make use of. And they've been on this journey
for roughly a year now. They've built up a team
of security researchers, and they're trying to figure out
how to scale up their capacity to find problems,
and Snapchange is a fuzzing tool, and fuzzing essentially
tosses a bunch of strange inputs into various break points
in a piece of software. And frankly, fuzzing as a
general tool has been responsible
for finding lots of problems. And they looked around, they're using plenty of
fuzzing tools as it is today. But when they looked, they said there
are some things that we can improve. Specifically, Snapchange is a tool
that works in an emulator or a hypervisor environment. It presumes that the software
is actually going to be running as a virtual machine, and it is able to inject
the fuzzing via that layer. And so I said, “Why are you
doing this? There are already tools
that do this.” And one of the call outs was,
well, those tools today require a modified KVM
and/or a modified kernel. So you've got to load a specific
kernel module that does not ship in tree. And that's a barrier to some folks for being able to easily deploy this,
being able to run it at scale. The other thing that they wanted
to do is they wanted to scale this across
multiple cores and so multiple CPUs at a single time and run that
allowing folks to hopefully scale up and make their fuzzing
activities a little faster. So Snapchange allows folks
to basically use breakpoints in code and submit all of this fuzzing data
into the program and to replay that,
and so dramatically more scalable and hopefully faster
for folks to use. This is really targeted at
the security researcher audience. This is not something that we
would expect an average developer to go make use of. We're excited about it, because
the security community seems to be finding this useful. And I'm really excited that this team is getting a little
bit of visibility, because they're doing amazing things
in terms of finding bugs, because their mandate
is both to find and to fix. They're not just looking at bugs
that they're finding in code and saying, “Hey, here's
a security vulnerability.” They're developing proof of concept. They're developing a patch
and shipping that to minimize the workload
on the open source maintainer, because we don't want
to stand up a team that basically creates
a denial of service, a social denial of service attack
on open source maintainers. So we want to provide them as much
help as possible when we're going out and
looking for security vulnerabilities. I'm going to interrupt you
for a second. Go slightly off script, because
I think this is super important. It’s something I learned from you
when I first started getting involved
more in open source security. So, by the way,
David is the president of the Apache Foundation
in his spare time. And very, very long and deep
involvement in open source community. And I remember when we first started
talking about these kind of security audits
and so forth, you sent me this postmortem
of a security audit that was done
on some Apache software. And it was so enlightening,
because what it made me realize is you can go in
and you can find bugs. There's no problem finding bugs
in large software code bases. Now what? Bugs.
Okay, great. Now what do I do? Where's the resources that are
needed to fix the bugs? That's a whole different thing. And it's also very hard to inject
those resources, even if they exist,
into an existing development team, an existing culture, an existing way
of building and developing software. So I found that super enlightening. And it was also kind of
an eye opener. Like it's not a matter
of finding bugs, it's a matter of creating this
virtuous cycle of finding things, but also developing the skills,
the capability of the community that owns the software,
prioritizing those fixes. All those things are a much harder
problem than just finding things. And I think that's a super important
story around how we need to, as a community,
get better at doing this stuff. I think that report that
you mentioned was talking about all of the influx of help
that happened after Heartbleed, and I use "help" in air quotes,
right? Because security is not
a one-time thing that you can say, all right, we're secure today
and then walk away. It requires that continuous
investment where you're making long
term investments in not just technology
but in communities and making sure that you can
actually shift the culture, shift the practice
to something more secure. It's not--you're right,
it's not about finding bugs. If it was that easy, we would— We'd be much better today. We would probably not be giving a
talk today on open source security. So. I said this earlier,
but open source projects do not work
on code contributions alone. And we think that AWS, you can see it
in our leadership principles, size and scale
bring great responsibility, and we certainly have
a responsibility to open source. And so we recognize that. And one of the mechanisms
that we can make use of is to support a number of open source
projects and open source foundations. And we do this
across a number of places. So we support places like
the Python Software Foundation, the Apache Software Foundation. We're members of the Linux Foundation
and Cloud Native Computing Foundation and provide a baseline
of support via that mechanism. That provides us a way to make sure that that base level
human infrastructure is in place and that people are able
to get things done. But I want to dive into
how we're thinking about funding
security responsibilities, because I think that is
a separate layer above just funding the open
source projects themselves. So the Python package index,
if you're not familiar with PyPI, it is a— You're not a Python developer
if you're not familiar with it. You aren't.
You aren’t. You know, this is how the world
consumes Python, right? It is the package repository. If you're a Java developer,
there's Maven Central. If you're a Python developer,
there's the Python package index, and it is a huge attack surface
for folks trying to impact
the software security supply chain. And we recognized this early on,
paid attention to it, started working with
the Python Software Foundation and said what can we do together
to improve this? And they said, “Well, you know, today
we're doing mainly reactive response to security issues. We don't really have a great
security strategy for the package repository itself. We're not proactively going out
and looking for threats. We would like to change that.” They put together a proposal
and brought that to Mark and I and said,
“Hey, this is what we'd like to do. Can you fund this?” And we said,
“Absolutely. This makes perfect sense. We'd love to jump in here,” because we consume packages
out of the Python package index. All of our developers
who are doing Python do that. Our customers do as well. And so does the rest of the world. You're not developing in Python
if you're not using this. And so we have been working with them to help create proactive strategies,
build up some internal staffing, so that they can actually
respond to issues timely. And we're not depending upon
volunteers in Nebraska to respond to a security issue
in the Python package. We just have some individual in mind
when you refer to, so we won't mention any names. We won't mention a comic's name,
but we're not responsible. We're not responsible if we're not
taking into account these distribution points and making sure that we are helping
to fund their security, because that impacts all of us. We have that shared destiny
we talked about earlier. We've also--and we've hinted around
at this a little bit earlier, but there's a number of scholarly
articles written by people far smarter
than I that are looking at the overall
timeline of security vulnerabilities. And they're reporting that 65%
of security vulnerabilities in the past decade
are memory related. Two thirds of security
vulnerabilities are from a single class
of security threat. And one of the reasons we are
so interested in Rust is that it provides tooling
to ensure memory safety. That's not a panacea for--Rust
does not make you magically secure. And I don't want to paint
that picture, but it is a much more
assured position from a memory safety perspective, and I'm excited about that for what
we're developing internally, Mark. But we looked at where some of
the entry points in terms of open source was. And I remember us sitting in your
office in Virginia a year ago now almost and talking about the places
where we were seeing attacks and seeing security vulnerabilities
in open source. And, again, security is not a point
in time thing that you can go say, “I'm secure today and I don't
have to worry about it anymore.” And so we looked at
where can we focus on things that are on a network boundary, things that are getting
lots of direct Internet traffic or they're parsing huge files. How do we go address that? And so we identified
four initial projects and asked the Prossimo project
out of the Internet Security Research group to go rewrite those for us. And we provided funding
to rewrite those. So those initial four
are the NTP daemon. We asked for a Rust implementation
of that, sudo and su, because again, increasing
your authorization level is something that you really don't
want to have memory issues in. Rustls— There's a long and sad history
of bugs in that. There are, a lot of memory bugs
specifically in sudo. Rustls, the TLS library for
the Rust programming language, we wanted to improve
how fast Rustls was going to be able
to be production ready. We want to make sure that--Rustls
is already Rust written,
so no inherent rewriting, but we want to mature
that rapidly, because we think
that a TLS implementation that's memory safe
is super important. If your encryption fails,
you've got lots of other problems, and then an AV1 decoder, and AV1 is itself
an open source success story. And we wanted to make sure
that that this decoder that's processing lots of huge files,
both audio, video and images is written well and is secure. So we've been doing--we've been
investing in a lot of that. And finally, the industry
as a whole has coalesced around the Open
Source Security Foundation. And Mark championed
joining OpenSSF years ago, right after it came out. We joined that. We started investing
and spending time there. Folks from Mark’s office
were certainly heavily invested in trying to advance
the state of security in open source. But we recognized that there
was opportunity to do more. And so last year we committed
$10 million towards OpenSSF to make investments
in long term sustainable, open source security initiatives. And we did a couple of those. I'll talk about them real quickly,
Alpha Omega, which has two objectives. The first is paying attention
to the 10,000 most widely used
open source components and creating automation around finding security
vulnerabilities and patching it. So they're really heavily focused
on automating security as much as possible. The other side of Alpha Omega
is focused on the top 100. What can we do that has
outsized impact across the most heavily
consumed open source packages? And how do we make that
security investment sustainable? They're doing great work. We're seeing lots of things
happening there in a number
of different communities where we continue
to be excited about that. Security scorecards, though,
Mark talked about consumption, right? And we at AWS,
we delegate open source consumption decisions to builders. Nobody comes to Mark
asking for permission to use
another programming language, even though he's in
the security organization. Nobody comes to me in
the open source organization saying, “I want to use this thing. Is it okay?” An individual developer
is doing that. And we think security scorecards,
which will provide an automated look at a number of health metrics
and security metrics, provides much greater information
to base decisions upon, so that those developers
who are deciding what open source they're consuming
can make better informed decisions. We're excited about some of the work
coming out of security scorecards and look forward
to that being more ubiquitous. And of course, we're doing a lot
of general support as well. So let's close out our session. And just as a reminder
of our takeaways and our pillars, work upstream and contribute
to the open source world and provide financial support. And for all of these things,
we encourage you, the broader community,
to join with us in these areas. Think about ways in which
your organization can work in one
or two or three of these ways, or come up with new ways
to work to support open source. Join with us. Come to us with ideas. We're very interested if you have
funding ideas, if you have engineering ideas that
you think can help in this world, that's super, super important. We're going to join together
to make the world a safer place, because we all depend
on secure open source. And we thank you very much for coming and have a great rest
of your time here at re:Inforce. -Thank you.
-Thanks. [applause]

## Subtitles with Timestamps

[00:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2s) The past 12 to 18 months, like,

[00:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=5s) no point in my previous
20 years involvement

[00:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=8s) in open source
has really driven home

[00:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=10s) just how pervasive and ubiquitous
open source has become.

[00:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=17s) Open source is truly everywhere.

[00:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=19s) And I know that it's in my watches.

[00:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=22s) I know that it's in the cars
that I drive.

[00:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=26s) It's the washing machine
in my house,

[00:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=28s) and of course all over the software
on the computers that we operate.

[00:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=34s) I've known that, frankly,
for 20 years.

[00:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=36s) I knew that open source
was everywhere,

[00:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=39s) that it was important.

[00:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=40s) And of course, open source
is important to AWS.

[00:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=43s) We build tools atop it.

[00:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=45s) We build services atop it.

[00:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=47s) Our customers love it.

[00:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=48s) And so we've got a vested
interest in the broader security

[00:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=53s) of open source in
the landscape that we operate in.

[01:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=60s) But as I said, the past 12
to 18 months

[01:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=62s) have been really
a huge change in people

[01:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=66s) recognizing just
how ubiquitous it is.

[01:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=70s) And so Synopsis, who provide
the Black Duck

[01:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=74s) software composition analysis tool,

[01:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=77s) they're telling us
that 96% of codebases

[01:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=80s) that they see contain open source.

[01:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=84s) 96%.

[01:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=88s) I've always known that open source
has been ubiquitous, but 96%?

[01:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=95s) So I want to spend some time
talking about open source,

[01:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=101s) how AWS thinks about it.

[01:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=103s) I want to say that it's not
just important,

[01:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=105s) but talk a little bit about
why it's important

[01:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=108s) and how we engage
in open source communities.

[01:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=112s) I think the why is important,

[01:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=113s) because it probably applies
to most companies,

[01:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=116s) and I want to explain
our commitment and our strategy.

[02:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=120s) AWS has this long history
of benefiting from open source.

[02:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=126s) AWS would not look like it
does today without open source.

[02:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=131s) If you'll remember EC2, it was
built atop the Xen hypervisor.

[02:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=137s) S3 was originally built
atop Apache Tomcat.

[02:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=142s) They were the foundational layers
that allowed us to innovate quickly

[02:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=146s) and deliver value
to our customers.

[02:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=149s) And we think that open source
is much better

[02:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=154s) in terms of being able to provide
those foundational layers

[02:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=159s) that allow us to innovate
and deliver value.

[02:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=161s) No one wants to reinvent the wheel
and write another web server.

[02:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=165s) We have a number of very good
open source web servers

[02:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=169s) that allow us to not have to spend
the time to re-implement that.

[02:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=175s) Of course, that means that we
need to have a very healthy,

[03:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=180s) a very sustainable open source
foundation to build atop.

[03:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=185s) And healthy means a couple
of different things, right?

[03:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=189s) We obviously, we want secure code.

[03:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=191s) We want well tested code
that operates well.

[03:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=194s) We also want the communities
that are building that code

[03:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=197s) to be sustainable
and to be healthy.

[03:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=200s) We don't want the one person
in Nebraska

[03:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=203s) holding up the entire Internet.

[03:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=207s) And so when we look at--when
we're looking

[03:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=210s) at how we pay attention
to open source,

[03:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=214s) we recognize that it's important
to our business,

[03:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=217s) it's important to our builders,

[03:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=219s) and we build, obviously,
plenty of things on top of it.

[03:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=225s) But it's not just important to AWS.

[03:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=227s) It's important to our customers.

[03:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=230s) Many of our customers tell us
that they have open source

[03:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=233s) first mandates in their business.

[03:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=238s) Meaning that when they're choosing
a new technology platform,

[04:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=241s) that they are defaulting to
open source if one is available.

[04:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=245s) And so with customers repeatedly
choosing open source,

[04:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=249s) asking us to help
with their open source workloads,

[04:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=253s) and whether that's
a database server,

[04:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=256s) whether it's AIML platforms
or container orchestration engines,

[04:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=263s) we have to make sure
that those workloads run

[04:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=265s) really well on top of AWS
and for our customers in general.

[04:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=272s) Open source also
is important to the world.

[04:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=276s) It has become a common foundation
that we're all dependent upon,

[04:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=281s) which means that we have
somewhat of a shared destiny,

[04:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=285s) because we're all
depending upon open source,

[04:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=288s) because open source
is ubiquitous.

[04:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=292s) We have a lot of conversations.

[04:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=294s) Mark and I get to speak
to customers frequently,

[04:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=297s) and customers
are continuously asking us,

[05:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=302s) “Tell us how you think
about open source.

[05:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=304s) How are you securing
your supply chain?”

[05:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=307s) We're having lots of software supply
chain security conversations today,

[05:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=311s) and that really comes down
to two questions.

[05:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=316s) The first is how are you
consuming open source safely?

[05:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=321s) What constraints are you
putting in to make sure

[05:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=325s) that open source is being consumed
in a responsible manner?

[05:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=329s) And then also, how are you
taking care

[05:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=331s) of the software development process

[05:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=335s) to ensure that all of these things
that you're ingesting are secure?

[05:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=340s) And people are lumping
both of those things

[05:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=344s) into our software supply
chain security conversations.

[05:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=349s) And so we want to talk a little bit
about that as well

[05:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=352s) and show you some of the things
that AWS is doing,

[05:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=356s) may not be a perfect fit
for other folks,

[05:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=358s) but at least it'll be
very transparent

[06:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=360s) in how we handle open source
and how we think about that process.

[06:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=365s) Mark, do you want to talk about
some of those conversations?

[06:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=369s) Yeah, good morning, everyone.
It's great to be here.

[06:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=372s) This presentation is very broadly

[06:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=375s) about how AWS works
with the open source community

[06:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=377s) to make it stronger,
healthier and more secure.

[06:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=380s) But we thought it would make sense
to at least briefly talk

[06:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=383s) about how we consume open source
and that conversation,

[06:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=387s) although a brief part
of this overall talk,

[06:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=388s) we could do a whole hour
just on this topic,

[06:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=391s) will at least give you some thoughts
about both how we operate,

[06:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=394s) but thoughts about
how you as well could operate.

[06:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=395s) There's not one perfect way
to do this,

[06:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=397s) but we think we have some
learnings we'd like to share.

[06:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=400s) So just briefly, in terms of
secure consumption,

[06:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=404s) we very much take a federated
approach to this topic,

[06:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=406s) as we do with many other topics.

[06:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=408s) We don't highly centralize
really anything at AWS,

[06:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=412s) but we still have central teams
that support certain core functions

[06:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=415s) to make sure that the teams
that have sort of direct

[06:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=418s) or immediate responsibility
are doing their job well.

[07:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=421s) And for us, open source consumption
begins in the engineering teams

[07:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=425s) that need--that decide
to use open source.

[07:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=427s) So the consumers of open source
take that core responsibility

[07:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=431s) for the software artifacts
they're using,

[07:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=433s) whether they develop them themselves

[07:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=435s) or whether they import something
from the outside world,

[07:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=437s) it's their responsibility to do that
in a safe, sane and secure fashion,

[07:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=441s) with the support of a bunch
of other teams.

[07:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=442s) But still, the core responsibility
exists in that initial consumer.

[07:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=447s) And in order to make sure that we
have ownership of these artifacts

[07:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=451s) once they're brought in,

[07:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=452s) we place that responsibility on sort
of that initial consuming team.

[07:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=456s) They can hand it off later,
perhaps, if that makes sense.

[07:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=459s) But some team has to really own
the health

[07:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=462s) and maintenance of that
core library or what have you,

[07:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=464s) and that's the builder team.

[07:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=467s) They need a lot of support
to do that well,

[07:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=468s) and that's where
our Builder Experience team,

[07:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=470s) which is a central team, comes in.

[07:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=472s) This is the team that runs
the core code repositories,

[07:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=475s) build servers, build pipelines,

[07:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=477s) as well as all
the deployment capabilities

[07:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=479s) and a lot of centralized testing
that runs on every single code check

[08:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=483s) in everything from unit tests
and so forth.

[08:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=485s) But security tests and code scans,
static code analysis,

[08:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=489s) software composition analysis,

[08:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=490s) all these tools are run
in a central service fashion

[08:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=493s) by the builder experience team.

[08:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=495s) So that means that any other
organization that wants to use

[08:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=499s) this open,
say, an open source library,

[08:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=500s) the first thing they're going to do

[08:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=501s) is they're going to look to see,
“Hey, is anybody else using this?”

[08:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=503s) Just like they would want to reuse
code that's internal only,

[08:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=507s) they're going to want to reuse
open source code as well,

[08:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=509s) because that means someone's taken
initial responsibility for vetting,

[08:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=512s) maintaining and updating that system.

[08:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=514s) And so this is where that
other team would go,

[08:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=516s) would go to the central code
repository and tools,

[08:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=519s) find that capability or that library

[08:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=522s) or that source code and progress
from there, again,

[08:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=527s) with that sort of federated
ownership and control.

[08:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=530s) And then finally,
we have a security team,

[08:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=532s) a central security engineering team,
especially on the proactive,

[08:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=536s) what we call proactive security
or Apse,

[08:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=538s) which does run a lot of the central
tooling to make sure that we're,

[09:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=541s) again, using and consuming
and deploying systems and code

[09:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=544s) in a very safe fashion
across the board,

[09:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=546s) including the open source components.

[09:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=548s) And so the Central Security
engineering team

[09:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=551s) not only runs a lot
of the security checks

[09:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=553s) in that central builder environment

[09:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=557s) and maintains both proprietary
and third party

[09:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=561s) and open source security
scanning tools and so forth.

[09:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=564s) They run, for example,
this is a little off the topic,

[09:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=566s) but a canary service.

[09:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=569s) So when you write your code,
you also write security

[09:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=572s) and variant types of checks,
which then the security team

[09:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=574s) has a service which runs
those constantly to make sure

[09:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=576s) that certain security invariants
of your service in production

[09:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=581s) are constantly
doing the right thing,

[09:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=583s) returning the right result,
the expected result from any call,

[09:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=585s) typically around authorization,

[09:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=587s) but lots of other security invariants
that you want to maintain.

[09:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=590s) You build essentially tests
that run

[09:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=592s) constantly against
the production environment.

[09:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=597s) Kind of helping hold this
all together

[09:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=599s) is our open source
program office.

[10:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=602s) They provide kind of
the general interface

[10:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=604s) to sort of the correct
and proper and healthy interaction

[10:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=608s) with the outside world,
along with David's team as well.

[10:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=611s) They're the ones that are doing
things like making sure

[10:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=613s) that we have good relationships
with the right outside builders,

[10:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=617s) sponsoring and funding things
that make sense.

[10:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=619s) We'll talk more about security
related funding later in the talk,

[10:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=623s) and in general, creating
that healthy interface

[10:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=626s) between AWS and the broader
open source community

[10:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=628s) to make sure
those lines of communication,

[10:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=630s) those relationships are there
to support the overall health

[10:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=633s) of this of this environment,

[10:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=635s) and again, using open source
in a secure fashion.

[10:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=638s) And we'll talk in a minute
about working upstream.

[10:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=640s) So another aspect of all of this
is if we do see need to make changes

[10:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=644s) or improvements
or security fixes or what have you,

[10:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=646s) a key part of what
we're going to be doing

[10:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=648s) is making sure that those
get pushed upstream as well.

[10:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=653s) So, after a little detour,
if you will,

[10:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=656s) although a very important one
on consumption,

[10:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=658s) we'll go back to sort of how we think

[10:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=659s) about--how we interact with
the broader world in open source.

[11:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=663s) And we'll focus on these
three pillars: work upstream.

[11:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=669s) That means when you're working
with something

[11:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=670s) where you're not the kind
of primary creator,

[11:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=674s) make sure that you are interacting
with that original source

[11:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=677s) in a way that is responsible

[11:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=679s) and contributing
to the common good there.

[11:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=681s) Release tools, and effectively
this is be the upstream in many cases

[11:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=686s) when you have things that the rest
of the community can benefit from,

[11:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=689s) put them out there
so others can benefit.

[11:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=691s) And then we'll talk also
about financial support as well.

[11:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=695s) We'll start with the work upstream.

[11:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=697s) So if we think if we take this
kind of long term and community

[11:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=703s) oriented approach to working in
the open source world,

[11:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=706s) we can benefit not only ourselves
but the broader community.

[11:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=708s) And we've been doing this
for a long time

[11:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=710s) and increasingly more
and more over the years.

[11:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=713s) I'll dive into a few of these.

[11:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=715s) We'll dive into a few of these
examples in more detail,

[11:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=717s) but just to cover a few in a more
kind of quick and anecdotal way,

[12:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=721s) I want to call out Xen project.

[12:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=723s) This was, as David mentioned, EC2,

[12:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=725s) one of our first
and most foundational services

[12:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=728s) originally launched
on the Xen hypervisor.

[12:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=731s) This is back in the days when
Intel processors

[12:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=733s) didn't have support
for hardware virtualization,

[12:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=737s) and people may remember some funky
things that were done in those days.

[12:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=740s) Xen was really pioneering with
this notion of Paravirtualization.

[12:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=744s) Raise your hand if you
remember Paravirtualization.

[12:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=746s) It's kind of dead, and it needs to be
dead, because it had some issues.

[12:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=750s) But it did an amazing job,

[12:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=752s) and we worked very closely
in that world of Xen

[12:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=755s) to make sure that we were deeply
involved with improvements,

[12:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=758s) patches and so forth.

[12:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=762s) Now we've been gradually
deprecating our use of Xen,

[12:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=765s) as probably many of you know,

[12:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=766s) and moving to KVM based,
the nitro hypervisor.

[12:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=769s) We're still active
in the Xen community,

[12:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=771s) and one of the last kind of
major contributions we made to Xen

[12:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=774s) was in the spectrum meltdown era,

[12:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=777s) when we realized that a lot of
shared state at the processor level

[13:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=781s) could lead to certain kinds
of side channel issues.

[13:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=784s) And Paravirtualization,
in particular,

[13:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=787s) was very problematic in that regard.

[13:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=789s) It was very problematic that
the kind of shared state

[13:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=792s) between the kernels and drivers
in the paravirtualized instances,

[13:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=797s) that you could have problems
of the type

[13:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=799s) that are manifested
in Specter meltdown.

[13:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=802s) So we actually created
an internal technology

[13:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=804s) to create a kind of shim layer,

[13:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=806s) so that the operating system
that's being hypervised

[13:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=809s) thinks
it's being paravirtualized,

[13:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=812s) but actually there's an HVM
hardware virtualization

[13:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=814s) layer sort of under the covers.

[13:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=816s) So you're essentially creating
a sort of fake copy

[13:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=819s) of some Xen internals
on the VM side

[13:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=822s) and then actual HVM capability
between the guest and the hypervisor.

[13:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=828s) This is a technology we call Vixen,
and we did push this upstream,

[13:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=831s) and so now any consumer
of--it was modified slightly,

[13:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=835s) but it did become
kind of the standard now,

[13:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=837s) so that Xen users
can run old-fashioned,

[14:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=840s) never updated operating systems
that expect Paravirtualization,

[14:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=843s) but actually are using
harbor primitives to do that.

[14:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=847s) There's many other great
examples here

[14:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=848s) before we get into
some of these others.

[14:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=850s) The one other one I want to call out
very recently in the KVM world,

[14:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=855s) those of you who are familiar
with operating system

[14:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=858s) and hypervisor security,
you might be familiar with something

[14:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=860s) that Microsoft calls
virtualization based security.

[14:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=863s) So for the Windows operating system
and the Hyper-V hypervisor,

[14:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=868s) they've developed some technology

[14:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=869s) that they can sort of
take parts of Windows

[14:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=871s) and run it in a separate--kind of
like a separate VM.

[14:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=874s) It's not exactly a separate VM,

[14:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=875s) but it's a hypervisor
protected memory space,

[14:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=879s) and that is designed to protect
against certain kinds

[14:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=881s) of cross process attacks,
essentially, that might cause trouble

[14:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=885s) with the things like the local
security authority in Windows LSA,

[14:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=889s) which maintains all of your passwords
and clear text in memory,

[14:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=893s) for example.

[14:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=895s) Now the problem is that that's
a proprietary Microsoft technology.

[14:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=898s) They released some information
about how they did that,

[15:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=900s) but it's definitely not open source.

[15:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=903s) We developed a VBS capability
for KVM,

[15:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=906s) which we just recently
started pushing upstream.

[15:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=908s) So anyone who uses the Linux--is
in the Linux ecosystem,

[15:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=912s) using the KVM hypervisor,

[15:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=914s) will be able to run these sort
of advanced and proprietary

[15:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=916s) Windows features and do that
on an open source basis.

[15:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=919s) So we're very excited about that.

[15:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=921s) Let's move on to some specifics here,
and we'll start with OpenJDK.

[15:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=926s) So we've had a long history
with Java.

[15:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=927s) We're a big Java shop.

[15:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=929s) Continue to be.

[15:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=930s) And back now, five years ago,
2017 timeframe, began to see a future

[15:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=935s) in which we really felt the need

[15:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=936s) to take a lot more ownership
for Java and our use of Java.

[15:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=941s) And in the 2017,
2018 time frame realized

[15:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=943s) we're not the only large enterprise

[15:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=945s) that is a little bit concerned
about the future of OpenJDK.

[15:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=948s) There was a change of ownership,
as you may recall, in the industry.

[15:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=951s) I won't name any names,
of the Java environment,

[15:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=954s) and there was a general concern

[15:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=957s) that the open version might need
some additional love and care

[16:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=961s) and really become more
of a full community effort.

[16:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=963s) So we joined in that effort.

[16:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=965s) We created our own Java distribution,
we call Corretto,

[16:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=969s) and since then we've really invested
heavily in the OpenJDK world,

[16:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=972s) and we release our Corretto capabilities
and runtime to the world for free.

[16:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=976s) You're welcome to use it.

[16:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=977s) It's fully supported by
our support organization

[16:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=979s) and by our engineering processes.

[16:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=981s) I won't go through all the different
things on the timeline

[16:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=984s) for the sake of time.

[16:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=985s) You can download the slides,
but basically it's just the point

[16:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=987s) we're making is that we've decided
to really help the community

[16:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=993s) jointly own the destiny
and the quality

[16:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=995s) and the features
of OpenJDK going forward

[16:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=997s) and making some very,
very deep investments in that.

[16:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1001s) And I'll hand off to David
for some more topics.

[16:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1004s) I just want to call out Corretto

[16:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1006s) has done amazing things
for our customers and for the users.

[16:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1011s) Specifically, we just saw New Relic
tell us

[16:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1015s) that Corretto is the most
widely consumed

[16:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1019s) OpenJDK distribution,
which is mind boggling,

[17:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1023s) but it tells me that customers
are actually finding value

[17:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1026s) in what we're providing.

[17:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1028s) So I'm super excited about that.

[17:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1030s) But I'm a little more excited
about Rust.

[17:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1033s) And how many folks know what Rust is?

[17:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1037s) Okay, so Rust is a new programming
language,

[17:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1040s) and I say new, it's been around--

[17:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1042s) David, does the world need
another programming language?

[17:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1044s) The answer is—

[17:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1045s) Yes, and more security tools.

[17:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1047s) Yes, it actually does.

[17:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1048s) And he'll explain why.

[17:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1050s) So Rust is a new programming language,
and I use the term new relatively.

[17:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1055s) It's certainly newer than C and Java,

[17:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1058s) and it has come about offering
the performance of C,

[17:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1064s) but with a number
of additional assurances.

[17:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1068s) So the biggest value from a security
perspective that we see with

[17:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1072s) Rust is thread safety
and memory safety.

[17:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1075s) And we're going to talk a little more
about memory safety

[17:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1077s) in a little while.

[17:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1078s) But when we were looking at
operating things at scale,

[18:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1083s) Mark said we're a large Java shop,

[18:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1085s) and we started paying attention
to Rust in 2017.

[18:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1090s) In 2018, we shipped Firecracker,
which was written primarily in Rust,

[18:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1096s) and that is an open source
operating system

[18:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1100s) that's really permitting
serverless technology.

[18:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1103s) So if you're running AWS Lambda,
Firecracker is there,

[18:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1108s) we've released that as an open source
project for people to consume.

[18:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1113s) And that was the first visible notice
that we gave the world

[18:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1117s) that we were
paying attention to Rust.

[18:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1119s) We had been using it for some
internal things already prior to that.

[18:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1123s) More recently, we launched a new
Linux distribution called Bottlerocket,

[18:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1127s) and Bottlerocket is heavily
Rust language focused

[18:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1134s) and is designed to provide
a really thin,

[18:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1138s) small security surface
for running containers.

[19:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1142s) And so we've also made
that open source.

[19:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1146s) Folks can download
and make use of that already.

[19:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1150s) In 2019, we announced that we were
sponsoring the Rust Project.

[19:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1156s) In 2020, we started hiring
a number of Rust maintainers,

[19:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1160s) because we recognized that Rust
was going to be important to how AWS

[19:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1165s) was going to develop in the future.

[19:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1167s) So we started building up a team
of folks who were already invested

[19:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1172s) in the Rust programming language,

[19:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1174s) who had already made
substantial contributions

[19:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1176s) and had leadership positions there.

[19:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1179s) Shortly after that, we helped found,
with a number of other stakeholders

[19:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1185s) in the community,
the Rust Foundation.

[19:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1188s) And today, EC2 looks at Rust
as its language of choice

[19:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1193s) for security sensitive applications
such as nitro enclaves.

[19:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1199s) And so we think that that Rust
is incredibly important

[20:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1204s) to what's going to be the future
of a number of different workloads

[20:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1208s) inside AWS.

[20:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1210s) And we're working,
we're heavily working.

[20:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1212s) We've got two teams who are focused
on upstream contributions

[20:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1217s) into the Rust programming language,

[20:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1219s) because we think that there is
so much benefit not just for AWS

[20:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1223s) in how we build our tools
and our services,

[20:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1227s) but for the rest of the world,

[20:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1228s) because we get into things
like memory safety.

[20:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1233s) But Mark and I, we just talked
about programming languages,

[20:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1235s) and I won't talk about a third,

[20:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1238s) because maybe the world does finally
have enough programming languages.

[20:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1242s) I want to talk a little further up
the stack with Kubernetes.

[20:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1246s) And Kubernetes is really
a workload orchestration

[20:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1250s) that the primary workload
is containers,

[20:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1254s) and it has become
incredibly successful.

[20:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1257s) And it's become successful
by a number of different measures,

[21:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1261s) the number of people contributing.

[21:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1263s) There are literally thousands
of people

[21:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1265s) who work on every
single release of Kubernetes.

[21:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1269s) The number of workloads that now
assume that Kubernetes

[21:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1273s) is going to be the underlying layer
that they're operating on.

[21:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1276s) And I can't tell you the number
of new tools

[21:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1279s) that I look at that presuppose
that they're going to be operating

[21:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1282s) in a Kubernetes environment.

[21:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1285s) We obviously recognized this
when our customers were telling us

[21:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1288s) that Kubernetes was important.

[21:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1290s) We have the EKS service and
obviously provide managed Kubernetes.

[21:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1296s) But we recognized a need really early
on that

[21:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1299s) we needed
to get involved in Kubernetes

[21:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1302s) and the rest of that Cloud Native
Computing Foundation arena.

[21:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1306s) And so we've been getting involved
in places like Container D,

[21:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1310s) etcd, Nerd Cuddle,
all of the surrounding technologies

[21:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1314s) that help make Kubernetes
so useful and so helpful,

[21:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1318s) because Kubernetes
is not just one thing.

[22:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1321s) It's essentially using a driver
model,

[22:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1324s) allowing people to plug
in different things,

[22:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1326s) like different network controllers,
different scheduling technology.

[22:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1333s) And that is one of the reasons
that it's been so successful

[22:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1336s) is that ability to plug in things.

[22:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1337s) But that means lots of help
is needed on the outside.

[22:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1342s) So etcd, Container D, etcetera,

[22:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1345s) are contributing technologies
to that success.

[22:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1348s) And we have heavily invested there,

[22:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1350s) taken leadership positions
in technical steering committees,

[22:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1355s) in the governing board
and a number of other places.

[22:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1359s) And also released some of our own
tooling,

[22:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1361s) where we recognized gaps that
our customers are pointing out to us.

[22:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1364s) So Carpenter was recently
released recently, a year ago,

[22:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1370s) was recently shown and provides
a lot of value for our customers

[22:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1375s) in trying to scale things
on Kubernetes.

[22:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1378s) But we also recognize that Kubernetes
does not exist

[23:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1382s) on code contributions alone.

[23:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1384s) So we've done a couple
of other things.

[23:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1386s) One is, despite how popular
Kubernetes is

[23:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1390s) and how fast it's innovating,

[23:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1392s) that's creating some upgrade
fatigue with customers.

[23:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1396s) And so they don't want to upgrade
every six months.

[23:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1399s) They've asked us for help, and we,
along with others in the community,

[23:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1402s) are working on figuring out
a longer support time frame for that,

[23:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1407s) because customers want to be able
to actually operate something,

[23:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1410s) not just be
in an infinite upgrade loop.

[23:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1414s) We're also, though, realizing that
there needs to be infrastructure

[23:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1419s) to actually test Kubernetes
in advance.

[23:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1421s) And so we committed millions
of dollars in cloud credits

[23:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1425s) every year for continuous integration
for the types of testing

[23:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1431s) that ensure that when you deploy
a new version of Kubernetes,

[23:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1436s) that hopefully it will be pain free.

[23:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1438s) We've been doing that,
as well as helping

[24:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1441s) with their release infrastructure now

[24:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1443s) and getting involved there
to make sure that, you know, again,

[24:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1448s) the project does not sustain
itself on code alone.

[24:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1454s) But that's not the only thing
we should be doing, right?

[24:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1457s) We talked a little bit
about adding features.

[24:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1461s) Mark talked about adding features
to KVM,

[24:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1466s) improving security on Xen,
and that's important.

[24:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1470s) And I think that AWS has an
obligation or responsibility

[24:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1475s) to release the security
improvements that it has.

[24:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1480s) And, Mark, do you want to start
talking about that?

[24:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1482s) Yeah. So in many ways,
again, as a shortcut,

[24:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1485s) you could say work upstream
is one thing.

[24:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1487s) Be upstream is another thing.

[24:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1489s) Of course there's an overlap
and a dynamic quality to that.

[24:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1492s) But in this case, what we're saying

[24:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1494s) is we have developed technology
from scratch

[24:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1497s) that we realize is very useful
for--I say from scratch.

[25:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1500s) I'm sure there's open source
libraries inside of those,

[25:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1503s) but basically significant
major projects

[25:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1506s) that we then want to release
to allow others to benefit from,

[25:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1508s) even when they're not using our
cloud platform or any of our tools.

[25:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1512s) And so we want to talk about a few
of those in this session as well.

[25:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1516s) We'll dive into, I think,
three of those,

[25:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1519s) but I'll call out a few

[25:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1520s) that don't have their own separate
slides in this overview slide.

[25:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1523s) So a launch from August of last year,

[25:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1526s) Open Cybersecurity Schema
framework, OCSF.

[25:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1531s) This is actually a set
of supporting open source tools,

[25:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1534s) but the core release
is actually of a standard

[25:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1537s) which allows security tools
to interoperate

[25:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1539s) in a much more seamless way.

[25:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1542s) When we would talk to customers

[25:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1543s) and working with a lot of partners
in the security space,

[25:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1546s) what we heard over and over again
was my security teams

[25:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1549s) spend too much time
on data munging and data cleansing.

[25:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1552s) They're doing this kind of
repetitive stuff.

[25:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1554s) They're writing tools
or they're doing manual things.

[25:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1556s) They're cutting and pasting between
multiple open windows on a screen.

[25:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1559s) Just crazy stuff to try to get
security tools

[26:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1562s) to actually work together

[26:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1563s) and to do that basic kind of function
you need to do often,

[26:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1567s) which is I need to do sort of a join
across two data sets.

[26:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1569s) And it was often very, very hard,
if not impossible.

[26:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1573s) So what we realized was
if we could create a standard

[26:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1576s) for how tools communicate

[26:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1577s) with one another,
there'd be a huge benefit to that.

[26:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1580s) So now we launched this last August
actually at Blackhat

[26:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1584s) with about 20 other partners
all signing up to support OCSF.

[26:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1588s) Now I think there's up to 60
or 70 companies

[26:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1590s) who are all committed
to either emitting or consuming

[26:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1594s) OCSF records
from their security products.

[26:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1598s) And that will make it much easier
going forward for security teams

[26:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1602s) to manage the data that's flowing
in and out of these tools.

[26:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1605s) We also use the OCSF format
as the native format of the Security

[26:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1609s) Lake product that we just launched
I think a week ago

[26:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1613s) and was in the keynote yesterday.

[26:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1615s) So any tool that can emit OCSF
can natively feed their data

[27:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1620s) into our security lake.

[27:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1622s) And that was not an accident,
by the way,

[27:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1624s) that we worked on both a standard

[27:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1625s) and a service together
that supports the standard.

[27:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1628s) So that's a really, I think, a really
interesting and impactful one.

[27:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1631s) David already mentioned Bottlerocket.

[27:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1632s) Bottlerocket you can think
of as a secure

[27:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1635s) Linux distribution
focused on container security.

[27:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1638s) So for example, it has a read
only file system.

[27:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1641s) There's no reason why file systems
need to be updated at the OS level,

[27:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1644s) if the only thing it's doing
is running containers

[27:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1647s) that are running virtualized
file systems on top.

[27:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1649s) So and it has many other such attributes
of very locked down, very secure

[27:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1654s) Linux foundation for running
container environments.

[27:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1658s) Firecracker we already mentioned.

[27:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1659s) Firecracker implements a technology
that are called microVMs.

[27:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1664s) So again, we don't trust container
boundaries as a security boundary.

[27:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1669s) In general, there's very bad track
record of containers

[27:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1673s) being fully secure

[27:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1674s) in terms of the ability
to escape from a container.

[27:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1676s) They really weren't designed
for that, so there's no blame there.

[27:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1679s) So we strongly believe in using
harbor based virtualization

[28:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1683s) whenever you have
a multi-tenanted or any workload

[28:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1686s) where you need strong isolation.

[28:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1688s) The problem is that VMs typically,
a typical virtual machine

[28:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1691s) takes a while to boot:

[28:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1693s) seconds, maybe a minute,
because they're big and complicated.

[28:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1696s) So Firecracker implements
a microVM technology

[28:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1700s) in which a full KVM virtual machine
can be booted

[28:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1703s) and executing user space code
in less than one eighth of a second.

[28:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1707s) So 125 milliseconds is
the design goal for Firecracker.

[28:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1710s) We've met that consistently
over time,

[28:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1713s) and that means
that you can now launch

[28:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1714s) VMs as quick as you can launch
a container essentially

[28:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1717s) or close enough
that you can use that

[28:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1719s) as a very foundational
property of your container

[28:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1722s) based or function
as a service workload.

[28:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1724s) So we use Firecracker underneath Lambda
and underneath our Fargate service,

[28:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1728s) but we also release it to the world.

[28:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1730s) And there's a lot of other vendors
now who use Firecracker

[28:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1733s) in their container
runtime environments,

[28:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1735s) and we're really excited
for the success of that.

[29:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1740s) I think you were going to call one
of these out before I move on.

[29:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1742s) Yeah, I’ve got a favorite.

[29:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1743s) I do have a favorite on this slide,
and it's trusted language extensions.

[29:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1748s) So PostgreSQL, the open source
database,

[29:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1751s) has a wonderfully vibrant
extension community,

[29:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1755s) and that allows Postgres to change
from a relational database

[29:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1761s) to a vector database to something
focused on geospatial

[29:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1765s) and a host of other things.

[29:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1767s) There are literally hundreds
of extensions to PostgreSQL,

[29:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1771s) the database itself.

[29:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1773s) And we recognized
from some of our own pain,

[29:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1777s) and while it didn't directly
impact our customers

[29:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1779s) because of defense in depth,
we saw that a number of folks

[29:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1783s) were calling out the extension space
as an attack surface

[29:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1788s) that would allow them to do nefarious
things to PostgreSQL databases,

[29:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1794s) true in hosted environments
as well as self-managed.

[29:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1798s) And so we created trusted
language extensions

[30:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1802s) and released that as open source.

[30:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1805s) We did that at re:Invent last year.

[30:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1807s) And I'm excited about this,

[30:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1808s) because not only does it
solve a problem for us,

[30:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1812s) and we could have
just solved that problem,

[30:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1814s) but we released this
because we recognized

[30:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1817s) that everyone should have a more
secure and a more safe PostgreSQL.

[30:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1822s) So the trusted language extensions

[30:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1824s) are probably my favorite
thing on this slide,

[30:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1827s) because it's something that
we've seen a significant problem,

[30:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1832s) identified that problem,

[30:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1834s) and then worked to not just
shut down the specific issues,

[30:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1839s) but to create a safer environment
to run those extensions in.

[30:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1843s) I'm super excited.

[30:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1845s) I'm really excited by seeing

[30:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1846s) how many people are adopting
trusted language extensions

[30:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1849s) as the environment in PostgreSQL
that have nothing to do with AWS.

[30:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1854s) That's awesome.

[30:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1855s) That's a great story.

[30:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1857s) So we'll dive into a couple of these.

[30:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1859s) Open quantum safe
is called out here, OQS,

[31:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1862s) and we'll talk about that
in the context of S2

[31:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1864s) and some other crypto stuff.

[31:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1865s) And then Cedar and maybe I think
we have one other example here

[31:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1868s) in terms of our decision
to work in the open

[31:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1872s) with core technologies
that we develop.

[31:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1875s) So you can imagine you run a cloud
platform, encryption super important.

[31:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1879s) It's one of the fundamental
properties of data isolation,

[31:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1882s) data security that customers rely on,
that we rely on.

[31:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1885s) So you really want to be constantly
on the cutting edge of cryptography

[31:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1891s) and of encryption technologies
across the board.

[31:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1894s) Customers, obviously, they're running
applications on top of our stack.

[31:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1897s) They want super-efficient systems

[31:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1900s) with minimum CPU
and memory utilization,

[31:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1902s) but they want state
of the art technology underneath.

[31:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1905s) So we've been on a journey now
for a number of years

[31:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1907s) to develop technology in this space

[31:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1910s) and to open source
the technology we develop,

[31:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1912s) because we believe it can benefit
the broader community.

[31:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1915s) I'll start with s2n.

[31:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1916s) s2n was one of our first forays
into this general space.

[32:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1920s) It originally stood
for signal to noise.

[32:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1922s) I'm not sure if we even spell
that out anymore, we call it s2n.

[32:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1925s) But you can think of s2n
as a very stripped down,

[32:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1928s) very minimalistic,
very feature poor, intentionally,

[32:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1932s) implementation of the TLS protocol.

[32:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1935s) Feature poor meaning that TLS
has a ton of features

[32:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1937s) that most people never use,

[32:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1939s) and but to implement those features
takes a lot of code

[32:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1943s) and therefore introduces
the possibility of more bugs.

[32:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1946s) The wakeup call for us and I think
for a lot of people in the industry

[32:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1949s) was the Heartbleed zero day.

[32:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1951s) Remember the Heartbleed one?

[32:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1952s) Raise your hand if you had a bad day
on the Heartbleed day.

[32:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1956s) We did, too, although we were able
to patch

[32:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1958s) a massive global fleet of load
balancers in less than 24 hours,

[32:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1961s) we still had literally
hundreds of thousands of hosts

[32:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1964s) that had to be patched
in our ELB service.

[32:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1968s) But that was a wakeup call,
because we looked at like, okay,

[32:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1970s) what's the root cause here?

[32:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1971s) Well, it's a bug in OpenSSL.

[32:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1973s) And okay, software has bugs,
but it was a pretty painful one.

[32:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1978s) But what about OpenSSL?

[32:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1979s) Oh, it's 300,000 lines of C code.

[33:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1983s) It's old, it's Crufty.

[33:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1984s) It's got--I mean, God bless
the community for keeping it up.

[33:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1987s) And we now we've been financially
supporting them ever since,

[33:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1991s) and it's done a ton of good
for the industry,

[33:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1993s) but it's not what we felt
really good about

[33:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1996s) in terms of relying on
as a core technology

[33:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=1998s) for very fundamental security
properties of our cloud.

[33:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2002s) So since then we've been kind of
on a journey

[33:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2004s) to both implement a replacement
and substitute

[33:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2008s) that in and use it as well
as release that to the world.

[33:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2011s) s2n was one of the first steps there.

[33:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2013s) So it's, again, just implements
the TLS part of the protocol,

[33:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2017s) still uses OpenSSL
for the cryptography parts

[33:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2020s) of the handshake and the encryption.

[33:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2023s) That was some years ago.

[33:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2025s) s2n is an interesting example too,
because this was before

[33:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2028s) Rust was kind of up and running
and popular, so it's written in C.

[33:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2032s) However, it's written
in a very strange and idiomatic C

[33:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2035s) that looks just like Rust,

[33:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2037s) because you can't do
any direct memory access.

[34:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2040s) It requires all these kind
of indirections.

[34:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2042s) And we have formal tests and proofs
that show that if any developer

[34:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2046s) does a check in that's not using
the proper memory handling functions

[34:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2052s) that are inside of s2n, sorry,
your code will get rejected.

[34:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2056s) So still using the C language,
but using it in a very carefully

[34:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2060s) crafted and memory safe fashion.

[34:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2062s) A couple of other really
interesting facts about s2n.

[34:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2064s) First of all, it's a project
that had, I think at the start,

[34:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2068s) maybe a little bit more now,
about 20,000 lines of code,

[34:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2071s) 80,000 lines of tests.

[34:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2072s) So it's a very, very test centric,
test heavy project.

[34:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2078s) And it was the first test,
first release to the wild,

[34:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2080s) as far as I know,

[34:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2081s) at least of any significant
piece of code,

[34:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2083s) in which formal verification
was part of the build

[34:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2087s) and the test and release process.

[34:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2088s) So all the people we hire,

[34:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2090s) and you've probably heard
in many talks from AWS,

[34:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2092s) a group we call the Automated
Reasoning team

[34:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2095s) or these formal verification
capabilities,

[34:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2098s) a branch of computer science
that has been a bit obscure.

[35:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2101s) It's been around for a long time.

[35:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2103s) It's not obscure anymore,
at least as far as we're concerned.

[35:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2104s) We're using more and more we're using
the tools

[35:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2106s) and techniques of formal verification
to prove the correctness of code.

[35:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2111s) In s2n, if you go to
the GitHub repository

[35:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2113s) and you look at the build instructions
and you download and try to build it,

[35:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2116s) you're going to actually download
a bunch of formal proofs

[35:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2118s) about the correctness
of various parts of that code.

[35:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2121s) Again, it doesn't mean the code
is bug free necessarily,

[35:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2122s) but it's a much higher standard than
we've traditionally done

[35:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2125s) for a lot of these systems.

[35:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2127s) So that was a big and important foray
into this space,

[35:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2131s) but we didn't want to stop there.

[35:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2132s) So subsequently we've also
open sourced our own libcrypto,

[35:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2137s) so now we're giving you
an open source reimplementation

[35:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2140s) of the core cryptographic primitives
you need for your network,

[35:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2145s) as well as other use cases

[35:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2147s) that are traditionally done
in the OpenSSL library.

[35:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2151s) I won't go on and on about libcrypto,
but it's out there.

[35:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2155s) One of the key things we're doing
with libcrypto

[35:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2157s) is we're taking on the burden
of FIPS validation.

[36:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2160s) That's one of the kind of things

[36:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2161s) that people often expect
of their cryptographic libraries.

[36:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2164s) They want that third
party validation.

[36:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2166s) And interestingly,
even around the world,

[36:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2168s) we still hear people are very happy
with FIPS validation,

[36:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2170s) even though it's technically
a US government standard.

[36:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2174s) And but it's hard for an open source
team to do that.

[36:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2177s) It's expensive, it's time consuming,
it's frustrating,

[36:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2180s) it takes a long time.

[36:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2181s) It's almost you almost kind of
require commercial interest

[36:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2183s) and commercial commitment to really
kind of go through the trouble,

[36:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2187s) which many companies do.

[36:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2188s) But we're doing that on behalf
of the open source users

[36:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2190s) of s2n and of libcrypto

[36:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2193s) We're taking that that through
FIPS validation,

[36:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2195s) and we'll keep that up to date
as time goes on,

[36:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2197s) which is kind of the hard part.

[36:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2198s) Often you get it through and then you
kind of like relax and move on,

[36:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2202s) and then your code gets out of date.

[36:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2203s) And so you get into this bad cycle.

[36:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2206s) So we're doing that with libcrypto.

[36:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2207s) And the final thing I want to call
out that's just briefly referenced

[36:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2210s) in this slide, and we could spend
a whole hour on it is

[36:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2213s) Post-quantum cryptography.

[36:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2214s) So we've made a lot of investments
in PQC.

[36:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2218s) Again, the nutshell version,
which I'm sure most of you know

[37:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2220s) is nobody has a sufficiently coherent
quantum computer today

[37:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2225s) to crack asymmetric cryptography.

[37:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2227s) But all the experts say
that if we can invent one,

[37:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2231s) and we don't usually like to bet
against engineering teams,

[37:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2233s) once problems go from theory
to engineering,

[37:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2236s) the engineers are often very good
at succeeding at very hard problems.

[37:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2239s) And so it's not unlikely that in
the future, not too distant future,

[37:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2243s) there will be a sufficiently
powerful quantum computer

[37:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2246s) that could crack today's
asymmetric cryptography.

[37:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2249s) Now, the good news is often
not mentioned,

[37:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2251s) which is symmetric cryptography

[37:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2253s) does not suffer much
from quantum computers.

[37:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2256s) So if you're using AS256
for encrypting something

[37:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2259s) that you write
to disk as EBS and S3 and Dynamo

[37:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2262s) and all our storage services do,

[37:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2264s) quantum computers would speed up
brute forcing of that,

[37:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2268s) cracking that crypto by a factor
of 100, 1,000, doesn't matter.

[37:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2273s) So much power is required to crack
those that

[37:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2277s) that's essentially irrelevant,

[37:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2279s) at least as far as we know,
according to today's experts.

[38:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2282s) But asymmetric cryptography,
totally different.

[38:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2285s) It's much, much--very susceptible
to being cracked

[38:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2287s) by a quantum computer
using brute force techniques.

[38:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2291s) And therefore, we have to get ahead
of this problem

[38:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2293s) before it becomes a problem.

[38:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2294s) So we've made a lot of investments
in post-quantum cryptography.

[38:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2297s) We have production systems today
in production

[38:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2299s) using hybrid key exchange,

[38:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2300s) which means that it encrypts
the inner keys of a TLS session

[38:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2305s) with both elliptic curve
and post-quantum

[38:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2309s) so that if one is cracked
or the other,

[38:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2312s) you still have
basically defense in depth.

[38:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2314s) So a lot of really interesting
technology going on there.

[38:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2317s) But again, the key thing is
we're doing this in the open,

[38:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2319s) so that anyone can benefit
from all the investments

[38:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2321s) and the work
that we're doing in this space.

[38:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2325s) Speaking of formal verification,

[38:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2328s) and because that's one of the key sub
themes of this open source release,

[38:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2333s) which we just made a month or so ago,

[38:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2335s) we've introduced to the world
a new--another new language.

[38:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2338s) Hey, we need new languages.

[38:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2339s) We really felt we did need
a new language in this case.

[39:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2341s) We looked long and hard
at existing authorization languages.

[39:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2346s) So this is a kind of a narrow
but very important part

[39:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2348s) of the security world

[39:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2350s) is how do I encode permissions
about access to systems?

[39:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2356s) If I could step back for those of you
who, like me,

[39:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2359s) have worked in sort of identity
and access management over the years,

[39:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2361s) as an industry, we've done a pretty
good job on the identity side, right?

[39:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2364s) We have a pretty good story
about SAML and OIDC

[39:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2367s) and blah, blah, blah.

[39:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2369s) That allows me to come across into
a system with some sort of validated,

[39:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2373s) cryptographically validated user
with a set of claims.

[39:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2376s) Okay, now I show up at a system.

[39:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2378s) Now what happens?

[39:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2379s) Somebody has to make
an authorization decision,

[39:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2382s) like what rights does
that person have in the system

[39:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2385s) that they're accessing?

[39:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2387s) There the industry has done
a terrible job of standardization.

[39:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2390s) We tried years ago with something
called XACML,

[39:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2392s) if you know what that is, boy,

[39:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2394s) we could go have a cup of coffee
and talk about that.

[39:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2397s) Failed miserably.

[39:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2398s) And if you think about today's
IT systems, on premises especially,

[40:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2403s) you have these
ACL models everywhere

[40:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2405s) SharePoint ACLs, Exchange,
different file systems,

[40:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2408s) everything has
an access control model

[40:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2410s) that's all completely disjoint,
completely heterogeneous,

[40:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2414s) and it's not a good story
in terms of wanting to understand

[40:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2419s) and answer those basic questions.

[40:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2420s) Who has access to what?

[40:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2421s) Like that is the holy grail
of access management systems?

[40:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2424s) Who has access to what?

[40:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2426s) Today, super hard to answer
that question.

[40:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2428s) It's easier in the cloud, by the way,

[40:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2429s) because you have a common identity
management system for all the APIs.

[40:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2433s) Still not super easy to answer,
and we're getting there,

[40:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2435s) but at least there's a possibility,

[40:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2436s) because of the unification
on the access side.

[40:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2439s) But long digression, but we decided
that our existing

[40:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2444s) IAM system works great,
but was it the right language

[40:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2447s) to expose for a broader
set of use cases?

[40:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2450s) We decided not.

[40:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2451s) I can go into lots
of great details why not.

[40:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2453s) We looked at existing open source
or standards technologies.

[40:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2456s) They didn't really meet
the requirements,

[40:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2458s) so we invented
a new one called Cedar.

[41:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2461s) And one of the many great things
about Cedar, which I won't go into,

[41:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2464s) but one of the most
interesting things is it was

[41:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2465s) built
by a joint engineering team

[41:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2468s) that included both experts
in access management,

[41:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2470s) but also formal
verification scientists

[41:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2473s) who built both the language
for formal verification

[41:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2477s) as well as the implementation,
the runtime and the libraries.

[41:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2481s) Those are also formally verified,

[41:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2482s) because you really want correctness
when it comes to access decisions.

[41:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2486s) So this is a really cool technology,

[41:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2487s) and there's some
great blogs on Cedar,

[41:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2489s) if you want to dig
into the gory details.

[41:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2492s) It includes another technology
called differential testing,

[41:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2494s) which is a very interesting
sort of probabilistic fuzzing,

[41:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2498s) if you will, because even
with formal verification,

[41:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2501s) you still want to do
some testing

[41:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2503s) to make sure that your tools
are all working properly.

[41:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2505s) So enough on Cedar, but it's
a very exciting release,

[41:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2508s) and we hope the world adopts this
and uses it everywhere

[41:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2510s) because even though there'll
still be some challenges

[41:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2513s) in terms of unification,

[41:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2514s) having a common access language
would be a huge win,

[41:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2517s) and we're working hard
to make that true.

[41:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2519s) Yeah. You know, Mark,
I was one of the naysayers

[42:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2522s) who said that there was
no need for Cedar,

[42:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2524s) because we have other
access languages out there.

[42:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2527s) And when this project
came up internally,

[42:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2529s) I was one of the folks who said,
“Why are we reinventing the wheel?

[42:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2533s) This doesn't make sense.”

[42:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2534s) But the formal verification
of both the engine,

[42:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2538s) the access engine,
and the policy itself really sold me

[42:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2542s) that this was something new
that actually needed to exist.

[42:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2545s) I'm excited about Cedar.

[42:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2548s) I'm excited about the attention
that it's getting as well,

[42:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2551s) because people seem
genuinely excited about this,

[42:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2554s) and those people
are not even AWS customers.

[42:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2557s) They're recognizing that this is
a gap

[42:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2559s) that we have
in the security space.

[42:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2563s) So I want to talk a little bit
about Snapchange,

[42:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2567s) which was another open source
release we made last month.

[42:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2571s) And Snapchange came out of a team
inside AWS

[42:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2574s) called Find and Fix
or our F2 team.

[42:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2578s) And to explain a little bit
about what F2 does,

[43:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2582s) the F2 team has a mandate
that they are to go look at what AWS

[43:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2588s) and our customers
are using the most

[43:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2591s) and then to audit it
to find problems,

[43:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2593s) specifically security problems
in the most commonly used

[43:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2597s) open source tools that AWS
and our customers make use of.

[43:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2603s) And they've been on this journey
for roughly a year now.

[43:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2608s) They've built up a team
of security researchers,

[43:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2611s) and they're trying to figure out
how to scale up their capacity

[43:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2615s) to find problems,
and Snapchange is a fuzzing tool,

[43:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2620s) and fuzzing essentially
tosses a bunch of strange

[43:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2624s) inputs into various break points
in a piece of software.

[43:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2629s) And frankly, fuzzing as a
general tool

[43:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2633s) has been responsible
for finding lots of problems.

[43:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2637s) And they looked around,

[43:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2639s) they're using plenty of
fuzzing tools as it is today.

[44:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2643s) But when they looked, they said there
are some things that we can improve.

[44:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2647s) Specifically, Snapchange is a tool
that works in an emulator

[44:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2653s) or a hypervisor environment.

[44:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2654s) It presumes that the software
is actually going to be

[44:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2656s) running as a virtual machine,

[44:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2660s) and it is able to inject
the fuzzing via that layer.

[44:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2667s) And so I said, “Why are you
doing this?

[44:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2672s) There are already tools
that do this.”

[44:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2673s) And one of the call outs was,
well, those tools today

[44:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2676s) require a modified KVM
and/or a modified kernel.

[44:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2681s) So you've got to load a specific
kernel module

[44:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2683s) that does not ship in tree.

[44:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2685s) And that's a barrier to some folks

[44:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2689s) for being able to easily deploy this,
being able to run it at scale.

[44:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2695s) The other thing that they wanted
to do

[44:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2696s) is they wanted to scale this across
multiple cores and so multiple

[45:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2702s) CPUs at a single time and run that
allowing folks to hopefully scale up

[45:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2708s) and make their fuzzing
activities a little faster.

[45:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2714s) So Snapchange allows folks
to basically use breakpoints in code

[45:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2720s) and submit all of this fuzzing data
into the program

[45:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2726s) and to replay that,
and so dramatically more scalable

[45:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2732s) and hopefully faster
for folks to use.

[45:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2734s) This is really targeted at
the security researcher audience.

[45:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2737s) This is not something that we
would expect an average developer

[45:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2740s) to go make use of.

[45:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2741s) We're excited about it, because
the security community

[45:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2744s) seems to be finding this useful.

[45:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2746s) And I'm really excited that this team

[45:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2748s) is getting a little
bit of visibility,

[45:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2751s) because they're doing amazing things
in terms of finding bugs,

[45:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2755s) because their mandate
is both to find and to fix.

[46:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2760s) They're not just looking at bugs
that they're finding in code

[46:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2764s) and saying, “Hey, here's
a security vulnerability.”

[46:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2767s) They're developing proof of concept.

[46:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2770s) They're developing a patch
and shipping

[46:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2771s) that to minimize the workload
on the open source maintainer,

[46:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2775s) because we don't want
to stand up a team

[46:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2778s) that basically creates
a denial of service,

[46:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2782s) a social denial of service attack
on open source maintainers.

[46:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2785s) So we want to provide them as much
help as possible

[46:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2788s) when we're going out and
looking for security vulnerabilities.

[46:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2791s) I'm going to interrupt you
for a second.

[46:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2793s) Go slightly off script, because
I think this is super important.

[46:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2795s) It’s something I learned from you
when I first started

[46:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2797s) getting involved
more in open source security.

[46:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2799s) So, by the way,
David is the president

[46:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2801s) of the Apache Foundation
in his spare time.

[46:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2803s) And very, very long and deep
involvement in open source community.

[46:48](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2808s) And I remember when we first started
talking about

[46:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2809s) these kind of security audits
and so forth,

[46:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2812s) you sent me this postmortem
of a security audit

[46:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2814s) that was done
on some Apache software.

[46:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2816s) And it was so enlightening,
because what it made me realize

[46:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2819s) is you can go in
and you can find bugs.

[47:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2821s) There's no problem finding bugs
in large software code bases.

[47:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2826s) Now what?

[47:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2828s) Bugs.
Okay, great.

[47:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2829s) Now what do I do?

[47:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2830s) Where's the resources that are
needed to fix the bugs?

[47:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2833s) That's a whole different thing.

[47:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2834s) And it's also very hard to inject
those resources,

[47:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2838s) even if they exist,
into an existing development team,

[47:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2841s) an existing culture, an existing way
of building and developing software.

[47:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2845s) So I found that super enlightening.

[47:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2846s) And it was also kind of
an eye opener.

[47:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2849s) Like it's not a matter
of finding bugs,

[47:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2850s) it's a matter of creating this
virtuous cycle of finding things,

[47:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2854s) but also developing the skills,
the capability of the community

[47:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2858s) that owns the software,
prioritizing those fixes.

[47:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2861s) All those things are a much harder
problem than just finding things.

[47:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2864s) And I think that's a super important
story around how we need to,

[47:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2867s) as a community,
get better at doing this stuff.

[47:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2870s) I think that report that
you mentioned was talking

[47:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2873s) about all of the influx of help
that happened after Heartbleed,

[47:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2877s) and I use "help" in air quotes,
right?

[48:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2880s) Because security is not
a one-time thing that you can say,

[48:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2883s) all right, we're secure today
and then walk away.

[48:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2887s) It requires that continuous
investment

[48:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2890s) where you're making long
term investments

[48:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2893s) in not just technology
but in communities

[48:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2896s) and making sure that you can
actually shift the culture,

[48:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2902s) shift the practice
to something more secure.

[48:25](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2905s) It's not--you're right,
it's not about finding bugs.

[48:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2907s) If it was that easy, we would—

[48:30](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2910s) We'd be much better today.

[48:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2911s) We would probably not be giving a
talk today on open source security.

[48:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2916s) So.

[48:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2919s) I said this earlier,
but open source projects

[48:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2922s) do not work
on code contributions alone.

[48:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2925s) And we think that AWS, you can see it
in our leadership principles,

[48:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2932s) size and scale
bring great responsibility,

[48:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2934s) and we certainly have
a responsibility to open source.

[48:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2939s) And so we recognize that.

[49:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2941s) And one of the mechanisms
that we can make use of

[49:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2945s) is to support a number of open source
projects and open source foundations.

[49:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2951s) And we do this
across a number of places.

[49:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2955s) So we support places like
the Python Software Foundation,

[49:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2958s) the Apache Software Foundation.

[49:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2960s) We're members of the Linux Foundation
and Cloud

[49:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2962s) Native Computing Foundation

[49:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2964s) and provide a baseline
of support via that mechanism.

[49:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2969s) That provides us a way to make sure

[49:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2971s) that that base level
human infrastructure is in place

[49:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2976s) and that people are able
to get things done.

[49:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2979s) But I want to dive into
how we're thinking

[49:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2981s) about funding
security responsibilities,

[49:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2985s) because I think that is
a separate layer above

[49:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2987s) just funding the open
source projects themselves.

[49:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2991s) So the Python package index,
if you're not familiar with PyPI,

[49:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2997s) it is a—

[49:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=2999s) You're not a Python developer
if you're not familiar with it.

[50:01](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3001s) You aren't.
You aren’t.

[50:03](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3003s) You know, this is how the world
consumes Python, right?

[50:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3006s) It is the package repository.

[50:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3008s) If you're a Java developer,
there's Maven Central.

[50:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3011s) If you're a Python developer,
there's the Python package index,

[50:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3015s) and it is a huge attack surface
for folks

[50:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3019s) trying to impact
the software security supply chain.

[50:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3023s) And we recognized this early on,
paid attention to it,

[50:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3026s) started working with
the Python Software Foundation

[50:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3029s) and said what can we do together
to improve this?

[50:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3032s) And they said, “Well, you know, today
we're doing mainly reactive

[50:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3035s) response to security issues.

[50:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3038s) We don't really have a great
security strategy

[50:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3041s) for the package repository itself.

[50:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3044s) We're not proactively going out
and looking for threats.

[50:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3047s) We would like to change that.”

[50:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3049s) They put together a proposal
and brought that to Mark and I

[50:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3051s) and said,
“Hey, this is what we'd like to do.

[50:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3053s) Can you fund this?” And we said,
“Absolutely.

[50:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3056s) This makes perfect sense.

[50:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3057s) We'd love to jump in here,”

[50:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3059s) because we consume packages
out of the Python package index.

[51:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3065s) All of our developers
who are doing Python do that.

[51:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3068s) Our customers do as well.

[51:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3070s) And so does the rest of the world.

[51:12](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3072s) You're not developing in Python
if you're not using this.

[51:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3076s) And so we have been working with them

[51:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3078s) to help create proactive strategies,
build up some internal staffing,

[51:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3084s) so that they can actually
respond to issues timely.

[51:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3088s) And we're not depending upon
volunteers in Nebraska

[51:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3094s) to respond to a security issue
in the Python package.

[51:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3097s) We just have some individual in mind
when you refer to,

[51:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3099s) so we won't mention any names.

[51:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3101s) We won't mention a comic's name,
but we're not responsible.

[51:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3106s) We're not responsible if we're not
taking into account

[51:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3110s) these distribution points

[51:52](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3112s) and making sure that we are helping
to fund their security,

[51:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3116s) because that impacts all of us.

[51:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3119s) We have that shared destiny
we talked about earlier.

[52:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3124s) We've also--and we've hinted around
at this a little bit earlier,

[52:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3128s) but there's a number of scholarly
articles

[52:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3131s) written by people far smarter
than I

[52:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3133s) that are looking at the overall
timeline of security vulnerabilities.

[52:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3138s) And they're reporting that 65%
of security vulnerabilities

[52:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3143s) in the past decade
are memory related.

[52:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3148s) Two thirds of security
vulnerabilities

[52:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3152s) are from a single class
of security threat.

[52:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3157s) And one of the reasons we are
so interested in Rust

[52:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3160s) is that it provides tooling
to ensure memory safety.

[52:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3164s) That's not a panacea for--Rust
does not make you magically secure.

[52:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3169s) And I don't want to paint
that picture,

[52:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3171s) but it is a much more
assured position

[52:55](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3175s) from a memory safety perspective,

[52:57](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3177s) and I'm excited about that for what
we're developing internally, Mark.

[53:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3182s) But we looked at where some of
the entry points

[53:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3186s) in terms of open source was.

[53:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3188s) And I remember us sitting in your
office in Virginia a year ago now

[53:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3194s) almost and talking about the places
where we were seeing attacks

[53:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3199s) and seeing security vulnerabilities
in open source.

[53:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3203s) And, again, security is not a point
in time thing that you can go say,

[53:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3208s) “I'm secure today and I don't
have to worry about it anymore.”

[53:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3211s) And so we looked at
where can we focus on things

[53:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3215s) that are on a network boundary,

[53:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3217s) things that are getting
lots of direct Internet traffic

[53:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3220s) or they're parsing huge files.

[53:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3223s) How do we go address that?

[53:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3225s) And so we identified
four initial projects

[53:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3229s) and asked the Prossimo project
out of the Internet Security Research

[53:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3233s) group to go rewrite those for us.

[53:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3236s) And we provided funding
to rewrite those.

[53:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3238s) So those initial four
are the NTP daemon.

[54:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3242s) We asked for a Rust implementation
of that, sudo and su,

[54:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3246s) because again, increasing
your authorization level

[54:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3251s) is something that you really don't
want to have memory issues in.

[54:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3255s) Rustls—

[54:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3256s) There's a long and sad history
of bugs in that.

[54:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3259s) There are, a lot of memory bugs
specifically in sudo.

[54:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3263s) Rustls, the TLS library for
the Rust programming language,

[54:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3269s) we wanted to improve
how fast Rustls

[54:32](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3272s) was going to be able
to be production ready.

[54:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3275s) We want to make sure that--Rustls
is already

[54:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3277s) Rust written,
so no inherent rewriting,

[54:41](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3281s) but we want to mature
that rapidly,

[54:44](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3284s) because we think
that a TLS implementation

[54:47](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3287s) that's memory safe
is super important.

[54:50](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3290s) If your encryption fails,
you've got lots of other problems,

[54:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3293s) and then an AV1 decoder,

[54:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3296s) and AV1 is itself
an open source success story.

[54:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3299s) And we wanted to make sure
that that this decoder

[55:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3304s) that's processing lots of huge files,
both audio, video and images

[55:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3310s) is written well and is secure.

[55:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3315s) So we've been doing--we've been
investing in a lot of that.

[55:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3320s) And finally, the industry
as a whole has coalesced

[55:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3324s) around the Open
Source Security Foundation.

[55:27](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3327s) And Mark championed
joining OpenSSF years ago,

[55:34](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3334s) right after it came out.

[55:37](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3337s) We joined that.

[55:38](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3338s) We started investing
and spending time there.

[55:42](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3342s) Folks from Mark’s office
were certainly heavily

[55:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3345s) invested in trying to advance
the state of security in open source.

[55:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3351s) But we recognized that there
was opportunity to do more.

[55:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3354s) And so last year we committed
$10 million towards OpenSSF

[56:00](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3360s) to make investments
in long term sustainable,

[56:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3364s) open source security initiatives.

[56:05](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3365s) And we did a couple of those.

[56:07](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3367s) I'll talk about them real quickly,
Alpha Omega,

[56:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3369s) which has two objectives.

[56:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3371s) The first is paying attention
to the 10,000

[56:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3374s) most widely used
open source components

[56:17](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3377s) and creating automation

[56:21](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3381s) around finding security
vulnerabilities and patching it.

[56:24](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3384s) So they're really heavily focused
on automating security

[56:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3388s) as much as possible.

[56:29](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3389s) The other side of Alpha Omega
is focused on the top 100.

[56:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3393s) What can we do that has
outsized impact

[56:36](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3396s) across the most heavily
consumed open source packages?

[56:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3400s) And how do we make that
security investment sustainable?

[56:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3403s) They're doing great work.

[56:45](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3405s) We're seeing lots of things
happening there

[56:49](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3409s) in a number
of different communities

[56:51](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3411s) where we continue
to be excited about that.

[56:54](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3414s) Security scorecards, though,
Mark talked about consumption, right?

[56:58](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3418s) And we at AWS,
we delegate open source

[57:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3422s) consumption decisions to builders.

[57:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3426s) Nobody comes to Mark
asking for permission

[57:08](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3428s) to use
another programming language,

[57:10](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3430s) even though he's in
the security organization.

[57:13](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3433s) Nobody comes to me in
the open source organization saying,

[57:15](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3435s) “I want to use this thing.

[57:16](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3436s) Is it okay?”

[57:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3438s) An individual developer
is doing that.

[57:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3440s) And we think security scorecards,
which will provide an automated

[57:23](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3443s) look at a number of health metrics
and security metrics,

[57:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3448s) provides much greater information
to base decisions upon,

[57:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3453s) so that those developers
who are deciding

[57:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3455s) what open source they're consuming
can make better informed decisions.

[57:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3460s) We're excited about some of the work
coming out of security scorecards

[57:43](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3463s) and look forward
to that being more ubiquitous.

[57:46](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3466s) And of course, we're doing a lot
of general support as well.

[57:53](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3473s) So let's close out our session.

[57:56](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3476s) And just as a reminder
of our takeaways and our pillars,

[57:59](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3479s) work upstream and contribute
to the open source world

[58:02](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3482s) and provide financial support.

[58:04](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3484s) And for all of these things,
we encourage you,

[58:06](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3486s) the broader community,
to join with us in these areas.

[58:09](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3489s) Think about ways in which
your organization

[58:11](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3491s) can work in one
or two or three of these ways,

[58:14](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3494s) or come up with new ways
to work to support open source.

[58:18](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3498s) Join with us.

[58:19](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3499s) Come to us with ideas.

[58:20](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3500s) We're very interested if you have
funding ideas,

[58:22](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3502s) if you have engineering ideas that
you think can help in this world,

[58:26](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3506s) that's super, super important.

[58:28](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3508s) We're going to join together
to make the world a safer place,

[58:31](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3511s) because we all depend
on secure open source.

[58:33](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3513s) And we thank you very much for coming

[58:35](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3515s) and have a great rest
of your time here at re:Inforce.

[58:39](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3519s) -Thank you.
-Thanks.

[58:40](https://www.youtube.com/watch?v=kMY8gGmWfAI&t=3520s) [applause]

