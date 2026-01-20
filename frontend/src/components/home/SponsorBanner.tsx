import Link from "next/link";

export default function SponsorBanner() {
  return (
    <section className="bg-gradient-to-r from-gray-100 to-gray-50 dark:from-gray-800 dark:to-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <span className="text-xs text-gray-500 dark:text-gray-400">赞助商</span>
            <div className="flex items-center space-x-6">
              {/* Sponsor placeholders */}
              <div className="h-8 px-4 bg-white dark:bg-gray-700 rounded flex items-center justify-center text-gray-400 text-sm">
                赞助商A
              </div>
              <div className="h-8 px-4 bg-white dark:bg-gray-700 rounded flex items-center justify-center text-gray-400 text-sm">
                赞助商B
              </div>
              <div className="hidden sm:flex h-8 px-4 bg-white dark:bg-gray-700 rounded items-center justify-center text-gray-400 text-sm">
                赞助商C
              </div>
            </div>
          </div>
          <Link
            href="/partners"
            className="text-xs text-purple-600 hover:text-purple-700"
          >
            成为赞助商
          </Link>
        </div>
      </div>
    </section>
  );
}
