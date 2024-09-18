# API-de-Flask-para-SwiftUI-App
Esta es una API creada con Flask para ser utilizada con una aplicación frontend creada con SwiftUI. La API proporciona funcionalidades específicas para la aplicación, y se puede configurar utilizando un archivo `.env` para las variables de entorno.


## Requisitos

Asegúrate de tener instalados los siguientes requisitos antes de ejecutar la aplicación:

- Python 3.x
- pip (gestor de paquetes de Python)

- ## Instalación

1. **Clona el repositorio:**

    ```bash
    git clone [https://github.com/tu_usuario/nombre_del_repositorio.git](https://github.com/DLeonProyects/API-de-Flask-para-SwiftUI-App.git)
    cd API-de-Flask-para-SwiftUI-App
    ```

2. **Crea un entorno virtual (opcional pero recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\\Scripts\\activate`
    ```

3. **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```


## Configuración

1. **Archivo `.env`:**

    Crea un archivo `.env` en el directorio raíz del proyecto. Este archivo debe contener las variables de entorno necesarias para la configuración de la API. A continuación, un ejemplo de cómo podría verse tu archivo `.env`:

    ```
    SECRET_KEY=tu_secreto
    MAIL_SERVER=smtp.tuservidor.com
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=tu_correo@example.com
    MAIL_PASSWORD=tu_contraseña
    ```

    Asegúrate de completar las variables de entorno con la información correcta para tu aplicación.

## Ejecución de la API

1. **Ejecuta la API:**

    Con el entorno virtual activado (si decidiste usar uno), ejecuta el siguiente comando para iniciar la aplicación:

    ```bash
    python app.py or python3 app.py
    ```

2. **Accede a la API:**

    La API estará disponible en `http://127.0.0.1:5000/` por defecto.

## Uso

Esta API se ha creado para ser utilizada con una aplicación frontend desarrollada con SwiftUI. Consulta la documentación de la API o el código fuente para ver los endpoints disponibles y cómo interactuar con ellos desde tu aplicación.

## Dependencias

Las dependencias necesarias para ejecutar esta API se enumeran en el archivo `requirements.txt` y se instalan automáticamente con `pip install -r requirements.txt`.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu nueva funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios y haz commit de ellos (`git commit -am 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.
