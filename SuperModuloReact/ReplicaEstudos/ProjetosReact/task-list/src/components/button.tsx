import { twMerge } from "tailwind-merge";

type ButtonProps = {
	children: React.ReactNode;
	className?: string;
    onClick?: () => void;
}

export const Button = ({ children, className = "",...props}: ButtonProps) => {
	return (
		<button
            {...props}
            className={twMerge("bg-zinc-950 text-white flex justify-center items-center w-12 h-12 rounded-2xl text-xl hover:bg-zinc-800 duration-300 hover:cursor-pointer", className)}
            >
			{children}
		</button>
	)
}