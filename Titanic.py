import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_df = pd.read_csv(url)

fig, axes = plt.subplots(2,2)

sns.countplot(data=titanic_df, x='Survived', ax=axes[0,0])
axes[0,0].set_title('Survival Count')

sns.barplot(data=titanic_df, x='Sex', y='Survived', ax=axes[0,1])
axes[0,1].set_title('Survival Rate by sex')

sns.histplot(data=titanic_df, x='Age', bins=50, kde=True, ax=axes[1,0])
axes[1,0].set_title('Age Distribution')

sns.barplot(data=titanic_df, x='Pclass', y='Survived', hue='Sex', ax=axes[1,1])
axes[1,1].set_title('Survival Rate by Class and Sex')

plt.figure(figsize=(12, 10))
corr = titanic_df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

plt.tight_layout()
plt.show()