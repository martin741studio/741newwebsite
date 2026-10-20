# Claude Mods Are Insane... You Need To Try These Right Now

- Channel: AI LABS
- URL: https://www.youtube.com/watch?v=ERNqRK6sMJY
- Published: 2026-10-09
- Duration: 13 min
- Views at fetch (2026-10-11): 23,441
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

If you've ever used Claude code and
wished it had a feature that would make
it so much better. Now you can just add
that feature yourself, that's because
Anthropic released Claude mods and they
let you do so much with Claude code that
you couldn't do previously. We spent a
lot of time trying different mods and
built the ones that changed how we work
with Claude every day. One of the ones
we created fixed our prompts before
Claude sees them. And we also created
one to manage our Claude code sessions.
And Claude also makes choices on its own
without telling us. So we built a mod
that catches those choices. And we also
created a mod that fixes a problem you
deal with in every session when you're
working with Claude Code. If this is
your first time, we're a software
company and this is our channel AIAs.
And in this video, we're going to go
over every mod we built and explain how
each one works in detail so you can set
them up for yourself, too. This section
is only for those who don't know what
Claude mods are. So, if you already know
what they are and how to set one up, you
can skip ahead to the next section using
the timestamps in the description down
below. Now, Claude mods are actually a
feature that Anthropic added to Claude
Code that lets you modify it and add in
new features that Claude Code doesn't
already have. They're basically plugins
that run inside Claude Code, but instead
of only adding things to it, they can
change how Claude Code itself looks and
works. A mod lets you change Claude
Code's interface by drawing its own
panel beside the chat or a strip above
the prompt box with buttons and text
boxes in it. It can also redraw parts of
Claude Code's own screen, like the row
for each action Claude takes or the box
Claude asks you questions in. You can
add your own workflows to it and change
the behavior of Claude or any of Claude
Code's existing features. Some people
are even creating custom pets for Claude
code, like a little pixel pet above the
prompt box that reacts whenever
something Claude runs fails or passes.
Now, you might think you already have
skills and plugins that can add extra
functionality to Claude code. So, why
would you need a mod? That's because a
mod works differently from Claude's
skills and plugins. It's always running
and does its job every single time. Just
like a built-in feature of Claude Code,
it can even change what Claude code
does, which the others can't because
they just add on to the existing
capabilities, but a mod changes them.
And no skill or plug-in can modify the
screen the way a mod does. Now, if
you're working with Claude Code, you
might have already seen and used a mod
without even knowing it. Claude Code
comes with two built-in mods. One of
them is the diff command which basically
lets you see what was changed since the
last time Claude committed the code to
git. This was a feature of Claude code
before Anthropic announced mods and it
is built on the exact framework mods are
built on. The second mod is called you
should know which basically runs a side
agent that watches while Claude works on
tasks. When that side agent finds an
important detail that you might miss
because Claude is working in a long
session, it shows you a small note about
it above the prompt. This isn't turned
on by default, so you need to turn it on
yourself. And like we've mentioned,
people have been creating a lot of mods
and they're also sharing them so that
other people can use them, too. There's
a whole marketplace for them at
claudemod.com where a lot of people have
uploaded theirs. So, you can also play
around with what others have been
building. And creating Claude mods for
yourself is really easy. If you're on
the latest Claude Code version, you'll
have a built-in skill called plug-in
authoring that already knows everything
about how to create Claude mods. So, if
you want to create a mod for yourself,
you just need to give Claude Code a
prompt telling it what you want the mod
to do. Claude loads the plug-in
authoring skill on its own and writes
all the code the mod needs. While Claude
is working, Claude Code will also ask
you if you want to turn on hot reload.
You need to allow hot reload so that the
mod loads as soon as Claude finishes its
turn, and you don't have to manually
reload it every time Claude makes a
change to it. That way, you can see for
yourself if the mod is working the way
you want as soon as Claude is done
making the change. But once Claude is
done, the mod only works in this session
and you can't use it in your other
sessions. That's because Claude saves it
in a temporary spot that gets cleared
after a while. So if you like how a mod
works and want to use it in other
sessions, too, you can just ask Claude
to install it for you. It gets saved and
all your new Claude code sessions can
use it too. So with this knowledge,
let's start with the first mod, which
makes a simple prompt better before you
send it. A lot of times, we don't tell
Claude exactly what we want. We just
give it a rough idea and let Claude
figure out the rest on its own. But this
way, Claude doesn't get the right
direction in first attempt and that's
sole because of weak prompting. So to
make that easier, we told Claude to
create a mod that basically takes a
simple prompt and makes it better. And
it doesn't just make it better. It
changes the prompt to fit the project
you're working in and all the skills you
have installed. The mod doesn't send the
prompt for you. Instead, it rewrites
your prompt right there in the prompt
bar so you can check it and send it
yourself. When you prompt Claude, it
creates the mod using the plug-in
authoring skill. Once the mod is made
and you open Claude code again, you'll
see the prompt enhancer right above the
prompt bar. It has two buttons called
enhance and send. So, write a simple
prompt and then press the keys the mod
set up. In the mod we made, that was
Ctrl X and then tab. That selects the
enhance button. If you're using Claude
Code's full screen mode, you can also
click these buttons with your mouse.
When you press enter, the mod asks the
model to rewrite your prompt right there
in the prompt bar. The new prompt is a
better version of the simple one we
gave. It names the installed skills that
fit what we asked for, so Claude doesn't
have to look for the right ones. It also
lists the big decisions Claude should
ask you about first instead of making
them on its own. It describes what the
finished thing should look like, too,
which helps keep Claude on the right
track. You can change anything in the
prompt. When it matches what you need,
you can send the prompt. Claude will
then load the skills named in the prompt
and do a better job than it did before.
We were working in an empty project, so
the prompt didn't have a project to fit.
But if you're working in a real project,
you'll see that the mod also adds
details about your project to the prompt
to make it even better. But before we
move to the next one, it would be great
if you subscribe to the channel and hit
the hype button. This small gesture of
support goes a long way for us. Now,
when you ask Claude to build any design,
Claude asks you questions to figure out
the look you want. But in those
questions, Claude only describes each
design style in words. And it's hard to
picture a design from words because
words can't really show the style Claude
has in mind. A lot of times we've picked
a design style that sounds good in words
but looks bad once Claude actually
builds it. So to fix that, we built
another mod that runs whenever Claude
needs to give you design styles to
choose from. The mod shows you what each
option looks like, so you can pick one
by seeing it. Now, when the mod is on,
you can just give Claude a prompt
telling it what you want to build.
Claude will ask you questions like it
normally does. And the mod will also
open a site that shows what each design
style looks like. Then you can select
whichever one you like the best. Once
you pick one, Claude will start
building. That way, the design turns out
much closer to what you actually want.
Now, when you're working with Claude and
something is unclear, Claude asks you
questions, but Claude only asks about
the big decisions that really change
things. For the small ones, it just
makes assumptions and then it does the
task you asked for. Most of the time
these guesses are right, but sometimes
they're wrong and you have to tell
Claude again to fix them. And unless you
check every single feature, you might
not even notice some of those guesses
until something breaks later on. So for
that, we created a mod that shows you
all the assumptions Claude makes. And
you can check right there whether each
one is right or wrong. If you want
something changed, you can just send it
back and have Claude fix it. Now, when
Claude finishes building this mod, you
can open Claude code again and give
Claude any task just like you normally
would. When the task is done, you'll see
the assumptions show up so you can check
them. In our case, a small strip above
the prompt bar showed that Claude made
six assumptions while working on our
task. When the prompt bar is empty and
you press zero, the mod opens the full
list where you can check each one. You
can move through the assumptions using
tab and mark each one as right or wrong.
If you mark any of them as wrong, the
mod sends Claude a new prompt about that
wrong assumption on its own. That way,
Claude fixes that part and keeps the
ones you marked as right. And if you
want to say something specific about an
assumption, you can type it right into
the list so Claude knows exactly how you
want it to turn out. But before we move
on the next setup, let's have a word by
our sponsor, Runway. We just finished
building Stride, our AI running coach
app ready to launch, but none of the
content to actually launch it. No hero
video, no images that match the vibe,
and no one to voice it. The plan was to
farm all of that out to three different
apps and just hope it lined up at the
end. That's when we found Runway, which
does all three in one place, so nothing
has to line up after the fact. We
generated a hero video with Gen 4.5,
built a matching set of images around
it, all in one workspace without
exporting between five different tools.
And surprisingly, the character stayed
consistent across every shot. Then we
recorded a clean voice over to tie the
whole thing together, and the final
assets came out ready to drop straight
into our launch. We still made every
creative call. Runway just handled the
grunt work so we could make more of what
actually mattered. Try Runway yourself
and use code create 15 for 15% off a
month of any plan. The links in the
description or scan the QR code on
screen. [snorts] When we're working with
Claude on anything, we get a lot of
ideas, but we don't want Claude to get
distracted right then. We wanted to
focus on the task it's working on. So,
we used to save those ideas in a notes
app to come back to later, but we'd
forget about them and it got hard to
keep track of them. So, we created a mod
that's basically an idea shelf. While
you're working on any task, you can put
every idea that pops into your head on
that shelf so Claude doesn't get pulled
away from what it's doing. Then you can
send those ideas to Claude later. Each
project gets its own idea shelf. So you
don't have one shelf for all your
projects. And even if you close Claude
code, the ideas stay saved. So if you're
working on a site and get an idea you
want to save, you can just use the idea
command and it opens a small box. Add
your idea here and the shelf saves it.
If you want to send that idea, select
the send button and press enter. or you
can just throw it away if you don't want
it. You can move between the buttons
using the tab key and then you'll see
all the ideas on the shelf. Now, if you
want to send any idea, just select send
and press enter. The mod sends that idea
to Claude as a prompt so Claude can work
on it. Now, we're always running
multiple Claude code sessions at the
same time, each working on a different
task, but keeping track of all of them
can be really hard. So, to make that
easier, we created a mod that basically
shows all the sessions that are running,
whether they're working in the same
folder or not. Then when Claude is done
building the mod, you can open a new
Claude code session and you'll see
something new on Claude code screen. It
shows which sessions are waiting on you,
which one is working right now and which
ones are done. The mod also updates each
session on its own. So when a working
session finishes, the mod marks it as
done. To see more about each session,
you can just run the sessions command or
press Ctrl X and then tab. Then you can
move through each session and see how
it's doing right from where you're
working. And if you're working and any
claude session needs you, you'll know
right away. So you don't have to open
every session to see which one has a
question for you. That way none of your
sessions get stuck waiting on you.
[snorts] Like we said before, we run
multiple Claude Code sessions at the
same time. We even run more than one
session in the same folder, which
basically means on the same project. And
when you do that, you need to keep track
of what each session is doing. So two
sessions don't end up doing the same
task. So to make that easier, we made a
mod that basically works as a session
tracker for sessions in the same folder.
It keeps track of what each session is
working on right now and what it's doing
next. Now once this mod is made, if you
open just one session, it works like
normal. Nothing new shows up on Claude
Code screen about other sessions. But if
you open a second Claude Code session in
the same folder, you'll see something
new show up on the second session
screen. It tells you there's another
session also working on this project. It
also shows what the first session is
working on and whether that work is
still going or done. And when you give
the second session a task, the first
session gets the same thing on its
screen showing what the second session
is doing. So you can keep track of which
task you gave each session. You might
know [snorts] that when you're working
with Claude, it often uses too many
technical terms and goes in circles,
making Claude's answers hard to
understand. It gets even harder when
you're running multiple sessions at once
because you lose track of what's
happening in each one. Then you read
Claude's summary and it doesn't help. So
you have to scroll up to see what was
going on. So for that, we built a mod
that basically turns all of Claude's
answers into a simple form that's easy
to understand. We also told Claude that
we run multiple sessions at a time. So
each answer should be complete enough
that anyone coming over from another
session gets it right away. There's also
one problem where Claude gives a few
short summaries in between long tool
calls. You'd often miss those summaries
unless you scrolled up. So, we asked
Claude to make sure those summaries
don't show up between the tool calls
either. When Claude was done, it also
added a check that uses a haiku model to
make sure the rules are followed. Now,
when you open a new Claude code session
and give Claude your task, you'll see
there's no text in between the tool
calls. All the text is just at the end
in the summary. Claude first writes its
answer with the tech words like it
usually does. Then, the mod steps in and
asks Claude to rewrite it in a simpler
way with everything you need to know so
you don't have to scroll around. The new
answer also tells you the next steps so
you know what to do after this. The mod
also has a status line that shows what
the session is working on in case you
switch to the session while it's still
working. Now, we refined all the mods
that were shown in this video. So, if
you want access to those, you'll find
them in AIABS Pro, which is our
community. So, if you found value in
what we do and want to support the
channel, this is the best way to do it.
The links in the description. That
brings us to the end of this video. If
you'd like to support the channel and
help us keep making videos like this,
you can do so by using the super thanks
button below. As always, thank you for
watching and I'll see you in the next
one.
