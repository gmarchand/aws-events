# AWS re:Inforce 2023 - Keynote with CJ Moses

[Video Link](https://www.youtube.com/watch?v=_piUB5FrYVE)

## Description

Learn how at AWS, security is as much about technology as it is about people and culture and how AWS is helping customers innovate faster on and off the cloud while maintaining a strong security posture. Hear about best practices for managing security, compliance, identity, and governance in the cloud from CJ Moses, Chief Information Security Officer (CISO), AWS; Debbie Wheeler, SVP & Chief Information Security Officer, Delta Air Lines; and Becky Weiss, Senior Principal Engineer, AWS.

You’ll also learn about new AWS Partner initiatives and programs as well as long-term investments in security innovation, including generative AI and post-quantum cryptography. This keynote includes a number of exciting launches and demos including Amazon CodeGuru Security, Amazon Detective Finding Groups, Amazon Verified Permissions, EC2 Connect Endpoint, Amazon Inspector - Lambda runtime code scan, Amazon Inspector - SBOM export, AWS Built-In for Partners and the AWS Global Partner Security Initiative

Speakers:
01:00 - CJ Moses, Chief Information Security Officer, AWS
19:34 - Becky Weiss, Senior Principal Engineer, AWS

New launches:
25:30 - Launch: Amazon Verified Permissions
27:35 - Launch: EC2 Connect Endpoint
38:11 - Launch: Amazon Inspector - Lambda runtime code scan
39:35 - Launch: Amazon Inspector - SBOM export
42:00 - Debbie Wheeler, SVP & Chief Information Security Officer, Delta Air Lines
52:06 - Launch: AWS Built In for Partners
57:54 - Launch: Amazon CodeGuru Security
59:09 - Launch: Amazon Detective Finding Groups

Learn more about AWS re:Inforce at https://go.aws/43DgUJg.

Subscribe: 
More AWS videos - http://bit.ly/2O3zS75 
More AWS events videos - http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers — including the fastest-growing startups, largest enterprises, and leading government agencies — are using AWS to lower costs, become more agile, and innovate faster.

#reInforce2023 #CloudSecurity #AWS #AmazonWebServices #CloudComputing

## Transcript

[clicking of keyboard] [internet dial-up tone] [music playing] Please welcome Chief Information
Security Officer, Amazon Web Services, C.J. Moses. [music playing] Love the energy. Love the energy. Thank you all for joining us
here at re:Inforce. Security is a discipline
that is constantly changing. New technologies like generative AI
can present new challenges, but also new opportunities. Opportunities to reevaluate and to rethink how we improve
our defense mechanisms through techniques like automation
and threat detection. At AWS, we invest
deeply in security. Protecting our customers
is our top priority. Today we look at the steps
we've taken to help build more resilient systems in this
ever changing landscape. So let's cut through the noise and dive into
the real world solutions that underline our deep commitment
to keeping your environment safe while you focus
on innovation. We work closely with you
to better understand your particular business needs. 90% of the services
and features that we build
come from your requests. Years ago when I was writing
the very first version of our Security White
Paper, the one question that customers
regularly asked me was, What is your responsibility
and what is ours? From that very basic question
we created a guiding principle, the Security Shared
Responsibility model. The easiest way
I know to explain this is if you have access,
you have responsibility. So in the case of infrastructure
such as data centers, you have no access,
therefore, that is exclusively
our responsibility. We call this security of the cloud. In the case of architecting
and implementing your use of our services,
you'll of course have access and therefore
we'll have responsibilities. We call this security in the cloud. And at AWS we provide you with
the guidance, services and technology to enable you to move
more quickly while remaining secure. We are continually investing
in new technologies that make security more affordable,
effective and straightforward. But our work doesn't stop there. Security is about people
and culture than it is technology. For a security strategy
to be successful, you need to have a deep understanding
of the human psychology. Back in the early 2000s, I was working with
the FBI's Behavioral Sciences unit, conducting interviews
of convicted cyber criminals. This was an extension of an
already successful program for creating criminal profiles
of serial killers. During these interviews,
I used a profiling algorithm which at a high level
consisted of three components. The 'Why' or the motivations. The 'How' being the methods and the 'Who' being the attributes of the person
that was committing the crime. Our interviews tried
to fill in the details on the first two parts of
the algorithm, the 'Why' and the 'How' in an effort to understand the 'Who'. In other words, if you can
determine the 'Why' and the 'How' a crime was committed, it would help lead to the 'Who'. My biggest takeaway from being part
of this program was that it's not a computer
committing the crime. There's always a human
behind the keyboard. And in cybersecurity, the more you know about
the 'Why' and the 'How', the better you can
understand the 'Who'. When I later joined AWS, I was able
to use some of these learnings to help build
better security products. I figured out that the algorithm
also worked if we lacked the 'How', but by developing threat intelligence on the 'Why' and
potentially on the 'Who', it'd enable us to create
better defenses that are aligned to counter
their preferred methods. Every action we take and every
defensive measure we build in takes
the human element into consideration. Today, I know that AWS is architected
to be the most secure and flexible way
to run your business. Every year we release thousands
of services and features that have been rigorously tested to meet our extremely
high security standards because good enough is never good
enough for us or our customers. For years, we pushed the limits of
conventional virtualization systems, but we knew we could do better. You see, the problem with
traditional virtualization was that the hypervisor had
direct access to the storage and network devices. So any vulnerability
in the hypervisor could potentially be exploited
by attackers to access
or modify network traffic and data. These systems couldn't provide
the level of security and performance
we wanted for our customers, so we decided to build
our own virtualization technology starting at the foundation,
the silicon. So we went to work and after five
years of research and development, we released AWS Nitro System. It was carefully designed to offload
virtualization and security functions to dedicated Amazon
designed hardware and software, enabling near bare metal performance
and enhanced security. Nitro is a fundamental
component of our infrastructure, and it was built to provide
the assurances and protection to meet the needs of even
the most sensitive workloads. Over the past decade, Nitro chips
have evolved quite a bit, with each generation
improving on the past. Our latest fifth generation
Nitro chip has lower latency, higher throughput and the ability
to handle more packets per second. We know that our customers'
needs around confidential computing fall into a couple
of distinct security and privacy dimensions. The need to protect data
from the cloud operator, that's us. The need to protect data from
the operators on the customer side, that's all of you. And AWS has the capabilities
to address both these customer needs. The Nitro system is designed
so that AWS operators doesn't have access
to customer data addressing the first requirement. The way we achieve this is by
completely removing unnecessary syscalls
from the OS running in the Nitro card to prevent these types
of interactions. As a result, there is no path
for any system or operator to log into an EC2 Nitro host. Access the memory of an EC2
instance or access any customer data. We also engineered the Nitro system
with a hardware based root of trust
using the Nitro security chip, allowing us to cryptographically
measure and validate the system. When AWS made its digital
sovereignty pledge last year, we committed to providing
greater transparency and assurances to customers about how AWS services
are designed and operated. This is especially important
when it comes to handling your data. As part of that increased
transparency, we engaged NCC Group, a leading cybersecurity
consulting firm in the UK. NCC has conducted an independent
architecture review of the Nitro system and the security assurances
we made to our customers. I'm happy to share that NCC
has now issued its report and affirmed our claims. Every time you spin up
a new Nitro based EC2 instance, you automatically benefit
from the advanced security and performance capabilities
we built into the Nitro system. Another example of our
investment in innovation can be found
in our serverless architecture. We knew that containers couldn't
provide the strict security boundaries we required
to meet our customers' needs. Our obsession for better security
gave birth to Firecracker. Firecracker is our open source
virtualization technology, purpose-built for creating and
managing secure multitenant container
and function-based services. We built Firecracker to be
highly secure with multiple levels
of isolation and protection. Firecracker uses a minimal
virtualized device model with just the necessary
components to run a micro VM. This minimalist design helped us
to reduce the attack surface and achieve the performance
you need. There are three key security features
that make Firecracker unique. First Firecracker statically links
all its dependencies at build time, so it's much harder to dynamically
load malicious libraries from the host system
to Firecracker during runtime. Secondly, we developed a jailer
to constrain the resources that can be accessed
by the Firecracker process. So even if a threat actor managed
to escape from the VM boundary, they would only have limited access
to the resources assigned to Firecracker
and confined to the jailer, hence the name. And finally, the Firecracker
process is isolated, using control groups and is given access to a very small,
tightly controlled set of syscalls, significantly minimizing
the kernel attack surface. So when you spin up an AWS
Lambda function or use AWS Fargate to run your container
based applications, you can rest assured that
the underlying infrastructure is not only performant and scalable, but it's also secure thanks
to Firecracker. We are constantly innovating
on your behalf so you can continue to focus
on what truly matters, safely creating value
for your customers. So far we've talked about
how security is embedded into our hardware,
but what about software security? How do we ensure that the millions
of lines of code at AWS spread across hundreds of services meet our very high
security standards? One way we achieve this is by having
a rigorous yet agile application security review process. Last year alone we performed
over 7500 AppSec reviews. Our AppSec process enables
engineering teams to identify and address security issues early, where it's easier
and more efficient to fix. At AWS, our builders have ownership
of security of their services. So we provide them with the tools, training and guidance on security
expectations to enable ownership and empower them to fix issues
early in the development process. As the code evolves, a number of
internal systems perform security testing and provide
feedback to builders automatically. This use of automation helps
our builders move faster and reduces the need for humans
to identify every potential issue. It's also enables us to take security
outputs from issues and reviews and feed them directly
into our automation process so that multiple teams benefit from
those lessons that have been learned. Without exception, nothing – nothing gets released to production unless it successfully passes
through the AppSec review process. By now, it should be clear that when
you run your applications on AWS, you inherit a world class
security team. This includes the people
that work on your behalf and the capabilities
that allow you to operate securely. That's because AWS supports
over 140 security standards and compliance certifications, including the likes of PCI-DSS,
HIPAA, GDPR. Okay, There's a lot of alphabet soup
there, but you get the point –
a lot of them. AWS offers the tools to help you
meet your compliance obligations and we are assessed regularly
by third party independent auditors
for certification, audits, audit reports
and attestations of compliance. However, one challenge
with these audits is that the auditors traditionally have
to physically visit a data center. Not only is this inefficient
and time consuming and from a security standpoint, the fewer humans you're bringing
into our facilities, the better, as the number
of audits increased every year, we wanted to reduce the friction
and decrease the risk. So we now offer virtual tours
of our data centers via the AWS Digital Audit Symposium. Even under scrutiny and evaluations, we're able to exceed a wide range
of geographic and industry standards, and we continue to pass,
impress and build trust. As I look back at the work
we've accomplished in the security space
over the last 17 years, the one thing that never ceases
to amaze me is the immense scale
of our operations. AWS spans 99 availability zones within 31 geographic regions
around the world with the most extensive
global cloud infrastructure. One of the challenges we're having
with such a large global presence and having worked with a wide
diversity of customers and workloads is that
we often become a target. Sometimes we are targeted
directly and sometimes indirectly
when our customers are. Our number one priority is
to prevent security issues from causing disruption
to your business. As we work to defend
our infrastructure and your data, we get a front seat
to what is happening on the Internet. And we have a unique opportunity to gather a lot of
security intelligence at scale and in real time. This is extremely important
because scale breeds intelligence which leads to better security. Every second we ingest 300GB of VPC
flow logs, every minute we analyze
three terabytes of data. Every day, Amazon
managed rules in AWS WAF process more than
350 billion requests, and last year we mitigated
over 700,000 DDoS attacks. So as we collect more threat
intelligence, we continuously integrate it
into the services such as GuardDuty and Amazon Route
53 Resolver DNS Firewall to adapt
and enhance our defense mechanisms. We also provide you with
a comprehensive set of services and prescriptive guidance to help you build
an effective mitigation strategy against the humans
behind the keyboard and the attacks they perpetrate. The effectiveness of our mitigation
strategies relies heavily on the ability
to quickly capture, analyze and act on threat intelligence. Always on, always monitoring,
always working on your behalf to proactively keep your data safe. At AWS, we focus on mean time
to defense. This is a measure of how quickly
we can take threat intelligence and use it to build
new security mechanisms and push them directly into services
such as GuardDuty, Inspector and WAF
as just a few of the examples. One way we do this is by using
a globally distributed network of threat sensors. This network, along with tools
such as automated malware analysis, active network probing,
botnet tracking, help us understand the threat actors’
tactics, techniques and procedures. In certain scenarios, we'll also
specially designed and isolated devices to join the third party's botnet. By doing so, we have a front seat
to the commands sent from the command and control hosts,
which allows us to stop attacks before the first packet
even makes it to the target. In the first three months
of this year, we disrupted 1 million
outbound botnet driven DDoS attacks from abusing
the Internet at large. Thanks to the threat intelligence
we got from analysis of 5.4 billion signals
from our Internet threat sensors and 1.5 billion signals
from our active network probes. Another example is ransomware. Traditionally, ransomware had
a standard operating mode that we're all familiar with. Threat actors would encrypt
critical data and extort victims for money. However, we've seen a shift
in these tactics in some areas. Instead of encrypting
and decrypting data, they simply prefer to inflict
damage to their victims by stealing their data
and or releasing it to the internet, or even worse,
just deleting it altogether. This is often called wiperware. We saw this new tactic in practice
in the wake of the Russian invasion of Ukraine. Some actors' motivation
went from ransomware one day to wiperware the next. Clearly their motivation, or the 'Why' from our algorithm
earlier in the presentation, changed from making money to causing
disruption to the command and control of the Ukrainian military
and chaos to the Ukrainian public. Again, it's the people
behind the keyboard. So understanding their motivations
can prepare us to protect against the 'How'. For example, customers can use AWS Backup to protect their data
from unauthorized tampering through cross-account backups and
centrally managed backup policies. In addition, AWS Backup Vault
Lock enforces write once, read many or WORM backups to help
protect your backups in your vault from accidental
or malicious deletion, disasters or the likes of ransomware. Let's not forget about the data
encryption, which should be an integral
part of your security strategy. Of course, whenever possible, the further up the stack
you move your solutions, the more you reduce
your attack surface since the infrastructure
is managed for you. After all, the best patching
is the kind of patching you don't have to do. As an example of why this is
important, in the wake of the Log4j
vulnerability disclosure in 2021, we patched AWS Lambda
within 24 hours, including our customers' environments
without any customer action. But we don't stop there. Often the threat Intel we capture
is critical not only for AWS and our customers, but for
the security of the wider Internet. In these cases, we work closely
with the security community and partners around the world
to isolate and take down threat actors. So far this year, we've shared
our intelligence of nearly a thousand botnet command
and control hosts with relevant hosting providers
and domain registrars to take down the botnets
control infrastructure. And in the same time period,
we traced back and worked with external parties to dismantle the sources of 230,000
L7 https DDoS attacks. By making the Internet a safer place, we can all focus our attention
on the important things – innovation and delivering for our customers. Next.
I'm thrilled to invite Becky Weiss to talk about the security in
the cloud and exciting new launches. [music playing] Thank you so much
for the kind introduction, C.J. It's a great privilege
to be here today. So far we've heard C.J.
talk about security of the cloud. All the work that we at AWS
are putting in behind the scenes to ensure that you have a secure
foundation upon which to build. And now we're going to talk
about the second part of that shared responsibility model,
security in the cloud. And in particular, we're going
to talk about some of the services and capabilities that we at AWS
provide you, our customers, so that you can build
and operate securely on AWS. And yes, that means this is
the part with the launches. So one of the best parts of my job
here at AWS is that I get to talk
to a lot of customers about what's top of mind for them as they work towards
securing their cloud environment. Over the last few years,
this concept of Zero Trust has figured increasingly prominently
in these discussions. But what exactly is Zero Trust? Well, Zero Trust is a concept
that's often defined in terms of what it argues against,
which was an argument that relied solely on a network perimeter
for its security. By now, many of us are familiar
with some of the challenges that accompanied such an environment. For one thing, once something
got inside that perimeter, movement among the systems
inside got easier. And also the visibility into that
activity wasn't always there either. So Zero Trust, in contrast,
offers a better way. In a Zero Trust architecture, it's not just a network perimeter
that's evaluated once upon entry. Rather, it's a combination
of identity, network device and other increasingly
sophisticated factors that get evaluated,
ideally on each and every axis. Now, I'll admit there's a lot
of buzz around Zero Trust, maybe even some hype and we do see a lot of people
getting stuck in the theory. So you might reasonably be
asking yourself, you know, well,
this sounds great and everything, but how concretely do
I pull this off? Where exactly do I start? So as it turns out, AWS
has had conviction in the Zero Trust approach
for over a decade. The combination of identity
and network signals has been baked deeply into services
such as AWS Identity and Access Management
and Amazon Virtual Private Cloud for years now, it's not new. In fact, AWS IAM right now is handling over 1 billion AWS API calls per second worldwide. And I'm here excited to tell you
about how we're building even more
our next chapter in our Zero Trust journey with you,
our customers. I'm going to talk to you
about some building blocks that we're building to enable you
to build these Zero Trust capabilities
into your own workloads. Let's start by imagining
a corporate application that you require your users
to access over a VPN. Maybe because there aren't
other controls. So your users have access
to this application because they're in the right network. And let's say you'd like
to modernize this application. You'd like to add user authentication,
you'd like to add device posture, you'd like to define
some fine grained rules about exactly what users can access
this application under what circumstances. And you could build all of that,
but there's some assembly required. Or you could use the recently
launched AWS Verified Access. AWS Verified Access gives you a Zero Trust user facing endpoint that you
can put in front of your application instead of that VPN requirement, typically without
requiring fundamental changes to your applications'
core business logic. This new service can take care of
authenticating your users by integrating either with AWS's own
IAM identity center or with an OIDC identity
provider of your choice. It's also integrated with CrowdStrike
and Jamf as device trust providers, enabling customers
to create rules such as a user can only access this application
when they're on a fully patched and up-to-date laptop. And all of these built
in authorization rules get evaluated on each request before the request
even reaches your application. Now for the builders here,
I want to zoom in on one particular detail
of AWS Verified Access that I think you're
going to find interesting. So what you're looking at here is
an example of a permission that a customer might put in front
of the Verified Access application. This is something
we launched recently. What you're looking at is Cedar,
our open source purpose built authorization, policy, language
and evaluation engine suitable
for a wide range of use cases. Cedar is optimized for
expressiveness performance and we prove its correctness using
our automated reasoning techniques. And it's also at the heart of the launch
I'm going to talk about next. So when customers talk to us about challenges
with security in the cloud, one topic that comes up
is building authorization systems for the resources
within their own applications. These systems can take months
to build and because they also tend
to be use case specific scaling that effort across
a large number of applications is also a bit of a challenge. Frankly, building these
authorization systems and getting them correct is hard. So instead of spending time
on the mechanics and correctness
of an authorization system, wouldn't you rather spend
that time focusing on what your application actually does? And that is why today I am thrilled
to announce the general availability
of Amazon Verified Permissions. [applause] This is a new service that enables
customers to centrally implement and enforce fine grained permissions so the resources
within the applications that they build and deploy. And Amazon Verified Permissions
are expressed in terms of that new Cedar
policy language that you just saw. Amazon Verified Permissions takes
care of evaluating granular permissions
within your application so that you get to focus on your
application's core business logic. It also helps you scale
your compliance audits by automatically checking that
the permissions that you define are working the way
that you intended. So as you can see, we're really
excited about this next chapter of Zero Trust. Now, going back to a few minutes ago, that question of Zero Trust
versus network controls, because we actually think
that's a false choice. We know that network controls
and perimeters will always be central
to security in the cloud, working in concert with, not instead
of, those Zero Trust capabilities. So I wanted to talk about some things
we're doing to help you there. Let's start by talking about how
you connect to your EC2 instances. Many of you are using AWS
Systems Manager session manager to interactively access
your EC2 instances, but at the same time,
SSH is a widespread and popular tool for controlling
and managing EC2 instances. Now, for quite some time
our customers have been able to use Amazon EC2
Instance Connect to SSH to their EC2 instances
with the added benefits of IAM authentication and authorization
and ephemeral keys. But until now, that still meant
that you needed network access to that EC2 instance, either directly
via a public IP address or by way of a bastion host
that you were responsible for patching,
maintaining and securing. So today I am excited to announce
the release of Amazon EC2 Instance Connect Endpoint. [applause] This is a new capability
that allows customers to SSH directly to their EC2 instances,
even if they're in a private subnet. So EC2 Instance Connect Endpoint
eliminates the need to have an internet facing EC2 host
and unlike a single bastion host, it's designed for high availability. EC2 Instance Connect Endpoint
also improves your security posture by relying on IAM
for strong authentication and authorization of connections before they even reach
your EC2 instances. And you also benefit
from centralized visibility because these connections
are logged to AWS CloudTrail, everything is fully auditable. Okay, so that was an EC2 instance
and now we're going to zoom all the way out
from that EC2 instance to your whole
AWS environment where we at continue to invest
in the power and breadth of all of these
different kinds of controls for the different sorts
of resources offered by AWS from compute to databases
to networking and storage. And each time we launch one of
these new controls, our customers are able to take
a step forward towards securing their cloud
environments. Now, at the same time, we also hear
from customers that there's a need to continue working to simplify security
in the cloud. There's always going to be a need
for a scalable and clearly defined perimeter
around your cloud environment, in addition to certainly not instead of these ubiquitous fine
grained controls. So why is that? Well, we see a lot of customers
observing that they're operating large and growing environments
with thousands of AWS accounts and even more people operating
in those AWS accounts. And they also recognize
that leveling up a large cloud security staff on cloud security skills is,
well, it's a bit of a journey. So they ask us at for a set
of preventive controls that they can put in place to define
their identity and network boundary. And they tell us that these
controls need to be complementary to all of these individual
IAM policies. The idea is this. Even if one of these operators,
somewhere in this large environment, has made a mistake and misconfigured
a resource, in fact, even if they're actively trying
to create an outside path, our customers tell us
these misconfigurations must not result
in unexpected access. So I get to work with our customers
on the topic of IAM quite a bit,
in fact it's my favorite topic. This topic of a straightforward
perimeter features prominently in these discussions. Now, I find that each customer
organization has its own words to describe
the goal that they're after, but it almost always
goes something like this. Regardless of which of AWS's
hundreds of services we're using, regardless of how large a cloud
environment we operate with, how many AWS accounts, regardless of how many people
are operating in here, and the mix of
their cloud security skills, we need to know that our data
and our resources is going to be accessible
to our organization only. And in many cases, they also add
that we need to know that this data is going to remain
within networks that we control. And therefore a large part
of what we work on at AWS and our security in the cloud
features and services works backward directly
from this goal statement. We even have a name for it. Call it data perimeters. And our focus on data
perimeters is not new. We're on a long journey
together with you, our customers, continually investing
in making this perimeter ever more straightforward
to implement at scale. And over the years
we've invested heavily in two central concepts
of the data perimeter. One is the Organization
and the other is the Amazon Virtual
Private Cloud. Today, our customers are using
the Service Control Policies features of AWS Organizations
to create broad based rules over what their users
can do in their cloud environment. One example preventing data
from being written to resources that are outside
their organization's control. And they use the VPC endpoint
policy capability to assert that all bound requests
from their network are being made on behalf of them. And it's in that vein that I'd like
to tell you about AWS's most
recent data perimeter launch. I'm going to guess that most of you
are familiar with the AWS Management Console
or the console. AWS Management Console
Private Access, which was made
generally available recently, allows you to take your virtual
private cloud network along with any on premise or corporate networks
that are connected to it and limit all use of the console
to your organization only. So why would you want to do
something like this? Well, let's go back to that
previous diagram where the VPC, the virtual
private cloud network, was one of the focal points
of the data perimeter. So you're trying to assert
that whenever anyone or anything in your VPC
is communicating with AWS, that they are doing so on behalf
of the environments that you control. Now for a long time, if these requests were going
directly to the service, you've been able to use virtual
private cloud policies to achieve this goal. Now, we've heard from customers that they're looking for
a similar kind of control, except for users interactively
signing in and using the AWS console. In other words, if someone's
in your network using AWS, you want to be sure that
they're doing so on behalf of you. But, let's say they're not. Let's say someone's in your network
trying to sign in to an outside unexpected
AWS account. Now, it doesn't matter who this is. It doesn't matter if they're
an employee or an intruder. It doesn't matter why
they're trying to do it. All that matters is that this is an
account that you were not expecting. And you can see here that AWS
Management Console Private Access is preventing
them from signing in. Good. Okay, now in this next example,
someone's using IAM Identity Center, which by the way,
is one of our recommended best practice ways of having
your users access the console. And they're a legitimate user is signing into a recognized account
that you are expecting. They succeed as expected and the lock icon confirms for us
that indeed they're using AWS Management
Console Private Access. And if you're not yet using
IAM Identity Center, don't worry AWS
Management Console Private Access works equally well for all
the different forms of sign in. In fact, we saw an IAM user
in our last failed sign in example. And I wanted to show you
one more level of detail into what AWS management
console private access is. So it's a VPC endpoint, in fact,
a pair of them. And you use DNS to route requests
from users’ browsers to this endpoint. And what you're looking at here
is actually the crux of the feature. This is the VPC endpoint policy that goes along
with console private access. And this policy here that you're
looking at is a broad based policy that says all sign in and use of
the console from this network needs to be for accounts
for people within my organization. So that's exactly what
this control does. It asserts that all use of the AWS
console from within your networks is occurring on behalf of
the environments that you control. And just like all of our other
VPC endpoints, there's nothing sitting here
in the middle intercepting your TLS connections
or inspecting the traffic. Rather, this is an example of one
of those identity level controls that's baked deeply
into our network so that our sign in system can
reject the outside login attempts. So far we've been talking about
preventive controls. I'd now like to move to the realm
of detective controls where we at have also been hard
at work on your behalf. Amazon GuardDuty is the service
that monitors your AWS environment, proactively detecting
and notifying on security threats across the breadth
of AWS's service offerings. And I'm excited to share with you
three new ways in which we've expanded the scope
of what GuardDuty has to offer. First, Amazon GuardDuty now offers
threat detection for Amazon Aurora
by profiling and monitoring access activity
to existing and new databases and using machine learning to accurately detect
suspicious logins. Second GuardDuty recently
added EKS runtime monitoring to detect runtime threats
from over 30 security findings to help you protect
your EKS clusters. And then finally, we've expanded
GuardDuty threat detection coverage to support
AWS Lambda functions by detecting malicious activity
such as a Lambda function that seems to have been repurposed
for unauthorized crypto mining, or one that seems to be communicating
with known bad actors or servers. Siemens is a great example
of how GuardDuty is a critical component
for any security strategy. One of the primary drivers
of Siemens' decision to use AWS was to strengthen
their security posture, automate the running of important
security tasks and centralize access
to all of their data. So they use EKS runtime monitoring
to deepen threat detection inside their containerized workloads, GuardDuty RDS Protection to help
protect data stored
in their Amazon Aurora databases and GuardDuty Lambda protection
to detect threats to their serverless applications. Now, as a builder myself, I know that
I'm responsible for the security
of the code that I write. But I also know that I don't have
my whole security team sitting right next to me for each
and every line of code that I write, as much as I enjoy that. Now, by using automated tools
early on to improve the security of the code that we write
and find issues early on, we can benefit everyone and get
to our business outcomes sooner. So if you work closely with AWS
Lambda functions, you're going to be excited
to hear that today we are making code scans
for Lambda generally available. [applause] Now Amazon Inspector could
already scan Lambda functions and their associated layers
for software vulnerabilities in their package dependencies. And now with this new feature
Inspector can also scan your own code
for security vulnerabilities such as injection flaws,
data leaks, weak or missing crypto and it has a high true positive rate. It provides actionable security
findings and remediation guidance that follow AWS
security's own best practices. Now, we all know that modern
applications rely increasingly on open source
and third party dependencies. In fact, if we look at our own
open source software, the AWS SDK, we can see that it pulls in quite
a few dependencies of its own. And in practice that means deep
and wide dependency trees which need to be managed
on an ongoing basis. And we hear from builders
that they need tools to manage, track and analyze packages and deployable artifacts
such as container images, Lambda functions and the software
that they deploy to EC2 instances. So today we are excited to announce
the launch of a new capability within Amazon Inspector to allow you
to automatically and centrally manage SBOM or Security Bill
of Materials exports. With one click, you can now
export SBOMs in open standard formats for all Inspector monitored resources
to a preconfigured S3 bucket, and from there you'll be able
to download the artifact, run Athena queries on it, or create QuickSight dashboards
to gain further insights. And this complements the existing
continual vulnerability management capabilities within Inspector by providing a detailed
software dependency list, contributing to your wider efforts
in securing your software. Our journey to help you improve
your security posture by implementing more comprehensive
Zero Trust architectures, robust data perimeters and granular
purpose built controls continues as we constantly innovate
on your behalf. And next, we're going to hear
from one of our customers about how their security, culture
and renewed focus on end-to-end security
is helping them scale and operate more securely on AWS. Thank you so much. [applause + music playing] The power of one, may be strong. But the power of 80,000,
it's unstoppable. And today, like every day, our goal is to put customers first. To welcome you with an experience
designed with you in mind. [music playing] Because at Delta, it's not just
the destination, it's the journey
that makes the difference. [music playing] [applause] Please welcome Senior Vice President
and Chief Information Security Officer,
Delta Airlines Debbie Wheeler. Good morning and thank you. In 2022, 420 million plus individuals experienced a data breach. And in 2022, Delta Airlines was entrusted
by 177 million passengers to deliver them safely
to their final destinations while protecting their personally
identifiable information. Ours is a complex industry
full of regulations and lots of safety protocols. And with a team of 90,000 people
around the world connecting millions of passengers
to their final destinations, doing so safely and securely,
a culture of security is imperative. I'd like to share with you today
three elements we believe contribute to
the security environment in Delta. And the first starts with fostering
a security aware culture. At Delta, people are our business. A vibrant security culture that embraces
the shared values of our people are critical to how we secure
our customer information and our employee information. We believe our people are key
in thwarting and defending the airline against
the cyber threats we experience and allowing us to maintain
a world class operation. The first element of our security
program starts with leadership. From the CEO to the CISO
to our ground handling crews, to our gate agents – every member of the Delta team must embrace a safe
and secure culture in order to provide for
the protection of our customers and our employees. Leadership sets that example, walking the walk
and talking the talk, we expect our employees
to follow. But leadership expects accountability and people need to buy into
the message that we're delivering. And in order for them to do so, we need to enable them with
the tools, the processes and data that allow them to protect
the information that our customers entrust
to our care. In a cloud environment,
you build it, you run it, you own it. And we've had to transition
how we think about security and how we enable
our people to do that. So, as we have embraced
the journey to the cloud, we have had to shift left,
the security inside of Delta. Depending on our development teams
to build security in from the beginning
of their development process rather than tacking it
on at the end. And in order to do that,
Delta has partnered with AWS and created the reference
architecture library that contains security approved patterns, configurations,
requirements and guardrails that we expect our developers
to implement into their code. In addition, the security team
at Delta has been focused on automation. Automation
allows our security services to scale across Delta's vast
IT portfolio. The use of automation
through AWS Security Hub, AWS GuardDuty and AWS
Config enables the security team to provide our developers
with centralized visibility to how their applications
are complying with our security requirements at any point during
the development process. The goal being no more surprise
security findings prior to moving
to production. Ours is a people-oriented
environment. And prior to our cloud journey, Delta has always been laser-focused
on safety and security. The third element that I want
to speak to you today with respect to our program and what we believe
makes it successful is perhaps
the most important element, and that is embracing the culture and the values your people have
and embedding your security message into that culture
and into those values. As I said, we are a diverse
workforce, 90,000 people, 70,000 of whom are customer
facing on any given day. They're using a myriad
of digital devices and applications
to serve our customers to protect their physical safety
as well as their digital safety. And as I said, our people
are critical to that mission. In order to ensure that
they're well equipped to provide those services
to our customers, we've worked tirelessly
with our employees to help them understand
security habits or hygiene that they can practice at home. Our thinking is if we can teach them
how to take care of their information and their personal life
and teach them how they can help their loved ones care
for their information, they'll bring those habits
back into the work environment, and that will extend to how
they protect the information that our customers and fellow
employees entrust to their care. Safety first, always. It's our core value. It headlines our flight plan. Our flight plan reflects
Delta's goals and objectives on an annual basis. And while the flight plan
changes year to year, what never changes
is safety first. Always. When I met with C.J. Moses and
Steve Schmidt several weeks ago, we talked about the journey
that Delta has been on and we talked about these core
principles that we believe contribute to the success
of our security awareness program. And they felt strongly that
in sharing these principles with all of you,
there may be benefit in how you develop
your own awareness programs. But I recognize that not
every industry, what works for Delta
may not work for you. We are all under a constant
barrage of threats. But what I will share with you
is this – our security aware culture has not
impeded our ability to innovate. It has not impeded the ability
that we have to collaborate with our development teams
and with our business partners. If anything, it has strengthened
those collaborations and it has allowed
our development teams to move in a more agile way
in securing the applications and the services
that they are designing. Fostering this environment
is contributing to how our teams are able to protect
not just the physical passenger, but the digital passenger as well. I'd like to thank C.J. for inviting
me to speak with you this morning and I'd like to remind you
all to please fly Delta. Thank you. [music and applause] Thank you. Thank you, Debbie. It's always great to see
how customers leverage AWS to innovate safely. So far we've talked about the shared
responsibility model and how a culture
of security empowers you to build the right
security strategy for your business. But there is another
critical component that extends the benefits of AWS,
and that's our AWS Partner Network. Our broad Marketplace provides
you with access to thousands of third party solutions
that integrate deeply into AWS and address specialized
security needs. But one thing we hear loud and clear
is that customers want the centralized
security data from the cloud on premises and custom sources to
gain better visibility and insights, which is difficult with all
the different logging formats. To help you with this challenge, we recently released Amazon
Security Lake – our new automated data lake service that enables customers
to centrally aggregate, manage and derive value from the security related
logs and event data. Data in Security Lake is stored
in an open cybersecurity schema
framework format, an open standard
developed in collaboration with other industry leaders. Today we have over 50 partners that integrate directly
with Security Lake to store and provide security analytics
to our customers. One customer that relies heavily
on Amazon Security Lake is FINRA. FINRA enables investors in firms
to participate in the stock market with confidence
by safeguarding its integrity. They use a wide variety of security
tools to secure their AWS environment and ensure the security
of their data. Using Amazon Security Lake, they centrally manage their security
data, saving substantial time and effort
in deriving value from their data. Now, another thing you told us is that when it comes to choosing
partner solutions, you want to have the assurance that
the third party products you choose are designed to integrate
with your existing services. That's why I'm excited to announce the preview
of Built-In Partner Solutions. Thank you. [applause] You can learn more by browsing
the AWS Built-In Partner page offerings by use case. Once released in AWS
Marketplace later this year, you'll be able to purchase
partner software coupled with AWS native tools
and an automated deployment powered by infrastructure as code
tools and validated by experts. And while we're on the subject
of partners, I'm excited to announce
a new initiative that we're launching today
in collaboration with our global systems
integrators, the AWS
Global Partner Security Initiative. With this new initiative will be
jointly developing end-to-end security solutions
and managed services, leveraging the capabilities, scale and deep security knowledge
of our GSI partners. Our partners will leverage
Amazon Security Lake to provide customers
the most robust cyber signals and threat intelligence information. We already have five partners
lined up, Atos, Deloitte, PwC, Accenture and Kyndryl,
and we will be onboarding more soon. Finally, we know that our customers
sometimes struggle to operationalize their security
for all sorts of reasons, including staffing
or skill shortages. This is exactly why our AWS
Partner Network has created three competencies containing
partners with some of the world's most talented AWS security experts. If you need software
and consulting solutions for specific workloads or use cases, then you can find a partner
in the security services competency. For 24 x 7 managed security services,
our partners in the Level one MSSP competency can provide you
with all the expertise you need. And finally, partners in the cloud
operations competency offer you comprehensive solutions
to help you with governance, monitoring, observability,
compliance and auditing. Security is a constantly
evolving landscape, so let's shift gears a little bit
and look at the areas where we're investing in
as we prepare for what lies ahead. For the past few months
generative AI, yes, I said it in large language models
have been capturing everyone's imagination. Generative AI is a type
of artificial intelligence that can create new texts,
photos, videos, even code
from simple language prompts. Generative AI is democratizing
content creation by providing simple,
yet extremely powerful tools that are open
and accessible to everyone. However, without clear security
guidance and governance, generative AI risks introducing a
number of security and privacy risks. As with any other tool, there is an opportunity
for people to misuse it. Threat actors could leverage
generative AI to automate the creation
of phishing emails, social engineering attacks
and other types of malicious content. Many of the generative
AI services available today have been trained
to prevent malicious use and have some form of guardrails that prevent users
from abusing their capabilities. But unfortunately, there are
almost always ways and scenarios where motivated actors will find
their way to abuse them. However, that same power and ease
of use can make artificial intelligence an indispensable tool
in the hands of security engineers. At AWS, we help you automate
the identification and resolution of issues
more effectively, and machine learning is one
of the biggest areas of impact. We're examining how large
language models can improve security throughout the threat prevention,
detection and response cycles. A couple of months ago, we announced
Amazon Bedrock and multiple generative AI services
and capabilities to help you build and scale your own generative
AI applications. Bedrock provides you the broad
range of foundational models so that you can choose the ones
that best fit your needs. Bedrock is yet another example
of how AWS is carefully considering
the security implications so that you don't have to. Bedrock enables private fine
tuning of foundation models and supports the encryption,
access control and auditing with AWS,
IAM, KMS and CloudTrail and with AWS PrivateLink. Data is securely transferred
through the AWS network and never through
the public internet. Bedrock never uses customer data
to train the underlying models. Instead, Bedrock makes a separate
copy of the Base Foundation model that is accessible
only to you and trains this private copy of the model. I think the easiest way to leverage
generative AI for security is when it's embedded
invisibly into applications. That's why we released
Amazon CodeWhisperer, our AI powered code companion that radically improves
developer productivity by generating code
suggestions in real time. CodeWhisperer is the only
AI coding companion with built in security scanning
to help you find remediations for hard-to-detect vulnerabilities. In addition, it can filter out
biased or unfair code recommendations and can flag these code suggestions
that resemble open source code. If developers choose to use
that code, CodeWhisperer logs the acceptance
along with the licensing information. In our efforts to improve
developer productivity, extended to support
the full development life cycle, because we know how important
it is to be able to identify and address security
vulnerabilities as early as possible. That's why I'm excited
to announce today the public preview
of Amazon CodeGuru Security. [applause] This newest service
in our AppSec toolchain integrates with IDEs
and the CI/CD pipelines and uses ML and automated reasoning
to help you build more secure code by detecting vulnerabilities
in your code at any stage of
the development life cycle. CodeGuru Security's enhanced
algorithms help engineers
and infosec teams save time by reducing false
positives detections. And how many of you feel
overwhelmed by the sheer volume of security
findings you need to analyze? I know I do. I think we all struggle
with the alert fatigue from time to time. Some of our customers run
thousands of applications in AWS, so they generate millions
of findings every week. Humans alone are not able
to deal with the increasing complexity
and volume of security threats. We found that the key
in managing modern security is to lean on artificial
intelligence and machine learning to help prioritize findings
and accelerate incident response. That's why today, I'm excited
to announce that we're expanding Finding Groups,
a feature in Amazon Detective that uses ML to distill
thousands of security findings to connected security events. [applause] Finding Groups enables you
to examine multiple activities as they relate
to a single security event by analyzing thousands
of unique security findings aggregated from AWS Security Hub
across hundreds of AWS resources. The output of this feature
makes it easier to understand the complex interactions
that resulted in a potential issue
or security event. Detective can now group
Amazon Inspector and GuardDuty findings to help you
answer hard questions like, was the EC2 instance compromised
because of a vulnerability? Or how did the threat actor move
laterally within my infrastructure? After the analysis, Finding Groups
produces interactive visualizations to help you conveniently view
all of the details related to multiple items
in the single panel. Finding Groups also maps according
to the MITTRE ATT&CK framework to help you improve
threat detection. However, there are many
more areas where LLMs can have a significant
impact on security teams by enhancing and complementing tools
and processes. For example, we can train
generative AI models to create threat
hunting queries, summarize the event data
from an attack, write a remediation code
for vulnerabilities, write penetration test scripts for to automate the creation
of YARA rules for malware detection. With generative AI taking care
of these lower level tasks, we can scale out
our security teams and enable them to focus
on innovation and higher level operations. As for mitigating generative
AI based attacks, we need to remember that this
technology only makes it easier for people that don't have deep
experience to create malicious code. So what generative AI really changes
is not how the malicious code works, but how it gets created. For example, even though these tools
may be used to generate more sophisticated
and accurate phishing emails, the way we protect our users
against them shouldn't and doesn't need
to really change. Another area we're focused
on at AWS is security in a world
where quantum computers are as prevalent
as today's classical computers. Classical processors use bits
to perform their operations, whereas quantum computers use qubits
to run multidimensional algorithms. Quantum computers, by encoding
information in quantum systems like atoms or photons, promise to speed up
some specific computational tasks that are beyond the reach
of classical computers. Additionally, the amount
of information a qubit system can represent
grows exponentially. For example, information
that 500 qubits can easily represent
will not even be possible with more than two
to the 500th classical bits. For context, even if you were
to run one of today's most powerful supercomputers
continuously for billions of years, it would not be able
to calculate this number. Building these machines
is a significant challenge and we had to come up
with a new way of thinking in order
to design their algorithms. But even at this early stage, quantum computing is driving
new discoveries in health care, energy, environmental systems,
smart materials and beyond. As exciting as it sounds, it also comes
with its own security challenges and as we like to say,
opportunities. One of these challenges
is cryptography. Information encrypted today
could be at risk when sufficiently powered quantum
computers become available. Some of the schemes we use today in public key
cryptographic algorithms to protect our data
will not be adequate in a post quantum
computing world. For example, to decrypt
a normal 2048 bit RSA key, it would take 300 trillion years
with a classical computer, whereas it would only take a day
in a fault tolerant quantum computer. Encryption is a fundamentally
important part of any business operation. It allows you to have
cryptographically provable confidence in the confidentiality
and integrity of your data. If you store data in AWS services, then we already mitigate
against store and decrypt attacks on the encrypted data
in the service. And AWS provides no method or data
path for access to ciphertexts that AWS created on your behalf. So it is difficult for the threat
actors to retrieve and store
such ciphertexts for later study. The encryption keys travel
solely within the control plane and the ciphertext is only visible
on the physical network. So AWS is leading in the development
of quantum resistant cloud scale cryptographic technology
and is working with the National Institute
of Standards and Technology and the broader
cryptographic community to help standardization efforts. We also maintain and contribute
to many open source projects on post-quantum crypto algorithms
and tools such as the AWS-LC, a general purpose post-quantum
cryptographic library and Open Quantum Safe that contains
a set of tools for prototyping and benchmarking post-quantum
cryptographic algorithms. The migration to PQC may not happen
overnight, but it's well underway
and it has the potential to impact everyone
that uses public key crypto today. At Amazon, we know the value
of long term thinking and we routinely make big,
long term investments in availability and security based upon our belief
of where the world is going. Post-quantum cryptography is
another example of an area where we are investing
for your future. To help you evaluate the readiness
of your application on AWS, we offer the option to run
quantum resistant cryptography alongside your traditional cryptography
in your applications today. We have contributed to a draft
standard on the post quantum hybrid key exchange and implemented and deployed the community
developed specification in s2n-tls, which implements the Transport Layer
Security protocol across all of AWS. And we've developed hybrid key
exchange to our most secure security
sensitive services like AWS, Key Management Service, Certificate
Manager, Secrets Manager. You can begin testing the impact
of Post-quantum cryptography in your applications by enabling hybrid post-quantum TLS
in your AWS SDK. As part of our shared
responsibility model, we are hoping to add post-quantum
cryptographic capabilities in more AWS services so that you can
prepare for a more secure future. I never get tired explaining
what security is and I'm excited
to come to work every day because our job is never done. In a landscape where everything
is constantly evolving and we get to tackle
new challenges and find different ways to stay
ahead in our defense mechanisms. Throughout this keynote, we talked
about how our security strategy is deeply rooted
in shared responsibility and how we are
constantly innovating to help you meet your security
and business needs. As we get ready for the exciting
couple of days ahead of us, let's remember to embrace the spirit
of enthusiasm and curiosity. Learning should be
an exciting adventure that sparks innovation
within us, so make sure to immerse yourself
in engaging sessions, productive discussions, and the opportunity to create
valuable connections. Together, we can create
a formidable defense against the threats
that lie ahead. Our collective knowledge
is the foundation of a resilient
security ecosystem. Thank you for joining us
on this remarkable journey where we're just getting started. re:Inforce 2023 will be
an unforgettable celebration of security and innovation
in the shared pursuit of knowledge. Let's build trust and secure
the future together. Thank you. [applause and music]

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=0s) [clicking of keyboard]

[00:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=5s) [internet dial-up tone]

[00:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=10s) [music playing]

[00:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=58s) Please welcome Chief Information
Security Officer,

[01:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=61s) Amazon Web Services, C.J. Moses.

[01:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=64s) [music playing]

[01:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=67s) Love the energy. Love the energy.

[01:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=73s) Thank you all for joining us
here at re:Inforce.

[01:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=76s) Security is a discipline
that is constantly changing.

[01:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=79s) New technologies like generative AI
can present new challenges,

[01:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=83s) but also new opportunities.

[01:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=85s) Opportunities to reevaluate

[01:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=87s) and to rethink how we improve
our defense mechanisms

[01:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=90s) through techniques like automation
and threat detection.

[01:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=94s) At AWS, we invest
deeply in security.

[01:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=96s) Protecting our customers
is our top priority.

[01:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=100s) Today we look at the steps
we've taken to help build

[01:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=104s) more resilient systems in this
ever changing landscape.

[01:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=108s) So let's cut through the noise

[01:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=109s) and dive into
the real world solutions

[01:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=111s) that underline our deep commitment
to keeping your environment safe

[01:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=115s) while you focus
on innovation.

[02:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=120s) We work closely with you
to better understand

[02:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=122s) your particular business needs.

[02:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=124s) 90% of the services
and features

[02:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=126s) that we build
come from your requests.

[02:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=130s) Years ago when I was writing
the very first version

[02:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=132s) of our Security White
Paper,

[02:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=134s) the one question that customers
regularly asked me

[02:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=137s) was, What is your responsibility
and what is ours?

[02:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=141s) From that very basic question
we created a guiding principle,

[02:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=146s) the Security Shared
Responsibility model.

[02:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=149s) The easiest way
I know to explain this

[02:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=150s) is if you have access,
you have responsibility.

[02:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=154s) So in the case of infrastructure
such as data centers,

[02:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=157s) you have no access,
therefore,

[02:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=158s) that is exclusively
our responsibility.

[02:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=162s) We call this security of the cloud.

[02:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=164s) In the case of architecting
and implementing

[02:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=166s) your use of our services,
you'll of course have access

[02:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=170s) and therefore
we'll have responsibilities.

[02:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=172s) We call this security in the cloud.

[02:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=174s) And at AWS we provide you with
the guidance, services and technology

[02:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=179s) to enable you to move
more quickly while remaining secure.

[03:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=184s) We are continually investing
in new technologies

[03:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=186s) that make security more affordable,
effective and straightforward.

[03:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=190s) But our work doesn't stop there.

[03:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=193s) Security is about people
and culture than it is technology.

[03:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=198s) For a security strategy
to be successful,

[03:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=200s) you need to have a deep understanding
of the human psychology.

[03:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=204s) Back in the early 2000s,

[03:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=206s) I was working with
the FBI's Behavioral

[03:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=208s) Sciences unit, conducting interviews
of convicted cyber criminals.

[03:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=212s) This was an extension of an
already successful program

[03:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=216s) for creating criminal profiles
of serial killers.

[03:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=220s) During these interviews,
I used a profiling algorithm

[03:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=223s) which at a high level
consisted of three components.

[03:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=226s) The 'Why' or the motivations.

[03:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=229s) The 'How' being the methods

[03:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=231s) and the 'Who'

[03:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=232s) being the attributes of the person
that was committing the crime.

[03:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=237s) Our interviews tried
to fill in the details

[03:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=239s) on the first two parts of
the algorithm, the 'Why' and the 'How'

[04:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=243s) in an effort to understand the 'Who'.

[04:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=245s) In other words, if you can
determine the 'Why' and the 'How'

[04:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=248s) a crime was committed,

[04:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=249s) it would help lead to the 'Who'.

[04:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=252s) My biggest takeaway from being part
of this program

[04:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=256s) was that it's not a computer
committing the crime.

[04:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=258s) There's always a human
behind the keyboard.

[04:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=261s) And in cybersecurity,

[04:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=262s) the more you know about
the 'Why' and the 'How',

[04:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=265s) the better you can
understand the 'Who'.

[04:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=269s) When I later joined AWS, I was able
to use some of these learnings

[04:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=273s) to help build
better security products.

[04:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=276s) I figured out that the algorithm
also worked if we lacked the 'How',

[04:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=280s) but by developing threat intelligence

[04:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=282s) on the 'Why' and
potentially on the 'Who',

[04:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=284s) it'd enable us to create
better defenses

[04:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=286s) that are aligned to counter
their preferred methods.

[04:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=290s) Every action we take and every
defensive measure

[04:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=293s) we build in takes
the human element into consideration.

[04:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=299s) Today, I know that AWS is architected
to be the most secure

[05:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=302s) and flexible way
to run your business.

[05:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=305s) Every year we release thousands
of services and features

[05:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=308s) that have been rigorously tested

[05:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=310s) to meet our extremely
high security standards

[05:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=312s) because good enough is never good
enough for us or our customers.

[05:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=318s) For years, we pushed the limits of
conventional virtualization systems,

[05:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=323s) but we knew we could do better.

[05:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=325s) You see, the problem with
traditional virtualization

[05:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=328s) was that the hypervisor had
direct access to the storage

[05:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=331s) and network devices.

[05:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=332s) So any vulnerability
in the hypervisor

[05:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=334s) could potentially be exploited
by attackers

[05:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=337s) to access
or modify network traffic and data.

[05:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=340s) These systems couldn't provide
the level of security

[05:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=342s) and performance
we wanted for our customers,

[05:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=344s) so we decided to build
our own virtualization technology

[05:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=347s) starting at the foundation,
the silicon.

[05:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=351s) So we went to work and after five
years of research and development,

[05:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=355s) we released AWS Nitro System.

[05:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=358s) It was carefully designed to offload
virtualization and security functions

[06:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=362s) to dedicated Amazon
designed hardware and software,

[06:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=366s) enabling near bare metal performance
and enhanced security.

[06:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=370s) Nitro is a fundamental
component of our infrastructure,

[06:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=373s) and it was built to provide
the assurances and protection

[06:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=376s) to meet the needs of even
the most sensitive workloads.

[06:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=380s) Over the past decade, Nitro chips
have evolved quite a bit,

[06:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=383s) with each generation
improving on the past.

[06:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=386s) Our latest fifth generation
Nitro chip has lower latency,

[06:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=390s) higher throughput and the ability
to handle more packets per second.

[06:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=395s) We know that our customers'
needs around confidential

[06:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=398s) computing fall into a couple
of distinct security

[06:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=402s) and privacy dimensions.

[06:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=404s) The need to protect data
from the cloud operator, that's us.

[06:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=408s) The need to protect data from
the operators on the customer side,

[06:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=412s) that's all of you.

[06:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=413s) And AWS has the capabilities
to address both these customer needs.

[06:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=418s) The Nitro system is designed
so that AWS

[07:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=422s) operators doesn't have access
to customer data

[07:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=425s) addressing the first requirement.

[07:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=428s) The way we achieve this is by
completely

[07:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=430s) removing unnecessary syscalls
from the OS running in the Nitro card

[07:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=433s) to prevent these types
of interactions.

[07:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=436s) As a result, there is no path
for any system or operator

[07:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=440s) to log into an EC2 Nitro host.

[07:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=443s) Access the memory of an EC2
instance or access any customer data.

[07:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=448s) We also engineered the Nitro system
with a hardware

[07:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=451s) based root of trust
using the Nitro security chip,

[07:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=454s) allowing us to cryptographically
measure and validate the system.

[07:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=460s) When AWS made its digital
sovereignty pledge last year,

[07:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=463s) we committed to providing
greater transparency

[07:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=465s) and assurances to customers

[07:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=467s) about how AWS services
are designed and operated.

[07:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=470s) This is especially important
when it comes to handling your data.

[07:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=474s) As part of that increased
transparency, we engaged NCC Group,

[07:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=477s) a leading cybersecurity
consulting firm in the UK.

[08:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=481s) NCC has conducted an independent
architecture

[08:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=483s) review of the Nitro system

[08:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=485s) and the security assurances
we made to our customers.

[08:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=488s) I'm happy to share that NCC
has now issued its report

[08:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=491s) and affirmed our claims.

[08:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=494s) Every time you spin up
a new Nitro based EC2 instance,

[08:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=497s) you automatically benefit
from the advanced security

[08:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=500s) and performance capabilities
we built into the Nitro system.

[08:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=503s) Another example of our
investment in innovation

[08:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=506s) can be found
in our serverless architecture.

[08:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=509s) We knew that containers couldn't
provide the strict security boundaries

[08:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=512s) we required
to meet our customers' needs.

[08:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=516s) Our obsession for better security
gave birth to Firecracker.

[08:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=520s) Firecracker is our open source
virtualization technology,

[08:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=523s) purpose-built for creating and
managing secure multitenant

[08:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=527s) container
and function-based services.

[08:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=530s) We built Firecracker to be
highly secure

[08:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=532s) with multiple levels
of isolation and protection.

[08:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=536s) Firecracker uses a minimal
virtualized device model

[08:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=539s) with just the necessary
components to run a micro VM.

[09:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=542s) This minimalist design helped us
to reduce the attack surface

[09:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=546s) and achieve the performance
you need.

[09:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=550s) There are three key security features
that make Firecracker unique.

[09:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=555s) First Firecracker statically links
all its dependencies at build time,

[09:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=560s) so it's much harder to dynamically
load malicious libraries

[09:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=563s) from the host system
to Firecracker during runtime.

[09:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=566s) Secondly, we developed a jailer
to constrain the resources

[09:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=570s) that can be accessed
by the Firecracker process.

[09:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=573s) So even if a threat actor managed
to escape from the VM boundary,

[09:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=577s) they would only have limited access
to the resources

[09:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=579s) assigned to Firecracker
and confined to the jailer,

[09:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=584s) hence the name.

[09:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=585s) And finally, the Firecracker
process is isolated,

[09:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=589s) using control groups

[09:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=590s) and is given access to a very small,
tightly controlled set of syscalls,

[09:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=595s) significantly minimizing
the kernel attack surface.

[09:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=599s) So when you spin up an AWS
Lambda function or use AWS Fargate

[10:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=602s) to run your container
based applications,

[10:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=605s) you can rest assured that
the underlying infrastructure

[10:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=608s) is not only performant and scalable,

[10:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=610s) but it's also secure thanks
to Firecracker.

[10:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=614s) We are constantly innovating
on your behalf

[10:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=616s) so you can continue to focus
on what truly matters,

[10:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=619s) safely creating value
for your customers.

[10:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=623s) So far we've talked about
how security is embedded

[10:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=626s) into our hardware,
but what about software security?

[10:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=630s) How do we ensure that the millions
of lines of code at AWS

[10:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=633s) spread across hundreds of services

[10:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=635s) meet our very high
security standards?

[10:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=638s) One way we achieve this is by having
a rigorous yet agile

[10:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=642s) application security review process.

[10:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=644s) Last year alone we performed
over 7500 AppSec reviews.

[10:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=649s) Our AppSec process enables
engineering teams to identify

[10:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=652s) and address security issues early,

[10:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=654s) where it's easier
and more efficient to fix.

[10:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=657s) At AWS, our builders have ownership
of security of their services.

[11:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=662s) So we provide them with the tools,

[11:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=664s) training and guidance on security
expectations to enable ownership

[11:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=668s) and empower them to fix issues
early in the development process.

[11:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=672s) As the code evolves, a number of
internal systems

[11:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=674s) perform security testing and provide
feedback to builders automatically.

[11:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=679s) This use of automation helps
our builders move faster

[11:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=682s) and reduces the need for humans
to identify every potential issue.

[11:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=687s) It's also enables us to take security
outputs from issues and reviews

[11:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=691s) and feed them directly
into our automation process

[11:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=694s) so that multiple teams benefit from
those lessons that have been learned.

[11:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=698s) Without exception, nothing –

[11:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=701s) nothing gets released to production

[11:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=703s) unless it successfully passes
through the AppSec review process.

[11:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=708s) By now, it should be clear that when
you run your applications on AWS,

[11:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=713s) you inherit a world class
security team.

[11:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=717s) This includes the people
that work on your behalf

[12:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=720s) and the capabilities
that allow you to operate securely.

[12:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=723s) That's because AWS supports
over 140 security standards

[12:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=726s) and compliance certifications,

[12:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=728s) including the likes of PCI-DSS,
HIPAA, GDPR.

[12:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=733s) Okay, There's a lot of alphabet soup
there,

[12:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=735s) but you get the point –
a lot of them.

[12:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=738s) AWS offers the tools to help you
meet your compliance obligations

[12:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=744s) and we are assessed regularly
by third party

[12:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=746s) independent auditors
for certification, audits,

[12:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=749s) audit reports
and attestations of compliance.

[12:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=753s) However, one challenge
with these audits is that

[12:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=756s) the auditors traditionally have
to physically visit a data center.

[12:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=760s) Not only is this inefficient
and time consuming

[12:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=763s) and from a security standpoint,

[12:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=764s) the fewer humans you're bringing
into our facilities,

[12:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=766s) the better, as the number
of audits increased every year,

[12:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=770s) we wanted to reduce the friction
and decrease the risk.

[12:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=774s) So we now offer virtual tours
of our data centers

[12:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=777s) via the AWS Digital Audit Symposium.

[13:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=780s) Even under scrutiny and evaluations,

[13:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=782s) we're able to exceed a wide range
of geographic and industry standards,

[13:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=786s) and we continue to pass,
impress and build trust.

[13:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=791s) As I look back at the work
we've accomplished

[13:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=794s) in the security space
over the last 17 years,

[13:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=799s) the one thing that never ceases
to amaze me

[13:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=800s) is the immense scale
of our operations.

[13:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=803s) AWS spans 99 availability zones

[13:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=806s) within 31 geographic regions
around the world

[13:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=809s) with the most extensive
global cloud infrastructure.

[13:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=813s) One of the challenges we're having
with such a large global presence

[13:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=816s) and having worked with a wide
diversity of customers

[13:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=819s) and workloads is that
we often become a target.

[13:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=823s) Sometimes we are targeted
directly

[13:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=825s) and sometimes indirectly
when our customers are.

[13:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=828s) Our number one priority is
to prevent security issues

[13:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=831s) from causing disruption
to your business.

[13:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=835s) As we work to defend
our infrastructure and your data,

[13:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=838s) we get a front seat
to what is happening on the Internet.

[14:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=842s) And we have a unique opportunity

[14:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=844s) to gather a lot of
security intelligence

[14:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=846s) at scale and in real time.

[14:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=849s) This is extremely important
because scale breeds intelligence

[14:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=853s) which leads to better security.

[14:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=856s) Every second we ingest 300GB of VPC
flow logs,

[14:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=862s) every minute we analyze
three terabytes of data.

[14:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=865s) Every day, Amazon
managed rules in AWS

[14:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=868s) WAF process more than
350 billion requests,

[14:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=872s) and last year we mitigated
over 700,000 DDoS attacks.

[14:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=877s) So as we collect more threat
intelligence,

[14:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=879s) we continuously integrate it
into the services

[14:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=881s) such as GuardDuty and Amazon Route
53 Resolver DNS Firewall

[14:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=886s) to adapt
and enhance our defense mechanisms.

[14:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=889s) We also provide you with
a comprehensive set

[14:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=891s) of services and prescriptive guidance

[14:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=893s) to help you build
an effective mitigation strategy

[14:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=895s) against the humans
behind the keyboard

[14:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=897s) and the attacks they perpetrate.

[15:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=900s) The effectiveness of our mitigation
strategies relies heavily

[15:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=904s) on the ability
to quickly capture, analyze

[15:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=906s) and act on threat intelligence.

[15:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=908s) Always on, always monitoring,
always working on your behalf

[15:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=912s) to proactively keep your data safe.

[15:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=914s) At AWS, we focus on mean time
to defense.

[15:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=919s) This is a measure of how quickly
we can take threat intelligence

[15:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=921s) and use it to build
new security mechanisms

[15:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=924s) and push them directly into services
such as GuardDuty,

[15:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=927s) Inspector and WAF
as just a few of the examples.

[15:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=930s) One way we do this is by using
a globally distributed

[15:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=933s) network of threat sensors.

[15:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=935s) This network, along with tools
such as automated malware analysis,

[15:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=938s) active network probing,
botnet tracking,

[15:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=942s) help us understand the threat actors’
tactics, techniques and procedures.

[15:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=948s) In certain scenarios, we'll also
specially designed and isolated devices

[15:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=953s) to join the third party's botnet.

[15:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=955s) By doing so, we have a front seat
to the commands sent

[15:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=959s) from the command and control hosts,
which allows us to stop attacks

[16:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=962s) before the first packet
even makes it to the target.

[16:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=965s) In the first three months
of this year,

[16:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=967s) we disrupted 1 million
outbound botnet driven DDoS

[16:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=971s) attacks from abusing
the Internet at large.

[16:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=974s) Thanks to the threat intelligence
we got from analysis

[16:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=976s) of 5.4 billion signals
from our Internet threat sensors

[16:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=980s) and 1.5 billion signals
from our active network probes.

[16:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=985s) Another example is ransomware.

[16:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=988s) Traditionally, ransomware had
a standard operating mode

[16:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=990s) that we're all familiar with.

[16:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=992s) Threat actors would encrypt
critical data

[16:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=993s) and extort victims for money.

[16:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=996s) However, we've seen a shift
in these tactics in some areas.

[16:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1001s) Instead of encrypting
and decrypting data,

[16:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1003s) they simply prefer to inflict
damage to their victims

[16:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1005s) by stealing their data
and or releasing it to the internet,

[16:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1008s) or even worse,
just deleting it altogether.

[16:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1011s) This is often called wiperware.

[16:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1014s) We saw this new tactic in practice
in the wake

[16:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1016s) of the Russian invasion of Ukraine.

[16:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1019s) Some actors' motivation
went from ransomware one day

[17:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1023s) to wiperware the next.

[17:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1025s) Clearly their motivation,

[17:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1027s) or the 'Why' from our algorithm
earlier in the presentation,

[17:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1032s) changed from making money to causing
disruption to the command

[17:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1034s) and control of the Ukrainian military
and chaos to the Ukrainian public.

[17:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1038s) Again, it's the people
behind the keyboard.

[17:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1041s) So understanding their motivations
can prepare us

[17:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1043s) to protect against the 'How'.

[17:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1047s) For example, customers can use

[17:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1049s) AWS Backup to protect their data
from unauthorized tampering

[17:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1052s) through cross-account backups and
centrally managed backup policies.

[17:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1057s) In addition, AWS Backup Vault
Lock enforces write once,

[17:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1061s) read many or WORM backups to help
protect your backups in your vault

[17:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1066s) from accidental
or malicious deletion,

[17:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1067s) disasters or the likes of ransomware.

[17:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1070s) Let's not forget about the data
encryption,

[17:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1074s) which should be an integral
part of your security strategy.

[17:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1079s) Of course, whenever possible,

[18:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1081s) the further up the stack
you move your solutions,

[18:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1083s) the more you reduce
your attack surface

[18:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1085s) since the infrastructure
is managed for you.

[18:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1088s) After all, the best patching
is the kind of

[18:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1091s) patching you don't have to do.

[18:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1093s) As an example of why this is
important,

[18:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1095s) in the wake of the Log4j
vulnerability disclosure in 2021,

[18:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1100s) we patched AWS Lambda
within 24 hours,

[18:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1103s) including our customers' environments
without any customer action.

[18:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1108s) But we don't stop there.

[18:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1111s) Often the threat Intel we capture
is critical not only for AWS

[18:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1114s) and our customers, but for
the security of the wider Internet.

[18:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1118s) In these cases, we work closely
with the security community

[18:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1121s) and partners around the world
to isolate

[18:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1123s) and take down threat actors.

[18:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1126s) So far this year, we've shared
our intelligence

[18:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1128s) of nearly a thousand botnet command
and control hosts with relevant

[18:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1132s) hosting providers
and domain registrars

[18:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1135s) to take down the botnets
control infrastructure.

[18:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1138s) And in the same time period,
we traced back

[19:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1141s) and worked with external parties

[19:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1142s) to dismantle the sources of 230,000
L7 https DDoS attacks.

[19:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1150s) By making the Internet a safer place,

[19:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1152s) we can all focus our attention
on the important things – innovation

[19:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1157s) and delivering for our customers.

[19:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1160s) Next.
I'm thrilled to invite Becky Weiss

[19:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1165s) to talk about the security in
the cloud and exciting new launches.

[19:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1171s) [music playing]

[19:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1183s) Thank you so much
for the kind introduction, C.J.

[19:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1186s) It's a great privilege
to be here today.

[19:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1189s) So far we've heard C.J.
talk about security of the cloud.

[19:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1193s) All the work that we at AWS
are putting in behind the scenes

[19:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1197s) to ensure that you have a secure
foundation upon which to build.

[20:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1202s) And now we're going to talk
about the second part

[20:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1204s) of that shared responsibility model,
security in the cloud.

[20:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1208s) And in particular, we're going
to talk about some of the services

[20:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1211s) and capabilities that we at AWS
provide you, our customers,

[20:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1215s) so that you can build
and operate securely on AWS.

[20:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1219s) And yes, that means this is
the part with the launches.

[20:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1222s) So one of the best parts of my job
here at AWS

[20:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1226s) is that I get to talk
to a lot of customers

[20:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1227s) about what's top of mind for them

[20:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1230s) as they work towards
securing their cloud environment.

[20:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1233s) Over the last few years,
this concept of Zero Trust

[20:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1237s) has figured increasingly prominently
in these discussions.

[20:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1241s) But what exactly is Zero Trust?

[20:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1245s) Well, Zero Trust is a concept
that's often defined in terms

[20:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1249s) of what it argues against,
which was an argument that relied

[20:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1253s) solely on a network perimeter
for its security.

[20:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1257s) By now, many of us are familiar
with some of the challenges

[21:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1260s) that accompanied such an environment.

[21:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1262s) For one thing, once something
got inside that perimeter,

[21:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1265s) movement among the systems
inside got easier.

[21:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1269s) And also the visibility into that
activity wasn't always there either.

[21:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1274s) So Zero Trust, in contrast,
offers a better way.

[21:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1278s) In a Zero Trust architecture,

[21:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1280s) it's not just a network perimeter
that's evaluated once upon entry.

[21:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1284s) Rather, it's a combination
of identity, network device

[21:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1288s) and other increasingly
sophisticated factors

[21:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1291s) that get evaluated,
ideally on each and every axis.

[21:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1296s) Now, I'll admit there's a lot
of buzz around Zero Trust,

[21:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1300s) maybe even some hype and we do see

[21:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1301s) a lot of people
getting stuck in the theory.

[21:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1304s) So you might reasonably be
asking yourself, you know,

[21:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1306s) well,
this sounds great and everything,

[21:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1308s) but how concretely do
I pull this off?

[21:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1310s) Where exactly do I start?

[21:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1313s) So as it turns out, AWS
has had conviction

[21:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1316s) in the Zero Trust approach
for over a decade.

[21:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1319s) The combination of identity
and network signals

[22:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1322s) has been baked deeply into services
such as AWS

[22:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1324s) Identity and Access Management
and Amazon Virtual Private

[22:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1328s) Cloud for years now, it's not new.

[22:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1331s) In fact, AWS IAM right now

[22:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1335s) is handling over 1 billion

[22:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1338s) AWS API calls per second worldwide.

[22:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1342s) And I'm here excited to tell you
about how we're building

[22:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1345s) even more
our next chapter in our Zero

[22:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1349s) Trust journey with you,
our customers.

[22:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1351s) I'm going to talk to you
about some building blocks

[22:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1353s) that we're building to enable you
to build these Zero

[22:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1357s) Trust capabilities
into your own workloads.

[22:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1361s) Let's start by imagining
a corporate application

[22:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1365s) that you require your users
to access over a VPN.

[22:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1368s) Maybe because there aren't
other controls.

[22:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1370s) So your users have access
to this application

[22:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1372s) because they're in the right network.

[22:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1375s) And let's say you'd like
to modernize this application.

[22:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1378s) You'd like to add user authentication,
you'd like to add device posture,

[23:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1381s) you'd like to define
some fine grained rules

[23:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1383s) about exactly what users can access
this application

[23:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1386s) under what circumstances.

[23:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1388s) And you could build all of that,
but there's some assembly required.

[23:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1393s) Or you could use the recently
launched AWS Verified Access.

[23:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1400s) AWS Verified Access gives you a Zero

[23:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1402s) Trust user facing endpoint that you
can put in front of your application

[23:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1406s) instead of that VPN requirement,

[23:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1408s) typically without
requiring fundamental changes

[23:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1410s) to your applications'
core business logic.

[23:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1414s) This new service can take care of
authenticating your users

[23:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1418s) by integrating either with AWS's own
IAM identity center

[23:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1421s) or with an OIDC identity
provider of your choice.

[23:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1425s) It's also integrated with CrowdStrike
and Jamf as device trust providers,

[23:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1429s) enabling customers
to create rules such as a user

[23:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1432s) can only access this application
when they're on a fully patched

[23:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1435s) and up-to-date laptop.

[23:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1437s) And all of these built
in authorization rules

[23:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1439s) get evaluated on each request

[24:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1441s) before the request
even reaches your application.

[24:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1445s) Now for the builders here,
I want to zoom in

[24:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1448s) on one particular detail
of AWS Verified Access

[24:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1451s) that I think you're
going to find interesting.

[24:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1454s) So what you're looking at here is
an example of a permission

[24:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1457s) that a customer might put in front
of the Verified Access application.

[24:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1462s) This is something
we launched recently.

[24:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1464s) What you're looking at is Cedar,
our open source purpose

[24:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1467s) built authorization, policy, language
and evaluation engine

[24:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1471s) suitable
for a wide range of use cases.

[24:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1474s) Cedar is optimized for
expressiveness performance

[24:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1477s) and we prove its correctness using
our automated reasoning techniques.

[24:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1481s) And it's also at the heart

[24:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1483s) of the launch
I'm going to talk about next.

[24:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1487s) So when customers talk to us

[24:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1489s) about challenges
with security in the cloud,

[24:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1491s) one topic that comes up
is building authorization systems

[24:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1495s) for the resources
within their own applications.

[24:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1499s) These systems can take months
to build

[25:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1502s) and because they also tend
to be use case specific scaling

[25:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1505s) that effort across
a large number of applications

[25:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1508s) is also a bit of a challenge.

[25:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1511s) Frankly, building these
authorization systems

[25:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1513s) and getting them correct is hard.

[25:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1516s) So instead of spending time
on the mechanics

[25:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1519s) and correctness
of an authorization system,

[25:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1521s) wouldn't you rather spend
that time focusing on

[25:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1524s) what your application actually does?

[25:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1527s) And that is why today I am thrilled
to announce

[25:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1530s) the general availability
of Amazon Verified Permissions.

[25:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1535s) [applause]

[25:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1542s) This is a new service that enables
customers to centrally implement

[25:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1545s) and enforce fine grained permissions

[25:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1547s) so the resources
within the applications

[25:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1549s) that they build and deploy.

[25:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1552s) And Amazon Verified Permissions
are expressed in terms

[25:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1555s) of that new Cedar
policy language that you just saw.

[25:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1559s) Amazon Verified Permissions takes
care

[26:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1561s) of evaluating granular permissions
within your application

[26:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1563s) so that you get to focus on your
application's core business logic.

[26:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1567s) It also helps you scale
your compliance audits

[26:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1570s) by automatically checking that
the permissions that you define

[26:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1572s) are working the way
that you intended.

[26:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1576s) So as you can see, we're really
excited about this

[26:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1578s) next chapter of Zero Trust.

[26:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1582s) Now, going back to a few minutes ago,

[26:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1584s) that question of Zero Trust
versus network controls,

[26:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1588s) because we actually think
that's a false choice.

[26:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1592s) We know that network controls
and perimeters

[26:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1594s) will always be central
to security in the cloud,

[26:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1598s) working in concert with, not instead
of, those Zero Trust capabilities.

[26:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1603s) So I wanted to talk about some things
we're doing to help you there.

[26:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1608s) Let's start by talking about how
you connect to your EC2 instances.

[26:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1612s) Many of you are using AWS
Systems Manager session manager

[26:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1615s) to interactively access
your EC2 instances,

[26:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1618s) but at the same time,
SSH is a widespread and popular tool

[27:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1622s) for controlling
and managing EC2 instances.

[27:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1626s) Now, for quite some time
our customers have been able

[27:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1627s) to use Amazon EC2
Instance Connect to SSH

[27:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1632s) to their EC2 instances
with the added benefits of IAM

[27:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1635s) authentication and authorization
and ephemeral keys.

[27:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1639s) But until now, that still meant
that you needed network access

[27:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1643s) to that EC2 instance,

[27:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1644s) either directly
via a public IP address

[27:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1647s) or by way of a bastion host
that you were responsible

[27:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1650s) for patching,
maintaining and securing.

[27:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1652s) So today I am excited to announce
the release of Amazon EC2

[27:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1657s) Instance Connect Endpoint.

[27:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1660s) [applause]

[27:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1665s) This is a new capability
that allows customers to SSH

[27:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1668s) directly to their EC2 instances,
even if they're in a private subnet.

[27:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1673s) So EC2 Instance Connect Endpoint
eliminates the need to have

[27:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1676s) an internet facing EC2 host
and unlike a single bastion host,

[28:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1680s) it's designed for high availability.

[28:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1683s) EC2 Instance Connect Endpoint
also improves your security posture

[28:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1687s) by relying on IAM
for strong authentication

[28:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1690s) and authorization of connections

[28:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1691s) before they even reach
your EC2 instances.

[28:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1696s) And you also benefit
from centralized visibility

[28:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1699s) because these connections
are logged to AWS CloudTrail,

[28:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1703s) everything is fully auditable.

[28:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1706s) Okay, so that was an EC2 instance
and now we're going to zoom

[28:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1709s) all the way out
from that EC2 instance

[28:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1712s) to your whole
AWS environment

[28:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1714s) where we at continue to invest
in the power and breadth

[28:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1718s) of all of these
different kinds of controls

[28:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1720s) for the different sorts
of resources offered by AWS

[28:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1723s) from compute to databases
to networking and storage.

[28:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1725s) And each time we launch one of
these new controls,

[28:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1728s) our customers are able to take
a step forward

[28:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1730s) towards securing their cloud
environments.

[28:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1734s) Now, at the same time, we also hear
from customers

[28:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1737s) that there's a need to continue

[28:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1739s) working to simplify security
in the cloud.

[29:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1742s) There's always going to be a need
for a scalable

[29:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1745s) and clearly defined perimeter
around your cloud environment,

[29:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1748s) in addition to certainly not instead

[29:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1750s) of these ubiquitous fine
grained controls.

[29:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1754s) So why is that?

[29:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1755s) Well, we see a lot of customers
observing that they're operating

[29:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1759s) large and growing environments
with thousands of AWS accounts

[29:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1764s) and even more people operating
in those AWS accounts.

[29:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1768s) And they also recognize
that leveling up

[29:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1770s) a large cloud security staff

[29:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1772s) on cloud security skills is,
well, it's a bit of a journey.

[29:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1778s) So they ask us at for a set
of preventive controls

[29:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1782s) that they can put in place to define
their identity and network boundary.

[29:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1786s) And they tell us that these
controls need to be complementary

[29:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1790s) to all of these individual
IAM policies.

[29:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1793s) The idea is this.

[29:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1795s) Even if one of these operators,
somewhere in this large environment,

[29:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1797s) has made a mistake and misconfigured
a resource, in fact,

[30:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1801s) even if they're actively trying
to create an outside path,

[30:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1804s) our customers tell us
these misconfigurations

[30:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1806s) must not result
in unexpected access.

[30:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1811s) So I get to work with our customers
on the topic of IAM

[30:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1815s) quite a bit,
in fact it's my favorite topic.

[30:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1818s) This topic of a straightforward
perimeter features

[30:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1821s) prominently in these discussions.

[30:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1823s) Now, I find that each customer
organization

[30:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1826s) has its own words to describe
the goal that they're after,

[30:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1829s) but it almost always
goes something like this.

[30:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1832s) Regardless of which of AWS's
hundreds of services we're using,

[30:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1835s) regardless of how large a cloud
environment we operate with,

[30:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1838s) how many AWS accounts,

[30:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1840s) regardless of how many people
are operating in here,

[30:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1842s) and the mix of
their cloud security skills,

[30:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1845s) we need to know that our data
and our resources

[30:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1849s) is going to be accessible
to our organization only.

[30:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1853s) And in many cases, they also add
that we need to know

[30:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1855s) that this data is going to remain
within networks that we control.

[31:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1860s) And therefore a large part
of what we work on at AWS

[31:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1863s) and our security in the cloud
features and services

[31:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1867s) works backward directly
from this goal statement.

[31:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1871s) We even have a name for it.

[31:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1872s) Call it data perimeters.

[31:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1874s) And our focus on data
perimeters is not new.

[31:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1879s) We're on a long journey
together with you,

[31:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1881s) our customers, continually investing
in making this perimeter

[31:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1886s) ever more straightforward
to implement at scale.

[31:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1891s) And over the years
we've invested heavily

[31:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1894s) in two central concepts
of the data perimeter.

[31:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1897s) One is the Organization
and the other

[31:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1899s) is the Amazon Virtual
Private Cloud.

[31:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1903s) Today, our customers are using
the Service Control Policies

[31:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1906s) features of AWS Organizations
to create broad

[31:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1910s) based rules over what their users
can do in their cloud environment.

[31:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1915s) One example preventing data
from being written to resources

[32:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1920s) that are outside
their organization's control.

[32:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1923s) And they use the VPC endpoint
policy capability to assert

[32:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1927s) that all bound requests
from their network

[32:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1930s) are being made on behalf of them.

[32:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1933s) And it's in that vein that I'd like
to tell you

[32:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1935s) about AWS's most
recent data perimeter launch.

[32:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1941s) I'm going to guess that most of you
are familiar with the AWS

[32:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1945s) Management Console
or the console.

[32:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1948s) AWS Management Console
Private Access,

[32:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1950s) which was made
generally available recently,

[32:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1953s) allows you to take your virtual
private cloud network along with any

[32:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1956s) on premise or corporate networks
that are connected to it

[32:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1959s) and limit all use of the console
to your organization only.

[32:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1966s) So why would you want to do
something like this?

[32:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1969s) Well, let's go back to that
previous diagram

[32:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1971s) where the VPC, the virtual
private cloud network,

[32:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1973s) was one of the focal points
of the data perimeter.

[32:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1976s) So you're trying to assert
that whenever anyone or anything

[32:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1979s) in your VPC
is communicating with AWS,

[33:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1982s) that they are doing so on behalf
of the environments that you control.

[33:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1987s) Now for a long time,

[33:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1989s) if these requests were going
directly to the service,

[33:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1992s) you've been able to use virtual
private cloud policies

[33:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1994s) to achieve this goal.

[33:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1997s) Now, we've heard from customers

[33:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=1999s) that they're looking for
a similar kind of control,

[33:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2002s) except for users interactively
signing in and using the AWS console.

[33:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2007s) In other words, if someone's
in your network using AWS,

[33:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2010s) you want to be sure that
they're doing so on behalf of you.

[33:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2014s) But, let's say they're not.

[33:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2017s) Let's say someone's in your network
trying to sign in

[33:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2020s) to an outside unexpected
AWS account.

[33:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2023s) Now, it doesn't matter who this is.

[33:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2024s) It doesn't matter if they're
an employee or an intruder.

[33:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2027s) It doesn't matter why
they're trying to do it.

[33:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2029s) All that matters is that this is an
account that you were not expecting.

[33:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2033s) And you can see here that AWS
Management Console

[33:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2036s) Private Access is preventing
them from signing in.

[34:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2041s) Good.

[34:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2042s) Okay, now in this next example,
someone's using IAM Identity Center,

[34:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2047s) which by the way,
is one of our recommended

[34:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2049s) best practice ways of having
your users access the console.

[34:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2053s) And they're a legitimate user

[34:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2054s) is signing into a recognized account
that you are expecting.

[34:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2058s) They succeed as expected

[34:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2060s) and the lock icon confirms for us
that indeed they're using

[34:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2063s) AWS Management
Console Private Access.

[34:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2066s) And if you're not yet using
IAM Identity

[34:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2069s) Center, don't worry AWS
Management Console Private

[34:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2072s) Access works equally well for all
the different forms of sign in.

[34:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2074s) In fact, we saw an IAM user
in our last failed sign in example.

[34:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2081s) And I wanted to show you
one more level of detail

[34:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2085s) into what AWS management
console private access is.

[34:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2089s) So it's a VPC endpoint, in fact,
a pair of them.

[34:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2092s) And you use DNS to route requests
from users’ browsers to this endpoint.

[34:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2098s) And what you're looking at here
is actually the crux of the feature.

[35:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2101s) This is the VPC endpoint policy

[35:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2103s) that goes along
with console private access.

[35:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2106s) And this policy here that you're
looking at is a broad based policy

[35:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2109s) that says all sign in and use of
the console from this network

[35:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2113s) needs to be for accounts
for people within my organization.

[35:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2119s) So that's exactly what
this control does.

[35:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2122s) It asserts that all use of the AWS
console from within your networks

[35:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2125s) is occurring on behalf of
the environments that you control.

[35:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2130s) And just like all of our other
VPC endpoints,

[35:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2132s) there's nothing sitting here
in the middle intercepting

[35:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2134s) your TLS connections
or inspecting the traffic.

[35:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2138s) Rather, this is an example of one
of those identity level

[35:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2140s) controls that's baked deeply
into our network

[35:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2143s) so that our sign in system can
reject the outside login attempts.

[35:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2149s) So far we've been talking about
preventive controls.

[35:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2154s) I'd now like to move to the realm
of detective controls

[35:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2156s) where we at have also been hard
at work on your behalf.

[36:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2160s) Amazon GuardDuty is the service
that monitors your AWS environment,

[36:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2164s) proactively detecting
and notifying on security threats

[36:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2168s) across the breadth
of AWS's service offerings.

[36:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2171s) And I'm excited to share with you
three new ways

[36:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2174s) in which we've expanded the scope
of what GuardDuty has to offer.

[36:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2179s) First, Amazon GuardDuty now offers
threat detection

[36:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2183s) for Amazon Aurora
by profiling

[36:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2186s) and monitoring access activity
to existing and new databases

[36:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2189s) and using machine learning

[36:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2190s) to accurately detect
suspicious logins.

[36:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2194s) Second GuardDuty recently
added EKS runtime monitoring

[36:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2199s) to detect runtime threats
from over 30 security findings

[36:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2202s) to help you protect
your EKS clusters.

[36:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2204s) And then finally, we've expanded
GuardDuty threat detection coverage

[36:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2208s) to support
AWS Lambda functions

[36:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2210s) by detecting malicious activity
such as a Lambda function

[36:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2214s) that seems to have been repurposed
for unauthorized crypto mining,

[36:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2217s) or one that seems to be communicating
with known bad actors or servers.

[37:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2224s) Siemens is a great example
of how GuardDuty is

[37:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2227s) a critical component
for any security strategy.

[37:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2230s) One of the primary drivers
of Siemens' decision to use AWS

[37:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2234s) was to strengthen
their security posture,

[37:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2236s) automate the running of important
security tasks

[37:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2239s) and centralize access
to all of their data.

[37:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2242s) So they use EKS runtime monitoring
to deepen threat detection

[37:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2245s) inside their containerized workloads,

[37:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2248s) GuardDuty RDS Protection to help
protect data

[37:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2251s) stored
in their Amazon Aurora databases

[37:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2253s) and GuardDuty Lambda protection
to detect threats

[37:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2257s) to their serverless applications.

[37:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2260s) Now, as a builder myself, I know that
I'm responsible

[37:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2264s) for the security
of the code that I write.

[37:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2268s) But I also know that I don't have
my whole security team

[37:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2271s) sitting right next to me for each
and every line of code that I write,

[37:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2273s) as much as I enjoy that.

[37:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2277s) Now, by using automated tools
early on

[38:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2281s) to improve the security of the code

[38:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2282s) that we write
and find issues early on,

[38:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2285s) we can benefit everyone and get
to our business outcomes sooner.

[38:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2289s) So if you work closely with AWS
Lambda functions,

[38:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2293s) you're going to be excited
to hear that today

[38:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2295s) we are making code scans
for Lambda generally available.

[38:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2301s) [applause]

[38:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2306s) Now Amazon Inspector could
already scan Lambda functions

[38:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2309s) and their associated layers
for software vulnerabilities

[38:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2312s) in their package dependencies.

[38:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2314s) And now with this new feature
Inspector can also scan

[38:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2317s) your own code
for security vulnerabilities

[38:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2320s) such as injection flaws,
data leaks, weak or missing crypto

[38:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2325s) and it has a high true positive rate.

[38:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2328s) It provides actionable security
findings and remediation guidance

[38:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2331s) that follow AWS
security's own best practices.

[38:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2336s) Now, we all know that modern
applications

[38:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2339s) rely increasingly on open source
and third party dependencies.

[39:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2344s) In fact, if we look at our own
open source software, the AWS SDK,

[39:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2348s) we can see that it pulls in quite
a few dependencies of its own.

[39:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2353s) And in practice that means deep
and wide dependency trees

[39:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2357s) which need to be managed
on an ongoing basis.

[39:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2360s) And we hear from builders
that they need tools to manage,

[39:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2363s) track and analyze packages

[39:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2365s) and deployable artifacts
such as container images,

[39:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2368s) Lambda functions and the software
that they deploy to EC2 instances.

[39:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2374s) So today we are excited to announce
the launch of a new capability

[39:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2377s) within Amazon Inspector to allow you
to automatically and centrally manage

[39:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2382s) SBOM or Security Bill
of Materials exports.

[39:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2393s) With one click, you can now
export SBOMs in open standard formats

[39:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2397s) for all Inspector monitored resources
to a preconfigured S3 bucket,

[40:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2402s) and from there you'll be able
to download the artifact,

[40:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2406s) run Athena queries on it,

[40:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2407s) or create QuickSight dashboards
to gain further insights.

[40:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2411s) And this complements the existing
continual vulnerability management

[40:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2414s) capabilities within Inspector

[40:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2416s) by providing a detailed
software dependency list,

[40:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2419s) contributing to your wider efforts
in securing your software.

[40:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2424s) Our journey to help you improve
your security posture

[40:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2428s) by implementing more comprehensive
Zero Trust architectures,

[40:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2432s) robust data perimeters and granular
purpose built controls continues

[40:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2437s) as we constantly innovate
on your behalf.

[40:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2440s) And next, we're going to hear
from one of our customers

[40:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2443s) about how their security, culture
and renewed focus

[40:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2446s) on end-to-end security
is helping them scale

[40:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2449s) and operate more securely on AWS.

[40:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2452s) Thank you so much.

[40:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2454s) [applause + music playing]

[40:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2459s) The power of one, may be strong.

[41:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2463s) But the power of 80,000,
it's unstoppable.

[41:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2472s) And today, like every day,

[41:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2477s) our goal is to put customers first.

[41:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2481s) To welcome you with an experience
designed with you in mind.

[41:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2487s) [music playing]

[41:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2493s) Because at Delta, it's not just
the destination,

[41:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2500s) it's the journey
that makes the difference.

[41:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2503s) [music playing]

[41:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2508s) [applause]

[41:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2514s) Please welcome Senior Vice President
and Chief Information

[41:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2518s) Security Officer,
Delta Airlines Debbie Wheeler.

[42:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2528s) Good morning and thank you.

[42:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2531s) In 2022, 420 million plus individuals

[42:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2537s) experienced a data breach.

[42:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2540s) And in 2022, Delta Airlines

[42:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2543s) was entrusted
by 177 million passengers

[42:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2548s) to deliver them safely
to their final destinations

[42:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2551s) while protecting their personally
identifiable information.

[42:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2555s) Ours is a complex industry
full of regulations

[42:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2559s) and lots of safety protocols.

[42:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2562s) And with a team of 90,000 people
around the world

[42:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2567s) connecting millions of passengers
to their final destinations,

[42:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2572s) doing so safely and securely,
a culture of security is imperative.

[42:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2579s) I'd like to share with you today
three elements

[43:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2582s) we believe contribute to
the security environment in Delta.

[43:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2589s) And the first starts with fostering
a security aware culture.

[43:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2595s) At Delta, people are our business.

[43:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2600s) A vibrant security culture

[43:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2603s) that embraces
the shared values of our people

[43:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2606s) are critical to how we secure
our customer information

[43:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2610s) and our employee information.

[43:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2613s) We believe our people are key
in thwarting

[43:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2617s) and defending the airline against
the cyber threats we experience

[43:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2622s) and allowing us to maintain
a world class operation.

[43:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2629s) The first element of our security
program starts with leadership.

[43:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2636s) From the CEO to the CISO
to our ground handling crews,

[44:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2642s) to our gate agents –

[44:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2643s) every member of the Delta team

[44:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2646s) must embrace a safe
and secure culture

[44:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2649s) in order to provide for
the protection of our customers

[44:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2652s) and our employees.

[44:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2654s) Leadership sets that example,

[44:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2657s) walking the walk
and talking the talk,

[44:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2659s) we expect our employees
to follow.

[44:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2663s) But leadership expects accountability

[44:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2666s) and people need to buy into
the message that we're delivering.

[44:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2671s) And in order for them to do so,

[44:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2673s) we need to enable them with
the tools, the processes and data

[44:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2678s) that allow them to protect
the information

[44:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2680s) that our customers entrust
to our care.

[44:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2684s) In a cloud environment,
you build it, you run it, you own it.

[44:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2691s) And we've had to transition
how we think about security

[44:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2695s) and how we enable
our people to do that.

[44:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2698s) So, as we have embraced
the journey to the cloud,

[45:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2702s) we have had to shift left,
the security inside of Delta.

[45:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2709s) Depending on our development teams
to build security in

[45:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2714s) from the beginning
of their development process

[45:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2717s) rather than tacking it
on at the end.

[45:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2720s) And in order to do that,
Delta has partnered with AWS

[45:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2725s) and created the reference
architecture library

[45:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2730s) that contains security

[45:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2732s) approved patterns, configurations,
requirements and guardrails

[45:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2737s) that we expect our developers
to implement into their code.

[45:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2742s) In addition, the security team
at Delta

[45:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2746s) has been focused on automation.

[45:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2748s) Automation
allows our security services

[45:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2751s) to scale across Delta's vast
IT portfolio.

[45:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2755s) The use of automation
through AWS Security Hub,

[45:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2759s) AWS GuardDuty and AWS
Config enables the security team

[46:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2765s) to provide our developers
with centralized visibility

[46:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2769s) to how their applications
are complying

[46:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2771s) with our security requirements

[46:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2774s) at any point during
the development process.

[46:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2777s) The goal being no more surprise
security findings

[46:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2781s) prior to moving
to production.

[46:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2784s) Ours is a people-oriented
environment.

[46:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2787s) And prior to our cloud journey,

[46:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2789s) Delta has always been laser-focused
on safety and security.

[46:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2795s) The third element that I want
to speak to you today

[46:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2798s) with respect to our program

[46:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2800s) and what we believe
makes it successful

[46:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2802s) is perhaps
the most important element,

[46:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2805s) and that is embracing the culture

[46:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2807s) and the values your people have
and embedding your security message

[46:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2812s) into that culture
and into those values.

[46:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2817s) As I said, we are a diverse
workforce, 90,000 people,

[47:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2821s) 70,000 of whom are customer
facing on any given day.

[47:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2826s) They're using a myriad
of digital devices

[47:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2828s) and applications
to serve our customers

[47:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2831s) to protect their physical safety
as well as their digital safety.

[47:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2836s) And as I said, our people
are critical to that mission.

[47:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2841s) In order to ensure that
they're well equipped

[47:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2844s) to provide those services
to our customers,

[47:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2848s) we've worked tirelessly
with our employees

[47:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2851s) to help them understand
security habits or hygiene

[47:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2855s) that they can practice at home.

[47:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2857s) Our thinking is if we can teach them
how to take care of their information

[47:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2862s) and their personal life
and teach them how they can help

[47:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2865s) their loved ones care
for their information,

[47:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2867s) they'll bring those habits
back into the work environment,

[47:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2870s) and that will extend to how
they protect the information

[47:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2874s) that our customers and fellow
employees entrust to their care.

[48:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2880s) Safety first, always.

[48:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2883s) It's our core value.

[48:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2885s) It headlines our flight plan.

[48:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2888s) Our flight plan reflects
Delta's goals and objectives

[48:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2891s) on an annual basis.

[48:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2893s) And while the flight plan
changes year to year,

[48:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2896s) what never changes
is safety first.

[48:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2900s) Always.

[48:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2903s) When I met with C.J. Moses and
Steve Schmidt several weeks ago,

[48:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2908s) we talked about the journey
that Delta has been on

[48:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2911s) and we talked about these core
principles that we believe contribute

[48:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2915s) to the success
of our security awareness program.

[48:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2918s) And they felt strongly that
in sharing these principles

[48:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2921s) with all of you,
there may be benefit

[48:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2923s) in how you develop
your own awareness programs.

[48:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2926s) But I recognize that not
every industry,

[48:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2929s) what works for Delta
may not work for you.

[48:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2931s) We are all under a constant
barrage of threats.

[48:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2935s) But what I will share with you
is this –

[48:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2938s) our security aware culture has not
impeded our ability to innovate.

[49:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2943s) It has not impeded the ability
that we have to collaborate

[49:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2946s) with our development teams
and with our business partners.

[49:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2950s) If anything, it has strengthened
those collaborations

[49:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2953s) and it has allowed
our development teams

[49:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2955s) to move in a more agile way
in securing the applications

[49:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2960s) and the services
that they are designing.

[49:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2963s) Fostering this environment
is contributing

[49:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2968s) to how our teams are able to protect
not just the physical passenger,

[49:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2974s) but the digital passenger as well.

[49:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2978s) I'd like to thank C.J. for inviting
me to speak with you this morning

[49:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2982s) and I'd like to remind you
all to please fly Delta.

[49:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2985s) Thank you.

[49:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2987s) [music and applause]

[49:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2991s) Thank you.

[49:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2997s) Thank you, Debbie.

[49:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=2998s) It's always great to see
how customers leverage AWS

[50:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3002s) to innovate safely.

[50:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3004s) So far we've talked about the shared
responsibility model

[50:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3007s) and how a culture
of security empowers you

[50:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3010s) to build the right
security strategy for your business.

[50:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3013s) But there is another
critical component

[50:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3015s) that extends the benefits of AWS,
and that's our AWS Partner Network.

[50:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3021s) Our broad Marketplace provides
you with access

[50:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3023s) to thousands of third party solutions
that integrate deeply into AWS

[50:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3030s) and address specialized
security needs.

[50:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3033s) But one thing we hear loud and clear
is that customers

[50:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3037s) want the centralized
security data from the cloud

[50:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3039s) on premises and custom sources to
gain better visibility and insights,

[50:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3044s) which is difficult with all
the different logging formats.

[50:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3048s) To help you with this challenge,

[50:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3050s) we recently released Amazon
Security Lake –

[50:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3054s) our new automated data lake service

[50:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3056s) that enables customers
to centrally aggregate,

[50:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3058s) manage and derive value

[51:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3060s) from the security related
logs and event data.

[51:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3064s) Data in Security Lake is stored
in an open

[51:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3067s) cybersecurity schema
framework format,

[51:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3069s) an open standard
developed in collaboration

[51:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3072s) with other industry leaders.

[51:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3074s) Today we have over 50 partners

[51:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3076s) that integrate directly
with Security Lake to store

[51:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3078s) and provide security analytics
to our customers.

[51:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3083s) One customer that relies heavily
on Amazon Security Lake is FINRA.

[51:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3088s) FINRA enables investors in firms
to participate in the stock market

[51:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3092s) with confidence
by safeguarding its integrity.

[51:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3096s) They use a wide variety of security
tools to secure their AWS environment

[51:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3101s) and ensure the security
of their data.

[51:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3104s) Using Amazon Security Lake,

[51:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3106s) they centrally manage their security
data,

[51:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3108s) saving substantial time and effort
in deriving value from their data.

[51:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3113s) Now, another thing you told us is

[51:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3115s) that when it comes to choosing
partner solutions,

[51:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3118s) you want to have the assurance that
the third party products you choose

[52:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3122s) are designed to integrate
with your existing services.

[52:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3127s) That's why I'm excited to announce

[52:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3129s) the preview
of Built-In Partner Solutions.

[52:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3133s) Thank you.

[52:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3134s) [applause]

[52:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3136s) You can learn more by browsing
the AWS Built-In Partner page

[52:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3140s) offerings by use case.

[52:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3142s) Once released in AWS
Marketplace later this year,

[52:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3146s) you'll be able to purchase
partner software

[52:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3148s) coupled with AWS native tools
and an automated deployment

[52:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3151s) powered by infrastructure as code
tools and validated by experts.

[52:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3157s) And while we're on the subject
of partners,

[52:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3159s) I'm excited to announce
a new initiative

[52:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3161s) that we're launching today
in collaboration

[52:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3162s) with our global systems
integrators,

[52:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3165s) the AWS
Global Partner Security Initiative.

[52:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3168s) With this new initiative will be
jointly developing

[52:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3172s) end-to-end security solutions
and managed services,

[52:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3175s) leveraging the capabilities,

[52:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3177s) scale and deep security knowledge
of our GSI partners.

[53:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3181s) Our partners will leverage
Amazon Security Lake

[53:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3183s) to provide customers
the most robust cyber signals

[53:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3186s) and threat intelligence information.

[53:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3188s) We already have five partners
lined up, Atos, Deloitte,

[53:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3193s) PwC, Accenture and Kyndryl,
and we will be onboarding more soon.

[53:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3200s) Finally, we know that our customers
sometimes struggle

[53:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3203s) to operationalize their security
for all sorts of reasons,

[53:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3206s) including staffing
or skill shortages.

[53:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3210s) This is exactly why our AWS
Partner Network has created

[53:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3213s) three competencies containing
partners with some of the world's

[53:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3216s) most talented AWS security experts.

[53:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3219s) If you need software
and consulting solutions

[53:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3221s) for specific workloads or use cases,

[53:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3224s) then you can find a partner
in the security services competency.

[53:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3227s) For 24 x 7 managed security services,
our partners in the Level one MSSP

[53:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3232s) competency can provide you
with all the expertise you need.

[53:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3235s) And finally, partners in the cloud
operations competency

[53:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3239s) offer you comprehensive solutions
to help you with governance,

[54:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3242s) monitoring, observability,
compliance and auditing.

[54:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3247s) Security is a constantly
evolving landscape,

[54:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3249s) so let's shift gears a little bit
and look at the areas

[54:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3252s) where we're investing in
as we prepare for what lies ahead.

[54:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3259s) For the past few months
generative AI, yes,

[54:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3261s) I said it in large language models
have been capturing

[54:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3265s) everyone's imagination.

[54:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3267s) Generative AI is a type
of artificial intelligence

[54:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3270s) that can create new texts,
photos, videos,

[54:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3273s) even code
from simple language prompts.

[54:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3276s) Generative AI is democratizing
content creation

[54:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3280s) by providing simple,
yet extremely powerful tools

[54:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3282s) that are open
and accessible to everyone.

[54:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3285s) However, without clear security
guidance and governance,

[54:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3288s) generative AI risks introducing a
number of security and privacy risks.

[54:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3295s) As with any other tool,

[54:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3297s) there is an opportunity
for people to misuse it.

[55:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3300s) Threat actors could leverage
generative AI

[55:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3302s) to automate the creation
of phishing emails,

[55:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3306s) social engineering attacks
and other types of malicious content.

[55:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3310s) Many of the generative
AI services available today

[55:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3312s) have been trained
to prevent malicious use

[55:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3315s) and have some form of guardrails

[55:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3317s) that prevent users
from abusing their capabilities.

[55:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3320s) But unfortunately, there are
almost always ways and scenarios

[55:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3324s) where motivated actors will find
their way to abuse them.

[55:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3328s) However, that same power and ease
of use

[55:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3330s) can make artificial intelligence

[55:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3332s) an indispensable tool
in the hands of security engineers.

[55:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3337s) At AWS, we help you automate
the identification

[55:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3340s) and resolution of issues
more effectively,

[55:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3342s) and machine learning is one
of the biggest areas of impact.

[55:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3347s) We're examining how large
language models can improve security

[55:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3350s) throughout the threat prevention,
detection and response cycles.

[55:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3353s) A couple of months ago, we announced
Amazon Bedrock

[55:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3358s) and multiple generative AI services
and capabilities to help you build

[56:02](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3362s) and scale your own generative
AI applications.

[56:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3365s) Bedrock provides you the broad
range of foundational models

[56:10](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3370s) so that you can choose the ones
that best fit your needs.

[56:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3372s) Bedrock is yet another example
of how AWS

[56:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3374s) is carefully considering
the security implications

[56:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3377s) so that you don't have to.

[56:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3379s) Bedrock enables private fine
tuning of foundation models

[56:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3383s) and supports the encryption,
access control

[56:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3385s) and auditing with AWS,
IAM, KMS and CloudTrail

[56:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3389s) and with AWS PrivateLink.

[56:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3391s) Data is securely transferred
through the AWS network

[56:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3394s) and never through
the public internet.

[56:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3397s) Bedrock never uses customer data
to train the underlying models.

[56:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3401s) Instead, Bedrock makes a separate
copy of the Base Foundation model

[56:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3405s) that is accessible
only to you and trains

[56:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3408s) this private copy of the model.

[56:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3412s) I think the easiest way to leverage
generative AI for security

[56:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3417s) is when it's embedded
invisibly into applications.

[57:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3420s) That's why we released
Amazon CodeWhisperer,

[57:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3424s) our AI powered code companion

[57:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3426s) that radically improves
developer productivity

[57:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3429s) by generating code
suggestions in real time.

[57:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3432s) CodeWhisperer is the only
AI coding companion

[57:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3435s) with built in security scanning
to help you find remediations

[57:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3438s) for hard-to-detect vulnerabilities.

[57:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3441s) In addition, it can filter out
biased or unfair code recommendations

[57:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3446s) and can flag these code suggestions
that resemble open source code.

[57:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3451s) If developers choose to use
that code,

[57:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3453s) CodeWhisperer logs the acceptance
along with the licensing information.

[57:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3458s) In our efforts to improve
developer productivity,

[57:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3461s) extended to support
the full development life cycle,

[57:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3465s) because we know how important
it is to be able

[57:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3467s) to identify and address security
vulnerabilities as early as possible.

[57:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3472s) That's why I'm excited
to announce today

[57:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3474s) the public preview
of Amazon CodeGuru Security.

[57:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3479s) [applause]

[58:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3485s) This newest service
in our AppSec toolchain

[58:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3487s) integrates with IDEs
and the CI/CD pipelines

[58:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3491s) and uses ML and automated reasoning
to help you build more secure code

[58:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3494s) by detecting vulnerabilities
in your code

[58:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3497s) at any stage of
the development life cycle.

[58:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3500s) CodeGuru Security's enhanced
algorithms

[58:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3503s) help engineers
and infosec teams save time

[58:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3505s) by reducing false
positives detections.

[58:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3511s) And how many of you feel
overwhelmed

[58:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3512s) by the sheer volume of security
findings you need to analyze?

[58:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3516s) I know I do.

[58:37](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3517s) I think we all struggle
with the alert fatigue

[58:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3519s) from time to time.

[58:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3522s) Some of our customers run
thousands of applications in AWS,

[58:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3526s) so they generate millions
of findings every week.

[58:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3529s) Humans alone are not able
to deal

[58:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3530s) with the increasing complexity
and volume of security threats.

[58:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3533s) We found that the key
in managing modern security

[58:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3537s) is to lean on artificial
intelligence and machine

[58:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3539s) learning to help prioritize findings
and accelerate incident response.

[59:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3544s) That's why today, I'm excited
to announce

[59:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3547s) that we're expanding Finding Groups,
a feature in Amazon Detective

[59:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3551s) that uses ML to distill
thousands of security findings

[59:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3554s) to connected security events.

[59:17](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3557s) [applause]

[59:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3563s) Finding Groups enables you
to examine multiple activities

[59:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3566s) as they relate
to a single security event

[59:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3568s) by analyzing thousands
of unique security findings

[59:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3571s) aggregated from AWS Security Hub
across hundreds of AWS resources.

[59:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3575s) The output of this feature
makes it easier to understand

[59:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3578s) the complex interactions
that resulted

[59:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3580s) in a potential issue
or security event.

[59:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3582s) Detective can now group
Amazon Inspector

[59:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3585s) and GuardDuty findings to help you
answer hard questions like,

[59:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3589s) was the EC2 instance compromised
because of a vulnerability?

[59:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3593s) Or how did the threat actor move
laterally within my infrastructure?

[59:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3597s) After the analysis, Finding Groups
produces interactive visualizations

[01:00:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3600s) to help you conveniently view
all of the details

[01:00:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3603s) related to multiple items
in the single panel.

[01:00:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3606s) Finding Groups also maps according
to the MITTRE ATT&CK framework

[01:00:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3609s) to help you improve
threat detection.

[01:00:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3613s) However, there are many
more areas

[01:00:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3615s) where LLMs can have a significant
impact on security teams

[01:00:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3618s) by enhancing and complementing tools
and processes.

[01:00:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3622s) For example, we can train
generative AI models

[01:00:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3624s) to create threat
hunting queries,

[01:00:27](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3627s) summarize the event data
from an attack,

[01:00:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3629s) write a remediation code
for vulnerabilities,

[01:00:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3631s) write penetration test scripts

[01:00:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3632s) for to automate the creation
of YARA rules for malware detection.

[01:00:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3638s) With generative AI taking care
of these lower level tasks,

[01:00:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3641s) we can scale out
our security teams

[01:00:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3643s) and enable them to focus
on innovation

[01:00:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3645s) and higher level operations.

[01:00:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3648s) As for mitigating generative
AI based attacks,

[01:00:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3651s) we need to remember that this
technology only makes it easier

[01:00:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3654s) for people that don't have deep
experience to create malicious code.

[01:00:59](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3659s) So what generative AI really changes
is not how the malicious code works,

[01:01:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3664s) but how it gets created.

[01:01:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3666s) For example, even though these tools
may be used

[01:01:08](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3668s) to generate more sophisticated
and accurate phishing emails,

[01:01:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3672s) the way we protect our users
against them

[01:01:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3675s) shouldn't and doesn't need
to really change.

[01:01:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3679s) Another area we're focused
on at AWS

[01:01:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3683s) is security in a world
where quantum computers

[01:01:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3686s) are as prevalent
as today's classical computers.

[01:01:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3690s) Classical processors use bits
to perform their operations,

[01:01:33](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3693s) whereas quantum computers use qubits
to run multidimensional algorithms.

[01:01:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3698s) Quantum computers, by encoding
information in quantum systems

[01:01:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3701s) like atoms or photons,

[01:01:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3703s) promise to speed up
some specific computational tasks

[01:01:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3706s) that are beyond the reach
of classical computers.

[01:01:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3709s) Additionally, the amount
of information a qubit system

[01:01:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3711s) can represent
grows exponentially.

[01:01:54](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3714s) For example, information
that 500 qubits

[01:01:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3717s) can easily represent
will not even be possible

[01:02:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3720s) with more than two
to the 500th classical bits.

[01:02:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3724s) For context, even if you were
to run one of today's

[01:02:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3727s) most powerful supercomputers
continuously for billions of years,

[01:02:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3731s) it would not be able
to calculate this number.

[01:02:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3735s) Building these machines
is a significant challenge

[01:02:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3739s) and we had to come up
with a new way of thinking

[01:02:22](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3742s) in order
to design their algorithms.

[01:02:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3745s) But even at this early stage,

[01:02:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3746s) quantum computing is driving
new discoveries in health care,

[01:02:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3750s) energy, environmental systems,
smart materials and beyond.

[01:02:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3755s) As exciting as it sounds,

[01:02:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3756s) it also comes
with its own security challenges

[01:02:39](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3759s) and as we like to say,
opportunities.

[01:02:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3761s) One of these challenges
is cryptography.

[01:02:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3764s) Information encrypted today
could be at risk

[01:02:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3767s) when sufficiently powered quantum
computers become available.

[01:02:51](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3771s) Some of the schemes we use today

[01:02:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3772s) in public key
cryptographic algorithms

[01:02:55](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3775s) to protect our data
will not be adequate

[01:02:57](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3777s) in a post quantum
computing world.

[01:03:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3780s) For example, to decrypt
a normal 2048 bit RSA key,

[01:03:05](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3785s) it would take 300 trillion years
with a classical computer,

[01:03:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3791s) whereas it would only take a day
in a fault tolerant quantum computer.

[01:03:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3796s) Encryption is a fundamentally
important part

[01:03:19](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3799s) of any business operation.

[01:03:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3801s) It allows you to have
cryptographically provable confidence

[01:03:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3805s) in the confidentiality
and integrity of your data.

[01:03:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3808s) If you store data in AWS services,

[01:03:30](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3810s) then we already mitigate
against store and decrypt attacks

[01:03:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3814s) on the encrypted data
in the service.

[01:03:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3816s) And AWS provides no method or data
path for access to ciphertexts

[01:03:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3821s) that AWS created on your behalf.

[01:03:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3823s) So it is difficult for the threat
actors to retrieve

[01:03:45](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3825s) and store
such ciphertexts for later study.

[01:03:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3829s) The encryption keys travel
solely within the control plane

[01:03:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3833s) and the ciphertext is only visible
on the physical network.

[01:03:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3838s) So AWS is leading in the development
of quantum resistant

[01:04:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3841s) cloud scale cryptographic technology
and is working

[01:04:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3844s) with the National Institute
of Standards and Technology

[01:04:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3847s) and the broader
cryptographic community

[01:04:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3849s) to help standardization efforts.

[01:04:12](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3852s) We also maintain and contribute
to many open source projects

[01:04:15](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3855s) on post-quantum crypto algorithms
and tools such as the AWS-LC,

[01:04:20](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3860s) a general purpose post-quantum
cryptographic library

[01:04:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3863s) and Open Quantum Safe that contains
a set of tools for prototyping

[01:04:28](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3868s) and benchmarking post-quantum
cryptographic algorithms.

[01:04:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3872s) The migration to PQC may not happen
overnight,

[01:04:35](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3875s) but it's well underway
and it has the potential

[01:04:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3878s) to impact everyone
that uses public key crypto today.

[01:04:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3883s) At Amazon, we know the value
of long term thinking

[01:04:46](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3886s) and we routinely make big,
long term investments in availability

[01:04:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3889s) and security based upon our belief
of where the world is going.

[01:04:53](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3893s) Post-quantum cryptography is
another example of an area

[01:04:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3896s) where we are investing
for your future.

[01:05:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3900s) To help you evaluate the readiness
of your application on AWS,

[01:05:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3903s) we offer the option to run
quantum resistant cryptography

[01:05:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3906s) alongside your traditional cryptography
in your applications today.

[01:05:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3911s) We have contributed to a draft
standard on the post quantum

[01:05:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3914s) hybrid key exchange and implemented

[01:05:16](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3916s) and deployed the community
developed specification in s2n-tls,

[01:05:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3921s) which implements the Transport Layer
Security protocol across all of AWS.

[01:05:26](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3926s) And we've developed hybrid key
exchange to our most

[01:05:31](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3931s) secure security
sensitive services like AWS,

[01:05:34](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3934s) Key Management Service, Certificate
Manager, Secrets Manager.

[01:05:38](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3938s) You can begin testing the impact
of Post-quantum

[01:05:41](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3941s) cryptography in your applications

[01:05:43](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3943s) by enabling hybrid post-quantum TLS
in your AWS SDK.

[01:05:47](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3947s) As part of our shared
responsibility model,

[01:05:49](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3949s) we are hoping to add post-quantum
cryptographic capabilities

[01:05:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3952s) in more AWS services so that you can
prepare for a more secure future.

[01:06:01](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3961s) I never get tired explaining
what security is

[01:06:04](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3964s) and I'm excited
to come to work every day

[01:06:06](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3966s) because our job is never done.

[01:06:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3969s) In a landscape where everything
is constantly evolving

[01:06:11](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3971s) and we get to tackle
new challenges

[01:06:14](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3974s) and find different ways to stay
ahead in our defense mechanisms.

[01:06:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3978s) Throughout this keynote, we talked
about how our security strategy

[01:06:21](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3981s) is deeply rooted
in shared responsibility

[01:06:25](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3985s) and how we are
constantly innovating to help

[01:06:29](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3989s) you meet your security
and business needs.

[01:06:32](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3992s) As we get ready for the exciting
couple of days ahead of us,

[01:06:36](https://www.youtube.com/watch?v=_piUB5FrYVE&t=3996s) let's remember to embrace the spirit
of enthusiasm and curiosity.

[01:06:40](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4000s) Learning should be
an exciting adventure

[01:06:42](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4002s) that sparks innovation
within us,

[01:06:44](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4004s) so make sure to immerse yourself
in engaging sessions,

[01:06:48](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4008s) productive discussions,

[01:06:50](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4010s) and the opportunity to create
valuable connections.

[01:06:52](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4012s) Together, we can create
a formidable defense

[01:06:56](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4016s) against the threats
that lie ahead.

[01:06:58](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4018s) Our collective knowledge
is the foundation

[01:07:00](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4020s) of a resilient
security ecosystem.

[01:07:03](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4023s) Thank you for joining us
on this remarkable journey

[01:07:07](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4027s) where we're just getting started.

[01:07:09](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4029s) re:Inforce 2023 will be
an unforgettable celebration

[01:07:13](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4033s) of security and innovation
in the shared pursuit of knowledge.

[01:07:18](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4038s) Let's build trust and secure
the future together.

[01:07:23](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4043s) Thank you.

[01:07:24](https://www.youtube.com/watch?v=_piUB5FrYVE&t=4044s) [applause and music]

