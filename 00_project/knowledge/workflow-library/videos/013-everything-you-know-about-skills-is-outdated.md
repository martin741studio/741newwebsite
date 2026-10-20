# Everything You Know About Skills IS OUTDATED

- Channel: Simon Scrapes
- URL: https://www.youtube.com/watch?v=e7TY56-yIvM
- Published: 2026-10-01
- Duration: 12 min
- Views at fetch (2026-10-11): 286,337
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

So, when Claude opens a long reference
file inside one of your skills, it
doesn't always read the whole thing. It
runs a head {dash} 100 command, which
basically reads the first 100 lines only
to work out whether the reference file
is going to add any information that it
actually needs. So, if your important
rules sit after line 100, as far as
Claude's concerned, they actually don't
exist. Now, skills launched early this
year, and we all learned how to build
them properly with good descriptions,
total lines under 200, reference files
separated, and writing them like a set
of instructions. But, the rules have now
completely changed. If your reference
file is over 100 lines and contains no
contents list, then the chances of it
being used are actually low. And
Anthropic's even updated their best
practice guide with six more rules like
this one, and they apply to every skill
you've already built. So, get these
right, and your skills will give you far
more consistent results, whichever model
is running them.
So, number one then is putting a
contents list, like an index, at the top
of any reference file that is over 100
lines, so that Claude can read the whole
file, or literally just jump straight to
the section it needs. So, Anthropic's
own example is an API reference here.
So, contents at the top, then we've got
five different lines. So, we've got
authentication and setup, core methods,
advanced features, error handling
patterns, and code examples. Then, the
sections come underneath it for each of
those sections. So, you can see
authentication and setup here. All
you're going to do is go into Claude
Code or Co-work, which is now actually
merged with chat. So, we've got Claude
Code or Chat, and you're going to go
through every skill in your {dot} Claude
{slash} skills folder. You're going to
find any reference file over 100 lines,
and you're going to add a contents list
at the top that matches its headings.
It's as simple as that.
Now, for number two, this totally
changed the way I think about skills.
So, before, I treated every skill as
having the same level of detail, giving
the same precise instructions where I
could. But, in reality, business
processes aren't as black and white as
that. Anthropic's say the detail in the
skill should depend on how fragile the
task is, and how much it varies. So,
they call this setting appropriate
degrees of freedom, and there are three
different levels to this. So, high
freedom is plain instructions. And their
example is a code review process. So,
it's going to check the structure, look
for bugs, suggest improvements for
readability and maintainability, and
then check it's going to follow the
project conventions. Now, there are lots
of good ways to do a code review, and
the right one depends on the actual
code. So, Claude gets the goal, and is
actually able to work out the rest. The
models are intelligent enough to work
out how to achieve those goals. And if
you're not a coder, you're a business
owner, that might be reviewing a sales
call, or drafting a LinkedIn post. Where
we've got high degrees of freedom. It's
plain text, and the approach can be
ambiguous. So, medium freedom is a
template with different settings in,
basically. So, they've got this template
down here, and we set up the different
settings. So, it can be including charts
true or false, and the format could be
markdown, it could be HTML, it could be
something else. So, it's basically, with
medium freedom, a preferred shape, a
template with some variation allowed, or
some variation is actually fine. So,
that might be a weekly client report,
for example. Versus low degrees of
freedom, where basically operations are
super fragile and error-prone. We need
to be super consistent, and a specific
sequence must be followed. So, think of
low degrees of freedom as an exact
command. So, their example here is a
database migration. And the instruction
here is to run exactly this script.
Don't change the command. Don't add
flags. And for you, that might be
anything touching money, or deleting
things. So, might be raising invoices,
removing members. These are things where
we want it to have strict adherence, and
therefore, we'd give it a specific
script, or few or no parameters where it
can actually vary there. Now, the three
things I actually took from these rules.
First, one skill can actually mix
different levels. So, the writing step
in an invoicing skill can be high
degrees of freedom, while the create the
invoice step might be really locked down
and low degrees of freedom. Second, the
question for each step is what happens
if Claude actually does it differently.
If the answer is nothing much changes,
then we can actually give it higher
degrees of freedom or loosen it. But
actually, if there's something
consequential, then we need to make sure
that we give it low degrees of freedom.
And then the third thing I learned is
that low freedom usually means a script
and not more plain text. With a script,
we're able to ask Claude to do something
the same way every single time. Now, the
third rule change that we're going to go
on to is about different models for
different skills. Now, before we do
that, I just want to give a massive
shout out to you guys and say thank you
so much for helping me hit 100K subs. I
appreciate you, all the time you spend
watching, and your kind comments
massively.
So, number three seems so obvious, but
actually nobody is doing it. So, when
you write and test your skills, you've
likely done it with one model. You've
chosen Sonnet, you've chosen Opus,
you've chosen new Fable models, probably
just using whatever is newest that
month. And I know I'm guilty of doing
this sometimes. But Anthropic say a
skill's result will depend on the model
underneath it, which is quite obvious.
So, you need to test it on every model
you plan to use it with. And then you're
writing your skills based on the amount
of detail that that model requires. And
the right amount of detail has actually
changed a lot. So, around 6 to 8 months
ago, some of the older models would skip
steps. So, we wrote numbered lists and
capital letters emphasizing certain
things like important. Now, it's the
total opposite with some of the newer
higher-end reasoning models. So, the
Fable 5 guide says that skills developed
for older models are often too
prescriptive for it, and they can make
the output worse. And as a result,
Anthropic are telling you to remove
older instructions if the model does
better without them. But when you
consider some of the smaller models,
some of the earlier Sonnet models, they
haven't moved or progressed as far. So,
the best practices page gives you one
question per model. So, when you're
testing these different models, for
Claude Haiku, for example, does the
skill provide enough guidance for Haiku?
For Sonnet, is the skill clear and
efficient? And for Opus, does the skill
avoid over-explaining? So, different
levels of detail required for different
models that they're required to be used
with. So, the skill has to sit somewhere
that works for all three unless you're
going to use it with a very specific
model. And I'd highly recommend running
your most used skill on the same task
with high Q, then with Opus, and then
with Sonnet. And if high Q misses a
step, that step either needs to be
clearer, or it should be a script you
should give it low degree of freedom.
Because a script, remember, runs the
same on every single model. And then if
the same output with Opus does worse
with the skill than without the skill,
then you're going to basically start
cutting instructions from the skill
until Opus is able to perform better.
And also, if you're planning on sharing
these skills, make sure that in that
YAML front matter, that block at the
beginning of a skill, that you actually
write what model these are intended to
be used with. So, onto the next rules,
which are about how the skill is
actually laid out and how it checks its
own work, starting with the nesting of
files, or what you shouldn't do when it
comes to actually nesting reference
files within skills.
So, Anthropic say to keep the body of
the skill.md file under 500 lines and
treat it like the contents page for
everything else. It also advises to
split content into separate files when
approaching this limit. And that's where
nesting comes in, because actually we're
splitting into separate reference files,
we're going to have to point to that
file from the skill.md. And their
example here is a PDF skill. So, the
skill.md has the instructions, and next
to it, there's a forms guide, and
there's a reference guide. This is an
API reference, and this is examples of
how it should fill out forms. And when
Claude is reading through this skill,
it's only going to open the reference
file and the forms file when it needs it
in a step of that skill. So, the actual
skill directory structure might look a
little bit like this. We have the PDF
skill with the skill.md file, a forms.md
file, which is the form filling guide,
the reference, or which is the API
reference, examples, and then a separate
scripts file. Remember, these scripts
are where we have low degrees of
freedom, where we basically need it to
complete this exactly and consistently
as is. And it's important to know when
you're using scripts that scripts
actually get run, they don't get read
into the memory. So, Claude doesn't
actually use up any of its context on
those scripts. Then they proceed to give
some more advice about how you should
set up skills, and they say that when a
skill covers several areas, split those
references by the area. So, their
example is a data skill with separate
files for finance, for sales, for
product and marketing. So, a question
about revenue never loads their
marketing.md file. So, for a client
reporting skill that you might have,
that's one file per client, for example.
Now, onto nested references. So, this is
where that trick from earlier, the
head-100 problem from the start actually
comes in. So, skill.md points to
advance.md, and advance.md points to
details.md, then Claude is more likely
to only preview details.md, so the
actual information at the bottom of the
chain, the details.md, is only going to
get read partially. So, the fix for this
is that every reference file is going to
link directly from the skill.md, just
one level deep. So, they recommend
keeping all references one level deep
from skill.md. So, you're going to open
your skill.md, you're going to list
every file that it points to, and look
for any file that's only reachable
through another file, and you can
actually get Claude to do this, too. And
you're going to make sure that all of
those are linked directly straight from
skill.md. Next, we're going to give
longer processes a proper checklist,
because Claude actually loves that.
So, for these complex jobs, these
complex skills, Anthropic say to break
the work into steps and give Claude a
checklist that it copies into its reply
and ticks off as it goes. So, you can
see here for this research progress,
we've got the five different steps
written down as a checklist. Now, this
does sound like the opposite advice of
the updated prompting advice they've
given to give it the whole job, not the
prescriptive steps, but it actually
isn't. So, steps are for when the order
actually matters, like checking the data
before you build the report on the data.
But, if the order actually doesn't
matter, then we're still going to leave
this checklist out. And their example
doesn't use any code. It's a research
synthesis workflow, and the checklist is
basically five lines, and they're not
super prescriptive. Read all source
documents. Identify key themes. So, it
gives it a goal and still leaves it
ambiguous. Each step is then going to
get a short paragraph underneath it, and
the important one I want to point out is
step five, which is verify citations.
Check that every claim references the
correct source document, and if
citations are incomplete, return to step
three. So, that go back to step three
line is what stops it ticking a failed
step in this checklist and actually
moving on. So, this is self-verification
effectively, and this is part of the
next rule, which is about making sure
our skills have a self-feedback loop to
correct their own courses of action.
So, Anthropic's own pattern on running
skill output validation is to run a
check or set of checks and then fix the
errors, and then repeat those steps
until it passes. They say that this
greatly improves output quality. And the
check itself doesn't have to be code. In
their first example, it's basically a
style guide. Claude is going to draft,
review the draft against the guide, note
each issue with the section it breaks,
revise it, and review it again. So, only
finalizes when everything passes. So,
for you, that style guide might be your
brand voice document that you're
checking and verifying against. And this
is the process under which the skill
starts improving itself.
So, when a draft fails for reason that
isn't in your voice document yet, have
Claude suggest a new rule at the end of
the run. You're going to approve that
rule, and it's going to go into the doc,
and the next run gets checked against
that new rule. And the Fable Five guide
says specifically that the model is good
at updating skills from what it learns
on the task.
Which brings us to the final rule,
building skills with portability in
mind. So, you may be working on your own
now on Claude, but what happens when
your teammate installs the skill that
you use every day? Inevitably, it's
going to break on day one for them. So,
the skill that you built is going to
work on your laptop because you
basically installed it and all the
dependencies, the libraries six months
ago and forgot which dependencies were
in that. But on a teammate's machine or
on a fresh code work session, it's not
going to be there. The dependency is
going to need to be installed. And the
rule is to avoid assuming tools are
installed. So, an example of doing this
badly is actually use the PDF library to
process the file, but instead, what we
would say in every single skill is
something along the lines of install the
required package, and then give it the
package name because if it's already
installed, it will effectively skip that
step. It's intelligent enough to
understand that it is installed and it
will skip that step. So, for every
script in a skill, put the install line
next to that script. So that if you are
sharing skills with your team or selling
your skills, this is going to be a
massive difference between a skill that
works on them on day one and one that
you have to help them set up and
potentially continue to maintain. So,
when we bring that all together, we've
got a ton of new rules. We've got a
contents list on long files over 100
lines. We've got multiple degrees of
freedom that can be used on the same
skill. We've got testing on the model
that you're going to use and documenting
that inside the skill front matter.
We've got references which sit one level
deep only. We've got checklists. We've
got feedback loops and then the
dependencies explicitly spelled out
inside the skills. And you'll probably
have noticed that most of these fixes
weren't about the words inside the
skill, which is why I think it's
becoming more important that the quality
of the skill comes from how its files
are laid out and what checks they run,
far more from how well the instructions
are written, especially as models get
better at interpreting different goals
and creating the instructions for
themselves. So, I've put an audit prompt
in the description for free that checks
a skill against all nine of these and
shows you what it would change before it
changes anything. And then if you stay
on to the next video, I'm going to talk
about Anthropic's prompting updates as
they've drastically changed in the last
6 months and you're going to need to
update all of your skill prompts.
See you in the next one.
