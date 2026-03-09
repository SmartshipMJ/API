import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips = sns.load_dataset('tips')

sns.set(style='whitegrid')
ax = sns.boxplot(x='day', y='total_bill', hue='smoker', data=tips)

plt.savefig('boxplot.png')
plt.savefig('boxplot.pdf')