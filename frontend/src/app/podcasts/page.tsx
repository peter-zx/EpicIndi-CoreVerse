export default function PodcastsPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">播客</h1>
        <p className="mt-2 text-gray-600 dark:text-gray-400">
          分享见闻观点，聊聊技术圈那些事
        </p>
      </div>

      {/* 播客列表占位 */}
      <div className="space-y-4">
        {[1, 2, 3, 4].map((i) => (
          <div key={i} className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm flex items-center space-x-4">
            <div className="w-20 h-20 bg-gradient-to-br from-purple-400 to-blue-400 rounded-lg flex items-center justify-center">
              <svg className="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 14c1.66 0 3-1.34 3-3V5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3z"/>
                <path d="M17 11c0 2.76-2.24 5-5 5s-5-2.24-5-5H5c0 3.53 2.61 6.43 6 6.92V21h2v-3.08c3.39-.49 6-3.39 6-6.92h-2z"/>
              </svg>
            </div>
            <div className="flex-1">
              <h3 className="font-medium text-gray-900 dark:text-white">播客标题占位 #{i}</h3>
              <p className="text-sm text-gray-500 mt-1">EP.{i} | 30:00</p>
            </div>
            <button className="p-3 bg-purple-600 text-white rounded-full hover:bg-purple-700">
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                <path d="M8 5v14l11-7z"/>
              </svg>
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
