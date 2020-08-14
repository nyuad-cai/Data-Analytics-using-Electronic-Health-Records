
# Data Analytics Pipeline to Predict Outcomes using Structured Medical Data (Electronic Health Records)

Table of contents
=================

<!--ts-->
   * [About the repository](#About-the-repository)
      * [Authors](#Authors)
      * [Requirements](#Requirements)
   * [Repository Content](#Repository-Content)
      * [Dataset](#Dataset)
      * [Exploratory Data Analysis](#Exploratory-Data-Analysis)
      * [Data preprocessing](#Data-preprocessing)
      * [Model](#Model)
      * [Plausible Data Dictionary](#Plausible-Data-Dictionary)
  * [Citation](#Citation)
<!--te-->
About the repository
============

<p align="center">
<img src="https://github.com/Ghadeer-O/Data-Analytics-using-Electronic-Health-Records/blob/master/logo.jpg " width="400" height="340"> 
</p>
This repository contains a generic EHR (Electronic Health Records) preprocessing pipeline completed at the Clinical AI Lab, New York University Abu Dhabi.
<<<<<<< HEAD
=======

>>>>>>> b3832fb699552051745de0c0c1275cf5f7d411af

Authors
--------------
Ghadeer Ghosheh : Research Assistant, Clinical AI Lab

Farah Shamout: Assistant Professor Emerging Scholar, Clinical AI Lab


Requirements
--------------
Please clone and download the project, unzip it to your preferred folder. Then run the following code in your computer to download the requirements.

```
pip install -r requirements.txt
```

Repository Content
====================
![Preprocessing highlights](https://github.com/Ghadeer-O/Data-Analytics-using-Electronic-Health-Records/blob/master/Input%20Files/figure.jpg)

Dataset
-------------------------
For the sake of demonstration, we generated a dummy dataset that contains typical EHR variables. 
The dummy dataset is composed of 1000 patient instances. The EHR includes typical demographic, vitals, and lab results along with a variable under the name of "Hospital death" which reports the final clinical outcome of the patients hospital stay.
 

Exploratory Data Analysis
-------------------------
Prior to apply any machine learning models, it is essential to understand the characteristics of the data at hand. Exploratory Data Analysis (EDA) is an initial investigation of the data with the aim to discover patterns, to detect anomalies, and better understand the variables and their distribution.

<<<<<<< HEAD
In this folder, we present a notebook showing an investigation of the dummy dataset that will be used throughout the repository. The notebook introduces some functions used to visualize the data as well as some libraries that accelerate the data analysis . The folder also includes a profiling report "report.html" that highlights the main quantile and descriptive statistical attributes, correlations, missing values and outliers present in the dataset. 
=======
In this folder, we present a notebook showing an investigation of the dummy dataset that will be used throughout the repository. The notebook introduces some functions used to visualize the data as well as some libraries that accelarate the data analysis . The folder also includes a profiling report "report.html" that highlights the main quantile and descriptive statistical attributes, correlations, missing values and outliers present in the dataset. 
>>>>>>> b3832fb699552051745de0c0c1275cf5f7d411af

Data preprocessing
----------------
This script includes functions that can be used preprocess Electronic Health records that is stored in "csv" file format. The file includes a set of functions that handle typical issues in EHR such as missing values, implausible and invalid values, and categorical encoding. The script also includes multiple functions that demonstrate examples of feature engineering that are specifically useful in clinical data analysis.

After calling the functions, the resulting datasets are stored in a pkl file under the name
"prepared.pkl".

In the script, all the functions have details on the purpose and usage of each of them.


Model
-----
After preprocessing, datasets are usually split into training and testing sets The training set is used to train the machine learning models, while the testing set is used to test and validate the predictions of the machine learning models. In this project we present a sample notebook that introduces commonly used libraries for building machine learning models applied to the dummy dataset with a with 8:2 split ratio for the training and testing sets.

The models included in the sample notebook are Logistic Regression, Multi-layer Perceptron Regressor, Support Vector Machine, Gradient Boosting Regressor, and  Ridge Regressor. 

Plausible Data Dictionary
-------------------------
An important aspect of clinical data preprocessing is making sure that the data used to train the machine learning model is clinically valid and free of implausible values. 
 
  * "Plausible_EHR.csv" is a plausible data dictionary compiled based on ANZICS core- Adult Patient Database for ICU patients.

This dictionary  includes 28 numerical clinical features such as labs, vitals, and labs blood gas. This is a helpful tool that can be used to detect and impute implausible and invalid entries. 

* Note: Please make sure that the unit of measure in the "Unit of measure" column matches the one used in your dataset to ensure proper implausible  values detection.

Citation
=========
For this work, please cite: [![DOI](https://zenodo.org/badge/272145962.svg)](https://zenodo.org/badge/latestdoi/272145962)






