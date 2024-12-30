import pandas as pd
import numpy as np

def generate_dataset(output_path, n_samples=1000):
    """
    Genera un dataset sintético para pruebas de pipelines MLOps.
    
    Parámetros:
    - output_path: Ruta donde se guardará el archivo CSV.
    - n_samples: Número de muestras a generar.
    """
    np.random.seed(42)  # Para reproducibilidad

    # Generar características sintéticas
    feature_1 = np.random.uniform(0, 100, n_samples)  # Valores continuos entre 0 y 100
    feature_2 = np.random.randint(0, 50, n_samples)   # Valores enteros entre 0 y 50
    feature_3 = np.random.choice([0, 1], n_samples)   # Valores binarios (0 o 1)
    feature_4 = np.random.normal(50, 10, n_samples)   # Valores con distribución normal
    feature_5 = np.random.choice(['A', 'B', 'C'], n_samples)  # Categorías

    # Generar etiquetas (target)
    labels = np.random.choice([0, 1], n_samples)  # Binario: 0 o 1

    # Crear DataFrame
    data = pd.DataFrame({
        "feature_1": feature_1,
        "feature_2": feature_2,
        "feature_3": feature_3,
        "feature_4": feature_4,
        "feature_5": feature_5,
        "label": labels
    })

    # Guardar en archivo CSV
    data.to_csv(output_path, index=False)
    print(f"Dataset sintético generado en: {output_path}")

if __name__ == "__main__":
    generate_dataset("data/dataset.csv")
