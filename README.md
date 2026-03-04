# Mnist Web

Aplicación web interactiva que permite configurar, entrenar y evaluar una red neuronal densamente conectada para la clasificación de dígitos manuscritos (MNIST), bajo una arquitectura desacoplada frontend-backend orientada a experimentación en Machine Learning.

---

## Proyecto Completo

Este repositorio corresponde únicamente al `backend` del sistema.

Aquí se implementa la API REST desarrollada con Django REST Framework, encargada de gestionar el entrenamiento, evaluación e inferencia de una red neuronal densa construida con Keras para la clasificación de dígitos manuscritos (MNIST).

Video demostración: [Mnist Web - Video](https://www.youtube.com/watch?v=nCE3aq7qerM)  
Repositorio Backend: [Mnist Web - Backend](https://github.com/shaitansix/Mnist_Web-Backend)  
Repositorio Frontend: [Mnist Web - Frontend](https://github.com/shaitansix/Mnist_Web-Frontend)  

---

## Arquitectura del Sistema

Descripción general de la arquitectura del proyecto:

- **Frontend:** React + Vite
- **Backend:** Django REST Framework
- **Modelo de ML:** Red neuronal densa implementada con Keras
- **Dataset:** MNIST
- **DevOps / Herramientas:** Docker, Git, GitHub 

### Descripción adicional

El sistema sigue una arquitectura cliente-servidor donde el frontend permite configurar dinámicamente la arquitectura y los hiperparámetros del modelo antes de enviar la solicitud de entrenamiento al backend mediante HTTP.

Una vez entrenado el modelo, el usuario puede evaluar su desempeño utilizando imágenes del conjunto de prueba o dibujando manualmente un dígito en la interfaz para que el modelo lo clasifique en tiempo real.

El frontend gestiona el estado de configuración, resultados de entrenamiento e inferencia, renderizando dinámicamente métricas como accuracy y predicciones generadas por el modelo.

---

## Funcionalidades Principales

- Exposición de endpoints REST para configuración dinámica de arquitectura neuronal (1 o 2 capas ocultas, 1 a 10 neuronas por capa).
- Recepción y validación de hiperparámetros: épocas, batch size, función de activación y tasa de aprendizaje.
- División configurable del dataset en conjuntos de entrenamiento y prueba.
- Entrenamiento del modelo bajo demanda mediante solicitudes HTTP.
- Evaluación automática del modelo y cálculo de métricas (accuracy).
- Implementación de inferencia sobre imágenes del conjunto de test.
- Procesamiento y clasificación de imágenes dibujadas por el usuario.
- Retorno estructurado de resultados en formato JSON.

---

## Aspectos Técnicos Destacados

- Implementación de red neuronal densa con Keras/TensorFlow integrada en API REST.
- Pipeline completo de entrenamiento: carga de dataset → preprocesamiento → entrenamiento → evaluación.
- Normalización y transformación de datos de entrada para inferencia consistente.
- Configuración dinámica del modelo sin necesidad de modificar el código fuente.
- Separación clara entre lógica de ML y capa de exposición API.
- Manejo estructurado de solicitudes HTTP y serialización de respuestas.
- Arquitectura modular que permite extender el modelo a configuraciones más complejas.
- Tiempo de entrenamiento inferior a 1 minuto bajo configuraciones estándar, con accuracy superior a 0.9 en la mayoría de los casos.

---

<!--
## Opciones de Despliegue

### Usando Docker

#### 1. Descargar la imagen
```bash
docker pull shaitansix/mnist_web-api:1
```

#### 2. Crear y ejecutar el contenedor
```bash
docker run --name mnist_web-api -e SECRET_KEY="hhha2%kgyg_!f7(^h4@l^%wwc@7z^%^^ql7rt&d_aea)n3+3-j" -e CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:4173,http://127.0.0.1:4173 -e ALLOWED_HOSTS=localhost,127.0.0.1 -p 8000:8000 shaitansix/mnist_web-api:1
```

#### 3. Crear superusuario
```bash
docker exec -it mnist_web-api python manage.py createsuperuser
```

#### 4. Acceder a la aplicación
```bash
http://localhost:8000/admin/
```

### Usando git clone

#### 1. Crear carpeta de trabajo

#### 2. Clonar repositorio
```bash
git clone https://github.com/shaitansix/Mnist_Web-Backend.git
cd Mnist_Web-Backend
```

#### 3. Crear y activar entorno virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux / Mac
```

#### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

#### 5. Configurar variables de entorno
Crear un archivo `.env.dev` en la raíz del proyecto:
```bash
SECRET_KEY=hhha2%kgyg_!f7(^h4@l^%wwc@7z^%^^ql7rt&d_aea)n3+3-j
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:4173,http://127.0.0.1:4173
ALLOWED_HOSTS=localhost,127.0.0.1
```

#### 6. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 7. Crear directorio para modelos
Crear la siguiente estructura para almacenar modelos entrenados:
```bash
data/keras_models/
```

#### 8. Crear superusuario (opcional)
Crear la siguiente estructura para almacenar modelos entrenados:
```bash
python manage.py createsuperuser
```

#### 9. Ejecutar servidor
```bash
python manage.py runserver
```

#### 10. Acceder a la aplicación
```bash
http://localhost:8000/admin/
```
-->
