# MLOps Pipeline Project

Este proyecto implementa un pipeline de MLOps en AWS que incluye las siguientes etapas:

1. Preprocesamiento de datos.
2. Entrenamiento de modelo.
3. Despliegue del modelo.
4. Monitoreo del modelo.

## requerimientos

python 3.0 o superior

## local

### crea un entorno virtual

```bash
   python -m venv env
```

### activa el entorno virtual

```bash
   .\env\Scripts\activate
```

### instala las dependencias

```bash
   pip install -r requirements.txt
```

### inicia el pepeline

```bash
   py run_pipeline.py
```

## Instrucciones para producion en aws

1. Configura las credenciales de AWS.
2. Ejecuta `src/preprocess.py` para preprocesar los datos.
3. Ejecuta `src/train.py` para entrenar el modelo.
4. Usa `deployment/deploy_model.py` para desplegar el modelo en SageMaker.
5. Configura métricas de monitoreo con `monitoring/cloudwatch_metrics.py`.

Consulta los scripts en cada carpeta para más detalles.
