import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

curr_anm = pd.read_csv('data/data/current_anomaly.csv')
curr_nm = pd.read_csv('data/data/current_normal.csv')
vib_anm = pd.read_csv('data/data/vibration_anomaly.csv')
vib_nm = pd.read_csv('data/data/vibration_normal.csv')

print(f"전류 데이터 크기: {curr_anm.shape}, {curr_nm.shape}")
print(f"진동 데이터 크기: {vib_anm.shape}, {vib_nm.shape}")
print(curr_anm.info())
print(curr_nm.info())
print(vib_anm.info())
print(vib_nm.info())

# sns.set(style='whitegrid')

# fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# sns.boxplot(data=curr_anm.head(100), ax=axes[0, 0])
# axes[0,0].set_title('Current Anomaly')
# sns.boxplot(data=curr_nm.head(100), ax=axes[0, 1])
# axes[0,1].set_title('Current Normal')

# sns.boxplot(data=vib_anm.head(100), ax=axes[1, 0])
# axes[1,0].set_title('Vibration Anomaly')
# sns.boxplot(data=vib_nm.head(100), ax=axes[1, 1])
# axes[1,1].set_title('Vibration Normal')

# plt.tight_layout()
# plt.savefig('combined_boxplot_analysis.png')
# plt.show()


