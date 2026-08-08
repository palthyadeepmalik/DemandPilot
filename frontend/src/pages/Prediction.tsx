import { useEffect, useState } from "react";
import axios from "axios";

type Prediction = {
  date: string;
  pizza_id: string;
  pizza_type_id: string;
  category: string;
  size: string;
  predicted_quantity: number;
};

type PredictionResponse = {
  date: string;
  total_predicted_quantity: number;
  predictions: Prediction[];
};

export default function Prediction() {
  const [data, setData] = useState<PredictionResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/prediction/tomorrow")
      .then((res) => {
        setData(res.data);
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return <div className="text-white text-xl">Loading predictions...</div>;
  }

  if (!data) {
    return <div className="text-red-500">Failed to load predictions.</div>;
  }


  console.log(data.predictions.length);
  return (
    <div className="space-y-6">
      <h1 className="text-4xl font-bold text-white">
        Tomorrow's Prediction
      </h1>

      <div className="bg-white rounded-xl p-6 shadow">
        <p className="text-gray-500">
          Forecast Date
        </p>

        <h2 className="text-3xl font-bold text-slate-900">
          {data.date}
        </h2>
      </div>

      <div className="bg-white rounded-xl p-6 shadow">
        <p className="text-gray-500">
          Total Predicted Orders
        </p>

        <h2 className="text-4xl font-bold text-blue-600">
          {data.total_predicted_quantity}
        </h2>
      </div>

      <div className="bg-white rounded-xl shadow overflow-auto">
        <table className="min-w-full">
          <thead className="bg-slate-200 text-slate-900">
            <tr>
              <th className="p-3 text-left">Pizza</th>
              <th className="p-3 text-left">Category</th>
              <th className="p-3 text-left">Size</th>
              <th className="p-3 text-right">Predicted Qty</th>
            </tr>
          </thead>

          <tbody>
            {data.predictions.map((pizza, index) => (
              <tr
                key={`${pizza.pizza_id}-${index}`}
                className="border-b hover:bg-slate-50"
              >
                <td className="p-3 text-slate-900">
                  {pizza.pizza_type_id}
                </td>

                <td className="p-3 text-slate-900">
                  {pizza.category}
                </td>

                <td className="p-3 text-slate-900">
                  {pizza.size}
                </td>

                <td className="p-3 text-right font-bold text-blue-600">
                  {pizza.predicted_quantity}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}