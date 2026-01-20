"use client";

import { useState, useEffect } from "react";
import Link from "next/link";

interface InviteCode {
  code: string;
  owner: string;
  remaining_quota: number;
  used_count: number;
  created_at: string;
}

export default function AdminInviteCodesPage() {
  const [inviteCodes, setInviteCodes] = useState<InviteCode[]>([]);
  const [loading, setLoading] = useState(true);
  const [showGenerateModal, setShowGenerateModal] = useState(false);
  const [generateForm, setGenerateForm] = useState({
    count: 1,
    quota: 50,
  });

  useEffect(() => {
    // TODO: 从 API 获取数据
    setLoading(false);
  }, []);

  const handleGenerate = async () => {
    // TODO: 调用 API 生成邀请码
    alert(`将生成 ${generateForm.count} 个邀请码，每个配额 ${generateForm.quota}`);
    setShowGenerateModal(false);
  };

  return (
    <div>
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          邀请码管理
        </h1>
        <button
          onClick={() => setShowGenerateModal(true)}
          className="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors"
        >
          ➕ 生成邀请码
        </button>
      </div>

      {/* 统计卡片 */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
          <p className="text-sm text-gray-600 dark:text-gray-400">总邀请码数</p>
          <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">0</p>
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
          <p className="text-sm text-gray-600 dark:text-gray-400">已使用</p>
          <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">0</p>
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
          <p className="text-sm text-gray-600 dark:text-gray-400">剩余配额</p>
          <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white">0</p>
        </div>
      </div>

      {/* 邀请码列表 */}
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm overflow-hidden">
        {loading ? (
          <div className="p-12 text-center">
            <div className="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-purple-600"></div>
            <p className="mt-4 text-gray-600">加载中...</p>
          </div>
        ) : inviteCodes.length === 0 ? (
          <div className="p-12 text-center text-gray-500">
            <p className="text-lg mb-2">暂无邀请码</p>
            <p className="text-sm">点击右上角"生成邀请码"按钮创建</p>
          </div>
        ) : (
          <table className="w-full">
            <thead className="bg-gray-50 dark:bg-gray-700 border-b border-gray-200 dark:border-gray-600">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  邀请码
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  所有者
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  已使用
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  剩余配额
                </th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  创建时间
                </th>
                <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 dark:text-gray-400 uppercase">
                  操作
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
              {inviteCodes.map((code) => (
                <tr key={code.code}>
                  <td className="px-6 py-4">
                    <code className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded text-sm font-mono">
                      {code.code}
                    </code>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">
                    {code.owner}
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">
                    {code.used_count}
                  </td>
                  <td className="px-6 py-4">
                    <span className={`px-2 py-1 text-xs rounded ${
                      code.remaining_quota > 0
                        ? "bg-green-100 text-green-700"
                        : "bg-gray-100 text-gray-700"
                    }`}>
                      {code.remaining_quota}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-sm text-gray-600 dark:text-gray-400">
                    {new Date(code.created_at).toLocaleDateString()}
                  </td>
                  <td className="px-6 py-4 text-right text-sm space-x-2">
                    <button className="text-purple-600 hover:text-purple-800">
                      查看使用记录
                    </button>
                    <button className="text-blue-600 hover:text-blue-800">
                      调整配额
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      {/* 生成邀请码模态框 */}
      {showGenerateModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 max-w-md w-full mx-4">
            <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-4">
              生成邀请码
            </h2>
            
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  生成数量
                </label>
                <input
                  type="number"
                  min="1"
                  max="100"
                  value={generateForm.count}
                  onChange={(e) => setGenerateForm({ ...generateForm, count: parseInt(e.target.value) })}
                  className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                  每个邀请码配额
                </label>
                <input
                  type="number"
                  min="1"
                  max="1000"
                  value={generateForm.quota}
                  onChange={(e) => setGenerateForm({ ...generateForm, quota: parseInt(e.target.value) })}
                  className="w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
                <p className="mt-1 text-xs text-gray-500">
                  每个邀请码可邀请的用户数量
                </p>
              </div>
            </div>

            <div className="mt-6 flex justify-end space-x-3">
              <button
                onClick={() => setShowGenerateModal(false)}
                className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700"
              >
                取消
              </button>
              <button
                onClick={handleGenerate}
                className="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700"
              >
                生成
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
