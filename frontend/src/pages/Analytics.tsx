import { useEffect, useState } from "react";

import {
  ResponsiveContainer,
  LineChart,
  Line,
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Legend,
} from "recharts";

import {
  getDailySales,
  getMonthlySales,
  getTopPizzas,
  getCategorySales,
  getHourlySales,
  getWeekendVsWeekday,
} from "../api/analytics";

const COLORS = [
  "#3B82F6",
  "#10B981",
  "#F59E0B",
  "#EF4444",
  "#8B5CF6",
  "#06B6D4",
];

export default function Analytics() {

  const [dailySales, setDailySales] = useState<any[]>([]);
  const [monthlySales, setMonthlySales] = useState<any[]>([]);
  const [topPizzas, setTopPizzas] = useState<any[]>([]);
  const [categorySales, setCategorySales] = useState<any[]>([]);
  const [hourlySales, setHourlySales] = useState<any[]>([]);
  const [weekendSales, setWeekendSales] = useState<any[]>([]);

  useEffect(() => {

    Promise.all([
      getDailySales(),
      getMonthlySales(),
      getTopPizzas(),
      getCategorySales(),
      getHourlySales(),
      getWeekendVsWeekday(),
    ]).then(
      ([
        daily,
        monthly,
        pizzas,
        categories,
        hourly,
        weekend,
      ]) => {

        setDailySales(daily);
        setMonthlySales(monthly);
        setTopPizzas(pizzas);
        setCategorySales(categories);
        setHourlySales(hourly);
        setWeekendSales(weekend);

      }
    );

  }, []);

  console.log("Daily Sales:", dailySales);
  return (

    <div className="space-y-8">

      <div>

        <h1 className="text-4xl font-bold text-white">
          Analytics Dashboard
        </h1>

        <p className="text-slate-400 mt-2">
          Business Intelligence & Sales Analytics
        </p>

      </div>

      {/* Daily Revenue */}

      <div className="bg-white rounded-xl shadow p-6">

        <h2 className="text-2xl font-bold text-slate-900 mb-4">
          Daily Revenue Trend
        </h2>

        <ResponsiveContainer
          width="100%"
          height={350}
        >

          <LineChart data={dailySales}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="date" />

            <YAxis />

            <Tooltip />

            <Legend />

            <Line
              type="monotone"
              dataKey="revenue"
              stroke="#2563eb"
              strokeWidth={3}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

      {/* Monthly Revenue */}

      <div className="bg-white rounded-xl shadow p-6">

        <h2 className="text-2xl font-bold text-slate-900 mb-4">
          Monthly Revenue
        </h2>

        <ResponsiveContainer
          width="100%"
          height={350}
        >

          <BarChart data={monthlySales}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="month" />

            <YAxis />

            <Tooltip />

            <Legend />

            <Bar
              dataKey="revenue"
              fill="#2563eb"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>
            {/* Category Sales */}

      <div className="bg-white rounded-xl shadow p-6">

        <h2 className="text-2xl font-bold text-slate-900 mb-4">
          Category Sales
        </h2>

        <ResponsiveContainer
          width="100%"
          height={350}
        >

          <PieChart>

            <Pie
              data={categorySales}
              dataKey="revenue"
              nameKey="category"
              outerRadius={120}
              label
            >

              {categorySales.map((_, index) => (

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

      {/* Top Selling Pizzas */}

      <div className="bg-white rounded-xl shadow p-6">

        <h2 className="text-2xl font-bold text-slate-900 mb-4">
          Top Selling Pizzas
        </h2>

        <ResponsiveContainer
          width="100%"
          height={400}
        >

          <BarChart data={topPizzas}>

            <CartesianGrid strokeDasharray="3 3"/>

            <XAxis
              dataKey="pizza_name"
              hide
            />

            <YAxis/>

            <Tooltip/>

            <Bar
              dataKey="total_sold"
              fill="#10B981"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

      {/* Hourly Sales */}

      <div className="bg-white rounded-xl shadow p-6">

        <h2 className="text-2xl font-bold text-slate-900 mb-4">
          Hourly Orders
        </h2>

        <ResponsiveContainer
          width="100%"
          height={350}
        >

          <LineChart data={hourlySales}>

            <CartesianGrid strokeDasharray="3 3"/>

            <XAxis dataKey="hour"/>

            <YAxis/>

            <Tooltip/>

            <Line
              type="monotone"
              dataKey="total_orders"
              stroke="#F59E0B"
              strokeWidth={3}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

      {/* Weekend vs Weekday */}

      <div className="bg-white rounded-xl shadow p-6">

        <h2 className="text-2xl font-bold text-slate-900 mb-4">
          Weekend vs Weekday
        </h2>

        <ResponsiveContainer
          width="100%"
          height={300}
        >

          <BarChart data={weekendSales}>

            <CartesianGrid strokeDasharray="3 3"/>

            <XAxis dataKey="day_type"/>

            <YAxis/>

            <Tooltip/>

            <Legend/>

            <Bar
              dataKey="orders"
              fill="#3B82F6"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>

  );

}