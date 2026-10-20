# Claude Context Engineering Explained: From RAG to Knowledge Graphs

- Channel: Agentic AI Institute
- URL: https://www.youtube.com/watch?v=ckAMHYw8JmE
- Published: 2026-09-09
- Duration: 57 min
- Views at fetch (2026-10-11): 22,709
- Transcript: YouTube auto captions via Apify (johnvc/YoutubeTranscripts). Internal use only. Never name the source in client material.

---

What is context? What's the difference between 
a prompt and a context? How to evaluate your  
context? We'll talk about rag, agentic rag and 
knowledge graphs. Intelligent first. These are  
the models. Then we add our knowledge, our 
company information. Then we add our memory.  
Then we add our tools and skills. And then we 
put our guardrail. So this is how claude builds  
its own system prompt. It loads your clot.md 
your skills.md. Then it takes all your tool  
descriptions. Then it takes if you have ran a tool 
the tool results then it does some eval of its own  
and then it keeps on building it then it stores 
it in the memory file and then it keeps rotating  
until you achieve your goal. What is a ragbased 
system? You create a vector database. What is a  
vector database? A single dimensional matrix is 
called a vector. So this is a vector. The thing  
that stores it is a vector store. So now instead 
of 5,000 pages, I only got 30 pages and I can do  
retrieval. So I did retrieval and I augmented this 
retrieval with my prompt. Hey, what is the payment  
terms? And I only put 30 pages now and I get a 
generated answer. This process is called rag.
Hi Jay. Hi Vance. How are you? Today is all 
about context. So I'm talking to the people who  
have context and people who don't have context in 
life. uh well should have a lot of context of this  
call how this call goes and lot of new people 
may not have the context and that's what the  
difference is that uh he's excited and he knows 
the first 5 minutes he's not that excited because  
I'm going to say the same thing so we're going 
to waste a lot of tokens for him so let's just  
skip through that today no introduction let's get 
to real things okay then what do you think So the  
context I think uh since I'm talking about AI and 
especially like agentic AI or generator generative  
AI context is focus or center for pretty much 
every conversation that I have had in my days  
as well as my interviews that I take or people I 
prepare for it remains such a common or critical  
thing of building agents that's very dear topic 
to me. Uh so today I thought I will just talk  
about context and I will take examples of claude 
how claude builds context then I will show you  
some real case study and problems that when you 
go try to solve for context what do you run into  
and then hopefully give you few suggestions or at 
least touch upon new things that you can apply for  
your improving your context. I may not be able to 
go deep in those techniques today uh just because  
45 minutes are not enough. Uh but give you enough 
links to go do your own discovery and uh happy to  
help and if you're part of our cohort then you 
need not to worry about it because we will be  
spending next week all about context engineering 
and whatever I say will be given to you as labs  
and we'll sit next to you and we'll make it 
happen for you. Okay, having said that, uh what  
is context? Look at that. This class just started 
today. No slides, nothing. Uh just like that, huh?  
Because we want don't want it to uh bore violence 
today. Okay. What is context? Anyone? Welcome if  
you just joined. We're 3 minutes late, so you're 
paying for it. Uh what is context? Uh what's the  
difference between a prompt and a context? Can 
somebody give me that? What is a prompt and what's  
context? Should I give you some some clues, some 
hints or you can just help me here? By the way,  
cameras on everybody cameras on. That's the only 
instruction I have for all of you. Uh only thing  
I need is cameras and rest is all free. Uh but 
uh cameras is something I need because otherwise  
I don't know who I'm talking to and if I don't 
know who I'm talking to I can't help you. Okay  
great. Now we have cameras. Now we know Ankita 
is here. So I need to move fast because Ankita  
will leave otherwise. So see okay prompt versus 
context. What's the difference? Let me just give  
you one. We have this intelligent models and they 
need your knowledge or your company knowledge.  
They need memory on what has happened so far. 
They need to call tools to get things done  
and they might have some test or evals or guard 
rails to ensure that things are done in the best  
possible way. That was the agent or harness. This 
is the harness. Uh so this is the harness. That's  
how you're building agent. And now the prompt for 
you is that hey uh what's a difference between a  
prompt and a context? Is prompt part of context? 
Is it subset? Is it same things? Anyone you can  
raise your hand and start talking maybe. Hey 
Mah, hope you had a good okay somebody said  
message me something but uh that's fine. One 
day I will be able to read all these messages  
and respond and take the class as well. That's 
what you expect. I will I will try that. But  
today what's the prompt? Okay, let's talk about 
prompts. What are prompts? Are prompts context?
Prompt sim.
Yeah, go ahead. Sorry. Prompt describes the 
action that you want to take. Context is the  
baseline information might be specific. I have 
this thing as a user I can send my prompt to it,  
right? which is you say hey explain what is 
neural networks to me and that's your prompt  
explain neural networks and then it goes into 
this system and it has a model so this is the  
model which is let's say opus 5.6 6 or GPT6 that 
came out yesterday. Uh so this is the model and  
there are more things here and is this the only 
prompt or there is another prompt. So this let's  
say this is explain neural networks. We explain 
neural networks. So a lot of people in at least  
our cohort asking this question to GPS these days 
uh because we are talking about intelligence in  
our cohort. We just got started. Our first class 
is tomorrow. But we did a Wednesday class where we  
discussed and the same class happens again on 
Saturday. So we talked about how these models  
are built and all that. So a lot of people are 
asking this question. Explain neural networks.  
That's a prompt. Is that context? Is that one and 
the same thing? Is that context also or not? Um  
so that's not the only prompt. There may also 
be a system prompt. Okay, great. New new thing,  
new thing. So this is the prompt is divided into 
two things. One is user prompt, one is system  
prompt. Yes. Great. So when I created my agent, 
my agent is generic agent. So I created a system  
prompt also in this harness and I told it, hey, 
you are a generic agent or a master agent. Your  
job is to help people. Please make sure this 
doesn't happen. Please make sure this happens.  
use these tools refer memory from here you have 
these data sources to build your context also good  
so that's my system prompt and can we say then 
when I send this prompt to child GPT or claude  
this prompt explain neural network the system 
prompts get added to it so user prompt plus  
system prompt cool is at context. So context is 
the understanding that the um that the model has  
built about you. What it knows about you is like 
sort of a memory that it keeps. So that's yeah so  
new things new things new things. So then you're 
saying hey the user prompt the system prompt the  
system prompt is whatever you explained what who 
you are what you have done in your life or what  
you want this system to behave. If I add the user 
prompt which is explain neural network then I add  
you are a generic this this this you have this 
tool to go search you have this and then there  
is a memory component also that what I have told 
you before is also kept in some kind of file and  
that's added to the context as well. So now it's 
getting beyond just the word prompt. What we are  
saying is context is user prompt plus system 
prompt plus memory memory. Anything else in  
the context I can fill rule results. Great. 
So any data that you can provide the model
user prompt. So user prompt can also have a file 
in it. Let's say I uploaded a contract and the  
contract file is also here. Okay. So that is also 
part of the prompt. Great. We increase this. So  
now it's bigger. Great. So user prompt can have 
instruction which is like hey here is my contract.  
Tell me the risks and I can attach the contract. 
So that is also context. Now my user prompt my  
system prompt which is like you are a lawyer. You 
have access to these tools. You are supposed to  
behave like this. You are not supposed to do this. 
That's also part of context. And then there is  
memory which is previous contracts I have uploaded 
or I have said that only look for indeinity or  
insurance and don't do this and all that and by 
the way my name is this I live in Mountain View  
all this is in memory that is also added to 
the context. Then somebody said tools which  
is interesting. So tools result. So let's say I 
attached a tool called search. Then the results  
of that search based on the user query are also 
added tools results in your context. But before  
I go tools result, is there anything about tools 
I need to add to my context? Uh the list of tools.  
Great. All my tools and the description of those 
tools, right? So tools and their descriptions  
because without that I can't know that I need to 
call search tool or I need to call case text tool  
or I need to call authenticator tool or I need 
to look in a database. What is that? I need to  
put all the descriptions. So all my descriptions 
are also loaded. When say people say tools can I  
also say MCP connectors right? Anything else I'm 
missing? Dynamically loaded skills. Great. Now  
I have this idea of skills also. So if I build a 
harness then I need skills and skills is like kind  
of tool. So what I need what will I load and also 
need scope and data too right? So I will add my  
skill descriptions. I will also add all the skills 
the user has added and their description like I'm  
calling tool. I need to call scripts also. So I 
will add all the descriptions and if there is a  
skill match then I need to get the skills also 
skills outcome. See my context is going above my  
board now. So seems like all of you got it. What 
a context is. And what is the problem with this  
context right? One is it's keep on increasing. 
So it takes up space. It takes up memory and uses  
it takes up memory. It takes up space. Yeah, it 
does take space. It took all my board space. Uh,  
so great. I think scope and boundary is biggest 
thing. So, so is there a is there a limit to it?  
So, let's say this is my harness. This is my 
model and my harness and this is like a model  
provider and model is taking all this context 
from you, right? Let's say opus 5.6. Then can  
I keep sending more and more context? What are 
the what are the challenges? What is the number  
one challenge? The context window, right? Context 
window. Who said that? Five points because I want  
succinct answer these days. I'm only giving 
points if I get answers but succinct answer.  
Context window. Okay. What is the idea of context 
window? I have this context. I can fit it in the  
window. But what is the model and context window 
challenge? 200. By the way, this question is like  
asked in every developer exam for anthropic. It's 
make sure you understand context window. Yeah,  
it's limited. Okay, great. So now I have lot of 
context that I want to send to these models and  
if I send more context I am better or my model or 
my harness behaves better or my harness is good  
but somebody's telling me that there is this idea 
of context window that I can't send all of this  
or there is a limit to what can I send page what 
is that limit for opus 5.6 Six. Anyone change my  
life? 1 million. I don't know to be honest. 
1 million. 1 million. 1 million tokens. That  
means 5,000 or so pages. Great. So I can't say 
send more than 5,000 pages in one request. Any  
other problems of sending more? So one is like 
I can't send there is a limit to it. So we have  
to figure out how to handle it. But any other 
any other challenges of sending more context?
How are how are these model providers charging us
input tokens input input tokens output tokens the 
more context the more input tokens the more you  
pay any other any other challenge so one is the 
limit one is there is a limit one is there is a  
money involved second there is a limit I can't 
send beyond that and third one latency great the  
More context you send, the more time it takes 
to get a response. Okay, that means we have to  
do context engineering. We have to learn how 
to get most of it and without bogging down the  
models but still get the best results. That means 
this is the new engineering practice. Welcome  
to our session on context engineering. after 15 
minutes or so I think we are all on same page that  
uh context what is context and what is context 
engineering let's get started what it takes to  
build context specific agents and do context 
engineering well did I did a good job I did it  
only for valance otherwise I was going and about 
to do my normal intro and all but then I was like  
let's not bore valance with it because he has 
came to all my session and this This is my 195th  
session or so. 196th we are getting into double 
century. I will be remembered as SAG. Huh? Seag  
did the first double century. I think somebody 
else did it before him. Uh I'm just talking  
cricket and it's an Indian cricketer. Let's see. 
I've gone international but Seagar lives with me  
here. Okay. Uh this is my don't worry about me. 
I've done good things in my life. I'm doing good  
things in my life. I'm teaching for a long time. 
That's all this slide says. You already turned on  
your cameras. You keep your questions to yourself. 
I don't take any question. I take questions but I  
take questions after the session not during the 
session. Uh but I would love to stay back and  
take my questions. But I want to finish it in like 
next 45 minutes or so. So keep your questions. I  
will ask you a lot of questions but you can't ask 
me questions for first 30 45 minutes but then you  
can ask me all the questions and I will answer 
them. Uh we talked about context. Then I will  
talk about how to build how claude builds. I will 
show you a live claude doc and show you how claude  
builds this context. How to evaluate your context. 
So okay you're going to add context then you need  
to know how to evaluate that you are sending the 
right context or the model is getting the right  
context. And if you know that you are you are 
not getting or your context is creating lot of  
problems or lot of task in completion in your 
agent then how can you fix them? We will talk  
about rag, agentic rag and knowledge graphs and 
then I will walk you through a case study. I think  
the case study is before knowledge graphs but 
and then I will ask you a lot of questions. Okay,  
I'm also changing the format today. After the 
session I ask you 10 questions okay and then  
you can ask me as many as questions. Okay, I 
will ask questions now. So first I will first  
you can't ask me questions and then I ask you 
questions and then only you can ask me questions.  
See asking questions to Mahes is a big deal now 
huh? Okay, you already understood this intelligent  
first. These are the models. Then we add our 
knowledge, our company information. Then we add  
our memory. Then we add our tools and skills. And 
then we put our guardrails together. That makes  
the harness. Uh that harness in claude world is 
first you get your claude.md file that stores your  
system prompt and your memory. Then you get your 
skills which stores your instructions on top of  
it. So another system prompt. So this is how cloud 
builds its own system prompt. It loads your cloud.  
MD your skills.mmd then it takes all your tool 
descriptions then it takes if you have ran a  
tool the tool results then it does some evals of 
its own and then it keeps on building it then it  
stores it in the memory file and then it keeps 
rotating until you achieve your goal you want to  
see that live okay let me show that live uh many 
things how they build this context okay let's do  
this on board and then I come back uh how plot 
builds its context Three things. By the way,  
this is also one of the questions they ask 
in the exam. Uh we are preparing people for  
developer exams. Mostly PMs who have never coded, 
never seen anything. And in next five weeks they  
will have developer certificate from anthropics. 
Isn't that magical? I think it's possible because  
coding is not that hard anymore. And I think 
anybody who has ever thought about coding should  
start coding at least at skill level or prompt 
level because that's all coding is these days.  
But coming back so um what are the techniques 
that Claude uses to build the context? So you  
go you attach a folder right and then you ask a 
question to Claude. What are the things? Let me  
give you one and then you give me others. Okay. 
uh claude context management. Okay, that's the  
topic. In that topic we are discussing. So first 
it goes and does simple file system search. Cool.  
So it goes and does a grip command and says 
whatever you say neural network then it will  
try to do a grip neural network in your codebase 
or if you ask it to go fix a token based file or  
authentication file it will first find the tokens 
and then go from there. Cool. So it does a file  
system search. Anything else it does? Your turn 
now. Compaction. Compaction comes much later. But  
let's put it here. Five points. Compaction. 
Compaction is this idea that I have lot of  
context. How can I remove reduce it? Before that 
you need to do lot of programming to get to right  
comp right context. Now you get it out of box. 
Cool. Anything else? It does past conversations  
and chats with the user. Great. Uh it loads them 
uh in your system and it loads the memory files,  
the clawed files, the skills files. So that's also 
there. Let's say that's outside the context like  
that's already built. But now it want context 
specific to solve this problem and it's looking  
for this file system to solve that. Can it does 
one more thing? uh it launches these tools and  
builds the context from the tools. anything 
else it does something special that only  
uh uh good people who want to get the certificate 
can tell me it has to do with the problem that I  
have limited context but I can send my problem to 
somebody else who specialized on this sub aent and  
then subent sub aent that's so cool sub agents 
I wanted to give all of you five five points so  
just add to your account whoever said sub agents 
the idea of sub agent is that this claude works  
in your main window. So it's only uh you attach 
a folder, you also select a model. Let's say you  
selected opus 5.6 but opus 5.6 has a 1 million 
context window. So what it can do is it can also  
launch sub agents and then use different model 
let's say sonet model with 256k context and do  
the internet search validations and do all the 
work and eventually just return 100k context and  
spend 256k context here but return only 50k or 
10k worth of information that is needed for me  
to take action. So that's the idea of sub agents. 
Everybody same page. So I can do semantic search.  
I can do file system. I can go and search your 
files. I can launch sub agents to go do job for  
me. And then I can do compaction. So these are the 
main techniques or tricks they use. Uh they also  
have semantic search. What is semantic search? 
Oh my god, look at these folks. Keyword search  
is this one, right? So this one I got similarity 
search based on similarity search semantic search  
meaning what is the semantic meaning similarity 
meaning searches meaning based vectorbased search  
vectorbased search who said vectorbased search 
10 point to you so idea is and same whoever said  
similarity search five point to you also so all 
of you are right vector-based similarity and all  
I will double click on it in a second but before 
I go there let's Look at this in action and I will  
show you how they build the context. They also 
created a video for it and I will show you all  
along that how they are building this context. So 
it's kind of fun for all of you to watch and then  
hopefully it stays in your memory. My goal is 
not to just tell you concepts but kind of hack  
your mind and be there forever. Okay. Uh so the 
idea is this. So this is the page of claude and  
they say this is explore our context window and 
how it works is that first you come in and let  
me just make it big first and then see if I can 
start from the beginning somehow. Drag and drop
shashant is here now this is not working. Okay,
I created my own problems. I am the responsible 
person that I took on this. Okay, great. Uh,  
so this is the context window and it doesn't 
reset. So, let me play it once forever. And  
I can't move it here also. So, I have to 
continue with these guys. Okay. Okay. Great.  
Let's try from the beginning. So what does 
the context of claude has? If you see it here,  
uh what it does is it basically starts with 
zero context. If you look at tokens on top,  
it has no tokens in the build beginning. Then it 
goes and load your system prompt. System prompt  
we discussed which is how you need to behave 
and all that. The makers of claude created  
it. So that's first thing. Then it loads 
your cloud. MD then memory, then skills,  
then MCP, then your rules, then you. So let's 
take an example. So now what you're seeing on  
the top is your tokens increasing. This is the 
limit on the context window and let's say you  
say fix the o bug where user gets 400k error. 
I send that it goes it creates the prompt and  
you can see how much I got. So 45 tokens there. 
But then it reads the files in your codebase and  
that is all getting added to your context and it 
goes and read these files. Then it goes fixes it.  
And eventually you are done and you have consumed 
20,000 tokens. That's your all the context window  
has everything to solve this problem. Here 
you can launch a sub agent and in this one  
you are saying do sub aent research and then 
and now you see that the context is not your  
your only context but now it has gone and sub 
sub aent separate context window. So it loads  
the sub aent system prompt which is a different 
prompt their own clot.md file and then it goes  
and start doing the research on that and once it 
is done it comes back and just give a summary of  
420 tokens back while it has spent 10,000 tokens 
in doing that but this is not counted in your main  
agent token because your main agent only got 420 
tokens back with the summary and then Claude can  
go and send a response and then you can go push 
it. So hopefully this helps you see see through  
like what goes behind the scenes. So these are 
the techniques it goes builds the context and  
then I showed you how it goes and what goes inside 
a cloud context window and how it get build every  
time you're querying it or every time you're 
asking things you are getting charged for not  
only the things that you send but whatever it goes 
through whether it's through sub aents and all but  
it has different techniques to manage and once it 
fills the context window it uses techniques like  
compaction to reduce the size of the window and 
we looked at some other day that 25% of problems  
in agents comes through that compaction process 
because it lose the context that you gave it and  
in complexion it has lost it that's an unsolved 
problem lot of people are trying to solve it it's  
not solved yet same page okay then I think this 
is good enough okay then you created the agents  
you have some kind of rag you created some kind 
of way to get context into them whether you are  
sending context by files and all but how can I 
evaluate my agents Okay, automatically there are  
few agents or few evaluators you can apply them. 
You need to check whether you get all the things  
that you need to answer a question are retrieved 
from your context. So if I touch a folder and if  
I say hey find these things can I check did I 
get all the things that I needed to answer the  
question from this folder. So that is checked 
by the retrieval checks or retrieval quality.  
Then if I get an answer is the answer based on 
the content that was or the context that was  
provided to the model that is the groundedness. 
The model can still hallucinate or make up its  
own answers even if you got all the relevant 
information. The groundedness score checks that  
that whether the answer is grounded in the context 
you provided or whether it made it up. The better  
the groundedness score, better the assurance you 
have that the things are taken from the contract  
that you provided and it did not created its own 
answer just to convince you. So first you need  
to make sure that you can retrieve everything 
you need to retrieve and then groundedness and  
then eventually you can follow up and see what is 
the response of these or responsiveness of this  
agent. Okay. Then you might ask me this is hard. 
So how can I set it up? How can I do this? Uh,  
I'm not going to show you. But in Claude, you know 
how the settings are. But if you want to see this,  
I can show you quickly. That was the plan. But I 
think you all are pros now. So you will laugh at  
me now if I show you basic things. But anyways, 
we do basic things. So this is how you build  
your context. You can come here, you can connect a 
project or a folder. And that's your first context  
building. Second context building is you can go 
and create lot of skills or you can attach lot  
of connectors. So I have connected everything in 
my life to claude and now all these descriptions  
are getting there also when these get called 
the output of these is getting called in this.  
Okay. So I built the agent and I want to now go 
and check how is my agent behaving. For that I  
recommend you these five or six evaluators from 
AI foundry. So AI foundry is a place where you  
go and create these agents. I have done a separate 
session where you can go and create a very simple  
agent in AI foundry but then you can also evaluate 
it. How you evaluate sin foundry? Oh my god messed  
it up. Okay. How you create agents in AI foundry? 
You can just open a. datecom you can create a new  
agent or I can show you an existing agent. So this 
is the agent we created. You select the model you  
provide the instructions you provide what tool 
and what kind of data you wanted to use for its  
own context building. Then you can add different 
knowledge points like you can create different  
knowledge sources your folders and all. Once you 
have created it then what you can do is you can go  
ahead and create evaluation for your agent. So 
when you create evaluation you can select your  
agent whatever is your agent you can go ahead and 
select it for your you can just say hey I want to  
create a new evaluation you can select agent model 
or data set I can say agent and then I can pick  
the agent that I just created then I go to next 
then I go to next frequency one time only you  
can provide your existing data set these are the 
conversation my users are already having with my  
data so I load that It also gives you that you can 
store all your user conversations. So these are  
the conversations we had with this agent and now 
I can use it to evaluate its quality on how good  
it is in managing context. Now you folks tell me 
what should I pick. Okay. Now questions for you.  
So these are out ofbox evaluators and let's say I 
want to evaluate how grounded the agent is on the  
retrieved context from my files. Groundness eval 
yay simple grounded eval groundedness evaluator.  
So I will go and set up groundedness evaluator. I 
can set up which judge model I want to use. I can  
provide it more context. Any other Any other ones? 
Okay, I won't I won't push you here because I have  
not brought you this yet. Retrieval. Retrieval. 
Great. So, I will take on groundedness. I will  
take on retrieval. And I'm going to give you list 
of put no relevance relevance maybe relevance  
is more like the model quality there. But I will 
also check check on tool call accuracy evaluator,  
tool input accur tool output utilization 
evaluator. And I'm going to give you a list  
of 10 that we use the most. Relevance. No, no, no. 
Let me refresh. I just told them to change these.  
Look at that. Never happens. Okay. I will send you 
the list of 10. Once you upload this, you will see  
the 10 evaluator that I picked to checking the 
quality of your context which we have set up for  
these. And once you do that, you will realize that 
your agents are not as good as you want them to be  
or they are not good as you think that they are 
good. Okay, let me walk you through a case study.  
So what happened is we build this uh idea that 
you know models have a problem that they cannot  
process more context because they have a context 
window problem. So if I send a large contract or  
if I send hundreds of contracts with 500 pages 
then I hit the context window of the model same  
page then I can't answer questions on a folder 
which has 10,000 or thousand of my contracts.  
easily a company of my size will have a thousand 
contract in this folder and if I upload all of  
them to my folder it may not answer question 
correctly because it hits the limit of that LLM  
for that either you can use claude claude we use 
the technique that we discussed or you can create  
your own agent and attach rag or build this rag 
based system what is a ragbased system you create  
a vector database what is a vector database it 
basically is a function where you go and take  
a file and first you break the file into smaller 
smaller chunks. This token splitter does that job  
and then you create embeddings for that. What is 
an embedding anyone? I am now going to push you  
all. Sorry. converting words to uh numeric or uh 
usable by vector database. So suddenly suddenly  
you just uh means I want to give you five points 
because it's a very brave answer. It's not that  
easy to just anybody say embedding and you can 
explain it. So we were talking about this semantic  
vector search right all of you pointed to this. 
This is now in action. Okay this is action time.  
What is now I have a large contract with 5,000 
pages and somebody asked a question which is  
5,000 pages of contract and I am I want to give 
the user gave saying hey can you tell me what  
is the payment terms for this contract right and 
it's 5,000 pages and the user is asking what are  
the payment terms in this so this is your model 
right so this is your harness this is your agent  
now your agent can process all the 5,000 and cost 
you a lot of money and have the latency and if  
it hits the limit just fail or hallucinate or you 
can put something like a vector search or semantic  
search in it or similarity search or relevance 
search what is vector search but the idea is  
that you take these 5,000 pages you divide them 
into similar sized chunks you can specify that  
that hey I only want 200 words in it 200 words so 
first you break this down then what you do is You  
take an embedding model which openai gives you, 
enthropy gives you and lot of open source gives  
you. Out of these chunks what you get is a vector 
which represents the meaning of that word into 01  
1 0 2 3 0.2 0.3 and all as something that love can 
be represented by this number. Right? And because  
love is a positive emotion similarly hate can come 
out and have the same representation 01 -12.3 but  
here I can put minus one. So in some kind of orbit 
arbitrary plane these two numbers these two words  
are same or similar but in some they are very 
opposite and this number specify that. So now if  
you look at every plane if I do three-dimensional 
representation of these two words because I can  
because I have them as numbers now then I can go 
and I can see these two are similar but from one  
aspect they're opposite also. So I have encoded 
the meaning of word in numbers and that's the  
beauty of these models which you need not to build 
or study. You just need to give them your chunks  
and they will create the embeddings which stores 
the meaning of these words in numbers somehow. And  
if you can do that then what you can do is then 
you can store all these embeddings in something  
called a vector store which is nothing but a 
database but it stores vectors and a single  
dimensional matrix is called a vector. So this 
is a vector. The thing that stores it is a vector  
store. And now you can go and as the user says 
payment terms, you can convert this payment terms  
into a vector 2 and then find similar vectors and 
then extract those chunks which are similar to it.  
So then you can say give me 30 200 words chunks 
where we discussed the word payment or where we  
see discuss fees or we discuss the word get 
paid how I got I only pass payments how I got  
fees get paid all those also in these chunks 
anyone because maybe they're in the same chunk  
similarity. Great. Because when I went in because 
I did this embedding step now I need not to do  
keyword search I can do a similarity search on 
these vectors and anything that is called payments  
or close by payments will also be retrieved by 
this vector store. So the vector store does not  
only re returns you the keys primary keys or 
some numbers or some exact string match or some  
fuzzy logic. It actually goes and looks for what 
does payment means and then in those planes look  
for something similar to it. And somebody said 
cosine similarity which is these vectors can be  
represented as these lines and then you can say 
hey I can find the delta between these two and  
if they are too close then I can say love and hate 
which will be in some plane like this and most of  
the planes like this I can extract both of them. 
So payment and fees and get paid all these words  
will be similar and that's why you will get all 
the similar chunks out. So now instead of 5,000  
pages I only got 30 pages and I can do retrieval. 
So I did retrieval and I augmented this retrieval  
with my prompt. Hey, what is the payment terms? 
And I only put 30 pages now and I get a generated  
answer. This process is called rag. I talked 
a lot about rag, so I won't go deep into this,  
but I hope you got a gist of it. The gist of it 
is the art of actually taking similar words out  
and then only focusing on the pages that are 
similar rather than putting all the contract  
allows us to go and do it at a at much easier 
way. Here is a lab. In this lab, what we are  
doing is we are first creating this vector 
store and then we are using the vector store  
to get the relevant chunks and then only using 
the those pages that we get to answer questions.  
We give you these labs. We do these labs in our 
course also. So if you have joined our course,  
don't worry about it. If you have not joined our 
course, don't worry about it either. U because  
you can do it on your own or at least you got the 
gist of it. Okay, then this rag thing worked for  
us and we were able to go solve the problem. Now 
we can access pages which are 500 or 5,000 pages  
long contracts. We solved one problem. But then 
what we saw is that hey we got normal things.  
If you ask a question like what is the name of 
borrower in a loan agreement, name of the lender,  
what is the amount of the loan? We were able to 
get all these terms out and answer these questions  
and create a small summary of a loan. The law 
firm's job is take a large 300page loan agreement  
and create a one or two page summary of key 
things in it so that their analyst can put it for  
reporting to IRS. That is the job they were trying 
to do. But then we saw something like then we said  
okay great why don't you buy it? They say, "Mah, 
we looked at this term called interest rate and  
instead of telling interest rate, it's telling me 
the formula on how to calculate it." And I'm like,  
"That's not really good. We did rag and now we 
have a problem." The rag found similarity. It  
looked for interest rate and the model when 
I ask it for interest rate, it's giving me  
interest rate is spread plus benchmark. And now 
the user needs to go look for what is spread,  
what is benchmark and do it manually. While I 
said I automated the process. So what can I do?
And without interest rate I can't sell it. By 
the way, same problem is hit by glean. Same  
problem is hit by Microsoft or Gemini or any 
model or any agent that you're going to build.  
it's going to fail if you're going to do rag on 
it or even agentic rag on it and you have to find  
these techniques and these techniques or these 
solution to these problems is the moat that you  
want in your products. So how we brought this mo 
we looked at this problem and we saw that actually  
calculating interest rate is not as simple as 
just getting the chunks out. First you have to  
figure out what is the formula or in this loan 
agreement what does it mean for interest rate?  
what is the interest rate formula and then we 
calculated it that interest rate can be three  
kinds two kinds mostly it can be just default rate 
which you and me understand everybody understands  
simple or compounding interest so a loan agreement 
can be given to people with 5% interest rate  
straightforward just find what is that and you're 
done or it can be sum of spread plus benchmark but  
if it is benchmark then you it can be liber which 
is London expert London exchange benchmark or  
cipher which is US exchange benchmark then it is 
what is the interest rate today what is the ratio  
or what is the index flow rate of interest today 
in that stock exchange you take that value plus  
you calculate the spread and that's your interest 
rate okay so it can be two kind either sum of  
these two or this but if it is this then you have 
to figure out what is that and you have to figure  
out what is the value of that and if you know 
all this then you can answer the question which  
is what is the interest rate same page so the real 
world or production systems are very complex and  
the question people ask are very complex and 
sometimes yields are multihop problems to find  
interest rate first I have to find out whether 
it is default or benchmark plus spread then if I  
know that I have to find its labor or cipher if I 
know that then I need to find what is the value of  
liber number so far in this contract. Make sense? 
So I have to hop through three things or four  
things to find this information and I need to know 
the relationships between these as well. Okay,  
then how can I solve this? Now my chunks when I go 
ask this question, what is the interest rate? We  
do a lookup and every time what we did is we found 
some of this information, we missed some of this  
information because our chunks were not coming 
out correctly. Even if we increase the number of  
chunks that we could retrieve, we couldn't find 
out how to get this to right answer. Okay. Then  
then what we did then what we did is we said hey 
let's create a knowledge graph. So what we did is  
we created a knowledge graph of how things are 
connected to each other and then we represented  
that as a enriched information that interest rate 
is made up of spread and benchmark or default  
rate. Benchmark can be of these two types. And 
once we have that, then instead of just taking  
the user query and sending it for retrieval, we 
first send it to a knowledger graph database. We  
extract what can interest rate be made up of in 
this contract and it says oh interest rate nearby  
things are spread and benchmark in this contract. 
So our question goes as find the interest rate  
but find interest rate is made up of spread and 
benchmark and benchmark is libar. If you send that  
information then we got the right answer chunks 
out and then we could answer the question. Now  
your question should be why it seems like a very 
involved process. Rag was simple enough. The best  
was just me attaching the folder and let Claude 
figure out what to do with it. That works great.  
If that doesn't work, you can attach a vector, 
you can create a vector database which we show you  
here. Just put your documents attach, pine cone, 
knowledge bases from AWS, Azure all support this  
and then you can create your vector store and then 
you can attach your vector store. Simple enough.  
But now you are talking about creating all 
the relationships and all of this to get to my  
answers which is not going to be easy. Right? So 
you need to understand knowledge graphs and most  
of the companies that are hiring for context these 
days are asking questions around knowledge graphs  
because that's the new differentiation that 
they have created in their context management  
systems. So what is context management? What is a 
knowledge graph? A knowledge graph is explained by  
this dude, but he does a complex job and I want 
to do a simple job, but I'm on time. So, let me  
see what can I do. Okay, let's do a quick tutorial 
on knowledge graphs and then I leave you with few  
resources on how to build your own knowledge 
graphs. Okay, what is the knowledge graph? A  
knowledge graph is a graphical representation of 
information. So instead of just taking entities,  
first step is to create knowledge graph is that 
hey you give me a contract and I out of this I  
extract entity relationship entity triplets. What 
does that means? That means for interest rate
that means interest rate entity is interest rate 
is sum of entity benchmark interest rate is sum  
of benchmark and what was the other thing now I 
forgot benchmark and spread spread okay benchmark  
and spread. So I can say that then I can say 
or is interest rate is made up of. So I have  
the relationship I have the entities and these 
entities can have properties. The properties  
can be benchmarks and then I can figure out how to 
connect them. The process of defining what are the  
entities in your system is also called ontology. 
So there is this idea of defining ontology.  
Ontology is the idea that how to define what 
entities you have, what are their properties and  
what are the relationships that you are looking 
for in this contract. Okay. So before you go and  
create a knowledge graph, you have to define an 
ontology which is hey I have these classes for us  
that could be hey interest lender borrower these 
are my classes. Then you can define the properties  
of these and then you can define the relationships 
also. Once you define these then I can go in this  
contract and I can figure out how what are 
the number of entities I have found in this  
contract. What are the properties I have found 
and what are the relationships. Once you extract  
these triplets, then you can use a n a a graph 
database like Neo4j or Neptune in or graph DB  
in Azure or Neptune in AWS to represent these as 
graphical nodes which are connected to each other.  
Once you have connected to each other or created 
this graph, then you need something called a graph  
query language GQL to take your plain English 
word which is what is interest rate and actually  
give you what are the nodes connected to this 
and give you that interest rate is made up of  
benchmark and spread and default rate as Once 
you get these entities back, you can also send  
a graph query language saying hey here is my node 
give me the first level connections of that node.  
So now I can extract all these words which are 
related to interest rate and that will enhance  
my query. My query was give me interest rate. But 
now if I get all this I can say interest rate is  
made up of spread and benchmark or default rate. 
Spread plus benchmark or default rate. So now at  
least when you go to rag or retrieval you have all 
these words also in your query benchmark spread  
default rate and then it can also go if you take 
two level then it can say benchmark can be liber  
or so for and it has a base rate. So if you take 
two level of nodes then you can find all these  
terms also make sense. Let me show you some things 
that will land. It's not easy to understand all  
this. It's okay. I I take your pain. It took me 
years to kind of do that. But I gave you enough  
resources. So I think that might help. So if you 
look at this uh this year what has happened is I  
was looking for some things that I can show 
you and get you excited about these things.  
So this is the so I was looking so by the 
way if you look at Wikipedia Wikipedia is  
all based on antologies and graphs. So this is 
uh visualizing tool of wiki data which is how  
to visualize data. So this is a knowledge graph 
of ancient intellectual network. So they connect  
everything to chocrats and Pluto is connected to 
it. Pluto is connected to uh Rome Lum and there  
was one more cool guy here but if you go here 
this is a knowledge graph and if you click on it  
these are the connections to it okay so I can see 
Socrates is connected to Plato Plato is connected  
to what Plato is connected to Aristotal okay then 
if anybody talks about Socrates and if I take two  
level connections then I can also see Aristotal in 
my search good and I can go from hair anywhere and  
I can see how they are connected and I can see the 
movement planetism is a philosopher and part of  
this movement that's why how they were connected 
to plate cool and then I can say my full network  
and then I can see all of this network once you 
have defined these ontologies these models can  
create these entity relationship entities for you 
and create this graph then you can pass this graph  
to your agent before you do rag to do an enriched 
queries or enhance your context windows or enhance  
the context that goes to your agent. Even it was 
proven that with knowledge or knowledge graphs the  
context get reduced by 30 to 50%. So it pays for 
itself but there is a cost for it. So please don't  
do it unless you need it in your evaluations. So 
first evaluate make sure you are losing context  
or you're failing on context and if you're failing 
on context then try rag first then try aentic rag  
first and if nothing works then only go into 
the world of ontologies and knowledge graphs  
now you may ask mah it's so hard to create these 
knowledge graphs why are you talking about them  
today I'm talking about it because I'm excited 
about this thing so finally uh Microsoft had  
released Microsoft fabric and IQ where they are 
We will allow you to create these ontologies in a  
much simpler way. We will give you you define what 
the entity is, the properties, the relationships  
and we will make sure that you can create the 
whole ontology. You can enrich your ontologies  
and then once you are done you can also connect 
this ontology to your agents that you are creating  
in foundry. That is the lab we are working on. I 
don't know whether it will land or not but I think  
it's got much simpler than what when I played with 
ontologies and I'm excited about it. By the way,  
they also have introduced graphs. So now you can 
create graphs from your copilot and then connect  
them to your agents. So that's another exciting 
thing that I'm excited about. I will leave you  
with these links to do to do your own discovery. 
I'm working on creating these as labs which we  
will be covering in our course. So if you are 
part of our course, we'll teach you ontologies,  
knowledge graphs and give you some labs on Azure 
AI foundry to go and create your ontologies and  
enhance your agents with knowledge graphs. So 
first we will take your agent we'll show you  
what problems it has with evaluations. Then we 
will do agentic rag solve those and then we will  
still show you these interest rate like problems 
and for that we will create ontologies or graphs  
or both and then we'll show you how connecting 
that ontology or graph solves that problem and  
also gives you better way to explain your answers 
and reduces your context size. That is all I had  
for all of you folks. I talked about how to get 
to context, how clot build context. I walked you  
through how to do evaluations or some standard 
evaluations. I didn't talk about human evals yet,  
but they are also very important. Then I kind 
of tried to give you TLDDR on knowledge graphs.  
So you can go and do your own stuff and I walked 
you through a case study and now I will ask you  
a lot of questions. Here are the resources. Uh 
that's the diagram I was showing. This is agent  
evaluators in Microsoft foundry. This is our labs 
on rag and here is knowledge graph but we will be  
building whole labs on it. So stay tuned. That is 
all I have. Our course starts tomorrow. Everybody  
can get 25% off. This will be the best course of 
your life. I will be the best instructor for your  
life. But if you want to take the course, please 
join. It's this Saturday. Uh the team is here.  
just sended a message and uh we are starting 
tomorrow and it's our first week first class  
and we will be talk about models and next week we 
will talk about these knowledge graphs and how to  
solve that for 3 hours rather than 30 minutes. 
So that's what you get and you get lot of other  
assets like claude certification preparation 
and actually building a real project with PRD  
what to put in evaluation what to put in context 
how to create a road map all that is covered in  
the course so a lot to cover and a lot to build 
with that said thanks a lot for staying back with
