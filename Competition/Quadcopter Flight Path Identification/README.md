# Quadcopter Flight Path Identification
<img src="https://img.shields.io/badge/Language-Mixed-D5AE22"> <img src="https://img.shields.io/badge/Last Update-19/08/2019-0A7BBC"> <img src="https://img.shields.io/badge/Status-Not Tested-D7624B">

As a quadcopter moves consistently in the space of longitude and latitude, adding a smoothing pipeline helps to predict a proper flight path. Below is a smoothing example for Experiment ID 1 using [07.csv](submissions/Submission%2007_Stack%20KNN_wo_Feature%20Engineering_w_MinMaxScaler.csv).

<p align="center">
    <img src="https://github.com/abyoso-hapsoro/past-works/assets/51505905/d5ebd01a-0098-46bb-b178-41da23df83d7" width="400" alt="Longitude">
    <img src="https://github.com/abyoso-hapsoro/past-works/assets/51505905/a1267b11-f09a-4a62-a312-bc065bec10f4" width="400" alt="Latitude">
</p>

The original predictions are given by the blue points then smoothed into the yellow line giving the Longitude and Latitude paths respectively.

## General Information
- Data available in Kaggle [here](https://www.kaggle.com/competitions/ittodaydsc2019/data)
- Learning Task: Double Objective Regression
- Evaluation Metric: [Mean Haversine Distance](https://github.com/mapado/haversine)

## Our Submissions
Our team submitted a total of 20 submissions. Submission details that I have documented are listed below.

05, 09, and 10.ipynb are using files from [data/old](data/old) while 14.ipynb is using files from [data](data)
| Num | Method | Additional Step | Handler | Submission | Code |
| :-: | ------ | --------------- | :-----: | :--------: | :--: |
|  1  | Orthogonal Matching Pursuit | <p align="center">-</p> | Me | [01.csv](submissions/Submission%2001_OMP_wo_Engineering.csv) | [05.ipynb](Submission%2005.ipynb) |
|  2  | k-Nearest Neighbors Regressor | MinMaxScaler | Me | [02.csv](submissions/Submission%2002_KNN_wo_Engineering_w_MinMaxScaler.csv) | [05.ipynb](Submission%2005.ipynb) |
|  3  | k-Nearest Neighbors Regressor | MinMaxScaler | Me | [03.csv](submissions/Submission%2003_KNN_wo_Engineering_w_MinMaxScaler.csv) | [05.ipynb](Submission%2005.ipynb) |
|  4  | Optimized k-Nearest Neighbors Regressor | MinMaxScaler | Me | [04.csv](submissions/Submission%2004_Optimized%20KNN_wo_Engineering_w_MinMaxScaler.csv) | [05.ipynb](Submission%2005.ipynb) |
|  5  | Optimized k-Nearest Neighbors Regressor | <ul><li>MinMaxScaler</li><li>PCA</li></ul> | Me | [05.csv](submissions/Submission%2005_Optimized%20KNN_w_PCA_w_MinMaxScaler.csv) | [05.ipynb](Submission%2005.ipynb) |
|  6  | Histogram-based Gradient Boosting Regressor | MinMaxScaler | Me | [06.csv](submissions/Submission%2006_Hist%20Grad%20Boost_wo_Feature%20Engineering_w_MinMaxScaler.csv) | [09.ipynb](Submission%2009.ipynb) |
|  7  | Stacking Regressor | MinMaxScaler | Me | [07.csv](submissions/Submission%2007_Stack%20KNN_wo_Feature%20Engineering_w_MinMaxScaler.csv) | [09.ipynb](Submission%2009.ipynb) |
|  8  | Histogram-based Gradient Boosting Regressor | <ul><li>MinMaxScaler</li><li>Stepwise Feature Selection</li></ul> | Me | [08.csv](submissions/Submission%2008_Hist%20Grad%20Boost_w_Feature%20Selection_w_MinMaxScaler.csv) | [09.ipynb](Submission%2009.ipynb) |
|  9  | Histogram-based Gradient Boosting Regressor | <p align="center">-</p> | Me | [09.csv](submissions/Submission%2009_Hist%20Grad%20Boost_wo_Feature%20Engineering_wo_Scaler.csv) | [09.ipynb](Submission%2009.ipynb) |
| 10  | Optimized Voting Regressor | <ul><li>MinMaxScaler</li><li>Lasso Feature Selection</li></ul> | Teammate | - | [10.ipynb](Submission%2010.ipynb) |
| 14  | Histogram-based Gradient Boosting Regressor | <ul><li>Used Previous Submission</li><li>Univariate Cubic Spline Smoothing</li></ul> | Teammate | - | [14.ipynb](Submission%2014.ipynb) |
| 16  | Stacking Regressor | <ul><li>Used Previous Submission</li><li>Univariate Cubic Spline Smoothing</li></ul> | Me | [16.csv](submissions/Submission%2016_Stacking%20with%20Smoothing.csv) | [14.ipynb](Submission%2014.ipynb) |
| Final | Regression Chain | <p align="center">UNDOCUMENTED</p> | Entire Team | [Final.csv](submissions/Final%20Submission_Hist%20Gradient%20Boost%20Regressor%20Chain.csv) | - |

## Competition Details
- Information about the competition can be found [here](https://www.instagram.com/p/By7s5G-g_RR/)
- To qualify for finals, teams are evaluated 45% based on prediction accuracy and 55% based on report
- 7 teams from Top 14 of Qualifiers was taken for Finals
- Our team finished at 10th of 56 participating teams in Qualifiers

![IT Today 2019 Qualifiers Result](https://github.com/abyoso-hapsoro/past-works/assets/51505905/dac6a77a-bfc7-49ac-a64b-edaa3fdeb115)

## Lessons Learned
- Organize and document better
- Delegate more time in analysis and report assembly instead of focusing only on modeling
- Keep better track of method performance especially the best performer, as the model detailed in the report is ambiguous

## Background
- Purpose: Data Science Competition IT Today 2019 Qualifiers, held by [Institut Pertanian Bogor](https://ipb.ac.id/)
- Involvement: Team
    - Role: Team Member, Lead Programmer
    - Team Size: 3
- Tech Stack: Python, scikit-learn

## Notes
- Planned for Improvement: No
- Python Version: 3.6
