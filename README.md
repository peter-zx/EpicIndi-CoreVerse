# AIGC散修学习平台

**Slogan**: aigc散修_竹相左边，只分享验证可行的前沿技术

一个基于 Next.js + FastAPI 的现代化学习社区平台，专注于AI、设计、开发等前沿技术的分享与学习。

## 技术栈

### 前端
- **框架**: Next.js 16 (App Router)
- **语言**: TypeScript
- **样式**: Tailwind CSS
- **状态管理**: React Context API

### 后端
- **框架**: FastAPI
- **语言**: Python 3.10+
- **数据库**: PostgreSQL 14+
- **ORM**: SQLAlchemy (异步)
- **认证**: JWT
- **迁移**: Alembic

### 存储
- **对象存储**: 阿里云OSS
- **视频**: OSS + B站嵌入
- **缓存**: Redis (可选)

## 核心功能

✅ **已实现**
- 用户认证系统（邀请码机制）
- JWT Token 认证
- 用户等级系统（8个等级）
- 积分系统基础
- 首页展示框架
- 所有功能页面骨架

⏳ **开发中**
- 内容管理（视频/图文/播客）
- 工具箱系统
- 论坛发帖评论
- 作业系统
- 悬赏任务
- 支付系统

## 快速开始

### 环境要求
- Node.js 18+
- Python 3.10+
- PostgreSQL 14+

### 1. 克隆项目
```bash
git clone <repository-url>
cd EpicIndi-CoreVerse
```

### 2. 启动后端

详细步骤见 [backend/README.md](./backend/README.md)

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# 编辑 .env 配置数据库
python scripts/init_db.py
uvicorn app.main:app --reload
```

### 3. 启动前端

详细步骤见 [frontend/DEPLOYMENT.md](./frontend/DEPLOYMENT.md)

```bash
cd frontend
npm install
cp .env.local.example .env.local
npm run dev
```

### 4. 访问应用
- 前端: http://localhost:3000
- 后端API: http://localhost:8000/api/v1/docs

### 5. 默认账号
- 管理员: `admin` / `admin123456`
- 邀请码在初始化脚本输出中

## 项目结构

```
EpicIndi-CoreVerse/
├── frontend/              # Next.js 前端
│   ├── src/
│   │   ├── app/          # 页面路由
│   │   ├── components/   # 组件
│   │   ├── contexts/     # 状态管理
│   │   ├── lib/          # 工具函数
│   │   └── types/        # 类型定义
│   └── public/           # 静态资源
│
├── backend/              # FastAPI 后端
│   ├── app/
│   │   ├── api/         # API路由
│   │   ├── core/        # 核心配置
│   │   ├── models/      # 数据库模型
│   │   ├── schemas/     # Pydantic模型
│   │   └── services/    # 业务逻辑
│   ├── alembic/         # 数据库迁移
│   └── scripts/         # 工具脚本
│
└── docs/                # 文档
```

## 数据库模型

- **用户系统**: User, UserLevel
- **内容管理**: Content, Category
- **论坛**: Post, Comment, ForumCategory
- **工具箱**: Tool
- **作业**: Homework, HomeworkSubmission, HomeworkReview
- **积分**: PointRecord, PaymentRecord
- **任务**: Task, TaskApplication
- **其他**: Partner, SiteConfig

## 核心特性

### 邀请制注册
- 新用户必须使用邀请码注册
- 每个用户初始5个邀请配额
- 成功邀请后配额-1

### 等级系统
8个修仙等级，从"见习散修"到"大乘散修"：
- 基于经验值自动升级
- 不同等级有不同权限
- 高等级可批阅作业、发布任务

### 积分系统
- 注册奖励100积分
- 日常活动获取积分
- 消费积分解锁内容/工具
- 支持充值购买

## 开发指南

### 添加新功能
1. 后端：创建模型 → 编写Schema → 实现Service → 添加API
2. 前端：定义类型 → 编写API调用 → 创建组件 → 添加路由

### 数据库迁移
```bash
cd backend
alembic revision --autogenerate -m "描述"
alembic upgrade head
```

### 代码规范
- 后端遵循 PEP 8
- 前端使用 ESLint + TypeScript
- 提交前运行 lint 检查

## 部署

### 开发环境
- 前端: `npm run dev`
- 后端: `uvicorn app.main:app --reload`

### 生产环境
- 前端: Vercel / Nginx
- 后端: Gunicorn + Nginx
- 数据库: PostgreSQL (云服务)
- 存储: 阿里云OSS

详细部署文档：
- [后端部署](./backend/README.md)
- [前端部署](./frontend/DEPLOYMENT.md)

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

[待定]

## 联系方式

- 作者: 竹相左边
- Slogan: 只分享验证可行的前沿技术

---

**当前版本**: v0.1.0 (开发中)
**最后更新**: 2026-01-17
