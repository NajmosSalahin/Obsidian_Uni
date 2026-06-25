## Chapter 5: Linear Mappings

### 5.1 Introduction

The main subject matter of linear algebra is the study of linear mappings and their representation by means of matrices. This chapter introduces us to these linear maps and Chapter 6 shows how they can be represented by matrices. First, however, we begin with a study of mappings in general.

---

### 5.2 Mappings, Functions

Let $A$ and $B$ be arbitrary nonempty sets. Suppose to each element $a \in A$ there is assigned a unique element of $B$, called the *image* of $a$. The collection $f$ of such assignments is called a *mapping* (or map) from $A$ into $B$, and it is denoted by

$$f: A \to B$$

The set $A$ is called the *domain* of the mapping, and $B$ is called the *target set*. We write $f(a)$, read "$f$ of $a$," for the unique element of $B$ that $f$ assigns to $a \in A$.

One may also view a mapping $f: A \to B$ as a computer that, for each input value $a \in A$, produces a unique output $f(a) \in B$.

> **Remark:** The term *function* is used synonymously with the word *mapping*, although some texts reserve the word "function" for a real-valued or complex-valued mapping.

Consider a mapping $f: A \to B$. If $A'$ is any subset of $A$, then $f(A')$ denotes the set of images of elements of $A'$; and if $B'$ is any subset of $B$, then $f^{-1}(B')$ denotes the set of elements of $A$, each of whose image lies in $B'$. That is,

$$f(A') = \{f(a) : a \in A'\} \qquad \text{and} \qquad f^{-1}(B') = \{a \in A : f(a) \in B'\}$$

We call $f(A')$ the *image* of $A'$ and $f^{-1}(B')$ the *inverse image* or *preimage* of $B'$. In particular, the set of all images (i.e., $f(A)$) is called the image or *range* of $f$.

To each mapping $f: A \to B$ there corresponds the subset of $A \times B$ given by $\{(a, f(a)) : a \in A\}$. We call this set the *graph* of $f$. Two mappings $f: A \to B$ and $g: A \to B$ are defined to be *equal*, written $f = g$, if $f(a) = g(a) for every $a \in A$—that is, if they have the same graph. Thus, we do not distinguish between a function and its graph. The negation of $f = g$ is written $f \neq g$ and is the statement:

$$\boxed{\text{There exists an } a \in A \text{ for which } f(a) \neq g(a).}$$

Sometimes the "barred" arrow ($\mapsto$) is used to denote the image of an arbitrary element $x \in A$ under a mapping $f: A \to B$ by writing

$$x \mapsto f(x)$$

This is illustrated in the following examples.

**Example 5.1:**

* Let $f: \mathbf{R} \to \mathbf{R}$ be the function that assigns to each real number $x$ its square $x^2$. We can denote this function by writing

$$f(x) = x^2 \qquad \text{or} \qquad x \mapsto x^2$$



Here the image of $-3$ is $9$, so we may write $f(-3) = 9$. However, $f^{-1}(9) = \{3, -3\}$. Also, $f(\mathbf{R}) = [0, \infty) = \{x : x \geq 0\}$ is the image of $f$.
* Let $A = \{a, b, c, d\}$ and $B = \{x, y, z, t\}$. Then the following defines a mapping $f: A \to B$:

$$f(a)=y, \quad f(b)=x, \quad f(c)=z, \quad f(d)=y \qquad \text{or} \qquad f = \{(a,y), (b,x), (c,z), (d,y)\}$$



The first defines the mapping explicitly, and the second defines the mapping by its graph. Here,

$$f(\{a, b, d\}) = \{f(a), f(b), f(d)\} = \{y, x, y\} = \{x, y\}$$



Furthermore, $f(A) = \{x, y, z\}$ is the image of $f$.

**Example 5.2:** Let $V$ be the vector space of polynomials over $\mathbf{R}$, and let $p(t) = 3t^2 - 5t + 2$.

* The derivative defines a mapping $\mathbf{D}: V \to V$ where, for any polynomial $f(t)$, we have $\mathbf{D}(f) = \frac{df}{dt}$. Thus, $\mathbf{D}(p) = \mathbf{D}(3t^2 - 5t + 2) = 6t - 5$.
* The integral from $0$ to $1$ defines a mapping $\mathbf{J}: V \to \mathbf{R}$. That is, for any polynomial $f(t)$,

$$\mathbf{J}(f) = \int_{0}^{1} f(t) \, dt, \qquad \text{and so} \qquad \mathbf{J}(p) = \int_{0}^{1} (3t^2 - 5t + 2) \, dt = \frac{1}{2}$$



Observe that the mapping in the second case is from the vector space $V$ into the scalar field $\mathbf{R}$, whereas the mapping in the first case is from the vector space $V$ into itself.

### Matrix Mappings

Let $A$ be any $m \times n$ matrix over $K$. Then $A$ determines a mapping $F_A: K^n \to K^m$ by

$$F_A(u) = Au$$

where the vectors in $K^n$ and $K^m$ are written as columns. For example, suppose

$$A = \begin{bmatrix} 1 & -4 & 5 \\ 2 & 3 & -6 \end{bmatrix} \qquad \text{and} \qquad u = \begin{bmatrix} 1 \\ 3 \\ -5 \end{bmatrix}$$

then

$$F_A(u) = Au = \begin{bmatrix} 1 & -4 & 5 \\ 2 & 3 & -6 \end{bmatrix} \begin{bmatrix} 1 \\ 3 \\ -5 \end{bmatrix} = \begin{bmatrix} -36 \\ 41 \end{bmatrix}$$

> **Remark:** For notational convenience, we will frequently denote the mapping $F_A$ by the letter $A$, the same symbol as used for the matrix.

### Composition of Mappings

Consider two mappings $f: A \to B$ and $g: B \to C$, illustrated below:

$$A \xrightarrow{\quad f \quad} B \xrightarrow{\quad g \quad} C$$

The *composition* of $f$ and $g$, denoted by $g \circ f$, is the mapping $g \circ f: A \to C$ defined by

$$(g \circ f)(a) \equiv g(f(a))$$

That is, first we apply $f$ to $a \in A$, and then we apply $g$ to $f(a) \in B$ to get $g(f(a)) \in C$. Viewing $f$ and $g$ as "computers," the composition means we first input $a \in A$ to get the output $f(a) \in B$ using $f$, and then we input $f(a)$ to get the output $g(f(a)) \in C$ using $g$.

Our first theorem tells us that the composition of mappings satisfies the associative law.

**Theorem 5.1:** *Let $f: A \to B$, $g: B \to C$, and $h: C \to D$. Then*

$$h \circ (g \circ f) = (h \circ g) \circ f$$

*Proof:* Let $a \in A$. Then


$$(h \circ (g \circ f))(a) = h((g \circ f)(a)) = h(g(f(a)))$$

$$((h \circ g) \circ f)(a) = (h \circ g)(f(a)) = h(g(f(a)))$$


*Thus, $(h \circ (g \circ f))(a) = ((h \circ g) \circ f)(a)$ for every $a \in A$, and so $h \circ (g \circ f) = (h \circ g) \circ f$.* $\blacksquare$

#### One-to-One and Onto Mappings

We formally introduce some special types of mappings.

* **Definition:** A mapping $f: A \to B$ is said to be *one-to-one* (or $1\text{-}1$ or *injective*) if different elements of $A$ have distinct images; that is,

$$\text{If } f(a) = f(a'), \text{ then } a = a'.$$


* **Definition:** A mapping $f: A \to B$ is said to be *onto* (or $f$ maps $A$ onto $B$ or *surjective*) if every $b \in B$ is the image of at least one $a \in A$.
* **Definition:** A mapping $f: A \to B$ is said to be a *one-to-one correspondence* between $A$ and $B$ (or *bijective*) if $f$ is both one-to-one and onto.

**Example 5.3:** Let $f: \mathbf{R} \to \mathbf{R}$, $g: \mathbf{R} \to \mathbf{R}$, and $h: \mathbf{R} \to \mathbf{R}$ be defined by

$$f(x) = 2^x, \qquad g(x) = x^3 - x, \qquad h(x) = x^2$$

The function $f$ is one-to-one. Geometrically, this means that each horizontal line does not contain more than one point of the graph of $f$. The function $g$ is onto. Geometrically, this means that each horizontal line contains at least one point of the graph of $g$. The function $h$ is neither one-to-one nor onto. For example, both $2$ and $-2$ have the same image $4$, and $-16$ has no preimage.

### Identity and Inverse Mappings

Let $A$ be any nonempty set. The mapping $f: A \to A$ defined by $f(a) = a$—that is, the function that assigns to each element in $A$ itself—is called the *identity mapping*. It is usually denoted by $\mathbf{1}_A$, $\mathbf{1}$, or $I$. Thus, for any $a \in A$, we have $\mathbf{1}_A(a) = a$.

Now let $f: A \to B$. We call $g: B \to A$ the inverse of $f$, written $f^{-1}$, if

$$f \circ g = \mathbf{1}_B \qquad \text{and} \qquad g \circ f = \mathbf{1}_A$$

We emphasize that $f$ has an inverse if and only if $f$ is a one-to-one correspondence between $A$ and $B$ (i.e., bijective). Also, if $b \in B$, then $f^{-1}(b) = a$, where $a$ is the unique element of $A$ for which $f(a) = b$.

---

### 5.3 Linear Mappings (Linear Transformations)

We begin with a definition.

**Definition:** Let $V$ and $U$ be vector spaces over the same field $K$. A mapping $F: V \to U$ is called a *linear mapping* or *linear transformation* if it satisfies the following two conditions:

$$\begin{aligned}
(1) \quad &\text{For any vectors } v, w \in V, &F(v + w) &= F(v) + F(w). \\
(2) \quad &\text{For any scalar } k \text{ and vector } v \in V, &F(kv) &= kF(v).
\end{aligned}$$

Namely, $F: V \to U$ is linear if it "preserves" the two basic operations of a vector space: vector addition and scalar multiplication.

Substituting $k = 0$ into condition (2), we obtain $F(0) = 0$. Thus, every linear mapping takes the zero vector into the zero vector.

Now for any scalars $a, b \in K$ and any vectors $v, w \in V$, we obtain

$$F(av + bw) = F(av) + F(bw) = aF(v) + bF(w)$$

More generally, for any scalars $a_i \in K$ and any vectors $v_i \in V$, we obtain the following basic property of linear mappings:

$$F(a_1v_1 + a_2v_2 + \dots + a_mv_m) = a_1F(v_1) + a_2F(v_2) + \dots + a_mF(v_m)$$

> **Remark 1:** A linear mapping $F: V \to U$ is completely characterized by the condition
> 
> $$F(av + bw) = aF(v) + bF(w) \qquad (*)$$
> 
> 
> 
> and so this condition is sometimes used as its definition.
> **Remark 2:** The term *linear transformation* rather than *linear mapping* is frequently used for linear mappings of the form $F: \mathbf{R}^n \to \mathbf{R}^m$.

**Example 5.4:**

1. Let $F: \mathbf{R}^3 \to \mathbf{R}^3$ be the "projection" mapping into the $xy$-plane; that is, $F$ is the mapping defined by $F(x,y,z) = (x,y,0)$. We show that $F$ is linear. Let $v = (a,b,c)$ and $w = (a',b',c')$. Then

$$F(v+w) = F(a+a', \, b+b', \, c+c') = (a+a', \, b+b', \, 0) = (a,b,0) + (a',b',0) = F(v) + F(w)$$



and, for any scalar $k$,

$$F(kv) = F(ka, kb, kc) = (ka, kb, 0) = k(a, b, 0) = kF(v)$$



Thus, $F$ is linear.
2. Let $G: \mathbf{R}^2 \to \mathbf{R}^2$ be the "translation" mapping defined by $G(x,y) = (x+1, y+2)$. Note that

$$G(0) = G(0,0) = (1,2) \neq 0$$



Thus, the zero vector is not mapped into the zero vector. Hence, $G$ is not linear.

**Example 5.5 (Derivative and Integral Mappings):** Consider the vector space $V = \mathbf{P}(t)$ of polynomials over the real field $\mathbf{R}$. Let $u(t)$ and $v(t)$ be any polynomials in $V$ and let $k$ be any scalar.

1. Let $\mathbf{D}: V \to V$ be the derivative mapping. One proves in calculus that

$$\frac{d(u+v)}{dt} = \frac{du}{dt} + \frac{dv}{dt} \qquad \text{and} \qquad \frac{d(ku)}{dt} = k \frac{du}{dt}$$



That is, $\mathbf{D}(u+v) = \mathbf{D}(u) + \mathbf{D}(v)$ and $\mathbf{D}(ku) = k\mathbf{D}(u)$. Thus, the derivative mapping is linear.
2. Let $\mathbf{J}: V \to \mathbf{R}$ be an integral mapping, say $\mathbf{J}(f(t)) = \int_{0}^{1} f(t) \, dt$. One also proves in calculus that

$$\int_{0}^{1} [u(t) + v(t)] \, dt = \int_{0}^{1} u(t) \, dt + \int_{0}^{1} v(t) \, dt \qquad \text{and} \qquad \int_{0}^{1} ku(t) \, dt = k \int_{0}^{1} u(t) \, dt$$



That is, $\mathbf{J}(u+v) = \mathbf{J}(u) + \mathbf{J}(v)$ and $\mathbf{J}(ku) = k\mathbf{J}(u)$. Thus, the integral mapping is linear.

**Example 5.6 (Zero and Identity Mappings):**

1. Let $F: V \to U$ be the mapping that assigns the zero vector $0 \in U$ to every vector $v \in V$. Then, for any vectors $v, w \in V$ and any scalar $k \in K$, we have

$$F(v+w) = 0 = 0+0 = F(v)+F(w) \qquad \text{and} \qquad F(kv) = 0 = k0 = kF(v)$$



Thus, $F$ is linear. We call $F$ the *zero mapping*, and we usually denote it by $0$.
2. Consider the identity mapping $I: V \to V$, which maps each $v \in V$ into itself. Then, for any vectors $v, w \in V$ and any scalars $a, b \in K$, we have

$$I(av+bw) = av+bw = aI(v)+bI(w)$$



Thus, $I$ is linear.

Our next theorem gives us an abundance of examples of linear mappings. In particular, it tells us that a linear mapping is completely determined by its values on the elements of a basis.

**Theorem 5.2:** *Let $V$ and $U$ be vector spaces over a field $K$. Let $\{v_1, v_2, \dots, v_n\}$ be a basis of $V$ and let $u_1, u_2, \dots, u_n$ be any vectors in $U$. Then there exists a unique linear mapping $F: V \to U$ such that $F(v_1) = u_1, F(v_2) = u_2, \dots, F(v_n) = u_n$.*

We emphasize that the vectors $u_1, u_2, \dots, u_n$ in Theorem 5.2 are completely arbitrary; they may be linearly dependent or they may even be equal to each other.

### Matrices as Linear Mappings

Let $A$ be any real $m \times n$ matrix. Recall that $A$ determines a mapping $F_A: K^n \to K^m$ by $F_A(u) = Au$ (where the vectors in $K^n$ and $K^m$ are written as columns). We show $F_A$ is linear. By matrix multiplication,

$$F_A(v+w) = A(v+w) = Av+Aw = F_A(v)+F_A(w)$$

$$F_A(kv) = A(kv) = k(Av) = kF_A(v)$$

In other words, using $A$ to represent the mapping, we have

$$A(v+w) = Av+Aw \qquad \text{and} \qquad A(kv) = k(Av)$$

Thus, the matrix mapping $A$ is linear.

### Vector Space Isomorphism

The notion of two vector spaces being isomorphic was defined in Chapter 4 when we investigated the coordinates of a vector relative to a basis. We now redefine this concept.

**Definition:** Two vector spaces $V$ and $U$ over $K$ are *isomorphic*, written $V \cong U$, if there exists a bijective (one-to-one and onto) linear mapping $F: V \to U$. The mapping $F$ is then called an *isomorphism* between $V$ and $U$.

Consider any vector space $V$ of dimension $n$ and let $S$ be any basis of $V$. Then the mapping

$$v \mapsto [v]_S$$

which maps each vector $v \in V$ into its coordinate vector $[v]_S$, is an isomorphism between $V$ and $K^n$.

### Kernel and Image of a Linear Mapping

We begin by defining two concepts.

**Definition:** Let $F: V \to U$ be a linear mapping. The *kernel* of $F$, written $\operatorname{Ker} F$, is the set of elements in $V$ that map into the zero vector $0$ in $U$; that is,

$$\operatorname{Ker} F = \{v \in V : F(v) = 0\}$$

The *image* (or *range*) of $F$, written $\operatorname{Im} F$, is the set of image points in $U$; that is,

$$\operatorname{Im} F = \{u \in U : \text{there exists } v \in V \text{ for which } F(v) = u\}$$

**Theorem 5.3:** *Let $F: V \to U$ be a linear mapping. Then the kernel of $F$ is a subspace of $V$ and the image of $F$ is a subspace of $U$.*

Now suppose that $v_1, v_2, \dots, v_m$ span a vector space $V$ and that $F: V \to U$ is linear. We show that $F(v_1), F(v_2), \dots, F(v_m)$ span $\operatorname{Im} F$. Let $u \in \operatorname{Im} F$. Then there exists $v \in V$ such that $F(v) = u$. Because the vectors $v_i$ span $V$ and $v \in V$, there exist scalars $a_1, a_2, \dots, a_m$ for which

$$v = a_1v_1 + a_2v_2 + \dots + a_mv_m$$

Therefore,

$$u = F(v) = F(a_1v_1 + a_2v_2 + \dots + a_mv_m) = a_1F(v_1) + a_2F(v_2) + \dots + a_mF(v_m)$$

Thus, the vectors $F(v_1), F(v_2), \dots, F(v_m)$ span $\operatorname{Im} F$.

We formally state the above result.

**Proposition 5.4:** *Suppose $v_1, v_2, \dots, v_m$ span a vector space $V$, and suppose $F: V \to U$ is linear. Then $F(v_1), F(v_2), \dots, F(v_m)$ span $\operatorname{Im} F$.*

**Example 5.7:**

1. Let $F: \mathbf{R}^3 \to \mathbf{R}^3$ be the projection of a vector $v$ into the $xy$-plane; that is, $F(x,y,z) = (x,y,0)$. Clearly the image of $F$ is the entire $xy$-plane—that is, points of the form $(x,y,0)$. Moreover, the kernel of $F$ is the $z$-axis—that is, points of the form $(0,0,c)$. That is,

$$\operatorname{Im} F = \{(a,b,c) : c=0\} = \text{xy-plane} \qquad \text{and} \qquad \operatorname{Ker} F = \{(a,b,c) : a=0, b=0\} = \text{z-axis}$$


2. Let $G: \mathbf{R}^3 \to \mathbf{R}^3$ be the linear mapping that rotates a vector $v$ about the $z$-axis through an angle $\theta$; that is,

$$G(x,y,z) = (x\cos\theta - y\sin\theta, \quad x\sin\theta + y\cos\theta, \quad z)$$



Observe that the distance of a vector $v$ from the origin $O$ does not change under the rotation, and so only the zero vector $0$ is mapped into the zero vector $0$. Thus, $\operatorname{Ker} G = \{0\}$. On the other hand, every vector $u$ in $\mathbf{R}^3$ is the image of a vector $v$ in $\mathbf{R}^3$ that can be obtained by rotating $u$ back by an angle of $\theta$. Thus, $\operatorname{Im} G = \mathbf{R}^3$, the entire space.

**Example 5.8:** Consider the vector space $V = \mathbf{P}(t)$ of polynomials over the real field $\mathbf{R}$, and let $H: V \to V$ be the third-derivative operator; that is, $H[f(t)] = \frac{d^3f}{dt^3}$. We claim that

$$\operatorname{Ker} H = \{\text{polynomials of degree } \leq 2\} = \mathbf{P}_2(t) \qquad \text{and} \qquad \operatorname{Im} H = V$$

The first statement comes from the fact that $H(at^2+bt+c) = 0$ but $H(t^\alpha) \neq 0$ for $n \geq 3$. The second comes from the fact that every polynomial $g(t)$ in $V$ is the third derivative of some polynomial $f(t)$ (which can be obtained by taking the antiderivative of $g(t)$ three times).

### Kernel and Image of Matrix Mappings

Consider a $3 \times 4$ matrix $A$ and the standard basis $\{e_1, e_2, e_3, e_4\}$ of $K^4$ written as columns:

$$A = \begin{bmatrix} a_1 & a_2 & a_3 & a_4 \\ b_1 & b_2 & b_3 & b_4 \\ c_1 & c_2 & c_3 & c_4 \end{bmatrix}, \quad e_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}, \quad e_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \quad e_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}, \quad e_4 = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}$$

Recall that $A$ may be viewed as a linear mapping $A: K^4 \to K^3$, where vectors are viewed as column vectors. The standard basis vectors span $K^4$, so their images $Ae_1, Ae_2, Ae_3, Ae_4$ span the image of $A$. But these images are precisely the columns of $A$:

$$Ae_1 = [a_1, b_1, c_1]^T, \quad Ae_2 = [a_2, b_2, c_2]^T, \quad Ae_3 = [a_3, b_3, c_3]^T, \quad Ae_4 = [a_4, b_4, c_4]^T$$

Thus, the image of $A$ is precisely the column space of $A$.

On the other hand, the kernel of $A$ consists of all vectors $v$ for which $Av = 0$. This means that the kernel of $A$ is the solution space of the homogeneous system $AX = 0$, called the *null space* of $A$.

We state the above results formally.

**Proposition 5.5:** *Let $A$ be any $m \times n$ matrix over a field $K$ viewed as a linear map $A: K^n \to K^m$. Then*

$$\operatorname{Ker} A = \operatorname{nullsp}(A) \qquad \text{and} \qquad \operatorname{Im} A = \operatorname{colsp}(A)$$

Here $\operatorname{colsp}(A)$ denotes the column space of $A$, and $\operatorname{nullsp}(A)$ denotes the null space of $A$.

### Rank and Nullity of a Linear Mapping

Let $F: V \to U$ be a linear mapping. The *rank* of $F$ is defined to be the dimension of its image, and the *nullity* of $F$ is defined to be the dimension of its kernel; namely,

$$\operatorname{rank}(F) = \dim(\operatorname{Im} F) \qquad \text{and} \qquad \operatorname{nullity}(F) = \dim(\operatorname{Ker} F)$$

The following important theorem holds.

**Theorem 5.6:** *Let $V$ be of finite dimension, and let $F: V \to U$ be linear. Then*

$$\dim V = \dim(\operatorname{Ker} F) + \dim(\operatorname{Im} F) = \operatorname{nullity}(F) + \operatorname{rank}(F)$$

Recall that the rank of a matrix $A$ was also defined to be the dimension of its column space and row space. If we now view $A$ as a linear mapping, then both definitions correspond because the image of $A$ is precisely its column space.

**Example 5.9:** Let $F: \mathbf{R}^4 \to \mathbf{R}^3$ be the linear mapping defined by

$$F(x,y,z,t) = (x-y+z+t, \quad 2x-2y+3z+4t, \quad 3x-3y+4z+5t)$$

1. **Find a basis and the dimension of the image of $F$:**
First, find the image of the usual basis vectors of $\mathbf{R}^4$:

$$\begin{aligned}
F(1,0,0,0) &= (1,2,3), & F(0,1,0,0) &= (-1,-2,-3) \\
F(0,0,1,0) &= (1,3,4), & F(0,0,0,1) &= (1,4,5)
\end{aligned}$$



By Proposition 5.4, these image vectors span $\operatorname{Im} F$. Hence, form the matrix $M$ whose rows are these image vectors and row reduce to echelon form:

$$M = \begin{bmatrix} 1 & 2 & 3 \\ -1 & -2 & -3 \\ 1 & 3 & 4 \\ 1 & 4 & 5 \end{bmatrix} \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 2 & 2 \end{bmatrix} \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$



Thus, $(1,2,3)$ and $(0,1,1)$ form a basis of $\operatorname{Im} F$. Hence, $\dim(\operatorname{Im} F) = 2$ and $\operatorname{rank}(F) = 2$.
2. **Find a basis and the dimension of the kernel of the map $F$:**
Set $F(v) = 0$, where $v = (x,y,z,t)$:

$$F(x,y,z,t) = (x-y+z+t, \quad 2x-2y+3z+4t, \quad 3x-3y+4z+5t) = (0,0,0)$$



Set corresponding components equal to each other to form the following homogeneous system whose solution space is $\operatorname{Ker} F$:

$$\begin{aligned}
x - y + z + t &= 0 \\
2x - 2y + 3z + 4t &= 0 \\
3x - 3y + 4z + 5t &= 0
\end{aligned}
\qquad \implies \qquad
\begin{aligned}
x - y + z + t &= 0 \\
z + 2t &= 0 \\
0 &= 0
\end{aligned}$$



The free variables are $y$ and $t$. Hence, $\dim(\operatorname{Ker} F) = 2$ or $\operatorname{nullity}(F) = 2$.
* Set $y = 1, t = 0$ to obtain the solution $(-1,1,0,0)$,
* Set $y = 0, t = 1$ to obtain the solution $(1,0,-2,1)$.


Thus, $(-1,1,0,0)$ and $(1,0,-2,1)$ form a basis for $\operatorname{Ker} F$.
As expected from Theorem 5.6, $\dim(\operatorname{Im} F) + \dim(\operatorname{Ker} F) = 2 + 2 = 4 = \dim \mathbf{R}^4$.

### Application to Systems of Linear Equations

Let $AX = B$ denote the matrix form of a system of $m$ linear equations in $n$ unknowns. Now the matrix $A$ may be viewed as a linear mapping $A: K^n \to K^m$. Thus, the solution of the equation $AX = B$ may be viewed as the preimage of the vector $B \in K^m$ under the linear mapping $A$. Furthermore, the solution of the associated homogeneous system $AX = 0$ may be viewed as the kernel of the linear mapping $A$. Applying Theorem 5.6 to this homogeneous system yields

$$\dim(\operatorname{Ker} A) = \dim K^n - \dim(\operatorname{Im} A) = n - \operatorname{rank} A$$

But $n$ is exactly the number of unknowns in the homogeneous system $AX = 0$. Thus, we have proved the following theorem from Chapter 4.

**Theorem 4.19:** *The dimension of the solution space $W$ of a homogeneous system $AX = 0$ of linear equations is $s = n - r$, where $n$ is the number of unknowns and $r$ is the rank of the coefficient matrix $A$.*

Observe that $r$ is also the number of pivot variables in an echelon form of $AX = 0$, so $s = n - r$ is also the number of free variables. Furthermore, the $s$ solution vectors of $AX = 0$ described in Theorem 3.14 are linearly independent. Accordingly, because $\dim W = s$, they form a basis for the solution space $W$. Thus, we have also proved Theorem 3.14.

---

### 5.5 Singular and Nonsingular Linear Mappings, Isomorphisms

Let $F: V \to U$ be a linear mapping. Recall that $F(0) = 0$. $F$ is said to be *singular* if the image of some nonzero vector $v$ is $0$—that is, if there exists $v \neq 0$ such that $F(v) = 0$. Thus, $F: V \to U$ is *nonsingular* if the zero vector $0$ is the only vector whose image under $F$ is $0$ or, in other words, if $\operatorname{Ker} F = \{0\}$.

**Example 5.10:** Consider the projection map $F: \mathbf{R}^3 \to \mathbf{R}^3$ and the rotation map $G: \mathbf{R}^3 \to \mathbf{R}^3$ appearing in Example 5.7. Because the kernel of $F$ is the $z$-axis, $F$ is singular. On the other hand, the kernel of $G$ consists only of the zero vector $0$. Thus, $G$ is nonsingular.

Nonsingular linear mappings may also be characterized as those mappings that carry independent sets into independent sets. Specifically, we prove the following theorem.

**Theorem 5.7:** *Let $F: V \to U$ be a nonsingular linear mapping. Then the image of any linearly independent set is linearly independent.*

### Isomorphisms

Suppose a linear mapping $F: V \to U$ is one-to-one. Then only $0 \in V$ can map into $0 \in U$, and so $F$ is nonsingular. The converse is also true. For suppose $F$ is nonsingular and $F(v) = F(w)$, then $F(v-w) = F(v) - F(w) = 0$, and hence $v-w = 0$ or $v = w$. Thus, $F(v) = F(w)$ implies $v = w$—that is, $F$ is one-to-one. We have proved the following proposition.

**Proposition 5.8:** *A linear mapping $F: V \to U$ is one-to-one if and only if $F$ is nonsingular.*

Recall that a mapping $F: V \to U$ is called an *isomorphism* if $F$ is linear and bijective. Also, recall that a vector space $V$ is said to be *isomorphic* to a vector space $U$, written $V \cong U$, if there is an isomorphism $F: V \to U$.

The following theorem applies.

**Theorem 5.9:** *Suppose $V$ has finite dimension and $\dim V = \dim U$. Suppose $F: V \to U$ is linear. Then $F$ is an isomorphism if and only if $F$ is nonsingular.*

---

### 5.6 Operations with Linear Mappings

We are able to combine linear mappings in various ways to obtain new linear mappings. These operations are very important and will be used throughout the text.

Let $F: V \to U$ and $G: V \to U$ be linear mappings over a field $K$. The sum $F + G$ and the scalar product $kF$, where $k \in K$, are defined to be the following mappings from $V$ into $U$:

$$(F+G)(v) \equiv F(v) + G(v) \qquad \text{and} \qquad (kF)(v) \equiv kF(v)$$

We now show that if $F$ and $G$ are linear, then $F+G$ and $kF$ are also linear. Specifically, for any vectors $v, w \in V$ and any scalars $a, b \in K$,

$$\begin{aligned}
(F+G)(av+bw) &= F(av+bw) + G(av+bw) \\
&= aF(v) + bF(w) + aG(v) + bG(w) \\
&= a[F(v) + G(v)] + b[F(w) + G(w)] \\
&= a(F+G)(v) + b(F+G)(w)
\end{aligned}$$

and

$$\begin{aligned}
(kF)(av+bw) &= kF(av+bw) \\
&= k[aF(v) + bF(w)] \\
&= akF(v) + bkF(w) \\
&= a(kF)(v) + b(kF)(w)
\end{aligned}$$

Thus, $F+G$ and $kF$ are linear.

**Theorem 5.10:** *Let $V$ and $U$ be vector spaces over a field $K$. Then the collection of all linear mappings from $V$ into $U$ with the above operations of addition and scalar multiplication forms a vector space over $K$.*

The vector space of linear mappings in Theorem 5.10 is usually denoted by

$$\operatorname{Hom}(V,U)$$

Here $\operatorname{Hom}$ comes from the word "homomorphism." The zero element of $\operatorname{Hom}(V,U)$ is the *zero mapping* from $V$ into $U$, denoted by $\mathbf{0}$ and defined by

$$\mathbf{0}(v) = 0$$

for every vector $v \in V$.

Suppose $V$ and $U$ are of finite dimension. Then we have the following theorem.

**Theorem 5.11:** *Suppose $\dim V = m$ and $\dim U = n$. Then $\dim[\operatorname{Hom}(V,U)] = mn$.*

### Composition of Linear Mappings

Now suppose $V$, $U$, and $W$ are vector spaces over the same field $K$, and suppose $F: V \to U$ and $G: U \to W$ are linear mappings. We picture these mappings as follows:

$$V \xrightarrow{\quad F \quad} U \xrightarrow{\quad G \quad} W$$

Recall that the composition function $G \circ F$ is the mapping from $V$ into $W$ defined by $(G \circ F)(v) = G(F(v))$. We show that $G \circ F$ is linear whenever $F$ and $G$ are linear. Specifically, for any vectors $v, w \in V$ and any scalars $a, b \in K$, we have

$$(G \circ F)(av+bw) = G(F(av+bw)) = G(aF(v)+bF(w)) = aG(F(v)) + bG(F(w)) = a(G \circ F)(v) + b(G \circ F)(w)$$

Thus, $G \circ F$ is linear.

The composition of linear mappings and the operations of addition and scalar multiplication are related as follows.

**Theorem 5.12:** *Let $V, U, W$ be vector spaces over $K$. Suppose the following mappings are linear:*

$$F: V \to U, \quad F': V \to U \qquad \text{and} \qquad G: U \to W, \quad G': U \to W$$

*Then, for any scalar $k \in K$:*

* **(i)** $G \circ (F + F') = G \circ F + G \circ F'$
* **(ii)** $(G + G') \circ F = G \circ F + G' \circ F$
* **(iii)** $k(G \circ F) = (kG) \circ F = G \circ (kF)$

---

### 5.7 Algebra $\mathcal{A}(V)$ of Linear Operators

Let $V$ be a vector space over a field $K$. This section considers the special case of linear mappings from the vector space $V$ into itself—that is, linear mappings of the form $F: V \to V$. They are also called *linear operators* or *linear transformations* on $V$. We will write $\mathcal{A}(V)$, instead of $\operatorname{Hom}(V,V)$, for the space of all such mappings.

Now $\mathcal{A}(V)$ is a vector space over $K$, and, if $\dim V = n$, then $\dim \mathcal{A}(V) = n^2$. Moreover, for any mappings $F, G \in \mathcal{A}(V)$, the composition $G \circ F$ exists and also belongs to $\mathcal{A}(V)$. Thus, we have a "multiplication" defined in $\mathcal{A}(V)$. [We sometimes write $FG$ instead of $G \circ F$ in the space $\mathcal{A}(V)$.]

> **Definition:** An *algebra* $\mathcal{A}$ over a field $K$ is a vector space over $K$ in which an operation of multiplication is defined satisfying, for every $F, G, H \in \mathcal{A}$ and every $k \in K$:
> * **(i)** $F(G + H) = FG + FH$,
> * **(ii)** $(G + H)F = GF + HF$,
> * **(iii)** $k(GF) = (kG)F = G(kF)$.
> 
> 
> The algebra is said to be *associative* if, in addition, $(FG)H = F(GH)$.

The above definition of an algebra and previous theorems give us the following result.

**Theorem 5.13:** *Let $V$ be a vector space over $K$. Then $\mathcal{A}(V)$ is an associative algebra over $K$ with respect to composition of mappings. If $\dim V = n$, then $\dim \mathcal{A}(V) = n^2$.*

This is why $\mathcal{A}(V)$ is called the *algebra of linear operators* on $V$.

### Polynomials and Linear Operators

Observe that the identity mapping $I: V \to V$ belongs to $\mathcal{A}(V)$. Also, for any linear operator $F$ in $\mathcal{A}(V)$, we have $FI = IF = F$. We can also form "powers" of $F$. Namely, we define

$$F^0 = I, \qquad F^2 = F \circ F, \qquad F^3 = F^2 \circ F = F \circ F \circ F, \qquad \dots$$

Furthermore, for any polynomial $p(t)$ over $K$, say,

$$p(t) = a_0 + a_1t + a_2t^2 + \dots + a_st^s$$

we can form the linear operator $p(F)$ defined by

$$p(F) = a_0I + a_1F + a_2F^2 + \dots + a_sF^s$$

(For any scalar $k$, the operator $kI$ is sometimes denoted simply by $k$.) In particular, we say $F$ is a *zero* of the polynomial $p(t)$ if $p(F) = 0$.

**Example 5.11:** Let $F: K^3 \to K^3$ be defined by $F(x,y,z) = (0,x,y)$. For any $(a,b,c) \in K^3$,

$$(F+I)(a,b,c) = (0,a,b) + (a,b,c) = (a, \, a+b, \, b+c)$$

$$F^3(a,b,c) = F^2(0,a,b) = F(0,0,a) = (0,0,0)$$

Thus, $F^3 = \mathbf{0}$, the zero mapping in $\mathcal{A}(V)$. This means $F$ is a zero of the polynomial $p(t) = t^3$.

### Square Matrices as Linear Operators

Let $\mathbf{M} = \mathbf{M}_{n,n}$ be the vector space of all square $n \times n$ matrices over $K$. Then any matrix $A$ in $\mathbf{M}$ defines a linear mapping $F_A: K^n \to K^n$ by $F_A(u) = Au$ (where the vectors in $K^n$ are written as columns). Because the mapping is from $K^n$ into itself, the square matrix $A$ is a linear operator, not simply a linear mapping.

Suppose $A$ and $B$ are matrices in $\mathbf{M}$. Then the matrix product $AB$ is defined. Furthermore, for any (column) vector $u$ in $K^n$,

$$F_{AB}(u) = (AB)u = A(Bu) = A(F_B(u)) = (F_A \circ F_B)(u)$$

In other words, the matrix product $AB$ corresponds to the composition of $A$ and $B$ as linear mappings. Similarly, the matrix sum $A+B$ corresponds to the sum of $A$ and $B$ as linear mappings, and the scalar product $kA$ corresponds to the scalar product of $A$ as a linear mapping.

### Invertible Operators in $\mathcal{A}(V)$

Let $F: V \to V$ be a linear operator. $F$ is said to be *invertible* if it has an inverse—that is, if there exists $F^{-1}$ in $\mathcal{A}(V)$ such that $F F^{-1} = F^{-1} F = I$. On the other hand, $F$ is invertible as a mapping if $F$ is both one-to-one and onto. In such a case, $F^{-1}$ is also linear and $F^{-1}$ is the inverse of $F$ as a linear operator.

Suppose $F$ is invertible. Then only $0 \in V$ can map into itself ($0$), and so $F$ is nonsingular. The converse is not true in the infinite-dimensional case, as seen by the following example.

**Example 5.12:** Let $V = \mathbf{P}(t)$, the vector space of polynomials over $K$. Let $F$ be the mapping on $V$ that increases by 1 the exponent of $t$ in each term of a polynomial; that is,

$$F(a_0 + a_1t + a_2t^2 + \dots + a_st^s) = a_0t + a_1t^2 + a_2t^3 + \dots + a_st^{s+1}$$

Then $F$ is a linear mapping and $F$ is nonsingular. However, $F$ is not onto, and so $F$ is not invertible.

The vector space $V = \mathbf{P}(t)$ in the above example has infinite dimension. The situation changes significantly when $V$ has finite dimension. Namely, the following theorem applies.

**Theorem 5.14:** *Let $F$ be a linear operator on a finite-dimensional vector space $V$. Then the following four conditions are equivalent.*

* **(i)** *$F$ is nonsingular: $\operatorname{Ker} F = \{0\}$.*
* **(ii)** *$F$ is one-to-one.*
* **(iii)** *$F$ is an onto mapping.*
* **(iv)** *$F$ is invertible.*

*Proof:* The proof mainly follows from Theorem 5.6, which tells us that

$$\dim V = \dim(\operatorname{Ker} F) + \dim(\operatorname{Im} F)$$

By Proposition 5.8, (i) and (ii) are equivalent. Note that (iv) is equivalent to (ii) and (iii) combined. Thus, to prove the theorem, we need only show that (i) and (iii) are equivalent.

* Suppose (i) holds. Then $\dim(\operatorname{Ker} F) = 0$, and so the above equation tells us that $\dim V = \dim(\operatorname{Im} F)$. This means $V = \operatorname{Im} F$ or, in other words, $F$ is an onto mapping. Thus, (i) implies (iii).
* Suppose (iii) holds. Then $V = \operatorname{Im} F$, and so $\dim V = \dim(\operatorname{Im} F)$. Therefore, the above equation tells us that $\dim(\operatorname{Ker} F) = 0$, and so $F$ is nonsingular. Therefore, (iii) implies (i).

Accordingly, all four conditions are equivalent. $\blacksquare$

> **Remark:** Suppose $A$ is a square $n \times n$ matrix over $K$. Then $A$ may be viewed as a linear operator on $K^n$. Because $K^n$ has finite dimension, Theorem 5.14 holds for the square matrix $A$. This is why the terms "nonsingular" and "invertible" are used interchangeably when applied to square matrices.

**Example 5.13:** Let $F$ be the linear operator on $\mathbf{R}^2$ defined by $F(x,y) = (2x+y, \quad 3x+2y)$.

* To show that $F$ is invertible, we need only show that $F$ is nonsingular. Set $F(x,y) = (0,0)$ to obtain the homogeneous system

$$2x + y = 0 \qquad \text{and} \qquad 3x + 2y = 0$$



Solve for $x$ and $y$ to get $x = 0$, $y = 0$. Hence, $F$ is nonsingular and so invertible.
* To find a formula for $F^{-1}$, we set $F(x,y) = (s,t)$ and so $F^{-1}(s,t) = (x,y)$. We have

$$2x + y = s \qquad \text{and} \qquad 3x + 2y = t$$



Solve for $x$ and $y$ in terms of $s$ and $t$ to obtain $x = 2s - t$, $y = -3s + 2t$. Thus,

$$F^{-1}(s,t) = (2s - t, \quad -3s + 2t) \qquad \text{or} \qquad F^{-1}(x,y) = (2x - y, \quad -3x + 2y)$$



where we rewrite the formula for $F^{-1}$ using standard variables $x$ and $y$ instead of $s$ and $t$.