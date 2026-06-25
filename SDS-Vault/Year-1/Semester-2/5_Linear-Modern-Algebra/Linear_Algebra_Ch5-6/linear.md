Chapter 5 Linear Mappings
-------------------------

### 5.1 Introduction

The main subject matter of linear algebra is the study of linear mappings and their representation by means of matrices. This chapter introduces us to these linear maps and Chapter 6 shows how they can be represented by matrices. First, however, we begin with a study of mappings in general.

### 5.2 Mappings, Functions

Let (A) and (B) be arbitrary nonempty sets. Suppose to each element in (a`\in `{=tex}A) there is assigned a unique element of (B); called the *image* of (a). The collection (f) of such assignments is called a *mapping* (or map) from (A) into (B), and it is denoted by

(f:A`\to `{=tex}B)

The set (A) is called the *domain* of the mapping, and (B) is called the *target set*. We write (f(a)), read "(f) of (a)," for the unique element of (B) that (f) assigns to (a`\in `{=tex}A).

One may also view a mapping (f:A`\to `{=tex}B) as a computer that, for each input value (a`\in `{=tex}A), produces a unique output (f(a)`\in `{=tex}B).

##### Remark:

The term *function* is used synonymously with the word *mapping*, although some texts reserve the word "function" for a real-valued or complex-valued mapping.

Consider a mapping (f:A`\to `{=tex}B). If (A\^{`\prime`{=tex}}) is any subset of (A), then (f(A\^{`\prime`{=tex}})) denotes the set of images of elements of (A\^{`\prime`{=tex}}); and if (B\^{`\prime`{=tex}}) is any subset of (B), then (f^{-1}(B^{`\prime`{=tex}})) denotes the set of elements of (A), each of whose image lies in (B). That is,

(f(A^{`\prime`{=tex}})={f(a):a`\in `{=tex}A^{`\prime`{=tex}}}) and (f^{-1}(B^{`\prime`{=tex}})={a`\in `{=tex}A:f(a)`\in `{=tex}B\^{`\prime`{=tex}}})

We call (f(A\^{`\prime`{=tex}})) the *image* of (A\^{`\prime`{=tex}}) and (f^{-1}(B^{`\prime`{=tex}})) the *inverse image* or *preimage* of (B\^{`\prime`{=tex}}). In particular, the set of all images (i.e., (f(A))) is called the image or *range* of (f).

To each mapping (f:A`\to `{=tex}B) there corresponds the subset of (A`\times `{=tex}B) given by ({(a,f(a)):a`\in `{=tex}A}). We call this set the *graph* of (f). Two mappings (f:A`\to `{=tex}B) and (g:A`\to `{=tex}B) are defined to be *equal*, written (f=g), if (f(a)=g(a)) for every (a`\in `{=tex}A)--that is, if they have the same graph. Thus, we do not distinguish between a function and its graph. The negation of (f=g) is written (f`\neq `{=tex}g) and is the statement:

(`\boxed{\text{There exists an $a\in A$ for which}\,f(a)\neq g(a).}`{=tex})

Sometimes the "'barred" arrow (`\mapsto`{=tex}) is used to denote the image of an arbitrary element (x`\in `{=tex}A) under a mapping (f:A`\to `{=tex}B) by writing

(x`\mapsto `{=tex}f(x))

This is illustrated in the following example.

Chapter 5 Linear Mappings
-------------------------

**Example 5.1**: \* Let (f`\colon`{=tex}`\mathbf{R}`{=tex}`\to`{=tex}`\mathbf{R}`{=tex}) be the function that assigns to each real number (x) its square (x\^{2}). We can denote this function by writing \[f(x)=x^{2}`\qquad`{=tex}`\text{or}`{=tex}`\qquad `{=tex}x`\mapsto `{=tex}x^{2}\] Here the image of (-3) is (9), so we may write (f(-3)=9). However, (f\^{-1}(9)={3,-3}). Also, (f(`\mathbf{R}`{=tex})=\[0,`\infty`{=tex})={x`\colon `{=tex}x`\geq 0`{=tex}}) is the image of (f). \* Let (A={a,b,c,d}) and (B={x,y,z,t}). Then the following defines a mapping (f`\colon `{=tex}A`\to `{=tex}B): \[f(a)=y,;f(b)=x,;f(c)=z,;f(d)=y`\qquad`{=tex}`\text{or}`{=tex}`\qquad `{=tex}f={(a,y),;(b,x),;(c,z),;(d,y)}\] The first defines the mapping explicitly, and the second defines the mapping by its graph. Here, \[f({a,b,d})={f(a),f(b),f(d)}={y,x,y}={x,y}\] Furthermore, (f(A)={x,y,z}) is the image of (f).

**Example 5.2**: Let (V) be the vector space of polynomials over (`\mathbf{R}`{=tex}), and let (p(t)=3t\^{2}-5t+2).

-   The derivative defines a mapping (`\mathbf{D}`{=tex}`\colon `{=tex}V`\to `{=tex}V) where, for any polynomials (f(t)), we have (`\mathbf{D}`{=tex}(f)=df/dt). Thus, (`\mathbf{D}`{=tex}(p)=`\mathbf{D}`{=tex}`\bigl{(}`{=tex}3t\^{2}-5t+2`\bigr{)}`{=tex}=6t-5)
-   The integral, say from (0) to (1), defines a mapping (`\mathbf{J}`{=tex}`\colon `{=tex}V`\to`{=tex}`\mathbf{R}`{=tex}). That is, for any polynomial (f(t)), \[`\mathbf{J}`{=tex}(f)=`\int`{=tex}*{0}\^{1}!f(t);dt,`\qquad`{=tex}`\text{ and so}`{=tex}`\qquad`{=tex}`\mathbf{J}`{=tex}(p)= `\int`{=tex}*{0}^{1}(3t^{2}-5t+2)=`\tfrac{1}{2}`{=tex}\] Observe that the mapping in ((b)) is from the vector space (V) into the scalar field (`\mathbf{R}`{=tex}), whereas the mapping in ((a)) is from the vector space (V) into itself.

### Matrix Mappings

Let (A) be any (m`\times `{=tex}n) matrix over (K). Then (A) determines a mapping (F\_{A}:K^{n}`\to `{=tex}K^{m}) by

\[F\_{A}(u)=Au\]

where the vectors in (K\^{n}) and (K\^{m}) are written as columns. For example, suppose

\[A=`\left[\begin{array}{rrr}1&-4&5\\ 2&3&-6\end{array}\right]`{=tex}`\qquad`{=tex}`\text{and}`{=tex}`\qquad `{=tex}u=`\left[\begin{array}{rrr}1\\ 3\\ -5\end{array}\right]`{=tex}\]

then

\[F\_{A}(u)=Au=`\left[\begin{array}{rrr}1&-4&5\\ 2&3&-6\end{array}\right]`{=tex}`\left[\begin{array}{rrr}1\\ 3\\ -5\end{array}\right]`{=tex}=`\left[\begin{array}{rrr}-36\\ 41\end{array}\right]`{=tex}\]

**Remark:** For notational convenience, we will frequently denote the mapping (F\_{A}) by the letter (A), the same symbol as used for the matrix.

### Composition of Mappings

Consider two mappings (f`\colon `{=tex}A`\to `{=tex}B) and (g:B`\to `{=tex}C), illustrated below:

\[A`\stackrel{{ f}}{{\longrightarrow}}`{=tex}B`\stackrel{{ g}}{{ \longrightarrow}}`{=tex}C\]

The *composition* of (f) and (g), denoted by (g`\circ `{=tex}f), is the mapping (g`\circ `{=tex}f:A`\to `{=tex}C) defined by

\[(g`\circ `{=tex}f)(a)`\equiv `{=tex}g(f(a))\]That is, first we apply (f) to (a`\in `{=tex}A), and then we apply (g) to (f(a)`\in `{=tex}B) to get (g(f(a))`\in `{=tex}C). Viewing (f) and (g) as "computers," the composition means we first input (a`\in `{=tex}A) to get the output (f(a)`\in `{=tex}B) using (f), and then we input (f(a)) to get the output (g(f(a))`\in `{=tex}C) using (g).

Our first theorem tells us that the composition of mappings satisfies the associative law.

**Theorem 5.1**: *Let (f:A`\to `{=tex}B), (g:B`\to `{=tex}C), (h:C`\to `{=tex}D). Then*

(h`\circ`{=tex}(g`\circ `{=tex}f)=(h`\circ `{=tex}g)`\circ `{=tex}f)\_\_

*We prove this theorem here. Let (a`\in `{=tex}A). Then*

((h`\circ`{=tex}(g`\circ `{=tex}f))(a)=h((g`\circ `{=tex}f)(a))=h(g(f(a))))\_\_

(((h`\circ `{=tex}g)`\circ `{=tex}f)(a)=(h`\circ `{=tex}g)(f(a))=h(g(f(a))))\_\_

*Thus, ((h`\circ`{=tex}(g`\circ `{=tex}f))(a)=((h`\circ `{=tex}g)`\circ `{=tex}f)(a)) for every (a`\in `{=tex}A), and so (h`\circ`{=tex}(g`\circ `{=tex}f)=(h`\circ `{=tex}g)`\circ `{=tex}f).*

#### One-to-One and Onto Mappings

We formally introduce some special types of mappings.

**Definition:**: A mapping (f:A`\to `{=tex}B) is said to be *one-to-one* (or 1-1 or *injective*) if different elements of (A) have distinct images; that is,

(`\qquad`{=tex}) If (f(a)=f(a\^{`\prime`{=tex}}),) then (a=a\^{`\prime`{=tex}}). **Definition:**: A mapping (f:A`\to `{=tex}B) is said to be *onto* (or (f) maps (A) onto (B) or *surjective*) if every (b`\in `{=tex}B) is the image of at least one (a`\in `{=tex}A). **Definition:**: A mapping (f:A`\to `{=tex}B) is said to be a *one-to-one correspondence* between (A) and (B) (or *bijective*) if (f) is both one-to-one and onto. **Example 5.3**: Let (f:`\mathbf{R}`{=tex}`\to`{=tex}`\mathbf{R}`{=tex}), (g:`\mathbf{R}`{=tex}`\to`{=tex}`\mathbf{R}`{=tex}), (h:`\mathbf{R}`{=tex}`\to`{=tex}`\mathbf{R}`{=tex}) be defined by

(f(x)=2^{x},`\qquad`{=tex}`\quad `{=tex}g(x)=x^{3}-x,`\qquad`{=tex}`\quad `{=tex}h(x)=x\^{2})\_\_

*The graphs of these functions are shown in Fig. 5-1. The function (f) is one-to-one. Geometrically, this means that each horizontal line does not contain more than one point of (f). The function (g) is onto. Geometrically, this means that each horizontal line contains at least one point of (g). The function (h) is neither one-to-one nor onto. For example, both (2) and (-2) have the same image (4), and (-16) has no preimage.*

### Identity and Inverse Mappings

Let (A) be any nonempty set. The mapping (f:A`\to `{=tex}A) defined by (f(a)=a)--that is, the function that assigns to each element in (A) itself--is called *identity mapping*. It is usually denoted by (`\mathbf{1}`{=tex}*{A}) or (`\mathbf{1}`{=tex}) or (I). Thus, for any (a`\in `{=tex}A), we have (`\mathbf{1}`{=tex}*{A}(a)=a).

Figure 5.1:

Chapter 5 Linear Mappings
-------------------------

Now let (f:A`\to `{=tex}B). We call (g:B`\to `{=tex}A) the inverse of (f), written (f\^{-1}), if

\[f`\circ `{=tex}g={`\bf 1`{=tex}}*{B}`\qquad`{=tex}`\mbox{and}`{=tex}`\qquad `{=tex}g`\circ `{=tex}f={`\bf 1`{=tex}}*{A}\]

We emphasize that (f) has an inverse if and only if (f) is a one-to-one correspondence between (A) and (B); that is, (f) is one-to-one and onto (Problem 5.7). Also, if (b`\in `{=tex}B), then (f\^{-1}(b)=a), where (a) is the unique element of (A) for which (f(a)=b)

### 5.3 Linear Mappings (Linear Transformations)

We begin with a definition.

**Definition:**: Let (V) and (U) be vector spaces over the same field (K). A mapping (F:V`\to `{=tex}U) is called a *linear mapping* or *linear transformation* if it satisfies the following two conditions:

\[
```{=tex}
\begin{array}{ll}(1)&\mbox{For any vectors }v,w\in V,\,F(v+w)=F(v)+F(w).\\ (2)&\mbox{For any scalar $k$ and vector }v\in V,\,F(kv)=kF(v).\end{array}
```
\]

Namely, (F:V`\to `{=tex}U) is linear if it "preserves" the two basic operations of a vector space, that of vector addition and that of scalar multiplication.

Substituting (k=0) into condition (2), we obtain (F(0)=0). Thus, every linear mapping takes the zero vector into the zero vector.

Now for any scalars (a,b`\in `{=tex}K) and any vector (v,w`\in `{=tex}V), we obtain

\[F(av+bw)=F(av)+F(bw)=aF(v)+bF(w)\]

More generally, for any scalars (a\_{i}`\in `{=tex}K) and any vectors (v\_{i}`\in `{=tex}V), we obtain the following basic property of linear mappings:

\[F(a\_{1}v\_{1}+a\_{2}v\_{2}+`\cdots`{=tex}+a\_{m}v\_{m})=a\_{1}F(v\_{1})+a\_{2}F(v\_{2})+`\cdots`{=tex}+a *{m}F(v*{m})\]

**Remark 1:** A linear mapping (F:V`\to `{=tex}U) is completely characterized by the condition

\[F(av+bw)=aF(v)+bF(w)\] (\*)

and so this condition is sometimes used as its defintion.

**Remark 2:** The term *linear transformation* rather than *linear mapping* is frequently used for linear mappings of the form (F:{`\bf R`{=tex}}^{n}`\to{\bf R}`{=tex}^{m}).

**Example 5.4**: 1. Let (F:{`\bf R`{=tex}}^{3}`\to{\bf R}`{=tex}^{3}) be the "projection" mapping into the (xy)-plane; that is, (F) is the mapping defined by (F(x,y,z)=(x,y,0)). We show that (F) is linear. Let (v=(a,b,c)) and (w=(a^{`\prime`{=tex}},b^{`\prime`{=tex}},c\^{`\prime`{=tex}})). Then \[
```{=tex}
\begin{array}{ll}F(v+w)=F(a+a^{\prime},\,\,\,b+b^{\prime},\,\,c+c^{\prime})=( a+a^{\prime},\,\,\,b+b^{\prime},\,\,\,0)\\ \hskip 14.226378pt=(a,b,0)+(a^{\prime},b^{\prime},0)=F(v)+F(w)\end{array}
```
\] and, for any scalar (k), \[F(kv)=F(ka,kb,kc)=(ka,kb,0)=k(a,b,0)=kF(v)\] Thus, (F) is linear. 2. Let (G:{`\bf R`{=tex}}^{2}`\to{\bf R}`{=tex}^{2}) be the "translation" mapping defined by (G(x,y)=(x+1,,,,y+2)). \[That is, (G) adds the vector ((1,2)) to any vector (v=(x,y)) in ({`\bf R`{=tex}}\^{2}).\] Note that \[G(0)=G(0,0)=(1,2)`\neq 0`{=tex}\] Thus, the zero vector is not mapped into the zero vector. Hence, (G) is not linear.

**Example 5.5** (Derivative and Integral Mappings): Consider the vector space (V=`\mathbf{P}`{=tex}(t)) of polynomials over the real field (`\mathbf{R}`{=tex}). Let (u(t)) and (v(t)) be any polynomials in (V) and let (k) be any scalar.

1.  Let (`\mathbf{D}`{=tex}:V`\to `{=tex}V) be the derivative mapping. One proves in calculus that \[`\frac{d(u+v)}{dt}`{=tex}=`\frac{du}{dt}`{=tex}+`\frac{dv}{dt}`{=tex}`\qquad`{=tex}`\text{and}`{=tex}`\qquad`{=tex}`\frac{d(ku) }{dt}`{=tex}=k,`\frac{du}{dt}`{=tex}\] That is, (`\mathbf{D}`{=tex}(u+v)=`\mathbf{D}`{=tex}(u)+`\mathbf{D}`{=tex}(v)) and (`\mathbf{D}`{=tex}(ku)=k`\mathbf{D}`{=tex}(u)). Thus, the derivative mapping is linear.
2.  Let (`\mathbf{J}`{=tex}:V`\to`{=tex}`\mathbf{R}`{=tex}) be an integral mapping, say \[`\mathbf{J}`{=tex}(,f(t),)=`\int`{=tex}*{0}\^{1}!f(t) dt\] One also proves in calculus that, \[`\int`{=tex}*{0}^{1}\[u(t),+,v(t)\]dt=`\int`{=tex}*{0}^{1}!u(t) dt+`\int`{=tex}*{0}\^{1}v(t) dt\]\ and\ \[`\int`{=tex}*{0}^{1}ku(t) dt=k`\int`{=tex}*{0}^{1}u(t) dt\] That is, (`\mathbf{J}`{=tex}(u+v)=`\mathbf{J}`{=tex}(u)+`\mathbf{J}`{=tex}(v)) and (`\mathbf{J}`{=tex}(ku)=k`\mathbf{J}`{=tex}(u)). Thus, the integral mapping is linear.

**Example 5.6** (Zero and Identity Mappings): 1. Let (F:V`\to `{=tex}U) be the mapping that assigns the zero vector (0`\in `{=tex}U) to every vector (v`\in `{=tex}V). Then, for any vectors (v,w`\in `{=tex}V) and any scalar (k`\in `{=tex}K), we have \[F(v+w)=0=0+0=F(v)+F(w)`\qquad`{=tex}`\text{and}`{=tex}`\qquad `{=tex}F(k,v)=0=k0=kF(v)\] Thus, (F) is linear. We call (F) the *zero mapping*, and we usually denote it by (0). 2. Consider the identity mapping (I:V`\to `{=tex}V), which maps each (v`\in `{=tex}V) into itself. Then, for any vectors (v,w`\in `{=tex}V) and any scalars (a,b`\in `{=tex}K), we have \[I(av+bw)=av+bw=al(v)+bI(w)\] Thus, (I) is linear.

Our next theorem (proved in Problem 5.13) gives us an abundance of examples of linear mappings. In particular, it tells us that a linear mapping is completely determined by its values on the elements of a basis.

**Theorem 5.2**: 1. Let (V) and (U) be vector spaces over a field (K). Let ({v\_{1},v\_{2},`\ldots`{=tex},v\_{n}}) be a basis of (V) and let (u\_{1},u\_{2},`\ldots`{=tex},u\_{n}) be any vectors in (U). Then there exists a unique linear mapping (F:V`\to `{=tex}U) such that (F(v\_{1})=u\_{1},F(v\_{2})=u\_{2},`\ldots`{=tex},F(v\_{n})=u\_{n}).

We emphasize that the vectors (u\_{1},u\_{2},`\ldots`{=tex},u\_{n}) in Theorem 5.2 are completely arbitrary; they may be linearly dependent or they may even be equal to each other.

### Matrices as Linear Mappings

Let (A) be any real (m`\times `{=tex}n) matrix. Recall that (A) determines a mapping (F\_{A}:K^{n}`\to `{=tex}K^{m}) by (F\_{A}(u)=Au) (where the vectors in (K\^{n}) and (K\^{m}) are written as columns). We show (F\_{A}) is linear. By matrix multiplication,

\[F\_{A}(v+w) =A(v+w)=Av+Aw=F\_{A}(v)+F\_{A}(w)\] \[F\_{A}(kv) =A(kv)=k(Av)=kF\_{A}(v)\]

In other words, using (A) to represent the mapping, we have

\[A(v+w)=Av+Aw`\qquad`{=tex}`\text{and}`{=tex}`\qquad `{=tex}A(kv)=k(Av)\]

Thus, the matrix mapping (A) is linear.

Chapter 5 Linear Mappings
-------------------------

### Vector Space Isomorphism

The notion of two vector spaces being isomorphic was defined in Chapter 4 when we investigated the coordinates of a vector relative to a basis. We now redefine this concept.

**definition:**: Two vector spaces (V) and (U) over (K) are *isomorphic*, written (V`\cong `{=tex}U), if there exists a bijective (one-to-one and onto) linear mapping (F:V`\to `{=tex}U). The mapping (F) is then called an *isomorphism* between (V) and (U).

Consider any vector space (V) of dimension (n) and let (S) be any basis of (V). Then the mapping

(v`\mapsto`{=tex}`\left[v\right]`{=tex}\_{S})

which maps each vector (v`\in `{=tex}V) into its coordinate vector (`\left[v\right]`{=tex}\_{S}), is an isomorphism between (V) and (K\^{n}).

### Kernel and Image of a Linear Mapping

We begin by defining two concepts.

**definition:**: Let (F:V`\to `{=tex}U) be a linear mapping. The *kernel* of (F), written (`\operatorname{Ker}`{=tex}F), is the set of elements in (V) that map into the zero vector 0 in (U); that is,

(`\operatorname{Ker}`{=tex}F={v`\in `{=tex}V:F(v)=0})

The *image* (or *range*) of (F), written (`\operatorname{Im}`{=tex}F), is the set of image points in (U); that is,

(`\operatorname{Im}`{=tex}F={u`\in `{=tex}U:`\text{there exists }`{=tex}v`\in `{=tex}V`\text{ for which }`{=tex}F(v)=u})

The following theorem is easily proved (Problem 5.22).

**theorem 5.3:**: Let (F:V`\to `{=tex}U) be a linear mapping. Then the kernel of (F) is a subspace of (V) and the image of (F) is a subspace of (U).

Now suppose that (v\_{1},v\_{2},`\ldots`{=tex},v\_{m}) span a vector space (V) and that (F:V`\to `{=tex}U) is linear. We show that (F(v\_{1}),F(v\_{2}),`\ldots`{=tex},F(v\_{m})) span (`\operatorname{Im}`{=tex}F). Let (u`\in`{=tex}`\operatorname{Im}`{=tex}F). Then there exists (v`\in `{=tex}V) such that (F(v)=u). Because the (v\_{i})'s span (V) and (v`\in `{=tex}V), there exist scalars (a\_{1},a\_{2},`\ldots`{=tex},a\_{m}) for which

(v=a\_{1}v\_{1}+a\_{2}v\_{2}+`\cdots`{=tex}+a\_{m}v\_{m})

Therefore,

(u=F(v)=F(a\_{1}v\_{1}+a\_{2}v\_{2}+`\cdots`{=tex}+a\_{m}v\_{m})=a\_{1}F(v\_{1})+a\_{2}F(v\_{2})+ `\cdots`{=tex}+a\_{m}F(v\_{m}))

Thus, the vectors (F(v\_{1}),F(v\_{2}),`\ldots`{=tex},F(v\_{m})) span (`\operatorname{Im}`{=tex}F).

We formally state the above result.

**Proposition 5.4**: (
```{=tex}
\begin{array}{ll}\text{Suppose }v_{1},v_{2},\ldots,v_{m}\text{ span a vector space }V\text{, and suppose }F:V\to U\text{ is linear. Then }F(v_{1}),F(v_{2}),\ldots,F(v_{m})\text{ span }\operatorname{Im}F.\end{array}
```
)\_\_

**Example 5.7**: 1. Let (F:`\mathbf{R}`{=tex}^{3}`\rightarrow`{=tex}`\mathbf{R}`{=tex}^{3}) be the projection of a vector (v) into the (xy)-plane \[as pictured in Fig. 5-2(a)\]; that is, (F(x,y,z)=(x,y,0)) Clearly the image of (F) is the entire (xy)-plane--that is, points of the form ((x,y,0)). Moreover, the kernel of (F) is the (z)-axis--that is, points of the form ((0,0,c)). That is, (`\operatorname{Im}`{=tex}F={(a,b,c):c=0}=xy)-plane and (`\operatorname{Ker}`{=tex}F={(a,b,c):a=0,b=0}=z)-axis 2. Let (G:`\mathbf{R}`{=tex}^{3}`\rightarrow`{=tex}`\mathbf{R}`{=tex}^{3}) be the linear mapping that rotates a vector (v) about the (z)-axis through an angle (`\theta`{=tex}) \[as pictured in Fig. 5-2(b)\]; that is, (G(x,y,z)=(x`\cos`{=tex}`\theta`{=tex}-y`\sin`{=tex}`\theta`{=tex}, x`\sin`{=tex}`\theta`{=tex}+y`\cos`{=tex}`\theta`{=tex}, z))Observe that the distance of a vector (v) from the origin (O) does not change under the rotation, and so only the zero vector (0) is mapped into the zero vector (0). Thus, Ker (G={0}). On the other hand, every vector (u) in (`\mathbf{R}`{=tex}\^{3}) is the image of a vector (v) in (`\mathbf{R}`{=tex}\^{3}) that can be obtained by rotating (u) back by an angle of (`\theta`{=tex}). Thus, Im (G=`\mathbf{R}`{=tex}\^{3}), the entire space.

**Example 5.8**: Consider the vector space (V=`\mathbf{P}`{=tex}(t)) of polynomials over the real field (`\mathbf{R}`{=tex}), and let (H:V`\to `{=tex}V) be the third-derivative operator; that is, (H\[f(t)\]=d^{3}f/d^{3}). \[Sometimes the notation (`\mathbf{D}`{=tex}\^{3}) is used for (H), where (`\mathbf{D}`{=tex}) is the derivative operator.\] We claim that

\[`\text{Ker}`{=tex} H={`\text{polynomials of degree}`{=tex}`\leq 2`{=tex}}=`\mathbf{P}`{=tex}\_{2}(t)`\qquad`{=tex}`\text{ and}`{=tex}`\qquad`{=tex}`\text{Im}`{=tex} H=V\]

The first comes from the fact that (H(a\^{2}+bt+c)=0) but (H(t\^{`\alpha`{=tex}})`\neq 0`{=tex}) for (n`\geq 3`{=tex}). The second comes from that fact that every polynomial (g(t)) in (V) is the third derivative of some polynomial (f(t)) (which can be obtained by taking the antiderivative of (g(t)) three times).

### Kernel and Image of Matrix Mappings

Consider, say, a (3`\times 4`{=tex}) matrix (A) and the usual basis ({e\_{1},e\_{2},e\_{3},e\_{4}}) of (K\^{4}) (written as columns):

\[A=
```{=tex}
\begin{bmatrix}a_{1}&a_{2}&a_{3}&a_{4}\\ b_{1}&b_{2}&b_{3}&b_{4}\\ c_{1}&c_{2}&c_{3}&c_{4}\end{bmatrix}
```
,`\qquad`{=tex}`\quad `{=tex}e\_{1}=
```{=tex}
\begin{bmatrix}1\\ 0\\ 0\\ 0\end{bmatrix}
```
,`\qquad`{=tex}`\quad `{=tex}e\_{2}=
```{=tex}
\begin{bmatrix}1\\ 0\\ 0\\ 0\end{bmatrix}
```
,`\qquad`{=tex}`\quad `{=tex}e\_{3}=
```{=tex}
\begin{bmatrix}1\\ 0\\ 0\\ 0\end{bmatrix}
```
,`\qquad`{=tex}`\quad `{=tex}e\_{4}=
```{=tex}
\begin{bmatrix}1\\ 0\\ 0\\ 0\end{bmatrix}
```
\]

Recall that (A) may be viewed as a linear mapping (A:K^{4}`\to `{=tex}K^{3}), where the vectors in (K\^{4}) and (K\^{3}) are viewed as column vectors. Now the usual basis vectors span (K\^{4}), so their images (Ae\_{1}), (Ae\_{2}), (Ae\_{3}), (Ae\_{4}) span the image of (A). But the vectors (Ae\_{1}), (Ae\_{2}), (Ae\_{3}), (Ae\_{4}) are precisely the columns of (A):

\[Ae\_{1}=\[a\_{1},b\_{1},c\_{1}\]^{T},`\qquad`{=tex}`\quad `{=tex}Ae\_{2}=\[a\_{2},b\_{2},c\_{2}\]^{T}, `\qquad`{=tex}`\quad `{=tex}Ae\_{3}=\[a\_{3},b\_{3},c\_{3}\]^{T},`\qquad`{=tex}`\quad `{=tex}Ae\_{4}=\[a\_{4},b\_{4},c\_\ {4}\]^{T}\]

Thus, the image of (A) is precisely the column space of (A).

On the other hand, the kernel of (A) consists of all vectors (v) for which (Av=0). This means that the kernel of (A) is the solution space of the homogeneous system (AX=0), called the *null space* of (A).

We state the above results formally.

**Proposition 5.5**: Let (A) be any (m`\times `{=tex}n) matrix over a field (K) viewed as a linear map (A:K^{n}`\to `{=tex}K^{m}). Then

\[`\text{Ker}`{=tex} A=`\text{nullsp}`{=tex}(A)`\qquad`{=tex}`\text{and}`{=tex}`\qquad`{=tex}`\text{Im}`{=tex} A=`\text{colsp}`{=tex}(A)\]

Here (`\text{colsp}`{=tex}(A)) denotes the column space of (A), and nullsp((A)) denotes the null space of (A).

Figure 5.2

Chapter 5 Linear Mappings
-------------------------

### Rank and Nullity of a Linear Mapping

Let (F:V`\to `{=tex}U) be a linear mapping. The *rank* of (F) is defined to be the dimension of its image, and the *nullity* of (F) is defined to be the dimension of its kernel; namely,

\[`\operatorname{rank}`{=tex}(F)=`\dim`{=tex}(`\operatorname{Im}`{=tex}F)`\qquad`{=tex}`\text{and}`{=tex}`\qquad `{=tex}`\operatorname{nullity}`{=tex}(F)=`\dim`{=tex}(`\operatorname{Ker}`{=tex}F)\]

The following important theorem (proved in Problem 5.23) holds.

**Theorem 5.6**: Let (V) be of finite dimension, and let (F:V`\to `{=tex}U) be linear. Then

\[`\dim `{=tex}V=`\dim`{=tex}(`\operatorname{Ker}`{=tex}F)+`\dim`{=tex}(`\operatorname{Im}`{=tex}F)=`\operatorname{ nullity}`{=tex}(F)+`\operatorname{rank}`{=tex}(F)\]

Recall that the rank of a matrix (A) was also defined to be the dimension of its column space and row space. If we now view (A) as a linear mapping, then both definitions correspond, because the image of (A) is precisely its column space.

**Example 5.9**: Let (F:`\mathbf{R}`{=tex}^{4}`\to`{=tex}`\mathbf{R}`{=tex}^{3}) be the linear mapping defined by

\[F(x,y,z,t)=(x-y+z+t,`\quad `{=tex}2x-2y+3z+4t,`\quad `{=tex}3x-3y+4z+5t)\]

1.  Find a basis and the dimension of the image of (F). First find the image of the usual basis vectors of (`\mathbf{R}`{=tex}\^{4}), \[F(1,0,0,0)=(1,2,3), F(0,0,1,0)=(1,3,4)\] \[F(0,1,0,0)=(-1,-2,-3), F(0,0,0,1)=(1,4,5)\] By Proposition 5.4, the image vectors span (`\operatorname{Im}`{=tex})(F). Hence, form the matrix (M) whose rows are these image vectors and row reduce to echelon form: \[M=`\left[\begin{array}{rrr}1&2&3\\ -1&-2&-3\\ 1&3&4\\ 1&4&5\end{array}\right]`{=tex}`\sim`{=tex}`\left[\begin{array}{rrr}1&2&3\\ 0&0&0\\ 0&1&1\\ 0&2&2\end{array}\right]`{=tex}`\sim`{=tex}`\left[\begin{array}{rrr}1&2&3\\ 0&1&1\\ 0&0&0\\ 0&0&0\end{array}\right]`{=tex}\] Thus, ((1,2,3)) and ((0,1,1)) form a basis of (`\operatorname{Im}`{=tex})(F). Hence, (`\dim`{=tex}(`\operatorname{Im}`{=tex}F)=2) and (`\operatorname{rank}`{=tex}(F)=2).
2.  Find a basis and the dimension of the kernel of the map (F). Set (F(v)=0), where (v=(x,y,z,t)), \[F(x,y,z,t)=(x-y+z+t,`\quad `{=tex}2x-2y+3z+4t,`\quad `{=tex}3x-3y+4z+5t)=(0,0,0)\] Set corresponding components equal to each other to form the following homogeneous system whose solution space is (`\operatorname{Ker}`{=tex}F): \[
    ```{=tex}
    \begin{array}{rrr}x-\ y+\ z+\ t=0&x-y+z+\ t=0&x-y+z+\ t=0&x-y+z+\ t=0\\ 2x-2y+3z+4t=0&\text{or}&z+2t=0&x-y+z+\ t=0\\ 3x-3y+4z+5t=0&z+2t=0&z+2t=0&z+2t=0\end{array}
    ```
    \] or \[
    ```{=tex}
    \begin{array}{rrr}x-y+z+\ t=0&x-y+z+\ t=0&x-y+z+\ t=0\\ 3x-3y+4z+5t=0&z+2t=0&z+2t=0\end{array}
    ```
    \] The free variables are (y) and (t). Hence, (`\dim`{=tex}(`\operatorname{Ker}`{=tex}F)=2) or (`\operatorname{nullity}`{=tex}(F)=2). 1. Set (y=1), (t=0) to obtain the solution ((-1,1,0,0)), 2. Set (y=0), (t=1) to obtain the solution ((1,0,-2,1)).

Thus, ((-1,1,0,0)) and ((1,0,-2,1)) form a basis for (`\operatorname{Ker}`{=tex}F).

As expected from Theorem 5.6, (`\dim`{=tex}(`\operatorname{Im}`{=tex}F)+`\dim`{=tex}(`\operatorname{Ker}`{=tex}F)=4=`\dim`{=tex}`\mathbf{R}`{=tex}\^{4}).

### Application to Systems of Linear Equations

Let (AX=B) denote the matrix form of a system of (m) linear equations in (n) unknowns. Now the matrix (A) may be viewed as a linear mapping

\[A:K^{n}`\to `{=tex}K^{m}\]Thus, the solution of the equation (AX=B) may be viewed as the preimage of the vector (B`\in `{=tex}K\^{m}) under the linear mapping (A). Furthermore, the solution of the associated homogeneous system

\[AX=0\]

may be viewed as the kernel of the linear mapping (A). Applying Theorem 5.6 to this homogeneous system yields

\[`\dim`{=tex}(`\operatorname{Ker}`{=tex}A)=`\dim `{=tex}K\^{n}-`\dim`{=tex}(`\operatorname{Im}`{=tex}A)=n-`\operatorname{ rank}`{=tex}A\]

But (n) is exactly the number of unknowns in the homogeneous system (AX=0). Thus, we have proved the following theorem of Chapter 4.

**Theorem 4.19**: (;;)\_\_: The dimension of the solution space (W) of a homogenous system (AX=0) of linear equations is (s=n-r), where (n) is the number of unknowns and (r) is the rank of the coefficient matrix (A).

Observe that (r) is also the number of pivot variables in an echelon form of (AX=0), so (s=n-r) is also the number of free variables. Furthermore, the (s) solution vectors of (AX=0) described in Theorem 3.14 are linearly independent (Problem 4.52). Accordingly, because (`\dim `{=tex}W=s), they form a basis for the solution space (W). Thus, we have also proved Theorem 3.14.

### 5.5 Singular and Nonsingular Linear Mappings, Isomorphisms

Let (F:V`\to `{=tex}U) be a linear mapping. Recall that (F(0)=0). (F) is said to be *singular* if the image of some nonzero vector (v) is 0--that is, if there exists (v`\neq 0`{=tex}) such that (F(v)=0). Thus, (F:V`\to `{=tex}U) is *nonsingular* if the zero vector 0 is the only vector whose image under (F) is 0 or, in other words, if (`\operatorname{Ker}`{=tex}F={0}).

**Example 5.10**: Consider the projection map (F:`\mathbf{R}`{=tex}^{3}`\to`{=tex}`\mathbf{R}`{=tex}^{3}) and the rotation map (G:`\mathbf{R}`{=tex}^{3}`\to`{=tex}`\mathbf{R}`{=tex}^{3}) appearing in Fig. 5.2. (See Example 5.7.) Because the kernel of (F) is the (z)-axis, (F) is singular. On the other hand, the kernel of (G) consists only of the zero vector 0. Thus, (G) is nonsingular.

Nonsingular linear mappings may also be characterized as those mappings that carry independent sets into independent sets. Specifically, we prove (Problem 5.28) the following theorem.

**Theorem 5.7**: (;;)\_\_: Let (F:V`\to `{=tex}U) be a nonsingular linear mapping. Then the image of any linearly independent set is linearly independent.

### Isomorphisms

Suppose a linear mapping (F:V`\to `{=tex}U) is one-to-one. Then only (0`\in `{=tex}V) can map into (0`\in `{=tex}U), and so (F) is nonsingular. The converse is also true. For suppose (F) is nonsingular and (F(v)=F(w)), then (F(v-w)=F(v)-F(w)=0), and hence, (v-w=0) or (v=w). Thus, (F(v)=F(w)) implies (v=w)--that is, (F) is one-to-one. We have proved the following proposition.

**Proposition 5.8**: (;;)\_\_: A linear mapping (F:V`\to `{=tex}U) is one-to-one if and only if (F) is nonsingular.

Recall that a mapping (F:V`\to `{=tex}U) is called an *isomorphism* if (F) is linear and if (F) is bijective (i.e., if (F) is one-to-one and onto). Also, recall that a vector space (V) is said to be *isomorphic* to a vector space (U), written (V`\cong `{=tex}U), if there is an isomorphism (F:V`\to `{=tex}U).

The following theorem (proved in Problem 5.29) applies.

**Theorem 5.9**: (;;)\_\_: Suppose (V) has finite dimension and (`\dim `{=tex}V=`\dim `{=tex}U). Suppose (F:V`\to `{=tex}U) is linear. Then (F) is an isomorphism if and only if (F) is nonsingular.

### 5.6 Operations with Linear Mappings

We are able to combine linear mappings in various ways to obtain new linear mappings. These operations are very important and will be used throughout the text.

Let (F:V`\to `{=tex}U) and (G`\colon `{=tex}V`\to `{=tex}U) be linear mappings over a field (K). The sum (F+G) and the scalar product (kF), where (k`\in `{=tex}K), are defined to be the following mappings from (V) into (U):

\[(F+G)(v)`\equiv `{=tex}F(v)+G(v)`\qquad`{=tex}`\text{and}`{=tex}`\qquad`{=tex}(kF)(v)`\equiv `{=tex}kF(v)\]

We now show that if (F) and (G) are linear, then (F+G) and (kF) are also linear. Specifically, for any vectors (v,w`\in `{=tex}V) and any scalars (a,b`\in `{=tex}K),

\[(F+G)(av+bw) =F(av+bw)+G(av+bw)\] \[=aF(v)+bF(w)+aG(v)+bG(w)\] \[=a\[F(v)+G(v)\]+b\[F(w)+G(w)\]\] \[=a(F+G)(v)+b(F+G)(w)\] \[`\text{and}`{=tex}`\qquad`{=tex}`\qquad`{=tex}(kF)(av+bw) =kF(av+bw)=k\[aF(v)+bF(w)\]\] \[=akF(v)+bkF(w)=a(kF)(v)+b(kF)(w)\]

Thus, (F+G) and (kF) are linear.

The following theorem holds.

**theorem 5.10:**: Let (V) and (U) be vector spaces over a field (K). Then the collection of all linear mappings from (V) into (U) with the above operations of addition and scalar multiplication forms a vector space over (K).

The vector space of linear mappings in Theorem 5.10 is usually denoted by

\[`\operatorname{Hom}`{=tex}(V,U)\]

Here (`\operatorname{Hom}`{=tex}) comes from the word "homomorphism." We emphasize that the proof of Theorem 5.10 reduces to showing that (`\operatorname{Hom}`{=tex}(V,U)) does satisfy the eight axioms of a vector space. The zero element of (`\operatorname{Hom}`{=tex}(V,U)) is the *zero mapping* from (V) into (U), denoted by (`\mathbf{0}`{=tex}) and defined by

\[`\mathbf{0}`{=tex}(v)=0\]

for every vector (v`\in `{=tex}V).

Suppose (V) and (U) are of finite dimension. Then we have the following theorem.

**theorem 5.11:**: Suppose (`\dim `{=tex}V=m) and (`\dim `{=tex}U=n). Then (`\dim[\operatorname{Hom}(V,U)]`{=tex}=mn).

### Composition of Linear Mappings

Now suppose (V), (U), and (W) are vector spaces over the same field (K), and suppose (F`\colon `{=tex}V`\to `{=tex}U) and (G:U`\to `{=tex}W) are linear mappings. We picture these mappings as follows:

\[V`\stackrel{{ F}}{{\longrightarrow}}`{=tex}U`\stackrel{{ G}}{{\longrightarrow}}`{=tex}W\]

Recall that the composition function (G`\operatorname{\circ}`{=tex}F) is the mapping from (V) into (W) defined by ((G`\operatorname{\circ}`{=tex}F)(v)=G(F(v))). We show that (G`\operatorname{\circ}`{=tex}F) is linear whenever (F) and (G) are linear. Specifically, for any vectors (v,w`\in `{=tex}V) and any scalars (a,b`\in `{=tex}K), we have

\[(G`\operatorname{\circ}`{=tex}F)(av+bw) =G(F(av+bw))=G(aF(v)+bF(w))\] \[=aG(F(v))+bG(F(w))=a(G`\operatorname{\circ}`{=tex}F)(v)+b(G`\operatorname{ \circ}`{=tex}F)(w)\]

Thus, (G`\operatorname{\circ}`{=tex}F) is linear.

The composition of linear mappings and the operations of addition and scalar multiplication are related as follows.

**Theorem 5.12**: *Let (V), (U), (W) be vector spaces over (K). Suppose the following mappings are linear:*

\[F:V`\to `{=tex}U,`\qquad `{=tex}F^{`\prime`{=tex}}:V`\to `{=tex}U`\qquad`{=tex}`\text{and}`{=tex}`\qquad `{=tex}G:U`\to `{=tex}W,`\qquad `{=tex}G^{`\prime `{=tex}}:U`\to `{=tex}W\]

*Then, for any scalar (k`\in `{=tex}K):*

\[
```{=tex}
\begin{array}{ll}\text{(i)}&G\circ(F+F^{\prime})=G\circ F+G\circ F^{\prime}. \\ \text{(ii)}&(G+G^{\prime})\circ F=G\circ F+G^{\prime}\circ F.\\ \text{(iii)}&k(G\circ F)=(kG)\circ F=G\circ(kF).\end{array}
```
\]

### 5.7 Algebra (A(V)) of Linear Operators

Let (V) be a vector space over a field (K). This section considers the special case of linear mappings from the vector space (V) into itself--that is, linear mappings of the form (F:V`\to `{=tex}V). They are also called *linear operators* or *linear transformations* on (V). We will write (A(V)), instead of (`\operatorname{Hom}`{=tex}(V,V)), for the space of all such mappings.

Now (A(V)) is a vector space over (K) (Theorem 5.8), and, if (`\dim `{=tex}V=n), then (`\dim `{=tex}A(V)=n\^{2}). Moreover, for any mappings (F,G`\in `{=tex}A(V)), the composition (G`\circ `{=tex}F) exists and also belongs to (A(V)). Thus, we have a "multiplication" defined in (A(V)). \[We sometimes write (FG) instead of (G`\circ `{=tex}F) in the space (A(V)).\]

**Remark:** An *algebra*(A) over a field (K) is a vector space over (K) in which an operation of multiplication is defined satisfying, for every (F,G,H`\in `{=tex}A) and every (k`\in `{=tex}K):

\[
```{=tex}
\begin{array}{ll}\text{(i)}&F(G+H)=FG+FH,\\ \text{(ii)}&(G+H)F=GF+HF,\\ \text{(iii)}&k(GF)=(kG)F=G(kF).\end{array}
```
\]

The algebra is said to be *associative* if, in addition, ((FG)H=F(GH)).

The above definition of an algebra and previous theorems give us the following result.

**Theorem 5.13**: *Let (V) be a vector space over (K). Then (A(V)) is an associative algebra over (K) with respect to composition of mappings. If (`\dim `{=tex}V=n), then (`\dim `{=tex}A(V)=n\^{2}).*

This is why (A(V)) is called the *algebra of linear operators* on (V).

### Polynomials and Linear Operators

Observe that the identity mapping (I:V`\to `{=tex}V) belongs to (A(V)). Also, for any linear operator (F) in (A(V)), we have (FI=IF=F). We can also form "powers" of (F). Namely, we define

\[F^{0}=I,`\qquad `{=tex}F^{2}=F`\circ `{=tex}F,`\qquad `{=tex}F^{3}=F^{2}`\circ `{=tex}F=F`\circ `{=tex}F`\circ `{=tex}F,`\qquad `{=tex}F ^{4}=F^{3}`\circ `{=tex}F,`\qquad`{=tex}`\ldots`{=tex}\]

Furthermore, for any polynomial (p(t)) over (K), say,

\[p(t)=a\_{0}+a\_{1}t+a\_{2}t^{2}+`\cdots`{=tex}+a\_{s}t^{2}\]

we can form the linear operator (p(F)) defined by

\[p(F)=a\_{0}I+a\_{1}F+a\_{2}F^{2}+`\cdots`{=tex}+a\_{s}F^{s}\]

(For any scalar (k), the operator (kl) is sometimes denoted simply by (k).) In particular, we say (F) is a *zero* of the polynomial (p(t)) if (p(F)=0).

**Example 5.14**: *Let (F:K^{3}`\to `{=tex}K^{3}) be defined by (F(x,y,z)=(0,x,y)). For any ((a,b,c)`\in `{=tex}K\^{3}),*

\[(F+I)(a,b,c)=(0,a,b)+(a,b,c)=(a, a+b, b+c)\] \[F^{3}(a,b,c)=F^{2}(0,a,b)=F(0,0,a)=(0,0,0)\]

*Thus, (F\^{3}=0), the zero mapping in (A(V)). This means (F) is a zero of the polynomial (p(t)=t\^{3}).*

Chapter 5 *Linear* Mappings
---------------------------

### Square Matrices as Linear Operators

Let (`\mathbf{M}`{=tex}=`\mathbf{M}`{=tex}*{n,n}) be the vector space of all square (n`\times `{=tex}n) matrices over (K). Then any matrix (A) in (M) defines a linear mapping (F*{A}:K^{n}`\to `{=tex}K^{n}) by (F\_{A}(u)=Au) (where the vectors in (K\^{n}) are written as columns). Because the mapping is from (K\^{n}) into itself, the square matrix (A) is a linear operator, not simply a linear mapping.

Suppose (A) and (B) are matrices in (M). Then the matrix product (AB) is defined. Furthermore, for any (column) vector (u) in (K\^{n}),

\[F\_{AB}(u)=(AB)u=A(Bu)=A(F\_{B}(U))=F\_{A}(F\_{B}(u))=(F\_{A}`\circ `{=tex}F\_{B})(u)\]

In other words, the matrix product (AB) corresponds to the composition of (A) and (B) as linear mappings. Similarly, the matrix sum (A+B) corresponds to the sum of (A) and (B) as linear mappings, and the scalar product (kA) corresponds to the scalar product of (A) as a linear mapping.

### Invertible Operators in (`\mathbf{A}`{=tex}(V))

Let (F:V`\to `{=tex}V) be a linear operator. (F) is said to be *invertible* if it has an inverse--that is, if there exists (F\^{-1}) in (A(V)) such that (FF^{-1}=F^{-1}F=I). On the other hand, (F) is invertible as a mapping if (F) is both one-to-one and onto. In such a case, (F\^{-1}) is also linear and (F\^{-1}) is the inverse of (F) as a linear operator (proved in Problem 5.15).

Suppose (F) is invertible. Then only (0`\in `{=tex}V) can map into itself, and so (F) is nonsingular. The converse is not true, as seen by the following example.

**Example 5.12**.: Let (V=`\mathbf{P}`{=tex}(t)), the vector space of polynomials over (K). Let (F) be the mapping on (V) that increases by 1 the exponent of (t) in each term of a polynomial; that is,

\[F(a\_{0}+a\_{1}t+a\_{2}t^{2}+`\cdots`{=tex}+a\_{s}t^{s})=a\_{0}t+a\_{1}t^{2}+a\_{2}t^{3}+ `\cdots`{=tex}+a\_{s}t\^{s+1}\]

Then (F) is a linear mapping and (F) is nonsingular. However, (F) is not onto, and so (F) is not invertible.

The vector space (V=`\mathbf{P}`{=tex}(t)) in the above example has infinite dimension. The situation changes significantly when (V) has finite dimension. Namely, the following theorem applies.

**Theorem 5.14**.: Let (F) be a linear operator on a finite-dimensional vector space (V). Then the following four conditions are equivalent.

\[
```{=tex}
\begin{array}{llll}\mbox{(i)}&F\mbox{ is nonsingular: Ker }F=\{0\}.&\mbox{(iii)}&F\mbox{ is an onto mapping.}\\ \mbox{(ii)}&F\mbox{ is one-to-one.}&\mbox{(iv)}&F\mbox{ is invertible.}\end{array}
```
\]

The proof of the above theorem mainly follows from Theorem 5.6, which tells us that

\[`\mbox{dim }`{=tex}V=`\mbox{dim}`{=tex}(`\mbox{Ker }`{=tex}F)+`\mbox{dim}`{=tex}(`\mbox{Im }`{=tex}F)\]

By Proposition 5.8, (i) and (ii) are equivalent. Note that (iv) is equivalent to (ii) and (iii). Thus, to prove the theorem, we need only show that (i) and (iii) are equivalent. This we do below.

-   Suppose (i) holds. Then (`\mbox{dim}`{=tex}(`\mbox{Ker }`{=tex}F)=0), and so the above equation tells us that (`\mbox{dim }`{=tex}V=`\mbox{dim}`{=tex}(`\mbox{Im }`{=tex}F)). This means (V=`\mbox{Im }`{=tex}F) or, in other words, (F) is an onto mapping. Thus, (i) implies (iii).
-   Suppose (iii) holds. Then (V=`\mbox{Im }`{=tex}F), and so (`\mbox{dim }`{=tex}V=`\mbox{dim}`{=tex}(`\mbox{Im }`{=tex}F)). Therefore, the above equation tells us that (`\mbox{dim}`{=tex}(`\mbox{Ker }`{=tex}F)=0), and so (F) is nonsingular. Therefore, (iii) implies (i).

Accordingly, all four conditions are equivalent.

**Remark:** Suppose (A) is a square (n`\times `{=tex}n) matrix over (K). Then (A) may be viewed as a linear operator on (K\^{n}). Because (K\^{n}) has finite dimension, Theorem 5.14 holds for the square matrix (A). This is why the terms "nonsingular" and "invertible" are used interchangeably when applied to square matrices.

**Example 5.13**.: Let (F) be the linear operator on (`\mathbf{R}`{=tex}\^{2}) defined by (F(x,y)=(2x+y,  3x+2y)).

-   To show that (F) is invertible, we need only show that (F) is nonsingular. Set (F(x,y)=(0,0)) to obtain the homogeneous system \[2x+y=0`\qquad`{=tex}`\mbox{and}`{=tex}`\qquad `{=tex}3x+2y=0\] \#\# Chapter 5 Linear Mappings

Solve for (x) and (y) to get (x=0), (y=0). Hence, (F) is nonsingular and so invertible. \* To find a formula for (F\^{-1}), we set (F(x,y)=(s,t)) and so (F\^{-1}(s,t)=(x,y)). We have \[
```{=tex}
\begin{array}{c}\left(2x+y,\ \ 3x+2y\right)=(s,t)\qquad\text{or}\qquad 2x+\ \ y=s\\ \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad 3x+2y=t\end{array}
```
\] Solve for (x) and (y) in terms of (s) and (t) to obtain ( x=2s-t), ( y=-3s+2t). Thus, \[F^{-1}(s,t)=`\left`{=tex}(2s-t,  -3s+2t`\right`{=tex})`\qquad`{=tex}`\text{or}`{=tex}`\qquad `{=tex}F^{-1}(x,y)= `\left`{=tex}(2x-y,  -3x+2y`\right`{=tex})\] where we rewrite the formula for (F\^{-1}) using (x) and (y) instead of (s) and (t).
