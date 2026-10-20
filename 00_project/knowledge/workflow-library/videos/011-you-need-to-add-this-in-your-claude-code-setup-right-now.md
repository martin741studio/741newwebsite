# You Need To Add This In Your Claude Code Setup Right Now

- Channel: AI LABS
- URL: https://www.youtube.com/watch?v=i6Q7bXnWGlM
- Published: 2026-10-05
- Duration: 16 min
- Views at fetch (2026-10-11): 35,153
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

Claude Code has a lot of hidden settings
and most people don't know they exist,
even the ones who open it every day. So,
we went through every setting and picked
the ones that changed how we work. One
of them is a setting that even the
people who build Claude code use
themselves and it completely changes a
command you probably run a lot. Another
one fixes the biggest problem with
running more than one session on the
same project. And there's a command that
teaches Claude how you work, so it
performs better. We also found some
keyboard shortcuts for the little things
that get in your way when you write a
prompt. If this is your first time,
we're a software company and this is our
channel AIAs. And in this video, we're
going to show you each of these hidden
settings and how to use them. [snorts]
Starting with the one setting that
creator of Claude Code themselves use in
their project, which is a fix toinit
command. This command writes claude.md
file for you. To do that, it reads your
project first and then writes down
everything it learns from it. But that's
a problem because the claw.md file is
only for the things the agent needs to
remember all the time. So if the agent
can learn something just by reading the
code, it doesn't belong in that file. To
fix this, there's a setting called
claude code new in it. You need to set
this to one in your terminal right
before you type the claw command to
launch claude code. It has to go before
the claude command because this way the
session can access this setting. With
this setting on, init straight away like
it did before. Instead, it asks you a
few questions about how you work. First,
it asks if you want to improve your
current setup or start fresh and if it
should make skills and hooks. Then, it
also asks how you use Git and how you're
planning to put your app online. From
your answers, it makes a small plan and
waits for you to check it. When you
approve the plan, it starts writing
everything. When it's done, your claw.md
file is a better one that has your own
way of working in it. And it also
creates skills and hooks to give you a
better starting point. If you're working
in another coding agent like Codex or
Cursor, you might already have a setup
there with the MCPS and instruction
files you've set up for that agent. If
you want to move all of that setup to
claude code, you don't need to start
from zero. Instead, you can move that
setup into claude code using the import
command. To use it, you just need to run
import with the name of the agent you
used before. Claude code will then show
you all the things it can copy,
including your instruction files for
that agent and the MCPS you've connected
to it along with anything else you've
set up there. Then it waits for you to
choose which settings you want to
import. After that, it makes a skill
that contains all the instructions to
copy the things you've selected and uses
that skill to copy everything into
clawed code. So you can use the same
setup you had in your previous agent in
claude code as well. No matter how
carefully you set up your claw.md and
other project files, they still get
outdated over time. That's because the
models keep getting better. So many of
the instructions you wrote for older
models don't help the new ones anymore.
Instead, they just fill Claude's context
with things it doesn't need, which makes
the models answers worse instead of
better. Your setup probably has many
skills and claude.md files. If you
changed all of them one by one, it would
take a very long time. So, there's a
command that checks them for you. To use
it, you type the clawed API command and
then add prompt audit after it. This
command reads your whole setup and uses
sub aents to check each part of it. Then
it gives you a report of every problem
it found along with the fixes it
suggests. When you ask Claude to apply
those fixes, your setup only keeps the
instructions that still help Claude.
You'll need this the most right after a
new model comes out because that's
usually when the most instructions
become outdated. Just [snorts] like your
instructions files, you need to
frequently update your skills, too. Most
of the skills that you have set up don't
even get used very often, but they still
sit in Claude's context for no reason.
To find those skills, there's a command
called skill doctor. It shows how often
each skill gets used and when it was
last used. It also shows how many tokens
each skill takes in the context window.
With that list, you can ask Claude to
delete the skills you don't use. Then
only the skills you use stay in Claude's
context. There's also a skills command
that lists every skill you have. And
when you press T on your keyboard, it
sorts that list by how many tokens each
skill takes in increasing order. So you
can tailor your setup accordingly. But
before we move on to the next setting,
it would be great if you subscribe to
the channel and hit the hype button.
This small gesture of support goes a
long way for us. You might already know
that when you start Claude code without
adding anything after it, it starts in
auto mode. In this mode, Claude allows
all commands that are safe on its own.
So it doesn't ask you for permission for
every single thing. But auto mode
doesn't know how you work and which
commands you usually let pass. There's a
command called auto mode setup that
teaches it exactly that. This command
reads your project and your past session
history. Then it changes auto mode's
rules to match the commands you usually
allow. When it's done reading, it shows
you the new setup to check. If you're
happy with it, you need to approve it
and then it updates auto mode settings.
From then on, Claude Code follows these
new rules in auto mode. Now, [snorts]
that command was for editing auto mode's
own config. But if you don't want that
config to change, there's another
command called fewer permission prompts.
This command searches your past sessions
for the commands and tools you use the
most. It only picks the ones that read
things and don't change anything. Then
it adds them to an allow list, which
lets Claude know that these commands are
allowed to run without asking you first.
And Claude Code saves this list in the
settings file of whichever project
you're working on. So you can let it
work on long tasks without worrying that
it's going to change anything that you
don't want it to. When Claude works on a
long task without stopping to ask you,
it needs as much free context as it can
get. But part of that context is already
used before you even type anything.
That's because there are connectors
already added in the Claude app like
notion and Slack. And they also load
into every Claude code session, even
when you never use them. So if you don't
need them, a setting called disable
claude AI connectors stops them from
loading. You set it to true in the
settings.json file in the main.claude
folder. This setting applies to all the
Claude Code sessions you open. After
that, the Claude apps MCP servers don't
appear in Claude Code anymore. You don't
even need to open the file yourself. You
can just ask Claude Code to add the
setting and it will edit the settings
file for you. There is also a setting to
turn off artifacts. When you work on a
design, Claude first makes an artifact
which opens the design as a page in your
browser. That way it shows you if its
plan is right. But the tool that makes
artifacts also loads into every session
and uses context. So if you don't need
it, you can add enable artifact to the
same file and set it to false. Then
claude doesn't make artifacts anymore,
no matter what you ask it to do. Now if
the app you're building with claude code
uses AI itself, you also need to test
whether its AI gives good answers. For
that, the same Claude API command from
before has a build eval command, too.
This command builds a set of tests.
These tests check if your app works well
in different situations. This command
writes these tests only once. That way,
every new version of your app gets
checked against the same tests. Another
command that Claude API has is hill
climb. This command keeps making changes
to your app and runs the tests after
each one to see how those changes affect
performance. It then scores the
responses. It only keeps the changes
that score higher than the previous one.
But both of these commands cost real API
money every time they run because every
test calls the model. And if your app
doesn't call claude or any other model,
build eval still helps. It basically
goes through your app and plans tests
for you without using the API. So you
can check if your app is working as it
should. Now when you start building a
feature, you usually ask Claude to plan
it first in plan mode. Claude writes the
whole plan and then it asks you to
choose a permission mode and start
building. Claude code also used to give
you an option to clear the context
before building, but it doesn't show
that option anymore. That option helps
because all the back and forth from
planning stays in the context while
Claude builds. If you clear it, Claude
starts building with only the plan in
the context. To get that option back,
you change a setting called show clear
context on plan accept. It's in the same
settings file in the main.claude folder,
and you need to set it to true. You can
ask Claude to do that for you, too. Then
every time you plan something, Claude
gives you the option to clear the
context first, the same way it used to.
But when you clear the context, the plan
doesn't disappear. The only difference
is that you won't see that file in your
project anymore. Instead, it saves every
plan in a folder called plans inside the
main.claude folder. So no matter which
folder you're working in, all your plans
go into that one folder. But you usually
want them in the same folder that you're
working in. So you can share them with
the people working on your project. To
do that, you add a setting called plans
directory to your settings.json file.
Then you set it to the name of the
folder inside your project where you
want your plans to go. From then on,
every plan you make in plan mode gets
saved in that folder. But before we move
on to the fix for the output Claude
gives, let's have a word by our sponsor,
Scribba. They've just launched a new
texttovideo AI tool called explain. When
you build something fast, understanding
the code later is the hard part, and
your standard AI chatbot just hands you
more text to read. Explain turns your
code, question or document into a
narrated video instantly. We connected
it to clawed code, pointed it at our
little URL shortener, and asked for a
walkthrough. Seconds later, we had a
real video tutorial that traced the
whole flow from shortening a link to the
redirect with narration and a moving
cursor guiding us through the actual
code. It even drew a diagram of how the
whole thing fits together, and every bit
of it came from our own repo. Explain
plays more like a personalized YouTube
lesson, not a chatbot. and it runs right
inside the tools we already use from
chat GPT plug-in to a Chrome extension.
So instead of writing heavy docs nobody
reads, we shipped something anyone could
just watch and it's free while it's in
beta. Try it now. The links in the
description below. You can also change
how Claude works with you using the
output style command. When you run this
command, it will list all the styles you
can choose from. There are five styles.
The default style is the one that's set
if you haven't changed it. Proactive is
basically where Claude acts first
instead of planning. so it does things
straight away. Concise is for when you
want shorter answers than Claude usually
gives. Explanatory is where Claude
explains more of what it's doing. And
the learning style is where Claude asks
you to write some of the work yourself
so you learn while you build. To switch
to any of these, you just need to type
the command followed by the name of the
style you want. From then on, Claude
uses that output style. Claude [snorts]
Code used to show you a summary of all
the reasoning it did when you pressed
control and O. But Claude Code doesn't
show these summaries anymore. To get
them back, you just need to add a
setting called show thinking summaries
to the settings.json file in the
main.claude folder. Then you need to set
it to true. When [snorts] you leave
Claude working on a long task and then
return, you have to scroll up a lot to
find your prompt and Claude's answer.
That's because Claude code normally
shows you every change it makes at each
step. But Claude code also has a focus
mode which only shows your prompt and
Claude's answer. It also shows a short
summary of what Claude did. To use focus
mode, you first need to run the TUI
command, which basically controls how
Claude code is laid out in your
terminal, and set it to full screen
because focus mode only works in full
screen mode. Then you need to run the
focus command. Now, when you give Claude
any task, you can still see what it's
doing and which files it's reading. But
those steps leave the screen when Claude
is done. So, when you return after a
long task, you only see Claude's answer,
and you don't have to scroll through a
lot to find things. Sometimes in the
middle of a chat, you want to try a
different idea without losing what
Claude has already done. For that,
Claude code has a command called branch.
Branch copies the chat you're in and
opens that copy as a new session. So,
you can try the new idea in the copy and
still keep your place in the first one.
But with branch, you still have to
prompt it yourself. When you just want a
task done on the side, you use fork
instead. Fork is basically branch, but
it starts the copy in the background and
gives it the task you want done. So the
copy works on that task while you keep
using your main session as you usually
do. And when the task is done, the
background session ends by itself. But
fork always makes a whole new session.
If you want the side task done inside
your current session, Claude hands it to
a sub agent. Normally a sub agent that
Claude starts has a fresh context. That
means it doesn't know anything about
your chat and it only gets the prompt
the main agent gave it when it started
it. That's where the subtask command
comes in because it starts a sub agent
with your full context. To use it, you
just need to run subtask and tell it
what you want it to do. Then the sub
agent works on that task with your whole
chat in its context. We often [snorts]
work on the same project in more than
one claude code session and each session
only knows its own chat. Now claude code
has a feature that lets these sessions
talk to each other. To see which
sessions you can reach, you run the list
agents command. So let's say you have
two sessions working on different parts
of the same project. The first session
needs to know something. the second
session has already worked out. But you
don't want to copy that context over
yourself. So you just ask the first
session to message the second one. The
first session gets the answer straight
from the second, even while the second
is still working. Then it continues its
work with that answer. Once [snorts] you
have many sessions running, you can't
watch all of them. And when Claude needs
something from you, it asks you a
question and waits for your answer. So
unless you're watching that session, you
won't know Claude is stuck. You might
return later and find Claude still
waiting. To fix that, there's a setting
called ask user question timeout. You
need to add it to the settings.json file
in the main.claude folder and set it to
60 seconds or any other time that you
want. When that time is up, Claude picks
the suggested answer on its own and
keeps working. So when you return,
Claude is still working instead of
waiting on a question. But Claude only
does this when it can move forward
without you. If a question needs your
answer before Claude can go any further,
it doesn't pick any option. Instead, it
keeps waiting until you reply. And with
[snorts] many sessions open, you also
don't know which one is waiting for your
reply and which one is already done. To
fix that, you need to run the config
command and find local notifications
further down the list. When you press
enter on it, you can choose the kind of
notification you want. We chose terminal
bell, but you can choose any of them.
With this setting on, Claude Code lets
you know when Claude is done or needs
your answer. When you switch to plan
mode, Claude code uses the same model
you started your session with, but you
can change that when you run the model
command and type opus plan after it.
Claude code uses opus only in plan mode.
For everything else, it uses the sonnet
model. So the plan gets the stronger
model and the building runs on sonnet.
Opus plan also saves your usage because
sonnet uses less of your limit than
opus. That matters most on the pro plan
because on that plan you'll hit your
limit a lot faster. The [snorts] sub
aents Claude starts use your limit to
and you can choose which model they use.
By default, each sub aent uses either
the same model as your session or a
model Claude code picks for it. To make
all your sub aents use one smaller
model, you can set claude code sub aent
model to the whichever one you want.
Then you set claude code sub aent model
force to one. You need this second
setting because without it, a sub aents
own file can still choose a different
model. But if you do want a sub aent's
own file to choose it, you can skip this
setting. Both settings go in the
settings.json file in the main.claude
folder. Claude code reads these settings
when it starts. So from your next
session, all your sub aents use the
model you chose. Aside from these
settings, there are some keyboard
shortcuts that also help in your
workflow. The first one is prompt
stashing. When you write a long prompt
and then remember another prompt you
wanted to send first, you can just press
Ctrl and S. Claude Code basically saves
the prompt and empties the prompt box.
So when you send the other prompt, your
previous prompt returns back and you can
send it later on. If you clear the whole
prompt by mistake, you don't have to
type your prompt again. You can just
press control and Y and your deleted
text returns. Other times you change a
prompt and want to undo that change. You
can just press control and the
underscore key and the prompt returns to
how it was before your last change. And
lastly, if you want to learn Claude
Code's features, it has a command for
that too called powerup. It gives you
short lessons inside Claude Code. And
each lesson shows a feature with an
animated demo so that you can learn
interactively while working with it. Now
all the skills and workflows and
everything else we build and show you in
all our videos can be found in AIABS Pro
which is our community. So if you found
value in what we do and want to support
the channel, this is the best way to do
it. The links in the description. That
brings us to the end of this video. If
you'd like to support the channel and
help us keep making videos like this,
you can do so by using the super thanks
button below. As always, thank you for
watching and I'll see you in the next
one.
