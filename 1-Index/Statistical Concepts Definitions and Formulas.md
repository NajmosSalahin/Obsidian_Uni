---
title: "[[Statistical Concepts Definitions and Formulas]]"
source: https://grok.com/chat/8e3072d5-40ab-44f7-8d8a-7810bd01f4a0
created: 2025-08-31
description: Grok is a free AI assistant designed by xAI to maximize truth and objectivity. Grok offers real-time search, image generation, trend analysis, and more.
tags:
  - clippings
  - STAT-1101
status: active
links:
  - "[[STAT-1101]]"
semester: "1.1"
related:
  - "[[STAT-1101]]"
banner: Github/Resources/Banners/Wallpaper/books.jpg
content-start: 186
---
### Information

##### **Definition:** Information refers to processed, organized, and interpreted data that provides meaning, context, and usefulness for decision-making. *It is derived from raw data through analysis, summarization, or transformation, making it actionable and relevant.

**Example:** Raw data like "daily temperatures: 25, 28, 30" becomes information when processed as "average weekly temperature is 27.67°C, indicating a warm week."

**Details/Equations/Formulas:** No specific mathematical formulas, but information is often obtained by applying statistical methods to data (e.g., calculating averages or trends). In information theory (Shannon's), it can be quantified as $I = -\log_2(p)$  , where $p$  is the probability of an event, measuring uncertainty reduction.

### Data

##### **Definition:** Data consists of raw, unprocessed facts, figures, observations, or measurements collected from various sources, without inherent meaning until analyzed. *It can be qualitative (descriptive) or quantitative (numerical).

**Example:** A list of students' exam scores: 85, 92, 78, 95, 88 (quantitative data). Or colors preferred by students: red, blue, green (qualitative data).

**Details/Equations/Formulas:** Data is classified as primary (collected firsthand) or secondary (from existing sources). No formulas, but data forms the basis for statistics, e.g., sample size $n$  or population size $N$  .

### Mean

##### **Definition:** The mean (or average) is a measure of central tendency that represents the arithmetic average of a set of numbers, calculated by summing all values and dividing by the number of values.

**Example:** For scores: 10, 20, 30, 40, 50. Mean = (10+20+30+40+50)/5 = 30.

**Details/Equations/Formulas:** For ungrouped data: $\bar{x} = \frac{\sum x_i}{n}$  , where $x_i$  are values and $n$  is the number of observations. It is sensitive to outliers.

### Median

##### **Definition:** The median is a measure of central tendency that represents the middle value in an ordered dataset. For even number of observations, it is the average of the two middle values.

**Example:** For scores: 10, 20, 30, 40, 50 (odd n=5), median = 30. For 10, 20, 30, 40 (even n=4), median = (20+30)/2 = 25.

**Details/Equations/Formulas:** Arrange data in ascending order. For odd $n$  : Median = value at position $\frac{n+1}{2}$  . For even $n$  : Average of values at $\frac{n}{2}$  and $\frac{n}{2}+1$  . It is robust to outliers.

### Mode

**Definition:** The mode is a measure of central tendency that represents the most frequently occurring value(s) in a dataset. A dataset can be unimodal (one mode), bimodal (two modes), or multimodal.

**Example:** In dataset: 5, 7, 5, 8, 9, 5. Mode = 5 (appears three times). If 5 and 7 both appear three times, bimodal: 5 and 7.

**Details/Equations/Formulas:** No direct formula; identified by counting frequencies. For continuous data, it is the value with highest density. Not always unique or existent.

### Variable

**Definition:** A variable is any characteristic, quantity, or attribute that can take different values across observations or entities in a study. It is what is measured or observed.

**Example:** In a student survey, "height" is a variable (values: 160 cm, 175 cm, etc.); "gender" is a variable (values: male, female).

**Details/Equations/Formulas:** Variables are independent (cause) or dependent (effect). No formulas, but in regression: $y = \beta_0 + \beta_1 x + \epsilon$  , where $x$  is independent variable, $y$  dependent.

### Cumulative Frequency

**Definition:** Cumulative frequency is the running total of frequencies up to a certain class or value in a frequency distribution, showing how many observations are less than or equal to a particular value.

**Example:** For marks: 0-10 (freq=2), 10-20 (freq=3), 20-30 (freq=5). Cumulative freq: 2 (up to 10), 5 (up to 20), 10 (up to 30).

**Details/Equations/Formulas:** For a frequency table, cumulative frequency $cf_i = cf_{i-1} + f_i$  , where $f_i$  is frequency of ith class. Used for ogives and percentiles.

### Discrete Variable

**Definition:** A discrete variable is a type of quantitative variable that can only take specific, countable values (integers), often from counting, with no intermediate values possible.

**Example:** Number of students in a class: 25, 30, 35 (can only be whole numbers, not 25.5).

**Details/Equations/Formulas:** Values are finite or countably infinite. Probability mass function (PMF): $P(X = k)$  , where $k$  is a discrete value. E.g., binomial distribution: $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$  .

### Indiscrete Variable (Continuous Variable)

**Definition:** An indiscrete variable (commonly called continuous variable) is a quantitative variable that can take any value within a given interval or range, including fractions, from measurement rather than counting.

**Example:** Height of students: 165.5 cm, 170.2 cm (can be any real number between limits).

**Details/Equations/Formulas:** Values are uncountably infinite. Probability density function (PDF): $f(x)$  , where $\int_{-\infty}^{\infty} f(x) \, dx = 1$  . E.g., normal distribution: $f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$  .

### Diagram of Data

**Definition:** A diagram of data refers to graphical representations used to visualize and summarize data for easy interpretation, such as bar charts, pie charts, histograms, or line graphs.

**Example:** A bar chart showing sales: Bars for months (Jan: height 100, Feb: 150) to compare values.

**Details/Equations/Formulas:** Types include: Bar diagram (for categorical data), Histogram (for continuous data with bars touching). No formulas, but ensure scales are accurate; e.g., histogram bin width = (max - min)/number of bins.

### Frequency Polygon

**Definition:** A frequency polygon is a line graph that connects the midpoints of the tops of bars in a histogram (or class midpoints plotted against frequencies), used to show the shape of a frequency distribution.

**Example:** For classes 0-10 (freq=5, midpoint=5), 10-20 (freq=8, midpoint=15). Plot points (5,5), (15,8) and connect with lines.

**Details/Equations/Formulas:** Plot midpoint $m_i = \frac{l_i + u_i}{2}$  vs. frequency $f_i$  , where $l_i, u_i$  are lower and upper class limits. Extend to axes for closure. Useful for comparing distributions.

### Ogive Curve

**Definition:** An ogive curve (or cumulative frequency curve) is a graphical representation of cumulative frequencies plotted against upper class boundaries, forming an S-shaped curve used to find medians, quartiles, etc.

**Example:** For cumulative freq: Up to 10 (cf=2), up to 20 (cf=5), up to 30 (cf=10). Plot (10,2), (20,5), (30,10) and connect smoothly.

**Details/Equations/Formulas:** Less-than ogive: Plot upper limits vs. less-than cf. More-than ogive: Lower limits vs. more-than cf. Median from intersection of ogives or at cf = n/2 on less-than ogive.

### Central Tendency

**Definition:** Central tendency refers to the statistical measures that describe the center or typical value of a dataset, summarizing where most data points cluster. Common measures: mean, median, mode.

**Example:** For incomes: 20k, 25k, 30k, 100k. Mean=43.75k (pulled by outlier), median=27.5k (better central value).

**Details/Equations/Formulas:** Properties: Mean for symmetric data, median for skewed, mode for nominal. Empirical relation: Mode ≈ 3(Median) - 2(Mean) for moderately skewed distributions.

### Arithmetic Mean

**Definition:** Arithmetic mean is the sum of all observations divided by the number of observations, a key measure of central tendency for quantitative data.

**Example:** Weights: 50, 60, 70 kg. Arithmetic mean = (50+60+70)/3 = 60 kg.

**Details/Equations/Formulas:** $\bar{x} = \frac{\sum_{i=1}^n x_i}{n}$  for population, or $\bar{x} = \frac{\sum_{i=1}^n x_i}{n}$  for sample. Properties: $\sum (x_i - \bar{x}) = 0$  . Assumes equal weights.

### Arithmetic Mean of Classified Data

**Definition:** For grouped or classified data, the arithmetic mean is calculated using class midpoints weighted by frequencies, assuming uniform distribution within classes.

**Example:** Classes: 0-10 (f=2, m=5), 10-20 (f=3, m=15). Mean = \[(2 *5) + (3* 15)\] / (2+3) = (10+45)/5 = 11.

**Details/Equations/Formulas:** $\bar{x} = \frac{\sum f_i m_i}{\sum f_i}$  , where $m_i = \frac{l_i + u_i}{2}$  , $f_i$  \= frequency. For open-ended classes, assume reasonable midpoints.

### Weighted Mean

**Definition:** Weighted mean is an average where each value is multiplied by a weight reflecting its importance, then summed and divided by total weights.

**Example:** Grades: Test (80, weight=0.4), Project (90, weight=0.6). Weighted mean = (80 *0.4 + 90* 0.6) / (0.4+0.6) = (32+54)/1 = 86.

**Details/Equations/Formulas:** $\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i}$  , where $w_i$  are weights. Used in indexes like GPA. If weights are frequencies, it reduces to arithmetic mean of grouped data.

### Determining Median of Classified Data

**Definition:** For grouped data, the median is found by identifying the median class (where cumulative frequency reaches n/2) and interpolating within it.

**Example:** n=10, cf: Up to 10 (3), up to 20 (7), up to 30 (10). Median class=10-20 (cf crosses 5). Median = 10 + \[(5-3)/4\]\*10 = 10 + (2/4)\*10 = 15.

**Details/Equations/Formulas:** Median = $l + \left( \frac{\frac{n}{2} - cf_{prev}}{f_m} \right) \times h$  , where $l$  \= lower limit of median class, $cf_{prev}$  \= cf before median class, $f_m$  \= frequency of median class, $h$  \= class width. Median class: First class where cf ≥ n/2.

### Determining Mode of Classified Data

**Definition:** For grouped data, the mode is in the modal class (highest frequency) and interpolated using frequencies of adjacent classes.

**Example:** Classes: 0-10 (f=3), 10-20 (f=5), 20-30 (f=4). Modal class=10-20. Mode = 10 + \[(5-3)/( (5-3) + (5-4) )\]\*10 = 10 + (2/(2+1))\*10 ≈ 10 + 6.67 = 16.67.

**Details/Equations/Formulas:** Mode = $l + \left( \frac{f_m - f_{prev}}{(f_m - f_{prev}) + (f_m - f_{next})} \right) \times h$  , where $l$  \= lower limit of modal class, $f_m$  \= max frequency, $f_{prev}$  and $f_{next}$  \= frequencies before and after, $h$  \= width. For bimodal, calculate both.

---




### Statistics

**Definition:** Statistics is the branch of mathematics that deals with the collection, organization, analysis, interpretation, and presentation of data to make informed decisions or inferences about a population.

**Example:** Collecting exam scores from a class, calculating the average score, and using it to assess overall performance.

**Details/Equations/Formulas:** Statistics is divided into descriptive (summarizing data) and inferential (making predictions). Key formula for sample variance: $s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$  , where $\bar{x}$  is the mean, $n$  is sample size.

### Population

**Definition:** A population is the entire set of individuals, objects, or measurements that are of interest in a statistical study, from which data could potentially be collected.

**Example:** All registered voters in a country for an election survey.

**Details/Equations/Formulas:** Denoted by $N$  (size). Population mean: $\mu = \frac{\sum X_i}{N}$  . Inferences are often made from samples to populations.

### Probability

**Definition:** Probability is a measure of the likelihood that a particular event will occur, expressed as a number between 0 and 1, where 0 indicates impossibility and 1 indicates certainty.

**Example:** The probability of rolling a 6 on a fair die is 1/6.

**Details/Equations/Formulas:** Basic formula: $P(E) = \frac{\text{number of favorable outcomes}}{\text{total number of possible outcomes}}$  . Axioms: $0 \leq P(E) \leq 1$  , $P(S) = 1$  (S is sample space), $P(A \cup B) = P(A) + P(B) - P(A \cap B)$  .

### Sample Space

**Definition:** The sample space is the set of all possible outcomes of a random experiment, denoted by S or Ω.

**Example:** For tossing a coin: S = {Heads, Tails}.

**Details/Equations/Formulas:** Finite or infinite. For two dice: |S| = 36. Probability: $P(E) = \frac{|E|}{|S|}$  for equally likely outcomes.

### Population

**Definition:** A population is the entire set of individuals, objects, or measurements that are of interest in a statistical study, from which data could potentially be collected.

**Example:** All students in a university for a study on average GPA.

**Details/Equations/Formulas:** Denoted by $N$  (size). Population variance: $\sigma^2 = \frac{\sum (X_i - \mu)^2}{N}$  . Contrasted with sample (subset).

### Quantitative Data

**Definition:** Quantitative data consists of numerical values that represent counts or measurements, allowing for mathematical operations like addition and averaging.

**Example:** Heights of students: 160 cm, 175 cm, 182 cm.

**Details/Equations/Formulas:** Subtypes: discrete (countable, e.g., integers) and continuous (measurable, e.g., reals). Mean: $\bar{x} = \frac{\sum x_i}{n}$  .

### Quantitative Data

**Definition:** Quantitative data consists of numerical values that represent counts or measurements, allowing for mathematical operations like addition and averaging.

**Example:** Number of books read by students: 5, 8, 12.

**Details/Equations/Formulas:** Can be interval (no true zero, e.g., temperature) or ratio (true zero, e.g., weight). Standard deviation: $\sigma = \sqrt{\frac{\sum (x_i - \mu)^2}{N}}$  .

### Central Tendency

**Definition:** Central tendency refers to the statistical measures that describe the center or typical value of a dataset, summarizing where most data points cluster.

**Example:** For scores: 10, 20, 30. Mean = 20, median = 20, mode = none.

**Details/Equations/Formulas:** Measures: mean $\bar{x} = \frac{\sum x_i}{n}$  , median (middle value), mode (most frequent). Empirical relation for skewed data: Mode ≈ 3(Median) - 2(Mean).

### Outliers

**Definition:** Outliers are data points that significantly differ from other observations in a dataset, potentially indicating variability, errors, or anomalies.

**Example:** In incomes: 20k, 25k, 30k, 1M. 1M is an outlier.

**Details/Equations/Formulas:** Detected via IQR method: Outlier if < Q1 - 1.5(IQR) or > Q3 + 1.5(IQR), where IQR = Q3 - Q1. Z-score: |z| > 3.

### Unimodal Dataset

**Definition:** A unimodal dataset is one that has a single peak or mode in its frequency distribution, indicating one predominant value or cluster.

**Example:** Heights in a homogeneous group, peaking around 170 cm.

**Details/Equations/Formulas:** In histogram, one clear hump. For normal distribution: PDF $f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$  , unimodal at μ.

### Bimodal Dataset

**Definition:** A bimodal dataset has two distinct peaks or modes in its frequency distribution, often suggesting two underlying subgroups.

**Example:** Heights of adults combining men and women, peaks at 165 cm and 175 cm.

**Details/Equations/Formulas:** Mixture of two distributions, e.g., two normals. No single formula, but can model as $f(x) = p \cdot N(\mu_1, \sigma_1) + (1-p) \cdot N(\mu_2, \sigma_2)$  .

### Multimodal Dataset

**Definition:** A multimodal dataset has three or more distinct peaks or modes in its frequency distribution, indicating multiple subgroups or processes.

**Example:** Test scores from multiple classes with different teaching methods, showing several peaks.

**Details/Equations/Formulas:** Generalization of bimodal. Modeled as finite mixture: $f(x) = \sum_{k=1}^K p_k f_k(x)$  , where $\sum p_k = 1$  .

### Statistical Measures

**Definition:** Statistical measures are numerical values that summarize or describe aspects of a dataset, including central tendency, dispersion, shape, and association.

**Example:** Mean, variance, correlation for a set of exam scores.

**Details/Equations/Formulas:** Dispersion: Variance $s^2 = \frac{\sum (x_i - \bar{x})^2}{n-1}$  . Shape: Skewness $\gamma = \frac{\sum (x_i - \bar{x})^3 / n}{(s^2)^{3/2}}$  . Association: Correlation $r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{ \sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2} }$  .

### Uniform Distribution

**Definition:** A uniform distribution is a probability distribution where all outcomes are equally likely within a defined interval, with constant probability density.

**Example:** Rolling a fair die: each face 1-6 has probability 1/6.

**Details/Equations/Formulas:** Discrete: P(X=k) = 1/n for k=1 to n. Continuous: PDF $f(x) = \frac{1}{b-a}$  for a ≤ x ≤ b. Mean: $\frac{a+b}{2}$  , variance: $\frac{(b-a)^2}{12}$  .

### Primary/Direct Data

**Definition:** Primary or direct data is information collected firsthand by the researcher for a specific purpose, through methods like surveys or experiments.

**Example:** Conducting interviews to gather opinions on a new product.

**Details/Equations/Formulas:** Sources: observations, questionnaires. Advantages: reliable, tailored. No formulas, but sample size determination: $n = \frac{z^2 p(1-p)}{e^2}$  for proportions.

### Secondary/Indirect Data

**Definition:** Secondary or indirect data is information collected by someone else for a different purpose, obtained from existing sources like publications or databases.

**Example:** Using government census data for market analysis.

**Details/Equations/Formulas:** Sources: books, journals, online databases. Advantages: cost-effective, time-saving. Potential issues: outdated or biased. No specific formulas.

### Unorganized Data

**Definition:** Unorganized data is raw data that has not been sorted, classified, or arranged in any meaningful way, making it difficult to analyze.

**Example:** A random list of numbers: 5, 2, 8, 1, 9.

**Details/Equations/Formulas:** Requires organization for analysis. No formulas, but first step to compute frequency table or sort.

### Organized Data

**Definition:** Organized data is raw data that has been sorted, grouped, or tabulated (e.g., into frequency distributions) for easier analysis and interpretation.

**Example:** Sorted list: 1, 2, 5, 8, 9; or frequency table.

**Details/Equations/Formulas:** Methods: arrays, tables. For grouped: class intervals. Mean from organized: $\bar{x} = \frac{\sum f_i m_i}{\sum f_i}$  .

### Frequency Histogram

**Definition:** A frequency histogram is a graphical representation of data using bars of different heights to show the frequency of data points in successive intervals.

**Example:** Bars for age groups: 0-10 (height=5), 10-20 (height=8).

**Details/Equations/Formulas:** Bars touch for continuous data. Bin width = (max - min)/k, where k is number of bins (Sturges' rule: k ≈ 1 + log2(n)).

### Line Diagram

**Definition:** A line diagram (or line graph) connects data points with lines to show trends or changes over time or categories.

**Example:** Plotting temperature over days: points connected by lines.

**Details/Equations/Formulas:** Useful for time series. No formula, but can fit lines like regression: y = mx + c.

### Random Experiment

**Definition:** A random experiment is a process or trial that can result in one of several possible outcomes, with uncertainty in which outcome will occur.

**Example:** Tossing a coin or rolling a die.

**Details/Equations/Formulas:** Outcomes must be well-defined and repeatable. Leads to sample space.

### Event

**Definition:** An event is a subset of the sample space, representing one or more outcomes of a random experiment.

**Example:** Event "even number" in die roll: {2,4,6}.

**Details/Equations/Formulas:** Simple (one outcome) or compound. P(E) = |E| / |S| for equally likely.

### Equally Likely Events

**Definition:** Equally likely events are outcomes in a sample space that have the same probability of occurring.

**Example:** Each face of a fair die: P=1/6.

**Details/Equations/Formulas:** Assumes fair experiment. P(each) = 1 / |S|.

### Mutually Exclusive Events

**Definition:** Mutually exclusive events are events that cannot occur at the same time; their intersection is empty.

**Example:** Drawing a red card or a black card from a deck (but not both colors).

**Details/Equations/Formulas:** P(A ∩ B) = 0. Addition rule: P(A ∪ B) = P(A) + P(B).

### Favourable Outcomes

**Definition:** Favourable outcomes are the specific results in the sample space that satisfy the conditions of a particular event.

**Example:** For "rolling >4": {5,6} out of {1,2,3,4,5,6}.

**Details/Equations/Formulas:** P(E) = number of favourable / total.

### Sample Space

**Definition:** The sample space is the set of all possible outcomes of a random experiment, denoted by S or Ω.

**Example:** For two coins: S = {HH, HT, TH, TT}.

**Details/Equations/Formulas:** Can be discrete or continuous. |S| determines probabilities.

### Sample Point

**Definition:** A sample point is a single, indivisible outcome in the sample space of a random experiment.

**Example:** "Heads" in coin toss.

**Details/Equations/Formulas:** Events are collections of sample points. P(sample point) = 1/|S| if equally likely.

### Logic Based Probabilities

**Definition:** Logic based probabilities (or classical/a priori) are probabilities determined by reasoning about equally likely outcomes without empirical data.

**Example:** Probability of heads in fair coin: 1/2, based on symmetry.

**Details/Equations/Formulas:** Assumes finite, equally likely outcomes. P(E) = |E| / |S|.

### Determination of Logic Based Probabilities

**Definition:** Determination of logic based probabilities involves identifying the sample space, assuming equally likely outcomes, and calculating the ratio of favorable to total outcomes.

**Example:** For drawing an ace from deck: 4/52 = 1/13.

**Details/Equations/Formulas:** Steps: Define S, list outcomes, count favorable. Formula: P = favorable / total.

### Two Special Events: Certain Events

**Definition:** A certain event is an event that is guaranteed to occur, with probability 1, such as the entire sample space.

**Example:** Rolling a number between 1 and 6 on a die.

**Details/Equations/Formulas:** P(certain) = 1. Union with any event doesn't change it.

### Impossible Events

**Definition:** An impossible event is one that cannot occur, with probability 0, such as the empty set.

**Example:** Rolling a 7 on a standard die.

**Details/Equations/Formulas:** P(impossible) = 0. Intersection with any event is impossible.

### Data Based Probability

**Definition:** Data based probability (or empirical/relative frequency) is estimated from observed data or experiments, approximating true probability through repeated trials.

**Example:** Tossing a coin 100 times, getting 55 heads: P(heads) ≈ 55/100 = 0.55.

**Details/Equations/Formulas:** P(E) ≈ frequency of E / total trials. As n → ∞, approaches true P (law of large numbers).

### Determination of Probability using Sample Space and Probability Tree

**Definition:** Determination of probability using sample space and probability tree involves listing all outcomes in sample space or using a tree diagram to visualize branches and calculate probabilities by multiplying along paths.

**Example:** Two coins: Tree branches for H/T each, P(HH) = (1/2)\*(1/2) = 1/4.

**Details/Equations/Formulas:** For independent events: P(path) = product of branch probs. Total P(E) = sum of path probs for E. For sample space: enumerate and sum.