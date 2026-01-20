# 数据库初始化快速指南

## 🚀 快速开始

数据库初始化脚本已准备好，一旦 PostgreSQL 服务启动，运行脚本即可完成所有配置。

---

## Windows 用户

### 1. 启动 PostgreSQL 服务

**方法1：使用服务管理器（推荐）**
1. 按 `Win + R`，输入 `services.msc`，回车
2. 找到 `postgresql-x64-14` 服务
3. 右键 → 启动

**方法2：使用管理员 PowerShell**
```powershell
Start-Service postgresql-x64-14
```

### 2. 运行初始化脚本

双击运行：
```
backend\scripts\START_DB_INIT.bat
```

或在命令行中：
```bash
cd backend\scripts
START_DB_INIT.bat
```

---

## macOS/Linux 用户

### 1. 启动 PostgreSQL 服务

**macOS (Homebrew):**
```bash
brew services start postgresql@14
```

**Linux (Ubuntu/Debian):**
```bash
sudo systemctl start postgresql
```

### 2. 运行初始化脚本

```bash
cd backend/scripts
bash start_db_init.sh
```

---

## 🎯 脚本功能

初始化脚本将自动完成：

1. ✅ **检查 PostgreSQL 服务状态**
   - 确保数据库服务正在运行

2. ✅ **创建数据库**
   - 数据库名：`epicindi_coreverse`
   - 如果已存在则跳过

3. ✅ **初始化数据库表结构**
   - 创建所有表（users, contents, forum, homework 等）
   - 配置 8 个用户等级
   - 创建内容分类、论坛分类、作业分类
   - 创建超级管理员账号
   - **生成 10 个初始邀请码**

4. ✅ **显示邀请码**
   - 脚本会输出 10 个可用的邀请码
   - 每个邀请码可邀请 50 人

---

## 📋 初始化后的信息

脚本成功运行后会显示：

### 超级管理员账号
```
用户名: admin
密码: admin123456
邮箱: admin@epicindi.com
邀请码: [随机生成]
```

### 10 个初始邀请码
```
============================================================
📋 初始邀请码列表（请妥善保管）:
============================================================
   1. ABC123XYZ
   2. DEF456UVW
   ...
  10. GHI789RST
============================================================
```

**请保存这些邀请码！** 用于用户注册。

---

## ⚠️ 常见问题

### 问题1: 脚本提示"PostgreSQL 服务未运行"

**解决方案：**
按照上述步骤启动 PostgreSQL 服务，然后重新运行脚本。

### 问题2: 密码认证失败

**错误信息：** `password authentication failed`

**解决方案：**
编辑 `backend/.env` 文件，修改 `POSTGRES_PASSWORD` 为你的实际密码：
```env
POSTGRES_PASSWORD=你的实际密码
```

### 问题3: 数据库已存在

脚本会自动跳过数据库创建步骤，这是正常的。

### 问题4: Python 依赖缺失

**解决方案：**
```bash
cd backend
pip install -r requirements.txt
```

---

## 🔄 重新初始化

如果需要重新初始化数据库（**警告：会删除所有数据**）：

### Windows:
```bash
"C:\Program Files\PostgreSQL\14\bin\psql.exe" -U postgres -c "DROP DATABASE IF EXISTS epicindi_coreverse;"
"C:\Program Files\PostgreSQL\14\bin\psql.exe" -U postgres -c "CREATE DATABASE epicindi_coreverse;"
```

### macOS/Linux:
```bash
dropdb -U postgres epicindi_coreverse
createdb -U postgres epicindi_coreverse
```

然后重新运行初始化脚本。

---

## 📝 后续步骤

初始化完成后：

1. **启动后端服务器**
   ```bash
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **访问前端注册页面**
   - http://localhost:3000/register

3. **使用邀请码注册**
   - 输入脚本显示的任意一个邀请码
   - 完成注册流程

4. **登录系统**
   - http://localhost:3000/login
   - 使用注册的账号登录

---

## 🎉 完成！

一切就绪后，你可以：
- ✅ 使用邀请码注册新用户
- ✅ 登录系统体验所有功能
- ✅ 浏览视频、图文、作业等板块
- ✅ 查看"联盟导演LOL"等新添加的分类

需要帮助？查看：
- 完整文档：`SETUP.md`
- 后端文档：`backend/README.md`
- 前端文档：`frontend/DEPLOYMENT.md`
