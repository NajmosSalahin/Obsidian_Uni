---
title: "Lecture 1: Probability and Counting | Statistics 110"
source: "https://www.youtube.com/watch?v=KbB0FjPg0mw&list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo"
author:
  - "[[Harvard University]]"
published: 2013-04-29
created: 2026-05-04
description: "We introduce sample spaces and the naive definition of probability (we'll get to the non-naive definition later). To apply the naive definition, we need to be able to count. So we introduce the multip"
tags:
  - "clippings"
---
< https://www.youtube.com/watch?v=KbB0FjPg0mw >
We introduce sample spaces and the naive definition of probability (we'll get to the non-naive definition later). To apply the naive definition, we need to be able to count. So we introduce the multiplication rule, binomial coefficients, and the sampling table (for sampling with/without replacement when order does/doesn't matter).

## Transcript

### Strategic Practice

**0:00** · SPEAKER: And the reason I call it strategic practice is kind of that-- they're going to be grouped by theme, like these are problems that help me practice this topic, these are problems that help you practice that topic and so on.

**0:11** · But just like, you know, as I said, I'm a chess player and my favorite chess tactics book, they'll start out with like a chapter on pins and then chapter on forks and chapter on skewers, or you're just practicing individual chess tactics, and then towards the end, you get the chapters that mix everything together and you don't know there's going to be a fork or a pin or a skewer.

**0:30** · Well, you know, like on an exam, I'm not going to tell you whether it's a fork or a pin or a skewer, but, you know, by doing a lot of problems, you're going to be improving your pattern recognition skills.

**0:42** · So a lot of this course is about pattern recognition and that just takes practice, right?

**0:46** · You have to practice as much as you can, so the more practice problems you do, the better, right?

**0:51** · I'm not trying to torture anyone with a lot of problems, but as I said last time, this is a difficult course and the best way to learn it is just by my doing a lot of problems.

### Homework

**1:03** · So anyway, those are there.

**1:04** · That also serves-- if you look at the solutions to these strategic practice problems-- then also, you could think of that as kind of an example of what ideally I would like to see on the homework.

**1:16** · So when you're writing up your homeworks, what I don't want to see is like the kind of thing I see sometimes, like, you know, you have like x plus 3 equals 4, and then you kind of decide to subtract 3 from both sides-- minus 3 equals 1, and then I need to square it for some reason.

**1:35** · A 1 squared is still 1, so that's OK, then it adds 7 equals 8.

**1:39** · Put a box around it, then that's the answer.

**1:42** · That's what you should not do.

**1:46** · What you should do is actually have words and sentences.

**1:54** · Just because this is a mathematical class, doesn't mean you shouldn't be using English and explaining things as well as equations.

### Clarity

**2:04** · So I'd like you to be as clear and detailed as possible in just fully justifying your answers, right?

**2:10** · Like, if the answer is 42, well, the TF knows that the answer is 42.

**2:16** · The question is, you know, what reasoning led you to think that?

**2:21** · So clarity is a good word.

**2:26** · And I'd even say honesty.

**2:31** · I hate it when students kind of like have a very, shall we say, sloppy argument that, I think the answer should work out to 12, and so they're just like, you know, put in some stuff somewhere and write it in a very messy way and come up with 12-- put a box around it.

**2:47** · That's very bad.

**2:49** · So if you don't understand something, then I'd much rather that you-- well of course, try to talk to people and figure it out, but I'd rather say you don't understand that than try to make something up like random gibberish.

**3:06** · I always think of it as like, you know, if I were considering hiring you to build a bridge for me, and I'm thinking of three possibilities, like either-- if you just tell me, here's the specifications, you do this, this, and this, I'm not going to have much confidence if you just say that that's the answer, right?

**3:25** · I'm not going to have blind faith in-- even if you've successfully built bridges before, I want to see why this is going to work.

**3:32** · And on the other hand, if you tell me a bridge design and it collapses, do you think I'd prefer that?

**3:39** · Or would I prefer if you tell me, you don't know how to build the bridge?

**3:42** · Well, if you tell me you don't know how to build the bridge, then I would much rather have that happen.

**3:47** · So clarity, honesty, and words.

**3:52** · You may be used in other math classes or just write, oh, the derivative of x squared is 2x, and maybe you don't need to write any words, but I like to see words, justifications, and thinking, not just equations.

**4:04** · OK?

**4:05** · So that's the style of the homework and, you know, you can look-- as I said, you can look at the strategic practice for some examples of what that should look like.

### Homeworks

**4:14** · Doesn't mean we're going to be grading based on your grammar and spelling and things like that, and it doesn't mean you have to write a great American novel, but it should it should be something that you could actually take your homework-- you should be able to actually read it out loud and it would actually sound like English with some equations thrown in.

**4:33** · But even equations, you can read out the equations.

**4:35** · In principle, you should be able to do that, that's what it should look like.

**4:38** · Whereas if you did this, then you just can't read that.

**4:42** · OK?

**4:42** · So homework's due in a week.

**4:44** · What else?

**4:45** · The review.

**4:47** · So math review handout.

**4:48** · I posted before, but I've made a few updates to it, so you can download a new copy of the math review and hopefully most of that material is review, but you should definitely take a look at everything in there.

**5:00** · And then today at 2:00-- review sessions are Fridays at 2:00 in Hall E.

**5:13** · Usually these Friday review sections we'll just be reviewing the week's worth of material, but today's one, which Bowe is going to do, is going to be a math review, so kind of dovetailing the math review handout.

**5:26** · So again, I mean, that's completely optional, but some of you may be rusty on your math and may find that useful.

**5:32** · It's supposed to be videotaped.

**5:34** · I have no control over when the video is posted, things like that.

**5:37** · Usually they're posted fairly soon, but that's not up to me, but anyway, that will be available.

**5:45** · OK.

**5:46** · Any questions by the way on anything about the course that we didn't get to yet?

**5:51** · Before we actually start?

**5:56** · OK.

**5:57** · Any other announcements?

**5:58** · Math reviews, strategic practice, OK.

**6:01** · Oh, and I also want to mention that-- so the homework's due at the beginning of class and there's really no leeway with late homework, because first of all, it's such a large core; secondly, I'm going to post the solutions to the homework very soon after you turn them in.

**6:17** · But I do drop the two lowest homework scores, so if it's late, it would just become one of your dropped two.

**6:27** · OK.

**6:28** · All right, so last time I was kind of quickly mentioning some of the areas where probability is used.

**6:36** · I wanted to just very briefly continue my little list, and then we'll start with the naive definition of probability, which was kind of the historical roots of the subject, but we'll quickly want to move beyond the naive stage.

**6:51** · OK?

**6:54** · But just to continue my little list a little bit.

**6:58** · So last time, I just mentioned very briefly in physics, quantum mechanics, it's all probability; genetics, you can't do genetics without probability; and some of the sciences-- econ, econometrics, and game theory, and so on.

**7:14** · But I want to mention a few of the less obvious applications, like history.

**7:22** · Well, you might think, what does history and probability have to do with each other?

**7:27** · I just want to mention very quickly one example of a really famous beautiful example that Mosteller-- you can look up details if you want you online-- Mosteller-Wallace did some beautiful work studying The Federalist Papers.

**7:48** · They were trying to resolve-- so The Federalist Papers were crucial documents in the history of the US, you know, having to do with the ratification of the US Constitution.

**7:58** · And there's a lot of disagreement over the authorship-- you know, who wrote some of them, so that's an important historical question, and so they were using probability, Bayes' rule, think things we're going to be doing to address that.

**8:11** · And Mosteller was actually the founder of the staff department in here, and he's actually my grand advisor-- so my advisor's adviser, so I like to talk about Mosteller.

**8:20** · I didn't get to meet him.

**8:22** · Actually, he died in 2006 and I came here in 2006 so I just missed him.

### Passfail

**8:26** · But anyway.

**8:26** · You know, it is used in history, and I wanted to mention-- when I mentioned history, it reminds me that I was also going to say something about pass/fail.

**8:36** · So if anyone wants to take the course pass/fail, I do allow it.

**8:41** · The reason is for flexibility, is because I trust you to decide what's best for you.

**8:46** · Obviously you have to-- if you're counting this for concentration credit, you'll have to check with your concentration advisor about whether that be OK.

**8:53** · It's OK with me.

**8:54** · I don't usually recommend it, but I've have had some cases before of students who were really afraid to take the course because they didn't know if they had enough math and they did pass/fail, and the story that this reminds me of here is one-- I had a history concentrator a few years ago.

### Applications

**9:14** · He had almost no math background, just basic calculus-- like 1B, so he was scared to take this, but he was interested in learning it.

**9:22** · So I let him take a pass/fail and he really loved it, and after that, every single elective he took for the rest of his time here was a stat course-- he stayed a history concentrator but did lots of statistics electives.

**9:33** · And now he's doing a PhD at Stanford in applying statistics to political science and history, so there are examples like that.

**9:43** · So there are more and more applications in history and government also.

**9:47** · You can check out IQSS at Harvard-- Institute for Quantitative Social Science.

**9:51** · Just take a look at their web page-- if you have any interest in social science and government, look at the IQSS stuff.

**9:56** · There there's a huge amount of activity there that's at the intersection of statistics, political science, history, government-- all come together.

**10:07** · There are a lot of applications-- an increasing number of applications in social sciences and even the humanities.

**10:15** · Last time I mentioned finance very quickly, and I wanted to especially recommend STAT 123, which is not offered this year, but it will be offered next year and probably the following year-- the prerequisite is STAT 110 and it's a very interesting course for many reasons, but-- I won't talk about it more now, but it is worth-- if you're interested in finance, then you should definitely be interested in this.

**10:42** · If you're not interested in finance, then don't worry about it.

**10:46** · All right.

**10:47** · And then one more is gambling.

**10:52** · And depending on how cynical you are, you could say that I've just repeated myself, but gambling is fun to talk about.

**11:03** · Gambling is sort of-- it's illegal in a lot of-- most forms of gambling are illegal in most parts of the US and has kind of an unsavory reputation.

**11:16** · And I never know if anyone has some strong moral objections to gambling is going to be offended if I talk about gambling.

**11:22** · It hasn't happened yet, but let me know if you're offended and I'll try to be more careful about it.

**11:29** · But anyway, gambling-- I feel justified in talking about gambling in STAT 110 because gambling is where probability came from-- that the historical roots of the subject are exactly in games of chance-- gambling.

**11:45** · And so it gives me a chance to talk about a little bit of the history.

**11:49** · It's also some familiar concrete example, like dice and cards and coins and things like that that people gamble with.

**11:59** · As I mentioned, the math prerequisite before, I didn't mention the cards prerequisite.

**12:04** · You should know what a 52 deck of cards, you know, like the-- you should know what-- basically what a standard deck of cards looks like.

**12:12** · So if you've never played-- you don't actually have to know how to play poker in this class, but you should be familiar with a deck of cards.

**12:18** · But you can easily learn that if you haven't played any card games before.

**12:24** · So this is historically well-motivated.

**12:28** · And it's also just a source of interesting examples that we can easily explain without getting into a lot of technicalities, and then we can learn things.

**12:36** · So there are some early examples, I'm just going to mention our Fermat and Pascal in the mid- 1650s.

**12:49** · And there are other examples as well, but this is arguably the most important kind of historical root of probability.

**12:56** · So Fermat, you've probably heard of Fermat's Last Theorem.

**12:59** · He was a famous mathematician and also a lawyer on this-- actually, he was a lawyer and a mathematician on the side, not the other way around.

**13:08** · Pascal was another very, very famous guy.

**13:11** · You know, Pascal's Wager, Pascal's.

**13:13** · Triangle, Pascal-- it was a programming language before C and so on.

**13:18** · Very, very famous person.

### Fairmont Pascal

**13:20** · So anyway, you know, they didn't have email back then obviously, so they were writing very long letters back and forth to each other.

**13:26** · And most of the letters have survived, you can actually find them online if you just look up, you know, Fermat Pascal correspondence.

**13:33** · It's pretty interesting to read their letters back and forth, and they were just writing letters back and forth to each other analyzing different gambling games, and it's like, if you have this gambling game, what's the probability that this will happen?

**13:44** · What's the probably that will happen?

**13:45** · And it was all completely new at the time.

**13:47** · You know, no one had mathematically derived these rules and how to work with probability, so they were just developing it just by writing letters back and forth discussing gambling.

**13:58** · OK?

**13:59** · So we will discuss some of those games that they talked about when we get to it.

**14:07** · And then I mentioned life at the end last time.

**14:10** · I'll come back to that.

**14:12** · Life.

**14:13** · I like to say statistics is the logic of uncertainty.

**14:22** · Math is the logic of certainty, statistics is the logic of uncertainty.

**14:27** · Everyone has uncertainty.

**14:29** · If you're 100% certain of everything, then there's something wrong with you.

**14:34** · Everyone has a lot of uncertainties and probability and statistics are how we quantify and update our beliefs and deal with uncertainty.

**14:46** · So that's what this course is going to be about.

**14:48** · It's going to be about quantifying uncertainty.

**14:53** · All right?

**14:53** · So now we can get to the naive definition of probability, which was the origins of the subject.

**15:05** · So let me tell you what a sample space is first, then I'll give you the naive definition.

**15:12** · So a sample space-- sample space just means the set of all possible outcomes of some experiment.

### Sample Space

**15:25** · And we're going to talk about experiments a lot in this class, but you should interpret the word experiment in an extremely broad manner.

**15:34** · An experiment can be just anything, right?

**15:37** · Do anything-- as long as there are certain possible outcomes.

**15:40** · So before the experiment, you don't know what's going to happen, because there are different possible outcomes and you don't know which one's going to happen.

**15:47** · You do the experiment and then something happens.

**15:49** · OK?

**15:50** · So what I just said was very, very general, right?

**15:52** · And I mean, that could describe any number of situations.

**15:56** · So a sample space is the set of all possible outcomes of an experiment.

**16:04** · And we can interpret experiment however we want.

**16:07** · So this is a very general concept.

**16:14** · All Possible outcomes of an experiment-- and we might say it's a random experiment, but I'm not going to use the word random right now because we haven't defined it.

**16:22** · I'm just interpreting this very, very generally.

**16:26** · OK.

**16:27** · And then we need one more concept, which is that of an event, and we'll come back to this, but the earlier you start thinking about events, the better.

**16:38** · An event is a subset of the sample space.

**16:49** · And by the way, there's also like a one-page handout that's on the course web page called Probability and Sets or something like that.

**16:57** · One of the big breakthroughs in probability that made it possible to actually treat this as a mathematical subject instead of just something more like astrology was the idea of using sets, OK?

**17:12** · So most of you have seen like unions and intersections and things like that, but if you don't know much, you know, like basic facts about set theory like that, I put a short introduction into the review handout, but you definitely need to be comfortable with unions, intersections, and complements in this course That was a huge breakthrough, because before, people just kind of tried to like solve probability problems by just kind of writing down some stuff that sounded intuitive, or reasoning by analogy and various heuristics Most of those heuristics unfortunately turned out to be completely wrong.

### Isaac Newton

**17:47** · And we'll talk about some of those famously wrong heuristics later.

**17:54** · But even-- I should mention Isaac Newton.

**17:58** · Sort of later than this-- roughly around the same time-- Isaac Newton also-- you know, Newton is one of the most famous and probably top three most famous mathematician physicists of all time, and there were gamblers who were asking Newton gambling questions as well.

**18:17** · Because at the time, no one knew how to do probabilities, so if you were like a degenerate gambler and you really needed to know the odds, then you had to go to someone of the stature of Isaac Newton, Fermat, or Pascal to get an answer.

**18:33** · You know, that was 300 years ago, and so one of the cool things is that after a few weeks of STAT 110, you'll be able to easily do calculations that 300 years ago, you'd have to consult Isaac Newton with.

**18:44** · And Newton-- we'll talk about some of Newton's stuff probably in the next lecture, but Newton did the calculation correctly, but even Newton's intuition turned out to be wrong for one of these.

**18:56** · It's just a gambling problem about dice.

**18:57** · His intuition was wrong.

**19:00** · So one thing that makes this subject difficult is that we're going to do a lot of things that are deeply, deeply counterintuitive to almost everyone.

**19:09** · And I think that makes this a fun subject.

**19:12** · It's a lot of fun teaching it, there are a lot of paradoxes we'll talk about, a lot of very surprising results.

**19:19** · So to me, that makes this more fun than calculus.

**19:23** · When you take a calculus class, I've never seen anyone shocked by anything.

**19:30** · I mean, the fundamental theorem of calculus, which we will need occasionally, is a very cool result.

**19:35** · It links differential calculus-- so derivatives and integrals are inverse to each other.

**19:41** · I mean, it's pretty cool, but it doesn't amaze anyone, It's not that counterintuitive.

**19:47** · Statistics is full of counterintuitive stuff, which just means you have to work hard, you have to think hard, and it will become more intuitive the more you think about it, the more problems you solve, OK?

**19:56** · But at first, a lot of this might seem counterintuitive, even to Isaac Newton.

**20:03** · So that's why we need to be more mathematically precise about it, because our intuitions can easily be completely wrong in probability, so that's why we need to make it more mathematical.

**20:13** · And then as I said, the breakthrough, mathematically-speaking, was to start thinking of events as subsets, OK?

**20:21** · So I'm going to draw a lot of Venn diagrams in this class.

**20:25** · Usually I'll call the sample space capital S. And that-- it's just a set.

**20:30** · The elements of the set are possible outcomes of the experiment, OK?

**20:34** · So if our experiment is to roll two dice, OK?

**20:41** · Six-sided dice, then there are 36 possible outcomes-- we'll actually get to where the 36 comes from in a bit.

**20:48** · There's 36 possible outcomes, and then this set would consist of all those outcomes, and then an event, let's call it A, is just some subset.

**20:57** · OK.

**20:58** · And so there are a lot of-- we'll get into this more later, but you should also look at the handout later about probability and sets, where we-- the purpose is to connect intuitive ideas about events and make that mathematically precise using unions and intersections and things like that.

**21:16** · OK?

**21:17** · So we'll get into that more later, but I just wanted to get this word out there to help us now with the naive definition of probability.

**21:33** · You could also call it the very naive definition of probability.

**21:36** · So you can only use this definition when you have strong justification for doing so.

**21:44** · The definition just says that the probability of an event A-- so this is our first use of a letter, capital P. Throughout this course, capital P means probability, so we write P of A, where A is an event.

**22:01** · So I'm imagining we have some experiment that we're considering, we have this sample space, we have a subset we're interested in-- A-- because we want to know what's the chance, what are the odds that some particular event will occur?

**22:15** · That's the question we're going to be considering throughout this course, OK?

**22:19** · So we want P of A.

**22:22** · How do we get that?

**22:23** · Well, that's a hard question, that's what this entire course is about.

**22:26** · But the naive definition would be to just say, that's just number of possible outcomes in the denominator, and then the number of favorable outcomes-- and by favorable, I mean favorable to A-- divided by a number of possible outcomes.

**22:51** · So the denominator is just the size of the sample space, it's the number of possible outcomes.

**22:56** · And the numerator is just how many of those outcomes did A occur?

**23:01** · OK?

**23:02** · So for example, if we flip a coin-- flip coin twice, there are four possible outcomes, right?

**23:18** · Either the coin lands heads on the first toss and heads on the second toss, or heads and then tails, or tails and then heads, or tails and then tails.

**23:27** · So we have these four different outcomes, OK?

**23:31** · Now suppose we want to know, what's the probability that both tosses are tails?

**23:39** · Then according to this, it would be one quarter, right?

**23:41** · Because we have one-- this would be the favorable outcome, there are four of them, 1/4, that's it.

**23:46** · So that's sort of like the high school definition of probability as well, to just count how many possibilities there are, how many of them did the thing you want happen, and that's it.

### Is a coin fair

**23:57** · But notice, though, I didn't say anything about, is it a fair coin?

**24:00** · Is it, you know-- and well, that's the question, is what does it actually mean for a coin to be fair?

**24:06** · I mean, we have to be careful of some circularity here.

**24:10** · So if we say a coin is fair, we mean heads and tails are equally likely, OK?

**24:15** · But even then, that's just talking about one toss, and if we have two tosses, well, what if the coin has some kind of sticky property that it lands tails and it's likely to land tails again the next time?

**24:25** · There are all kinds of different possibilities that we'll consider.

**24:28** · But the most naive way to write this down would be, OK, we have these four cases.

**24:31** · If we treat them all as equally likely, then if we want the probability of some event, we just count how many of those happen, divide by a number of things, that's it.

**24:40** · That's the naive definition.

**24:43** · So it has a huge assumption.

**24:48** · It assumes that all outcomes are equally likely.

**24:57** · And it also assumes that there are finitely many outcomes.

**25:02** · I'll have to say finite sample space.

**25:08** · So if the outcome of your experiment could be like any real number or any integer, then the denominator would be infinity and then this is meaningless, OK?

**25:17** · So it has to be-- in order to apply, it has to be that we have a finite denominator.

**25:24** · And the assumption is that everything is equally likely, well, that's a very, very strong assumption, OK?

**25:29** · Now that's a reasonable assumption in some problems where we have some kind of symmetry, right?

**25:36** · Like if we roll a six-sided die and we think, you know, if all six sides are equally likely just because it's a symmetrical cube, then maybe it's reasonable to say each one is 1/6, 1/6, 1/6, right?

**25:49** · But it could just as easily be a loaded die that's weighted towards one side more than another and then, you know.

### Life on Neptune

**25:57** · So taken to an extreme, this kind of led to a dead end at some point and got kind of ridiculed.

**26:03** · Like, if you take this to an extreme, you could say, well, what if I want to know what's the probability that there is life on Neptune, OK?

**26:15** · Well, I've never been there.

**26:16** · I don't know if there is life on Neptune or not, so either there is or there isn't, that's two possibilities.

**26:23** · One of them has life, the other one doesn't, so it'd be 1/2, OK?

**26:28** · So most people would agree, that's a ridiculous argument.

**26:31** · Despite that, you can find many examples in the media, in the news-- there's a Daily Show clip I really like kind of making fun of this, I'll post the link at some point.

**26:42** · And I've seen various examples where people are taking seriously arguments of that form, or they're using the naive definition with no justification.

**26:51** · There's no justification for using the naive definition in that case, right?

**26:55** · And the situation gets even worse.

**26:57** · I just said, well, according to this, the probability of life on Neptune is 1/2.

**27:01** · Now what if I asked you instead, what's the probability that there's intelligent life on Neptune?

**27:08** · Well, again, either there is or there isn't, so that would also be 1/2.

**27:13** · But there's something that seems-- something's severely wrong with-- you know, shouldn't it be strictly less likely that there's intelligent life than that there's any kind of life?

**27:22** · Or there should be a strict inequality there, OK?

**27:27** · And that's not reflected.

**27:28** · So we'll quickly need to go beyond this.

**27:31** · However, as I said, this is where the subject got its start-- and for gambling, so it's still important.

**27:37** · It's important both to understand how the subject evolved, but it's also important for a lot of problems where we are able to assume equally likely.

**27:46** · I'm just emphasizing the fact that you need some justification or be very clear about what you're able to assume.

**27:54** · And if you are able to assume that all the outcomes are equally likely and there's finitely many, then this is the definition of probability, it's perfectly good, otherwise you can't.

**28:03** · OK?

### Counting

**28:05** · So in order to be able to actually-- I mean, I did a very, very simple example here, I just wrote down the four outcomes and we did it, but for anything that's more difficult than that, it would become too tedious to list everything out.

**28:20** · So therefore, the first major topic in this class is, how do we count?

**28:26** · OK?

**28:27** · So I said that calculus is a prerequisite.

**28:30** · Counting is not really a prerequisite, so we're going to start-- I'm trying to make this as self-contained as possible, we start with counting.

**28:39** · So some basic principles of counting.

**28:51** · Because if we don't know how to count, then we would never be able to compute the numerator and denominator there, right?

**28:57** · All right.

**28:58** · So there are a couple of principles that we need.

**29:00** · First one, I don't really know if it has a standard name, but I just call it the multiplication rule.

**29:11** · And it says-- it's a pretty simple principle, but it underlies most of what we'll need for counting, except for one other counting method that we'll get to next time.

**29:28** · Multiplication rule says that if we have an experiment-- again, I'm going to say this kind of abstractly because this is a general principle, and then we'll see examples of how to use this.

**29:44** · So if we have an experiment with, let's say, n1 possible outcomes, OK?

**29:55** · So we do some experiment and there are n sub 1 possible outcomes.

**30:01** · And then we do a second experiment such that for each outcome of the first experiment, then there are n2 possible outcomes for the second experiment.

**30:18** · I'll just abbreviate experiment to expt.

**30:22** · There are n2 possible outcomes for the second experiment-- that should be n2 here-- for a second experiment, et cetera, do as many experiments as you want.

**30:36** · So I'll just put dot-dot-dot.

**30:38** · Let's say we're going to do r experiments, and there are n sub r-- and so for each-- no matter what happened with the previous r minus 1 experiments, there n sub r possible outcomes for the rth experiment.

**30:56** · OK.

**30:57** · Almost done stating this.

**30:59** · There are n sub r outcomes possible for the rth experiment.

**31:09** · Then the conclusion-- so we sort of have all these separate experiments that we're doing sequentially one after the other, OK?

**31:17** · Then overall, there are n1 times n2 times blah blah blah times nr overall possible outcomes for the combined experiment.

**31:29** · The combined experiment consists of doing all these smaller experiments one after the other.

**31:35** · Overall possible experiment outcomes.

**31:43** · Formally, you can prove this using induction, but I would prefer that you understand why this is true just by thinking about it, thinking about examples, OK?

**31:56** · And the way I like to visualize it is just by drawing a simple tree diagram.

**32:03** · So I promised someone while were waiting outside that I'd mentioned ice cream today.

**32:08** · I like to talk about ice cream examples with counting for reasons that I might mention.

**32:14** · Ice cream example-- this is a very, very simple example, but once you understand this example completely, then all this stuff I wrote here becomes obvious.

**32:25** · Simple experiment, you go and get ice cream and suppose you have different options.

**32:33** · Suppose just for simplicity that there are only three flavors-- chocolate, vanilla, and strawberry-- and suppose that there are two different types of cone.

**32:43** · And so you go in, you choose which type of cone you want and which type of flavor you want, that's it.

**32:49** · OK?

**32:49** · That's the experiment.

**32:50** · So that experiment consists of two parts, right?

**32:52** · The first experiment is you choose which type of cone you want and on the second experiment is you choose which flavor you want, right?

**32:59** · So very, very simple.

**33:01** · So I would just depict it like this, where let's say at the first branch, you choose either C for a cake cone or a W for a waffle cone, and then once you've chosen which type of cone you want, then you can either choose chocolate, vanilla, or strawberry-- CVS.

**33:20** · Was not a sponsor today, but maybe it'll get sponsorship later.

**33:24** · Chocolate, vanilla, strawberry, there we go-- that's the tree diagram.

**33:28** · Once you understand this tree, all this abstract stuff should become obvious.

**33:33** · How many possibilities are there?

**33:34** · Well obviously there's 6.

**33:35** · 1, 2, 3, 4, 5, 6.

**33:38** · Why is it 6?

**33:38** · 6 equals 2 times 3.

**33:43** · Now notice also that 6 equals 3 times 2.

**33:47** · We could have-- they're not going to force you to first choose a cone and then choose the flavor.

**33:52** · You could choose the flavor first and then choose the cone and they should be able to handle that, right?

**33:57** · So you can draw that tree for yourself, it could have split three ways and then two ways, there's still six outcomes.

**34:02** · That is all this is saying, right?

**34:04** · So you can imagine a massive tree where it branches many times, millions of branches, but if you understand this simple little tree, then you'll see where that's coming from.

**34:17** · OK?

**34:18** · So you all know about exponential growth.

**34:23** · 6 is still a pretty small number, but if you imagine that there are many branches and each time it keeps branching different ways, if you multiply 2 times 2 times 2 many times, it's going to grow exponentially fast, like 2 to the 10th power is 1,024.

**34:37** · So if we had 10 choices and each choice we can only choose between two things, there's still over 1,000 possibilities.

**34:42** · So these grow very, very, very fast, and that's why it's hopeless to try to just list them out except for the very simplest problem.

**34:52** · OK, so that's the multiplication rule.

**34:55** · Well let's do one quick example.

**34:59** · Find the probability of a full house in poker-- and I'll tell you what that is.

**35:05** · I'm assuming you know what a deck of cards is, but I'm not assuming you know the term full house with a five-card hand.

**35:13** · So a standard deck of cards has 52 cards, and you get five cards.

**35:19** · And we're assuming that the cards are completely shuffled so that all sets of five cards are equally likely, OK?

**35:27** · That's the assumption.

**35:30** · OK.

**35:31** · Then I have to tell you what a full house is.

**35:35** · But if I'm going to use the naive definition of probability, I want to know, what's the number of possible hands?

**35:44** · Well that's 52, choose 5.

**35:46** · I think most of you have seen this, sometimes people write this as like 52C5, you know, combinations and things-- this is a preferable notation.

**35:55** · I'll remind you what it is in case you haven't seen it, but hopefully most of you seen that before.

**36:01** · We'll be seeing a lot of these in this course, those are called a binomial coefficient.

**36:09** · It's pronounced n choose k and written like that.

**36:12** · And it's defined as n factorial over n minus k factorial k factorial.

**36:21** · I'm assuming you've seen factorials before, but if not, you definitely should make sure you know what factorials are.

**36:32** · We'll also define this as 0 if k is greater than n.

**36:39** · What this quantity is supposed to represent is the number of way-- if you have n people, how many ways can you choose k out of the n people, OK?

**36:47** · So choose a subset of size k where order doesn't matter.

**36:51** · So I'll say a number of subsets of size k where order doesn't matter of a group of n people or n objects.

### Choosing

**37:08** · So if k is greater than n, it has to be defined as 0, because you can't choose-- if you have 10 people, you can't choose 11 of them, it's impossible, OK?

**37:17** · So if k is less than or equal to n, it's equal to this, and let me just quickly tell you the reason why.

**37:28** · If we choose-- we know we need to make some choices, right?

**37:33** · This follows almost immediately from the multiplication rule, so I'll just quickly justify this.

**37:40** · Let's choose the first person, OK?

**37:42** · So we have we have n people and we want to select k of them, OK?

**37:46** · Pick the first person.

**37:47** · There are n choices, right?

**37:49** · Because you can pick anyone.

**37:50** · Now, and then the next person could be anyone except the one you already chose, so it's going to be n minus 1.

**37:56** · And then the next one is n minus 2.

**37:58** · And it goes all the way like that until it goes down to n minus k plus 1, because if k is 1, I want to stop at n.

**38:07** · If k is 2, I want to stop at n minus 1.

**38:11** · So that would be the answer if we were picking people in a specific order, OK?

**38:15** · But these k people I just selected, I could have chosen them in any order, right?

**38:21** · So I have to divide this by k factorial because I've over-counted by that factor.

**38:26** · And that's actually the same thing as n factorial over n minus k factorial k factorial, because if you write up these factorials, all of the stuff is going to cancel and this is what's left, right?

**38:40** · If you imagine-- this is n times n minus 1, n minus 2, all the way down to 1; this 1, you know, the same thing, starting at n minus k-- cancel stuff, this is what's left.

**38:48** · OK?

**38:49** · So that's where this thing comes from.

**38:50** · All right.

**38:51** · Now coming back to this full house problem, a full house is defined as having three cards of one rank and two of another.

**39:01** · For example, three 7's and two 10's, OK?

**39:06** · That's called a full house.

**39:09** · So if we use the naive definition, which is justified if we assume that the cards are completely shuffled, the denominator is 52 choose 5, because I'm just choosing 5 cards out of 52 with all possibilities equally likely.

**39:22** · Now let's get the numerator.

**39:24** · For the numerator, so I'll just say-- for a full house then, I'm just going to write as an example, three 7's and two 10's.

**39:34** · It really helps to just have some concrete example in mind, some numbers to think about.

**39:40** · So we want to-- now what's the probability?

**39:42** · Well, first of all, I need to choose-- what do I have three of?

**39:49** · I wrote down 7's here, but that could have been anything, all right?

**39:52** · There are 13 possibilities, or you could say 13 choose 1.

**39:56** · Now I'm multiplying because I'm using the multiplication rule, OK?

**40:00** · So in my mind, I'm imagining-- I'm not going to draw the whole tree because I'd have to draw 13 branches, but I'm imagining that at the first branching, I'm choosing any rank-- ace, 2, 3, 4, whatever.

**40:12** · Now in my mind, I'm imagining I chose 7, so I'm focusing on the 7 branch, and then it's branching further.

**40:18** · I have 13 choices and I have 7's and I need three 7's.

**40:22** · Well, there are four 7's in a deck of cards and I need to choose three out of the four, so I'm going to multiply by 4 choose 3.

**40:30** · Then I need to choose what the other one is, so I wrote 10's here, but it could have been anything.

**40:35** · There's 12 possibilities, because it could be anything except 7's in that case.

**40:39** · And then we need two of those, 4 choose 2.

**40:43** · And that's it.

**40:45** · Now there are other ways to write the answer, OK?

**40:48** · But I recommend thinking about it this way, thinking in terms of the tree.

**40:52** · It's a more structured way to do it, you're less likely to make a mistake.

**40:56** · If you have some other method you like for doing these problems, you can try to do it and then compute and see if it's the same, but it helps to think in terms of the tree-- think in terms of the multiplication rule.

**41:08** · OK.

**41:09** · Well that's the probability of a full house.

**41:15** · So n choose k is what's called a binomial coefficient, but it's also an example of a choice, right?

**41:24** · We're choosing k things out of n where order doesn't matter.

**41:28** · So I want to quickly talk about what happens if the order matters, that kind of thing.

**41:35** · So what we're doing is sampling, so I call this the sampling table.

### Sampling

**41:46** · So it's going to be a 2x2 table, and we'll try to fill it in.

**41:56** · So sampling means we have some population of items or people or anything, and we're drawing a sample.

**42:05** · So we're choosing k objects out of n, and we want to know how many ways are there to do it.

**42:14** · And there are two possibilities.

**42:17** · Either we do it-- I'm going to draw a 2x2 table.

**42:26** · Either we sample with replacement-- replacement means, for example, imagine we were conducting a survey and we pick a person and ask them a bunch of questions and then we kind of put them back.

**42:41** · With replacing, we're allowed to pick the same person again.

**42:44** · Without replacement would mean, then the next person we pick has to be someone different.

**42:48** · So there's two different applications-- sometimes the replacement is relevant and sometimes not replacement, so sampling with or without replacement.

**42:59** · And then the other possibility-- do we care about order or not?

**43:03** · So I'll say order matters or order doesn't matter.

### Order Matters

**43:12** · And they want to fill in this table.

**43:15** · Does everyone understand the setup of the problem?

**43:18** · We have. n objects or n people, we're going to pick k of them.

**43:21** · In this case, this is with replacements, so we pick one, put it back; pick one, put it back, OK?

**43:28** · Until we have k of them.

**43:29** · And order matters, meaning if I pick, you know, Fred and then I pick John, that would count differently from-- as a different possibility of picking John and then Fred, OK?

**43:42** · So in this case, it's immediate-- how many possibilities there are is just n to the k.

**43:47** · I don't need to do any calculation for that, that's just immediate from the multiplication rule.

**43:51** · There's n choices each time, OK?

**43:54** · So that's it.

**43:55** · Now this corner here, that's what we just did.

**44:03** · Pick k people without replacement, order doesn't matter, that's n choose k-- is the number of ways to do that, OK?

**44:09** · Now let's think about this one-- order matters, and we pick without replacement.

**44:15** · Again, it's immediate from the multiplication rule, OK?

**44:18** · So you don't have to memorize it.

**44:20** · I don't want you to memorize this table, I want you to understand, like-- you should understand why this is immediate, this is immediate, this is immediate.

**44:28** · I didn't write it yet, but it's n times n minus 1, blah blah blah, all the way down to n minus k plus 1.

**44:40** · Because there's n choices for the first person, and then since I'm not replacing that person and there's n minus 1 choices and so on, until we get to n minus k plus 1.

**44:50** · Now this is closely connected to this as we just showed on that board.

**44:53** · If you take this thing and divide it by k factorial, you'll get this, OK?

**44:56** · And you should think about why that makes sense.

**44:58** · OK, so these three boxes were all very easy to fill in, right?

**45:05** · So hopefully this one will be easy.

**45:08** · Actually, it's not.

**45:11** · You can try to figure this one out for yourself-- and I think it's good practice to try to think about it, but it's very, very difficult, at least compared to these three, OK?

**45:23** · Order of magnitude more difficult. It turns out that the answer is n plus k minus 1 choose k.

**45:31** · And for practice, you may want to try-- just choose some very small values of n and k and verify that this is correct in a small example.

**45:41** · And if you enjoy, you know, solving these kinds of things, you could think about why this is true.

**45:45** · We'll prove this next time.

**45:47** · So these three should be obvious to you once you understand the multiplication rule.

**45:52** · This one is much more subtle but useful.

**45:55** · So for now, you know, you should know this result, but we'll prove it next time.

**46:02** · So this is basically kind of summarizes most of what we need for counting.

**46:06** · This is all you need for counting-- almost everything for the homework.

**46:11** · And there are-- at this point, you can do most of the homework.

**46:16** · There are a couple of little things we'll get to on Wednesday.

**46:19** · Normally I'll cover everything you need by Monday, but in this case, we have a holiday, so there's a couple of loose ends.

**46:24** · Most of the homework you can do already, so just start already.

**46:27** · OK, so have a good weekend.