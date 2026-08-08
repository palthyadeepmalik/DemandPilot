import { NavLink } from "react-router-dom";

const links = [
  { name: "Dashboard", path: "/" },
  { name: "Analytics", path: "/analytics" },
  { name: "Prediction", path: "/prediction" },
  { name: "Inventory", path: "/inventory" },
  { name: "Decision Support", path: "/decision-support" }
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-800 border-r border-slate-700 flex flex-col">
      <div className="p-6">
        <h1 className="text-2xl font-bold text-cyan-400">
          DemandPilot
        </h1>
      </div>

      <nav className="flex flex-col gap-2 px-4">
        {links.map((link) => (
          <NavLink
            key={link.path}
            to={link.path}
            className={({ isActive }) =>
              `rounded-lg px-4 py-3 transition ${
                isActive
                  ? "bg-cyan-500 text-white"
                  : "text-slate-300 hover:bg-slate-700"
              }`
            }
          >
            {link.name}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}