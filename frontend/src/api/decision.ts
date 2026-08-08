import axios from "axios";

const API = "http://127.0.0.1:8000";

export const getDecisionSupport = async () => {
  const res = await axios.get(`${API}/decision-support`);
  return res.data;
};