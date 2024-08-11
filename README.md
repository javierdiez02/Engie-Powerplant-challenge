# Powerplant Coding Challenge

## Requisitos
- Python 3.8+
- Flask

## Instalación
```bash
pip install -r requirements.txt

## Instrucciones para Probar la API

### Requisitos Previos
- **Postman**: Asegúrate de tener Postman instalado. 

### Cómo Probar la API con Postman

1. **Iniciar el Servidor Flask**:
   - Asegúrate de que el servidor Flask esté ejecutándose en `http://localhost:8888`.
   - Para iniciar el servidor, ejecuta el siguiente comando en tu terminal:
     ```bash
     python appy.py
     ```

2. **Configuración de la Solicitud en Postman**:

   1. **Abrir Postman y Crear una Nueva Solicitud**:
      - Haz clic en `New` > `Request` para crear una nueva solicitud.

   2. **Configurar el Método y la URL**:
      - Selecciona `POST` en el menú desplegable a la izquierda del campo de la URL.
      - Introduce la siguiente URL: `http://localhost:8888/productionplan`.

   3. **Configurar los Headers**:
      - Dirígete a la pestaña `Headers`.
      - Añade el siguiente encabezado:
        - **Key**: `Content-Type`
        - **Value**: `application/json`

   4. **Configurar el Cuerpo de la Solicitud (Body)**:
      - Ve a la pestaña `Body`.
      - Selecciona `raw` y elige `JSON` en el menú desplegable a la derecha.
      - Copia y pega el ejemplo de payload JSON
  
3. **Enviar la Solicitud**:
 - Haz clic en el botón `Send` en la parte superior derecha.
 - Verás la respuesta de la API en la parte inferior de Postman.