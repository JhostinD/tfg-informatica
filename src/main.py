import main_etl
import main_ia


if __name__ == '__main__':

    '''
    PHASE 1: Data extraction from BigQuery Dataset
    '''

    # Retrieving raw data from Google Cloud Platform dataset (House-canary)
    data_raw = main_etl.extract()

    # Transforming raw data into processed data for database
    data_processed = main_etl.transform(data_raw)


    '''
    PHASE 2: Neural Network training with retrieved data
    '''
    model, X_test_scaled, y_test = main_ia.compile_and_train_model(data_processed)

    # Hacer predicciones sobre el conjunto de prueba
    predictions = model.predict(X_test_scaled)

    # Visualizar las primeras 5 predicciones junto con los valores reales
    for i in range(5):
        print("Predicción:", predictions[i])
        print("Valor real:", y_test.iloc[i].values)
        print()  # Salto de línea para separar las predicciones