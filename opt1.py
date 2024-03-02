import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Naming Columns 
column_names=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
data= pd.read_csv('housing.csv',header=None, delimiter=r'\s+', names=column_names)

# Compute the correlation matrix
correlation_matrix = data.corr()

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Histogram of housing prices (MEDV)
plt.figure(figsize=(8, 6))
sns.histplot(data['MEDV'], kde=True, bins=30, color='blue')
plt.title("Distribution of House Prices (MEDV)")
plt.xlabel("Median Value (in $1000s)")
plt.ylabel("Frequency")
plt.show()

# Relationship between rooms (RM) and house prices (MEDV)
plt.figure(figsize=(8, 6))
plt.scatter(data['RM'], data['MEDV'], alpha=0.5, color='green')
plt.title("Relationship Between Average Number of Rooms (RM) and House Prices (MEDV)")
plt.xlabel("Average Number of Rooms")
plt.ylabel("Median Value (in $1000s)")
plt.show()

# Impact of pupil-teacher ratio (PTRATIO) on house prices (MEDV)
# Group data by PTRATIO and calculate the median MEDV for each group
ptratio_median = data.groupby('PTRATIO')['MEDV'].median().reset_index()

# Create a bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='PTRATIO', y='MEDV', data=ptratio_median, palette="viridis")
plt.title("Impact of Pupil-Teacher Ratio (PTRATIO) on House Prices (MEDV)")
plt.xlabel("Pupil-Teacher Ratio")
plt.ylabel("Median Value (in $1000s)")
plt.xticks(rotation=90)
plt.show()

