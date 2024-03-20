import tensorflow as tf
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def compile_and_train_model(data_processed: DataFrame):
    # Divide data in features (X) and labels (y)
    X = data_processed.drop(['zip', 'msa'], axis=1)  # Delete 'zip' and 'msa' columns because they are not numerical
    #y = data_processed[['zip', 'msa', 'month', 'hpi_value', 'hpi_real']]   # features don't work when using 'month' column (date type)
    y = data_processed[['zip', 'msa', 'hpi_value', 'hpi_real']]

    # Divide data in test and train sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features in order to increase model performance
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Define neural network architecture
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(5)  # 5 output neurons to predict 5 columns
    ])

    # Compile model
    model.compile(optimizer='adam', loss='mse')

    # Convert all columns to float32 data type
    X_train_scaled = X_train_scaled.astype('float32')
    X_test_scaled = X_test_scaled.astype('float32')
    y_train = y_train.astype('float32')
    y_test = y_test.astype('float32')

    # Train model
    model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_data=(X_test_scaled, y_test))

    return model, X_test_scaled, y_test

'''
import tensorflow as tf
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

def compile_and_train_model(data_processed: DataFrame):
    # Codificación cíclica de la columna 'month'
    data_processed['month_sin'] = np.sin((data_processed['month'] - 1) * (2. * np.pi / 12))
    data_processed['month_cos'] = np.cos((data_processed['month'] - 1) * (2. * np.pi / 12))
    
    # Ahora 'X' incluirá las nuevas columnas 'month_sin' y 'month_cos' en lugar de 'month'
    X = data_processed.drop(['zip', 'msa', 'month'], axis=1)  
    y = data_processed[['zip', 'msa', 'month', 'hpi_value', 'hpi_real']]  # Suponiendo que queremos predecir estos dos campos

    # Divide data in test and train sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features to increase model performance
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Neural network architecture
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(y.shape[1])  # Adjusted to predict the number of columns in 'y'
    ])

    # Compile model
    model.compile(optimizer='adam', loss='mse')

    # Convert all columns to float32 data type
    X_train_scaled = X_train_scaled.astype('float32')
    X_test_scaled = X_test_scaled.astype('float32')
    y_train = y_train.astype('float32')
    y_test = y_test.astype('float32')

    # Train model
    model.fit(X_train_scaled, y_train, epochs=100, batch_size=32, validation_data=(X_test_scaled, y_test))

    return model, X_test_scaled, y_test
'''