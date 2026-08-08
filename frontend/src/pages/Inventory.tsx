import { useEffect, useState } from "react";
import { getInventory } from "../api/inventory";
import type { InventoryResponse } from "../types/inventory";

export default function Inventory() {
  const [data, setData] = useState<InventoryResponse | null>(null);

  useEffect(() => {
    getInventory().then(setData);
  }, []);

  if (!data) {
    return (
      <div className="text-white text-xl">
        Loading...
      </div>
    );
  }

  return (
    <div className="space-y-8">

      <h1 className="text-4xl font-bold text-white">
        Inventory Planning
      </h1>

      <div className="grid grid-cols-2 gap-6">

        <div className="bg-white rounded-xl shadow p-6">

          <p className="text-gray-500">
            Forecast Date
          </p>

          <h2 className="text-3xl font-bold text-slate-900">
            {data.forecast_date}
          </h2>

        </div>

        <div className="bg-white rounded-xl shadow p-6">

          <p className="text-gray-500">
            Predicted Pizzas
          </p>

          <h2 className="text-3xl font-bold text-blue-600">
            {data.predicted_pizzas}
          </h2>

        </div>

      </div>

      <div className="bg-white rounded-xl shadow">

        <div className="p-6 border-b">

          <h2 className="text-2xl font-bold text-slate-900">
            Ingredient Requirements
          </h2>

        </div>

        <table className="w-full">

          <thead className="bg-slate-100 text-slate-900">

            <tr>

              <th className="p-4 text-left">
                Ingredient
              </th>

              <th className="p-4 text-right">
                Required Quantity
              </th>

            </tr>

          </thead>

          <tbody>

            {data.ingredients.map((item, index) => (

              <tr
                key={index}
                className="border-b hover:bg-slate-50"
              >

                <td className="p-4 text-slate-900">
                  {item.ingredient}
                </td>

                <td className="p-4 text-right font-bold text-blue-600">
                  {item.required_quantity.toFixed(2)} kg
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}