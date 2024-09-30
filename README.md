# Tienda de Cafe-It Hardware 

Este proyecto tiene fines educativos y pertenece a la comunidad de desarrolladores de Café IT - Sgo Del Estero

## Requisitos 

* Tener instalado python

### Sigue estos pasos para clonar el repositorio

1. Instalar git en tu pc en caso de no tener:

    * Pagina Oficial de git: https://git-scm.com/downloads

2. Clonar el repositorio en tu pc:
    
    * Windows
    ```bash
        git clone https://github.com/AlvaroOk007/tienda-cafe-it-hardware-sgo-django.git
    ```

### Ejecutar la aplicacion en tu computadora

1. Crear entorno virtual para aislar la aplicacion de tus demas aplicaciones

    * Windows
    ```bash
        python -m venv env
    ```

2. Activar el entorno virtual (IMPORTANTE):

    * Windows
    ```bash
        env\Scripts\activate
    ```
3. Instalar dependencias de la aplicacion: 

    * Windows
    ```bash
        pip install -r requirements.txt
    ```

4. Cambio al directorio "tiendaHardware":

    * Windows
    ```bash
        cd tiendaHardware
    ```

5. Realizo migraciones:

    * Windows
    ```bash
        python manage.py migrate
    ```

6. Le doy mecha:

    * Windows
    ```bash
        python manage.py runserver
    ```
    