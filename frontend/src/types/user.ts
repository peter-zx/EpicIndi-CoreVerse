// 用户相关类型定义

export interface User {
  id: number;
  username: string;
  email: string;
  nickname: string | null;
  avatar: string | null;
  bio: string | null;
  role: 'user' | 'senior' | 'admin' | 'super_admin';
  level: number;
  experience: number;
  points: number;
  total_points_earned: number;
  invite_code: string;
  invite_quota: number;
  is_active: boolean;
  is_verified: boolean;
  created_at: string;
  last_login_at: string | null;
}

export interface UserPublic {
  id: number;
  username: string;
  nickname: string | null;
  avatar: string | null;
  bio: string | null;
  level: number;
  role: string;
  created_at: string;
}

export interface UserProfile extends User {
  invited_count: number;
}

export interface RegisterData {
  username: string;
  email: string;
  password: string;
  invite_code: string;
}

export interface LoginData {
  username: string;
  password: string;
}

export interface Token {
  access_token: string;
  token_type: string;
}

export interface InviteCodeInfo {
  code: string;
  remaining_quota: number;
  invited_users: UserPublic[];
}

export interface InviteCodeValidation {
  valid: boolean;
  message: string;
  inviter: UserPublic | null;
}

// API响应类型
export interface ApiResponse<T> {
  code: number;
  message: string;
  data: T;
}

export interface ApiListResponse<T> {
  code: number;
  message: string;
  data: T[];
  total: number;
  page: number;
  page_size: number;
}
