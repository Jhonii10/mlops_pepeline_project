import argparse
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model(train_data_path, model_output_path):
    # Cargar datos
    X_train = pd.read_csv(f"{train_data_path}/X_train.csv")
    y_train = pd.read_csv(f"{train_data_path}/y_train.csv")

    # Entrenar modelo
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train.values.ravel())

    # Guardar modelo entrenado
    joblib.dump(model, f"{model_output_path}/model.joblib")
    print("Modelo entrenado y guardado en:", model_output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_data", required=True, help="Ruta a los datos de entrenamiento")
    parser.add_argument("--output", required=True, help="Ruta para guardar el modelo entrenado")
    args = parser.parse_args()
    train_model(args.train_data, args.output)
