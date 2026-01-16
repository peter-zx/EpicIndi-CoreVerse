export default function PartnersPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div className="text-center mb-12">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">合作伙伴</h1>
        <p className="mt-2 text-gray-600 dark:text-gray-400">
          感谢以下伙伴的支持与合作
        </p>
      </div>

      {/* 赞助商展示 */}
      <div className="mb-16">
        <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-6 text-center">赞助商</h2>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="bg-white dark:bg-gray-800 rounded-xl p-8 shadow-sm flex items-center justify-center">
              <span className="text-gray-400">Logo #{i}</span>
            </div>
          ))}
        </div>
      </div>

      {/* 合作方式 */}
      <div className="bg-gradient-to-r from-purple-600 to-blue-600 rounded-2xl p-8 md:p-12 text-white text-center">
        <h2 className="text-2xl font-bold mb-4">成为合作伙伴</h2>
        <p className="mb-6 text-purple-100 max-w-2xl mx-auto">
          如果您对我们的平台感兴趣，希望进行商务合作、品牌赞助或技术交流，
          欢迎与我们联系。
        </p>
        <div className="flex flex-wrap justify-center gap-4">
          <a
            href="mailto:contact@example.com"
            className="px-6 py-3 bg-white text-purple-600 rounded-lg font-medium hover:bg-purple-50"
          >
            发送邮件
          </a>
          <button className="px-6 py-3 border border-white/50 rounded-lg font-medium hover:bg-white/10">
            了解更多
          </button>
        </div>
      </div>
    </div>
  );
}
