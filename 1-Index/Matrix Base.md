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

Definition:

The transpose of a matrix is formed by interchanging its rows and columns.15 If matrix 16$A$ has dimensions 17$m \times n$, its transpose 18$A^T$ (or 19$A'$) has dimensions 20$n \times m$.21

Mathematical Operation:

The first row of 22$A$ becomes the first column of 23$A^T$.24

The second row of 25$A$ becomes the second column of 26$A^T$.27

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

**Would you like me to generate a few practice problems involving finding the transpose or identifying these matrix types to help you prepare for the exam?**