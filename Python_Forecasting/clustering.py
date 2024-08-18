import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('WalmartSales.csv')

# Selecionar as colunas relevantes para a clusterização
data = df[['Store', 'Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']]

# Agregar os dados por loja
data_grouped = data.groupby('Store').mean().reset_index()

# Padronizar os dados
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_grouped.drop('Store', axis=1))

# Determinar o número ideal de clusters usando o método Elbow
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)

# Plotar o gráfico do método Elbow
plt.figure(figsize=(8, 5))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Número de Clusters')
plt.ylabel('Inércia')
plt.title('Método Elbow para Seleção do Número de Clusters')
plt.show()

# Treinar o modelo K-means com o número ideal de clusters (exemplo: 3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
data_grouped['Cluster'] = kmeans.fit_predict(data_scaled)

# Visualizar os clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Weekly_Sales', y='Temperature', hue='Cluster', data=data_grouped, palette='viridis')
plt.title('Segmentação de Lojas com K-means')
plt.show()

# Analisar a média das variáveis em cada cluster
cluster_analysis = data_grouped.groupby('Cluster').mean()
print(cluster_analysis)
