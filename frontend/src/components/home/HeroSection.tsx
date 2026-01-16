import Link from "next/link";

export default function HeroSection() {
  return (
    <section className="bg-gradient-to-r from-purple-600 via-purple-700 to-blue-600 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-24">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
          {/* Author Info */}
          <div>
            <div className="flex items-center space-x-4 mb-6">
              <div className="w-20 h-20 rounded-full bg-white/20 flex items-center justify-center text-3xl">
                {/* Avatar placeholder */}
                <span>ZX</span>
              </div>
              <div>
                <h1 className="text-2xl md:text-3xl font-bold">竹相左边</h1>
                <p className="text-purple-200">AIGC散修</p>
              </div>
            </div>
            
            <p className="text-xl md:text-2xl font-medium mb-4">
              只分享验证可行的前沿技术
            </p>
            
            <p className="text-purple-100 mb-8 leading-relaxed">
              8年平面设计师，2022年开始探索AI领域。从Stable Diffusion到YOLOv8，
              从爬虫脚本到强化学习，一路实践验证，只分享真正跑通的技术方案。
            </p>

            <div className="flex flex-wrap gap-3">
              <span className="px-3 py-1 bg-white/20 rounded-full text-sm">Stable Diffusion</span>
              <span className="px-3 py-1 bg-white/20 rounded-full text-sm">AI绘画</span>
              <span className="px-3 py-1 bg-white/20 rounded-full text-sm">Python</span>
              <span className="px-3 py-1 bg-white/20 rounded-full text-sm">工具开发</span>
              <span className="px-3 py-1 bg-white/20 rounded-full text-sm">YOLOv8</span>
            </div>
          </div>

          {/* Stats & CTA */}
          <div className="bg-white/10 backdrop-blur-sm rounded-2xl p-8">
            <div className="grid grid-cols-2 gap-6 mb-8">
              <div className="text-center">
                <div className="text-3xl font-bold">100+</div>
                <div className="text-purple-200 text-sm">视频教程</div>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold">50+</div>
                <div className="text-purple-200 text-sm">实用工具</div>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold">200+</div>
                <div className="text-purple-200 text-sm">图文教程</div>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold">1000+</div>
                <div className="text-purple-200 text-sm">社区成员</div>
              </div>
            </div>

            <div className="space-y-3">
              <Link
                href="/register"
                className="block w-full bg-white text-purple-600 text-center py-3 rounded-lg font-medium hover:bg-purple-50 transition-colors"
              >
                加入学习
              </Link>
              <Link
                href="/videos"
                className="block w-full border border-white/50 text-center py-3 rounded-lg font-medium hover:bg-white/10 transition-colors"
              >
                浏览内容
              </Link>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
