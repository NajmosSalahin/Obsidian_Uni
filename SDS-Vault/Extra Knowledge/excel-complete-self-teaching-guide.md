# Excel for Data Science — The Complete Self-Teaching Guide

This guide is written so it can be your **only** resource. It doesn't assume you've used Excel beyond basic data entry, and it doesn't assume you'll look anything up elsewhere. Every concept is explained in plain language, every formula is demonstrated on one running example dataset (so you see real numbers go in and real numbers come out), and every section tells you exactly which menu, tab, and button to click.

**How to actually learn this:** don't just read it. Open a blank Excel workbook right now, type in the practice dataset in Part 0, and physically do every example as you reach it. Reading about a VLOOKUP teaches you nothing. Typing one in and watching it pull the right value teaches you everything.

---

## If you only have 3 days

| Day | What to do | Sections |
|---|---|---|
| **Day 1** | Set up the practice dataset. Learn formula basics, clean the data, learn logical and lookup functions. | Parts 0–5 |
| **Day 2** | Learn conditional aggregation, text/date functions, then build your first PivotTable and chart. | Parts 6–11 |
| **Day 3** | Learn conditional formatting, statistics, and advanced formulas. Do the final practice exercise and read the interview Q&A. | Parts 12–15, 21–22 |

Everything else (Power Query, Power Pivot, macros, collaboration tools) is in here for completeness and for your growth *after* you get the job — skim it now, come back to it later.

---

# Part 0: Your Practice Dataset

Everything in this guide builds on **one dataset** so concepts connect to each other instead of feeling like random disconnected examples. Open Excel, create a new workbook, rename Sheet1 to **Orders**, and type this in exactly (including the messiness — it's intentional, you'll clean it in Part 3):

**Orders sheet** — type this starting at cell A1 (row 1 is headers):

| OrderID | CustomerName | Region | Product | Quantity | UnitPrice | OrderDate | Status |
|---|---|---|---|---|---|---|---|
| 1001 | John Smith | East | Laptop | 2 | 800 | 2026-01-05 | Delivered |
| 1002 |   jane doe | West | Mouse | 5 | 15 | 2026-01-06 | Delivered |
| 1003 | Mike Brown | East | Keyboard | 3 | 25 | 2026-01-07 | Pending |
| 1003 | Mike Brown | East | Keyboard | 3 | 25 | 2026-01-07 | Pending |
| 1004 | Sara Lee | North | Monitor | 1 | 200 | 2026-01-08 | Delivered |
| 1005 | DAVID KIM | West | Laptop | 1 | 800 | 2026-01-09 | Cancelled |
| 1006 | Emma Wilson | South | Mouse | 10 | 15 | 2026-01-10 | Delivered |
| 1007 | John Smith | East | Monitor | 2 | 200 | 2026-01-12 | Delivered |
| 1008 | Mike Brown  | North | Keyboard | 4 | 25 | 2026-01-13 | Delivered |
| 1009 | Sara Lee | North | Laptop | 1 | 800 | 2026-01-14 | Pending |
| 1010 | Emma Wilson | South | Monitor | 3 | 200 | 2026-01-15 | Delivered |
| 1011 | JANE DOE | West | Keyboard | 2 | 25 | 2026-01-16 | Delivered |
| 1012 | David Kim | West | Mouse | 6 | 15 | 2026-01-18 | Delivered |
| 1013 | John Smith | East | Mouse | 4 | 15 | 2026-01-19 | Pending |
| 1014 | Sara Lee | North | Mouse | 8 | 15 | 2026-01-20 | Delivered |
| 1015 | Emma Wilson | South | Laptop | 2 | 800 | 2026-01-21 | Delivered |
| 1016 | Mike Brown | East | Monitor | 1 | 200 | 2026-01-22 | Cancelled |
| 1017 | David Kim | West | Monitor | 2 | 200 | 2026-01-23 | Delivered |

Notice row 4 is an exact repeat of row 3 (a duplicate entry — happens constantly in real data), row 2 has extra spaces before "jane doe", row 9 has a trailing space after "Mike Brown", and the same customers appear with inconsistent capitalization (DAVID KIM / David Kim, jane doe / JANE DOE). **Don't fix any of this yet** — you'll learn to fix it properly in Part 3, and seeing the "wrong" numbers first is part of the lesson.

**Column reference for this guide:** A = OrderID, B = CustomerName, C = Region, D = Product, E = Quantity, F = UnitPrice, G = OrderDate, H = Status. Row 1 is headers, so your data runs from row 2 to row 19 (18 rows of data, rows 2–19).

Now add a second sheet called **Products** (right-click any sheet tab → Insert, or click the `+` next to the sheet tabs) and type this:

**Products sheet:**

| Product | Category | ReorderLevel |
|---|---|---|
| Laptop | Electronics | 5 |
| Mouse | Accessories | 20 |
| Keyboard | Accessories | 15 |
| Monitor | Electronics | 8 |

You now have a small but realistic two-table setup — exactly the shape of real business data: one table of transactions, one small reference/lookup table. Keep both workbooks open as you go through every section below.

---

# Part 1: Getting Oriented in Excel

Before formulas, you need to know what you're looking at.

- **Workbook** = the whole file (e.g., `Practice.xlsx`). **Worksheet** (or "sheet") = one tab inside it (you now have "Orders" and "Products"). **Cell** = a single box, named by its column letter + row number (e.g., `C5`). **Range** = a rectangular group of cells, written as `top-left:bottom-right` (e.g., `A2:H19` is your whole Orders table).
- **The Ribbon** (the toolbar across the top) is organized into tabs. The ones you'll live in:
  - **Home** — fonts, colors, number formats, basic editing
  - **Insert** — tables, charts, PivotTables
  - **Formulas** — the function library, formula auditing tools
  - **Data** — sort, filter, data validation, Power Query ("Get & Transform"), what-if analysis
  - **Review** — comments, protect sheet
  - **View** — freeze panes, gridlines
- **The Name Box** (top-left, shows the active cell's address) and the **Formula Bar** (the long bar next to it, shows the actual formula in the selected cell, not just its displayed result) — these two are how you'll constantly check "what is actually in this cell."
- **Sheet tabs** at the bottom let you switch between Orders and Products, or add new sheets.

### Navigating efficiently
- `Ctrl + Arrow key` — jump to the last filled cell in that direction (e.g., from A2, `Ctrl+Down` jumps straight to A19, the bottom of your data).
- `Ctrl + Home` — jump to A1. `Ctrl + End` — jump to the last used cell.
- `Ctrl + G` (or `F5`) — "Go To" a specific cell by typing its address.
- Click and drag the small square at the bottom-right corner of a selected cell (the **fill handle**) to copy a formula or pattern down a column — you'll use this constantly.

### Saving
Save your practice file as `.xlsx` (File → Save As). You'll also hear about `.csv` (plain data, no formulas or formatting — what you get from databases/exports) and `.xlsm` (a workbook that contains macros). For everything in this guide, `.xlsx` is what you want.

---

# Part 2: Formula Fundamentals

This is the single most important section in the entire guide. Almost everything else is "more functions" built on these rules.

### The four rules of every formula
1. Every formula starts with `=`. Without it, Excel treats what you type as plain text or a number, not an instruction.
2. You reference other cells by their address: `=E2*F2` means "take whatever number is in E2, multiply it by whatever number is in F2."
3. Standard operators work as you'd expect: `+` add, `-` subtract, `*` multiply, `/` divide, `^` power (e.g., `=2^3` is 8), `%` percent.
4. Order of operations is the same as basic math: parentheses first, then `^`, then `*`and `/`, then `+` and `-`. When unsure, just add parentheses — `=(E2*F2)+10` is always safer than guessing.

### Your first real formula: build a Revenue column
Go to your **Orders** sheet, type `Revenue` in **I1**, then click **I2** and type:

```
=E2*F2
```

Press Enter. You should see **1600** appear (Quantity 2 × UnitPrice 800 for order 1001). That's your first calculated column.

Now select I2 again, grab the **fill handle** (the small square at the bottom-right of the cell) and drag it down to I19. Excel automatically adjusts the formula for every row — I3 becomes `=E3*F3`, I4 becomes `=E4*F4`, and so on. This automatic adjustment is called a **relative reference**, and it's the default behavior.

**Check yourself:** I2 should read 1600, I9 (order 1008) should read 100, I19 (order 1017) should read 400. If your numbers don't match, double check you typed the dataset exactly as given.

### Relative vs. absolute references — the concept that trips everyone up
Type `8` into cell **K1** (this will represent a hypothetical "tax rate %" — pretend it's 8%, so really store `0.08` — go back and type `0.08` instead). Now in **L2**, try:

```
=I2*K1
```

Drag this down to L19. You'll see it break — because as the formula copies down, `K1` shifts too (it becomes `K2`, `K3`, an empty cell), so you get zeros or errors instead of a consistent tax calculation. This is the single most common beginner mistake in Excel.

**The fix:** lock the reference to K1 with dollar signs, so it never shifts no matter where you copy the formula:

```
=I2*$K$1
```

Now drag it down again — every row correctly multiplies its own Revenue by the same fixed K1 value. `$K$1` is called an **absolute reference**. The `$` before the column letter locks the column; the `$` before the row number locks the row. You can also mix them (`$K1` locks only the column, `K$1` locks only the row) for more advanced layouts, but for now just remember: **if a formula refers to one fixed "settings" cell that should never change as you copy the formula, put `$` in front of both the column letter and row number.**

*Shortcut:* with your cursor inside a cell reference in the formula bar, press `F4` to cycle through `A1` → `$A$1` → `A$1` → `$A1` automatically.

You can delete columns K and L now — they were just to demonstrate the concept.

### AutoSum and quick aggregation
Click an empty cell below your Revenue column (e.g., I20) and either type `=SUM(I2:I19)` or use the **Σ AutoSum** button on the Home tab, which guesses the range for you. You should get **7395** — that's the total of all 18 rows including the duplicate (you'll see this number change once you clean the data in Part 3, which is itself a useful lesson in why cleaning matters before you trust any total).

### Reading and fixing formula errors
You will see these constantly. Knowing what each one means instantly makes you look competent:

| Error | What it means | Typical fix |
|---|---|---|
| `#REF!` | The formula refers to a cell that no longer exists (you deleted a row/column it depended on) | Rebuild the reference |
| `#VALUE!` | You're doing math on something that isn't a number (e.g., text in a cell you're trying to multiply) | Check the cell's actual content/type |
| `#NAME?` | Excel doesn't recognize a function name (usually a typo, like `=VLOOKKUP`) | Check spelling |
| `#N/A` | A lookup function couldn't find a match | Check the lookup value exists, and check for extra spaces (see Part 3!) |
| `#DIV/0!` | You divided by zero or an empty cell | Wrap with `IFERROR` (Part 4) or check the denominator |
| `#NUM!` | A formula produced a number too large/invalid for Excel, or an invalid argument | Check your inputs |
| `#####` | Not actually an error — the column is just too narrow to display the number | Widen the column |

You now know enough to build and debug any basic formula. Everything from here is just new vocabulary — new functions — applied to the exact same `=FUNCTION(arguments)` pattern.

---

# Part 3: Data Cleaning — Making the Data Trustworthy

In a real data science role, this is where most of your time actually goes — not fancy analysis, but making sure the numbers are even correct before you analyze them. Let's clean the mess you typed in Part 0.

### Removing the duplicate row
Rows 3 and 4 (OrderID 1003, both Mike Brown, both Keyboard) are identical — a classic double-entry error. Select your full data range A1:H19, then **Data tab → Remove Duplicates**. A dialog appears letting you pick which columns to check for duplication — leave all columns checked (meaning "only remove rows where every column matches") and click OK. Excel will report it removed 1 duplicate row, leaving 17 unique rows.

Re-check your Revenue total (`=SUM(I2:I18)` now, since you have one fewer row): it should now read **7320** instead of 7395. That 75-unit difference was a phantom order that never should have counted — exactly why cleaning comes before analysis, not after.

### Fixing inconsistent text: TRIM, CLEAN, and PROPER
Your CustomerName column has three separate problems: extra leading/trailing spaces, inconsistent CAPITALIZATION, and (as a result) what looks like 6 customers is actually still 6 people, but a naive count could get confused by the spacing.

Add a new column **J**, header `CleanName`, and in J2 type:

```
=PROPER(TRIM(B2))
```

This is a **nested formula** — Excel evaluates the inside function first. `TRIM(B2)` strips leading, trailing, and repeated internal spaces. `PROPER(...)` then capitalizes the first letter of each word. Drag this down to J18. Row 2 (`  jane doe`) should now correctly read `Jane Doe`.

**Important nuance worth knowing for an interview:** Excel's comparison functions (`COUNTIF`, `SUMIF`, `VLOOKUP`, `MATCH`, and the `=` operator) already **ignore capitalization** by default — `"jane doe"` and `"JANE DOE"` are treated as the same text. What they do **not** ignore is extra spaces — `"  jane doe"` and `"jane doe"` are treated as *different* text, because the characters literally don't match. So `TRIM` is the fix that actually matters for accurate counts; `PROPER` is mostly for how the data *looks* to a human reader.

Once J2:J18 looks right, you'd normally select the column, Copy (`Ctrl+C`), then **Paste Special → Values Only** on top of column B to lock in the clean text and delete the now-redundant column J. (Paste Special → Values is how you convert any formula's *result* into permanent text/numbers — useful any time you want to "freeze" a calculated column.)

### Other cleaning tools you should know
- **Find & Replace** (`Ctrl+H`): swaps text across a whole sheet at once. Supports wildcards: `*` matches any number of characters, `?` matches exactly one. E.g., finding `Mon*` would match "Monitor" and "Monday."
- **Text to Columns** (Data tab): splits one column into several based on a delimiter (comma, space, etc.) or fixed character width. Classic use case: a column pasted from another system as `"Smith, John"` that you need split into separate First/Last columns.
- **Flash Fill** (`Ctrl+E`): type the *result* you want in the first one or two rows next to a column (e.g., type "John" next to "John Smith" manually), and Excel detects the pattern and fills the rest automatically. Great for quick one-off extractions without writing a formula.
- **CLEAN()**: removes non-printable characters that sometimes come along with text copied from websites or other software — invisible characters that look fine but break formula matching. Use it the same way as TRIM, often nested together: `=PROPER(TRIM(CLEAN(B2)))`.

You now have a clean, trustworthy 17-row dataset. Every example from here forward assumes you're working with the cleaned version.

---

# Part 4: Logical Functions — Teaching Excel to Make Decisions

These functions let a cell's result depend on a condition, instead of always being a fixed calculation.

### IF — the building block
Syntax: `=IF(condition, value_if_true, value_if_false)`

Add column **K**, header `OrderSize`, and in K2:

```
=IF(I2>500,"High Value","Standard")
```

Drag down. Order 1001 (Revenue 1600) should show "High Value"; order 1003 (Revenue 75) should show "Standard." The condition (`I2>500`) can use `>`, `<`, `>=`, `<=`, `=`, or `<>` (not equal to).

### Nested IF and IFS — more than two outcomes
If you need more than two outcomes, you can nest IFs inside each other:

```
=IF(I2>1000,"High",IF(I2>300,"Medium","Low"))
```

This reads as: if Revenue > 1000, "High"; otherwise, if Revenue > 300, "Medium"; otherwise, "Low." Excel checks conditions in order and stops at the first one that's true.

Once you have more than 2–3 conditions, nested IFs get hard to read. `IFS` is a cleaner way to write the exact same logic:

```
=IFS(I2>1000,"High",I2>300,"Medium",TRUE,"Low")
```

The `TRUE` at the end acts as a catch-all "else" — without it, any value that doesn't match an earlier condition returns an error instead of a result.

### AND / OR — combining conditions
```
=IF(AND(C2="East",I2>500),"East + High Value","Other")
=IF(OR(H2="Cancelled",H2="Pending"),"Not Delivered","Delivered")
```

`AND` requires every condition to be true; `OR` requires at least one to be true.

### IFERROR — catching errors gracefully
Wrap any formula that *might* error (most commonly lookups) so a missing match shows something useful instead of an ugly `#N/A`:

```
=IFERROR(some_formula_here, "Not Found")
```

You'll use this constantly once you start doing lookups, which is exactly what's next.

---

# Part 5: Lookup Functions — Pulling Data From Another Table

This is the most-tested Excel skill in interviews, and the one that most separates "knows data entry" from "can actually work with data." The task: pull each order's product **Category** from your Products sheet into the Orders sheet, matching on Product name.

### VLOOKUP
Syntax: `=VLOOKUP(lookup_value, table_array, column_index_number, exact_match)`

Add column **L** on the Orders sheet, header `Category`, and in L2 type:

```
=VLOOKUP(D2, Products!$A$2:$C$5, 2, FALSE)
```

Breaking this down:
- `D2` — the value you're looking up (the Product name in this row, e.g. "Laptop")
- `Products!$A$2:$C$5` — the table to search in. Note the `Products!` prefix tells Excel which sheet, and the `$` locks the range so it doesn't shift when you drag the formula down (always lock your lookup table range — see Part 2 on absolute references)
- `2` — which column of that range to return a value from (column A=1 is Product, B=2 is Category, C=3 is ReorderLevel — so `2` returns Category)
- `FALSE` — means "exact match only." Always use `FALSE` unless you specifically need approximate matching (which is rare and easy to get wrong). Leaving this out, or using `TRUE`, is the single most common VLOOKUP bug.

Drag down to L18. Order 1001 (Laptop) should show "Electronics"; order 1003 (Keyboard) should show "Accessories."

**The catch with VLOOKUP:** it can only look to columns *to the right* of your lookup column, and it breaks silently if someone inserts a new column inside the table range. That's exactly why INDEX-MATCH became the traditional "professional" alternative.

### INDEX + MATCH — the more flexible classic
This is two functions working together. `MATCH` finds the *position* of a value; `INDEX` returns the value at a given position. Combined:

```
=INDEX(Products!$B$2:$B$5, MATCH(D2, Products!$A$2:$A$5, 0))
```

Read it inside-out: `MATCH(D2, Products!$A$2:$A$5, 0)` finds *where* in the Product column "Laptop" sits (position 1). `INDEX(Products!$B$2:$B$5, 1)` then returns whatever is in position 1 of the Category column. The `0` in MATCH means exact match (same idea as `FALSE` in VLOOKUP).

The advantage: you can look up values to the *left* of the lookup column, and the formula doesn't break if someone inserts a column in between — because each piece refers to a single column, not a fixed numbered position.

### XLOOKUP — the modern replacement (Excel 365 / 2021+)
If your version of Excel has it, this does what INDEX-MATCH does with far simpler syntax:

```
=XLOOKUP(D2, Products!$A$2:$A$5, Products!$B$2:$B$5, "Not Found")
```

That's: lookup value, the column to search, the column to return from, and an optional 4th argument for what to show if nothing matches (no more wrapping in IFERROR).

**What to actually say in an interview:** *"VLOOKUP only searches left-to-right and breaks if columns shift. INDEX-MATCH is more flexible and was the professional standard for years. XLOOKUP is the modern function that replaces both with simpler, more robust syntax — I'd use XLOOKUP if it's available, INDEX-MATCH if it's not."* That single sentence demonstrates real fluency, not just memorized syntax.

### A deliberate error, on purpose
Go to cell M1, type "Webcam", and in M2 try `=VLOOKUP(M1, Products!$A$2:$C$5, 2, FALSE)`. Since "Webcam" doesn't exist in your Products table, you'll get `#N/A`. Now wrap it: `=IFERROR(VLOOKUP(M1, Products!$A$2:$C$5, 2, FALSE), "Not Found")`. This is the realistic pattern you'll use anywhere a lookup might legitimately fail (new products, typos, missing records).

---

# Part 6: Conditional Aggregation — SUMIF, COUNTIF, AVERAGEIF

These answer "what's the total/count/average **of just the rows that match a condition**?" — arguably the single most common real-world Excel task.

### SUMIF — sum with one condition
Syntax: `=SUMIF(range_to_check, condition, range_to_sum)`

In an empty area (say, starting at cell N1), build a small summary table:

| | Region | Total Revenue |
|---|---|---|
| | East | `=SUMIF($C$2:$C$18,O2,$I$2:$I$18)` |
| | West | (same formula, dragged down) |
| | North | |
| | South | |

If you type "East", "West", "North", "South" in O2:O5 and put the SUMIF formula in P2 then drag it down, you should get exactly:

| Region | Total Revenue |
|---|---|
| East | 2335 |
| West | 1415 |
| North | 1220 |
| South | 2350 |

If your numbers match, your cleaning from Part 3 and your formula are both correct — this is a great self-check.

### SUMIFS — sum with multiple conditions
Add an "S" and you can stack conditions, in pairs of (range, condition):

```
=SUMIFS($I$2:$I$18, $C$2:$C$18, "East", $H$2:$H$18, "Delivered")
```

This sums Revenue only where Region is East **and** Status is Delivered — narrower than the SUMIF above. Try it and you should get **2000** (Laptop 1600 + Monitor 400, excluding the Pending Keyboard and Mouse orders).

### COUNTIF / COUNTIFS — counting instead of summing
Same idea, but counts matching rows instead of summing a column:

```
=COUNTIF($H$2:$H$18,"Delivered")
```

This should return **12**. Try `=COUNTIF($H$2:$H$18,"Pending")` (should be **3**) and `=COUNTIF($H$2:$H$18,"Cancelled")` (should be **2**) — 12+3+2 = 17, matching your total row count, which is a good way to sanity-check you haven't miscounted.

### AVERAGEIF / AVERAGEIFS
```
=AVERAGEIF($D$2:$D$18,"Mouse",$I$2:$I$18)
```

This averages Revenue for just the Mouse orders. You should get **99** — Excel found the five Mouse orders (75, 150, 90, 60, 120) and averaged them. If you only counted four and got 108.75, you missed that order 1013 ("John Smith," Region East) is also a Mouse order — a good reminder to always double-check by filtering rather than trusting your own scan of the data (Part 9 covers filtering properly).

### MAXIFS / MINIFS
Same pattern again: `=MAXIFS($I$2:$I$18,$D$2:$D$18,"Laptop")` gives you the highest revenue among Laptop orders (1600).

**The pattern to memorize:** every one of these functions follows *"the range to check, the condition to match, then (for SUM/AVERAGE/MAX/MIN) the range to actually calculate."* Once that clicks, you can write all of them from memory.

---

# Part 7: Text Functions — Reshaping and Extracting Text

You already used `TRIM` and `PROPER` in Part 3. Here's the rest of the text toolkit, with examples on your data.

| Function | Example (on your data) | Result | What it does |
|---|---|---|---|
| `LEFT` | `=LEFT(B2,4)` | "John" | First 4 characters from the left |
| `RIGHT` | `=RIGHT(B2,5)` | "Smith" | Last 5 characters from the right |
| `MID` | `=MID(B2,6,5)` | "Smith" | 5 characters starting at position 6 |
| `LEN` | `=LEN(B2)` | 10 | Counts total characters (useful for spotting hidden extra spaces — compare LEN before/after TRIM) |
| `FIND` | `=FIND(" ",B2)` | 5 | Position of the first space — often used inside LEFT/MID to split names without knowing the length in advance |
| `CONCAT` or `&` | `=C2&" - "&D2` | "East - Laptop" | Joins text together. The `&` operator does the same thing inline, without needing a function: `=C2&" - "&D2` |
| `TEXTJOIN` | `=TEXTJOIN(", ",TRUE,D2:D5)` | "Laptop, Mouse, Keyboard, Monitor" | Joins a whole range with a delimiter in one go; the `TRUE` tells it to skip any blank cells |
| `TEXT` | `=TEXT(I2,"$#,##0")` | "$1,600" | Formats a number as text in a specific display format — useful for building readable labels/sentences that include numbers |
| `SUBSTITUTE` | `=SUBSTITUTE(B2,"Smith","S.")` | "John S." | Replaces a specific piece of text within a string |

**A practical combo:** to build a one-line order summary like "John Smith ordered 2 Laptop(s) for $1,600", you'd write:

```
=B2&" ordered "&E2&" "&D2&"(s) for "&TEXT(I2,"$#,##0")
```

This kind of formula is exactly what shows up in real reporting — joining clean values from several columns into one readable sentence.

---

# Part 8: Date Functions

Your OrderDate column (G) is a real date value, not text — which is what lets Excel do math on it.

| Function | Example | What it does |
|---|---|---|
| `TODAY()` | `=TODAY()` | Current date (updates automatically every day) |
| `DATEDIF` | `=DATEDIF(G2,TODAY(),"d")` | Days between OrderDate and today ("d"=days, "m"=months, "y"=years) |
| `YEAR` / `MONTH` / `DAY` | `=MONTH(G2)` | Extracts just that part of a date — returns `1` for any January date |
| `EOMONTH` | `=EOMONTH(G2,0)` | Last day of the order's month (use `1` instead of `0` for next month's end, `-1` for last month's) |
| `NETWORKDAYS` | `=NETWORKDAYS(G2,TODAY())` | Counts only business days (Mon–Fri) between two dates — useful for SLA/turnaround calculations |
| `WEEKDAY` | `=WEEKDAY(G2)` | Day of week as a number (1=Sunday by default) |

**Why this matters for analysis:** once a column is recognized as a true date (not text that merely *looks* like a date), you can group, sort, and filter by month/quarter/year instantly — which is exactly what you'll do in the PivotTable section next. A quick way to check: if `=MONTH(G2)` returns an error, your date is actually stored as text and needs to be fixed first (select the column → Data tab → Text to Columns → Finish, which often auto-converts text dates into real dates).

---

# Part 9: Organizing Data — Tables, Named Ranges, Sort & Filter

### Convert your range into an official Table
Click any cell inside A1:L18 (or wherever your data currently ends), then press `Ctrl+T`. Confirm "My table has headers" is checked, click OK. This does several useful things at once:
- The range gets a name (check the Table Design tab to rename it from "Table1" to something like `OrdersTbl`)
- It auto-expands when you add new rows or columns right below/beside it
- Formulas referencing it can use **structured references** instead of cell addresses — e.g. `=SUM(OrdersTbl[Revenue])` instead of `=SUM(I2:I18)`, which stays correct automatically even as rows are added
- A filter dropdown arrow appears automatically on every header

**Do this before building PivotTables on real data** — it means your Pivot will automatically include new rows in the future without you having to manually expand its source range.

### Named Ranges
Formulas tab → Define Name. This lets you name a single cell or range and refer to it by that name anywhere — e.g. naming cell `K1` as `TaxRate` lets you write `=I2*TaxRate` instead of `=I2*$K$1`, which is both more locked-down (no risk of forgetting the `$`) and more readable.

### Sorting
Data tab → Sort. You can sort by multiple levels at once (e.g., primarily by Region, then within each region by Revenue descending) — click "Add Level" in the Sort dialog for each additional rule.

### Filtering
With your Table's filter dropdowns (from `Ctrl+T` above), click any header's dropdown arrow to filter to specific values, or use the search box to filter to text containing something. Try filtering Status to only "Delivered" — you should see exactly 12 rows remain, matching your COUNTIF result from Part 6.

For more complex criteria (e.g., "Region = East AND Revenue > 300"), use **Advanced Filter** (Data tab) — it reads its conditions from a separate small criteria range you set up elsewhere on the sheet, rather than from dropdown clicks.

---

# Part 10: PivotTables — The Most Important Skill in This Guide

A PivotTable summarizes thousands of rows into a small, readable table in seconds, without writing a single formula. This is the skill that will be tested in almost every Excel-for-data interview or assessment. Let's build one from scratch, step by step.

### Step 1: Build it
1. Click anywhere inside your Orders table.
2. Go to **Insert tab → PivotTable**.
3. In the dialog, confirm the table/range is correct, choose **New Worksheet**, click OK. A new sheet appears with a blank Pivot grid on the left and a **Field List** panel on the right showing all your column headers (OrderID, CustomerName, Region, Product, Quantity, UnitPrice, OrderDate, Status, Revenue, OrderSize, Category...).

### Step 2: Place your fields
The Field List panel has four boxes at the bottom: **Filters**, **Columns**, **Rows**, **Values**. Drag fields into them like this:
- Drag **Region** into the **Rows** box
- Drag **Product** into the **Columns** box
- Drag **Revenue** into the **Values** box

Excel instantly builds a grid. By default it will show "Sum of Revenue" because Revenue is numeric. If your data is clean (Part 3 done correctly), your finished PivotTable should show **exactly** this:

| Sum of Revenue | Keyboard | Laptop | Monitor | Mouse | Grand Total |
|---|---|---|---|---|---|
| **East** | 75 | 1600 | 600 | 60 | 2335 |
| **North** | 100 | 800 | 200 | 120 | 1220 |
| **South** | 0 (blank) | 1600 | 600 | 150 | 2350 |
| **West** | 50 | 800 | 400 | 165 | 1415 |
| **Grand Total** | 225 | 4800 | 1800 | 495 | 7320 |

If your numbers match this exactly, every formula and cleaning step you've done so far in this guide is correct — this table is your proof. (South shows blank/0 for Keyboard simply because no South orders happened to be for keyboards in this dataset — completely normal.)

### Step 3: Change the calculation
Click the "Sum of Revenue" field (either in the grid or in the Values box) → **Value Field Settings**. You can switch from Sum to Count, Average, Max, Min, and more — try **Count of Revenue** to instead see how many *orders* (not how much revenue) happened per region/product combination.

### Step 4: Show values as a percentage
Right-click any number inside the Pivot grid → **Show Values As → % of Grand Total**. Instantly every cell becomes a percentage of the 7320 total instead of a raw dollar figure — useful for "what share of revenue comes from each region" type questions without any extra formulas.

### Step 5: Group dates
Drag **OrderDate** into Rows (replacing or alongside Region). Right-click any date in the grid → **Group** → choose **Months** (and Years, if your data spanned multiple years). This rolls 18 individual order dates up into clean monthly buckets — exactly how you'd build a "revenue by month" summary on a real, much larger dataset.

### Step 6: Add a calculated field
PivotTable Analyze tab (appears when you click inside the Pivot) → **Fields, Items & Sets → Calculated Field**. Name it `AvgOrderValue`, and set the formula to `=Revenue/Quantity` (referencing the field names directly, no cell addresses). This adds a new field to your Values area computed from your existing Pivot fields — useful any time the metric you want isn't a column in your raw data but is derivable from columns that are.

### Step 7: Slicers — turn it into an interactive filter
PivotTable Analyze tab → **Insert Slicer** → check "Status". A small floating button panel appears with "Delivered / Pending / Cancelled" as clickable buttons. Click "Delivered" and your whole Pivot instantly recalculates to show only delivered orders. This is what makes a Pivot feel like a live dashboard instead of a static table — and it's a one-click feature, not a formula.

**What to say in an interview:** *"I'd start with a PivotTable to get a fast summary of the data — rows for the category I'm grouping by, values for the metric, then add slicers so the summary is interactive rather than static."* That sentence alone covers what most interviewers are actually listening for.

---

# Part 11: Charts & Visualization

### Building a chart from your PivotTable
Click inside your PivotTable from Part 10 → **PivotTable Analyze tab → PivotChart** → choose **Clustered Column** → OK. You now have a bar chart of Revenue by Region and Product that updates live if you click your slicer buttons or change the underlying data. This "PivotChart" approach (rather than a static chart) is what you want whenever the data might change or the viewer needs to filter it themselves.

### Choosing the right chart type
| Chart type | Use it for |
|---|---|
| **Column / Bar** | Comparing totals across categories (e.g., Revenue by Region) — your default choice for most business comparisons |
| **Line** | Showing a trend over time (e.g., Revenue by Month) |
| **Scatter** | Showing the relationship between two numeric variables (e.g., Quantity vs. Revenue) — this is the one true "data science" chart type, used to visually spot correlation |
| **Pie** | Share of a whole, but only when you have a small number of categories (4–5 max) — bar charts are almost always clearer, so use pie sparingly |
| **Combo** | Mixing two chart types on one chart with two different scales (e.g., bars for Revenue + a line for Order Count) — Insert tab → Recommended Charts → Combo |

### A quick scatter chart, by hand
Select your Quantity (E) and Revenue (I) columns (hold `Ctrl` to select two non-adjacent columns) → **Insert tab → Scatter**. You'll get a cloud of 17 points. This is the same data you'll formally analyze with `CORREL` in Part 14 — looking at the scatter first, before the formula gives you a number, is good practice for building real intuition about your data.

### Sparklines
Insert tab → Sparklines → Line (or Column). Select a row of data as the source and a single cell as the destination — you get a tiny in-cell mini-chart. Useful in dashboards where you want a trend indicator next to every row without taking up a full chart's worth of space.

### Trendlines
Right-click any data series on a Line or Scatter chart → **Add Trendline**. Check "Display Equation on chart" and "Display R-squared value" to see the linear fit directly on the chart — a fast visual companion to the `TREND`/`FORECAST.LINEAR` formulas in Part 15.

---

# Part 12: Conditional Formatting & Data Validation

### Conditional Formatting — make patterns visible at a glance
Select your Revenue column (I2:I18). **Home tab → Conditional Formatting**:
- **Color Scales** instantly shades every cell from low (e.g., red) to high (e.g., green) — great for scanning a long column for outliers in seconds.
- **Data Bars** draws a small in-cell bar proportional to the value — like a tiny built-in chart inside the cell itself.
- **Highlight Cells Rules → Greater Than** — type `500` to highlight every order above 500 in one click.
- **Custom Formula rule** (Conditional Formatting → New Rule → "Use a formula to determine which cells to format") is the most powerful option, because it can reference *other* cells. For example, select your whole H column (Status) and use the formula `=$H2="Cancelled"` to highlight every cancelled order red — this references the Status column to format rows, which the simpler built-in rules can't do.

### Data Validation — preventing bad data at the source
This is the cleaning tool you apply *before* messy data ever gets typed in, rather than fixing it after (Part 3). Select your Status column (H2:H18), **Data tab → Data Validation**:
- **Allow: List**, **Source:** type `Delivered,Pending,Cancelled` (comma-separated, no spaces) — this turns the cell into a dropdown, so whoever enters data can only pick from those three exact values, eliminating the "delivered" vs "Delivered" vs "DELIVERED" inconsistency you cleaned up earlier.
- **Allow: Whole Number** with a Minimum/Maximum — restricts entry to a numeric range (e.g., Quantity must be between 1 and 1000).
- **Allow: Custom**, with a formula — the most flexible option, lets you validate against any logical condition you can write as a formula.

You can also add an **Input Message** (a tooltip shown when the cell is selected) and an **Error Alert** (a popup shown if someone tries to enter something invalid) under the other tabs of the same dialog — useful for building forms that other, less Excel-fluent people will fill in.

---

# Part 13: What-If Analysis

These tools work backwards or explore multiple scenarios, instead of calculating forward from fixed inputs.

### Goal Seek — "what input gives me this output?"
Suppose you want to know: what quantity would order 1001 (currently 2 Laptops, Revenue 1600 in cell I2) need to be, for Revenue to hit exactly 2000?

You could do the algebra yourself (2000 ÷ 800 = 2.5), but on a more complex formula you often can't. Instead: **Data tab → What-If Analysis → Goal Seek**.
- **Set cell:** I2 (the Revenue formula)
- **To value:** 2000
- **By changing cell:** E2 (the Quantity)

Click OK. Excel iterates automatically and sets E2 to **2.5**, which makes I2 read 2000. (Revert E2 back to 2 afterward, or undo with `Ctrl+Z`.) Goal Seek only works backward through **one** changing cell at a time — for anything more complex, you'd move to Data Tables or build the algebra by hand.

### Data Tables — see a range of outcomes at once
A **Data Table** (different from an Excel Table from Part 9) lets you see how a formula's result changes across a whole range of possible inputs, in a grid, without manually trying each one. Data tab → What-If Analysis → Data Table. One-variable Data Tables show outcomes across a range of one input (e.g., Revenue at every Quantity from 1 to 10); two-variable Data Tables show outcomes across two inputs at once (e.g., Revenue at every combination of Quantity and UnitPrice).

### Scenario Manager — save and compare named "what-if" sets
Data tab → What-If Analysis → Scenario Manager. Lets you save multiple named sets of input values (e.g., "Best Case", "Worst Case", "Most Likely") for the same set of cells, then switch between them or generate a summary comparing all of them side by side — useful for budget or forecast planning where you want to present a few discrete possibilities rather than one number.

---

# Part 14: Statistical Functions

These move you from "summarizing" data (Parts 6 and 10) to actually *characterizing* it — spread, relationships, and relative position. All examples below use your cleaned Revenue column (I2:I18, 17 values).

| Function | Formula | Your result | What it tells you |
|---|---|---|---|
| AVERAGE | `=AVERAGE(I2:I18)` | 430.59 | The mean order revenue |
| MEDIAN | `=MEDIAN(I2:I18)` | 200 | The middle value — notice this is far below the average, which tells you the data is skewed by a few large orders (the 1600s) pulling the mean upward |
| STDEV.S | `=STDEV.S(I2:I18)` | 505.00 | Sample standard deviation — how spread out revenue is around the average. A standard deviation (505) larger than the average itself (430.59) confirms what MEDIAN already hinted at: this data is highly variable, not tightly clustered |
| PERCENTILE | `=PERCENTILE(I2:I18,0.75)` | 600 | 75% of orders have revenue at or below 600 |
| PERCENTILE | `=PERCENTILE(I2:I18,0.9)` | 1120 | 90th percentile — useful for spotting "top tier" orders |
| LARGE | `=LARGE(I2:I18,1)` | 1600 | The single highest value (use `LARGE(range,2)` for 2nd highest, etc.) |

**Use STDEV.S (not STDEV.P) by default** — `.S` treats your data as a *sample* of a larger population (the normal real-world case); `.P` treats it as the *entire* population and is only correct when your data genuinely is every possible data point, not just a sample of it.

### CORREL — measuring the relationship between two variables
```
=CORREL(E2:E18, I2:I18)
```

This measures how Quantity relates to Revenue, returning **−0.40**. Correlation ranges from −1 (perfectly inverse) to +1 (perfectly aligned); 0 means no relationship.

**This result is genuinely interesting, not just a number to report** — you might expect "more units ordered = more revenue," but it's actually *negatively* correlated here. Why? Because Laptops (the highest-revenue product) are typically ordered in small quantities (1–2 units), while Mice and Keyboards (low unit price) are sometimes ordered in bulk (5–10 units). **Quantity alone doesn't drive revenue here — unit price does.** Being able to notice and explain a counter-intuitive result like this, instead of just stating the number, is exactly the kind of thinking a data role is testing for.

### RANK — ranking values
Build a small summary first, in a fresh empty area like column R (not the N:P area you used for the region summary in Part 6): list your 6 unique customers (use your cleaned names from Part 3) in R2:R7, then in S2 use `=SUMIF($J$2:$J$18,R2,$I$2:$I$18)` and drag down to get each customer's total revenue. Then rank them:

```
=RANK.EQ(S2, $S$2:$S$7, 0)
```

(the final `0` means rank highest-to-lowest; use `1` for lowest-to-highest). On this data, your customers should rank: Emma Wilson (2350, rank 1), John Smith (2060, rank 2), David Kim (1290, rank 3), Sara Lee (1120, rank 4), Mike Brown (375, rank 5), Jane Doe (125, rank 6) — note Jane Doe and Mike Brown rank lowest specifically *because* their orders happened to be small-ticket items (Mouse/Keyboard), tying directly back to the correlation insight above.

### The Analysis ToolPak (one-click statistics)
For more advanced stats (regression, ANOVA, histograms) without writing formulas by hand: **File → Options → Add-ins → Manage: Excel Add-ins → Go → check "Analysis ToolPak" → OK.** It then appears under the Data tab as **Data Analysis**. Selecting **Regression** and pointing it at, say, Quantity (X) and Revenue (Y) gives you a full regression output (coefficients, R², p-values) in one click — the bridge between basic Excel and proper statistical analysis.

---

# Part 15: Advanced Formulas

These are newer, more powerful tools. If your Excel version doesn't have them (they require Excel 365 or Excel 2021+), skip to Part 16 — but recognize the names, since interviewers increasingly expect awareness of them even if you can't demo them live.

### Dynamic Arrays — formulas that "spill" into multiple cells
Older Excel formulas return one value per cell. Dynamic array functions return a whole list that automatically spills into the cells below/right of the formula, with no dragging required.

```
=UNIQUE(J2:J18)
```

Typed into a single empty cell, this spills out a list of your 6 unique cleaned customer names automatically — no manual dedup needed for a quick lookup list (note: this is for *display/reference*, it doesn't modify your actual data the way Remove Duplicates in Part 3 did).

```
=FILTER(A2:H18, H2:H18="Delivered")
```

Spills out only the rows where Status is "Delivered" — a live, formula-driven filtered view that updates automatically if your source data changes, unlike the manual filter dropdown from Part 9.

```
=SORT(I2:I18, 1, -1)
```

Spills the Revenue column sorted descending (`-1`; use `1` for ascending) — useful when you want a sorted list to exist as a formula output, not just a manual one-time sort.

### SUMPRODUCT — conditional math without IF/array entry
```
=SUMPRODUCT((C2:C18="East")*(H2:H18="Delivered")*I2:I18)
```

This achieves the same result as the SUMIFS in Part 6 (sum of East + Delivered revenue = 2000) but via a different mechanism: each condition becomes an array of TRUE/FALSE (treated as 1/0), and multiplying them together effectively means "AND." SUMPRODUCT is worth knowing because it's more flexible than SUMIFS in edge cases (e.g., conditions that aren't simple equality).

### LET — naming intermediate values for readability
```
=LET(eastRev, SUMIF(C2:C18,"East",I2:I18), totalRev, SUM(I2:I18), eastRev/totalRev)
```

This computes East's revenue, then total revenue, names both, and returns East's share — all in one formula, but readable because each piece has a name instead of being a buried sub-formula. Particularly useful once formulas get long enough that you'd otherwise lose track of what each part does.

---

# Part 16: Power Query & Power Pivot — Excel's "Real" Data Tools

Everything so far works on data already sitting in a sheet. These two tools are what Excel uses once data gets larger, messier, or comes from outside Excel entirely — this is the layer that actually overlaps with "data science" in a job-title sense, and the layer that leads naturally into Power BI/SQL if you keep growing in this direction.

### Power Query (Data tab → Get Data, sometimes labeled "Get & Transform")
Power Query is a dedicated import-and-clean engine, separate from your worksheet formulas.
1. **Get Data** lets you import from a CSV file, a folder of files, a website table, or a database — not just data you've manually typed in.
2. Importing opens the **Power Query Editor**, a separate window where you apply cleaning steps visually: remove a column, filter rows, split a column by delimiter, change a column's data type, rename headers.
3. Every step you click is recorded in the **Applied Steps** panel on the right, in order, like a mini macro.
4. Click **Close & Load**, and the cleaned result lands in your sheet as a Table.

**The single biggest advantage over manual cleaning (Part 3):** if the source CSV gets updated tomorrow with new rows, you don't redo any of your cleaning by hand — you just click **Refresh**, and every recorded step (remove duplicates, trim spaces, split columns...) reruns automatically on the new data. This is the difference between a one-time cleanup and a repeatable, production-grade data pipeline — and it's exactly the kind of distinction worth mentioning in an interview if asked "how would you handle data that updates regularly?"

Two more features worth knowing by name:
- **Merge Queries** — joins two tables together based on a matching column, conceptually identical to a SQL `JOIN` or to what your VLOOKUP/INDEX-MATCH in Part 5 did, but built for combining entire tables rather than one cell at a time.
- **Append Queries** — stacks two tables with the same columns on top of each other (e.g., combining "January Orders" and "February Orders" into one table).

### Power Pivot & the Data Model
Once you have multiple related tables (like your Orders and Products sheets), **Power Pivot** lets you formally connect them via a **relationship** (Region/Product-style matching, but managed once instead of repeated in every VLOOKUP) and treat them as one connected model — similar in spirit to a small database. It also removes the practical row-limit pressure of a normal worksheet, handling millions of rows efficiently.

Power Pivot calculations use a different formula language called **DAX** (Data Analysis Expressions). Structurally similar to Excel formulas but built for working across whole tables and relationships rather than individual cells, e.g.:

```
EastRevenue := CALCULATE(SUM(Orders[Revenue]), Orders[Region]="East")
```

You don't need to be fluent in DAX for most entry-level roles — just recognize that it exists and roughly what it's for, since it's a near-guaranteed next step if you keep working with Excel-based analysis.

### When to graduate beyond Excel entirely
Once a dataset is too large for a worksheet, needs to refresh automatically from a live source on a schedule, or needs to be shared as an interactive report rather than a file — that's the natural point to move to **Power BI** (built on the same Power Query/DAX skills you've just learned, just with better visuals and sharing) or to a coding tool like **Python with pandas** / **SQL**. Knowing this progression — and that Excel skills transfer directly into it — is itself a good thing to mention if an interviewer asks where you see your data skills going.

---

# Part 17: Automation — Macros & VBA

### Macros (no coding required to start)
Developer tab → Record Macro (if you don't see the Developer tab: File → Options → Customize Ribbon → check "Developer"). Click Record, perform any sequence of actions (formatting cells, building a chart, applying a filter), click Stop. Excel saves every click as a reusable macro you can replay with one button — useful any time you do the exact same multi-step task repeatedly (e.g., reformatting a weekly report the same way every time).

### VBA (Visual Basic for Applications)
This is the actual code language behind macros — when you record a macro, Excel writes VBA code for you automatically, viewable via **Developer tab → Visual Basic**. You can also write VBA by hand for logic too complex to "record" (loops, conditions, custom functions). You don't need to learn VBA for most data-analysis roles, but recognizing what it is and that it's "the code behind macros" is a reasonable baseline.

### Office Scripts (the modern equivalent, for Excel on the web)
A JavaScript-based alternative to VBA, built for Excel on the web and integrates with Power Automate for scheduling/triggering. Functionally similar purpose to VBA macros, different underlying technology — worth knowing the name exists if you're using Excel Online rather than desktop.

---

# Part 18: Collaboration & Sharing

- **Comments** (threaded, for discussion on a cell) vs. **Notes** (older-style sticky note, static text only) — both added via right-click on a cell.
- **Track Changes / Version History** — available when a file is stored on OneDrive or SharePoint; lets you see and restore earlier versions, or see what specifically changed and who changed it.
- **Protect Sheet / Protect Workbook** (Review tab) — lock specific cells from being edited (commonly used to protect formulas while leaving input cells open) or lock the whole structure from changes.
- **Co-authoring** — when a file is stored in OneDrive/SharePoint, multiple people can edit simultaneously, with each person's cursor and edits visible live, similar to Google Sheets.

---

# Part 19: Keyboard Shortcuts Worth Memorizing

| Shortcut | Action |
|---|---|
| `Ctrl+T` | Convert selected range to a Table |
| `Ctrl+1` | Open Format Cells |
| `Ctrl+E` | Flash Fill |
| `Ctrl+H` | Find & Replace |
| `Ctrl+Shift+L` | Toggle filter dropdown arrows |
| `Alt+=` | AutoSum |
| `F4` | Cycle a cell reference through relative/absolute while editing a formula |
| `Ctrl+Arrow` | Jump to the edge of a block of data |
| `Ctrl+Space` / `Shift+Space` | Select entire column / entire row |
| `Ctrl+;` | Insert today's date as a static value |
| `Alt+F1` | Instantly insert a default chart from the selected data |
| `Ctrl+Z` / `Ctrl+Y` | Undo / Redo |
| `F2` | Edit the active cell directly |
| `Ctrl+\`` (backtick) | Toggle showing formulas instead of their results in every cell |

---

# Part 20: Quick Reference — Every Formula in This Guide

Use this as a lookup table once you already understand the concepts above — it's not meant to teach you a function for the first time, only to remind you of syntax once you already know what the function does.

| Function | Syntax |
|---|---|
| SUM | `=SUM(range)` |
| AVERAGE | `=AVERAGE(range)` |
| COUNT / COUNTA | `=COUNT(range)` / `=COUNTA(range)` |
| MAX / MIN / MEDIAN | `=MAX(range)` |
| IF | `=IF(condition, value_if_true, value_if_false)` |
| IFS | `=IFS(cond1, val1, cond2, val2, TRUE, default)` |
| AND / OR | `=AND(cond1, cond2)` |
| IFERROR | `=IFERROR(formula, value_if_error)` |
| VLOOKUP | `=VLOOKUP(lookup_value, table_array, col_index, FALSE)` |
| INDEX+MATCH | `=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))` |
| XLOOKUP | `=XLOOKUP(lookup_value, lookup_range, return_range, [if_not_found])` |
| SUMIF / SUMIFS | `=SUMIF(check_range, condition, sum_range)` |
| COUNTIF / COUNTIFS | `=COUNTIF(check_range, condition)` |
| AVERAGEIF / AVERAGEIFS | `=AVERAGEIF(check_range, condition, avg_range)` |
| TRIM / CLEAN / PROPER | `=TRIM(text)` |
| LEFT / RIGHT / MID | `=LEFT(text, num_chars)` |
| CONCAT / TEXTJOIN | `=TEXTJOIN(delimiter, ignore_empty, range)` |
| TEXT | `=TEXT(value, "format_code")` |
| DATEDIF | `=DATEDIF(start_date, end_date, "d")` |
| EOMONTH / NETWORKDAYS | `=EOMONTH(date, months)` |
| STDEV.S / VAR.S | `=STDEV.S(range)` |
| CORREL | `=CORREL(range1, range2)` |
| PERCENTILE / LARGE / SMALL | `=PERCENTILE(range, 0.9)` |
| RANK.EQ | `=RANK.EQ(value, range, 0)` |
| TREND / FORECAST.LINEAR | `=FORECAST.LINEAR(new_x, known_y, known_x)` |
| UNIQUE / FILTER / SORT | `=FILTER(range, condition_range)` |
| SUMPRODUCT | `=SUMPRODUCT(array1*array2*...)` |
| LET | `=LET(name1, value1, name2, value2, ..., result)` |

---

# Part 21: Interview Prep

### "Tell me about a time you worked with data in Excel" — you now have a real answer
You can honestly describe the exact exercise you just did: *"I worked with an order dataset that had duplicate rows and inconsistent text formatting. I used TRIM and Remove Duplicates to clean it, which actually changed the total revenue figure once corrected. Then I used VLOOKUP to pull in product category data from a separate reference table, built SUMIFS to break down revenue by region, and used a PivotTable with slicers to make it explorable. I also ran a quick correlation check between quantity and revenue and found it was actually negative, because high-value products were ordered in smaller quantities than low-value ones."* That's a complete, honest, specific answer built entirely from this guide.

### Common questions and strong answers
1. **"VLOOKUP vs. INDEX-MATCH vs. XLOOKUP — what's the difference?"** VLOOKUP only searches left-to-right and breaks if columns are inserted; INDEX-MATCH is more flexible and doesn't break as easily; XLOOKUP is the modern function that does what INDEX-MATCH does with simpler syntax and built-in error handling.
2. **"SUMIF vs. SUMIFS?"** SUMIF takes exactly one condition; SUMIFS takes any number of conditions, all of which must be true (an AND relationship).
3. **"How do you remove duplicates from a dataset?"** Select the range, Data tab → Remove Duplicates, choose which columns define "duplicate." Always check the count of rows removed against what you expect, rather than assuming the tool got it right.
4. **"Why use absolute references (`$`)?"** To lock a reference so it doesn't shift when a formula is copied or dragged — essential for anything referencing a single fixed cell, like a tax rate or a lookup table's location.
5. **"How would you summarize a large dataset quickly?"** A PivotTable — rows for the grouping category, values for the metric, optionally a calculated field for any derived metric, and slicers to make it interactive.
6. **"How do you handle errors in formulas?"** Wrap with `IFERROR`, but also diagnose the root cause first — for lookups specifically, check for extra spaces or case mismatches in the data, not just the formula syntax.
7. **"What's a calculated field in a PivotTable?"** A custom metric computed from existing Pivot fields (e.g., revenue ÷ quantity for average order value) rather than a column that already exists in the raw data.
8. **"What's Power Query and why use it instead of cleaning manually?"** It records cleaning steps so they automatically re-apply when the source data refreshes — repeatable, not one-time.
9. **"When would you use a Pivot vs. a formula?"** PivotTables for fast exploratory summarization of large or unfamiliar data; formulas (SUMIFS etc.) when the result needs to live inline as part of a structured, ongoing report.
10. **"What does it mean if a correlation is negative?"** The two variables move in opposite directions — as one increases, the other tends to decrease. It doesn't mean there's no relationship; it means the relationship runs the opposite way you might assume.

### Live test / assessment tips
- Read every instruction fully before touching anything — half of test failures are answering the wrong question correctly.
- `Ctrl+Z` exists for a reason — try a formula, see if it works, undo if it doesn't. Experimentation under time pressure is normal.
- If a function is unfamiliar, start typing its name — Excel's autocomplete tooltip shows the exact argument order, which is often enough to get unstuck without outside help.
- A working-but-inelegant answer (e.g., a SUMPRODUCT instead of a cleaner SUMIFS) beats a perfect answer left unfinished. Time-box yourself per question.

---

# Part 22: Final Practice Exercise (Self-Test)

Do this entirely from memory, without scrolling back up, using your cleaned Orders dataset. This is the realistic shape of an actual skills assessment. Write your answers down, then check them against the answer key below.

1. What is the total Revenue across all orders, after removing the duplicate row?
2. Write a formula to find the Category of the product "Monitor" using your Products lookup table.
3. Write a formula for total Revenue from the **West** region only.
4. Write a formula for total Revenue from the **West** region, **Delivered** orders only.
5. How many orders have Status = "Pending"?
6. Build a PivotTable showing Revenue by Region and Product. What is the Grand Total?
7. What is the average Revenue for "Mouse" orders?
8. What is the correlation between Quantity and Revenue, and is it positive or negative?
9. Which customer has the highest total Revenue?
10. Using Goal Seek, what Quantity would make order 1001's Revenue equal exactly 4000 (UnitPrice 800)?

### Answer key
1. **7320** (17 rows after removing the duplicate 1003 entry)
2. `=VLOOKUP("Monitor", Products!$A$2:$C$5, 2, FALSE)` → **Electronics**
3. `=SUMIF(C2:C18,"West",I2:I18)` → **1415**
4. `=SUMIFS(I2:I18, C2:C18,"West", H2:H18,"Delivered")` → **615** (West Delivered orders only: Mouse 75 + Keyboard 50 + Mouse 90 + Monitor 400 = 615. If you got 1415 instead, you forgot the Status condition — that figure includes order 1005, which is West but Cancelled, so it should be excluded)
5. `=COUNTIF(H2:H18,"Pending")` → **3**
6. **7320** (same Grand Total as your overall SUM — a Pivot should never change your totals, only reorganize them; if it doesn't match, your Pivot's source range is missing rows)
7. `=AVERAGEIF(D2:D18,"Mouse",I2:I18)` → **99**
8. `=CORREL(E2:E18,I2:I18)` → **≈ −0.40, negative** — quantity and revenue move in opposite directions here, because high-priced products (laptops) tend to be ordered in small quantities
9. **Emma Wilson** (total Revenue 2350)
10. **5** (4000 ÷ 800 = 5)

If you got most of these right without looking back, you're genuinely ready. If a couple were wrong, re-read just that specific Part above — you don't need to reread the whole guide, just the section behind the question you missed.

---

# Closing Notes

Everything in Parts 0–10 plus 21–22 is genuinely enough to walk into a 3-day-notice interview and hold your own. Parts 11–20 are there so this document keeps being useful in week 2, month 2, and year 2 of the job — when you'll actually need conditional formatting tricks, Power Query, or a DAX calculation, and won't have to go hunting for a new resource. Keep this file. Update it with your own notes as you discover quirks specific to your company's spreadsheets. That's how a reference guide turns into actual expertise.
