---
banner: Github/Resources/Banners/Wallpaper/anna-scarfiello-Pxf5syDVuxQ.jpg
content-start: 326
---
### 1. Diagonal Matrix

Definition:

A square matrix is called a diagonal matrix if all its non-diagonal elements are zero. The elements on the principal diagonal (from top-left to bottom-right) can be non-zero or zero.1

Mathematical Condition:

A square matrix $A = [a_{ij}]$ is a diagonal matrix if:

$$a_{ij} = 0 \quad \text{for all} \quad i \neq j$$

Example:

$$A = \begin{bmatrix} 5 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 9 \end{bmatrix}$$

---

### 2. Scalar Matrix

Definition:

A scalar matrix is a specific type of diagonal matrix where all the elements on the principal diagonal are equal to the same non-zero scalar (constant).2

Mathematical Condition:

A square matrix $A = [a_{ij}]$ is a scalar matrix if:

$$a_{ij} = \begin{cases} 0 & \text{if } i \neq j \\ k & \text{if } i = j \quad (\text{where } k \text{ is a constant}) \end{cases}$$

Example:

$$A = \begin{bmatrix} 4 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4 \end{bmatrix}$$

---

### 3. Unit Matrix (Identity Matrix)

Definition:

A Unit Matrix, denoted by 3$I$, is a scalar matrix where each element on the principal diagonal is equal to 4$1$.5 It acts as the multiplicative identity in matrix algebra (similar to the number 1 in standard arithmetic).6

Mathematical Condition:

A square matrix $A = [a_{ij}]$ is a unit matrix if:

$$a_{ij} = \begin{cases} 0 & \text{if } i \neq j \\ 1 & \text{if } i = j \end{cases}$$

Example ($I_3$):

$$I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

---

### 4. Incidence Matrix

Definition:

Used primarily in Graph Theory, an incidence matrix represents the relationship between the vertices (nodes) and edges (connections) of a graph.7

Explanation:

For a graph with 8$n$ vertices and 9$m$ edges, the incidence matrix is an 10$n \times m$ matrix.11

- **Rows** represent vertices.
    
- **Columns** represent edges.
    
- If an edge connects to a vertex, the value is usually 12$1$ (or 13$-1$ in directed graphs to show direction).14 If there is no connection, the value is $0$.
    

Example (Undirected Graph):

If Edge 1 connects Vertex A and Vertex B:

$$M = \begin{bmatrix} 1 & ... \\ 1 & ... \\ 0 & ... \end{bmatrix} \begin{matrix} \leftarrow \text{Vertex A} \\ \leftarrow \text{Vertex B} \\ \leftarrow \text{Vertex C} \end{matrix}$$

---

### 5. Triangular Matrix

Definition:

A square matrix is triangular if all entries either below or above the principal diagonal are zero. There are two types:

A. Upper Triangular Matrix:

All elements below the principal diagonal are zero.

$$(a_{ij} = 0 \quad \text{for all} \quad i > j)$$

$$U = \begin{bmatrix} 1 & 5 & 6 \\ 0 & 2 & 8 \\ 0 & 0 & 3 \end{bmatrix}$$

B. Lower Triangular Matrix:

All elements above the principal diagonal are zero.

$$(a_{ij} = 0 \quad \text{for all} \quad i < j)$$

$$L = \begin{bmatrix} 1 & 0 & 0 \\ 4 & 2 & 0 \\ 7 & 9 & 3 \end{bmatrix}$$

---

### 6. Symmetric Matrix

Definition:

A square matrix is symmetric if it is equal to its transpose. Visually, the matrix is a "mirror image" across the principal diagonal.

Mathematical Condition:

$$A = A^T$$

Or, element-wise:

$$a_{ij} = a_{ji} \quad \text{for all } i, j$$

Example:

Note how the 7s match and the 4s match across the diagonal.

$$A = \begin{bmatrix} 1 & \mathbf{7} & \mathbf{4} \\ \mathbf{7} & 2 & \mathbf{0} \\ \mathbf{4} & \mathbf{0} & 5 \end{bmatrix}$$

---

### 7. Transposed Matrix (Transpose of a Matrix)

![[Pasted image 20251125160049.png]]

Example:

If:

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$$

Then $A^T$ is:

$$A^T = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$$

---

### Summary Table for Quick Revision

|**Matrix Type**|**Key Characteristic**|
|---|---|
|**Diagonal**|Non-diagonal elements are 0.|
|**Scalar**|Diagonal elements are equal; others are 0.|
|**Unit**|Diagonal elements are exactly 1; others are 0.|
|**Incidence**|Maps connections between graph vertices and edges.|
|**Triangular**|Zeros strictly above (Lower) or below (Upper) the diagonal.|
|**Symmetric**|$A = A^T$ (Mirror image across diagonal).|
|**Transpose**|Rows become columns ($A \to A^T$).|

---

Matrix Addition: ![[Pasted image 20251124194433.png]]
Matrix addition obeys the following laws.

**1.** The commutative law:
$$A + B = B + A.$$

**2.** The associative law:
$$A + (B + C) = (A + B) + C.$$

**3.** The distributive law for scalar multiplication:
$$k(A + B) = kA + kB$$
Matrix Multiplication: 
![[Pasted image 20251124195012.png]]
**1.** The associative law:
$$A(BC)=(AB)C$$
**2.** The distributive law: 
$$A(B+C)=AB+AC$$
**3.** The anticommutative law:
$$AB\neq BA$$$$(AB)^r \neq A^rB^r$$

**4.** The distributive law for scalar multiplication:
$$(K_1+K_2)A=K_1A+K_2A=A(K1+K2)$$

 ![[Pasted image 20251125160945.png]]
 Proof:![[Pasted image 20251125161506.png]]![[Pasted image 20251125161000.png]]Proof:![[Pasted image 20251125161524.png]]![[Pasted image 20251125161025.png]]
  Proof: Let $C = AB$. The $(i, j) _{th}$ element of $C$ is

$$c_{ij} = \sum_{r=1}^{n} a_{ir} b_{rj}$$

from Equation (3.15). Also, the element in the $j_{th}$ row and $i_{th}$ column of $B^T A^T$ is observed to be

$$c_{ji} = \sum_{r=1}^{n} a_{jr} b_{ri}$$

which is also the $j, i$th element of $C^T$, so that $(AB)^T = C^T = B^T A^T$.

---
### Basic Idea of Kronecker and Hadamard Product:

#### 1. Hadamard Product (Element-wise)

Symbol: 1$A \circ B$ (or 2$A \odot B$)3

Condition: 4$A$ and 5$B$ must have the same dimensions.6

Definition:

Simply multiply corresponding entries.7

$$(A \circ B)_{ij} = A_{ij} \cdot B_{ij}$$

Example:

Let $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ and $B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$.

$$A \circ B = \begin{bmatrix} 1\cdot5 & 2\cdot6 \\ 3\cdot7 & 4\cdot8 \end{bmatrix} = \begin{bmatrix} 5 & 12 \\ 21 & 32 \end{bmatrix}$$

---

#### 2. Kronecker Product

Symbol: $A \otimes B$

Condition: Can be done with matrices of any size.

Result Size: If 8$A$ is 9$m \times n$ and 10$B$ is 11$p \times q$, the result is 12$mp \times nq$.13

Definition:

Multiply every single element of $A$ by the entire matrix $B$.

$$A \otimes B = \begin{bmatrix} a_{11}B & \dots & a_{1n}B \\ \vdots & \ddots & \vdots \\ a_{m1}B & \dots & a_{mn}B \end{bmatrix}$$

Example:

Let $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ and $B = \begin{bmatrix} 0 & 5 \\ 1 & 1 \end{bmatrix}$.

$$A \otimes B = \begin{bmatrix} 1 \cdot \begin{bmatrix} 0 & 5 \\ 1 & 1 \end{bmatrix} & 2 \cdot \begin{bmatrix} 0 & 5 \\ 1 & 1 \end{bmatrix} \\ 3 \cdot \begin{bmatrix} 0 & 5 \\ 1 & 1 \end{bmatrix} & 4 \cdot \begin{bmatrix} 0 & 5 \\ 1 & 1 \end{bmatrix} \end{bmatrix}$$

$$= \begin{bmatrix} 0 & 5 & 0 & 10 \\ 1 & 1 & 2 & 2 \\ 0 & 15 & 0 & 20 \\ 3 & 3 & 4 & 4 \end{bmatrix}$$

### Summary of Differences

|**Feature**|**Hadamard (A∘B)**|**Kronecker (A⊗B)**|
|---|---|---|
|**Dimensions**|Must match ($m \times n$ and $m \times n$)|Arbitrary ($m \times n$ and $p \times q$)|
|**Result Size**|Same as inputs ($m \times n$)|Huge ($mp \times nq$)|
|**Commutative?**|**Yes** ($A \circ B = B \circ A$)|**No** ($A \otimes B \neq B \otimes A$)|

---

## Key properties of the Kronecker Product:

1. The anticommutative law:

$$A \otimes B \neq B \otimes A$$

2. Let $A, B, C,$ and $D$ be matrices such that the products  $AC$ and $BD$ exist. Then

$$(A \otimes B)(C \otimes D) = AC \otimes BD$$

3. The associative law:

$$A \otimes (B \otimes C) = (A \otimes B) \otimes C$$

4. Transpose Property

$$(A \otimes B)^T = A^T \otimes B^T$$

5. Let $A, B, C,$ and $D$ be conformable for addition. Then

$$(A + B) \otimes (C + D) = (A \otimes C) + (A \otimes D) + (B \otimes C) + (B \otimes D)$$

6. Let $A$ be an $n \times k$ matrix. Then the Kronecker power is defined as

$$A^{(2)} = A \otimes A,$$

$$A^{(r+1)} = A \otimes A^{(r)}, \quad r = 2, 3, \dots$$

Also, it can be shown that

$$(AB)^{(r)} = A^{(r)} B^{(r)}.$$

---
determinant $|\mathbf{A}|$, when expanding by elements of a row

$$|\mathbf{A}| = \sum_{j=1}^{n} a_{ij}(-1)^{i+j}|\mathbf{M}_{ij}| \quad \text{for any } i,$$

and when expanding by elements of a column

$$|\mathbf{A}| = \sum_{i=1}^{n} a_{ij}(-1)^{i+j}|\mathbf{M}_{ij}| \quad \text{for any } j.$$

---
Determinant of a Transpose:
![[Pasted image 20251125165702.png]]
Proof: 
Let $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$.

- The determinant is: **$|A| = ad - bc$**.
    

Now, take the transpose $A^T$ (rows become columns):

$A^T = \begin{bmatrix} a & c \\ b & d \end{bmatrix}$.

- The determinant is: **$|A^T| = ad - cb$**.
    

Since $bc = cb$, $|A| = |A^T|$.

 ---
 ![[Pasted image 20251125171355.png]]


---
Two Rows The Same:![[Pasted image 20251125171902.png]]
Proof:
Let $M$ be a $2 \times 2$ matrix with identical rows:

$$M = \begin{bmatrix} a & b \\ a & b \end{bmatrix}$$

Using the definition of a determinant:

$$|M| = (a \cdot b) - (a \cdot b) = 0$$

