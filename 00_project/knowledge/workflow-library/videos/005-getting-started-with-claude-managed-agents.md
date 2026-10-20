# Getting started with Claude Managed Agents

- Channel: CJ Avilla (cjav_dev)
- URL: https://www.youtube.com/watch?v=g1QfVjyrWzg
- Published: 2026-10-07
- Duration: 6 min
- Views at fetch (2026-10-11): 13,488
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

So, I've been talking to a lot of people
about Claude managed agents and I think
it's really really powerful, but I don't
think many people have even really seen
how to get started or how to set up a
Claude managed agent directly through
the Claude console. And so, I wanted to
just log in and walk you through what
that looks like. It's super simple. So,
we're going to log in to
platform.claude.com.
Just recently, you're able to use your
API credits from your Max or Teams
subscriptions for platform features. So,
you can use the API or you can use
Claude managed agents. And so, I think
this is like a really great time if you
are a Claude Code Max user and you've
never used the API and you've never seen
Claude managed agents to jump in and
give them a shot. An agent is
a persisted versioned config that gives
you a model, a system prompt, and some
tools. So, I've got a code reviewer, one
that gives me a brief for what's kind of
happening on social media channels that
I'm listening to. I have an agent that
helps me manage my website. I've got one
that helps me generate podcast episodes
based on blog posts that I'm interested
in. So, lots of different agents. A
great place to start with managed agents
is in this quick start view. You can
describe a kind of agent that you want
and Claude can generate one for you or
you can start with one of the quick
start examples. So, here we'll start
with deep researcher. But, what I really
wanted to show you was the agent config.
So, this is some YAML that is going to
configure the agent. Um the it's going
to have a name. Here, it's called deep
researcher, a description. We set the
model ID and what effort we want to run
at. And then, you give it a system
prompt. You can also give an agent a set
of tools and some metadata if you want.
I'm just going to say, let's use this
template. And Claude is going to walk us
through a few different steps for
getting started with our deep researcher
agent. An environment lets you control
things like
do you want to allow certain network,
you know, domains for outbound access or
do you want it to be unrestricted? So,
for a deep researcher, I might want this
to be unrestricted because I want the
agent to be able to go out and crawl the
web to find more information about
certain details. Now, it has a plan for
what it's going to create for that
research environment and now it's ready
and it's unrestricted. Now, it asks if I
want to start a test sessions. We can
say, yeah, go ahead, start a session.
Now, a session you'll be familiar with
like a conversation or like when you
chat with Claude. Each of those sort of
like chat sessions where you have many
messages back and forth is very
analogous to the session that's running
with your agent. The difference is that
your agent has access to lots of tools
and MCP servers and often times these
sessions are not kicked off necessarily
from you chatting with it, but it might
be from different signals. Maybe there's
like a webhook notification or it might
be based on like a cron job that you've
set up. Another thing that's kind of
interesting about Claude and agents is
that it's a great way to deploy
tools and like agentic features into
your software and so you might kick off
these sessions by making an API call to
create a session. Let's go look in the
agents view here. You'll you'll see this
new deep researcher that we just created
and again you'll see the description,
the system prompt. If we want to, we can
change features of this so like and
every time you save a new version, you
get updated to a different version and
if you want to, you can always roll back
to a previous version. So, I also want
to talk about tools, skills and
multi-agent. So, tools by default, you
can set up this built-in set of tools
and this gives your agent access to
bash, read and write. You can like read,
write, edit files, look for files. You
can also search and fetch things from
the web and you can also add MCP
servers. So, for example, for our deep
researcher here, maybe we want to allow
it to like look in our Google Drive and
we don't actually have to like set up
too much auth or anything. We can just
say like "Yeah, I want to use the Google
Drive MCP server and I acknowledge that
this is what I want to use." And you can
give it a vault. So, a vault is a a
place where you can store vault
credentials so that um
when the agent is running, if it tries
to access an MCP server or an API, it
can like swap those vault credentials at
the egress point so your agent never
actually has access to your keys, which
is like a really important kind of like
safety consideration. Um once this is
kind of like
configured, now we have access to Google
Drive. So, we've given our agent an MCP
server. We can also add skills. So, if
we want to, we can go through I have
like a bunch of skill skill like custom
skills that I have built around my brand
voice. There's also some built-in ones
for working with PowerPoint and Docs and
other things like that. Um so, uh one of
the things that I might do is say uh
let's give it my brand voice just so
that it uses my voice when it's
generating reports.
Multi-agent is also really interesting.
So, there's lots of different
multi-agent kind of like ways you can
orchestrate this. One is you can add a
team of sub-agents. So, maybe you have
this deep researcher and you want to
give it a sub-agent that specializes in
looking at Reddit or looking at um you
know, Twitter or something like that.
But, let's stop there and we'll start a
new session and uh this time we'll just
say like, "Yes, I own the vault.
Research cool travel spots in Paris."
I'm going to use my deep research
environment. It's got access to Google.
And if I want, I can set a budget. So, I
can say like, "Don't spend more than $5
on this." So, say create session here.
Research cool spots to visit with my
family. So, we've got this deep
researcher. It's generating um You can
see like a a set of events that are
going to fire. So, the dashboard here
just gives you like a really handy way
to inspect and look at all of the events
that are being emitted and what the data
might include as part of those events.
You can see what tools are being called,
which resources are being read and
written to, and then uh all the
different threads. So, though you'll see
there were a few web searches were fired
off. There was some thinking that
happened, and then a report was printed
out um telling me about this.
So, real quickly, on the left you'll
also see deployments. This is a way to
like schedule runs to go and fire on a
cron basis. So, maybe we want to get a
report every day about what's happening
on
um our social media platform or We
didn't talk about memory stores yet, but
you can create a memory store, and this
gives um your agents a place to kind of
like take notes in between sessions, so
that at the end of one session they can
write down um what happened in that
session, and then you can also um have
future sessions mount those same memory
stores. Um so, memory stores can be
really powerful. That's just like a
super quick and dirty overview of Claude
managed agents, and uh yeah, if you have
questions, just drop them below or hit
me up on Twitter, and um
yeah, uh if you built something, please
let me know. I think it'll so I'm
excited to see what you'll build.
