Customer Segmentation — Unsupervised Learning

Project Overview

This project applies unsupervised machine learning to discover hidden mathematical groupings in unlabelled retail customer data. Using distance-based algorithms, dimensionality reduction, and cluster analysis, the project segments customers into distinct personas to enable targeted business decisions.


Objectives


Apply KMeans clustering to identify natural customer groupings
Use PCA to reduce 20+ features into 2–3 dimensions for clustering and visualization
Validate the optimal number of clusters using the Elbow Method and Silhouette Score
Translate resulting clusters into actionable business personas



Dataset


Source: Customer Personality Analysis — Kaggle
File: marketing_campaign.csv
Shape: 2,240 rows × 29 columns
Domain: Retail / Marketing


Key Features

FeatureDescriptionIncomeAnnual household incomeYear_BirthCustomer birth year (engineered into Age)Dt_CustomerEnrollment date (engineered into Customer_Tenure)MntWines, MntFruits, etc.Spending per product categoryNumWebPurchases, NumStorePurchases, etc.Purchase channel countsAcceptedCmp1–5, ResponseMarketing campaign responsesEducationEducation level (ordinal encoded)Marital_StatusMarital status (one-hot encoded, later dropped for clustering)


Project Pipeline

1. Data Collection


Downloaded via kagglehub and loaded with pandas using tab separator (sep='\t')


2. Data Preprocessing


Dropped irrelevant columns: ID, Z_CostContact, Z_Revenue
Handled missing values: Income filled with median
Converted Dt_Customer to datetime


3. Feature Engineering


Age = 2024 − Year_Birth
Customer_Tenure = days since enrollment date


4. Encoding


Education → OrdinalEncoder (Basic < 2n Cycle < Graduation < Master < PhD)
Marital_Status → One-Hot Encoding (dropped before clustering to avoid marital-status-dominated segments)


5. Scaling


Applied StandardScaler to normalize all features before PCA


6. Dimensionality Reduction (PCA)


Reduced 20+ columns to 3 principal components
Clustering and visualization performed on PCA output


7. Optimal K Selection


Elbow Method — plotted inertia vs K to find the point of diminishing returns
Silhouette Score — computed for K=2 to K=10
Final K selected: 4 — balances mathematical validity with business interpretability


8. KMeans Clustering


Fitted KMeans with K=4 on PCA-reduced data
Cluster labels assigned back to original dataframe


9. Visualization


2D scatter plot of customer segments using PCA components 1 and 2



Customer Personas

ClusterPersonaKey Characteristics0Comfortable SpendersHigh income, high spending, few children, low web visits, prefer offline channels1Settled Mid-TierMedium income, moderate spending, teenagers at home, digitally active, oldest group2Budget ConsciousLowest income, lowest spending, most children, youngest group, high web visits but low campaign response3Premium LoyalistsHighest income, highest spending on wine and meat, most campaign-responsive, few children, most valuable segment


Key Skills Demonstrated


Dimensionality Reduction (PCA)
KMeans Clustering
Distance Metrics
Elbow Method & Silhouette Score
Business Intelligence Translation



Libraries Used

numpy, pandas, matplotlib, seaborn, scikit-learn, kagglehub


How to Run


Open Customer_Segmentation.ipynb in Google Colab
Run all cells sequentially
Dataset downloads automatically via kagglehub



