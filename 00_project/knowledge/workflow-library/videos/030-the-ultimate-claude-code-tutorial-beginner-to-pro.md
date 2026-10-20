# The Ultimate Claude Code Tutorial (Beginner to Pro)

- Channel: Zinho Automates
- URL: https://www.youtube.com/watch?v=OVm2AGTxYuE
- Published: 2026-08-17
- Duration: 20 min
- Views at fetch (2026-10-11): 124,740
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

So, 2 months ago, I did a Claude code
tutorial, but since then, Claude has had
some major updates. And the way that
you're supposed to use it has it
genuinely changed. And Litti, I'm not
the one saying it. Anthropic's own
engineers are tweeting about it
currently as we speak. The old playbook
doesn't fully work anymore because
Claude is definitely now. So, today we
are going from the basics all the way to
the advanced stuff. And I'm going to be
walking you through the latest changes
and the exact way to use Claude code
right now. Because honestly, quite a lot
has shifted these past few months. And
you are going to see that in the video.
So, just a couple of things to get ready
for. They include things like a preview
system that tests its own builds,
sessions that you can run side by side,
a way to view what Claude makes like a
manager instead of a coder. And the big
one that everyone is talking about, jobs
that keep running after you've closed
your laptop. So, let's say you've never
touched Claude code before. Don't worry
because I'll keep the basics as simple
as possible as we go. And also, if you
want all the prompts to follow along,
all of it is inside our free school
community. The link is down in the
description below. And also, we are
currently on 33,000 members. So, come
and join us today. And also, I guarantee
you you're going to love being part of
the community. But right now, let's hop
over to the laptop and let's get
started.
Now, first things first, we are going to
be using Claude code inside the desktop
app, okay? So, it's the easiest way in.
So, what you need to do is download the
Claude desktop application. Then you're
going to sign in to your account and
then you're going to click the code tab
at the top. And then, that's basically
where all of the magic happens, okay?
So, the layout is pretty simple. Your
chats in the middle and then your
project files sits on one side and a
preview of what you are building shows
up on the other. So, you simply just
point at the folder and you are ready.
So, a quick thing before we start
building and it's basically nothing new.
So, the model selector sits here right
next to the prompt bar. So, keep Sonnet
as your default, okay? It handles the
vast majority of what you throw at it
and only switch to Opus when you hit a
genuinely hard problem. So, that's
basically things like tricky logic or
let's say a bug that just won't go away,
okay? And also, you'll see Fable 5 and
that's the sharpest coding model in the
setup. So, this is the one where you
reach for only on the seriously harder
bolts. So, when you want the most
powerful thing that Claude can possibly
give, that's when you switch to Fable 5.
Because it can practically one-shot an
entire bolt. But, the problem with that
is it is pretty pricey as your daily
driver, okay? So, only save it for when
it truly counts. So, right next to the
model, there's an if it's setting, okay?
So, that's how hard Claude thinks before
it acts. So, leave that on default for
most things and only push it to max when
a problem really needs some extra
reasoning. And also, make sure to keep
half an eye on the context window. So,
that little usage meter up top, that is
the context window. So, that's Claude's
working memory of the session and when
it fills up, then Claude starts
forgetting earlier decisions. So, I'll
show you how to manage that later on in
the video. But, for now, I want to get
on to what has actually changed.
So, the first thing that I want us to
talk about is, funnily enough, how to
actually talk to Claude. Because this is
where most beginners always seem to dev
up, okay? So, it's also the thing that
weirdly has actually changed the most.
The basics has to be discussed first. A
good prompt is just a clear one. That's
the best way to think about it. Before
you build, be specific about five
things, okay? So, what you are building,
what it's for, what it needs to do, what
it should look like, and what it should
never do. And that's pretty simple. So,
nail those five things, and then Claude
basically isn't guessing on anything.
It's building what's actually in your
head. So, now here's what's changed. And
it's almost the opposite of the advice
that's been floating around for a couple
of months. The old way was to simply
just pile on the rules. You can do this,
but like never do that, always format in
this way. But Anthropic's own engineers
just lifted went public, and they said
that with the newest models, that
actually backfires, and it doesn't work
as well as so many people think.
Stacking the rules it doesn't sharpen
Claude anymore. It simply just boxes it
in. So, the new move that you should be
going with is to give it a judgment
instead of a rule book, okay? Describe
the standard that you want, and then let
Claude be the one to actually reach for
it. Same story with the examples, okay?
Showing it three samples used to help.
Now, it simply just copies them, and
then it stops exploring. So, instead of
here's exactly what to do, you set the
bar, and you let a very capable model
figure out how to clear it. So, keep
that mindset for everything that follows
from here on out, okay?
Now, start every build in plan mode.
Super important. Flip the mode selected
to plan, and then Claude reads your
files, and then it thinks the problem
through, and then it asks you questions.
So, without you having to touch a single
file until you say go. It's the one
habit that stops Claude from confidently
building the wrong thing. Then, before
you type a single word, click on the
mic. This is the thing that most people
usually skip, and it's the one that
separates a good build from a great one.
You see, because when you type, you
compress. You self-edit, [music] and
then it cuts the context that actually
matters.
When you talk, you actually leak all of
it. So, what I would do is I would
switch to plan mode and then hit the
mic, and then
>> [music]
>> simply just talk like we are now. So,
for this whole video, I'm building one
light thing, a habit tracker that I'm
calling Streak. So, I simply just sit
back, and then I have ample that, a
simple clean tracker where I add a
habit, I check it off daily, and then I
watch my streak grow. And it should
never nag me. That's something that I
really want. So, Claude hands back a
plan and then a couple of questions on
top of that, and it will say things
like, "Should Streak reset at midnight?
Do I want reminders?" And only once I
approve, does it actually start the
build. Now, that's the real unlock here.
The people getting the best results
aren't the ones that's typing. They are
the ones that are talking, because
that's how you hand Claude the most to
work with.
>> [music]
>> Now, watch what it does after it builds.
It spins up the dev server on its own,
and opens the app, it clicks the
buttons, it fills the forms, and it
fixes what's broken before it ever tells
you it's done. It tests itself. Now,
watch the preview on the right side, and
you'll see that it's moving through the
app on its own. Now, that's Claude
running its own QA pass, catching and
fixing mistakes beforehand handing the
build back to us. And that is
>> [laughter]
>> literally so amazing.
Now, the first version of won't be
perfect. Let's get that out the way. So,
you simply just talk to it like a
designer. You don't need the code, you
describe what's off. So, on Streak,
that's the cards feel cramped, or the
streak numbers are too small, or the
check off feels a bit laggy. So, then
you simply just send it, and then the
preview updates, and you go again.
Build, preview, describe, and then
refine. The process is so simple. That's
basically the loop that you always have
to remember. It rewards how clearly you
can describe what's wrong, not how much
code you know, okay? So, there's no
terminal really required over here.
Now, when a Claude says that it's done,
don't just test it, okay? Open up the
diff view, and it's one of the most
underused features in the app. Now,
every time Claude edits a file, you see
exactly what changed line by line, just
like a pull request review at a real
company. You don't need to understand
the code. You just need to see that
something changed where you expected,
and nothing changed where you didn't.
Now, on top of that, you can even
comment a line like a note on a
document. On streak, I'll simply just
drop this. Make the streak flame orange,
not gray. Something pretty simple. And
then, what does Claude do? Claude
adjusts. There's one more piece, a
built-in code review that you can run as
a command. You can kick it off, and
Claude then audits its own work. It's
tuned for stuff that really matters.
It's stuff like real bugs, broken logic,
security holes that that it may find.
Not necessarily style nitpicks. Now,
over on streak, it catches a spot where
missing a day wasn't resetting the
streak. And that is basically a real bug
before I ever hit it. Now, you are not a
coder here. You are the manager
reviewing a very fast and very capable
teammate.
Now, we are moving on to where Claude
code really changed, and it came state
from Anthropic. In July, they published
how they now handle context. And the
headline was pretty wild at the time.
For the newest models, they cut over 80%
of Claude codes own system prompt. And
they did that with no drop in coding
performance. The takeaway for your
Claude MD isn't a warehouse, it's a
directory. The models are now good
enough to find context on their own. So,
a giant individual file is dead weight.
It loads every session and then it burns
your budget before Claude ever writes a
line.
Keep only what Claude genuinely can't
learn from your code base. Your brand
voice, your inner message style, the one
architecture call that isn't obvious.
Plus also pointers to where the detail
lives in your skill files. So, to set it
up, simply just type in forward slash
init and then Claude generates the file
automatically. Then, open it up and
simply just start deleting. Cut anything
obvious from the code. So, keep only
what's irreplaceable, okay? So, the test
would a senior developer already know
this from the folder? If yes, then
simply just cut it. Now, for sleek, my
whole file is literally just three
lines. Keep it dark with one warm
accent, keep the copy friendly, and
never guilt therapy, and design rules
live in the design skill. And the
payoff, when I ask for a new weekly view
later, then it comes back dark, warm,
and friendly without me repeating a
single thing. Then it's fast and then
it's powerful.
Claude MD beats a 50-line file that
tells Claude what it already knows. Now,
that template is inside our free school
community. Go and grab it for your next
build.
Now, your Claude MD stays thin because
the detail lives somewhere better,
[music] and that is skills. A skill is
just a saved process that you hand
Claude once, and then it simply just
uses it forever. [music] So, you would
write down how you want something done,
and you save it, and from that point on,
you simply just trigger it with a slash
command, or Claude will simply just pull
it on its own when it's relevant. Now,
think about anything that you do the
same way every single time. How do you
like your components that then how your
brand looks, your a research routine
that you would run every single week.
Each one of those becomes a skill. So,
you are never re-explaining yourself. On
Sleek, those designs, those that I
mentioned, are loved in a design skill.
So, anytime Claude builds a new screen,
it already knows the look without me
having to say a word. Write the process
once, and then simply just use it
forever, and it's going to make your
life so much easier.
So far, Claude's been working inside
your project, but your work doesn't live
in one place. It's in GitHub, it's in
Slack, Notion, your Google Sheets. MCP
is how you connect Claude to all of it.
It stands for Model Context Protocol,
but forget the name, cuz I know that can
sound a bit technical. What it basically
means that Claude can reach into the
tools that you already use. And setting
it up takes only a few seconds, and I'll
show you right now. So, open the
connectors menu, and then click to add
the tool that you want, and you're
connected. Now, once it's in, you simply
just talk to it. So, on Sleek, I connect
Google Sheets, and I ask Claude to log
every completed habit to a sheet, so
that the data basically lives somewhere
real instead of tapped in the app. Now,
pick one tool that you actually use to
wire it up. Now, that's basically the
moment with Claude stops being an app
that you visit, and it starts becoming
the thing that it runs your other apps.
Now, did you know that you can also run
multiple sessions side by side, each
isolated so that they can't break each
[music] other. Now, on Steak, one
session builds a stat page while another
cleans up the styling. It's the same
project that's running at once, but
there's no collisions whatsoever. And
you don't even have to be at your laptop
while this happening. Cloud sessions
keeps running after you close the app.
You simply just send off a big job, you
walk away, and you can literally just
come back an hour later and you'll still
find that it's done. It's so cool that
you can literally fire a task while
you're on your phone at a coffee shop as
you're picking up a cup of coffee,
>> [music]
>> and you can literally turn home after
you finish that coffee, and then the
work will just be done. So, let's say
you maybe need to ask something
mid-build, then what you do is you open
up a side chat, and the main build keeps
going while your question gets answered
in a separate thread. So, that means
there's no interruption, and your
laptop's no longer the bottleneck. Your
imagination, technically, is.
Now, remember that usage meter that I
pointed out earlier? When it fills up,
Cloud starts forgetting decisions found
earlier in the session. So, here's how
you deal with it. Two commands is all
you need. Forward {slash} compact
squeezes the conversation into a
summary, and then it just keeps on
going. So, use it to keep building in
that same session, and then forward
{slash} clear wipes everything for a
full reset, so you can use it when you
switch to something that's completely
different. And one more tip that I want
to mention, if something looks wrong,
then don't describe it, okay? Screenshot
it, paste it in, and then say, "Fix
this." Now, over on Steak, the counter
was overlapping the date on mobile, so
then I pasted in a screenshot, I said,
"Fix this," and it was gone. Now, for
the hardest problems, bump the effort up
to max. It is slower and pricier, but
it's a different class when it comes to
the results. Now, before you wrap up a
session, run forward {slash} doctor. It
scans your setup and it finds the dead
weight, unused skills, forgotten
connectors, bloat in your Claude MD, and
then it tells you exactly what to
delete. Now, over on stake, it flagged a
connector that I wired up earlier and I
never actually used again. So, it's gone
in simply just one click. Now, that's
how you keep things thin, how you keep
things trimmed every few sessions, and
it's not perfect on day one, but it
definitely a difference.
And now that you've got your workflow
down, here's one advanced technique
that's worth knowing about. It's been
going viral recently, so you might have
seen it, and it just shows how far these
models have come. It's called the
Gauntlet Loop from a builder called Matt
Schumer, and the wild part is that it's
basically a three-line prompt. The
structure is pretty simple. First is the
task, so what you want to build. And the
second is the bold method. You tell the
main agent to fan out sub agents, each
one taking a piece, and each with a
critic checking its work. The third is
the bar. So, you tell it not to stop
until every critic is genuinely wild,
and that's basically it. The agents
build, critique, and then they loop
against your standard until [music]
it's hit. And in the desktop app, you
can actually watch the whole thing run
in the workflows panel, and you can see
it all phase by phase. Now, we have to
discuss this, and that's because this
isn't magic. A loop like this eats a lot
of time and a lot of tokens, okay? And
it optimizes toward whatever bar you
set. So, if you point it at [music] a
weak idea, it will simply just polish
the wrong thing beautifully, and that's
not necessarily what we want. So, don't
start from zero with it. Build a solid
first version the normal way, then turn
the gauntlet loop loose to sharpen it,
and then basically just make sure that
your foundation is set first, then
simply just a loop to polish it, and
you're going to get the best results.
Now, once this is actually working, we
can actually now focus on getting it
online in just one sentence. I'm
literally just going to go over to
Claude, and I'm going to tell it to
deploy it to Vercel, and then it
configures the project, it pushes the
ball, and it hands me back a live URL.
Something that I can now share, I can
open on my phone, and I can send to
anyone that I want to without ever
leaving the app. And on top of that,
there's more waiting once you are
comfortable. Routines run jobs on
Anthropic's cloud on a schedule. Review
your pull requests overnight, triage
your bugs every Monday morning.
Now, a few rules that you have to take
with you before you start building
because I learned this in the past few
months, and you don't need to follow my
mistakes. Please.
So, the first one is talk, don't type,
okay? We mentioned that earlier in the
video, but let's touch on it again. So,
when you type, you compress, and you cut
the context that actually matters. When
you talk, you leak all of it. So, click
the mic before you write a word. Now,
moving on to the next one, keep your
Claude MD thin. Treat it as a directory
that points, not a warehouse that
stores. If Claude can learn it from your
code, it doesn't belong in the file.
Now, after that, compact before you
switch tasks. Clean context makes a
better output, and it takes about 5
seconds to keep everything that comes
after it sharp. And the last one that I
want to mention, and this is probably
the most important one, send your big
jobs to the cloud. Fire the task, walk
away, and literally it come back to it
finished. Your laptop isn't your limit
anymore, your imagination now is. So,
that is Claude Code updated. The version
that actually exists right now.
Everything that we covered, prompting
for judgement plan mode, the voice, the
thin Claude MD, the skills, the
connectors, the parallel, the Claude
sessions, the doctor ordered.
It's literally just the foundation,
okay?
It's how you go from the version that
made you close the app to the one that
makes you wonder how you worked without
it. And all of the stuff that we
discussed today, all of it is inside our
free school community. The prompts from
today's board, the thin Claude MD
templates, the full workflow, all of it
is inside our school and the link is
down in the description below. And also
remember, it's free. So, go over today,
go and join. I guarantee you are going
to love it. And also, since you made it
to the end of this video, give this
video a like, subscribe to the channel,
and turn on those bell notifications so
that you never miss another upload. And
also, check out some of the other videos
on the channel. I know there's a bunch
of things that you can learn over there.
And as always, I'll catch you on the
next one.
