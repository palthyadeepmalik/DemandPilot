import { useEffect, useState } from "react";

import {
    getDashboard,
    getRevenueTrend,
    getCategorySales,
    getHourlySales,
    getTopPizzas,
    getWeekendVsWeekday,
} from "../api/analytics";

import StatCard from "../components/cards/StatCard";
import RevenueChart from "../components/charts/RevenueChart";
import CategoryPieChart from "../components/charts/CategoryPieChart";
import HourlySalesChart from "../components/charts/HourlySalesChart";
import TopPizzaChart from "../components/charts/TopPizzaChart";
import WeekendChart from "../components/charts/WeekendChart";

export default function Dashboard() {

    const [summary, setSummary] = useState<any>(null);
    const [revenueData, setRevenueData] = useState<any[]>([]);
    const [categoryData, setCategoryData] = useState<any[]>([]);
    const [hourlyData, setHourlyData] = useState<any[]>([]);
    const [topPizzaData, setTopPizzaData] = useState<any[]>([]);
    const [weekendData, setWeekendData] = useState<any[]>([]);

    useEffect(() => {

        const fetchDashboard = async () => {

            try {

                const dashboard = await getDashboard();
                const revenue = await getRevenueTrend();
                const categories = await getCategorySales();
                const hourly = await getHourlySales();
                const topPizzas = await getTopPizzas();
                const weekend = await getWeekendVsWeekday();

                setSummary(dashboard);
                setRevenueData(revenue);
                setCategoryData(categories);
                setHourlyData(hourly);
                setTopPizzaData(topPizzas);
                setWeekendData(weekend);

            } catch (error) {

                console.error("Dashboard Error:", error);

            }

        };

        fetchDashboard();

    }, []);

    if (!summary) {
        return (
            <div className="p-6 text-xl">
                Loading Dashboard...
            </div>
        );
    }

    return (
        <div className="space-y-10">

            {/* Page Title */}

            <div>

                <h1 className="text-4xl font-bold">
                    Dashboard
                </h1>

                <p className="text-slate-400 mt-2">
                    AI-powered inventory planning analytics
                </p>

            </div>

            {/* KPI Cards */}

            <div className="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-6">

                <StatCard
                    title="Revenue"
                    value={`$${summary.total_revenue.toLocaleString()}`}
                    subtitle="Total Revenue"
                />

                <StatCard
                    title="Orders"
                    value={summary.total_orders.toLocaleString()}
                    subtitle="Orders Processed"
                />

                <StatCard
                    title="Pizzas Sold"
                    value={summary.total_pizzas_sold.toLocaleString()}
                    subtitle="Total Quantity Sold"
                />

                <StatCard
                    title="Best Seller"
                    value={summary.top_pizza}
                    subtitle={`${summary.top_pizza_sales} Sold`}
                />

            </div>

            {/* Revenue Chart */}

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">
              <RevenueChart data={revenueData} />

              <CategoryPieChart data={categoryData} />
            </div>

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">

              <HourlySalesChart
                data={hourlyData}
              />

              <TopPizzaChart
                data={topPizzaData}
              />

            </div>
            <div className="mt-6">
              <WeekendChart data={weekendData} />
            </div>

        </div>
    );
}