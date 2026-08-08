import {
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
} from "recharts";

type Props = {
    data: any[];
};

export default function TopPizzaChart({ data }: Props) {
    return (
        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-xl font-semibold text-slate-800 mb-6">
                Top Selling Pizzas
            </h2>

            <ResponsiveContainer width="100%" height={350}>

                <BarChart
                    data={data}
                    layout="vertical"
                    margin={{ left: 60 }}
                >

                    <CartesianGrid strokeDasharray="3 3" />

                    <XAxis type="number" />

                    <YAxis
                        dataKey="pizza_name"
                        type="category"
                        width={150}
                    />

                    <Tooltip />

                    <Bar
                        dataKey="total_sold"
                        fill="#f97316"
                        radius={[0, 6, 6, 0]}
                    />

                </BarChart>

            </ResponsiveContainer>

        </div>
    );
}