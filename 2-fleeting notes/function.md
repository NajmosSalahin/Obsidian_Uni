---
title: function
created: 2026-03-18
type: literature
tags:
  - reading-notes
  - flashcards
aliases:
---
# function


## Definitions

### Section 0.1: Functions

- **Function:** A relationship where a variable $y$ depends on a variable $x$ in such a way that each value of $x$ determines exactly one value of $y$. It is also described as a rule that associates a unique output with each input.

    
- **Independent Variable (Argument):** The variable $x$ in the functional relationship $y = f(x)$.
    
- **Dependent Variable:** The variable $y$ in the relationship $y = f(x)$, so named because its value is determined once a specific value for $x$ is chosen.
    
- **Real-Valued Function of a Real Variable:** A function where both the independent and dependent variables are real numbers.
    
- **Graph of a Function:** In the $xy$-plane, this is the graph of the equation $y = f(x)$.
    
- **Zeros (Roots or $x$-intercepts):** The values of $x$ for which $f(x) = 0$; these are the points where the graph intersects the $x$-axis.
    
- **Vertical Line Test:** A curve in the $xy$-plane represents a function if and only if no vertical line intersects the curve more than once.
    
- **Absolute Value (Magnitude):** Defined as $|x| = x$ if $x \ge 0$ and $|x| = -x$ if $x < 0$.
    
- **Piecewise-Defined Function:** A function defined by different formulas for different parts of its domain.
    
- **Domain:** The set of all allowable inputs ($x$-values) for a function.
    
- **Range:** The set of all resulting outputs ($y$-values) as $x$ varies over the domain.
    
- **Natural Domain:** If no domain is explicitly stated, it is the set of all real numbers for which a formula yields a real value.
    

### Section 0.2: New Functions from Old

- **Arithmetic Operations on Functions:** Given functions $f$ and $g$, their sum ($f+g$), difference ($f-g$), product ($fg$), and quotient ($f/g$) are defined by performing the corresponding operation on their outputs.
    
- **Composition of Functions:** The function $f \circ g$ (the composition of $f$ with $g$) is defined by $(f \circ g)(x) = f(g(x))$.
    
- **Symmetry (About the $y$-axis):** A curve is symmetric about the $y$-axis if replacing $x$ with $-x$ produces an equivalent equation.
    
- **Symmetry (About the $x$-axis):** A curve is symmetric about the $x$-axis if replacing $y$ with $-y$ produces an equivalent equation.
    
- **Symmetry (About the origin):** A curve is symmetric about the origin if replacing both $x$ with $-x$ and $y$ with $-y$ produces an equivalent equation.
    
- **Even Function:** A function where $f(-x) = f(x)$; its graph is symmetric about the $y$-axis.
    
- **Odd Function:** A function where $f(-x) = -f(x)$; its graph is symmetric about the origin.
    

### Section 0.3: Families of Functions

- **Parameters:** Constants that are varied to produce a family of curves.
    
- **Power Function:** A function of the form $f(x) = x^p$, where $p$ is a constant.
    
- **Inversely Proportional:** A variable $y$ is inversely proportional to $x$ if $y = k/x$ for some positive constant $k$.
    
- **Polynomial:** A function that can be expressed as a sum of terms of the form $cx^n$, where $c$ is a constant and $n$ is a nonnegative integer.
    
- **Degree of a Polynomial:** The highest power of $x$ that occurs with a nonzero coefficient.
    
- **Rational Function:** A function expressible as the ratio of two polynomials.
    
- **Vertical Asymptote:** A vertical line $x = a$ that the graph of a function closely approximates as $x$ approaches $a$.
    
- **Horizontal Asymptote:** A horizontal line $y = L$ that the graph of a function approaches as $x$ increases or decreases indefinitely.
    
- **Algebraic Function:** A function constructed from polynomials using addition, subtraction, multiplication, division, and root extraction.
    
- **Amplitude, Period, and Frequency:** For trigonometric functions of the form $y = A \sin Bx$, the amplitude is $|A|$, the period is $2\pi/|B|$, and the frequency is $|B|/2\pi$.
    

### Section 0.4: Inverse Functions

- **Inverse Functions:** Two functions $f$ and $g$ such that $g(f(x)) = x$ and $f(g(y)) = y$ for all $x$ and $y$ in their respective domains.
    
- **One-to-One (Invertible):** A function that assigns distinct outputs to distinct inputs.
    
- **Increasing Function:** A function where $f(x_1) < f(x_2)$ whenever $x_1 < x_2$.
    
- **Decreasing Function:** A function where $f(x_1) > f(x_2)$ whenever $x_1 < x_2$.
    
- **Inverse Trigonometric Functions:** Defined as the inverses of trigonometric functions restricted to specific domains to make them one-to-one (e.g., $\sin^{-1}$ is the inverse of $\sin x$ restricted to $[-\pi/2, \pi/2]$).
    

### Section 0.5: Exponential and Logarithmic Functions

- **Exponential Function (Base $b$):** A function of the form $f(x) = b^x$, where $b > 0$.
    
- **Natural Exponential Function:** The exponential function with base $e \approx 2.718282$.
    
- **Logarithm (Base $b$):** The exponent to which $b$ must be raised to produce a given value $x$.
    
- **Natural Logarithm ($\ln x$):** The logarithm with base $e$; it is the inverse of the natural exponential function.
    

---

## Formulas

### Geometry and Physics Formulas

- **Circumference of a circle:** $C = 2\pi r$.
    
- **Newton’s Law of Universal Gravitation:** $F = G \frac{m_1 m_2}{r^2}$.
    
- **Equation of a circle centered at the origin (radius 5):** $x^2 + y^2 = 25$.
    
- **Volume of an open box (constructed from a 16-by-30 inch cardboard with cut-out squares of side $x$):** $V(x) = (16 - 2x)(30 - 2x)x = 480x - 92x^2 + 4x^3$.
    
- **Distance traveled at constant speed:** $D(t) = 100t$.
    
- **Boyle’s Law (ideal gas pressure and volume):** $PV = k$.
    
- **Law of Cosines:** $c^2 = a^2 + b^2 - 2ab \cos \theta$.
    
- **Horizontal range of a projectile:** $R = \frac{v^2}{g} \sin 2\theta$.
    
- **Satellite horizon sensor angle:** $\sin \theta = \frac{R}{R + h}$.
    
- **Electrical resistance of pure metal wire:** $R = R_0(1 + kT)$.
    
- **Empirical Wind Chill Index (at 32°F):** $W = 32$ for $0 \leq v \leq 3$ and $W = 55.628 - 22.07v^{0.16}$ for $v > 3$.
    
- **National Weather Service WCT Index:** $WCT = T$ for $0 \leq v \leq 3$ and $WCT = 35.74 + 0.6215T - 35.75v^{0.16} + 0.4275Tv^{0.16}$ for $v > 3$.
    

### Algebraic and Function Formulas

- **Definition of Absolute Value:** $|x| = x$ if $x \geq 0$ and $|x| = -x$ if $x < 0$.
    
- **Algebraic properties of absolute value:** $|-a| = |a|$, $|ab| = |a||b|$, $|a/b| = |a|/|b|$, and $|a + b| \leq |a| + |b|$.
    
- **Square root and absolute value identity:** $\sqrt{x^2} = |x|$.
    
- **Arithmetic operations on functions:** $(f + g)(x) = f(x) + g(x)$, $(f - g)(x) = f(x) - g(x)$, $(fg)(x) = f(x)g(x)$, and $(f / g)(x) = f(x) / g(x)$.
    
- **Composition of functions:** $(f \circ g)(x) = f(g(x))$.
    
- **Symmetry tests (Even and Odd):** Even functions satisfy $f(-x) = f(x)$, while odd functions satisfy $f(-x) = -f(x)$.
    
- **Equation of a line (Slope-Intercept):** $y = mx + b$.
    
- **Power Function family:** $f(x) = x^p$.
    
- **Inverse Proportionality:** $y = k/x$ or $xy = k$.
    
- **General Polynomial Form:** $c_0 + c_1x + c_2x^2 + \dots + c_nx^n$.
    

### Trigonometry and Inverse Trigonometry

- **Sinusoidal function families:** $f(x) = A \sin(Bx - C)$ and $g(x) = A \cos(Bx - C)$.
    
- **Amplitude, Period, and Frequency:** Amplitude $= |A|$, Period $= \frac{2\pi}{|B|}$, and Frequency $= \frac{|B|}{2\pi}$.
    
- **Cancellation equations for inverses:** $f^{-1}(f(x)) = x$ and $f(f^{-1}(x)) = x$.
    
- **Inverse Secant identity:** $\sec^{-1} x = \cos^{-1}(1/x)$.
    
- **Common Inverse Trig Identities:** $\sin^{-1} x + \cos^{-1} x = \pi/2$, $\cos(\sin^{-1} x) = \sqrt{1 - x^2}$, $\sin(\cos^{-1} x) = \sqrt{1 - x^2}$, and $\tan(\sin^{-1} x) = \frac{x}{\sqrt{1 - x^2}}$.
    
- **Additional Trig Identities:** $\sec(\tan^{-1} x) = \sqrt{1 + x^2}$ and $\sin(\sec^{-1} x) = \frac{\sqrt{x^2 - 1}}{|x|}$.
    

### Exponentials and Logarithms

- **Laws of Exponents:** $b^p b^q = b^{p+q}$, $b^p / b^q = b^{p-q}$, and $(b^p)^q = b^{pq}$.
    
- **Approximation of the constant $e$:** $(1 + 1/x)^x \approx e$ as $x$ increases indefinitely.
    
- **Relationship between bases and logarithms:** $y = \log_b x$ if and only if $x = b^y$.
    
- **Natural Logarithm:** $y = \ln x$ if and only if $x = e^y$.
    
- **Logarithmic Cancellation:** $\log_b(b^x) = x$, $b^{\log_b x} = x$, $\ln(e^x) = x$, and $e^{\ln x} = x$.
    
- **Algebraic properties of logarithms:** $\log_b(ac) = \log_b a + \log_b c$, $\log_b(a/c) = \log_b a - \log_b c$, and $\log_b(a^r) = r \log_b a$.
    
- **Radioisotope power supply output:** $P = 75e^{-t/125}$.
    
- **Change of Base formula:** $\log_b x = \frac{\ln x}{\ln b}$.
    

### Scientific Logarithmic Scales

- **Sound Level ($\beta$ in decibels):** $\beta = 10 \log(I/I_0)$, where $I_0 = 10^{-12} \text{ W/m}^2$.
    
- **Acidity (pH Scale):** $\text{pH} = -\log[H^+]$.
    
- **Richter Scale Earthquake Energy:** $\log E = 4.4 + 1.5M$.
    

---

## Theorems and Their Associated Proofs

### Theorem 0.2.3: Symmetry Tests

A plane curve is subject to the following symmetry tests:

(a) It is symmetric about the $y$-axis if and only if replacing $x$ by $-x$ in its equation produces an equivalent equation.

(b) It is symmetric about the $x$-axis if and only if replacing $y$ by $-y$ in its equation produces an equivalent equation.

(c) It is symmetric about the origin if and only if replacing both $x$ by $-x$ and $y$ by $-y$ in its equation produces an equivalent equation.

**Proof:** The sources provide these tests as a theorem without a formal proof block.

### Theorem 0.4.2: Inverse Existence from Solving for $x$

If an equation $y = f(x)$ can be solved for $x$ as a function of $y$, say $x = g(y)$, then $f$ has an inverse and that inverse is $f^{-1}(y) = g(y)$.

**Proof:** Substituting $y = f(x)$ into $x = g(y)$ yields $x = g(f(x))$, which confirms the first requirement of inverse functions. Furthermore, substituting $x = g(y)$ into $y = f(x)$ yields $y = f(g(y))$, which confirms the second requirement.

### Theorem 0.4.3: One-to-One and Inverses

A function has an inverse if and only if it is one-to-one (invertible).

**Proof:** The sources state this theorem based on the observation that a function must assign distinct outputs to distinct inputs to be undoable, but they do not provide a formal proof block.

### Theorem 0.4.4: The Horizontal Line Test

A function has an inverse function if and only if its graph is cut at most once by any horizontal line.

**Proof:** This is presented as a geometric interpretation of the one-to-one requirement in Theorem 0.4.3; no formal proof block is provided.

### Theorem 0.4.5: Reflection about $y = x$

If a function $f$ has an inverse, then the graphs of $y = f(x)$ and $y = f^{-1}(x)$ are reflections of one another about the line $y = x$.

**Proof:** If $(a, b)$ is a point on the graph $y = f(x)$, then $b = f(a)$, which is equivalent to $a = f^{-1}(b)$. This means $(b, a)$ is a point on the graph of $y = f^{-1}(x)$. Reversing the coordinates of a point geometrically reflects that point about the line $y = x$.

### Theorem 0.5.1: Exponential and Logarithmic Inverses

If $b > 0$ and $b \neq 1$, then the exponential function $b^x$ and the logarithmic function $\log_b x$ are inverse functions.

**Proof:** Because the graph of $f(x) = b^x$ passes the horizontal line test, it has an inverse. Solving the equation $x = b^y$ for $y$ yields $y = \log_b x$ by the definition of a logarithm, which establishes the inverse relationship.

### Theorem 0.5.2: Algebraic Properties of Logarithms

If $b > 0$, $b \neq 1$, $a > 0$, $c > 0$, and $r$ is any real number, then:

(a) Product Property: $\log_b(ac) = \log_b a + \log_b c$.

(b) Quotient Property: $\log_b(a/c) = \log_b a - \log_b c$.

(c) Power Property: $\log_b(a^r) = r \log_b a$.

(d) Reciprocal Property: $\log_b(1/c) = -\log_b c$.

**Proof:** The sources do not provide a formal proof for these properties in the text, though they are assigned as an exercise for the reader.

### Other Labeled Principles (Presented similarly to Theorems)

- **0.1.3 The Vertical Line Test:** A curve in the $xy$-plane is the graph of a function if and only if no vertical line intersects the curve more than once.
    
- **0.1.4 Properties of Absolute Value:** Includes results such as $|-a| = |a|$, $|ab| = |a||b|$, and the triangle inequality $|a + b| \leq |a| + |b|$.
    

---

## Mathematical Problems

### Section 0.1: Functions

**Quick Check Exercises 0.1**

- **Evaluation and Domain:** Finding the natural domain, range, and specific values (e.g., $f(3)$ or $f(t^2-1)$) for functions like $f(x) = \sqrt{x+1}+4$.
    
- **Graph Identification:** Determining which geometric "letters" represent the graph of a function $y=f(x)$ based on the orientation of the y-axis.
    
- **Interpreting Graphs:** Extracting domain, range, and solutions to $f(x)=k$ from a provided plot.
    
- **Table-to-Function Analysis:** Determining if $y$ is a function of $x$ from temperature forecast data.
    
- **Variable Relationships:** Expressing dimensions (length, width, area) of a rectangle as functions of one another.
    

**Exercise Set 0.1**

- **Numerical and Graphical Analysis:** Using tables and graphs to find values of $y$ for given $x$, identifying maximum/minimum values, and applying the vertical line test.
    
- **Natural Domains:** Comparing the domains of two different algebraic expressions.
    
- **Applied Data:** Analyzing U.S. household median income graphs (1990–2005) to find growth rates and periods of decline.
    
- **Function Evaluation:** Calculating values for piecewise and algebraic functions.
    
- **Continuity Concepts:** Explaining if real-world data (population, temperature, cereal boxes on a shelf) would produce continuous or broken curves.
    
- **Geometric Modeling:** Expressing the volume of a box, the height of a pendulum, or the length of a chord as functions of a single variable.
    
- **Physics and Optimization:** Estimating dimensions to minimize the cost of a can or finding the height of a rocket based on a camera's elevation angle.
    

### Section 0.2: New Functions from Old

**Quick Check Exercises 0.2**

- **Arithmetic Operations:** Finding formulas and domains for $f+g$, $f-g$, $fg$, and $f/g$.
    
- **Composition:** Finding $f \circ g$ and $g \circ f$ and their domains.
    
- **Graph Shifting:** Identifying the direction and units of shift for $y=1+(x-2)^2$ compared to $y=x^2$.
    

**Exercise Set 0.2**

- **Transformations:** Sketching graphs by translating, reflecting, and stretching basic parent functions (e.g., $y=|x|$, $y=1/x$, $y=\sqrt{x}$).
    
- **Function Decomposition:** Breaking down a complex function into a composition of two simpler functions ($f = g \circ h$).
    
- **Symmetry and Parity:** Classifying functions as even, odd, or neither using algebraic tests or provided tables/graphs.
    
- **Complex Graphing:** Using a graphing utility to explore four-cusped hypocycloids and greatest integer functions.
    

### Section 0.3: Families of Functions

**Quick Check Exercises 0.3**

- **Symmetry and Asymptotes:** Identifying which integer powers ($n$) in $y=x^n$ result in symmetry about the y-axis or origin, or produce a vertical asymptote.
    
- **Trigonometric Properties:** Identifying the amplitude and period of $y=A \sin Bx$.
    

**Exercise Set 0.3**

- **Family of Lines:** Finding equations for lines with fixed slopes, perpendicular lines, or lines passing through specific points.
    
- **Depreciation and Physics:** Modeling business item value over time and using Boyle's Law ($PV=k$) to graph pressure versus volume.
    
- **Power and Rational Functions:** Matching equations to graphs and identifying horizontal and vertical asymptotes.
    
- **Trigonometric Modeling:** Finding equations of the form $y = y_0 + A \sin(Bx - C)$ for provided waves and modeling standard electrical outlet voltage.
    

### Section 0.4: Inverse Functions

**Quick Check Exercises 0.4**

- **Invertibility:** Determining if real-world scenarios (people in line, weight of lead) are one-to-one.
    
- **Inverse Operations:** Finding an original number after a sequence of operations (doubling, adding, cubing).
    
- **Inverse Trig:** Calculating exact values for $\sin^{-1}(-1)$, $\tan^{-1}(1)$, and $\sec^{-1}(-2)$.
    

**Exercise Set 0.4**

- **Finding Inverses:** Deriving algebraic formulas for $f^{-1}(x)$ and stating their domains.
    
- **Horizontal Line Test:** Determining if functions are one-to-one.
    
- **Trig Identities:** Using the triangle method to simplify expressions like $\tan(\cos^{-1} x)$.
    
- **Applied Trig:** Calculating the range of a soccer ball, daylight hours in Alaska, or "line of sight" angles for airplanes.
    

### Section 0.5: Exponential and Logarithmic Functions

**Quick Check Exercises 0.5**

- **Exponents:** Expressing values like $\sqrt{8}$ or $5$ as powers of 4.
    
- **Solving Equations:** Finding $x$ for equations like $e^x = 1/2$ or $2 \log x - \log(x+1) = \log 4 - \log 3$.
    

**Exercise Set 0.5**

- **Logarithm Properties:** Expanding and condensing logarithmic expressions using product, quotient, and power rules.
    
- **Solving Complex Equations:** Solving for $x$ in equations involving $e^x$, such as $e^{-2x} - 3e^{-x} = -2$.
    
- **Applied Logarithmic Scales:**
    
    - **Radioactive Decay:** Calculating the mass of potassium-42 over time.
        
    - **Chemistry:** Finding the pH of substances like tomatoes or milk.
        
    - **Decibels:** Comparing the intensity of jet aircraft, rock music, or car horns.
        
    - **Richter Scale:** Finding the energy released in the 1906 San Francisco earthquake.
        

### Chapter 0 Review Exercises

The review section synthesizes all concepts, including:

- **Optimization:** Finding the minimum cost for a rectangular storage container.
    
- **Coordinate Geometry:** Finding the distance between a fixed point and a point moving along a curve $y=1/x$.
    
- **Environmental Modeling:** Predicting the coldest day of the year in Anchorage or the growth of a sheep population in Colorado.
    
- **Physics:** Calculating terminal velocity for a package dropped from a helicopter.
    

---









> [!info]+ PrismJS and editing views
> [Source mode](https://obsidian.md/help/edit-and-read#Source%20mode) and [Live Preview](https://obsidian.md/help/edit-and-read#Live%20Preview) do not support PrismJS, and may render syntax highlighting differently.
