"use client";

import { useAuth } from "@/contexts/AuthContext";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import Link from "next/link";

export default function AdminLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const { user, isLoading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    // 检查用户是否是管理员
    if (!isLoading && (!user || (user.role !== "ADMIN" && user.role !== "SUPER_ADMIN"))) {
      router.push("/login?redirect=/admin");
    }
  }, [user, isLoading, router]);

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="inline-block animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-purple-600"></div>
          <p className="mt-4 text-gray-600">加载中...</p>
        </div>
      </div>
    );
  }

  if (!user || (user.role !== "ADMIN" && user.role !== "SUPER_ADMIN")) {
    return null;
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      {/* 顶部导航栏 */}
      <header className="bg-white dark:bg-gray-800 shadow-sm border-b border-gray-200 dark:border-gray-700">
        <div className="flex items-center justify-between px-6 py-4">
          <div className="flex items-center space-x-4">
            <Link href="/admin" className="text-xl font-bold text-purple-600">
              AIGC散修 管理后台
            </Link>
          </div>
          <div className="flex items-center space-x-4">
            <span className="text-sm text-gray-600 dark:text-gray-400">
              {user.nickname || user.username}
            </span>
            <span className="px-2 py-1 text-xs bg-purple-100 text-purple-700 rounded">
              {user.role === "SUPER_ADMIN" ? "超级管理员" : "管理员"}
            </span>
            <Link
              href="/"
              className="text-sm text-gray-600 hover:text-purple-600 dark:text-gray-400"
            >
              返回前台
            </Link>
          </div>
        </div>
      </header>

      <div className="flex">
        {/* 侧边栏 */}
        <aside className="w-64 bg-white dark:bg-gray-800 min-h-[calc(100vh-73px)] border-r border-gray-200 dark:border-gray-700">
          <nav className="p-4 space-y-1">
            <NavLink href="/admin" icon="📊">
              仪表盘
            </NavLink>
            
            <div className="pt-4 pb-2">
              <p className="px-4 text-xs font-semibold text-gray-400 uppercase">内容管理</p>
            </div>
            <NavLink href="/admin/contents" icon="🎬">
              内容管理
            </NavLink>
            <NavLink href="/admin/categories" icon="📁">
              分类管理
            </NavLink>
            
            <div className="pt-4 pb-2">
              <p className="px-4 text-xs font-semibold text-gray-400 uppercase">用户管理</p>
            </div>
            <NavLink href="/admin/users" icon="👥">
              用户列表
            </NavLink>
            <NavLink href="/admin/invite-codes" icon="🎫">
              邀请码管理
            </NavLink>
            
            <div className="pt-4 pb-2">
              <p className="px-4 text-xs font-semibold text-gray-400 uppercase">社区管理</p>
            </div>
            <NavLink href="/admin/homeworks" icon="📝">
              作业管理
            </NavLink>
            <NavLink href="/admin/forum" icon="💬">
              论坛管理
            </NavLink>
            <NavLink href="/admin/tasks" icon="💼">
              任务管理
            </NavLink>
            
            <div className="pt-4 pb-2">
              <p className="px-4 text-xs font-semibold text-gray-400 uppercase">系统设置</p>
            </div>
            <NavLink href="/admin/settings" icon="⚙️">
              系统设置
            </NavLink>
          </nav>
        </aside>

        {/* 主内容区 */}
        <main className="flex-1 p-8">
          {children}
        </main>
      </div>
    </div>
  );
}

function NavLink({ href, icon, children }: { href: string; icon: string; children: React.ReactNode }) {
  return (
    <Link
      href={href}
      className="flex items-center space-x-3 px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-purple-50 dark:hover:bg-gray-700 rounded-lg transition-colors"
    >
      <span>{icon}</span>
      <span>{children}</span>
    </Link>
  );
}
