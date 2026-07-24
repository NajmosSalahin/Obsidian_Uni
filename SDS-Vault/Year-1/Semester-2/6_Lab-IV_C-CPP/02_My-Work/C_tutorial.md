I can see this is your STAT-1206 "Programming with C" tutorial exam paper. Let me answer all four questions for you.

## 1. Define C program. Write down the importance of C. (03 marks)

**Definition:** A C program is a set of instructions written in the C programming language that a computer follows to perform a specific task. It consists of functions, variables, and statements arranged according to C syntax rules, with `main()` as the entry point of execution.

**Importance of C:**
- **Foundation language** – It is the base for many modern languages like C++, Java, and Python, so learning C builds strong programming fundamentals.
- **Fast and efficient** – C programs execute quickly and use memory efficiently because it is a low-level, compiled language.
- **Portability** – C programs can run on different types of computers and operating systems with little or no modification.
- **System programming** – It is widely used to develop operating systems, compilers, and embedded systems (e.g., UNIX was written in C).
- **Rich library support** – C provides many built-in functions that simplify complex tasks.
- **Structured programming** – It supports breaking a large program into smaller functions, making code easier to understand and debug.

---

## 2. Explain the basic structure of a C program with a suitable figure. (03 marks)

A C program follows a fixed structure, executed from top to bottom:

```
Documentation Section
Link Section (Preprocessor Directives)
Definition Section
Global Declaration Section
main() Function Section
{
    Declaration Part
    Executable Part
}
Sub Program Section (User-defined Functions)
```

**Explanation of each part:**
1. **Documentation Section** – Comments describing the program's purpose (optional).
2. **Link Section** – Contains header files like `#include <stdio.h>` needed for built-in functions.
3. **Definition Section** – Defines constants using `#define` (e.g., `#define PI 3.14`).
4. **Global Declaration Section** – Variables declared outside all functions, accessible throughout the program.
5. **main() Function** – Every C program must have exactly one `main()` function; execution always starts here.
   - **Declaration Part** – Declares variables used in the function.
   - **Executable Part** – Contains statements that perform the actual task.
6. **Sub Program Section** – Contains user-defined functions called from `main()` or elsewhere.

**Example illustrating the structure:**
```c
#include <stdio.h>        // Link Section
#define PI 3.14            // Definition Section
int x = 10;                 // Global Declaration

int main()                  // main() Function
{
    int a, b;               // Declaration Part
    a = 5;                  // Executable Part
    b = a + x;
    printf("%d", b);
    return 0;
}

void display()               // Sub Program Section
{
    printf("Hello");
}
```

---

## 3. What are the steps involved in executing a C program? Explain the process of compiling and running a C program with a suitable figure. (05 marks)

**Steps involved in executing a C program:**

1. **Writing/Editing the program** – The source code is written in a text editor and saved with a `.c` extension (e.g., `program.c`).
2. **Preprocessing** – The preprocessor handles directives (like `#include`, `#define`) and expands them into the code, producing an expanded source code.
3. **Compilation** – The compiler translates the preprocessed source code into assembly code, then into **object code** (machine-readable, `.obj` file). Syntax errors are detected at this stage.
4. **Linking** – The linker combines the object code with required library functions and other object files to produce an **executable file** (`.exe`).
5. **Loading** – The executable program is loaded into the computer's main memory (RAM) by the loader.
6. **Execution** – The CPU executes the instructions in the program, and the output is displayed to the user.

**Figure — Compilation and Execution Process:**

```
 Source Code (program.c)
          │
          ▼
   Preprocessor  ───► Expanded Source Code
          │
          ▼
      Compiler   ───► Object Code (program.obj)
          │
          ▼
       Linker     ───► Executable File (program.exe)
                        (links library functions)
          │
          ▼
       Loader     ───► Loads program into memory
          │
          ▼
      Execution   ───► Output displayed
```

**Brief explanation:**
- **Compiling** converts human-readable C code into machine-understandable object code, checking for syntax errors along the way.
- **Running** involves linking the object code with libraries to create an executable, then loading it into memory so the CPU can execute the instructions and produce output.

---

## 4. Discuss the rules of naming a variable in ANSI C with suitable examples. Write down the rules for defining identifiers. (04 marks)

**Rules for naming variables (identifiers) in ANSI C:**

1. **Allowed characters** – A variable name can only contain letters (A-Z, a-z), digits (0-9), and the underscore (`_`).
   - Valid: `sum`, `total_marks`, `x1`
   - Invalid: `total-marks`, `sum#1`

2. **Must start with a letter or underscore** – It cannot begin with a digit.
   - Valid: `_count`, `age`
   - Invalid: `1count`, `2value`

3. **No spaces or special symbols** – Spaces, commas, and symbols like `@`, `%`, `&`, `*` are not allowed.
   - Valid: `student_name`
   - Invalid: `student name`, `student@name`

4. **Case sensitivity** – C is case-sensitive, so `Sum`, `sum`, and `SUM` are treated as three different variables.

5. **Cannot use reserved keywords** – Words that have special meaning in C (like `int`, `float`, `return`, `if`, `while`) cannot be used as variable names.
   - Invalid: `int`, `float`, `for`

6. **Length restriction** – ANSI C allows identifiers up to 31 characters to be significant (though most modern compilers support much longer names).

7. **No two special symbols in a row and must be meaningful** – Good practice recommends using descriptive names, though not a strict compiler rule.

**Examples of valid identifiers:**
```c
int age;
float total_marks;
char _grade;
double studentHeight1;
```

**Examples of invalid identifiers:**
```c
int 1number;     // starts with a digit
float total-marks;  // contains a hyphen
char student name; // contains a space
int float;         // reserved keyword
```

---
