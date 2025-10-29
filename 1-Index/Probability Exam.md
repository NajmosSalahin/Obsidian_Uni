My apologies. The markdown and LaTeX formatting can be fragile.

Here is the cleaned-up and deduplicated content again, with all LaTeX expressions properly formatted.

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