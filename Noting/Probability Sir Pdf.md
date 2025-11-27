---
banner: Github/Resources/Banners/Wallpaper/anime_girl_plus_rockets.png
content-start: 291
---
---
## Probabilistic Concepts: Definitions

### (i) Trial

- **Definition:** A trial is an experiment or an action that results in one or more outcomes.
    
- **Example:** Tossing a coin once is a trial. Throwing a dice once is also a trial.
    

---

### (ii) Experiment

- **Definition:** A process or action that leads to an outcome, or a repeatable procedure with uncertain outcome(s).
    
- **Example:** Tossing a coin, rolling a die.
    

---

### (iii) Sample Space

- **Definition:** The set of all possible outcomes of a trial or experiment.
    
- **Example:**
    
    - Tossing a coin: $S=\{H,T\}$.
        
    - Tossing two coins: $S=\{HH,HT,TH,TT\}$.
        
    - Rolling a die: $S=\{1,2,3,4,5,6\}$.
        

---

### (iv) Event

- **Definition:** An event is a subset of the sample space, i.e., a collection of possible outcomes of a trial.
    
- **Example:** If we roll a die, the sample space is $S=\{1,2,3,4,5,6\}$.
    
    - Event "getting an even number" $=E=\{2,4,6\}$.
        
    - Event "getting a number greater than $4$" $=F=\{5,6\}$.
        

---

### (v) Equally Likely

- **Definition:** Outcomes are said to be equally likely if each has the same chance (probability) of occurring.
    
- **Example:** Tossing a fair coin: two outcomes {Head, Tail}, both equally likely with probability $=0.5$ each.
    
- **Counter Example:** Drawing a card from a deck where some cards are missing outcomes are not equally likely.
    

---

### (vi) Mutually Exclusive

- **Definition:** Two or more events are mutually exclusive (disjoint) if they cannot occur at the same time.
    
- **Example:**
    
    - When tossing a die, the event $A=$ {rolling an odd number) and $B=$ {rolling an even number} are mutually exclusive.
        
    - Tossing a coin $\rightarrow$ Event $A=\{Head\}$, Event $B=\{Tail\}$. Since both cannot occur together, they are mutually exclusive.
        
- **Counter Example:** Events $A=$ {rolling a number greater than 3) and $B=$ {rolling an even number} are not mutually exclusive (since 4 and 6 belong to both).
    

---

### (vii) Independent Events

- **Definition:** Occurrence of one does not change the probability of the other: $P(A\cap B)=P(A)P(B)$.
    
- **Example:** Two separate fair coin tosses: A = {first toss is H}, B={second toss is H}; $P(A\cap B)=\frac{1}{4}=\frac{1}{2}\cdot\frac{1}{2}$.
    

---

---

## Set Theory: Definitions

### 1. Set

- **Definition:** A collection of distinct, well-defined objects.
    
- **Example:** $A=\{1,2,3,4\}$ is a set of numbers.
    

### 2. Subset

- **Definition:** A set A is called a subset of B if every element of A is also in B.
    
- **Notation:** $A\subseteq B$.
    
- **Example:** If $B=\{1,2,3,4,5\}$ then $A=\{2,4\}$ is a subset of B.
    

### 3. Universal Set

- **Definition:** The set that contains all objects under consideration in a given context.
    
- **Notation:** U.
    
- **Example:** If we are studying even and odd numbers under 1 to 10, then $U=\{1,2,3,4,5,6,7,8,9,10\}$.
    

### 4. Empty Set (Null Set)

- **Definition:** A set with no elements.
    
- **Notation:** $\emptyset$ or {}.
    
- **Example:** $A=\{x|x^{2}+1=0, x\in R\}=\phi$ (since no real number squared $+1=0$).
    

### 5. Disjoint Sets

- **Definition:** Two sets are disjoint if they have no elements in common.
    
- **Example:** $A=\{1,2,3\}$, $B=\{4,5,6\}$. Here, $A\cap B=\emptyset$.
    

### 6. Power Set

- **Definition:** The set of all subsets of a set A.
    
- **Notation:** $P(A)$.
    
- **Example:** If $A=\{1,2\}$ then $P(A)=\{\emptyset,\{1\},\{2\},\{1,2\}\}$.
    

### 7. Product Set (Cartesian Product)

- **Definition:** For sets A and B, the product set is $A\times B=\{(a,b)|a\in A, b\in B\}$.
    
- **Example:** If $A=\{1,2\}$, $B=\{x,y\}$ then $A\times B=\{(1,x),(1,y),(2,x),(2,y)\}$.
    

### 8. Countable and Uncountable Sets

- **Countable Set:** A set whose elements can be put into one-to-one correspondence with natural numbers (finite or countably infinite).
    
    - **Example:**
        
        - $N=\{1,2,3,4,...\}$ (natural numbers) is countably infinite.
            
        - The outcomes of rolling a die {1, 2, 3, 4, 5, 6} is a finite countable set.
            
        - The set of even integers $\{0,\pm2,\pm4,...\}$ is countably infinite.
            
- **Uncountable Set:** A set that cannot be listed or paired with natural numbers; it has infinitely many elements that cannot be counted.
    
    - **Example:**
        
        - The set of real numbers between 0 and 1, i.e., $(0, 1)$, is uncountable.
            
        - The interval $[0, 5]$ is also uncountable.
            

### 9. Real Line

- **Definition:** The set of all real numbers represented as points on a straight line.
    
- **Example:** The number line showing ..., -2, -1, 0, 1, 2, ... and all decimal values.
    

### 10. Venn Diagram

- **Definition:** A pictorial representation of sets and their relationships using closed curves (usually circles) inside a rectangle (universal set).
    
- **Example:** Two overlapping circles show union, intersection, and disjoint sets.
    

### 11. Classes of Sets

- Some important classes:
    
    - **Finite Set:** Limited elements, e.g. {1,2,3}.
        
    - **Infinite Set:** Unlimited elements, e.g. natural numbers {1, 2, 3, ...}.
        
    - **Equal Sets:** Same elements, e.g. $\{a,b\}=\{b,a\}$.
        
    - **Equivalent Sets:** Different elements but same number of elements, e.g. {1,2,3} and {x,y,z}.
        
    - **Overlapping Sets:** At least one common element.
        
    - **Disjoint Sets:** No common element.
        
    - **Subsets/Proper subsets**.
        

---

---

## Probability: Axioms, Types, and Consequences

### Definition and Types

- **Axiomatic Definition:** A function $P:F\rightarrow[0,1]$ assigning numbers to events satisfying Kolmogorov's axioms.
    
- **Types (Interpretations):**
    
    - **Classical (equally likely):** $P(A)=\frac{\#A}{\#S}$.
        
    - **Frequentist (relative frequency):** long-run limit of frequency.
        
    - **Subjective/Bayesian:** degree of belief updated by Bayes' rule.
        
    - **Axiomatic:** abstract measure satisfying axioms below.
        

---

### The Axioms of Probability (Kolmogorov)

1. **Non-negativity:** $P(A)\ge0$ for any event A.
    
2. **Normalization:** $P(S)=1$, where S is the sample space.
    
3. **Countable Additivity:** If $A_1, A_2, ...$ are pairwise disjoint events, then $P(\bigcup_{i}A_{i})=\sum_{i}P(A_{i})$.
    
    - (For two disjoint events, this simplifies to $P(A\cup B)=P(A)+P(B)$).
        

---

### Consequences from Axioms

**(i) Probability of Empty Set:** $P(\emptyset)=0$.

- Proof: Since S and $\emptyset$ are mutually exclusive and $S\cup\emptyset=S$,
    
    $P(S)=P(S)+P(\emptyset)$.
    
    By Axiom 2, $1 = 1 + P(\emptyset)$, so $P(\emptyset)=0$.
    

**(ii) Probability of the Complement:** $P(A^{c})=1-P(A)$.

- Proof: Since $A \cup A^{c} = S$ and $A \cap A^{c} = \emptyset$, by additivity:
    
    $P(S) = P(A \cup A^{c}) = P(A) + P(A^{c})$.
    
    By Axiom 2, $1 = P(A) + P(A^{c})$, so $P(A^{c}) = 1 - P(A)$.
    

**(iii) Probability is Between 0 and 1:** $0\le P(A)\le1$.

- Proof: From Axiom 1, $P(A)\ge0$.
    
    From consequence (ii), $P(A)=1-P(A^{c})$.
    
    Since $P(A^{c})\ge0$ (by Axiom 1), it must be that $P(A)\le1$.
    
    Thus, $0\le P(A)\le1$.
    

**(iv) General Additivity (for finite disjoint events):** If $A_{1},A_{2},...,A_{n}$ are mutually exclusive, then $P(\bigcup_{i=1}^{n}A_{i})=\sum_{i=1}^{n}P(A_{i})$.

**(v) Subadditivity:** For _any_ events $E_{1}, E_{2}, ...$ (not necessarily disjoint), $P(\bigcup_{i=1}^{\infty}E_{i})\le\sum_{i=1}^{\infty}P(E_{i})$.

---

### Numerical Example (General Additivity)

- **Experiment:** Die roll.
    
- $P(\text{even}) = P(\{2,4,6\}) = 3/6 = 1/2$.
    
- $P(>4) = P(\{5,6\}) = 2/6 = 1/3$.
    
- Since the events "even" and ">4" overlap at {6} (which has $P(\{6\})=1/6$), they are _not_ mutually exclusive.
    
- The general additivity rule (for non-disjoint events, $P(A \cup B) = P(A) + P(B) - P(A \cap B)$) gives:
    
    $P(\text{even} \cup >4)=\frac{1}{2}+\frac{1}{3}-\frac{1}{6}=\frac{3}{6}+\frac{2}{6}-\frac{1}{6}=\frac{4}{6}=\frac{2}{3}$.
    

---

---

## Problems and Proofs

### 1(b). If $A\subset B$

If A is a subset of B ($A\subset B$), then:

- **(i)** $A\cap B=A$ (every element of A already lies in B).
    
- **(ii)** $B \cup A^{c}=U$ (the universal set): for any x, either $x\notin A$ (so $x\in A^{c}$) or $x\in A$. If $x\in A$, then $x\in B$ (since $A\subset B$). Thus, any x is in $A^{c}$ or in $B$.
    
- **(iii)** $A\cap B^{c}=\emptyset$ (nothing can be in A but also outside its superset B).
    

---

### 1(c). Proof of Subadditivity

For any events $E_{1}, E_{2}, ...$, prove $P(\bigcup_{i=1}^{\infty}E_{i})\le\sum_{i=1}^{\infty}P(E_{i})$.

- **Proof:** Define a new collection of disjoint sets $F_i$:
    
    - $F_{1}=E_{1}$
        
    - $F_{i}=E_{i}\setminus\bigcup_{j=1}^{i-1}E_{j}$ (for $i\ge2$) (i.e., $F_i$ is the part of $E_i$ not in any previous $E_j$).
        
- By construction, the $F_i$ are disjoint, and $\bigcup_{i}F_{i}=\bigcup_{i}E_{i}$.
    
- Also, $F_{i}\subseteq E_{i}$ for all $i$. By monotonicity (a consequence of the axioms), this means $P(F_i) \le P(E_i)$.
    
- Using countable additivity (Axiom 3) on the disjoint sets $F_i$:
    
    $P(\bigcup E_{i})=P(\bigcup F_{i})=\sum_{i}P(F_{i})\le\sum_{i}P(E_{i})$.
    

---

### 2(c). Drawing Balls

- **Problem:** Drawing 3 balls from a bag containing 6 white and 5 black balls (assuming without replacement). Find the probability of 1 white and 2 black.
    
- **Total ways:** The total number of ways to choose 3 balls from 11 is $\binom{11}{3}=165$.
    
- **Favourable ways:** The number of ways to choose 1 white ball from 6 is $\binom{6}{1}=6$. The number of ways to choose 2 black balls from 5 is $\binom{5}{2}=10$.
    
    - Total favourable ways = $6 \times 10 = 60$.
        
- **Probability:** $P=\frac{\text{Favourable}}{\text{Total}} = \frac{60}{165}=\frac{12}{33}=\frac{4}{11}\approx0.3636$.
    

---

### 2(c). Three Horses

- **Problem:** Three horses A, B, C are in a race. “A is twice as likely as B” and “B is twice as likely as C”. Find the probability that B or C wins.
    
- **Solution:**
    
    - Let $P(C) = x$.
        
    - Then $P(B) = 2x$ and $P(A) = 2 \times P(B) = 2(2x) = 4x$.
        
    - Since one must win (Axiom 2), $P(A) + P(B) + P(C) = 1$.
        
    - $4x + 2x + x = 1 \Rightarrow 7x = 1 \Rightarrow x = \frac{1}{7}$.
        
    - So, $P(A) = \frac{4}{7}$, $P(B) = \frac{2}{7}$, $P(C) = \frac{1}{7}$.
        
- **Probability (B or C wins):**
    
    - Since B and C winning are mutually exclusive events:
        
    - $P(B \cup C) = P(B) + P(C) = \frac{2}{7} + \frac{1}{7} = \frac{3}{7}$.
        

---

### 2(d). Random point in a circle

- **Problem:** A random point is selected in a circle. What is the probability it is closer to the center than to the circumference?.
    
- **Solution:**
    
    - Let the circle have radius $R$. The total area is $\pi R^{2}$.
        
    - Let the point be at a distance $r$ from the center.
        
    - The distance to the circumference is $R - r$.
        
    - We want the points where the distance to the center ($r$) is less than the distance to the circumference ($R-r$).
        
    - $r < R - r \Rightarrow 2r < R \Rightarrow r < R/2$.
        
    - This "favourable region" is a smaller disk in the center with radius $R/2$.
        
    - The area of this favourable region is $\pi(R/2)^{2} = \frac{\pi R^{2}}{4}$.
        
- Probability: The probability is the ratio of the areas:
    
    $p = \frac{\text{Favourable Area}}{\text{Total Area}} = \frac{\pi(R/2)^{2}}{\pi R^{2}} = \frac{1}{4}$

---
## 1. Set Operations (New Definitions)

* **Membership:** $x\in A$ (x is an element of A).
* **Union:** $A \cup B = \{x: x \in A \text{ or } x\in B\}$.
* **Intersection:** $A \cap B = \{x: x \in A \text{ and } x \in B\}$.
* **Complement (relative to U):** $A^{c}=U\backslash A$.
* **Cardinality:** $|A|=$ number of elements.

### Step-by-Step Example

Let $U=\{1,2,3,4,5\}$, $A=\{1,3,5\}$, $B=\{2,3\}$.

1.  **Compute $A \cup B$:** List elements that are in A or in B.
    * Combine $\{1,3,5\}$ and $\{2,3\}$ without repetition to get $\{1, 3, 5, 2\}$.
    * Sorted: $A\cup B=\{1,2,3,5\}$.
2.  **Compute $A \cap B$:** Find elements common to both.
    * Both contain 3 only.
    * $A\cap B=\{3\}$.
3.  **Compute $A^{c}$ (relative to U):** Remove A's elements from U.
    * $U\backslash A=\{2,4\}$.
    * $A^{c}=\{2,4\}$.
4.  **Compute $|A|$:** Count elements of $A=\{1,3,5\}$.
    * There are 3 elements.
    * $|A|=3$.

---

## 2. Functions

### Definition
A function $f$ from set X (domain) to set Y (codomain) is a rule assigning each $x\in X$ exactly one $f(x)\in Y$.
* **Properties:** one-to-one (injective), onto (surjective), inverse (if exists), composition.

### Example (Point Function)
Let $X=\{1,2,3,4\}$. Define $f:X\rightarrow R$ by $f(x)=2x$.
* $f(1)=2$
* $f(2)=4$
* $f(3)=6$
* $f(4)=8$

---

## 3. Point Function vs. Set Function

* **Point function:** A function whose input is a single point $x$ (element of domain).
    * **Example:** $f(x)=2x$.
* **Set function:** A function whose inputs are sets (subsets of some universe).
    * **Examples:** Cardinality $|A|$, measure $\mu(A)$, probability $P(A)$, or a sum over the set $S(A)=\sum_{x\in A}g(x)$.

### Example Linking Both
Let $U=\{1,2,3,4\}$.
Define point function $g(x)=x^{2}$ for $x\in U$.
Define set function $G(A)=\sum_{x\in A}g(x)$ (sum of squares on A).

**Compute $G(\{1,3\})$:**
1.  Compute $g(1)=1^{2}=1$.
2.  Compute $g(3)=3^{2}=9$.
3.  Sum: $G(\{1,3\})=1+9=10$.

* **Indicator function:** The indicator $I_{A}(x)$ is a point function defined by $I_{A}(x)=1$ if $x\in A$ and 0 otherwise. It ties sets and point functions together.

---

## 4. Counting Principles

### (A) Rule of Sum (Addition Rule)
If there are $m$ ways to do task A or $n$ ways to do task B, and the tasks are mutually exclusive (no overlap), the total ways $=m+n$.
* **Example:** Choose a vowel (5 ways) or a digit (10 ways) $\rightarrow 5+10=15$ ways.

### (B) Rule of Product (Multiplication Rule)
If a procedure has $k$ ordered stages (or successive, independent stages) with $n_{1}, n_{2}, ..., n_{k}$ choices respectively, the total ways $=n_{1}\cdot n_{2}\cdot\cdot\cdot n_{k}$.
* **Example:** Create a 3-character string where each position can be A/B/C/D (4 choices). Total ways $=4\cdot4\cdot4 = 64$ strings.

### (C) Factorials
$n!=n(n-1)(n-2)\cdot\cdot\cdot2\cdot1$.
* **Example:** $5!=5\cdot4\cdot3\cdot2\cdot1=120$.

### (D) Permutations (Ordered Arrangements)
The number of ordered selections of size $r$ from $n$ items.
* **Formula:** ${}_{n}P_{r}=\frac{n!}{(n-r)!}=n(n-1)\cdot\cdot\cdot(n-r+1)$.
* **Example:** Arrange 3 of 5 books in order.
    * ${}_{5}P_{3}=5\cdot4\cdot3 = 60$ arrangements.

### (E) Combinations (Unordered Selections)
The number of unordered selections of size $r$ from $n$ items.
* **Formula:** $\binom{n}{r}=\frac{n!}{r!(n-r)!}$.
* **Example:** Choose 3 students out of 8.
    * $\binom{8}{3}=\frac{8\cdot7\cdot6}{3\cdot2\cdot1} = \frac{336}{6} = 56$.

### (F) Pigeonhole Principle
If $N$ objects are placed into $k$ boxes and $N>k$, then some box contains at least two objects.

---

## 5. Binomial Theorem

### Statement
For any real/complex $x, y$ and integer $n\ge0$:
$(x+y)^{n}=\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^{k}$.

### Proof (by Induction)
* **Base Case ($n=0$):** $(x+y)^{0}=1$. The right-hand side (RHS) is $\binom{0}{0}x^{0}y^{0}=1$. It holds.
* **Inductive Step:** Assume true for $n$. We must show it holds for $n+1$.
    $(x+y)^{n+1}=(x+y)(x+y)^{n}=(x+y)\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^{k}$.
* **Distribute:**
    $(x+y)^{n+1}=\sum_{k=0}^{n}\binom{n}{k}x^{n+1-k}y^{k}+\sum_{k=0}^{n}\binom{n}{k}x^{n-k}y^{k+1}$.
* **Re-index:** Re-index the second sum with $j=k+1$. Using Pascal's identity $\binom{n}{k}+\binom{n}{k-1}=\binom{n+1}{k}$, the expression simplifies to:
    $(x+y)^{n+1}=\sum_{k=0}^{n+1}\binom{n+1}{k}x^{n+1-k}y^{k}$.

*(A combinatorial proof is also noted: the coefficient $\binom{n}{k}$ counts the ways to choose which $k$ factors contribute $y$ when expanding $(x+y)^n$).*

---

## 6. Principle of Mathematical Induction (PMI)

### PMI (Simple Form)
Let $P(n)$ be a statement about integers $n\ge n_{0}$. If:
1.  $P(n_{0})$ is true (base case), and
2.  $P(k)\Rightarrow P(k+1)$ for all $k\ge n_{0}$ (inductive step),
then $P(n)$ holds for all $n\ge n_{0}$.

### Application
Prove $n!\ge2^{n}$ for $n\ge4$.
* **Base $n=4$:** $4!=24$ and $2^{4}=16$. Since $24\ge16$, the base case is true.
* **Inductive Step:** Assume $k!\ge2^{k}$ for some $k\ge4$. We must show $(k+1)!\ge2^{k+1}$.
    * $(k+1)!=(k+1) \cdot (k!)$.
    * By assumption, $(k+1) \cdot (k!) \ge (k+1) \cdot 2^{k}$.
    * Since $k\ge4$, we know $k+1 \ge 5$, which is greater than 2.
    * Therefore, $(k+1) \cdot 2^{k} \ge 2 \cdot 2^{k} = 2^{k+1}$.
    * This shows $(k+1)!\ge2^{k+1}$. By induction, the statement is true.

---

## 7. Inequalities for $n$ Events

### Lower bound for intersection (Bonferroni)
$P(\bigcap_{i=1}^{n}A_{i})\ge\sum_{i=1}^{n}P(A_{i})-(n-1)$.
* **Proof:** Note $P(A_{i}^{c})=1-P(A_{i})$. Using Boole's inequality (which was covered as Subadditivity in the previous file) on the union of the complements:
    $P(\bigcap_{i=1}^{n}A_{i})=1-P(\bigcup_{i=1}^{n}A_{i}^{c})$
    $\ge 1-\sum_{i=1}^{n}P(A_{i}^{c})$
    $= 1-\sum_{i=1}^{n}(1-P(A_{i})) = \sum_{i=1}^{n}P(A_{i})-(n-1)$.

*(Note: The Union bound (Boole's inequality / Subadditivity) is skipped as it was in the previous file.)*

---

## 8. Short Solved Mixed Example

* **Problem:** Universe $U=\{1,2,3,4\}$. Point function $f(x)=x+1$. Let $A=\{1,3\}$.
    * (a) Compute $f(2)$.
    * (b) Compute set function $F(A)=\sum_{x\in A}f(x)$.
    * (c) How many ordered pairs (a, b) with $a\in A, b\in U$?
* **Solutions:**
    * (a) $f(2)=2+1=3$.
    * (b) Compute $f(1)=1+1=2$ and $f(3)=3+1=4$. Sum $F(A)=2+4=6$.
    * (c) Number of ordered pairs $=|A|\cdot|U|$ by the product rule.
        * $|A|=2$, $|U|=4$.
        * Total $=2\cdot4=8$.