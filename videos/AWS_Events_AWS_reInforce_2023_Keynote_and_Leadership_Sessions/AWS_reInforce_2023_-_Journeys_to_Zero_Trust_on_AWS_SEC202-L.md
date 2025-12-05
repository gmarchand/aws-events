# AWS re:Inforce 2023 - Journeys to Zero Trust on AWS (SEC202-L)

[Video Link](https://www.youtube.com/watch?v=Uke2CmFaVZ8)

## Description

Through customer feedback and deployments, AWS has gained more insight into how organizations are moving forward with Zero Trust architectures for different use cases. In this session, Jess Szmajda, General Manager, Network Firewall & Firewall Manager, AWS, and Quint Van Deman, Principal, Office of the CISO, AWS,  discuss how customers use AWS to implement a Zero Trust security model for their workloads and also present their real-world architectures. Discover how you can use new AWS services to put Zero Trust into production and benefit from the security it provides. Also, learn how AWS envisions simplifying Zero Trust to help improve the safety of modern digital society.

Learn more about AWS re:Inforce at https://go.aws/3p6Wolr.

Subscribe: 
More AWS videos - http://bit.ly/2O3zS75 
More AWS events videos - http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers — including the fastest-growing startups, largest enterprises, and leading government agencies — are using AWS to lower costs, become more agile, and innovate faster.

#reInforce2023 #CloudSecurity #AWS #AmazonWebServices #CloudComputing

## Transcript

Hey, all.
I'm Jess Szmajda. I'm the general manager of some of
our security services here at AWS, including Network
Firewall and Firewall Manager. Previously, I built--I
led the team that built AWS Verified Access,
our first higher level service that helps you simplify
zero trust on AWS. Today I'm joined by Quint Van Deman
from the office of our CSO. Quint's been leading our AWS zero trust efforts
for a few years now and has had thousands
of conversations with customers just like you on what we can do to
help you on your Zero Trust journey. So I'm going to let Quint
take it away now. Awesome.
Thanks, Jess. Thanks for joining us, everybody. So let's get into things. Now, bar raising security
has been central to AWS since the beginning. It always has been and continues
to be our top priority. And you see the intention
of this security resulting in security architectures
that we think are absolutely bar raising in terms of what
you can build on AWS. You know, I'm talking
about features that maybe you haven't
thought about for a while, because it's just sort of the way
the cloud has always worked. But software defined
micro perimeters, request level authentication
and authorization, accurate maintenance-free
state inventory or state and inventory data,
machine identities with cryptographically
verifiable hardware root of trust, credential distribution
at hyper scale and so on. All of these types of concepts
would be very, very familiar in any conversation
in and around zero trust. And that's what we're going
to talk about today. All right. So I'm going to start by doing
a little grounding with us today. We'll talk a little bit
about motivations. We'll talk a little bit
about what AWS thinks zero trust is in terms of
the necessary definitions and maybe some guiding
principles and tenets. Then I'm going to turn it
over to Jess. And as she mentioned a little bit,
she's going to talk to you about what's new for us
in this space, right. We've had some really
important innovations on your behalf in the--particularly
throughout this spring and leading up to here at re:Inforce
that she's going to walk through, and then I'll take back
over at the end, and we're going to do
a little bit of envisioning. I want to give you a little bit
of a feel of where we're
going in this space. It's not the reality
of the world today, but I think it's important
for you to understand how we see this world
continuing to evolve and what we're going
to continue to bring for you. Now, as just mentioned,
over the last handful of years, I've had the chance to talk
with countless numbers of great customers
such as yourselves. And we really, when we sit down, we really work hard
to meet you all where you are. That means listening to your specific outcomes that you're after in terms
of the business side of zero trust. It means understanding and detailing
the technical challenges that you're after, right? It means understanding the existing
security architectures that you have, the existing
investments that you've made and how we might go about
layering zero trust on top of that. But the key in the end of that
is that getting to zero trust sort of depends on where
you're starting, where you're at. Now, for some customers, the move
towards zero trust has been just self-motivated. It's a natural, logical iteration of the continued evolution
of cyber security in general and defense in depth in particular. For other customers, the motivation
has been driven by public policy and regulation
from all corners of the world. But in general, the security risks
we face are pressing, and they're guiding you all to be
more precise about the controls that you use to control access
and audit the same. We're always after this raising
of the security bar. So despite the hype, despite the fact
that it in some ways became whitewashed across
everything across the industry, we really believe
in this term, zero trust, right? We believe deeply in the outcomes
and the benefits that it provides. And we've done so in our own
organization across Amazon, across AWS for many, many years where we've been
putting those concepts to work. Right? So this really is--we do
fundamentally believe that zero trust,
despite some of the hype, does lead to better
security outcomes and success. So now through those conversations, there were a bunch of points
of commonality that always continue to come back. Customers
had questions like, “Where do I start? What does good look like? How do I explain zero trust
to my organization? How do I leverage the investments
that I've made?” We're not starting from scratch here. But ultimately, all of that tends
to end up circling around and coming back to a very
practical question like this one, which is sort of the age old
question of security in the cloud. I think this is a great question
to form as the backdrop for zero trust, because it just allows us
to be practical, better every day. And if we're going to--and zero trust
is increasingly the term that we might use to describe
what good looks like here. But if we anchor on this question, it really helps us
move forward effectively. Okay. So invariably, you know,
the world needs definitions to get going on zero trust. And this is the one that
we've offered for many years now, that Zero Trust is a conceptual model
and an associated set of mechanisms that focus on providing security
controls around digital assets that do not solely
or fundamentally depend on traditional network
parameters. Now, instead, we're going
to rely on identity, device, other advanced signals to bring in
and make ever more continuous, adaptive and sophisticated access
control decisions. Now, the other thing I want
to bring your attention to is that we're very deliberate,
that this is a security model, right? Zero trust is not something
you're going to buy. You may buy products. You might buy products from AWS. You might buy products from
our great partner organizations. You might build products or services
that help you get to zero trust. But you need to start by
considering it as a security model. It's not a simple checkbox thing that you're going
to buy off the shelf. Okay, so now definitions
are necessary. But at Amazon we really find
that guiding principles or tenants, as we might call them, really help
sharpen our thinking in this space. And we've been offering
a number of guiding principles to our customers for a while
that we'll walk through here today. The first is simply to avoid
a binary choice. It's pretty easy to get going
in any zero trust conversation, and someone will invariably
throw out something to the effect
of the network perimeter is dead. Long live the identity
centric perimeter, or perhaps vice versa, depending
on their particular persuasion. But we really think that
that's a false choice, right? While network perimeters like as
what we sort of just walked through, we no longer want to think of
as sufficient, they're very useful, they're very well understood,
they're very easy to reason about. They've been around a long time. There's a lot of strong skillset
and expertise within many of your organizations, most of your organizations
around how to do network security. Now, inside of that, you know,
often identity centric controls can provide greater levels
of granularity. You've been using identity
centric controls to talk
to the cloud for years, literally since the dawn
of the cloud, right? But ideally, those two things
shouldn't be an and, they should be an or right. They ought to work together
in good harmony. And ideally, not only should
they coexist, but they should be aware
of one another right? Now, the original example,
or at least the most sort of easy to get a hold of example
was something like a VPC endpoint. So this was a control at the edge
of your network that understood
the identities, resources and network locations involved
that were flowing across it. And you could write a policy that
understood all of those dimensions and really delivered
excellent access control. So we're going to see today how
this theme of this convergence has continued to evolve
in some of the new services. But this is a really important point
that you don't need to throw out what's been working
in order to get to what's next. Now the second guiding principle
that we've been offering to you for a while is this notion of working
backwards from your use cases. When we originally started
talking with customers a good handful of years ago, we largely saw synergy
around these three, right, about how you get humans
to applications. The proverbial any user from any
coffee shop anywhere in the world, no VPN required. How we might think about moving
zero trust into the data center, service to service, machine
to machine, a lot of names there. And then sort of a broad bucket
for stuff that existed wholly outside the corporate
network entirely, right? The IoT enabled wind turbine
or oil tank sitting well outside
the corporate network, beaming critical telemetry
to the cloud. And what's interesting about
those use cases is that they share these very same, these very familiar
underlying technical principles. We want to get away from the network. We want to bring identity
and other contexts to bear. But at the same time, they're very
different in the objectives thereafter or the outcomes
that they're after. The first might be about mobility. It might be about workforce
happiness, it might be about work from home
in the middle of a pandemic. The second is typically about
reducing pathways through--unnecessary pathways,
through our organization, particularly those
that lead to data, right? But if we focus on use cases,
again, we get very practical. We get really focused on the problems
that we're trying to solve, and we avoid getting mired in this
what is or what is not zero trust that can often bleed too much
into these conversations, right. And so I really strongly encourage
you to think about zero trust is the how. Zero trust isn't the what. You aren't implementing
zero trust for zero trust sake. You're implementing zero trust
for a business outcome or a technical outcome that are generally going
to align to these use cases. Now, in the time since then, again,
there was maybe as folks got a little bit further
down the path of understanding and implementing zero trust, other use cases
have clearly come to light that are generally now
sort of bucketed under the banner of zero trust. There's likely many more,
but maybe a few others that I'll sort of explicitly call
out, operator to workload, right. How distinct from a business
user accessing an application
through a web browser, maybe think about this as how
an operator might go in through SSH to get to a,
you know, an operating system or a database engine, right. Human to data, whether that's
in the realm of data science or otherwise, right. Where we've got folks that have--that
need by the function of what they're trying to do, very
close and intimate access to data. But we also obviously that data has
a lot of sensitivity to it, right? And how can we bring
zero trust principles to make sure that very intimate
access is carefully controlled? And then perhaps it's one of the,
you know, a bit further down
the maturity curve, but how can we even think
about taking zero trust to its ultimate state, where the things
that we're considering in terms of access decisions
are way down within the applications, even more granular than something
you might get from a cloud API call, right? And so all of this brings me,
oh, sorry, and finally,
our last principle, right? That simply that zero trust is still
in a relatively nascent state. It still is not something
that we think one size fits all. Now, that's relatively
decent guidance for just about anything
in the cloud, right? If you try to wedge everything
into one, friction is going to ensue for
your workforce and otherwise, right. So use this where it really matters. Start with protecting--or start by
using zero trust to protect the things
that really matter the most to you, and use that as a way
to credibly build experience, muscle memory and authenticity in the way
you might roll it out more broadly. At the same time, we really think
of this as a way to give you— to let you retire some of the controls
that you've had for a while, but they're probably brittle, and they're probably not
really adding much value, right? Maybe we think of the VPN and some
of those things in that light. So not only is it guidance to help
you understand where you should, you know, use zero trust
and extend your security model, but also think of this principle as a way to let's use it
to simplify things and get things out that are
no longer really doing their job. Okay, so now we regularly get
feedback that indicates that these principles are
really helping folks stay grounded and focused on improving
their security each and every day
in very practical and real ways. And I hope that that will help you
in a similar fashion. But customers don't just share
what's worked, of course. They share there--as you continue
to share, as you should, for sure, continue to share
your fair share of suggestions and capabilities
that we can improve upon, where we could provide
more assistance. So there's lots of permutations
of use cases out there. But again, those first two that I
mentioned around humans to applications and controlling
flow of data are very common and are often expressed back to back. And you all have really told us
that you want to be able to integrate and fuse your technology
investments in a way that just gets
to those better outcomes rather than those siloed piece parts. So Jess is going to talk to you
a bit more about the services that we're building that bring you
these capabilities with much less assembly
required, much more AWS opinionated guidance built in, right. Now, before I turn it over to her
here, you know, for context what you all were
experiencing, right, as we gave you
at first those lower level primitives is a long held Amazon belief. In short, primitives, not frameworks. Our Amazon CTO, Werner Vogels wrote
and spoke about this extensively when he reflected
on the first 10 years of AWS. But in short, it's our very
deliberate way of building software and systems from the bottom up,
and there's a lot to unpack here. And if you're interested,
I'd encourage you to read his blog about how successful complex systems must evolve out of collections
of simple systems. But for zero trust specifically,
this really guides us in decomposing big and ambiguous problems,
where the clarity of the end state isn't nearly as good as the clarity
of where we might begin. And this allows us to make progress
while continuing to gain insights, what's working, what's not, and ensuring that we're being
very deliberate in working backwards from your pain
points, not our preconceived notions. So I'd like to bring in Jess to share
with you how those very insights have led to the next generation
of higher level zero trust focused services. Jess, take it away. Thanks, Quint. [applause] So let's learn a little bit more
about how AWS is helping you simplify zero trust
in your organizations. So something we've observed is that
when we give you those sort
of flexible primitives and tools that we had Werner talk about there
for a second in text, you do something
that's really amazing. Not only do you use them to solve
the problems that we expect you to solve,
but you also solve problems that we had no idea
you were going to solve. You find interesting opportunities
to apply these technologies to problems
that crop up in your world, and that's really exciting, because then my job is to come
and talk to you, learn about the problems
you're solving, and find better ways
to solve those problems. And through that sort of
iterative cycle, we build even better systems for each
other and make the world go better. So in the world of zero trust, this means that we're focusing on
simple foundational services that you can use
to solve those use cases that Quint talked about directly. And then over time, we'll find better
ways to make it even simpler for you. So I want to talk by diving deeper
into that first use case, which is the human to app use case. This is somebody sitting
in a coffee shop, maybe working from home, accessing
a secure corporate application. Now, this is a dynamic security
environment. There's a lot of things going on
in this space, and it's not the same kind of thing
that we've been used to, where you have a worker on a
corporate network that you can trust. So how do you establish trust
in this situation between somebody who may
have left her laptop open or may have needed to get
patches installed on a machine and get sensitive data accessed? It's a tricky thing. Now, a lot of you have been solving
this with a variety of techniques. The first one is obviously VPN. In my last role before I came over
to Network Firewall, I was the GM of VPN. And so I understand VPN. VPN is fantastic. Don't get me wrong,
I'd love to sell you more VPN. The challenge with VPN is you log in
at the front door, you get access
to the corporate network. Maybe you re-authenticate
from time to time, but you still have to dial
into the network and then you get other challenges
of getting your data transferred. Maybe somebody's trying
to go to YouTube. It gets a little complicated
in some other ways. On the other hand, some of you who have been securing
your Web applications by putting them directly
on the Internet and layering various security
services like Shield or WAF, and helping you establish trust from that untrusted endpoint
into your application. But again, usually these rely on
authenticating once at the front door and you can control session length,
but that can get pretty annoying. So we knew this could be simpler. And I think a lot of you have seen
a lot of ways that this could be simpler,
and that's why we introduced AWS Verified Access,
which is now GA at the end of April. Access helps you simplify access
to corporate applications using zero trust principles. Instead of having to check
just once at login, verified access checks
every request in real time based on the latest security data,
using policies that you define. Your end users get seamless
experience accessing their corporate
applications and instead of having
to assemble multiple services, you just put verified access
in front of your application. You can write a unique policy
per app and control access that way. Diving in a little deeper,
delivering zero trust, AWS Verified Access,
or AVA as I like to call it, AWS Verified Access, AVA. AVA brokers security signals
from some of our partners like Okta or Ping Identity
on the identity side, or CrowdStrike and Jamf
on the device side. It brings these security signals
together and enables you to write policy
using Cedar to guarantee the right kind of access
that you're looking for. You write an application policy
per application, you can group them together
to simplify. You can even write policy
that includes network path, back to Quint’s not an or,
or an and, it's an easier thing for--it's definitely
an easy thing for you to say, “Well, I only want to have access
from these geographies.” You can definitely put that
right into the access policy. Verified access also logs
all of these security data, the access requests
into central logs, which simplifies your security
and audit team’s ability to see what's going on and make sure
that the right things are happening. You can send these logs to your
Siem partners that you're already using, like
Datadog, Rapid7, IBM, Sumo Logic. It makes it easier. We're getting great feedback
already on AVA. In fact, here we've got a quote
from Deloitte. Deloitte is using AVA as part
of their zero trust architecture for their client applications. It helps them deliver security by reducing their configuration
overhead, gives them a central,
unified ingress point, helps them manage access policies
instead of infrastructure, and helps them standardize
and secure their private applications
while expediting new development. We're really proud of the feedback
we're getting so far, and we're looking forward to more. Now, the next use case
I want to talk about is that machine to machine use case. This is sort of an east-west thing. So AVA helps secure the front door
to your application. But once you're inside the castle,
as we like to say, there's often multiple services
that have to work together in order to deliver
the value of your application. This can be just a web server
and a database server, or more likely these days,
it's a collection of microservices that are working together
to deliver value. I talked to one CSO. He said, “I have all these
microservices running on my network and it's hard for me to know
who's talking to what or even if they should be.” It's a really tricky problem
for a lot of our customers. We want to help you eliminate unnecessary network
paths through this. That's the goal. So our customers are solving
this problem in a few ways today. One customer I know is using lots
of micro segmented security groups. This works really well, but this is on the order
of thousands of security groups with security group referencing
and fine detail permissions. It's amazing, but it's
difficult to manage. Some other customers are working
on more of a service mesh kind of architecture. So maybe you'll put a private link at
the front door into your service mesh and then you're running all
these sidecars and your containers. You're managing all those sidecars,
you're patching all those sidecars, you're configuring
all those sidecars. It's a lot. It adds up. Maybe some of you are all in
on serverless, and you've got lambdas and you've got
an API gateway in front, and you're using
IAM access policies, and that's giving you
a lot of security, but maybe you're not
all the way in on serverless. There's a lot of things
that have to work together here. So the net is that we recognize
this as complex, and we knew when we stepped back
to think about how to simplify this, we had this insight. You don't actually want to think
about networking. You want to think about
designing your application. You want to create systems
that work together, that communicate together
in the right way. But you don't want to have to think
about IPs and ports. That's just extra overhead. So we stepped way back. We thought big. And we realized that, you know, we're AWS, we’re giving you
all this compute substrate. Why are we making you think
about networking all the time? It didn't make sense. So that's why we built
Amazon VPC Lattice. VPC Lattice, which is now
GA at the end of March, is a complete re-imagination
of how services communicate, discover and connect to each other. It connects your services at scale
across a variety of different compute substrates,
including EC2, ECS, EKS, Lambda. It all works together. You define specific access policies
on which services can talk to which, and you can even
put in advanced network controls like how to do load distribution to make these things
work well together. Lambda streamlines the service
to service interaction, making you not have to think
about the networking anymore. Now let's look at how you use
Lattice in a zero trust use case. So instead of implementing
all this complexity yourself, you can focus right in
on your application. And then Lattice comes in
and takes over the connectivity. With Lattice, your services
aren't exposed to a network. So what's actually happening is that
when these services communicate, they're communicating in this link
local address space. This is the 169.254 address space. You're already using this to talk
to our instance metadata service, for example. This is our special porthole
to inject AWS capability into your services. And what this means is that you can
actually shut down all open ports
on these microservices. If you go and you try to Nmap
one of these things, it doesn't even show up. It's a really amazing property. So there's no ports open. Additionally, Lattice handles
the connectivity for you, so you don't have to set up network
paths between your services. These can be running across different
VPCs or in different subnets. Lattice just handles figuring out
how to make the connectivity work. On top of that, every request
is authenticated in real time by IAM. You get short lived credentials
between these microservices, and those requests
are constantly checked, and I think as you heard yesterday, IAM is handling a billion
requests every second, and so it's definitely
able to handle the scale. And in net, Lattice helps you weld
that computer shut, which is a really fantastic
security property. So the next thing I want to talk
about is that there's a consistent
through line throughout all of these
zero trust conversations. So we've talked about north south
into the front door. We've talked about east west
between microservices. But there's another dimension,
and that is every time you set a zero trust policy,
you write policy. Zero trust is about defining
very tightly what it is you do trust, and that means writing
a lot of policies, and that means a lot of writing
if it isn't done right. So the idea here is that we knew you needed to be able
to define policies. Now we have a lot of experience
doing that with IAM. Obviously like I just mentioned, we're running IAM
at an incredible scale. We've got tons of years
of experience working on that. It works really well. The problem, though, with zero trust is that the policies that you need
to write in this world are about your business,
your domain, your users. IAM is great, but it only talks about
AWS’s domain of space of things. So we knew we needed something
a little bit different. It needed to represent your world. Now given that we can't use IAM
for this, next, what is it that we need to think about
when we create a policy system? Now, based on our experience, we know
that you need to have something that you can write
the right policies that you need. It needs to be expressive. It needs to be--you need to be able
to clearly write down what you trust. It also needs to be fast. It needs to be really performant. I think that one's obvious. Third, it needs to be provable. Now, this one's less obvious, but it's super important
in a security space. Now, we've made a differentiated
investment here at AWS in automated reasoning. We have an incredible group of people
with formal reasoning background who come in and help us formally
prove a lot of our systems. And through that experience,
we recognized that this provability tenant was incredibly important
in policy design. And so I think you've seen this
by using IAM access analyzer. That product has made
a huge difference in your quality of life, I think. So these are the three sort of core principles around
the right kind of policy system. It has to be expressive,
performant and provable. So again, looking at the options
that we had, I am only about AWS products here. We looked at open source products
like Open Policy Agent or Rego. We looked at some other products
out there, and some of those hit
the expressive part. A lot of them hit
the performant part. Very few of them hit provable. And those that did hit provable
didn't hit expressive. So we realized we needed
something new in the world. And we recognize
that that was a big deal. Introducing a new policy language
is a new thing for us to learn, and that's a challenge. But we were convinced
that we needed to do this, and that's why we introduced Cedar. Cedar’s designed to hit those
three capabilities in a way that
no other policy system can. And we've seen that
to be true so far. Cedar, by the way,
is now open source. So you can see how we built it. You can use it in your applications. I'm really excited about it. At the same time, we saw another
thing happening in the world, and that is a lot of you
are building authentication systems into your own applications. I did this myself before coming
to Amazon as CTO of a company that I co-founded,
and we built this incredibly powerful and complicated authentication system
into our application. It was Ruby on Rails, which I liked, but we had mixed opinions
over the years. It was great. It was custom, it was tailored
to our needs. It worked really well, but it was
really hard to change and it was really hard to get right. And that's what I've heard
a lot of you say. It's hard to get these things right. It's hard to change them. And with this advent of zero trust,
we've been focusing so much more on bringing multiple
security signals into the table, like now that you need to think
about device trust and other things, you often have to go and edit
those authentication systems and authorization systems,
and that's a lot of extra work. And as we see more and more change
and more and more growth in this space, we know there's going to be more and
more undifferentiated heavy lifting. And that's the thing. You're not able to focus
on your business domain when you're dealing
with authorization. So, again, we knew we had
an incredible set of experience with IAM, and then with this revelation
of knowing that we need to use Cedar to help write better policies, we recognized that we could help you
in another way, and that's why we launched
Amazon Verified Permissions, which now became GA yesterday. Verified Permissions is a
scalable permissions management system that gives you fine grained
authorization into your applications. You can embed it deeply
into your systems. Helps you accelerate
application development by not having to worry about
that kind of authorization system. You can just plug it right in. It gives you that authenticated, the proven power of Cedar to help you
protect your data and resources. And it simplifies compliance
audits by logging all of these access
requests centrally, so you can categorically define
who has access to what. Let's look at AVP. I like to shorten things, Amazon Verified Permissions
in a zero trust space. So to get started using AVP, you start by defining
your business domain. You create an entity
mapping of your business objects and the actions
you can take upon them. Often you can figure out a way
to export this from your system, but AVP has to understand
your domain, because, again, you're going
to write policies about your domain. You then integrate AVP’s SDK
into your application, and every time you want to make
an access decision, you call the library. You call the API. You pass in a context, and AVP
responds with permit or forbid. Now, that context can be something
from your own application, like your user identity
and what they’re trying to access. But you can also, if you've put AVA
at the front door, AVA gives you a JSON object
out the back for every request that you can actually just consume,
either pass it on directly to AVP or combine it with your own
application's context to get that entire set of end
to end zero trust. So you can get the authentication
information, you can get device
trust information from AVA. You can layer in maybe the business
model that you're trying to access
and some of the domain information, and you get a really powerful
set of permissions capabilities. Later, you can audit all those
permissions at scale using verified permissions. I think it's a really exciting end
to end story that we're able to bring
to the table now. And I hope you find that
to be true as well. All right. So I'm done talking about
what we have on the truck today. I'm going to bring Quint back
on stage so we can talk about where we're
going to go in the future. Awesome. Thanks, Jess. [applause] Awesome. So the final thought that we want
to share with you all today is a little bit of our vision
for where we see zero trust going, even beyond the evolutions that Jess
has shared with you today, right? If I had one phrase for it,
it would be ubiquitous authorization. We continue to see these worlds
of identity and networking continue
to converge and collide. We saw that originally with that
first guiding principle that I offered for you
about avoiding that binary choice, about how these things
work better together. Continuing from that original example
of the VPC endpoint, we've seen that principle
continue to strengthen and resolve as we've brought you
Amazon Verified Access or VPC Lattice and more. Now another way that we might think
about that are identity and the associated set of signals
like device and behavior are some of the most
important signals into zero trust, while network enforcement points
continue to be some of the most important places
to enforce zero trust, right? And if we're able to think about
these things in this converged way, we might be able to get to a point
where we're able to do what we've never been
able to achieve before: authorization that happens
from the outermost perimeter to the deepest rings within the core, with such sophistication,
adaptability, continuousness, and more, that would have
just been unimaginable or at least unattainable
just years ago. Now we think this represents
some pretty stark ways in which our view
of zero trust differs from other folks in the industry. I absolutely agree that making
perimeter controls more intelligent and sophisticated is absolutely
great incremental progress. But to really get to the value, to really get to the promise
of zero trust, we need to be thinking about
evaluating these access decisions, these authorization decisions across
the entire life span of a request, as it moves from the outermost to the innermost portions
of our organization. Now, why might we think about that? Authentication and identity
has been centralized for years, but authorization has really
been spread to the wind. It's buried, and there's maybe
some group information, and so we might make some coarse
grained decisions in that identity provider. But beyond that, it's buried in file
ACLs, it's buried in table grants, it's buried in all sorts
of downstream systems throughout your enterprise that are literally impossible
to reason about in a collective way, much less gain control
over or audit, right? And so this is in essence
what we think is the fundamental problem to solve. And with your help, we intend
to solve it ubiquitously. Now, in this sense,
ubiquity also implies consistency. We need a couple of things
to make this work. The first thing that we need
consistently across this environment is shared auth context. The identities and contexts
that are operating or that are associated with a request
as it flows through these various enforcement points must
propagate along with the request, even when the request is comprised
of multiple related flows. Think of a simple example of this is a human clicks
a button in an application and that results
in some microservices calls that might end up in a Lambda
function with its own identity that's now operating
on behalf of that human as it goes and retrieves some data. Now, within AWS technology today, this notion of identity propagation
is already there. You might not have seen it,
but if you go and use a service like Amazon Athena,
that you might use to query into S3, Athena understands its role,
its permissions as an AWS service, but it also understands you,
the user, and your permissions
that it's operating on behalf of. Now, within our ecosystem today, there's still a bit of a pivot point,
right? And the example that I described, you can see and reason
about both the human identity and Lambda's identity as it operates
on behalf of the human. But there is that pivot point. We aren't fully converged yet, right? But we see a pathway to getting
that done and work is already well underway. Now, the second thing that we need to
have consistent across this environment is a consistent
authorization evaluation. And Jess just walked you through
the Cedar policy language and its corresponding
evaluation engine, which we really see as our pathway
to giving you this consistency. We see a hierarchy of policies that
logically inherent and stack together to represent the types
of authorization decisions that you want in increasingly
granular ways as you move through the environment. We also see this as one place
to integrate all your signal and context providers. Jess talked about identity
providers, device providers. There's lots of things that need
to feed into these decisions, and we don't want to be doing
those integrations at each and every point of this stack. We want to do it once, and certainly we think that this is
the right layer to do it in, right. Now, again, today just we see half
this world operates in Cedar. You heard Jess talked about the use
of Cedar and verified, access verified permissions, right. But a lot of the world,
the traditional world of AWS, operates in the language of identity
and access management, IAM, right. As an interesting piece
of Amazon history, or not history, but a flavor of color, our existing language internally
is known as Balsa. So I don't know
all the history on it, but apparently we've got
some hobbyist woodworkers afoot somewhere
in the bowels of AWS, right. Okay. And then now the last point
of consistency that we need are this notion of this
combined place to bring together all this logs, all this telemetry. You know, a big part
of what zero trust is, it’s about making all these siloed piece parts
work better together, right? We want to be able to let those
security tools do their job, but omit telemetry
that goes into a place that we can reason about collectively and ideally bring that flywheel
back around and help inform all those various
enforcement points, right. So now finally, we're going to wrap
all of that in AWS opinionated guidance, right,
back to some of those questions I shared at the onset. Where do I start?
How do I get going? What should I do next? Where is my risk? Where can I make a meaningful impact,
right? And we're going to lead you along
the way, along those journeys, right? So, listen, there's a lot
to digest here, right? We look forward to your continued
feedback as we go about building this vision, but we think we're meaningfully
on our way towards making it real. We talked today about
how verified access might be that enforcement
point for applications, verify permissions for app logic. You've got things that we didn't
even talk about today, session manager and others
for infrastructure, Lattice for microservices. And we're going to continue
to converge these worlds of networking and identity
that are going to fill in even further vertical slivers
of this diagram and many more, right? So we think we're on our way
to making it a real—we really think we're on our way to making
this vision a reality for you, right? And we'd like to offer that we think
we're ready in a position to have authorization join this club of ubiquity
alongside encryption, right. We long ago recognized that this
consistent authorization vision was necessary, right. When we built AWS, you know,
again, all these services that have this one
common authorization language, right. And think now as we apply zero trust,
AWS applying that same rigor, that same philosophy
of ubiquitous authorization, as Jess explained, even into
your domain, beyond our domain. So we aren't there yet, but we
really think that when we get there, we're going to have something
that really delights you. Now to close it out, we have
an Amazon expression that it's always day one, right? And that's just really our way of
making sure we stay in the mentality that we're building and innovating
on your behalf each and every day. So we're definitely well underway
on this journey, right? You can go back to the earliest days
of AWS and how folks are using
our API calls over the world's most untrustworthy network
in the world, the Internet, to call and query
their most sensitive data. We've been at this for a long time, and we think we've made
some meaningful progress in what we've shared
with you here today about how bringing
together things in a more packaged
and more refined way, right. But we think that where we're
going again is unique, right. And we really look forward to you all keeping--to going along
on this journey along with us. And so with that,
really appreciate your time today. I look forward to your feedback. Please do fill out your surveys. We really take that meaningfully. And if you all, any of you
all have questions or would like to talk about
zero trust in greater depth, Jess and I are going to hang out
in the hallway after a quick second to take any questions
that you might have. So thanks and enjoy the rest
of your time here at re:Inforce. [applause]

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=0s) Hey, all.
I'm Jess Szmajda.

[00:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1s) I'm the general manager of some of
our security services here at AWS,

[00:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=4s) including Network
Firewall and Firewall Manager.

[00:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=7s) Previously, I built--I
led the team

[00:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=9s) that built AWS Verified Access,
our first higher level service

[00:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=12s) that helps you simplify
zero trust on AWS.

[00:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=15s) Today I'm joined by Quint Van Deman
from the office of our CSO.

[00:18](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=18s) Quint's been leading our AWS

[00:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=20s) zero trust efforts
for a few years now

[00:22](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=22s) and has had thousands
of conversations with customers

[00:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=24s) just like you on what we can do to
help you on your Zero Trust journey.

[00:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=28s) So I'm going to let Quint
take it away now.

[00:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=29s) Awesome.
Thanks, Jess.

[00:31](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=31s) Thanks for joining us, everybody.

[00:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=32s) So let's get into things.

[00:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=34s) Now, bar raising security
has been central to AWS

[00:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=38s) since the beginning.

[00:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=40s) It always has been and continues
to be our top priority.

[00:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=43s) And you see the intention
of this security

[00:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=47s) resulting in security architectures
that we think are absolutely bar

[00:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=50s) raising in terms of what
you can build on AWS.

[00:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=54s) You know, I'm talking
about features

[00:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=55s) that maybe you haven't
thought about for a while,

[00:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=57s) because it's just sort of the way
the cloud has always worked.

[00:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=59s) But software defined
micro perimeters,

[01:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=61s) request level authentication
and authorization,

[01:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=64s) accurate maintenance-free
state inventory or state

[01:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=68s) and inventory data,
machine identities

[01:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=70s) with cryptographically
verifiable hardware root of trust,

[01:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=75s) credential distribution
at hyper scale and so on.

[01:18](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=78s) All of these types of concepts
would be very,

[01:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=80s) very familiar in any conversation
in and around zero trust.

[01:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=84s) And that's what we're going
to talk about today.

[01:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=87s) All right.

[01:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=88s) So I'm going to start by doing
a little grounding with us today.

[01:31](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=91s) We'll talk a little bit
about motivations.

[01:33](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=93s) We'll talk a little bit
about what AWS thinks zero trust

[01:37](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=97s) is in terms of
the necessary definitions

[01:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=100s) and maybe some guiding
principles and tenets.

[01:42](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=102s) Then I'm going to turn it
over to Jess.

[01:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=104s) And as she mentioned a little bit,
she's going to talk to you about

[01:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=108s) what's new for us
in this space, right.

[01:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=110s) We've had some really
important innovations on your behalf

[01:53](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=113s) in the--particularly
throughout this spring

[01:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=115s) and leading up to here at re:Inforce
that she's going to walk through,

[01:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=119s) and then I'll take back
over at the end,

[02:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=120s) and we're going to do
a little bit of envisioning.

[02:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=122s) I want to give you a little bit
of a feel

[02:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=123s) of where we're
going in this space.

[02:06](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=126s) It's not the reality
of the world today,

[02:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=128s) but I think it's important
for you to understand

[02:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=130s) how we see this world
continuing to evolve

[02:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=132s) and what we're going
to continue to bring for you.

[02:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=137s) Now, as just mentioned,
over the last handful of years,

[02:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=140s) I've had the chance to talk
with countless numbers

[02:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=143s) of great customers
such as yourselves.

[02:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=145s) And we really, when we sit down,

[02:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=147s) we really work hard
to meet you all where you are.

[02:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=150s) That means listening to your specific

[02:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=152s) outcomes that you're after in terms
of the business side of zero trust.

[02:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=156s) It means understanding and detailing
the technical challenges

[02:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=159s) that you're after, right?

[02:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=161s) It means understanding the existing
security architectures

[02:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=164s) that you have, the existing
investments that you've made

[02:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=167s) and how we might go about
layering zero trust on top of that.

[02:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=172s) But the key in the end of that
is that getting to zero trust

[02:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=176s) sort of depends on where
you're starting, where you're at.

[03:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=180s) Now, for some customers, the move
towards zero trust

[03:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=184s) has been just self-motivated.

[03:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=187s) It's a natural, logical iteration

[03:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=189s) of the continued evolution
of cyber security in general

[03:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=193s) and defense in depth in particular.

[03:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=196s) For other customers, the motivation
has been driven by public policy

[03:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=200s) and regulation
from all corners of the world.

[03:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=203s) But in general, the security risks
we face are pressing,

[03:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=207s) and they're guiding you all to be
more precise about the controls

[03:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=212s) that you use to control access
and audit the same.

[03:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=216s) We're always after this raising
of the security bar.

[03:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=219s) So despite the hype, despite the fact
that it in some ways

[03:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=224s) became whitewashed across
everything across the industry,

[03:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=227s) we really believe
in this term, zero trust, right?

[03:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=231s) We believe deeply in the outcomes
and the benefits that it provides.

[03:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=234s) And we've done so in our own
organization across Amazon,

[03:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=239s) across AWS for many,

[04:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=240s) many years where we've been
putting those concepts to work.

[04:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=243s) Right?

[04:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=244s) So this really is--we do
fundamentally believe

[04:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=247s) that zero trust,
despite some of the hype,

[04:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=249s) does lead to better
security outcomes and success.

[04:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=253s) So now through those conversations,

[04:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=255s) there were a bunch of points
of commonality

[04:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=257s) that always continue to come back.

[04:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=260s) Customers
had questions like,

[04:21](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=261s) “Where do I start?

[04:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=263s) What does good look like?

[04:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=264s) How do I explain zero trust
to my organization?

[04:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=267s) How do I leverage the investments
that I've made?”

[04:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=270s) We're not starting from scratch here.

[04:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=272s) But ultimately, all of that tends
to end up circling around

[04:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=275s) and coming back to a very
practical question like this one,

[04:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=279s) which is sort of the age old
question of security in the cloud.

[04:42](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=282s) I think this is a great question
to form

[04:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=284s) as the backdrop for zero trust,

[04:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=285s) because it just allows us
to be practical, better every day.

[04:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=289s) And if we're going to--and zero trust
is increasingly the term

[04:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=292s) that we might use to describe
what good looks like here.

[04:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=295s) But if we anchor on this question,

[04:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=297s) it really helps us
move forward effectively.

[05:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=300s) Okay.

[05:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=301s) So invariably, you know,
the world needs definitions

[05:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=305s) to get going on zero trust.

[05:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=307s) And this is the one that
we've offered for many years now,

[05:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=310s) that Zero Trust is a conceptual model
and an associated set of mechanisms

[05:14](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=314s) that focus on providing security
controls around digital assets

[05:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=317s) that do not solely
or fundamentally depend

[05:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=320s) on traditional network
parameters.

[05:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=323s) Now, instead, we're going
to rely on identity, device,

[05:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=327s) other advanced signals to bring in
and make ever more continuous,

[05:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=332s) adaptive and sophisticated access
control decisions.

[05:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=339s) Now, the other thing I want
to bring your attention to

[05:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=341s) is that we're very deliberate,
that this is a security model, right?

[05:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=345s) Zero trust is not something
you're going to buy.

[05:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=347s) You may buy products.

[05:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=348s) You might buy products from AWS.

[05:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=350s) You might buy products from
our great partner organizations.

[05:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=352s) You might build products or services
that help you get to zero trust.

[05:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=356s) But you need to start by
considering it as a security model.

[05:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=359s) It's not a simple checkbox thing

[06:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=361s) that you're going
to buy off the shelf.

[06:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=365s) Okay, so now definitions
are necessary.

[06:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=369s) But at Amazon we really find
that guiding principles or tenants,

[06:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=373s) as we might call them, really help
sharpen our thinking in this space.

[06:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=377s) And we've been offering
a number of guiding principles

[06:21](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=381s) to our customers for a while
that we'll walk through here today.

[06:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=387s) The first is simply to avoid
a binary choice.

[06:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=392s) It's pretty easy to get going
in any zero trust conversation,

[06:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=396s) and someone will invariably
throw out

[06:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=398s) something to the effect
of the network perimeter is dead.

[06:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=401s) Long live the identity
centric perimeter,

[06:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=403s) or perhaps vice versa, depending
on their particular persuasion.

[06:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=407s) But we really think that
that's a false choice, right?

[06:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=410s) While network perimeters like as
what we sort of just walked through,

[06:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=414s) we no longer want to think of
as sufficient, they're very useful,

[06:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=418s) they're very well understood,
they're very easy to reason about.

[07:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=421s) They've been around a long time.

[07:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=422s) There's a lot of strong skillset
and expertise

[07:06](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=426s) within many of your organizations,

[07:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=428s) most of your organizations
around how to do network security.

[07:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=432s) Now, inside of that, you know,
often identity centric controls

[07:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=437s) can provide greater levels
of granularity.

[07:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=439s) You've been using identity
centric controls

[07:21](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=441s) to talk
to the cloud for years,

[07:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=443s) literally since the dawn
of the cloud, right?

[07:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=446s) But ideally, those two things
shouldn't be an and,

[07:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=449s) they should be an or right.

[07:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=452s) They ought to work together
in good harmony.

[07:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=454s) And ideally, not only should
they coexist,

[07:37](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=457s) but they should be aware
of one another right?

[07:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=459s) Now, the original example,
or at least the most sort of easy

[07:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=465s) to get a hold of example
was something like a VPC endpoint.

[07:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=468s) So this was a control at the edge
of your network

[07:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=471s) that understood
the identities, resources and network

[07:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=474s) locations involved
that were flowing across it.

[07:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=477s) And you could write a policy that
understood all of those dimensions

[08:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=481s) and really delivered
excellent access control.

[08:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=484s) So we're going to see today how
this theme of this convergence

[08:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=489s) has continued to evolve
in some of the new services.

[08:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=492s) But this is a really important point
that you don't need to throw out

[08:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=495s) what's been working
in order to get to what's next.

[08:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=500s) Now the second guiding principle
that we've been offering to you

[08:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=504s) for a while is this notion of working
backwards from your use cases.

[08:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=508s) When we originally started
talking with customers

[08:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=510s) a good handful of years ago,

[08:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=512s) we largely saw synergy
around these three, right,

[08:37](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=517s) about how you get humans
to applications.

[08:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=520s) The proverbial any user from any
coffee shop anywhere in the world,

[08:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=524s) no VPN required.

[08:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=525s) How we might think about moving
zero trust into the data center,

[08:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=529s) service to service, machine
to machine, a lot of names there.

[08:53](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=533s) And then sort of a broad bucket
for stuff that existed

[08:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=536s) wholly outside the corporate
network entirely, right?

[08:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=539s) The IoT enabled wind turbine
or oil tank

[09:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=543s) sitting well outside
the corporate network,

[09:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=545s) beaming critical telemetry
to the cloud.

[09:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=547s) And what's interesting about
those use cases is that they share

[09:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=551s) these very same, these very familiar
underlying technical principles.

[09:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=555s) We want to get away from the network.

[09:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=556s) We want to bring identity
and other contexts to bear.

[09:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=559s) But at the same time, they're very
different in the objectives

[09:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=563s) thereafter or the outcomes
that they're after.

[09:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=568s) The first might be about mobility.

[09:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=570s) It might be about workforce
happiness,

[09:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=572s) it might be about work from home
in the middle of a pandemic.

[09:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=575s) The second is typically about
reducing pathways

[09:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=578s) through--unnecessary pathways,
through our organization,

[09:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=581s) particularly those
that lead to data, right?

[09:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=585s) But if we focus on use cases,
again, we get very practical.

[09:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=589s) We get really focused on the problems
that we're trying to solve,

[09:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=592s) and we avoid getting mired in this
what is or what is not zero trust

[09:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=597s) that can often bleed too much
into these conversations, right.

[10:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=601s) And so I really strongly encourage
you to think

[10:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=603s) about zero trust is the how.

[10:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=605s) Zero trust isn't the what.

[10:06](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=606s) You aren't implementing
zero trust for zero trust sake.

[10:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=609s) You're implementing zero trust
for a business outcome

[10:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=612s) or a technical outcome

[10:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=613s) that are generally going
to align to these use cases.

[10:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=616s) Now, in the time since then, again,
there was maybe as folks

[10:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=620s) got a little bit further
down the path of understanding

[10:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=623s) and implementing zero trust,

[10:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=625s) other use cases
have clearly come to light

[10:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=627s) that are generally now
sort of bucketed

[10:31](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=631s) under the banner of zero trust.

[10:33](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=633s) There's likely many more,
but maybe a few others

[10:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=636s) that I'll sort of explicitly call
out, operator to workload, right.

[10:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=639s) How distinct from a business
user accessing

[10:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=643s) an application
through a web browser,

[10:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=645s) maybe think about this as how
an operator might go in through SSH

[10:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=649s) to get to a,
you know, an operating system

[10:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=651s) or a database engine, right.

[10:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=654s) Human to data, whether that's
in the realm of data science

[10:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=658s) or otherwise, right.

[10:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=659s) Where we've got folks that have--that
need by the function

[11:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=662s) of what they're trying to do, very
close and intimate access to data.

[11:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=667s) But we also obviously that data has
a lot of sensitivity to it, right?

[11:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=670s) And how can we bring
zero trust principles

[11:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=672s) to make sure that very intimate
access is carefully controlled?

[11:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=676s) And then perhaps it's one of the,
you know,

[11:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=680s) a bit further down
the maturity curve,

[11:21](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=681s) but how can we even think
about taking zero trust

[11:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=684s) to its ultimate state,

[11:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=686s) where the things
that we're considering

[11:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=688s) in terms of access decisions
are way down within the applications,

[11:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=692s) even more granular than something
you might get

[11:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=695s) from a cloud API call, right?

[11:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=698s) And so all of this brings me,
oh, sorry,

[11:42](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=702s) and finally,
our last principle, right?

[11:46](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=706s) That simply that zero trust is still
in a relatively nascent state.

[11:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=710s) It still is not something
that we think one size fits all.

[11:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=715s) Now, that's relatively
decent guidance

[11:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=717s) for just about anything
in the cloud, right?

[12:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=720s) If you try to wedge everything
into one,

[12:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=724s) friction is going to ensue for
your workforce and otherwise, right.

[12:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=727s) So use this where it really matters.

[12:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=730s) Start with protecting--or start by
using zero trust

[12:14](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=734s) to protect the things
that really matter the most to you,

[12:18](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=738s) and use that as a way
to credibly build experience,

[12:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=740s) muscle memory and authenticity

[12:22](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=742s) in the way
you might roll it out more broadly.

[12:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=745s) At the same time, we really think
of this as a way to give you—

[12:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=750s) to let you retire some of the controls
that you've had for a while,

[12:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=754s) but they're probably brittle,

[12:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=755s) and they're probably not
really adding much value, right?

[12:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=758s) Maybe we think of the VPN and some
of those things in that light.

[12:42](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=762s) So not only is it guidance to help
you understand where you should,

[12:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=768s) you know, use zero trust
and extend your security model,

[12:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=771s) but also think of this principle

[12:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=772s) as a way to let's use it
to simplify things

[12:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=775s) and get things out that are
no longer really doing their job.

[13:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=782s) Okay, so now we regularly get
feedback that indicates

[13:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=785s) that these principles are
really helping folks stay grounded

[13:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=788s) and focused on improving
their security each

[13:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=791s) and every day
in very practical and real ways.

[13:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=793s) And I hope that that will help you
in a similar fashion.

[13:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=797s) But customers don't just share
what's worked, of course.

[13:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=800s) They share there--as you continue
to share, as you should,

[13:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=803s) for sure, continue to share
your fair share of suggestions

[13:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=807s) and capabilities
that we can improve upon,

[13:31](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=811s) where we could provide
more assistance.

[13:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=814s) So there's lots of permutations
of use cases out there.

[13:37](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=817s) But again, those first two that I
mentioned around humans

[13:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=820s) to applications and controlling
flow of data are very common

[13:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=824s) and are often expressed back to back.

[13:46](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=826s) And you all have really told us
that you want to be able to integrate

[13:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=830s) and fuse your technology
investments in a way

[13:53](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=833s) that just gets
to those better outcomes

[13:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=836s) rather than those siloed piece parts.

[13:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=838s) So Jess is going to talk to you
a bit more about the services

[14:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=841s) that we're building that bring you
these capabilities

[14:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=845s) with much less assembly
required, much more AWS

[14:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=850s) opinionated guidance built in, right.

[14:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=852s) Now, before I turn it over to her
here, you know,

[14:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=855s) for context what you all were
experiencing, right,

[14:18](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=858s) as we gave you
at first those lower level primitives

[14:22](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=862s) is a long held Amazon belief.

[14:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=864s) In short, primitives, not frameworks.

[14:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=866s) Our Amazon CTO, Werner Vogels wrote
and spoke about this extensively

[14:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=872s) when he reflected
on the first 10 years of AWS.

[14:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=875s) But in short, it's our very
deliberate way of building software

[14:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=879s) and systems from the bottom up,
and there's a lot to unpack here.

[14:42](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=882s) And if you're interested,
I'd encourage you to read his blog

[14:46](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=886s) about how successful complex systems

[14:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=888s) must evolve out of collections
of simple systems.

[14:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=892s) But for zero trust specifically,
this really guides us in decomposing

[14:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=897s) big and ambiguous problems,
where the clarity of the end state

[15:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=901s) isn't nearly as good as the clarity
of where we might begin.

[15:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=905s) And this allows us to make progress
while continuing to gain insights,

[15:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=909s) what's working, what's not,

[15:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=911s) and ensuring that we're being
very deliberate

[15:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=913s) in working backwards from your pain
points, not our preconceived notions.

[15:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=917s) So I'd like to bring in Jess to share
with you how those very insights

[15:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=920s) have led to the next generation
of higher level

[15:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=923s) zero trust focused services.

[15:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=925s) Jess, take it away.

[15:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=926s) Thanks, Quint.

[15:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=928s) [applause]

[15:33](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=933s) So let's learn a little bit more
about how AWS is helping you

[15:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=935s) simplify zero trust
in your organizations.

[15:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=939s) So something we've observed is that
when we give you

[15:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=941s) those sort
of flexible primitives and tools

[15:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=944s) that we had Werner talk about there
for a second in text,

[15:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=949s) you do something
that's really amazing.

[15:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=950s) Not only do you use them to solve
the problems

[15:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=952s) that we expect you to solve,
but you also solve problems

[15:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=954s) that we had no idea
you were going to solve.

[15:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=956s) You find interesting opportunities
to apply

[15:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=958s) these technologies to problems
that crop up in your world,

[16:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=961s) and that's really exciting,

[16:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=963s) because then my job is to come
and talk to you,

[16:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=965s) learn about the problems
you're solving,

[16:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=967s) and find better ways
to solve those problems.

[16:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=969s) And through that sort of
iterative cycle,

[16:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=970s) we build even better systems for each
other and make the world go better.

[16:14](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=974s) So in the world of zero trust,

[16:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=977s) this means that we're focusing on
simple foundational services

[16:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=980s) that you can use
to solve those use cases

[16:22](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=982s) that Quint talked about directly.

[16:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=984s) And then over time, we'll find better
ways to make it even simpler for you.

[16:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=989s) So I want to talk by diving deeper
into that first use case,

[16:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=992s) which is the human to app use case.

[16:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=994s) This is somebody sitting
in a coffee shop,

[16:37](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=997s) maybe working from home, accessing
a secure corporate application.

[16:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1001s) Now, this is a dynamic security
environment.

[16:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1003s) There's a lot of things going on
in this space,

[16:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1005s) and it's not the same kind of thing
that we've been used to,

[16:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1007s) where you have a worker on a
corporate network that you can trust.

[16:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1011s) So how do you establish trust
in this situation

[16:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1014s) between somebody who may
have left her laptop open

[16:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1017s) or may have needed to get
patches installed on a machine

[17:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1020s) and get sensitive data accessed?

[17:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1022s) It's a tricky thing.

[17:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1025s) Now, a lot of you have been solving
this with a variety of techniques.

[17:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1028s) The first one is obviously VPN.

[17:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1030s) In my last role before I came over
to Network Firewall,

[17:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1032s) I was the GM of VPN.

[17:14](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1034s) And so I understand VPN.

[17:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1035s) VPN is fantastic.

[17:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1036s) Don't get me wrong,
I'd love to sell you more VPN.

[17:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1039s) The challenge with VPN is you log in
at the front door,

[17:22](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1042s) you get access
to the corporate network.

[17:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1044s) Maybe you re-authenticate
from time to time,

[17:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1046s) but you still have to dial
into the network

[17:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1048s) and then you get other challenges
of getting your data transferred.

[17:31](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1051s) Maybe somebody's trying
to go to YouTube.

[17:33](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1053s) It gets a little complicated
in some other ways.

[17:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1055s) On the other hand, some of you

[17:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1056s) who have been securing
your Web applications

[17:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1058s) by putting them directly
on the Internet

[17:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1060s) and layering various security
services like Shield or WAF,

[17:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1064s) and helping you establish trust

[17:46](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1066s) from that untrusted endpoint
into your application.

[17:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1071s) But again, usually these rely on
authenticating once at the front door

[17:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1076s) and you can control session length,
but that can get pretty annoying.

[17:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1079s) So we knew this could be simpler.

[18:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1081s) And I think a lot of you have seen
a lot of ways

[18:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1082s) that this could be simpler,
and that's why we introduced AWS

[18:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1085s) Verified Access,
which is now GA at the end of April.

[18:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1090s) Access helps you simplify access
to corporate applications

[18:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1093s) using zero trust principles.

[18:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1095s) Instead of having to check
just once at login,

[18:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1097s) verified access checks
every request in real time

[18:21](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1101s) based on the latest security data,
using policies that you define.

[18:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1105s) Your end users get seamless
experience

[18:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1107s) accessing their corporate
applications

[18:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1110s) and instead of having
to assemble multiple services,

[18:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1112s) you just put verified access
in front of your application.

[18:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1115s) You can write a unique policy
per app and control access that way.

[18:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1120s) Diving in a little deeper,
delivering zero trust,

[18:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1123s) AWS Verified Access,
or AVA as I like to call it,

[18:46](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1126s) AWS Verified Access, AVA.

[18:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1129s) AVA brokers security signals
from some of our partners like Okta

[18:53](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1133s) or Ping Identity
on the identity side,

[18:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1135s) or CrowdStrike and Jamf
on the device side.

[18:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1138s) It brings these security signals
together

[19:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1140s) and enables you to write policy
using Cedar

[19:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1144s) to guarantee the right kind of access
that you're looking for.

[19:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1147s) You write an application policy
per application,

[19:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1150s) you can group them together
to simplify.

[19:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1152s) You can even write policy
that includes network path,

[19:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1155s) back to Quint’s not an or,
or an and, it's an easier thing

[19:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1159s) for--it's definitely
an easy thing for you to say,

[19:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1160s) “Well, I only want to have access
from these geographies.”

[19:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1163s) You can definitely put that
right into the access policy.

[19:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1166s) Verified access also logs
all of these security data,

[19:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1170s) the access requests
into central logs,

[19:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1172s) which simplifies your security
and audit team’s ability

[19:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1174s) to see what's going on and make sure
that the right things are happening.

[19:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1178s) You can send these logs to your
Siem partners

[19:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1180s) that you're already using, like
Datadog, Rapid7, IBM, Sumo Logic.

[19:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1185s) It makes it easier.

[19:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1189s) We're getting great feedback
already on AVA.

[19:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1192s) In fact, here we've got a quote
from Deloitte.

[19:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1194s) Deloitte is using AVA as part
of their zero trust architecture

[19:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1196s) for their client applications.

[19:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1199s) It helps them deliver security

[20:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1201s) by reducing their configuration
overhead,

[20:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1203s) gives them a central,
unified ingress point,

[20:06](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1206s) helps them manage access policies
instead of infrastructure,

[20:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1209s) and helps them standardize
and secure their private

[20:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1211s) applications
while expediting new development.

[20:14](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1214s) We're really proud of the feedback
we're getting so far,

[20:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1216s) and we're looking forward to more.

[20:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1220s) Now, the next use case
I want to talk about

[20:22](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1222s) is that machine to machine use case.

[20:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1225s) This is sort of an east-west thing.

[20:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1227s) So AVA helps secure the front door
to your application.

[20:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1232s) But once you're inside the castle,
as we like to say,

[20:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1235s) there's often multiple services
that have to work together

[20:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1238s) in order to deliver
the value of your application.

[20:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1241s) This can be just a web server
and a database server,

[20:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1244s) or more likely these days,
it's a collection of microservices

[20:46](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1246s) that are working together
to deliver value.

[20:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1249s) I talked to one CSO.

[20:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1251s) He said, “I have all these
microservices running on my network

[20:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1254s) and it's hard for me to know
who's talking

[20:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1256s) to what or even if they should be.”

[20:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1258s) It's a really tricky problem
for a lot of our customers.

[21:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1262s) We want to help you eliminate

[21:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1263s) unnecessary network
paths through this.

[21:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1265s) That's the goal.

[21:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1267s) So our customers are solving
this problem in a few ways today.

[21:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1271s) One customer I know is using lots
of micro segmented security groups.

[21:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1276s) This works really well,

[21:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1277s) but this is on the order
of thousands of security groups

[21:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1280s) with security group referencing
and fine detail permissions.

[21:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1283s) It's amazing, but it's
difficult to manage.

[21:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1286s) Some other customers are working
on more of a service

[21:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1290s) mesh kind of architecture.

[21:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1292s) So maybe you'll put a private link at
the front door into your service mesh

[21:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1295s) and then you're running all
these sidecars and your containers.

[21:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1298s) You're managing all those sidecars,
you're patching all those sidecars,

[21:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1301s) you're configuring
all those sidecars.

[21:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1303s) It's a lot.

[21:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1304s) It adds up.

[21:46](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1306s) Maybe some of you are all in
on serverless,

[21:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1308s) and you've got lambdas and you've got
an API gateway in front,

[21:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1311s) and you're using
IAM access policies,

[21:53](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1313s) and that's giving you
a lot of security,

[21:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1315s) but maybe you're not
all the way in on serverless.

[21:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1318s) There's a lot of things
that have to work together here.

[22:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1321s) So the net is that we recognize
this as complex,

[22:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1325s) and we knew when we stepped back
to think about how to simplify this,

[22:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1328s) we had this insight.

[22:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1330s) You don't actually want to think
about networking.

[22:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1332s) You want to think about
designing your application.

[22:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1335s) You want to create systems
that work together,

[22:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1337s) that communicate together
in the right way.

[22:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1339s) But you don't want to have to think
about IPs and ports.

[22:21](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1341s) That's just extra overhead.

[22:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1344s) So we stepped way back.

[22:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1345s) We thought big.

[22:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1346s) And we realized that, you know,

[22:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1349s) we're AWS, we’re giving you
all this compute substrate.

[22:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1352s) Why are we making you think
about networking all the time?

[22:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1354s) It didn't make sense.

[22:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1356s) So that's why we built
Amazon VPC Lattice.

[22:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1361s) VPC Lattice, which is now
GA at the end of March,

[22:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1364s) is a complete re-imagination
of how services communicate,

[22:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1368s) discover and connect to each other.

[22:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1370s) It connects your services at scale
across a variety of different

[22:53](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1373s) compute substrates,
including EC2, ECS, EKS, Lambda.

[23:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1380s) It all works together.

[23:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1382s) You define specific access policies
on which services can talk to which,

[23:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1387s) and you can even
put in advanced network controls

[23:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1389s) like how to do load distribution

[23:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1391s) to make these things
work well together.

[23:14](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1394s) Lambda streamlines the service
to service interaction,

[23:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1397s) making you not have to think
about the networking anymore.

[23:21](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1401s) Now let's look at how you use
Lattice in a zero trust use case.

[23:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1405s) So instead of implementing
all this complexity yourself,

[23:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1408s) you can focus right in
on your application.

[23:31](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1411s) And then Lattice comes in
and takes over the connectivity.

[23:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1416s) With Lattice, your services
aren't exposed to a network.

[23:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1420s) So what's actually happening is that
when these services communicate,

[23:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1423s) they're communicating in this link
local address space.

[23:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1425s) This is the 169.254 address space.

[23:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1429s) You're already using this to talk
to our instance metadata service,

[23:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1432s) for example.

[23:53](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1433s) This is our special porthole
to inject AWS

[23:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1436s) capability into your services.

[23:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1438s) And what this means is that you can
actually shut down

[24:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1442s) all open ports
on these microservices.

[24:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1445s) If you go and you try to Nmap
one of these things,

[24:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1447s) it doesn't even show up.

[24:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1449s) It's a really amazing property.

[24:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1451s) So there's no ports open.

[24:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1453s) Additionally, Lattice handles
the connectivity for you,

[24:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1456s) so you don't have to set up network
paths between your services.

[24:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1460s) These can be running across different
VPCs or in different subnets.

[24:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1464s) Lattice just handles figuring out
how to make the connectivity work.

[24:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1469s) On top of that, every request
is authenticated in real time by IAM.

[24:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1475s) You get short lived credentials
between these microservices,

[24:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1478s) and those requests
are constantly checked,

[24:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1480s) and I think as you heard yesterday,

[24:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1481s) IAM is handling a billion
requests every second,

[24:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1485s) and so it's definitely
able to handle the scale.

[24:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1488s) And in net, Lattice helps you weld
that computer shut,

[24:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1492s) which is a really fantastic
security property.

[24:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1498s) So the next thing I want to talk
about

[25:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1500s) is that there's a consistent
through line

[25:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1502s) throughout all of these
zero trust conversations.

[25:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1504s) So we've talked about north south
into the front door.

[25:06](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1506s) We've talked about east west
between microservices.

[25:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1509s) But there's another dimension,
and that is every time

[25:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1512s) you set a zero trust policy,
you write policy.

[25:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1516s) Zero trust is about defining
very tightly what it is you do trust,

[25:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1520s) and that means writing
a lot of policies,

[25:22](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1522s) and that means a lot of writing
if it isn't done right.

[25:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1526s) So the idea here is that we knew

[25:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1529s) you needed to be able
to define policies.

[25:31](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1531s) Now we have a lot of experience
doing that with IAM.

[25:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1535s) Obviously like I just mentioned,

[25:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1536s) we're running IAM
at an incredible scale.

[25:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1538s) We've got tons of years
of experience working on that.

[25:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1541s) It works really well.

[25:42](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1542s) The problem, though, with zero trust

[25:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1544s) is that the policies that you need
to write in this world

[25:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1547s) are about your business,
your domain, your users.

[25:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1552s) IAM is great, but it only talks about
AWS’s domain of space of things.

[25:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1557s) So we knew we needed something
a little bit different.

[25:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1559s) It needed to represent your world.

[26:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1562s) Now given that we can't use IAM
for this, next, what is it

[26:06](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1566s) that we need to think about
when we create a policy system?

[26:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1570s) Now, based on our experience, we know
that you need to have something

[26:14](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1574s) that you can write
the right policies that you need.

[26:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1577s) It needs to be expressive.

[26:18](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1578s) It needs to be--you need to be able
to clearly write down what you trust.

[26:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1584s) It also needs to be fast.

[26:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1585s) It needs to be really performant.

[26:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1587s) I think that one's obvious.

[26:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1589s) Third, it needs to be provable.

[26:31](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1591s) Now, this one's less obvious,

[26:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1592s) but it's super important
in a security space.

[26:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1595s) Now, we've made a differentiated
investment here at AWS

[26:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1598s) in automated reasoning.

[26:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1600s) We have an incredible group of people
with formal reasoning background

[26:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1603s) who come in and help us formally
prove a lot of our systems.

[26:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1607s) And through that experience,
we recognized that this provability

[26:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1611s) tenant was incredibly important
in policy design.

[26:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1615s) And so I think you've seen this
by using IAM access analyzer.

[26:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1619s) That product has made
a huge difference

[27:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1620s) in your quality of life, I think.

[27:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1622s) So these are the three sort of core

[27:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1625s) principles around
the right kind of policy system.

[27:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1627s) It has to be expressive,
performant and provable.

[27:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1632s) So again, looking at the options
that we had,

[27:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1636s) I am only about AWS products here.

[27:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1640s) We looked at open source products
like Open Policy Agent or Rego.

[27:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1644s) We looked at some other products
out there,

[27:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1646s) and some of those hit
the expressive part.

[27:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1650s) A lot of them hit
the performant part.

[27:33](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1653s) Very few of them hit provable.

[27:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1655s) And those that did hit provable
didn't hit expressive.

[27:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1659s) So we realized we needed
something new in the world.

[27:42](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1662s) And we recognize
that that was a big deal.

[27:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1664s) Introducing a new policy language
is a new thing for us to learn,

[27:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1669s) and that's a challenge.

[27:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1670s) But we were convinced
that we needed to do this,

[27:53](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1673s) and that's why we introduced Cedar.

[27:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1675s) Cedar’s designed to hit those
three capabilities

[27:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1678s) in a way that
no other policy system can.

[28:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1680s) And we've seen that
to be true so far.

[28:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1683s) Cedar, by the way,
is now open source.

[28:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1685s) So you can see how we built it.

[28:06](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1686s) You can use it in your applications.

[28:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1688s) I'm really excited about it.

[28:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1691s) At the same time, we saw another
thing happening in the world,

[28:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1696s) and that is a lot of you
are building authentication systems

[28:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1699s) into your own applications.

[28:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1704s) I did this myself before coming
to Amazon as CTO

[28:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1708s) of a company that I co-founded,
and we built this incredibly powerful

[28:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1712s) and complicated authentication system
into our application.

[28:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1715s) It was Ruby on Rails, which I liked,

[28:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1718s) but we had mixed opinions
over the years.

[28:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1721s) It was great.

[28:42](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1722s) It was custom, it was tailored
to our needs.

[28:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1725s) It worked really well, but it was
really hard to change

[28:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1727s) and it was really hard to get right.

[28:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1729s) And that's what I've heard
a lot of you say.

[28:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1731s) It's hard to get these things right.

[28:53](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1733s) It's hard to change them.

[28:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1734s) And with this advent of zero trust,
we've been focusing so much more

[28:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1737s) on bringing multiple
security signals into the table,

[29:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1740s) like now that you need to think
about device trust and other things,

[29:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1743s) you often have to go and edit
those authentication systems

[29:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1745s) and authorization systems,
and that's a lot of extra work.

[29:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1750s) And as we see more and more change
and more

[29:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1753s) and more growth in this space,

[29:14](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1754s) we know there's going to be more and
more undifferentiated heavy lifting.

[29:18](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1758s) And that's the thing.

[29:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1759s) You're not able to focus
on your business domain

[29:21](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1761s) when you're dealing
with authorization.

[29:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1764s) So, again, we knew we had
an incredible

[29:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1766s) set of experience with IAM,

[29:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1768s) and then with this revelation
of knowing that we need to use Cedar

[29:31](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1771s) to help write better policies,

[29:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1774s) we recognized that we could help you
in another way,

[29:37](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1777s) and that's why we launched
Amazon Verified Permissions,

[29:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1780s) which now became GA yesterday.

[29:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1783s) Verified Permissions is a
scalable permissions management system

[29:46](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1786s) that gives you fine grained
authorization into your applications.

[29:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1790s) You can embed it deeply
into your systems.

[29:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1792s) Helps you accelerate
application development

[29:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1794s) by not having to worry about
that kind of authorization system.

[29:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1797s) You can just plug it right in.

[29:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1799s) It gives you that authenticated,

[30:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1801s) the proven power of Cedar to help you
protect your data and resources.

[30:06](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1806s) And it simplifies compliance
audits

[30:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1809s) by logging all of these access
requests centrally,

[30:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1811s) so you can categorically define
who has access to what.

[30:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1817s) Let's look at AVP.

[30:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1819s) I like to shorten things,

[30:21](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1821s) Amazon Verified Permissions
in a zero trust space.

[30:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1824s) So to get started using AVP,

[30:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1826s) you start by defining
your business domain.

[30:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1830s) You create an entity
mapping of your business objects

[30:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1832s) and the actions
you can take upon them.

[30:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1834s) Often you can figure out a way
to export this from your system,

[30:37](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1837s) but AVP has to understand
your domain,

[30:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1839s) because, again, you're going
to write policies about your domain.

[30:42](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1842s) You then integrate AVP’s SDK
into your application,

[30:46](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1846s) and every time you want to make
an access decision,

[30:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1849s) you call the library.

[30:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1851s) You call the API.

[30:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1852s) You pass in a context, and AVP
responds with permit or forbid.

[30:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1857s) Now, that context can be something
from your own application,

[31:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1860s) like your user identity
and what they’re trying to access.

[31:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1864s) But you can also, if you've put AVA
at the front door,

[31:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1868s) AVA gives you a JSON object
out the back for every request

[31:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1872s) that you can actually just consume,
either pass it on directly to AVP

[31:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1876s) or combine it with your own
application's context

[31:18](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1878s) to get that entire set of end
to end zero trust.

[31:22](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1882s) So you can get the authentication
information,

[31:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1884s) you can get device
trust information from AVA.

[31:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1887s) You can layer in maybe the business
model

[31:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1889s) that you're trying to access
and some of the domain information,

[31:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1892s) and you get a really powerful
set of permissions capabilities.

[31:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1896s) Later, you can audit all those
permissions at scale

[31:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1899s) using verified permissions.

[31:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1901s) I think it's a really exciting end
to end story

[31:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1903s) that we're able to bring
to the table now.

[31:46](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1906s) And I hope you find that
to be true as well.

[31:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1908s) All right.

[31:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1910s) So I'm done talking about
what we have on the truck today.

[31:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1912s) I'm going to bring Quint back
on stage

[31:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1914s) so we can talk about where we're
going to go in the future.

[31:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1918s) Awesome.

[31:59](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1919s) Thanks, Jess.

[32:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1920s) [applause]

[32:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1924s) Awesome.

[32:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1925s) So the final thought that we want
to share with you all today

[32:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1930s) is a little bit of our vision
for where we see zero trust going,

[32:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1933s) even beyond the evolutions that Jess
has shared with you today, right?

[32:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1939s) If I had one phrase for it,
it would be ubiquitous authorization.

[32:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1946s) We continue to see these worlds
of identity

[32:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1948s) and networking continue
to converge and collide.

[32:31](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1951s) We saw that originally with that
first guiding principle

[32:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1955s) that I offered for you
about avoiding that binary choice,

[32:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1959s) about how these things
work better together.

[32:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1963s) Continuing from that original example
of the VPC endpoint,

[32:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1967s) we've seen that principle
continue to strengthen

[32:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1971s) and resolve as we've brought you
Amazon Verified Access

[32:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1975s) or VPC Lattice and more.

[32:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1978s) Now another way that we might think
about that are identity

[33:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1980s) and the associated set of signals
like device and behavior

[33:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1984s) are some of the most
important signals into zero trust,

[33:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1988s) while network enforcement points
continue to be

[33:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1991s) some of the most important places
to enforce zero trust, right?

[33:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1996s) And if we're able to think about
these things in this converged way,

[33:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=1999s) we might be able to get to a point
where we're able to do

[33:22](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2002s) what we've never been
able to achieve before:

[33:24](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2004s) authorization that happens
from the outermost perimeter

[33:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2007s) to the deepest rings within the core,

[33:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2009s) with such sophistication,
adaptability, continuousness,

[33:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2014s) and more, that would have
just been unimaginable

[33:37](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2017s) or at least unattainable
just years ago.

[33:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2020s) Now we think this represents
some pretty stark ways

[33:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2023s) in which our view
of zero trust differs

[33:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2025s) from other folks in the industry.

[33:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2028s) I absolutely agree that making
perimeter controls more intelligent

[33:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2032s) and sophisticated is absolutely
great incremental progress.

[33:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2036s) But to really get to the value,

[33:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2037s) to really get to the promise
of zero trust,

[34:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2040s) we need to be thinking about
evaluating these access decisions,

[34:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2043s) these authorization decisions across
the entire life span of a request,

[34:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2047s) as it moves from the outermost

[34:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2050s) to the innermost portions
of our organization.

[34:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2053s) Now, why might we think about that?

[34:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2055s) Authentication and identity
has been centralized for years,

[34:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2059s) but authorization has really
been spread to the wind.

[34:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2063s) It's buried, and there's maybe
some group information,

[34:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2066s) and so we might make some coarse
grained decisions

[34:28](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2068s) in that identity provider.

[34:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2069s) But beyond that, it's buried in file
ACLs, it's buried in table grants,

[34:33](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2073s) it's buried in all sorts
of downstream systems

[34:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2076s) throughout your enterprise

[34:37](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2077s) that are literally impossible
to reason about in a collective way,

[34:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2081s) much less gain control
over or audit, right?

[34:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2085s) And so this is in essence
what we think

[34:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2088s) is the fundamental problem to solve.

[34:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2091s) And with your help, we intend
to solve it ubiquitously.

[34:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2096s) Now, in this sense,
ubiquity also implies consistency.

[35:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2100s) We need a couple of things
to make this work.

[35:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2102s) The first thing that we need
consistently across this environment

[35:06](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2106s) is shared auth context.

[35:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2108s) The identities and contexts
that are operating

[35:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2111s) or that are associated with a request
as it flows through

[35:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2115s) these various enforcement points must
propagate along with the request,

[35:19](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2119s) even when the request is comprised
of multiple related flows.

[35:23](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2123s) Think of a simple example of this

[35:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2125s) is a human clicks
a button in an application

[35:27](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2127s) and that results
in some microservices calls

[35:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2130s) that might end up in a Lambda
function with its own identity

[35:33](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2133s) that's now operating
on behalf of that human

[35:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2135s) as it goes and retrieves some data.

[35:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2138s) Now, within AWS technology today,

[35:41](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2141s) this notion of identity propagation
is already there.

[35:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2143s) You might not have seen it,
but if you go and use a service

[35:46](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2146s) like Amazon Athena,
that you might use to query into S3,

[35:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2150s) Athena understands its role,
its permissions as an AWS service,

[35:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2154s) but it also understands you,
the user,

[35:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2157s) and your permissions
that it's operating on behalf of.

[36:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2160s) Now, within our ecosystem today,

[36:04](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2164s) there's still a bit of a pivot point,
right?

[36:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2165s) And the example that I described,

[36:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2168s) you can see and reason
about both the human identity

[36:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2171s) and Lambda's identity as it operates
on behalf of the human.

[36:14](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2174s) But there is that pivot point.

[36:16](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2176s) We aren't fully converged yet, right?

[36:18](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2178s) But we see a pathway to getting
that done and work

[36:21](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2181s) is already well underway.

[36:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2185s) Now, the second thing that we need to
have consistent across this environment

[36:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2190s) is a consistent
authorization evaluation.

[36:33](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2193s) And Jess just walked you through
the Cedar policy language

[36:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2196s) and its corresponding
evaluation engine,

[36:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2198s) which we really see as our pathway
to giving you this consistency.

[36:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2203s) We see a hierarchy of policies that
logically inherent and stack together

[36:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2207s) to represent the types
of authorization decisions

[36:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2212s) that you want in increasingly
granular ways

[36:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2215s) as you move through the environment.

[36:57](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2217s) We also see this as one place
to integrate all your signal

[37:01](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2221s) and context providers.

[37:02](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2222s) Jess talked about identity
providers, device providers.

[37:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2225s) There's lots of things that need
to feed into these decisions,

[37:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2228s) and we don't want to be doing
those integrations at each

[37:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2231s) and every point of this stack.

[37:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2233s) We want to do it once,

[37:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2235s) and certainly we think that this is
the right layer to do it in, right.

[37:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2240s) Now, again, today just we see half
this world operates in Cedar.

[37:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2246s) You heard Jess talked about the use
of Cedar and verified,

[37:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2250s) access verified permissions, right.

[37:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2252s) But a lot of the world,
the traditional world of AWS,

[37:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2255s) operates in the language of identity
and access management, IAM, right.

[37:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2260s) As an interesting piece
of Amazon history, or not history,

[37:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2263s) but a flavor of color,

[37:45](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2265s) our existing language internally
is known as Balsa.

[37:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2268s) So I don't know
all the history on it,

[37:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2269s) but apparently we've got
some hobbyist woodworkers

[37:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2272s) afoot somewhere
in the bowels of AWS, right.

[37:55](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2275s) Okay.

[37:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2276s) And then now the last point
of consistency that we need

[38:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2280s) are this notion of this
combined place to bring together

[38:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2283s) all this logs, all this telemetry.

[38:05](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2285s) You know, a big part
of what zero trust is,

[38:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2287s) it’s about making all these siloed

[38:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2289s) piece parts
work better together, right?

[38:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2293s) We want to be able to let those
security tools do their job,

[38:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2297s) but omit telemetry
that goes into a place

[38:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2300s) that we can reason about collectively

[38:22](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2302s) and ideally bring that flywheel
back around and help inform

[38:26](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2306s) all those various
enforcement points, right.

[38:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2309s) So now finally, we're going to wrap
all of that in AWS

[38:32](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2312s) opinionated guidance, right,
back to some of those questions

[38:35](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2315s) I shared at the onset.

[38:36](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2316s) Where do I start?
How do I get going?

[38:38](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2318s) What should I do next?

[38:39](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2319s) Where is my risk?

[38:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2320s) Where can I make a meaningful impact,
right?

[38:42](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2322s) And we're going to lead you along
the way, along those journeys, right?

[38:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2327s) So, listen, there's a lot
to digest here, right?

[38:52](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2332s) We look forward to your continued
feedback as we go

[38:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2334s) about building this vision,

[38:56](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2336s) but we think we're meaningfully
on our way towards making it real.

[39:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2340s) We talked today about
how verified access

[39:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2343s) might be that enforcement
point for applications,

[39:06](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2346s) verify permissions for app logic.

[39:08](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2348s) You've got things that we didn't
even talk about today,

[39:11](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2351s) session manager and others
for infrastructure,

[39:13](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2353s) Lattice for microservices.

[39:15](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2355s) And we're going to continue
to converge these worlds

[39:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2357s) of networking and identity
that are going to fill in

[39:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2360s) even further vertical slivers
of this diagram and many more, right?

[39:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2365s) So we think we're on our way
to making it a real—we really think

[39:30](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2370s) we're on our way to making
this vision a reality for you, right?

[39:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2374s) And we'd like to offer that we think
we're ready in a position

[39:37](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2377s) to have authorization join this club

[39:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2380s) of ubiquity
alongside encryption, right.

[39:44](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2384s) We long ago recognized that this
consistent authorization vision

[39:49](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2389s) was necessary, right.

[39:50](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2390s) When we built AWS, you know,
again,

[39:53](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2393s) all these services that have this one
common authorization language, right.

[39:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2398s) And think now as we apply zero trust,
AWS applying that same rigor,

[40:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2403s) that same philosophy
of ubiquitous authorization,

[40:06](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2406s) as Jess explained, even into
your domain, beyond our domain.

[40:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2409s) So we aren't there yet, but we
really think that when we get there,

[40:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2412s) we're going to have something
that really delights you.

[40:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2417s) Now to close it out, we have
an Amazon expression

[40:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2420s) that it's always day one, right?

[40:21](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2421s) And that's just really our way of
making sure we stay in the mentality

[40:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2425s) that we're building and innovating
on your behalf each and every day.

[40:29](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2429s) So we're definitely well underway
on this journey, right?

[40:31](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2431s) You can go back to the earliest days
of AWS

[40:34](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2434s) and how folks are using
our API calls over the world's

[40:37](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2437s) most untrustworthy network
in the world, the Internet,

[40:40](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2440s) to call and query
their most sensitive data.

[40:42](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2442s) We've been at this for a long time,

[40:43](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2443s) and we think we've made
some meaningful progress

[40:47](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2447s) in what we've shared
with you here today

[40:48](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2448s) about how bringing
together things

[40:51](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2451s) in a more packaged
and more refined way, right.

[40:54](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2454s) But we think that where we're
going again is unique, right.

[40:58](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2458s) And we really look forward to you

[41:00](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2460s) all keeping--to going along
on this journey along with us.

[41:03](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2463s) And so with that,
really appreciate your time today.

[41:07](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2467s) I look forward to your feedback.

[41:09](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2469s) Please do fill out your surveys.

[41:10](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2470s) We really take that meaningfully.

[41:12](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2472s) And if you all, any of you
all have questions

[41:14](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2474s) or would like to talk about
zero trust in greater depth,

[41:17](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2477s) Jess and I are going to hang out
in the hallway after a quick second

[41:20](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2480s) to take any questions
that you might have.

[41:22](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2482s) So thanks and enjoy the rest
of your time here at re:Inforce.

[41:25](https://www.youtube.com/watch?v=Uke2CmFaVZ8&t=2485s) [applause]

