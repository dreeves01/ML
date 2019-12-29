import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
data = pd.read_csv("PhishingData.csv")
pearsoncorr = data.corr(method='pearson')

sb.heatmap(pearsoncorr, 
            xticklabels=pearsoncorr.columns,
            yticklabels=pearsoncorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5)

plt.show()