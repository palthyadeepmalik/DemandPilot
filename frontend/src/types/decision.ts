export interface Recommendation {
  priority: string;
  ingredient: string;
  message: string;
}

export interface DecisionResponse {
  forecast_date: string;
  predicted_pizzas: number;
  recommendations: Recommendation[];
}