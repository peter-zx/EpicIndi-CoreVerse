export default function VideosPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">视频教程</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-400">
            从零到一的实战视频教程，手把手带你入门前沿技术
          </p>
        </div>
      </div>

      {/* 分类筛选 */}
      <div className="flex flex-wrap gap-2 mb-8">
        {["全部", "联盟导演LOL", "AI绘画", "机器学习", "Python", "工具开发", "设计"].map((cat) => (
          <button
            key={cat}
            className="px-4 py-2 bg-white dark:bg-gray-800 rounded-full text-sm hover:bg-purple-100 dark:hover:bg-purple-900 transition-colors"
          >
            {cat}
          </button>
        ))}
      </div>

      {/* 视频列表占位 */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {[1, 2, 3, 4, 5, 6].map((i) => (
          <div key={i} className="bg-white dark:bg-gray-800 rounded-xl overflow-hidden shadow-sm">
            <div className="aspect-video bg-gray-200 dark:bg-gray-700 flex items-center justify-center">
              <span className="text-gray-400">视频封面</span>
            </div>
            <div className="p-4">
              <h3 className="font-medium text-gray-900 dark:text-white">视频标题占位</h3>
              <p className="mt-2 text-sm text-gray-500">0 次观看</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
