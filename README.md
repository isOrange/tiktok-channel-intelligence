# TikTok Channel Intelligence

TikTok Channel Intelligence 是一个用于 TikTok 渠道账号采集、视频指标入库和数据看板展示的 FastAPI 后端项目。

项目当前聚焦三个核心能力：

- 管理 TikTok 渠道账号数据源。
- 使用 `yt-dlp` 采集公开视频指标并写入 MySQL。
- 为前端看板提供总览、筛选项、账号排行、店铺汇总、视频列表和内容信号接口。

## 技术栈

- Python
- FastAPI
- SQLAlchemy Async
- MySQL
- Alembic
- yt-dlp

## 项目结构

```text
src/apps/system/
  auth/                  # 登录、JWT、当前用户
  users/                 # 用户基础能力
  health/                # 健康检查

src/apps/business/
  channel_intelligence/  # TikTok 渠道数据源、采集记录、视频指标和看板接口

migrations/              # Alembic 数据库迁移
scripts/                 # 数据采集验证脚本
```

## 本地运行

1. 创建数据库：

```sql
CREATE DATABASE tiktok_channel_intelligence CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

2. 配置环境变量：

```text
JWT_SECRET_KEY=change-me
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=mysql+asyncmy://root:your-password@127.0.0.1:3306/tiktok_channel_intelligence
```

3. 执行迁移：

```powershell
.venv\Scripts\python.exe -m alembic upgrade head
```

4. 启动服务：

```powershell
.venv\Scripts\python.exe -m uvicorn main:app --reload
```

5. 打开接口文档：

```text
http://127.0.0.1:8000/docs
```

## 核心接口

```text
GET  /channel-intelligence/dashboard
GET  /channel-intelligence/summary
GET  /channel-intelligence/shops
GET  /channel-intelligence/accounts
GET  /channel-intelligence/videos
GET  /channel-intelligence/filters
GET  /channel-intelligence/signals
POST /channel-intelligence/sources
GET  /channel-intelligence/sources
POST /channel-intelligence/sources/{source_id}/collect
GET  /channel-intelligence/collection-runs
```

## 当前边界

当前采集基于 TikTok 公开页面数据，适合做公开视频指标看板。GMV、成交、广告成本等非公开经营数据不在当前数据源范围内。
