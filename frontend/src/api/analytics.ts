import axios from "axios";

const API = import.meta.env.VITE_API_URL;

// Dashboard Summary
export const getDashboard = async () => {
  const res = await axios.get(`${API}/analytics/dashboard`);
  return res.data;
};

// Revenue Trend
export const getRevenueTrend = async () => {
  const res = await axios.get(`${API}/analytics/daily-sales`);
  return res.data;
};

// Daily Sales
export const getDailySales = async () => {
  const res = await axios.get(`${API}/analytics/daily-sales`);
  return res.data;
};

// Monthly Sales
export const getMonthlySales = async () => {
  const res = await axios.get(`${API}/analytics/monthly-sales`);
  return res.data;
};

// Top Pizzas
export const getTopPizzas = async () => {
  const res = await axios.get(`${API}/analytics/top-pizzas`);
  return res.data;
};

// Category Sales
export const getCategorySales = async () => {
  const res = await axios.get(`${API}/analytics/category-sales`);
  return res.data;
};

// Hourly Sales
export const getHourlySales = async () => {
  const res = await axios.get(`${API}/analytics/hourly-sales`);
  return res.data;
};

// Weekend vs Weekday
export const getWeekendVsWeekday = async () => {
  const res = await axios.get(`${API}/analytics/weekend-vs-weekday`);
  return res.data;
};

// Alias (optional)
export const getWeekendSales = getWeekendVsWeekday;