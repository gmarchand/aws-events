# AWS re:Invent 2021 - Build a high-throughput asset-tracking architecture

[Video Link](https://www.youtube.com/watch?v=G8Rkuu6X-_8)

## Description

Industry leaders are well aware of how geospatial data can help them optimize asset utilization, deliveries, geomarketing, and many other use cases. However, the process of tracking assets effectively presents challenges that go beyond the business level. This session uses vehicle tracking as an example to show how you can architect a serverless solution that tackles the technical challenges that this topic conventionally presents, including scalability, complexity, and real-time aspects.

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK
 
Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

(chill beat music) - Hello, everyone. Welcome to Work 309, where we show you how to architect a high throughput asset
tracking application. My name is Fernando. I'm a Senior Specialist
Solution Architect on AWS for mobile and front end technologies. And I'm here with my
friend, Raphael, today. - Hi everyone, my name's
Raphael Leandro Junior, I'm Global Solutions Architect for consumer packaged goods
and transportation at AWS. - And in today's sessions, we'll walk you through how to tackle common technical challenges relating to building a high throughput
solution for asset tracking, and how we were able to achieve success by using a combination of
AWS services in doing so. And we have a very simple
agenda for you today. First, we'll be talking about use cases for asset tracking applications
and why they are important. We'll also be focusing on
challenges that consumers face when building and testing solutions that require high throughput. Then we'll cover the
solution, the technology used, and architectural
considerations around it. Finally, let's go through
a very important piece in any solution that needs to scale and maintain its integrity, simulating. Let's start by talking about applications and the challenges faced when building asset tracking solutions. First, we need to understand that today, location data comes from everywhere, vehicles, buildings, satellites,
networking appliances, mobile devices, trackers,
landmarks, wearables. You can really observe that
it is estimated that by 2025, the location-based service market is expected to be worth $39.2 billion. That's a big growth from
what it was worth in 2020, which was $17.8 billion. That amounts to a 17.1% growth per year. And why do we track assets? Well, the easy answer is to make informed decisions based on the data provided by them. Pick a vehicle, for example, maybe an oil temperature
of 230 degrees Celsius is enough information for a driver to be really okay with how
the vehicle is performing. This data can indicate much more, though. It could indicate that, well, based on this temperature
level, the weather, the road conditions, and
maybe the amount of time that it is taking for
the oil level to drop, that this vehicle needs to
go under maintenance, ASAP. Understanding the current
location of an asset and how far they are from a destination is also crucial for businesses to make decisions on operations. If I know that a truck is 15 minutes away from my loading dock, I can start preparing
the personnel in the area to receive my goods. Having the ability to
adjust my area beforehand can increase my productivity by a lot. And if you have the information
on where your assets are and for how long they're
staying in certain areas, maybe you can determine if
assets are constantly idle or working for more time than expected. This, paired with sensor data, can give you a big
advantage in understanding exactly how your assets are performing, and you can really understand if they're current under maintenance, functioning really well, or even if they need to be replaced. And of course, tracking assets provide a myriad of challenges
from a technical perspective. Think of it this way. Imagine back in 2012, not that long ago, you got a requirement to build a solution that needed to receive data from 50 trucks via SOAP API calls every five minutes. You went ahead and created a solution, hosted on two load-balanced
virtual machines, connected to a single database instance. You had to manage all of that
infrastructure, of course, OS updates, antivirus,
database patches, everything. Hardware really becomes
obsolete very quickly, right? But you're powering through,
everything's working. That worked out at the time, but time changes, technology evolves. Maybe you're now supporting 150 vehicles sending data every two minutes and you have a lot more
people interested in the data. So maybe you have created
a replica of your database for only reading tens of tasks, and you really changed
your monolithic application to support not only SOAP,
but REST APIs as well. Everything works, but things
tend to break more often. One day, you get a message from the CIO, "Solution's amazing. Ah, let's use it to track
all shipments in the company, all 150 shipments." What do you do? Business challenges aside, there's a number of technical challenges that you're not prepared for. Your infrastructure is
the same since 2012. Is that enough to receive
this amount of data? Can your monolithic application scale to consume a hundred times more data than what it is expecting? How the performance look like? How are you onboarding new
vehicles extremely quickly, guaranteeing that well,
traffic remains secure and never leaves your
database or your project, unless it's really allowed to. How are you making sure
that, as your traffic scales, that you're keeping identity and access management under control? How many people can manage your solution? Who can deploy your application or play with your infrastructure? By the way, can your database
with a single read replica handle all of this load? How do you answer this question? How can you test it? Are you ready to reproduce data coming from hundreds of
thousands of devices? And that's the use case that we chose to present a solution for. It relies on vehicles as assets. We chose vehicles because
they're able to produce a very large number of sensor data, and they are constantly moving,
providing us the ability to add tracking capabilities
into our solution. The telemetry data comes
from fictitious sensors, speed, acceleration, torque, oil and fuel level, things that cars have. And all of this data fits
perfectly into monitoring and adding a solution
that will be presented not only to address the high scalability, but to dig deep into the details
produced by each vehicle. And all of that is part of a
simulation engine created by us to consume millions of
requests per minute. I'm going to pass it over to Rafael, who's going to talk to
you about the solution. - Thank you, Fernando. To present the solution, we'd
like to start with a demo and then we return back to the deck to explain the architecture design, and the logical flow
supporting the solution. - This is our solution demo. On the right side, we have a simple web
application including a map. On the left side, the incoming dashboard, where we will see all information
regarding the vehicles. This demo is prepared not only to receive
data from real vehicles, but also to simulate those
vehicles for testing protocols. So let's say you have 20 trucks in a fleet going from your exhibition centers to dealer sites, for instance. And, of course, you'd like to track them. So let's include those vehicles here. The vehicles, all right The solution generates
a route for each vehicle also including a geofencing area. As an example for this demo, each geofence will represent an area around
the distribution center where the vehicle just left. The vehicles are popping
up on the map right now and sending data, as you can see on the
monitoring dashboard. Let's take a look closer at one vehicle to see it moving on the map. So let's pick one vehicle here. We just need to zone in. Okay, a little bit more. Let's see more. All right. Okay, so the vehicle's running and updating its position
on the map properly, right? Although the routes are dynamically generated by the solution, the vehicle positions are real, following the given route,
which enable us to receive real latitude and longitude pairs to make the simulation more
similar to the reality. Let's zoom out here to see
more vehicles on the map. All right, that is a good, that is good. Okay, so looking at the
monitoring dashboard, you can see the number
of vehicles running. You can also see the
number of geofence events, which means, in this case,
that all those 20 vehicles left the distribution center area. We also can see the
number of location events and telemetry events that
we are receiving per minute. Right? So with these numbers, we
can say that you are saving almost 3000 events per minute, including location and telemetry events for those 20 vehicles. Below some critical information we decided to monitor closely, which includes a list of
the highest speed vehicles, a list of the lowest fuel level vehicles, and a list of the highest
oil temperature vehicles. If you'd like to see more information about any specific vehicle, you can just click on the vehicle, such as this one, for example,
with the highest speed. And here you can see all metrics about that specific vehicle in real time, including its speed, oil
temperature, fuel level, the positions within the
last minute, and so on. Let's move back to the main dashboard. Okay, so now imagine
that one of your vehicles is in high risk by running with an extremely
low fuel level, for instance. In that case, we expect to be alerted so we can take actions immediately. So let's simulate that
and put the mobile phone in the screen in order
to wait for the message. So let's put a mobile phone here first. All right. Now, let's select one
vehicle here on the map. Let's see, let's pick this one in London. We selected this. We can see the VIN number start with 9J9 and let's simulate the low fuel level. Okay so, as you can see, the vehicle pin just changed its color to red. So it represent a red flag in the map, and also you can see the same information in the lowest fuel level vehicles. That specific vehicle is
showing with 1% of fuel level, which is a high risk, right? Regarding the text message, in our mobile we just
received a text message alerting about that high risk vehicle with the VIN number, the
fuel level which is 1%, and also the position for that vehicle. Then you can open and click on this and see the right
location of that vehicle. All right, let's move back
to the dashboard here. Okay, so we've tested this
solution with 20 vehicles and we received about 2,900, 3000 events per minute. But what if you have 100,000 vehicles? Let's onboard those on the map, let's onboard 100,000 vehicles here. You will see more and more vehicles popping up on the map shortly. And also, they did formation
on the monitoring dashboard. Everything in scale tends
to be more complex, right? You need to deal with
the underlying resources for scalability and many other factors. That's why building our resilient and our scalable
architecture is important. Doesn't matter if you
have just few vehicles sending 3000 events per minute
or thousands of vehicles sending 10 million events per minute, you can build an architecture that keeps up with your
growth and your new load. So now, you can see that we
have almost 100,000 vehicles. It's counting and we
are receiving now about 20 million, 25 million events per minute. So here we have a high throughput
solution that can receive a large amount of events
each minute, right? Yeah, so now there are 5
million events per minute. Okay, so additionally to that, it's also important to monitor the underlying infrastructure
supporting the solution. In this dashboard, we are
monitoring important metrics for Lambda functions in this solution, including errors, portals, service limits, and any other issue that
can impact the solution. And you can see with this graph here, when we just launch 100,000 vehicles, you can see this graph,
this peaking right here. All right, so let's go
back to the main dashboard. All right, all those geofence events, we just received all of them. Okay, so we now have
100,000 vehicles running, about 30 million events per minute. Okay, so let's go back
to the presentation deck to understand how the architect design and the logical flow look like. Okay, so let's walk through the architectural design for the solution. We'll dive deep into each specific flow in the following slides, including why we choose
each specific service, but intention for now is to
provide you the big picture and the vision of what we are using. The fleet of simulated vehicles send their telemetry and location data over MQTT to AWS IoT Core. Those messages are
filtered using IoT rules and sent to different services,
depending on the case. For example, the IoT rule is responsible to capture all messages and store them in a time series database
with Amazon Timestream, by leveraging it's built-in integration. So we don't need to write
additional code for that. All the location messages
coming from the vehicles are saved to a Lambda function where two actions are performed. First is a dual-facing validation that checks if the vehicle
entered in or exited a predefined area of interest or geofence, which is one of the Amazon
Location Service features. If so, it generates an
event in Amazon EventBridge that triggers a Lambda
function responsible to start that in a Timestream database. The second action is to register
the new vehicle position in AWS AppSync, which
will generate a notation and store the new position
in a DynamoDB table. That notation in AWS AppSync
is captured by the application, the AWS Amplify, who will update the vehicle position on the map. An IoT rule is also being
used to filter critical events that require an immediate attention, such as a vehicle in high speed
or in any other high risk. We filter those messages to send over to another Lambda
function that we process and notify whoever's needed through Amazon Simple
Notification Service. In terms of monitoring, we are using Amazon Managed Grafana, leveraging it's default
integration with both Amazon Timestream service, where we have now all data
about the vehicle's trip, and also, Amazon CloudWatch, where we follow some
important service metrics, such as API throttling,
errors, and limits. This architecture is fully serverless, so we don't need to deal or manage any virtual machine's operational system. Now that you have a vision of
database services in scope, let's talk about the security
aspects for the solution. Secure is job zero, and will
always be our top priority. In a typical off-premises security model, customers are responsible
for the end-to-end security and reliability in their
data centers, which includes facilities, power, cooling,
hardware, and so on. In AWS, we have a shared
responsibility model with the customer, where
AWS manages and controls the components from the
host operational system and the virtualization layer down, to the physical security of the facilities in which the services operate. And AWS customers are responsible for building security applications. The level of responsibility, however, for each change depend on
the AWS services you choose to build your solution. If you choose infrastructure services using virtual machines with
Amazon EC2, for example, you are responsible to secure everything from the traditional system layer that will support your application, which means that you should
think about security patches, hardening, updates, OS,
firewall, antivirus solutions, and so on. On the other hand, by using serverless services
as we are doing today, AWS takes even more responsibility. With that model, customers
don't need to deal with the traditional system
layer or network components. Our service architecture
provides infrastructure security and network isolation, by design, which will release you to
focus more on your business, application, and innovation. With this, we've quickly addressed one of the security challenges that
Fernando mentioned before, but you still have your
portion of responsibility with security, which include developing secure application code validated with automated CI/CD process, encrypt your data and manage the access and
authorization policies, following the least privileged principle. Talking about authentication
and authorization, AWS provides a number of
different authentication method to support your environments. For your IoT devices, you
can use client certificates, AWS IAM, or Amazon Cognito. Once the data achieves AWS IoT, the permissions among
services are provided by IAM roles and policies. Some carriers use mobile
device to track vehicle. So if that is your case, probably you will prefer to have HTTPS end
points to send your data, and authentication method will follow your connection portal. To authenticate to Amazon Managed Grafana, we are using AWS Single Sign-On and for the web application,
we are using Amazon Cognito. We think, at AWS, you manage the privacy
controls of your data, control how your data is used, who has access to it,
and how it is encrypted. We make it easy to encrypt
data in transit and at rest using keys, either managed by AWS or fully-managed by you. You can build your own keys that were generated and
managed outside of the AWS. AWS Database and Storage Services provide encryption at rest,
which for the solution includes not only Amazon Timestream and Amazon DynamoDB databases, but also geofences collection
with Amazon location and environmental variables
and deployment packages with AWS London. We easily keep all data in the
solution encrypted at rest. AWS IoT message broker
encrypts all communication while you're in transit, using TLS 1.2, including the connection
between the devices and the AWS IoT. All AWS services use TLS 1.2 and beyond to communicate to each other, unless otherwise specified, which means that all data in this solution are also encrypted in transit, by default. Still, in data protection
and data privacy area it's important to remember to avoid using personal identifiable information to name your resources. For example, don't use any mail address, a personal name or document number as part of your IoT topic or to name your geofence collection. You don't want an IoT topic
named with the driver's name, or a geofence collection
with the actual address. So now that you had a good idea of how the architecture looks like
and its security aspects, let's dive deep into each logical flow. Everything starts with the vehicles, or simulated trucks, in our case. In a real world scenario, you can equip your vehicles
with sensors or devices that collect metrics continuously. For example, using OBDII devices to provide
the real time data, in addition to a series of
diagnostic trouble codes. You can connect your IoT devices to our cloud-based service, AWS IoT Core, which forms the backbone
for IoT deployments, to securely connect all your devices and handle their data at scale. You can not only ingest IoT data to AWS, but also keep a communication
among your devices and send back information as needed. In our solution, we are
using MQTT as the protocol to send telemetry data
from the vehicle devices to AWS IoT topic or a message
broker with AWS IoT Core. All messages go to a topic that includes the vehicle VIN, which we are using as the device ID. MQTT is a lightweight and widely-adopted messaging protocol that is
designed for constrained devices, but AWS IoT Core also supports MQTT over WebSocket Secure,
HTTPS, and Loader One protocols. Our soft limit to be aware of is the inbound virtual requests
per second, per account, priority for message broker, which is currently 20,000
per second in most regions. It's manageable. You can work with AWS
support to increase this, based on your use case. Check the actual limit for
the region you selected. Each vehicle sends a number of
different metrics per second, including location, with the
pair of latitude and longitude, acceleration, fuel level, speed, oil temperature, engine speed, torque and
transmission, odometer, and other five metrics, but it could be much more. In a real world scenario, you
will probably prefer to send all metrics at once, at a more spaced frequency
such as every five second, almost a minute, or even in a few minutes, depending on your environments, budget and your appetite for your time. You can even implement the name key method that will change the
frequency to send metrics depends on the actual vehicle speed. So if your vehicle is too fast, probably you would like to
send your metrics more often, almost in a fraction
of second, for example. If a vehicle is too slow, you'll be okay by sending
metrics almost in a few minutes. A good idea here would it be embed an IoT gateway with AWS IoT
Greengrass in each vehicle, that would not only process the data and take automated actions locally, based on the code you deployed
from your AWS environment, but also handle eventual
connectivity issues, keeping this solution
working, even if the vehicle is still probably
disconnected from the AWS IoT. It also can preprocess data and group all metrics before
sending it over to AWS IoT. You could also implement
a machine learning model that keep you running at the edge. In other words, embedded in your vehicle. One idea could be implementing
a machine learning module to alert the driver
about the optimum moment to refill the tank, for example. If you just need to ingest
data from IoT devices to AWS, with no reverse communication or communication among devices, you can consider to use IoT Basic Ingest, to reduce costs and to manage better your quota for the service. With Basic Ingest, you send
your messages directly to the IoT rule that we will
explain in the next slide, bypassing the traditional IoT topic. Once the message reach the
IoT topic in the AWT IoT Core, you can easily filter
messages and directed them to the appropriate target
by using IoT rules. In AWS IoT, rules are defined
using a SQL-like syntax. First example, here, we are filtering all location messages
related to all vehicles. We are picking the vehicle VIN, latitude, longitude, and time stamp, and send them to AWS Lambda function, where, in that Lambda function, we are using Python to
update vehicle position and validate geofence device that Fernando will
explain in a few slides. In the second example, we are
filtering a critical event directly from the IoT topic to notify operators as soon as possible. In this case, we can easily track if a vehicle is running with
a critical oil temperature, by using that simple SQL-like syntax. Third example here, we are
getting all the messages to store them in a Timestream database. You just need to include the
SQL statement to do that. Select the Timestream database
and the table as a target. And now you will have all vehicles data in the Amazon Timestream. We chose Amazon Timestream
because it's a fast, scalable, fully-managing, purpose-built
time series database that makes easy to store and analyze trillions of time series
data points per day. It manages the life cycle
of time series data, by keeping recent data in memory
and moving historical data to a cost-optimized storage tier, based upon the user-defined policies. It has built-in time
series analytics functions, helping you identify trends and patterns in your data, in near-real time. It's serverless and
automatically scale up or down to adjust capacity and performance. Because you don't need to manage the underlying infrastructure, you can focus on optimizing
and building your applications. You can easily plug your
monitoring system to Timestream, such as Amazon Managed Grafana. Amazon Managed Grafana is
a fully-managed and secure data visualization
service that you can use for instantly query,
correlate, and visualize perishable metrics, logs, and
traces from multiple sources. The service makes it
easy to deploy, operate, and scale Grafana, which is a widely deployed
data visualization tool that is popular for its
extensible data support. It's integrated with AWS data sources that collect operational data,
including Amazon CloudWatch, Amazon Loki search service,
Amazon Timestream, and others. For user authentication and authorization, Amazon Managed Grafana can integrate with identity providers
that support SAML 2, and also can integrate
with AWS Single Sign-On. We are using Amazon Managed Grafana as our single operational
monitoring for all data. We can easily create monitoring by leveraging its integration
with Amazon Timestream, that supports a rich SQL-like language. So we can monitor what you
saw in the demo and much more. This is an example of a query
from Grafana to Timestream, to list the top 100
vehicles in high speed. We are selecting vehicles VINs and their average speeds
in a given timeframe, limiting up to 100 and
reverse ordering by speed. So we can show first the
vehicles in highest speed. In green, other labels Grafana provide you to make it simpler to create queries. So you don't need to enter
your default database and table every time and can use
the same time filter you defined for your entire dashboard. In addition to vehicle monitoring, we can include AWS services monitoring with the Amazon CloudWatch integration. So we can follow eventual API throttling, any errors while processing events, service limits, and others. As we mentioned before, there are some critical events that we may want to notify
operators immediately. For that, you can filter messages directly from the IoT
topic using IoT rules and use an AWS Lambda as target to process the event and
send it over to Amazon SNS that will notify all the
subscribers for that kind of event, by using email, mobile
text, push notifications, PagerDuty, or any other destination
supported by Amazon SNS. In that way, important events
reach to the right people as quick as the solution
receives them, in real time. Now, I hand over, back to Fernando. - Another very important piece of every asset tracking solution is the ability to notify
interested parties when assets are inside areas of interest. With Amazon Location Service's
geofence collections, you can automatically
evaluate a vehicle's position against all of the geofences
inside that collection. It all starts with the
incoming data on AWS IoT Core, as Raphael explained. The arriving data is
processed by the topic rule and sent to AWS Lambda, where the geofence lookup is initiated. The request contains the vehicle VIN, which is the asset identifier, and the current positioning,
latitude and longitude format. Amazon Location evaluates this position against all of the
geofences in the collection to determine if an asset is
entering or exiting an area. If any of these events occur, this event is sent to Amazon EventBridge, where a Lambda function is
triggered, and the action is saved on Timestream
for monitoring purposes. This event contains the asset information, the geofence breached, the event itself, either enter or exit, and the timestamp associated to the event. With all of these events, you
can calculate for how long an asset stayed within a certain area, if they are outside an allowable location, or even notify interested
bodies of asset movement. You'd also want a real-time
visualization representation of where your assets are. With AWS Amplify, you can leverage AppSync to create subscriptions that will trigger front end updates in every
vehicle movement that occurs. The incoming data is
processed by AWS IoT Core, and the Lambda function
sends a mutation request to AWS AppSync, which is our GraphQL serverless solution. This mutation contains vehicle VIN, and the current location set. AppSync has two responsibilities here. First one, store the vehicles last
position on Amazon DynamoDB, one of our NoSQL databases, famous for its single digit millisecond
performance, at any scale. And also, AppSync is responsible for triggering a front
end update on our map, as you saw in the demo. So every time a vehicle moves,
you see represented on a map. Now we have been talking about storing a lot of location data in the solution, and we need to start
thinking about good practices that we can implement
to avoid storing data that we do not really need, not only from a data volume perspective, but also from a security
and privacy perspective. You can see here, from
a location perspective, how we can broaden an area to make coordinates more
general and less precise by just removing a decimal place. By rounding up, we can
aggregate all assets within a radius of a position. One decimal place, for
example, is broad enough to aggregate all of the
assets within a city. That's about 11.1
kilometers or seven miles. As we add a decimal place,
we get more precise. At two decimal places,
we can aggregate assets within a town of 1.11 kilometer radius, or three quarters of a mile. Three decimals can be a
facility or a warehouse, four decimals could be the lane of a road, and five decimals would give us a car, at 1.11 meters or 3.5 feet. Amazon Location Service have the ability to store location data
up to six decimal places, which would give you the position of a cup
of coffee, for example. However, you really need
a very accurate GPS device to collect such an accurate position. And when working with sensitive
data of asset locations, we should design an architecture that only takes what we need to respect the consumer's privacy. We're also improving performance by minimizing lookup queries, and then saving costs by
removing query redundancy. We can refer to this as
least privileged precision, to store and handle only the
level of location precision that our use case needs. Moreover, we can generate
cache-friendly identifier using a geocoding system like geohashing. There are a few open
source ones out there, but Geohash is one that
is in the public domain. And to bring this back to our use case, a vessel tracking application would want to localize vessels
positioned in the ocean. So three decimals of precision would suit the requirements really well. For a vehicle's exact
location on the road, though, you may want to add more
precision to your query to identify where the car is. And these are the features that Amazon Location
provides to you today. With maps, you can add
a visualization layer into any application. Places gives you searching capabilities, geocoding and reverse geocoding. Routes will give you information on how to get from point A to point B. All of these features are backed by two trusted AWS partners, huge players in the geospatial market, Esri and HERE Technologies. Their data currently supports millions of applications on a daily basis. From a privacy standpoint, all queries that are made to Esri and HERE are anonymized, and you can
choose which data provider to use, with one single
API to consume from. So you can basically change providers without changing source code, or creating new agreements
with new companies and not even generating new credentials. All you need is an AWS account. There are also no penalties if you stop using the service. Start and stop whenever you want. You also get data ownership on geocoding and reverse
geocoding results, being able to store them in your own storage services or databases. Trackers will let you send and retrieve real-time batch geolocation information for vehicles, mobile
devices, and any other assets that can actually provide
their location information. Amazon Location Service
this year introduced Positions Filtering as
a new option to trackers that really enables cost reduction and reduces jitter effects from inaccurate device location updates, along with the addition of true
position filtering options. And lastly, you can use
geofences in a solution like this to identify areas that are interesting to this particular use case. And that's what geofences are, areas of interest were actions related to geolocations can occur. Geofence collections on Amazon Location provides the capability of detecting enter and exit events on these areas. By providing the current
position of a vehicle, these collections are
automatically evaluated against all the geofences
that they have stored. Once it is detected that a vehicle has entered
one of those geofences, an enter event is posted
to Amazon EventBridge for further processing. The location evaluation
can happen via an API call or by linking trackers and
geofencing collections together, really freeing you from
calling the API directly. This is great from an automation
and integration standpoint. Finally, tracker and geo-fencing data never leaves your AWS account. That data is encrypted by
default, at rest and in transit, and you can even use your own
keys to encrypt it, as well. Now that you understood
to the building blocks that we're using to guarantee security, performance efficiency, and operational excellence
in this solution, let's talk about a very
important piece of every solution that needs to handle events as
close to reality as possible, simulating. Raphael showed you before during our demo, how this application scales. When you start from 10 or 20 cars, things are very easy
to manage and control. Not a lot of compute power
is needed at this point to maintain this very
small amount of data. Scaling to 100,000 vehicles,
however, can be daunting. How can we test with 100,000
vehicles instead of 10? Let me show you. First of all, we created
a simulation engine. That simulation engine relies on an AWS Amplify hosted
front end, built in ReactJS. This front end communicates
with AWS via REST APIs, that basically create a
number of Lambda functions that handles the vehicle
simulation processes. The rest of the architecture
is virtually the same, as the Lambda functions are now the ones communicating to AWS IoT Core. If you were managing 10
cars, you could easily spin up 10 Lambda functions
to represent them. By scaling to 100,000 cars, however, if you keep the same process, you will face issues like timeouts, concurrency issues, and also service limits. On average, we were able to invoke 17.5 Lambda functions each second, and we can try to use a fan out pattern. So instead of invoking all
of them in a single loop, we can create 100 batches that will create Lambda functions that will
manage 10 vehicles each, which gives us 100K in
total, which is what we need. And we can also have an
intermediary Lambda function that will trigger individual
workers for each vehicle. We have a scaler that reads the configuration of all
tasks that we have to execute and divides them into
batches of 100 Lambdas, invoking trigger Lambda functions, right? We'll pass one batch to each of them. In our case, we'll have to invoke it 100
times with 100 Lambdas each. Trigger function receives
a batch of requests and invokes the vehicle's
function for each of them. Since each of the triggers
will have to invoke only up to 100 workers, it should take them five to 10 seconds. Each vehicle function will
be responsible to handle only 10 vehicles, so we won't
be blocking other processes. You could play with those numbers to achieve the level
desired by your solution. But from a cost perspective, you can even reduce the
memory and timeout limits for the Lambda functions now. Make sure that you're requesting
any service limit increases that are needed on your AWS account, to handle a solution like this. And when you're
architecting for the cloud, you need to keep API throttling in mind, particularly the types of calls and the frequency in
which they are called. When the allotted rate limit
for an API call is exceeded, you receive an error response and the call will be throttled. Excessive API throttling
can result in job failure, delays, and operational inefficiencies, that will ultimately
cost your organization time and money, of course. Retry logics are automatically implemented when you leverage the AWS SDK,
so maybe do that (laughs). But you can do it on your own, as well, as the pseudocode on the right suggests. In addition to simple retries, each AWS SDK implements an
exponential backoff algorithm for best flow control. The idea behind exponential
backoff is to use progressively longer waits between retries for consecutive error responses. And retries can be very ineffective if all clients retry at the same time. To avoid this problem, we employ jitter, a random amount of time before
making or retrying to request to help prevent large bursts, by spreading out the arrival rate. Most exponential back office algorithms already use jitter to prevent
successful collisions. The last piece of our simulation engine is the dynamic route creation process. When we scale our vehicles, our trigger Lambdas generate routes, based on origin and destination
points stored on DynamoDB. They call Amazon Location
to calculate the routes and store all the polylines in memory, which are used to mimic the
vehicle driving process, as you saw it on the
demo that Rafael showed. We also pick a random point of the route that represents an area of interest and create a dynamic geofence
with a 300 meter radius, so whenever the vehicle
enters or leaves an area, a geofence event is presented
on Grafana for visualization. And this is our solution. Well, if you want to
build something similar, a very good way to start testing your
asset tracking solution is by leveraging AWS IoT Device Simulator. It's a one-click deployment process that leverages AWS
CloudFormation templates to deploy the solution for you, in your AWS account, in minutes. With IoT Device Simulator, you can not only simulate vehicles, but also simulate
different types of devices with your own desired metrics. It creates an entry
point with AWS IoT Core that you can leverage to
onboard your own data, like we did in the demo. And that's all we have for today. We'd like to thank you for your presence. Thank you so much. (chill beat music)

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1s) (chill beat music)

[00:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=10s) - Hello, everyone.

[00:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=11s) Welcome to Work 309,

[00:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=13s) where we show you how to architect

[00:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=15s) a high throughput asset
tracking application.

[00:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=18s) My name is Fernando.

[00:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=19s) I'm a Senior Specialist
Solution Architect on AWS

[00:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=23s) for mobile and front end technologies.

[00:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=25s) And I'm here with my
friend, Raphael, today.

[00:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=28s) - Hi everyone, my name's
Raphael Leandro Junior,

[00:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=31s) I'm Global Solutions Architect

[00:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=32s) for consumer packaged goods
and transportation at AWS.

[00:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=36s) - And in today's sessions,

[00:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=38s) we'll walk you through how to tackle

[00:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=39s) common technical challenges relating to

[00:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=42s) building a high throughput
solution for asset tracking,

[00:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=46s) and how we were able to achieve success

[00:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=48s) by using a combination of
AWS services in doing so.

[00:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=55s) And we have a very simple
agenda for you today.

[00:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=58s) First, we'll be talking about use cases

[01:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=60s) for asset tracking applications
and why they are important.

[01:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=64s) We'll also be focusing on
challenges that consumers face

[01:07](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=67s) when building and testing solutions

[01:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=69s) that require high throughput.

[01:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=72s) Then we'll cover the
solution, the technology used,

[01:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=76s) and architectural
considerations around it.

[01:20](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=80s) Finally, let's go through
a very important piece

[01:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=83s) in any solution that needs to scale

[01:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=85s) and maintain its integrity,

[01:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=87s) simulating.

[01:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=91s) Let's start by talking about applications

[01:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=93s) and the challenges faced

[01:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=94s) when building asset tracking solutions.

[01:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=99s) First, we need to understand that today,

[01:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=102s) location data comes from everywhere,

[01:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=104s) vehicles, buildings, satellites,
networking appliances,

[01:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=108s) mobile devices, trackers,
landmarks, wearables.

[01:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=112s) You can really observe that
it is estimated that by 2025,

[01:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=116s) the location-based service market

[01:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=118s) is expected to be worth $39.2 billion.

[02:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=121s) That's a big growth from
what it was worth in 2020,

[02:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=124s) which was $17.8 billion.

[02:07](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=127s) That amounts to a 17.1% growth per year.

[02:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=134s) And why do we track assets?

[02:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=135s) Well, the easy answer is

[02:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=137s) to make informed decisions

[02:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=138s) based on the data provided by them.

[02:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=141s) Pick a vehicle, for example,

[02:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=143s) maybe an oil temperature
of 230 degrees Celsius

[02:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=147s) is enough information for a driver

[02:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=149s) to be really okay with how
the vehicle is performing.

[02:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=152s) This data can indicate much more, though.

[02:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=154s) It could indicate that, well,

[02:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=156s) based on this temperature
level, the weather,

[02:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=159s) the road conditions, and
maybe the amount of time

[02:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=162s) that it is taking for
the oil level to drop,

[02:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=165s) that this vehicle needs to
go under maintenance, ASAP.

[02:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=169s) Understanding the current
location of an asset

[02:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=172s) and how far they are from a destination

[02:54](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=174s) is also crucial for businesses

[02:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=177s) to make decisions on operations.

[03:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=180s) If I know that a truck

[03:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=181s) is 15 minutes away from my loading dock,

[03:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=184s) I can start preparing
the personnel in the area

[03:07](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=187s) to receive my goods.

[03:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=190s) Having the ability to
adjust my area beforehand

[03:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=192s) can increase my productivity by a lot.

[03:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=196s) And if you have the information
on where your assets are

[03:20](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=200s) and for how long they're
staying in certain areas,

[03:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=203s) maybe you can determine if
assets are constantly idle

[03:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=207s) or working for more time than expected.

[03:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=210s) This, paired with sensor data,

[03:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=212s) can give you a big
advantage in understanding

[03:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=214s) exactly how your assets are performing,

[03:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=218s) and you can really understand

[03:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=220s) if they're current under maintenance,

[03:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=222s) functioning really well,

[03:43](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=223s) or even if they need to be replaced.

[03:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=229s) And of course, tracking assets

[03:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=231s) provide a myriad of challenges
from a technical perspective.

[03:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=235s) Think of it this way.

[03:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=236s) Imagine back in 2012, not that long ago,

[04:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=240s) you got a requirement to build a solution

[04:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=241s) that needed to receive data from 50 trucks

[04:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=244s) via SOAP API calls every five minutes.

[04:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=248s) You went ahead and created a solution,

[04:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=250s) hosted on two load-balanced
virtual machines,

[04:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=254s) connected to a single database instance.

[04:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=257s) You had to manage all of that
infrastructure, of course,

[04:20](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=260s) OS updates, antivirus,
database patches, everything.

[04:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=265s) Hardware really becomes
obsolete very quickly, right?

[04:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=268s) But you're powering through,
everything's working.

[04:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=271s) That worked out at the time,

[04:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=272s) but time changes, technology evolves.

[04:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=276s) Maybe you're now supporting 150 vehicles

[04:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=279s) sending data every two minutes

[04:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=282s) and you have a lot more
people interested in the data.

[04:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=284s) So maybe you have created
a replica of your database

[04:47](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=287s) for only reading tens of tasks,

[04:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=291s) and you really changed
your monolithic application

[04:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=293s) to support not only SOAP,
but REST APIs as well.

[04:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=297s) Everything works, but things
tend to break more often.

[05:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=302s) One day, you get a message from the CIO,

[05:05](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=305s) "Solution's amazing.

[05:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=306s) Ah, let's use it to track
all shipments in the company,

[05:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=309s) all 150 shipments."

[05:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=312s) What do you do?

[05:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=314s) Business challenges aside,

[05:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=315s) there's a number of technical challenges

[05:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=317s) that you're not prepared for.

[05:20](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=320s) Your infrastructure is
the same since 2012.

[05:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=323s) Is that enough to receive
this amount of data?

[05:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=326s) Can your monolithic application scale

[05:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=328s) to consume a hundred times more data

[05:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=331s) than what it is expecting?

[05:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=334s) How the performance look like?

[05:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=336s) How are you onboarding new
vehicles extremely quickly,

[05:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=340s) guaranteeing that well,
traffic remains secure

[05:43](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=343s) and never leaves your
database or your project,

[05:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=346s) unless it's really allowed to.

[05:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=349s) How are you making sure
that, as your traffic scales,

[05:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=352s) that you're keeping identity

[05:54](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=354s) and access management under control?

[05:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=357s) How many people can manage your solution?

[06:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=361s) Who can deploy your application

[06:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=363s) or play with your infrastructure?

[06:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=366s) By the way, can your database
with a single read replica

[06:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=369s) handle all of this load?

[06:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=371s) How do you answer this question?

[06:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=374s) How can you test it?

[06:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=376s) Are you ready to reproduce data

[06:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=377s) coming from hundreds of
thousands of devices?

[06:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=383s) And that's the use case

[06:24](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=384s) that we chose to present a solution for.

[06:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=387s) It relies on vehicles as assets.

[06:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=389s) We chose vehicles because
they're able to produce

[06:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=392s) a very large number of sensor data,

[06:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=394s) and they are constantly moving,
providing us the ability

[06:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=397s) to add tracking capabilities
into our solution.

[06:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=401s) The telemetry data comes
from fictitious sensors,

[06:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=404s) speed, acceleration,

[06:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=406s) torque, oil and fuel level,

[06:50](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=410s) things that cars have.

[06:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=411s) And all of this data fits
perfectly into monitoring

[06:54](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=414s) and adding a solution
that will be presented

[06:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=416s) not only to address the high scalability,

[06:59](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=419s) but to dig deep into the details
produced by each vehicle.

[07:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=423s) And all of that is part of a
simulation engine created by us

[07:07](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=427s) to consume millions of
requests per minute.

[07:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=430s) I'm going to pass it over to Rafael,

[07:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=432s) who's going to talk to
you about the solution.

[07:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=434s) - Thank you, Fernando.

[07:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=436s) To present the solution, we'd
like to start with a demo

[07:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=439s) and then we return back to the deck

[07:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=441s) to explain the architecture design,

[07:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=443s) and the logical flow
supporting the solution.

[07:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=447s) - This is our solution demo.

[07:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=449s) On the right side,

[07:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=449s) we have a simple web
application including a map.

[07:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=453s) On the left side, the incoming dashboard,

[07:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=455s) where we will see all information
regarding the vehicles.

[07:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=459s) This demo is prepared

[07:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=461s) not only to receive
data from real vehicles,

[07:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=464s) but also to simulate those
vehicles for testing protocols.

[07:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=468s) So let's say you have 20 trucks in a fleet

[07:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=471s) going from your exhibition centers

[07:54](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=474s) to dealer sites, for instance.

[07:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=476s) And, of course, you'd like to track them.

[07:59](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=479s) So let's include those vehicles here.

[08:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=483s) The vehicles, all right

[08:05](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=485s) The solution generates
a route for each vehicle

[08:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=488s) also including a geofencing area.

[08:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=490s) As an example for this demo, each geofence

[08:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=494s) will represent an area around
the distribution center

[08:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=497s) where the vehicle just left.

[08:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=499s) The vehicles are popping
up on the map right now

[08:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=502s) and sending data,

[08:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=503s) as you can see on the
monitoring dashboard.

[08:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=506s) Let's take a look closer at one vehicle

[08:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=509s) to see it moving on the map.

[08:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=511s) So let's pick one vehicle here.

[08:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=515s) We just need to zone in.

[08:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=519s) Okay, a little bit more.

[08:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=524s) Let's see more.

[08:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=528s) All right.

[08:50](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=530s) Okay, so the vehicle's running

[08:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=532s) and updating its position
on the map properly, right?

[08:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=536s) Although the routes are

[08:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=537s) dynamically generated by the solution,

[09:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=541s) the vehicle positions are real,

[09:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=543s) following the given route,
which enable us to receive

[09:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=546s) real latitude and longitude pairs

[09:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=549s) to make the simulation more
similar to the reality.

[09:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=554s) Let's zoom out here to see
more vehicles on the map.

[09:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=561s) All right, that is a good, that is good.

[09:24](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=564s) Okay, so looking at the
monitoring dashboard,

[09:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=567s) you can see the number
of vehicles running.

[09:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=570s) You can also see the
number of geofence events,

[09:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=573s) which means, in this case,
that all those 20 vehicles

[09:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=577s) left the distribution center area.

[09:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=581s) We also can see the
number of location events

[09:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=584s) and telemetry events that
we are receiving per minute.

[09:47](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=587s) Right?

[09:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=588s) So with these numbers, we
can say that you are saving

[09:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=593s) almost 3000 events per minute,

[09:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=596s) including location and telemetry events

[09:59](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=599s) for those 20 vehicles.

[10:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=603s) Below some critical information

[10:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=604s) we decided to monitor closely,

[10:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=606s) which includes a list of
the highest speed vehicles,

[10:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=609s) a list of the lowest fuel level vehicles,

[10:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=612s) and a list of the highest
oil temperature vehicles.

[10:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=616s) If you'd like to see more information

[10:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=619s) about any specific vehicle,

[10:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=622s) you can just click on the vehicle,

[10:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=625s) such as this one, for example,
with the highest speed.

[10:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=633s) And here you can see all metrics

[10:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=635s) about that specific vehicle in real time,

[10:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=637s) including its speed, oil
temperature, fuel level,

[10:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=641s) the positions within the
last minute, and so on.

[10:47](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=647s) Let's move back to the main dashboard.

[10:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=651s) Okay, so now imagine
that one of your vehicles

[10:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=655s) is in high risk

[10:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=657s) by running with an extremely
low fuel level, for instance.

[11:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=662s) In that case, we expect to be alerted

[11:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=666s) so we can take actions immediately.

[11:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=670s) So let's simulate that
and put the mobile phone

[11:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=673s) in the screen in order
to wait for the message.

[11:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=675s) So let's put a mobile phone here first.

[11:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=681s) All right.

[11:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=683s) Now, let's select one
vehicle here on the map.

[11:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=688s) Let's see, let's pick this one in London.

[11:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=694s) We selected this.

[11:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=695s) We can see the VIN number start with 9J9

[11:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=701s) and let's simulate the low fuel level.

[11:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=706s) Okay so,

[11:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=708s) as you can see, the vehicle pin

[11:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=711s) just changed its color to red.

[11:54](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=714s) So it represent a red flag in the map,

[11:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=717s) and also you can see the same information

[12:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=720s) in the lowest fuel level vehicles.

[12:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=722s) That specific vehicle is
showing with 1% of fuel level,

[12:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=729s) which is a high risk, right?

[12:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=732s) Regarding the text message,

[12:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=734s) in our mobile we just
received a text message

[12:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=739s) alerting about that high risk vehicle

[12:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=743s) with the VIN number, the
fuel level which is 1%,

[12:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=747s) and also the position for that vehicle.

[12:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=750s) Then you can open and click on this

[12:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=754s) and see the right
location of that vehicle.

[12:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=760s) All right, let's move back
to the dashboard here.

[12:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=764s) Okay, so we've tested this
solution with 20 vehicles

[12:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=769s) and we received about

[12:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=771s) 2,900,

[12:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=773s) 3000 events per minute.

[12:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=775s) But what if you have

[12:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=777s) 100,000 vehicles?

[13:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=780s) Let's onboard those on the map,

[13:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=784s) let's onboard 100,000 vehicles here.

[13:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=795s) You will see more and more vehicles

[13:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=797s) popping up on the map shortly.

[13:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=799s) And also, they did formation
on the monitoring dashboard.

[13:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=805s) Everything in scale tends
to be more complex, right?

[13:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=809s) You need to deal with
the underlying resources

[13:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=812s) for scalability and many other factors.

[13:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=815s) That's why building our resilient

[13:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=818s) and our scalable
architecture is important.

[13:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=820s) Doesn't matter if you
have just few vehicles

[13:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=824s) sending 3000 events per minute
or thousands of vehicles

[13:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=829s) sending 10 million events per minute,

[13:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=833s) you can build an architecture

[13:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=835s) that keeps up with your
growth and your new load.

[13:59](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=839s) So now, you can see that we
have almost 100,000 vehicles.

[14:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=844s) It's counting and we
are receiving now about

[14:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=848s) 20 million, 25 million events per minute.

[14:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=855s) So here we have a high throughput
solution that can receive

[14:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=861s) a large amount of events
each minute, right?

[14:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=865s) Yeah, so now there are 5
million events per minute.

[14:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=868s) Okay, so additionally to that,

[14:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=871s) it's also important to monitor

[14:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=872s) the underlying infrastructure
supporting the solution.

[14:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=875s) In this dashboard, we are
monitoring important metrics

[14:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=879s) for Lambda functions in this solution,

[14:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=881s) including errors, portals, service limits,

[14:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=885s) and any other issue that
can impact the solution.

[14:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=888s) And you can see with this graph here,

[14:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=892s) when we just launch 100,000 vehicles,

[14:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=895s) you can see this graph,
this peaking right here.

[15:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=900s) All right, so let's go
back to the main dashboard.

[15:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=904s) All right, all those geofence events,

[15:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=908s) we just received all of them.

[15:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=912s) Okay, so we now have
100,000 vehicles running,

[15:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=917s) about

[15:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=919s) 30 million events per minute.

[15:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=922s) Okay, so let's go back
to the presentation deck

[15:24](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=924s) to understand how the architect design

[15:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=927s) and the logical flow look like.

[15:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=931s) Okay, so let's walk through

[15:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=933s) the architectural design for the solution.

[15:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=936s) We'll dive deep into each specific flow

[15:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=938s) in the following slides,

[15:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=939s) including why we choose
each specific service,

[15:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=942s) but intention for now is to
provide you the big picture

[15:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=945s) and the vision of what we are using.

[15:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=948s) The fleet of simulated vehicles

[15:50](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=950s) send their telemetry and location data

[15:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=953s) over MQTT to AWS IoT Core.

[15:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=956s) Those messages are
filtered using IoT rules

[15:59](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=959s) and sent to different services,
depending on the case.

[16:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=962s) For example, the IoT rule is responsible

[16:05](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=965s) to capture all messages and store them

[16:07](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=967s) in a time series database
with Amazon Timestream,

[16:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=970s) by leveraging it's built-in integration.

[16:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=973s) So we don't need to write
additional code for that.

[16:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=977s) All the location messages
coming from the vehicles

[16:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=979s) are saved to a Lambda function

[16:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=981s) where two actions are performed.

[16:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=983s) First is a dual-facing validation

[16:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=986s) that checks if the vehicle
entered in or exited

[16:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=990s) a predefined area of interest or geofence,

[16:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=993s) which is one of the Amazon
Location Service features.

[16:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=997s) If so, it generates an
event in Amazon EventBridge

[16:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1001s) that triggers a Lambda
function responsible

[16:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1004s) to start that in a Timestream database.

[16:47](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1007s) The second action is to register
the new vehicle position

[16:50](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1010s) in AWS AppSync, which
will generate a notation

[16:54](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1014s) and store the new position
in a DynamoDB table.

[16:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1018s) That notation in AWS AppSync
is captured by the application,

[17:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1023s) the AWS Amplify, who will update

[17:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1026s) the vehicle position on the map.

[17:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1029s) An IoT rule is also being
used to filter critical events

[17:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1033s) that require an immediate attention,

[17:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1037s) such as a vehicle in high speed
or in any other high risk.

[17:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1043s) We filter those messages

[17:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1045s) to send over to another Lambda
function that we process

[17:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1048s) and notify whoever's needed

[17:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1050s) through Amazon Simple
Notification Service.

[17:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1054s) In terms of monitoring,

[17:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1055s) we are using Amazon Managed Grafana,

[17:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1058s) leveraging it's default
integration with both

[17:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1061s) Amazon Timestream service,

[17:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1062s) where we have now all data
about the vehicle's trip,

[17:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1066s) and also, Amazon CloudWatch,

[17:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1068s) where we follow some
important service metrics,

[17:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1071s) such as API throttling,
errors, and limits.

[17:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1075s) This architecture is fully serverless,

[17:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1078s) so we don't need to deal or manage

[18:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1080s) any virtual machine's operational system.

[18:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1083s) Now that you have a vision of
database services in scope,

[18:07](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1087s) let's talk about the security
aspects for the solution.

[18:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1094s) Secure is job zero, and will
always be our top priority.

[18:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1098s) In a typical off-premises security model,

[18:20](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1100s) customers are responsible
for the end-to-end security

[18:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1103s) and reliability in their
data centers, which includes

[18:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1107s) facilities, power, cooling,
hardware, and so on.

[18:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1111s) In AWS, we have a shared
responsibility model

[18:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1114s) with the customer, where
AWS manages and controls

[18:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1118s) the components from the
host operational system

[18:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1120s) and the virtualization layer down,

[18:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1122s) to the physical security of the facilities

[18:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1124s) in which the services operate.

[18:47](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1127s) And AWS customers are responsible

[18:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1129s) for building security applications.

[18:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1132s) The level of responsibility, however,

[18:54](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1134s) for each change depend on
the AWS services you choose

[18:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1138s) to build your solution.

[19:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1140s) If you choose infrastructure services

[19:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1142s) using virtual machines with
Amazon EC2, for example,

[19:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1146s) you are responsible to secure everything

[19:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1149s) from the traditional system layer

[19:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1151s) that will support your application,

[19:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1153s) which means that you should
think about security patches,

[19:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1156s) hardening, updates, OS,
firewall, antivirus solutions,

[19:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1161s) and so on.

[19:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1163s) On the other hand,

[19:24](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1164s) by using serverless services
as we are doing today,

[19:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1168s) AWS takes even more responsibility.

[19:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1171s) With that model, customers
don't need to deal

[19:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1175s) with the traditional system
layer or network components.

[19:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1179s) Our service architecture
provides infrastructure security

[19:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1182s) and network isolation, by design,

[19:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1184s) which will release you to
focus more on your business,

[19:47](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1187s) application, and innovation.

[19:50](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1190s) With this, we've quickly addressed one of

[19:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1193s) the security challenges that
Fernando mentioned before,

[19:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1196s) but you still have your
portion of responsibility

[19:59](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1199s) with security, which include

[20:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1201s) developing secure application code

[20:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1204s) validated with automated CI/CD process,

[20:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1206s) encrypt your data

[20:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1208s) and manage the access and
authorization policies,

[20:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1211s) following the least privileged principle.

[20:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1214s) Talking about authentication
and authorization,

[20:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1217s) AWS provides a number of
different authentication method

[20:20](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1220s) to support your environments.

[20:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1223s) For your IoT devices, you
can use client certificates,

[20:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1228s) AWS IAM, or

[20:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1230s) Amazon Cognito.

[20:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1232s) Once the data achieves AWS IoT,

[20:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1234s) the permissions among
services are provided

[20:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1237s) by IAM roles and policies.

[20:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1239s) Some carriers use mobile
device to track vehicle.

[20:43](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1243s) So if that is your case, probably you will

[20:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1246s) prefer to have HTTPS end
points to send your data,

[20:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1251s) and authentication method

[20:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1252s) will follow your connection portal.

[20:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1256s) To authenticate to Amazon Managed Grafana,

[20:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1258s) we are using AWS Single Sign-On

[21:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1260s) and for the web application,
we are using Amazon Cognito.

[21:05](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1265s) We think, at AWS,

[21:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1266s) you manage the privacy
controls of your data,

[21:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1269s) control how your data is used,

[21:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1271s) who has access to it,
and how it is encrypted.

[21:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1275s) We make it easy to encrypt
data in transit and at rest

[21:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1278s) using keys, either managed by AWS

[21:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1282s) or fully-managed by you.

[21:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1285s) You can build your own keys

[21:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1287s) that were generated and
managed outside of the AWS.

[21:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1292s) AWS Database and Storage Services

[21:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1294s) provide encryption at rest,
which for the solution

[21:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1298s) includes not only Amazon Timestream

[21:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1300s) and Amazon DynamoDB databases,

[21:43](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1303s) but also geofences collection
with Amazon location

[21:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1306s) and environmental variables
and deployment packages

[21:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1309s) with AWS London.

[21:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1311s) We easily keep all data in the
solution encrypted at rest.

[21:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1316s) AWS IoT message broker
encrypts all communication

[21:59](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1319s) while you're in transit,

[22:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1321s) using TLS 1.2,

[22:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1323s) including the connection
between the devices

[22:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1326s) and the AWS IoT.

[22:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1328s) All AWS services use TLS 1.2 and beyond

[22:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1332s) to communicate to each other,

[22:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1334s) unless otherwise specified,

[22:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1336s) which means that all data in this solution

[22:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1339s) are also encrypted in transit, by default.

[22:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1343s) Still, in data protection
and data privacy area

[22:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1345s) it's important to remember to avoid using

[22:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1348s) personal identifiable information

[22:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1350s) to name your resources.

[22:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1352s) For example, don't use any mail address,

[22:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1354s) a personal name or document number

[22:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1357s) as part of your IoT topic

[22:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1359s) or to name your geofence collection.

[22:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1362s) You don't want an IoT topic
named with the driver's name,

[22:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1366s) or a geofence collection
with the actual address.

[22:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1371s) So now that you had a good idea of how

[22:54](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1374s) the architecture looks like
and its security aspects,

[22:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1378s) let's dive deep into each logical flow.

[23:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1381s) Everything starts with the vehicles,

[23:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1383s) or simulated trucks, in our case.

[23:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1386s) In a real world scenario,

[23:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1388s) you can equip your vehicles
with sensors or devices

[23:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1391s) that collect metrics continuously.

[23:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1393s) For example, using

[23:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1395s) OBDII devices to provide
the real time data,

[23:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1398s) in addition to a series of
diagnostic trouble codes.

[23:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1402s) You can connect your IoT devices

[23:24](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1404s) to our cloud-based service, AWS IoT Core,

[23:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1408s) which forms the backbone
for IoT deployments,

[23:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1411s) to securely connect all your devices

[23:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1413s) and handle their data at scale.

[23:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1417s) You can not only ingest IoT data to AWS,

[23:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1419s) but also keep a communication
among your devices

[23:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1422s) and send back information as needed.

[23:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1425s) In our solution, we are
using MQTT as the protocol

[23:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1429s) to send telemetry data
from the vehicle devices to

[23:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1432s) AWS IoT topic or a message
broker with AWS IoT Core.

[23:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1438s) All messages go to a topic

[24:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1440s) that includes the vehicle VIN,

[24:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1442s) which we are using as the device ID.

[24:05](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1445s) MQTT is a lightweight and widely-adopted

[24:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1448s) messaging protocol that is
designed for constrained devices,

[24:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1452s) but AWS IoT Core also supports

[24:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1455s) MQTT over WebSocket Secure,
HTTPS, and Loader One protocols.

[24:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1461s) Our soft limit to be aware of

[24:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1463s) is the inbound virtual requests
per second, per account,

[24:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1466s) priority for message broker,

[24:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1468s) which is currently 20,000
per second in most regions.

[24:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1472s) It's manageable.

[24:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1473s) You can work with AWS
support to increase this,

[24:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1477s) based on your use case.

[24:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1479s) Check the actual limit for
the region you selected.

[24:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1485s) Each vehicle sends a number of
different metrics per second,

[24:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1489s) including location, with the
pair of latitude and longitude,

[24:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1493s) acceleration,

[24:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1495s) fuel level,

[24:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1497s) speed,

[24:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1498s) oil temperature,

[25:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1500s) engine speed, torque and
transmission, odometer,

[25:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1504s) and other five metrics,

[25:05](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1505s) but it could be much more.

[25:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1508s) In a real world scenario, you
will probably prefer to send

[25:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1512s) all metrics at once,

[25:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1514s) at a more spaced frequency
such as every five second,

[25:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1519s) almost a minute,

[25:20](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1520s) or even in a few minutes,

[25:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1523s) depending on your environments,

[25:24](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1524s) budget and your appetite for your time.

[25:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1528s) You can even implement the name key method

[25:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1530s) that will change the
frequency to send metrics

[25:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1533s) depends on the actual vehicle speed.

[25:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1536s) So if your vehicle is too fast,

[25:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1538s) probably you would like to
send your metrics more often,

[25:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1542s) almost in a fraction
of second, for example.

[25:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1545s) If a vehicle is too slow,

[25:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1546s) you'll be okay by sending
metrics almost in a few minutes.

[25:50](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1550s) A good idea here would it be embed

[25:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1552s) an IoT gateway with AWS IoT
Greengrass in each vehicle,

[25:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1557s) that would not only process the data

[25:59](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1559s) and take automated actions locally,

[26:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1561s) based on the code you deployed
from your AWS environment,

[26:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1564s) but also handle eventual
connectivity issues,

[26:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1568s) keeping this solution
working, even if the vehicle

[26:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1572s) is still probably
disconnected from the AWS IoT.

[26:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1576s) It also can preprocess data

[26:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1578s) and group all metrics before
sending it over to AWS IoT.

[26:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1582s) You could also implement
a machine learning model

[26:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1585s) that keep you running at the edge.

[26:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1586s) In other words, embedded in your vehicle.

[26:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1589s) One idea could be implementing
a machine learning module

[26:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1593s) to alert the driver
about the optimum moment

[26:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1596s) to refill the tank, for example.

[26:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1600s) If you just need to ingest
data from IoT devices to AWS,

[26:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1605s) with no reverse communication

[26:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1606s) or communication among devices,

[26:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1608s) you can consider to use IoT Basic Ingest,

[26:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1611s) to reduce costs and to manage better

[26:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1613s) your quota for the service.

[26:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1616s) With Basic Ingest, you send
your messages directly to the

[27:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1620s) IoT rule that we will
explain in the next slide,

[27:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1623s) bypassing the traditional IoT topic.

[27:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1628s) Once the message reach the
IoT topic in the AWT IoT Core,

[27:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1633s) you can easily filter
messages and directed them

[27:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1636s) to the appropriate target
by using IoT rules.

[27:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1639s) In AWS IoT, rules are defined
using a SQL-like syntax.

[27:24](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1644s) First example, here, we are filtering

[27:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1646s) all location messages
related to all vehicles.

[27:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1650s) We are picking the vehicle VIN,

[27:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1652s) latitude, longitude, and time stamp,

[27:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1654s) and send them to AWS Lambda function,

[27:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1657s) where, in that Lambda function,

[27:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1659s) we are using Python to
update vehicle position

[27:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1662s) and validate geofence device

[27:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1664s) that Fernando will
explain in a few slides.

[27:47](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1667s) In the second example, we are
filtering a critical event

[27:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1671s) directly from the IoT topic

[27:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1672s) to notify operators as soon as possible.

[27:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1675s) In this case, we can easily track

[27:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1677s) if a vehicle is running with
a critical oil temperature,

[28:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1681s) by using that simple SQL-like syntax.

[28:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1684s) Third example here, we are
getting all the messages

[28:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1689s) to store them in a Timestream database.

[28:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1692s) You just need to include the
SQL statement to do that.

[28:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1695s) Select the Timestream database
and the table as a target.

[28:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1699s) And now you will have all vehicles data

[28:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1702s) in the Amazon Timestream.

[28:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1705s) We chose Amazon Timestream
because it's a fast, scalable,

[28:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1709s) fully-managing, purpose-built
time series database

[28:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1712s) that makes easy to store and analyze

[28:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1715s) trillions of time series
data points per day.

[28:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1719s) It manages the life cycle
of time series data,

[28:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1722s) by keeping recent data in memory
and moving historical data

[28:47](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1727s) to a cost-optimized storage tier,

[28:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1729s) based upon the user-defined policies.

[28:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1732s) It has built-in time
series analytics functions,

[28:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1735s) helping you identify trends and patterns

[28:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1738s) in your data, in near-real time.

[29:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1742s) It's serverless and
automatically scale up or down

[29:05](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1745s) to adjust capacity and performance.

[29:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1748s) Because you don't need to manage

[29:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1749s) the underlying infrastructure,

[29:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1751s) you can focus on optimizing
and building your applications.

[29:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1755s) You can easily plug your
monitoring system to Timestream,

[29:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1758s) such as Amazon Managed Grafana.

[29:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1762s) Amazon Managed Grafana is
a fully-managed and secure

[29:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1765s) data visualization
service that you can use

[29:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1768s) for instantly query,
correlate, and visualize

[29:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1771s) perishable metrics, logs, and
traces from multiple sources.

[29:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1777s) The service makes it
easy to deploy, operate,

[29:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1780s) and scale Grafana,

[29:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1781s) which is a widely deployed
data visualization tool

[29:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1784s) that is popular for its
extensible data support.

[29:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1789s) It's integrated with AWS data sources

[29:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1792s) that collect operational data,
including Amazon CloudWatch,

[29:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1796s) Amazon Loki search service,
Amazon Timestream, and others.

[30:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1802s) For user authentication and authorization,

[30:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1804s) Amazon Managed Grafana can integrate

[30:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1806s) with identity providers
that support SAML 2,

[30:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1810s) and also can integrate
with AWS Single Sign-On.

[30:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1815s) We are using Amazon Managed Grafana

[30:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1817s) as our single operational
monitoring for all data.

[30:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1821s) We can easily create monitoring

[30:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1823s) by leveraging its integration
with Amazon Timestream,

[30:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1826s) that supports a rich SQL-like language.

[30:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1829s) So we can monitor what you
saw in the demo and much more.

[30:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1834s) This is an example of a query
from Grafana to Timestream,

[30:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1839s) to list the top 100
vehicles in high speed.

[30:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1842s) We are selecting vehicles VINs

[30:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1844s) and their average speeds
in a given timeframe,

[30:47](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1847s) limiting up to 100 and
reverse ordering by speed.

[30:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1852s) So we can show first the
vehicles in highest speed.

[30:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1856s) In green, other labels Grafana provide you

[30:59](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1859s) to make it simpler to create queries.

[31:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1862s) So you don't need to enter
your default database and table

[31:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1866s) every time and can use
the same time filter

[31:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1869s) you defined for your entire dashboard.

[31:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1874s) In addition to vehicle monitoring,

[31:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1876s) we can include AWS services monitoring

[31:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1879s) with the Amazon CloudWatch integration.

[31:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1882s) So we can follow eventual API throttling,

[31:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1885s) any errors while processing events,

[31:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1888s) service limits, and others.

[31:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1891s) As we mentioned before,

[31:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1892s) there are some critical events

[31:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1894s) that we may want to notify
operators immediately.

[31:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1897s) For that, you can filter messages

[31:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1899s) directly from the IoT
topic using IoT rules

[31:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1902s) and use an AWS Lambda as target

[31:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1905s) to process the event and
send it over to Amazon SNS

[31:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1909s) that will notify all the
subscribers for that kind of event,

[31:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1912s) by using email, mobile
text, push notifications,

[31:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1916s) PagerDuty, or any other destination
supported by Amazon SNS.

[32:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1922s) In that way, important events
reach to the right people

[32:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1926s) as quick as the solution
receives them, in real time.

[32:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1930s) Now, I hand over, back to Fernando.

[32:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1934s) - Another very important piece

[32:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1935s) of every asset tracking solution

[32:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1938s) is the ability to notify
interested parties

[32:20](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1940s) when assets are inside areas of interest.

[32:24](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1944s) With Amazon Location Service's
geofence collections,

[32:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1947s) you can automatically
evaluate a vehicle's position

[32:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1951s) against all of the geofences
inside that collection.

[32:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1955s) It all starts with the
incoming data on AWS IoT Core,

[32:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1958s) as Raphael explained.

[32:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1960s) The arriving data is
processed by the topic rule

[32:43](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1963s) and sent to AWS Lambda,

[32:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1965s) where the geofence lookup is initiated.

[32:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1968s) The request contains the vehicle VIN,

[32:50](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1970s) which is the asset identifier,

[32:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1972s) and the current positioning,
latitude and longitude format.

[32:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1976s) Amazon Location evaluates this position

[32:59](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1979s) against all of the
geofences in the collection

[33:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1981s) to determine if an asset is
entering or exiting an area.

[33:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1986s) If any of these events occur,

[33:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1988s) this event is sent to Amazon EventBridge,

[33:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1991s) where a Lambda function is
triggered, and the action

[33:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1994s) is saved on Timestream
for monitoring purposes.

[33:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=1997s) This event contains the asset information,

[33:20](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2000s) the geofence breached, the event itself,

[33:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2002s) either enter or exit,

[33:24](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2004s) and the timestamp associated to the event.

[33:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2007s) With all of these events, you
can calculate for how long

[33:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2009s) an asset stayed within a certain area,

[33:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2012s) if they are outside an allowable location,

[33:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2015s) or even notify interested
bodies of asset movement.

[33:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2021s) You'd also want a real-time
visualization representation

[33:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2024s) of where your assets are.

[33:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2026s) With AWS Amplify, you can leverage AppSync

[33:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2029s) to create subscriptions that will trigger

[33:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2031s) front end updates in every
vehicle movement that occurs.

[33:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2036s) The incoming data is
processed by AWS IoT Core,

[34:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2040s) and the Lambda function
sends a mutation request

[34:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2043s) to AWS AppSync,

[34:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2044s) which is our GraphQL serverless solution.

[34:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2048s) This mutation contains vehicle VIN,

[34:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2051s) and the current location set.

[34:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2054s) AppSync has two responsibilities here.

[34:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2056s) First one,

[34:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2057s) store the vehicles last
position on Amazon DynamoDB,

[34:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2062s) one of our NoSQL databases, famous for its

[34:24](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2064s) single digit millisecond
performance, at any scale.

[34:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2069s) And also, AppSync is responsible

[34:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2071s) for triggering a front
end update on our map,

[34:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2073s) as you saw in the demo.

[34:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2075s) So every time a vehicle moves,
you see represented on a map.

[34:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2080s) Now we have been talking about storing

[34:43](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2083s) a lot of location data in the solution,

[34:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2085s) and we need to start
thinking about good practices

[34:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2088s) that we can implement
to avoid storing data

[34:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2091s) that we do not really need,

[34:54](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2094s) not only from a data volume perspective,

[34:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2096s) but also from a security
and privacy perspective.

[35:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2100s) You can see here, from
a location perspective,

[35:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2102s) how we can broaden an area

[35:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2104s) to make coordinates more
general and less precise

[35:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2108s) by just removing a decimal place.

[35:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2111s) By rounding up, we can
aggregate all assets

[35:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2113s) within a radius of a position.

[35:16](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2116s) One decimal place, for
example, is broad enough

[35:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2118s) to aggregate all of the
assets within a city.

[35:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2121s) That's about 11.1
kilometers or seven miles.

[35:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2125s) As we add a decimal place,
we get more precise.

[35:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2128s) At two decimal places,
we can aggregate assets

[35:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2130s) within a town of 1.11 kilometer radius,

[35:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2133s) or three quarters of a mile.

[35:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2135s) Three decimals can be a
facility or a warehouse,

[35:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2138s) four decimals could be the lane of a road,

[35:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2141s) and five decimals would give us a car,

[35:43](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2143s) at 1.11 meters or 3.5 feet.

[35:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2146s) Amazon Location Service have the ability

[35:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2148s) to store location data
up to six decimal places,

[35:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2151s) which would give you

[35:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2152s) the position of a cup
of coffee, for example.

[35:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2155s) However, you really need
a very accurate GPS device

[35:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2158s) to collect such an accurate position.

[36:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2163s) And when working with sensitive
data of asset locations,

[36:05](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2165s) we should design an architecture

[36:07](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2167s) that only takes what we need

[36:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2168s) to respect the consumer's privacy.

[36:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2171s) We're also improving performance

[36:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2173s) by minimizing lookup queries,

[36:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2175s) and then saving costs by
removing query redundancy.

[36:20](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2180s) We can refer to this as
least privileged precision,

[36:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2183s) to store and handle only the
level of location precision

[36:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2187s) that our use case needs.

[36:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2189s) Moreover, we can generate
cache-friendly identifier

[36:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2193s) using a geocoding system like geohashing.

[36:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2196s) There are a few open
source ones out there,

[36:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2198s) but Geohash is one that
is in the public domain.

[36:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2205s) And to bring this back to our use case,

[36:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2206s) a vessel tracking application

[36:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2208s) would want to localize vessels
positioned in the ocean.

[36:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2211s) So three decimals of precision

[36:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2213s) would suit the requirements really well.

[36:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2216s) For a vehicle's exact
location on the road, though,

[36:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2218s) you may want to add more
precision to your query

[37:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2221s) to identify where the car is.

[37:05](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2225s) And these are the features

[37:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2226s) that Amazon Location
provides to you today.

[37:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2229s) With maps, you can add
a visualization layer

[37:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2231s) into any application.

[37:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2233s) Places gives you searching capabilities,

[37:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2235s) geocoding and reverse geocoding.

[37:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2238s) Routes will give you information

[37:20](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2240s) on how to get from point A to point B.

[37:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2243s) All of these features are backed

[37:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2245s) by two trusted AWS partners,

[37:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2247s) huge players in the geospatial market,

[37:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2250s) Esri and HERE Technologies.

[37:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2252s) Their data currently supports

[37:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2253s) millions of applications on a daily basis.

[37:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2258s) From a privacy standpoint,

[37:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2259s) all queries that are made to Esri and HERE

[37:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2262s) are anonymized, and you can
choose which data provider

[37:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2265s) to use, with one single
API to consume from.

[37:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2269s) So you can basically change providers

[37:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2271s) without changing source code,

[37:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2273s) or creating new agreements
with new companies

[37:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2276s) and not even generating new credentials.

[37:59](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2279s) All you need is an AWS account.

[38:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2282s) There are also no penalties

[38:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2283s) if you stop using the service.

[38:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2286s) Start and stop whenever you want.

[38:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2289s) You also get data ownership

[38:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2291s) on geocoding and reverse
geocoding results,

[38:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2294s) being able to store them

[38:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2295s) in your own storage services or databases.

[38:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2299s) Trackers will let you send and retrieve

[38:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2301s) real-time batch geolocation information

[38:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2303s) for vehicles, mobile
devices, and any other assets

[38:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2308s) that can actually provide
their location information.

[38:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2313s) Amazon Location Service
this year introduced

[38:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2315s) Positions Filtering as
a new option to trackers

[38:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2318s) that really enables cost reduction

[38:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2320s) and reduces jitter effects

[38:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2322s) from inaccurate device location updates,

[38:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2324s) along with the addition of true
position filtering options.

[38:49](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2329s) And lastly, you can use
geofences in a solution like this

[38:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2332s) to identify areas that are interesting

[38:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2335s) to this particular use case.

[38:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2338s) And that's what geofences are,

[39:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2340s) areas of interest were actions related

[39:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2342s) to geolocations can occur.

[39:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2344s) Geofence collections on Amazon Location

[39:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2346s) provides the capability of detecting

[39:09](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2349s) enter and exit events on these areas.

[39:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2353s) By providing the current
position of a vehicle,

[39:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2355s) these collections are
automatically evaluated

[39:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2357s) against all the geofences
that they have stored.

[39:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2361s) Once it is detected that

[39:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2363s) a vehicle has entered
one of those geofences,

[39:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2366s) an enter event is posted
to Amazon EventBridge

[39:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2369s) for further processing.

[39:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2372s) The location evaluation
can happen via an API call

[39:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2375s) or by linking trackers and
geofencing collections together,

[39:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2379s) really freeing you from
calling the API directly.

[39:43](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2383s) This is great from an automation
and integration standpoint.

[39:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2388s) Finally, tracker and geo-fencing data

[39:50](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2390s) never leaves your AWS account.

[39:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2393s) That data is encrypted by
default, at rest and in transit,

[39:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2396s) and you can even use your own
keys to encrypt it, as well.

[40:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2402s) Now that you understood
to the building blocks

[40:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2404s) that we're using to guarantee security,

[40:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2406s) performance efficiency,

[40:07](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2407s) and operational excellence
in this solution,

[40:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2410s) let's talk about a very
important piece of every solution

[40:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2414s) that needs to handle events as
close to reality as possible,

[40:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2418s) simulating.

[40:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2422s) Raphael showed you before during our demo,

[40:24](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2424s) how this application scales.

[40:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2426s) When you start from 10 or 20 cars,

[40:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2429s) things are very easy
to manage and control.

[40:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2431s) Not a lot of compute power
is needed at this point

[40:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2434s) to maintain this very
small amount of data.

[40:40](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2440s) Scaling to 100,000 vehicles,
however, can be daunting.

[40:43](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2443s) How can we test with 100,000
vehicles instead of 10?

[40:47](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2447s) Let me show you.

[40:50](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2450s) First of all, we created
a simulation engine.

[40:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2453s) That simulation engine relies

[40:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2455s) on an AWS Amplify hosted
front end, built in ReactJS.

[41:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2460s) This front end communicates
with AWS via REST APIs,

[41:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2464s) that basically create a
number of Lambda functions

[41:07](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2467s) that handles the vehicle
simulation processes.

[41:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2471s) The rest of the architecture
is virtually the same,

[41:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2473s) as the Lambda functions are now the ones

[41:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2475s) communicating to AWS IoT Core.

[41:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2481s) If you were managing 10
cars, you could easily

[41:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2483s) spin up 10 Lambda functions
to represent them.

[41:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2487s) By scaling to 100,000 cars, however,

[41:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2490s) if you keep the same process,

[41:32](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2492s) you will face issues like

[41:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2495s) timeouts,

[41:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2496s) concurrency issues,

[41:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2498s) and also service limits.

[41:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2502s) On average, we were able to invoke

[41:44](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2504s) 17.5 Lambda functions each second,

[41:46](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2506s) and we can try to use a fan out pattern.

[41:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2508s) So instead of invoking all
of them in a single loop,

[41:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2511s) we can create 100 batches that will create

[41:54](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2514s) Lambda functions that will
manage 10 vehicles each,

[41:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2517s) which gives us 100K in
total, which is what we need.

[42:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2521s) And we can also have an
intermediary Lambda function

[42:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2524s) that will trigger individual
workers for each vehicle.

[42:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2528s) We have a scaler that reads

[42:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2530s) the configuration of all
tasks that we have to execute

[42:13](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2533s) and divides them into
batches of 100 Lambdas,

[42:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2537s) invoking trigger Lambda functions, right?

[42:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2542s) We'll pass one batch to each of them.

[42:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2545s) In our case,

[42:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2546s) we'll have to invoke it 100
times with 100 Lambdas each.

[42:30](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2550s) Trigger function receives
a batch of requests

[42:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2554s) and invokes the vehicle's
function for each of them.

[42:37](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2557s) Since each of the triggers
will have to invoke

[42:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2559s) only up to 100 workers,

[42:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2562s) it should take them five to 10 seconds.

[42:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2565s) Each vehicle function will
be responsible to handle

[42:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2568s) only 10 vehicles, so we won't
be blocking other processes.

[42:52](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2572s) You could play with those numbers

[42:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2573s) to achieve the level
desired by your solution.

[42:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2576s) But from a cost perspective,

[42:58](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2578s) you can even reduce the
memory and timeout limits

[43:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2581s) for the Lambda functions now.

[43:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2584s) Make sure that you're requesting
any service limit increases

[43:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2588s) that are needed on your AWS account,

[43:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2590s) to handle a solution like this.

[43:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2594s) And when you're
architecting for the cloud,

[43:15](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2595s) you need to keep API throttling in mind,

[43:17](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2597s) particularly the types of calls

[43:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2599s) and the frequency in
which they are called.

[43:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2602s) When the allotted rate limit
for an API call is exceeded,

[43:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2605s) you receive an error response

[43:27](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2607s) and the call will be throttled.

[43:29](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2609s) Excessive API throttling
can result in job failure,

[43:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2613s) delays,

[43:34](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2614s) and operational inefficiencies,

[43:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2616s) that will ultimately
cost your organization

[43:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2619s) time and money, of course.

[43:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2622s) Retry logics are automatically implemented

[43:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2625s) when you leverage the AWS SDK,
so maybe do that (laughs).

[43:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2628s) But you can do it on your own, as well,

[43:50](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2630s) as the pseudocode on the right suggests.

[43:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2633s) In addition to simple retries,

[43:55](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2635s) each AWS SDK implements an
exponential backoff algorithm

[44:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2640s) for best flow control.

[44:02](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2642s) The idea behind exponential
backoff is to use

[44:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2644s) progressively longer waits between retries

[44:07](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2647s) for consecutive error responses.

[44:10](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2650s) And retries can be very ineffective

[44:12](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2652s) if all clients retry at the same time.

[44:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2654s) To avoid this problem, we employ jitter,

[44:18](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2658s) a random amount of time before
making or retrying to request

[44:22](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2662s) to help prevent large bursts,

[44:23](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2663s) by spreading out the arrival rate.

[44:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2666s) Most exponential back office algorithms

[44:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2668s) already use jitter to prevent
successful collisions.

[44:35](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2675s) The last piece of our simulation engine

[44:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2676s) is the dynamic route creation process.

[44:39](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2679s) When we scale our vehicles,

[44:41](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2681s) our trigger Lambdas generate routes,

[44:43](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2683s) based on origin and destination
points stored on DynamoDB.

[44:48](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2688s) They call Amazon Location
to calculate the routes

[44:51](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2691s) and store all the polylines in memory,

[44:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2693s) which are used to mimic the
vehicle driving process,

[44:57](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2697s) as you saw it on the
demo that Rafael showed.

[45:00](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2700s) We also pick a random point of the route

[45:04](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2704s) that represents an area of interest

[45:06](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2706s) and create a dynamic geofence
with a 300 meter radius,

[45:11](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2711s) so whenever the vehicle
enters or leaves an area,

[45:14](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2714s) a geofence event is presented
on Grafana for visualization.

[45:19](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2719s) And this is our solution.

[45:21](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2721s) Well, if you want to
build something similar,

[45:25](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2725s) a very good way

[45:26](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2726s) to start testing your
asset tracking solution

[45:28](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2728s) is by leveraging AWS IoT Device Simulator.

[45:31](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2731s) It's a one-click deployment process

[45:33](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2733s) that leverages AWS
CloudFormation templates

[45:36](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2736s) to deploy the solution for you,

[45:38](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2738s) in your AWS account, in minutes.

[45:42](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2742s) With IoT Device Simulator,

[45:43](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2743s) you can not only simulate vehicles,

[45:45](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2745s) but also simulate
different types of devices

[45:47](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2747s) with your own desired metrics.

[45:50](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2750s) It creates an entry
point with AWS IoT Core

[45:53](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2753s) that you can leverage to
onboard your own data,

[45:56](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2756s) like we did in the demo.

[46:01](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2761s) And that's all we have for today.

[46:03](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2763s) We'd like to thank you for your presence.

[46:05](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2765s) Thank you so much.

[46:08](https://www.youtube.com/watch?v=G8Rkuu6X-_8&t=2768s) (chill beat music)

