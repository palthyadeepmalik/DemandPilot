import axios from "axios";
import type { InventoryResponse } from "../types/inventory";

const API = "http://127.0.0.1:8000";

export async function getInventory(): Promise<InventoryResponse> {
  const response = await axios.get(`${API}/inventory/`);
  return response.data;
}