"use client";

import { useAuth } from "@/contexts/AuthContext";

export default function AdminDashboard() {
  const { user } = useAuth();

  const stats = [
    { label: "总用户数", value: "0", icon: "👥", color: "bg-blue-500" },
    { label: "内容总数", value: "0", icon: "🎬", color: "bg-green-500" },
    { label: "作业总数", value: "0", icon: "📝", color: "bg-yellow-500" },
    { label: "待审核", value: "0", icon: "⏳", color: "bg-red-500" },
  ];

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
          欢迎回来，{user?.nickname || user?.username}
        </h1>
        <p className="mt-2 text-gray-600 dark:text-gray-400">
          这是你的管理后台仪表盘
        </p>
      </div>

      {/* 统计卡片 */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {stats.map((stat) => (
          <div
            key={stat.label}
            className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm"
          >
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-600 dark:text-gray-400">
                  {stat.label}
                </p>
                <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">
                  {stat.value}
                </p>
              </div>
              <div className={`${stat.color} p-3 rounded-lg text-white text-2xl`}>
                {stat.icon}
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* 快速操作 */}
      <div className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm mb-8">
        <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-4">
          快速操作
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <QuickAction
            href="/admin/contents/new"
            icon="➕"
            title="发布内容"
            description="发布新的视频、图文或播客"
          />
          <QuickAction
            href="/admin/homeworks/new"
            icon="📝"
            title="发布作业"
            description="创建新的作业任务"
          />
          <QuickAction
            href="/admin/invite-codes"
            icon="🎫"
            title="生成邀请码"
            description="创建新的用户邀请码"
          />
        </div>
      </div>

      {/* 最近活动 */}
      <div className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm">
        <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-4">
          最近活动
        </h2>
        <div className="space-y-4">
          <div className="text-center py-8 text-gray-500">
            暂无数据，请先初始化数据库
          </div>
        </div>
      </div>
    </div>
  );
}

function QuickAction({
  href,
  icon,
  title,
  description,
}: {
  href: string;
  icon: string;
  title: string;
  description: string;
}) {
  return (
    <a
      href={href}
      className="block p-4 border-2 border-gray-200 dark:border-gray-700 rounded-lg hover:border-purple-500 dark:hover:border-purple-500 transition-colors"
    >
      <div className="text-3xl mb-2">{icon}</div>
      <h3 className="font-medium text-gray-900 dark:text-white">{title}</h3>
      <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
        {description}
      </p>
    </a>
  );
}
