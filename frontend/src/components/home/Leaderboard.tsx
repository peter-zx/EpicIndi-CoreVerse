import Link from "next/link";

// Mock data
const mockLeaderboard = [
  { rank: 1, username: "AIExplorer", points: 12580, level: 8 },
  { rank: 2, username: "创意小达人", points: 9870, level: 7 },
  { rank: 3, username: "技术宅小明", points: 8650, level: 6 },
  { rank: 4, username: "设计转AI", points: 7420, level: 6 },
  { rank: 5, username: "学习达人", points: 6890, level: 5 },
];

export default function Leaderboard() {
  return (
    <section className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-lg font-bold text-gray-900 dark:text-white">
          积分排行榜
        </h2>
        <Link
          href="/leaderboard"
          className="text-purple-600 hover:text-purple-700 text-sm"
        >
          更多
        </Link>
      </div>

      <div className="space-y-3">
        {mockLeaderboard.map((user) => (
          <div
            key={user.rank}
            className="flex items-center space-x-3 p-2 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
          >
            {/* Rank */}
            <div className={`w-6 h-6 rounded-full flex items-center justify-center text-sm font-bold ${
              user.rank === 1
                ? "bg-yellow-400 text-yellow-900"
                : user.rank === 2
                ? "bg-gray-300 text-gray-700"
                : user.rank === 3
                ? "bg-orange-400 text-orange-900"
                : "bg-gray-100 text-gray-600 dark:bg-gray-600 dark:text-gray-300"
            }`}>
              {user.rank}
            </div>

            {/* Avatar placeholder */}
            <div className="w-8 h-8 rounded-full bg-gradient-to-br from-purple-400 to-blue-400 flex items-center justify-center text-white text-xs font-bold">
              {user.username.charAt(0)}
            </div>

            {/* Info */}
            <div className="flex-1 min-w-0">
              <div className="flex items-center space-x-2">
                <span className="text-sm font-medium text-gray-900 dark:text-white truncate">
                  {user.username}
                </span>
                <span className="px-1.5 py-0.5 bg-purple-100 text-purple-700 text-xs rounded">
                  Lv.{user.level}
                </span>
              </div>
            </div>

            {/* Points */}
            <div className="text-sm font-medium text-purple-600">
              {user.points.toLocaleString()}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
