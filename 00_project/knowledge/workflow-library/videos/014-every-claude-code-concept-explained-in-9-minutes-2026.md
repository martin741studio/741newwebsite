# Every Claude Code Concept Explained in 9 Minutes (2026)

- Channel: Tech With Diego
- URL: https://www.youtube.com/watch?v=qlT4NyuWClU
- Published: 2026-09-30
- Duration: 9 min
- Views at fetch (2026-10-11): 19,431
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

Claude Code. In this video I'm going to
explain every Claude Code concept.
[music]
From prompts and tokens to context
windows, skills, hooks, sub agents, and
more. [music] This is going to feel like
an adventure. Along the way, we are
going to collect commands for our
inventory because once you understand
the concept, using the commands makes
more sense. And by the end, you will
have everything you need to [music] use
Claude Code way better. My name is
Diego. I'm a senior DevOps engineer
based in Paris, and I like breaking down
thick concepts into simple and visual
explanations. If you want to see more
videos like this one, feel free to
subscribe. [music] And that's all. Back
to the video. Claude Code is an AI
coding agent made by Anthropic. You give
it instructions in natural language, and
it reads your files, writes new code,
edits [music] existing code, and runs
commands, all by itself. You probably
already use Claude Chat, [music] the
classic one in your browser. You ask it
questions, it gives you answers. But
what makes Claude Code more powerful
than Claude Chat? The answer [music] is
where it runs. Claude Chat runs on
Anthropic's servers. It can only see
what you type or share into the chat
box. Claude Code runs on your machine.
That's why it can open your files and
execute commands.
>> [music]
>> And that's pretty cool. So how do you
actually open it? There are three ways.
Your terminal, your IDE [music] like VS
Code, or the desktop app. No matter
which one you pick, it's the same Claude
Code running [music] behind. Now that
it's open running, time to talk to it.
Prompts. Prompts are the messages you
send to Claude. They can be super short
like fix this bug, or really long and
specific like this. [music] The more
specific, the better. You can also use
the at symbol to mention a specific
files or folders. But every time you
send a prompt, it costs something.
Tokens. [music]
A token is a piece of a word. Common
words like sun fit into one token, but
longer words like unforgettable get
split into smaller common patterns like
this. [music] Every input you send,
every file Claude reads, and every
response it generates, [music]
all of that is measured in tokens. And
tokens cost money. To check how much you
have spent during your conversations,
type {slash} [music] usage. That's the
first command for our inventory. And
those conversations that we mentioned
have a name,
>> [music]
>> sessions. A session is one continuous
conversation with Claude. You open it,
you talk, you [music] close it. That's
one session. And here, we just found a
new command for our inventory, {slash}
resume. It lists all your previous
sessions
>> [music]
>> and lets you pick the one you want to
continue. But don't try to do everything
in one session, because each session has
a limit. And that limit is called
context [music] window. The context
window is how much Claude can remember
during a single session. And that space
[music] is not infinite. {Slash} context
shows you how much of the context window
you have used in your current session.
And you don't want that bar to fill up.
[music] Let's just say things get ugly.
Context rot. As the context window fills
up, Claude starts forgetting things that
happened at the beginning of your
conversation. It might forget a decision
you made [music] or write code that
breaks something it already fixed. But
what can you do about it? {Slash}
compact summarizes the entire session
into something smaller. You keep the
important [music] stuff and you get a
lot of space back in your context
window. And {slash} clear erases the
whole conversation. Fresh start with
zero context. It's basically the same
thing as creating a new session. [music]
And just like that, two more commands
for our inventory. A cool thing about
the context window is that [music] its
size depends on the model we are using.
But what is a model? A model [music] is
the brain behind Claude code. And there
are different brains to choose from.
They differ in a few things, how smart
they are and how large their context
window is. Bigger models think better,
but cost more per token. Smaller ones
are cheaper, but less capable. To switch
between them, use /model. And a /effort
controls how hard the model thinks.
[music]
Low for simple tasks, high for complex
ones. So, now you have a smart model
thinking hard running on your computer
with [music] access to all your files
and system. Maybe we should set some
limits before things get crazy.
Permissions.
>> [music]
>> This is where you decide what Claude can
touch on your machine. An allow list for
things it can always do without asking,
[music] and a deny list for things it
can never do. You can use a /permissions
[music] to see and change those rules.
But, there is a faster way to do this.
Modes. A mode is one setting that
changes how much Claude asks you. There
are a few of them. Manual. It [music]
asks you before every single change.
Slower, but you approve everything.
Accept edits. [music] It writes and
edits files automatically without
asking. But, it will still ask before
running other type of commands. [music]
Auto. Claude decides by itself when it
actually needs to ask you. For risky
[music] commands. Plan. Here, Claude
doesn't change anything. It reads your
code and gives you a plan first,
step-by-step, and you decide if approve
it or not. You can cycle through these
modes with shift [music] tab. One of the
first limitations we learn when we start
working with LLMs is that each session
starts [music] as a blank page. So,
every time you have to explain your
project from a scratch. [music]
Claude.md. It is a file you write, and
Claude reads it automatically at the
start of every single session. Things
like which tools your project uses, like
React and Postgres, the way you like
your code written, and any other rule
that is important for you. You have a
global one in your .cloud folder that
applies to all your projects, and a
project one that lives inside each
project folder. You can generate this
file automatically using [music] a
{slash} init. Claude will read and
analyze the full project and write the
Claude.md itself. If you open your {dot}
Claude folder, you will see another file
[music] in there, memory.md.
Claude writes this one itself. It is
where it saves what it learns while
working [music] with you. You don't have
to touch it, but you can type {slash}
memory to see what is inside. So far, we
have Claude doing a bit of everything,
but for some tasks, you need [music] a
specialist. Like in every good
adventure, you get to pick a class, like
a mage, a scientist, or a blacksmith.
Skills. Skills turn Claude into any of
those.
>> [music]
>> A skill is a predefined set of
instructions for a specific task. You
can have a code review skill, a security
review skill, a documentation skill.
Each one tells Claude exactly how to
approach that type of work. But there is
a problem [music] with skills and the
way LLMs work in general. You cannot be
100% sure that Claude is going to do
exactly what you asked. It's not
deterministic. So instead of depending
on probabilities, we can guarantee it.
Hooks. A hook is a script that runs
automatically every time Claude does
something specific. A hook has two
parts, when it runs and what it runs.
Let's [music] say you want the test of
your application to run every time
Claude finishes [music] a task. You
could write that rule in your Claude.md
and hope Claude remembers. Most of the
time it will. Most of the time. Or
instead, [music] you can create a hook.
When Claude finishes a task, it will run
the script containing your tests every
time with no exceptions. Next, [music]
MCP, Model Context Protocol. MCP is an
open standard for connecting AI tools to
external services. This is how you You
Claude code with tools [music] like
GitHub, Notion, Slack, and more. You can
manage those connections with /mcp. So,
now we have skills, hooks, [music] and
MCPs. If you group all that into one
package, you create something called app
login. So, Cloud is pretty well equipped
by now, but it's still doing one thing
at a time. Sub agents. Cloud Code can
launch [music] sub agents. Each one gets
its own context window, its own task,
and they can run in parallel. An
important concept when using sub [music]
agents is work trees. A Git work tree is
an isolated copy of your project. Each
agent should work on its own copy
[music] to avoid conflicts. And when
they are done, you merge the results. To
create sub agents, you just ask Cloud
something like, "Let's tackle this task
in parallel with multiple sub agents."
[music] And with that, our adventure
comes to an end. We learned a lot of
concepts and collected a lot of
commands, but this is just the
beginning. With Cloud Code, you can go a
lot further, like running [music] loops
so it keeps working on its own, or
running it in headless mode. But that's
for another video. If this video helped
you understand Cloud Code better, let me
know in the comments. Even a short
comment helps the video reach more
people. I will appreciate it. Thanks for
watching and see you in the next one.
