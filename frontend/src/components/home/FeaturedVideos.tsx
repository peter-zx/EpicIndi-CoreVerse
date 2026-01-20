import Link from "next/link";

// Mock data - 后续从API获取
const mockVideos = [
  {
    id: 1,
    title: "Stable Diffusion 从零开始部署教程",
    cover: "/placeholder-video.jpg",
    duration: "25:30",
    views: 12500,
    category: "AI绘画",
  },
  {
    id: 2,
    title: "ComfyUI 工作流搭建实战",
    cover: "/placeholder-video.jpg",
    duration: "18:45",
    views: 8900,
    category: "AI绘画",
  },
  {
    id: 3,
    title: "YOLOv8 目标检测快速入门",
    cover: "/placeholder-video.jpg",
    duration: "32:10",
    views: 6700,
    category: "机器学习",
  },
  {
    id: 4,
    title: "Python爬虫封装EXE实战",
    cover: "/placeholder-video.jpg",
    duration: "45:20",
    views: 5400,
    category: "Python",
  },
];

export default function FeaturedVideos() {
  return (
    <section>
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
          热门视频
        </h2>
        <Link
          href="/videos"
          className="text-purple-600 hover:text-purple-700 text-sm font-medium"
        >
          查看全部 &rarr;
        </Link>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
        {mockVideos.map((video) => (
          <Link
            key={video.id}
            href={`/videos/${video.id}`}
            className="group bg-white dark:bg-gray-800 rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-shadow"
          >
            {/* Thumbnail */}
            <div className="relative aspect-video bg-gray-200 dark:bg-gray-700">
              <div className="absolute inset-0 flex items-center justify-center">
                <svg className="w-12 h-12 text-gray-400" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M8 5v14l11-7z" />
                </svg>
              </div>
              <div className="absolute bottom-2 right-2 bg-black/70 text-white text-xs px-2 py-1 rounded">
                {video.duration}
              </div>
              <div className="absolute top-2 left-2 bg-purple-600 text-white text-xs px-2 py-1 rounded">
                {video.category}
              </div>
            </div>

            {/* Info */}
            <div className="p-4">
              <h3 className="font-medium text-gray-900 dark:text-white group-hover:text-purple-600 transition-colors line-clamp-2">
                {video.title}
              </h3>
              <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
                {video.views.toLocaleString()} 次观看
              </p>
            </div>
          </Link>
        ))}
      </div>
    </section>
  );
}
