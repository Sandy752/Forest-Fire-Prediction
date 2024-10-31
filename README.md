![GitHub repo size](https://img.shields.io/github/repo-size/Sandy752/Forest-Fire-Prediction?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/Sandy752/Forest-Fire-Prediction?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/Sandy752/Forest-Fire-Prediction?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/Sandy752/Forest-Fire-Prediction?color=red&style=for-the-badge)


# Algerian forest fires project

Website -(http://forest-fire-prediction-env.eba-hb3a34jp.ap-south-1.elasticbeanstalk.com/predict)
## Table of contents
* [Dataset Preview](#dataset-preview)
* [Demo](#demo)   
* [Tools Used](#3)
* [Libraries](#4)
* [Algorithms Used](#5)
* [Model Performance Summary](#model-performance-summary)
* [Installation](#installation)


## Dataset Preview

A preview of top five rows.


| day | month | year | Temperature | RH | Ws | Rain | FFMC | DMC | DC  | ISI | BUI | FWI | Classes  | Region |
|-----|-------|------|-------------|----|----|------|------|-----|-----|-----|-----|-----|----------|--------|
| 1   | 6     | 2012 | 29          | 57 | 18 | 0.0  | 65.7 | 3.4 | 7.6 | 1.3 | 3.4 | 0.5 | not fire | 0      |
| 2   | 6     | 2012 | 29          | 61 | 13 | 1.3  | 64.4 | 4.1 | 7.6 | 1.0 | 3.9 | 0.4 | not fire | 0      |
| 3   | 6     | 2012 | 26          | 82 | 22 | 13.1 | 47.1 | 2.5 | 7.1 | 0.3 | 2.7 | 0.1 | not fire | 0      |
| 4   | 6     | 2012 | 25          | 89 | 13 | 2.5  | 28.6 | 1.3 | 6.9 | 0.0 | 1.7 | 0.0 | not fire | 0      |
| 5   | 6     | 2012 | 27          | 77 | 16 | 0.0  | 64.8 | 3.0 | 14.2| 1.2 | 3.9 | 0.5 | not fire | 0      |



<h3>Tools Used </h3><a id="3"></a>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

<h3>Libraries</h3><a id="4"></a>

![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-FF7F0E?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-30B5E3?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![AWS Elastic Beanstalk](https://img.shields.io/badge/AWS%20Elastic%20Beanstalk-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![AWS Pipeline](https://img.shields.io/badge/AWS%20Pipeline-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)


<h3>Algorithms Used<h3><a id="5"></a>

1. Linear Regression
2. Lasso
3. LogisticRegression

## Model Performance Summary

| Model Name            | R² Score |
|-----------------------|----------|
| Linear Regression      | 0.9847   |
| Lasso                  | 0.9492   |
| Logistic Regression    | 0.9836   |

**Summary:**  
The Logistic Regression model demonstrates a strong performance with an R² score of 0.9836, indicating its effectiveness in capturing the variance in the target variable, similar to the linear regression model.

## Installation

* Clone this repository and unzip it.

* create new  venv with python 3 and activate it .

* Install the required packages using

 ``` bash
pip install -r requirements.txt
```

* Execute the command:
``` bash
  python3 app.py
```

* Open ```http://127.0.0.1:5000/``` in your browser.