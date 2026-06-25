# Chapter 5: Linear Mappings — Question Sets

## Set 1: Mappings, Functions — Domain, Image, Preimage, Graph

1. What is a mapping f : A → B? Define the domain A and the target set B.

2. For a mapping f : A → B, define:
   (a) f(A₀) for A₀ ⊆ A
   (b) f⁻¹(B₀) for B₀ ⊆ B
   (c) the graph of f

3. Let A = {a, b, c, d} and B = {x, y, z, t}. Define f(a) = y, f(b) = x, f(c) = z, f(d) = y.
   Find f({a, b, d}) and f(A).

4. Let V be the vector space of polynomials over R, and let p(t) = 3t² − 5t + 2.
   (a) Compute D(p) where D : V → V is the derivative mapping.
   (b) Compute J(p) where J : V → R is the integral mapping from 0 to 1.

---

## Set 2: Composition, One-to-One, Onto, Identity, Inverse

1. Define the composition g ∘ f of two mappings f : A → B and g : B → C.
   State the associative law for the composition of three mappings.

2. Define:
   (a) one-to-one (injective) mapping
   (b) onto (surjective) mapping
   (c) bijective mapping

3. Let f : R → R, g : R → R, h : R → R be defined by
   f(x) = 2^x, g(x) = x³ − x, h(x) = x².
   Which of these are one-to-one? Which are onto?

4. Define the identity mapping 1_A : A → A.
   When does a mapping f : A → B have an inverse f⁻¹?

---

## Set 3: Definition and Examples of Linear Mappings

1. State the two conditions that define a linear mapping F : V → U.
   What can you conclude about F(0)?

2. Show that the projection mapping F : R³ → R³ defined by
   F(x, y, z) = (x, y, 0) is linear.

3. Show that the translation mapping G : R² → R² defined by
   G(x, y) = (x + 1, y + 2) is NOT linear.

4. Consider the vector space V = P(t) of polynomials over R.
   (a) Show the derivative mapping D : V → V is linear.
   (b) Show the integral mapping J : V → R defined by J(f) = ∫₀¹ f(t) dt is linear.

---

## Set 4: Zero/Identity Mappings, Theorem 5.2, Matrix Mappings, Isomorphism

1. Show that the zero mapping 0 : V → U (which assigns the zero vector 0 ∈ U to every v ∈ V)
   is linear, and that the identity mapping I : V → V is linear.

2. Let {v₁, v₂, ..., v_n} be a basis of V and let u₁, u₂, ..., u_n be any vectors in U.
   What can you say about the existence of a linear mapping F : V → U such that F(v_i) = u_i?

3. Let A be any m × n matrix over K. Show that the mapping F_A : Kⁿ → K^m defined by
   F_A(u) = Au is linear.

4. Define an isomorphism between two vector spaces V and U over K.
   Describe the isomorphism between an n-dimensional vector space V and Kⁿ using coordinates
   relative to a basis.

---

## Set 5: Kernel, Image, Rank, Nullity

1. Define the kernel Ker F and the image Im F of a linear mapping F : V → U.
   What can you say about Ker F and Im F in terms of being subspaces?

2. Suppose v₁, v₂, ..., v_m span a vector space V and F : V → U is linear.
   What can you say about F(v₁), F(v₂), ..., F(v_m)?

3. State the relationship between dim V, dim(Ker F), and dim(Im F) for a linear mapping
   F : V → U where V is of finite dimension.

4. Let A be any m × n matrix over a field K viewed as a linear map A : Kⁿ → K^m.
   What do Ker A and Im A correspond to in matrix terms?

---

## Set 6: Worked Examples — Kernel and Image

1. Let F : R³ → R³ be the projection into the xy-plane:
   F(x, y, z) = (x, y, 0). Find Im F and Ker F.

2. Let G : R³ → R³ be the rotation about the z-axis through an angle θ:
   G(x, y, z) = (x cos θ − y sin θ, x sin θ + y cos θ, z).
   Find Im G and Ker G.

3. Consider the vector space V = P(t) of polynomials over R and let H : V → V
   be the third-derivative operator, H(f(t)) = d³f/dt³. Find Ker H and Im H.

4. Let F : R⁴ → R³ be the linear mapping defined by
   F(x, y, z, t) = (x − y + z + t, 2x − 2y + 3z + 4t, 3x − 3y + 4z + 5t).
   (a) Find a basis and the dimension of Im F.
   (b) Find a basis and the dimension of Ker F.
   (c) Verify that dim(Im F) + dim(Ker F) = dim R⁴.

---

## Set 7: Singular, Nonsingular, Isomorphisms

1. Define singular and nonsingular linear mappings.
   From earlier examples, which of the projection F and the rotation G are singular
   and which are nonsingular?

2. Let F : V → U be a nonsingular linear mapping. What can you say about the image
   of any linearly independent set?

3. For a linear mapping F : V → U, what is the relationship between F being one-to-one
   and F being nonsingular?

4. Suppose V has finite dimension and dim V = dim U. If F : V → U is linear,
   when does F become an isomorphism?

---

## Set 8: Operations with Linear Mappings

1. Let F : V → U and G : V → U be linear mappings over a field K.
   Define the sum F + G and the scalar product kF. Show that F + G and kF are linear.

2. What algebraic structure does the collection of all linear mappings from V into U
   form? If dim V = m and dim U = n, what is dim(Hom(V, U))?

3. Suppose F : V → U and G : U → W are linear. Show that the composition
   G ∘ F : V → W is linear.

4. Let V, U, W be vector spaces over K. Suppose F, F' : V → U and G, G' : U → W
   are linear. For any scalar k ∈ K, state the three relationships involving
   composition, addition, and scalar multiplication.

---

## Set 9: Algebra A(V), Polynomials, Square Matrices, Invertible Operators

1. What is A(V) and what is its dimension if dim V = n?
   What algebraic structure does A(V) form with respect to composition of mappings?

2. Define powers F², F³ of a linear operator F ∈ A(V).
   For a polynomial p(t) = a₀ + a₁t + a₂t² + ... + a_s t^s over K, define p(F).
   Let F : K³ → K³ be defined by F(x, y, z) = (0, x, y).
   Compute (F + I)(a, b, c) and F³(a, b, c). What polynomial is F a zero of?

3. Let A and B be n × n matrices over K. Explain how the matrix product AB
   corresponds to composition of their associated linear mappings.

4. (a) For a finite-dimensional vector space V, state the four equivalent conditions
   for a linear operator F on V.
   (b) Let F be the linear operator on R² defined by F(x, y) = (2x + y, 3x + 2y).
   Show that F is invertible and find a formula for F⁻¹.
