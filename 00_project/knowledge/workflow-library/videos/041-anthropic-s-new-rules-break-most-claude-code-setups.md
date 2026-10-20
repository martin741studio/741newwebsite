# Anthropic's New Rules Break Most Claude Code Setups

- Channel: Eric Tech
- URL: https://www.youtube.com/watch?v=rYb_xSjx-Fw
- Published: 2026-07-29
- Duration: 9 min
- Views at fetch (2026-10-11): 22,357
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

If you're using Claude code to build
your second brain, then you got to check
out this video because in this video
we're going to cover this article that
Tharik, who's a member of technical
staff from the Anthropic team, has
recently released this article for the
new rules for context engineering for
Claude 5 models. In this article, we're
going to go over exactly how to improve
our Claude code's accuracy, as well as
how to save token usage for the latest
Claude 5 models. So, with that being
said, let's not waste any time, let's
get straight into the video. All right,
so what the article starts saying here
is that whenever you send message to
Claude, the prompt is only a small part
of the context it gets. So, much of
those contexts is actually assembled by
your system prompt, skills, Claude MD
files, memories, and so much more. Now,
we call this context engineering, and we
probably already know that by now. And
what he's saying here is that this could
be really hard for model here to evolve
because as the model here for a score,
right, the intelligence score here start
to increase, start to getting better and
smarter, it's really hard to actually
brains all the knowledge that new models
are having and into the new systems. So,
whenever you're switching models like
GPT-4.5 or 4.8 through from Opus here
all the way to Opus 5, right? Let's say
if you're using Opus 4.5 and you're
using the same Claude MD file or same
the system prompts, and let's say you're
going to switch the model here to Opus 5
here, right? So, it doesn't really makes
any difference to swap the model here
because the guardrails, or in this case
the hardness around the model here is
already preset. And one of the example
that they give in the article is the
instruction collision. So, for example,
let's say the system prompt here say,
"Do not add comments." And your Claude
MD here says, "Comment or document
everything." And your prompt says, "Make
this readable." Then what happened here
is that when you give these instructions
to Claude and also along with your
system prompt, your Claude MD or in this
case your Claude or your large language
model here is actually going to burn a
lot of tokens for the reasoning because
there's actually a contradictions in
terms of the instructions that you give.
Or let's say if we have another failure
example, here you can see it's called
the kitchen sink file. And essentially
inside of a Claude MD file, you can see
we have our 1,400 lines, right? So,
there's a lot of instructions on how to
do things. But, you can see that only
few of them are being used inside of the
session. For example, the first line,
how to run test. Let's say this how to
run test is bunch of rules on how to do
it, right? And it's actually being used
5% of the session, or maybe close to
nothing, right? Or close to not being
used at all, or underused 2% of the
session here. So, but this Claude MD
file here is actually being loaded 100%
of the time every time we're sending
questions or sending in prompts back to
Claude. So, there's actually a lot of
useless stuff that's actually inside of
the Claude MD file that we can be the
package that into a skill so that we can
be able to load that whenever we need
it. Okay? So, there's a lot of things
that are sending back and forth that
costing money for tokens, that costing
inaccuracy for results, and that's why
you can see that Anthropic team has
deleted over 80% of their system prompt
for models like Opus 5 and Fable 5 with
no measurement loss on the coding
evaluation. And they're able to do that
by using a single skill called Claude
Doctor, which is a command called
{slash} doctor in Claude Co here to
right-size your skill and also your
Claude MD files. So, now if I were to
navigate to my second brain, here you
can see my this is my Eric OS folder,
and I have all the projects, all my
knowledge base, as well as the raw
folders, skills, MCPs, they're all in
there. And what I'm going to do here is
I'm going to do {slash} doctor here. And
you can see that here's the definition.
So, health check for the user's Claude
Co setup, fix the issues, diagnose
installations and health. Now, what we
want to do here is that if you want to
actually see the full definition, you
can actually just ask it. Say, "Hey,
what does actually the {slash} doctor
do, right? What does this actually the
skill do?" So, in this case, I'm going
to um
ask this, and what's going to happen
here is Claude is going to give you a
definition of what {slash} doctor does.
Okay, so here you can see {slash} doctor
here is going to help you to audit your
Claude Co setup, report it, and then
help you to apply if you approve it. So,
what it inspect here, you can see the
Claude JSON file, skill usage, plugin
usage, and so many more. So, you can see
that these are all the 10 checks that it
checks. So installing health, skills,
and MCPs, guiding your cloud and the
file here, and you can see there's so
many things that it should actually
check to making sure that actually
protects or refactoring your contacts.
And the TLDR for this is that it finds
extensions that you pick contacts for,
and but you never use. So it blows in
your contacts for the cloud and the
files, permission prompts that you keep
hitting. Then fix the ones that you
actually approve. So here you can see if
you say the words then you're actually
going to run it. I'm just going to say
yes. Uh run it for me. So I'm just going
to have this run it and let's see what
it does. Now, before we continue this
video, my name is Eric and I have used
to work as a senior software engineer
working at companies like Amazon and
Microsoft. And recently I started my
school community where I help you to
master AI agents, automations, and
building real SaaS product here. Now, in
this community you're going to get a
six-level courses where you can actually
start from the foundations from building
a simple workflows all the way to
building AI SaaS product here and
turning all the skills you learn into
offers and packages. And in this
community here you're also going to get
weekly live calls. So if you have any
questions, you can also bring that in
our weekly live calls every Friday here
where you can ask any questions,
learning topics, and getting real
updates. And of course, if you have any
questions, you can also check it out in
our community tab for the Q&A sessions
where you can actually post your real
question here and I'll make sure to
answer that within 24 hours. So if
you're interested for that, make sure to
check it out in the link in the
description below. Okay, so finally you
can see that we have our response back
for the full reports. So here's actually
what gets touched. Nothing's deleted
from the disk, disabling in the settings
only. So [snorts] here you can see for
group A we have the 36 user skills
disabled. So for example, the Hexo
families, designs, dev, marketing, and
stuff like that. Uh group B here you can
see is only related to projects. So here
you can see for Obsidian, uh video and
stamps, things like that are part of the
group B. Now, these are all project
only. So pretty much those are probably
being used a lot, but I don't think we
should delete that. There's also group
C, so five plugins to disable. so you
can see that PR review, context seven
here, Stripe code review, and also code
summarizer. And here you can see
there's also group D for two text edits
here. So
remove the 12-line here for understand
anything, and also the Claude MD here,
so refining that a bit more. So you can
see that total roughly around 6,000
tokens back per sessions. For your
skills listing dropped from 10,000 to
6.9 thousand. So it's safely under the
10,000 cap, so it stops getting
truncated. So what we can do here is
what I recommend to do is just say like,
"Okay, so out of those skills, I want to
cherry-pick which skill to install, and
or in this case keep, right?" So the
ones that I want to keep out of it, or
in this case disable for now, is maybe
context seven and Stripe, because I
don't think that I use that a lot.
Maybe for code review or code
summarizer, or in this case the PR
reviews, I want to keep at least like
the best, like one of them, right? So
those are all good for in terms of like
coding projects, I still want to keep
them.
In terms of like other things, right? So
I think group B, I still need them.
Those are all good skills that I think I
do need them. And in terms of the group
A, I think I think there's a lot of
skills in there. So what we can do here
is that we can actually be able to
cherry-pick, and I'm just going to
submit that. And having Claude here to
figure out, based on what I just said,
on what to stay and what not to stay.
And one other tip here that I always
want to give here is figure out what are
the skills that are redundant, right?
Maybe skills like what you just saw,
that does the same thing, like the PR
reviews or the code summarizer. Maybe
there's a skill that does even better,
right? That replace them all, or even
have a simpler version that, right? By
simply just asking Claude, simply using
the slash
doctor, and just going to trigger that
skill, and that's going to help you
identify exactly what are things that
are redundant, and try to see what we
can do to simplify that, right? So you
can see that here are the group two. So,
code quality you already have natively.
So, you can see that these are the
skills that we have. Group three, the
browser stack duplicates. So, you can
see there are some skills that one using
Playwright, the other one using like
another one like connect Chrome here.
So, you can see that there's different
skills that does the same thing. Maybe
we can go to refactor using just one
single skill, right? Keeping just one
that works using Playwright CLI.
>> [snorts]
>> Right? Or
skills that never been used before,
right?
You know, G stack deploy and planning
that never been used before. Maybe we
can just turn it out, right? So, those
are basically what we can do here. So,
for redundancy here for which redundant
skill groups should I disable? So, group
one, you can see these are the skills we
have. Group two, group three, group
four. So, what we can do here is that we
can actually go to just figure out one
and just going to stick with that,
right? So, for example, for code quality
here, I'm just going to choose that one
and the browser duplications as well as
the deploy and planning. I'm just going
to duplicate remove that as one
that one as well. And just going to
submit here and just going to have
Claude here to further refine that as
well. Okay, so that's another tip is
that you could also using slash doctor
here to figure out what are the skills
that redundant based on the skill list
that we have. And then figure out
exactly how we can go to just keep one
that does the best out of all of them
and see which one actually
don't really need because our model here
is getting so powerful, we can just rely
on the model itself without using the
skill. So, you can see that's exactly
what I recommend here. All right,
[clears throat] so that's pretty much it
for this video on how to improve your
context engineer with the Claude 5
models. Now, if you actually want to
take this even further by reducing more
tokens for your context usage, then you
can check out those two videos right
here. But pretty much that's it for this
video and if you do find value in this
video, please make sure to like this
video. Consider subscribing for more
content like this. With that being said,
I'll see you in the next video.
