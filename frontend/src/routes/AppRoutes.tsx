import { BrowserRouter, Routes, Route } from "react-router-dom";

import DashboardLayout from "../layouts/DashboardLayout";

import Dashboard from "../pages/Dashboard";
import Analytics from "../pages/Analytics";
import Prediction from "../pages/Prediction";
import Inventory from "../pages/Inventory";
import DecisionSupport from "../pages/DecisionSupport";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<DashboardLayout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route path="/prediction" element={<Prediction />} />
          <Route path="/inventory" element={<Inventory />} />
          <Route path="/decision-support" element={<DecisionSupport />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}