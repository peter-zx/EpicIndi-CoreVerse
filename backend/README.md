# AIGC散修学习平台 - 后端部署指南

## 环境要求

- Python 3.10+
- **PostgreSQL 14+** (外部依赖，需要单独安装)
- Redis 6+ (可选，用于缓存)

## 快速开始

### 0. 安装 PostgreSQL（外部依赖）

**Windows 系统：**

```bash
# 方法1: 使用 Chocolatey 包管理器（推荐）
choco install postgresql

# 方法2: 手动下载安装
# 访问 https://www.postgresql.org/download/windows/
# 下载并安装 PostgreSQL 14 或更高版本
```

**macOS 系统：**

```bash
# 使用 Homebrew
brew install postgresql@14
brew services start postgresql@14
```

**Linux 系统：**

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib

# CentOS/RHEL
sudo yum install postgresql-server postgresql-contrib
sudo postgresql-setup initdb
sudo systemctl start postgresql
```

**默认配置：**
- 用户名: `postgres`
- 密码: 安装时设置（本地开发可用 `postgres`）
- 端口: `5432`

### 1. 安装依赖

```bash
cd backend
pip install -r requirements.txt
```

### 2. 配置环境变量

复制环境变量模板：
```bash
cp .env.example .env
```

编辑 `.env` 文件，配置数据库连接：
```env
# 数据库配置（本地开发默认值）
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=epicindi_coreverse

# 安全密钥（生产环境必须修改）
SECRET_KEY=your-super-secret-key-change-in-production
```

⚠️ **如果你的 PostgreSQL 密码不是 `postgres`，请修改 `POSTGRES_PASSWORD`**

### 3. 创建数据库

在 PostgreSQL 中创建数据库：
```sql
CREATE DATABASE epicindi_coreverse;
```

### 4. 初始化数据库

运行初始化脚本：
```bash
python scripts/init_db.py
```

这将：
- 创建所有数据库表
- 初始化8个用户等级配置
- 创建内容分类和论坛分类
- 创建超级管理员账号
- **创建10个初始邀请码（用于冷启动注册）**

**默认管理员账号：**
- 用户名: `admin`
- 密码: `admin123456`
- 邮箱: `admin@epicindi.com`

**初始邀请码：**
- 脚本会生成10个邀请码，每个可邀请50人
- 邀请码会在初始化完成后显示在终端
- 请妥善保管这些邀请码，用于早期用户注册

⚠️ **请立即修改默认密码！**

### 5. 启动后端服务

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

访问 API 文档：
- Swagger UI: http://localhost:8000/api/v1/docs
- ReDoc: http://localhost:8000/api/v1/redoc

## 创建测试用户（可选）

```bash
python scripts/create_test_users.py
```

这将创建3个测试账号：
- testuser1 / test123456
- testuser2 / test123456
- senior1 / test123456 (高级用户)

## 数据库迁移（使用Alembic）

### 生成迁移文件
```bash
alembic revision --autogenerate -m "描述"
```

### 执行迁移
```bash
alembic upgrade head
```

### 回滚迁移
```bash
alembic downgrade -1
```

## 用户等级说明

| 等级 | 名称 | 所需经验 | 特权 |
|------|------|---------|------|
| 1 | 见习散修 | 0 | 下载3次/天 |
| 2 | 炼气散修 | 100 | 下载5次/天 |
| 3 | 筑基散修 | 500 | 下载10次/天 |
| 4 | 金丹散修 | 1500 | 发布任务 + 下载20次/天 |
| 5 | 元婴散修 | 3000 | 发布任务 + 下载30次/天 |
| 6 | 化神散修 | 5000 | 批阅作业 + 下载50次/天 |
| 7 | 渡劫散修 | 10000 | 批阅作业 + 下载100次/天 |
| 8 | 大乘散修 | 20000 | 全部权限 + 下载999次/天 |

## 积分规则

- 注册奖励: 100积分
- 每日登录: 10积分
- 发帖: 20积分
- 评论: 5积分
- 提交作业: 30积分
- 批阅作业: 50积分

## 常见问题

### 1. 数据库连接失败
- 检查 PostgreSQL 是否启动
- 确认 `.env` 中的数据库配置正确
- 确认数据库已创建

### 2. 模块导入错误
```bash
# 安装所有依赖
pip install -r requirements.txt
```

### 3. Alembic 迁移失败
```bash
# 重新初始化 Alembic
rm -rf alembic/versions/*
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```

## 生产环境配置

### 1. 修改安全配置
```env
DEBUG=False
SECRET_KEY=使用强随机密钥
```

生成安全密钥：
```python
import secrets
print(secrets.token_urlsafe(32))
```

### 2. 配置阿里云OSS
```env
OSS_ACCESS_KEY_ID=你的AccessKeyId
OSS_ACCESS_KEY_SECRET=你的AccessKeySecret
OSS_BUCKET_NAME=你的Bucket名称
OSS_ENDPOINT=oss-cn-hangzhou.aliyuncs.com
```

### 3. 使用 Gunicorn
```bash
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 目录结构

```
backend/
├── app/
│   ├── api/           # API路由
│   ├── core/          # 核心配置
│   ├── models/        # 数据库模型
│   ├── schemas/       # Pydantic模型
│   ├── services/      # 业务逻辑
│   └── main.py        # 入口文件
├── alembic/           # 数据库迁移
├── scripts/           # 工具脚本
└── requirements.txt   # 依赖列表
```

## API 端点预览

### 认证
- POST `/api/v1/auth/register` - 用户注册
- POST `/api/v1/auth/login` - 用户登录
- POST `/api/v1/auth/validate-invite-code` - 验证邀请码

### 用户
- GET `/api/v1/users/me` - 获取当前用户信息
- PUT `/api/v1/users/me` - 更新用户信息
- GET `/api/v1/users/leaderboard` - 积分排行榜

详细API文档请查看：http://localhost:8000/api/v1/docs
