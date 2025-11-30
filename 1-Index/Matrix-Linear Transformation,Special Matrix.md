Linear Transformations:

**Definition 3.16.** A transformation $T$ is said to be linear if $T$ transforms every vector $X \in E^{(n)}$ into a vector $T(X) \in E^{(m)}$ such that for any two vectors $X_1$ and $X_2 \in E^{(n)}$ and any two scalars $c_1$ and $c_2$, we have$$T(c_1X_1 + c_2X_2) = c_1T(X_1) + c_2T(X_2) \quad$$**Definition 3.17.** The vector space consisting of all vectors $Y=AX$ is known as the _range space_ of $A$, and the space that contains $X$ is known as the _domain_ of $A$. The space that consists of vectors $X$ such that $AX=0$ is termed _the null space_ of $A$.

**Theorem 3.19.** Let $T$ denote a linear transformation associated with an $n \times n$ matrix $A$ from vector space $V$ into vector space $W$ [which contains the range space T(V)]. Then the following propositions hold:

i. If $U \leq V$, then $T(U) \leq W$, and when vectors $X_1, X_2, \dots, X_n$ span $U$, the set $T(X_1), T(X_2), \dots, T(X_n)$ spans $T(U)$.
![[Pasted image 20251130210717.png]]


ii. $\dim(V) = \dim[R(A)] + \dim[N(A)]$, where $V$ is the domain of $T$.
![[Pasted image 20251130210758.png]]![[Pasted image 20251130210802.png]]

**Theorem 3.20.** Let $A^T$ be the transpose of matrix $A$. Then $N(A)$ and $R(A^T)$ are orthogonal complements.![[Pasted image 20251130210906.png]]

System of Linear Equations:
A **system of linear equations** is a collection of two or more linear equations that involve the same set of variables.
