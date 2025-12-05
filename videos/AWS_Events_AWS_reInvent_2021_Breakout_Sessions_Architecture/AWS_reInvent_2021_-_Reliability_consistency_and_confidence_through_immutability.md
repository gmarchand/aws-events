# AWS re:Invent 2021 - Reliability, consistency, and confidence through immutability

[Video Link](https://www.youtube.com/watch?v=n00QuaNzjiY)

## Description

Immutable infrastructure is a model in which no updates, security patches, or configuration changes happen “in place” on production systems. If any change is needed, a new version of the architecture is built and deployed. Because changes aren’t allowed in immutable infrastructure, you can be confident in the deployed system. Immutable infrastructures are more consistent, reliable, and predictable, and they simplify many aspects of software development and operations by preventing common issues related to mutability. In this session, dive deep into the topic to learn why immutable infrastructure is essential in cloud architecture.

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK
 
Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

(upbeat music) - Hi everyone and thanks
for joining this session. Immutable infrastructure is
a model in which no updates, security patches or configuration changes happen in place on production systems. If any change is needed, a new
version of the architecture is built and deployed. And because changes aren't allowed in immutable infrastructure, you can be confident
in the deployed system. I'm Gunnar Grosch. I am a
developer advocate at AWS. And in this session we're
gonna dive deep into the topic to learn why immutable
infrastructure is essential in cloud architecture. As per the dictionary,
something that is immutable is something that's not capable
or susceptible to change. So why does it matter? Before answering this question, let's take a look at immutability
in programming languages because the problem with mutability there, it's probably a lot more
familiar to many of you. So I love many different
programming languages and Python is one of them. But mutability in Python
can and often is a headache. So let's simply assign variables here, something simple and yet as
you can see in this example, in Python if you assign a
variable to another variable of a mutable data type, any changes are reflected
by both variables. So the new variable bar
is just an alias for foo. So let's do the same in Erlang now. Or try to do because you can't. Languages such as Erlang, Rust, Scala, Haskell, Clojure and a few others, they offer immutable data structures and single assignment
variables with the premise that immutability leads to better code. Simpler to understand
and easier to maintain. And at this point,
you're probably wondering why does immutability matter and what does it have to
do with cloud architecture. Well, headaches. The immutable infrastructure paradigm comes from the same ideas behind immutability in
programming language. It is the idea that your architecture doesn't change once it is deployed and it saves you from headaches. So let's dive into into it and look at traditional
infrastructure first so we can understand the
issue with immutability here. Not so long ago it was
quite common for folks to brag about uptime. The problem though is that
long periods of uptime often indicates
potentially lethal problems because critical updates,
either software or hardware, often require rebooting. So let me ask you this
very simple question. Which of these two choices
make you more anxious? First, rebooting a server
that's been up for 16 years or second, rebooting a server
that's just being built? Well, I guess we answer the same thing. Just talking about rebooting
a 16 year old server, it gives me anxiety because
I have no idea what's changed in the 16 years since its initial boot up. So how many undocumented hotfix were done? Why was it never rebooted? Are there some hidden
or magic dependencies? To me, that's really terrifying. Other common practice in
traditional infrastructure is mutable deployments, meaning the deployment
pipeline gets the code, fetches the dependency,
builds the artifacts and deploys them for
every environment stage of the deployment pipeline. One build per environment. What you test and validate here isn't what you're gonna end up deploying. Also in traditional IT infrastructure, servers are typically updated
and modified in place. We SSH into our servers, we install, we update or upgrade packages. We tweak and we optimize
configuration files. It goes something like this. You log in, you stop the app,
you update the repositories, you do a library upgrade, you test. Sometimes you debug often
and you restart the app and then you hope for the best. And during that time, the
system is often down by the way. All of these were and often
still are standard practices. Less common practice though is to document all of these changes. And interestingly, the process is like change management and ITIL. They've been created in the industry to try to solve the
problems due to changes, but never addressed the
root cause of these issues and instead they just slow things down. So in my opinion, the solution
to mutability isn't process, but not doing changes in the first place and with the cloud, it's
becoming more and more easy. And even for more advanced architecture using multi-availability
zones, auto scaling groups, I've seen and I guess I'm
guilty to this myself, I'm used to SSH to fix and tune things up. So we say just a quick
edit to the config file to save the weekend and we promise that we'll document and automate the fix first thing Monday morning,
but perhaps we never do. So I like to call this
practice SSH love syndrome. These practices make servers mutable. They change, author, they are created. So besides giving you headaches, mutations also lead to
configuration drifts which happens when active
configurations diverge from the initially approved
and deployed configuration. One of the main challenges
with configuration drifts is that they make it hard to
just replace or debug things, making recovering from issues difficult. So how many of your
applications fetch dependencies from the internet during the build process or even worse at runtime? I've seen places where
deploying to production meant first launching any instance. In this sense it could be a different AMI between different environments, then fetching the code from
different repos, building it, replacing the artifacts in place and finally, rebooting the server. One step was probably missing though and that is the pray step. I'm sure all of you are either smiling or horrified by that the idea. But how about your pip and npm install? How about docker build? What guarantees do you have that the dependencies you're installing that they don't change
between deployments? And what if you're deploying
to multiple machines or multiple environments? Don't you believe that
this can be a problem? So you can read how one
programmer broke the internet by deleting a tiny piece
of code, a blog post. And what happens if your code repository has issues when you deploy and you can't download
your code when you need it? So installing dependencies at runtime isn't attack vector for a
malicious code injection and it renders auto scaling slow. And that deployment behavior,
it's fragile at best and it leads to deployment
mistakes and frequent rollbacks. And that's just if you're lucky. Luckily of course, there
is a solution to this and put simply, immutable
infrastructure is a model in which new updates, security patches or configuration changes happen in place on production systems. If any change is needed, the
new version of the architecture is built and deployed into production. And this is not a new idea. In fact, the term
immutable infrastructure, it was coined by Chad
Fowler in this blog post, "Trash Your Servers and Burn Your Code: Immutable Infrastructure
and Disposable Components." It was published in 2013. Since then, the idea has rightfully so gained popularity and followers, especially as systems
have become more complex and more distributed. And immutable infrastructure
means that if a server needs an update or a fix,
new servers are deployed instead of updating the ones already used. Once it is deployed, we simply
update the routing mechanism to route the traffic to the
new version of the application. So deploying applications
in immutable infrastructure should use the canary deployment pattern. Canary deployment is a technique used to reduce the risk of failure when new versions of
applications enter production by creating a new environment with the latest version of the software. You then gradually roll out the change to a small subset of users and slowly making it
available to everybody if no deployment errors are detected. So canary deployment is
sometimes called a phase or an incremental rollout. And once the new version
is deployed to all users, you can slowly decommission
the old version and this strategy minimizes the potential blast radius of failure, limiting the impact on customers. It is therefore a preferred version. And the benefit of canary
deployment is of course the near immediate rollback it gives you. But more importantly, you
get fast and safer deployment so it's real production test data. The main challenge with canary deployment is routing traffic to multiple
versions of the application. So consider several routing
or partitioning mechanism. Internal teams versus customers. Paying customers versus
non-paying customers. Your graphic-based routing
using feature flags or perhaps even random. And by keeping canary
traffic selection random, most users aren't adversely
affected at any time by potential bugs in the new version. And no single user is adversely
affected all the time. So how do we do canary deployments on AWS? Route 53, a DNS service, lets you use a weighted routing policy
to split the traffic between the old and the new version of the software you are deploying. Weighted routing enables you
to associate multiple resources with a single domain
name or a subdomain name and choose how much traffic
is routed to each resource. It is particularly useful
for canary deployments. And to configure a weighted
routing for canary deployments, you assign each record a relative weight that corresponds with how
much traffic you wanna send to each resource. So Route 53 sends traffic to a resource based on the way that
you assign to the record as a proportion of the total
weight for all records. So in this example, the
resource with a weight of 10 gets 10 hundredth of the traffic so 10% and the other resource gets 90%. If there's one inconvenience to using DNS, it is propagation time. So Amazon Route 53 is designed
to propagate updates you make to your DNS records to
its worldwide network of authoritative DNS service within 60 seconds under normal conditions. However, caching DNS resolvers
are outside of the control of Amazon Route 53 service and you will cache your
resource record sets according to their time
to live, the TTL value. So watch out for the default
TTL values and shorten them. The worst part is that some resolvers don't even respect that detail. I guess that is why DNS is often found guilty in many outages. So this is what we call
an old school method and one we used in
production for many years, rolling deployments for auto scaling. And the basic version of that
pattern needs at least two auto scaling groups
behind the load balancer. You can then update one of
the two auto scaling groups with the new golden image V2 here, incorporating the latest
version of the software and replacing the current
instance with the new one using a rolling update. So rolling updates launched
a new instance first and once are healthy
with the load balancer, it drains the connections
with the old instances and terminates them progressively. It is therefore a safe deployment method and with no downtime. For example, app V2 is the
canary with 1/4 of the traffic. You can then slowly increase
the number of instances in that second group
and progressively reduce the number of instances in
the first auto scaling group. And this method is easy to
automate since CloudFormation supports the update policy attributes for auto scaling groups with the auto scaling
rolling update policy. AWS launched weighted target groups for application load balancer which lets you control
the traffic distribution between multiple versions
of an application. So when you create an
application load balancer, you create one or more listeners and configure listener rules to direct the traffic to one target group. A target group tells a load balancer where to direct traffic, to, for instance, EC2 instances, Lambda functions and so on. And to do canary deployment,
you can use forward actions to route request one
or more target groups. If you specify multiple target
groups for forward action, you must specify a weight
for each target group. For example, if you
specify two target groups, one with a weight of 10 and the other with the weight of 100, the target group with a weight of 100 receives 10 times more requests
as the other target group. If it requires session stickiness, you can enable target groups stickiness for a particular rule. When the application load balancer received the first request, it generates a cookie
that encodes information about the selected target group, encrypts the cookie and
includes that cookie in the response to the client so the client then
needs to add that cookie in subsequent requests to the
application load balancer. So with the, or for your
serverless applications, you have the option of
using Amazon API Gateway since it supports canary
release deployments. You can set the percentage of API requests that are handled by the new
API deployments to a stage. When canary settings
are enabled for a stage, API Gateway will generate
a new CloudWatch logs group and CloudWatch metrics
for the requests handled by the canary deployment API. You can use these metrics
to monitor the performance and the errors of the new
API and then react to them. You can then gradually
increase the percentage of request handled by
the new API deployment or roll back if errors are detected. Note that currently API
Gateway canary deployments only work for REST APIs,
not the new HTTP APIs. Finally, with AWS Lamba
alias traffic shifting, you can implement canary
deployments of Lambda functions. Simply update the version
weights on a particular alias and the traffic will be routed
to the new function versions based on the specified weight. So you can easily monitor the
health of that new version using CloudWatch metrics
for that specific alias and roll back if errors are detected. So changing aliases weight
and checking the behavior of the newly deployed functions should of course be automated. Fortunately AWS CodeDeploy can help as it can automatically
update function alias weights based on a predefined set of preferences and automatically roll back if needed. So to start using AWS Lambda
alias traffic shifting with CodeDeploy, in just
a few lines of code, you can check out the AWS SAM integration. So out of the box they give
you automatic alias creation, gradual shifting of traffic
with rollback if needed, pre-traffic and post
traffic test functions to verify if the deployment is successful and CloudWatch alarm integrations. So let's have a look at that in a demo. So let's do an AWS Lambda traffic shifting with the help of AWS CodeDeploy. And we're gonna do that
using the AWS SAM framework. So let's look at that demo. Our sample application is a
basic AWS SAM application, a simple hello world. This is template for our application. It mainly consists of
one AWS Lambda function and that Lambda function
is a hello world app. So let's open up the Lambda function code. And as you can see one basic handler which then returns a response
with a hello world message each time it's invoked. So let's try it out by simply
curling the URL for our API. And yes, it returns a
hello world message for us. So switching back to the template. So these were the properties
for our hello world function and we are setting a live
alias for our Lambda function so let's switch something in the code. Let's make a change to hello
demo instead, save that and now let's deploy this application using sam build and sam deploy. So this will then build
our serverless application and then deploy it. And as this is a demo of doing deployments using safe methods, we are using AWS CodeDeploy
to do a linear deployment, 10% of the new version every one minute. We've also set up a pre-traffic hook and the pre-traffic hook in this case, it is also an AWS Lambda
function which then allows us to test our new version
of the Lambda function. So this is also defined in our template. So once again, a simple
serverless AWS Lambda function and that function will then run to verify the output of
our new Lambda function. So it has an environment
variable with the new version of our hello world function. Let's look at the code quickly as well. This is the code for our
pre-traffic Lambda function. We using the AWS SDK to be
able to update CodeDeploy. We're starting on tests and then basically doing an
invoke of our new version of the hello world Lambda function. If there are errors, we
will then return that error. If it succeeds, we will
return that response. If there is 400 error code
on the Lambda line location, we will then say that the
validation has failed. And then basically update our CodeDeploy deployment using that. So if it fails, we will update
CodeDeploy, the deployment, or if it succeeds, we will update so the deployment can proceeded. Back to the template, besides
having that pre-traffic hook, we've also set up two alarms
for our Lambda function, alias on error metrics
and on the new version. So these are also defined
in our SAM template. So the first one is every
metrics on our alias version so the hello world function that is live. And then we have an alarm set
up for the latest version. That is the new version of
our hello world function. So it will monitor our Lambda function and if there are alarms, they will then be triggered
in AWS CloudWatch. So that's the basic setup. If we now check our deployment progress, we can see that the CodeDeploy
deployment has started. So let's switch over to AWS CodeDeploy to have a look there. Just refreshing. Alright, so we have a new
deployment in progress and this is then the new version
of our AWS Lambda function. And as we can see the
pre-deployment validation, that's our pre-traffic
hook, it has succeeded so the tests we have in our
Lambda function succeeded. And we can also see that it
has deployed the new version and started shifting traffic. So 30% of traffic has already
shifted to the new version of the Lambda function. If we check the AWS Lambda console and check our hello world function, we can see that we have
new versions deployed. Version five was the one that was live and then version six is the
new version of our application. And checking on their aliases, we can see that version six right now receives 40% of traffic and
version five 60% of traffic. So that's all updated using CodeDeploy. Alright, so let's try our function then. So once again calling the API using curl. Hello demo, the new version. Hello world, the old version. Hello world, hello world. Hello demo, hello demo. So as you can see, we're
receiving both the new and the old version when calling
the API which is intended as we're shifting traffic
towards the new version. So if the pre-deployment
validation hadn't succeeded, it would've stopped the
deployment straight away. We're also able to stop and
roll back deployment manually using the button in the
console or using the APIs or the CLI. But since we have alarms
set up in CloudWatch, we can also make use of those. So let's just try what
happens if an alarm set off. They are both in the okay state now, but we can use the CLI
to set the alarm state of our CloudWatch alarms. So let's set the alarm
state of one of these alarms into the alarm state instead
of the okay state it has now. So send that command using the AWS CLI. Let's update in CloudWatch. We can see one is now in an alarm state. Switching back to CodeDeploy, straight away we can see that
the deployment is canceled and that is since an alarm was triggered. So now AWS CodeDeploy
switches 100% of traffic back to the original function. If we check in the Lambda console, we can see that version five,
that is the old version, now receives 100% of traffic. And if we tested in the CLI using curl, we can see that we're getting hello world, hello world,
hello world so the old version. So that was a demo of using
AWS Lambda traffic shifting with AWS CodeDeploy and using AWS SAM to do
that makes it very easy. So let's talk about
security considerations and I wanna hit the nail on the head here. Mutability's one of the most critical attack vectors for cyber crimes. When a bad actor attacks a host, most of the time it will try
to modify servers in some way. For example, changing configuration files, opening network ports, replacing binaries, modifying libraries or injecting new code. So a change means the
architecture is compromised and it should be isolated
and replaced immediately. And that is really DevSecOps at its best, detect, isolate replace. So let's look at some
event-driven patterns. Extended the idea to cloud operations, the immutability paradigm lets you monitor any authorized changes
happening in the infrastructure. So event-driven automations
is an important pattern for responding to changes. Leveraging this pattern
lets your architecture react in response to events. So an event is a change
in state or an update or worse, a change in configuration. Remember our immutable pattern? So doing this on AWS clouds
means detecting changes using AWS CloudTrail and AWS Config, alerting using SNS,
remediating with AWS Lambda and replacing with AWS CloudFormation. For example, here's a simple pattern that responds to a change in
an S3 bucket configuration. And if a change event is
triggered, reverts that change and reapplies a strict configuration. in this example, setting a bucket private after it was made public. Here's another simple pattern that responds to a change in
security group configurations and if a change event is triggered, reverts that change and then reapplies a strict configuration, in this example, denying access
via SSH from any locations, the famous IP 0.0.0.0/0. And as you can see, the
event-driven pattern is an extension of the
immutability pattern and it's something that you
should put in your toolbox. So let's take a look at that demo example, how we can use event-driven
automatic remediation by leveraging the
services like AWS Config, AWS CloudTrail and AWS Lambda. My friend Adrian Hornsby
has created an example of how we can use event-driven
automatic remediation using AWS Lambda. So this is a basic CDK application so I'm just gonna walk you
through what it actually deploys. So it starts off by setting up a role and managed policy for AWS Config. Then we create the configuration
recorder for AWS Config to be able to record the event changes. Setting up an S3 bucket,
adding policies to that bucket. And we're adding the Config
bucket to our resource policy. Creating a delivery channel for Config and also setting up a CloudTrail trail. Creating a manage rule for a Config and also enabling the Config recorder. And this is the pattern that triggers if there are changes in
Config compliant rules. Setting up an EventBridge rule
based on that event pattern and also adding an AWS Lambda function. And the Lambda function
is what will then revoke the SSH access in this case. And this is a basic
Python AWS Lambda function and it will then receive
that event from EventBridge and based on the content in that event, it will then allow us
to revoke SSH access. So based on the security
group in question, we will then be able to
update the IP permissions and then basically revoke public access for that specific security group. So I have already deployed this CDK stack and these are the resources
that gets deployed. So we have everything
regarding AWS Config, we have our events rule, we
have our AWS Lambda function. So looking in the Config console, we can see that one rule is now set up. It is compliant as of now. We have a rule set up in EventBridge and that rule consists
of this event pattern so when something is noncompliant, it will then target
the AWS Lambda function and then disable SSH. So this is our target,
the Lambda function. And as we can see in the Lambda console, we also have that Lambda
function in place now, the code we looked at in VS Code before. So let's try it out. Let's then make a change to
our default security group. I'm gonna edit the inbound
rules and add a new rule. And in this case, of
course gonna select SSH. And then allow it from
anywhere and save this rule. So I have pre-baked this
example so we can now switch to Config and have a look. As you can see now, the resources in scope are now noncompliant. So this means that it would now invoke our AWS Lambda function. Let's see if it has invoked it. We can check on their monitoring. And we can see that this Lambda function should now have been invoked once. Yes, successfully. So if we check the VPC console again and check our security
group, let's refresh, the inbound rule that I added, inbound SSH from
everywhere, is now removed, meaning that our AWS Config rule should now switch back to being compliant. No resources in scope. So that was a great
example of how we can use event-driven automatic
remediation to, in this case, block access from anywhere to SSH by using AWS Config and having
an event-driven invocation of a Lambda function that
then remediates that issue. So there are plenty of benefits
to immutable architecture so I wanna walk you through some of them. So by frequently replacing
servers from a base known and version controlled configuration, the infrastructure is
reset to a known state, avoiding configuration drifts. All configuration changes
start with a verified and documented configuration
push to the code repository. For instance, a git push. Since no changes are
allowed on deployed servers, you can remove SSH access permanently. That prevents manual or
undocumented hotfixes, resulting in complicated
or hard to reproduce setups which we know often lead to downtime. And deployments are simplified because they don't need to
support upgrade scenarios so upgrades are just new deployments. Of course system upgrades
in immutable infrastructure are slightly slower since any change requires full redeploy. But the key here is pipeline automation. And deployment either
completes successfully or nothing changes. It renders the deployment process more reliable and trustworthy
with no in between states. Plus, it is a lot easier to comprehend. And deployments using
canary patterns are safer because the previous working
version isn't changed. You can roll to it if your
deployment errors are detected and roll back. And additionally, since the same process to deploy the new version is used to roll back to older versions, it makes the deployment process safer. And since all servers are
running a particular application use the same image, there are no differences between
our different environments. One build deploy to multiple environments and it prevents inconsistent environments and simplifies testing and debugging. And since servers use the same base image, they are consistent and repeatable. It makes auto scaling
trivial to implement, significantly increasing your
capacity to scale on demand. And the toolchain is simplified since you can get rid of
configuration management tools managing production software upgrades so no extra tools or agents on servers, changes are made to the base
image, tested and rolled out. And by denying all changes to
servers, you can disable SSH and remove shell access to servers. That reduces the attack
vectors for bad actors, improving your organization's security... So as I said, there
are plenty of benefits. The most important to me are safer deployment
and increased security. So if you wanna get some
additional resources on architecture and your infrastructure, check out the AWS
Well-Architected Framework, check out our AWS Architecture Center, use the AWS Well-Architected Labs and take a look at our
AWS Solutions Library where we have vetted
reference implementations and well-architected
patterns available for you. So with that, I wanna
thank you all for watching. We've looked at how
immutable infrastructures are more consistent,
reliable and predictable and they simplify many aspects
of software development and operations by preventing common issues related to mutability. If you have any questions or comments, do reach out on Twitter @gunnargrosch or connect on LinkedIn. I'm happy to connect. Thank you very much for watching. (upbeat music)

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1s) (upbeat music)

[00:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=10s) - Hi everyone and thanks
for joining this session.

[00:13](https://www.youtube.com/watch?v=n00QuaNzjiY&t=13s) Immutable infrastructure is
a model in which no updates,

[00:17](https://www.youtube.com/watch?v=n00QuaNzjiY&t=17s) security patches or configuration changes

[00:20](https://www.youtube.com/watch?v=n00QuaNzjiY&t=20s) happen in place on production systems.

[00:23](https://www.youtube.com/watch?v=n00QuaNzjiY&t=23s) If any change is needed, a new
version of the architecture

[00:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=27s) is built and deployed.

[00:29](https://www.youtube.com/watch?v=n00QuaNzjiY&t=29s) And because changes aren't allowed

[00:31](https://www.youtube.com/watch?v=n00QuaNzjiY&t=31s) in immutable infrastructure,

[00:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=33s) you can be confident
in the deployed system.

[00:36](https://www.youtube.com/watch?v=n00QuaNzjiY&t=36s) I'm Gunnar Grosch. I am a
developer advocate at AWS.

[00:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=39s) And in this session we're
gonna dive deep into the topic

[00:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=43s) to learn why immutable
infrastructure is essential

[00:46](https://www.youtube.com/watch?v=n00QuaNzjiY&t=46s) in cloud architecture.

[00:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=51s) As per the dictionary,
something that is immutable

[00:54](https://www.youtube.com/watch?v=n00QuaNzjiY&t=54s) is something that's not capable
or susceptible to change.

[00:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=59s) So why does it matter?

[01:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=61s) Before answering this question,

[01:03](https://www.youtube.com/watch?v=n00QuaNzjiY&t=63s) let's take a look at immutability
in programming languages

[01:08](https://www.youtube.com/watch?v=n00QuaNzjiY&t=68s) because the problem with mutability there,

[01:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=70s) it's probably a lot more
familiar to many of you.

[01:16](https://www.youtube.com/watch?v=n00QuaNzjiY&t=76s) So I love many different
programming languages

[01:19](https://www.youtube.com/watch?v=n00QuaNzjiY&t=79s) and Python is one of them.

[01:20](https://www.youtube.com/watch?v=n00QuaNzjiY&t=80s) But mutability in Python
can and often is a headache.

[01:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=84s) So let's simply assign variables here,

[01:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=87s) something simple and yet as
you can see in this example,

[01:31](https://www.youtube.com/watch?v=n00QuaNzjiY&t=91s) in Python if you assign a
variable to another variable

[01:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=95s) of a mutable data type,

[01:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=97s) any changes are reflected
by both variables.

[01:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=101s) So the new variable bar
is just an alias for foo.

[01:46](https://www.youtube.com/watch?v=n00QuaNzjiY&t=106s) So let's do the same in Erlang now.

[01:49](https://www.youtube.com/watch?v=n00QuaNzjiY&t=109s) Or try to do because you can't.

[01:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=112s) Languages such as Erlang, Rust, Scala,

[01:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=115s) Haskell, Clojure and a few others,

[01:58](https://www.youtube.com/watch?v=n00QuaNzjiY&t=118s) they offer immutable data structures

[02:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=121s) and single assignment
variables with the premise

[02:05](https://www.youtube.com/watch?v=n00QuaNzjiY&t=125s) that immutability leads to better code.

[02:08](https://www.youtube.com/watch?v=n00QuaNzjiY&t=128s) Simpler to understand
and easier to maintain.

[02:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=132s) And at this point,
you're probably wondering

[02:14](https://www.youtube.com/watch?v=n00QuaNzjiY&t=134s) why does immutability matter

[02:16](https://www.youtube.com/watch?v=n00QuaNzjiY&t=136s) and what does it have to
do with cloud architecture.

[02:20](https://www.youtube.com/watch?v=n00QuaNzjiY&t=140s) Well, headaches.

[02:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=141s) The immutable infrastructure paradigm

[02:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=144s) comes from the same ideas

[02:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=145s) behind immutability in
programming language.

[02:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=148s) It is the idea that your architecture

[02:31](https://www.youtube.com/watch?v=n00QuaNzjiY&t=151s) doesn't change once it is deployed

[02:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=153s) and it saves you from headaches.

[02:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=159s) So let's dive into into it

[02:40](https://www.youtube.com/watch?v=n00QuaNzjiY&t=160s) and look at traditional
infrastructure first

[02:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=163s) so we can understand the
issue with immutability here.

[02:49](https://www.youtube.com/watch?v=n00QuaNzjiY&t=169s) Not so long ago it was
quite common for folks

[02:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=172s) to brag about uptime.

[02:54](https://www.youtube.com/watch?v=n00QuaNzjiY&t=174s) The problem though is that
long periods of uptime

[02:58](https://www.youtube.com/watch?v=n00QuaNzjiY&t=178s) often indicates
potentially lethal problems

[03:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=181s) because critical updates,
either software or hardware,

[03:05](https://www.youtube.com/watch?v=n00QuaNzjiY&t=185s) often require rebooting.

[03:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=187s) So let me ask you this
very simple question.

[03:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=190s) Which of these two choices
make you more anxious?

[03:14](https://www.youtube.com/watch?v=n00QuaNzjiY&t=194s) First, rebooting a server
that's been up for 16 years

[03:18](https://www.youtube.com/watch?v=n00QuaNzjiY&t=198s) or second, rebooting a server
that's just being built?

[03:22](https://www.youtube.com/watch?v=n00QuaNzjiY&t=202s) Well, I guess we answer the same thing.

[03:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=205s) Just talking about rebooting
a 16 year old server,

[03:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=208s) it gives me anxiety because
I have no idea what's changed

[03:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=213s) in the 16 years since its initial boot up.

[03:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=217s) So how many undocumented hotfix were done?

[03:40](https://www.youtube.com/watch?v=n00QuaNzjiY&t=220s) Why was it never rebooted?

[03:42](https://www.youtube.com/watch?v=n00QuaNzjiY&t=222s) Are there some hidden
or magic dependencies?

[03:45](https://www.youtube.com/watch?v=n00QuaNzjiY&t=225s) To me, that's really terrifying.

[03:50](https://www.youtube.com/watch?v=n00QuaNzjiY&t=230s) Other common practice in
traditional infrastructure

[03:53](https://www.youtube.com/watch?v=n00QuaNzjiY&t=233s) is mutable deployments,

[03:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=235s) meaning the deployment
pipeline gets the code,

[03:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=239s) fetches the dependency,
builds the artifacts

[04:03](https://www.youtube.com/watch?v=n00QuaNzjiY&t=243s) and deploys them for
every environment stage

[04:06](https://www.youtube.com/watch?v=n00QuaNzjiY&t=246s) of the deployment pipeline.

[04:08](https://www.youtube.com/watch?v=n00QuaNzjiY&t=248s) One build per environment.

[04:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=250s) What you test and validate here

[04:13](https://www.youtube.com/watch?v=n00QuaNzjiY&t=253s) isn't what you're gonna end up deploying.

[04:18](https://www.youtube.com/watch?v=n00QuaNzjiY&t=258s) Also in traditional IT infrastructure,

[04:20](https://www.youtube.com/watch?v=n00QuaNzjiY&t=260s) servers are typically updated
and modified in place.

[04:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=264s) We SSH into our servers, we install,

[04:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=267s) we update or upgrade packages.

[04:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=270s) We tweak and we optimize
configuration files.

[04:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=273s) It goes something like this.

[04:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=275s) You log in, you stop the app,
you update the repositories,

[04:40](https://www.youtube.com/watch?v=n00QuaNzjiY&t=280s) you do a library upgrade, you test.

[04:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=284s) Sometimes you debug often
and you restart the app

[04:49](https://www.youtube.com/watch?v=n00QuaNzjiY&t=289s) and then you hope for the best.

[04:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=291s) And during that time, the
system is often down by the way.

[04:56](https://www.youtube.com/watch?v=n00QuaNzjiY&t=296s) All of these were and often
still are standard practices.

[05:00](https://www.youtube.com/watch?v=n00QuaNzjiY&t=300s) Less common practice though

[05:02](https://www.youtube.com/watch?v=n00QuaNzjiY&t=302s) is to document all of these changes.

[05:05](https://www.youtube.com/watch?v=n00QuaNzjiY&t=305s) And interestingly, the process

[05:08](https://www.youtube.com/watch?v=n00QuaNzjiY&t=308s) is like change management and ITIL.

[05:11](https://www.youtube.com/watch?v=n00QuaNzjiY&t=311s) They've been created in the industry

[05:13](https://www.youtube.com/watch?v=n00QuaNzjiY&t=313s) to try to solve the
problems due to changes,

[05:15](https://www.youtube.com/watch?v=n00QuaNzjiY&t=315s) but never addressed the
root cause of these issues

[05:19](https://www.youtube.com/watch?v=n00QuaNzjiY&t=319s) and instead they just slow things down.

[05:23](https://www.youtube.com/watch?v=n00QuaNzjiY&t=323s) So in my opinion, the solution
to mutability isn't process,

[05:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=327s) but not doing changes in the first place

[05:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=330s) and with the cloud, it's
becoming more and more easy.

[05:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=333s) And even for more advanced architecture

[05:36](https://www.youtube.com/watch?v=n00QuaNzjiY&t=336s) using multi-availability
zones, auto scaling groups,

[05:40](https://www.youtube.com/watch?v=n00QuaNzjiY&t=340s) I've seen and I guess I'm
guilty to this myself,

[05:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=344s) I'm used to SSH to fix and tune things up.

[05:48](https://www.youtube.com/watch?v=n00QuaNzjiY&t=348s) So we say just a quick
edit to the config file

[05:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=352s) to save the weekend and we promise

[05:54](https://www.youtube.com/watch?v=n00QuaNzjiY&t=354s) that we'll document and automate the fix

[05:57](https://www.youtube.com/watch?v=n00QuaNzjiY&t=357s) first thing Monday morning,
but perhaps we never do.

[06:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=361s) So I like to call this
practice SSH love syndrome.

[06:05](https://www.youtube.com/watch?v=n00QuaNzjiY&t=365s) These practices make servers mutable.

[06:08](https://www.youtube.com/watch?v=n00QuaNzjiY&t=368s) They change, author, they are created.

[06:11](https://www.youtube.com/watch?v=n00QuaNzjiY&t=371s) So besides giving you headaches,

[06:13](https://www.youtube.com/watch?v=n00QuaNzjiY&t=373s) mutations also lead to
configuration drifts

[06:16](https://www.youtube.com/watch?v=n00QuaNzjiY&t=376s) which happens when active
configurations diverge

[06:20](https://www.youtube.com/watch?v=n00QuaNzjiY&t=380s) from the initially approved
and deployed configuration.

[06:23](https://www.youtube.com/watch?v=n00QuaNzjiY&t=383s) One of the main challenges
with configuration drifts

[06:26](https://www.youtube.com/watch?v=n00QuaNzjiY&t=386s) is that they make it hard to
just replace or debug things,

[06:31](https://www.youtube.com/watch?v=n00QuaNzjiY&t=391s) making recovering from issues difficult.

[06:38](https://www.youtube.com/watch?v=n00QuaNzjiY&t=398s) So how many of your
applications fetch dependencies

[06:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=401s) from the internet during the build process

[06:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=403s) or even worse at runtime?

[06:46](https://www.youtube.com/watch?v=n00QuaNzjiY&t=406s) I've seen places where
deploying to production

[06:48](https://www.youtube.com/watch?v=n00QuaNzjiY&t=408s) meant first launching any instance.

[06:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=411s) In this sense it could be a different AMI

[06:54](https://www.youtube.com/watch?v=n00QuaNzjiY&t=414s) between different environments,

[06:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=415s) then fetching the code from
different repos, building it,

[07:00](https://www.youtube.com/watch?v=n00QuaNzjiY&t=420s) replacing the artifacts in place

[07:02](https://www.youtube.com/watch?v=n00QuaNzjiY&t=422s) and finally, rebooting the server.

[07:05](https://www.youtube.com/watch?v=n00QuaNzjiY&t=425s) One step was probably missing though

[07:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=427s) and that is the pray step.

[07:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=430s) I'm sure all of you are either smiling

[07:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=432s) or horrified by that the idea.

[07:15](https://www.youtube.com/watch?v=n00QuaNzjiY&t=435s) But how about your pip and npm install?

[07:20](https://www.youtube.com/watch?v=n00QuaNzjiY&t=440s) How about docker build?

[07:22](https://www.youtube.com/watch?v=n00QuaNzjiY&t=442s) What guarantees do you have

[07:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=444s) that the dependencies you're installing

[07:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=447s) that they don't change
between deployments?

[07:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=450s) And what if you're deploying
to multiple machines

[07:32](https://www.youtube.com/watch?v=n00QuaNzjiY&t=452s) or multiple environments?

[07:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=457s) Don't you believe that
this can be a problem?

[07:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=459s) So you can read how one
programmer broke the internet

[07:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=463s) by deleting a tiny piece
of code, a blog post.

[07:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=467s) And what happens if your code repository

[07:50](https://www.youtube.com/watch?v=n00QuaNzjiY&t=470s) has issues when you deploy

[07:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=472s) and you can't download
your code when you need it?

[07:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=475s) So installing dependencies at runtime

[07:58](https://www.youtube.com/watch?v=n00QuaNzjiY&t=478s) isn't attack vector for a
malicious code injection

[08:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=481s) and it renders auto scaling slow.

[08:05](https://www.youtube.com/watch?v=n00QuaNzjiY&t=485s) And that deployment behavior,
it's fragile at best

[08:09](https://www.youtube.com/watch?v=n00QuaNzjiY&t=489s) and it leads to deployment
mistakes and frequent rollbacks.

[08:13](https://www.youtube.com/watch?v=n00QuaNzjiY&t=493s) And that's just if you're lucky.

[08:18](https://www.youtube.com/watch?v=n00QuaNzjiY&t=498s) Luckily of course, there
is a solution to this

[08:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=501s) and put simply, immutable
infrastructure is a model

[08:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=504s) in which new updates, security patches

[08:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=507s) or configuration changes happen in place

[08:29](https://www.youtube.com/watch?v=n00QuaNzjiY&t=509s) on production systems.

[08:31](https://www.youtube.com/watch?v=n00QuaNzjiY&t=511s) If any change is needed, the
new version of the architecture

[08:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=515s) is built and deployed into production.

[08:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=521s) And this is not a new idea.

[08:42](https://www.youtube.com/watch?v=n00QuaNzjiY&t=522s) In fact, the term
immutable infrastructure,

[08:45](https://www.youtube.com/watch?v=n00QuaNzjiY&t=525s) it was coined by Chad
Fowler in this blog post,

[08:49](https://www.youtube.com/watch?v=n00QuaNzjiY&t=529s) "Trash Your Servers and Burn Your Code:

[08:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=532s) Immutable Infrastructure
and Disposable Components."

[08:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=535s) It was published in 2013.

[08:57](https://www.youtube.com/watch?v=n00QuaNzjiY&t=537s) Since then, the idea has rightfully so

[09:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=541s) gained popularity and followers,

[09:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=544s) especially as systems
have become more complex

[09:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=547s) and more distributed.

[09:11](https://www.youtube.com/watch?v=n00QuaNzjiY&t=551s) And immutable infrastructure
means that if a server

[09:14](https://www.youtube.com/watch?v=n00QuaNzjiY&t=554s) needs an update or a fix,
new servers are deployed

[09:18](https://www.youtube.com/watch?v=n00QuaNzjiY&t=558s) instead of updating the ones already used.

[09:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=561s) Once it is deployed, we simply
update the routing mechanism

[09:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=565s) to route the traffic to the
new version of the application.

[09:29](https://www.youtube.com/watch?v=n00QuaNzjiY&t=569s) So deploying applications
in immutable infrastructure

[09:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=573s) should use the canary deployment pattern.

[09:36](https://www.youtube.com/watch?v=n00QuaNzjiY&t=576s) Canary deployment is a technique

[09:38](https://www.youtube.com/watch?v=n00QuaNzjiY&t=578s) used to reduce the risk of failure

[09:40](https://www.youtube.com/watch?v=n00QuaNzjiY&t=580s) when new versions of
applications enter production

[09:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=584s) by creating a new environment

[09:46](https://www.youtube.com/watch?v=n00QuaNzjiY&t=586s) with the latest version of the software.

[09:48](https://www.youtube.com/watch?v=n00QuaNzjiY&t=588s) You then gradually roll out the change

[09:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=591s) to a small subset of users

[09:54](https://www.youtube.com/watch?v=n00QuaNzjiY&t=594s) and slowly making it
available to everybody

[09:57](https://www.youtube.com/watch?v=n00QuaNzjiY&t=597s) if no deployment errors are detected.

[09:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=599s) So canary deployment is
sometimes called a phase

[10:02](https://www.youtube.com/watch?v=n00QuaNzjiY&t=602s) or an incremental rollout.

[10:05](https://www.youtube.com/watch?v=n00QuaNzjiY&t=605s) And once the new version
is deployed to all users,

[10:08](https://www.youtube.com/watch?v=n00QuaNzjiY&t=608s) you can slowly decommission
the old version

[10:11](https://www.youtube.com/watch?v=n00QuaNzjiY&t=611s) and this strategy minimizes

[10:13](https://www.youtube.com/watch?v=n00QuaNzjiY&t=613s) the potential blast radius of failure,

[10:16](https://www.youtube.com/watch?v=n00QuaNzjiY&t=616s) limiting the impact on customers.

[10:19](https://www.youtube.com/watch?v=n00QuaNzjiY&t=619s) It is therefore a preferred version.

[10:23](https://www.youtube.com/watch?v=n00QuaNzjiY&t=623s) And the benefit of canary
deployment is of course

[10:26](https://www.youtube.com/watch?v=n00QuaNzjiY&t=626s) the near immediate rollback it gives you.

[10:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=628s) But more importantly, you
get fast and safer deployment

[10:32](https://www.youtube.com/watch?v=n00QuaNzjiY&t=632s) so it's real production test data.

[10:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=635s) The main challenge with canary deployment

[10:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=637s) is routing traffic to multiple
versions of the application.

[10:42](https://www.youtube.com/watch?v=n00QuaNzjiY&t=642s) So consider several routing
or partitioning mechanism.

[10:46](https://www.youtube.com/watch?v=n00QuaNzjiY&t=646s) Internal teams versus customers.

[10:49](https://www.youtube.com/watch?v=n00QuaNzjiY&t=649s) Paying customers versus
non-paying customers.

[10:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=652s) Your graphic-based routing
using feature flags

[10:57](https://www.youtube.com/watch?v=n00QuaNzjiY&t=657s) or perhaps even random.

[10:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=659s) And by keeping canary
traffic selection random,

[11:02](https://www.youtube.com/watch?v=n00QuaNzjiY&t=662s) most users aren't adversely
affected at any time

[11:06](https://www.youtube.com/watch?v=n00QuaNzjiY&t=666s) by potential bugs in the new version.

[11:08](https://www.youtube.com/watch?v=n00QuaNzjiY&t=668s) And no single user is adversely
affected all the time.

[11:15](https://www.youtube.com/watch?v=n00QuaNzjiY&t=675s) So how do we do canary deployments on AWS?

[11:22](https://www.youtube.com/watch?v=n00QuaNzjiY&t=682s) Route 53, a DNS service, lets you use

[11:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=685s) a weighted routing policy
to split the traffic

[11:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=688s) between the old and the new version

[11:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=690s) of the software you are deploying.

[11:32](https://www.youtube.com/watch?v=n00QuaNzjiY&t=692s) Weighted routing enables you
to associate multiple resources

[11:36](https://www.youtube.com/watch?v=n00QuaNzjiY&t=696s) with a single domain
name or a subdomain name

[11:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=699s) and choose how much traffic
is routed to each resource.

[11:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=703s) It is particularly useful
for canary deployments.

[11:49](https://www.youtube.com/watch?v=n00QuaNzjiY&t=709s) And to configure a weighted
routing for canary deployments,

[11:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=712s) you assign each record a relative weight

[11:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=715s) that corresponds with how
much traffic you wanna send

[11:58](https://www.youtube.com/watch?v=n00QuaNzjiY&t=718s) to each resource.

[12:00](https://www.youtube.com/watch?v=n00QuaNzjiY&t=720s) So Route 53 sends traffic to a resource

[12:03](https://www.youtube.com/watch?v=n00QuaNzjiY&t=723s) based on the way that
you assign to the record

[12:06](https://www.youtube.com/watch?v=n00QuaNzjiY&t=726s) as a proportion of the total
weight for all records.

[12:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=730s) So in this example, the
resource with a weight of 10

[12:14](https://www.youtube.com/watch?v=n00QuaNzjiY&t=734s) gets 10 hundredth of the traffic so 10%

[12:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=741s) and the other resource gets 90%.

[12:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=744s) If there's one inconvenience to using DNS,

[12:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=748s) it is propagation time.

[12:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=750s) So Amazon Route 53 is designed
to propagate updates you make

[12:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=755s) to your DNS records to
its worldwide network

[12:38](https://www.youtube.com/watch?v=n00QuaNzjiY&t=758s) of authoritative DNS service

[12:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=759s) within 60 seconds under normal conditions.

[12:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=763s) However, caching DNS resolvers
are outside of the control

[12:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=767s) of Amazon Route 53 service

[12:50](https://www.youtube.com/watch?v=n00QuaNzjiY&t=770s) and you will cache your
resource record sets

[12:53](https://www.youtube.com/watch?v=n00QuaNzjiY&t=773s) according to their time
to live, the TTL value.

[12:57](https://www.youtube.com/watch?v=n00QuaNzjiY&t=777s) So watch out for the default
TTL values and shorten them.

[13:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=781s) The worst part is that some resolvers

[13:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=784s) don't even respect that detail.

[13:06](https://www.youtube.com/watch?v=n00QuaNzjiY&t=786s) I guess that is why DNS

[13:08](https://www.youtube.com/watch?v=n00QuaNzjiY&t=788s) is often found guilty in many outages.

[13:14](https://www.youtube.com/watch?v=n00QuaNzjiY&t=794s) So this is what we call
an old school method

[13:17](https://www.youtube.com/watch?v=n00QuaNzjiY&t=797s) and one we used in
production for many years,

[13:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=801s) rolling deployments for auto scaling.

[13:23](https://www.youtube.com/watch?v=n00QuaNzjiY&t=803s) And the basic version of that
pattern needs at least two

[13:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=808s) auto scaling groups
behind the load balancer.

[13:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=810s) You can then update one of
the two auto scaling groups

[13:34](https://www.youtube.com/watch?v=n00QuaNzjiY&t=814s) with the new golden image V2 here,

[13:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=817s) incorporating the latest
version of the software

[13:40](https://www.youtube.com/watch?v=n00QuaNzjiY&t=820s) and replacing the current
instance with the new one

[13:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=823s) using a rolling update.

[13:45](https://www.youtube.com/watch?v=n00QuaNzjiY&t=825s) So rolling updates launched
a new instance first

[13:48](https://www.youtube.com/watch?v=n00QuaNzjiY&t=828s) and once are healthy
with the load balancer,

[13:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=831s) it drains the connections
with the old instances

[13:54](https://www.youtube.com/watch?v=n00QuaNzjiY&t=834s) and terminates them progressively.

[13:57](https://www.youtube.com/watch?v=n00QuaNzjiY&t=837s) It is therefore a safe deployment method

[13:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=839s) and with no downtime.

[14:02](https://www.youtube.com/watch?v=n00QuaNzjiY&t=842s) For example, app V2 is the
canary with 1/4 of the traffic.

[14:08](https://www.youtube.com/watch?v=n00QuaNzjiY&t=848s) You can then slowly increase
the number of instances

[14:11](https://www.youtube.com/watch?v=n00QuaNzjiY&t=851s) in that second group
and progressively reduce

[14:15](https://www.youtube.com/watch?v=n00QuaNzjiY&t=855s) the number of instances in
the first auto scaling group.

[14:19](https://www.youtube.com/watch?v=n00QuaNzjiY&t=859s) And this method is easy to
automate since CloudFormation

[14:23](https://www.youtube.com/watch?v=n00QuaNzjiY&t=863s) supports the update policy attributes

[14:26](https://www.youtube.com/watch?v=n00QuaNzjiY&t=866s) for auto scaling groups

[14:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=867s) with the auto scaling
rolling update policy.

[14:34](https://www.youtube.com/watch?v=n00QuaNzjiY&t=874s) AWS launched weighted target groups

[14:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=877s) for application load balancer

[14:38](https://www.youtube.com/watch?v=n00QuaNzjiY&t=878s) which lets you control
the traffic distribution

[14:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=881s) between multiple versions
of an application.

[14:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=884s) So when you create an
application load balancer,

[14:48](https://www.youtube.com/watch?v=n00QuaNzjiY&t=888s) you create one or more listeners

[14:50](https://www.youtube.com/watch?v=n00QuaNzjiY&t=890s) and configure listener rules

[14:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=892s) to direct the traffic to one target group.

[14:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=895s) A target group tells a load balancer

[14:58](https://www.youtube.com/watch?v=n00QuaNzjiY&t=898s) where to direct traffic, to, for instance,

[15:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=901s) EC2 instances, Lambda functions and so on.

[15:06](https://www.youtube.com/watch?v=n00QuaNzjiY&t=906s) And to do canary deployment,
you can use forward actions

[15:09](https://www.youtube.com/watch?v=n00QuaNzjiY&t=909s) to route request one
or more target groups.

[15:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=912s) If you specify multiple target
groups for forward action,

[15:15](https://www.youtube.com/watch?v=n00QuaNzjiY&t=915s) you must specify a weight
for each target group.

[15:18](https://www.youtube.com/watch?v=n00QuaNzjiY&t=918s) For example, if you
specify two target groups,

[15:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=921s) one with a weight of 10

[15:23](https://www.youtube.com/watch?v=n00QuaNzjiY&t=923s) and the other with the weight of 100,

[15:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=925s) the target group with a weight of 100

[15:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=928s) receives 10 times more requests
as the other target group.

[15:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=933s) If it requires session stickiness,

[15:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=935s) you can enable target groups stickiness

[15:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=937s) for a particular rule.

[15:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=939s) When the application load balancer

[15:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=941s) received the first request,

[15:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=943s) it generates a cookie
that encodes information

[15:46](https://www.youtube.com/watch?v=n00QuaNzjiY&t=946s) about the selected target group,

[15:48](https://www.youtube.com/watch?v=n00QuaNzjiY&t=948s) encrypts the cookie and
includes that cookie

[15:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=951s) in the response to the client

[15:53](https://www.youtube.com/watch?v=n00QuaNzjiY&t=953s) so the client then
needs to add that cookie

[15:56](https://www.youtube.com/watch?v=n00QuaNzjiY&t=956s) in subsequent requests to the
application load balancer.

[16:03](https://www.youtube.com/watch?v=n00QuaNzjiY&t=963s) So with the, or for your
serverless applications,

[16:06](https://www.youtube.com/watch?v=n00QuaNzjiY&t=966s) you have the option of
using Amazon API Gateway

[16:09](https://www.youtube.com/watch?v=n00QuaNzjiY&t=969s) since it supports canary
release deployments.

[16:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=972s) You can set the percentage of API requests

[16:15](https://www.youtube.com/watch?v=n00QuaNzjiY&t=975s) that are handled by the new
API deployments to a stage.

[16:20](https://www.youtube.com/watch?v=n00QuaNzjiY&t=980s) When canary settings
are enabled for a stage,

[16:22](https://www.youtube.com/watch?v=n00QuaNzjiY&t=982s) API Gateway will generate
a new CloudWatch logs group

[16:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=987s) and CloudWatch metrics
for the requests handled

[16:29](https://www.youtube.com/watch?v=n00QuaNzjiY&t=989s) by the canary deployment API.

[16:32](https://www.youtube.com/watch?v=n00QuaNzjiY&t=992s) You can use these metrics
to monitor the performance

[16:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=995s) and the errors of the new
API and then react to them.

[16:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=999s) You can then gradually
increase the percentage

[16:42](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1002s) of request handled by
the new API deployment

[16:45](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1005s) or roll back if errors are detected.

[16:48](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1008s) Note that currently API
Gateway canary deployments

[16:50](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1010s) only work for REST APIs,
not the new HTTP APIs.

[16:56](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1016s) Finally, with AWS Lamba
alias traffic shifting,

[17:00](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1020s) you can implement canary
deployments of Lambda functions.

[17:03](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1023s) Simply update the version
weights on a particular alias

[17:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1027s) and the traffic will be routed
to the new function versions

[17:11](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1031s) based on the specified weight.

[17:14](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1034s) So you can easily monitor the
health of that new version

[17:16](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1036s) using CloudWatch metrics
for that specific alias

[17:20](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1040s) and roll back if errors are detected.

[17:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1044s) So changing aliases weight
and checking the behavior

[17:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1047s) of the newly deployed functions

[17:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1050s) should of course be automated.

[17:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1053s) Fortunately AWS CodeDeploy can help

[17:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1055s) as it can automatically
update function alias weights

[17:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1059s) based on a predefined set of preferences

[17:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1061s) and automatically roll back if needed.

[17:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1064s) So to start using AWS Lambda
alias traffic shifting

[17:48](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1068s) with CodeDeploy, in just
a few lines of code,

[17:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1071s) you can check out the AWS SAM integration.

[17:54](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1074s) So out of the box they give
you automatic alias creation,

[17:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1079s) gradual shifting of traffic
with rollback if needed,

[18:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1084s) pre-traffic and post
traffic test functions

[18:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1087s) to verify if the deployment is successful

[18:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1090s) and CloudWatch alarm integrations.

[18:15](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1095s) So let's have a look at that in a demo.

[18:18](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1098s) So let's do an AWS Lambda traffic shifting

[18:22](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1102s) with the help of AWS CodeDeploy.

[18:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1104s) And we're gonna do that
using the AWS SAM framework.

[18:29](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1109s) So let's look at that demo.

[18:32](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1112s) Our sample application is a
basic AWS SAM application,

[18:38](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1118s) a simple hello world.

[18:40](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1120s) This is template for our application.

[18:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1123s) It mainly consists of
one AWS Lambda function

[18:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1127s) and that Lambda function
is a hello world app.

[18:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1132s) So let's open up the Lambda function code.

[18:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1135s) And as you can see one basic handler

[18:58](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1138s) which then returns a response
with a hello world message

[19:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1144s) each time it's invoked.

[19:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1147s) So let's try it out by simply
curling the URL for our API.

[19:15](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1155s) And yes, it returns a
hello world message for us.

[19:20](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1160s) So switching back to the template.

[19:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1165s) So these were the properties
for our hello world function

[19:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1170s) and we are setting a live
alias for our Lambda function

[19:36](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1176s) so let's switch something in the code.

[19:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1179s) Let's make a change to hello
demo instead, save that

[19:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1184s) and now let's deploy this application

[19:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1187s) using sam build and sam deploy.

[19:53](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1193s) So this will then build
our serverless application

[19:58](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1198s) and then deploy it.

[20:02](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1202s) And as this is a demo of doing deployments

[20:05](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1205s) using safe methods,

[20:08](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1208s) we are using AWS CodeDeploy
to do a linear deployment,

[20:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1212s) 10% of the new version every one minute.

[20:18](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1218s) We've also set up a pre-traffic hook

[20:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1221s) and the pre-traffic hook in this case,

[20:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1224s) it is also an AWS Lambda
function which then allows us

[20:29](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1229s) to test our new version
of the Lambda function.

[20:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1235s) So this is also defined in our template.

[20:38](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1238s) So once again, a simple
serverless AWS Lambda function

[20:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1244s) and that function will then run

[20:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1247s) to verify the output of
our new Lambda function.

[20:54](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1254s) So it has an environment
variable with the new version

[20:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1259s) of our hello world function.

[21:02](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1262s) Let's look at the code quickly as well.

[21:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1267s) This is the code for our
pre-traffic Lambda function.

[21:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1272s) We using the AWS SDK to be
able to update CodeDeploy.

[21:19](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1279s) We're starting on tests

[21:22](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1282s) and then basically doing an
invoke of our new version

[21:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1287s) of the hello world Lambda function.

[21:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1290s) If there are errors, we
will then return that error.

[21:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1295s) If it succeeds, we will
return that response.

[21:40](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1300s) If there is 400 error code
on the Lambda line location,

[21:45](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1305s) we will then say that the
validation has failed.

[21:50](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1310s) And then basically update

[21:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1311s) our CodeDeploy deployment using that.

[21:56](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1316s) So if it fails, we will update
CodeDeploy, the deployment,

[22:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1321s) or if it succeeds, we will update

[22:03](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1323s) so the deployment can proceeded.

[22:06](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1326s) Back to the template, besides
having that pre-traffic hook,

[22:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1332s) we've also set up two alarms
for our Lambda function,

[22:17](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1337s) alias on error metrics
and on the new version.

[22:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1344s) So these are also defined
in our SAM template.

[22:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1348s) So the first one is every
metrics on our alias version

[22:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1353s) so the hello world function that is live.

[22:38](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1358s) And then we have an alarm set
up for the latest version.

[22:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1361s) That is the new version of
our hello world function.

[22:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1367s) So it will monitor our Lambda function

[22:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1371s) and if there are alarms,

[22:53](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1373s) they will then be triggered
in AWS CloudWatch.

[22:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1379s) So that's the basic setup.

[23:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1381s) If we now check our deployment progress,

[23:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1384s) we can see that the CodeDeploy
deployment has started.

[23:08](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1388s) So let's switch over to AWS CodeDeploy

[23:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1392s) to have a look there.

[23:19](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1399s) Just refreshing.

[23:20](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1400s) Alright, so we have a new
deployment in progress

[23:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1405s) and this is then the new version
of our AWS Lambda function.

[23:31](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1411s) And as we can see the
pre-deployment validation,

[23:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1413s) that's our pre-traffic
hook, it has succeeded

[23:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1417s) so the tests we have in our
Lambda function succeeded.

[23:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1421s) And we can also see that it
has deployed the new version

[23:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1424s) and started shifting traffic.

[23:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1427s) So 30% of traffic has already
shifted to the new version

[23:50](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1430s) of the Lambda function.

[23:53](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1433s) If we check the AWS Lambda console

[23:57](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1437s) and check our hello world function,

[24:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1441s) we can see that we have
new versions deployed.

[24:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1447s) Version five was the one that was live

[24:11](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1451s) and then version six is the
new version of our application.

[24:16](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1456s) And checking on their aliases,

[24:18](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1458s) we can see that version six right now

[24:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1461s) receives 40% of traffic and
version five 60% of traffic.

[24:26](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1466s) So that's all updated using CodeDeploy.

[24:31](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1471s) Alright, so let's try our function then.

[24:34](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1474s) So once again calling the API using curl.

[24:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1481s) Hello demo, the new version.

[24:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1483s) Hello world, the old version.

[24:46](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1486s) Hello world, hello world.

[24:48](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1488s) Hello demo, hello demo.

[24:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1492s) So as you can see, we're
receiving both the new

[24:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1495s) and the old version when calling
the API which is intended

[25:00](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1500s) as we're shifting traffic
towards the new version.

[25:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1504s) So if the pre-deployment
validation hadn't succeeded,

[25:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1510s) it would've stopped the
deployment straight away.

[25:13](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1513s) We're also able to stop and
roll back deployment manually

[25:16](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1516s) using the button in the
console or using the APIs

[25:19](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1519s) or the CLI.

[25:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1521s) But since we have alarms
set up in CloudWatch,

[25:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1524s) we can also make use of those.

[25:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1527s) So let's just try what
happens if an alarm set off.

[25:32](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1532s) They are both in the okay state now,

[25:34](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1534s) but we can use the CLI
to set the alarm state

[25:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1537s) of our CloudWatch alarms.

[25:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1539s) So let's set the alarm
state of one of these alarms

[25:45](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1545s) into the alarm state instead
of the okay state it has now.

[25:50](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1550s) So send that command using the AWS CLI.

[25:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1555s) Let's update in CloudWatch.

[25:58](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1558s) We can see one is now in an alarm state.

[26:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1561s) Switching back to CodeDeploy,

[26:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1564s) straight away we can see that
the deployment is canceled

[26:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1567s) and that is since an alarm was triggered.

[26:11](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1571s) So now AWS CodeDeploy
switches 100% of traffic

[26:17](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1577s) back to the original function.

[26:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1581s) If we check in the Lambda console,

[26:23](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1583s) we can see that version five,
that is the old version,

[26:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1587s) now receives 100% of traffic.

[26:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1590s) And if we tested in the CLI using curl,

[26:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1595s) we can see that we're getting

[26:36](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1596s) hello world, hello world,
hello world so the old version.

[26:42](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1602s) So that was a demo of using
AWS Lambda traffic shifting

[26:46](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1606s) with AWS CodeDeploy

[26:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1607s) and using AWS SAM to do
that makes it very easy.

[26:53](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1613s) So let's talk about
security considerations

[26:57](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1617s) and I wanna hit the nail on the head here.

[26:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1619s) Mutability's one of the most critical

[27:02](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1622s) attack vectors for cyber crimes.

[27:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1624s) When a bad actor attacks a host,

[27:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1627s) most of the time it will try
to modify servers in some way.

[27:11](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1631s) For example, changing configuration files,

[27:14](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1634s) opening network ports, replacing binaries,

[27:17](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1637s) modifying libraries or injecting new code.

[27:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1641s) So a change means the
architecture is compromised

[27:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1644s) and it should be isolated
and replaced immediately.

[27:29](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1649s) And that is really DevSecOps at its best,

[27:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1653s) detect, isolate replace.

[27:38](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1658s) So let's look at some
event-driven patterns.

[27:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1661s) Extended the idea to cloud operations,

[27:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1664s) the immutability paradigm lets you monitor

[27:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1667s) any authorized changes
happening in the infrastructure.

[27:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1671s) So event-driven automations
is an important pattern

[27:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1675s) for responding to changes.

[27:57](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1677s) Leveraging this pattern
lets your architecture

[28:00](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1680s) react in response to events.

[28:02](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1682s) So an event is a change
in state or an update

[28:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1687s) or worse, a change in configuration.

[28:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1690s) Remember our immutable pattern?

[28:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1692s) So doing this on AWS clouds
means detecting changes

[28:17](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1697s) using AWS CloudTrail and AWS Config,

[28:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1701s) alerting using SNS,
remediating with AWS Lambda

[28:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1705s) and replacing with AWS CloudFormation.

[28:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1710s) For example, here's a simple pattern

[28:32](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1712s) that responds to a change in
an S3 bucket configuration.

[28:36](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1716s) And if a change event is
triggered, reverts that change

[28:40](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1720s) and reapplies a strict configuration.

[28:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1723s) in this example, setting a bucket private

[28:46](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1726s) after it was made public.

[28:50](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1730s) Here's another simple pattern

[28:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1732s) that responds to a change in
security group configurations

[28:56](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1736s) and if a change event is triggered,

[28:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1739s) reverts that change

[29:00](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1740s) and then reapplies a strict configuration,

[29:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1744s) in this example, denying access
via SSH from any locations,

[29:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1750s) the famous IP 0.0.0.0/0.

[29:16](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1756s) And as you can see, the
event-driven pattern

[29:19](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1759s) is an extension of the
immutability pattern

[29:22](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1762s) and it's something that you
should put in your toolbox.

[29:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1767s) So let's take a look at that demo example,

[29:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1770s) how we can use event-driven
automatic remediation

[29:34](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1774s) by leveraging the
services like AWS Config,

[29:38](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1778s) AWS CloudTrail and AWS Lambda.

[29:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1783s) My friend Adrian Hornsby
has created an example

[29:45](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1785s) of how we can use event-driven
automatic remediation

[29:49](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1789s) using AWS Lambda.

[29:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1792s) So this is a basic CDK application

[29:56](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1796s) so I'm just gonna walk you
through what it actually deploys.

[30:00](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1800s) So it starts off by setting up a role

[30:05](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1805s) and managed policy for AWS Config.

[30:11](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1811s) Then we create the configuration
recorder for AWS Config

[30:15](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1815s) to be able to record the event changes.

[30:19](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1819s) Setting up an S3 bucket,
adding policies to that bucket.

[30:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1825s) And we're adding the Config
bucket to our resource policy.

[30:31](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1831s) Creating a delivery channel for Config

[30:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1835s) and also setting up a CloudTrail trail.

[30:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1839s) Creating a manage rule for a Config

[30:43](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1843s) and also enabling the Config recorder.

[30:48](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1848s) And this is the pattern that triggers

[30:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1851s) if there are changes in
Config compliant rules.

[30:56](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1856s) Setting up an EventBridge rule
based on that event pattern

[31:03](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1863s) and also adding an AWS Lambda function.

[31:06](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1866s) And the Lambda function
is what will then revoke

[31:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1870s) the SSH access in this case.

[31:13](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1873s) And this is a basic
Python AWS Lambda function

[31:18](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1878s) and it will then receive
that event from EventBridge

[31:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1884s) and based on the content in that event,

[31:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1888s) it will then allow us
to revoke SSH access.

[31:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1893s) So based on the security
group in question,

[31:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1897s) we will then be able to
update the IP permissions

[31:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1904s) and then basically revoke public access

[31:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1907s) for that specific security group.

[31:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1911s) So I have already deployed this CDK stack

[31:54](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1914s) and these are the resources
that gets deployed.

[31:58](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1918s) So we have everything
regarding AWS Config,

[32:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1921s) we have our events rule, we
have our AWS Lambda function.

[32:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1927s) So looking in the Config console,

[32:09](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1929s) we can see that one rule is now set up.

[32:11](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1931s) It is compliant as of now.

[32:15](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1935s) We have a rule set up in EventBridge

[32:19](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1939s) and that rule consists
of this event pattern

[32:23](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1943s) so when something is noncompliant,

[32:26](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1946s) it will then target
the AWS Lambda function

[32:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1953s) and then disable SSH.

[32:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1957s) So this is our target,
the Lambda function.

[32:42](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1962s) And as we can see in the Lambda console,

[32:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1964s) we also have that Lambda
function in place now,

[32:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1967s) the code we looked at in VS Code before.

[32:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1972s) So let's try it out.

[32:53](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1973s) Let's then make a change to
our default security group.

[32:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1979s) I'm gonna edit the inbound
rules and add a new rule.

[33:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1987s) And in this case, of
course gonna select SSH.

[33:13](https://www.youtube.com/watch?v=n00QuaNzjiY&t=1993s) And then allow it from
anywhere and save this rule.

[33:23](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2003s) So I have pre-baked this
example so we can now

[33:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2007s) switch to Config and have a look.

[33:29](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2009s) As you can see now, the resources in scope

[33:33](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2013s) are now noncompliant.

[33:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2015s) So this means that it would now

[33:38](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2018s) invoke our AWS Lambda function.

[33:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2021s) Let's see if it has invoked it.

[33:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2024s) We can check on their monitoring.

[33:49](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2029s) And we can see that this Lambda function

[33:54](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2034s) should now have been invoked once.

[33:57](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2037s) Yes, successfully.

[34:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2041s) So if we check the VPC console again

[34:03](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2043s) and check our security
group, let's refresh,

[34:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2047s) the inbound rule that I added,

[34:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2050s) inbound SSH from
everywhere, is now removed,

[34:17](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2057s) meaning that our AWS Config rule

[34:22](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2062s) should now switch back to being compliant.

[34:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2065s) No resources in scope.

[34:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2068s) So that was a great
example of how we can use

[34:31](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2071s) event-driven automatic
remediation to, in this case,

[34:36](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2076s) block access from anywhere to SSH

[34:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2079s) by using AWS Config and having
an event-driven invocation

[34:45](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2085s) of a Lambda function that
then remediates that issue.

[34:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2091s) So there are plenty of benefits
to immutable architecture

[34:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2095s) so I wanna walk you through some of them.

[34:58](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2098s) So by frequently replacing
servers from a base known

[35:02](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2102s) and version controlled configuration,

[35:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2104s) the infrastructure is
reset to a known state,

[35:07](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2107s) avoiding configuration drifts.

[35:09](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2109s) All configuration changes
start with a verified

[35:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2112s) and documented configuration
push to the code repository.

[35:16](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2116s) For instance, a git push.

[35:18](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2118s) Since no changes are
allowed on deployed servers,

[35:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2121s) you can remove SSH access permanently.

[35:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2124s) That prevents manual or
undocumented hotfixes,

[35:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2128s) resulting in complicated
or hard to reproduce setups

[35:32](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2132s) which we know often lead to downtime.

[35:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2135s) And deployments are simplified

[35:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2137s) because they don't need to
support upgrade scenarios

[35:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2141s) so upgrades are just new deployments.

[35:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2144s) Of course system upgrades
in immutable infrastructure

[35:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2147s) are slightly slower since any change

[35:50](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2150s) requires full redeploy.

[35:52](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2152s) But the key here is pipeline automation.

[35:56](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2156s) And deployment either
completes successfully

[35:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2159s) or nothing changes.

[36:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2161s) It renders the deployment process

[36:03](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2163s) more reliable and trustworthy
with no in between states.

[36:06](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2166s) Plus, it is a lot easier to comprehend.

[36:10](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2170s) And deployments using
canary patterns are safer

[36:14](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2174s) because the previous working
version isn't changed.

[36:17](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2177s) You can roll to it if your
deployment errors are detected

[36:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2181s) and roll back.

[36:23](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2183s) And additionally, since the same process

[36:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2185s) to deploy the new version

[36:26](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2186s) is used to roll back to older versions,

[36:28](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2188s) it makes the deployment process safer.

[36:32](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2192s) And since all servers are
running a particular application

[36:36](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2196s) use the same image,

[36:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2197s) there are no differences between
our different environments.

[36:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2201s) One build deploy to multiple environments

[36:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2204s) and it prevents inconsistent environments

[36:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2207s) and simplifies testing and debugging.

[36:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2211s) And since servers use the same base image,

[36:53](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2213s) they are consistent and repeatable.

[36:56](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2216s) It makes auto scaling
trivial to implement,

[36:59](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2219s) significantly increasing your
capacity to scale on demand.

[37:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2224s) And the toolchain is simplified

[37:06](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2226s) since you can get rid of
configuration management tools

[37:09](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2229s) managing production software upgrades

[37:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2232s) so no extra tools or agents on servers,

[37:14](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2234s) changes are made to the base
image, tested and rolled out.

[37:20](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2240s) And by denying all changes to
servers, you can disable SSH

[37:24](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2244s) and remove shell access to servers.

[37:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2247s) That reduces the attack
vectors for bad actors,

[37:30](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2250s) improving your organization's security...

[37:34](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2254s) So as I said, there
are plenty of benefits.

[37:37](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2257s) The most important to me

[37:39](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2259s) are safer deployment
and increased security.

[37:44](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2264s) So if you wanna get some
additional resources

[37:47](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2267s) on architecture and your infrastructure,

[37:51](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2271s) check out the AWS
Well-Architected Framework,

[37:55](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2275s) check out our AWS Architecture Center,

[37:58](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2278s) use the AWS Well-Architected Labs

[38:01](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2281s) and take a look at our
AWS Solutions Library

[38:04](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2284s) where we have vetted
reference implementations

[38:06](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2286s) and well-architected
patterns available for you.

[38:12](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2292s) So with that, I wanna
thank you all for watching.

[38:15](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2295s) We've looked at how
immutable infrastructures

[38:18](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2298s) are more consistent,
reliable and predictable

[38:21](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2301s) and they simplify many aspects
of software development

[38:25](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2305s) and operations by preventing common issues

[38:27](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2307s) related to mutability.

[38:29](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2309s) If you have any questions or comments,

[38:32](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2312s) do reach out on Twitter @gunnargrosch

[38:35](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2315s) or connect on LinkedIn.

[38:36](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2316s) I'm happy to connect.

[38:38](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2318s) Thank you very much for watching.

[38:41](https://www.youtube.com/watch?v=n00QuaNzjiY&t=2321s) (upbeat music)

