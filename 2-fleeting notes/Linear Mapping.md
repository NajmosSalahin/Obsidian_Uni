**THEOREM 5.1:** Let $f : A \to B, \, g : B \to C, \, h : C \to D$. Then  
$$h \circ (g \circ f) = (h \circ g) \circ f$$

We prove this theorem here. Let $a \in A$. Then  
$$(h \circ (g \circ f))(a) = h((g \circ f)(a)) = h(g(f(a)))$$  
$$((h \circ g) \circ f)(a) = (h \circ g)(f(a)) = h(g(f(a)))$$

Thus, $(h \circ (g \circ f))(a) = ((h \circ g) \circ f)(a)$ for every $a \in A$, and so $h \circ (g \circ f) = (h \circ g) \circ f$.

# One-to-One and Onto Mappings

We formally introduce some special types of mappings.

**DEFINITION:**  
A mapping $f : A \to B$ is said to be **one-to-one** (or 1-1 or *injective*) if different elements of $A$ have distinct images; that is,  
$$\text{If } f(a) = f(a'), \text{ then } a = a'.$$

**DEFINITION:**  
A mapping $f : A \to B$ is said to be **onto** (or $f$ maps $A$ onto $B$ or *surjective*) if every $b \in B$ is the image of at least one $a \in A$.

**DEFINITION:**  
A mapping $f : A \to B$ is said to be a **one-to-one correspondence** between $A$ and $B$ (or *bijective*) if $f$ is both one-to-one and onto.
