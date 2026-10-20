# Claude Code Setup Guide By The Creator Himself

- Channel: AI LABS
- URL: https://www.youtube.com/watch?v=pGro_uKt-_M
- Published: 2026-07-31
- Duration: 14 min
- Views at fetch (2026-10-11): 28,728
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

Boris Cherny, who is the creator of
Claude Code, sat down for an interview.
And interestingly, he said that even
though we have capable models like Fable
5 now, people are still using them the
same way they used Sonnet 3.5, which is
why he says you're carrying dead weight
into Claude and you don't even realize
it. So, if you can't get the latest
models working right, it isn't the model
that's wrong, it's the way you're using
it. Now, these might sound like
something you do once and forget about,
but they're something you should be
using every time a new model comes out,
whether that's from Anthropic or OpenAI
or anyone else. In the interview, Boris
goes into detail about how his team
works today. And honestly, who
understands these workflows better than
the person who created them in the first
place? We've started applying the same
approach ourselves, and we found it
really helpful. Now, if you're new here,
we're a software company and this is AI
Labs, where we show you how to optimize
a business with AI using proven methods
from our own team. And in this video,
we're going over which of his tips to
actually use and how to apply them. The
first thing Boris says in his talk is
that you should delete your setup every
time a new model comes out. And when
Opus 5 shipped, Anthropic did exactly
that to Claude Code and deleted about
80% of its system prompt. That sounds
reckless right up until you look at what
a setup actually costs you. Your setup
is everything you've added to steer
Claude, which include your Claude.md,
all the skills you create, your hook
setup, and more. All of these are
injected into the context window when
you launch Claude and stay there the
whole time. Now, we've talked about our
second brain before, which is a folder
that contains all our research,
strategies, and more in one place, and
the whole team works out of it. There's
the usage command. It shows how much of
your 5-hour window you've burned
through, and it breaks down where that's
coming from. Which of your skills are
eating the most, and which habits are
driving it. In our case, it was
workflows that spin up sub-agents
running several sessions at once and
leaving sessions going without
compacting them. The reason deleting
works is that most of what's in your
setup was never about your project. It
was for correcting things the model used
to get wrong. We've covered a lot of
frameworks that use slash commands to
control Claude on this channel like B
Mad, GSD, and more, which fires the
commands automatically at set points.
All handed the model rigid steps so it
couldn't wander off because models
needed that much hand-holding. On a
model this capable, the hand-holding
isn't helping anymore. It's the thing
that's getting in the model's way. So,
to find out whether your own setup is
earning its place, you strip it all out
and watch how the model does without it.
Run the context command in an empty
session before you've typed a single
word, and it already shows 3% of the
million token window used up. That's the
system prompt and the built-in tools
loading by default, already shaping how
Claude behaves before you've asked for
anything. That 3% is Claude's own and
you can't touch it. Everything on top of
it is yours. But, the better option is
safe mode, which turns off all of your
clutter, the Claude.md files, the
skills, the plugins, everything you've
installed, and leaves you running on
nothing but the base system prompt. Run
the context command there, and nothing
of yours is loaded. Then you run the
things you normally run and watch how
the model does. If it's fine without
your setup, that's your signal to start
cutting. And this isn't something you do
once. Every single lab ships a new model
after few months. So, if your project
isn't brand new, its setup is tuned for
a model which is two generations behind.
The rule for what survives is one
question. Would Claude have worked this
out on its own? If it would have, delete
the line. You see this most with the
command that starts your project. Every
time you made a new landing page and ran
the init command in that folder, the
Claude.md ended up with a line that says
use npm run dev to start it. You wrote
that in because the previous models
didn't know how your page starts and
wouldn't run it unless you asked. That's
over now because it works that out and
runs it on its own with no Claude.md at
all. But, anything where your setup
differs from what Claude already knows,
that stays in the Claude.md. For
example, you wanted testing through the
Versel's agent browser instead of the
one it reaches for by default. It can't
guess that or a test of your own or a
service that has to be running first, so
you need to add that in. You don't have
to do this by hand, either. Anthropic
shipped the doctor command and it trims
by exactly that rule. It cuts what
Claude could work out from your project
and keeps the areas where it made
mistakes, the reasoning, and anything
that's different from what a tool does
by default. We run it on that second
brain every so often, especially after a
new model release. It goes through
everything you've set up and hands back
a health report with a verdict on each
piece and a list of things it wants to
change. Nothing happens until you say
so, so you can work through them one by
one. One thing that makes rebuilding
easier is that installing other people's
skills isn't the risk it used to be.
This is because Boris says that the
models are less likely to get affected
by prompt injections now. The obvious
worry with any skill you pull in is
what's hidden inside it. We installed a
skill off GitHub and it had instructions
inside it telling our project to send
data out to a URL. Claude didn't follow
them and it didn't quietly skip them,
either. It told us in the chat that the
skill had asked and that it had skipped
it because the skill didn't look
trustworthy. Boris's line is that hidden
instructions like that can't get through
anymore, so you can install what you
want without treating it as a risk. But
before we move on to the next tip, it
would be great if you subscribe to the
channel and hit the hype button. This
small gesture of support goes a long way
for us. Once you've stripped all of that
out, something else has to tell the
agent when it's actually done. And Boris
says this is the single most important
thing people get wrong. That thing is an
eval, which is basically a fixed check
that decides whether the work is done
and it has to be strict enough to fail.
Saying run it and see if it looks better
is just guessing with extra steps. A
check you can't fail isn't a check. This
idea isn't new. You write the check down
before you build the thing, so there's
never an argument later about whether
it's finished. And it doesn't have to be
a test, has to be something that can
come back as a no. Some examples of
these would be checks for seeing if a
page fits on a phone screen, ensuring
that wrong password doesn't get you in,
and the text has no m-dashes. What the
check looks like depends entirely on the
job. Anthropic wrote up two of their own
big rewrites, and between them they used
three different kinds of tests. Bun is a
framework Claude code is built upon. Its
rewrite had a full set of tests that all
had to pass, and it had the eight
reviewer agents, each looking for one
kind of problem instead of everything at
once. The last one was a parity check,
which ran every command through both the
old version and the new one, and checked
if the answers came back the same. The
example worth copying is Boris's own. He
gave Claude an empty code base and told
it to rewrite the Claude desktop app in
Swift, run the old one inside a virtual
Mac, screenshot it, compare that against
its own version pixel by pixel, and not
stop until it was done. That ran for
over 2 weeks, and that comparison is the
only reason it could keep going that
long. Without something to tell itself
it isn't finished, an agent stalls out
in an hour, and you're back to watching
it. The checking you used to write into
the prompt yourself, it now does on its
own. Whenever we build an app now, we
give it a simple prompt telling it what
we want, and Claude works through the
parts it needs to build. You used to
have to put a line in the prompt telling
it to check how the page looked in a
browser. Now it launches headless Chrome
sessions by default, which is a browser
that runs with no window on screen, and
it takes screenshots of different areas
so it can see whether anything's
overlapping. It also goes back over the
code and flags anything that breaks a
rule, so it catches what would have
broken the app just by reading it. There
is a limit, though. All of that only
catches what breaks loudly, but not the
other issues that have to do more with
just breaking the app. Only you can say
what done and correct means for your
task, and your checks expire, too. Boris
says they last two or three model
generations, then everything starts
passing, and you need to throw the set
out and write different ones from
wherever it's struggling now. But before
we move forward, let's have a word by
our sponsor. If you've ever made an AI
video, you know the real pain isn't the
generating, it's jumping between one
tool for the script, another for
characters, another for scenes,
storyboards, and editing, and then
watching your character change face from
shot to shot. So, we brought the whole
thing into Buzzy Canvas, one visual
workspace where the entire workflow
lives. You start with a simple idea, and
Buzzy Canvas helps expand it into a
structured video workflow from script
and character concept art to scene
planning or storyboard frames or local
edits and final video generation, all
inside one visual workspace instead of
jumping between multiple AI tools.
Because every step is visual, you
actually control it, adjusting lighting,
camera angles, and individual frames
while character and three-view
references keep everyone consistent
across a long video. Powered by first
look models like SeaArt 2.5, Buzzy
Canvas isn't just another AI video
generator. It's a full production
pipeline for films, ads, music videos,
and more. Check out Buzzy Canvas using
the link in the description. Knowing
what done looks like also changes how
much you have to write in the first
place. We used to give it long prompts
with each and everything in them because
if you left a gap, it went off the
rails. Nobody trusted the model with
more, and the prompts matched. Now, you
say what you want, and it works out the
route. If you tell it how to do
something instead of what you want,
you'll never get better than your own
approach. Boris says experienced
engineers are the worst at this because
they're trying to get the model to do
the task exactly the way they'd have
done it. What works now is higher level.
So, you only need to describe the task
along with the limits it has to stay
inside and what finished looks like.
Then Claude will figure out the rest.
The other half of the same habit is
aiming higher. Give it tasks slightly
harder than you think it can handle
because you only write all that detail
when you've quietly assumed it can't
take the whole thing, and that's
actually out of date. And there's a
second version of this that shows up the
moment you try to get a design out of
it. You take an inspiration image, hand
it to your agent, and tell it to build a
UI inspired by that design. What comes
back is a near copy. So, instead of
handing over the image, describe it. Say
the style you want and the look you're
going for instead of giving it the
answer and it works out the approach
itself. And it's not only design, the
same thing shows up when you're using it
to come up with ideas. You give it one
that worked for you, ask for more like
it, and everything that comes back looks
exactly like the one you gave it.
Anything concrete you hand it, it treats
as something to copy instead of
something to learn from. So, describe it
instead and it has to work its way there
itself. Now, the rule at the start
actually came from Boris and it was to
delete anything Claude can figure out on
its own. But, that's only half of it
because he also says every team should
still be writing the Claude.mds and
skills that let an agent work on their
project without being told anything
extra. So, there's still stuff worth
adding and when the model keeps getting
something wrong, the question is what
kind of gap you're looking at. There are
four answers and they go from the
cheapest to the most expensive. The
cheapest one is that the instruction
just isn't clear and to fix that, you
just change the prompt. That's most of
them and it costs you nothing. The next
one is something the model needs to know
every single time and that's what goes
in Claude.md. You need to keep this
lightweight. This could be a quick line
on what the project's for and then the
things that would trip an agent up.
Anything it can see for itself is just
dead weight. Then there's the thing
you're explaining for the fifth time and
that's when you make it a skill. Skills
work best as lightweight guides that let
Claude find information when it needs
it. So, you don't want to lock them down
with rules unless the area actually
calls for it. They're worth writing when
they hold something that's particular to
you or your team because Claude already
knows the generic best practices. So,
writing those down is just waste. And if
a skill gets long, you split it across
files so only the part it needs gets
loaded. The difference between Claude.md
and skills is when they load. Your
Claude.md gets loaded on every session
start, but a skill only gets read when
Claude actually needs it. So, the short
always true stuff goes in Claude.md and
anything long or occasional goes in a
skill that Claude.md tells it to go
read. In ours, that's a short Claude.md
at the top with most of the detail in
skills next to it like the instructions
for how to verify our work because
Claude only needs those when it's
checking something. Same instruction
except one costs you every turn and the
other costs nothing until it's used. And
the most expensive one is when the
information is somewhere Claude can't
get to at all. That's the only one where
you build it a way in. And this is where
you use an MCP server, which basically
connects it to whatever's holding that
information. This one isn't for when it
misunderstood you, and it's not for when
you're repeating yourself. It's for when
there's genuinely no way for it to know.
That's everything you can do with a
single prompt. When a job is too big for
one, you split it across several agents
and there's more than one way to do
that. You can hand the parts out
yourself with sub agents and decide what
each one gets. The way Boris brings up
is the dynamic workflow, and that's for
the jobs that need hundreds of agents
rather than a handful. You say use a
workflow and Claude plans the whole
thing out itself, splitting the job up,
sending a wave of agents out at once,
waiting for all of them to report back,
then sending out the next wave based on
what they found. You don't plan any of
it. We don't recommend actually using
them though. The biggest example is that
bun rewrite where a million lines of
code got rebuilt in under two weeks off
a single prompt with them steering it
along the way. What nobody mentions is
that it cost about $165,000
at API pricing. And once it was all
added in, 19 things were broken that
none of their existing checks had
caught. And the money is the smaller
problem here. When one agent goes wrong,
you lose an hour. And when hundreds of
them have been running for two weeks,
you lose the whole two weeks. You get no
result at the end of it and you can't
tell which one started it. That's too
much to risk on anything you're actually
trying to ship. What we use instead is
routines, and they're the ones you'll
actually use day-to-day. They're
recurring jobs that run in the cloud, so
they keep going after you close your
laptop. Anthropic runs 20 to 30 a day
across their apps, and each one is a
single sentence, which is something like
clean up all the stuff you don't need,
including the stuff left over from
features you already removed, because
the agent still reads through it every
time it goes looking around your
project. Write tests for the parts that
don't have any. So, you're the one who
finds out when something breaks instead
of a user. Find the places where the
same thing got built twice and merge
them, because if you're working on a
large project or second brain system,
the models tend to forget the things
already exist. Now, all the skills and
workflows and everything else we build
and show you in all our videos can be
found in AI Labs Pro, which is our
community. So, if you found value in
what we do and want to support the
channel, this is the best way to do it.
The link's in the description. That
brings us to the end of this video. If
you'd like to support the channel and
help us keep making videos like this,
you can do so by using the Super Thanks
button below. As always, thank you for
watching, and I'll see you in the next
one.
