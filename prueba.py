from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId

# Crea la aplicación FastAPI
app = FastAPI()

# Conexión a MongoDB
try:
    # Intenta establecer la conexión
    client = MongoClient('mongodb://localhost:27017/')

    # Selecciona la base de datos
    db = client['microInfo']
    ADMIN = db['admin']

    # Imprime un mensaje si la conexión es exitosa
    print("Conexión exitosa a MongoDB Atlas")

except Exception as e:
    print("Error de conexión a MongoDB Atlas:", e)

# Define el endpoint GET para buscar un admin por ID
@app.get("/admin/{admin_id}")
async def get_admin_by_id(admin_id: str):
    respuesta = []
    try:
        # Busca el admin por su ID en la colección
        admin = ADMIN.find({"_id": ObjectId(admin_id)})

        for resultado in admin:
            resultado['_id'] = str(resultado['_id'])
            respuesta.append(resultado)
        # Si el admin no se encuentra, levanta una excepción HTTP 404
        if respuesta is None:
            raise HTTPException(status_code=404, detail="Admin no encontrado")

        return respuesta

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor, {e}")
