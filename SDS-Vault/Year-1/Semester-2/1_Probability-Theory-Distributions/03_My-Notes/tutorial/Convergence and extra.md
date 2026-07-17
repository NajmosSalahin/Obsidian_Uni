## Page 1

Chapter 5

Convergence

The convergence of sequences of random variables to some limit random variable
is an important concept in probability theory, and its applications to statistics and
stochastic processes. The same concepts are known in more general mathematics as
stochastic convergence. There exist several modes of convergence of random variables,

some of which are described below.

5.1 Convergence in Distribution

With this mode of convergence, we increasingly expect to see the next outcome in
a sequence of random experiments becoming better and better modeled by a given
probability distribution. Convergence in distribution is the weakest form of conver-
gence. However, convergence in distribution is very frequently used in practice; most

often it arises from application of the central limit theorem.

5.1.1 Definition

A sequence of real valued random variables {X,,}, n = 1,2,-+- is said to be converge
in distribution, or converge weakly, or converge in law to a random variable

X if it follows as

lim F),(z) = F(a),

n—0o

for every number x € R at which F is continuous. Here F,, and F are the cumulative

distribution functions of random variables X,, and X, respectively.

79


## Page 2

CHAPTER 5. CONVERGENCE

Convergence in distribution may be denoted as
L, d,
X, > X or X, > X.

5.1.2 Properties
Some of the properties of convergence in distribution are as follow:
1. Let X, 4X and cisa constant, then

(i) X,+ce5Xte, and

(ii) cX, 4 ex.
2. Key 4X and ¥,, 4 c, then

(i) X, +¥%, 5X +e,
(ii) X,Y, 4 eX, and

(iii) 22 4 X (c £0).

5.1.3. Examples

Example 1: Let {X,,} be a sequence of binomial variates having distribution
n n—r
PriXw=r]= ("Ara Pa) 2
r
Let E [X,] =nP,, = be a finite constant, then

-yyr
Pr [X, =r] > es

as n — 00.
Example 2: Let {X,,} be a sequence of t variates having distribution

MX, =) = +, .—+

STAT-2101: Probability Theory 80


## Page 3

CHAPTER 5. CONVERGENCE

then it follows that

1
f(X,=th=— .e 2” asn 00.

Var

5.2 Convergence in Probability

The basic idea behind this type of convergence is that the probability of an “unusual”
outcome becomes smaller and smaller as the sequence progresses. The concept of
convergence in probability is used very often in statistics. For example, an estimator
is called consistent if it converges in probability to the quantity being estimated.
Convergence in probability is also the type of convergence established by the weak
law of large numbers.

5.2.1 Definition

A sequence of random variables {X,},.n = 1,2,:-- is said to be converges in
probability towards the random variable X if for all « > 0

lim Pr (|X, — X| >) =0.
n—-co

Convergence in probability is denoted by adding the letter p over an arrow indicating

convergence, or using the“plim” probability limit operator:
X, 4 X or X, 4 X or plim X, =X.
n—00
5.2.2 Properties
Some of the properties of convergence in probability are as follow:
1X,5X +3X,-x 50.

2. X, 4X, X, 5Y Pr[X =Y]=1.

3. X, 3X, Y, 4 Y, then

STAT-2101: Probability Theory 81


## Page 4

CHAPTER 5. CONVERGENCE

(i) X.Y, 4

X+Y

(ii) X:Y_ 3 XY
(ii) BAF

n

4. Xy 4 X,andk is a constant > kX, ARX.

5X, 5k = X25 Re.

6. Xn 5 a, Yn *b XnYn 5 ab, where a, b are constants.

7. Xp *, X and Y is a random variable > XnY AXY.

8 X,51 3X41.

9. Convergence in probability implies convergence in distribution: X;, ai xXx >
X, 4X.

All the above statement can be easily varified.

5.2.3 Some Examples

Example 1: Let X,, X2,--- be a sequence of independent and identically distributed
random variables with = E (X;) and o? = Var (X;) < co for i= 1,2,+++ ,oo. Then

sample mean X,, converges in probability to pu.

Solution: We have the following
_ _ o?
E (X,) =p and Var (X,.) =—,
n
By Chebyshev’s inequality

Pr (Xn B (Sq), 2) < VO)

for € > 0. Hence

o2

Pr (\Xn =p = a) < ne’

STAT-2101: Probability Theory 82


## Page 5

CHAPTER 5. CONVERGENCE

Taking the limit as n tends to infinity, we get
2

lim Pr (\Xn = p| > €) < lim a

2?
n—+00 noo NE

which yields

lim Pr (\Xn - in| > e) =0.

n-0o

So the sample mean X,, converges in probability to jz, also written as X;, 4 [

Example 2: Let X, ~ Exponential(n), show that X,, 4.0. That is, the sequence

X,, X9,--++ converges in probability to the zero random variable X.

Solution: We have

lim Pr (|X, —0|>e€) = lim Pr(X;, > €)
n—->oco

n—->co

= lim {1 — Pr(X, <.©)]

n=00

= lim [1 _ (d _ e”)]

n+00

lim e¢
noo

= 0, foralle>0.

Hence the sequence of random variables X,, X2,--- convergence in probability to the

zero random variable X.
Example 3: If X ~ Binomial(n,p), then X;, 4 Dp.

Solution: Assignment

Theorem 5.2.1. Convergence in probability implies convergence in distribution. That

can be also written as

X,5X 3X,4X.

STAT-2101: Probability Theory 83


## Page 6

CHAPTER 5. CONVERGENCE

Proof. In order to prove convergence in distribution, one must show that the sequence
of cumulative distribution functions converges to the Fy at every point where F’y is

continuous. Let a be such a point. For every € > 0, we have

Pr(X, <a) < Pr(X < ate) + Pr(|X, — X|>e)

Pr(X <a—e) < Pr(X,, < a) + Pr(|X, — X| >)

So, we have

IA

Pr(X <a-—e)—Pr(|X, — X| >) Pr(X,, < a)

lA

Pr(X <a+e)+Pr(|X,—X|>e).
Taking the limit as n — oo, we obtain:

Fx(a—e) < lim Pr(X, < a) < Fx(a +e),

noo
where Fy = Pr(X < a) is the cumulativedistribution function of X. This function is
continuous at a by assumption, and therefore both Fy(a—e) and Fy(a+e) converge

to Fx(a) as € > 0*. Taking this limit, we obtain

lim Pr(X,, < a) = Pr(X <a),

n—0o

which means that {X,} converges to X in distribution.

5.3 Almost Sure Convergence

This is the type of stochastic convergence that is most similar to pointwise convergence
known from elementary real analysis.
5.3.1 Definition

A sequence of random variables {X,,}, n = 1,2,--- is said to be converges almost

surely (a.s) or almost everywhere or with probability 1 or strongly to another

STAT-2101: Probability Theory 84


## Page 7

CHAPTER 5. CONVERGENCE

random variable X if and only if
or, equivalently,
jim, Pr [fx |X, — X| > ¢| = 0 for every e.

Almost sure convergence is often denoted by adding the letters a.s. over an arrow
indicating convergence: X,, cs X or X, 3 X with probability 1.
5.3.2 Properties
Some of the properties of almose surely are as follow:
1. If X,, “3 X and X,, “3 Y, then X = Y almost surely.
2. If X, 3 X and Y, SY, then aXy+ bY, aX + bY, Va,bER.
3. If X, “3 X and Y, “3 Y, then X,Y, “3 XY.

4. Almost sure convergence implies convergence in probability, and hence implies

Rx ox, 4x.

convergence in distribution: X, “$ X > X,

5. Convergence in probability implies there exists a sub-sequence (k,,) which almost

surely converges: X, > X => X;, “3 X.

5.3.3 Examples

Example 1: Consider an animal of some short-lived species. We record the amount
of food that this animal consumes per day. This sequence of numbers will be unpre-
dictable, but we may be quite certain that one day the number will become zero, and

will stay zero forever after.

Example 2: Consider a man who tosses seven coins every morning. Each afternoon,

he donates one pound to a charity for each head that appeared. The first time the

STAT-2101: Probability Theory 85


## Page 8

CHAPTER 5. CONVERGENCE

result is all tails, however, he will stop permanently.

Let X,,Xo,--- be the daily amounts the charity received from him. We may be

almost sure that one day this amount will be zero, and stay zero forever after that.

Theorem 5.3.1. Convergence almost surely implies convergence in probability. That

can be also written as

X,78X >X,5X.

Proof. We have

|X, —X|>e nen Xn -X|>6
So that
Pr [|Xn — X| > < Pr [2 |Xn —X}> €] -
According to the law of large numbers
Pr [ey [Xn — X| > €] = 0 as n — 0.
Therefore,

Pr [|[Xn — X| > €] + 0 as n— oo.

Hence, X, “3 X => X, 3X.

5.4 Laws of Large Numbers

The law of large numbers (LN) is a theorem that describes the result of performing
the same experiment a large number of times. According to the law, the average of
the results obtained from a large number of trials should be close to the expected

value, and will tend to become closer as more trials are performed.

The LEN is important because it guarantees stable long-term results for the averages

STAT-2101: Probability Theory 86


## Page 9

CHAPTER 5. CONVERGENCE

of some random events.

—— Theoretical mean
—— Observed averages

Average

0 200 400 600 800 1000
Number of trials

Figure 5.1: Average Dice Roll by Number of Rolls.

An illustration of the law of large numbers using a particular run of rolls of a single
dice. As the number of rolls in this run increases, the average of the values of all
the results approaches 3.5. While different runs would show a different shape over a
small number of throws (at the left), over a large number of rolls (to the right) they

would be extremely similar.

Two different versions of the law of large numbers are described below; they are called

the strong law of large numbers, and the weak law of large numbers.

Chebyshev’s Inequality: Let X be a random variable with mean jy and standard

deviation 7. Then Chebyshev’s inequality states that

P(|X — pI) 2 ko) < Or, P(|X — pI) < ko) 21

1 1

for any nonzero positive constant k.

STAT-2101: Probability Theory 87


## Page 10

CHAPTER 5. CONVERGENCE

5.4.1 Weak Law of Large Numbers

The weak law of large numbers (WLLN) states that the sample average converges in

probability towards the expected value

> OP
Xn > fl, when n — oo.

That is, for any positive number e«,

lim Pr( |X, — | >€) =0.

n—0o

Interpreting this result, the weak law states that for any nonzero margin specified,
no matter how small, with a sufficiently large sample there will be a very high prob-
ability that the average of the observations will be close to the expected value; that

is, within the margin.
Necessary and Sufficient Conditions
Necessary and sufficient conditions for the existence of WLLN are
(i) E (X;) exists for all 4,
(ii) B, = Var [X1, Xo,-+- , X;] exists and
(iii) 48 + 0 asn > oo.

Condition (i) is necessary without it the law itself cannot be stated. But the condition

(ii) and (iii) are not necessary, (iii) is however a sufficient condition.

Theorem 5.4.1 (Chebyshev’s Law of Large Numbers). Given X1, X2,--+ an infinite
sequence of i.i.d. random variables with finite expected value E (X;) = up < co Vi, we

are interested in the convergence of the sample average X= 2(Xy +-+-4+X,).

STAT-2101: Probability Theory 88


## Page 11

CHAPTER 5. CONVERGENCE

The weak law of large numbers states:

z= O~P
Xn —> pb when n + o.

Proof. This proof uses the assumption of finite Var(X;) = 0? (for all i). The inde-
pendence of the random variables implies no correlation between them, and we have

that as the following

Var(X,) = Var(2(Xi +--+: + X,))

1
= pe Var(Xi +++ + Xn)

no?”

n2 n°

The common mean sz of the sequence is the mean of the sample average:
E(Xn) =p.

Using Chebyshev’s inequality on X,, restilts in

—_ o?
P([X, — p| Del< -

This may be used to obtain the following:

o2

P(|X, ~ wl] <2) =1—P(X, — yu] 2) >1-

As n approaches infinity, the expression approaches 1. And by definition of conver-
gence in probability, we have obtained

=~ OP.
Xn > pb when n — oo.

Hence the theorem.

5.4.2 Strong Law of Large Numbers

The strong law of large numbers states that the sample average converges almost

surely to the expected value

STAT-2101: Probability Theory 89


## Page 12

CHAPTER 5. CONVERGENCE

xX, > p, when n > oo.

That is,

Pr( lm X, = ) =1

n—-0o

What this means is that the probability that, as the number of trials ”n” goes to in-

finity, the average of the observations converges to the expected value, is equal to one.

Necessary and Sufficient Conditions

Necessary and sufficient conditions for the existence of SLLN are
(i) E (X;) exists for all i, and
8 co 0?
(ii) O72 Ge < 00.

Condition (i) is necessary for the existence of strong law of large numbers and condi-
2
tion (ii) is sufficient. That is convergence of 7°, % is sufficient for the existence of

strong law of large numbers.

Theorem 5.4.2 (Kolmogorov Law of Large Numbers). Let {X;}, 7=1,2,---, bea

sequence of independent random variables such that E (X;) = pu; and Var (X;) = 0?.

Then hold the following

os 2

Set co + Ky — sin 40,
i
i=1
that is, the sequence X,, X2,--- obeys the strong law of large numbers.

Proof. **Assignment

Assignment: Differentiate between WLLN and SLLN.

STAT-2101: Probability Theory 90


## Page 13

CHAPTER 5. CONVERGENCE

Example: Let X; assume two values i and —i with equal probabilities. Show that
the law of large numbers cannot be applied to the independent random variables

‘ ,
X,,X9,--+, Le, Xs.

Solution: We have

1 1
E (Xj) q+ 5! 1) =0, (= 1,2,---,
and
2 PR
Var [X;] = E [X7] aa ?,i=1,2)--
Since X1, Xo,--- ,X, are independent random variables, we can obtain as
B, 1
a = pa eT Xa t MBF + Xn]

= 5 [12 +2 Fan]

— n(n +1)(2n +1)
~ 6n?
n(1+})(2+ 1)
= 7 00 as N —> 00.

Hence law of large numbers does not hold.

Example: Let X; can have two values i* and —i* with equal probabilities. Show
that the law of large numbers can be applied to the independent random variables

X1, Xo,+++, ifa < }.

STAT-2101: Probability Theory 91


## Page 14

CHAPTER 5. CONVERGENCE

Solution: We have

So we can obtain as

1 1
E[Xj] = 3) + g(-*) =0,i1=1,2,---,

and
gay? __jay2
Var [Xj] = B [x2] = CPN pe gia...
2 2
Since X1, X9,--- ,X, are independent random variables, we can obtain as
B,
2 av arl& + Xo +---+X,]

= 3 [120 4 2° 4.0 4+ 79]

=a / xv dx [From Euler-Maclaurin’s Formula]
nm Jo

n
qeotl

n? [2a+1],
2o+1

nr

n2"2a+1
perk

1
aa >Oasn +00 ifa <5.

Hence the results follows law of large numbers.
Example: Let {X,,} be mutually independent and identically distributed random
variables with mean ju and finite variance. If S$, = X, + X9+---+ Xp, prove that

the low of large numbers does not hold for the sequence {5S,,}.

Solution: Since $1, S2,-++ ,S, are mutually independent and identically distributed

STAT-2101: Probability Theory 92


## Page 15

CHAPTER 5. CONVERGENCE

random variables, so

Bn
ne

1

1

= <yVar [Xi + (Xi + Xa) +--+ (Xa + Xa t+ Xa]
1

= Var [nXy + (n-1)X2 +++ + 2Xna +X]

= 2 [n?Var (X1) + (n= 1)?Var (X2) + +++ + 2?Var (X,-1) + Var (X)|

Let Var (X;) = 0? for all i, therefore

2
2s = 2 [P+ Pte +n7]
o’n(n + 1)(2n + 1)
6n?
onl + 2+ a) oo as N > 00
6

Hence law of large numbers does not hold.for the sequence {S',}.

5.5 Central Limit Theorem

The central limit theorem (CLT) establishes that, in some situations, when inde-
pendent random variables are added, their properly normalized sum tends toward
a normal distribution (informally a “bell curve” distribution) even if the original
variables themselves are not normally distributed. The theorem is a key concept in
probability theory because it implies that probabilistic and statistical methods that
work for normal distributions can be applicable to many problems involving other

types of distributions.

For example, suppose that a sample is obtained containing a large number of obser-
vations, each observation being randomly generated in a way that does not depend
on the values of the other observations, and that the arithmetic mean of the ob-
served values is computed. If this procedure is performed many times, the central

limit theorem says that the distribution of the average will be closely approximated

STAT-2101: Probability Theory 93


## Page 16

CHAPTER 5. CONVERGENCE

by a normal distribution. A simple example of this is that if one flips a coin many
times the probability of getting a given number of heads in a series of flips will ap-

proach a normal curve, with mean equal to half the total number of flips in each series.

This theorem was first stated by Laplace in 1812 and a regorous proof under fairly
general conditions was given by Liapounoff in 1901. Below list some particular cases

of this general central limit theorem.
(i) De-Moirve’s Laplace theorem,
(ii) Lindeberge-Levy theorem,

(iii) Liapounov’s theorem, and

(iv) Lindeberg-Feller theorem.

5.5.1 Classical Central Limit Theorem

Let {X1, Xo,--- ,X,} be a random sample of size n, that is, a sequence of independent
and identically distributed random variables drawn from a distribution of expected
value given by jz and finite variance given by o?. Suppose we are interested in the

sample average

of these random variables. By the law of large numbers, the sample averages converge
in probability and almost surely to the expected value js as n + oo. The classical cen-
tral limit theorem describes the size and the distributional form of the stochastic fluc-
tuations around the deterministic number jz during this convergence. More precisely,
it states that as n gets larger, the distribution of the difference between the sample
average S;, and its limit 4, when multiplied by the factor /n (that is /n (Sp — 14)),
approximates the normal distribution with mean 0 and variance o”. For large enough

n, the distribution of S,, is close to the normal distribution with mean jz and variance

STAT-2101: Probability Theory 94


## Page 17

CHAPTER 5. CONVERGENCE

The usefulness of the theorem is that the distribution of /n (S;, — 44) approaches
normality regardless of the shape of the distribution of the individual X;. Formally,

the theorem can be stated as follows:

Theorem 5.5.1 (Lindeberg—Lévy CLT). Suppose {X1, Xo,---} is a sequence of inde-
pendent and identically distributed random variables with E (X;) = ys and Var (X;) =
a? < co. Then as n approaches infinity, the random variables /n(S;, — j2) conver-

gence in distribution to a normal N (0,07):
Vn(Sn— pL) SN (0, a”) .

Proof. The central limit theorem has a simple proof using characteristic function. It

is similar to the proof of the (weak) law of large numbers.

Assume {X,, Xo,--- ,X,,} are independent“and identically distributed random vari-
ables, each with mean jz and finite variance o?. The sum X, + Xj +---+ X, has
mean np and variance no”. Considerthe random variable

Xi t+: +K, —np "Xu “1
Zn = = Yn

No

where in the last step we defined the new random variables Y; = Xi each with zero

mean and unit variance. The characteristic function of Z, is given by

where in the last step we used the fact that all of the Y; are identically distributed.

The characteristic function of Y; is, by Taylor’s theorem,

where o0(t) is little o notation for some function of t that goes to zero more rapidly

than ¢?. By the limit of the exponential function (e* = (1+ £)"), the characteristic

STAT-2101: Probability Theory 95


## Page 18

CHAPTER 5. CONVERGENCE

function of Z,, equals

e ? ” 1p
vz,(t)= (1-57 +0 »e 2 nox.
nr n

All of the higher order terms vanish in the limit n — oo. The right hand side equals

the characteristic function of a standard normal distribution N (0,1), which implies
through Lévy’s continuity theorem that the distribution of Z,, will approach N(0, 1)
as n — oo. Therefore, the sum X; +--+ + X, will approach that of the normal
distribution N (nu,no?), and the sample average

—XitertXn
— n

Sn

converges to the normal distribution, NV (u. =).

STAT-2101: Probability Theory 96
