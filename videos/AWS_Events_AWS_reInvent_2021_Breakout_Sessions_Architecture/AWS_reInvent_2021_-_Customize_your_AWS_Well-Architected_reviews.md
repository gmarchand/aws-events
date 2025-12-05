# AWS re:Invent 2021 - Customize your AWS Well-Architected reviews

[Video Link](https://www.youtube.com/watch?v=BsEd_Ue_0TQ)

## Description

Customize your AWS Well-Architected reviews with best practices and technology requirements for your organization to evaluate risk and drive improvement in your workloads.

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK
 
Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

Right, thank you so much for coming everybody. Appreciate you taking the time, Today, we are going to be talking about customizing your Well-Architected Review. I'm Samir Kopal, I lead the product and engineering teams for Well-Architected. And I'm Ilana Greenberg, the product manager for Well-Architected. Just to understand the crowd, how many of you are aware of Well-Architected as a framework or the tool or have used it? That's great, that's a great mix here. So today we are going to cover, we'll talk about a little bit about a history of Well-Architected, how it's evolved, where it is today. And then we're going to talk about this really cool feature that we launched yesterday called custom lenses. And we want to talk about what is the problem that we are addressing with that. We're going to talk about an overview of what the feature is, and then we are going to go do a deep dive on how to actually use it in the tool. And we have a customer use case, we'll go through that, and I promise I'll leave time in the end for any questions you guys have. All right, so what is Well-Architected? A little bit of a lesson in history. So Well-Architected started when we had a popular service, have an outage back in 2012, and a lot of our customers were impacted. And we recognize that there's some customers who didn't get impacted. And the reason for that was they built in resiliency, reliability into their architecture. And the thinking then was how do we take this learning and share it with everybody? How do you make sure that we have customers that work with us follow the same best practices? And fast forward a few years, we had the Well-Architected Framework with four pillars, security, performance, reliability, and cost optimization. And we continued to evolve on that. So we use that internally, we use that with our customers, we got feedback, we did tens and thousands of reviews to figure out what works, what doesn't. And when we realized that, we recognized one aspect was is we need a process that weaves architecture into your organizational structure. And that was the birth of the fifth pillar, which was operational excellence. Operational excellence brings together the process that allows you to follow these best practices. So the three elements to Well-Architected, one is the Well-Architected Framework. It's available as a white paper. The Well-Architected Tool that revolves around the Well-Architected Framework. So it adds the pillars, the questions, the best practices, all of that is in the Well-Architected Tool. And that allows you to measure and improve your workload health in a very structured, consistent way across all your workloads. When I say, workloads, a workload is just a collection of resources. It could be an application, it could be a platform, it could be a service, it could be a single Redshift Cluster, whatever you wanna call it. But a workload is what you're evaluating. And then there is the improvement plan. The improvement plan is, well, I know what my risks are, how do I mitigate them? What do I do? Where do I go? What's the best practice? So that's the improvement plan around Well-Architected. So these are the three elements. Now let's talk a little bit about why it is important to do a review. I'll give you an example of when we launched the Well-Architected Tool back in 2018 at re:Invent exactly three years ago. And I was the software engineering manager back then, running the service. I read the white paper, I was aware we had subject matter experts on the team. So I was well aware of what Well-Architected is, and best practices, recommendations, things like that. But when I formally sat down and did the review for the service itself, one of the things I realized is it's a conversation starter, there are things that you don't think of upfront, right? And when you start doing the review, that's where you start having those conversations. An example would be, how are we going to manage if there is an incident running on game day? How are we going to know what's going to happen? Are we gonna update our runbooks? We've not launched, it's not in production. So how do we do that? So those things that you start thinking of. Typically, the world was where, hey, it's post production, if you have an incident, we have someone who's on call, they'll take care of it. But how can you optimize those things? And that is what I learned is where you can identify these risks early. It has that conversation, you can identify those risks early, you can start planning for those risks. The other thing, how many of you here have been in a situation where you're looking at an architecture or you're looking at a design or code and say, well, why did we make this decision? It happens all the time. And then you look back and say, well, I need to go back to some Wiki pages or some internal documentation, or I need to go in and follow some email threads. Or the person who did this is no longer with the organization. Very common, right? And there is no structured way to document. It's scattered, it's hard to find, but with Well-Architected, the tool gives you the ability to document those decisions. It gives you the ability to write why you made that trade off, cost and performance. Hey, we made this decision at this point for this very reason and that's in there,. So it's there, you can go look at the workload, you can go look at why it is. So it gives you that document, the decisions and the trade-offs. And then comes the part where you start addressing those risks that you've identified. So you're going to start looking at, well, now we know we have five security risks, three operational excellence risks, and you start improving the health of your workload. Now you might prioritize some things differently. You might look at it and say, well, this is an internal tool, cost is more important, it's behind a firewall. Security is probably less important to me. Or it could be the other way where it's like, I don't care about cost, I need extremely high availability, high performance systems. So you can start prioritizing and improving the health of your workload. It's very critical to keep doing that. And then the last part of this is how do you actually go ahead and implement continuous improvement into your processes? A lot of times when we do code deploys, we look at it and say, did I run my integration test? Did I on the unit test? What's that coverage looking like? So you're looking at your code consistently to look for improving your code quality. A lot of times we miss out on looking at architectural risks. I went from being multi-AZ To Single-AZ in this deployment. It's a massive risk for reliability. So you started looking at that and it helps you do that. Because now when you make a change, you can say, run a Well-Architected review, let's see whether we increase the number of risks we had, or did we decrease the number of risks that we had. So that's why it becomes critical to have those reviews. And it becomes a continuous improvement process for you to do. Now why we need to customize it. So we understand with Well-Architected, that Well-Architected is a general framework, it's a generic framework that allows you to learn measures, improve your workload, but it doesn't tailor it to your specific needs. You're looking for compliance best practices in there. You're looking for finance best practices in there. A lot of big enterprises have Cloud Center of Excellence teams that will go ahead and have a whole lot of best practices that they've built over years of experience. Customizing the review will allow you to do that. So custom lenses, which was launched yesterday, allows you to go ahead and add your own best practices. And we'll get into details of how that looks, but it allows you to incorporate those organizational best practices into a single place. That brings me to my next point. Today, a lot of these best practices are scattered. There are tools that will do security best practices, that are tools that will do performance best practices, and then you have Well-Architected. All of these things you have to manage in different places. And when you're starting to do that, it's hard to prioritize, it's hard to look at it and say, well, which one do I pick? But if you have a central place where you're looking at all your workloads, and you're looking at all the risks that you have, and you're trying to then prioritize, it becomes a lot easier because you have a bigger picture there. The same thing with workloads, you're not looking at individual workloads, you're looking at a portfolio. So all workloads within that account, now you can also cross prioritize across your workloads to say, well, if I fix these five security issues that I have, it affects 15 workloads, it's a big change. And then as Well-Architected evolved. So Well-Architected went, as I said, from four pillars to five pillars, from 40 questions to 50 questions. So that kept evolving over time because we kept learning new things. And we understand that as our customers, you learn new things all the time. It could be an outcome of an incident that you had. It could be a change in direction where we're moving from data centers to the cloud. We need to do things differently. We need to follow different best practices. It could be a finance manager comes in and says, well, this is the budget that you need to live in. So with all of that, you need to be able to update your best practices. So custom lens is going to give you that flexibility, it's going to give you the ability to not just create, but you can now update those as you learn more, as you go, you're going to learn a lot more about these things. And with that, I'll hand it over to Ilana to walk you guys through what custom lenses are. Great, thanks Samir. So what is a custom lens? So an important thing to note about a custom lens is that it's not meant to replace the Well-Architected Framework. It's really there to act as an overlay to give you that opportunity to add in your own internal and organizational best practices as Samir was mentioning. So we'll get into what custom lenses actually look like. But at a high level, you're able to create your own pillars, questions, best practices, helpful resources, and improvement plans. So starting with pillars, pillars are really a great way to organize your lens. There are essentially categories for how you want to organize your questions. So the pillars can be whatever you'd like. They can be specific to your organization, let's say like a finance pillar or a deployment pillar. Or you can reuse one of the Well-Architected Framework pillars like security or reliability, and then add in your own custom questions within that pillar so that it's more tailored towards your business. Within those pillars, you can have a set of questions. So these questions are the questions that make up that pillar and you can organize them and name them however you like. So let's say we created the finance pillar. An example of a question that could go in your finance pillar would be what financial approvals did you receive before you launched? Then within those questions, you can choose which best practices make that question true? So for example, let's go ahead with our finance example. Our question was what financial approvals did you receive before launching? A couple of examples of best practices could be seeking approval from the finance department, seeking approval from the cost optimization team, So these are all of the best practices that make that one question true. And when you actually create your lens, you'll be able to create a set of reading rules that will identify which best practices are necessary to make the question have no risk, medium risk or high risk. And you'll determine those rating rules, which will then translate to your improvement plan later on, which I'll talk about in just a couple of minutes. You can also provide helpful resources. So helpful resources are really there at the best practice level. So in our finance example, when we gave a best practice of checking with your cost optimization team, if you wanted to provide a helpful resource for that best practice, you could, you could give a little bit more context to what that means so that whoever is using your custom lens, gets a little more understanding about what that best practice is asking them to do. And then lastly, you'll be able to have your own improvement plan. So as Samir was mentioning earlier, the improvement plan is really there to help you remediate any risks that you find from your review and from the questions that you've answered. So when you're actually creating your custom lens, you'll have the opportunity to create your own improvement plans at the best practice level as well. So before we go ahead and do a walkthrough of the feature, what can we really do with custom lenses? So we talked about a little bit about authorizing the lens, which of course we want you to author as many custom lenses as you please. And then you can also share your custom lens. So we know that custom lenses are not only meant for you and your team, but maybe they're meant for multiple teams across your organization. So we give you the opportunity to share the custom lens, either with one person or multiple people, you can really share it with anybody. And then of course you can apply your custom lenses to your workload. So you can apply the custom lens that you've created and upload it yourself. And you can also apply lenses that were shared with you to your workload as well. So we'll go ahead and start the walkthrough. So when you go to the Well-Architected Tool, you'll see a new section called custom lenses. When you click on that, you'll be brought to this table here with two sections. One says owned by me, and one says shared with me. So the owned by me section are those custom lenses that you've uploaded. And then the shared with me section are any custom lenses that were shared with you and that you've accepted. We'll talk a lot about sharing lenses and accepting lenses that were shared with you. But for now, we'll go through the experience of actually creating your custom lens. So you go ahead, click Create, and you're brought to this page here. So the way that you actually author your lens is in a JSON template, so that JSON template has all of the elements that I was mentioning earlier. They have the pillars, the questions, the best practices, the helpful resources, as well as the improvement plan. So you can go ahead and you download the file from this download file button and you can fill out your lens, create your lens, make sure you have all the content you want in there. When you're ready, you can go ahead and choose the file and upload it into the tool. We do have documentation that's linked in this page right here, where it says documentation. That gives you some tips and tricks about how to actually fill out the JSON if you need it. But once you're ready, you can go ahead and click submit. Once you've submitted your custom lens, you'll be brought to this page here that shows you that you've successfully imported your lens. Now, if you happen to make a mistake or you entered something incorrectly, you will get an error saying, what you need to fix. So you can go back, change your JSON, update whatever you need to, re-upload it into the tool, until you got a successfully imported lens notification. You'll notice that when you first upload your custom lens, the default status is in draft form. So this is because we know that your lenses may not be created in a day or a week, and you may want to keep your custom lens in a draft format for awhile until you're ready to publish it. An important thing to note about the custom lens's draft status is that you can't really do anything in the draft status. So you can't apply it to your workload and you can't share it with anyone else. You must publish it before it's ready. So when you're ready to publish it, you go ahead, click publish, and here it'll be brought to versioning. So you want to make sure that you think of ways that you're going to kind of version and name your lens. This is really important because we know that content evolves over time. You might be making updates. So picking a version way that you're going to name the lens will be helpful for you, not only when you're reviewing your workload against the lens, but also when you're looking at the improvement plan and making continuous updates. Similarly to before, when you successfully publish your lens, you will get this notification that says you have successfully published it and your status will change from draft to published. So now let's talk a little bit about sharing. So because your lens is published, now, you have the opportunity to either apply it to the workload, as I mentioned before, or you can share it. So again, sharing is a great way to make sure that everyone who needs to use your custom best practices and custom lens has access to it. So when you're ready, you can go ahead, click on the lens and click share, and you'll be brought to this page here. So here you can enter in the various accounts that you'd like to share it with. So you can share it with one account or multiple accounts. If you choose to share it with multiple accounts, just separate out the account numbers with comma and click create. So what this does is it sends an invitation to whoever you've sent it to, and they have the opportunity to accept or reject the lens. So in order to see who you've shared it with, just as a reminder to keep track of, you can click into your custom lens, go to the overview page and click on share. When you click on share, you'll see a list of everyone that you've shared it with. So you can see here, I've only shared it with one other person and that status is pending. So that pending status is there when you first send an invitation. As I mentioned, people have to accept the lens before they can actually apply it to their workload. So as soon as the person that you shared it with has accepted their custom lens, that status there from pending will change to accepted. All right, so as Samir was mentioning earlier, we know that your best practices change and evolve over time. And so we give you opportunity to edit your custom lens as well. So if you want to do that, you go ahead, you click into your overview page and at the bottom, you'll see the opportunity to click edit. So when you click edit, you'll be brought to this edit a custom lens page. You can download the existing JSON file, as you originally filled it out when you first uploaded it and you can edit your JSON file there. You also don't have to download it from the tool if you've saved your JSON file elsewhere, but you can go ahead, update your lens, edit it. And then when you're ready, re-upload it into the tool and click submit. When you do that, it'll bring you to this page where you'll get an overview of what has changed. So this is, for example, if you've added a pillar, removed a pillar, updated a question, just general overview of what's changed to make sure that what you've changed is actually what you want to change. At the bottom of this page, you'll see a versioning section. So you have two options. You can select major version or minor version. Major versions are really there for changes that really affect the context or the content of the lens. So let's say you are adding a pillar or removing a pillar or adding a bunch of questions. That's probably considered a major version change. What happens when you select a major version change is whoever you've shared your custom lens with, and whoever has it applied to a workload, they'll get a notification saying the author has updated this lens, choose to upgrade. So those really are meant for changes that are bigger, things that you want people who are using the lens to know about. You can also select a minor version. So minor versions are smaller. These are things like text changes or typos or a grammatical error. Things that don't really change the essence of the lens or the context, but really just, you want to quickly update it. And if you select minor version, no notification will be sent. The lens will automatically be updated. And whoever is using the lens, won't really know about it. Again, you want to choose your version name. So here is a great way to continue whatever naming convention you've used at the beginning when you started versioning, select it, put it in, and then go ahead and publish your custom lens. You also can delete your custom lens if you choose. So if you choose to do that, you can go into your owned by me section, click on your lens and go ahead and click delete. An important thing to know here is that if you delete your custom lens, whoever has that lens applied to their workload already will still have access to your lens content. Now, if it wasn't applied to a lens, then they won't be able to start a new workload review. But since they've already started their review with that lens, they still will be able to access it. They will see a notification saying that the author has decided to delete the lens so that they know that it was deleted, but they will still have access to that. So to confirm your deletion, you go ahead, enter in the title of your lens and go ahead and click delete. So we've talked a lot about the authoring experience, how to share, how to edit, how to use the JSON file. Now we're going to switch gears and talk a little bit about how to actually accept a custom lens and then apply your custom lenses to your workload review. So in the same place where you go to see the custom lenses section, you'll see a new section underneath it called share invitations. So this is where you'll be able to see any lenses that were shared with you. You'll be able to see the name of the lens as well as the owner. Now, an important thing to know about sharing and accepting custom lenses is that they're in read only mode. So only the author of the lens can actually edit it. So if it's shared with you or you're sharing it with somebody else, that's in read only mode. So I'm going to go ahead. I'm going to accept my lens share, and I can keep track of it in my shared with me section. So this is back to that main home screen, where you have the owned by me and shared with me. All of these are accepted shares that you've accepted from someone else who shared it with you. And then they're also all the lenses that you have uploaded yourself. So anything in these two columns are applicable that you can use towards your workload review. So when you go ahead and you're ready to start actually reviewing your custom lens, you go ahead to the Well-Architected Tool, you define your workload as you would today. And when you get to this apply lenses section, this is where you'll notice a little bit of a change from what you might be used to today. So the Well-Architected Framework, as well as any AWS authored lenses will have that AWS logo attached to it. So this is to clearly identify what was authored by AWS and what is considered a custom lens. So underneath there, you'll see the different custom lenses that you have access to. These are either lenses that you've uploaded yourself or lenses that you've accepted shares from. So you'll be able to see the owner so that you can choose what you want to apply. So once you're ready, you go ahead select the lenses that you want to apply to your workload, and you go ahead and move forward. So this is really where your JSON file comes to life. So it's a very similar experience to what we're used to in the Well-Architected Tool today, but you'll be able to see the different pillars that you've created on the left-hand side, as well as all of the custom questions that are within that pillar. Once you go ahead and click on the question, you'll be able to see the question description as well as all of the best practices that you've identified make up that question. We also talked a little bit about helpful resources. So the helpful resources that you have identified per best practice are on that info link right next to each best practice. When you click on that, the helpful resources will appear on the right-hand side and give you that extra context we were talking about what the best practices. All of the functionality of the Well-Architected Tool that exists today applies here. So what I mean by that is you can still mark an entire question as not applicable to your workload, and you can also mark individual best practices as not applicable. And then of course you can add notes, which will also transfer over into the improvement plan. So once you've gone ahead, you've done your review, you've gone through your custom lens, you can go ahead and look at your improvement plan. So this is where your custom improvement plan comes to life. You'll be able to see which high and medium risk issues you've identified with your custom lens. And when you click on any of those risks, you'll be able to see the customized improvement plans that you've identified for that best practice. So when you click on those recommended improvement items, that's where your customized improvements will show how to remediate any risk for that question. So you can look at your improvement plan within the Tool, as we do today, you can also generate a PDF report. So we know that sometimes it's really nice to take away your improvement plan so that you can have a hard copy for documentation or for collaboration. It's another way to generate the report, but everything that's in your improvement plan that you've seen in the tool will also be applied here. So that is the general walkthrough of how to use custom lenses. And we just want to remind everybody that Well-Architected is really meant for that continuous improvement. So we recommend coming back to the tool, saving milestones, going through the Well-Architected review, as well as your custom lenses and continuing to come back so that you can track your improvements over time. We do want to answer your questions and I promise we will get there, but before we do, we want to invite Joe up from Vanguard to help answer some questions about his use case. Hi everyone, good afternoon, how's it going? My name is Joe Wagner and I am a technical architect with Vanguard. And right now I sit in our portfolio modernization unit and we've been partnered with Ilana and Samir on the custom lens functionality here over the last few months. Great, thanks for being here. So can you explain just a little bit about how and why custom lenses are needed within your organization and what pain points the custom lenses helps you solve? Sure, yeah. So one of the areas that we've identified at Vanguard as needing improvement is communicating out our best practices and our standards to our very many development teams that we have in the different subdivisions. So by being able to leverage the custom lens functionality and put questions we care about based on a given technology that a unit might be developing on, we can go ahead and make sure they get those best practices and standards as early as possible within their process so that they don't end up in a situation where they're all set to deploy, to prod., and then they get bonked on the head with something they didn't even know that they needed to go to work and make sure that they were doing or not doing, whatever the case may be. Great, so could you provide just a high level example of what type of content you guys are looking to use in the custom lens, if you can? Sure, like I mentioned a minute ago, definitely one of the areas that we know we wanted to get better at was making sure that teams knew what kind of standards or best practices were expected of them. So that's really going to be kind of like our first target for use of the custom lens functionality. We want to make sure that teams know what they need to do or not do. So if a team is building something in ECS and we have a bunch of different patterns or anti-patterns that we want to make sure that we either use or avoid, then we're going to go ahead and put that into a lens, make sure that the teams know they're on the hook to answer the lens and make sure they're aware of what we want them to do or not do. And then we'll look to go ahead and branch out functionality once we can and make sure that we're really effectively communicating out to the teams, what they should do. Great, very cool, and then last question. So how will custom lenses and using it within your Well-Architected Reviews help you track and measure your workload health over time? Yeah, sure, the functionality that was mentioned a little while back, especially around risk evaluations for questions is really one of the lanes we want to go down. So now that we've been able to go ahead and make our custom lenses, we know teams are getting the information that they needed to get as early as possible. We can then leverage the risks that get generated out of the tool, or hopefully not any risks, but we'll see, but we can leverage those risks with our deploy pipeline and make automated enforcement actions based on what kind of risks may come out of a question. And it could be as simple as going to a team and saying, hey, you answered question one on the imaginary ECS lens a certain way, we need to talk a little more about that, all the way up to having a build fail in the pipeline, because they've got a high risk on ECS lens question number three, we're blocking their deployment. So that way we know that things aren't getting out into a production environment that aren't built to the standards that we want to make sure are in place. Awesome, thanks, Joe, thanks for being here.
Thanks a lot guys. A great example of how to use custom lenses. So I think we are ready for Q&A. So I'll pass it back to Samir to answer any of your questions. All right, anybody have questions on custom lenses? Yes please. (audience member speaking) So the question is sharing, does it support AWS Organizations? At the moment, no, but that's something that's coming soon. Any other questions? Yeah, please. (audience member speaking) So the question is, can you share a specific version of the lens? No, we update the version, so you always have the latest version that you're sharing. We don't keep historical records of the versions because once you update a lens, you want the latest, best practices to be applied. So you want to share that. However, if someone's using an older version, they can choose not to upgrade. So they can upgrade when they're ready to do so, but continue doing the review with an older version, just like you do today with Well-Architected Framework. So when we have the Well-Architected Framework, and we do an upgrade, you can choose when you want to upgrade it. Yes, please. (audience member speaking) So the question is, can we have different versions of the same domain or topic and have multiple lenses around that? Yes, you can, so you can create lenses, you can create multiple lenses and you can choose to share it with certain groups. We also have the APIs available, so everything that you can do in the console, you could do through an API. So you could go ahead and build something that can automatically apply a lens to a workload, depending on what the need is. So if it's a different classification, you could apply one version of the lens. And if it's something else, you could apply that as well. So you could do it that way. Yes, please. (audience member speaking) I'm sorry, can you repeat the question? (audience member speaking) Do the APIs support the sharing capabilities? Yes, so the APIs give you all of the same abilities that you have in the console. So every feature that you knew in the console you could do using the APIs. (audience member speaking) Yeah, that's the best advantage of using APIs, you can build these lenses, you can apply them, you can pre-fill some of the answers based on automation or some of the things that you are running within your own organization. Yes, please. (audience member speaking) The question is, can we transfer the ownership of the lens? Unfortunately, no. We want one author and owner of the lens, the account that owns it. So you can't really transfer it to another account. (audience member speaking) So you can share the lens and it can be applied and it's a JSON, remember it's a JSON, that you could check it into code. So you could put it into a repository for someone to use that as well. So you can always use third party tools outside to maintain that JSON. Yes, please. (audience member speaking) The question is can an author provide someone that they've shared the lens right/write permissions? Unfortunately, no, you can't because when you share it, you're sharing the lens, you're not sharing the JSON. So you're sharing the lens that they apply. So it's only read only, but as I said, you can share the JSON outside for people to go ahead and use that just. Yes, please. (audience member speaking) I'm sorry, can you speak up a little? (audience member speaking) Yeah, so there are two questions, the first one is it integrated with CloudWatch SNS, other services? Not yet, as I said, Organizations is something that's going to come, and continue to integrate with the other services as well. Your second question was around- (audience member speaking) Yeah, so we do have documentation, so you can click on it and I'll give you the JSON templates You can look at what the JSON template is, it'll give you all the fields, the descriptions, what validations we run. And as Ilana pointed out, when you do upload it, it runs the validation, it tells you where you know where you need to fix it if there is an error. Yes, please. (audience member speaking) So the question is are we thinking of building out a marketplace for people to share lenses? Is that? Yes, eventually, maybe like, we'll see how it goes. We want to see our customers actually use custom lenses. It's definitely a topic that we've talked about, but as I said, you can share it today. You could have a GitHub repo that you can put it in for people to use it. But yes, as we work with our partners, as we work with our customers, we realize there's a need, where for example, a compliance lens, it applies to a whole bunch of customers within an industry. And there is something that's really good out there. Of course is there is definitely that option that we can explore. Yes, please. (audience member speaking) So if I understand the question correctly, it is what role would custom lenses play if you're building a partnership with Well-Architected? So can you explain a little more about what the partnership is? (audience member speaking) So that is something that you have to work with your organization, right? Like for example, if you have a security focused team, so let's say you have a special team that's just focused on security, and they have a more detailed version of the security pillar, right? You can choose to say, my custom lens is going to be about the security and you can mark all security questions in Well-Architected as unapplicable, not applicable. And then you can go in and have this custom lens being used instead, so you could do that. Marking questions that AWS recommends is not applicable, you want to probably consider, because those come from a lot of knowledge. So you may want to like be more specific with a custom lens. Remember the custom lens is an overlay to the Well-Architected Framework, it's not really a replacement of the Well-Architected Framework. Yes, please. (audience member speaking) Yes, so the question is, can we expand, can you start with Well-Architected, and then expand to a custom lens? Yes, absolutely. So the Well-Architected Framework is by default. So you get that applied to your workload every time you define a workload, then you can go in and assign a custom lens. Now, with that said, that doesn't mean you have to go through the 52 questions of Well-Architected first, and then answer your custom lens. You can always pick which lens you want to go review. And you could go ahead and review that. So the order of how you review it is up to you. Yes, please. (audience member speaking) So we will be publishing them as lenses in the tool. We won't be publishing the JSON. So we will be publishing those just like we do today. So we have serverless FDR and SaaS already in there. So the same way, when you have a new lens, we'll just publish that as a lens that you can apply. (audience member speaking) You'll have to create your own custom lens in that case, if you have to pick and choose. All right, any more questions? Yes, please. (audience member speaking) So the question is, can you combine more than two lenses in one? When you're creating your own custom lens, you can, but you can apply multiple lenses to the workload as well. So let's say there is AWS, there's Well-Architected framework, then that is a serverless lens, and you write your own custom lens. You can go ahead and apply all three to your workload. So you could say, a custom lens can literally have two questions, right? Because everything else is covered between the two lenses, and you want to have these two additional questions. You can go ahead and add that, and you can apply that many lenses. Look around the room. All right, if there no more questions. Thank you so much, appreciate the feedback. Please take the time to do that. And thank you for attending, and good luck. Thank you. (audience applauds)

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1s) Right, thank you so much for coming everybody.

[00:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=3s) Appreciate you taking the time,

[00:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=5s) Today, we are going to be talking about customizing

[00:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=7s) your Well-Architected Review.

[00:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=8s) I'm Samir Kopal, I lead the product and engineering teams

[00:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=11s) for Well-Architected.

[00:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=12s) And I'm Ilana Greenberg,

[00:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=13s) the product manager for Well-Architected.

[00:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=16s) Just to understand the crowd,

[00:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=19s) how many of you are aware of Well-Architected

[00:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=21s) as a framework or the tool or have used it?

[00:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=24s) That's great, that's a great mix here.

[00:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=27s) So today we are going to cover,

[00:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=29s) we'll talk about a little bit about a history

[00:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=30s) of Well-Architected, how it's evolved, where it is today.

[00:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=33s) And then we're going to talk about this really cool feature

[00:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=35s) that we launched yesterday called custom lenses.

[00:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=38s) And we want to talk about what is the problem

[00:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=41s) that we are addressing with that.

[00:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=42s) We're going to talk about an overview

[00:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=45s) of what the feature is,

[00:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=46s) and then we are going to go do a deep dive

[00:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=49s) on how to actually use it in the tool.

[00:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=51s) And we have a customer use case, we'll go through that,

[00:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=54s) and I promise I'll leave time in the end

[00:56](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=56s) for any questions you guys have.

[00:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=59s) All right, so what is Well-Architected?

[01:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=60s) A little bit of a lesson in history.

[01:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=63s) So Well-Architected started when we had a popular service,

[01:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=68s) have an outage back in 2012,

[01:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=70s) and a lot of our customers were impacted.

[01:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=73s) And we recognize that there's some customers

[01:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=76s) who didn't get impacted.

[01:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=77s) And the reason for that was they built in

[01:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=79s) resiliency, reliability into their architecture.

[01:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=82s) And the thinking then was how do we take this learning

[01:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=86s) and share it with everybody?

[01:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=87s) How do you make sure that we have customers

[01:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=90s) that work with us follow the same best practices?

[01:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=93s) And fast forward a few years,

[01:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=95s) we had the Well-Architected Framework with four pillars,

[01:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=98s) security, performance, reliability, and cost optimization.

[01:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=101s) And we continued to evolve on that.

[01:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=103s) So we use that internally, we use that with our customers,

[01:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=105s) we got feedback,

[01:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=106s) we did tens and thousands of reviews to figure out

[01:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=109s) what works, what doesn't.

[01:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=110s) And when we realized that,

[01:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=113s) we recognized one aspect was is we need a process

[01:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=117s) that weaves architecture into your organizational structure.

[02:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=120s) And that was the birth of the fifth pillar,

[02:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=123s) which was operational excellence.

[02:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=125s) Operational excellence brings together

[02:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=127s) the process that allows you to follow these best practices.

[02:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=131s) So the three elements to Well-Architected,

[02:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=135s) one is the Well-Architected Framework.

[02:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=138s) It's available as a white paper.

[02:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=140s) The Well-Architected Tool that revolves

[02:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=142s) around the Well-Architected Framework.

[02:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=144s) So it adds the pillars, the questions, the best practices,

[02:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=147s) all of that is in the Well-Architected Tool.

[02:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=150s) And that allows you to measure and improve

[02:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=153s) your workload health in a very structured, consistent way

[02:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=156s) across all your workloads.

[02:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=158s) When I say, workloads,

[02:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=159s) a workload is just a collection of resources.

[02:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=161s) It could be an application, it could be a platform,

[02:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=164s) it could be a service,

[02:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=165s) it could be a single Redshift Cluster,

[02:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=167s) whatever you wanna call it.

[02:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=170s) But a workload is what you're evaluating.

[02:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=173s) And then there is the improvement plan.

[02:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=174s) The improvement plan is, well, I know what my risks are,

[02:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=178s) how do I mitigate them?

[02:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=179s) What do I do?

[03:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=180s) Where do I go?

[03:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=181s) What's the best practice?

[03:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=182s) So that's the improvement plan around Well-Architected.

[03:06](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=186s) So these are the three elements.

[03:09](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=189s) Now let's talk a little bit about

[03:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=191s) why it is important to do a review.

[03:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=192s) I'll give you an example of when

[03:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=195s) we launched the Well-Architected Tool back in 2018

[03:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=198s) at re:Invent exactly three years ago.

[03:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=200s) And I was the software engineering manager back then,

[03:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=204s) running the service.

[03:25](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=205s) I read the white paper,

[03:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=206s) I was aware we had subject matter experts on the team.

[03:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=209s) So I was well aware of what Well-Architected is,

[03:31](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=211s) and best practices, recommendations, things like that.

[03:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=214s) But when I formally sat down and did the review

[03:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=216s) for the service itself,

[03:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=218s) one of the things I realized is it's a conversation starter,

[03:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=222s) there are things that you don't think of upfront, right?

[03:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=224s) And when you start doing the review,

[03:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=226s) that's where you start having those conversations.

[03:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=227s) An example would be,

[03:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=229s) how are we going to manage if there is an incident

[03:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=232s) running on game day?

[03:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=234s) How are we going to know what's going to happen?

[03:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=235s) Are we gonna update our runbooks?

[03:56](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=236s) We've not launched, it's not in production.

[03:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=238s) So how do we do that?

[03:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=239s) So those things that you start thinking of.

[04:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=241s) Typically, the world was where,

[04:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=244s) hey, it's post production, if you have an incident,

[04:06](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=246s) we have someone who's on call, they'll take care of it.

[04:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=248s) But how can you optimize those things?

[04:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=250s) And that is what I learned is where you can

[04:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=253s) identify these risks early.

[04:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=256s) It has that conversation,

[04:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=257s) you can identify those risks early,

[04:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=258s) you can start planning for those risks.

[04:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=260s) The other thing, how many of you here have been

[04:23](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=263s) in a situation where you're looking at an architecture

[04:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=266s) or you're looking at a design or code and say,

[04:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=269s) well, why did we make this decision?

[04:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=272s) It happens all the time.

[04:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=274s) And then you look back and say,

[04:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=275s) well, I need to go back to some Wiki pages

[04:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=277s) or some internal documentation,

[04:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=280s) or I need to go in and follow some email threads.

[04:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=283s) Or the person who did this

[04:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=284s) is no longer with the organization.

[04:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=286s) Very common, right?

[04:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=287s) And there is no structured way to document.

[04:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=290s) It's scattered, it's hard to find,

[04:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=291s) but with Well-Architected,

[04:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=292s) the tool gives you the ability to document those decisions.

[04:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=297s) It gives you the ability to write

[04:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=298s) why you made that trade off, cost and performance.

[05:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=301s) Hey, we made this decision at this point

[05:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=303s) for this very reason and that's in there,.

[05:06](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=306s) So it's there, you can go look at the workload,

[05:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=308s) you can go look at why it is.

[05:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=311s) So it gives you that document,

[05:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=313s) the decisions and the trade-offs.

[05:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=315s) And then comes the part where you start

[05:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=317s) addressing those risks that you've identified.

[05:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=319s) So you're going to start looking at,

[05:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=321s) well, now we know we have five security risks,

[05:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=322s) three operational excellence risks,

[05:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=324s) and you start improving the health of your workload.

[05:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=327s) Now you might prioritize some things differently.

[05:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=329s) You might look at it and say,

[05:31](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=331s) well, this is an internal tool, cost is more important,

[05:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=333s) it's behind a firewall.

[05:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=335s) Security is probably less important to me.

[05:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=336s) Or it could be the other way where it's like,

[05:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=338s) I don't care about cost, I need extremely high availability,

[05:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=341s) high performance systems.

[05:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=342s) So you can start prioritizing

[05:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=344s) and improving the health of your workload.

[05:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=346s) It's very critical to keep doing that.

[05:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=348s) And then the last part of this is

[05:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=351s) how do you actually go ahead and implement

[05:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=353s) continuous improvement into your processes?

[05:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=359s) A lot of times when we do code deploys,

[06:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=361s) we look at it and say, did I run my integration test?

[06:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=365s) Did I on the unit test?

[06:06](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=366s) What's that coverage looking like?

[06:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=367s) So you're looking at your code consistently

[06:09](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=369s) to look for improving your code quality.

[06:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=372s) A lot of times we miss out on looking at

[06:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=375s) architectural risks.

[06:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=376s) I went from being multi-AZ To Single-AZ

[06:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=378s) in this deployment.

[06:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=379s) It's a massive risk for reliability.

[06:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=382s) So you started looking at that and it helps you do that.

[06:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=384s) Because now when you make a change, you can say,

[06:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=387s) run a Well-Architected review,

[06:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=388s) let's see whether we increase the number of risks we had,

[06:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=390s) or did we decrease the number of risks that we had.

[06:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=392s) So that's why it becomes critical to have those reviews.

[06:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=395s) And it becomes a continuous improvement process

[06:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=397s) for you to do.

[06:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=399s) Now why we need to customize it.

[06:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=402s) So we understand with Well-Architected,

[06:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=405s) that Well-Architected is a general framework,

[06:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=409s) it's a generic framework that allows you to learn measures,

[06:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=412s) improve your workload,

[06:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=413s) but it doesn't tailor it to your specific needs.

[06:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=418s) You're looking for compliance best practices in there.

[07:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=421s) You're looking for finance best practices in there.

[07:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=423s) A lot of big enterprises

[07:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=425s) have Cloud Center of Excellence teams that will go ahead

[07:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=427s) and have a whole lot of best practices

[07:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=430s) that they've built over years of experience.

[07:14](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=434s) Customizing the review will allow you to do that.

[07:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=437s) So custom lenses, which was launched yesterday,

[07:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=439s) allows you to go ahead and add your own best practices.

[07:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=441s) And we'll get into details of how that looks,

[07:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=444s) but it allows you to incorporate those organizational

[07:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=447s) best practices into a single place.

[07:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=450s) That brings me to my next point.

[07:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=452s) Today, a lot of these best practices are scattered.

[07:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=455s) There are tools that will do security best practices,

[07:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=457s) that are tools that will do performance best practices,

[07:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=460s) and then you have Well-Architected.

[07:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=462s) All of these things you have to manage in different places.

[07:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=466s) And when you're starting to do that,

[07:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=466s) it's hard to prioritize, it's hard to look at it and say,

[07:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=470s) well, which one do I pick?

[07:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=472s) But if you have a central place

[07:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=473s) where you're looking at all your workloads,

[07:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=475s) and you're looking at all the risks that you have,

[07:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=477s) and you're trying to then prioritize,

[07:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=479s) it becomes a lot easier

[08:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=481s) because you have a bigger picture there.

[08:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=484s) The same thing with workloads,

[08:06](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=486s) you're not looking at individual workloads,

[08:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=487s) you're looking at a portfolio.

[08:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=488s) So all workloads within that account,

[08:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=490s) now you can also cross prioritize across your workloads

[08:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=493s) to say, well, if I fix these five security issues

[08:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=496s) that I have, it affects 15 workloads, it's a big change.

[08:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=501s) And then as Well-Architected evolved.

[08:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=504s) So Well-Architected went, as I said,

[08:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=506s) from four pillars to five pillars,

[08:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=508s) from 40 questions to 50 questions.

[08:31](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=511s) So that kept evolving over time

[08:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=513s) because we kept learning new things.

[08:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=515s) And we understand that as our customers,

[08:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=517s) you learn new things all the time.

[08:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=519s) It could be an outcome of an incident that you had.

[08:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=522s) It could be a change in direction

[08:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=524s) where we're moving from data centers to the cloud.

[08:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=529s) We need to do things differently.

[08:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=531s) We need to follow different best practices.

[08:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=533s) It could be a finance manager comes in and says,

[08:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=535s) well, this is the budget that you need to live in.

[08:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=537s) So with all of that,

[08:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=539s) you need to be able to update your best practices.

[09:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=542s) So custom lens is going to give you that flexibility,

[09:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=544s) it's going to give you the ability to not just create,

[09:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=548s) but you can now update those as you learn more, as you go,

[09:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=551s) you're going to learn a lot more about these things.

[09:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=555s) And with that, I'll hand it over to Ilana

[09:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=557s) to walk you guys through what custom lenses are.

[09:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=561s) Great, thanks Samir.

[09:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=562s) So what is a custom lens?

[09:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=564s) So an important thing to note about a custom lens

[09:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=567s) is that it's not meant to replace

[09:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=568s) the Well-Architected Framework.

[09:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=570s) It's really there to act as an overlay

[09:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=573s) to give you that opportunity to add in your own

[09:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=576s) internal and organizational best practices

[09:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=578s) as Samir was mentioning.

[09:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=580s) So we'll get into what custom lenses actually look like.

[09:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=584s) But at a high level, you're able to create

[09:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=586s) your own pillars, questions, best practices,

[09:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=590s) helpful resources, and improvement plans.

[09:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=593s) So starting with pillars,

[09:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=595s) pillars are really a great way to organize your lens.

[09:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=598s) There are essentially categories

[09:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=599s) for how you want to organize your questions.

[10:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=602s) So the pillars can be whatever you'd like.

[10:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=605s) They can be specific to your organization,

[10:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=607s) let's say like a finance pillar or a deployment pillar.

[10:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=612s) Or you can reuse

[10:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=613s) one of the Well-Architected Framework pillars

[10:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=615s) like security or reliability,

[10:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=618s) and then add in your own custom questions

[10:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=620s) within that pillar

[10:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=621s) so that it's more tailored towards your business.

[10:25](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=625s) Within those pillars, you can have a set of questions.

[10:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=629s) So these questions are the questions

[10:31](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=631s) that make up that pillar and you can organize them

[10:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=634s) and name them however you like.

[10:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=635s) So let's say we created the finance pillar.

[10:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=639s) An example of a question that could go

[10:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=641s) in your finance pillar would be what financial approvals

[10:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=644s) did you receive before you launched?

[10:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=648s) Then within those questions,

[10:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=649s) you can choose which best practices make that question true?

[10:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=654s) So for example, let's go ahead with our finance example.

[10:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=658s) Our question was what financial approvals

[11:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=660s) did you receive before launching?

[11:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=662s) A couple of examples of best practices

[11:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=664s) could be seeking approval from the finance department,

[11:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=668s) seeking approval from the cost optimization team,

[11:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=671s) So these are all of the best practices

[11:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=672s) that make that one question true.

[11:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=675s) And when you actually create your lens,

[11:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=677s) you'll be able to create a set of reading rules

[11:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=680s) that will identify which best practices are necessary

[11:23](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=683s) to make the question have no risk, medium risk or high risk.

[11:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=687s) And you'll determine those rating rules,

[11:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=688s) which will then translate to your improvement plan later on,

[11:31](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=691s) which I'll talk about in just a couple of minutes.

[11:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=695s) You can also provide helpful resources.

[11:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=697s) So helpful resources are really there

[11:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=699s) at the best practice level.

[11:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=701s) So in our finance example,

[11:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=703s) when we gave a best practice of

[11:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=705s) checking with your cost optimization team,

[11:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=708s) if you wanted to provide a helpful resource

[11:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=709s) for that best practice, you could,

[11:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=711s) you could give a little bit more context to what that means

[11:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=714s) so that whoever is using your custom lens,

[11:56](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=716s) gets a little more understanding

[11:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=718s) about what that best practice is asking them to do.

[12:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=721s) And then lastly,

[12:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=722s) you'll be able to have your own improvement plan.

[12:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=725s) So as Samir was mentioning earlier,

[12:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=728s) the improvement plan is really there to help you

[12:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=730s) remediate any risks that you find from your review

[12:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=733s) and from the questions that you've answered.

[12:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=735s) So when you're actually creating your custom lens,

[12:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=737s) you'll have the opportunity

[12:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=739s) to create your own improvement plans

[12:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=741s) at the best practice level as well.

[12:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=744s) So before we go ahead and do a walkthrough of the feature,

[12:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=749s) what can we really do with custom lenses?

[12:31](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=751s) So we talked about a little bit about authorizing the lens,

[12:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=754s) which of course we want you to author

[12:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=756s) as many custom lenses as you please.

[12:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=758s) And then you can also share your custom lens.

[12:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=761s) So we know that custom lenses are not only

[12:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=763s) meant for you and your team,

[12:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=765s) but maybe they're meant for multiple teams

[12:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=767s) across your organization.

[12:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=768s) So we give you the opportunity to share the custom lens,

[12:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=771s) either with one person or multiple people,

[12:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=774s) you can really share it with anybody.

[12:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=777s) And then of course you can apply

[12:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=778s) your custom lenses to your workload.

[13:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=780s) So you can apply the custom lens that you've created

[13:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=783s) and upload it yourself.

[13:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=785s) And you can also apply lenses that were shared with you

[13:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=788s) to your workload as well.

[13:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=791s) So we'll go ahead and start the walkthrough.

[13:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=793s) So when you go to the Well-Architected Tool,

[13:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=796s) you'll see a new section called custom lenses.

[13:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=799s) When you click on that,

[13:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=800s) you'll be brought to this table here with two sections.

[13:23](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=803s) One says owned by me, and one says shared with me.

[13:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=806s) So the owned by me section

[13:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=808s) are those custom lenses that you've uploaded.

[13:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=810s) And then the shared with me section

[13:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=812s) are any custom lenses that were shared with you

[13:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=815s) and that you've accepted.

[13:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=816s) We'll talk a lot about sharing lenses and accepting lenses

[13:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=819s) that were shared with you.

[13:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=820s) But for now, we'll go through the experience

[13:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=822s) of actually creating your custom lens.

[13:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=825s) So you go ahead, click Create,

[13:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=827s) and you're brought to this page here.

[13:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=829s) So the way that you actually author your lens

[13:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=832s) is in a JSON template,

[13:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=834s) so that JSON template has all of the elements

[13:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=837s) that I was mentioning earlier.

[13:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=839s) They have the pillars, the questions, the best practices,

[14:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=842s) the helpful resources, as well as the improvement plan.

[14:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=845s) So you can go ahead and you download the file

[14:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=848s) from this download file button

[14:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=850s) and you can fill out your lens, create your lens,

[14:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=852s) make sure you have all the content you want in there.

[14:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=855s) When you're ready,

[14:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=855s) you can go ahead and choose the file

[14:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=857s) and upload it into the tool.

[14:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=859s) We do have documentation

[14:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=860s) that's linked in this page right here,

[14:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=862s) where it says documentation.

[14:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=864s) That gives you some tips and tricks

[14:25](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=865s) about how to actually fill out the JSON if you need it.

[14:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=868s) But once you're ready, you can go ahead and click submit.

[14:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=872s) Once you've submitted your custom lens,

[14:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=874s) you'll be brought to this page here that shows you

[14:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=876s) that you've successfully imported your lens.

[14:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=879s) Now, if you happen to make a mistake

[14:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=881s) or you entered something incorrectly,

[14:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=883s) you will get an error saying, what you need to fix.

[14:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=886s) So you can go back, change your JSON,

[14:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=888s) update whatever you need to, re-upload it into the tool,

[14:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=890s) until you got a successfully imported lens notification.

[14:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=895s) You'll notice that when you first upload your custom lens,

[14:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=898s) the default status is in draft form.

[15:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=902s) So this is because we know that your lenses

[15:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=904s) may not be created in a day or a week,

[15:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=907s) and you may want to keep your custom lens in a draft format

[15:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=910s) for awhile until you're ready to publish it.

[15:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=913s) An important thing to note about

[15:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=915s) the custom lens's draft status

[15:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=917s) is that you can't really do anything in the draft status.

[15:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=920s) So you can't apply it to your workload

[15:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=922s) and you can't share it with anyone else.

[15:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=924s) You must publish it before it's ready.

[15:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=927s) So when you're ready to publish it, you go ahead,

[15:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=930s) click publish, and here it'll be brought to versioning.

[15:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=934s) So you want to make sure that you think of ways

[15:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=936s) that you're going to kind of version and name your lens.

[15:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=939s) This is really important because we know

[15:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=941s) that content evolves over time.

[15:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=943s) You might be making updates.

[15:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=944s) So picking a version way that you're going to name the lens

[15:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=948s) will be helpful for you,

[15:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=950s) not only when you're reviewing your workload

[15:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=952s) against the lens,

[15:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=953s) but also when you're looking at the improvement plan

[15:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=955s) and making continuous updates.

[15:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=958s) Similarly to before,

[16:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=960s) when you successfully publish your lens,

[16:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=962s) you will get this notification that says

[16:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=964s) you have successfully published it

[16:06](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=966s) and your status will change from draft to published.

[16:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=972s) So now let's talk a little bit about sharing.

[16:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=975s) So because your lens is published,

[16:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=977s) now, you have the opportunity to either apply it

[16:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=980s) to the workload, as I mentioned before, or you can share it.

[16:23](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=983s) So again, sharing is a great way to make sure

[16:25](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=985s) that everyone who needs to use your custom best practices

[16:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=988s) and custom lens has access to it.

[16:31](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=991s) So when you're ready, you can go ahead,

[16:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=992s) click on the lens and click share,

[16:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=994s) and you'll be brought to this page here.

[16:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=997s) So here you can enter in the various accounts

[16:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1000s) that you'd like to share it with.

[16:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1002s) So you can share it with one account or multiple accounts.

[16:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1005s) If you choose to share it with multiple accounts,

[16:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1007s) just separate out the account numbers with comma

[16:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1010s) and click create.

[16:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1012s) So what this does is it sends an invitation

[16:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1014s) to whoever you've sent it to,

[16:56](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1016s) and they have the opportunity to accept or reject the lens.

[17:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1020s) So in order to see who you've shared it with,

[17:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1023s) just as a reminder to keep track of,

[17:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1025s) you can click into your custom lens,

[17:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1027s) go to the overview page and click on share.

[17:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1030s) When you click on share,

[17:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1032s) you'll see a list of everyone that you've shared it with.

[17:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1035s) So you can see here,

[17:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1036s) I've only shared it with one other person

[17:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1038s) and that status is pending.

[17:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1040s) So that pending status is there

[17:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1042s) when you first send an invitation.

[17:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1044s) As I mentioned, people have to accept the lens

[17:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1047s) before they can actually apply it to their workload.

[17:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1050s) So as soon as the person that you shared it with

[17:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1052s) has accepted their custom lens,

[17:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1054s) that status there from pending will change to accepted.

[17:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1060s) All right, so as Samir was mentioning earlier,

[17:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1063s) we know that your best practices

[17:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1065s) change and evolve over time.

[17:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1067s) And so we give you opportunity to edit your custom lens

[17:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1070s) as well.

[17:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1071s) So if you want to do that, you go ahead,

[17:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1073s) you click into your overview page and at the bottom,

[17:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1077s) you'll see the opportunity to click edit.

[18:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1080s) So when you click edit,

[18:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1081s) you'll be brought to this edit a custom lens page.

[18:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1085s) You can download the existing JSON file,

[18:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1088s) as you originally filled it out

[18:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1090s) when you first uploaded it

[18:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1091s) and you can edit your JSON file there.

[18:14](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1094s) You also don't have to download it from the tool

[18:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1096s) if you've saved your JSON file elsewhere,

[18:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1099s) but you can go ahead, update your lens, edit it.

[18:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1102s) And then when you're ready,

[18:23](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1103s) re-upload it into the tool and click submit.

[18:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1108s) When you do that,

[18:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1109s) it'll bring you to this page

[18:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1110s) where you'll get an overview of what has changed.

[18:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1113s) So this is, for example, if you've added a pillar,

[18:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1116s) removed a pillar, updated a question,

[18:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1118s) just general overview of what's changed

[18:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1120s) to make sure that what you've changed

[18:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1122s) is actually what you want to change.

[18:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1126s) At the bottom of this page, you'll see a versioning section.

[18:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1129s) So you have two options.

[18:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1131s) You can select major version or minor version.

[18:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1134s) Major versions are really there for changes

[18:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1137s) that really affect the context or the content of the lens.

[19:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1141s) So let's say you are adding a pillar or removing a pillar

[19:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1145s) or adding a bunch of questions.

[19:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1147s) That's probably considered a major version change.

[19:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1151s) What happens when you select a major version change

[19:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1153s) is whoever you've shared your custom lens with,

[19:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1156s) and whoever has it applied to a workload,

[19:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1159s) they'll get a notification saying

[19:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1161s) the author has updated this lens, choose to upgrade.

[19:25](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1165s) So those really are meant for changes that are bigger,

[19:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1168s) things that you want people who are using the lens

[19:31](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1171s) to know about.

[19:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1172s) You can also select a minor version.

[19:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1175s) So minor versions are smaller.

[19:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1177s) These are things like text changes or typos

[19:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1180s) or a grammatical error.

[19:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1182s) Things that don't really change the essence of the lens

[19:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1185s) or the context, but really just,

[19:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1187s) you want to quickly update it.

[19:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1188s) And if you select minor version,

[19:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1191s) no notification will be sent.

[19:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1192s) The lens will automatically be updated.

[19:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1195s) And whoever is using the lens, won't really know about it.

[19:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1199s) Again, you want to choose your version name.

[20:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1202s) So here is a great way to continue

[20:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1204s) whatever naming convention you've used at the beginning

[20:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1207s) when you started versioning, select it, put it in,

[20:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1210s) and then go ahead and publish your custom lens.

[20:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1215s) You also can delete your custom lens if you choose.

[20:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1219s) So if you choose to do that,

[20:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1221s) you can go into your owned by me section,

[20:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1224s) click on your lens and go ahead and click delete.

[20:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1229s) An important thing to know here

[20:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1230s) is that if you delete your custom lens,

[20:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1233s) whoever has that lens applied to their workload already

[20:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1238s) will still have access to your lens content.

[20:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1242s) Now, if it wasn't applied to a lens,

[20:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1244s) then they won't be able to start a new workload review.

[20:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1247s) But since they've already started their review

[20:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1249s) with that lens, they still will be able to access it.

[20:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1253s) They will see a notification saying

[20:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1255s) that the author has decided to delete the lens

[20:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1257s) so that they know that it was deleted,

[21:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1260s) but they will still have access to that.

[21:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1262s) So to confirm your deletion, you go ahead,

[21:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1265s) enter in the title of your lens

[21:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1268s) and go ahead and click delete.

[21:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1272s) So we've talked a lot about the authoring experience,

[21:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1275s) how to share, how to edit, how to use the JSON file.

[21:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1279s) Now we're going to switch gears

[21:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1281s) and talk a little bit about how to actually accept

[21:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1284s) a custom lens and then apply your custom lenses

[21:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1287s) to your workload review.

[21:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1289s) So in the same place where you go to see

[21:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1292s) the custom lenses section,

[21:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1294s) you'll see a new section underneath it called

[21:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1296s) share invitations.

[21:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1297s) So this is where you'll be able to see any lenses

[21:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1300s) that were shared with you.

[21:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1302s) You'll be able to see the name of the lens

[21:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1304s) as well as the owner.

[21:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1306s) Now, an important thing to know about

[21:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1308s) sharing and accepting custom lenses

[21:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1310s) is that they're in read only mode.

[21:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1312s) So only the author of the lens can actually edit it.

[21:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1317s) So if it's shared with you

[21:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1319s) or you're sharing it with somebody else,

[22:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1321s) that's in read only mode.

[22:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1322s) So I'm going to go ahead.

[22:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1324s) I'm going to accept my lens share,

[22:06](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1326s) and I can keep track of it in my shared with me section.

[22:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1330s) So this is back to that main home screen,

[22:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1332s) where you have the owned by me and shared with me.

[22:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1335s) All of these are accepted shares

[22:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1337s) that you've accepted from someone else

[22:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1340s) who shared it with you.

[22:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1342s) And then they're also all the lenses

[22:23](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1343s) that you have uploaded yourself.

[22:25](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1345s) So anything in these two columns are applicable

[22:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1349s) that you can use towards your workload review.

[22:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1355s) So when you go ahead and you're ready

[22:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1356s) to start actually reviewing your custom lens,

[22:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1359s) you go ahead to the Well-Architected Tool,

[22:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1362s) you define your workload as you would today.

[22:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1364s) And when you get to this apply lenses section,

[22:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1368s) this is where you'll notice a little bit of a change

[22:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1370s) from what you might be used to today.

[22:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1372s) So the Well-Architected Framework,

[22:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1374s) as well as any AWS authored lenses

[22:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1377s) will have that AWS logo attached to it.

[23:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1380s) So this is to clearly identify what was authored by AWS

[23:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1384s) and what is considered a custom lens.

[23:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1387s) So underneath there, you'll see the different custom lenses

[23:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1390s) that you have access to.

[23:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1391s) These are either lenses that you've uploaded yourself

[23:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1395s) or lenses that you've accepted shares from.

[23:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1397s) So you'll be able to see the owner

[23:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1399s) so that you can choose what you want to apply.

[23:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1402s) So once you're ready, you go ahead select the lenses

[23:25](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1405s) that you want to apply to your workload,

[23:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1407s) and you go ahead and move forward.

[23:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1409s) So this is really where your JSON file comes to life.

[23:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1413s) So it's a very similar experience

[23:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1416s) to what we're used to in the Well-Architected Tool today,

[23:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1418s) but you'll be able to see the different pillars

[23:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1421s) that you've created on the left-hand side,

[23:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1423s) as well as all of the custom questions

[23:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1425s) that are within that pillar.

[23:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1427s) Once you go ahead and click on the question,

[23:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1430s) you'll be able to see the question description

[23:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1433s) as well as all of the best practices that you've identified

[23:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1435s) make up that question.

[23:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1438s) We also talked a little bit about helpful resources.

[24:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1441s) So the helpful resources that you have identified

[24:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1443s) per best practice are on that info link

[24:06](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1446s) right next to each best practice.

[24:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1448s) When you click on that,

[24:09](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1449s) the helpful resources will appear on the right-hand side

[24:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1452s) and give you that extra context

[24:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1453s) we were talking about what the best practices.

[24:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1457s) All of the functionality of the Well-Architected Tool

[24:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1460s) that exists today applies here.

[24:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1462s) So what I mean by that is you can still mark

[24:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1464s) an entire question as not applicable to your workload,

[24:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1467s) and you can also mark individual best practices

[24:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1470s) as not applicable.

[24:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1472s) And then of course you can add notes,

[24:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1473s) which will also transfer over into the improvement plan.

[24:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1477s) So once you've gone ahead, you've done your review,

[24:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1480s) you've gone through your custom lens,

[24:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1482s) you can go ahead and look at your improvement plan.

[24:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1484s) So this is where your custom improvement plan comes to life.

[24:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1487s) You'll be able to see which high and medium risk issues

[24:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1490s) you've identified with your custom lens.

[24:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1492s) And when you click on any of those risks,

[24:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1494s) you'll be able to see the customized improvement plans

[24:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1499s) that you've identified for that best practice.

[25:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1501s) So when you click on those recommended improvement items,

[25:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1504s) that's where your customized improvements

[25:06](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1506s) will show how to remediate any risk for that question.

[25:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1510s) So you can look at your improvement plan

[25:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1512s) within the Tool, as we do today,

[25:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1515s) you can also generate a PDF report.

[25:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1518s) So we know that sometimes it's really nice

[25:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1519s) to take away your improvement plan

[25:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1521s) so that you can have a hard copy for documentation

[25:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1524s) or for collaboration.

[25:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1526s) It's another way to generate the report,

[25:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1528s) but everything that's in your improvement plan

[25:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1530s) that you've seen in the tool will also be applied here.

[25:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1534s) So that is the general walkthrough

[25:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1537s) of how to use custom lenses.

[25:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1540s) And we just want to remind everybody that

[25:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1542s) Well-Architected is really meant

[25:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1544s) for that continuous improvement.

[25:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1546s) So we recommend coming back to the tool, saving milestones,

[25:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1550s) going through the Well-Architected review,

[25:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1552s) as well as your custom lenses

[25:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1554s) and continuing to come back

[25:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1555s) so that you can track your improvements over time.

[25:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1559s) We do want to answer your questions

[26:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1561s) and I promise we will get there, but before we do,

[26:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1564s) we want to invite Joe up from Vanguard to help answer

[26:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1570s) some questions about his use case.

[26:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1575s) Hi everyone, good afternoon, how's it going?

[26:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1577s) My name is Joe Wagner

[26:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1578s) and I am a technical architect with Vanguard.

[26:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1581s) And right now I sit in our portfolio modernization unit

[26:25](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1585s) and we've been partnered with Ilana and Samir

[26:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1587s) on the custom lens functionality here

[26:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1589s) over the last few months.

[26:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1590s) Great, thanks for being here.

[26:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1593s) So can you explain just a little bit about how and why

[26:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1596s) custom lenses are needed within your organization

[26:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1599s) and what pain points the custom lenses helps you solve?

[26:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1603s) Sure, yeah.

[26:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1604s) So one of the areas that we've identified at Vanguard

[26:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1607s) as needing improvement is communicating out

[26:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1611s) our best practices and our standards

[26:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1613s) to our very many development teams

[26:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1615s) that we have in the different subdivisions.

[26:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1618s) So by being able to leverage the custom lens functionality

[27:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1622s) and put questions we care about based on a given technology

[27:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1625s) that a unit might be developing on,

[27:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1627s) we can go ahead and make sure they get those

[27:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1630s) best practices and standards as early as possible

[27:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1633s) within their process so that they don't end up

[27:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1635s) in a situation where they're all set to deploy, to prod.,

[27:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1638s) and then they get bonked on the head

[27:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1640s) with something they didn't even know that they needed

[27:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1642s) to go to work and make sure that they were doing

[27:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1644s) or not doing, whatever the case may be.

[27:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1646s) Great, so could you provide just a high level example

[27:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1649s) of what type of content you guys are looking to use

[27:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1652s) in the custom lens, if you can?

[27:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1654s) Sure, like I mentioned a minute ago,

[27:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1657s) definitely one of the areas that we know we wanted to

[27:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1659s) get better at was making sure that teams

[27:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1662s) knew what kind of standards or best practices

[27:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1664s) were expected of them.

[27:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1665s) So that's really going to be kind of like our first target

[27:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1668s) for use of the custom lens functionality.

[27:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1671s) We want to make sure that teams know what they need to do

[27:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1675s) or not do.

[27:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1675s) So if a team is building something in ECS

[27:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1678s) and we have a bunch of different patterns or anti-patterns

[28:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1681s) that we want to make sure that we either use or avoid,

[28:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1684s) then we're going to go ahead and put that into a lens,

[28:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1687s) make sure that the teams know they're on the hook

[28:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1690s) to answer the lens and make sure they're aware of

[28:14](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1694s) what we want them to do or not do.

[28:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1696s) And then we'll look to go ahead and branch out

[28:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1698s) functionality once we can and make sure

[28:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1700s) that we're really effectively communicating

[28:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1702s) out to the teams, what they should do.

[28:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1704s) Great, very cool, and then last question.

[28:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1707s) So how will custom lenses and using it

[28:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1710s) within your Well-Architected Reviews

[28:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1712s) help you track and measure your workload health

[28:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1714s) over time?

[28:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1715s) Yeah, sure, the functionality that was mentioned

[28:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1718s) a little while back, especially around risk evaluations

[28:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1722s) for questions is really one of the lanes we want to go down.

[28:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1726s) So now that we've been able to go ahead

[28:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1729s) and make our custom lenses,

[28:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1730s) we know teams are getting the information

[28:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1732s) that they needed to get as early as possible.

[28:55](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1735s) We can then leverage the risks that get

[28:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1737s) generated out of the tool, or hopefully not any risks,

[29:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1740s) but we'll see,

[29:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1741s) but we can leverage those risks with our deploy pipeline

[29:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1744s) and make automated enforcement actions based on

[29:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1748s) what kind of risks may come out of a question.

[29:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1751s) And it could be as simple as going to a team and saying,

[29:14](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1754s) hey, you answered question one

[29:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1755s) on the imaginary ECS lens a certain way,

[29:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1759s) we need to talk a little more about that,

[29:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1762s) all the way up to having a build fail in the pipeline,

[29:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1766s) because they've got a high risk on ECS lens

[29:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1769s) question number three, we're blocking their deployment.

[29:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1772s) So that way we know that things aren't getting out

[29:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1776s) into a production environment

[29:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1777s) that aren't built to the standards

[29:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1779s) that we want to make sure are in place.

[29:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1781s) Awesome, thanks, Joe,

[29:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1782s) thanks for being here.
Thanks a lot guys.

[29:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1783s) A great example of how to use custom lenses.

[29:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1787s) So I think we are ready for Q&A.

[29:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1789s) So I'll pass it back to Samir

[29:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1791s) to answer any of your questions.

[29:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1794s) All right, anybody have questions on custom lenses?

[29:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1798s) Yes please.

[29:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1799s) (audience member speaking)

[30:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1805s) So the question is sharing,

[30:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1808s) does it support AWS Organizations?

[30:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1811s) At the moment, no, but that's something that's coming soon.

[30:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1815s) Any other questions?

[30:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1818s) Yeah, please.

[30:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1820s) (audience member speaking)

[30:23](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1823s) So the question is,

[30:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1824s) can you share a specific version of the lens?

[30:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1827s) No, we update the version,

[30:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1829s) so you always have the latest version that you're sharing.

[30:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1832s) We don't keep historical records of the versions

[30:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1834s) because once you update a lens,

[30:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1836s) you want the latest, best practices to be applied.

[30:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1839s) So you want to share that.

[30:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1841s) However, if someone's using an older version,

[30:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1844s) they can choose not to upgrade.

[30:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1846s) So they can upgrade when they're ready to do so,

[30:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1848s) but continue doing the review with an older version,

[30:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1851s) just like you do today with Well-Architected Framework.

[30:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1853s) So when we have the Well-Architected Framework,

[30:56](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1856s) and we do an upgrade,

[30:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1857s) you can choose when you want to upgrade it.

[31:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1861s) Yes, please.

[31:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1862s) (audience member speaking)

[31:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1879s) So the question is,

[31:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1880s) can we have different versions of the same domain or topic

[31:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1884s) and have multiple lenses around that?

[31:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1886s) Yes, you can, so you can create lenses,

[31:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1888s) you can create multiple lenses

[31:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1889s) and you can choose to share it with certain groups.

[31:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1892s) We also have the APIs available,

[31:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1894s) so everything that you can do in the console,

[31:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1896s) you could do through an API.

[31:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1898s) So you could go ahead and build something

[31:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1899s) that can automatically apply a lens to a workload,

[31:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1903s) depending on what the need is.

[31:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1904s) So if it's a different classification,

[31:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1906s) you could apply one version of the lens.

[31:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1908s) And if it's something else, you could apply that as well.

[31:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1911s) So you could do it that way.

[31:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1912s) Yes, please.

[31:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1913s) (audience member speaking)

[31:56](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1916s) I'm sorry, can you repeat the question?

[31:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1917s) (audience member speaking)

[32:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1922s) Do the APIs support the sharing capabilities?

[32:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1924s) Yes, so the APIs give you all of the same abilities

[32:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1928s) that you have in the console.

[32:09](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1929s) So every feature that you knew in the console

[32:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1932s) you could do using the APIs.

[32:14](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1934s) (audience member speaking)

[32:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1937s) Yeah, that's the best advantage of using APIs,

[32:19](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1939s) you can build these lenses, you can apply them,

[32:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1942s) you can pre-fill some of the answers based on automation

[32:25](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1945s) or some of the things that you are running

[32:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1947s) within your own organization.

[32:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1950s) Yes, please.

[32:31](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1951s) (audience member speaking)

[32:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1954s) The question is, can we transfer the ownership of the lens?

[32:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1957s) Unfortunately, no.

[32:39](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1959s) We want one author and owner of the lens,

[32:41](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1961s) the account that owns it.

[32:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1963s) So you can't really transfer it to another account.

[32:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1965s) (audience member speaking)

[32:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1970s) So you can share the lens and it can be applied

[32:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1973s) and it's a JSON, remember it's a JSON,

[32:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1974s) that you could check it into code.

[32:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1977s) So you could put it into a repository

[32:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1979s) for someone to use that as well.

[33:00](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1980s) So you can always use third party tools

[33:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1982s) outside to maintain that JSON.

[33:06](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1986s) Yes, please.

[33:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1987s) (audience member speaking)

[33:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=1996s) The question is can an author provide someone

[33:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2001s) that they've shared the lens right/write permissions?

[33:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2004s) Unfortunately, no, you can't because when you share it,

[33:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2006s) you're sharing the lens, you're not sharing the JSON.

[33:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2010s) So you're sharing the lens that they apply.

[33:32](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2012s) So it's only read only, but as I said,

[33:36](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2016s) you can share the JSON outside

[33:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2018s) for people to go ahead and use that just.

[33:42](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2022s) Yes, please.

[33:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2023s) (audience member speaking)

[33:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2024s) I'm sorry, can you speak up a little?

[33:46](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2026s) (audience member speaking)

[33:56](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2036s) Yeah, so there are two questions,

[33:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2037s) the first one is it integrated with CloudWatch SNS,

[34:01](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2041s) other services?

[34:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2042s) Not yet, as I said,

[34:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2043s) Organizations is something that's going to come,

[34:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2045s) and continue to integrate with the other services as well.

[34:09](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2049s) Your second question was around-

[34:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2051s) (audience member speaking)

[34:14](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2054s) Yeah, so we do have documentation,

[34:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2055s) so you can click on it and I'll give you the JSON templates

[34:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2058s) You can look at what the JSON template is,

[34:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2060s) it'll give you all the fields, the descriptions,

[34:22](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2062s) what validations we run.

[34:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2064s) And as Ilana pointed out, when you do upload it,

[34:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2067s) it runs the validation,

[34:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2068s) it tells you where you know where you need to fix it

[34:31](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2071s) if there is an error.

[34:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2074s) Yes, please.

[34:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2075s) (audience member speaking)

[34:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2094s) So the question is are we thinking of building out

[34:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2098s) a marketplace for people to share lenses?

[34:59](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2099s) Is that?

[35:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2102s) Yes, eventually, maybe like, we'll see how it goes.

[35:04](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2104s) We want to see our customers actually use custom lenses.

[35:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2108s) It's definitely a topic that we've talked about,

[35:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2111s) but as I said, you can share it today.

[35:13](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2113s) You could have a GitHub repo that you can put it in

[35:16](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2116s) for people to use it.

[35:18](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2118s) But yes, as we work with our partners,

[35:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2120s) as we work with our customers,

[35:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2121s) we realize there's a need,

[35:23](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2123s) where for example, a compliance lens,

[35:24](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2124s) it applies to a whole bunch of customers within an industry.

[35:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2128s) And there is something that's really good out there.

[35:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2130s) Of course is there is definitely that option

[35:31](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2131s) that we can explore.

[35:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2134s) Yes, please.

[35:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2135s) (audience member speaking)

[35:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2143s) So if I understand the question correctly,

[35:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2145s) it is what role would custom lenses play

[35:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2149s) if you're building a partnership with Well-Architected?

[35:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2151s) So can you explain a little more about

[35:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2153s) what the partnership is?

[35:54](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2154s) (audience member speaking)

[36:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2168s) So that is something that you have to work with

[36:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2170s) your organization, right?

[36:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2171s) Like for example, if you have a security focused team,

[36:14](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2174s) so let's say you have a special team

[36:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2175s) that's just focused on security,

[36:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2177s) and they have a more detailed version

[36:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2180s) of the security pillar, right?

[36:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2181s) You can choose to say, my custom lens is going to be about

[36:25](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2185s) the security and you can mark all security questions

[36:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2187s) in Well-Architected as unapplicable, not applicable.

[36:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2190s) And then you can go in and have this custom lens

[36:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2194s) being used instead, so you could do that.

[36:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2197s) Marking questions that AWS recommends is not applicable,

[36:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2200s) you want to probably consider,

[36:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2203s) because those come from a lot of knowledge.

[36:45](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2205s) So you may want to like be more specific

[36:48](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2208s) with a custom lens.

[36:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2209s) Remember the custom lens is an overlay

[36:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2211s) to the Well-Architected Framework,

[36:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2212s) it's not really a replacement

[36:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2213s) of the Well-Architected Framework.

[36:56](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2216s) Yes, please.

[36:56](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2216s) (audience member speaking)

[37:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2223s) Yes, so the question is, can we expand,

[37:05](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2225s) can you start with Well-Architected,

[37:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2227s) and then expand to a custom lens?

[37:09](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2229s) Yes, absolutely.

[37:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2230s) So the Well-Architected Framework is by default.

[37:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2232s) So you get that applied to your workload

[37:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2235s) every time you define a workload,

[37:17](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2237s) then you can go in and assign a custom lens.

[37:20](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2240s) Now, with that said,

[37:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2241s) that doesn't mean you have to go through the 52 questions

[37:23](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2243s) of Well-Architected first, and then answer your custom lens.

[37:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2246s) You can always pick which lens you want to go review.

[37:29](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2249s) And you could go ahead and review that.

[37:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2250s) So the order of how you review it is up to you.

[37:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2253s) Yes, please.

[37:34](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2254s) (audience member speaking)

[37:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2264s) So we will be publishing them as lenses in the tool.

[37:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2267s) We won't be publishing the JSON.

[37:50](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2270s) So we will be publishing those just like we do today.

[37:52](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2272s) So we have serverless FDR and SaaS already in there.

[37:57](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2277s) So the same way, when you have a new lens,

[37:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2278s) we'll just publish that as a lens that you can apply.

[38:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2283s) (audience member speaking)

[38:09](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2289s) You'll have to create your own custom lens in that case,

[38:12](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2292s) if you have to pick and choose.

[38:15](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2295s) All right, any more questions?

[38:21](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2301s) Yes, please.

[38:23](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2303s) (audience member speaking)

[38:26](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2306s) So the question is, can you combine

[38:27](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2307s) more than two lenses in one?

[38:28](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2308s) When you're creating your own custom lens, you can,

[38:30](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2310s) but you can apply multiple lenses to the workload as well.

[38:33](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2313s) So let's say there is AWS,

[38:35](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2315s) there's Well-Architected framework,

[38:37](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2317s) then that is a serverless lens,

[38:38](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2318s) and you write your own custom lens.

[38:40](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2320s) You can go ahead and apply all three to your workload.

[38:43](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2323s) So you could say,

[38:44](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2324s) a custom lens can literally have two questions, right?

[38:47](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2327s) Because everything else is covered between the two lenses,

[38:49](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2329s) and you want to have these two additional questions.

[38:51](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2331s) You can go ahead and add that,

[38:53](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2333s) and you can apply that many lenses.

[38:58](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2338s) Look around the room.

[39:02](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2342s) All right, if there no more questions.

[39:03](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2343s) Thank you so much, appreciate the feedback.

[39:07](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2347s) Please take the time to do that.

[39:08](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2348s) And thank you for attending, and good luck.

[39:10](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2350s) Thank you.

[39:11](https://www.youtube.com/watch?v=BsEd_Ue_0TQ&t=2351s) (audience applauds)

