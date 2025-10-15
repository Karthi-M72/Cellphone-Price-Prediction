# 📱 Cell Phone Price Prediction – A Machine Learning Approach

**Dataset Credit:** Mobile Price Classification Dataset (Kaggle)


## 🎯 Objective

To predict the **price range of cell phones** based on their technical specifications.
This project applies **Machine Learning models** to help manufacturers, retailers, and consumers make data-driven decisions on pricing strategies and product positioning.


## 🔑 Key Insights from the Analysis

* Features like **RAM, battery power, and pixel resolution** were the most influential in predicting price ranges.
* Devices with **higher RAM and battery capacity** consistently mapped to premium categories.
* **Number of cores, processor speed, and internal memory** also contributed significantly to price prediction.
* Screen size, talk time, and camera resolution were important secondary features.


## ✅ Recommended Actions

* **Manufacturers**: Focus on optimizing **RAM, battery life, and internal memory** for budget-friendly models to increase competitiveness.
* **Retailers**: Use predictive insights to classify products more accurately and suggest alternatives to customers based on specs.
* **Consumers**: Compare devices with similar RAM, battery, and processor specifications when evaluating price vs. performance.


## 🛠️ What I Worked On

* Started with a **structured dataset** (~2,000 rows × 21 features).
* Performed **data preprocessing**:
  * Normalized numerical features.
* Conducted **exploratory data analysis (EDA)** to identify the most impactful specifications.
* Built and compared multiple ML models:

  * Logistic Regression
  * Decision Tree
  * Random Forest
  * Support Vector Machine (SVM)
  * XGBoost
  * Gradient Boosting
* Evaluated models using **Accuracy** on the test set.


## 📊 Model Performance

**Best Performing Model:** Logistic Regression
**Accuracy (Test Set):** ~94.75%

Other models for comparison:

* Support Vector Machine (SVM): ~89.25%
* Decision Tree: ~84.25%
* Random Forest: ~89.75%
* Gradient Boosting: ~90.00%
* XGBoost: ~92.00%

**Logistic Regression provided the most balanced and reliable performance.**


## 🌟 Impact

* Strengthened skills in **EDA, feature analysis, and model evaluation**.
* Showcased how **machine learning can assist pricing strategy** in the consumer electronics market.
* Developed a working **interactive Streamlit app** that predicts price ranges and suggests phones matching user specifications.
