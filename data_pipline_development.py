import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# 1. Create Raw Data (simulating loaded CSV)
data = {
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Eva'],
    'Age': [25, 63, np.nan, 45, 70],
    'City': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore'],
    'Salary': [50000, 60000, 52000, np.nan, 80000]
}

df = pd.DataFrame(data)
print("🔹 Original Data:")
print(df)

# 2. Define Features
numerical_features = ['Age', 'Salary']
categorical_features = ['City']

# 3. Preprocessing Pipelines
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# 4. Full Transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# 5. Apply Transformations
processed_array = preprocessor.fit_transform(df)

# 6. Combine Processed Data
# Get transformed column names
encoded_cat_cols = preprocessor.named_transformers_['cat']['encoder'].get_feature_names_out(categorical_features)
all_columns = numerical_features + list(encoded_cat_cols)
processed_df = pd.DataFrame(processed_array, columns=all_columns)

print("\n Transformed Data:")
print(processed_df)

# 7. Save the processed data
processed_df.to_csv("processed_data.csv", index=False)
print("\n Processed data saved as 'processed_data.csv'")

output:

🔹 Original Data:
    Name   Age       City   Salary
0  Alice  25.0      Delhi  50000.0
1    Bob  63.0     Mumbai  60000.0
2  Carol   NaN    Chennai  52000.0
3  David  45.0    Kolkata      NaN
4    Eva  70.0  Bangalore  80000.0

 Transformed Data:
        Age    Salary  City_Bangalore  City_Chennai  City_Delhi  City_Kolkata  \
0 -1.650675 -0.989510             0.0           0.0         1.0           0.0   
1  0.785273 -0.047120             0.0           0.0         0.0           0.0   
2  0.000000 -0.801032             0.0           1.0         0.0           0.0   
3 -0.368597  0.000000             0.0           0.0         0.0           1.0   
4  1.234000  1.837661             1.0           0.0         0.0           0.0   

   City_Mumbai  
0          0.0  
1          1.0  
2          0.0  
3          0.0  
4          0.0  

 Processed data saved as 'processed_data.csv'

