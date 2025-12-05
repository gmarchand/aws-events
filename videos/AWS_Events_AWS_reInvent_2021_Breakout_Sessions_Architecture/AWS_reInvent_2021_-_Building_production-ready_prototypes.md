# AWS re:Invent 2021 - Building production-ready prototypes

[Video Link](https://www.youtube.com/watch?v=-_Zl9u9i1KI)

## Description

Did your prototype convince leadership to move forward but gloss over details like exception handling, least-privilege access, continuous delivery, and monitoring? Provisioning prototypes can involve error-prone manual actions, custom scripts, templates, and domain-specific languages. AWS CDK and AWS Solutions Constructs allow rapid development based on reusable components that implement common architecture patterns. Constructs are built on top of the AWS CDK and can be combined to implement complex architectures that follow AWS Well-Architected Framework principles. You don’t have to choose between doing it fast and doing it right—in this session, learn how to do both.

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK

Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

(upbeat music) - Hey, everybody, welcome to ARC330, and today we're gonna talk about production-ready prototyping. My name is Martin Bishop. I'm a Chief Technologist for
our UK Public Sector Business, and I'm joined today by Fabian Labat who's a Senior Solutions Architect in our Financial Services Business. We've both been with
AWS for about six years and lots of experience dealing with different kinda customers. And all customers that we
engage with have shared that they really wanna go
from idea to implementation as quickly as possible. So today we're gonna share a bit of the best practice
that we've built up over time. Before we dive in, just
go through the agenda. I'm gonna start off by setting the scene, and we're gonna come up with an idea that we wanna implement as our prototype, then we're gonna have a
look at some principles for prototyping. Fabian's gonna dive deep and we're gonna actually
go and build the prototype, then we'll talk about
some additional things that you can also do to make
your prototyping more robust. So as an organization, our fictitious company today will be an ecommerce organization. We sell products, and we've got
sort of a modern application as you'd expect with a
REST-based API in the backend and a bunch of clients in the frontend. And we were analyzing
customer satisfaction and customer behavior, and one of the specific
problems that we picked up was that certain customers
were buying a product, returning it, and then buying and very
almost equivalent product but maybe from a different manufacturer. And this really got us thinking like what could we do to
share like that knowledge that was obviously
obtained by the customer making that first purchase to
help inform other customers? So unsurprising to many of you, especially those in
the ecommerce business, we came up with this idea that we really wanna be
able to do a product review or have our customers
submit product reviews. So we basically keep it simple. We want to be able to
associate it with a product, a review that includes a
title, some text, and a rating for the given product. So now we've got our basic idea, but we're faced with this challenge, like how are we gonna do this? Do we do it right, sort of in air quotes, or are we gonna do it really fast? And this is a common dilemma. It's like, okay, obviously,
I wanna show off my work as quickly as possible and I get customer feedback
as quickly as possible, or I can spend maybe more time building a well-architected application and, you know, spending
more time designing it and et cetera. So at AWS, we really like to
challenge these constraints and try and find ways that we can be both fast
and right wherever possible. So let's have a look at some of the principles for prototyping. This is really just best
practice I built up over time in engaging with customers
and helping them move quickly. So the first of this is working backwards or work backwards, and work backwards is an
AWS or Amazon methodology that we use to determine what
products we're going to build. We ask a set of five
really specific questions, the first question being
who is your customer? The second: What is the
customer problem or opportunity? The third: What is the most
important customer benefit? And this is really key
because we wanna focus on like really delivering
that specific thing that will delight the customer rather than sort of trying to solve too many problems at once. And we also wanna challenge
ourselves and understand like how do we know
what the customer needs? And by asking this question,
like sometimes it leads us to actually go and talk to
customers, or find more data, or like test ideas with customers before we start writing
or implementing anything. And then finally, the question is like
what is the experience? What do we want the
experience to look like? So based off of this, we go on and we create
two primary artifacts, one being a press release and the other being a
frequently asked questions. And the press release
is super interesting. And when I talk to customers
about this approach, we create the press release
as if we have done the thing, as if we have created and
implemented the service that we have in mind. And that press release gives
us really interesting tool to challenge and test the idea both internally and externally. Next, at AWS, we always
say security is job zero, and so second principle is
like don't do scrappy security. I think for many organizations, having, earning customer trust is hard. Maintaining that trust and ensuring that you treat customer data in the most secure way that you can is super important. So this is definitely not an
area that we want to compromise even when we're trying to move quickly. Third principle is a bias
for action with serverless. So what do I mean by this? Bias for action is an
AWS leadership principle which is really all
about sort of recognizing that speed really matters in business. And by being able to move quickly, we could probably validate or invalidate whether we were doing the right thing and get feedback from customers sooner. But in using serverless technologies, we're also able to move quickly but without exposing ourselves
to the need to, for example, manage underlying
infrastructure or servers and make use of higher-level
services like AWS Lambda where you can just bring your code and AWS will execute it on your behalf, or AWS API Gateway and
a managed API Gateway, again, without having to
manage the underlying services, so using serverless
technologies wherever possible. The next principle is
foundation over throwaway. So, again, sometimes we start with an idea and we just wanna test it super quickly. But it can almost be
a blessing and a curse when the idea works because now if I've
built it really quickly and I've not thought about using this as a foundational capability, then I might have to spend
a lot of time reworking it, and the last thing that you want to do is have to go back to
your customers and say, "Look, that great feature
that we released to you, that we were testing, we're gonna have to turn that
off because we need to go and do a bunch of
re-engineering to scale it." So, really, you wanna build
something that's foundational and that can scale if it works rather than building something that you know you're
gonna throw away later. Then we're gonna also kind of relate it to being foundational. It's also really important to recognize that first impressions are long lasting or first impressions last. What I mean by this is as a customer, I guess some of us have
experienced this in our own lives, if you go and consume a
service for the first time and you have a really
good, positive experience, then you want to go back
and use the service again. But there's so much choice out there, the opposite is also true. If I go and try and use a
service and it doesn't work, or it has random failures, or, you know, I just don't
enjoy using the service, then I'm probably not gonna
come back any time soon. This also applies to
instrumenting and thinking about how you're going
to operate your prototype even if you're starting at small scale. You want to know when
something has gone wrong and be able to react to that from an operational perspective. And then last but definitely not least, infrastructure as code but
really everything as code. Obviously, your application logic would probably already be code, but with the CDK, your infrastructure can
also truly now be code, and even things like
the operational aspects could be captured as code. So really important to try and do as much you can in code, and Fabian's gonna show us
a bit more about that later. So just to summarize, these are the principles for prototyping. Let's say we've now
applied these principles, and we wanna now move ahead
with this idea for reviews. We've done our working backwards, we've done a press release, and we've kinda ended up with
this mockup for the service. So we will have the ability
to select the product, input the title, a description
for the review, a writing, and submit that. Once submitted, this will be submitted
up to our backend API. And let's just have a look at what the high-level architecture is that we've defined for this new service. Firstly, we've got our user. They create their review on their device, and they now need to
submit that somewhere. That is submitted up
to Amazon API Gateway. An API Gateway is a fully managed service that makes it easy for you
to create, maintain, monitor, and secure your APIs at any scale, so it's really great. Again, I can start really small and grow and scale as needed. Next up, that review
needs to be processed. So we're gonna use AWS Lambda, and we're gonna have a
bit of code in Lambda to kinda check that
this review makes sense and do whatever sort of logic is required at that first level with AWS Lambda. And finally, once we know
we've got a product review, we're gonna pass that onto Amazon SQS. And at this stage, that's enough. We wanna focus on
collecting these reviews. We'll see what we get coming in, and then we'll decide sort
of what the next stage is for this prototype. So with that, let's get building, and I'll hand over to Fabian. - Thank you, Martin. Let's now explore the
different options we have to build our prototype. For architects and developers coming from a traditional
technical background, it's very tempting to
jump first into ClickOps. By prototyping using ClickOps, we mean provisioning cloud infrastructure using the provider's web console directly and manually creating each resource. The issue is that ClickOps
is slow, error-prone, and a non-repeatable way to
build the infrastructure. I personally have started many
experiments using ClickOps and soon became frustrated
by the tedious work. I knew that you can use declarative tools like CloudFormation to build your infrastructure
as code in AWS. So to build my prototype, I started by writing in
CloudFormation YAML template. I created each of the resources
I needed for the prototype: an API Gateway, a backend Lambda
function, and an SQS queue. But soon I realized that I also needed IAM Roles, Policies,
Permissions, Methods, Deployment, an API Account, API Resources,
API Stages, and more. After all this work, in the end, I needed to create 16 resources and write over 250 lines of YAML. I was very happy with the result. However, my prototype has some issues. While you can enforce least
privilege with CloudFormation, I'll be honest, I used a star
so the prototype work quickly. And I also used fixed
names for the resources so now I need to worry
about name collisions with all the stacks and
resources in my account. There's gotta be a better way to do this. So I discover AWS Cloud
Development Kit or CDK. With AWS CDK, you define
infrastructure as code using existing languages
that we're all familiar with like Python, Java, or TypeScript. The CDK provides a higher
level of abstraction over CloudFormation
YAML and JSON templates. I like to think about
these abstraction layers similar to concepts known
by developers already, like machine code is the
lower level of software and languages are
translated to machine code so the computer can execute them. AWS APIs are what AWS uses to build resources on your behalf. In my example, assembly
would be CloudFormation, and higher-level languages
like Python or Java compared to the AWS CDK. With the CDK, you instantiate an object for each resource you want to create. For example, if I want
to create an SQS queue, in this TypeScript example, you instantiate the object using sqs.Queue and pass parameters, the stack where the
resource will be created, a name for the resource, an optional parameters for the SQS queue, like in my example the
maximum size of messages and a delivery delay of 15 seconds. But one of the best parts of
the CDK is that you can use your favorite programming
language features. We can, for example,
create multiple resources with a single loop and use the language string
replacement functions to uniquely name these resources. You can also link resources. For example, here, I create an sqs.Queue and also create an sns.Topic. And with a single line of code and the power of a method
call addSubscription, I now have the queue
subscribed to my topic. These three lines of code
created four resources, and this line alone is
responsible for 25 lines of CloudFormation YAML. But let's jump to the real demo where I'll show you the
power of the CDK in action. I start by installing the
AWS Cloud Development Kit in my system using Node
Package Manager or npm. I make a folder for my project and initialize it with
the command cdk init. I'm using TypeScript as
my language of choice. After a few seconds, the CDK created the necessary scaffolding. I also need to install the required CDK modules for my project. In my case, I need the
cdk apigateway module, the cdk lambda module, and the cdk sqs module. We'll now be working
in the TypeScript file created by the CDK under the lib folder. I import the modules we just install: apigateway, lambda, and sqs. I also need to import path to use it in the Lambda properties. Now I'm ready to instantiate my sqs.Queue just with a single line of code. I also instantiate the
backend lambda.Function. For lambda, I specify a few parameters. For the runtime, we'll choose NODEJS. The main handler function will be index.handler. I also want to specify
an environment variable. In my case, I want to have the QUEUE_URL as a variable for the Lambda to use it. I also need to tell the CDK
where my lambda call is. In my case, I will have a
folder inside lib called lambda. I also need to grant permissions
to the Lambda function so it can send messages to the queue. And lastly, we need to instantiate
the API Gateway REST API. In the Lambda REST API parameters, we specify which function is responsible for handling the requests. I'll create a folder for my Lambda code and paste the JavaScript code
required to accept requests and send the messages to SQS. Let's spend a few minutes to explain the Lambda
function we just wrote. We validate incoming
requests from API Gateway and then we send the
messages to an SQS queue. Let's take a look at the
validateMessage code. We'll return false if
the message does not have the required fields for the review. In my case, I want a review
to have a product id, a title, a text, and rating. If the validateMessage
does not return an error, then the writeQueueMessage
function executes, and the AWS SDK for
JavaScript sends a message to the SQS queue with
the request data payload. We're ready now to deploy
the application to AWS. Let's go back to the demo. If this is the first
time you're using the CDK on your AWS account and region, we need to use cdk bootstrap first. Then we execute cdk deploy. Review the changes and let the CDK create the
stack with all the resources. Every time that we run cdk deploy, the CDK will create a new
change set on CloudFormation and deploy these changes to your account. The process may take a few
minutes depending on the type and number of resources
that you're deploying. Let's take a look at the
CloudFormation console and review the resources
that were created. We should have two stacks, one called the CDK Toolkit, these are resources required with CDK, and their application stack. If we click on the Resources, we can see that we have
17 total resources, including an API, a Lambda function, and an SQS queue. That's all the additional
required resources for the application. The CDK also create an
output with API endpoint URL so we can start using it. A few keynotes. You can also use the command cdk diff to review what changes the CDK is making before you execute cdk deploy. Also, version two of the AWS CDK is designed to make writing
infrastructure as code in your preferred programming
language even easier. For a prototype, we're
using CDK version one because CDK version two is
still under developer preview. However, it's important to mention the main differences in CDK version two. In CDK version two, construct
library is a single package, so you don't need to import
each resource separately. Experimental modules are not
included in the main construct, and the CDK version two
will require bootstrapping using the modern stack on
your account and region. But once the CDK version
two is generally available, we'll update the code for the prototype. We're ready to show our final application. To test our API, I'll use
Insomnia, an API client test tool. However, you can use something
like Curl or Postman. From the subject line, I already prefill the
API Gateway endpoint URL and I show you some payload
with an example review. I press Send, and we can see
that review has been accepted. I'll remove the rating field
just to see what happens. I click Send, and we can see that
review has been rejected. Finally, let's use the AWS CLI to pull four messages in the queue. We can see the message with
our review is in the queue and ready for downstream processing. I really love the CDK. I wrote 25 lines of code
instead of 250 lines of YAML. I have least-privilege permissions that are configured for me automatically. I can share or redeploy the
stack as many times as I want. It took me minutes instead of hours, thanks to the editor code
completion and the CDK tooling. And I have infrastructure
as code that is testable. After the prototype demo, the team and management is excited. But are we ready to move
this code to production? There are still a few
issues in the current state. For example, messages in our
SQS queue are not encrypted. The API endpoint is unprotected, so anyone with a URL can post reviews. I don't like security by obscurity. And there are no mechanisms for messages that cannot
be processed in the queue. I think we can do a little
bit better than that. So let's take our current
architecture and improve upon. We can have Amazon Cognito
to protect the endpoint and only allow reviews
by authenticated users. We can also encrypt the SQS queue with KMS and have a dead-letter queue for messages that cannot
be processed successfully. For the improved version of our prototype, I'd still use a CDK, but I'll
add AWS Solutions Constructs. AWS Solutions Constructs is an open-source extension of the CDK that provides multi-service,
well-architected patterns for quickly defining solutions in code. Some example of these common patterns are an S3 bucket that
triggers a Lambda function to process new and updated objects, a Kinesis Firehose that
routes to an S3 bucket, a DynamoDB stream feeding
to a Lambda function, or SQS queue subscribed to an SNS topic. These constructs reduce the
number of objects in code that you have to manage and also create best practices by default. If we bring back the
abstraction layers example, the AWS Solutions Constructs represent a layer on top of the CDK similar to what a library or framework like React represents to JavaScript. To build our prototype, we'll
use two solutions constructs: first, the CognitoToApigatewayToLambda. This construct implements a Cognito, securing an API Gateway
Lambda back for REST API. And the second solution
construct is called LambdaToSqs. This construct implements
a Lambda function connected to an SQS queue. AWS Solution Constructs provide well-architected components. The constructs have opinionated defaults but also allow for easy customization. For example, in the LambdaToSqs construct, the Lambda configuration includes settings like keep-alive in node,
less-privilege security so only the function can
send messages to a queue, X-Ray tracing enabled by default, and an environment variable so the QUEUE_URL can be
used in the Lambda code without hard coding. And the SQS queue already includes a
dead-letter queue for us, encryption at rest with
KMS and in transit. But the real power of solutions constructs is when we combine them together. We can use the two constructs we have now, CognitoToApiGatewayToLambda
and LambdaToSqs, and tell the CDK that the
Lambda function is common to both constructs. But let me show you the actual CDK code where we define these constructs. First, we instantiate the CognitoToApiGatewayToLambda object. Then we provide properties
for the user pool, the Lambda function, and the API Gateway. Then we instantiate our second construct, the LambdaToSqs object. We now have a prototype that includes authorization,
encryption, and error-handling, and we use two solution constructs and link them together
with a single line of code. Let's jump back to our demo, and let me show the improved application we built with solution
constructs and the CDK. If we take a look at the stack created with the CDK and
the solutions constructs, now we have an API authorizer
in addition to the REST API. You can also see the Cognito user pool the construct created. And we also have a dead-letter queue for messages that fail
processing in our reviews queue. Let's go back to Insomnia
and test the new API. As suspected, we are not
authorized to post a review. Insomnia lets you configure
a Cognito user we pre-created to test authenticated calls. We add the required Authorization
header to the request, and now the review is accepted. We can go even further and
expand our architecture with more solutions constructs. We currently have the
Cognito API Lambda construct together with the Lambda SQS construct. What about if we add the
capability to process SQS messages and store the reviews in a DynamoDB table? We can add a new
construct call SqsToLambda and a new construct call LambdaToDynamoDB. Similarly, to the last two constructs, we'll share a Lambda function responsible for consuming
the messages from SQS and storing the reviews as
items into DynamoDB table. But what about if you want to have a test for dev environment and
two production environments in multiple regions like
in EMEA and America? With the CDK, we can do
this in a few lines of code. We'll tell the CDK which account
and region are associated with each environment, and then we just
instantiate our application on each of these environments. Now we can use cdk deploy and specify the stack we want to deploy. But no production-ready
prototype is complete without a dashboard and alarms. When we mean infrastructure
as code, we mean everything, including observability and monitoring. So for my prototype, I want to create a CloudWatch
dashboard for my application to show the number of API
requests I'm getting per minute, how long the Lambda function is executing for the 99 percentile, and what is the API latency for the 99 percentile of my customers? I can start by instantiating
the dashboard and the CDK the same way I'll do
with any other resource. First, we need to instantiate
the CloudWatch metrics. Here is the code where I create a new one-minute count
metric for the API Gateway. Then I can instantiate
the new dashboard widget by specifying the width, title,
and the metric to be shown. Let's now create an alarm to alert us when the P99 of our Lambda
function execution duration exceeds 500 milliseconds. We instantiate the alarm by
calling the method createAlarm in the lambdaDurationMetric. And the last thing that we want to do is to show an annotation in the widget. When we define the widget,
we can include an annotation as part of the graph widget properties. After we initialize all the
widgets in our dashboard, we just need to call the addWidget method. Here you can see the code
where I call the method once per row of widgets that I want to show. I think by now we have a
production-ready prototype. Let's take a look at
the final architecture. We have an API secured by Cognito, a Lambda that validates requests and sends reviews to an SQS
queue for downstream processing, another Lambda processes
new messages in the queue and persists the reviews
in a DynamoDB table. We also have built-in
monitoring and observability with CloudWatch and X-Ray. But the previous diagram only shows our application high-level architecture. However, I want to show
you the full picture and all the resources in our stack as our display in CloudFormation Designer. Here's where you can really appreciate how much it was able to accomplish by using infrastructure as code. By using the AWS CDK plus
AWS Solutions Constructs, my prototype is well-architected, made from four constructs and
about 100 lines of TypeScript. It includes 30 resources on multiple environments
and multiple regions. And the best part of all is that I did not have to
write 820 lines of YAML. So, Martin, back to you to
tell us what else can we do with our production-ready prototype. - That's great, Fabian. That's really, like it's
amazing to see the evolution from clicking around the console through choosing CloudFormation and ultimately CDK and constructs, and that's just incredible what you can do with really not a lot of code. So what else could we do given this foundation of using
CDK and using constructs? Like one really interesting aspect that I think is kind of a
game changer in some aspects is the ability to not
test your infrastructure while it's code and as code. So we've got a few approaches within CDK for testing your infrastructure, first being snapshots, secondly, validation, and then most exciting
to me, to be honest, is the fine-grained assertions. And with these different
test capabilities, you can even go as far as implementing test-driven development where you define the tests or the outcomes that you wanna check for
in your infrastructure and then build the CDK to see if you've met those requirements. And when you're past all your tests, you're done with your development. Obviously, you don't need to go all the way to test-driven development, so let's just have a look at some of the test
capabilities within CDK. So first off, I mentioned we've got snapshots
as a testing capability. And here you can see
there's a bit of code, and at the last line there, you can see it's synthesizing
the CloudFormation stack, and it's matching that to a snapshot. What this basically means is
we've got a reference snapshot. If we look at the next slide, we'll see we've got, the
first time I execute this, I get the window on the bottom left, and I've created the reference snapshot. And the next time I do a deployment, in this case I've changed
one parameter on the alarm, and you can see that it's really simple to see what has changed and then to take an appropriate action. So one action, for example, might be just to pause your pipeline here and have a manual approval step but with the output of
this, like you can really do kind of whatever makes
sense to your business, but really simple but powerful capability, especially if you've
got a known good state that you manage for your infrastructure. Next up is validation, and this is really basically
unit-testing your code and just treating it like any other code. It doesn't matter that
it's infrastructure code. So in this example, again,
we've got read capacity, and we want read capacity, as
you can see at the top there, to be between five and 20, and the unit test at the bottom, we're just passing in a value of three. and testing that, we
actually get an exception. So, again, by just doing this, you can test that your code is actually, your infrastructure code
is actually behaving in the way that you want it to behave. Finally, and this is probably
the most exciting bit for me, is using the fine-grained assertions. And here we've got an
assertion that you can see is like when this stack is created, I just wanna know that the output or the resulting CloudFormation
contains a DynamoDB table. I'm just using that assertion. But the assertions are really powerful, and there are a number
of different assertions that we can also, for
example, check on parameters. I can check that all
the DynamoDB's created, DynamoDB tables created within the stack have encryption turned on. So by doing this, you can
really implement tests that validate your best practices as you could do with, say, AWS Config once the infrastructure is deployed. But the beauty of this is
like these tests will run before you actually have to deploy any of your infrastructure. So in addition to using the AWS-provided Solution Constructs, you can also build your own, and this is, again, super, super powerful. As an organization, you
probably have a, you know, a set of applications or stacks
that really matter to you and that are reusable
across your business. And you've also got a set of best practice or maybe even compliance
requirements that you, ways that you require your teams to build. And by capturing and codifying these as reusable constructs
for your own organization, you can enable your teams to
build both faster and safer. So, hopefully, you've enjoyed the talk and enjoyed seeing what's
possible with the CDK. And just coming back to the principles and kinda summarizing
where we're at there, I didn't talk about
working backwards as much, but like taking the time to understand customer
requirements and diving deep there. Again, within AWS and Amazon, we actually spend a lot of time doing that before we jump in to write code because you can actually
do a lot of prototyping without having to develop
a lot of the code itself. Secondly, we weren't scrappy with security because we've used constructs
that implement best practice, like we're able to show that those best practices are included in our implementation. We've used a lot of
serverless technologies, and the beauty with that
is that the stack could run for, you know, single-figure
budget dollar values or really low dollar values per month, and it will scale as you gain traction and as you gain adoption. And then we've also got a good foundation, and we can extend this and expand on it kind of as Fabian showed
you throughout his build like really without
re-engineering a lot of things, just adding capability and
enhancing the solution. We know we can have good first impressions 'cause we've got, again, using
the serverless capabilities, we've gotta manage infrastructure and manage components that we're using, but we've also got operational
monitoring capabilities, and we can hook that into our existing operational processes. And, finally, everything
we've done and shown you today is in the code. It's all this infrastructure. The application logic and even the monitoring and
alerting configs that we can do has been done in the code. So, if you're interested in seeing more, here's a few sessions you
might wanna look into. So as mentioned, building your
own higher-order constructs, so there's a session on that, SVS319. If you're interested in understanding where you can get access to
maybe open-source constructs or how you can share
constructs that you've built, CDK is an open-source project, and we're like engaging
with the community, and the community helping each other is really super important, so check out OPN205. CDKs also got capability around continuous
deployment and pipelines. We didn't really get into that today. There's a dedicated session
for that, so DOP305. I'd really recommend checking that out both how you could use
CDK to standout pipelines and also how you can think about using CDK within your pipelines. And then finally, if you're
just interested in understanding what's new with CDK and
CloudFormation and that whole space, please check out DOP315. If you are interested in
trying out any of the code or examples that we've
used in this presentation, you can access that at the first link, and then I've got a link to just CDK, the AWS Solution Constructs. And I also wanna give a shoutout
to the AWS CDK workshop. This is a really, really good workshop. If you're just getting started with CDK, it will take you right from
bootstrapping your account for the first time right through to building
your own constructs and doing testing, like really the full gamut of
capabilities within the CDK. And if you're interested in more of the kind of the software side, the non-technical side, like how do we use working backwards, here's a link to a blog post from Werner on working backwards. So with that, I'd just like
to say thank you very much for your time and your
interest in this talk, and thanks, Fabian, for really diving deep and showing us how we
could use CDK to build, so thank you. (upbeat music)

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=0s) (upbeat music)

[00:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=11s) - Hey, everybody, welcome to ARC330,

[00:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=13s) and today we're gonna talk

[00:15](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=15s) about production-ready prototyping.

[00:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=17s) My name is Martin Bishop.

[00:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=18s) I'm a Chief Technologist for
our UK Public Sector Business,

[00:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=22s) and I'm joined today by Fabian Labat

[00:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=25s) who's a Senior Solutions Architect

[00:26](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=26s) in our Financial Services Business.

[00:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=29s) We've both been with
AWS for about six years

[00:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=31s) and lots of experience

[00:32](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=32s) dealing with different kinda customers.

[00:34](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=34s) And all customers that we
engage with have shared

[00:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=37s) that they really wanna go
from idea to implementation

[00:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=41s) as quickly as possible.

[00:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=42s) So today we're gonna share

[00:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=43s) a bit of the best practice
that we've built up over time.

[00:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=48s) Before we dive in, just
go through the agenda.

[00:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=50s) I'm gonna start off by setting the scene,

[00:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=52s) and we're gonna come up with an idea

[00:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=53s) that we wanna implement as our prototype,

[00:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=56s) then we're gonna have a
look at some principles

[00:57](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=57s) for prototyping.

[00:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=59s) Fabian's gonna dive deep

[01:00](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=60s) and we're gonna actually
go and build the prototype,

[01:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=64s) then we'll talk about
some additional things

[01:05](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=65s) that you can also do to make
your prototyping more robust.

[01:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=70s) So as an organization,

[01:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=73s) our fictitious company today

[01:15](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=75s) will be an ecommerce organization.

[01:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=78s) We sell products, and we've got
sort of a modern application

[01:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=81s) as you'd expect with a
REST-based API in the backend

[01:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=85s) and a bunch of clients in the frontend.

[01:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=88s) And we were analyzing
customer satisfaction

[01:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=91s) and customer behavior,

[01:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=93s) and one of the specific
problems that we picked up

[01:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=96s) was that certain customers
were buying a product,

[01:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=100s) returning it,

[01:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=101s) and then buying and very
almost equivalent product

[01:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=104s) but maybe from a different manufacturer.

[01:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=106s) And this really got us thinking

[01:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=108s) like what could we do to
share like that knowledge

[01:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=111s) that was obviously
obtained by the customer

[01:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=113s) making that first purchase to
help inform other customers?

[01:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=116s) So unsurprising to many of you,

[01:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=119s) especially those in
the ecommerce business,

[02:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=121s) we came up with this idea

[02:02](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=122s) that we really wanna be
able to do a product review

[02:05](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=125s) or have our customers
submit product reviews.

[02:09](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=129s) So we basically keep it simple.

[02:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=132s) We want to be able to
associate it with a product,

[02:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=134s) a review that includes a
title, some text, and a rating

[02:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=138s) for the given product.

[02:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=140s) So now we've got our basic idea,

[02:24](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=144s) but we're faced with this challenge,

[02:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=145s) like how are we gonna do this?

[02:26](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=146s) Do we do it right, sort of in air quotes,

[02:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=150s) or are we gonna do it really fast?

[02:32](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=152s) And this is a common dilemma.

[02:34](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=154s) It's like, okay, obviously,
I wanna show off my work

[02:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=157s) as quickly as possible

[02:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=158s) and I get customer feedback
as quickly as possible,

[02:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=161s) or I can spend maybe more time

[02:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=164s) building a well-architected application

[02:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=166s) and, you know, spending
more time designing it

[02:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=169s) and et cetera.

[02:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=171s) So at AWS, we really like to
challenge these constraints

[02:55](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=175s) and try and find ways

[02:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=176s) that we can be both fast
and right wherever possible.

[03:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=181s) So let's have a look

[03:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=181s) at some of the principles for prototyping.

[03:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=184s) This is really just best
practice I built up over time

[03:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=188s) in engaging with customers
and helping them move quickly.

[03:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=191s) So the first of this is working backwards

[03:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=194s) or work backwards,

[03:16](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=196s) and work backwards is an
AWS or Amazon methodology

[03:19](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=199s) that we use to determine what
products we're going to build.

[03:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=203s) We ask a set of five
really specific questions,

[03:26](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=206s) the first question being
who is your customer?

[03:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=209s) The second: What is the
customer problem or opportunity?

[03:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=213s) The third: What is the most
important customer benefit?

[03:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=216s) And this is really key
because we wanna focus

[03:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=218s) on like really delivering
that specific thing

[03:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=221s) that will delight the customer

[03:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=223s) rather than sort of trying

[03:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=224s) to solve too many problems at once.

[03:47](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=227s) And we also wanna challenge
ourselves and understand

[03:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=229s) like how do we know
what the customer needs?

[03:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=232s) And by asking this question,
like sometimes it leads us

[03:55](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=235s) to actually go and talk to
customers, or find more data,

[03:57](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=237s) or like test ideas with customers

[04:00](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=240s) before we start writing
or implementing anything.

[04:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=244s) And then finally,

[04:05](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=245s) the question is like
what is the experience?

[04:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=247s) What do we want the
experience to look like?

[04:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=250s) So based off of this,

[04:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=251s) we go on and we create
two primary artifacts,

[04:16](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=256s) one being a press release

[04:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=257s) and the other being a
frequently asked questions.

[04:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=260s) And the press release
is super interesting.

[04:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=262s) And when I talk to customers
about this approach,

[04:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=265s) we create the press release
as if we have done the thing,

[04:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=268s) as if we have created and
implemented the service

[04:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=271s) that we have in mind.

[04:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=273s) And that press release gives
us really interesting tool

[04:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=275s) to challenge and test the idea

[04:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=277s) both internally and externally.

[04:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=280s) Next, at AWS, we always
say security is job zero,

[04:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=284s) and so second principle is
like don't do scrappy security.

[04:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=289s) I think for many organizations,

[04:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=290s) having, earning customer trust is hard.

[04:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=293s) Maintaining that trust

[04:55](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=295s) and ensuring that you treat customer data

[04:57](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=297s) in the most secure way that you can

[05:00](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=300s) is super important.

[05:02](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=302s) So this is definitely not an
area that we want to compromise

[05:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=304s) even when we're trying to move quickly.

[05:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=308s) Third principle is a bias
for action with serverless.

[05:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=312s) So what do I mean by this?

[05:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=314s) Bias for action is an
AWS leadership principle

[05:16](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=316s) which is really all
about sort of recognizing

[05:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=318s) that speed really matters in business.

[05:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=321s) And by being able to move quickly,

[05:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=323s) we could probably validate or invalidate

[05:26](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=326s) whether we were doing the right thing

[05:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=329s) and get feedback from customers sooner.

[05:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=333s) But in using serverless technologies,

[05:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=336s) we're also able to move quickly

[05:39](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=339s) but without exposing ourselves
to the need to, for example,

[05:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=343s) manage underlying
infrastructure or servers

[05:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=346s) and make use of higher-level
services like AWS Lambda

[05:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=351s) where you can just bring your code

[05:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=352s) and AWS will execute it on your behalf,

[05:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=354s) or AWS API Gateway and
a managed API Gateway,

[05:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=359s) again, without having to
manage the underlying services,

[06:02](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=362s) so using serverless
technologies wherever possible.

[06:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=367s) The next principle is
foundation over throwaway.

[06:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=371s) So, again, sometimes we start with an idea

[06:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=374s) and we just wanna test it super quickly.

[06:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=377s) But it can almost be
a blessing and a curse

[06:19](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=379s) when the idea works

[06:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=381s) because now if I've
built it really quickly

[06:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=383s) and I've not thought about using this

[06:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=385s) as a foundational capability,

[06:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=388s) then I might have to spend
a lot of time reworking it,

[06:32](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=392s) and the last thing that you want to do

[06:34](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=394s) is have to go back to
your customers and say,

[06:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=396s) "Look, that great feature
that we released to you,

[06:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=398s) that we were testing,

[06:39](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=399s) we're gonna have to turn that
off because we need to go

[06:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=402s) and do a bunch of
re-engineering to scale it."

[06:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=404s) So, really, you wanna build
something that's foundational

[06:47](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=407s) and that can scale if it works

[06:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=410s) rather than building something

[06:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=411s) that you know you're
gonna throw away later.

[06:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=416s) Then we're gonna also kind of relate it

[06:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=419s) to being foundational.

[07:00](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=420s) It's also really important to recognize

[07:02](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=422s) that first impressions are long lasting

[07:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=424s) or first impressions last.

[07:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=426s) What I mean by this is as a customer,

[07:09](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=429s) I guess some of us have
experienced this in our own lives,

[07:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=433s) if you go and consume a
service for the first time

[07:15](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=435s) and you have a really
good, positive experience,

[07:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=437s) then you want to go back
and use the service again.

[07:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=440s) But there's so much choice out there,

[07:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=442s) the opposite is also true.

[07:24](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=444s) If I go and try and use a
service and it doesn't work,

[07:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=447s) or it has random failures,

[07:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=449s) or, you know, I just don't
enjoy using the service,

[07:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=453s) then I'm probably not gonna
come back any time soon.

[07:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=457s) This also applies to
instrumenting and thinking

[07:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=460s) about how you're going
to operate your prototype

[07:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=462s) even if you're starting at small scale.

[07:45](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=465s) You want to know when
something has gone wrong

[07:47](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=467s) and be able to react to that

[07:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=469s) from an operational perspective.

[07:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=472s) And then last but definitely not least,

[07:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=474s) infrastructure as code but
really everything as code.

[07:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=478s) Obviously, your application logic

[07:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=479s) would probably already be code,

[08:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=481s) but with the CDK,

[08:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=484s) your infrastructure can
also truly now be code,

[08:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=487s) and even things like
the operational aspects

[08:09](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=489s) could be captured as code.

[08:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=491s) So really important

[08:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=492s) to try and do as much you can in code,

[08:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=494s) and Fabian's gonna show us
a bit more about that later.

[08:19](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=499s) So just to summarize,

[08:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=500s) these are the principles for prototyping.

[08:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=503s) Let's say we've now
applied these principles,

[08:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=505s) and we wanna now move ahead
with this idea for reviews.

[08:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=509s) We've done our working backwards,

[08:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=511s) we've done a press release,

[08:32](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=512s) and we've kinda ended up with
this mockup for the service.

[08:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=515s) So we will have the ability
to select the product,

[08:39](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=519s) input the title, a description
for the review, a writing,

[08:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=522s) and submit that.

[08:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=524s) Once submitted,

[08:45](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=525s) this will be submitted
up to our backend API.

[08:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=530s) And let's just have a look

[08:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=531s) at what the high-level architecture is

[08:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=533s) that we've defined for this new service.

[08:55](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=535s) Firstly, we've got our user.

[08:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=538s) They create their review on their device,

[09:00](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=540s) and they now need to
submit that somewhere.

[09:02](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=542s) That is submitted up
to Amazon API Gateway.

[09:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=546s) An API Gateway is a fully managed service

[09:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=548s) that makes it easy for you
to create, maintain, monitor,

[09:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=551s) and secure your APIs at any scale,

[09:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=554s) so it's really great.

[09:15](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=555s) Again, I can start really small

[09:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=557s) and grow and scale as needed.

[09:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=560s) Next up, that review
needs to be processed.

[09:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=562s) So we're gonna use AWS Lambda,

[09:24](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=564s) and we're gonna have a
bit of code in Lambda

[09:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=567s) to kinda check that
this review makes sense

[09:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=570s) and do whatever sort of logic is required

[09:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=573s) at that first level with AWS Lambda.

[09:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=576s) And finally, once we know
we've got a product review,

[09:39](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=579s) we're gonna pass that onto Amazon SQS.

[09:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=582s) And at this stage, that's enough.

[09:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=584s) We wanna focus on
collecting these reviews.

[09:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=586s) We'll see what we get coming in,

[09:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=588s) and then we'll decide sort
of what the next stage is

[09:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=591s) for this prototype.

[09:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=594s) So with that, let's get building,

[09:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=596s) and I'll hand over to Fabian.

[09:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=598s) - Thank you, Martin.

[09:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=599s) Let's now explore the
different options we have

[10:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=601s) to build our prototype.

[10:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=604s) For architects and developers

[10:05](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=605s) coming from a traditional
technical background,

[10:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=607s) it's very tempting to
jump first into ClickOps.

[10:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=611s) By prototyping using ClickOps,

[10:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=613s) we mean provisioning cloud infrastructure

[10:15](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=615s) using the provider's web console directly

[10:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=618s) and manually creating each resource.

[10:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=621s) The issue is that ClickOps
is slow, error-prone,

[10:24](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=624s) and a non-repeatable way to
build the infrastructure.

[10:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=627s) I personally have started many
experiments using ClickOps

[10:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=630s) and soon became frustrated
by the tedious work.

[10:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=635s) I knew that you can use declarative tools

[10:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=636s) like CloudFormation

[10:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=638s) to build your infrastructure
as code in AWS.

[10:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=642s) So to build my prototype,

[10:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=643s) I started by writing in
CloudFormation YAML template.

[10:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=646s) I created each of the resources
I needed for the prototype:

[10:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=649s) an API Gateway, a backend Lambda
function, and an SQS queue.

[10:55](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=655s) But soon I realized that I also needed

[10:57](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=657s) IAM Roles, Policies,
Permissions, Methods, Deployment,

[11:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=661s) an API Account, API Resources,
API Stages, and more.

[11:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=666s) After all this work, in the end,

[11:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=668s) I needed to create 16 resources

[11:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=671s) and write over 250 lines of YAML.

[11:15](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=675s) I was very happy with the result.

[11:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=677s) However, my prototype has some issues.

[11:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=681s) While you can enforce least
privilege with CloudFormation,

[11:24](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=684s) I'll be honest, I used a star
so the prototype work quickly.

[11:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=688s) And I also used fixed
names for the resources

[11:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=691s) so now I need to worry
about name collisions

[11:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=693s) with all the stacks and
resources in my account.

[11:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=697s) There's gotta be a better way to do this.

[11:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=700s) So I discover AWS Cloud
Development Kit or CDK.

[11:45](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=705s) With AWS CDK, you define
infrastructure as code

[11:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=708s) using existing languages
that we're all familiar with

[11:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=711s) like Python, Java, or TypeScript.

[11:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=714s) The CDK provides a higher
level of abstraction

[11:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=716s) over CloudFormation
YAML and JSON templates.

[12:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=721s) I like to think about
these abstraction layers

[12:03](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=723s) similar to concepts known
by developers already,

[12:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=726s) like machine code is the
lower level of software

[12:09](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=729s) and languages are
translated to machine code

[12:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=731s) so the computer can execute them.

[12:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=733s) AWS APIs are what AWS uses

[12:16](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=736s) to build resources on your behalf.

[12:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=738s) In my example, assembly
would be CloudFormation,

[12:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=741s) and higher-level languages
like Python or Java

[12:24](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=744s) compared to the AWS CDK.

[12:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=748s) With the CDK, you instantiate an object

[12:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=751s) for each resource you want to create.

[12:34](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=754s) For example, if I want
to create an SQS queue,

[12:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=758s) in this TypeScript example,

[12:39](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=759s) you instantiate the object using sqs.Queue

[12:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=764s) and pass parameters,

[12:45](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=765s) the stack where the
resource will be created,

[12:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=768s) a name for the resource,

[12:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=770s) an optional parameters for the SQS queue,

[12:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=773s) like in my example the
maximum size of messages

[12:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=776s) and a delivery delay of 15 seconds.

[13:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=781s) But one of the best parts of
the CDK is that you can use

[13:03](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=783s) your favorite programming
language features.

[13:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=786s) We can, for example,
create multiple resources

[13:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=788s) with a single loop

[13:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=790s) and use the language string
replacement functions

[13:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=792s) to uniquely name these resources.

[13:16](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=796s) You can also link resources.

[13:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=798s) For example, here, I create an sqs.Queue

[13:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=802s) and also create an sns.Topic.

[13:24](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=804s) And with a single line of code

[13:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=805s) and the power of a method
call addSubscription,

[13:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=808s) I now have the queue
subscribed to my topic.

[13:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=811s) These three lines of code
created four resources,

[13:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=815s) and this line alone is
responsible for 25 lines

[13:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=818s) of CloudFormation YAML.

[13:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=821s) But let's jump to the real demo

[13:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=822s) where I'll show you the
power of the CDK in action.

[13:47](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=827s) I start by installing the
AWS Cloud Development Kit

[13:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=830s) in my system using Node
Package Manager or npm.

[13:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=839s) I make a folder for my project

[14:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=847s) and initialize it with
the command cdk init.

[14:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=852s) I'm using TypeScript as
my language of choice.

[14:19](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=859s) After a few seconds,

[14:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=860s) the CDK created the necessary scaffolding.

[14:26](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=866s) I also need to install

[14:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=867s) the required CDK modules for my project.

[14:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=870s) In my case, I need the
cdk apigateway module,

[14:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=877s) the cdk lambda module,

[14:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=883s) and the cdk sqs module.

[14:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=890s) We'll now be working
in the TypeScript file

[14:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=892s) created by the CDK under the lib folder.

[14:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=896s) I import the modules we just install:

[14:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=898s) apigateway, lambda, and sqs.

[15:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=907s) I also need to import path

[15:09](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=909s) to use it in the Lambda properties.

[15:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=918s) Now I'm ready to instantiate my sqs.Queue

[15:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=921s) just with a single line of code.

[15:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=929s) I also instantiate the
backend lambda.Function.

[15:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=935s) For lambda, I specify a few parameters.

[15:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=938s) For the runtime, we'll choose NODEJS.

[15:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=943s) The main handler function

[15:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=946s) will be index.handler.

[15:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=954s) I also want to specify
an environment variable.

[15:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=958s) In my case, I want to have the QUEUE_URL

[16:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=961s) as a variable for the Lambda to use it.

[16:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=970s) I also need to tell the CDK
where my lambda call is.

[16:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=974s) In my case, I will have a
folder inside lib called lambda.

[16:24](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=984s) I also need to grant permissions
to the Lambda function

[16:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=987s) so it can send messages to the queue.

[16:34](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=994s) And lastly, we need to instantiate
the API Gateway REST API.

[16:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1001s) In the Lambda REST API parameters,

[16:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1003s) we specify which function is responsible

[16:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1006s) for handling the requests.

[16:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1011s) I'll create a folder for my Lambda code

[16:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1016s) and paste the JavaScript code
required to accept requests

[16:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1019s) and send the messages to SQS.

[17:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1027s) Let's spend a few minutes

[17:09](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1029s) to explain the Lambda
function we just wrote.

[17:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1032s) We validate incoming
requests from API Gateway

[17:16](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1036s) and then we send the
messages to an SQS queue.

[17:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1040s) Let's take a look at the
validateMessage code.

[17:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1043s) We'll return false if
the message does not have

[17:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1045s) the required fields for the review.

[17:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1047s) In my case, I want a review
to have a product id,

[17:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1050s) a title, a text, and rating.

[17:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1053s) If the validateMessage
does not return an error,

[17:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1056s) then the writeQueueMessage
function executes,

[17:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1060s) and the AWS SDK for
JavaScript sends a message

[17:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1063s) to the SQS queue with
the request data payload.

[17:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1068s) We're ready now to deploy
the application to AWS.

[17:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1072s) Let's go back to the demo.

[17:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1074s) If this is the first
time you're using the CDK

[17:57](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1077s) on your AWS account and region,

[17:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1079s) we need to use cdk bootstrap first.

[18:05](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1085s) Then we execute cdk deploy.

[18:09](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1089s) Review the changes

[18:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1090s) and let the CDK create the
stack with all the resources.

[18:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1097s) Every time that we run cdk deploy,

[18:19](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1099s) the CDK will create a new
change set on CloudFormation

[18:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1103s) and deploy these changes to your account.

[18:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1107s) The process may take a few
minutes depending on the type

[18:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1111s) and number of resources
that you're deploying.

[18:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1115s) Let's take a look at the
CloudFormation console

[18:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1117s) and review the resources
that were created.

[18:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1121s) We should have two stacks,

[18:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1124s) one called the CDK Toolkit,

[18:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1126s) these are resources required with CDK,

[18:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1129s) and their application stack.

[18:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1132s) If we click on the Resources,

[18:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1133s) we can see that we have
17 total resources,

[18:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1138s) including an API,

[19:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1141s) a Lambda function, and an SQS queue.

[19:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1144s) That's all the additional
required resources

[19:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1146s) for the application.

[19:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1148s) The CDK also create an
output with API endpoint URL

[19:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1152s) so we can start using it.

[19:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1154s) A few keynotes.

[19:16](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1156s) You can also use the command cdk diff

[19:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1158s) to review what changes the CDK is making

[19:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1161s) before you execute cdk deploy.

[19:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1165s) Also, version two of the AWS CDK

[19:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1167s) is designed to make writing
infrastructure as code

[19:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1170s) in your preferred programming
language even easier.

[19:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1173s) For a prototype, we're
using CDK version one

[19:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1176s) because CDK version two is
still under developer preview.

[19:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1180s) However, it's important to mention

[19:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1182s) the main differences in CDK version two.

[19:45](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1185s) In CDK version two, construct
library is a single package,

[19:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1188s) so you don't need to import
each resource separately.

[19:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1191s) Experimental modules are not
included in the main construct,

[19:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1194s) and the CDK version two
will require bootstrapping

[19:57](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1197s) using the modern stack on
your account and region.

[20:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1201s) But once the CDK version
two is generally available,

[20:03](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1203s) we'll update the code for the prototype.

[20:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1207s) We're ready to show our final application.

[20:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1210s) To test our API, I'll use
Insomnia, an API client test tool.

[20:16](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1216s) However, you can use something
like Curl or Postman.

[20:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1220s) From the subject line,

[20:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1221s) I already prefill the
API Gateway endpoint URL

[20:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1225s) and I show you some payload
with an example review.

[20:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1228s) I press Send, and we can see
that review has been accepted.

[20:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1233s) I'll remove the rating field
just to see what happens.

[20:39](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1239s) I click Send,

[20:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1241s) and we can see that
review has been rejected.

[20:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1246s) Finally, let's use the AWS CLI

[20:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1249s) to pull four messages in the queue.

[20:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1252s) We can see the message with
our review is in the queue

[20:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1256s) and ready for downstream processing.

[21:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1261s) I really love the CDK.

[21:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1264s) I wrote 25 lines of code
instead of 250 lines of YAML.

[21:09](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1269s) I have least-privilege permissions

[21:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1270s) that are configured for me automatically.

[21:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1273s) I can share or redeploy the
stack as many times as I want.

[21:16](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1276s) It took me minutes instead of hours,

[21:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1278s) thanks to the editor code
completion and the CDK tooling.

[21:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1282s) And I have infrastructure
as code that is testable.

[21:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1287s) After the prototype demo,

[21:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1289s) the team and management is excited.

[21:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1291s) But are we ready to move
this code to production?

[21:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1296s) There are still a few
issues in the current state.

[21:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1298s) For example, messages in our
SQS queue are not encrypted.

[21:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1303s) The API endpoint is unprotected,

[21:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1306s) so anyone with a URL can post reviews.

[21:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1308s) I don't like security by obscurity.

[21:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1311s) And there are no mechanisms

[21:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1312s) for messages that cannot
be processed in the queue.

[21:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1316s) I think we can do a little
bit better than that.

[21:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1319s) So let's take our current
architecture and improve upon.

[22:03](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1323s) We can have Amazon Cognito
to protect the endpoint

[22:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1326s) and only allow reviews
by authenticated users.

[22:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1330s) We can also encrypt the SQS queue with KMS

[22:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1333s) and have a dead-letter queue

[22:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1334s) for messages that cannot
be processed successfully.

[22:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1340s) For the improved version of our prototype,

[22:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1342s) I'd still use a CDK, but I'll
add AWS Solutions Constructs.

[22:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1348s) AWS Solutions Constructs

[22:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1350s) is an open-source extension of the CDK

[22:32](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1352s) that provides multi-service,
well-architected patterns

[22:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1356s) for quickly defining solutions in code.

[22:39](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1359s) Some example of these common patterns

[22:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1361s) are an S3 bucket that
triggers a Lambda function

[22:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1364s) to process new and updated objects,

[22:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1366s) a Kinesis Firehose that
routes to an S3 bucket,

[22:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1369s) a DynamoDB stream feeding
to a Lambda function,

[22:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1373s) or SQS queue subscribed to an SNS topic.

[22:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1376s) These constructs reduce the
number of objects in code

[22:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1379s) that you have to manage

[23:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1381s) and also create best practices by default.

[23:05](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1385s) If we bring back the
abstraction layers example,

[23:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1388s) the AWS Solutions Constructs

[23:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1390s) represent a layer on top of the CDK

[23:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1392s) similar to what a library or framework

[23:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1394s) like React represents to JavaScript.

[23:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1398s) To build our prototype, we'll
use two solutions constructs:

[23:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1403s) first, the CognitoToApigatewayToLambda.

[23:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1407s) This construct implements a Cognito,

[23:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1409s) securing an API Gateway
Lambda back for REST API.

[23:34](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1414s) And the second solution
construct is called LambdaToSqs.

[23:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1418s) This construct implements
a Lambda function

[23:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1420s) connected to an SQS queue.

[23:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1423s) AWS Solution Constructs

[23:45](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1425s) provide well-architected components.

[23:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1428s) The constructs have opinionated defaults

[23:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1430s) but also allow for easy customization.

[23:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1433s) For example, in the LambdaToSqs construct,

[23:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1436s) the Lambda configuration includes settings

[23:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1438s) like keep-alive in node,
less-privilege security

[24:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1441s) so only the function can
send messages to a queue,

[24:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1444s) X-Ray tracing enabled by default,

[24:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1447s) and an environment variable

[24:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1448s) so the QUEUE_URL can be
used in the Lambda code

[24:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1451s) without hard coding.

[24:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1453s) And the SQS queue

[24:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1454s) already includes a
dead-letter queue for us,

[24:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1457s) encryption at rest with
KMS and in transit.

[24:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1462s) But the real power of solutions constructs

[24:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1465s) is when we combine them together.

[24:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1468s) We can use the two constructs we have now,

[24:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1470s) CognitoToApiGatewayToLambda
and LambdaToSqs,

[24:34](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1474s) and tell the CDK that the
Lambda function is common

[24:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1477s) to both constructs.

[24:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1480s) But let me show you the actual CDK code

[24:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1483s) where we define these constructs.

[24:45](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1485s) First, we instantiate

[24:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1486s) the CognitoToApiGatewayToLambda object.

[24:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1490s) Then we provide properties
for the user pool,

[24:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1494s) the Lambda function, and the API Gateway.

[24:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1498s) Then we instantiate our second construct,

[25:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1501s) the LambdaToSqs object.

[25:05](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1505s) We now have a prototype

[25:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1507s) that includes authorization,
encryption, and error-handling,

[25:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1512s) and we use two solution constructs

[25:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1514s) and link them together
with a single line of code.

[25:19](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1519s) Let's jump back to our demo,

[25:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1521s) and let me show the improved application

[25:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1523s) we built with solution
constructs and the CDK.

[25:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1527s) If we take a look at the stack

[25:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1528s) created with the CDK and
the solutions constructs,

[25:32](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1532s) now we have an API authorizer
in addition to the REST API.

[25:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1537s) You can also see the Cognito user pool

[25:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1541s) the construct created.

[25:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1542s) And we also have a dead-letter queue

[25:45](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1545s) for messages that fail
processing in our reviews queue.

[25:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1549s) Let's go back to Insomnia
and test the new API.

[25:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1553s) As suspected, we are not
authorized to post a review.

[26:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1561s) Insomnia lets you configure
a Cognito user we pre-created

[26:05](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1565s) to test authenticated calls.

[26:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1568s) We add the required Authorization
header to the request,

[26:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1577s) and now the review is accepted.

[26:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1585s) We can go even further and
expand our architecture

[26:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1588s) with more solutions constructs.

[26:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1591s) We currently have the
Cognito API Lambda construct

[26:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1595s) together with the Lambda SQS construct.

[26:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1597s) What about if we add the
capability to process SQS messages

[26:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1601s) and store the reviews in a DynamoDB table?

[26:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1604s) We can add a new
construct call SqsToLambda

[26:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1608s) and a new construct call LambdaToDynamoDB.

[26:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1611s) Similarly, to the last two constructs,

[26:55](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1615s) we'll share a Lambda function

[26:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1616s) responsible for consuming
the messages from SQS

[26:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1619s) and storing the reviews as
items into DynamoDB table.

[27:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1626s) But what about if you want to have a test

[27:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1627s) for dev environment and
two production environments

[27:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1630s) in multiple regions like
in EMEA and America?

[27:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1634s) With the CDK, we can do
this in a few lines of code.

[27:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1638s) We'll tell the CDK which account
and region are associated

[27:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1641s) with each environment,

[27:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1642s) and then we just
instantiate our application

[27:24](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1644s) on each of these environments.

[27:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1647s) Now we can use cdk deploy

[27:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1649s) and specify the stack we want to deploy.

[27:34](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1654s) But no production-ready
prototype is complete

[27:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1656s) without a dashboard and alarms.

[27:39](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1659s) When we mean infrastructure
as code, we mean everything,

[27:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1663s) including observability and monitoring.

[27:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1668s) So for my prototype,

[27:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1669s) I want to create a CloudWatch
dashboard for my application

[27:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1672s) to show the number of API
requests I'm getting per minute,

[27:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1676s) how long the Lambda function is executing

[27:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1678s) for the 99 percentile,

[28:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1681s) and what is the API latency

[28:02](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1682s) for the 99 percentile of my customers?

[28:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1686s) I can start by instantiating
the dashboard and the CDK

[28:09](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1689s) the same way I'll do
with any other resource.

[28:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1693s) First, we need to instantiate
the CloudWatch metrics.

[28:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1697s) Here is the code where I create

[28:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1698s) a new one-minute count
metric for the API Gateway.

[28:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1702s) Then I can instantiate
the new dashboard widget

[28:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1705s) by specifying the width, title,
and the metric to be shown.

[28:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1711s) Let's now create an alarm to alert us

[28:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1713s) when the P99 of our Lambda
function execution duration

[28:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1717s) exceeds 500 milliseconds.

[28:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1720s) We instantiate the alarm by
calling the method createAlarm

[28:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1723s) in the lambdaDurationMetric.

[28:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1726s) And the last thing that we want to do

[28:48](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1728s) is to show an annotation in the widget.

[28:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1731s) When we define the widget,
we can include an annotation

[28:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1734s) as part of the graph widget properties.

[28:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1738s) After we initialize all the
widgets in our dashboard,

[29:00](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1740s) we just need to call the addWidget method.

[29:03](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1743s) Here you can see the code
where I call the method once

[29:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1746s) per row of widgets that I want to show.

[29:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1750s) I think by now we have a
production-ready prototype.

[29:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1753s) Let's take a look at
the final architecture.

[29:16](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1756s) We have an API secured by Cognito,

[29:19](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1759s) a Lambda that validates requests

[29:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1760s) and sends reviews to an SQS
queue for downstream processing,

[29:24](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1764s) another Lambda processes
new messages in the queue

[29:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1767s) and persists the reviews
in a DynamoDB table.

[29:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1770s) We also have built-in
monitoring and observability

[29:32](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1772s) with CloudWatch and X-Ray.

[29:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1775s) But the previous diagram only shows

[29:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1777s) our application high-level architecture.

[29:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1780s) However, I want to show
you the full picture

[29:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1782s) and all the resources in our stack

[29:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1784s) as our display in CloudFormation Designer.

[29:47](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1787s) Here's where you can really appreciate

[29:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1789s) how much it was able to accomplish

[29:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1790s) by using infrastructure as code.

[29:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1794s) By using the AWS CDK plus
AWS Solutions Constructs,

[29:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1798s) my prototype is well-architected,

[30:02](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1802s) made from four constructs and
about 100 lines of TypeScript.

[30:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1806s) It includes 30 resources

[30:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1808s) on multiple environments
and multiple regions.

[30:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1811s) And the best part of all

[30:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1813s) is that I did not have to
write 820 lines of YAML.

[30:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1818s) So, Martin, back to you to
tell us what else can we do

[30:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1821s) with our production-ready prototype.

[30:24](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1824s) - That's great, Fabian.

[30:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1825s) That's really, like it's
amazing to see the evolution

[30:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1828s) from clicking around the console

[30:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1829s) through choosing CloudFormation

[30:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1831s) and ultimately CDK and constructs,

[30:34](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1834s) and that's just incredible what you can do

[30:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1836s) with really not a lot of code.

[30:39](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1839s) So what else could we do

[30:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1842s) given this foundation of using
CDK and using constructs?

[30:45](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1845s) Like one really interesting aspect

[30:47](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1847s) that I think is kind of a
game changer in some aspects

[30:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1852s) is the ability to not
test your infrastructure

[30:55](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1855s) while it's code and as code.

[30:57](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1857s) So we've got a few approaches within CDK

[31:00](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1860s) for testing your infrastructure,

[31:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1861s) first being snapshots,

[31:03](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1863s) secondly, validation,

[31:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1864s) and then most exciting
to me, to be honest,

[31:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1867s) is the fine-grained assertions.

[31:09](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1869s) And with these different
test capabilities,

[31:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1872s) you can even go as far as implementing

[31:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1874s) test-driven development

[31:15](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1875s) where you define the tests or the outcomes

[31:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1878s) that you wanna check for
in your infrastructure

[31:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1881s) and then build the CDK

[31:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1882s) to see if you've met those requirements.

[31:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1885s) And when you're past all your tests,

[31:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1887s) you're done with your development.

[31:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1888s) Obviously, you don't need to go

[31:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1889s) all the way to test-driven development,

[31:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1891s) so let's just have a look

[31:32](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1892s) at some of the test
capabilities within CDK.

[31:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1896s) So first off,

[31:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1897s) I mentioned we've got snapshots
as a testing capability.

[31:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1900s) And here you can see
there's a bit of code,

[31:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1902s) and at the last line there,

[31:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1904s) you can see it's synthesizing
the CloudFormation stack,

[31:47](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1907s) and it's matching that to a snapshot.

[31:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1909s) What this basically means is
we've got a reference snapshot.

[31:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1912s) If we look at the next slide,

[31:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1913s) we'll see we've got, the
first time I execute this,

[31:57](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1917s) I get the window on the bottom left,

[31:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1919s) and I've created the reference snapshot.

[32:02](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1922s) And the next time I do a deployment,

[32:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1924s) in this case I've changed
one parameter on the alarm,

[32:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1928s) and you can see that it's really simple

[32:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1930s) to see what has changed

[32:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1933s) and then to take an appropriate action.

[32:15](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1935s) So one action, for example,

[32:16](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1936s) might be just to pause your pipeline here

[32:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1938s) and have a manual approval step

[32:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1940s) but with the output of
this, like you can really do

[32:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1943s) kind of whatever makes
sense to your business,

[32:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1945s) but really simple but powerful capability,

[32:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1948s) especially if you've
got a known good state

[32:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1950s) that you manage for your infrastructure.

[32:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1953s) Next up is validation,

[32:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1955s) and this is really basically
unit-testing your code

[32:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1958s) and just treating it like any other code.

[32:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1960s) It doesn't matter that
it's infrastructure code.

[32:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1963s) So in this example, again,
we've got read capacity,

[32:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1966s) and we want read capacity, as
you can see at the top there,

[32:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1969s) to be between five and 20,

[32:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1972s) and the unit test at the bottom,

[32:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1974s) we're just passing in a value of three.

[32:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1976s) and testing that, we
actually get an exception.

[32:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1979s) So, again, by just doing this,

[33:01](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1981s) you can test that your code is actually,

[33:03](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1983s) your infrastructure code
is actually behaving

[33:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1986s) in the way that you want it to behave.

[33:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1988s) Finally, and this is probably
the most exciting bit for me,

[33:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1992s) is using the fine-grained assertions.

[33:15](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1995s) And here we've got an
assertion that you can see

[33:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=1998s) is like when this stack is created,

[33:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2000s) I just wanna know that the output

[33:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2003s) or the resulting CloudFormation
contains a DynamoDB table.

[33:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2007s) I'm just using that assertion.

[33:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2009s) But the assertions are really powerful,

[33:31](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2011s) and there are a number
of different assertions

[33:33](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2013s) that we can also, for
example, check on parameters.

[33:36](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2016s) I can check that all
the DynamoDB's created,

[33:39](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2019s) DynamoDB tables created within the stack

[33:42](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2022s) have encryption turned on.

[33:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2024s) So by doing this, you can
really implement tests

[33:47](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2027s) that validate your best practices

[33:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2030s) as you could do with, say, AWS Config

[33:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2033s) once the infrastructure is deployed.

[33:55](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2035s) But the beauty of this is
like these tests will run

[33:57](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2037s) before you actually have to deploy

[33:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2038s) any of your infrastructure.

[34:02](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2042s) So in addition to using

[34:03](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2043s) the AWS-provided Solution Constructs,

[34:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2047s) you can also build your own,

[34:08](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2048s) and this is, again, super, super powerful.

[34:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2051s) As an organization, you
probably have a, you know,

[34:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2053s) a set of applications or stacks
that really matter to you

[34:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2058s) and that are reusable
across your business.

[34:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2060s) And you've also got a set of best practice

[34:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2063s) or maybe even compliance
requirements that you,

[34:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2065s) ways that you require your teams to build.

[34:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2068s) And by capturing and codifying these

[34:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2070s) as reusable constructs
for your own organization,

[34:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2075s) you can enable your teams to
build both faster and safer.

[34:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2080s) So, hopefully, you've enjoyed the talk

[34:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2083s) and enjoyed seeing what's
possible with the CDK.

[34:47](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2087s) And just coming back to the principles

[34:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2089s) and kinda summarizing
where we're at there,

[34:51](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2091s) I didn't talk about
working backwards as much,

[34:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2093s) but like taking the time

[34:55](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2095s) to understand customer
requirements and diving deep there.

[34:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2098s) Again, within AWS and Amazon,

[35:00](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2100s) we actually spend a lot of time doing that

[35:02](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2102s) before we jump in to write code

[35:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2104s) because you can actually
do a lot of prototyping

[35:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2107s) without having to develop
a lot of the code itself.

[35:11](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2111s) Secondly, we weren't scrappy with security

[35:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2113s) because we've used constructs
that implement best practice,

[35:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2117s) like we're able to show

[35:19](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2119s) that those best practices are included

[35:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2121s) in our implementation.

[35:23](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2123s) We've used a lot of
serverless technologies,

[35:26](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2126s) and the beauty with that
is that the stack could run

[35:30](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2130s) for, you know, single-figure
budget dollar values

[35:34](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2134s) or really low dollar values per month,

[35:37](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2137s) and it will scale as you gain traction

[35:40](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2140s) and as you gain adoption.

[35:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2143s) And then we've also got a good foundation,

[35:45](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2145s) and we can extend this and expand on it

[35:47](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2147s) kind of as Fabian showed
you throughout his build

[35:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2149s) like really without
re-engineering a lot of things,

[35:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2153s) just adding capability and
enhancing the solution.

[35:57](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2157s) We know we can have good first impressions

[35:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2159s) 'cause we've got, again, using
the serverless capabilities,

[36:02](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2162s) we've gotta manage infrastructure

[36:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2164s) and manage components that we're using,

[36:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2167s) but we've also got operational
monitoring capabilities,

[36:09](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2169s) and we can hook that

[36:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2170s) into our existing operational processes.

[36:13](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2173s) And, finally, everything
we've done and shown you today

[36:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2177s) is in the code.

[36:18](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2178s) It's all this infrastructure.

[36:20](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2180s) The application logic

[36:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2181s) and even the monitoring and
alerting configs that we can do

[36:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2185s) has been done in the code.

[36:28](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2188s) So, if you're interested in seeing more,

[36:32](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2192s) here's a few sessions you
might wanna look into.

[36:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2195s) So as mentioned, building your
own higher-order constructs,

[36:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2198s) so there's a session on that, SVS319.

[36:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2201s) If you're interested in understanding

[36:43](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2203s) where you can get access to
maybe open-source constructs

[36:46](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2206s) or how you can share
constructs that you've built,

[36:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2209s) CDK is an open-source project,

[36:50](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2210s) and we're like engaging
with the community,

[36:53](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2213s) and the community helping each other

[36:54](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2214s) is really super important,

[36:56](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2216s) so check out OPN205.

[36:58](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2218s) CDKs also got capability

[37:00](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2220s) around continuous
deployment and pipelines.

[37:05](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2225s) We didn't really get into that today.

[37:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2227s) There's a dedicated session
for that, so DOP305.

[37:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2230s) I'd really recommend checking that out

[37:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2232s) both how you could use
CDK to standout pipelines

[37:15](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2235s) and also how you can think about using CDK

[37:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2237s) within your pipelines.

[37:19](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2239s) And then finally, if you're
just interested in understanding

[37:21](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2241s) what's new with CDK and
CloudFormation and that whole space,

[37:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2245s) please check out DOP315.

[37:29](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2249s) If you are interested in
trying out any of the code

[37:32](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2252s) or examples that we've
used in this presentation,

[37:35](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2255s) you can access that at the first link,

[37:38](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2258s) and then I've got a link to just CDK,

[37:41](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2261s) the AWS Solution Constructs.

[37:44](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2264s) And I also wanna give a shoutout
to the AWS CDK workshop.

[37:47](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2267s) This is a really, really good workshop.

[37:49](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2269s) If you're just getting started with CDK,

[37:52](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2272s) it will take you right from
bootstrapping your account

[37:55](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2275s) for the first time

[37:55](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2275s) right through to building
your own constructs

[37:57](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2277s) and doing testing,

[37:59](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2279s) like really the full gamut of
capabilities within the CDK.

[38:04](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2284s) And if you're interested

[38:05](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2285s) in more of the kind of the software side,

[38:06](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2286s) the non-technical side,

[38:07](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2287s) like how do we use working backwards,

[38:10](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2290s) here's a link to a blog post from Werner

[38:12](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2292s) on working backwards.

[38:14](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2294s) So with that, I'd just like
to say thank you very much

[38:17](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2297s) for your time and your
interest in this talk,

[38:19](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2299s) and thanks, Fabian, for really diving deep

[38:22](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2302s) and showing us how we
could use CDK to build,

[38:25](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2305s) so thank you.

[38:27](https://www.youtube.com/watch?v=-_Zl9u9i1KI&t=2307s) (upbeat music)

