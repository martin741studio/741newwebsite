# Claude Code: The Advanced Guide (99% of Devs Skip These Features)

- Channel: Tech With Tim
- URL: https://www.youtube.com/watch?v=kt5a-TXmWew
- Published: 2026-09-07
- Duration: 19 min
- Views at fetch (2026-10-11): 110,588
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

In this video, I'm going to show you
nine advanced Cloud Code features that
most people don't even know exist. We're
going to go through custom sub agents,
skills, hooks, MCP servers, parallel
sessions with things like Git work
trees, headless mode, and much more.
Now, every single one of these is going
to come with a real demo so you can see
how you would actually use it. And by
the end of this video, you'll be able to
set it all up in your own project. Now,
if you want the references in this
video, I'll leave a link below. You can
join my school community. It is
completely free and I'll have everything
here so you can follow along with a
textbased guide. With that said, let's
get into it and look at the first
feature. So, the first feature on my
list here is custom sub aents. Now, most
people know that Claude is capable of
creating its own sub agents. That means
you can give it a prompt and
automatically it can delegate to other
agents or do things in parallel, right?
So, it can have multiple agents running
at the exact same time. Now, Claude will
do this automatically and it can make
its own agents without you doing
anything. However, you can also create
your own custom sub agents that Claude
can then invoke. Now, the way you do
that is you create a doc folder. You
then create a nested agents folder and
inside of there you create some markdown
files that specify what the agents are.
So, you can see I have two here. I have
a debugger agent and a reviewer agent.
And the format and syntax looks like
this. Now, you don't need to manually
write all of this yourself. You can tell
Claude to create the agent spec for you.
But when you have this, it will specify
a list of agents that Claude can then
invoke. So you'll notice we have a
reviewer and a debugger. And for these,
we have a name, description, the tools
that they're allowed to use, as well as
optionally the model that we want them
to run. This can be helpful, especially
if you're running a lot of sub aents to
reduce the cost. So once we have those
set up, what we can do is run Claude
inside of our project. So I'm inside of
the sub aents folder here. And if we
want to make sure that these sub aents
are appearing, we can run /context. When
we do that, it should show us here that
we have two custom sub aents. You can
see they're specified right here. And
then if we ask Claude to do something
that would involve invoking the sub
agents, you should see it spin that up
automatically. So, for example, I may
say something like, please review this
PR before I merge it. Tell me if there's
any issues. Okay, let's go ahead and
press on enter. And we should see that
it pulls up our reviewing sub agent here
and does that automatically. Boom. So,
you can see I'll have the reviewer agent
examine. And then you can see that it is
calling the reviewer sub aent and
running that in its own thread. Okay. So
we can see the review agent is done and
then we get back the overall response.
And effectively what claw does here is
it will invoke the sub aent and then it
will only take the response from that
sub aent and bring that into context for
the main thread that we're currently
chatting inside of. The reason this is
important is it means that our main
thread stays a little bit leaner. So we
can have separate context windows for
each of the individual sub aents that
only need to know what it is that
they're specifically working on which
typically will give us better accuracy
than doing everything in one massive
thread where when we start getting near
the context window limit as you guys
probably see the agents start to get a
lot dumber. So that's custom sub agents.
I would only create them when you want
to delegate things out of the main
thread when you want specific rules to
be set up in terms of tools read only
you know models to be used etc. but they
are super useful and you can create them
in the way that I showed you. Moving on,
we talk about skills, but I'm going to
show you some advanced features that you
haven't seen before related to them.
Now, if you're unfamiliar, a skill is
just a markdown file that outlines a set
of procedures or a set of steps that are
kind of like a reusable workflow. Rather
than constantly telling the model to do
the same thing over and over again, you
create a skill. So, it's kind of a
reusable workflow and then you can
trigger it. Now the model can
automatically call the skill and it will
discover it when it needs to use it or
you can manually invoke the skill
yourself and force the model to go
through the process. Now that's actually
the first feature of skills that I want
to talk about here. First skills sit
inside of doclaude/skills
similar to how we have this agents
folder for the sub agents. You can make
them manually by writing them yourself.
You can ask the agent to create them for
you or you can import them from
something like a GitHub repo or someone
else's skill that's already been
written. Now when you create the skill
you'll see that you can have a name and
a description and this is the only thing
the model will see before it decides to
invoke the skill. Now inside the skill
you then have all of the steps. Now
another interesting thing you can do is
add this flag called disable model
invocation to your skill which most
people don't know about. Now what this
will do is actually tell the model
whether or not it can call this skill
itself or whether you have to invoke it
manually. So when you set this to true,
essentially that will prevent the agent
from automatically loading the skill. So
it won't sit inside of the context. And
this will only be used when you invoke
the skill yourself. So I'm going to show
you what I mean by that. But if I go
into my terminal here and I invoke
claude from this folder first, we can
type /sklls and see all of the ones
available. So you can see that we have
this deploy skill and this roll back
skill. These are projectbased skills, so
they're just available in this specific
folder. And you'll see that one of them
is locked because I have that disable
model invocation. Now, if I want to
actually run that skill, I can invoke it
manually by just typing / rollback and
then it should go through the process of
actually invoking the skill. Now, I'm
just going to cancel it for right now
because I don't want to do that.
Alternatively, if I want to run a
different skill, so let's say maybe the
deploying skill, I can actually add an
argument to this when I run it. So,
slash deploy and then staging. So, you
don't just have to do the slash command.
You can say afterwards what you want to
be done. Then again, Claude should find
the skill, discover it, figure out what
needs to be done, and then go ahead and
actually run the entire process. I'm not
going to walk you through the full
thing. I'm sure you guys understand what
skills are. I also could tell Claude to
do something that would involve invoking
the skill, and then it would just figure
it out and call the correct one. Point
is that they have a few more features. I
wanted to show you that kind of locking
uh feature, which is quite useful when
you want to have to manually invoke it
and not accidentally have the model do
it on your behalf. So, the next feature
to talk about is called hooks. Now, this
is a much more advanced feature. It
really deserves its own video, but I'll
quickly cover it here so you can look
into it more if it seems useful. Now,
Claude has a bunch of different events
that will happen throughout its agentic
loop. The events look something like
this. And while they look a little bit
confusing, you can at least get an idea
of kind of the flow. For example, we
have session start, user prompt, submit,
pre-tool use, right? You get the idea.
And all of these things will occur
throughout some kind of process while
you're using clawed code. Now what you
can actually do is you can hook into
these events and you can trigger a bash
command to run whenever these events
occur. So for example if we scroll down
you can see all the events like session
start setup user prompt submit whatever.
So you can do something like hey
whenever it's set up I want to
automatically create a markdown file or
I want to automatically test my
application or hey after we use a tool
or before we use a tool I want to make
sure that tool is permitted. You get the
idea. Okay. So there's a lot of
interesting stuff you can hook into here
to customize how claude works. And the
way you do that is by writing a config
file that looks something like this. So
let me show you an actual example here
on Windows. You can see that this is an
example of a config file that you can
create right inside of a hooks folder
inside of claw. So what you'll do if you
want to create hooks is you'll create a
cloud folder. You'll create a hooks
folder. You'll create a settings.json.
And then the hooks can include different
files that you want to actually run or
different scripts that you want to run
when an event occurs. So for example,
what we have here is post tool use and
pre-tool use. And what will happen here
is that we're going to match against
edit and write. And whenever there's a
tool that has edit or write, we're going
to run this Python claude hooks format
hook.py Python script. So that's going
to automatically format all of the code
for us before any tool is ran or sorry
after any tool is ran. Then we have
pre-tool use. And what this is going to
do is run the block dangerous. So what
that's going to do is it's going to
block any dangerous commands or whatever
from being ran before it allows those to
run. So if we have an exit code too,
that means block the tool calls so that
it cannot work in claude. I'm not going
to go through exactly how you set it up,
but the point is we can have these hooks
and I'm going to show you now how they
actually work. So let me get out of
claude. Let's change into the other
directory which is 03 hooks and let's
run claude and give it some prompts. You
can see how they trigger. Okay, so we're
just going to say something like add a
function called get average age to
messy.js that returns the average age of
all of the users.
Okay, and let's see what we get here. So
we can see we're reading a file messy.js
searching for a pattern. Okay, so we're
going to go yes, we do want to allow
this. So let's proceed. Okay, keep
going. Read file and we should see that
the hook will actually trigger now
because it's gone with that process.
Perfect. So you can see the post tool
use hook then ran prettier on the file
automatically. So the whole file got
reformatted after my edit. So you can
see this ran right both our hooks went
through and essentially it just worked
right. So we didn't need to do anything.
It just automatically formatted the
file. And if we go back here maybe we
can have a look at uh let's see here
message.js and you can see that it was
formatted. So the next feature I want to
show you is related to MCPs or model
context protocol. Now, these are servers
that you can add inside of Clawude that
allow you to connect to external tools.
Of course, there's tons of different
MCPs that are worth adding, and I'll
make an entire video on that. But one
that I want to highlight here that I've
been using a lot recently is Granola.
Now, they've kindly sponsored this video
and been a long-term partner of the
channel, but this is an AI note-taking
app that I use pretty much every single
day that automatically transcribes your
meetings without joining your call. So,
rather than having that little annoying
noteaker that joins in, it just sits on
your computer. It reads your computer
audio and it keeps track of all of your
notes, keeps track of your calendar and
sends you reminders and then saves
everything in a nicely formatted way so
you can view it and also pull it into AI
to have additional context. So earlier
this year they actually released an
official MCP server. You can see I'm
connected to it right here. It allows us
to query all of the different meetings
and I want to show you just in live time
how it works. Using the Granola MCP
server, tell me what I learned in my
most recent Indonesian lesson. And
that's because using Granola, I actually
automatically transcribe all of my
lessons with my teacher. So, it should
tell me some words that I actually
learned here. Let's see. Cool. So, we
can see it pulled the most recent
transcript and gave me all of the
information. Now, we'll just open up the
UI so you can see what it looks like.
Notice that we have the Indonesian
language lesson and a bunch of other
stuff that I was going through and you
get the point. Granola is great.
Download it from the link in the
description. And now, let's move to the
next feature. So, the next feature to
discuss here is work trees. Now, this is
super useful whenever you're going to
run Claude in parallel and you want to
make sure that agents aren't changing
things that other agents are working on.
It's effectively essential if you want
to have multiple agents that are working
on the same pieces of projects. Now,
workree is really an isolated copy of
your project that's on your own
computer. It's similar to something like
a git branch, but it differs just
slightly and works better with agents.
Now, you don't really need to understand
the mechanics of the work tree, but what
you need to know is how to invoke one
and create one. Now Claude will
sometimes do this automatically for you
but you can do it manually and it's best
practice to create it on your own. So
for example I'm inside of a folder you
know work trees right where I have a
quick demo set up. What I can do is run
claude but rather than just running
claude I can add this work tree flag.
Now for the work tree flag after this I
can do something like fix delete bug.
Now what I'm doing is giving this work
tree a name. And when I go ahead and
press on enter here, Claude is now going
to be running inside of my folder, but
inside of this work tree. So it's on its
own isolated version, which is
essentially a copy of whatever was
inside of my project. And from here, I
can give this a prompt. So let me just
copy this in. Read bug.md. Reproduce the
bug, right? Find the root cause and fix
it. And at the same time, I can create a
new work tree in another terminal. So
claude workree. And let's go maybe
feature dark mode or something because
we want to add a dark mode feature. And
again, I'm just going to copy in another
prompt. From here, let's put it in this,
I don't know, auto mode. And same thing
here. Okay. So, let's go yes and just
put it in auto mode. And you'll see that
both of these are now going to work in
their own repo or own copy of the repo.
So, they're not accidentally going to
mess something up. All right. So, we can
see that both of the agents have
finished. So, now let's just open up
another cloud code session here. This
one I didn't put in a work tree. And I'm
going to say, can you find all of the
changes that have been made across the
different work trees for this repo or
for this project and tell me which ones
are there and just ensure that they are
actually in isolation and then I want to
combine them together. Okay, so let's
press enter here. And by the way, if you
guys are wondering what I'm using to
dictate, I'm using a really cool tool
called Whisper Flow. You can see I have
almost 300,000 words at this point. I
use it literally every single day. I do
have a partnership with them. It's free
to try out, so I'll leave a link to it
in the description, but it's just the
fastest way to work with AI, as you guys
can see from my own usage. So, anyways,
would highly recommend from here. Let's
go. Yes, I'm just going to put this in
auto mode, so it can run. And let's see
what it tells us. So, you can see right
away that it found both of the work
trees, and now it's inspecting them. And
then what we'll be able to do is
actually combine these changes together
without losing anything or messing up
either one of these branches, right,
that we're running in isolation. Okay.
And we can see it was able to kind of
reconcile all of this together. And now
it told us what was in both work trees
and then it combined them or merged them
so that now everything is in this one
repo. Anyways, that's work trees.
Definitely use them especially when you
have multiple agents. So the next
feature I want to show you here is
headless mode. Now this allows you to
run claude without actually being in the
interactive terminal which is super
useful when you want to use this as a
part of something like a bash script or
kind of a one-step process. So I'm just
going to show you a few really quick
examples and of course if it's going to
be useful to you, you'll know. So you
can see that I'm inside of the headless
folder and what I'm going to do is
actually let's make sure we get the full
thing. I'm going to run the cat command.
So this is just going to log out
whatever is in this build log.txt and
then it's going to pipe that into this
where we have claude-p which essentially
is prompt and then we place a prompt
right here. So what's going to happen
when I run this is claude is going to
run but it runs in headless mode where
it's not opening up the interactive
window for us and it just gives us the
response. So I was able to take the
result of the build log. I was able to
include that as part of the context in
this clawed prompt and then just tell
it, hey, you know, why did this fail?
And then it gave me the response right
here directly in my terminal, which
means you can then use this as a part of
other scripts. Now I'm going to show you
even how we could use this with
something like JSON. So for example, now
I said, hey, I want the output format to
be in JSON, and I want to use jq to
actually parse out the result. And now
we're going to have this in a format
where I can use it more kind of reliably
in a script. So here you can see build
failed gives us the errors. You get the
idea. Now let's have a look at maybe
some of the metadata here. So same thing
I'm going to do this again. Summarize
this build failure in one sentence.
Output format JSON. And notice this is
what the result looks like. So we get
the result. We get the total cost, the
number of turns, and then the duration
in milliseconds. And of course the cost
doesn't really make sense in this
context cuz I have the subscription. But
you get the idea. Let's do one more. So
maybe I want to run this, but I only
want to allow it to read something. So,
I don't want it to actually have access
to a bunch of tools. I can add allowed
tools read. The reason I'm showing this
to you is that you don't need to use
cloud from the interactive terminal. You
can trigger it from scripts. You can run
it on one-off prompts using this
command, which I always thought was
really useful. So, to kind of prove what
I mean here, notice that I wrote this
triage script. And you can see that what
we actually do here is we run this
clawed headless mode automatically and
then get the result and print it out.
Now, I'm not going to run this script,
but the point is I can do something like
this where I'm actually triggering it
inside of a script. All right. So, the
next feature that I want to show you
here is checkpoints and rewinding. Now,
in order to do this, I'm just going to
do a prompt in a new example that I have
here where where I tell it to rewrite
app.js from scratch as a single tip
calculator class. We have like, you
know, a quick kind of React example or
whatever. And we'll just give this a
second here to rewrite it. And I want to
show you how I can roll back so we can
actually go back to different
checkpoints in case Claude makes a
mistake. So this is effectively the app
I had. Super simple, right? Where we can
just calculate the tip based on the bill
amount splitting between a certain
number of people. You get the idea. Now,
let's do one more prompt here where I'm
just going to tell it to rename every
function and its ID and not to touch
index.html. And hopefully I'm going to
have this actually break the app so I
can show you how we can roll back to a
working version. So now you're going to
see that actually the app is completely
broken. and if I try to do anything, it
just doesn't work because I
intentionally broke it. So, let's say
you were to do that, but obviously
unintentionally, and you wanted to go
back to a previous point. Well, Claude
will actually checkpoint different
builds for you. So, what you can do here
is you can use the command slashre.
Now, when you do that, it's going to
show you whatever was in the current
conversation, and you can go back at any
point. So, we have current, we have
rename every function, we have rewrite
every app, whatever. So, I'm going to go
to rewrite, and I'm going to go restore
code and conversation. And now it brings
me back to this stage where if I go back
to my application here and I refresh.
Okay, let's put in 100. And you can see
now the app is working. So basically
just understand that you have that /re
feature. So you can always roll back in
case you make a mistake. Now this next
feature is super useful when you want to
go back into an old conversation that
you had in a particular project. So
let's say I go into I don't know three
hooks, right? And I want to go back into
the previous conversation that we had at
that point. Well, in order to do that, I
can actually just type claude- continue.
Now, this is going to bring me back into
whatever that conversation was because
the session is stored and saved on our
machine. There's actually multiple ways
to get into different sessions, which
I'm going to show you in a second. But
the point is that you can do this,
right? So, you don't need to always
restart a new session. You can resume
different sessions. You'll even notice
here that it has various IDs for each
session, which you can manually invoke
to get back into regardless of what
directory you're in. So now that you
understand continue, let's talk about
being a little bit more proactive with
our sessions. So you saw that random ID
we had for sessions previously. That's
great. But you can actually name your
sessions as well. So for example, when I
run claude, I can do dash n and then
call this something like o refactor. Now
I've just named the session o refactor.
So it's always going to be saved as
that. And again, I can give this a long
prompt. So let's paste something in like
this. And notice in the bottom right of
my screen that it shows us what session
we're in. We'll just put this in auto
mode so we can go. So I'm going to say
look at source uh you know ojs make a
change whatever and then we can get out
of this session and come back into at
any point that we want. Okay. So let's
get out of this and I'm going to show
you again if I want to resume this one I
can do claw d-res and then off refactor
and it's going to bring me right back in
to where I was before. There's some
other interesting stuff we can do in
here. For example, we can use slash
branch. Now when we do that it's going
to create a branch of the current
conversation but not override this
session. So when I do that, notice that
I'm now in a branch. Okay. And then I
can ask it to do something that's maybe
risky that I want to potentially have to
get back to the main conversation for.
So let's say actually scrap incremental
changes, rewrite the entire module as a
class with static methods and see how
that looks. Okay. And you can see that
we're now working inside of this branch
of the main conversation. Okay. So this
is finished. And now what I can do if I
want to go back to the original branch,
so not the one that I just branched off
on, I can type slashres and I can go
back into this before the branch. So we
no longer have those changes that were
applied. And then same thing, I can go
sloom here and you can see we have the
branch and I can go back into that. The
point of me showing this to you is that
you can be really clever how you manage
sessions inside of Claude. There's
actually a lot more that you can do that
I haven't shown you in this video
because it's meant just to be kind of a
quick run through, but you can name
them, you can branch them, you can
resume them, you can go in and out of
them, and you can be really clever and
have a lot of parallel work going on
that's also going to be safe. So anyways
guys, with that said, that's going to
wrap up this video. If you enjoyed,
leave a like, subscribe, and I will see
you in the next one.
