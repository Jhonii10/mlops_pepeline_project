import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(input_path, output_path):
    # Cargar datos
    data = pd.read_csv(input_path)

    # Identificar columnas categóricas y realizar encoding
    categorical_columns = data.select_dtypes(include=["object"]).columns
    data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

    # Dividir en características (X) y etiquetas (y)
    X = data.drop("label", axis=1)
    y = data["label"]

    # División en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Guardar datos procesados
    X_train.to_csv(f"{output_path}/X_train.csv", index=False)
    y_train.to_csv(f"{output_path}/y_train.csv", index=False)
    X_test.to_csv(f"{output_path}/X_test.csv", index=False)
    y_test.to_csv(f"{output_path}/y_test.csv", index=False)
    print(f"Datos preprocesados y guardados en: {output_path}")

if __name__ == "__main__":
    preprocess_data("data/dataset.csv", "preprocessed_data")
