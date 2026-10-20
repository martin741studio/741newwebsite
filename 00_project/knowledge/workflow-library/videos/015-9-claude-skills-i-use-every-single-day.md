# 9 Claude Skills I Use Every Single Day

- Channel: Dubibubi
- URL: https://www.youtube.com/watch?v=LCwT00LrPZg
- Published: 2026-09-26
- Duration: 21 min
- Views at fetch (2026-10-11): 77,208
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

There are over 500,000 Claude skills out
there. GitHub is full of them, but most
of them don't even work, and some are
just nicely formatted system props with
a readme file. Very few are actually
worth installing. And you might think
you don't need them. Models are already
powerful enough, [screaming] right? Why
add a skill file? But here's the thing.
Every model follows its own patterns.
And once you've seen it, you can't unsee
it. That's why you need something to
steer it. These skills are built by
people in the trenches. You've got a
meta engineer, a security researcher,
and they've repackaged what works for
them, so you can use it, too. From a
skill that cuts your token usage by 65%
to one that creates motion graphics
using natural language. I've tested
hundreds of skills at this point, and
these nine are the ones I keep coming
back to every single day. Thanks to
HubSpot for sponsoring this video. We're
starting with the absolute holy grail of
Claude skills. The skill that arguably
started this whole craze with over half
a million installs. Of course, I'm
talking about the caveman skill because
why use many token when few token do
trick? If you haven't heard about the
caveman skill before, then chances are
that you are probably a caveman yourself
because this is unironically one of the
most useful skills I've ever installed
and probably the most entertaining as
well. We all know Cord is a complete
yapper. You ask for one simple request
and you get three paragraphs of great
question, but let me walk you through my
approach. That preamble is [music] not
only annoying, but it costs you tokens.
And tokens equals money. What I love
about Caveman is it drops all of it and
just gives it to you straight. It's like
having a spam filter for your inbox, but
it also saves you tokens. The creator
claims a 65% reduction in tokens saved,
but I actually tested this myself and it
was closer to about 35%. I'd ranked
Caveman higher, but everyone already
knows about it, so I'll leave it at
number nine. Next is a new skill that's
been gaining attention from an upand
cominging developer. Millions of lines
of code at Meta, Netflix, and now
Cursor, the person who helps build and
maintain the React compiler. That is who
wrote number eight. Of course, I'm
talking about Pstack. [music] Pack is a
set of skills from Potato with an E. And
the one that everyone's going crazy
about is Potato Mode. Her pitch is one
of my favorite lines I've [music] ever
read in a repo. I don't want to ship
like a team of 20 slob artists. And then
she says, if you want to go fast, you
first need to go deep. Which is the
exact opposite of how everyone is
currently using agents. By the way, the
move right now is spin up eight parallel
agents and pray.
And you can do it. It technically works.
It feels incredible for about 20 minutes
until Sunday comes around and you're
looking at 8,000 lines of code trying to
figure out which one of your robot
children broke your app. The insight in
Pstack is that the problem is not
running parallel agents. The problem is
trust. You cannot safely run 10 agents
if you do not trust what the agent
produces. Make one agent rigorous first,
then run parallel agents. Once you have
felt the difference, you cannot go back.
Once you go deep, you can't go to sleep.
And the cherry on top is the fact that
these are the actual skills she uses
every day at Kursa to ship thousands of
lines of code every single day. Okay.
Okay. Number eight was pretty solid, but
if you thought that was good, wait till
I tell you about rank seven. Hard credit
API keys, security rules, completely
skip auto tokens sitting in local
storage, and my personal favorite,
letting the browser decide how much
something costs. Do you know what that
means? Someone opens DevTools, changes
your $99 product to 1 cent, hits buy,
and Stripe just processes it because
your app basically asks the customer,
"How much would you like to pay?" So,
number seven is Vive Security built by
Chris Rarok. I never know how to
pronounce his name, and the team at
Aloa. If you've been anywhere near this
side of YouTube, you probably already
know Chris. I watch him all the time.
And this isn't just some generic prompt
that says, "Check my app for security
problems. It actually understands what
your app is using. If you're using
Superbase, it checks for Superbase
specific security issues. If you're
using Next.js, it checks for next.js
issues. And I think this skill is
massively underrated. It has under a,000
stars because the scary part about bike
coding isn't that you intentionally
wrote insecure code. The AI did. It
confidently hard-coded your API key. It
confidently skipped your security rules
[music]
and you confidently clicked approve on
it. So use AI [music] to check AI. Run
this on your app every time you make a
big update. I ran it on a side project
I'd already shipped 6 weeks earlier and
it found a few fatal [music] problems.
All right, Vive Security catches the
vulnerabilities you did not know Claude
wrote. But there is another blind spot
almost everyone has and it is bigger
than security. So, here's an
uncomfortable truth I learned while
researching for this video. Most of you
are using maybe 10% of what Claude can
actually do. You open the chat, you
type, you close it. That is the whole
workflow. Meanwhile, [music]
skills, co-work, code, and design are
just sitting there untouched. And I get
it. Anthropic shoots new stuff faster
than anyone can track. It is confusing.
That's why I wanted to share this free
guide called Claude at Work from HubSpot
that maps the entire ecosystem. It has
every product side by side so you can
see where each one fits. It even has the
current model lineup with which model
should I use breakdown and [music] three
realworld workflows showing you how to
chain these tools together. This guide
will show you exactly how the skills
like the ones we're talking about in
this video can fit into your daily
workflow in a way that actually
multiplies their capabilities. My
favorite one is the workflow that takes
a single video and turns it into a full
week of content across platforms. Step
by step with which Claude product to use
at which stage. If you're someone who
makes content, that one workflow alone
is worth the download. It takes one
breed and it will show you capabilities
you did not know you [music] had. Check
it out in the description. And thanks to
HubSpot for sponsoring today's video.
All right, back to the skills because
number six is about fixing the thing
Ford is genuinely the worst at. No AI
slop. Built by Peter Yang, it kills 22
patterns of AI writing that have
infected basically everything on the
internet right now. You probably already
know these. A lot of us have developed a
physical reaction to them. It's not X,
it's Y. The future isn't coming. It's
already here. What nobody tells you is,
and don't even get me started on the m
dashes, every single platform, [music]
LinkedIn, Twitter, Substack, YouTube
comments, they are everywhere. And here
is the trap. When you use AI to fix AI
writing, it polishes out the exact stuff
that made it sound human. Your weird
sentence length, your bad analogies, the
joke that only lands if people know you,
those were the good bits. Most writing
[music] skills sand them off and hand
you back a nicer flavor of the same
problem. This skill's actual trick is it
removes the patterns without flattening
your voice. And then this is the part I
genuinely love. It lists everything it
changed so you can actually argue with
it. All right, so as you can see, I've
made Claude write a short sales script
about my app Ace and it is full of AI
terminology. Here's the part that
matters. It's not X, it's Y. Wow.
So, we're going to go ahead and run the
no AI slop
skill. Let's see how it does.
And boom. As you can see, we now have a
script. And Ace is a onetime payment.
$150 for lifetime [music] access,
including every future update Ace ships.
No recurring fee ever. That's a huge
difference from here's the part that
matters. Ace isn't a subscription, it's
a one payment. Like that's a way better
improvement. And here you can see what
actually changes. So it's really easy to
understand. Rewrite the offer line. And
then if you want, you can argue in and
be like, "Hey, I actually didn't want
you to rewrite the offer line." It's
really cool.
That is the writing slot dealt with.
Number five deals with the code slot
problem. Coming in at number five, of
course, I'm talking about ponytail. And
Ponytail makes your agents think like
the laziest senior developer in the
room. [music] He says nothing. He writes
one line and it works. You know the guy.
Every team has one. You spend 2 days
building an app. You showing him and he
looks at it for 8 seconds [music] and
goes, "Why didn't you just do this?"
This skill is the embodiment of that
ponytailed individual. A perfect
anti-slop skill for code volume. Because
here is the thing a lot of people don't
realize about AI coding. The problem is
not that Claude writes bad code. It
actually writes pretty good code if you
know what you're doing. It just writes
far too much of it. Ponytail claims to
reduce the amount of code Claude writes
by up to 94%. But from my own test, it's
closer to around 50%. And there's some
pretty neat side effects, too, like pass
being about 20% cheaper and 27% faster.
Everything is verifiable on the repo,
but I recommend you try it for yourself.
Ponytail is one idea executed perfectly.
Right, let's go. Number four is the
entire operating system, and I'm about
to say something that might ruffle a few
feathers. Remember superpowers? Everyone
lost their minds over it. Every thread,
every video, every this changes
everything post. And honestly, it
deserved it at the time. It was good.
But this replaces it. I'm talking about
matte poke skills. And I'm not going to
lie, it is the best base layer I have
ever used because this is not a clever
one-trick skill like caveman or
ponytail. It is the foundation you put
underneath everything else. Here's how I
actually use it. And if you steal one
thing from this video, steal this. I
give my agent a link to the repo, kick
off a longunning task, and tell it to
use the skills where they make sense.
That is the whole instruction. I do not
micromanage which skill fires where
because the descriptions inside the
skills are actually good enough. It just
picks correctly. For example, inside
Matt Pok's skills, there is a code
review skill. I have Claude Fable
orchestrate Sonic models to do the heavy
execution work. It then uses the code
review skill to make Sonet review its
own output before it ever comes back to
Fable, the orchestrator agent. The slop
actually gets caught inside that loop.
The same model that wrote it is now the
same model that judges it. It never hits
my eyeballs. I just get a finished
product that's ready to test. All right,
foundation, reviewer, security, editor,
all the boring stuff is sorted, which
means we can finally get to the fun
stuff. All right, what if I told you
every single piece of motion graphics in
this video that you're watching was made
using the skill hyperframes? And I'm
going to say this straight up, but I
think it's actually better than
remotion. Remotion's great, but I'm not
trying to start a fight. Hyperframes
just produces better outputs more of the
time with less nagging. So, if you make
content, you already know the problem.
Motion graphics are the single worst
effort [music] to payoff ratio in the
entire pipeline. A 4-se secondond
animation that makes one point clearly
can eat an hour of your life in After
Effects. Then you watch it back and go,
"Actually, the easing is wrong." So,
here's what I'm going to do. I'm going
to describe an animation out loud right
now and we're going to see what comes
back. I'm going to link the hyperframe
skill and just say
create an animation of a really big
crazy firework explosion in the night
sky. And I'm just going to let this run
and let's see what it generates. And
we're done. That took roughly 8 minutes.
Let's have a look at the video.
Damn,
that looks nice. Wow, I love how it
explodes and shakes the sky. Well, there
you go. In 8 minutes, we were able to
create this sick ass motion graphics.
Imagine trying to do that in After
Effects. That would literally take you
an entire day to get all the particles
to look like that. Hyperframes makes
cool animations, but coming in at number
two, it turns Claude into an
awardwinning designer. All right, this
one's actually cheating slightly, but
coming in at number two, it's actually
two skills.
>> No, no, no. You can't do that. No.
>> Hey, it's my video. I make the rules
around here. But I'm not going to lie,
there are a lot of design skills out
there. Genuinely dozens at this point.
And I'm going to say something that
sounds harsh, but I [music] mean it.
Most of them are like the same six
prompts about white space wearing
different hats. These two are the ones
that survived on my [music] machine. And
the reason they both survived is they
are good at completely opposite things.
Taste is the oneshot king. If it's a
blank page, no existing design language,
you need something that looks [music]
intentional on the first try. Taste just
hands it to you. It is the I need a
landing page in 20 minutes and I need it
ASAP kind of skill. Impeccable is
[music] the opposite. It's the analyst.
It's not trying to be clever. It is
trying to be right. Point out a real app
with 15 screens and it goes through them
properly one by one. Maybe you've got
inconsistent spacing. [music]
You've got four different grays that
should be one gray. That button that's
like two pixels off on one screen only.
Things you have absolutely looked
directly [music] at and not seen. And
the combination of these two is where it
gets stupid. Taste for the first class.
Do you have something with a point of
view impeccable to grade it and grind
out every inconsistency? One gives you
the idea, the other gives you the
discipline. I've shipped things with
this combination that people assumed I
paid a designer for. Actually, no.
Before number one, here are four skills
that did not make the list, but
absolutely could have because I've seen
comments about every single one of these
and I would rather address them now than
read about it in the comments for the
next 6 months straight. First, unlazy.
This one genuinely hurt to cut out. It
is an anti- laziness skill for agents
built around something called the depth
tree method. [music]
Here's what it does. It splits a task
into layers and gives every single leaf
the full time budget of the whole task.
So, effort actually multiplies with
depth instead of getting thinner. It's
built on actual research into model
laziness and premature [music]
completion. That thing Claude does where
it writes about 80% of the code and then
types the rest follows the same pattern.
I hate that. Unlazy fixes it. So if you
do long agentic runs, this is amazing.
Go get it. Next, you've got AI job
search. Exactly [clears throat] what it
sounds like if you are job hunting right
now. This is probably the most
immediately valuable thing in this
entire video and it did not even make
the list. Next, you got agent reach.
Give your agents access to gated parts
of the internet. Use it responsibly
though, please.
>> With great power comes great
responsibility.
>> Fourth, you've got open design. And this
one fixes a genuinely annoying
limitation. Claw design is one of my
favorite creations from the Anthropic
team, but you cannot extend it with
skills. Open Design lets you. It's
basically an open-sourced free claw
design alternative that lets you use
skills like impeccable and taste to
improve on your UI screens. And I want
to reframe something real quick because
number one is not the flashiest skill on
its list. Hyperframes makes pretty
things. Ponytail has better numbers.
Number one is here for a different
reason. It is probably the most
versatile, most underrated, and biggest
upgrade to your agent skill artillery
today.
Now, this skill was originally built to
train AI models. The mechanism is
brutally simple. Run hundreds of tiny
experiments, keep what works, and then
throw away what doesn't. Repeat. And
that's it. That is the whole thing. Now
read that again and tell me what part of
it is actually about machine learning.
Nothing. Nothing about that is specific
to models. It is just the scientific
method. With the patience problem
removed, because the reason you and I do
not run 100 experiments on anything in
our lives is not that we do not believe
in the method. It's that 100 experiments
is 100 experiments. So run 100
experiments to optimize your budget. Run
100 experiments on your calorie intake.
[music] Run 100 experiments on your
app's UI. Run hundreds of experiments on
your thumbnails. You are not limited by
the skill. You are [music] limited by
what you thought to point it at. All
right. Now, a lot of people don't know
this, but when I first built Ace, I
actually ran the autoresarcher skill on
my app, and it was able to create a lot
of tiny little delight moments within my
app. Like, if we just click on any of
these and we look at the whiteboard,
even the loading screen, you can see
like just being able to connect the
models and stuff like that. It it
created a lot of tiny delight moments,
like literally hundreds of them, and
they stacked up on top of each other to
the point where like I don't even know
what is and what isn't done by the auto
research skill anymore. Things like the
line glowing when it's connected, the
ability to change the things, the pill
of the model picker here, like how that
menu looks. A lot of this was designed
and implemented by the auto researcher
skill, but we're not going to be doing
that today for today's example. I've
actually got my gym workout and I've
pasted it in. It's a 5day upper lower
split. All I'm going to say is use the
auto research skill methodology because
we're not using the skill because it's
used to train AI agents. We're using the
methodology of the skill to run 100 tiny
experiments to improve my gym routine. I
want to gain hypertrophy around the
arms, look bulkier and tone. I'm 167 176
cm tall and I weigh 80 kg. I'm a 25
male. Now, I'm going to go ahead and
send that front.
And I'm doing this just to prove that
[music] you can literally run this skill
on anything and it will find the most
optimal best solution. Just like when I
ran it on my app and I focused it on
finding, you know, animations and tiny
little delight moments that would make a
user want to stay on the app and have a
more enjoyable experience. It's the
exact same thing I'm doing with my
workout routine. And I'm using Opus 5 on
medium effort cuz you need to also
consider that running 100 experiments is
not cheap. So, I'm going to let this run
and let's see how it does.
Okay. So, as you can see, it went ahead
and ran 100 experiments. Five base
diagnosis, five things wrong in effect
order. Direct arm volume is seven sets a
week each. Priority range is 12 to 20.
Five of seven triceps sets are push
downs. No stretch position biceps work
at all. So, yeah, pretty interesting.
Let's have a look. And boom. If you
compare it to the previous plan,
you can see day one, we've got barbble
bench press, three sets, six to eight
reps, lat pull down, incline bench,
seated cable row. This all seems to look
the same, okay? Except we it changed it
to an overhead cable, easy tricep
extension, and then it also did incline
dumbbell curls. Okay, so it's changed
that slightly. Day two, we've got lower,
which is unchanged. And then day three,
it's actually doing arm priority. So,
it's changed this completely to weighted
dips or close grip bench, weighted
chin-ups, overhead press, chest
supported. So, very armheavy movements
here. Lower is the same. Then upper,
it's actually added a bit more of what
we missed in day three. Super cool. And
there you go. Everything else on this
list makes you faster at something you
were already doing. This one actually
changes the size of the problem you're
willing to attack and it costs nothing.
It is just a text file. And there you
have it, the secrets to all my favorite
skills. I've left a link to all of them
in the description. Leave a like on your
way out. Peace.
