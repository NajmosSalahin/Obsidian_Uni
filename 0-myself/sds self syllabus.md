**Job-Ready Statistics & Data Science Syllabus (2026 Edition)**

### Macro Topic 1: Programming & Tooling Foundations
**Topic 1.1: Python Proficiency**  
**Subtopic 1.1.1: Core Python & Data Structures**  
- Microtopics: Lists/tuples/dicts/sets (time/space complexity analysis, slicing, shallow vs deep copy), list/dict/set comprehensions and generator expressions (lazy evaluation, memory efficiency), decorators (function/class decorators, functools.wraps, caching with lru_cache), context managers (custom __enter__/__exit__, contextlib), error handling (try/except/else/finally, custom exceptions, exception groups in Python 3.11+), OOP (classes, inheritance, multiple inheritance, dataclasses, @property, dunder methods, slots for memory optimization), functional programming (lambda, map/filter/reduce, itertools, partial application), typing (type hints, generics, Protocols, runtime checking with typing_extensions), async basics (asyncio, async/await, concurrent.futures for I/O-bound tasks).  
**Subtopic 1.1.2: Scientific Python Stack**  
- Microtopics: NumPy (ndarray operations, broadcasting rules, vectorization vs loops, advanced indexing, ufuncs, memory views), Pandas (indexing with loc/iloc, groupby/agg/apply/transform, merge/join/concat/pivot, time-series handling with resample/rolling/shift, multi-index and categorical data, performance with eval/query), Matplotlib/Seaborn/Plotly (static vs interactive plots, subplots/grids, customization with rcParams/themes, Plotly Dash for web apps, publication-ready exports).  
**Subtopic 1.1.3: Performance & Best Practices**  
- Microtopics: Profiling (cProfile, line_profiler, memory_profiler), vectorization and numba/jit, parallel processing (joblib, multiprocessing, Dask for larger-than-memory data), code style (PEP8, black/ruff, type checking with mypy/pyright).

**Topic 1.2: SQL & Database Interaction**  
**Subtopic 1.2.1: Core SQL**  
- Microtopics: SELECT/WHERE/GROUP BY/HAVING/ORDER BY/LIMIT, JOINs (INNER/LEFT/RIGHT/FULL/SELF/cross joins, anti-joins with NOT EXISTS), subqueries and correlated subqueries, CTEs (WITH clause, recursive CTEs for hierarchies), window functions (ROW_NUMBER/RANK/DENSE_RANK, LAG/LEAD/NTILE, running totals, moving averages, percentile functions), date/time manipulation (DATE_TRUNC, EXTRACT, interval arithmetic, timezone handling), string functions and pattern matching (LIKE, REGEXP).  
**Subtopic 1.2.2: Advanced & Production SQL**  
- Microtopics: Query optimization (EXPLAIN/EXPLAIN ANALYZE, indexing strategies on single/composite columns, covering indexes, partitioning), handling NULLs/edge cases (COALESCE, NULLIF, three-valued logic pitfalls), pivoting/unpivoting (CROSSTAB or conditional aggregation), JSON/JSONB handling (in Postgres), materialized views and refresh strategies, integration with Python (SQLAlchemy ORM/core, psycopg2/psycopg3, pandas read_sql with chunksize for large results).  
**Subtopic 1.2.3: Big Data SQL Variants**  
- Microtopics: Spark SQL basics (DataFrames, SparkSession, Catalyst optimizer), dbt fundamentals (models, tests, sources, macros for reusable SQL).

**Topic 1.3: Version Control, Reproducibility & Environment Management**  
- Microtopics: Git workflows (feature branches, rebasing, cherry-pick, interactive rebase, GitHub/GitLab PR workflows, .gitignore patterns for data/science projects), dependency management (Poetry/pyproject.toml, Pipenv, conda environments, pyenv for Python versions), reproducible research (Jupyter kernels, papermill for parameterized notebooks, requirements.txt vs lock files, DVC for data and model versioning), containerization basics (Dockerfile for DS projects, docker-compose for local DB + app).

### Macro Topic 2: Mathematical & Statistical Foundations
**Topic 2.1: Probability & Distributions**  
**Subtopic 2.1.1: Core Probability**  
- Microtopics: Axioms of probability, conditional probability and Bayes’ theorem (with odds form and naive Bayes intuition), independence vs conditional independence, random variables (discrete/continuous, PMF/PDF/CDF), expectation/variance/covariance/correlation (properties, linearity of expectation), common distributions (Bernoulli, Binomial, Poisson, Geometric, Negative Binomial, Uniform, Normal, Multivariate Normal, Exponential, Gamma, Beta, t-distribution, chi-square, F-distribution, Log-normal).  
**Subtopic 2.1.2: Sampling & Estimation**  
- Microtopics: Law of large numbers (weak/strong), Central Limit Theorem (with simulation proofs and Berry-Esseen bounds intuition), sampling distributions, point estimation (MLE, method of moments), interval estimation (confidence intervals construction for mean/proportion/variance), bias-variance decomposition for estimators.

**Topic 2.2: Inferential Statistics**  
**Subtopic 2.2.1: Hypothesis Testing**  
- Microtopics: Null/alternative hypotheses, Type I/II errors and power, p-values and significance levels, parametric tests (z-test, t-test one/two-sample/paired, chi-square goodness-of-fit/independence, ANOVA one/two-way, F-test), non-parametric tests (Mann-Whitney, Wilcoxon signed-rank, Kruskal-Wallis, Kolmogorov-Smirnov), power analysis and sample size calculation (using statsmodels or G*Power formulas), multiple testing corrections (Bonferroni, Holm, Benjamini-Hochberg FDR, family-wise error rate).  
**Subtopic 2.2.2: Regression & Correlation**  
- Microtopics: Simple/multiple linear regression (OLS derivation, matrix form, assumptions and diagnostics: linearity, homoscedasticity, normality of residuals, independence), logistic regression (logit link, maximum likelihood, odds ratios), multicollinearity detection (VIF, condition number), correlation vs causation pitfalls, partial and semi-partial correlation.

**Topic 2.3: Advanced Statistical Concepts**  
- Microtopics: Bayesian inference (priors/posteriors, conjugate priors, MCMC with PyMC or Stan basics, credible intervals), bootstrapping and permutation tests (non-parametric inference), survival analysis (Kaplan-Meier, Cox proportional hazards, log-rank test), time-series stationarity tests (ADF, KPSS), ARIMA/SARIMA/Prophet modeling intuition.

### Macro Topic 3: Data Wrangling & Exploratory Data Analysis (EDA)
**Topic 3.1: Data Cleaning & Feature Engineering**  
**Subtopic 3.1.1: Handling Messy Data**  
- Microtopics: Missing data mechanisms (MCAR/MAR/MNAR) and strategies (deletion, mean/median/mode, KNN imputation, MICE, deep learning imputation with autoencoders), outliers (detection with IQR/z-score/Isolation Forest, treatment via winsorizing/capping/transformations), data type conversion and encoding (one-hot, label, target, frequency, binary, embeddings for high-cardinality), scaling/normalization (StandardScaler, MinMaxScaler, RobustScaler, log/power transforms).  
**Subtopic 3.1.2: Feature Creation & Selection**  
- Microtopics: Domain-driven feature engineering (binning, interactions, polynomial features, date/time cyclicals, text features with TF-IDF or embeddings), automated feature selection (recursive feature elimination, forward/backward/stepwise, mutual information, chi2, ANOVA F-value), dimensionality reduction for features (PCA loadings interpretation).

**Topic 3.2: EDA Techniques**  
- Microtopics: Univariate analysis (summary stats, histograms, boxplots, QQ-plots), multivariate analysis (correlation matrices/heatmaps, pair plots, scatter matrices), distribution comparisons (ECDF, violin plots), dimensionality reduction visualization (PCA, t-SNE, UMAP projections), interactive EDA tools (pandas-profiling/ydata-profiling, sweetviz, AutoViz).

### Macro Topic 4: Machine Learning & Predictive Modeling
**Topic 4.1: Supervised Learning**  
**Subtopic 4.1.1: Classical ML Algorithms**  
- Microtopics: Linear/logistic regression (closed-form, gradient descent from scratch, regularization L1/L2/ElasticNet), decision trees (entropy/Gini/entropy gain, pruning, handling categorical features), ensemble methods (bagging, Random Forest, boosting: AdaBoost, Gradient Boosting, XGBoost/LightGBM/CatBoost with early stopping, hyperparameter tuning via Optuna/Bayesian optimization/GridSearchCV/RandomizedSearchCV), SVM (kernel trick, soft margin, one-class SVM), Naive Bayes variants.  
**Subtopic 4.1.2: Model Evaluation & Validation**  
- Microtopics: Train/test/validation splits (hold-out, stratified, time-series split), cross-validation (k-fold, stratified k-fold, leave-one-out, nested CV for hyperparameter tuning), metrics for classification (accuracy, precision/recall/F1/precision-recall curve, ROC-AUC, confusion matrix, calibration plots), regression metrics (RMSE/MAE/MAPE/R²/adjusted R², quantile loss), imbalanced data handling (SMOTE, class weights, focal loss).

**Topic 4.2: Unsupervised & Semi-Supervised Learning**  
- Microtopics: Clustering (K-means++ initialization, elbow/silhouette/GAP statistic, hierarchical agglomerative, DBSCAN/HDBSCAN, Gaussian Mixture Models), dimensionality reduction (PCA eigenvalues/variance explained, t-SNE/UMAP for visualization, autoencoders), anomaly/outlier detection (Isolation Forest, LOF, one-class SVM), association rules (Apriori, FP-growth).

**Topic 4.3: Model Interpretation & Debugging**  
- Microtopics: Global/local interpretability (feature importance via permutation/Gini, partial dependence plots/PDP, ICE plots), SHAP/LIME values (additive explanations, TreeSHAP for trees, KernelSHAP), learning curves and bias-variance diagnosis, residual analysis and model diagnostics.

### Macro Topic 5: Advanced AI, Deep Learning & Generative Models
**Topic 5.1: Neural Networks Fundamentals**  
- Microtopics: Perceptron and multi-layer perceptrons, forward/backward propagation (derive gradients with chain rule, vectorized implementation), activation functions (ReLU/LeakyReLU/ELU/GELU/swish, softmax), loss functions (MSE, cross-entropy, hinge), optimizers (SGD with momentum, RMSProp, Adam/AdamW, learning rate schedulers), regularization (L1/L2, dropout, batch/layer normalization, early stopping).

**Topic 5.2: Deep Learning Architectures**  
- Microtopics: Convolutional Neural Networks (CNNs: convolutions, pooling, padding, strides, ResNet/VGG/Inception blocks, transfer learning), Recurrent Neural Networks (RNNs, LSTMs/GRUs for sequences, vanishing gradient solutions, bidirectional), Transformers (self-attention mechanism derivation, multi-head attention, positional encoding, BERT/GPT architecture intuition).

**Topic 5.3: Modern Generative AI Practices**  
- Microtopics: Prompt engineering (zero/few-shot, chain-of-thought, tree-of-thoughts, ReAct), Retrieval-Augmented Generation (RAG: vector stores, embeddings with sentence-transformers, LangChain/LlamaIndex), fine-tuning LLMs (PEFT methods: LoRA/QLoRA, full fine-tuning vs parameter-efficient), evaluation of generative models (BLEU/ROUGE/METEOR/BERTScore, human preference with Elo, perplexity), diffusion models and GANs basics (for image generation tasks).

### Macro Topic 6: MLOps & Production ML Systems
**Topic 6.1: ML Lifecycle & Experiment Tracking**  
- Microtopics: Experiment tracking (MLflow, Weights & Biases, Comet ML), model and data versioning (DVC, Git LFS, LakeFS), pipeline orchestration (Prefect, Airflow, Kubeflow Pipelines, ZenML).

**Topic 6.2: Deployment & Serving**  
- Microtopics: Model serving (FastAPI/Flask REST APIs, TorchServe/TensorFlow Serving, BentoML), containerization (Docker for models, ONNX for interoperability), cloud platforms (AWS SageMaker, Azure ML, GCP Vertex AI, Hugging Face Spaces), batch vs real-time/streaming inference (Kafka/Kinesis for streaming).

**Topic 6.3: Monitoring, Reliability & Scalability**  
- Microtopics: Data and model drift detection (Evidently AI, Alibi Detect, statistical tests like KS/PSI), performance monitoring (Prometheus/Grafana, custom logging), A/B testing and canary/ shadow deployments, CI/CD for ML (GitHub Actions + MLflow, ArgoCD), scalability (PySpark for distributed data, Horovod/Ray for distributed training, Ray Serve).

### Macro Topic 7: Experimentation, Causal Inference & Business Impact
**Topic 7.1: A/B Testing & Experiment Design**  
- Microtopics: Randomized controlled trials (RCTs), power/sample size calculation (using statsmodels or Evan Miller’s formula), randomization and stratification, CUPED variance reduction, sequential testing (always-valid inference), multi-armed bandits (epsilon-greedy, UCB, Thompson sampling), multiple testing in experiments.

**Topic 7.2: Causal Inference**  
- Microtopics: Potential outcomes framework (ATE/ATT/ATU), confounding and selection bias, Directed Acyclic Graphs (DAGs with d-separation), propensity score matching/weighting/inverse probability weighting, difference-in-differences and synthetic control, instrumental variables and two-stage least squares, regression discontinuity design, do-calculus and causal discovery basics (with DoWhy or causalml libraries).

**Topic 7.3: Business Metrics & Storytelling**  
- Microtopics: North-star and proxy metrics definition, cohort analysis and retention curves, funnel analysis, customer lifetime value (CLV) modeling, executive dashboards (Tableau/Power BI/Streamlit), narrative building (insight → recommendation → business impact).

### Macro Topic 8: Visualization, Communication & Professional Skills
**Topic 8.1: Visualization Tools & Principles**  
- Microtopics: Grammar of Graphics (ggplot2/Plotly principles), effective chart selection (bar/line/scatter/heatmap/tree maps), color theory and accessibility (ColorBrewer, Viridis), interactive dashboards (Plotly Dash, Streamlit, Panel, Tableau), geospatial visualization (Folium, Kepler.gl).

**Topic 8.2: Communication & Soft Skills**  
- Microtopics: Structuring presentations (problem-statement → analysis → insight → recommendation → next steps), technical writing (READMEs, project reports, blog posts), stakeholder Q&A handling, cross-functional collaboration (with product/engineering), ethics in DS (bias/fairness/privacy, model cards).