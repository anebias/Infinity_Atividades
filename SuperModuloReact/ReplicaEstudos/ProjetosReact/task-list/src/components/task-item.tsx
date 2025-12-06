import { Button } from "./button"
import type { Task } from "../App"

// Props Atualizadas para Receberem as Funções
type TaskItemProps = {
	task: Task;
	deleteTask: (taskId: string) => void;
	updateTask: (taskId: string) => void;
}

export const TaskItem = ({ task, deleteTask, updateTask }: TaskItemProps) => (
	<li className={`${!task.completed ? "bg-white" : "bg-zinc-300"} text-xl shadow w-lg p-6 flex justify-between items-center rounded-xl`}>
		<div className={`${!task.completed ? "" : "line-through "}flex items-center gap-4`}>
			{/* 
			Quando o usuário clicar no checkbox e o valor mudar, 
			chamamos a função passando o ID da task que renderizou o checkbox
			*/}
			<input
				type="checkbox"
				className="w-4 h-4"
				value={task.completed ? 'true' : 'false'}
				onChange={() => updateTask(task.id)}
			/>
			<p>{task.name}</p>
		</div>
		{/* 
		Quando o usuário clica no botão de excluir, 
		nós chamamos a função passando o ID da task que renderizou o botão 
		*/}
		<Button
			disabled={task.completed}
			onClick={() => deleteTask(task.id)}
			className={`text-[16px] w-fit h-fit px-4 py-1 ${task.completed ? "bg-red-300 hover:bg-red-300 hover:cursor-not-allowed" : "bg-red-500 hover:bg-red-600"} rounded-xl`}
		>
			Excluir
		</Button>
	</li>
)

