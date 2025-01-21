# Spotify Data Pipeline using AWS Services

## Overview
This project demonstrates how to build a scalable and efficient data pipeline to process Spotify data using AWS services such as **S3**, **Glue**, **Athena**, and **Crawler**. The data source used for this project is an open-source Spotify dataset from Kaggle.

## Key AWS Services Used
- **Amazon S3**: For storing raw and processed data.
- **AWS Glue**: For data transformation and cleaning.
- **AWS Glue Crawler**: For creating table schemas and cataloging data.
- **Amazon Athena**: For querying the processed data.

## Data Source
The dataset is sourced from Kaggle and consists of three CSV files:
- **artists.csv**: Contains information about artists.
- **albums.csv**: Contains information about albums.
- **tracks.csv**: Contains information about tracks.

## Project Workflow
### Architecture
![Spotify Data Pipeline Architecture](https://github.com/srujanguptha/Spotify_ETL_AWS/blob/main/Architecture.png)

### Step 1: Initial Setup
1. **Dataset Download**: Downloaded the Spotify dataset from Kaggle.
2. **AWS IAM Role Creation**: 
   - Created an IAM user role with restricted access to the following AWS services:
     - **Amazon S3**
     - **AWS Glue**
     - **AWS Glue Crawler**
     - **Amazon Athena**

### Step 2: Data Storage in S3
1. Created an S3 bucket named **spotify_ETL_project**.
2. Organized the bucket into two folders:
   - **staging/**: To store raw CSV files.
   - **datawarehouse/**: To store processed and transformed data.
3. Uploaded the raw dataset (artists.csv, albums.csv, tracks.csv) into the **staging/** folder.

### Step 3: Data Transformation with AWS Glue
1. **AWS Glue Job Creation**:
   - Set up a Glue job to process and transform the data.
   - Loaded the raw data from the **staging/** folder.
2. **Joining Tables**:
   - Performed joins between the three datasets (artists, albums, tracks) to consolidate the information.
3. **Field Selection and Cleaning**:
   - Removed unnecessary columns from the data to keep it relevant and concise.
4. **Data Output**:
   - Saved the transformed and cleaned data into the **datawarehouse/** folder in the S3 bucket.
## Glue Visual
![Glue visual](https://github.com/srujanguptha/Spotify_ETL_AWS/blob/main/AWS_Glue_Visual.png)


### Step 4: Crawling Data with AWS Glue Crawler
1. Created an AWS Glue Crawler to:
   - Crawl the data in the **datawarehouse/** folder.
   - Automatically infer the schema and generate table definitions in the AWS Glue Data Catalog.

### Step 5: Querying Data with Amazon Athena
1. Configured Amazon Athena to connect to the AWS Glue Data Catalog.
2. Queried the processed data stored in the **datawarehouse/** folder using SQL in Athena.
3. Verified that the transformations were successful and generated insights from the data.

## Key Highlights
- **Data Processing**:
  - Raw data was cleaned, transformed, and joined to create a unified dataset.
- **Schema Generation**:
  - AWS Glue Crawler automatically inferred schemas, reducing manual effort.
- **Querying with Athena**:
  - Enabled querying of large datasets directly from S3 using standard SQL.

## AWS Glue Crawler: Use Case
The AWS Glue Crawler simplifies schema generation and table creation in the Glue Data Catalog by:
- Scanning the data in the S3 **datawarehouse/** folder.
- Automatically detecting changes in the schema when new data is added.
- Creating or updating tables in the Glue Data Catalog for use with Athena.

## Tools and Technologies
- **Amazon S3**: For data storage.
- **AWS Glue**: For ETL (Extract, Transform, Load) processing.
- **AWS Glue Crawler**: For schema inference and data cataloging.
- **Amazon Athena**: For interactive querying of processed data.
- **Kaggle**: For sourcing the dataset.

## Results
- Successfully built an automated data pipeline to transform raw Spotify data into a clean and queryable dataset.
- Utilized Athena to generate insights, showcasing the efficiency and scalability of the pipeline.

## Challenges Faced
- **Schema Design**: Determining the appropriate schema for the final dataset required careful planning.
- **Data Cleaning**: Ensuring data integrity and removing unnecessary fields were critical for accurate results.
- **AWS Configuration**: Setting up IAM roles and managing permissions required attention to detail.

## Future Enhancements
- Integrate **AWS Lambda** to trigger Glue jobs and Crawlers automatically.
- Use **AWS QuickSight** for data visualization and reporting.
- Add support for streaming data using AWS Kinesis.

## How to Run the Project
1. Download the dataset from Kaggle and upload the files to the **staging/** folder in your S3 bucket.
2. Configure the Glue job to process the data and store the output in the **datawarehouse/** folder.
3. Run the Glue Crawler to create table schemas.
4. Use Athena to query the processed data.
