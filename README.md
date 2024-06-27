# Phase 1: Stock Market Data Pipeline and Automation

**Project Manager and Report Author: Kahee Chan**  
**Project Duration: 6/16/2024 - 6/23/2024**  
**Contact Information: chankahee06731@gmail.com**

---

## Table of Contents

- [Executive Summary](#executive-summary)
- [Objectives](#objectives)
  - [Data Extraction](#data-extraction)
  - [Data Transformation](#data-transformation)
  - [Data Loading](#data-loading)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Cloud Computing Solution Walk-through](#cloud-computing-solution-walk-through)
- [Challenges and Solutions](#challenges-and-solutions)
- [Results](#results)
- [Extension, Applications, and Future Work](#extension-applications-and-future-work)
- [Contributing](#contributing)
- [License](#license)

---

## Executive Summary

**Stock Market Data Pipeline Automation** is the First Phase of the **Algorithmic Trading and Stock Data Analysis Project**. It aims to develop an efficient and sustainable way to maintain the continuity of data updating through the process of collecting, processing, and storing, which serves as the foundation for future stock analysis, decision making, and trading strategies. This report presents the final outcome of this phase.

The primary objective for **Phase 1: Stock Market Data Pipeline and Automation** is to develop an automated data pipeline for updating **SPY market data** in a **SQL database** using **Amazon Web Services (AWS)**. It ensures that the data is continuously updated without disruption, significantly reducing the time for data extraction on a local machine through manual intervention and increasing the ability to store data using SQL databases instead of local CSV files.

The phase automates the following routine: **Data Extraction → Data Transformation → Data Loading**. It sets up an **AWS Lambda Function** to retrieve data from the **yfinance API**, maintain consistency and accuracy for the extracted data, and store it in an **Amazon RDS PostgreSQL Database**. **AWS EventBridge** and **AWS CloudWatch** are used to schedule the data updates, handle errors, and provide logging mechanisms to monitor the pipeline’s performance.

Despite the challenges, the project successfully established an automated stock market data pipeline that updates the SPY data daily. This setup significantly reduces manual effort and improves data organization, providing a strong foundation for future project phases.

---

## Objectives

### Data Extraction

- Develop and Deploy AWS Lambda Functions to retrieve **SPY Stock Market Data** from the yfinance API on a daily basis.

### Data Transformation

- Align and clean newly retrieved data from the yfinance API to the basic format of the original setup of the PostgreSQL Database.
- Introduce two separate modes, ‘append’ and ‘replace,’ to optimize the overall time execution.

### Data Loading

- Store the processed data in an **Amazon RDS PostgreSQL Database** to reduce manual intervention and increase the ability to handle a large volume of data.

### Automation

- Use AWS EventBridge and AWS CloudWatch to schedule data updates, handle errors, and implement logging mechanisms.
- Automatically send an email using the smtplib Python package to users to confirm a successful update.

---

## Technologies Used

- **Python 3.10**: Programming language for developing project algorithms, automation scripts, and application code.
- **boto3**: Package to upload and retrieve CSV files containing ticker data.
- **yfinance**: API for SPY Data Extraction.
- **pandas**: Package for Data Organization, Transformation, and Formatting for PostgreSQL.
- **sqlalchemy**: Package to connect PostgreSQL and upload SPY data.
- **smtplib**: Package to send email confirmations.
- **Docker**: Packaging the application code and dependencies into a single container package.
- **AWS Services**: S3, ECR, Lambda, RDS, EventBridge, CloudWatch, IAM, CLI.

---

## Installation

To set up this project locally, follow these steps and AWS Setup Reference Here:
https://www.notion.so/Phase-1-Stock-Market-Data-Pipeline-and-Automation-15eb0b4c7e45476ba35dd22d0e899adb?pvs=4#9110a1cced7a4e899131368cf335b160

**Clone the repository**:
   ```sh
   git clone https://github.com/kaheechan/algorithmic-trading-and-stock-market-analysis.git
  ```

---

## Challenges and Solutions

Problem: Local Machine Dependency
Solution: Use AWS services (Lambda, RDS, EventBridge) to automate the ETL process without relying on a local machine.

Problem: "Unable to import module" Error
Solution: Use Docker to package the application and its dependencies.

Problem: Large File Size
Solution: Use Docker to build and deploy the application, avoiding AWS Lambda size limitations.

---

## Results

SPY Market Data successfully updated based on the crom scheduler, there are 4 main benefits for completing this phase:

Easy Data Accessibility: Automates data extraction using yfinance API, including dividends data.
Efficient Data Management: Reduces the time and effort for data processing, eliminates the need for local storage.
Automatic Email Confirmation: Sends confirmation emails for successful updates.
Reliability: Utilizes AWS infrastructure for a robust and scalable solution.

---

## Extension, Applications, and Future Work

Future Phases
Phase 2: Stock Market Data Analysis and Automation

Data Analysis for SPY Market Data using technical analysis and automated recommendations.
Phase 3: Individual Stock Data Analysis and Automation

Extending analysis to individual stocks within the SPY Market.
Long-term Goals
Implement AI, Data Science, Econometrics, and other advanced techniques to enhance the project.

---

## License
LICENSE

