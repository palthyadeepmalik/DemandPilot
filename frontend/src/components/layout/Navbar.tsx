export default function Navbar() {
  return (
    <header className="h-16 border-b border-slate-700 bg-slate-800 flex items-center justify-between px-8">
      <h2 className="text-xl font-semibold">
        AI Inventory Planning System
      </h2>

      <div className="flex items-center gap-3">
        <div className="h-10 w-10 rounded-full bg-cyan-500 flex items-center justify-center font-bold">
          N
        </div>

        <span className="text-slate-300">
          Nitish
        </span>
      </div>
    </header>
  );
}