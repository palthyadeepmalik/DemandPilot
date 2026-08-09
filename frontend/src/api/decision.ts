import axios from "axios";

const API = import.meta.env.VITE_API_URL;

export const getDecisionSupport = async () => {
  const res = await axios.get(`${API}/decision-support`);
  return res.data;
};