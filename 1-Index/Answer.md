# 1.
### 1. Data Compression

This technique reduces file size to optimize storage and transmission.

- **Lossy Compression:** Removes irrelevant or redundant data to save space, though some quality is lost (e.g., MP3, JPEG).
    
- **Lossless Compression:** Retains all original data by finding patterns, allowing for exact reconstruction (e.g., ZIP, PNG).
    
    - **Huffman Coding:** A specific lossless method that assigns shorter codes to frequent symbols.
        

### 2. Data Storage Solutions

These are specialized systems for keeping data organized and accessible.

- **Relational Databases:** Store structured data in tables using SQL for management (e.g., MySQL, PostgreSQL).
    
- **NoSQL Databases:** Designed for unstructured data like social media content (e.g., MongoDB, Cassandra).
    
- **Data Warehouses:** Store integrated data from multiple sources specifically for complex analysis (e.g., Amazon Redshift).
    
- **Cloud Storage:** Provides scalable, remote access to datasets (e.g., Amazon AWS, Microsoft Azure, Google Cloud).
    
- **Object Storage:** Stores data as objects, ideal for unstructured data (e.g., Amazon S3).
    

### 3. Data Indexing

Indexing organizes data to speed up retrieval, avoiding slow sequential searches.

- **B-tree Indexing:** Uses a tree structure for efficient range searching.
    
- **Hash Indexing:** Uses hash functions to map data to specific indices for fast retrieval.
    
- **Bitmap Indexing:** Creates bitmaps for quick identification of matching records.
    

### 4. Data Chunking
 
Also known as segmentation, this divides large datasets into smaller, manageable "chunks" (with metadata) to handle capacity limits.

- **Benefits:** It increases processing speed, improves resource utilization across machines, and offers better fault tolerance (only the affected chunk needs recovering).
    

### 5. Cloud Computing

This provides cost-effective remote infrastructure for storage and analysis.

- It allows access to advanced tools like machine learning and data warehouses without heavy local hardware.
    
- **Examples:** Amazon AWS, Microsoft Azure, Google Cloud.
    

# 2.
### **What is Big Data?**

Big Data is defined as any data that is too huge and complex to be processed using traditional processing systems. Essentially, it refers to datasets that are beyond the computational capability of standard data-processing tools.

### **The Four Vs of Big Data**

Big Data is characterized by four specific dimensions, often referred to as the "Four Vs":

**1. Volume**

This refers to the sheer amount of data being generated daily across different media.
It is quantified using massive units such as gigabytes (1 billion bytes), terabytes ($10^{12}$ bytes), and sometimes petabytes ($10^{15}$ bytes).
All industries are currently grappling with the dilemma of how to handle such vast amounts of data.
    

**2. Velocity**

This refers to the speed at which data gets generated.
Data generation occurs rapidly, often measured by hours or even milliseconds.

**3. Variety**

This refers to the different forms data can take, such as tables, text, voice, or video. The text classifies these into three types:
Structured Data: Typically captured in spreadsheets (like Excel) and represented by rows and columns.
Semi-structured Data: Includes emails, chats, phone conversations, image files, graphics, and sensor data (GPS, RFID, smart meters).
Unstructured Data: Includes social media content like chats, videos, and Twitter feeds, which require specific algorithms to process.

**4. Veracity**

This deals with the authenticity of the captured data, specifically whether it is trustworthy and bias-free.
Ensuring authenticity is a huge challenge due to the high speed (velocity), volume, and variety of the data being generated.

# 3.

### **1. Web Scraping**

**Definition:** The process of automatically extracting data from websites using tools (scrapers).

- **Example:** A travel company collecting hotel prices from various booking sites to create a strategy without manual work.
    
- **Common Techniques:**
    
    - **Web Crawling:** Navigating through links to collect data from multiple pages.
        
    - **HTML Parsing & XPath:** Analyzing page structure and navigating HTML tags to find specific data.
        
    - **Regular Expressions:** Searching for specific patterns (e.g., emails, phone numbers).
        
    - **APIs & JSON/XML:** Directly accessing structured data systems without scraping the interface.
        

![Image of web scraping process diagram](https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRjT_Vk8UdU3-QlsqnR7wGWRIAhAVSF7PZ4ABsOVF420vEPWOc1kLjHUyUyPoPFwLLIz9CWRadDP9tJNYa8WVyes_qrWi4E3OvANyGYbopY8SHttdw)
### **2. Social Media Data Collection**

**Definition:** Gathering information from platforms like Twitter or Instagram using APIs or monitoring tools.

- **Example:** Analyzing tweets with specific hashtags to measure customer satisfaction and preferences.
    
- **Common Techniques:**
    
    - **API Integration:** Retrieving structured data based on user interactions.
        
    - **Social Listening:** Monitoring online conversations to detect trends and behavior.
        
    - **Network Analysis:** Mapping relationships to identify influencers.
        
# 4.
 
Importance's of python programming in
data science:
1. Scripting Language with Structured Programming
Style: Python's scripting capabilities with a
structured programming style make it efficient for
writing and executing data science algorithms.
2. Dynamic Built-in Data Structures: Python has
dynamic data structures that are highly useful for
data manipulation and analysis, which is essential in
data science.
3. Database Connectivity: Python provides interfaces
to connect to databases like MySQL, Oracle, and
PostgreSQL, enabling data scientists to access,
manipulate, and analyze large datasets stored in
relational databases.
4. Extensible Language: Python can be integrated with
other programming languages such as C and C++,
allowing data scientists to leverage existing tools and
optimize performance when necessary.
5. Libraries for Internet Protocols: Python has built-in
libraries for handling Internet protocols such as
HTML, XML, JSON, and more, which are critical for
web scraping and web-based data collection for data
science projects.
These features make Python a powerful and versatile tool
for various data science tasks.

# 5.

### **1. Data Structures**

Data is classified based on its organization and how easily it can be managed by traditional systems.

- **Structured Data:**
    
    - **Definition:** This data is highly organized and follows a rigid format, typically utilizing rows and columns.
        
    - **Examples:** Excel sheets, spreadsheets, and data stored in **Relational Databases** (like MySQL or PostgreSQL) which use tables to store information.
        
- **Semi-Structured Data:**
    
    - **Definition:** This data does not reside in a fixed database format (like a strict table) but contains some organizational properties like tags or markers to separate data elements.
        
    - **Examples:** Emails, chats, phone conversations, image files, graphics, and sensor data from sources like GPS, RFID, and smart meters.
        
    - **Formats:** While not explicitly listed in the images, this category often includes formats like JSON or XML used in API data exchange (as mentioned in your previous text regarding web scraping).
        
- **Unstructured Data:**
    
    - **Definition:** This data lacks a pre-defined data model and is the most complex to process. It is growing rapidly due to social media usage.
        
    - **Examples:** Social media content (Twitter feeds, chats), videos, voice recordings, and complex medical imagery like X-rays or CT scans.
        
    - **Storage:** **NoSQL Databases** (like MongoDB) and **Object Storage** (like Amazon S3) are specifically designed to handle this type of data.
        

### **2. Dataset File Formats (Compression)**

The documents also highlight specific file formats used to compress datasets for efficient handling.

- **Lossy Formats:** These reduce file size by removing some data, commonly used for multimedia.
    
    - **Examples:** **MP3** (audio) and **JPEG** (images).
        
- **Lossless Formats:** These reduce file size without losing any information, allowing for exact reconstruction.
    
    - **Examples:** **ZIP** (archives) and **PNG** (images).
        

# 6.

the pros and cons of data science are:
Pros:
1. ==Data-Driven Decision Making:== Technology and machine learning in data science allow for automated, data-driven decisions, improving efficiency and accuracy in various tasks.
2. ==Machine Learning and AI:== Data scientists use machine learning and artificial intelligence to process and analyze large datasets, enabling faster and more accurate decision-making.
3. ==Abundant Data Collection:== The ability to collect vast amounts of data has enhanced the capacity to analyze and understand complex patterns, which leads to improved insights and better predictions.
Cons:
4. ==Ethical and Privacy Concerns:== With the ability to collect vast amounts of personal data (e.g., contact information, health records, location, photos, and search history), there are growing concerns about who can access and use this data. People are worried about their privacy being compromised.
5. ==Bias in Data:== Machine learning algorithms and AI systems are trained on historical data. If that data has biases, the algorithms will also inherit those biases and may make biased decisions.
6. ==Lack of Consent:== Many individuals do not know when their data is being collected, or who has access to it, raising issues about consent and privacy.

# 7.

==Popular Database Software==

- **Relational Databases (SQL):** These organize data into structured tables (rows and columns).
    
    - **PostgreSQL:** The most advanced open-source option.
        
    - **MySQL:** The most popular for web applications.
        
    - **SQLite:** Lightweight and embedded (used in phones/browsers).
        
    - **Microsoft SQL Server:** Enterprise-grade with tight Windows integration.
        
    - **Oracle Database:** Powerful, complex, used by large enterprises.
        
- **NoSQL Databases:** These are non-tabular and handle unstructured or semi-structured data.4
    
    - **MongoDB:** Document-based (stores data like JSON files).
        
    - **Redis:** Key-Value store (stores data in memory for extreme speed).
        
    - **Cassandra:** Wide-column store (good for massive data across many servers).
        
    - **Neo4j:** Graph database (good for connecting relationships, like social networks).
        
- **Cloud Data Warehouses:**
    
    - **Snowflake:** Built specifically for the cloud to handle massive analytics workloads.
        
    - **Google BigQuery:** Serverless data warehouse for analytics.
        
# 8.

Schema:
• A schema is the structure that defines how data is organized in a dataset or database, including:
o Attributes/Features: Columns representing data characteristics (e.g., Semester, Instructor).
o Entities/Items: Rows representing individual data entries (e.g., specific classes).
o Relationships: How different data points are connected.
o Data Types: Specifies the type of data each attribute holds (e.g., integers, text).

# 9.

Similarity: 

| **Aspect**          | **Description**                                                                    |
| ------------------- | ---------------------------------------------------------------------------------- |
| **Data Analysis**   | Both involve analyzing data to extract insights.                                   |
| **Methods**         | Both use quantitative methods, including statistical and computational techniques. |
| **Decision-Making** | Both aim to inform decisions based on data.                                        |

Difference: 

| **Aspect**  | **Statistics**                                                       | **Data Science**                                                                                         |
| ----------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Focus**   | Focuses on analyzing **structured data** to make inferences.         statistics, machine learning, and computer science, handling both **structured and unstructured data**. *. |
| **Methods** | Uses traditional statistical techniques like **hypothesis testing**. | Uses **advanced algorithms**, machine learning, and big data too                                         |
| **Goal**    | Aims to understand **data relationships** and test hypotheses.       | Focuses on building **predictive models** and finding patterns in complex d                              |

# 10.

## **Data Cleaning and Preprocessing**

Data cleaning and preprocessing is an important stage in any data science task. It refers to the technique of organizing and converting raw data into usable structures for further analysis. It involves extracting irrelevant or duplicate values, handling missing values and correcting errors. This ensures that the data is accurate, comprehensive and ready for analysis. Data cleaning and preprocessing typically involve the following steps:

- **(I) Data integration:** It refers to merging data from multiple sources into a data set.
    
- **(II) Data cleaning:** In this step, data is assessed for any errors or inconsistencies and appropriate actions are taken to correct them. This may include removing duplicate values, handling missing values/data and correcting formatting misconceptions.
    
- **(III) Data transformation:** The step prepares the data for the next step by transforming into a format that is suitable for further analysis. This may involve converting data type, scaling or normalizing numerical data or encoding categorical values.
    
- **(IV) Data reduction:** If the data set contains a large number of columns or features, data reduction method may be used to select only the most appropriate ones for analysis.
    
- **(V) Data discretization:** It involves grouping continuous data into categories or ranges which can help facilitate analysis.
    
- **(VI) Data Sampling:** In some cases, the data may be too large to analyze in its entirety. In such cases, a representative subset of the data is selected for analysis while still maintaining the overall characteristics of the original.
    
# 11. 


## **Origins and Foundation of Data Science**

While information technology began generating and processing data in the early 19th century, the true foundation of modern data science was laid over 50 years ago. This foundation is attributed to **John W. Tukey**, a mathematician who published the pivotal article "The Future of Data Analysis".

### **Key Pioneers and Contributions**

Several prominent figures played crucial roles in establishing data science as an indisputable domain:

- **John Chambers:** Designed the S system, which served as the basis for future statistical programming languages, including R. He received the Software System Award in 1999.
    
- **Jeff Wu:** A Professor at Georgia Tech who officially coined the term "Data Science" in 1997.
    
- **William Cleveland:** A Distinguished Professor at Purdue University known for authoring significant books on data visualization.
    
- **Leo Breiman:** A distinguished statistician at UC Berkeley and a pioneer in machine learning techniques.
    

### **Modern Evolution**

The 20th century witnessed drastic advancements in generating, capturing, and processing data, moving the field far beyond its 19th-century roots.

---
# 12.
## **Foundational Fields of Study**

Data science is drawn from three traditional fields that act as its foundation:

1. **Mathematics and Statistics:** These form the logic underlying algorithms. Key concepts include descriptive and inferential statistics, probability, hypothesis testing, and mathematical modeling for optimal decision-making.
    
2. **Computer Science (Information Technology):** Provides the structure for algorithms. It involves using high-level programming languages like R and Python, designed to be accessible even to non-programmers.
    
3. **Domain Knowledge:** Expert knowledge in a specific area of application is crucial for creating metrics and making sense of data for decision-making.
    
    - **Medicine:** Used to interpret model outputs using specific medical terms.
        
    - **Engineering:** Used to understand and solve problems specific to various engineering branches.
        

---
# 13.
## **Data Science and Decision-Making**

Data science is the science of understanding data using processes, tools, and techniques to aid in decision-making. It involves moving from intuition-based to data-based decisions through three main steps:

1. **Data Visualization:** Identifying, collecting, and exploring data using plots and graphs to spot trends (e.g., identifying months with maximum rainfall).
    
2. **Data Mining:** Probing deeply to derive patterns and average information from the data.
    
3. **Model Building:** Using past data to predict future outcomes (e.g., predicting if it will rain tomorrow).
    

---
# 14. 
## **Types of Data**

1. **Structured Data:** Resides in fixed fields within a record and relies on a defined data model (e.g., an Excel table). SQL is the preferred method for querying this data.
    
2. **Unstructured Data:** Difficult to fit into a standard model because content varies or is context-specific (e.g., email body content).
    
3. **Natural Language:** A sub-category of unstructured data involving linguistics and ambiguity. It is highly challenging because words can have different meanings based on emotion or intent.
    
4. **Machine-generated Data:** Information created automatically by computers or sensors without human intervention (e.g., web server logs, telemetry, and IoT).
    
5. **Graph-based (Network) Data:** Focuses on relationships between objects using nodes, edges, and properties (e.g., Facebook or LinkedIn connections).
    
6. **Audio, Image, and Video:** Easy for humans to recognize but difficult for computers; deep learning algorithms are used for interpretation.
    
7. **Streaming Data:** Data that flows in real-time as events occur rather than being loaded in batches (e.g., "Trending" topics on Twitter or stock market tickers).
    

---
# 15.
## **Data Storage for Big Data**

Big data requires storage solutions that can handle large volumes, offer high performance for access, and guarantee scalability and reliability. Common types include:

1. **Relational Database:** Organizes data in tables and uses SQL for retrieval and management. It is used for traditional structured data like financial information.
    
2. **NoSQL Database:** Designed to handle unstructured data, such as social media content or data from sensors, using non-relational data models.
    
3. **Data Warehouse:** A centralized repository that combines data from multiple sources to allow for complex query and analysis, commonly used for business intelligence reporting.
    
4. **Cloud Storage:** Storing data on remote servers accessed over the internet, offering scalability and cost-effectiveness.
    
5. **Object Storage:** Data is stored as objects consisting of both data and metadata; often used for images and videos.

# 16.

5: Describe about the data Science process. Time : / Date : /


(I) The first step is to identify the problem and define the problem statement

(II) The second step is to collect the data from the different sources. The data should be collected to adress the problem in the organization.

(III) The third step is exploratory data analysis. It involves the steps in data preprocessing

(IV) The fourth step is to visualize the data

(V) The fifth step is to prepare the data for Model building. It involves creating new variable or doing factor analysis to reduce the number of variable.


machine learnings algorithms and advanced ensemble, deep learning and AI techniques.

data science process model :

object > Data collection > Exploratory Data analysis > Data visualization > Dimensionality reduction > Model building.


# 17.

![[Pasted image 20251218211848.png]]
Types of Correlation
(a) POSITIVE: If the values of the two variables deviate in the same direction(both increase/ decrease same time)

Some examples of series of positive correlation are :
(i) Heights and weights.
(ii) The family income and expenditure on luxury items.
(iii) Amount of rainfall and yield of crop (up to a point).
(iv) Price and supply of a commodity and so on.

AND NEGATIVE:  if the variables deviate in the opposite direction

Some examples of negative correlation are the series relating to :
(i) Price and demand of a commodity.
(ii) Volume and pressure of a perfect gas.
(iii) Sale of woollen garments and the day temperature, and so on.

