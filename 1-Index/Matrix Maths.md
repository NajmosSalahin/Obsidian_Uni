Question 13: ![[Pasted image 20251125205150.png]]
$$A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}$$

$$B = \begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{pmatrix}$$


The trace is the sum of the main diagonal:

$$\text{tr}(A) = a_{11} + a_{22}$$

$$\text{tr}(B) = b_{11} + b_{22}$$

Show that, $\text{tr}(A \otimes B) = (a_{11} + a_{22})(b_{11} + b_{22})$.

We multiply every element of $A$ by the whole matrix $B$.

$$A \otimes B = \begin{pmatrix} a_{11}\begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{pmatrix} & a_{12}\begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{pmatrix} \\ \\ a_{21}\begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{pmatrix} & a_{22}\begin{pmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{pmatrix} \end{pmatrix}$$

Expand this into a single $4 \times 4$ matrix:

$$A \otimes B = \begin{pmatrix} \mathbf{a_{11}b_{11}} & a_{11}b_{12} & a_{12}b_{11} & a_{12}b_{12} \\ a_{11}b_{21} & \mathbf{a_{11}b_{22}} & a_{12}b_{21} & a_{12}b_{22} \\ a_{21}b_{11} & a_{21}b_{12} & \mathbf{a_{22}b_{11}} & a_{22}b_{12} \\ a_{21}b_{21} & a_{21}b_{22} & a_{22}b_{21} & \mathbf{a_{22}b_{22}} \end{pmatrix}$$

sum the bolded elements along the main diagonal:

$$\text{tr}(A \otimes B) = a_{11}b_{11} + a_{11}b_{22} + a_{22}b_{11} + a_{22}b_{22}$$
factor $a_{11}$ from the first two terms, and $a_{22}$ from the last two terms:

$$= a_{11}(b_{11} + b_{22}) + a_{22}(b_{11} + b_{22})$$

$(b_{11} + b_{22})$ is a common factor. Factor that out:

$$= (a_{11} + a_{22})(b_{11} + b_{22})$$

- $(a_{11} + a_{22})$ is $\text{tr}(A)$
    
- $(b_{11} + b_{22})$ is $\text{tr}(B)$
    

Therefore:

$$\text{tr}(A \otimes B) = \text{tr}(A)\text{tr}(B)$$

Question 12:![[Pasted image 20251125205215.png]]


Q1:
Here are the solutions to the exercises presented in the image.

### **Exercise 1**

**Goal:** Verify Equation (3.22) ($A^r A^q = A^{r+q} = A^q A^r$) for the case $r = 2$ and $q = 3$, given:
$$A = \begin{pmatrix} 2 & 4 & 5 \\ 1 & 1 & 2 \\ 0 & 6 & 8 \end{pmatrix}$$

**Step 1: Calculate $A^2$ ($A \times A$)**
$$A^2 = \begin{pmatrix} 2 & 4 & 5 \\ 1 & 1 & 2 \\ 0 & 6 & 8 \end{pmatrix} \begin{pmatrix} 2 & 4 & 5 \\ 1 & 1 & 2 \\ 0 & 6 & 8 \end{pmatrix} = \begin{pmatrix} 8 & 42 & 58 \\ 3 & 17 & 23 \\ 6 & 54 & 76 \end{pmatrix}$$

**Step 2: Calculate $A^3$ ($A^2 \times A$)**
$$A^3 = \begin{pmatrix} 8 & 42 & 58 \\ 3 & 17 & 23 \\ 6 & 54 & 76 \end{pmatrix} \begin{pmatrix} 2 & 4 & 5 \\ 1 & 1 & 2 \\ 0 & 6 & 8 \end{pmatrix} = \begin{pmatrix} 58 & 422 & 588 \\ 23 & 167 & 233 \\ 66 & 534 & 746 \end{pmatrix}$$

**Step 3: Verify equality ($A^2 A^3 = A^3 A^2$)**
To verify the equation, we calculate the product in both orders.
* **LHS ($A^2 A^3$):**
    $$\begin{pmatrix} 8 & 42 & 58 \\ 3 & 17 & 23 \\ 6 & 54 & 76 \end{pmatrix} \begin{pmatrix} 58 & 422 & 588 \\ 23 & 167 & 233 \\ 66 & 534 & 746 \end{pmatrix} = \begin{pmatrix} 5258 & 41362 & 57758 \\ 2083 & 16387 & 22883 \\ 6606 & 52122 & 72796 \end{pmatrix}$$

* **RHS ($A^3 A^2$):**
    $$\begin{pmatrix} 58 & 422 & 588 \\ 23 & 167 & 233 \\ 66 & 534 & 746 \end{pmatrix} \begin{pmatrix} 8 & 42 & 58 \\ 3 & 17 & 23 \\ 6 & 54 & 76 \end{pmatrix} = \begin{pmatrix} 5258 & 41362 & 57758 \\ 2083 & 16387 & 22883 \\ 6606 & 52122 & 72796 \end{pmatrix}$$

**Conclusion:** Since $A^2 A^3 = A^3 A^2$, the equation is verified.

---

### **Exercise 2**

**Given:**
$$A = \begin{pmatrix} 2 & 4 & 5 \\ 1 & 1 & 2 \\ 0 & 6 & 8 \end{pmatrix}, \quad B = \begin{pmatrix} 2 & 2 & 9 \\ 6 & 1 & 6 \\ 5 & 1 & 0 \end{pmatrix}$$

**a. Show that $AB \neq BA$**

* **Calculate $AB$:**
    $$AB = \begin{pmatrix} 2(2)+4(6)+5(5) & 2(2)+4(1)+5(1) & 2(9)+4(6)+5(0) \\ 1(2)+1(6)+2(5) & 1(2)+1(1)+2(1) & 1(9)+1(6)+2(0) \\ 0(2)+6(6)+8(5) & 0(2)+6(1)+8(1) & 0(9)+6(6)+8(0) \end{pmatrix}$$
    $$AB = \begin{pmatrix} 53 & 13 & 42 \\ 18 & 5 & 15 \\ 76 & 14 & 36 \end{pmatrix}$$

* **Calculate $BA$:**
    $$BA = \begin{pmatrix} 2(2)+2(1)+9(0) & 2(4)+2(1)+9(6) & 2(5)+2(2)+9(8) \\ 6(2)+1(1)+6(0) & 6(4)+1(1)+6(6) & 6(5)+1(2)+6(8) \\ 5(2)+1(1)+0(0) & 5(4)+1(1)+0(6) & 5(5)+1(2)+0(8) \end{pmatrix}$$
    $$BA = \begin{pmatrix} 6 & 64 & 86 \\ 13 & 61 & 80 \\ 11 & 21 & 27 \end{pmatrix}$$

**Conclusion:** Clearly, $AB \neq BA$.

**b. Compute $A + B$ and $A - B$**

* **$A + B$ (Element-wise addition):**
    $$A + B = \begin{pmatrix} 2+2 & 4+2 & 5+9 \\ 1+6 & 1+1 & 2+6 \\ 0+5 & 6+1 & 8+0 \end{pmatrix} = \begin{pmatrix} 4 & 6 & 14 \\ 7 & 2 & 8 \\ 5 & 7 & 8 \end{pmatrix}$$

* **$A - B$ (Element-wise subtraction):**
    $$A - B = \begin{pmatrix} 2-2 & 4-2 & 5-9 \\ 1-6 & 1-1 & 2-6 \\ 0-5 & 6-1 & 8-0 \end{pmatrix} = \begin{pmatrix} 0 & 2 & -4 \\ -5 & 0 & -4 \\ -5 & 5 & 8 \end{pmatrix}$$

**c. Show that $3A = 3IA$**

* $I$ is the Identity matrix $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$.
* A fundamental property of matrices is that $IA = A$.
* Therefore, multiplying the scalar 3 by $IA$ is identical to multiplying 3 by $A$.
* **Verification:**
    $$3A = \begin{pmatrix} 6 & 12 & 15 \\ 3 & 3 & 6 \\ 0 & 18 & 24 \end{pmatrix}$$
    $$3IA = 3 \left( \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 2 & 4 & 5 \\ 1 & 1 & 2 \\ 0 & 6 & 8 \end{pmatrix} \right) = 3 \begin{pmatrix} 2 & 4 & 5 \\ 1 & 1 & 2 \\ 0 & 6 & 8 \end{pmatrix} = \begin{pmatrix} 6 & 12 & 15 \\ 3 & 3 & 6 \\ 0 & 18 & 24 \end{pmatrix}$$

---

### **Exercise 3**

**Prerequisites: Calculate Determinants**
* **$|A|$:**
    $|A| = 2(8 - 12) - 4(8 - 0) + 5(6 - 0)$
    $|A| = 2(-4) - 32 + 30 = -8 - 32 + 30 = \mathbf{-10}$
* **$|B|$:**
    $|B| = 2(0 - 6) - 2(0 - 30) + 9(6 - 5)$
    $|B| = -12 + 60 + 9 = \mathbf{57}$

**a. Show that $|3A| = 3^3 |A|$**
* **Property:** For an $n \times n$ matrix, $|kA| = k^n|A|$. Here, $n=3$ and $k=3$.
* **LHS:** From Ex 2c, $3A = \begin{pmatrix} 6 & 12 & 15 \\ 3 & 3 & 6 \\ 0 & 18 & 24 \end{pmatrix}$.
    $|3A| = 6(72 - 108) - 12(72 - 0) + 15(54 - 0)$
    $|3A| = 6(-36) - 864 + 810 = -216 - 864 + 810 = \mathbf{-270}$
* **RHS:** $3^3 |A| = 27 \times (-10) = \mathbf{-270}$
* **Result:** LHS = RHS.

**b. Show that $|AB| = |A||B|$**
* **LHS:** We calculated matrix $AB$ in Ex 2a.
    $|AB| = 53(180 - 210) - 13(648 - 1140) + 42(252 - 380)$
    $|AB| = 53(-30) - 13(-492) + 42(-128)$
    $|AB| = -1590 + 6396 - 5376 = \mathbf{-570}$
* **RHS:** $|A||B| = (-10) \times 57 = \mathbf{-570}$
* **Result:** LHS = RHS.

**c. Show that $|A \otimes B| = |A|^3 |B|^3$**
* This involves the **Kronecker Product** ($\otimes$). A property of the Kronecker product for an $n \times n$ matrix $A$ and an $m \times m$ matrix $B$ is: $|A \otimes B| = |A|^m |B|^n$.
* Here, both matrices are $3 \times 3$, so $n=3$ and $m=3$.
* Therefore, the equation represents the standard determinant property for Kronecker products.
* **Calculation:**
    $|A|^3 |B|^3 = (-10)^3 \times (57)^3$
    $= -1000 \times 185,193$
    $= \mathbf{-185,193,000}$


Q9:

Given Matrices:

$$A = \begin{pmatrix} 2 & 11 & 3 \\ 0 & 4 & -5 \\ 6 & 10 & 14 \\ 9 & -1 & 3 \end{pmatrix}, \quad B = \begin{pmatrix} 2 & 11 & 6 \\ 5 & -3 & 4 \\ -9 & 2 & 0 \end{pmatrix}$$

Definition of Trace:

The trace of a square matrix is the sum of the elements on its main diagonal (from the top-left to the bottom-right).

---

### **a. Find the trace of matrix B.**

Matrix $B$ is a $3 \times 3$ square matrix. Its main diagonal elements are $2$, $-3$, and $0$.

$$\text{tr}(B) = 2 + (-3) + 0$$

$$\text{tr}(B) = -1$$

**Answer:** The trace of matrix $B$ is **-1**.

---

### **b. Find the trace of $A^T A$ and verify Equation (3.71).**

Equation (3.71) states that for any two matrices $X$ and $Y$ such that the products $XY$ and $YX$ are defined square matrices, **$\text{tr}(XY) = \text{tr}(YX)$**.

In this problem, we are asked to find $\text{tr}(A^T A)$ and then use the matrices $A^T$ and $A$ to verify this property (i.e., show that $\text{tr}(A^T A) = \text{tr}(A A^T)$).

Step 1: Find the transpose of A ($A^T$).

To find $A^T$, we swap the rows and columns of $A$.

$$A^T = \begin{pmatrix} 2 & 0 & 6 & 9 \\ 11 & 4 & 10 & -1 \\ 3 & -5 & 14 & 3 \end{pmatrix}$$

Step 2: Calculate $\text{tr}(A^T A)$.

$A^T$ is a $3 \times 4$ matrix and $A$ is a $4 \times 3$ matrix, so their product $A^T A$ is a $3 \times 3$ matrix. To find the trace, we only need to calculate the diagonal elements.

- 1st diagonal element: (Row 1 of $A^T$) $\cdot$ (Col 1 of $A$)
    
    $$(2)(2) + (0)(0) + (6)(6) + (9)(9) = 4 + 0 + 36 + 81 = 121$$
    
- 2nd diagonal element: (Row 2 of $A^T$) $\cdot$ (Col 2 of $A$)
    
    $$(11)(11) + (4)(4) + (10)(10) + (-1)(-1) = 121 + 16 + 100 + 1 = 238$$
    
- 3rd diagonal element: (Row 3 of $A^T$) $\cdot$ (Col 3 of $A$)
    
    $$(3)(3) + (-5)(-5) + (14)(14) + (3)(3) = 9 + 25 + 196 + 9 = 239$$
    

Now, sum the diagonal elements:

$$\text{tr}(A^T A) = 121 + 238 + 239 = 598$$

**Answer:** The trace of $A^T A$ is **598**.

Step 3: Verify Equation (3.71) by calculating $\text{tr}(A A^T)$.

$A$ is a $4 \times 3$ matrix and $A^T$ is a $3 \times 4$ matrix, so their product $A A^T$ is a $4 \times 4$ matrix. We calculate its diagonal elements.

- 1st diagonal element: (Row 1 of $A$) $\cdot$ (Col 1 of $A^T$)
    
    $$(2)(2) + (11)(11) + (3)(3) = 4 + 121 + 9 = 134$$
    
- 2nd diagonal element: (Row 2 of $A$) $\cdot$ (Col 2 of $A^T$)
    
    $$(0)(0) + (4)(4) + (-5)(-5) = 0 + 16 + 25 = 41$$
    
- 3rd diagonal element: (Row 3 of $A$) $\cdot$ (Col 3 of $A^T$)
    
    $$(6)(6) + (10)(10) + (14)(14) = 36 + 100 + 196 = 332$$
    
- 4th diagonal element: (Row 4 of $A$) $\cdot$ (Col 4 of $A^T$)
    
    $$(9)(9) + (-1)(-1) + (3)(3) = 81 + 1 + 9 = 91$$
    

Now, sum the diagonal elements:

$$\text{tr}(A A^T) = 134 + 41 + 332 + 91 = 598$$

Conclusion:

We found that $\text{tr}(A^T A) = 598$ and $\text{tr}(A A^T) = 598$.

Since $\text{tr}(A^T A) = \text{tr}(A A^T)$, Equation (3.71) is verified.




