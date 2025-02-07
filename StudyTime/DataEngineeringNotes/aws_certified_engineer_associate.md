**For AWS Certified Data Engineering Associate certificate I am referring to the following Sources**:


YouTube Videos:
- [AWS Certified Data Engineer by Johnny Chivers](https://youtu.be/6G0bLDIcO7Y?si=dpGk17BYnK8UUzwd) - duration 4:44:30
- [Fundamentals of Data Engineering Masterclass](https://youtu.be/hf2go3E2m8g?si=13Ir4O5OLw6c0y3e) - duration 3:02:25
- [AWS Certified Data Engineer by ClayDesk E-learning](https://youtu.be/Xl40yelD4PU?si=sLbKRWalv1kXR1li) - duration 14:12:04

---

- [Types Of Data:](#types-of-data)
  - [1. Structured Data](#1-structured-data)
  - [2. Unstructured Data](#2-unstructured-data)
  - [3. Semi-structured Data](#3-semi-structured-data)
- [Properties of Data](#properties-of-data)
  - [1. Volumes of Data](#1-volumes-of-data)
  - [2. Velocity of Data](#2-velocity-of-data)
  - [3. Variety of Data](#3-variety-of-data)
- [Data Warehouses vs Data Lakes vs Data Lakehouses](#data-warehouses-vs-data-lakes-vs-data-lakehouses)
  - [1. Data Warehouses](#1-data-warehouses)
  - [2. Data Lakes](#2-data-lakes)
  - [3. Data Lakehouses](#3-data-lakehouses)

---

## Types Of Data:
### 1. Structured Data

- **Identifiers**
  - Organized in predefined manner
  - easily searchable
  - stored in tabular format
  - fields are descret and defined
- **Example Types**
  - Databases like MySQL, PostgreSQL
  - Data Warehouse like AWS Redshift
  - Spreadsheets
### 2. Unstructured Data
- **Identifiers**
  - Lacks predefined manor or organisation
  - not easily searchable
  - wide variety of data types
  - wide variety of formats
- **Example Types**
  - Text documents
  - multi-media files
  - social media posts
  - Emails
### 3. Semi-structured Data
- **Identifiers**
  - Elements of both structured and unstructured data
  - does not neatly fit into tabular format
  - has some organisational properties
  - uses tags/markers to separate elements
- **Example Types**
  - XML files
  - JSON files
  - NoSQL Databases
  - HTML contents

---
## Properties of Data

### 1. Volumes of Data
- This will be defined as Scale or Quantity of Data being generated, stored or processed.
- **Challenges**
  - Storage Managements
    - For large amount of data you can consider services like AWS Redshift, AWS S3, and for transactional volumes of data you can use AWS RDS service
  - Processing Power
    - For extremely large amount of data you can consider service like AWS EMR, AWS Lambda.
  - Data Integration and what's the governance structure we can use
    - For data integration, it includes how you catalog the data. You can consider service like AWS Glue or AWS Datazone

### 2. Velocity of Data
- This will be defined as at what speed of data is being generated, transmitted and processed.
- **Challenges**
  - Is it required Real-Time Processing?
  - what is the latency on that data?

### 3. Variety of Data
- This will be defined as diversity of data types, formats and sources.
- **Challenges**
  - Data Integration
    - with different sources, it starts creating complication in data integration.
  - Data Quality
  - Interoperability

---

## Data Warehouses vs Data Lakes vs Data Lakehouses

### 1. Data Warehouses
- it is centralized repository that stores structured from multiple sources
- **Features**
  - it allows schema-on-write, as the data is already processed before storing into data warehouse, so it identifies schema of those data
  - it stored structured data
  - it has fast query performance
  - it ensures data integrity and data consistency
- **Examples**
  - Amazon Redshift
  - Snowflake
  - Google BigQuery

### 2. Data Lakes
- it is centralized repository to store data, both structured and unstructured, at any scale
- **Features**
  - it allows schema-on-read
  - it stored all data with low latency
  - highly scalable
  - allows for data exploration and experimentation
- **Example**
  - Apache Hadoop
  - S3
  - Microsoft Azure Data Lake Storage

### 3. Data Lakehouses
- combines elements of data lakes and data warehouses to provide unified data platform
- **Features**
  - it stored structured and unstructured data
  - it allows schema-on-read and schema-on-write
  - it allows real-time data analytics
  - it minimizes data movement and duplication
- **Example**
  - Databricks Lakehouse
  - Google BigLake
