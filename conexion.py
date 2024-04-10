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
    ASIGNACION = db['asignacion']
    CHECADOR = db['checador']
    CHOFER = db['chofer']
    ESCANEO = db['escaneo']
    REPORTES = db['reportes']
    RUTA = db['ruta']
    UNIDADES = db['unidades']

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

# Define el endpoint GET para consultar todos los documentos en la colección "asignacion"
@app.get("/asignacion/")
async def get_all_asignaciones():
    respuesta = []
    try:
        # Consulta todos los documentos en la colección "asignacion"
        asignaciones = ASIGNACION.find()

        for asignacion in asignaciones:
            asignacion['_id'] = str(asignacion['_id'])
            respuesta.append(asignacion)

        return respuesta

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor, {e}")

# Define el endpoint GET para consultar todos los documentos en la colección "checador"
@app.get("/checador/")
async def get_all_checadores():
    respuesta = []
    try:
        # Consulta todos los documentos en la colección "checador"
        checadores = CHECADOR.find()

        for checador in checadores:
            checador['_id'] = str(checador['_id'])
            respuesta.append(checador)

        return respuesta

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor, {e}")
    
# Define el endpoint GET para consultar todos los documentos en la colección "chofer"
@app.get("/chofer/")
async def get_all_choferes():
    respuesta = []
    try:
        # Consulta todos los documentos en la colección "chofer"
        choferes = CHOFER.find()

        for chofer in choferes:
            chofer['_id'] = str(chofer['_id'])
            respuesta.append(chofer)

        return respuesta

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor, {e}")

# Define el endpoint GET para consultar todos los documentos en la colección "checador"
@app.get("/escaneo/")
async def get_all_escaneos():
    respuesta = []
    try:
        # Consulta todos los documentos en la colección "asignacion"
        escaneos = ESCANEO.find()

        for escaneo in escaneos:
            escaneo['_id'] = str(escaneo['_id'])
            respuesta.append(escaneo)

        return respuesta

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor, {e}")
    
# Define el endpoint GET para consultar todos los documentos en la colección "checador"
@app.get("/reportes/")
async def get_all_reportes():
    respuesta = []
    try:
        # Consulta todos los documentos en la colección "asignacion"
        reportes = REPORTES.find()

        for reporte in reportes:
            reporte['_id'] = str(reporte['_id'])
            respuesta.append(reporte)

        return respuesta

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor, {e}")
    
# Define el endpoint GET para consultar todos los documentos en la colección "checador"
@app.get("/ruta/")
async def get_all_rutas():
    respuesta = []
    try:
        # Consulta todos los documentos en la colección "asignacion"
        rutas = RUTA.find()

        for ruta in rutas:
            ruta['_id'] = str(ruta['_id'])
            respuesta.append(ruta)

        return respuesta

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor, {e}")
    
# Define el endpoint GET para consultar todos los documentos en la colección "checador"
@app.get("/unidades/")
async def get_all_unidades():
    respuesta = []
    try:
        # Consulta todos los documentos en la colección "asignacion"
        unidades = UNIDADES.find()

        for unidad in unidades:
            unidad['_id'] = str(unidad['_id'])
            respuesta.append(unidad)

        return respuesta

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor, {e}")