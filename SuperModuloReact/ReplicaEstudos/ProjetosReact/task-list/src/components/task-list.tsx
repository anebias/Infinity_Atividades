// components/task-list.tsx
import type { Task } from "../App";
import { TaskItem } from "./task-item";

type TaskListProps = {
  tasks: Task[];
  deleteTask: (task: Task) => Promise<void>;
  updateTaskComplete: (task: Task) => Promise<void>;
};

export const TaskList = ({
  tasks,
  deleteTask,
  updateTaskComplete,
}: TaskListProps) => {
  if (tasks.length == 0) {
    return <p className="pt-10 text-center">Não há tarefas cadastradas.</p>;
  }

  return (
    <ul className="pt-10 flex flex-col items-center gap-4">
      {tasks.map((task) => (
        <TaskItem
          key={task.id}
          task={task}
          deleteTask={deleteTask}
          updateTaskComplete={updateTaskComplete}
        />
      ))}
    </ul>
  );
};