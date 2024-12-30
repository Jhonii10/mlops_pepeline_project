import subprocess
import sys

def check_and_install_dependencies():
    """Verifica e instala las dependencias necesarias."""
    required_packages = ["pandas", "joblib", "scikit-learn"]
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"El paquete '{package}' no está instalado. Instalándolo ahora...")
            subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)

def generate_data():
    print("Generando dataset sintético...")
    subprocess.run(["py", "src/generate_dataset.py"], check=True)
    print("Dataset generado.")

def run_preprocess():
    print("Ejecutando preprocesamiento...")
    subprocess.run(["py", "src/preprocess.py"], check=True)
    print("Preprocesamiento completado.")

def run_train():
    print("Entrenando modelo...")
    subprocess.run([
        "py", "src/train.py", 
        "--train_data", "preprocessed_data", 
        "--output", "deployment"
    ], check=True)
    print("Entrenamiento completado.")

def run_deploy():
    print("Desplegando modelo...")
    subprocess.run(["py", "deployment/deploy_model.py"], check=True)
    print("Modelo desplegado exitosamente.")

if __name__ == "__main__":
    try:
        print("Verificando dependencias...")
        check_and_install_dependencies()
        
        generate_data()
        run_preprocess()
        run_train()
        # run_deploy()
        print("Pipeline completado.")
    except subprocess.CalledProcessError as e:
        print(f"Error durante la ejecución: {e}")
