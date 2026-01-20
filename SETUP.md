# AIGC散修学习平台 - 环境配置指南

本指南将帮助你从零开始搭建完整的开发环境。

---

## 📋 前置要求

- **Node.js** 18+ 
- **Python** 3.10+
- **PostgreSQL** 14+ （本指南重点）
- Git

---

## 🗄️ PostgreSQL 数据库安装

### Windows 系统

#### 方法1: 使用安装程序（推荐新手）

1. **下载 PostgreSQL**
   - 访问：https://www.postgresql.org/download/windows/
   - 下载 PostgreSQL 14 或更高版本安装程序
   - 推荐下载：`postgresql-14.x-x-windows-x64.exe`

2. **安装步骤**
   ```
   - 运行安装程序
   - 选择安装目录（默认 C:\Program Files\PostgreSQL\14）
   - 选择组件：全部勾选
   - 数据目录：使用默认
   - 设置超级用户密码：postgres（或自定义密码，需记住）
   - 端口：5432（默认）
   - 区域：Chinese, China
   - 完成安装后会自动启动 PostgreSQL 服务
   ```

3. **验证安装**
   ```bash
   # 打开命令提示符（CMD）或 PowerShell
   psql --version
   
   # 应显示类似：psql (PostgreSQL) 14.x
   ```

#### 方法2: 使用 Chocolatey（推荐开发者）

```bash
# 以管理员身份运行 PowerShell
choco install postgresql

# 安装后启动服务
net start postgresql-x64-14
```

#### 方法3: 使用 Docker

```bash
# 启动 PostgreSQL 容器
docker run -d \
  --name epicindi-postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=epicindi_coreverse \
  -p 5432:5432 \
  postgres:14

# 验证容器运行
docker ps
```

---

### macOS 系统

#### 使用 Homebrew

```bash
# 安装 PostgreSQL
brew install postgresql@14

# 启动服务
brew services start postgresql@14

# 验证安装
psql --version
```

#### 使用 Postgres.app（GUI 应用）

1. 下载：https://postgresapp.com/
2. 解压并拖到 Applications 文件夹
3. 打开应用，点击 "Initialize" 初始化数据库
4. 添加到 PATH：
   ```bash
   echo 'export PATH="/Applications/Postgres.app/Contents/Versions/14/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

---

### Linux 系统

#### Ubuntu/Debian

```bash
# 更新包列表
sudo apt update

# 安装 PostgreSQL
sudo apt install postgresql postgresql-contrib

# 启动服务
sudo systemctl start postgresql
sudo systemctl enable postgresql

# 验证安装
psql --version
```

#### CentOS/RHEL

```bash
# 安装 PostgreSQL
sudo yum install postgresql-server postgresql-contrib

# 初始化数据库
sudo postgresql-setup initdb

# 启动服务
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

---

## 🔧 创建数据库

### 方法1: 使用 psql 命令行

```bash
# Windows: 打开 SQL Shell (psql) 或命令提示符
# macOS/Linux: 打开终端

# 连接到 PostgreSQL
psql -U postgres

# 输入密码（安装时设置的密码）

# 创建数据库
CREATE DATABASE epicindi_coreverse;

# 验证数据库已创建
\l

# 退出 psql
\q
```

### 方法2: 使用 pgAdmin（图形界面）

1. 打开 pgAdmin（安装 PostgreSQL 时一起安装）
2. 连接到本地服务器（localhost）
3. 右键 "Databases" → "Create" → "Database"
4. 数据库名称：`epicindi_coreverse`
5. 点击 "Save"

### 方法3: 使用命令行一键创建

```bash
# Windows (PowerShell/CMD)
psql -U postgres -c "CREATE DATABASE epicindi_coreverse;"

# macOS/Linux
sudo -u postgres psql -c "CREATE DATABASE epicindi_coreverse;"
```

---

## ⚙️ 项目配置

### 1. 后端配置

```bash
cd backend

# 确保 .env 文件已存在（已自动创建）
# 如果密码不是 postgres，需要修改 .env 文件：
```

编辑 `backend/.env` 文件：

```env
# 数据库配置
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres  # 修改为你的密码
POSTGRES_DB=epicindi_coreverse

# 其他配置保持默认
```

### 2. 安装 Python 依赖

```bash
cd backend

# 创建虚拟环境（推荐）
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 3. 初始化数据库

```bash
cd backend

# 运行初始化脚本
python scripts/init_db.py
```

**成功后会显示：**
```
============================================================
AIGC散修学习平台 - 数据库初始化
============================================================

🔧 创建数据库表...
✅ 数据库表创建成功
🔧 初始化用户等级...
✅ 创建了 8 个等级配置
🔧 初始化内容分类...
✅ 创建了 7 个内容分类
⚠️  论坛分类已存在，跳过
⚠️  作业分类已存在，跳过
🔧 创建超级管理员账号...
✅ 超级管理员创建成功
   用户名: admin
   邮箱: admin@epicindi.com
   密码: admin123456
   邀请码: XXXXX

🔧 创建初始邀请码用户...
✅ 初始邀请码创建成功
   共创建 10 个邀请码，每个可邀请 50 人

============================================================
📋 初始邀请码列表（请妥善保管）:
============================================================
   1. ABC123XYZ
   2. DEF456UVW
   ...
  10. GHI789RST
============================================================

✅ 数据库初始化完成！
```

**请记录这些邀请码！** 它们将用于用户注册。

### 4. 启动后端服务

```bash
cd backend

# 启动 FastAPI 服务器
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

访问：
- API 文档：http://localhost:8000/api/v1/docs
- 健康检查：http://localhost:8000/health

### 5. 安装前端依赖

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

访问：http://localhost:3000

---

## 🎯 验证安装

### 1. 检查 PostgreSQL 服务

```bash
# Windows
sc query postgresql-x64-14

# macOS
brew services list | grep postgresql

# Linux
sudo systemctl status postgresql

# Docker
docker ps | grep postgres
```

### 2. 测试数据库连接

```bash
# 方法1: psql 连接
psql -U postgres -d epicindi_coreverse -c "SELECT version();"

# 方法2: Python 脚本测试
cd backend
python -c "from app.core.database import engine; import asyncio; asyncio.run(engine.connect())"
```

### 3. 测试完整流程

1. 打开前端注册页面：http://localhost:3000/register
2. 输入初始化时获得的邀请码
3. 完成注册
4. 登录系统

---

## ❌ 常见问题排查

### 问题1: 无法连接数据库

**错误信息：** `ConnectionRefusedError` 或 `could not connect to server`

**解决方案：**
```bash
# 检查 PostgreSQL 是否运行
# Windows:
net start postgresql-x64-14

# macOS:
brew services start postgresql@14

# Linux:
sudo systemctl start postgresql

# Docker:
docker start epicindi-postgres
```

### 问题2: 密码认证失败

**错误信息：** `password authentication failed`

**解决方案：**
1. 确认 `.env` 文件中的密码正确
2. 重置 PostgreSQL 密码：
   ```bash
   psql -U postgres
   ALTER USER postgres PASSWORD 'new_password';
   ```
3. 更新 `backend/.env` 文件中的 `POSTGRES_PASSWORD`

### 问题3: 数据库不存在

**错误信息：** `database "epicindi_coreverse" does not exist`

**解决方案：**
```bash
psql -U postgres -c "CREATE DATABASE epicindi_coreverse;"
```

### 问题4: 端口被占用

**错误信息：** `Port 5432 is already in use`

**解决方案：**
```bash
# Windows: 查找占用进程
netstat -ano | findstr :5432
taskkill /PID <PID> /F

# macOS/Linux: 查找占用进程
lsof -i :5432
kill -9 <PID>
```

### 问题5: 依赖安装失败

**错误信息：** `ModuleNotFoundError: No module named 'xxx'`

**解决方案：**
```bash
cd backend

# 重新安装依赖
pip install -r requirements.txt

# 如果特定包失败，单独安装
pip install "pydantic[email]"
pip install email-validator
```

---

## 🔐 安全建议

### 生产环境配置

1. **修改默认密码**
   ```bash
   psql -U postgres -d epicindi_coreverse
   ALTER USER admin WITH PASSWORD 'strong_password_here';
   ```

2. **生成强随机密钥**
   ```python
   import secrets
   print(secrets.token_urlsafe(32))
   ```
   
   将输出的密钥替换 `backend/.env` 中的 `SECRET_KEY`

3. **限制数据库访问**
   - 编辑 `pg_hba.conf` 文件
   - 仅允许必要的 IP 地址访问

4. **启用 SSL 连接**
   ```env
   # backend/.env
   DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/epicindi_coreverse?ssl=require
   ```

---

## 📚 进阶配置

### 使用 pgAdmin 管理数据库

1. 打开 pgAdmin：http://localhost:5050
2. 添加新服务器：
   - Name: Local Dev
   - Host: localhost
   - Port: 5432
   - Username: postgres
   - Password: your_password

### 配置自动备份

```bash
# 创建备份脚本
pg_dump -U postgres epicindi_coreverse > backup_$(date +%Y%m%d).sql

# Windows 计划任务 / Linux cron job 自动执行
```

### 性能优化

```sql
-- 查看数据库统计
SELECT * FROM pg_stat_database WHERE datname = 'epicindi_coreverse';

-- 分析慢查询
ALTER DATABASE epicindi_coreverse SET log_min_duration_statement = 1000;
```

---

## 🎉 完成！

现在你已经成功配置好了完整的开发环境：

- ✅ PostgreSQL 数据库运行中
- ✅ 数据库已初始化，包含 10 个邀请码
- ✅ 后端 API 服务器运行在 http://localhost:8000
- ✅ 前端应用运行在 http://localhost:3000
- ✅ 可以使用邀请码注册新用户

**下一步：**
- 使用邀请码注册你的第一个用户
- 登录系统体验完整功能
- 开始开发新功能！

有问题？查看：
- 后端文档：`backend/README.md`
- 前端文档：`frontend/DEPLOYMENT.md`
- 项目概览：`README.md`
