# 📡 TelecomInvestmentAnalysis

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Folder Organization](#folder-organization)
- [Setup](#setup)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)


## Overview: Key Functionalities

### Task 1 - User Overview Analysis

1. **Handset Analysis**:
   - **Identify Top 10 Handsets**: Analyze and rank the top 10 most frequently used handsets by customers.
   - **Top 3 Manufacturers**: Determine the top 3 handset manufacturers based on the data.
   - **Top 5 Handsets per Manufacturer**: For each of the top 3 manufacturers, identify their top 5 handsets.
   - **Marketing Recommendations**: Provide insights and recommendations to marketing teams based on handset usage.

2. **Behavior Analysis**:
   - **Aggregate User Data**: Calculate metrics such as number of xDR sessions, session duration, total data volume (DL and UL) per user for each application.
   - **Exploratory Data Analysis (EDA)**: Perform EDA to understand the dataset, identify and handle missing values and outliers, and derive insights.
   - **Univariate and Bivariate Analysis**: Analyze individual variables, their distributions, and relationships between variables.
   - **Dimensionality Reduction**: Apply PCA to reduce data dimensions and interpret results.

### Task 2 - User Engagement Analysis

1. **Engagement Metrics**:
   - **Aggregate Engagement Data**: Calculate session frequency, session duration, and total traffic per customer.
   - **Cluster Analysis**: Normalize engagement metrics and apply k-means clustering to categorize users into engagement groups.
   - **Top Engaged Users**: Identify the top 10 most engaged users per application and plot top 3 most used applications.

2. **Clustering and Optimization**:
   - **Determine Optimal k**: Use the elbow method to find the optimal number of clusters for user engagement.
   - **Cluster Interpretation**: Provide insights into the clusters and their characteristics.

### Task 3 - Experience Analytics

1. **Experience Metrics**:
   - **Aggregate Metrics**: Compute average TCP retransmission, RTT, handset type, and throughput per customer.
   - **Top/Bottom Values**: List top 10 and bottom 10 values for TCP retransmission, RTT, and throughput.
   - **Distribution Analysis**: Analyze the distribution of throughput and TCP retransmission by handset type.

2. **Experience Clustering**:
   - **K-means Clustering**: Segment users into experience clusters and describe each cluster based on network parameters and device characteristics.

### Task 4 - Satisfaction Analysis

1. **Satisfaction Scoring**:
   - **Compute Scores**: Assign engagement and experience scores based on clustering results and calculate satisfaction scores.
   - **Top Satisfied Users**: Identify the top 10 satisfied customers based on their scores.

2. **Regression and Clustering**:
   - **Predictive Modeling**: Build a regression model to predict satisfaction scores.
   - **Clustering on Scores**: Run k-means clustering on engagement and experience scores to find satisfaction clusters.
   - **Score Aggregation**: Aggregate average satisfaction and experience scores per cluster.

3. **Data Export and Deployment**:
   - **Export Data**: Export user scores to a MySQL database and provide a screenshot of the query results.
   - **Model Deployment**: Deploy the model using Docker or MLops tools and track its performance with a detailed report.

### Dashboard Development

1. **Design and Development**:
   - **Visualization Tools**: Create a dashboard using visualization libraries to display insights effectively.
   - **Usability**: Ensure the dashboard is user-friendly, with intuitive navigation and clear labels.
   - **Interactivity**: Incorporate interactive elements to enhance user engagement.
   - **Deployment**: Deploy the dashboard and make it accessible via a public URL.


## Technologies

This repository contains the backend code used to provide services to the client. It is written in Python and utilizes various libraries and frameworks for data analysis, technical indicators, and web application development. The project follows a modular structure with clear separation of concerns to ensure maintainability and scalability.

The set of technologies we utilized in this project:

1. **Programming Language**: [![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=yellow)](https://www.python.org/)
2. **Data Visualization**: [![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-3776AB?style=flat&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4D8A?style=flat&logo=plotly&logoColor=white)](https://plotly.com/)
3. **Data Manipulation**: [![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Data_Manipulation-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
4. **Version Control**: [![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=flat&logo=git&logoColor=white)](https://git-scm.com/)
5. **Data Hosting**: [![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=flat&logo=googledrive&logoColor=white)](https://www.google.com/drive/)
6. **Scikit-Learn**: [![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
7. **Seaborn**: [![Seaborn](https://img.shields.io/badge/Seaborn-6D9EC1?style=flat&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)


## Folder Organization

```
📁.github
└──
    └── 📁workflows
         └── 📃blank.yml
└── 📁notebooks
         └── 📓userEngagmentanalysis.ipynb
         └── 📓userOveriewAnalysis.ipynb
└── 📁scripts
         └── 📃__init__.py
         └── 📃customer_engagment.py
         └── 📃data_cleanming_and_preprocessing.py
         └── 📃db_setup.py
         └── 📃edaForAgeregatedData.py
         └── 📃models.py
         └── 📃overviewOverSpecificApplication.py
         └── 📃useroverview.py
         └── 📃userOverviewOverCleanedData.py
└── 💻src
    └── 📁dashboard-div
                    └── 📝app.py
└── ⌛tests
         └── 📃__init__.py
         
└── 📜.gitignore
└── 📰README.md
└── 🔋requirements.txt
└── 📇setup.py.py
└── 📇TA_Lib-0.4.29-cp312-cp312-win_amd64.whl
└── 📇templates.py

```

### Folder Structure: A Deep Dive

- **📁.github**: This folder contains GitHub-related configurations, including CI/CD workflows.

  - **📁workflows**: Contains the CI/CD pipeline definitions.
    - **📃blank.yml**: Configuration for Continuous Integration.
    - **📃unittests.yml**: Configuration for running unit tests.

- **📁notebooks**: This directory holds Jupyter notebooks and related Python files.
    ## 📓 User Engagement Analysis
**Overview**: This notebook focuses on analyzing user engagement with telecom services. It helps in understanding how users interact with different applications and provides insights into improving user experience and QoS (Quality of Service).

### **Tasks**
1. **User Overview Analysis**:
   - **Objective**: Conduct an Exploratory Data Analysis (EDA) to understand user behavior and provide insights based on telecom dataset.
   - **Sub-tasks**:
     - Identify the top 10 handsets used by customers.
     - Determine the top 3 handset manufacturers.
     - Identify the top 5 handsets per top 3 manufacturers.
     - Make recommendations to marketing teams based on findings.
   - **Data Analysis**:
     - **Task 1.1**: Aggregate user data across various applications (e.g., Social Media, Google, Email, etc.), focusing on session details and data usage.
     - **Task 1.2**: Conduct EDA, handle missing values and outliers, perform statistical analyses, and visualize data:
       - Describe variables and their types.
       - Segment users into deciles based on session duration.
       - Compute and analyze basic metrics (mean, median, etc.).
       - Perform univariate and bivariate analyses.
       - Compute correlation matrix and perform PCA for dimensionality reduction.

2. **User Engagement Analysis**:
   - **Objective**: Assess user engagement across applications to improve network resource allocation and enhance user experience.
   - **Sub-tasks**:
     - Aggregate engagement metrics (session frequency, duration, total traffic) per customer.
     - Normalize metrics and apply k-means clustering to classify customers into engagement groups.
     - Analyze and interpret metrics for each cluster.
     - Identify top 10 engaged users per application and visualize the top 3 most used applications.
     - Optimize and determine the number of engagement clusters using the elbow method and interpret results.

### **Key Insights**
- **User Behavior**: Insights into handset usage and manufacturer preferences.
- **Engagement Metrics**: Understanding of user engagement through detailed metrics and clustering.
- **Recommendations**: Actionable insights for marketing and technical teams to enhance user experience and optimize resource allocation.

- **📁scripts**: Contains Python scripts used throughout the project.

  - ## Modules Overview

This directory contains essential Python modules for analyzing and processing customer engagement data. Each module serves a specific purpose in the data analysis pipeline.

### **Modules**

- **📃 `__init__.py`**: Initializes the package and allows importing of modules.

- **📃 `customer_engagment.py`**: Contains functions for analyzing customer engagement metrics, including session frequency, duration, and total traffic.

- **📃 `data_cleanming_and_preprocessing.py`**: Provides utilities for data cleaning and preprocessing, such as handling missing values, outliers, and data transformation.

- **📃 `db_setup.py`**: Handles the setup and configuration of the database, including connections and schema initialization.

- **📃 `edaForAgeregatedData.py`**: Performs Exploratory Data Analysis (EDA) on aggregated data, including visualization and statistical analysis.

- **📃 `models.py`**: Defines the data models and structures used in the project, including ORM models for database interactions.

- **📃 `overviewOverSpecificApplication.py`**: Analyzes user engagement and behavior for specific applications, providing insights into usage patterns.

- **📃 `useroverview.py`**: Contains functions for conducting a comprehensive overview analysis of user behavior, including handset usage and manufacturer preferences.

- **📃 `userOverviewOverCleanedData.py`**: Performs analysis on cleaned data to provide an overview of user behavior and engagement metrics, focusing on accuracy and reliability.

### **Usage**
These modules are designed to be used in conjunction with each other to streamline the data analysis process, from data preparation and cleaning to in-depth analysis and model creation.


- **💻src**: The main source code of the project, including the Streamlit dashboard and other related files.

  - **📁dashboard-div**: Holds the code for the dashboard.
    - **📝app.py**: Main application file for the dashboard.
    - **📝README.md**: Documentation specific to the dashboard component.

- **⌛tests**: Contains test files, including unit and integration tests.

  - ****init**.py**: Initialization file for the test module.

- **📜.gitignore**: Specifies files and directories to be ignored by Git.

- **📰README.md**: The main documentation for the entire project.

- **🔋requirements.txt**: Lists the Python dependencies required to run the project.

- **📇setup.py.py**: used to authenticate who the package writer is.

- **📇TA_Lib-0.4.29-cp312-cp312-win_amd64.whl**: A TA-lib library data used for installing in windows.

- **📇templates.py**: Contains templates used within the project, possibly for generating or processing data.

## Setup

1. Clone the repo

```bash
git clone https://github.com/Bereket-07/User_Analysis_and_Engagement.git
```
2. Change directory

```bash
cd User_Analysis_and_Engagement
```

3. Install all dependencies

```bash
pip install -r requirements.txt
```

4. change directory to run the streamlit app locally.

```bash
cd src\dashboard-div
```

5. Start the streamlit app

```bash
streamlit run app.py
```

## Contributing

We welcome contributions to this project! To get started, please follow these guidelines:

### How to Contribute

1. **Fork the repository**: Click the "Fork" button at the top right of this page to create your own copy of the repository.
2. **Clone your fork**: Clone the forked repository to your local machine.
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
3. **Create a new branch**: Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature
   ```
4. **Make your changes**: Implement your feature or fix the bug. Ensure your code adheres to the project's coding standards and style.
5. **Commit your changes**: Commit your changes with a descriptive message.
   ```bash
   git add .
   git commit -m 'Add new feature or fix bug'
   ```
6. **Push your branch**: Push your branch to your forked repository.
   ```bash
   git push origin feature/your-feature
   ```
7. **Create a Pull Request**: Go to the repository on GitHub, switch to your branch, and click the `New Pull Request` button. Provide a detailed description of your changes and submit the pull request.

## Additional Information

- **Bug Reports**: If you find a bug, please open an issue in the repository with details about the problem.

- **Feature Requests**: If you have ideas for new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License

### Summary

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). It is a simple and easy-to-understand license that places very few restrictions on reuse, making it a popular choice for open source projects.

By using this project, you agree to include the original copyright notice and permission notice in any copies or substantial portions of the software.
