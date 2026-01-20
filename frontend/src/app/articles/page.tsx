export default function ArticlesPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">图文教程</h1>
        <p className="mt-2 text-gray-600 dark:text-gray-400">
          深度技术文章，详细图文讲解
        </p>
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

      {/* 文章列表占位 */}
      <div className="space-y-6">
        {[1, 2, 3, 4, 5].map((i) => (
          <div key={i} className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm">
            <h3 className="text-xl font-medium text-gray-900 dark:text-white">文章标题占位 #{i}</h3>
            <p className="mt-2 text-gray-600 dark:text-gray-400">文章摘要内容占位...</p>
            <div className="mt-4 text-sm text-gray-500">0 次阅读 | 0 评论</div>
          </div>
        ))}
      </div>
    </div>
  );
}
