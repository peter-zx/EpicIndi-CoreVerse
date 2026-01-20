export default function HomeworkPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">作业练习</h1>
        <p className="mt-2 text-gray-600 dark:text-gray-400">
          实践出真知，完成作业获得积分奖励
        </p>
      </div>

      {/* 分类筛选 */}
      <div className="flex flex-wrap gap-2 mb-8">
        {["全部", "联盟导演LOL", "AI绘画", "视频剪辑", "编程实战", "设计练习"].map((cat) => (
          <button
            key={cat}
            className="px-4 py-2 bg-white dark:bg-gray-800 rounded-full text-sm hover:bg-purple-100 dark:hover:bg-purple-900 transition-colors"
          >
            {cat}
          </button>
        ))}
      </div>

      {/* 作业列表占位 */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {[1, 2, 3, 4].map((i) => (
          <div key={i} className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm">
            <div className="flex items-start justify-between">
              <div>
                <span className="px-2 py-1 bg-purple-100 text-purple-700 text-xs rounded">进行中</span>
                <h3 className="mt-3 font-medium text-gray-900 dark:text-white">
                  作业标题占位 #{i}
                </h3>
                <p className="mt-2 text-sm text-gray-500">作业描述占位...</p>
              </div>
            </div>
            <div className="mt-4 pt-4 border-t border-gray-100 dark:border-gray-700 flex items-center justify-between">
              <div className="text-sm text-gray-500">
                <span>0 人已提交</span>
                <span className="mx-2">|</span>
                <span>截止: 7天后</span>
              </div>
              <div className="text-purple-600 font-medium">+30 积分</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
