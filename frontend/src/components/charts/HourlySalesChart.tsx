import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer,
    CartesianGrid,
} from "recharts";

type Props = {
    data: any[];
};

export default function HourlySalesChart({ data }: Props) {
    return (
        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-xl font-semibold text-slate-800 mb-6">
                Hourly Sales
            </h2>

            <ResponsiveContainer width="100%" height={350}>

                <BarChart data={data}>

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis dataKey="hour" />

                    <YAxis />

                    <Tooltip />

                    <Bar
                        dataKey="orders"
                        fill="#2563eb"
                        radius={[6, 6, 0, 0]}
                    />

                </BarChart>

            </ResponsiveContainer>

        </div>
    );
}