import tensorflow as tf
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Prepares features and labels, defines model properties and compiles the model
def compile_and_train_model(data_processed: DataFrame):
    # Dividing data in features (X) and labels (y)
    X = data_processed.drop(['hpi_value', 'hpi_real'], axis=1)
    y = data_processed[['hpi_value', 'hpi_real']]

    # Dividing data in training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scaling features in order to increase model performance
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Defining neural network architecture
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(2)  # 2 output neurons to predict hpi_value y hpi_real
    ])

    # Compiling model
    model.compile(optimizer='adam', loss='mse')

    # Train model
    model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_data=(X_test_scaled, y_test))

    return model, X_test_scaled, y_test
