import Link from "next/link";

// Mock data
const mockTasks = [
  {
    id: 1,
    title: "帮我写一个图片批量重命名脚本",
    reward: 200,
    deadline: "3天后截止",
  },
  {
    id: 2,
    title: "SD模型效果测试报告撰写",
    reward: 150,
    deadline: "5天后截止",
  },
  {
    id: 3,
    title: "ComfyUI工作流调试",
    reward: 300,
    deadline: "7天后截止",
  },
];

export default function OpenTasks() {
  return (
    <section className="bg-white dark:bg-gray-800 rounded-xl shadow-sm p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-lg font-bold text-gray-900 dark:text-white">
          待揭榜任务
        </h2>
        <Link
          href="/tasks"
          className="text-purple-600 hover:text-purple-700 text-sm"
        >
          更多
        </Link>
      </div>

      <div className="space-y-3">
        {mockTasks.map((task) => (
          <Link
            key={task.id}
            href={`/tasks/${task.id}`}
            className="block p-3 border border-gray-200 dark:border-gray-700 rounded-lg hover:border-purple-300 dark:hover:border-purple-600 transition-colors"
          >
            <h3 className="text-sm font-medium text-gray-900 dark:text-white line-clamp-1">
              {task.title}
            </h3>
            <div className="mt-2 flex items-center justify-between">
              <span className="text-xs text-gray-500">{task.deadline}</span>
              <span className="px-2 py-1 bg-purple-100 text-purple-700 text-xs font-medium rounded">
                {task.reward} 积分
              </span>
            </div>
          </Link>
        ))}
      </div>

      <Link
        href="/tasks/create"
        className="mt-4 block w-full text-center py-2 border-2 border-dashed border-gray-300 dark:border-gray-600 text-gray-500 dark:text-gray-400 rounded-lg hover:border-purple-400 hover:text-purple-600 transition-colors text-sm"
      >
        + 发布悬赏任务
      </Link>
    </section>
  );
}
