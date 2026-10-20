# The ONLY Claude Skills Tutorial Beginners Need in 2026

- Channel: 100x Engineers
- URL: https://www.youtube.com/watch?v=TyB7kLZPVKo
- Published: 2026-08-01
- Duration: 25 min
- Views at fetch (2026-10-11): 65,854
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

Claude Skills is easily one of the best
things you can learn in 2026 to level up
in AI. And I'm sure you've heard a lot
about it already. Maybe you even tried
creating your own custom skill at some
point. But I'd like to take this
opportunity to cover everything you need
to know about Claude Skills all the way
from using it as an absolute beginner to
an absolute pro. In this video, we will
cover the following things. What is a
Claude Skill? How to use it? Level one
of using Claude Skill, which is using
Claude's default skills. Level two,
which is modifying a Claude Skill. Level
three, which is using partner skills
[music] and plugins. And level four,
creating your own custom skill. And
finally, I will give you a pro secret.
This is basically [music] a tip that I
haven't seen anybody give out in any
Claude Skill tutorial video. And if you
learn this pro secret, the way you write
your custom Claude Skill is going to be
five times better than most people's.
And we'll cover all of this using
real-life examples and demos [music] of
workflows that I personally use for my
work. So, hit that subscribe button and
let's get [music] into it.
Let's start with learning what a Claude
Skill actually is. In case you already
know the basics and you just want to go
straight to the demos, feel free to
navigate this video using the chapters.
But in simple words, a Claude Skill is a
file that contains a set of instructions
and guidelines to perform a certain
task. It's that simple. The coolest
example I can think of is the movie
Matrix, where Neo learns kung fu inside
the Matrix. There is a scene where he's
just downloading martial arts skills
while being plugged into the Matrix.
That's very similar to what skills are.
For example, let's say that you make
decks in a certain way. There's a format
that you use, there's certain brand
colors, there's certain fonts, and even
a specific tonality. A Claude Skill is a
file that contains all those guidelines
and instructions. So, that every time
you want to perform that task, say make
a deck, instead of writing all those
instructions every time you prompt, you
can just invoke the skill and get
exactly the output you want. And this
file is a dot md file, which stands for
markdown, which is a fancy way of saying
that it's just a read-only text file.
Now, in order to use Claude Skill, you
need to make sure of this one thing on
your Claude account. Go to customize and
click on capabilities. And if you scroll
down, you'll see this thing that says
code execution and file creation. Just
make sure that both these things are
toggled on. Now, most of the times this
is toggled on by default in most
accounts, but just make sure of this
before trying out Claude skills. Once
that is set, let's see how to use a
skill. Now, there are fundamentally two
ways to use a skill. The first is when
you prompt normally and Claude
automatically selects the relevant
skill. For example, let me ask Claude to
turn this research paper that I have
into a deck. So, I'll upload my research
file and I'll just say, "Turn this into
a deck so that I can understand this
easily."
Now, I haven't asked Claude to activate
any particular skill at all over here.
But, if you see, it's already saying
loaded pptx.skill, which basically is
Claude understanding my requirement and
loading a skill that is already there
inside Claude by default, which is
basically a skill required to create
PowerPoint presentations. So, here
Claude automatically invoked the PPT
skill. So, that's the first way of using
it. You don't directly invoke it. The
second way to call a skill, which is
what you'd be using a lot of, is when
you call it directly instead of letting
Claude decide by itself. To do this, all
you need to do is in the chat, type
forward slash and out comes a list. Now,
you won't be able to see a lot of
options here because you haven't enabled
a lot of Claude's default skills and
neither have you created a lot of custom
skills. But, I have quite a lot of
skills that I have installed and created
over here, so I can see a long list of
skills. You can see UGC ads, I can see
seed on director, which actually creates
prompts for me. I can do video prompt
builder, which is another prompt
building skill that I have. There's a
campaign planning skill, there's a
competitive brief skill, there's a
content draft skill, quite a lot of
skills that I actually have over here.
And if I want to use one of these
skills, I just have to click on it and
type my prompt and Claude will use the
skill by default. And that's how you use
a skill that you already have. Now that
you know how to use a skill, let's go to
level one of Claude skills, which is
using Claude's default skills. If you
click on customize and if you go to
skills and click on browse over here,
you will basically get to see a bunch of
default skills that Claude already has
built in. This opens up this box that
you can see in front of you, which shows
a set of skills that were designed by
Claude for some of the most common
tasks. If you want to know more about
what a skill does, just click on one of
these things and you will get a
description over here. So, I've clicked
on Theme Factory, and Theme Factory is
basically a skill that provides curated
collection of professional fonts and
color themes, each with carefully
selected color palettes and font
pairing. So, it's basically just a
collection of fonts, and you can already
see some of the font files that are
already added over here. So, if you want
to know more about other skills, you can
just click on it and you can just read
the summary of it. Now, if I want to add
any of these skills, all I need to do is
click on this plus icon, and that's it.
It's added onto my skill library. And
now every time I hit forward slash in
the chat, I can access this skill
directly. Let's actually try this out
and create an output. Now, let's scroll
through this. I can see this skill
called forward slash learn, and the
description is use this skill when the
user wants intellectual understanding.
Learning how or why something works, not
getting a task done, or soliciting
Claude's judgment. This kind of seems
like an interesting skill. So, what I'm
going to do is I'm going to click on
install, but before that, I'm actually
going to write a prompt without having
this skill triggered. So, I already have
that written over here, and my prompt is
I want to learn about convolutional
neural networks. And Claude made me made
me a basic generic response. It
basically gave me the definition, it
gave me the core idea, it kind of gave
me the entire answer that I was actually
looking for, and also some resources
that it was actually pointing me
towards. Now, let's see what actually
happens when this skill is actually
activated. So, I'm going to first click
on install. I'm going to close this.
I'm going to do forward slash learn,
which is me invoking the skill, and I'll
write the same prompt. I want to learn
about convolutional neural networks, and
I'll click on enter.
Now, Claude is going to first call on
the skill. You can actually see that
right here. It's loading the learn skill
right here.
And observe how it actually responds. So
instead of giving me the information,
it's actually asking me a question.
What's your starting point? Do you
already know how neural networks are or
are you fairly new to this whole area?
Is there something specific pulling you
towards CNNs? So it's basically trying
to get more and more context out of me
so that it can determine where I am in
the learning process and teach me
accordingly rather than give me a
generic response. So do you see how the
simple addition of a skill completely
changed how Claude is responding to you?
And this by the way is just level one.
These are just Claude's default skills.
I want you to go and explore some of
these default skills and see how your
output actually changes. And once you're
done with that, let's move on to level
two. Now in level two, instead of just
using a default skill, we're going to
modify it and use it. So here we have
this default skill called brand
guidelines. And it is basically a skill
that emulates Claude's brand guidelines
whenever you make a deck or a document
or a PDF or something like that. Just so
that Claude can actually give you nicely
formatted things. It is going to give
you in Claude's brand colors. But what
if I want to do it for my brand colors?
Because Claude's brand colors are
basically orange and gray and all that.
What if I have much more of a poppy vibe
and I actually want to do that? So what
we're going to try and do over here is
we're going to use this skill and we're
going to modify the skill so we don't
have to write it all the way from
scratch. And instead of using Claude's
brand guidelines, we're going to add our
own brand guidelines over here. So
firstly make sure that the skill is
already installed and activated. And now
I'm just going to go and write a simple
prompt. Okay, so here's my prompt. I
want to use {forward slash} brand
guidelines, which is the brand
guidelines skill, and create a new skill
by duplicating it. This new skill must
follow my brand colors and typography
that I've uploaded instead of
Anthropic's. Create a new skill based on
brand guidelines skill and call it brand
book. This is uh want to call this new
skill as brand book instead of brand
guidelines and give me an option to save
this skill. So, here I've basically
uploaded my brand guidelines. This is
just a random brand book that I actually
generated using ChatGPT, but you would
obviously use your own brand guidelines
over here. And let's actually press
enter.
All right. So, that modification has
basically been done and this is what the
new skill document actually looks like.
Now, I basically just asked Claude in
order to give me a button to save this
skill so that every time I press forward
slash it actually comes as a part of my
skills. All I need to do is I just need
to save this.
Now, the next time I actually open a new
chat,
I can see this new skill called brand
book, which is just the skill that I had
modified right now. Now, what I'm going
to do is I'm going to ask Claude in
order to make that same PPT that I did
using that research paper earlier. So,
I'm just going to upload that research
paper.
And I'm just going to write the same
prompt, which is make a deck to help me
understand this
better.
All right. And the deck is ready and
here it is. Look at that. Just for
contrast, let me show you what the
previous deck actually looked like. So,
this is with Claude's brand guidelines
and this is with my new brand
guidelines. Do you see that?
All the colors, all of it just with a
new skill. So, now every time I want to
use my brand guideline for anything, be
it a deck, be it uh a PDF, be it an
image or whatever it is, all I need to
do is I need to press forward slash and
brand book or whatever I want to call
that skill. Ultimately, what we did here
was use the base skill and modify it
according to our specific needs. But,
the next level is about using plugins
and partner skills, which open up a
whole new range of possibilities. So,
let's go to level three. In the same
window here, when you click on customize
and browse, if you just click on
plugins, you will see a wide range of
domains like marketing, productivity,
sales, data, blah blah blah. Each of
these options basically pack tons of
skills that are relevant to that
particular domain. So, everything that
you see over here is a collection of
skills in that particular domain. So,
let's for example go to marketing, okay?
Now, here in marketing you can see that
there are eight skills. There's a brand
review skill, there's a campaign plan
skill, there's a competitive brief
skill. Whenever you hover over each and
every one of it, you'll actually see
So, if I'm hovering over content
creation, I will basically see draft
marketing content across channels, blog
posts, social media, email newsletters,
landing pages, press release, blah blah
blah, make it SEO optimized, give
headline options and call to actions.
Right? And if I click on it, I'll
basically see the entire skill file. So,
I can get a much more detailed
understanding of what is exactly in the
skill file. Now, based on what I do at
work, I can basically choose to install
whatever I actually want from here. If
I'm in finance, I can just install this
entire finance package and I'll get that
entire finance package as a part of my
plugins. So, for example, if I wanted to
install this finance package, I just
click on this button. And next time when
I go to chat and I press forward slash,
I can just scroll,
and I can see all my finance related
skills in one place. It also nicely
segregates them. So, depending on what
line of work you're in, Claude also
gives you a collection of skills for
your particular domain. And now, because
you have already learned the level two,
which is modifying these skills, you can
modify it according to your own needs.
Now, if I were to go to one of the
domains, let's say marketing again, you
will see this thing below called as
connectors. Now, this is what is super
special about using Claude skills at
level three. So, everything that you see
in connectors over here is basically a
tool that you might use at work. Like
for example, in the marketing domain,
the connectors are Slack, Canva, Figma,
HubSpot, Amplitude, Notion, Ahrefs,
Clavio, Supermetrics, etc. These are
basically tools that a lot of marketers
use on a day-to-day basis. If I were to
go to, let's say, sales,
I might see Slack, HubSpot, Close,
Monday. You can see a lot of CRMs over
here. You can see Notion, which is for
organization. You can see Fireflies,
which is a meeting note-taker app. You
can see a lot of tools that a lot of
sales people use in their everyday
lives. Now, what are these connectors
exactly and how exactly do they relate
to skills? A very simple way you can
visualize what connectors are is imagine
Claude as the brain. Okay, the brain
does all the thinking. The brain does
all the decision-making. Now, connectors
are basically hands and legs. Brain
can't do much by itself unless it has
access to hands, legs, eyes, because
hands and legs are the things in our
bodies that actually do actions. So, the
brain, which is Claude, gets connection
to Slack, HubSpot, your everyday tools,
so that it can actually perform
real-world actions for you. This is what
the entire Agentic framework is
basically based on, and this is the
superpower that actually Claude offers
everyone. So, right now, I'm here in the
sales domain, and you can use all these
sales skills that you actually see over
here on all these tools. So, you can do
account research on, let's say, HubSpot.
You can do call summary on, let's say,
monday.com. So, the next level of using
Claude's skills is to basically connect
to the existing apps that you use every
day in your work and use skills in
parallel to them. Now, if I go to
plugins and click on partners over here,
you will see names of some of the tools
that you will use every day. These are
basically skills written by these
companies in order to help you use their
tools and capabilities in the best
possible way through Claude. Like, for
example, you can see Slack over here.
All these skills are basically written
by Slack for Claude, so that Claude can
actually use Slack in the best way
possible. Let me show you an example
over here. We are basically going to use
a partner skill that is written by
Canva. Now, Canva is something that a
lot of amateur designers actually use if
you want to get a quick design done. So,
I'm first actually going to install the
partner skill of Canva. I'm going to
click on browse over here. I'm going to
go to plugins. I'll click on partners
and I will type Canva. Now, all I need
to do is I need to click on this plus
symbol. I'm going to add that to my
skill repository. And just to see what
all skills Canva actually has provided
for Claude, there are six skills in
specific. There's a brand check skill,
there's an implement feedback, there's
design feedback, edit design, resize for
social media and bulk create. Let's
actually try attempting the resize for
social media. But before we actually use
this Canva skill, we actually need to
connect our Claude account to our Canva
account. And the way you actually do
that is by clicking this tab over here
that says connectors. I'm going to go on
connectors and I will just click on this
plus icon. Now, when I do that, it
should redirect me directly to Canva.
Now, basically, I will just need to
follow the steps over here. I'll need to
log in to my Canva account, authorize
Claude to be able to use Canva, and then
finally, I should be done. So, we've
done two things over here. We've
connected our Claude account to our
Canva account and we have installed the
Canva skill repository in the plugins
tab. So, let me actually just type my
prompt. I'm first going to upload my
picture over here. This is basically a
landscape picture, which is 16 by 9. And
I'm going to select the skill that I
want and I'm going to type convert this
image into 1 is to 1, 9 is to 16, 3 is
to 2, and 4 is to 3, and give me the
outputs over here.
And did you see that? We have all the
four outputs over here in all the four
aspect ratios that we actually asked.
All of it right inside Claude. We didn't
have to go to Canva, we didn't have to
do anything. And this is just one very
tiny example of how you can actually use
third-party applications like Canva
within Claude itself. Now, there's a lot
more that you can actually do, but I'm
going to leave that up to you. Now, onto
the last level, which is creating your
own custom skill. Now, this is something
that I use quite a lot. I use this more
than anything else, actually. You can
see a lot of my custom skills over here.
Like, if I just press forward slash, all
the first skills that you see over here
are all custom skills that I have
designed or my team has designed
internally for company work. The easiest
way to do this is to enter forward slash
and type skill creator. Claude literally
has a skill whose only job is to help
you create a skill. Once you click on
this, you just need to follow the
instructions on screen. But, for the
best outputs, make sure that you're
giving your instructions as clearly as
you can. Now, I'm going to create a
custom skill just to show you what the
best practices are for you to follow so
that you can do the same things while
you're creating your custom skill as
well. So, let's actually create a skill
that writes Instagram reel scripts
exactly like me for the 100X Engineers
page in my tonality, in my style. For
this, I have a document file where I
have more than 100 scripts I have
written for this page, which I will be
using as reference material in order to
create this custom skill. Let's get
started. So, I'm going to click on
enter.
All right. So, I'm creating a new skill
from
scratch.
All right. So, here is where you
describe your task. I am going to
describe my task with incredible amount
of detail. Just watch me write this
prompt. So, here's the prompt. This
skill should output a 60-second long
Instagram reel script for the 100X
Engineers page. The script always starts
with a catchy hook, which goes for about
two to three lines at max, lasting 10 to
15 seconds. Look at the level of detail
I'm going just for a 60-second long
Instagram script. Then comes the body,
where I explain the content of the video
in easy-to-understand language. And
finally, comes the call to action, which
is always follow 100X for more. I've
also uploaded a doc containing plenty of
scripts that I've manually written so
that you can copy my tonality and
diction. These scripts are for Instagram
specifically, and feel free to ask me
any more questions. Now, I know there's
a lot of grammatical errors over here,
but just ignore that. Claude just auto
corrects for it.
But, towards the end, I very
deliberately asked Claude to ask me more
questions in case it actually needs more
information. So, here, the output is
just like a 150-word long thing. The
main instruction that I've given Claude
is the distinction between the hook,
body, and call to action. But, even
better than that is the document that I
actually uploaded. The more reference
documents you have for these LLMs,
regardless of whether it is Claude, GPT,
or whatever it is, the better output it
actually gives you. This is true whether
you're making a skill or if you're just
normally prompting it. If you have
reference material, always, always use
it. Remember this tip. Now, let's answer
Claude's questions. What will you
typically give Claude as input to
generate a script? I'm basically going
to give it a raw article. Should the
output include anything besides the
spoken script? Example, visual, B-rolls,
notes on screen use. No, I it should
just be the script.
Do you want test cases set up to verify
the skill works well? Yes. This is very
important. Whenever you design a skill,
you want to see the output and you want
to get into a feedback loop with Claude.
So, you want to give it a task, you want
to see how well it does, you want to
give it feedback so that the skill
actually understands what is the best
kind of output that you actually want.
Now, if you give it references, it'll
give you outputs much closer to what you
actually want. But, sometimes when you
don't have references, you have to train
it. So, at this level of skill making,
the more context you have, the more
detail you go into, but the better your
outputs are actually going to be. That
is the key of unlocking level four of
writing Claude skills.
All right. So, here, Claude has given me
three test outputs. Okay, the first one
is basically something about SeaDance.
So, let's just check it out. This is
SeaDance 2.5, ByteDance's brand new AI
video model, and it's going after
Hollywood and every ad agency on the
planet. That's a pretty decent hook.
Native 4K 30-second clips and something
no other AI video tool has done yet.
That kind of summarizes all the features
of the model as well. Pretty nice and
the call to action is also pretty
accurate. For more AI stuff, follow
100X. And it has given us a bunch of
other tests as well in different
formats. So now I'm just going to answer
these questions and give it feedback. So
the first question is does the voice
diction feel right or too generic in
places? I would say the hook is
sometimes
too generic.
It's not
catchy enough
consistently.
Otherwise, it's fine. Right, let's
answer question two.
Test three's handling of uncertain tool
name. Good instinct or should the skill
push you for the real name instead of
writing around it? It should push me
for
the real name
instead of
beating around the bush. So you see how
this is a back-and-forth process where
I'm just giving it feedback and then
it's going to give me more outputs and
then finally I'll get exactly what I
want.
All right, so now that I've given it
feedback saying that the hooks are
actually not nice, it has basically
given me three test hooks. So now I have
to give feedback on this. Now I can keep
going on and on about this until I get
the exact output I want, but for now for
the sake of this video, I'm just going
to say these are good, package the
skill. And now I'm saying this for the
thousandth time, but the key over here
is to really work with the model until
you get exactly what you want, giving it
feedback again and again. All right, so
we have the skill over here. This is
what it actually looks like. You can
actually read the entire document. You
can make changes to it, whatever it is.
And finally, if you want to save this so
that you get it in your forward slashes,
just click on this button over here
and this skill is saved. So the next
time I actually want to write reels for
my Instagram scripts, I can just type
reel script writer, which is basically
what the skill is called. And I can give
it a topic, I can give it an article,
and it is basically going to give me the
script. So, let's actually just give it
a random article from the internet,
okay? This is a news article that I
found. This is not something that we
would usually cover on our page, but
just for the sake of showing you an
example, let's actually try this out.
So, you can see that here I wrote
absolutely no prompt. All I did was I
invoked the skill and I typed the link
of the article that I actually want
reference. I didn't even say write me a
script. That's how easy these skills
are.
And we have a script over here. This is
Johnny Gannon, a career CIA operative
who spent two decades pulling spy
families out of the most dangerous
regimes in the Middle East. That's a
pretty damn good hook. Nice. This is a
pretty decent script. We have the call
to action. We have everything in like
very, very easy, simple to understand
language as well. Quick diversion, if
you love watching tutorials like this
and want to go deeper and unlock some
crazy abilities using Claude and Applied
AI for your professional business, we
run a 6-month Applied AI cohort roughly
twice a year. Back when we started this
program in 2023, we were the first in
the world to offer a 6-month in-depth
Applied AI program. And we're proudly
still the most up-to-date curriculum in
the world because we update our
curriculum every 2 weeks. We cover
topics like Claude code, agentic
frameworks, full-stack web coding, UGC
ad creation, avatars, and much more
across three modules: advanced visual
gen AI, LLMs, and agents. And most of
our students, roughly 70% of them, have
at least 8+ years of experience. So,
it's one of the most elite and premium
communities that you get to become a
part of. Here's just some of our alumni
for your reference. If you are
interested or want to know more about
this program, you can sign up for the
waitlist on our website. I've linked it
below in the description. Let's now talk
about the pro secret that's going to
help you write your skills five times
better than most people out there. So,
before we wrap up, I want to show you
something that almost nobody on YouTube
is showing. You know those default
skills that we used in level one, the
ones that we used to create PPTs and
Word docs? Have you ever wondered what's
actually written inside them? Like what
does Anthropic's own skill file actually
look like? Here's a secret. Those files
are sitting inside Claude's sandbox
right now and you can actually read
them. All you need to do is type this
prompt which says run this in bash and
show me the output and it has certain
file directories over here. If you know
CLI, you would understand exactly what
I'm typing but if you don't understand
CLI, just copy and paste this.
So this is what the output looks like.
This is basically a list of files in
Claude's own directory. Now you can
actually open these files and read
Claude's own skills and see how they are
actually writing these skills so that
you can write your skills five times
better. Let's actually open one of these
files and see. So in order to open one
of these files, you just need to copy
and paste this prompt. So when you want
to open a particular kind of folder, all
you need to do is mention that
particular folder over here. So here I'm
trying to open the PPTX folder. If you
want to open the front-end design
folder, you just have to change that to
or that to front-end over here.
So I'm just going to click on this and
let's see what the file actually has.
And this is what that file contains.
Just look at the level of detail. This
is the exact instruction manual Claude
reads every time it makes a deck for
you. And I want you to notice three
things over here. The first thing is
look how detailed the description is. It
lists every single trigger word, deck
slides, presentation.pptx.
This is why their skills always trigger
and yours might not in certain
scenarios. The second thing is most of
the file is warnings about what not to
do. Great skills document the mistakes
and not just the steps. And the third
one is these are not just instructions.
There are actual Python scripts inside
and that's the ceiling you're aiming
for. So the next time you're writing
your own skill and you're wondering am I
doing this right? I would ask you don't
guess. Just open Anthropic's own files
and copy their pattern. This is one way
where you're literally learning from the
source. Now, you obviously can't get to
this level of skill writing in like a
day or even a week or maybe even a
month, which is why the best way to get
started is from level one. Start with
level one, code a level two, code a
level three, code a level four, and then
aspire to write skills just [music] like
Anthropic does. So, that's the complete
journey from using default skills to
modifying them to partner skills and
plugins to building your own and finally
reading Anthropic's own skill files like
a pro. And here's my honest advice.
Don't try to do all of this today. Just
do level one today. Make one deck with
[music] the PPTX file. And then
tomorrow, modify one of your skill for
your brand. Skills are learned by reps,
not by actually watching [music]
videos. So, if this video helped you
understand learn Claude skills better,
hit that subscribe button, and I'll see
you in the next one.
