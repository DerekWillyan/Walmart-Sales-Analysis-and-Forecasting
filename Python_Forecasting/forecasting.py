import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet

# Carregar os dados
df = pd.read_csv('/home/derekwillyan/Documentos/dataset/Walmart dataset/archive/Walmart_Sales.csv')

# Converter a coluna 'Date' para datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filtrar os dados para uma loja específica (ex: loja 1)
store_sales = df[df['Store'] == 1]

# Agregar as vendas por semana
weekly_sales = store_sales.resample('W', on='Date').sum()

# Plotar as vendas semanais
plt.figure(figsize=(10, 6))
plt.plot(weekly_sales.index, weekly_sales['Weekly_Sales'])
plt.title('Vendas Semanais - Loja 1')
plt.xlabel('Data')
plt.ylabel('Vendas Semanais')
plt.show()

### Previsão com ARIMA ###

# Dividir os dados em treino e teste
train = weekly_sales.iloc[:-12]  # Dados até 12 semanas antes
test = weekly_sales.iloc[-12:]   # Últimas 12 semanas para teste

# Ajustar o modelo ARIMA
model_arima = ARIMA(train['Weekly_Sales'], order=(5, 1, 0))
model_arima_fit = model_arima.fit()

# Fazer previsões
forecast_arima = model_arima_fit.forecast(steps=12)
test['ARIMA_Predictions'] = forecast_arima

# Plotar as previsões
plt.figure(figsize=(10, 6))
plt.plot(train.index, train['Weekly_Sales'], label='Treinamento')
plt.plot(test.index, test['Weekly_Sales'], label='Dados Reais')
plt.plot(test.index, test['ARIMA_Predictions'], label='Previsões ARIMA', linestyle='--')
plt.title('Previsão de Vendas - ARIMA')
plt.xlabel('Data')
plt.ylabel('Vendas Semanais')
plt.legend()
plt.show()

### Previsão com Prophet ###

# Preparar os dados para o Prophet
prophet_data = weekly_sales.reset_index()[['Date', 'Weekly_Sales']]
prophet_data.columns = ['ds', 'y']

# Criar e ajustar o modelo Prophet
model_prophet = Prophet(yearly_seasonality=True, weekly_seasonality=True)
model_prophet.fit(prophet_data)

# Fazer previsões para as próximas 12 semanas
future_dates = model_prophet.make_future_dataframe(periods=12, freq='W')
forecast_prophet = model_prophet.predict(future_dates)

# Plotar as previsões do Prophet
model_prophet.plot(forecast_prophet)
plt.title('Previsão de Vendas - Prophet')
plt.xlabel('Data')
plt.ylabel('Vendas Semanais')
plt.show()

# Plotar os componentes (tendência, sazonalidade) do modelo Prophet
model_prophet.plot_components(forecast_prophet)
plt.show()
