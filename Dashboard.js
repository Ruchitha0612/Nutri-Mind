import React from 'react';
import { Line, Bar } from 'react-chartjs-2';
import { Chart, CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend } from 'chart.js';

Chart.register(CategoryScale, LinearScale, PointElement, LineElement, BarElement, Title, Tooltip, Legend);

const Dashboard = () => {
  // Mock data for symptom severity over time
  const symptomData = {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [
      {
        label: 'Bloating Severity',
        data: [2, 3, 4, 2, 1, 3, 2],
        borderColor: 'rgba(75,192,192,1)',
        backgroundColor: 'rgba(75,192,192,0.2)',
        tension: 0.3,
      },
      {
        label: 'Cramps Severity',
        data: [1, 2, 2, 1, 1, 2, 1],
        borderColor: 'rgba(255,99,132,1)',
        backgroundColor: 'rgba(255,99,132,0.2)',
        tension: 0.3,
      },
    ],
  };

  // Mock data for meals vs. gut reaction
  const mealsGutData = {
    labels: ['Oatmeal', 'Pizza', 'Salad', 'Chicken', 'Rice', 'Yogurt', 'Soup'],
    datasets: [
      {
        label: 'Gut Reaction (1=Good, 5=Bad)',
        data: [1, 4, 2, 2, 1, 5, 2],
        backgroundColor: 'rgba(54, 162, 235, 0.6)',
      },
    ],
  };

  // Mock data for hydration trends
  const hydrationData = {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [
      {
        label: 'Water Intake (cups)',
        data: [7, 8, 6, 9, 7, 8, 10],
        borderColor: 'rgba(153, 102, 255, 1)',
        backgroundColor: 'rgba(153, 102, 255, 0.2)',
        tension: 0.3,
      },
    ],
  };

  return (
    <div style={{ maxWidth: 900, margin: '0 auto', padding: 24 }}>
      <h2>Health Dashboard</h2>
      <div style={{ marginBottom: 40 }}>
        <h3>Symptom Severity Over Time</h3>
        <Line data={symptomData} options={{ responsive: true, plugins: { legend: { position: 'top' } } }} />
      </div>
      <div style={{ marginBottom: 40 }}>
        <h3>Meals vs. Gut Reaction</h3>
        <Bar data={mealsGutData} options={{ responsive: true, plugins: { legend: { display: false } } }} />
      </div>
      <div>
        <h3>Hydration Trends</h3>
        <Line data={hydrationData} options={{ responsive: true, plugins: { legend: { position: 'top' } } }} />
      </div>
    </div>
  );
};

export default Dashboard; 