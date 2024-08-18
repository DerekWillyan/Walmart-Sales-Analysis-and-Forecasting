# Python Forecasting and Clustering

Esta pasta contém os scripts de previsão de vendas e segmentação de lojas utilizando técnicas de Machine Learning. As análises incluem a previsão de séries temporais com Prophet e a clusterização de lojas com K-means.

## 📂 Arquivos

```
Python_Forecasting/
├── forecasting.py
├── clustering.py
├── requirements.txt
└── README.md
```

### 1. **forecasting.py**
Este script realiza a previsão de vendas semanais usando o modelo Prophet. Ele utiliza os dados históricos de vendas para prever tendências futuras e permite ajustes sazonais.

#### Principais funcionalidades:
- Treinamento do modelo Prophet com dados de vendas históricos.
- Previsão de vendas futuras para semanas específicas.
- Visualização da série temporal com gráficos.

### 2. **clustering.py**
Este script executa a clusterização das lojas usando o algoritmo K-means. A segmentação é feita com base em características como vendas médias, temperatura e preço de combustível.

#### Principais funcionalidades:
- Pré-processamento dos dados e padronização.
- Aplicação do algoritmo K-means para agrupar lojas com características similares.
- Visualização dos clusters gerados com gráficos.

## 🚀 Como Executar

1. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o script de previsão:
   ```bash
   python forecasting.py
   ```

3. Execute o script de clusterização:
   ```bash
   python clustering.py
   ```

## 🛠️ Dependências

As dependências estão listadas no arquivo `requirements.txt`:

```
pandas==2.0.3
numpy==2.0.0
matplotlib==3.7.2
scikit-learn==1.3.0
prophet==1.1.4
seaborn==0.12.2
```

Certifique-se de que todas as bibliotecas estão instaladas corretamente antes de executar os scripts.

## 📊 Visualizações

Os gráficos gerados pelos scripts são salvos automaticamente como arquivos PNG na pasta raiz do projeto. Você também pode visualizar as saídas diretamente ao rodar os scripts em um ambiente como Jupyter Notebook.

## 📈 Modelos e Técnicas Utilizadas

- **Prophet**: Um modelo de série temporal desenvolvido pelo Facebook, ideal para prever vendas sazonais e capturar tendências de longo prazo.
- **K-means**: Um algoritmo de clusterização que agrupa lojas com base em suas características, permitindo segmentações como alto desempenho, desempenho médio e baixo desempenho.

---

Este README fornece uma visão clara e detalhada das funcionalidades e como usar os scripts. Caso precise de mais informações ou tenha outras dúvidas, estou à disposição!
