export type Ingredient = {
  ingredient: string;
  required_quantity: number;
};

export type InventoryResponse = {
  forecast_date: string;
  predicted_pizzas: number;
  ingredients: Ingredient[];
};