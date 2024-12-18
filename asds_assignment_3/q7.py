import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data_path = 'data.txt'

df = pd.read_csv(data_path, sep='\s+')

print(df.columns)

# df.head()
# print(df)

features = ['effp2', 'mincab', 'execdom', 'disprop', 'intgrou', 'federal', 
            'bicam', 'const', 'judrev', 'cenbank'] # we dont want the country feature as that is what we want to classify

X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

pca = PCA()

pca.fit(X_scaled)

explained_variance = pca.explained_variance_ratio_
cummulative_variance = pca.explained_variance_ratio_.cumsum()
principal_components = pca.components_
pca_scores = pca.transform(X_scaled)

print(f"Explained variance ratio: {explained_variance}")
print(f"Cumulative explained variance: {cummulative_variance}")

principal_components_df = pd.DataFrame(principal_components, columns=features)
# print(principal_components_df)

pca_scores_df = pd.DataFrame(pca_scores, columns=[f'PC{i+1}' for i in range(len(explained_variance))], index=df.index)

# looking into country specific results to compare USA vs Finland
pca_scores_df['country'] = df['country']

usa_pca = pca_scores_df[pca_scores_df['country'] == 'USA']
finland_pca = pca_scores_df[pca_scores_df['country'] == 'Finland']

print("USA PCA Scores:\n", usa_pca)
print("Finland PCA Scores:\n", finland_pca)

plt.figure(figsize=(8, 6))
plt.scatter(pca_scores_df['PC1'], pca_scores_df['PC2'])

plt.scatter(usa_pca['PC1'], usa_pca['PC2'], color='red', label='USA')
plt.scatter(finland_pca['PC1'], finland_pca['PC2'], color='brown', label='Finland')

plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA of Democratic Countries')
plt.legend()
plt.show() # no longer have to save the plot, fixed by updating a library related to matplotlib (forgot specifically what library)

# display the different principal component weights to better understand what features are actually being displayed
loadings = pca.components_
loadings_df = pd.DataFrame(loadings, columns=df.columns[1:], index=[f"PC{i+1}" for i in range(loadings.shape[0])])
print(loadings_df)