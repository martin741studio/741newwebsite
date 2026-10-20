# Claude Code Hooks, Explained Simply.

- Channel: Agentic Lab
- URL: https://www.youtube.com/watch?v=AP7c9YTcaw8
- Published: 2026-08-27
- Duration: 8 min
- Views at fetch (2026-10-11): 33,659
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

I genuinely believe that hooks are the
most powerful feature for coding agents.
Yet, most people don't really understand
them. There seems to be some level of
mystique around them, when to use them,
and how they work. Even anthropic docs
are quite nebulous. But the reality is
they are an extremely simple feature to
understand, and their skill ceiling on
mastery is near infinite. And once you
understand how to actually use them
properly, you can effectively do any
knowledge work with them. stitch
together automations, enforce rules, and
revolutionize your coding agent
workflows. In this video, I'll simplify
exactly what hooks are, how they work,
and relate to agents, and the insane
things you can do with them once you
really understand them. I'm Roman. I
published a top 3% paper at Nurips, the
best AI conference in the world. Now,
I'm on a mission to push coding agents
to their absolute limits. So, let's
start by defining what a hook is. A hook
is an event that triggers a script. The
event answers when should my code run
and the script answers what should it
do.
Now let me break it down even simpler.
Let's say that we wanted to summarize
every single session you have in your
cloud code and put it into a folder of
markdown files aka a knowledge base. So
this would give you that persistent
memory over long term that you can
query. So breaking this pattern into
event plus script language, the event
would be that the session ended and the
script would be something that spawns an
agent to summarize and move it into a
marked folder.
Okay, so now that we understand the very
simple underlying concept behind what a
hook is, how do we know which events we
can choose from that launch our scripts?
And just think of a script as behavior.
Now you have to think in terms of the
agent life cycle aka what are the
different things that happen within a
harness like claude code for example.
The most common examples would be user
submits a prompt claude compacts a sub
aent is spawned a tool is called a
session begins etc. So the harness cla
code in this case would be listening for
one of the events to occur and then it's
going to attach a script to it. That's
why they call it a hook. very very
similar to web hooks in traditional
software development. And since scripts
can effectively do anything or be as
complex as you like, you can imagine why
hooks are so powerful in a tool like
cloud code. Okay, so why do I love hooks
so much specifically? Well, the answer
is simple. A language model is
probabilistic in nature. For a given
input, there's no guarantee of a good
output or even the same output across
many trials. There are no guarantees
with agents and this means that the rule
that you wrote or the many rules that
you write in your claw.mds don't always
get filed and don't get listened to
especially over the course of a long
session. Now a script is the opposite.
We have cheap instant identical every
single time and never created. Hooks let
you add that layer of determinism into
this probabilistic system which makes
them incredibly powerful. They're like
the glue. The docs say it in very
similar language. Hooks make certain
actions quote always happen rather than
relying on the LLM to choose to run
them. And rule of thumb, if the check is
binary and mechanical, it should be in a
hook. But if it needs judgment, you have
to leave it in the prompt level. And
prompt level is something like a
skill.cloud/ruules,
you adding it to your prompt, etc. But
the hook is a layer up and it interacts
in the harness layer where once again a
harness is something like your cloud
code or your codeex or your co-pilot. So
I like to break my prompts for how to
set up hooks into four sections very
simply. Starting with event, we simply
pick from the life cycle events in cloud
code. This will tell us when we would
like to have our script triggered. So
going back to the example from earlier,
let's say that every time the session
ends, we want our hook to fire.
Then we have the behavior. So what
should the script actually do and what
do we want to have happen? So in this
case, back to the example, we want it to
spawn a forked claw-P agent to summarize
this session into my knowledge base.
That's obviously very simple,
simplified, but we would just add to
that more and more to be more clear on
how it should merge, what the knowledge
base is, etc. Then we have to tell it
the why. This helped it kind of
understand our motivations and point it
in that northstar direction it needs. So
this is persistent memory of what I've
worked on and my patterns. So that's why
I want this created. And then finally we
have the edge case. This is built from
intuition and experience or from
previous runs that must be fixed. So I
like to keep these lean as well.
Typically I don't like to give it a
bunch of edge cases. I prefer to eval my
hooks rather than trying to predefine
every single edge case ahead of time.
But the obvious ones I let it know.
Little tip as well, I call it
birectional prompting. You can have the
model ask you a couple of questions
about what you want. Now, mapping this
into a prompt. This is an example of a
prompt I might type into Cloud Code or
Codeex when I'm trying to set up a hook.
Claude handles the schema and the
wiring. So, it really is as simple as
this. So for example, the prompt might
be can we create a session end hook
which spawns a forked claw-P agent to
summarize the session into my knowledge
base. I would say probably on every
session. The point is persistent memory
of what I've worked on and my patterns.
Watch out for knowledgebased bloat and
don't let sub aents or automations
summarize their own sessions. So very
simple there. And claude when it's
outputting it will output a very complex
looking hook like this. But you don't
actually have to worry too much about
all of this complexity. You just have
Claude eat that complexity for you so
that you can focus on the higher level
stuff. So Claude's going to handle the
schemas. Claude's going to handle the
creation of the hook. And you're just
abstracting up a layer. That's what I
always say with agentic coding.
Engineering is not dead. You're just
abstracting up a layer. Now let's talk
about all of the events that you can
choose from that you can mix and match
with hooks. Here's a list of all the
events in clot code. You can take a look
or pause the video if you want. And by
the way, I compiled a list of one
creative/interesting use case for
building a hook triggered by each and
every event in this list. And you can
get it in my free community linked
below, school.com/agentic.
So, in more recent months, hooks have
become even more powerful. Hooks can
trigger an HTTP call, an MCP
[clears throat] tool, a prompt, or even
spawn a sub aent.
And here are some extra advanced things
to consider about hooks. Hooks can be
put inside of a skill or a custom agent,
meaning that a hook will only be active
in a session where you invoked a certain
skill. So, comment below about a
creative use case you could see for this
in your setup because I found that these
are incredibly powerful as a pattern.
Number two, hooks can have matchers,
which is like an if statement at the
hook layer that will only ever run the
hook if the matcher hits. Think about
something like matcher bash, which would
mean that your pre-tool use hook would
only run if the command was actually
bash. Matchers can make it so that your
hooks don't constantly run. Number
three, you can have hooks that spawn sub
aents or even other cloud code or codeex
instances. For example, you could have a
hook that when your cloud code stops,
you spawn a code agent to red team your
implementation and open up its analysis
when finished. So with all this
complexity, here's what to do today. Go
open up your cloud.mmd or your rules
files or whatever you're using to inject
prompts into your agent or rules into
your agents. Read every single line and
ask one question to yourself. Could this
be a hook instead?
So, what you're going to want to do if
you realize that this could be a hook
instead is, of course, pick your
battles, but go install some of these
hooks so that you can remove this bloat
from your claw.md or your rule files.
This is how you actually guarantee the
behavior in your agent. So, if you want
to go further, join my free community,
school.com/agentic.
So, inside is the list I mentioned
earlier where I'm giving every single
cloud code life cycle event and a
creative hook worth building on each
one. It's all in there for free.
