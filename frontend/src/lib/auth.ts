import { get, post, postForm, put } from '@/lib/api';
import type {
  User,
  UserProfile,
  UserPublic,
  RegisterData,
  Token,
  InviteCodeInfo,
  InviteCodeValidation,
  ApiResponse,
  ApiListResponse,
} from '@/types/user';

/**
 * 用户注册
 */
export async function register(data: RegisterData): Promise<ApiResponse<User>> {
  return post<ApiResponse<User>>('/auth/register', data);
}

/**
 * 用户登录
 */
export async function login(username: string, password: string): Promise<Token> {
  return postForm<Token>('/auth/login', { username, password });
}

/**
 * 验证邀请码
 */
export async function validateInviteCode(inviteCode: string): Promise<InviteCodeValidation> {
  return post<InviteCodeValidation>('/auth/validate-invite-code', {
    invite_code: inviteCode,
  });
}

/**
 * 获取当前用户信息
 */
export async function getCurrentUser(): Promise<ApiResponse<UserProfile>> {
  return get<ApiResponse<UserProfile>>('/users/me');
}

/**
 * 更新当前用户信息
 */
export async function updateCurrentUser(data: {
  nickname?: string;
  avatar?: string;
  bio?: string;
  phone?: string;
}): Promise<ApiResponse<User>> {
  return put<ApiResponse<User>>('/users/me', data);
}

/**
 * 获取我的积分信息
 */
export async function getMyPoints(): Promise<ApiResponse<{
  points: number;
  total_earned: number;
  level: number;
  experience: number;
}>> {
  return get('/users/me/points');
}

/**
 * 获取我的邀请码信息
 */
export async function getMyInviteCode(): Promise<ApiResponse<InviteCodeInfo>> {
  return get<ApiResponse<InviteCodeInfo>>('/users/me/invite-code');
}

/**
 * 获取我邀请的用户列表
 */
export async function getMyInvitedUsers(): Promise<ApiListResponse<UserPublic>> {
  return get<ApiListResponse<UserPublic>>('/users/me/invited-users');
}

/**
 * 获取用户排行榜
 */
export async function getLeaderboard(limit = 10): Promise<ApiListResponse<UserPublic>> {
  return get<ApiListResponse<UserPublic>>(`/users/leaderboard?limit=${limit}`);
}

/**
 * 获取用户公开信息
 */
export async function getUserProfile(userId: number): Promise<ApiResponse<UserPublic>> {
  return get<ApiResponse<UserPublic>>(`/users/${userId}`);
}
