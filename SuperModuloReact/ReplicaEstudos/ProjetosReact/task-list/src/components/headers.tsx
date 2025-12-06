import { useState } from "react";
import { Button } from "./button";

type HeaderProps = {
    addTask: (taskName: string) => void
};

export const Header = ({ addTask }: HeaderProps ) => {

    const [taskName,setTaskName] = useState('');

    const handleAddTask = () => {
        if(!taskName.trim()){
            return
        };

        addTask(taskName);
        setTaskName('');
    };

    return(
	<header className="flex flex-col items-center pt-8 gap-16">
		<h1 className="text-3xl"> My Tasks </h1>
		<div className="flex gap-4">
			<input 
                type="text" 
                className="bg-white shadow w-80 h-12 text-xl py-2 px-4 outline-0 rounded-2xl" 
                value={taskName}
                onChange={(event)=>{setTaskName(event.target.value)}}
                />
			<Button onClick={handleAddTask}>+</Button>
		</div>
	</header>
    )
}