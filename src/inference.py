import joblib
import pandas as pd

def predict(model_path, input_data_path):
    # Cargar modelo
    model = joblib.load(model_path)

    # Cargar datos de entrada
    data = pd.read_csv(input_data_path)

    # Realizar predicciones
    predictions = model.predict(data)
    print("Predicciones:", predictions)
    return predictions

if __name__ == "__main__":
    predict("deployment/model.joblib", "preprocessed_data/X_test.csv")
