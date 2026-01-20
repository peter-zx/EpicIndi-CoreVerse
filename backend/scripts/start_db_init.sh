#!/bin/bash
# AIGC散修学习平台 - 数据库初始化脚本 (Linux/macOS)

echo "============================================================"
echo "AIGC散修学习平台 - 数据库初始化脚本"
echo "============================================================"
echo ""
echo "此脚本将完成以下操作："
echo "1. 检查 PostgreSQL 服务状态"
echo "2. 创建数据库（如果不存在）"
echo "3. 运行初始化脚本（创建表、生成邀请码）"
echo ""

echo "============================================================"
echo "步骤 1/3: 检查 PostgreSQL 服务状态"
echo "============================================================"
echo ""

# 检查 PostgreSQL 是否运行
if command -v pg_isready &> /dev/null; then
    if pg_isready -q; then
        echo "[成功] PostgreSQL 服务正在运行"
    else
        echo "[错误] PostgreSQL 服务未运行"
        echo ""
        echo "请先启动 PostgreSQL 服务："
        echo "  macOS: brew services start postgresql@14"
        echo "  Linux: sudo systemctl start postgresql"
        echo ""
        exit 1
    fi
else
    echo "[警告] 无法检测 PostgreSQL 状态，尝试继续..."
fi
echo ""

echo "============================================================"
echo "步骤 2/3: 创建数据库"
echo "============================================================"
echo ""

# 创建数据库
createdb -U postgres epicindi_coreverse 2>/dev/null
if [ $? -eq 0 ]; then
    echo "[成功] 数据库创建成功"
else
    echo "[提示] 数据库可能已存在，继续执行..."
fi
echo ""

echo "============================================================"
echo "步骤 3/3: 运行数据库初始化脚本"
echo "============================================================"
echo ""
echo "正在创建表结构、等级配置、分类..."
echo "正在生成 10 个初始邀请码..."
echo ""

# 运行初始化脚本
python3 scripts/init_db.py
if [ $? -ne 0 ]; then
    echo ""
    echo "[错误] 数据库初始化失败"
    echo ""
    echo "可能的原因："
    echo "1. PostgreSQL 密码不是 'postgres'"
    echo "2. 数据库连接配置错误"
    echo "3. Python 依赖未安装完整"
    echo ""
    echo "请检查 backend/.env 文件中的数据库配置"
    echo ""
    exit 1
fi

echo ""
echo "============================================================"
echo "初始化完成！"
echo "============================================================"
echo ""
echo "下一步："
echo "1. 启动后端服务器："
echo "   cd backend"
echo "   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"
echo ""
echo "2. 访问前端：http://localhost:3000/register"
echo "3. 使用上面显示的邀请码进行注册"
echo ""
