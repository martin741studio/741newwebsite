# Claude Code Just Dropped MODS. (Master it in 10 Minutes).

- Channel: Tristen O'Brien
- URL: https://www.youtube.com/watch?v=LDn7rQKIFro
- Published: 2026-10-05
- Duration: 10 min
- Views at fetch (2026-10-11): 204,893
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

So Claude has just given us one of the
biggest updates that they have ever
given us. They call it Claude mods. And
basically, if you could think of a
feature that you wish Claude Code had,
and you can describe it, well, Claude
Code will build it right into itself,
which means that you can turn Claude
Code into pretty much any tool that you
want it to be. And in this video, I'm
going to walk you through how you can
build your own mods. I'm going to walk
you through the six clawed mods that I
built for myself this week. But to kick
off this video, let's go through what
Claude mods are and what Enthropic
actually announced. So, a mod is just a
small add-on that changes how Claude
Code looks and how Claude Code works. It
came out on October 1st, and if you've
already updated your software, then it's
turned on for you and it's ready to use.
Now, it works in the Claude Code
terminal and also works in the Claude
tab inside of the desktop app, but it
doesn't work inside of the Claude chat.
So, you do want to make sure that you're
using this inside of Claude Code. Now,
you might be thinking, "Well, I already
have skills and I already have
connectors." And that's true, but those
work from the outside. A skill tells
Claude how to do a job. A connector
plugs Claude into another app. But a mod
runs inside of Claude code itself. So,
it can change exactly what you see on
the screen, which means that you can add
buttons, you can add a panel, you could
add a miniame that you can play while
you wait for Claude to finish. Which
takes me to the first mod that I built,
which I call Clean View. Now, when I'm
working on a project, sometimes I don't
want to see all that text flying by when
I'm using claw code. I don't necessarily
care about the code that's behind it. I
don't care about the tools that it's
calling. I just want to see what it's
working on, how far along it is and what
else it has to do. And with this mod,
when you take a look down here at the
bottom right, it says Tristan's tools.
Now, we're going to go through all of
these in a bit, but one of them is clean
view. Now, since that's turned on, I'm
going to type a prompt like build me a
weather dashboard for New York City. And
then I'm going to hit enter. And you're
going to see that all of that noise
that's usually there is gone. All I get
is a simple checklist. It thinks about
what I asked. It comes up with a plan.
It shows me every step of the way what
it's doing, how much is left, and then
when it's done, it's going to give me
the dashboard that I asked for. Now,
that's not the point, though. Yes, this
dashboard looks pretty nice. But back in
Clawed Code, the point I'm trying to
make is that I get a short summary of
what it did, and that's really all I
want. It's clean. It's minimalistic, and
it's what I typically appreciate. But
how does a claude mod change what's on
my screen? Well, every time Claude does
something like run a file or run a
command, it sends out a little signal
called an event. A mod is just a small
piece of code that listens for those
events. And when one of those events
comes through, the mod can do one of
three things. It can watch it, it can
change it, or can handle it itself. So
the normal thing that you're expecting
to happen never happens. So, with the
cleaning view mod, the one that we're
looking at right now, every time Claude
is about to show one of those technical
rows, one of those tools that it needs
to call, the mod is going to step in and
it's going to hide it. And when Claude
finishes the step, the mod is going to
check it off the list. Now, the good
news here is that Claude code has a
built-in skill that teaches Claude how
to build these mods. All you're going to
have to do is describe what you want and
then Claude is going to build it for
you. But more on that later. Let's jump
over to the second mod I built, which I
call employee control panel. Now,
normally if you want to switch models,
you would have to type in slashmodel and
then pick the one from the list. Or if
you want to change how hard Claude
thinks, then you had to type in
slasheffort and then do the same thing.
Now, those work for sure, but to be
honest, I hate typing in the slash
commands just to change the model or
effort. So, with this mod, I'm going to
click Tristan's tools at the bottom
here, and you're going to see that the
model and effort are right there for me
to change. And when I change them, you
can take a look at the status bar below.
it changes right away. So, I don't have
to take the time to type in slash
commands just to pick the model or
effort I want. I'm just going to go to
my toolbar and it's right there for me
to change. Now, I know this one is
small, but it does make my day easier
and I think it's going to make your day
easier, too. But the next mod is going
to put a whole team of employees to work
at once, and I call it the agent dock,
which actually is pretty awesome. When
you give Claude a big job, it can hand
pieces of those to helper agents. Now,
these little agents are just extra
copies of Claude that can each take a
small piece of the work. But the problem
here is that you don't always get to see
what the agents are doing. And you
usually don't get to select how many
agents you want to work on your project
at any given time. But with this mod, if
I type in /doc, I'm going to get to pick
how many agents I want on my team for
the very next prompt that I give Claude.
And I'm going to select up to 50 agents.
Now, I'm going to give it a real job
here to test this out. This is for a new
bakery called Golden Crumb. And what I
want to do is I want to create a
dashboard that tracks 50 different tasks
before the grand opening. Now, in my
little toolbar down here, you can also
pick what type of helper you're going to
use for these agents. You can either use
fast and cheap or you can use the same
model that you're using like Opus 5.5.
But take a look at this. Every agent
gets its own card and its own task with
its own progress bar. Now, we selected
50. 20 of them are showing right now. 10
are working. The rest are just waiting
their turn. And when they're all done,
Claude is going to pull everything
together in one dashboard. Now, heads up
on this one, though. If you do select a
big team, like 50 agents, you will go
through your plan a lot faster. My mod
does warn me about that before I go too
big, but it is worth knowing in case you
build this yourself. Now, the next mod
is one that I use every single day. But
before I show you what that is, take a
look at the session bar over here on the
lefth hand side. You can see which
sessions are actively running. You can
jump to whichever session that you want
to jump into. And this is something that
I built. And if you like it, please go
ahead and subscribe and comment session
bar. If I do get enough comments, I'll
go ahead and shoot a video on that one
as well. But let's get back to mod
number four, which is Claude photos.
Now, I make AI photos and videos every
single day, but we know that Claude
can't make them on their own. Now, what
that normally means is that you have to
leave Claude and go into a different
tool like Gemini or Chatt or any other
tool that's running Seance2.5. But I
don't do that. I use one tool, which is
Higsfield. Now, the reason why I like
Hicksfield so much is because yes, it
has every top image and video and audio
model all in one place, but they have a
connector right inside of Claude. So, it
just made sense to build a mod right on
top of it. And full disclosure, I did
reach out to Higsfield to see if they
wanted to partner on this video and they
are sponsoring it, which makes sense
since this whole mod runs on top of
Higsfield. Now, if I type in /create,
take a look at this. I get a full photo
and video experience right inside of
Claude. On the top right, I get to see
how many Higsfield credits I have. Then
I get to describe the type of video or
photo that I want. Now, I'm just going
to ask it to make a photo of me riding a
train. It can pick my outfit. It can
pick my expression, whatever. This is
just for a demo, but then I get to pick
whether I want this as a photo or video.
So, of course, I'm going to pick photo.
And then I get to pick the model that
I'm going to use. Now, I'm going to
select Nano Banana Pro because I think
it's one of the best ones that's out
there. I get to pick my image size,
which would be 16 by9. And I'm going to
pick that I want this in 4K. Then I also
can do some of the extra settings here,
which is where I can upload a photo of
me so it knows what I look like. With
that said, Claude is going to take that
one sentence and turn it into a much
bigger and more detailed prompt that's
written exactly for the model that we
chose. And of course, you can change the
prompt if you want, but it's a much more
detailed prompt than I would have ever
used. So, when I hit enter, it has the
tasks already lined up for me. Now, one
thing it's going to do is it's going to
tell me how many credits this is going
to use, and it's going to pause there
until I click yes. Now, I did that on
purpose because I don't want a crazy
amount of tokens or credits being used
without my approval. But once I hit
that, it's going to do one interesting
thing. Now, since this is running in the
terminal, it's going to give me this
little pixel preview, which I thought
was just fun to add in. You know, you
could remove that if you don't want to
use it. But down here is where you click
and see the real photo. And that is me
on the train just like I asked. But I
never had to leave Claude. And this
photo is already saved on my computer.
Now, of course, this is just the tip of
the iceberg when it comes to Hicksfield.
We all create images. We all create
videos. If you've never been to
Hicksfield's website, you should
definitely check it out. They have some
of the coolest and most popular AI
videos that you can just copy the prompt
and make it yourself if you want to. And
most of them are the videos that you see
that are going viral online. So, if you
haven't checked them out, check it out.
The link is in my description to try out
Hicksfield. But that does take us to the
fifth mod and I call it Roadtrip. Now,
this one I built just for fun, but I do
like it and I have been using it. It's a
mini racing game that plays right inside
of Claude Code while you wait for Claude
to build your project. So, let's say
that you ask Claude to make your weather
dashboard better. While it's running,
you can just click play and now you're
driving. You're playing the game. And
every so often in the game, it's going
to ask you a quiz question about Claude,
which by the way, let me tell you, is a
lot better than just staring at the
screen waiting for Claude to finish.
Those are five mods that I built this
week. Now, you're probably wondering how
you can build these yourself. You're
going to want to make sure that Claude
Code is up to date because Claude Mods
needs version 2.1.287,
I believe, or newer. Then, all you have
to do is open up Claude Code and just
describe the mod that you want. Claude
Code is going to start building it, and
then it's going to ask you to reload.
When it does that, you're going to want
to say yes. And when you do that, your
mod is going to show up as soon as
Claude finishes. And if you don't like
something, you can just talk to it like
a normal human. You just tell it what
you don't like and what you want changed
and it's going to change it for you.
Now, one thing to keep in mind is a mod
is just a type of a plugin, which means
it installs the same way a plugin does.
So, if somebody shares a mod with you,
you can type in /plugin and search for
it and install it just like any other
plugin. One thing to keep in mind though
is that a mod that Claude builds for you
are temporary by default, which means
that as you're building these and you
find the ones that you like, you're
going to ask Claude to save it as a
plugin and install it. That way, it's
going to be there for you every single
time that you open up Claude. Now, mods
don't cost anything extra, but you do
need a paid plan that includes Claude
Code. And of course, if a mod is running
in the background, it is using your
subscription credits as well. And that's
it. And just remember that a mod is just
a feature that you describe, and Claude
is going to build it right inside of
Claude Code for you. So, thanks again
for watching. Thanks again to Higsfield
for sponsoring this video and check out
the link in the description.
