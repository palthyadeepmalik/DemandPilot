import { useEffect, useState } from "react";

import { getDecisionSupport } from "../api/decision";

import type {
  DecisionResponse,
  Recommendation,
} from "../types/decision";

export default function DecisionSupport() {
  const [data, setData] =
    useState<DecisionResponse | null>(null);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {
    getDecisionSupport()
      .then((res) => {
        console.log(res);
        setData(res);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="text-white text-2xl">
        Loading...
      </div>
    );
  }

  if (!data) {
    return (
      <div className="text-red-500">
        Failed to load.
      </div>
    );
  }

  return (
    <div className="space-y-6">

      <h1 className="text-4xl font-bold text-white">
        Decision Support
      </h1>

      {/* Summary Cards */}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">

        <div className="bg-white rounded-xl p-6 shadow">
          <p className="text-gray-500">
            Forecast Date
          </p>

          <h2 className="text-3xl font-bold text-slate-900 mt-2">
            {data.forecast_date}
          </h2>
        </div>

        <div className="bg-white rounded-xl p-6 shadow">
          <p className="text-gray-500">
            Predicted Pizzas
          </p>

          <h2 className="text-3xl font-bold text-blue-600 mt-2">
            {data.predicted_pizzas}
          </h2>
        </div>

      </div>

      {/* Recommendations */}

      <div className="space-y-4">

        {data.recommendations.map(
          (
            recommendation: Recommendation,
            index: number
          ) => (
            <div
              key={index}
              className={`rounded-xl p-5 shadow text-white ${
                recommendation.priority === "HIGH"
                  ? "bg-red-500"
                  : recommendation.priority === "MEDIUM"
                  ? "bg-yellow-500"
                  : "bg-green-500"
              }`}
            >
              <h2 className="text-2xl font-bold">
                {recommendation.priority}
              </h2>

              <p className="text-xl mt-2">
                {recommendation.ingredient}
              </p>

              <p className="mt-3">
                {recommendation.message}
              </p>
            </div>
          )
        )}

      </div>

    </div>
  );
}