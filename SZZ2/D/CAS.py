import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from pmdarima import auto_arima
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Function to load and preprocess data
def load_and_preprocess(data_path):
    souvenir_data = pd.read_csv(data_path)
    souvenir_data['date'] = pd.date_range(start='2000-01-01', periods=len(souvenir_data), freq='M')
    souvenir_data.set_index('date', inplace=True)
    # souvenir_data.drop(['month'], axis=1, inplace=True)
    # Log transformation to stabilize variance
    souvenir_data['sales'] = np.log(souvenir_data['sales'])
    return souvenir_data

# Function to plot time series data
def plot_time_series(data):
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['sales'], marker='o', linestyle='-')
    plt.title('Časový vývoj prodejů suvenýrů')
    plt.xlabel('Datum')
    plt.ylabel('Prodeje')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.hist(data['sales'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Histogram prodejů suvenýrů')
    plt.xlabel('Prodeje')
    plt.ylabel('Frekvence')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 6))
    plt.boxplot(data['sales'], vert=False, flierprops=dict(marker='o', color='red', markersize=10))
    plt.title('Boxplot prodejů suvenýrů')
    plt.xlabel('Prodeje')
    plt.grid(True)
    plt.show()

# Function to decompose the series
def decompose_series(data):
    decomposition = seasonal_decompose(data['sales'], model='multiplicative')
    fig = decomposition.plot()
    fig.set_size_inches(14, 8)
    fig.tight_layout(pad=3.0)
    plt.show()

# Function to model and forecast
def model_and_forecast(data):
    # Split data
    split_point = int(len(data) * 0.8)
    train_data, test_data = data.iloc[:split_point], data.iloc[split_point:]

    # Holt-Winters model
    hw_model = ExponentialSmoothing(train_data['sales'],
                                    seasonal='mul', 
                                    seasonal_periods=12, 
                                    trend='add').fit()
    hw_predictions = hw_model.forecast(len(test_data))
    rmse_hw = np.sqrt(((test_data['sales'] - hw_predictions) ** 2).mean())
    print(f"RMSE for Holt-Winters model: {rmse_hw}")

    # ARIMA model
    auto_arima_model = auto_arima(train_data['sales'], seasonal=True, m=12, stepwise=True,
                                  suppress_warnings=True, D=1, trace=True, error_action='ignore', max_order=None,
                                  out_of_sample_size=10)
    print(auto_arima_model.summary())

    arima_predictions = auto_arima_model.predict(n_periods=len(test_data))

    plt.figure(figsize=(14, 7))
    plt.plot(train_data.index, train_data['sales'], label='Trénovací data')
    plt.plot(test_data.index, test_data['sales'], label='Skutečné prodeje')
    plt.plot(test_data.index, arima_predictions, label='Predikce auto_arima', linestyle='--')
    plt.title('Predikce auto_arima vs Skutečné prodeje')
    plt.xlabel('Datum')
    plt.ylabel('Prodeje')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main execution block
if __name__ == "__main__":
    data_path = 'SZZ2/D/souvenirtimeseries.csv'
    souvenir_data = load_and_preprocess(data_path)
    plot_time_series(souvenir_data)
    decompose_series(souvenir_data)
    model_and_forecast(souvenir_data)