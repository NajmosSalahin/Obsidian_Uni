### Chapter 1: Introduction / Computer Fundamentals

**1.1 Define a computer and explain why it is also referred to as a data processor.**

- **Definition:** A computer is defined as an electronic device that can perform arithmetic operations at high speed.
    
- **Data Processor:** It is referred to as a data processor because it can store, process, and retrieve data whenever desired.
    

1.2 List and briefly describe four characteristic features of a modern computer system.

Based on the text, four key characteristics are:

1. **Automatic:** Once given a job, the computer can work on it automatically without human intervention.
    
2. **Speed:** Computers perform operations at very high speeds, well beyond human capability.
    
3. **Accuracy:** In addition to being fast, computers are incredibly accurate.
    
4. **Diligence:** Computers can perform repetitive tasks without suffering from monotony or tiredness (unlike humans).
    

1.3 What are the three core components involved in the activity of data processing? Explain the relationship between them.

The three core components are Data, Data Processing (Manipulation), and Information.

- **Relationship:** Data acts as the raw material used as input. This data undergoes data processing (manipulating data) within the computer. The final output produced from this processing is Information, which is the processed data.
    

1.4 Describe four key characteristics of the First Generation of computers (1942–1955).

1. **Technology:** They used **vacuum tubes** as the main electronic component.
    
2. **Size:** They were **bulky and large** in size, often occupying entire rooms.
    
3. **Power & Heat:** They consumed a large amount of electricity and generated significant heat, requiring air conditioning.
    
4. **Language:** Programming was done in **machine language** (low-level language), making them difficult to program.
    

**1.5 Identify four pioneers or early computing devices mentioned in the evolution of computers and state their contribution.**

1. **Blaise Pascal:** Invented the first mechanical adding machine in 1642.
    
2. **Baron Gottfried Wilhelm von Leibniz:** Invented the first calculator for multiplication in 1671.
    
3. **Herman Hollerith:** Introduced the concept of punched cards, which were used as input media until the late 1970s.
    
4. **Charles Babbage:** Designed the "Difference Engine" (1822) and the "Analytical Engine" (1842), establishing fundamental principles for digital computer design (considered the father of modern digital computers).
    

---

### **Chapter 2: Basic Computer Organization**

2.1 List and briefly explain the five basic operations performed by a computer system.

The five basic operations are:

1. **Inputting:** The process of entering data and instructions into the computer system.
    
2. **Storing:** Saving data and instructions to make them available for processing.
    
3. **Processing:** Performing arithmetic (add, subtract, etc.) or logical (comparisons) operations on data to convert them into useful information.
    
4. **Outputting:** The process of producing useful information or results for the user (e.g., printed reports or visual display).
    
5. **Controlling:** Directing the manner and sequence in which all the above operations are performed.
    

2.2 State the three main functions performed by the Input Unit of a computer system.

The Input Unit performs the following functions:

1. It **accepts** (or reads) instructions and data from the outside world.
    
2. It **converts** these instructions and data into a computer-acceptable form.
    
3. It **supplies** the converted instructions and data to the computer system for further processing.
    

2.3 Differentiate between Primary Storage and Secondary Storage based on four characteristics (Capacity, Speed, Cost, and Volatility).

|**Characteristic**|**Primary Storage**|**Secondary Storage**|
|---|---|---|
|**Capacity**|Small capacity|Large capacity|
|**Speed**|Fast in operation|Slower than primary storage|
|**Cost**|Expensive|Cheaper (per bit of storage)|
|**Volatility**|Volatile (loses data on power failure)|Non-volatile (retains data without power)|

**2.4 Explain the primary role of the Central Processing Unit (CPU) and list four registers essential to instruction execution.**

- **Role of CPU:** The CPU is the "brain" of the computer responsible for performing all calculations and comparisons (ALU) and controlling the operations of other units (CU).
    
    1. **Program Counter (PC):** Keeps track of the address of the next instruction to be executed.
        
    2. **Instruction Register (IR):** Holds the current instruction being executed.
        
    3. **Memory Address Register (MAR):** Holds the address of the active memory location.
        
    4. **Accumulator (ACC):** Stores intermediate arithmetic and logical results.
        

2.5 List four types of information held (or stored) within the Storage Unit of a computer system.

The storage unit holds:

1. **Data** required for processing (received from input devices).
    
2. **Instructions** required for processing.
    
3. **Intermediate results** of processing.
    
4. **Final results** of processing, before they are released to an output device.
    

---

### **Chapter 3: Number Systems**

**3.1 Distinguish between Non-positional Number Systems and Positional Number Systems, citing two characteristics for each.**

- **Non-positional Number Systems:**
    
    1. Use symbols (like Roman numerals I, II, III) where each symbol represents the same value regardless of its position.
        
    2. It is difficult to perform arithmetic calculations with these systems.
        
- **Positional Number Systems:**
    
    1. The value of a digit depends on its position within the number.
        
    2. There are a limited set of symbols (digits) used to represent values.
        

**3.2 List the four main positional number systems and state the base value for each.**

1. **Decimal Number System:** Base = 10.
    
2. **Binary Number System:** Base = 2.
    
3. **Octal Number System:** Base = 8.
    
4. Hexadecimal Number System: Base = 16.
    
    (Note: The list of systems is in the text, though Octal/Hex bases are standard knowledge.)
    

**3.3 State four characteristics of the Binary Number System.**

1. It is a positional number system.
    
2. It has only **2 symbols** or digits (0 and 1).
    
3. Its **base is 2**.
    
4. The maximum value of a single digit is 1 (one less than the base).
    

3.4 Describe the three factors that determine the value of a digit in a positional number system.

The value of each digit is determined by:

1. The **digit itself**.
    
2. The **position** of the digit in the number.
    
3. The **base** of the number system.
    

3.5 Explain the three steps involved in the process of converting a number of another base (Base b) to the Decimal Number System (Base 10).


1. **Determine the positional value:** Identify the position of each digit (power of the base `b` starting from 0 at the right).
    
2. **Multiply:** Multiply each digit by its corresponding position weight (Base `b` raised to the power of the position).
    
3. **Sum:** Add all the products calculated in the previous step to get the final decimal value.