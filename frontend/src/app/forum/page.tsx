import Link from "next/link";

export default function ForumPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="flex items-center justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">社区论坛</h1>
          <p className="mt-2 text-gray-600 dark:text-gray-400">
            交流学习心得，分享技术见解
          </p>
        </div>
        <Link
          href="/forum/new"
          className="px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700"
        >
          发帖
        </Link>
      </div>

      {/* 分类标签 */}
      <div className="flex flex-wrap gap-2 mb-8">
        {["全部", "技术讨论", "问答求助", "作品分享", "资源分享", "闲聊灌水"].map((cat) => (
          <button
            key={cat}
            className="px-4 py-2 bg-white dark:bg-gray-800 rounded-full text-sm hover:bg-purple-100 dark:hover:bg-purple-900 transition-colors"
          >
            {cat}
          </button>
        ))}
      </div>

      {/* 帖子列表占位 */}
      <div className="space-y-4">
        {[1, 2, 3, 4, 5].map((i) => (
          <div key={i} className="bg-white dark:bg-gray-800 rounded-xl p-5 shadow-sm">
            <div className="flex items-start space-x-4">
              <div className="w-10 h-10 rounded-full bg-gradient-to-br from-purple-400 to-blue-400 flex-shrink-0" />
              <div className="flex-1">
                <h3 className="font-medium text-gray-900 dark:text-white hover:text-purple-600 cursor-pointer">
                  帖子标题占位 #{i}
                </h3>
                <p className="mt-1 text-sm text-gray-500 line-clamp-2">
                  帖子内容预览占位...
                </p>
                <div className="mt-3 flex items-center space-x-4 text-xs text-gray-400">
                  <span>用户名</span>
                  <span>0 回复</span>
                  <span>0 浏览</span>
                  <span>1小时前</span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
