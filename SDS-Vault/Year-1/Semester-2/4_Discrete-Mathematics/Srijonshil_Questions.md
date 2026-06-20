# Srijonshil Questions — Discrete Mathematics

> See `Srijonshil_Answers.md` for full answers, embedded diagrams, and an Appendix covering extra slide content (examples, exercises, one bonus gate-comparison topic) not phrased as a numbered question here.

---

## Question 1: Discrete Mathematics & Propositions

**(a)** What is discrete mathematics?  
**(b)** What is a proposition? What are atomic and compound propositions?  
**(c)** What is negation? What is conjunction? What is disjunction? Construct truth tables.  
**(d)** What is exclusive or? What is a conditional statement? What is a bi-conditional statement? Construct truth tables.

---

## Question 2: Tautology, Contradiction, Cryptography & Applications

**(a)** What is a tautology? What is a contradiction?  
**(b)** What is cryptography? What is encryption? What is decryption?  
**(c)** What is the role of number theory and modular arithmetic in RSA?  
**(d)** How does discrete mathematics contribute to cryptography?

---

## Question 3: Functions, Predicates & Quantifiers

**(a)** What is a function?  
**(b)** What is a one-to-one function?  
**(c)** What is an onto function?  
**(d)** What is a predicate? What are universal and existential quantifiers?

---

## Question 4: Theorem, Proof Methods, Logic & Fallacies

**(a)** What is a theorem? What is an axiom? What is a proof? What is logic?  
**(b)** What is a direct proof? What is a proof by contradiction?  
**(c)** What is a proof by contrapositive? What is a proof by mathematical induction?  
**(d)** What is a fallacy? What is a division by zero fallacy?

---

## Question 5: Lemma, Corollary, Conjecture & Recurrence Basics

**(a)** What is a lemma? What is a corollary? What is a conjecture?  
**(b)** What is a recurrence relation? Derive the recurrence relation for the bank interest problem and find the amount after 30 years.  
**(c)** What is the characteristic equation? What are characteristic roots?  
**(d)** Solve: aₙ = aₙ₋₁ + 2aₙ₋₂, with a₀ = 2, a₁ = 7.

---

## Question 6: Advanced Recurrence Relations & Fibonacci

**(a)** Solve: aₙ = −6aₙ₋₁ − 9aₙ₋₂, with a₀ = −6, a₁ = 3.  
**(b)** Solve: aₙ = 6aₙ₋₁ − 11aₙ₋₂ + 6aₙ₋₃, with a₀ = 2, a₁ = 5, a₂ = 15.  
**(c)** Derive the explicit formula for the Fibonacci sequence.  
**(d)** What is the general solution for real and distinct roots? What is the general solution for real and equal roots?

---

## Question 7: Logic Gates & Boolean Circuits

> _Added — present in Lec_1.pdf (pp. 19–22) but not in the original Srijonshil set._

**(a)** What is a logic gate? Explain the AND, OR, and NOT gates with truth tables.  
**(b)** What are NAND, NOR, XOR, and XNOR gates? Construct their truth tables.  
**(c)** A circuit has inputs A, B, C, where one AND gate produces AB, an OR gate produces B+C, a second AND gate produces BC, and a third AND gate combines BC with (B+C). All outputs feed a final OR gate. Derive the boolean expression for the output Q.  
**(d)** Two XOR gates take inputs (A,B) and (C,D); their outputs feed an AND gate to give output F. Separately, inputs A and B feed both an OR gate and a NAND gate, whose outputs feed a final AND gate to give output Y. Derive the boolean expressions for F and Y, and show what identity Y demonstrates.

---

## Question 8: Cryptography History, Tautology Practice & Recurrence Verification

> _Added — present in Lec_1.pdf (p. 7) and Lec_1.pdf (pp. 17–18) and Sir_Notes.pdf (p. 3) but not in the original Srijonshil set._

**(a)** Give a brief timeline of the history of cryptography, from ancient times to the modern era.  
**(b)** Is x→(x∨y) a tautology? Is [(p→q)∧p]→p a tautology? Construct truth tables and justify your answer.  
**(c)** Is (p∨q)→(p∧q) a tautology? Is (r→s)↔(s→r) a tautology? Construct truth tables and justify your answer.  
**(d)** What does it mean for a sequence to be a "solution" of a recurrence relation? Verify that aₙ = 3n is a solution of the recurrence relation aₙ = 2aₙ₋₁ − aₙ₋₂.