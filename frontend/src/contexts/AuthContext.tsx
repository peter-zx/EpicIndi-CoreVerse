"use client";

import React, { createContext, useContext, useEffect, useState, useCallback } from 'react';
import { getToken, setToken, removeToken } from '@/lib/api';
import { getCurrentUser, login as apiLogin, register as apiRegister } from '@/lib/auth';
import type { UserProfile, RegisterData } from '@/types/user';

interface AuthContextType {
  user: UserProfile | null;
  isLoading: boolean;
  isAuthenticated: boolean;
  login: (username: string, password: string) => Promise<void>;
  register: (data: RegisterData) => Promise<void>;
  logout: () => void;
  refreshUser: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<UserProfile | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  const refreshUser = useCallback(async () => {
    const token = getToken();
    if (!token) {
      setUser(null);
      setIsLoading(false);
      return;
    }

    try {
      const response = await getCurrentUser();
      setUser(response.data);
    } catch (error) {
      console.error('Failed to fetch user:', error);
      removeToken();
      setUser(null);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    refreshUser();
  }, [refreshUser]);

  const login = async (username: string, password: string) => {
    const response = await apiLogin(username, password);
    setToken(response.access_token);
    await refreshUser();
  };

  const register = async (data: RegisterData) => {
    await apiRegister(data);
    // 注册成功后自动登录
    await login(data.username, data.password);
  };

  const logout = () => {
    removeToken();
    setUser(null);
  };

  const value = {
    user,
    isLoading,
    isAuthenticated: !!user,
    login,
    register,
    logout,
    refreshUser,
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}
