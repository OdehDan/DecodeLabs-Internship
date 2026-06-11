💧 Water Quality Potability Prediction

A machine learning project that predicts whether water is safe for human consumption based on physicochemical properties. Built with public health in mind — the goal is to minimize unsafe water being classified as safe.


📌 Problem Statement

Globally, 2 billion people live without access to safe drinking water. Contaminated water causes cholera, typhoid, dysentery, and countless other diseases. This project builds a binary classification model to predict water potability (safe = 1, unsafe = 0) using measurable water quality parameters, helping automate safety assessments based on WHO standards.


📂 Dataset


Source: Kaggle — Water Potability Dataset by Aditya Kadiwal
Size: 3,276 rows × 10 columns
Target: Potability (1 = Safe, 0 = Not Safe)
Class distribution: ~61% Not Potable / ~39% Potable (imbalanced)


Features

FeatureDescriptionphpH level of waterHardnessCalcium and magnesium salt concentrationSolidsTotal dissolved solids (TDS)ChloraminesAmount of chloramines (disinfectant)SulfateSulfate concentrationConductivityElectrical conductivityOrganic_carbonTotal organic carbonTrihalomethanesTHM concentration (disinfection byproduct)TurbidityCloudiness of water


⚙️ Methodology

1. Exploratory Data Analysis


Examined data types (all continuous — no encoding needed)
Identified class imbalance: 60.9% non-potable vs 39.1% potable


2. Data Cleaning


Handled missing values in ph, Sulfate, and Trihalomethanes:

ph → filled with mean (normally distributed)
Sulfate → filled with median (skewed distribution)
Trihalomethanes → filled with mean (normally distributed)



Confirmed zero duplicate rows


3. Feature Engineering

Three domain-informed features were created:

FeatureFormula / LogicRationaleph_quality1 if pH in [6.5, 8.5] else 0Encodes WHO safe drinking water pH rangedisinfection_byproduct_riskOrganic_carbon × ChloraminesHigh values → more THM formationmineral_composition_qualityHardness / (Solids + 1)High solids with low hardness signals contamination

4. Modeling


Train/test split: 80/20, stratified
Scaling: StandardScaler applied to both splits
Class imbalance: Handled via class_weight="balanced" in both models
Evaluation: 5-fold cross-validation (F1 score), then test set evaluation


Models Trained


Logistic Regression (max_iter=1000, class_weight="balanced")
Random Forest (n_estimators=100, max_depth=10, class_weight="balanced")



📊 Evaluation Metrics

Models were evaluated on accuracy, precision, recall, F1-score (per class), and ROC-AUC.


Priority metric: Recall for Class 0 (Non-Potable)
Misclassifying unsafe water as safe is the highest-risk error — it leads directly to disease exposure. Recall for the non-potable class is therefore the primary optimization target.




✅ Final Model: Random Forest

Random Forest was selected as the final model because it achieved better recall and F1-score on the non-potable class, making it more appropriate for this safety-critical task.


🛠️ Tech Stack


Python 3
pandas, numpy — data manipulation
matplotlib, seaborn — visualization
scikit-learn — modeling and evaluation
kagglehub — dataset download



🚀 How to Run


Clone this repository
Install dependencies:


bash   pip install pandas numpy matplotlib seaborn scikit-learn kagglehub


Open Water_Quality_Potability.ipynb in Jupyter or Google Colab
Run all cells from top to bottom



