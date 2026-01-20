"use client";

import { useState, useEffect } from "react";
import Link from "next/link";

interface Homework {
  id: number;
  title: string;
  description: string;
  status: string;
  submission_count: number;
  base_points: number;
  deadline?: string;
  created_at: string;
}

export default function AdminHomeworksPage() {
  const [homeworks, setHomeworks] = useState<Homework[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // TODO: 从 API 获取数据
    setLoading(false);
  }, []);

  return (
    <div>
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          作业管理
        </h1>
        <Link
          href="/admin/homeworks/new"
          className="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors"
        >
          ➕ 发布新作业
        </Link>
      </div>

      {/* 统计卡片 */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-6">
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
          <p className="text-sm text-gray-600 dark:text-gray-400">总作业数</p>
          <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">0</p>
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
          <p className="text-sm text-gray-600 dark:text-gray-400">总提交数</p>
          <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">0</p>
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
          <p className="text-sm text-gray-600 dark:text-gray-400">待批阅</p>
          <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">0</p>
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
          <p className="text-sm text-gray-600 dark:text-gray-400">已批阅</p>
          <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">0</p>
        </div>
      </div>

      {/* 作业列表 */}
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm overflow-hidden">
        {loading ? (
          <div className="p-12 text-center">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-purple-600"></div>
            <p className="mt-4 text-gray-600">加载中...</p>
          </div>
        ) : homeworks.length === 0 ? (
          <div className="p-12 text-center text-gray-500">
            <p className="text-lg mb-2">暂无作业</p>
            <p className="text-sm">点击右上角"发布新作业"按钮开始创建</p>
          </div>
        ) : (
          <table className="w-full">
            <thead className="bg-gray-50 dark:bg-gray-700 border-b border-gray-200 dark:border-gray-600">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  标题
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  状态
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  提交数
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  积分奖励
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  截止时间
                </th>
                <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  操作
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
              {homeworks.map((homework) => (
                <tr key={homework.id}>
                  <td className="px-6 py-4">
                    <div className="text-sm font-medium text-gray-900 dark:text-white">
                      {homework.title}
                    </div>
                    <div className="text-sm text-gray-500 mt-1 line-clamp-1">
                      {homework.description}
                    </div>
                  </td>
                  <td className="px-6 py-4">
                    <span className="px-2 py-1 text-xs rounded bg-green-100 text-green-700">
                      {homework.status}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">
                    {homework.submission_count}
                  </td>
                  <td className="px-6 py-4 text-sm text-purple-600 font-medium">
                    +{homework.base_points}
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">
                    {homework.deadline 
                      ? new Date(homework.deadline).toLocaleDateString()
                      : "无期限"
                    }
                  </td>
                  <td className="px-6 py-4 text-right text-sm space-x-2">
                    <Link
                      href={`/admin/homeworks/${homework.id}/submissions`}
                      className="text-purple-600 hover:text-purple-800"
                    >
                      查看提交
                    </Link>
                    <Link
                      href={`/admin/homeworks/${homework.id}/edit`}
                      className="text-blue-600 hover:text-blue-800"
                    >
                      编辑
                    </Link>
                    <button className="text-red-600 hover:text-red-800">
                      删除
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
