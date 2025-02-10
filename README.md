# FastAPI con SQLModel

Este proyecto implementa una API utilizando FastAPI y SQLModel para manejar clientes, transacciones, planes de suscripción y datos meteorológicos.

## Requisitos previos

- Python 3.10+
- FastAPI
- SQLModel
- Uvicorn

## Instalación

Crea un entorno virtual:

```sh
$ source venv/bin/activate  
$ pip install -r requirements.txt
```

## Ejecución

Para iniciar el servidor, entra a la carpeta del proyecto y ejecuta:

```sh
$ cd curso_fastapi_project/
$ fastapi dev app/main.py
```

La API estará disponible en `http://127.0.0.1:8000` y la documentación interactiva en:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Modelos de Datos

### Customer
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "johndoe@example.com",
  "age": 30,
  "description": "Cliente frecuente"
}
```

### Transaction
```json
{
  "id": 1,
  "customer_id": 1,
  "ammount": 100,
  "description": "Pago mensual"
}
```

### Plan
```json
{
  "id": 1,
  "name": "Premium",
  "price": 50,
  "descripcion": "Acceso ilimitado"
}
```

### Weather
```json
{
  "id": 1,
  "city_name": "Madrid",
  "date": "2024-02-10 12:00:00",
  "temp_max": 25.3,
  "temp_min": 15.8,
  "lat": 40.4168,
  "lon": -3.7038
}
```

## Ejemplos de Uso

### Crear un Cliente

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/customers' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Jane Doe",
    "email": "janedoe@example.com",
    "age": 28,
    "description": "Nueva suscripción"
  }'
```

### Obtener un Cliente por ID

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/customers/1' \
  -H 'Accept: application/json'
```

### Crear una Transacción

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/transactions' \
  -H 'Content-Type: application/json' \
  -d '{
    "customer_id": 1,
    "ammount": 150,
    "description": "Pago anual"
  }'
```

### Listar Transacciones

```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/transactions' \
  -H 'Accept: application/json'
```

### Suscribir Cliente a un Plan

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/customers/1/plans/1' \
  -H 'Accept: application/json'
```

## Endpoints del Clima

### Obtener todos los registros de clima guardados
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/weather' \
  -H 'Accept: application/json'
```

### Obtener el clima actual de una ubicación específica
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/weather/{lat}/{lon}/{cnt}' \
  -H 'Accept: application/json'
```
- `lat`: Latitud de la ubicación
- `lon`: Longitud de la ubicación
- `cnt`: Número de días que se devolverá en la respuesta

### Guardar el día más caluroso en la base de datos
```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/save_weather/{lat}/{lon}/{cnt}' \
  -H 'Accept: application/json'
```

### Eliminar un registro de clima por ID
```sh
curl -X 'DELETE' \
  'http://127.0.0.1:8000/weather/{weather_id}' \
  -H 'Accept: application/json'
```

📌 **Autor:** Nicolle Rodríguez Laytón

