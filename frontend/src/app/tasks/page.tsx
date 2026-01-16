import Link from "next/link";

export default function TasksPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">悬赏任务</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-400">
            用积分发布任务，让高手帮你解决问题
          </p>
        </div>
        <Link
          href="/tasks/create"
          className="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700"
        >
          发布任务
        </Link>
      </div>

      {/* 状态筛选 */}
      <div className="flex flex-wrap gap-2 mb-8">
        {["全部", "待揭榜", "进行中", "已完成"].map((status) => (
          <button
            key={status}
            className="px-4 py-2 bg-white dark:bg-gray-800 rounded-full text-sm hover:bg-purple-100 dark:hover:bg-purple-900 transition-colors"
          >
            {status}
          </button>
        ))}
      </div>

      {/* 任务列表占位 */}
      <div className="space-y-4">
        {[1, 2, 3, 4, 5].map((i) => (
          <div key={i} className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm">
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <div className="flex items-center space-x-2">
                  <span className="px-2 py-1 bg-green-100 text-green-700 text-xs rounded">待揭榜</span>
                  <span className="text-xs text-gray-400">3天后截止</span>
                </div>
                <h3 className="mt-3 font-medium text-gray-900 dark:text-white">
                  任务标题占位 #{i}
                </h3>
                <p className="mt-2 text-sm text-gray-500 line-clamp-2">
                  任务描述占位...
                </p>
              </div>
              <div className="ml-6 text-right">
                <div className="text-2xl font-bold text-purple-600">200</div>
                <div className="text-xs text-gray-500">积分悬赏</div>
              </div>
            </div>
            <div className="mt-4 pt-4 border-t border-gray-100 dark:border-gray-700 flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <div className="w-6 h-6 rounded-full bg-gray-200" />
                <span className="text-sm text-gray-600">发布者</span>
              </div>
              <button className="px-4 py-2 bg-purple-600 text-white text-sm rounded-lg hover:bg-purple-700">
                揭榜
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
