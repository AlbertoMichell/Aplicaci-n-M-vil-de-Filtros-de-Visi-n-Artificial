# Aplicación Móvil de Filtros de Visión Artificial

Esta es una aplicación móvil desarrollada en Flutter que permite aplicar diversos filtros de procesamiento de imágenes utilizando OpenCV a través de un backend en Python con FastAPI.

## Qué hace esta aplicación

La aplicación permite capturar o seleccionar imágenes y aplicar diferentes tipos de filtros de visión artificial organizados en categorías:

- Filtros Elementales (Puntuales)
- Filtros Espaciales (Convolución)
- Filtros Morfológicos
- Otros Filtros OpenCV

## Arquitectura del Proyecto

El proyecto tiene una arquitectura cliente-servidor:

### Frontend (Flutter)
```
lib/
├── main.dart                           # Punto de entrada
├── models/
│   └── filter_category.dart           # Modelos de datos
├── services/
│   └── image_processing_service.dart  # Comunicación con API
└── screens/
    ├── home_screen.dart                # Pantalla principal
    ├── filter_selection_screen.dart    # Selección de filtros
    └── filter_apply_screen.dart        # Aplicación de filtros
```

### Backend (Python + FastAPI + OpenCV)
```
backend/
├── main.py              # API REST con endpoints
└── requirements.txt     # Dependencias Python
```

## Qué necesitas tener instalado

### Para el Frontend (Flutter)
- Flutter SDK (versión 3.0.0 o superior)
- Android Studio o Xcode (según la plataforma)
- Un dispositivo Android/iOS o emulador

### Para el Backend (Python)
- Python 3.8 o superior
- pip (gestor de paquetes Python)

## Cómo instalar y configurar

### 1. Clonar el repositorio

```bash
git clone https://github.com/AlbertoMichell/Aplicaci-n-M-vil-de-Filtros-de-Visi-n-Artificial.git
cd Aplicaci-n-M-vil-de-Filtros-de-Visi-n-Artificial
```

### 2. Configurar el Backend

```bash
cd backend
pip install -r requirements.txt
```

### 3. Configurar el Frontend

```bash
cd ..
flutter pub get
```

### 4. Configurar la URL del Backend

Edita el archivo `lib/services/image_processing_service.dart` y cambia la URL base:

```dart
static const String baseUrl = 'http://TU_IP:8000';
```

Reemplar `TU_IP` con:
- `localhost` para un emulador Android
- `10.0.2.2` para el emulador de Android Studio
- La IP de la computadora si se usa un dispositivo físico

## Cómo compilar y ejecutar el proyecto

Hay tres formas de usar esta aplicación:

### Opción 1: Ejecutar en modo desarrollo

Primero, inicia el backend:

```bash
cd backend
python main.py
```

El servidor quedará corriendo en `http://0.0.0.0:8000`

Para verificar que funcione visita: `http://localhost:8000/docs`

Luego, en otra terminal, ejecuta la aplicación:

```bash
flutter run
```

Si tienes varios dispositivos conectados:

```bash
flutter devices  # Lista los dispositivos disponibles
flutter run -d <device-id>
```

### Opción 2: Compilar APK de release

Para generar un APK optimizado:

```bash
flutter build apk --release
```

El APK se generará en: `build/app/outputs/flutter-apk/app-release.apk`

Para un APK de depuración:

```bash
flutter build apk --debug
```

### Opción 3: Usar el APK precompilado

Este repositorio incluye un APK ya compilado en:

```
build/app/outputs/flutter-apk/app-release.apk
```

Para instalar en dispositivo Android:

1. Descarga el archivo APK
2. Habilita "Instalar aplicaciones de fuentes desconocidas" en el dispositivo
3. Abre el archivo APK
4. Sigue las instrucciones de instalación




## Filtros implementados

### Filtros Espaciales:
- Desenfoque Gaussiano
- Filtro de Mediana
- Filtro de Enfoque (Sharpen)
- Detección de Bordes (Sobel)
- Detección de Bordes (Laplaciano)

### Filtros Morfológicos:
- Erosión
- Dilatación
- Apertura
- Cierre

### Otros Filtros:
- Canny Edge Detection
- Escala de Grises
- Detección de Contornos
- Ecualización de Histograma

## Funcionalidades de la aplicación

- Captura de foto con cámara
- Selección de imagen de galería
- Manejo de permisos (cámara y almacenamiento)
- Control deslizante (Slider) para ajustar parámetros de filtros
- Vista lado a lado de imagen original y procesada
- Aplicar múltiples filtros en secuencia
- Funcionalidad de "Deshacer" para revertir el último filtro
- Botón de "Reset" para volver a la imagen original
- Indicador de carga mientras se procesa
- Opción para guardar imagen en galería

## Endpoints de la API

- `GET /health` - Verificar estado del servidor
- `POST /filter/brightness_contrast` - Ajustar brillo y contraste
- `POST /filter/gamma` - Corrección gamma
- `POST /filter/negative` - Negativo de imagen
- `POST /filter/quantization` - Cuantización de niveles
- `POST /filter/gaussian_blur` - Desenfoque gaussiano
- `POST /filter/median_blur` - Filtro de mediana
- `POST /filter/sharpen` - Filtro de enfoque
- `POST /filter/sobel` - Detección de bordes Sobel
- `POST /filter/laplacian` - Detección de bordes Laplaciano
- `POST /filter/erosion` - Erosión morfológica
- `POST /filter/dilation` - Dilatación morfológica
- `POST /filter/opening` - Apertura morfológica
- `POST /filter/closing` - Cierre morfológico
- `POST /filter/canny` - Detección de bordes Canny
- `POST /filter/grayscale` - Conversión a escala de grises
- `POST /filter/contours` - Detección de contornos
- `POST /filter/histogram_equalization` - Ecualización de histograma

## Tecnologías usadas

### Frontend
- Flutter/Dart - Framework multiplataforma
- image_picker - Captura y selección de imágenes
- permission_handler - Manejo de permisos
- http - Cliente HTTP para comunicación con API
- image_gallery_saver - Guardar imágenes en galería
- flutter_spinkit - Indicadores de carga animados

### Backend
- Python - Lenguaje de programación
- FastAPI - Framework web para APIs
- OpenCV - Biblioteca de visión artificial
- NumPy - Procesamiento numérico
- Uvicorn - Servidor ASGI

## Problemas comunes y soluciones

### El backend no se puede conectar
- Revisa que el servidor esté corriendo en el puerto 8000
- Revisa que la IP en `image_processing_service.dart` sea correcta
- Revisa firewall y permisos de red

### Problemas con permisos en Android
- Asegúrate de que `AndroidManifest.xml` tiene todos los permisos
- En Android 13+, necesitas permisos adicionales

### Error al guardar imagen
- Revisa los permisos de almacenamiento
- En Android 10+, revisa la configuración de `requestLegacyExternalStorage`

### Error: "SDK location not found"
Configura la variable de entorno `ANDROID_HOME` para que apunte a tu instalación de Android SDK.

### Error al ejecutar `flutter pub get`
Revisa tu conexión a internet y ejecuta:

```bash
flutter clean
flutter pub cache repair
flutter pub get
```

