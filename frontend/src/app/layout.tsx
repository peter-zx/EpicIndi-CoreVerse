import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Header from "@/components/layout/Header";
import Footer from "@/components/layout/Footer";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "AIGC散修 | 竹相左边 - 只分享验证可行的前沿技术",
  description: "AIGC散修学习平台，分享AI、设计、开发等前沿技术，提供工具下载、视频教程、图文教程、播客内容，以及作业练习和社区论坛。",
  keywords: ["AIGC", "AI学习", "前沿技术", "工具分享", "Stable Diffusion", "技术教程"],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN">
      <body className={`${inter.variable} antialiased bg-gray-50 dark:bg-gray-900`}>
        <div className="min-h-screen flex flex-col">
          <Header />
          <main className="flex-1">
            {children}
          </main>
          <Footer />
        </div>
      </body>
    </html>
  );
}
