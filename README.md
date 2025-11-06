# Aplicación Móvil de Filtros de Visión Artificial# Aplicacion Movil de Filtros de Vision Artificial



Aplicación móvil Flutter que implementa filtros de procesamiento de imágenes utilizando técnicas de visión artificial.Aplicacion movil desarrollada en Flutter que permite aplicar diversos filtros de procesamiento de imagenes utilizando OpenCV a traves de un backend en Python con FastAPI.



## 📋 Características## Descripcion



- Procesamiento de imágenes en tiempo realEsta aplicacion permite a los usuarios capturar o seleccionar imagenes y aplicar diferentes tipos de filtros de vision artificial organizados en categorias:

- Múltiples filtros de visión artificial

- Interfaz intuitiva y fácil de usar- Filtros Elementales (Puntuales)

- Compatible con Android- Filtros Espaciales (Convolucion)

- Filtros Morfologicos

## 🛠️ Requisitos Previos- Otros Filtros OpenCV



Antes de compilar y ejecutar el proyecto, asegúrate de tener instalado:## Arquitectura del Proyecto



- **Flutter SDK** (versión 3.35.7 o superior)El proyecto sigue una arquitectura cliente-servidor:

  - [Guía de instalación de Flutter](https://docs.flutter.dev/get-started/install)

- **Android Studio** o **Visual Studio Code**### Frontend (Flutter)

- **Android SDK** (API 21 o superior)```

- **Git**lib/

├── main.dart                    # Punto de entrada de la aplicacion

## 📦 Instalación├── models/

│   └── filter_category.dart    # Modelos de datos para filtros

### 1. Clonar el repositorio├── services/

│   └── image_processing_service.dart  # Servicio de comunicacion con API

```bash└── screens/

git clone https://github.com/AlbertoMichell/Aplicaci-n-M-vil-de-Filtros-de-Visi-n-Artificial.git    ├── home_screen.dart              # Pantalla principal

cd Aplicaci-n-M-vil-de-Filtros-de-Visi-n-Artificial    ├── filter_selection_screen.dart  # Seleccion de filtros

```    └── filter_apply_screen.dart      # Aplicacion de filtros

```

### 2. Instalar dependencias

### Backend (Python + FastAPI + OpenCV)

```bash```

flutter pub getbackend/

```├── main.py              # API REST con todos los endpoints

└── requirements.txt     # Dependencias Python

## 🚀 Compilación y Ejecución```



### Opción 1: Ejecutar en modo desarrollo## Requisitos Previos



Para ejecutar la aplicación en un dispositivo conectado o emulador:### Para el Frontend (Flutter)

- Flutter SDK (version 3.0.0 o superior)

```bash- Android Studio o Xcode (segun plataforma objetivo)

flutter run- Un dispositivo Android/iOS o emulador

```

### Para el Backend (Python)

### Opción 2: Compilar APK de release- Python 3.8 o superior

- pip (gestor de paquetes Python)

Para generar un APK optimizado para distribución:

## Instalacion

```bash

flutter build apk --release### 1. Clonar el Repositorio

```

```bash

El APK se generará en: `build/app/outputs/flutter-apk/app-release.apk`git clone <URL-del-repositorio>

cd Appmovil

### Opción 3: Usar el APK precompilado```



Este repositorio incluye un APK ya compilado. Puedes encontrarlo en:### 2. Configurar el Backend



``````bash

build/app/outputs/flutter-apk/app-release.apkcd backend

```pip install -r requirements.txt

```

Para instalarlo en tu dispositivo Android:

### 3. Configurar el Frontend

1. Descarga el archivo APK

2. Habilita "Instalar aplicaciones de fuentes desconocidas" en tu dispositivo```bash

3. Abre el archivo APK en tu dispositivocd ..

4. Sigue las instrucciones de instalaciónflutter pub get

```

## 🔧 Comandos Útiles

### 4. Configurar la URL del Backend

### Verificar la instalación de Flutter

Editar el archivo `lib/services/image_processing_service.dart` y cambiar la URL base:

```bash

flutter doctor```dart

```static const String baseUrl = 'http://TU_IP:8000';

```

### Limpiar el proyecto

Reemplazar `TU_IP` con:

```bash- `localhost` si estas usando un emulador Android

flutter clean- `10.0.2.2` si estas usando el emulador de Android Studio

flutter pub get- La IP de tu computadora si estas usando un dispositivo fisico

```

## Ejecucion

### Ejecutar en modo debug

### 1. Iniciar el Backend

```bash

flutter run --debug```bash

```cd backend

python main.py

### Compilar para diferentes plataformas```



```bashEl servidor estara disponible en `http://0.0.0.0:8000`

# APK para Android

flutter build apkPuedes verificar que funciona visitando: `http://localhost:8000/docs`



# App Bundle para Google Play Store### 2. Ejecutar la Aplicacion Flutter

flutter build appbundle

En otra terminal:

# APK dividido por arquitectura (menor tamaño)

flutter build apk --split-per-abi```bash

```flutter run

```

## 📱 Dispositivos Compatibles

O para especificar un dispositivo:

- **Plataforma**: Android

- **API mínima**: 21 (Android 5.0 Lollipop)```bash

- **API objetivo**: 34flutter devices  # Ver dispositivos disponibles

flutter run -d <device-id>

## 🏗️ Estructura del Proyecto```



```## Generacion de APK (Android)

.

├── android/          # Código nativo de AndroidPara generar un APK de lanzamiento:

├── assets/           # Recursos (imágenes, fuentes, etc.)

├── lib/              # Código fuente de Flutter/Dart```bash

│   ├── main.dart    # Punto de entrada de la aplicaciónflutter build apk --release

│   └── ...```

├── build/            # Archivos compilados (incluye APK)

├── pubspec.yaml      # Dependencias del proyectoEl APK estara en: `build/app/outputs/flutter-apk/app-release.apk`

└── README.md         # Este archivo

```Para un APK de depuracion:



## 🐛 Solución de Problemas```bash

flutter build apk --debug

### Error: "SDK location not found"```



Configura la variable de entorno `ANDROID_HOME` apuntando a tu instalación de Android SDK.## Funcionalidades Implementadas



### Error al ejecutar `flutter pub get`### Funcionalidades Principales



Verifica tu conexión a internet y ejecuta:1. Modulo de Entrada de Imagen

   - Captura de foto con camara

```bash   - Seleccion de imagen de galeria

flutter clean   - Manejo de permisos (camara y almacenamiento)

flutter pub cache repair

flutter pub get2. Modulo de Procesamiento con OpenCV

```   - Backend en Python con FastAPI

   - Integracion de OpenCV para procesamiento

### El APK no se instala en el dispositivo   - Separacion clara entre UI y logica de procesamiento



- Verifica que la instalación de fuentes desconocidas esté habilitada3. Sistema de Menus por Clasificacion

- Asegúrate de que el dispositivo tenga Android 5.0 o superior   - Menu principal organizado por categorias

- Desinstala versiones anteriores de la aplicación   - Submenu para cada categoria con filtros especificos



## 👤 Autor4. Filtros Implementados:



**Alberto Michell**   **Filtros Elementales:**

- GitHub: [@AlbertoMichell](https://github.com/AlbertoMichell)   - Brillo y Contraste

- Email: albertomichell@live.com   - Transformacion Gamma

   - Negativo

## 📄 Licencia   - Cuantizacion de niveles



Este proyecto es de código abierto y está disponible para uso educativo y de investigación.   **Filtros Espaciales:**

   - Desenfoque Gaussiano

## 🤝 Contribuciones   - Filtro de Mediana

   - Filtro de Enfoque (Sharpen)

Las contribuciones son bienvenidas. Por favor:   - Deteccion de Bordes (Sobel)

   - Deteccion de Bordes (Laplaciano)

1. Fork el proyecto

2. Crea una rama para tu funcionalidad (`git checkout -b feature/NuevaFuncionalidad`)   **Filtros Morfologicos:**

3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)   - Erosion

4. Push a la rama (`git push origin feature/NuevaFuncionalidad`)   - Dilatacion

5. Abre un Pull Request   - Apertura

   - Cierre

## 📞 Soporte

   **Otros Filtros:**

Si encuentras algún problema o tienes preguntas, por favor abre un [issue](https://github.com/AlbertoMichell/Aplicaci-n-M-vil-de-Filtros-de-Visi-n-Artificial/issues) en GitHub.   - Canny Edge Detection

   - Escala de Grises

---   - Deteccion de Contornos

   - Ecualizacion de Histograma

**Nota**: Este repositorio incluye los archivos de compilación (`build/`) para facilitar la distribución del APK. En un proyecto de producción típico, estos archivos normalmente se excluirían del control de versiones.

### Funcionalidades Adicionales

- Control deslizante (Slider) para ajustar parametros de filtros
- Vista lado a lado de imagen original y procesada
- Posibilidad de aplicar multiples filtros en secuencia
- Funcionalidad de "Deshacer" para revertir el ultimo filtro
- Boton de "Reset" para volver a la imagen original
- Indicador de carga mientras se procesa
- Opcion para guardar imagen en galeria

## Estructura de la API

### Endpoints Principales

- `GET /health` - Verificar estado del servidor
- `POST /filter/brightness_contrast` - Ajustar brillo y contraste
- `POST /filter/gamma` - Correccion gamma
- `POST /filter/negative` - Negativo de imagen
- `POST /filter/quantization` - Cuantizacion de niveles
- `POST /filter/gaussian_blur` - Desenfoque gaussiano
- `POST /filter/median_blur` - Filtro de mediana
- `POST /filter/sharpen` - Filtro de enfoque
- `POST /filter/sobel` - Deteccion de bordes Sobel
- `POST /filter/laplacian` - Deteccion de bordes Laplaciano
- `POST /filter/erosion` - Erosion morfologica
- `POST /filter/dilation` - Dilatacion morfologica
- `POST /filter/opening` - Apertura morfologica
- `POST /filter/closing` - Cierre morfologico
- `POST /filter/canny` - Deteccion de bordes Canny
- `POST /filter/grayscale` - Conversion a escala de grises
- `POST /filter/contours` - Deteccion de contornos
- `POST /filter/histogram_equalization` - Ecualizacion de histograma

## Tecnologias Utilizadas

### Frontend
- **Flutter/Dart**: Framework multiplataforma para desarrollo movil
- **image_picker**: Captura y seleccion de imagenes
- **permission_handler**: Manejo de permisos
- **http**: Cliente HTTP para comunicacion con API
- **image_gallery_saver**: Guardar imagenes en galeria
- **flutter_spinkit**: Indicadores de carga animados

### Backend
- **Python**: Lenguaje de programacion
- **FastAPI**: Framework web moderno para APIs
- **OpenCV**: Biblioteca de vision artificial
- **NumPy**: Procesamiento numerico
- **Uvicorn**: Servidor ASGI

## Solucion de Problemas

### El backend no se puede conectar
- Verificar que el servidor este corriendo en el puerto 8000
- Verificar que la IP en `image_processing_service.dart` sea correcta
- Verificar firewall y permisos de red

### Problemas con permisos en Android
- Asegurar que `AndroidManifest.xml` tiene todos los permisos
- En Android 13+, puede requerir permisos adicionales

### Error al guardar imagen
- Verificar permisos de almacenamiento
- En Android 10+, verificar configuracion de `requestLegacyExternalStorage`

## Contribuidores

[Agregar nombres de los integrantes del equipo]

## Licencia

Este proyecto fue desarrollado como parte del curso de Vision Artificial.

---

Para mas detalles tecnicos, consultar el archivo `MEMORIA_TECNICA.md`
