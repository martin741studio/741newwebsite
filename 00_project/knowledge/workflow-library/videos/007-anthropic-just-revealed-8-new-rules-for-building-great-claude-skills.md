# Anthropic Just Revealed 8 New Rules for Building Great Claude Skills

- Channel: Ben AI
- URL: https://www.youtube.com/watch?v=npS5jzOoji8
- Published: 2026-10-06
- Duration: 14 min
- Views at fetch (2026-10-11): 22,017
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

I recently looked at Entropic's guides
and best practices on cloth skills, and
I found eight tips and techniques to
build far more effective skills for
automating work. So, in this video, I'll
cover eight ways from beginning to
advanced to build better skills that
actually automate work reliably. If you
don't know me yet, I'm Ben. I'm a
three-time founder and now run an AI
agency and one of the largest AI
communities for professionals and
business owners where I teach how to use
AI to automate work or build an AI
business. starting with the first and
probably most important one which is to
stop prompting or planning your skills
into existence but instead to do the
task once together with Claude and then
turn it into a skill after. Now many
people including me used to build skills
by thinking through planning out a
process and then giving an extensive
prompt to Claude to build a skill out of
the task you're trying to automate. But
the entropic guide specifically says to
complete a task first without a skill
because as you work, you'll naturally
provide context, explain preferences,
and share procedural knowledge in order
to get to a good outcome. And then after
successfully completing the task with
Claude, you ask Claude to create a skill
out of the process, which is really easy
to do with the turn into a skill button
here in every chat or by just telling
Claude after you've done a task, please
just turn this into a skill. And the
reason is simple. Just like with humans,
the show don't tell principle works far
more efficiently because people tend to
be bad at describing a process that
lives in their head. But it becomes easy
when they actually do the task. And this
method becomes even more efficient and
easier to do for some kind of task with
their new record a skill feature, which
I honestly think is one of the most
underrated and underused features in
Cloud right now, where you just do the
task once you're trying to automate
yourself. You explain what and why
you're doing it. Clot captures your
screen and all the clicks you make,
reads the voice transcription to
understand why you're doing this, and
then when you stop, it automatically
turns the entire process into a skill.
For example, here I built my email triad
skill through this method because I've
seen that this simply brings out a lot
of the things that are hard to
articulate around a task when you're
just trying to explain it versus
actually doing it. So, I highly
recommend uh to making the record a
scale feature or doing the task once
together with clot and turning it into a
scale after as your default way of
building skills because you'll uh you'll
see that in general they work far more
efficiently than prompting a skill into
existence. Now, the second key principle
to follow when building skills is to
build focused taskspecific skills. This
is what I've personally also learned,
and I've seen this as one of the most
common mistakes people make when
building skills, which is building
skills that are too broad or pack in too
many tasks inside of the same skill. And
Tropics in-depth guide on building
skills specifically mentions that the
most effective skill creators iterate on
a single task before expanding the
skill. And in their best practices
guide, they specifically mention to keep
skills small in scope focused and to
create separate skills for different
workflows because multiple focused
skills compose better than one large
skill. But how do you know if you've
included too much in the scale? And the
way I like to think about it, which is
also how we approach scoping in my AI
agency, is when you look at the entire
process you want to automate or build a
skill out of, for example, this only
start with the smallest part of that
process that would still give you value
and build a skill around that first part
first. So in this case, research would
already give me value. So once that part
works, from there, you can expand or
often what's even better is to build
separate skills for the rest of the
workflow. So, I don't pack all of these
inside of one skill. I separate them and
then I run them separately in the same
chat window if I want. And another added
benefit of this is that smaller skill
files also keep the context window
cleaner, meaning your AI will actually
perform better. Now, the next one is to
treat a skill like a business process,
not like a finished file. As Entropics
guides mention, skills are living
documents. So, just like any business
process, they should be updated when
things change or new edge cases appear.
In a blog article, Entropic mentioned
that their best skills began as a few
lines and they got better because people
kept adding to them as cloth hit new
edge cases. I've personally also seen
this. Rarely are skills perfect in the
first try. Uh my best skills I've
probably iterated on and updated them at
least five to 10 times and some only
become useful after that many
iterations. And entropic actually
recommends using one chat for pure
building of the skill and refining of
the skill and one separate chat for
testing the skill to make sure it's
unbiased. So once you have the first
version with clot A you basically test
um the the skill on a real workflow with
cloud B and if it makes a mistake you
tell that to cla and try to refine it
with cla and again that is to make it
unbiased and to have one specific focus
for each of the agents. And that cycle
of course you can repeat multiple times.
You can even add in a self-improvement
rule in the scale if you often hit edge
cases which is essentially a line like
this here that instructs claw that every
correction you give in a chat will
automatically be updated in the scale
file. You can add in a self-improvement
rule really simple by just saying
something like add in a self-improvement
rule that instructs the skill that
whenever I give a new update point out a
correction or mistake it automatically
updates the skill with a new rule. Now,
if you want access to all of the prompts
that I cover from this video to build
better skills and even a skill creator
skill that I developed myself that
automatically applies all of the best
practices from this video automatically
on new skills you want to build or to
optimize existing ones, you can download
them for free in the first link in the
description below. Now, the next one
might sound obvious, but many people
don't do it yet, which is to add in
input and output examples. Now, this is
one of the most mentioned best practices
in these guides uh for skills where
output quality depends on seeing
examples provide input or output pairs
just like with regular prompting. And
this is of course because examples
convey the desired style and level of
detail to clot more clearly than
descriptions alone. And examples are one
of the most reliable ways to steer CLA's
output format, tone, and structure. Now,
in my experience too, having good output
examples is really key for design, copy,
or creative scale use cases. In my
experience, you really want to have at
least three to five good examples, but
I've seen especially for copywriting,
even up to 20 examples can get you far
better outputs in your skill. Again,
it's the show don't tell principle. So,
when building your skills, really take
the time to give it some good examples
if you have them. And if you don't have
good examples yet, you can take them
from others. Or an easy way to build up
these examples is again to add in a
self-improvement rule that automatically
saves good outputs every time you run
the skill. Again, you can simply add a
role to your scale with a prompt like
add a self improvement role to the
scale. Anytime I correct your output
during a process or get an output I
explicitly like, ask me whether that
should become permanent in the scale. If
I say yes, update it with the saved
example. Again, you can get the full
prompt in the free resource. Now, the
next one is to add progressive
disclosure into your skill. But before
continuing very quickly, if you enjoy
this type of content, you'll really
enjoy my AI accelerator where you'll get
access to my 30-day Claude course that
gets you from beginner to pro in 30 days
and less than 1 hour a day. It teaches
you everything you need to know and
nothing you don't in order to actually
use cloth to automate work. On top of
that, you'll get access to a full course
on growing an AI business, from getting
your first clients to scaling an AI
business based on everything me and my
team have learned over the last three
years. You'll also get access to
unlimited one-on-one live AI consulting
with AI experts to get personalized
guidance and help and a big library of
skills templates and resources across
all business departments to give you a
heads. So, definitely check it out in
the link in the description below if you
want to dive deeper into AI. Now,
Entropics engineering blog uh mentions
that progressive disclosure is the core
design principle that makes agent skills
flexible and scalable and that because
of progressive disclosure, it
essentially means that the amount of
context that can be bundled into a skill
is effectively unbounded. But if you
don't apply this correctly, it will hurt
the performance. And in my experience,
the skill creator skill from entropic
itself doesn't always uh apply this
principle very well. So what does this
actually mean? Progressive disclosure.
Of course, a skill can consist of a
skill.mmd that lays out the process to
follow and a reference folder with extra
files and context. Now, we all know that
skills and agents perform better when we
give them more context and we can add
them into reference files inside of the
skill. For example, my newsletter skill
here, I have uh extra context on my
background, what we do, my ICP, my voice
personality, and examples. But
progressive disclosure essentially means
that we only want our agent to use
reference files when it's required and
not make it read all of it at the start
when using the skill. Because if we load
all of these context files at once, it
will pollute the context window leading
to a worse performance. So we want to
make sure that the skill only reads the
relevant reference files at each of the
steps in the process. So you can see in
my newsletter scale in each of the steps
I specifically mention the reference
files it has to read before executing
that step and I do that for each of the
steps in the process. In the next one it
reads another one and so forth. And this
really works far better than plot just
reading everything at the start because
it starts forgetting everything at the
last step. Now again in my experience
the skill creator scale by Entropic
doesn't apply this principle very often
automatically. So you can use a prompt
like this uh which again you can copy
and paste in the link in the description
below or again use my skill creator
skill which automatically applies this
principle um when building or updating
an existing skill. Now the next
important tip is to force the use of sub
aents for research or investigation
step. Now Entropic specifically mentions
that the context window is your
fundamental constraint. So we need to
use sub aents to keep research out of
it. And because many skills actually
follow a very similar pattern of a
process which is first to getting data
from somewhere from the internet or from
your softwares then interpreting that
data and then getting something useful
out of it. For example, a data analytic
skill would first have to go through
your softwares then pull the data and
interpret it and then create a nice
report or a dashboard. Uh an ideation
skill will do research on the internet
then filter the ideas and create good
suggestions for you. Many scales follow
a similar pattern. The problem with this
is that MCP or connector use to get this
initial data burns a lot of tokens and
because it uses a lot of tokens, it
pollutes and fills up the context window
all the way at the start and make cloud
perform significantly worse at the most
important step of your skill, which is
actually interpreting the data and
getting something useful out of it. And
this is simply because the more your
context window fills up with tokens, the
dumber cloud gets. So if you have a
research or connector step at the start,
you want to make sure to do that with
sub agents so they actually do that.
Then only uh send back a summary to the
main agent that doesn't pollute the the
context window that much so your agent
still has high performance when doing
the most important uh steps. Now
sometimes cloud does this automatically,
but very often it doesn't. So adding in
a simple rule uh to do that initial
investigation step through sub agents
can instantly significantly improve the
quality of your skill outputs. For
example, in my uh video title ideation
skill that first does research on top
performing um titles for a specific
topic on YouTube, I have a specific
instruction here. every connector call
runs inside of a sub agent so that it
doesn't pollute the context window when
it's actually interpreting that data and
giving me good suggestions for titles.
Again, I've added a prompt here u that
you can use to build new skills or
update existing ones um so that it uh
incorporates this specific rule inside
of the skill or again you can use my
skill creator skill which automatically
adds this rule in. Now the next one is
to let your skills give you multiple
outputs at every checkpoint. Now many
skills especially copywriting and design
type skills can function uh exactly as
they were intended but you just don't
like the specific angle wording or
direction it took at the output which
still results in endlessly iterating and
improving on output. Now, one really
easy way to save time on this iteration
loop is to make your skill give you
multiple variations. Because if you get
multiple variations to choose from, the
likelihood that one of them is in the
right direction is just a lot higher.
And even when you have to iterate, there
will be fewer things you have to
correct. Now, I've been adding this in
for every human in the loop step at
every scale, and it saves me a ton of
time on uh iteration. For example, in my
newsletter skill, at the first human in
the loop step, it gives me multiple
variations on potential angles I can
take for this newsletter. Now, usually
there's one that I like or I have to
correct a small thing. The next step,
based on that angle that I chose, it
generates three uh variations of
outlines we can use for the newsletter.
Again, I can pick it, make some small
adjustments, and steer it more and more
in the right direction uh to get to the
final newsletter output. And I do this
for each of the steps, getting to
subject lines, getting to the copy of
the newsletter, and it really speeds up
the workflow, and you sort of direct the
model towards a good output. Now, this
doesn't come out of the best practices
guide of Entropic, but it's actually how
they design many of their own skills,
and that's also where I got the idea
from. So, it's a simple rule you can add
into your skill. I added a prompt again
if you want to update or build a new
skill with this rule embedded. Or again,
you can use my skill creator skill which
is also in the free resource to
automatically embed this into your
skill. And then the last one is to stop
the skill from autot triggering if you
don't want it to autotrigger. Now skills
of course can be triggered uh with the
slash command. Uh but they can also be
autotriggered if cloth thinks one is
relevant to use for a specific task you
give it. And it does this by reading the
description of your skill. Now, in my
and many other people's experience, when
you want to use a skill, you just always
use the slash command. And the autot
trigger often leads to a model
triggering the skill when you don't want
it to be triggered. Now, many people
don't know this is possible, but
Entropic actually made it possible to
turn off this auto trigger. All we have
to add into the skill is a rule that's
called disable model invocation and set
it to true. For example, you can see
that in my LinkedIn writer scale here,
we have this line here at the top,
disable model invocation true. And this
means clock uh cannot autotrigger it but
I can still use it with the slack. And
this has another benefit because now the
skill description is not loaded in every
new chat with claude which keeps the
context window cleaner. Now again quite
easy to do. You can use this prompt
which again will be in the free
resource. Make this a human triggered
scale only. I don't want cloud to auto
invoke it. Set disable model invocation
to true in the front map. Or you can use
my skill creator scale which will ask
you if you want to autotrigger your
scale or not. And based on that it will
automatically embed this rule.
