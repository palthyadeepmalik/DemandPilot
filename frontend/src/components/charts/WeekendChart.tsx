import {
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid,
} from "recharts";

type Props = {
    data: any[];
};

export default function WeekendChart({ data }: Props) {
    return (
        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-xl font-semibold text-slate-800 mb-6">
                Weekend vs Weekday Sales
            </h2>

            <ResponsiveContainer width="100%" height={350}>

                <BarChart data={data}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis dataKey="day_type" />

                    <YAxis />

                    <Tooltip />

                    <Bar
                        dataKey="revenue"
                        fill="#22c55e"
                        radius={[6, 6, 0, 0]}
                    />

                </BarChart>

            </ResponsiveContainer>

        </div>
    );
}