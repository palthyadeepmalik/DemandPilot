import api from "./client";

export interface PredictionRequest {
  pizza_id: string;
  prediction_date: string;
}

export interface PredictionResponse {
  pizza_id: string;
  prediction_date: string;
  predicted_quantity: number;
}

export const predictDemand = async (
  data: PredictionRequest
): Promise<PredictionResponse> => {
  const response = await api.post("/predict", data);
  return response.data;
};