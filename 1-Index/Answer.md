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

[^1]: 
