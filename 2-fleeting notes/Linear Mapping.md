## Topic 1: Mappings and Functions

### Definitions

**Mapping:** Let $A$ and $B$ be arbitrary nonempty sets. Suppose to each element in $a\in A$ there is assigned a unique element of $B$; called the image of $a$. The collection $f$ of such assignments is called a mapping (or map) from $A$ into $B$, and it is denoted by $f:A\rightarrow B$.

The set $A$ is called the domain of the mapping, and $B$ is called the target set. We write $f(a)$, read "f of a," for the unique element of $B$ that $f$ assigns to $a\in A$. One may also view a mapping $f:A\rightarrow B$ as a computer that, for each input value $a\in A.$ produces a unique output $f(a)\in B$.

**Image and Inverse Image:** Consider a mapping $f:A\rightarrow B$. If $A^{\prime}$ is any subset of $A$, then $f(A^{\prime})$ denotes the set of images of elements of $A^{\prime}$ and if $B^{\prime}$ is any subset of $B$, then $f^{-1}(B^{\prime})$ denotes the set of elements of $A$, each of whose image lies in $B$. That is, $f(A^{\prime})=\{f(a):a\in A^{\prime}\}$ and $f^{-1}(B^{\prime})=\{a\in A:f(a)\in B^{\prime}\}$.

We call $f(A^{\prime})$ the image of $A^{\prime}$ and $f^{-1}(B^{\prime})$ the inverse image or preimage of $B^{\prime}$. In particular, the set of all images (i.e., $f(A)$) is called the image or range of $f$.

**Graph of a Mapping:** To each mapping $f:A\rightarrow B$ there corresponds the subset of $A\times B$ given by $\{(a,f(a)):a\in A\}$. We call this set the graph of $f$.

**Equality of Mappings:** Two mappings $f:A\rightarrow B$ and $g:A\rightarrow B$ are defined to be equal, written $f=g$, if $f(a)=g(a)$ for every $a\in A$ that is, if they have the same graph. The negation of $f=g$ is written $f\ne g$ and is the statement: There exists an $a\in A$ for which $f(a)\ne g(a).$.Thus, we do not distinguish between a function and its graph.

### Remarks

**Remark:** The term function is used synonymously with the word mapping, although some texts reserve the word "function" for a real-valued or complex-valued mapping.

### Examples

**EXAMPLE 5.1:**

**(a)** Let $f:R\rightarrow R$ be the function that assigns to each real number $x$ its square $x^{2}$.

We can denote this function by writing $f(x)=x^{2}$ or $x\mapsto x^{2}$. Here the image of $3$ is $9$, so we may write $f(-3)=9$. However, $f^{-1}(9)=\{3,-3\}$. Also, $f(R)=[0,\infty)=\{x:x\ge0\}$ is the image of $f$.

**(b)** Let $A=\{a,b,c,d\}$ and $B=\{x,y,z,t\}$. Then the following defines a mapping $f:A\rightarrow B$: $f(a)=y$, $f(b)=x$, $f(c)=z$, $f(d)=y$ or $f=\{(a,y),(b,x),(c,z),(d,y)\}$.

The first defines the mapping explicitly, and the second defines the mapping by its graph. Here, $f(\{a,b,d\})=\{f(a),f(b),f(d)\}=\{y,x,y\}=\{x,y\}$. Furthermore, $f(A)=\{x,y,z\}$ is the image of $f$.

**EXAMPLE 5.2:** Let $V$ be the vector space of polynomials over $R$, and let $p(t)=3t^{2}-5t+2$.

**(a)** The derivative defines a mapping $D:V\rightarrow V$ where, for any polynomials $f(t)$, we have $D(f)=df/dt$.Thus, $D(p)=D(3t^{2}-5t+2)=6t-5$.

**(b)** The integral, say from $0$ to $1$, defines a mapping $J:V\rightarrow R$. That is, for any polynomial $f(t)$, $J(f)=\int_{0}^{1}f(t)dt$.

and so $J(p)=\int_{0}^{1}(3t^{2}-5t+2)=\frac{1}{2}$. Observe that the mapping in (b) is from the vector space $V$ into the scalar field $R$, whereas the mapping in (a) is from the vector space $V$ into itself.

---

## Topic 2: Matrix Mappings & Composition

### Definitions

**Matrix Mappings:** Let $A$ be any $m\times n$ matrix over $K$. Then $A$ determines a mapping $F_{A}:K^{n}\rightarrow K^{m}$ by $F_{A}(u)=Au$ where the vectors in $K^{n}$ and $K^{m}$ are written as columns.For example, suppose $A=[\begin{matrix}1&-4&5\\ 2&3&-6\end{matrix}]$ and $u=[\begin{matrix}1\\ 3\\ -5\end{matrix}]$, then

$$F_{A}(u)=Au=[\begin{matrix}1&-4&5\\ 2&3&-6\end{matrix}][\begin{matrix}1\\ 3\\ -5\end{matrix}]=[\begin{matrix}-36\\ 41\end{matrix}]$$

**Composition of Mappings:** Consider two mappings $f:A\rightarrow B$ and $g:B\rightarrow C$. The composition of $f$ and $g$, denoted by $g\circ f$ is the mapping $g\circ f:A\rightarrow C$ defined by $(g\circ f)(a)\equiv g(f(a))$.

That is, first we apply $f$ to $a\in A$, and then we apply $g$ to $f(a)\in B$ to get $g(f(a))\in C$. Viewing $f$ and $g$ as "computers," the composition means we first input $a\in A$ to get the output $f(a)\in B$ using $f$, and then we input $f(a)$ to get the output $g(f(a))\in C$ using $g$.

### Theorems & Proofs

**THEOREM 5.1:** Let $f:A\rightarrow B$, $g:B\rightarrow C$, $h:C\rightarrow D$. Then $h\circ(g\circ f)=(h\circ g)\circ f$.

**Proof:** Let $a\in A.$ Then $(h\circ(g\circ f))(a)=h((g\circ f)(a))=h(g(f(a)))$ and $((h\circ g)\circ f)(a)=(h\circ g)(f(a))=h(g(f(a)))$. Thus, $(h\circ(g\circ f))(a)=((h\circ g)\circ f)(a)$ for every $a\in A$, and so $h\circ(g\circ f)=(h\circ g)\circ f$.

### Remarks

**Remark:** For notational convenience, we will frequently denote the mapping $F_{A}$ by the letter $A$, the same symbol as used for the matrix.

---

## Topic 3: Types of Mappings

### Definitions

**One-to-One (Injective):** A mapping $f:A\rightarrow B$ is said to be one-to-one (or 1-1 or injective) if different elements of $A$ have distinct images; that is, If $f(a)=f(a^{\prime})$, then $a=a^{\prime}$.

**Onto (Surjective):** A mapping $f:A\rightarrow B$ is said to be onto (or $f$ maps $A$ onto $B$ or surjective) if every $b\in B$ is the image of at least one $a\in A$.

**One-to-One Correspondence (Bijective):** A mapping $f:A\rightarrow B$ is said to be a one-to-one correspondence between $A$ and $B$ (or bijective) if $f$ is both one-to-one and onto.

**Identity Mapping:** Let $A$ be any nonempty set. The mapping $f:A\rightarrow A$ defined by $f(a)=a$ that is, the function that assigns to each element in $A$ itself is called identity mapping.

It is usually denoted by $I_{A}$ or $1$ or $\mathbf{1}$. Thus, for any $a\in A$, we have $1_{A}(a)=a$.

**Inverse Mapping:** Now let $f:A\rightarrow B$. We call $g:B\rightarrow A$ the inverse of $f$, written $f^{-1}$, if $f\circ g=1_{B}$ and $g\circ f=1_{A}$.

We emphasize that $f$ has an inverse if and only if $f$ is a one-to-one correspondence between $A$ and $B$; that is, $f$ is one-to-one and onto. Also, if $b\in B$, then $f^{-1}(b)=a$, where $a$ is the unique element of $A$ for which $f(a)=b$.

### Examples

**EXAMPLE 5.3:** Let $f:R\rightarrow R$, $g:R\rightarrow R$, $h:R\rightarrow R$ be defined by $f(x)=2^{x}$, $g(x)=x^{3}-x$, $h(x)=x^{2}$.

The function $f$ is one-to-one. Geometrically, this means that each horizontal line does not contain more than one point of $f$. The function $g$ is onto. Geometrically, this means that each horizontal line contains at least one point of $g$. The function $h$ is neither one-to-one nor onto. For example, both 2 and -2 have the same image 4, and -16 has no preimage. .