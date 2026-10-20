# Claude's Creator Just Told Us How to Actually Use Claude in 2026

- Channel: AI Edge
- URL: https://www.youtube.com/watch?v=tRmLQZJYQdA
- Published: 2026-09-17
- Duration: 20 min
- Views at fetch (2026-10-11): 118,794
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

So, I've been ramping up the
implementation of AI across my business.
But before I spent tens of thousands of
dollars on claude credits and
developers, I wanted to work out what
the new best system would be in 2026.
So, instead of watching content
creators, I went through over a 100
hours of official material from
Anthropic, the creators of Claude and
Claude Code, including the head of
Claude Code, Boris Churnney, who
honestly completely changed my
perspective of how we need to be using
AI. He actually suggested that you
should delete your Claude MD, your
custom skills, and your custom
instructions because the model is now
smarter without them. Which at face
value sounded crazy. But the more I
started to dig in, the more I realized
he had a point. And the way we have to
use Claude now is completely different
from even 6 months ago because these new
models operate in a completely different
manner. So, in today's video, I'm going
to break down each learning, and then
I'm going to break down exactly how that
learning is now materially changing how
I'm using AI. I tried out all of these
techniques on my real business setup,
and honestly, I was mind-blown. If you
want to make sure you stay on the
cutting edge of AI, make sure you
subscribe to the channel and click the
notification bell because I'm obsessed
with this stuff. And whenever I learn
something new, I'm going to give it to
you. There are specifically two things
right now which I think you need to be
doing if you're half serious about AI.
All right, so lesson number one, and
this is coming from Boris himself, who
created Claude Code inside a fourperson
team at Anthropic, controversially said
that you should delete everything. He's
done a few talks recently, and I noticed
his loudest theme is actually
subtraction and not addition. In fact,
this is actually how they build Claude
code. Every time a new model ships,
Anthropic deletes most of Claude Code's
system prompt and slowly builds up the
lines back at a time. They call this
ablation because they found that the new
models actually run better and more
efficiently with less instruction
because most of what was in the system
prompt was actually correcting an issue
that the model didn't have before. So,
if you've been using your old skills
that were optimized for Opus, you'll
probably notice if you try them on
Fable, they probably won't work the same
because the huge amount of context and
instructions that you needed to give the
old models simply isn't necessary now
because the old models are smarter and
they think differently. So, he actually
advised users to undertake the same
ablation process. He said every 6 months
you should delete your Claude MD file
and just see what the model does bare
and the output will probably actually be
better than with the skills and the
memory. Now, personally, I'm still using
skills. Personally, I still have a
memory system. I'm not saying disregard
your memory system, but I think the
concept of ablation and the concept of
testing the new models without all of
your old bloat and then building it back
up slowly again based on what the new
model needs is super relevant. You've
probably also experienced when you give
a model too much context, it actually
starts working worse. But I think if
you're going to delete anything, delete
the lines that are telling the model how
to behave. I think context on who you
are in your business is still going to
be relevant, but all of those old
instructions we needed to add like think
in this way, respond in this way, act in
this way. That kind of stuff probably
isn't as necessary now. So, you can
really keep three things. your context,
your goals, and your definition of what
completion looks like for a specific
task. Work that normally for a day. And
if the model keeps tripping on a
particular thing, then add a line back
for it and slowly build it back up.
That's the entire ablation process that
Anthropic also runs internally. And if
the creators of Claude Code are
literally recommending that you do these
things and are doing them internally,
it's a pretty good indication that this
is the best practice when it comes to
using Claude in 2026. Now, in the
description below, I'm going to give you
access to a free ablation prompt that
you can copy and paste and put it into
your own Claude. What it's going to do
is read your current setup, ask you a
few questions about what and how you
actually use Claude, and then hand you
back a lean version of instructions that
are actually applicable to you. It's
available for free alongside all the
other resources from these videos in my
school community below. And that
community is amazing because it's where
I'm keeping you guys up to date in
between these videos of the way I'm
changing how I'm using AI. In the
future, I'm going to be adding a skill
library, including the skills on how I'm
creating my own content and my marketing
funnels and pipelines. So, lesson one
focused on deletion or subtraction.
Lesson two is all about verification,
aka how you actually prompt Claude. So,
Boris says that the most common mistake
that he sees when it comes to users
using Claude is oversp specification,
which if you're doing this, I don't
blame you cuz a year ago, this is
literally what you had to do to get the
output that you wanted. So users would
have to go, you know, step one, do this,
step two, do this, step three, then do
this. The issue is you're telling the AI
how to think. And by telling it how to
think, it might actually arrive at a
worse destination because you are
limiting how smart and capable these
models actually are. So instead, what
you should be focusing on is optimizing
for a clear specification of the output,
verifying what creates a successful
output in your mind instead of giving
Claude all of the instructions as to how
to arrive at that output. You don't need
to micromanage the new models,
especially the mythos class models like
Fable. They actually do worse when you
micromanage them. Like a lot of the time
now, I'll just dump something into
Claude code. I have no idea how to do
it, and I'll just ask it to get it done.
For example, I was researching for this
video. I was scraping X to find real
clips from Boris and other members of
Anthropic speaking about best practices
and I just dumped all of the links into
claude code and I said hey transcribe
all of these and it just did it on my
behalf. I didn't need to tell it how to
do it. These models are now smart enough
to be able to do the work on your
behalf. The real example which really
hit home as to how powerful this
verification mindset is was a company
called Bun. If you haven't heard of it,
it's a massively popular JavaScript
runtime. So essentially the engine that
executes JavaScript code. It gets over
20 million downloads a month and it's
actually the thing that Claude Code
itself runs on, but it was written in a
low-level language called Zigg. So it
started to experience lots of issues
like memory issues, crashes, bugs,
leaks. So its creator decided to test
whether claude code could rewrite the
entire thing rewritten in a language
called Rust, which would solve a lot of
these problems. For reference, that's
over 530,000
lines of code, which the creator said
would take an engineering team around a
whole year to complete. And you know how
long it took with Claude code? 11 days
with just one engineer steering the
prompt. That had around 64 coding agents
running the rewrite. And that Rust
version is in production right now. So
if you use Claude code, you are
literally running code that Claude wrote
for itself. And Daario, the CEO of
Anthropic, has said now that the
majority of code for Claude itself is
now written by Claude itself and just
overseen by software engineers. So the
demand for software engineers is
shifting from the act of physical coding
to more the ability to curate, oversee
and verify. So in that entire coding
process, Claude was able to verify the
work at every step of the way. So the
lesson in this isn't that the rewrite is
possible because the prompt was really
clever. It's possible because the
checking and verification process was
automatic. So instead, by becoming end
goal orientated, and I'll show you a
very good system for this in just a
couple of minutes, Claude becomes a lot
more effective than trying to involve
yourself every step of the way. So in
practice, what I try and do now is
actually challenge Claude. I think of my
base idea and then I think, how can I
actually make this harder? How could I
ask Claude to do something I don't think
it can do or I think is really hard. And
more often than not, it can actually do
that thing. So, I think sometimes we
actually need to challenge Claude more.
You'd be surprised at how capable it
actually is. Sometimes I'll just have
Claude code on my second monitor while
I'm working. And something I'm about to
do on my computer, I'll just voice
prompt into the monitor next to me, I'll
be like, "Hey, Claude, can you do this?"
Just to see if it can do it, and it
often can. Whether it's rewriting files
on my desktop, whether it's searching
for a lost file, whether it's scraping a
YouTube page to deliver some data,
whether it's going onto my notion and
curating my entire content slate,
whether it's reviewing a product that I
need to do due diligence on, it can do
all of these things. And you know, I
almost need to get out of the habit, and
I have just been drilling this in over
time, you know, of not doing work
manually myself and thinking, can Claude
do it? you know, instead of trying to
look at a company and review all of the
specifics, get Claude to do it and I
just review the output. And this shift
is making me a lot more AI native over
time without me needing to be like, oh,
I want to become more AI native now. You
just gradually start to introduce it
into your life by just having it open
and leaning on it. And that leads me on
to the third lesson. The model can do
way more than you realize. There's a
story that happened inside Anthropic
that stuck with me when I was watching
all of this content. So, someone
actually discovered by accident that
Claude can actually draw portraits and
landscapes using OpenCV, which is a
computer vision library. Nobody even
trained it to draw, and nobody knew that
it could. Boris thinks that there are
dozens, maybe hundreds of abilities
sitting in the model right now that
nobody knows about because nobody's
asked. So, if you come up with something
insane, just try. you don't actually
know what it's capable of because
neither do the creators of Anthropic,
which the more that I think about it is
like a little scary, but anyway. So, to
make this actionable, make it a goal
that once a week you give Claude a task
that you don't think is possible,
something that you never delegate. Worst
case, it fails and you lost 10 minutes.
And if you set Claude code to automatic,
it can operate on your behalf without
the need for constant approvals. And you
can even run it on a scheduled session
or a loop which we're going to get into
so it can verify its behavior on its own
behalf. For example, I don't know, on a
Friday evening, you could come up with a
business idea, just a crazy idea you've
been thinking of, and be like, "Hey,
build the landing page. Here's the
scope. Build the pipeline. Build the
research funnel. This is the output.
This is the company I'd like to create.
Go about your weekend. And then on
Sunday evening or Monday morning, check
in. See what it was able to create."
Maybe you've created a business in a
weekend that you didn't know was
possible before, but Claude did it. Or
maybe it fails, but what do you have to
lose? You probably spend an hour on a
Friday evening watching Netflix anyway,
so why not spend a few minutes prompting
something that could generate you
potentially thousands of dollars or
provide you a massive productivity
unlock? I've been doing this in my
business a lot. Like even this morning,
I thought of a new way to prospect
potential clients. And I've already
actioned a prompt that's going to build
an entire scraping system that I don't
know if it's actually possible, but if
it is, it could potentially land me
hundreds of new leads for my agency
every single month. And to make that
possible, this brings me into lesson
number four, agents managing agents. So,
the fourth theme kind of sounds like
sci-fi until you actually dive into the
details, but Boris says that he actually
no longer even speaks to agents directly
because his agents are talking to other
agents. And on a normal night, he says
he has thousands of them running while
he sleeps. Inside Anthropic, this is
manifested into Claude actually
maintaining its very own code base. They
run 20 to 30 daily routines and each one
is a single sentence. The result in
Boris words is engineer productivity up
hundreds of percent every single month
and accelerating fast. And he says
they're still bottlenecked on engineers,
which tells you how much work then
becomes available once the ceiling
inevitably lifts. So once again, how do
you make this actionable? How do you get
an agent to manage an agent? Well,
simply, and I've done a full video
breakdown on this if you want to watch
it. I'll leave a link below. Pick a
reoccurring task that you do every
single week or every single day.
Something that happens on some sort of
cadence. It could be running a business
development research sweep. It could be
automated outreach for prospective
clients or managing inbound deal flow.
It could even be managing your own
monthly accounting. Pick one task to
begin with and put it on a schedule.
This functionality is available inside
Claude and it's automatically going to
spawn and run an agent on your behalf.
So don't try and build an agent army on
day one of dozens of different flows.
Just pick one high leverage thing that
you already do and try and automate it.
And then the next week automate another
thing and another thing and another
thing. And that's how in a month you
take four workflows that take you hours
a week and you fully automate them. And
within 6 months you've automated 24
workflows. That's how you build the
blocks to becoming a fully autonomous AI
individual or AI business. Now, when I
say fully autonomous, I don't mean that
you won't be involved. In fact, you're
more important than ever. You give the
direction, the taste, and creativity to
the agents to do the work, but you're no
longer the hands in the business. The
agents are, at least for anything
digital. So, now let's get into lesson
number four. And this has already been
something that I've been implementing in
my daily work, and that is loops. We
just spoke about setting reoccurring
tasks, but how do you make sure that the
tasks execute autonomously and executed
in the correct manner? Well, that's
where loops come in. And this is now the
best way to be using Claude in 2026. I
recently did a video where I said
prompting is dead. Loops are the future.
And that is 100% my belief and also the
belief of those at anthropic because the
new model is so good at verification
that it's able to correct its own work,
thus paving the way for truly autonomous
loops. So a lot of the tasks that I just
discussed run on a looping schedule
where I give it the goal, so the defined
output, and I give it the loop, which is
the interval for the time I'm expecting
a process to take with mini loops or
verifications happening along the way.
The reason Claude didn't ship this
before is because it simply wasn't safe.
A year ago, if an agent read a malicious
instruction, aka a prompt injection,
like delete everything on the user's
computer or install this piece of
malware, there was a real chance it
would just do it. Boris says that with
the new clawed models and the
classifiers that Anthropic now runs on
all traffic, they can't demonstrate
prompt injection anymore. So the big
unlock is that unsupervised agents
weren't really viable at the start of
this year because you couldn't trust the
information they were reading. But now
that constraint is mostly gone. So it's
created a huge shift in how I and many
others are completing work because
before you'd used to be the loop
yourself. You'd prompt, check the
output, give feedback, prompt again.
You'd be sitting in the middle of every
task. But now Clawude does the
verification of every step. So the AI
now runs that cycle internally. It
tries. It checks its own work against
your definition of done. It fixes what
fails and it only comes back when it
passes based on your end goal. So they
essentially took Boris's verification
idea and they turned it into an
actionable system that you can now use
within Claude. I've done a full video on
this if you want to check it out. It's a
loop engineering masterass, but let me
break it down really simple quickly.
Essentially, you want to start with a
goal. So forward/goal determines the
final output that you would want. Then
alongside that you can use forward/loop
to dictate to claude code what interval
you would like that task to be
completed. For example, I can ask
for/goal scan this competitor channel
for new uploads. Log the title views
views per day topic to the niche tracker
MD file. Flag any video doing 3x the
channel's median as an outlier with one
line on why the title or thumbnail
works. done equals tracker updated
outliers flagged stop after eight runs
and then I can do forward/loop and state
the interval that I would like this task
to complete and you don't really need to
spell it out more than that because if
you give claude a goal and you give it
an interval it's going to automatically
be running mini loops to verify its own
work especially if you're using fable
where I think this is most effective but
the new opus models still do this as
well it really just depends on the
complexity of the task and if you're
willing to spend the extra money for
fable it's honestly too expensive
expensive for most people. I still use
it in many cases. But what you can
actually say to Claude, which I also put
into my loops masterass, is default to
the best model for each step of the
task. So then you essentially use Fable
as an orchestration model. So Fable
outlines the strategy and it defers to
Opus or it defers to Haiku or Sonnet
when it thinks that model is better
optimized for that task. That's
essentially agent orchestration with
Fable as the orchestrator. So if you
want to link that full video, I'll link
it down below. And of course in my free
school community, we also have a bunch
of the top loops that I actually run
inside my own business. So loops is part
one of what I think creates really
strong agentic work in 2026 on chord. By
the way, a lot of these principles apply
to GPT as well, but I'm a chord power
user. That's why I'm focusing on chord
in today's video. But the second part,
which is lesson number five, is
utilizing graph engineering. This is
also something I did a full master class
on, which you can check out. But let me
give you the quick explanation cuz this
really has changed how I create
processes in my business and as a result
has made all of my processes so much
more efficient. So for most businesses
and even most individuals that do work,
which I'm presuming is you, you
essentially keep a lot of processes in
your head. I have even been surprised at
times when I really try and unpack it
how many processes are just in my head
that are just intuition built up over
years. But what I realized is that most
processes can actually be broken down
into a defined set of variables and a
defined set of steps that lead to the
end goal. Like in the past, I'd be
scanning X for content ideas. But what
was I actually doing? Well, I was
looking for posts that had a statistical
outlier. I was looking for posts that
matched the subject matter that I was
interested in. And I was looking at
posts which had a viral hook and viral
copy that I could then lean on to create
more content. So even my ex research
process was really a process that could
be broken down into a set of agentic
steps. Even my deal flow process I
realized was a process that could be
broken down to reaching out to a
prospective client, drafting the message
in a particular way based on that
client. finding the right touch points
for the client, reviewing and scanning
those touch points, automatically
tracking them in our system once we've
landed the client, automatically
scheduling a call, a follow-up, a
proposal, and then going to the final
deal procurement stage where it then
shifted from an outreach pipeline to an
implementation pipeline which then
shifts to a separate graph. So to sum it
up simply, what I did is I started
breaking down every workflow in my life
and my business and I started creating a
graph, a very visual workflow with HTML
in Claude that clearly stated across
each step of the way what task needed to
be done, why it needed to be done, and
who needed to do it. Whether it was an
AI specifying which AI specifying using
which skills, and then if it was a human
to verify a process. I clearly outlined
where human intervention is needed. And
when I started going through this
process of breaking down a workflow like
land a client into a set of 20
individual SOPs, I realized that like 17
or 18 out of the 20 could actually now
be done by AI. And by engineering a
graph, that is I think the most
effective way for us as humans to pass
our work to AI because it's so much more
visual. Now the AI doesn't need visuals.
It just needs a markdown file. So this
is more of an exercise for you to
visualize where the agents can step in
so you can better curate what work needs
to be done. So that is the taste and
knowledge compression aka you giving
your knowledge to AI side of the
equation because your brain is
essentially an algorithm that's trained
on years of data. So our goal is to
compress that into an AI and into a
format that we understand because if you
don't understand what the AI is doing
then you don't know how it's arriving at
an output. So this completely bypasses
that and that's why graph engineering is
so impactful in 2026. So in my school
community, I've also put a bunch of
graphs that I use in my business and you
could then take them if you're in a
similar niche like the agency niche or
the content niche and you can then apply
that format to your own work. In my
resource library, I also have the full
prompt from that video. So you can take
that prompt, put it into claude code and
start creating graphs for yourself. And
what I recommend is that for each task
you actually create it could be a notion
library. It could be an Excel
spreadsheet. I personally use Google
sheets created with claude and I have a
library of every single workflow and
then I have a HTML and MD file for every
single workflow that the AI can read. So
I keep my own library and then as I have
ideas and as business processes evolve,
I simply edit that library. So I have a
constant library of graphs which are
reflecting the current automated
workflows in my business. Now, before
you get overwhelmed, going back to what
I said before, just pick one process and
start with it. Like, that is all you
need to do. That's like my homework
after watching this video. Just pick one
task and automate it. And if you want a
more in-depth summary on graph
engineering, I'll also leave the link
below because I did a full video guide
on it where I actually break down the
real processes in my business and how
I've graph engineered them into aic
workflows. So, those are the best five
ways that you can use Claude right now
in 2026. I'll keep you updated as things
change because things are evolving so
fast. Claude is literally coding itself.
So the best practices now might not be
the best practices in a few months. So
make sure you subscribe to the channel
to stay upto date. If you join my free
school community, I'll also keep you
updated in between videos as well as
giving you all of the resources
including the prompt from today's video.
I will see you in the next one. Thanks
for watching. See you later. Peace.
