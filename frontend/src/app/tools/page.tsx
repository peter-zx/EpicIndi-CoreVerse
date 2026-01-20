export default function ToolsPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">工具箱</h1>
        <p className="mt-2 text-gray-600 dark:text-gray-400">
          实用工具合集，开箱即用，节省你的时间
        </p>
      </div>

      {/* 分类筛选 */}
      <div className="flex flex-wrap gap-2 mb-8">
        {["全部", "AI工具", "视频处理", "音频处理", "数据处理", "设计工具"].map((cat) => (
          <button
            key={cat}
            className="px-4 py-2 bg-white dark:bg-gray-800 rounded-full text-sm hover:bg-purple-100 dark:hover:bg-purple-900 transition-colors"
          >
            {cat}
          </button>
        ))}
      </div>

      {/* 工具列表占位 */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {[1, 2, 3, 4, 5, 6].map((i) => (
          <div key={i} className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm">
            <div className="w-14 h-14 bg-gradient-to-br from-purple-500 to-blue-500 rounded-xl flex items-center justify-center text-white font-bold text-xl mb-4">
              T{i}
            </div>
            <h3 className="font-medium text-gray-900 dark:text-white">工具名称 #{i}</h3>
            <p className="mt-2 text-sm text-gray-500">工具描述占位...</p>
            <div className="mt-4 flex items-center justify-between">
              <span className="text-xs text-gray-400">0 次下载</span>
              <span className="px-2 py-1 bg-green-100 text-green-700 text-xs rounded">免费</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
