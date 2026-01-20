"use client";

import { useState, useEffect } from "react";
import Link from "next/link";

interface User {
  id: number;
  username: string;
  email: string;
  nickname?: string;
  role: string;
  level: number;
  points: number;
  experience: number;
  is_active: boolean;
  created_at: string;
}

export default function AdminUsersPage() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState({
    search: "",
    role: "all",
    status: "all",
  });

  useEffect(() => {
    // TODO: 从 API 获取数据
    setLoading(false);
  }, [filter]);

  const roleOptions = [
    { value: "all", label: "全部角色" },
    { value: "USER", label: "普通用户" },
    { value: "SENIOR", label: "高级用户" },
    { value: "ADMIN", label: "管理员" },
    { value: "SUPER_ADMIN", label: "超级管理员" },
  ];

  const statusOptions = [
    { value: "all", label: "全部状态" },
    { value: "active", label: "正常" },
    { value: "banned", label: "已封禁" },
  ];

  const getRoleBadge = (role: string) => {
    const roleMap: Record<string, { label: string; color: string }> = {
      USER: { label: "用户", color: "bg-gray-100 text-gray-700" },
      SENIOR: { label: "高级", color: "bg-blue-100 text-blue-700" },
      ADMIN: { label: "管理", color: "bg-purple-100 text-purple-700" },
      SUPER_ADMIN: { label: "超管", color: "bg-red-100 text-red-700" },
    };
    const config = roleMap[role] || roleMap.USER;
    return (
      <span className={`px-2 py-1 text-xs rounded ${config.color}`}>
        {config.label}
      </span>
    );
  };

  return (
    <div>
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          用户管理
        </h1>
      </div>

      {/* 筛选器 */}
      <div className="bg-white dark:bg-gray-800 rounded-lg p-4 mb-6">
        <div className="flex flex-wrap gap-4">
          <div className="flex-1 min-w-[200px]">
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              搜索用户
            </label>
            <input
              type="text"
              value={filter.search}
              onChange={(e) => setFilter({ ...filter, search: e.target.value })}
              placeholder="搜索用户名、邮箱或昵称"
              className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              角色
            </label>
            <select
              value={filter.role}
              onChange={(e) => setFilter({ ...filter, role: e.target.value })}
              className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
            >
              {roleOptions.map((role) => (
                <option key={role.value} value={role.value}>
                  {role.label}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              状态
            </label>
            <select
              value={filter.status}
              onChange={(e) => setFilter({ ...filter, status: e.target.value })}
              className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
            >
              {statusOptions.map((status) => (
                <option key={status.value} value={status.value}>
                  {status.label}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {/* 用户列表 */}
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm overflow-hidden">
        {loading ? (
          <div className="p-12 text-center">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-purple-600"></div>
            <p className="mt-4 text-gray-600">加载中...</p>
          </div>
        ) : users.length === 0 ? (
          <div className="p-12 text-center text-gray-500">
            <p className="text-lg mb-2">暂无用户</p>
            <p className="text-sm">请先初始化数据库并完成用户注册</p>
          </div>
        ) : (
          <table className="w-full">
            <thead className="bg-gray-50 dark:bg-gray-700 border-b border-gray-200 dark:border-gray-600">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  用户
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  角色
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  等级
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  积分
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  状态
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  注册时间
                </th>
                <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  操作
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
              {users.map((user) => (
                <tr key={user.id}>
                  <td className="px-6 py-4">
                    <div>
                      <div className="text-sm font-medium text-gray-900 dark:text-white">
                        {user.nickname || user.username}
                      </div>
                      <div className="text-sm text-gray-500">
                        {user.email}
                      </div>
                    </div>
                  </td>
                  <td className="px-6 py-4">
                    {getRoleBadge(user.role)}
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">
                    Lv.{user.level}
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">
                    {user.points}
                  </td>
                  <td className="px-6 py-4">
                    <span className={`px-2 py-1 text-xs rounded ${
                      user.is_active
                        ? "bg-green-100 text-green-700"
                        : "bg-red-100 text-red-700"
                    }`}>
                      {user.is_active ? "正常" : "已封禁"}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">
                    {new Date(user.created_at).toLocaleDateString()}
                  </td>
                  <td className="px-6 py-4 text-right text-sm space-x-2">
                    <Link
                      href={`/admin/users/${user.id}`}
                      className="text-purple-600 hover:text-purple-800"
                    >
                      查看
                    </Link>
                    <button className="text-blue-600 hover:text-blue-800">
                      编辑
                    </button>
                    {user.is_active ? (
                      <button className="text-red-600 hover:text-red-800">
                        封禁
                      </button>
                    ) : (
                      <button className="text-green-600 hover:text-green-800">
                        解封
                      </button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      {/* 统计信息 */}
      <div className="mt-6 grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-white dark:bg-gray-800 rounded-lg p-4 shadow-sm">
          <p className="text-sm text-gray-600 dark:text-gray-400">总用户数</p>
          <p className="mt-1 text-2xl font-bold text-gray-900 dark:text-white">0</p>
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg p-4 shadow-sm">
          <p className="text-sm text-gray-600 dark:text-gray-400">今日新增</p>
          <p className="mt-1 text-2xl font-bold text-gray-900 dark:text-white">0</p>
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg p-4 shadow-sm">
          <p className="text-sm text-gray-600 dark:text-gray-400">活跃用户</p>
          <p className="mt-1 text-2xl font-bold text-gray-900 dark:text-white">0</p>
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg p-4 shadow-sm">
          <p className="text-sm text-gray-600 dark:text-gray-400">封禁用户</p>
          <p className="mt-1 text-2xl font-bold text-gray-900 dark:text-white">0</p>
        </div>
      </div>
    </div>
  );
}
