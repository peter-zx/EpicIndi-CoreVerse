"use client";

import Link from "next/link";
import { useState } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { useAuth } from "@/contexts/AuthContext";
import { validateInviteCode } from "@/lib/auth";

export default function RegisterPage() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { register, isAuthenticated } = useAuth();
  
  const [formData, setFormData] = useState({
    inviteCode: searchParams.get("code") || "",
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const [agreeTerms, setAgreeTerms] = useState(false);
  const [error, setError] = useState("");
  const [inviteStatus, setInviteStatus] = useState<{
    checked: boolean;
    valid: boolean;
    message: string;
    inviterName?: string;
  }>({ checked: false, valid: false, message: "" });
  const [isLoading, setIsLoading] = useState(false);

  // 如果已登录，重定向到首页
  if (isAuthenticated) {
    router.push("/");
    return null;
  }

  // 验证邀请码
  const checkInviteCode = async () => {
    if (!formData.inviteCode || formData.inviteCode.length < 6) {
      setInviteStatus({ checked: false, valid: false, message: "" });
      return;
    }

    try {
      const result = await validateInviteCode(formData.inviteCode);
      setInviteStatus({
        checked: true,
        valid: result.valid,
        message: result.message,
        inviterName: result.inviter?.nickname || result.inviter?.username,
      });
    } catch {
      setInviteStatus({
        checked: true,
        valid: false,
        message: "验证失败，请检查网络连接",
      });
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
    setError("");
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");

    // 验证表单
    if (formData.password !== formData.confirmPassword) {
      setError("两次输入的密码不一致");
      return;
    }

    if (formData.password.length < 8) {
      setError("密码长度至少8位");
      return;
    }

    if (!agreeTerms) {
      setError("请先阅读并同意用户协议和隐私政策");
      return;
    }

    if (!inviteStatus.valid) {
      setError("请输入有效的邀请码");
      return;
    }

    setIsLoading(true);

    try {
      await register({
        username: formData.username,
        email: formData.email,
        password: formData.password,
        invite_code: formData.inviteCode,
      });
      router.push("/");
    } catch (err) {
      setError(err instanceof Error ? err.message : "注册失败，请重试");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-[80vh] flex items-center justify-center py-12 px-4">
      <div className="max-w-md w-full">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">注册</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-400">
            加入AIGC散修，开启学习之旅
          </p>
        </div>

        <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-sm p-8">
          {error && (
            <div className="mb-4 p-3 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg text-red-600 dark:text-red-400 text-sm">
              {error}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                邀请码 <span className="text-red-500">*</span>
              </label>
              <div className="flex space-x-2">
                <input
                  type="text"
                  name="inviteCode"
                  value={formData.inviteCode}
                  onChange={handleChange}
                  onBlur={checkInviteCode}
                  className="flex-1 px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
                  placeholder="请输入邀请码"
                  required
                  disabled={isLoading}
                />
                <button
                  type="button"
                  onClick={checkInviteCode}
                  className="px-4 py-3 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-600"
                  disabled={isLoading}
                >
                  验证
                </button>
              </div>
              {inviteStatus.checked && (
                <p className={`mt-1 text-xs ${inviteStatus.valid ? "text-green-600" : "text-red-500"}`}>
                  {inviteStatus.message}
                  {inviteStatus.valid && inviteStatus.inviterName && (
                    <span className="ml-1">（邀请人：{inviteStatus.inviterName}）</span>
                  )}
                </p>
              )}
              <p className="mt-1 text-xs text-gray-500">需要邀请码才能注册，可向已注册用户索取</p>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                用户名 <span className="text-red-500">*</span>
              </label>
              <input
                type="text"
                name="username"
                value={formData.username}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
                placeholder="3-50字符，字母数字下划线中文"
                required
                minLength={3}
                maxLength={50}
                disabled={isLoading}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                邮箱 <span className="text-red-500">*</span>
              </label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
                placeholder="请输入邮箱"
                required
                disabled={isLoading}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                密码 <span className="text-red-500">*</span>
              </label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
                placeholder="至少8位，包含字母和数字"
                required
                minLength={8}
                disabled={isLoading}
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                确认密码 <span className="text-red-500">*</span>
              </label>
              <input
                type="password"
                name="confirmPassword"
                value={formData.confirmPassword}
                onChange={handleChange}
                className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
                placeholder="请再次输入密码"
                required
                disabled={isLoading}
              />
            </div>

            <div className="flex items-start">
              <input
                type="checkbox"
                checked={agreeTerms}
                onChange={(e) => setAgreeTerms(e.target.checked)}
                className="rounded border-gray-300 mt-1"
                disabled={isLoading}
              />
              <span className="ml-2 text-sm text-gray-600 dark:text-gray-400">
                我已阅读并同意{" "}
                <Link href="/terms" className="text-purple-600 hover:underline">
                  用户协议
                </Link>{" "}
                和{" "}
                <Link href="/privacy" className="text-purple-600 hover:underline">
                  隐私政策
                </Link>
              </span>
            </div>

            <button
              type="submit"
              disabled={isLoading || !inviteStatus.valid}
              className="w-full py-3 bg-purple-600 text-white rounded-lg font-medium hover:bg-purple-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {isLoading ? "注册中..." : "注册"}
            </button>
          </form>

          <div className="mt-6 text-center text-sm text-gray-600 dark:text-gray-400">
            已有账号？{" "}
            <Link href="/login" className="text-purple-600 hover:text-purple-700 font-medium">
              立即登录
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
