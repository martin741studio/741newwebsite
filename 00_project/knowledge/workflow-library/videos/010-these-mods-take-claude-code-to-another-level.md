# These Mods Take Claude Code to Another Level

- Channel: Mark Kashef
- URL: https://www.youtube.com/watch?v=UcvD53jqHRU
- Published: 2026-10-05
- Duration: 15 min
- Views at fetch (2026-10-11): 38,631
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

All right, so watch this. I'm going to
show you a very interesting example of
using mods to their fullest potential.
I'm going to use Claude Code to use
Codex's computer use to execute a task.
All I have to do is I'm going to do
{slash} codex-cu
and I'm going to say on. Now, this
should be activated and then I'll send
over this prompt right here.
What this prompt will do will make
Claude Code ignore its own internal
browser and instead find and use a
bridge to use Codex's computer use to
execute this task.
So you can see right here, it's starting
to use the computer use module and you
can see the very bottom, it's activated
and we should see it open up the
calculator app. There you go, manipulate
it, take notes of exactly what it
calculates, in this case some
hypothetical subscription, and come up
with a result.
All right, so we sped it up but you can
see here it was able to manipulate the
calculator, write its findings in a text
document, bold it and format it so we
can read it. So in this video, I'm going
to walk you through how I put this
together and how you can too. And I've
got another mod to show you that I think
you're really going to like, especially
if you've ever used something like
Claude and thought, "Why can't it just
do this?" Because now you can build a
lot of these missing features yourself.
So if you want to take your mod game to
the next level, then let's dive in. So
in my last video, I walked you through
what mods are and how they work. But as
a quick refresh, you can think of a mod
as an extra add-on that allows you to
tailor and configure how Claude Code
works for you. You can add a tool,
change how it handles certain tasks, or
give yourself a button of some sort for
something that you always do all the
time and you want to create a shortcut
for. So I wanted to take my basic mods
and go a step further.
Could I use mods to actually add
features that I always wish Claude had
or be able to emulate features that I
really like in Codex that I've been
patiently waiting for the Anthropic team
to put together.
Let me show you how I approached the
computer use one. So, when I sent Claude
that prompt, it had to decide which
button to press. Based on the goal it
extracted from the prompt, it realizes
that it needed to use a mod. And once it
realized which mod to use, it then
passed on this information to use the
set of tools from Codex. And we
basically made these tools available at
the discretion of Claude. So, instead of
having to use Codex models to
orchestrate Codex functions, we could
use Claude to orchestrate those same
tools. So, in this case, when we told it
to use the calculator, Claude
essentially became the brain with access
to the limbs of Codex. And every single
time it clicked or made an action, all
of that information, that visual
confirmation, would propagate back to
Claude that would then make the next
decision as to where it should click
next. And they might be wondering how
it's possible for us to access the tools
that should be only designed for the
Codex app. The main thing to understand
is that a lot of these tools can be
exposed as an MCP. And pretty much any
LLM, not just Claude, can access them if
you build a proper bridge to enable that
connection. Now, I'm going to break down
phase by phase exactly what I asked
Claude to do, but essentially I asked it
to watch Codex, open up and use its
computer use, and basically listen in
for all the services it was using. And I
did this to try to reverse engineer how
I could possibly access these controls.
Once it figured it out, it created a
script that basically is called a
launcher. And this launcher allows us to
launch into the next step. Now, the next
obstacle is if we're going to rent a
tool from another service, one thing
that pops up are permissions. So, Codex
would constantly ask, "Can I use this
tool? Can I click here?" And we needed a
way that Claude wouldn't have to deal
with this over and over again. So, after
pushing it a bit, it created a little
program that allows it to maintain a
live connection to a Codex session. And
this bridge, otherwise known as a
helper, doesn't only allow the
connection to stay open, but handles all
the permission layers behind the scenes.
So, anytime it asks for permission, it
automatically gets an approval from that
session. All right, so with that out of
the way, here's the complete build
prompt. So, the first part of the prompt
is obviously breaking down exactly what
the North Star is. And in our case, I
said very clearly, I want a Claude code
mod that makes you use Codex's computer
use instead of your own whenever I ask
you to do something on my Mac, like use
a calculator or write a note. Codex can
click and type inside my apps in the
background without taking over my mouse.
Now, one annoying thing about Claude is
many times it will tell you that a lot
of these hacky connections aren't
possible from the get-go until you probe
it and you ask it, well, I'm going to
open up the Codex app and I want you to
watch me run a computer use and I want
you to listen in for all the tools that
are being run behind the scenes. Maybe
there's a way for us to access them.
Usually, when you have it run it and
actually check, it'll realize that it's
wrong and it is possible. And that's the
thread you want to pull on to reverse
engineer the rest of the connection. So,
we go from explaining the goal to
over-explaining how to connect to Codex.
So, you'll see here, as an insurance
policy to make sure every single time we
update the Codex app, that this doesn't
break. We always want to connect it to
the latest and greatest version of that
app. Over here, this is where we're
mentioning the launcher and this is
what's connecting to the MCP server and
this is the name of that specific MCP
server that gives you access to computer
use. And like we mentioned, we had a
bridge between Codex and Claude and this
is the instruction for that bridge.
Build a persistent local helper that
acts as an MCP client to that server. It
must initialize the connection, handle
tool calls and app approval requests,
etc. Now, because this is experimental,
we want to make sure that the first time
it uses a tool, that it asks us
permission. Once we tell it you're good
to go, we don't want to be asked again.
So, in this case, we just say make it
ask me before it uses an app for the
first time. Give me three choices, just
like you can see here, allow for this
chat, always allow or don't allow. Now,
maybe sometimes I still want it to use
Claude's internal browser because it's
an easier way for it to check its own
work for a variety of things like going
through an app that I put together or a
webpage it just needs to scroll through.
So, I just wanted to make a way that I
can turn it on and turn it off very
easily, but by default have it on for
every single chat. And one extra note
here, instead of me having to use the
agents API and pay extra, this allows us
to use an existing subscription to the
existing Codex app and not have any
extra cost in between. Now, this next
part is more technical, so let's you
read the prompt as I'm also going to
make this available to you, as well as
the prompt for the next thing I'm about
to show you down the second link in the
description. But, the TLDR is that I
wanted to make sure that if I use this
tool in an existing chat and then I
created a new chat that I wouldn't be
stuck using that tool and having it
focused on servicing that prior chat.
Then obviously, to make sure it works we
have to test it and using a calculator
is probably one of the easiest things
you could do to make sure it's working
end to end. Part seven essentially asks
Claude to create a series of
troubleshooting steps in case for
whatever reason the computer use tool
from Codex misfires. In number eight, I
had AI help me with quite a bit, which
is telling it exactly where these files
should go so I wouldn't have a very
bloated mod library. Now, realistically,
did I take this one prompt and have it
one shot it and work on the first time?
Absolutely not. But, after a few tries I
gave it a slash goal, I told it exactly
what to troubleshoot based on all the
errors it was having and eventually,
maybe after an hour, it finally got it.
Now, obviously for you I'm not going to
make you go down the same rabbit hole if
you want to emulate this exact same mod.
So, I'm going to make available also my
GitHub repo with all the underlying code
so you can take it, plug and play,
retrofit it and do as you wish. Now, the
other mod I wanted to show you and walk
you through is called threats. I know,
I'm not in Claude, I'm in Codex and I'm
here for a reason because I was always
jealous and waiting for a point where
Claude could do this exact same function
that I'm about to show you that I've
shown in prior videos before. Hey, so I
want you to spin up a series of
different threads with different models
depending on the level of intelligence
we need for different parts of this
task. But I want to do a full research
sweep on what are the best models to
combine together. Should it be Opus 5.5
and GPT-6 Astra? What effort levels?
Should it just be GPT-6 models? Should
it just be Opus models? Or anything like
Sonnet 5.5 or Opus 5.5? I want you to
spin up a series of threads, have one
lead thread, and have that lead thread
organize that sub-threads to make sure
they're always reporting back and we
have one cohesive answer at the very
end. Absolute mouthful there, but if I
send this over, the beautiful feature
that it has is it can spin up all of
these threads, name them, run them in
parallel, have a thread that's
overseeing the rest of the threads, and
this becomes a very helpful
functionality at scale. And boom, just
like that, you have five threads on the
go all working together, and this is not
something you can do, at least in the
Claude desktop app. You can MacGyver the
terminal to get the same level behavior,
and obviously you can use things like
Herder if you are more technically
inclined.
But if you just want to use the desktop
app, there must be a better way. If you
go spin up a brand new chat on Claude
desktop and ask it something like, "Can
you spin up threads in the desktop app
with different models if I ask?" And in
this case, I'm telling it to not use the
mod that I've already put together. It
says it can't do that, and the best it
could do is run sub-agents on a chosen
model. But since there's a mod for this,
we could send the exact same prompt, and
I'll say, "Make sure to leverage the
thread mod." And it should be able to
start spinning up the exact same
behavior in a different way from the way
Codex does it. And there we go, it
starts using the threads creation
portion of the mod, and they should pop
up at the bottom left-hand side right
here. You can see right here, it's
beginning the thread process. It pops up
a pane on the right-hand side where we
can keep track of exactly what is
happening, what model is the lead, and
what are the other threads being spun
up, and exactly how much are spending in
the process. And one super interesting
thing is you can add your own, like I
said, buttons, where if I want to steer
the conversation, if I want to steer the
task for all the different threads, I
can do so from one centralized place in
this pane. [music] And there we go. We
were able to spin up all these different
threads and emulate the exact same
experience from Codex, and in many ways
upgrade that experience. Cuz again, we
can manage all of it from here. We have
full transparency. We have all the
transcripts. And we could add a lot more
richness and complexity to this initial
feature. And when they're done, the
unified work ends up in this main chat.
Now again, big picture. Trying to
explain this feature in plain words,
even by having AI meta prompt for me,
was a bit tricky. So what I had to do
was very similar to what I did with
computer use. So I told Claude I was
about to open the Codex app and create
multiple threads from one conversation.
And I wanted it to audit all the logs
from Codex to see exactly what it was
doing, how it was deciding to create
those threads, and how it created it,
most importantly for me, in the Codex
app itself, not just some terminal.
Typically, it's a lot easier to create
this behavior in a terminal experience.
But if you want it on a main UI desktop
app, you have to MacGyver it a little.
So here's the prompt that I sent over,
and I'll go over the most pertinent
parts. So in layman's terms, I told it I
want to build a Claude code mod called
threads. Before you write anything, load
the plugin authoring skill, and
basically remind yourself how mods work.
So go and check your documentation so
you fully context prime yourself before
we take the next step forward. Then I
break down the concept. I want this chat
to be the boss of a small team. When I
say something like start a haiku helper
to list my files and an opus helper to
review my readme, the mod should start
each helper in its own real Claude code
session on the model I asked for. And
ideally, if I tell it to use its
judgment, similar to what I showed you
in Codex, it should be able to do that,
too. Now at this point, I was already
burnt by Claude, so I explicitly told
it, "Before deciding a feature is
impossible, inspect the installed mod
authoring API, the current CLI for help,
and distinguish a missing tool in this
chat from a capability that can be
implemented." So, I started pushing on
it, and I started having it break down,
"How does the Codex app work? And how
does the Claude code app work?" And then
it told me, "There happens to be tools
that manage the sidebar. There are tools
that manage the threads in the chats."
So, then by allowing it to recognize
what tools it has access to, and giving
it the goal, and actually doing a slash
goal, I kept pushing it and pushing it
to realize that this was possible. It
just has to be a lot more creative. Now,
similar to the first mod, we also needed
the concept of helper here as well. So,
in this case, I said, "Each helper is a
normal Claude code session, and if
you're confused on what models you can
use, go and literally use Claude {dash}
{dash} help." Now, in the terminal, this
just allows you to troubleshoot all the
core functionality of Claude, which it
could use itself to remind itself. And
then we spoon-fed it what to look for,
which is setting the model, giving the
session a name, showing it in the Claude
desktop sidebar, in which case we tell
it, "Go and look at the different tools
you can use to manipulate the sidebar,
skip the permission prompts, because
initially it would create a brand new
session, then ask you to go into that
session, click enter to give it
permission to execute that prompt." And
then once you got that working, we went
to the next level of granularity, which
is effort level, and adding extra
instructions. Now, the inspiration for
this pain here didn't just come out by
itself. We actually told it, "To see the
progress of all the threads, we needed
to always have a way to keep track of,
are any of these threads stuck? And if
so, can you keep an eye on it?" So, then
we were able to give it an idea on how
to create and how to log the API
equivalent cost of running all these
extra sessions. Now, these next sections
here go into the devil in the details to
explain how to guide different types of
work, in what order, and exactly what
this might look like in practice. So, in
this case, you might make plan with
Opus. You want to spend your tokens
wisely there. Then, it would leave some
notes. Those notes would then go to
potentially a Sonnet helper. And then,
once Sonnet is done, it might pass it
off for a final check or a final result
by Haiku to take an extra scan. Now, one
really important thing for very
complicated mods is giving it an
explicit set of different things to
test. So, ideally, I gave it a what's
called {slash} goal. And basically, this
does burn tons of tokens, but sometimes
when Claude is refusing or denying that
something's possible, and you throw it a
{slash} goal. In this case, you may get
something specific, which is, "Okay, you
have this feature. I want you to battle
test this. And now, I want you to start
creating one thread, sending it a
message, sending it a step-by-step plan,
and watching it execute till the end. If
that works, let's move on and create two
threads, and so on." So, giving it that
{slash} goal gives it an extra push to
see what's possible and evaluate it. And
one extra nuance here is I wanted to
make sure that every single thread it
spins up was something that was remote
control eligible. So, if I wanted to
walk away from my computer and manage
those sub threads, that I could. And
even this was something that I had to
specify after quite a bit of iteration.
And obviously, there's way more detail
there, but I'll let you read the prompt
for yourself and see what parts interest
you the most. Now, were those super easy
to put together? No. Is it still
possible and is there pretty much
unlimited possibility with what you can
do if you can just imagine exactly what
the goal is, how you want to accomplish
it, and most importantly, how you can
get something like Claude to test its
own work? Yes. And all you have to do is
really take something like all of my
prompts from my last video, this video,
the code, and even feeding all that code
gives something like Claude and Opus 5.5
enough inspiration to take on the next
big hairy task that you want.
>> [music]
>> And that's pretty much it. So, if you
wanted to grab all the resources for
these two mods that I showed you, again,
they'll be down in the second link in
the description below. And as always, if
you want to take your learning to the
next level and go much deeper on topics
like mods, to fully understand how the
system works and how you could apply it,
check the first link down below for my
early adopters community. For the rest
of you, if you found this helpful and
novel, I'd super appreciate a like and a
comment down below. Really helps the
video and the channel, and I'll see you
all in the next one.
