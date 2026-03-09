import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips = sns.load_dataset('tips')

#tips.to_csv('tips.csv', index=False)

#sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
#plt.title('Total Bill vs Tip')
#plt.show()

corr = tips.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title('Total Bill by Day and Sex')
plt.show()

