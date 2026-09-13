from fastapi import FastAPI

from src.apps.business.channel_intelligence.routers import router as channel_intelligence_router
from src.apps.system.auth.routers import router as auth_router
from src.apps.system.health.routers import router as health_router
from src.apps.system.users.routers import router as user_router

app = FastAPI(
    title="TikTok Channel Intelligence API",
    description="TikTok 渠道数据采集与分析看板后端",
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(channel_intelligence_router)


@app.get("/")
async def root():
    return {"message": "TikTok Channel Intelligence API is running"}
