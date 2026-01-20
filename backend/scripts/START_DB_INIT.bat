@echo off
chcp 65001 >nul
echo ============================================================
echo AIGC散修学习平台 - 数据库初始化脚本
echo ============================================================
echo.
echo 此脚本将完成以下操作：
echo 1. 检查 PostgreSQL 服务状态
echo 2. 创建数据库（如果不存在）
echo 3. 运行初始化脚本（创建表、生成邀请码）
echo 4. 重启后端 API 服务器
echo.
echo ============================================================
echo 步骤 1/4: 检查 PostgreSQL 服务状态
echo ============================================================
echo.

sc query postgresql-x64-14 | findstr "RUNNING" >nul
if errorlevel 1 (
    echo [错误] PostgreSQL 服务未运行
    echo.
    echo 请先启动 PostgreSQL 服务：
    echo 1. 按 Win+R，输入 services.msc
    echo 2. 找到 postgresql-x64-14 服务
    echo 3. 右键 - 启动
    echo.
    pause
    exit /b 1
) else (
    echo [成功] PostgreSQL 服务正在运行
    echo.
)

echo ============================================================
echo 步骤 2/4: 创建数据库
echo ============================================================
echo.

"C:\Program Files\PostgreSQL\14\bin\createdb.exe" -U postgres epicindi_coreverse 2>nul
if errorlevel 1 (
    echo [提示] 数据库可能已存在，继续执行...
) else (
    echo [成功] 数据库创建成功
)
echo.

echo ============================================================
echo 步骤 3/4: 运行数据库初始化脚本
echo ============================================================
echo.
echo 正在创建表结构、等级配置、分类...
echo 正在生成 10 个初始邀请码...
echo.

python scripts\init_db.py
if errorlevel 1 (
    echo.
    echo [错误] 数据库初始化失败
    echo.
    echo 可能的原因：
    echo 1. PostgreSQL 密码不是 'postgres'
    echo 2. 数据库连接配置错误
    echo 3. Python 依赖未安装完整
    echo.
    echo 请检查 backend\.env 文件中的数据库配置
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo 步骤 4/4: 重启后端 API 服务器
echo ============================================================
echo.
echo [提示] 后端服务器需要手动重启
echo.
echo 请在新的命令行窗口运行：
echo   cd backend
echo   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
echo.
echo ============================================================
echo 初始化完成！
echo ============================================================
echo.
echo 下一步：
echo 1. 启动后端服务器（见上方提示）
echo 2. 访问前端：http://localhost:3000/register
echo 3. 使用上面显示的邀请码进行注册
echo.
pause
