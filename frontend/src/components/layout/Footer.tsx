import Link from "next/link";

export default function Footer() {
  return (
    <footer className="bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-700">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Brand */}
          <div className="col-span-1 md:col-span-2">
            <h3 className="text-xl font-bold bg-gradient-to-r from-purple-600 to-blue-500 bg-clip-text text-transparent">
              AIGC散修
            </h3>
            <p className="mt-2 text-sm text-gray-600 dark:text-gray-400">
              只分享验证可行的前沿技术
            </p>
            <p className="mt-4 text-sm text-gray-500 dark:text-gray-500">
              平面设计师转型AI领域，分享学习路上的经验与工具，
              希望能帮助更多人快速入门前沿技术。
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-sm font-semibold text-gray-900 dark:text-white mb-4">
              快速链接
            </h4>
            <ul className="space-y-2">
              <li>
                <Link href="/videos" className="text-sm text-gray-600 dark:text-gray-400 hover:text-purple-600">
                  视频教程
                </Link>
              </li>
              <li>
                <Link href="/articles" className="text-sm text-gray-600 dark:text-gray-400 hover:text-purple-600">
                  图文教程
                </Link>
              </li>
              <li>
                <Link href="/tools" className="text-sm text-gray-600 dark:text-gray-400 hover:text-purple-600">
                  工具箱
                </Link>
              </li>
              <li>
                <Link href="/forum" className="text-sm text-gray-600 dark:text-gray-400 hover:text-purple-600">
                  社区论坛
                </Link>
              </li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="text-sm font-semibold text-gray-900 dark:text-white mb-4">
              联系方式
            </h4>
            <ul className="space-y-2">
              <li>
                <Link href="/partners" className="text-sm text-gray-600 dark:text-gray-400 hover:text-purple-600">
                  商务合作
                </Link>
              </li>
              <li>
                <Link href="/about" className="text-sm text-gray-600 dark:text-gray-400 hover:text-purple-600">
                  关于我们
                </Link>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-8 pt-8 border-t border-gray-200 dark:border-gray-700">
          <p className="text-center text-sm text-gray-500 dark:text-gray-500">
            &copy; {new Date().getFullYear()} AIGC散修_竹相左边. All rights reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
