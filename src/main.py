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

    # Predict over the test set
    predictions = model.predict(X_test_scaled)

    # Visualize the first 5 predictions along the real values
    for i in range(len(predictions)):
        print("Predicción:", predictions[i])
        print("Valor real:", y_test.iloc[i].values)
        print()  # In order to separate predictions