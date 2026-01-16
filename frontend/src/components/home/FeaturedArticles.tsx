import Link from "next/link";

// Mock data
const mockArticles = [
  {
    id: 1,
    title: "2024年AI绘画技术发展趋势分析",
    excerpt: "从Midjourney V6到SDXL Turbo，AI绘画技术在2024年迎来了重大突破...",
    category: "观点",
    readTime: "8分钟",
    views: 5600,
  },
  {
    id: 2,
    title: "为什么我选择从设计师转型AI领域",
    excerpt: "作为一个8年设计师，我在2022年做出了一个重要决定...",
    category: "播客",
    readTime: "12分钟",
    views: 4200,
  },
  {
    id: 3,
    title: "ComfyUI vs WebUI：该选哪个？",
    excerpt: "两款主流SD前端的详细对比，帮你找到最适合的工具...",
    category: "图文",
    readTime: "6分钟",
    views: 7800,
  },
];

export default function FeaturedArticles() {
  return (
    <section>
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
          热门观点
        </h2>
        <Link
          href="/articles"
          className="text-purple-600 hover:text-purple-700 text-sm font-medium"
        >
          查看全部 &rarr;
        </Link>
      </div>

      <div className="space-y-4">
        {mockArticles.map((article) => (
          <Link
            key={article.id}
            href={`/articles/${article.id}`}
            className="block p-5 bg-white dark:bg-gray-800 rounded-xl shadow-sm hover:shadow-md transition-shadow"
          >
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <div className="flex items-center space-x-2 mb-2">
                  <span className={`px-2 py-0.5 text-xs rounded-full ${
                    article.category === "观点" 
                      ? "bg-orange-100 text-orange-700"
                      : article.category === "播客"
                      ? "bg-blue-100 text-blue-700"
                      : "bg-green-100 text-green-700"
                  }`}>
                    {article.category}
                  </span>
                  <span className="text-xs text-gray-400">{article.readTime}</span>
                </div>
                <h3 className="font-medium text-gray-900 dark:text-white hover:text-purple-600 transition-colors">
                  {article.title}
                </h3>
                <p className="mt-2 text-sm text-gray-500 dark:text-gray-400 line-clamp-2">
                  {article.excerpt}
                </p>
              </div>
            </div>
            <div className="mt-3 text-xs text-gray-400">
              {article.views.toLocaleString()} 次阅读
            </div>
          </Link>
        ))}
      </div>
    </section>
  );
}
