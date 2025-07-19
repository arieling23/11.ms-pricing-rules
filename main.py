from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from app.graphql.schema import schema
from app.auth.dependencies import get_current_user
from app.config.logging_config import logger
from app.db.db import init_db
from app.config.settings import PORT  # ✅ Importar puerto desde .env

app = FastAPI()

# Log de inicio
logger.info("🚀 Iniciando microservicio ms-pricing-rules")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JWT context
async def get_context(request: Request):
    user = await get_current_user(request)
    logger.info(f"🔐 Solicitud autenticada de: {user.get('sub')}")
    return {"request": request, "user": user}

# GraphQL
graphql_app = GraphQLRouter(schema, context_getter=get_context)
app.include_router(graphql_app, prefix="/api/pricing")

# Conexión a la base de datos al iniciar
@app.on_event("startup")
async def startup_event():
    logger.info("🔄 Iniciando conexión a la base de datos...")
    await init_db()

# Ejecutar usando el puerto de .env
if __name__ == "__main__":
    import uvicorn
    logger.info(f"🟢 Servidor escuchando en puerto {PORT}")
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)
