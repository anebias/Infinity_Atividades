import './App.css';
import { Header } from '../components/headers.tsx';
import { Search } from 'lucide-react';

export function App(){
  return (
    <div className = 'pb-20'>
      <Header />

      <main>
        <div className='max-w-[1400px] m-auto flex flex-col gap-16'>
          <section className='flex flex-col items-center gap-8 mt-32'>
            <h1 className='text-3xl' > O que você busca? </h1>
              <div className='flex bg-white shadow-lg shadow-indigo-200 max-w-[600px] w-full p-4 rounded-3xl border border-zinc-300 items-center'>
                <Search />
                <input type="text" className='w-full pl-4 outline-0 text-lg'/>
              </div>
          </section>
        </div>
      </main>

    </div>
  )
}

