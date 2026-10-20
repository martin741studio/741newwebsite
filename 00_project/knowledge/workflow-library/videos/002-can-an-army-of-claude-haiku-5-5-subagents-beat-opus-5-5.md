# Can an Army of Claude Haiku 5.5 Subagents Beat Opus 5.5?

- Channel: Dubibubi
- URL: https://www.youtube.com/watch?v=Ug3x37N6Z_E
- Published: 2026-10-09
- Duration: 15 min
- Views at fetch (2026-10-11): 116,465
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

Haiku 5.5 is out and it costs 40 times
less than Opus 5.5 which is kind of
insane if you think about it because
that means for every dollar Opus spends
Haiku spends 2 and a half
but cheap models are usually cheap for a
reason right on their own they're fast
but they tend to fall apart the moment
you give them any meaningful work so
today we're putting two opuses
headto-head one will work solo and the
other will command an army of haiku
agents so we can answer the question can
we really get the same quality of work,
but for a fraction of the cost. Now,
I've designed three different tests to
push both setups to their absolute
limits. Each test, there will be four
points up for grabs. Two points for who
has the best Apple quality, and one
point each for who is the cheapest and
who is the fastest. So, let's get
straight into it. For the first test,
we're building a game that you probably
played at least once in your lifetime.
That's right, we're building an Angry
Birds clone. And this is actually a
really good first test for the team
because a game like this is a lot of
work. You've got physics, levels, menus,
scores. So, this will really show us how
well Haiku will be able to execute on
these more complex tasks. So, on the
left, we've got Opus 5.5 on its own. On
the right, we'll be running our Haiku
army through Opus. I've got both set to
extra high effort. So, here is the
prompt for the Angry Birds clone. And
boom, I've sent it. Now, both sides get
the exact same prompt. The only
difference is that on this side, I've
added the /delegate skill, which is my
own custom skill that turns Opus into a
manager. It does all the thinking and
planning, then hands the actual building
to Haiku sub aents. The reason I'm using
a skill is because I actually noticed
that when I would just ask Opus to use
Haiku sub agents directly inside the
prompt, it would actually start to cut
corners and the handoff ended up being
quite messy. However, with the skill,
I'm able to clearly define Opus' role as
the manager as well as Haiku's role as
the executor. This makes the end result
a lot tighter, and it costs the exact
same. Now, you could easily just build
your own version of this skill by just
copying the transcript of this video.
But if you just want mine, which is
ready to go, it's inside my community
with a bunch of other skills and
resources. I'll leave a link in the
description. Anyways, you know the
drill. We've got the usage tracking
dashboard here. So, we can measure the
input tokens, the output tokens, how
long each build takes, and what it all
costs with Opus and Haiku tracked
separately on the team side. So,
nothing's going to slip past us. So, I'm
going to let these models cook and I'll
see you in a bit. A few moments later.
All right, both builds are complete.
We're starting off with the Haiku team.
Let's go ahead and play. Level one,
first flight.
Ooh, I like that noise.
Boom. Oh, that's satisfying. That's
really satisfying.
Boom. Easy enough. Wait, my guy didn't
die. You're joking.
Boom. Okay,
we won the first round. We didn't get
three stars, but is what it is. Okay,
Canyon Clash. Let's give this a go. I
like that there's TNT there, too. That's
kind of cool. It's actually kind of
satisfying.
Boom. Oh, three stars, baby. We did that
 All right, this is the last level.
pretty good. Oh, we should be able to
get this easy, man. It's actually crazy
to think that Haiku built this. I never
would have believed that in a million
years.
Come on.
Yes. There we go. Yo, that was pretty
fun. That was pretty solid. All right,
Haiku. Not bad. Not bad. Let's try out
Opus solo build. All right, this
definitely feels a bit more 3D. Whoa.
Okay, it's got this cool little
animation here. It's pretty satisfying.
Even the way that the sling kind of goes
back and forth. Super satisfying.
Oh, that was such a good hit. Come on.
You guys got to give me props for that.
I think in terms of output quality, the
Solo Opus build definitely wins here.
Let's have a look at the dashboard.
So, interesting. Okay, not a huge
saving, but it still is a saving. And it
opus with the haiku taking significantly
longer here. Now, I do want to point out
that
initially haiku is actually losing in
cost because it looks like it tends to
frontr run a lot of the token usage
because it's spawning a bunch of
different sub aents to complete the task
as you can see the gap here. However,
now there's obviously a difference and
we can see Haiku tokens made up 91% of
the lanes total compared to Opus' 9%.
So, I'm going to have to give Opus by
itself another point for winning on the
time. And I'm going to give Haiku one
point for the cost. Opus is in the lead.
Let's see if Haiku can bring it back in
the second test. All right, next up.
Building a game is one thing, but a plan
can only tell you what to build. It
can't really tell you how it should
feel. So, I want to see if Haiku has any
taste. For this test, I'm getting
inspiration from Kevin Neo where it gets
Claude to create these beautiful
animations using code. So, we're going
to be doing the exact same thing. Here's
the prompt. We're making an animated
samurai short film, which is going to be
30 to 60 seconds with a full story
hero's journey arc. And every frame will
be drawn using JavaScript in the
browser. they have full creative freedom
over what the story is about. So, let's
see how they actually do. Anyways, I'm
going to let these two run and I'll see
you in a bit. So, in case you were
wondering, this is actually what it
looks like when you're running up a
bunch of sub aents. You can see on the
right hand side a bunch of Haiku 5.5
agents that are running. You can see how
many tokens they're using, their tool
calls, and you can actually go in and
view their transcripts if you like to
see what it is specifically that they're
working on. You can see we've got 13 14
total Haiku sub aents running right now.
So, a lot of delegation happening. Let's
see the final result. All right, both
models are done. I'm really excited
about this one. Let's start with Solo
Opus.
>> They say a red thread binds us to those
we love. His daughter tied one to his
sword so he would always find his way
home.
>> Dude, Opus made this. Oh my god. I'm
impressed. I'm impressed with myself,
man. I'm That's crazy. I used 11 labs
for the narration, by the way, if you're
wondering.
>> Then smoke rose beyond the mountains,
and he went to meet it.
>> [bell]
>> Damn.
The thread remembered for him
clean
>> and it led him home.
[music]
Some threads cannot be cut.
>> Wow. I am really impressed. I'm not
going to lie. I wasn't expecting that
good of an output. I don't know how
Haiku is going to be able to compete
with this, but I'm super excited now to
see what Haiku did. Let's take a look.
Every story begins with a separate
beneath the old plum tree. A master
passed on his blade.
The wind took him and let only pedal.
>> Then rude the b
loud on the sound effects
in the darkness. His master's words
returned. That's pretty cool.
>> O.
When the ick settled, Spray did return
>> and the circle was complete.
>> Don't get me wrong, Haiku's is
impressive, but this test has just made
me realize how freaking good Opus 5.5
is. Holy This felt like a movie.
Even the way that it was narrated, even
the sound, everything about Opus Solo
has absolutely blew me away.
>> They say like, how nice is the voice?
>> A red thread binds us to we love,
>> dude.
This is incredible. Absolutely
incredible. Wow. I'm not going to lie. I
think Opus definitely wins on output
here. Again, I'm going to have to give
it two points. Let's have a look at the
dashboard. And I'm not going to lie,
you're not going to be impressed.
70. Dude, haiku costing nearly 80% more
took an extra hour and it still produced
a worse result.
>> Come on, man. The gap between Haiku
managing everything and then Opus
planning its management really isn't as
effective as I thought it would be. Now,
I'd be interested to see like if we had
Sonnet in here, would it cost more or
would Opus actually not have to give as
much feedback and so it would end up
costing less? That is something that I
want to try after this. But anyway, I
think it's a flatout outright winner for
the second test. Opus 5.5 on Solo wins
in quality, it wins in speed, and it
wins in cost. [clears throat]
Man, Haiku really got to bring it back
with this next one. Let's see how it
goes. All right, for the final test,
we're going in the complete opposite
direction because one thing I actually
use these models for constantly is
reviewing code. And this is the test
where the team could actually fall apart
because finding a bug means
understanding how the whole app fits
together. And that's exactly the kind of
thinking we took away from Haiku. Here's
how it's going to work. I'm going to
give them access to my app as code. And
we're going to see how many bugs they
can find and fix. Solo Opus does it all
by itself. And on the team side, Opus
splits up the app and hands each piece
to Haiku, which will hunt for bugs. At
the end, I'll be sharing their bug
report with GPT6 Astra, which is
currently the best model for code
review, and it's going to give them a
score. For each confirmed bug, they're
going to get one point. However, for
every bug that's made up or
hallucinated, they actually end up
losing a point. So, if Haiku just makes
up a bunch of bugs to look busy, it
actually hurts the overall score. All
right, I'm going to let these models
cook and I'll see you in a bit. Okay,
both builds have just finished up and I
actually want to start on the usage
tracker first because we can see a
massive 61%
saved compared to Opus. And this is
interesting because we can really see
the Haiku team shine a little bit in the
code review task compared to when we
were doing the animations, right? So,
it's interesting to see the strengths
and weaknesses that we're getting here.
So, without further ado, let's go ahead
and look at Haiku's score chart. So, we
can see here that I found a total of 103
bugs.
However, those are just the confirmed
ones. It actually ended up with 14 that
were rejected or hallucinated or made
up, leaving its final score to 89. Now,
this is still pretty solid. When I gave
Fable this task, it actually scored
around 21 bugs recently. So 89 is still
really really good. I recently gave this
task to Sonnet 5.5 and you can see it
found a total of 87 bugs with a score of
85. So the Haiku team scoring 89 is
pretty is not bad. It would have beat
Sonet by itself. But will it beat Opus
5.5?
Let's have a look. And boom. As you can
see, final score 122 confirmed bugs.
There wasn't a single bug that was made
up, which is really interesting because
both models or both teams have Opus
except one team with Haiku seems to get
lost in the source a little bit. Now,
I'm not sure if it's the haiku models or
the handoff or the back and forth and
where these madeup bugs are coming from,
but one thing is clear. Opus definitely
wins this task on output quality. So,
that's two points to Opus for finding
more bugs and having a better output
quality. However, that's one point to
Haiku for cost. And we're going to have
to give Opus one point for speed as
well, as it did finish the task 10
minutes faster. So, after all three
tests, it's 10 points to two for solo
Opus 5.5.
Damn, I honestly didn't expect it to be
that one-sided. Opus won on quality
every single time. Haiku's only two
points came from cost, and on the
Samurai film, it didn't even win that.
The team cost nearly 80% more and took a
whole extra hour. Now, don't get me
wrong, Haiku still built a playable
Angry Birds game and found over 100 real
bugs inside of my app. But I think the
problem is the handoff. Every time Opus
hands Haiku a job and checks its work,
that back and forth costs tokens. On the
code review, where the app splits into
separate pieces, the team saved 61%. On
the film, where everything has to fit
together, the savings completely just
disappeared. So, if a job splits cleanly
into pieces, like hunting for bugs, give
it to a haiku team. If it needs taste or
the full picture, let Opus do it alone.
Next, I want to run this same setup with
Sonnet 5.5 doing the work and see if a
smarter worker means Opus has to step in
less. So, if you want my slash delegate
skill, it's inside my community link in
the description. Let me know in the
comments which models you want me to
test next. I'll see you in the next one.
Peace.
