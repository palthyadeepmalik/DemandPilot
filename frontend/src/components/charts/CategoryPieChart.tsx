import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    ResponsiveContainer,
    Legend,
} from "recharts";

type Props = {
    data: any[];
};

const COLORS = [
    "#2563eb",
    "#22c55e",
    "#f97316",
    "#a855f7",
    "#ef4444",
];

export default function CategoryPieChart({ data }: Props) {

    return (
        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-xl font-semibold text-slate-800 mb-6">
                Category Sales
            </h2>

            <ResponsiveContainer width="100%" height={350}>

                <PieChart>

                    <Pie
                        data={data}
                        dataKey="revenue"
                        nameKey="category"
                        outerRadius={120}
                        label
                    >

                        {data.map((_, index) => (

                            <Cell
                                key={index}
                                fill={COLORS[index % COLORS.length]}
                            />

                        ))}

                    </Pie>

                    <Tooltip />

                    <Legend />

                </PieChart>

            </ResponsiveContainer>

        </div>
    );

}