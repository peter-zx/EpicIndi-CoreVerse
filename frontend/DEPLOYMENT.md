# AIGC散修学习平台 - 前端部署指南

## 环境要求

- Node.js 18+
- npm 9+

## 快速开始

### 1. 安装依赖

```bash
cd frontend
npm install
```

### 2. 配置环境变量

复制环境变量模板：
```bash
cp .env.local.example .env.local
```

编辑 `.env.local` 文件：
```env
# 后端API地址
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1

# 网站信息
NEXT_PUBLIC_SITE_NAME=AIGC散修
NEXT_PUBLIC_SITE_SLOGAN=只分享验证可行的前沿技术
```

### 3. 启动开发服务器

```bash
npm run dev
```

访问：http://localhost:3000

### 4. 构建生产版本

```bash
npm run build
npm run start
```

## 功能说明

### 已实现功能

✅ 用户认证
- 登录/注册（含邀请码验证）
- JWT Token 管理
- 用户状态管理（AuthContext）

✅ 首页展示
- 作者信息展示
- 热门视频/工具/图文
- 积分排行榜
- 待揭榜任务

✅ 页面骨架
- 视频列表页
- 图文列表页
- 播客列表页
- 工具箱页
- 论坛页
- 作业系统页
- 悬赏任务页
- 合作伙伴页

### 待实现功能

⏳ 内容详情页
⏳ 用户个人中心
⏳ 积分商城
⏳ 管理后台

## 技术栈

- **框架**: Next.js 16 (App Router)
- **语言**: TypeScript
- **样式**: Tailwind CSS
- **状态管理**: React Context
- **HTTP客户端**: Fetch API

## 目录结构

```
frontend/
├── src/
│   ├── app/              # 页面路由
│   │   ├── page.tsx      # 首页
│   │   ├── login/        # 登录页
│   │   ├── register/     # 注册页
│   │   ├── videos/       # 视频页
│   │   ├── articles/     # 图文页
│   │   └── ...
│   ├── components/       # 组件
│   │   ├── layout/       # 布局组件
│   │   ├── home/         # 首页组件
│   │   └── ui/           # UI组件
│   ├── contexts/         # Context状态管理
│   │   └── AuthContext.tsx
│   ├── lib/              # 工具函数
│   │   ├── api.ts        # API请求
│   │   └── auth.ts       # 认证相关
│   └── types/            # TypeScript类型
│       └── user.ts
└── public/               # 静态资源
```

## 开发指南

### 添加新页面

1. 在 `src/app/` 下创建目录
2. 创建 `page.tsx` 文件
3. 导出默认组件

示例：
```tsx
// src/app/profile/page.tsx
export default function ProfilePage() {
  return <div>个人中心</div>
}
```

### 使用认证状态

```tsx
import { useAuth } from '@/contexts/AuthContext';

export default function MyComponent() {
  const { user, isAuthenticated, login, logout } = useAuth();
  
  return (
    <div>
      {isAuthenticated ? (
        <p>欢迎, {user?.nickname}</p>
      ) : (
        <button onClick={() => login('username', 'password')}>
          登录
        </button>
      )}
    </div>
  );
}
```

### API 调用

```tsx
import { get, post } from '@/lib/api';

// GET 请求
const data = await get<ResponseType>('/endpoint');

// POST 请求
const result = await post<ResponseType>('/endpoint', { data });
```

## 生产环境部署

### 使用 Vercel (推荐)

```bash
npm install -g vercel
vercel
```

### 使用 Docker

```dockerfile
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

EXPOSE 3000
CMD ["npm", "run", "start"]
```

### 静态导出

```bash
npm run build
npm run export
```

## 常见问题

### 1. API 连接失败
- 确认后端服务已启动
- 检查 `.env.local` 中的 API URL
- 检查 CORS 配置

### 2. 构建失败
```bash
# 清理缓存
rm -rf .next node_modules package-lock.json
npm install
npm run build
```

### 3. 类型错误
```bash
# 检查类型
npm run type-check
```

## 性能优化建议

1. **图片优化**: 使用 Next.js Image 组件
2. **代码分割**: 使用动态导入
3. **缓存策略**: 配置合适的 Cache-Control
4. **CDN加速**: 静态资源使用 CDN

## 开发注意事项

1. 所有组件使用 TypeScript
2. 遵循 ESLint 规则
3. 使用 Tailwind CSS，避免内联样式
4. API 调用需要错误处理
5. 敏感信息使用环境变量

## 测试账号

使用后端创建的测试账号：
- testuser1 / test123456
- testuser2 / test123456

或使用管理员邀请码注册新账号。
