import random
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

ua = []
ui = []
ba = []
bi = []

## generate data for PCA, make sure all numbers in each array are unique
# for i in range(5):
#     ua.append(round(random.uniform(0.001, 0.025), 3))
#     ui.append(round(random.uniform(0.001, 0.025), 3))
#     ba.append(round(random.uniform(0.001, 0.025), 3))
#     bi.append(round(random.uniform(0.001, 0.025), 3))
#
# print(ua)
# print(ui)
# print(ba)
# print(bi)

ua = [0.016, 0.014, 0.001, 0.004, 0.012]
ui = [0.02, 0.016, 0.012, 0.017, 0.013]
ba = [0.018, 0.005, 0.014, 0.016, 0.019]
bi = [0.006, 0.014, 0.003, 0.011, 0.001]

combos = []
for i in ua:
    for j in ui:
        for k in ba:
            for l in bi:
                combos.append([i, j, k, l])
uac = []
uic = []
bac = []
bic = []

for m in combos:
    uac.append(m[0])
    uic.append(m[1])
    bac.append(m[2])
    bic.append(m[3])

num_spots = []
for n in combos:
    num_spots.append(random.uniform(10,100))  # number of spots defined by combination of weighted values


spot_type = []

for o in num_spots:
    if o < 60:
        spot_type.append("Disperse_Spots")
    else:
        spot_type.append("Dense_Spots")

col = []
for q in spot_type:
    if q == "Disperse_Spots":
        col.append("Blue")
    else:
        col.append("Red")

# for PCA, need ua,ui,ba,bi as data and spot_type as labels

data = pd.DataFrame(index=spot_type)

names = ["ua", "ui", "ba", "bi"]
categories = [uac, uic, bac, bic]

for p in range(len(categories)):
    data[names[p]] = categories[p]
print(num_spots)
print(spot_type)
print(data)
quit()

scaled_data = preprocessing.scale(data)

# print(scaled_data)

pca = PCA()

pca.fit(scaled_data)
pca_data = pca.transform(scaled_data)

# Scree Plot
per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
labels = ['PC' + str(x) for x in range(1, len(per_var) + 1)]

plt.bar(x=range(1, len(per_var) + 1), height=per_var, tick_label=labels)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Component')
plt.title('Scree Plot')
plt.show()

# the following code makes a fancy looking plot using PC1 and PC2
pca_df = pd.DataFrame(pca_data, index= spot_type, columns = labels)
print(pca_df)
plt.scatter(pca_df.PC1, pca_df.PC2,c = col)
plt.title('My PCA Graph')
plt.xlabel('PC1 - {0}%'.format(per_var[0]))
plt.ylabel('PC2 - {0}%'.format(per_var[1]))

plt.show()

for sample in pca_df.index:
    plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))

# plt.show()

## get the name of the top 10 measurements (genes) that contribute
## most to pc1.
## first, get the loading scores
loading_scores = pd.Series(pca.components_[1], index=names)
## now sort the loading scores based on their magnitude
sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)

# get the names of the top 10 genes
top_n = sorted_loading_scores[0:4].index.values

## print the gene names and their scores (and +/- sign)
print(loading_scores[top_n])
