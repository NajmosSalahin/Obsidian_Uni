# Chapter 5: Linear Mappings — Answer Sets

## Set 1: Mappings, Functions — Domain, Image, Preimage, Graph

**1.** Let A and B be arbitrary nonempty sets. Suppose to each element in a ∈ A there is assigned a unique element of B, called the image of a. The collection f of such assignments is called a mapping (or map) from A into B, and it is denoted by f : A → B. The set A is called the domain of the mapping, and B is called the target set.

**2.** If A₀ is any subset of A, then f(A₀) denotes the set of images of elements of A₀; and if B₀ is any subset of B, then f⁻¹(B₀) denotes the set of elements of A, each of whose image lies in B. That is,
    f(A₀) = {f(a) : a ∈ A₀} and f⁻¹(B₀) = {a ∈ A : f(a) ∈ B₀}.
We call f(A₀) the image of A₀ and f⁻¹(B₀) the inverse image or preimage of B₀. To each mapping f : A → B there corresponds the subset of A × B given by {(a, f(a)) : a ∈ A}. We call this set the graph of f.

**3.** f({a, b, d}) = {f(a), f(b), f(d)} = {y, x, y} = {x, y}. f(A) = {x, y, z} is the image of f.

**4.** (a) The derivative defines a mapping D : V → V where, for any polynomial f(t), we have D(f) = df/dt. Thus,
    D(p) = D(3t² − 5t + 2) = 6t − 5.
    (b) The integral, say from 0 to 1, defines a mapping J : V → R. That is, for any polynomial f(t),
    J(f) = ∫₀¹ f(t) dt, and so J(p) = ∫₀¹ (3t² − 5t + 2) dt = 1/2.

---

## Set 2: Composition, One-to-One, Onto, Identity, Inverse

**1.** Consider two mappings f : A → B and g : B → C. The composition of f and g, denoted by g ∘ f, is the mapping g ∘ f : A → C defined by (g ∘ f)(a) = g(f(a)). That is, first we apply f to a ∈ A, and then we apply g to f(a) ∈ B to get g(f(a)) ∈ C.

Theorem 5.1: Let f : A → B, g : B → C, h : C → D. Then h ∘ (g ∘ f) = (h ∘ g) ∘ f.

**2.** (a) A mapping f : A → B is said to be one-to-one (or 1-1 or injective) if different elements of A have distinct images; that is, If f(a) = f(a′), then a = a′.
    (b) A mapping f : A → B is said to be onto (or f maps A onto B or surjective) if every b ∈ B is the image of at least one a ∈ A.
    (c) A mapping f : A → B is said to be a one-to-one correspondence between A and B (or bijective) if f is both one-to-one and onto.

**3.** The function f is one-to-one. Geometrically, this means that each horizontal line does not contain more than one point of f. The function g is onto. Geometrically, this means that each horizontal line contains at least one point of g. The function h is neither one-to-one nor onto. For example, both 2 and −2 have the same image 4, and −16 has no preimage.

**4.** The mapping f : A → A defined by f(a) = a — that is, the function that assigns to each element in A itself — is called identity mapping. It is usually denoted by 1_A or 1 or I. Thus, for any a ∈ A, we have 1_A(a) = a.

Now let f : A → B. We call g : B → A the inverse of f, written f⁻¹, if f ∘ g = 1_B and g ∘ f = 1_A. We emphasize that f has an inverse if and only if f is a one-to-one correspondence between A and B; that is, f is one-to-one and onto.

---

## Set 3: Definition and Examples of Linear Mappings

**1.** Let V and U be vector spaces over the same field K. A mapping F : V → U is called a linear mapping or linear transformation if it satisfies the following two conditions:
    (1) For any vectors v, w ∈ V, F(v + w) = F(v) + F(w).
    (2) For any scalar k and vector v ∈ V, F(kv) = kF(v).
Substituting k = 0 into condition (2), we obtain F(0) = 0. Thus, every linear mapping takes the zero vector into the zero vector.

**2.** Let F : R³ → R³ be the "projection" mapping into the xy-plane: F(x, y, z) = (x, y, 0). Let v = (a, b, c) and w = (a′, b′, c′). Then
    F(v + w) = F(a + a′, b + b′, c + c′) = (a + a′, b + b′, 0)
             = (a, b, 0) + (a′, b′, 0) = F(v) + F(w)
    and, for any scalar k,
    F(kv) = F(ka, kb, kc) = (ka, kb, 0) = k(a, b, 0) = kF(v).
Thus, F is linear.

**3.** Let G : R² → R² be the "translation" mapping defined by G(x, y) = (x + 1, y + 2). [That is, G adds the vector (1, 2) to any vector v = (x, y) in R².] Note that
    G(0) = G(0, 0) = (1, 2) ≠ 0.
Thus, the zero vector is not mapped into the zero vector. Hence, G is not linear.

**4.** (a) Let D : V → V be the derivative mapping. One proves in calculus that
    d(u + v)/dt = du/dt + dv/dt and d(ku)/dt = k(du/dt).
    That is, D(u + v) = D(u) + D(v) and D(ku) = kD(u). Thus, the derivative mapping is linear.
    (b) Let J : V → R be an integral mapping, say J(f(t)) = ∫₀¹ f(t) dt. One also proves in calculus that
    ∫₀¹ (u(t) + v(t)) dt = ∫₀¹ u(t) dt + ∫₀¹ v(t) dt and ∫₀¹ k u(t) dt = k ∫₀¹ u(t) dt.
    That is, J(u + v) = J(u) + J(v) and J(ku) = kJ(u). Thus, the integral mapping is linear.

---

## Set 4: Zero/Identity Mappings, Theorem 5.2, Matrix Mappings, Isomorphism

**1.** (a) Let F : V → U be the mapping that assigns the zero vector 0 ∈ U to every vector v ∈ V. Then, for any vectors v, w ∈ V and any scalar k ∈ K, we have
    F(v + w) = 0 = 0 + 0 = F(v) + F(w) and F(kv) = 0 = k0 = kF(v).
    Thus, F is linear. We call F the zero mapping, and we usually denote it by 0.
    (b) Consider the identity mapping I : V → V, which maps each v ∈ V into itself. Then, for any vectors v, w ∈ V and any scalars a, b ∈ K, we have
    I(av + bw) = av + bw = aI(v) + bI(w).
    Thus, I is linear.

**2.** Let V and U be vector spaces over a field K. Let {v₁, v₂, ..., v_n} be a basis of V and let u₁, u₂, ..., u_n be any vectors in U. Then there exists a unique linear mapping F : V → U such that F(v₁) = u₁, F(v₂) = u₂, ..., F(v_n) = u_n. We emphasize that the vectors u₁, u₂, ..., u_n are completely arbitrary; they may be linearly dependent or they may even be equal to each other.

**3.** Let A be any real m × n matrix. Recall that A determines a mapping F_A : Kⁿ → K^m by F_A(u) = Au (where the vectors in Kⁿ and K^m are written as columns). By matrix multiplication,
    F_A(v + w) = A(v + w) = Av + Aw = F_A(v) + F_A(w)
    F_A(kv) = A(kv) = k(Av) = kF_A(v).
Thus, the matrix mapping A is linear.

**4.** Two vector spaces V and U over K are isomorphic, written V ≅ U, if there exists a bijective (one-to-one and onto) linear mapping F : V → U. The mapping F is then called an isomorphism between V and U. Consider any vector space V of dimension n and let S be any basis of V. Then the mapping v ↦ [v]_S, which maps each vector v ∈ V into its coordinate vector [v]_S, is an isomorphism between V and Kⁿ.

---

## Set 5: Kernel, Image, Rank, Nullity

**1.** Let F : V → U be a linear mapping. The kernel of F, written Ker F, is the set of elements in V that map into the zero vector 0 in U; that is,
    Ker F = {v ∈ V : F(v) = 0}.
The image (or range) of F, written Im F, is the set of image points in U; that is,
    Im F = {u ∈ U : there exists v ∈ V for which F(v) = u}.
The kernel of F is a subspace of V and the image of F is a subspace of U.

**2.** Suppose v₁, v₂, ..., v_m span a vector space V and suppose F : V → U is linear. Then F(v₁), F(v₂), ..., F(v_m) span Im F.

**3.** Let V be of finite dimension, and let F : V → U be linear. Then
    dim V = dim(Ker F) + dim(Im F) = nullity(F) + rank(F).

**4.** Let A be any m × n matrix over a field K viewed as a linear map A : Kⁿ → K^m. Then
    Ker A = nullsp(A) and Im A = colsp(A).
Here colsp(A) denotes the column space of A, and nullsp(A) denotes the null space of A.

---

## Set 6: Worked Examples — Kernel and Image

**1.** Let F : R³ → R³ be the projection into the xy-plane: F(x, y, z) = (x, y, 0). Clearly the image of F is the entire xy-plane — that is, points of the form (x, y, 0). Moreover, the kernel of F is the z-axis — that is, points of the form (0, 0, c). That is,
    Im F = {(a, b, c) : c = 0} = xy-plane and Ker F = {(a, b, c) : a = 0, b = 0} = z-axis.

**2.** Let G : R³ → R³ be the linear mapping that rotates a vector v about the z-axis through an angle θ: G(x, y, z) = (x cos θ − y sin θ, x sin θ + y cos θ, z). Observe that the distance of a vector v from the origin O does not change under the rotation, and so only the zero vector 0 is mapped into the zero vector 0. Thus, Ker G = {0}. On the other hand, every vector u in R³ is the image of a vector v in R³ that can be obtained by rotating u back by an angle of θ. Thus, Im G = R³, the entire space.

**3.** Consider the vector space V = P(t) of polynomials over the real field R, and let H : V → V be the third-derivative operator; that is, H(f(t)) = d³f/dt³. We claim that
    Ker H = {polynomials of degree ≤ 2} = P₂(t) and Im H = V.
The first comes from the fact that H(at² + bt + c) = 0 but H(tⁿ) ≠ 0 for n ≥ 3. The second comes from the fact that every polynomial g(t) in V is the third derivative of some polynomial f(t) (which can be obtained by taking the antiderivative of g(t) three times).

**4.** Let F : R⁴ → R³ be defined by F(x, y, z, t) = (x − y + z + t, 2x − 2y + 3z + 4t, 3x − 3y + 4z + 5t).

(a) First find the image of the usual basis vectors of R⁴:
    F(1, 0, 0, 0) = (1, 2, 3),  F(0, 0, 1, 0) = (1, 3, 4)
    F(0, 1, 0, 0) = (−1, −2, −3),  F(0, 0, 0, 1) = (1, 4, 5)
By Proposition 5.4, the image vectors span Im F. Hence, form the matrix M whose rows are these image vectors and row reduce to echelon form:

    M = [1 2 3; −1 −2 −3; 1 3 4; 1 4 5] → [1 2 3; 0 0 0; 0 1 1; 0 2 2] → [1 2 3; 0 1 1; 0 0 0; 0 0 0]

Thus, (1, 2, 3) and (0, 1, 1) form a basis of Im F. Hence, dim(Im F) = 2 and rank(F) = 2.

(b) Set F(v) = 0, where v = (x, y, z, t):
    F(x, y, z, t) = (x − y + z + t, 2x − 2y + 3z + 4t, 3x − 3y + 4z + 5t) = (0, 0, 0).

    Set corresponding components equal to each other to form the following homogeneous system whose solution space is Ker F:
    x − y + z + t = 0
    2x − 2y + 3z + 4t = 0
    3x − 3y + 4z + 5t = 0

    which reduces to:
    x − y + z + t = 0
    z + 2t = 0

    The free variables are y and t. Hence, dim(Ker F) = 2 or nullity(F) = 2.
    (i) Set y = 1, t = 0 to obtain the solution (−1, 1, 0, 0).
    (ii) Set y = 0, t = 1 to obtain the solution (1, 0, −2, 1).
    Thus, (−1, 1, 0, 0) and (1, 0, −2, 1) form a basis for Ker F.

(c) As expected from Theorem 5.6, dim(Im F) + dim(Ker F) = 4 = dim R⁴.

---

## Set 7: Singular, Nonsingular, Isomorphisms

**1.** Let F : V → U be a linear mapping. Recall that F(0) = 0. F is said to be singular if the image of some nonzero vector v is 0 — that is, if there exists v ≠ 0 such that F(v) = 0. Thus, F : V → U is nonsingular if the zero vector 0 is the only vector whose image under F is 0 or, in other words, if Ker F = {0}.

Consider the projection map F : R³ → R³ and the rotation map G : R³ → R³ appearing in Fig. 5-2. (See Example 5.7.) Because the kernel of F is the z-axis, F is singular. On the other hand, the kernel of G consists only of the zero vector 0. Thus, G is nonsingular.

**2.** Let F : V → U be a nonsingular linear mapping. Then the image of any linearly independent set is linearly independent.

**3.** Suppose a linear mapping F : V → U is one-to-one. Then only 0 ∈ V can map into 0 ∈ U, and so F is nonsingular. The converse is also true. For suppose F is nonsingular and F(v) = F(w), then F(v − w) = F(v) − F(w) = 0, and hence, v − w = 0 or v = w. Thus, F(v) = F(w) implies v = w — that is, F is one-to-one. A linear mapping F : V → U is one-to-one if and only if F is nonsingular.

**4.** Suppose V has finite dimension and dim V = dim U. Suppose F : V → U is linear. Then F is an isomorphism if and only if F is nonsingular.

---

## Set 8: Operations with Linear Mappings

**1.** Let F : V → U and G : V → U be linear mappings over a field K. The sum F + G and the scalar product kF, where k ∈ K, are defined to be the following mappings from V into U:
    (F + G)(v) = F(v) + G(v) and (kF)(v) = kF(v).
If F and G are linear, then F + G and kF are also linear. Specifically, for any vectors v, w ∈ V and any scalars a, b ∈ K:
    (F + G)(av + bw) = F(av + bw) + G(av + bw)
                     = aF(v) + bF(w) + aG(v) + bG(w)
                     = a(F(v) + G(v)) + b(F(w) + G(w))
                     = a(F + G)(v) + b(F + G)(w)
and
    (kF)(av + bw) = kF(av + bw) = k(aF(v) + bF(w))
                  = akF(v) + bkF(w) = a(kF)(v) + b(kF)(w).
Thus, F + G and kF are linear.

**2.** The collection of all linear mappings from V into U with the above operations of addition and scalar multiplication forms a vector space over K. This vector space is usually denoted by Hom(V, U). If dim V = m and dim U = n, then dim(Hom(V, U)) = mn.

**3.** Suppose V, U, and W are vector spaces over the same field K, and suppose F : V → U and G : U → W are linear mappings. Recall that the composition function G ∘ F is the mapping from V into W defined by (G ∘ F)(v) = G(F(v)). For any vectors v, w ∈ V and any scalars a, b ∈ K:
    (G ∘ F)(av + bw) = G(F(av + bw)) = G(aF(v) + bF(w))
                      = aG(F(v)) + bG(F(w)) = a(G ∘ F)(v) + b(G ∘ F)(w).
Thus, G ∘ F is linear.

**4.** Let V, U, W be vector spaces over K. Suppose the following mappings are linear: F : V → U, F′ : V → U and G : U → W, G′ : U → W. Then, for any scalar k ∈ K:
    (i) G ∘ (F + F′) = G ∘ F + G ∘ F′.
    (ii) (G + G′) ∘ F = G ∘ F + G′ ∘ F.
    (iii) k(G ∘ F) = (kG) ∘ F = G ∘ (kF).

---

## Set 9: Algebra A(V), Polynomials, Square Matrices, Invertible Operators

**1.** Let V be a vector space over a field K. We will write A(V), instead of Hom(V, V), for the space of all linear mappings from V into itself. A(V) is a vector space over K, and if dim V = n, then dim A(V) = n². A(V) is an associative algebra over K with respect to composition of mappings. If dim V = n, then dim A(V) = n².

**2.** Observe that the identity mapping I : V → V belongs to A(V). Also, for any linear operator F in A(V), we have FI = IF = F. We can also form "powers" of F. Namely, we define
    F⁰ = I, F² = F ∘ F, F³ = F² ∘ F = F ∘ F ∘ F, F⁴ = F³ ∘ F, ...
Furthermore, for any polynomial p(t) over K, say p(t) = a₀ + a₁t + a₂t² + ... + a_s t^s, we can form the linear operator p(F) defined by
    p(F) = a₀I + a₁F + a₂F² + ... + a_sF^s.
(For any scalar k, the operator kI is sometimes denoted simply by k.)

Let F : K³ → K³ be defined by F(x, y, z) = (0, x, y). For any (a, b, c) ∈ K³:
    (F + I)(a, b, c) = (0, a, b) + (a, b, c) = (a, a + b, b + c)
    F³(a, b, c) = F²(0, a, b) = F(0, 0, a) = (0, 0, 0).
Thus, F³ = 0, the zero mapping in A(V). This means F is a zero of the polynomial p(t) = t³.

**3.** Let M = M_{n,n} be the vector space of all square n × n matrices over K. Then any matrix A in M defines a linear mapping F_A : Kⁿ → Kⁿ by F_A(u) = Au. Suppose A and B are matrices in M. Then the matrix product AB is defined. Furthermore, for any (column) vector u in Kⁿ:
    F_{AB}(u) = (AB)u = A(Bu) = A(F_B(u)) = F_A(F_B(u)) = (F_A ∘ F_B)(u).
In other words, the matrix product AB corresponds to the composition of A and B as linear mappings.

**4.** (a) Let F be a linear operator on a finite-dimensional vector space V. Then the following four conditions are equivalent:
    (i) F is nonsingular: Ker F = {0}.
    (ii) F is one-to-one.
    (iii) F is an onto mapping.
    (iv) F is invertible.

(b) Let F be the linear operator on R² defined by F(x, y) = (2x + y, 3x + 2y).
    (a) To show that F is invertible, we need only show that F is nonsingular. Set F(x, y) = (0, 0) to obtain the homogeneous system
    2x + y = 0 and 3x + 2y = 0.
    Solve for x and y to get x = 0, y = 0. Hence, F is nonsingular and so invertible.
    (b) To find a formula for F⁻¹, we set F(x, y) = (s, t) and so F⁻¹(s, t) = (x, y). We have
    (2x + y, 3x + 2y) = (s, t) or 2x + y = s, 3x + 2y = t.
    Solve for x and y in terms of s and t to obtain x = 2s − t, y = −3s + 2t. Thus,
    F⁻¹(s, t) = (2s − t, −3s + 2t) or F⁻¹(x, y) = (2x − y, −3x + 2y),
    where we rewrite the formula for F⁻¹ using x and y instead of s and t.
