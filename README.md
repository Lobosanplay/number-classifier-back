# 🔢 Number Classifier Backend

Backend de FastAPI para clasificación de dígitos manuscritos utilizando Random Forest con dataset MNIST.

## 📋 Descripción

Este proyecto es el backend para un clasificador de dígitos que recibe imágenes de 28x28 píxeles y predice el número dibujado (0-9). Utiliza un modelo de Random Forest entrenado con el dataset MNIST.

## ⚠️ Advertencia sobre Precisión del Modelo

**El modelo actual puede presentar fallos en sus predicciones debido a las siguientes limitaciones:**

### 🎯 Limitaciones Conocidas:

1. **Dataset modificado**: El modelo se entrena con datos MNIST donde todos los valores no-negros (1-254) se reemplazan por 255
2. **Simple preprocesamiento**: Solo realiza rotaciones básicas sin técnicas avanzadas de aumento de datos
3. **Modelo básico**: Random Forest puede no ser óptimo para tareas de visión por computadora
4. **Sensibilidad al dibujo**: La calidad del dibujo del usuario afecta significativamente la precisión

### 📊 Problemas Comunes de Predicción:

- **Dígitos descentrados**: El modelo espera dígitos centrados como en MNIST
- **Trazos muy finos/gruesos**: Difiere del grosor estándar de MNIST
- **Rotaciones inesperadas**: Aunque aplicamos rotación, puede no ser suficiente
- **Valores intermedios**: Convertimos todo a blanco/negro, perdiendo información de grises

## 🚀 Características

- **FastAPI**: Framework web moderno y rápido
- **Random Forest**: Modelo de ensemble con 500 estimadores
- **Preprocesamiento automático**: Rotación y limpieza de imágenes
- **CORS configurado**: Compatible con frontend React
- **Modelo persistente**: Guarda y carga el modelo entrenado
- **Manejo de errores**: Try-catch para operaciones críticas

## 📁 Estructura del Proyecto

```
📦src
 ┣ 📂model
 ┃ ┗ 📜rnd_clf_model.pkl        # Modelo entrenado serializado
 ┣ 📂service
 ┃ ┗ 📜modelNumberClassifier.py # Lógica de entrenamiento del modelo
 ┗ 📜main.py                    # Aplicación FastAPI principal
```

## 🔧 Instalación

### Prerrequisitos
- Python 3.8+
- pip

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/Lobosanplay/number-classifier-back.git
cd number-classifier-back
```

2. **Crear entorno virtual (recomendado)**
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

## 📦 Dependencias Principales

```txt
fastapi>=0.104.0
uvicorn>=0.24.0
scikit-learn>=1.3.0
numpy>=1.24.0
scipy>=1.11.0
joblib>=1.3.0
pydantic>=2.4.0
```

## 🚀 Uso

### Iniciar el servidor

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

El servidor estará disponible en: `http://localhost:8000`

### Endpoints

#### POST `/`
**Descripción**: Recibe una imagen de 28x28 píxeles y devuelve la predicción del dígito.

**Request Body**:
```json
{
  "numbers": [0, 0, 255, 0, ..., 0, 255, 0]   
}
```
784 valores (0-255)

**Response**:
```json
"5"   
```
Dígito predicho como string

**Ejemplo con curl**:
```bash
curl -X POST "http://localhost:8000/" \
     -H "Content-Type: application/json" \
     -d '{"numbers": [/* 784 valores */]}'
```

## 🔍 Flujo de Procesamiento

1. **Recepción**: Recibe array de 784 valores (28x28)
2. **Reshape**: Convierte a matriz 28x28
3. **Flip**: Invierte verticalmente la imagen
4. **Rotate**: Rota -90 grados
5. **Limpiar**: Convierte a array 1D de 784 valores
6. **Predicción**: Clasifica con Random Forest
7. **Respuesta**: Devuelve dígito como string

## 📊 Rendimiento Esperado

- **Random Forest actual**: ~90-95% de precisión en condiciones ideales
- **Con mejoras propuestas**: ~97-99% de precisión
- **Tiempo de inferencia**: < 100ms por predicción

## 🐛 Solución de Problemas

### Error: "Modelo no encontrado"
```bash
# El modelo se creará automáticamente al primer inicio
# Verificar que existe:
ls model/rnd_clf_model.pkl
```

### Error: "ImportError: No module named 'sklearn'"
```bash
pip install scikit-learn
```

### Error: CORS desde frontend
Verificar que el frontend esté en `http://localhost:5173` o actualizar:
```python
allow_origins=["http://localhost:5173"]
```

### Baja precisión en predicciones
1. Verificar que el dibujo esté centrado
2. Usar valores extremos (0 o 255, no intermedios)
3. Dibujar con trazos claros y definidos
4. Probar con dígitos de tamaño similar a MNIST

## 🤝 Integración con Frontend

Este backend está diseñado para funcionar con:
- **Frontend React**: [https://github.com/Lobosanplay/number-classifier-front](https://github.com/Lobosanplay/number-classifier-front)
- **Puerto**: 8000
- **Formato**: JSON array de 784 enteros (0-255)

## 👥 Contribuir

1. Haz fork del proyecto
2. Crea tu rama de feature (`git checkout -b feature/mejora-modelo`)
3. Commit tus cambios (`git commit -m 'Mejora: Añadir CNN'`)
4. Push a la rama (`git push origin feature/mejora-modelo`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## ⚠️ Disclaimer

Este es un proyecto educativo. La precisión del modelo puede variar y no debe usarse en aplicaciones críticas sin mejoras sustanciales.
