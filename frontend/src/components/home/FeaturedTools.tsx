import Link from "next/link";

// Mock data
const mockTools = [
  {
    id: 1,
    name: "字幕识别工具",
    description: "快速识别视频字幕，支持多种格式导出",
    icon: "CC",
    downloads: 3200,
    isFree: true,
  },
  {
    id: 2,
    name: "免费音乐播放器",
    description: "简洁好用的本地音乐播放器",
    icon: "MU",
    downloads: 2800,
    isFree: true,
  },
  {
    id: 3,
    name: "数据清洗工具",
    description: "一键清洗表格数据，去重去空",
    icon: "DC",
    downloads: 1900,
    isFree: false,
    points: 50,
  },
  {
    id: 4,
    name: "图片批量处理",
    description: "批量压缩、格式转换、水印添加",
    icon: "IMG",
    downloads: 2100,
    isFree: false,
    points: 30,
  },
];

export default function FeaturedTools() {
  return (
    <section>
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
          热门工具
        </h2>
        <Link
          href="/tools"
          className="text-purple-600 hover:text-purple-700 text-sm font-medium"
        >
          查看全部 &rarr;
        </Link>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {mockTools.map((tool) => (
          <Link
            key={tool.id}
            href={`/tools/${tool.id}`}
            className="flex items-start space-x-4 p-4 bg-white dark:bg-gray-800 rounded-xl shadow-sm hover:shadow-md transition-shadow"
          >
            {/* Icon */}
            <div className="w-12 h-12 rounded-lg bg-gradient-to-br from-purple-500 to-blue-500 flex items-center justify-center text-white font-bold flex-shrink-0">
              {tool.icon}
            </div>

            {/* Info */}
            <div className="flex-1 min-w-0">
              <div className="flex items-center space-x-2">
                <h3 className="font-medium text-gray-900 dark:text-white truncate">
                  {tool.name}
                </h3>
                {tool.isFree ? (
                  <span className="px-2 py-0.5 bg-green-100 text-green-700 text-xs rounded-full">
                    免费
                  </span>
                ) : (
                  <span className="px-2 py-0.5 bg-purple-100 text-purple-700 text-xs rounded-full">
                    {tool.points}积分
                  </span>
                )}
              </div>
              <p className="mt-1 text-sm text-gray-500 dark:text-gray-400 line-clamp-1">
                {tool.description}
              </p>
              <p className="mt-1 text-xs text-gray-400">
                {tool.downloads.toLocaleString()} 次下载
              </p>
            </div>
          </Link>
        ))}
      </div>
    </section>
  );
}
