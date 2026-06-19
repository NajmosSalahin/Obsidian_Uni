# Srijonshil Answers — Discrete Mathematics

> **Note:** All answers are directly extracted/sourced from the lecture PDFs (Lec_1.pdf, Lec_2.pdf, Sir Notes.pdf).

---

## প্রশ্ন ১: Discrete Mathematics ও Proposition

### ক. Discrete mathematics কী?

Discrete mathematics is a branch of mathematics that deals with mathematical structures and objects that are fundamentally discrete or separate in nature. Discrete mathematics is the part of mathematics devoted to the study of discrete objects. Discrete mathematics is the branch of mathematics dealing with objects that can assume only distinct, separated values. The term "discrete mathematics" is therefore used in contrast with "continuous mathematics," which is the branch of mathematics dealing with objects that can vary smoothly (which includes calculus). Whereas discrete objects can often be characterized by integers, continuous objects require real numbers.

Discrete mathematics or finite mathematics is the branch of mathematics in which the mathematical organizations are fundamentally isolated, that is, the notion of continuity does not apply to them.

*(Source: Lec_1.pdf, pp. 1–2)*

### খ. রহিমের বক্তব্যকে প্রতীকী যুক্তিবিজ্ঞানের ভাষায় প্রকাশ ও সত্যতা সারণি

ধরি,
- p: "আজ বৃষ্টি হবে"
- q: "তাপমাত্রা ৩০° এর নিচে থাকবে"

রহিমের বক্তব্য: "আজ বৃষ্টি হবে **এবং** তাপমাত্রা ৩০° এর নিচে থাকবে।"

প্রতীকী রূপ: **p ∧ q**

A conjunction is a compound statement formed by joining two statements with the connector AND. The conjunction "p and q" is symbolized by p ∧ q. A conjunction is true when both of its combined parts are true; otherwise it is false.

| p | q | p ∧ q |
|---|---|-------|
| T | T |   T   |
| T | F |   F   |
| F | T |   F   |
| F | F |   F   |

*(Source: Lec_1.pdf, pp. 13–14)*

### গ. করিমের বক্তব্যের সত্যতা সারণি ও ধরন নির্ণয়

করিমের বক্তব্য: "যদি তাপমাত্রা ৩০° এর নিচে থাকে তবে বৃষ্টি হবে না।"

প্রতীকী রূপ: **q → ¬p**

এটি একটি **Conditional Statement** (শর্তসাপেক্ষ বক্তব্য)।

The conditional statement p → q is the proposition "if p, then q." The conditional statement p → q is false when p is true and q is false, and true otherwise. In the conditional statement p → q, p is called the hypothesis and q is called the conclusion.

| q | p | ¬p | q → ¬p |
|---|---|----|--------|
| T | T | F  |   F    |
| T | F | T  |   T    |
| F | T | F  |   T    |
| F | F | T  |   T    |

*(Source: Lec_1.pdf, p. 16)*

### ঘ. Tautology ও Contradiction

**Tautology:** A compound statement that is always true regardless of the truth value of the individual statements is defined to be a tautology.

উদাহরণ: p ∨ ¬p — এটি সর্বদা সত্য।

**Contradiction:** A proposition that is false under all circumstances is called Contradiction.

উদাহরণ: p ∧ ¬p — এটি সর্বদা মিথ্যা।

Truth table for contradiction:

| p | ¬p | p ∧ ¬p |
|---|----|--------|
| T | F  |   F    |
| F | T  |   F    |

*(Source: Lec_1.pdf, pp. 17, 19)*

---

## প্রশ্ন ২: Cryptography ও Number Theory

### ক. Cryptography কাকে বলে?

Cryptography is the science of protecting information by transforming it into a secure format so that only authorized parties can read or understand it.

In computer science, cryptography refers to secure information and communication techniques derived from mathematical concepts and a set of rule-based calculations called algorithms, to transform messages in ways that are hard to decipher.

*(Source: Lec_1.pdf, pp. 5–6)*

### খ. Encryption এবং Decryption-এর মধ্যে পার্থক্য

It involves two main processes:

**Encryption:** Converting plain text into unreadable code (cipher text).

**Decryption:** Converting cipher text back into the original plain text.

*(Source: Lec_1.pdf, p. 6)*

### গ. RSA অ্যালগরিদমে Number Theory ও Modular Arithmetic-এর ভূমিকা

Number Theory: Prime numbers and modular arithmetic are used in RSA, Diffie-Hellman, and similar systems. Logic: Boolean operations are used in encryption algorithms. Combinatorics: Used to calculate the number of possible keys and determine password complexity. Graph Theory: Applied in network security and data routing. Probability and Statistics: Required for random number generation and security analysis.

*(Source: Lec_1.pdf, p. 6)*

### ঘ. Discrete Mathematics কীভাবে Cryptography-তে অবদান রাখে

Discrete mathematics is central to cryptography, the science of secure communication. Concepts such as modular arithmetic, number theory, and Boolean algebra are essential in designing and analyzing cryptographic algorithms. Discrete mathematics also helps in understanding and developing protocols for secure data transmission, authentication, and encryption.

Discrete mathematics has wide-ranging applications in computer science, cryptography, information theory, operations research, optimization, and many other fields. It provides the foundation for solving real-world problems using rigorous mathematical techniques and logical reasoning.

*(Source: Lec_1.pdf, pp. 2, 4)*

---

## প্রশ্ন ৩: Function, Predicate ও Quantifier

### ক. Function কাকে বলে?

A function is a special kind of relation between two sets, say A (domain) and B (codomain), such that: Every element of A is related to exactly one element of B. Formally: f : A → B means that for each a ∈ A, there exists a unique b ∈ B such that f(a) = b.

*(Source: Lec_2.pdf, p. 1)*

### খ. উদ্দীপকের ফাংশনটি one-to-one কিনা নির্ণয়

f(x) = 2x + 3, A = {1, 2, 3}, B = {5, 7, 9}

f(1) = 2(1) + 3 = 5
f(2) = 2(2) + 3 = 7
f(3) = 2(3) + 3 = 9

A one-to-one function, also known as an injective function, is a function where distinct inputs always produce distinct outputs. This means no two different inputs map to the same output, ensuring each element in the function's codomain is the image of at most one element from its domain.

এখানে, ভিন্ন ভিন্ন input (1, 2, 3) ভিন্ন ভিন্ন output (5, 7, 9) দিচ্ছে। সুতরাং ফাংশনটি **one-to-one (injective)**।

*(Source: Lec_2.pdf, p. 1)*

### গ. P(x)-এর জন্য ∀ এবং ∃-এর সত্যতা মূল্যায়ন

P(x): x² > 5, A = {1, 2, 3}

- P(1): 1² = 1 > 5 → **False**
- P(2): 2² = 4 > 5 → **False**
- P(3): 3² = 9 > 5 → **True**

**∀x ∈ A, P(x):** "For all x in A, x² > 5" → False (কারণ x = 1 এবং x = 2-এর জন্য সত্য নয়)।

**∃x ∈ A, P(x):** "There exists x in A such that x² > 5" → True (কারণ x = 3-এর জন্য সত্য)।

Universal Quantifier (∀): "For all." Example: ∀x ∈ R, x² ≥ 0
Existential Quantifier (∃): "There exists." Example: ∃x ∈ R, x² = 4

*(Source: Lec_2.pdf, p. 2)*

### ঘ. Injective এবং Surjective Function-এর পার্থক্য

**One-to-one function (Injective):** A one-to-one function, also known as an injective function, is a function where distinct inputs always produce distinct outputs. This means no two different inputs map to the same output, ensuring each element in the function's codomain is the image of at most one element from its domain. You can test if a function is one-to-one graphically by using the horizontal line test, which requires that any horizontal line drawn through the graph intersects it at no more than one point.

**Onto function (Surjective):** An onto function, also known as a surjective function, is a function where every element in its codomain (the set of all possible outputs) is mapped to by at least one element in its domain (the set of all inputs). In simpler terms, the function "covers" its entire codomain.

পার্থক্য:
| Injective (One-to-one) | Surjective (Onto) |
|---|---|
| Distinct inputs → distinct outputs | Every element of codomain is mapped |
| Codomain-এর প্রতিটি element সর্বোচ্চ একবার ম্যাপ হয় | Codomain-এর প্রতিটি element অন্তত একবার ম্যাপ হয় |
| Horizontal line test ব্যবহার করা যায় | Codomain = Range হতে হবে |

*(Source: Lec_2.pdf, pp. 1–2)*

---

## প্রশ্ন ৪: Methods of Proof ও Mathematical Structures

### ক. Theorem এবং Axiom-এর মধ্যে পার্থক্য

**Theorem:** A theorem is a mathematical statement that has been proven to be true using logical reasoning based on axioms, definitions, and previously established theorems.

**Axioms (or Postulates):** Axioms (or postulates) are basic assumptions or self-evident truths accepted without proof, which serve as the foundation for developing a logical system or theory.

সারসংক্ষেপ: Axiom হচ্ছে স্বতঃসিদ্ধ যা প্রমাণ ছাড়াই মেনে নেওয়া হয়, আর Theorem হচ্ছে সেই বিবৃতি যা Axiom-এর ভিত্তিতে প্রমাণ করা হয়।

*(Source: Lec_2.pdf, pp. 4–5)*

### খ. "দুটি জোড় পূর্ণসংখ্যার যোগফল জোড়" — Direct Proof

**Direct Proof:** Where you directly show that the conclusion follows from the premise.

ধরি, a এবং b দুটি জোড় পূর্ণসংখ্যা।

**Step 1:** যেহেতু a জোড়, তাই a = 2k, যেখানে k ∈ Z
**Step 2:** যেহেতু b জোড়, তাই b = 2m, যেখানে m ∈ Z
**Step 3:** a + b = 2k + 2m = 2(k + m)
**Step 4:** 2(k + m) = 2 × একটি পূর্ণসংখ্যা, যা জোড়।

∴ a + b জোড়। (Proved)

*(Source: Lec_2.pdf, p. 3)*

### গ. Proof by Contradiction পদ্ধতিতে প্রমাণ

**Proof by contradiction:** Which assumes the negation of the statement and derives a false outcome.

**Step 1:** ধরি, বিবৃতিটি মিথ্যা — অর্থাৎ, দুটি জোড় পূর্ণসংখ্যার যোগফল জোড় নয় (বিজোড়)।

**Step 2:** ধরি, a = 2k এবং b = 2m (দুটি জোড় সংখ্যা)।

**Step 3:** তাহলে a + b = 2k + 2m = 2(k + m) = 2n, যেখানে n = k + m একটি পূর্ণসংখ্যা।

**Step 4:** 2n আকারের সংখ্যা সর্বদা জোড় হয়।

**Step 5:** কিন্তু আমরা ধরে নিয়েছিলাম a + b জোড় নয় — এটি একটি **contradiction** (বিরোধ)।

∴ আমাদের অনুমান মিথ্যা। সুতরাং, দুটি জোড় পূর্ণসংখ্যার যোগফল জোড়। (Proved)

*(Source: Lec_2.pdf, p. 3)*

### ঘ. Lemma, Corollary এবং Conjecture

**Lemma:** A lemma is a helping theorem — a proven statement used as a stepping stone to prove another, more significant theorem.

উদাহরণ: "Let a and b be even integers. Then a + b is also even." — এটি একটি Lemma হতে পারে যা বড় Theorem প্রমাণে সাহায্য করে।

**Corollary:** A corollary is a statement that follows readily from a theorem that has already been proven. It often appears as a direct consequence.

উদাহরণ: "The sum of two even integers is even." — এটি উপরোক্ত Theorem-এর একটি Corollary।

**Conjecture:** A conjecture is an unproven statement believed to be true based on observations or partial evidence but not yet proven.

উদাহরণ: "Every even number greater than 2 is the sum of two prime numbers." — এটি Goldbach's Conjecture, যা এখনও প্রমাণিত হয়নি।
উদাহরণ: 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5.

*(Source: Lec_2.pdf, pp. 7–9)*

---

## প্রশ্ন ৫: Recurrence Relation — Distinct Roots ও Application

### ক. Recurrence Relation কাকে বলে?

A recurrence relation for the sequence {aₙ} is an equation that expresses aₙ in terms of one or more of the previous terms of the sequence, namely a₀, a₁, a₂, …, aₙ₋₁ for all integer n with n ≥ n₀, where n₀ is a non-negative integer.

Example: aₙ = aₙ₋₁ − aₙ₋₂. The order of this equation is n − (n − 2) = 2.

*(Source: Sir Notes.pdf, p. 1)*

### খ. ব্যাংকের টাকার পরিমাণের জন্য Recurrence Relation

Let Pₙ be the amount in account after n years.

Recurrence relation:
Pₙ = Pₙ₋₁ + 0.05(Pₙ₋₁)
⇒ Pₙ = Pₙ₋₁(1 + 0.05)
⇒ Pₙ = (1.05)Pₙ₋₁

Initial deposit, P₀ = 10,000 Tk.

P₁ = (1.05)P₀ = (1.05) × 10,000
P₂ = (1.05)P₁ = (1.05)² × 10,000
...
P₃₀ = (1.05)³⁰ × 10,000 Tk.

∴ P₃₀ = (1.05)³⁰ × 10,000 Tk.

*(Source: Sir Notes.pdf, pp. 4–5)*

### গ. aₙ = aₙ₋₁ + 2aₙ₋₂ সমাধান

Given recurrence: aₙ = aₙ₋₁ + 2aₙ₋₂, with a₀ = 2, a₁ = 7.

Let aₙ = rⁿ be a solution.

rⁿ = rⁿ⁻¹ + 2rⁿ⁻²

Dividing both sides by rⁿ⁻²:
r² = r + 2
⇒ r² − r − 2 = 0
⇒ r² − 2r + r − 2 = 0
⇒ r(r − 2) + (r − 2) = 0
⇒ (r + 1)(r − 2) = 0
∴ r = 2, −1

Roots are real and distinct.

The general solution is:
aₙ = α₁(2)ⁿ + α₂(−1)ⁿ

When n = 0:
a₀ = α₁ + α₂ = 2 ⇒ α₁ + α₂ = 2 … (3)

When n = 1:
a₁ = 2α₁ − α₂ = 7 … (4)

Solving (3) and (4):
α₁ = 3, α₂ = −1

∴ aₙ = 3·2ⁿ − (−1)ⁿ

which is the solution of the given recurrence relation.

*(Source: Sir Notes.pdf, pp. 5–7)*

### ঘ. Characteristic Equation, Characteristic Roots ও Fibonacci Explicit Formula

**Characteristic Equation:** When solving recurrence relations, we try to find solutions of the form aₙ = rⁿ, where r is a constant.

If aₙ = rⁿ is a solution of aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + … + cₖaₙ₋ₖ, then:

rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻² + … + cₖrⁿ⁻ᵏ

Divide by rⁿ⁻ᵏ and subtract:
rᵏ − c₁rᵏ⁻¹ − c₂rᵏ⁻² − … − cₖ₋₁r − cₖ = 0

This is called the **characteristic equation** of the recurrence relation. The solutions of this equation are called the **characteristic roots**.

**Fibonacci Sequence Explicit Formula:**
fₙ = fₙ₋₁ + fₙ₋₂, f₀ = 0, f₁ = 1

Characteristic equation: r² − r − 1 = 0
r = (1 ± √5)/2

So r₁ = (1 + √5)/2, r₂ = (1 − √5)/2

General solution: fₙ = α₁r₁ⁿ + α₂r₂ⁿ

Using f₀ = 0, f₁ = 1:
α₁ = 1/√5, α₂ = −1/√5

∴ fₙ = (1/√5)[(1 + √5)/2]ⁿ − (1/√5)[(1 − √5)/2]ⁿ

which is the explicit formula for the Fibonacci sequence.

*(Source: Sir Notes.pdf, pp. 2, 11–12)*

---

## প্রশ্ন ৬: Recurrence Relation — Repeated Roots ও Multiple Roots

### ক. Linear Homogeneous Recurrence Relation কাকে বলে?

Linear homogeneous recurrence relations of degree two have the form:
aₙ = c₁aₙ₋₁ + c₂aₙ₋₂

where c₁ and c₂ are real numbers. It is called "linear" because each term is linear, "homogeneous" because there is no constant term, and "degree two" because aₙ depends on two previous terms.

*(Source: Sir Notes.pdf, pp. 2–3)*

### খ. প্রথম Sequence সমাধান (Repeated Roots)

aₙ = −6aₙ₋₁ − 9aₙ₋₂, with a₀ = −6, a₁ = 3.

Let aₙ = rⁿ be a solution.

rⁿ = −6rⁿ⁻¹ − 9rⁿ⁻²

Dividing both sides by rⁿ⁻²:
r² = −6r − 9
⇒ r² + 6r + 9 = 0
⇒ (r + 3)² = 0
⇒ (r + 3)(r + 3) = 0
∴ r = −3, −3

The roots are real and equal.

The general solution for repeated roots is:
aₙ = α₁r₁ⁿ + nα₂r₂ⁿ

When n = 0:
a₀ = α₁ + 0 = −6 ⇒ α₁ = −6

When n = 1:
a₁ = α₁r₁ + α₂r₂
⇒ 3 = (−6)(−3) + α₂(−3)
⇒ 3 = 18 − 3α₂
⇒ 3α₂ = 15
∴ α₂ = 5

Putting values:
aₙ = −6(−3)ⁿ + 5n(−3)ⁿ

which is the solution of the given recurrence relation.

*(Source: Sir Notes.pdf, pp. 6–8)*

### গ. দ্বিতীয় Sequence-এর Characteristic Equation ও Roots

aₙ = 6aₙ₋₁ − 11aₙ₋₂ + 6aₙ₋₃, with a₀ = 2, a₁ = 5, a₂ = 15.

Let aₙ = rⁿ be a solution.

rⁿ = 6rⁿ⁻¹ − 11rⁿ⁻² + 6rⁿ⁻³

Dividing both sides by rⁿ⁻³:
r³ = 6r² − 11r + 6
⇒ r³ − 6r² + 11r − 6 = 0
⇒ r³ − r² − 5r² + 5r + 6r − 6 = 0
⇒ r²(r − 1) − 5r(r − 1) + 6(r − 1) = 0
⇒ (r − 1)(r² − 5r + 6) = 0
⇒ (r − 1)(r² − 3r − 2r + 6) = 0
⇒ (r − 1)[r(r − 3) − 2(r − 3)] = 0
⇒ (r − 1)(r − 2)(r − 3) = 0

∴ r = 1, 2, 3

Here, the roots are real and distinct.

*(Source: Sir Notes.pdf, pp. 8–9)*

### ঘ. Real & Distinct Roots vs Real & Equal Roots

**Theorem for Distinct Roots:**
Let c₁ and c₂ be real numbers. Suppose that r² − c₁r − c₂ = 0 has two distinct roots r₁ and r₂. Then the sequence {aₙ} is a solution of the recurrence relation aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ if and only if:

aₙ = α₁r₁ⁿ + α₂r₂ⁿ for n = 0, 1, 2, …

where α₁ and α₂ are constants.

**Distinct Roots Example (aₙ = aₙ₋₁ + 2aₙ₋₂):**
r = 2, −1
aₙ = α₁(2)ⁿ + α₂(−1)ⁿ

**Equal Roots Example (aₙ = −6aₙ₋₁ − 9aₙ₋₂):**
r = −3, −3
aₙ = α₁(−3)ⁿ + nα₂(−3)ⁿ

**পার্থক্য:**
| Distinct Roots | Equal Roots |
|---|---|
| General solution: aₙ = α₁r₁ⁿ + α₂r₂ⁿ | General solution: aₙ = α₁rⁿ + nα₂rⁿ |
| দুটি ভিন্ন basis solution | একটি basis solution, দ্বিতীয়টি n × basis |
| Roots: r₁ ≠ r₂ | Roots: r₁ = r₂ |

*(Source: Sir Notes.pdf, pp. 2–3, 7–8)*
