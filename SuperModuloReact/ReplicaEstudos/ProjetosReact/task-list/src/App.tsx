// App.tsx
import { useState } from "react";
import { Header } from "./components/headers";
import { TaskList } from "./components/task-list";

export type Task = {
  id: string;
  name: string;
  completed: boolean;
}

export function App() {
  const [tasks, setTasks] = useState<Task[]>([])

  const addTask = (taskName: string) => {
    const newTask: Task = {
      id: crypto.randomUUID(),
      name: taskName,
      completed: false
    }

    setTasks([...tasks, newTask])
  }

	// Função para excluir a task, recebe o ID da task que vai excluir
  const deleteTask = (taskId: string) => {
    const taskToDelete = tasks.find((task) => task.id == taskId)

    if (!taskToDelete) {
      return
    }

    const otherTasks = tasks.filter((task) => task.id != taskId)
    setTasks(otherTasks)
  }

	// Função para atualizar a task, recebe o ID da task que vai atualizar
  const updateTask = (taskId: string) => {
    const taskToUpdate = tasks.find((task) => task.id == taskId)

    if (!taskToUpdate) {
      return
    }

    taskToUpdate.completed = !taskToUpdate.completed
    const otherTasks = tasks.filter((task) => task.id != taskId)
    setTasks([...otherTasks, taskToUpdate])
  }

  return (
    <div className="bg-gray-100 h-screen">
      <Header addTask={addTask} />
			{/* Passando como Props as Funções de Exclusão e Atualização */}
      <TaskList
        tasks={tasks}
        deleteTask={deleteTask}
        updateTask={updateTask}
      />
    </div>
  )
}