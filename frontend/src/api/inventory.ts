import axios from "axios";
import type { InventoryResponse } from "../types/inventory";

const API = import.meta.env.VITE_API_URL;

export async function getInventory(): Promise<InventoryResponse> {
  const response = await axios.get(`${API}/inventory/`);
  return response.data;
}