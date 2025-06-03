import axios from 'axios';

const API_BASE = 'http://localhost:8000';

export async function getUserProfile(userId) {
  try {
    const res = await axios.get(`${API_BASE}/user/profile/${userId}`);
    return res.data;
  } catch (err) {
    console.error('Error fetching user profile:', err);
    throw err;
  }
}

export async function setUserProfile(profile) {
  try {
    const res = await axios.post(`${API_BASE}/user/profile`, profile);
    return res.data;
  } catch (err) {
    console.error('Error setting user profile:', err);
    throw err;
  }
}

export async function chatWithAI(message) {
  try {
    const res = await axios.post(`${API_BASE}/chat`, { user_message: message });
    return res.data.response;
  } catch (err) {
    console.error('Error chatting with AI:', err);
    throw err;
  }
}

export async function submitDailyLog(logData) {
  // Placeholder: implement backend endpoint for daily logs if needed
  try {
    // Example: await axios.post(`${API_BASE}/daily-log`, logData);
    console.log('Submitting daily log:', logData);
    return { success: true };
  } catch (err) {
    console.error('Error submitting daily log:', err);
    throw err;
  }
} 