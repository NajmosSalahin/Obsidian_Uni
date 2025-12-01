Here is the text from the uploaded images, organized by mathematical topic for clarity.

### **1. Sums of Outer Products**

**5.1.4 Sums of Outer Products**

Let $\mathbf{a}_1, \mathbf{a}_2, \dots, \mathbf{a}_c$ be the columns of $\mathbf{A}$, and $\mathbf{\beta}'_1, \mathbf{\beta}'_2, \dots, \mathbf{\beta}'_c$ be the rows of $\mathbf{B}$, then the product $\mathbf{AB}$ expressed as,

$$\mathbf{AB} = [\mathbf{a}_1 \quad \mathbf{a}_2 \dots \mathbf{a}_c] \begin{bmatrix} \mathbf{\beta}'_1 \\ \mathbf{\beta}'_2 \\ \vdots \\ \mathbf{\beta}'_c \end{bmatrix} = \sum_{j=1}^{c} \mathbf{a}_j \mathbf{\beta}'_j,$$

is the sum of outer products of the columns of $\mathbf{A}$ with the corresponding rows in $\mathbf{B}$.

---

### **2. Properties of Inner and Outer Products**

The inner product of two vectors is a scalar and is therefore symmetric: $\mathbf{x}'\mathbf{y} = (\mathbf{x}'\mathbf{y})' = \mathbf{y}'\mathbf{x}$. In contrast, the outer product of two vectors (see Section 4.7.5) is not necessarily symmetric: $\mathbf{xy}' = (\mathbf{yx}')' \neq (\mathbf{xy}')'$. Indeed, such a product is not necessarily even square.

Also, regarding the symmetry of products involving transposes:

$$(\mathbf{AA}')' = (\mathbf{A}')'\mathbf{A}' = \mathbf{AA}' \quad \text{and} \quad (\mathbf{A}'\mathbf{A})' = \mathbf{A}'(\mathbf{A}')' = \mathbf{A}'\mathbf{A}.$$

---

### **3. Skew-Symmetric Matrices**

**5.1.6 Skew-Symmetric Matrices**

A symmetric matrix $\mathbf{A}$ has the property $\mathbf{A} = \mathbf{A}'$; in contrast there are also matrices $\mathbf{B}$ having the property $\mathbf{B}' = -\mathbf{B}$. Their diagonal elements are zero and each off-diagonal element is minus its symmetric partner; that is, $b_{ii} = 0$ and $b_{ij} = -b_{ji}$. An example is

$$\mathbf{B} = \begin{bmatrix} 0 & 1 & -3 \\ -1 & 0 & 2 \\ 3 & -2 & 0 \end{bmatrix}.$$

Such matrices, having $\mathbf{B}' = -\mathbf{B}$, are called _skew-symmetric_.

---

### **4. Idempotent Matrices**

_Note: The following text describes the properties of idempotent matrices._

...matrices are of this nature; they are called idempotent matrices. Thus when $\mathbf{K}$ is such that $\mathbf{K}^2 = \mathbf{K}$, we say $\mathbf{K}$ is _idempotent_ (from Latin, _idem_ meaning “same,” and _potent_ “power”). All idempotent matrices are square (otherwise $\mathbf{K}^2$ does not exist); identity matrices and square null matrices are idempotent. When $\mathbf{K}$ is idempotent, all powers of $\mathbf{K}$ equal $\mathbf{K}$; that is, $\mathbf{K}^r = \mathbf{K}$ for $r$ being a positive integer, and $(\mathbf{I} - \mathbf{K})$ is idempotent. Thus

$$\mathbf{K}^2 = \mathbf{K} \text{ implies } (\mathbf{I} - \mathbf{K})^2 = \mathbf{I} - \mathbf{K},$$

but $\mathbf{K} - \mathbf{I}$ is not idempotent. A product of two idempotent matrices is idempotent if the matrices commute in multiplication.

---

### **5. Nilpotent and Unipotent Matrices**

A matrix $\mathbf{A}$ satisfying $\mathbf{A}^2 = \mathbf{0}$ is called _nilpotent_, and that for which $\mathbf{A}^2 = \mathbf{I}$ could be called _unipotent_.

**Example 5.9**

$$\mathbf{A} = \begin{bmatrix} 1 & 2 & 5 \\ 2 & 4 & 10 \\ -1 & -2 & -5 \end{bmatrix} \text{ is nilpotent;} \quad \mathbf{B} = \begin{bmatrix} \mathbf{I} & \mathbf{X} \\ 0 & -\mathbf{I} \end{bmatrix} \text{ is unipotent.}$$

Variations on these definitions are $\mathbf{A}^k = \mathbf{A}$, $\mathbf{A}^k = \mathbf{0}$, and $\mathbf{A}^k = \mathbf{I}$ for some positive integer $k > 2$. An example is the matrix

$$\mathbf{B} = \begin{bmatrix} 0 & 0 & 6 \\ \frac{1}{2} & 0 & 0 \\ 0 & \frac{1}{3} & 0 \end{bmatrix},$$

for which $\mathbf{B}^3 = \mathbf{I}$, but $\mathbf{B}^2 \neq \mathbf{I}$.

---

### **6. Theorem 5.1: Rank of an Idempotent Matrix**

**Theorem 5.1** _If $\mathbf{K}$ is an $n \times n$ idempotent matrix, then its rank $r$ is equal to its trace, that is, $r = r(\mathbf{K}) = tr(\mathbf{K})$._

_Proof._ Let $l_1, l_2, \dots, l_r$ be linearly independent vectors that span (form a basis for) the column space of $\mathbf{K}$. Let $\mathbf{L} = [l_1 \vdots l_2 \vdots \dots \vdots l_r]$, then $\mathbf{L}$ is of order $n \times r$ and rank $r$. The $i$th column, $k_i$ of $\mathbf{K}$ can then be expressed as a linear combination of the columns of $\mathbf{L}$ ($i = 1, 2, \dots, n$). We can therefore write $k_i = \mathbf{L}m_i$ where $m_i$ is a vector of coefficients consisting of $r$ elements ($i = 1, 2, \dots, n$). Let $\mathbf{M}$ be a matrix of order $r \times n$ whose columns are $m_1, m_2, \dots, m_n$. Thus $\mathbf{K}$ can be written as

$$\mathbf{K} = \mathbf{LM}. \tag{5.20}$$

It follows that $r(\mathbf{K}) \leq r(\mathbf{M}) \leq r$, since the rank of $\mathbf{M}$ cannot exceed the number of its rows. But, $r(\mathbf{K}) = r$. We conclude that $r(\mathbf{M}) = r$.

Since $\mathbf{K}$ is idempotent, $\mathbf{K}^2 = \mathbf{K}$. We then have from (5.20),

$$\mathbf{LMLM} = \mathbf{LM}. \tag{5.21}$$

Furthermore, because $\mathbf{L}$ is of full-column rank, multiplying both sides of (5.21) on the left by $\mathbf{L}'$ and noting that $\mathbf{L}'\mathbf{L}$ is nonsingular by the fact that it is of order $r \times r$ of rank $r$, we get, after multiplying both of the resulting sides of (5.21) on the left by the inverse of $\mathbf{L}'\mathbf{L}$,

$$\mathbf{MLM} = \mathbf{M}. \tag{5.22}$$

Similarly, $\mathbf{M}$ being of full-row rank, the matrix $\mathbf{MM}'$ is nonsingular. Multiplying the two sides of (5.22) on the right by $\mathbf{M}'$ and then multiplying the resulting equation on the right by the inverse of $\mathbf{MM}'$, we get

$$\mathbf{ML} = \mathbf{I}_r. \tag{5.23}$$

It follows from (5.20) and (5.23) that $r(\mathbf{K}) = r = tr(\mathbf{ML}) = tr(\mathbf{LM}) = tr(\mathbf{K})$. Thus, $r(\mathbf{K}) = tr(\mathbf{K})$.

Since the trace of $\mathbf{K}$, being the sum of its diagonal elements, is easy to compute, this theorem facilitates the finding of the rank of $\mathbf{K}$, which, in general, is more difficult to determine, when $\mathbf{K}$ is idempotent.

---

### **7. Orthogonal Matrices and Vector Norms**

**Definition 5.2** Another useful class of matrices is that for which $\mathbf{A}$ has the property $\mathbf{AA}' = \mathbf{I} = \mathbf{A}'\mathbf{A}$. Such matrices are called _orthogonal_. We lead up to them with the following definitions:

The _norm_ of a real vector $\mathbf{x}' = [x_1 \quad x_2 \quad \dots \quad x_n]$ is defined as

$$\text{norm of } \mathbf{x} = \sqrt{\mathbf{x}'\mathbf{x}} = \left( \sum_{i=1}^{n} x_i^2 \right)^{\frac{1}{2}} \tag{5.24}$$

For example, the norm of $\mathbf{x}' = [1 \quad 2 \quad 2 \quad 4]$ is $(1 + 4 + 4 + 16)^{\frac{1}{2}} = 5$. (The square root is taken as positive.) A vector is said to be either _normal_ or a _unit vector_ when its norm is unity; that is, when $\mathbf{x}'\mathbf{x} = 1$. An example is $\mathbf{x}' = [.2 \quad .4 \quad .4 \quad .8]$. Any non-null vector $\mathbf{x}$ can be changed into a unit vector by multiplying it by the scalar $1 / \sqrt{\mathbf{x}'\mathbf{x}}$; that is,

$$\mathbf{u} = \left( \frac{1}{\sqrt{\mathbf{x}'\mathbf{x}}} \right) \mathbf{x}$$

is the _normalized_ form of $\mathbf{x}$ (because $\mathbf{u}'\mathbf{u} = 1$).
