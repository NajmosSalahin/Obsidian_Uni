# Srijonshil Answers — Discrete Mathematics

> All answers are directly extracted from the lecture PDFs (Lec_1.pdf, Lec_2.pdf, Sir Notes.pdf).

---

## Question 1: Discrete Mathematics & Propositions

### (a) What is discrete mathematics?

Discrete mathematics is a branch of mathematics that deals with mathematical structures and objects that are fundamentally discrete or separate in nature. Discrete mathematics is the part of mathematics devoted to the study of discrete objects. Discrete mathematics is the branch of mathematics dealing with objects that can assume only distinct, separated values. The term "discrete mathematics" is therefore used in contrast with "continuous mathematics," which is the branch of mathematics dealing with objects that can vary smoothly (which includes calculus). Whereas discrete objects can often be characterized by integers, continuous objects require real numbers.

Discrete mathematics or finite mathematics is the branch of mathematics in which the mathematical organizations are fundamentally isolated, that is, the notion of continuity does not apply to them.

*(Source: Lec_1.pdf, pp. 1–2)*

### (b) What is a conjunction? Construct a truth table for p˄q.

A conjunction is a compound statement formed by joining two statements with the connector AND. The conjunction "p and q" is symbolized by p˄q. A conjunction is true when both of its combined parts are true; otherwise it is false.

| p | q | p˄q |
|---|---|-------|
| T | T |   T   |
| T | F |   F   |
| F | T |   F   |
| F | F |   F   |

*(Source: Lec_1.pdf, pp. 13–14)*

### (c) What is a conditional statement? Construct a truth table for p→q.

Let p and q be propositions. The conditional statement p→q is the proposition "if p, then q." The conditional statement p→q is false when p is true and q is false, and true otherwise. In the conditional statement p→q, p is called the hypothesis and q is called the conclusion.

| p | q | p→q |
|---|---|-------|
| T | T |   T   |
| T | F |   F   |
| F | T |   T   |
| F | F |   T   |

*(Source: Lec_1.pdf, p. 16)*

### (d) What is a tautology? What is a contradiction?

A compound statement, that is always true regardless of the truth value of the individual statements, is defined to be a tautology.

A proposition that is false under all circumstances is called Contradiction.

| p | ~p | p˄~p |
|---|----|--------|
| T | F  |   F    |
| F | T  |   F    |

*(Source: Lec_1.pdf, pp. 17, 19)*

---

## Question 2: Cryptography & Number Theory

### (a) What is cryptography?

Cryptography is the science of protecting information by transforming it into a secure format so that only authorized parties can read or understand it.

In computer science, cryptography refers to secure information and communication techniques derived from mathematical concepts and a set of rule-based calculations called algorithms, to transform messages in ways that are hard to decipher.

*(Source: Lec_1.pdf, pp. 5–6)*

### (b) What is encryption? What is decryption?

It involves two main processes:

Encryption: Converting plain text into unreadable code (cipher text).

Decryption: Converting cipher text back into the original plain text.

*(Source: Lec_1.pdf, p. 6)*

### (c) What is the role of number theory and modular arithmetic in RSA?

Number Theory: Prime numbers and modular arithmetic are used in RSA, Diffie-Hellman, and similar systems. Logic: Boolean operations are used in encryption algorithms. Combinatorics: Used to calculate the number of possible keys and determine password complexity. Graph Theory: Applied in network security and data routing. Probability and Statistics: Required for random number generation and security analysis.

*(Source: Lec_1.pdf, p. 6)*

### (d) How does discrete mathematics contribute to cryptography?

Discrete mathematics is central to cryptography, the science of secure communication. Concepts such as modular arithmetic, number theory, and Boolean algebra are essential in designing and analyzing cryptographic algorithms. Discrete mathematics also helps in understanding and developing protocols for secure data transmission, authentication, and encryption.

Discrete mathematics has wide-ranging applications in computer science, cryptography, information theory, operations research, optimization, and many other fields. It provides the foundation for solving real-world problems using rigorous mathematical techniques and logical reasoning.

*(Source: Lec_1.pdf, pp. 2, 4)*

---

## Question 3: Function, Predicate & Quantifier

### (a) What is a function?

A function is a special kind of relation between two sets, say A (domain) and B (codomain), such that: Every element of A is related to exactly one element of B. Formally: f : A → B means that for each a ∈ A, there exists a unique b ∈ B such that f(a) = b.

*(Source: Lec_2.pdf, p. 1)*

### (b) What is a one-to-one function?

A one-to-one function, also known as an injective function, is a function where distinct inputs always produce distinct outputs. This means no two different inputs map to the same output, ensuring each element in the function's codomain is the image of at most one element from its domain. You can test if a function is one-to-one graphically by using the horizontal line test, which requires that any horizontal line drawn through the graph intersects it at no more than one point.

*(Source: Lec_2.pdf, p. 1)*

### (c) What is a predicate? What are universal and existential quantifiers?

Predicate: A statement involving variables that becomes true or false when specific values are substituted.

Quantifiers: Symbols that specify how many elements in a domain satisfy a predicate.

Universal Quantifier (∀): "For all."

Existential Quantifier (∃): "There exists."

*(Source: Lec_2.pdf, p. 2)*

### (d) What is an onto function?

An onto function, also known as a surjective function, is a function where every element in its codomain (the set of all possible outputs) is mapped to by at least one element in its domain (the set of all inputs). In simpler terms, the function "covers" its entire codomain.

*(Source: Lec_2.pdf, p. 2)*

---

## Question 4: Methods of Proof & Mathematical Structures

### (a) What is a theorem? What is an axiom?

A theorem is a mathematical statement that has been proven to be true using logical reasoning based on axioms, definitions, and previously established theorems.

Axioms (or postulates) are basic assumptions or self-evident truths accepted without proof, which serve as the foundation for developing a logical system or theory.

*(Source: Lec_2.pdf, pp. 4–5)*

### (b) What is a direct proof?

Direct proof: Where you directly show that the conclusion follows from the premise.

*(Source: Lec_2.pdf, p. 3)*

### (c) What is a proof by contradiction?

Proof by contradiction: Which assumes the negation of the statement and derives a false outcome.

*(Source: Lec_2.pdf, p. 3)*

### (d) What is a lemma? What is a corollary? What is a conjecture?

A lemma is a helping theorem — a proven statement used as a stepping stone to prove another, more significant theorem.

A corollary is a statement that follows readily from a theorem that has already been proven. It often appears as a direct consequence.

A conjecture is an unproven statement believed to be true based on observations or partial evidence but not yet proven.

*(Source: Lec_2.pdf, pp. 7–9)*

---

## Question 5: Recurrence Relation — Distinct Roots

### (a) What is a recurrence relation?

A recurrence relation for the sequence {aₙ} is an equation that expresses aₙ in terms of one or more of the previous terms of the sequence, namely a₀, a₁, a₂, …, aₙ₋₁ for all integer n with n ≥ n₀, where n₀ is a non-negative integer.

*(Source: Sir Notes.pdf, p. 1)*

### (b) Solve: aₙ = aₙ₋₁ + 2aₙ₋₂, with a₀ = 2, a₁ = 7.

aₙ = aₙ₋₁ + 2aₙ₋₂, with a₀ = 2, a₁ = 7.

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

### (c) What is the characteristic equation of a recurrence relation?

When solving recurrence relations, we try to find solutions of the form aₙ = rⁿ, where r is a constant.

If aₙ = rⁿ is a solution of aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + … + cₖaₙ₋ₖ if and only if:
rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻² + … + cₖrⁿ⁻ᵏ

Divide by rⁿ⁻ᵏ and subtract:
rᵏ − c₁rᵏ⁻¹ − c₂rᵏ⁻² − … − cₖ₋₁r − cₖ = 0

This is called the characteristic equation of the recurrence relation. The solutions of this equation are called the characteristic roots of the recurrence relation.

*(Source: Sir Notes.pdf, pp. 2–3)*

### (d) Derive the explicit formula for the Fibonacci sequence: fₙ = fₙ₋₁ + fₙ₋₂, f₀ = 0, f₁ = 1.

fₙ = fₙ₋₁ + fₙ₋₂, f₀ = 0, f₁ = 1.

Let fₙ = rⁿ be a solution.

rⁿ = rⁿ⁻¹ + rⁿ⁻²

Dividing both sides by rⁿ⁻²:
r² = r + 1
⇒ r² − r − 1 = 0

r = (1 ± √5)/2

∴ r₁ = (1 + √5)/2, r₂ = (1 − √5)/2

The roots are real and distinct.

The general solution is:
fₙ = α₁r₁ⁿ + α₂r₂ⁿ

When n = 0:
f₀ = α₁ + α₂ = 0 ⇒ α₁ + α₂ = 0 … (3)

When n = 1:
f₁ = α₁r₁ + α₂r₂ = 1 … (4)

Solving (3) and (4):
α₁ = 1/√5, α₂ = −1/√5

∴ fₙ = (1/√5)[(1 + √5)/2]ⁿ − (1/√5)[(1 − √5)/2]ⁿ

which is the required formula.

*(Source: Sir Notes.pdf, pp. 11–12)*

---

## Question 6: Recurrence Relation — Repeated Roots & Degree Three

### (a) Solve: aₙ = −6aₙ₋₁ − 9aₙ₋₂, with a₀ = −6, a₁ = 3.

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

The general solution is:
aₙ = α₁r₁ⁿ + nα₂r₂ⁿ

When n = 0:
a₀ = α₁ + 0 = −6 ⇒ α₁ = −6

When n = 1:
a₁ = α₁r₁ + α₂r₂
⇒ 3 = (−6)(−3) + α₂(−3)
⇒ 3 = 18 − 3α₂
⇒ 3α₂ = 15
∴ α₂ = 5

Putting the values:
aₙ = −6(−3)ⁿ + 5n(−3)ⁿ

which is the solution of the given recurrence relation.

*(Source: Sir Notes.pdf, pp. 6–8)*

### (b) Solve: aₙ = 6aₙ₋₁ − 11aₙ₋₂ + 6aₙ₋₃, with a₀ = 2, a₁ = 5, a₂ = 15.

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

### (c) What is the general solution for a recurrence relation with real and distinct roots?

Let c₁ and c₂ be real numbers. Suppose that r² − c₁r − c₂ = 0 has two distinct roots r₁ and r₂. Then the sequence {aₙ} is a solution of the recurrence relation aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ if and only if:
aₙ = α₁r₁ⁿ + α₂r₂ⁿ for n = 0, 1, 2, …
where α₁ and α₂ are constants.

*(Source: Sir Notes.pdf, p. 2)*

### (d) What is the general solution for a recurrence relation with real and equal roots?

The general solution is:
aₙ = α₁r₁ⁿ + nα₂r₂ⁿ

*(Source: Sir Notes.pdf, p. 7)*
