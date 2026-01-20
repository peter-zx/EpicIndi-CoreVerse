import HeroSection from "@/components/home/HeroSection";
import FeaturedVideos from "@/components/home/FeaturedVideos";
import FeaturedTools from "@/components/home/FeaturedTools";
import FeaturedArticles from "@/components/home/FeaturedArticles";
import Leaderboard from "@/components/home/Leaderboard";
import OpenTasks from "@/components/home/OpenTasks";
import SponsorBanner from "@/components/home/SponsorBanner";

export default function Home() {
  return (
    <div className="min-h-screen">
      {/* Hero Section - 作者信息 */}
      <HeroSection />

      {/* 赞助商广告 */}
      <SponsorBanner />

      {/* Main Content Grid */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Left Column - Main Content */}
          <div className="lg:col-span-2 space-y-12">
            {/* 热门视频 */}
            <FeaturedVideos />

            {/* 热门工具 */}
            <FeaturedTools />

            {/* 热门图文/观点 */}
            <FeaturedArticles />
          </div>

          {/* Right Column - Sidebar */}
          <div className="space-y-8">
            {/* 积分排行榜 */}
            <Leaderboard />

            {/* 待揭榜任务 */}
            <OpenTasks />
          </div>
        </div>
      </div>
    </div>
  );
}
