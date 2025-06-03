import React, { useState } from 'react';

const FoodIntakeForm = () => {
  const [foodIntake, setFoodIntake] = useState('');
  const [digestiveSymptoms, setDigestiveSymptoms] = useState('');
  const [mood, setMood] = useState('');
  const [activityLevel, setActivityLevel] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // TODO: handle form submission (e.g., send to backend)
    const formData = {
      foodIntake,
      digestiveSymptoms,
      mood,
      activityLevel,
    };
    alert('Form submitted!');
    console.log(formData);
  };

  return (
    <form onSubmit={handleSubmit} style={{ maxWidth: 400, margin: '0 auto' }}>
      <h2>Daily Health Log</h2>
      <div style={{ marginBottom: 16 }}>
        <label>Food Intake<br />
          <textarea
            name="foodIntake"
            value={foodIntake}
            onChange={e => setFoodIntake(e.target.value)}
            placeholder="Describe what you ate today..."
            rows={3}
            style={{ width: '100%' }}
            required
          />
        </label>
      </div>
      <div style={{ marginBottom: 16 }}>
        <label>Digestive Symptoms<br />
          <input
            type="text"
            name="digestiveSymptoms"
            value={digestiveSymptoms}
            onChange={e => setDigestiveSymptoms(e.target.value)}
            placeholder="e.g., bloating, cramps, none"
            style={{ width: '100%' }}
          />
        </label>
      </div>
      <div style={{ marginBottom: 16 }}>
        <label>Mood<br />
          <select
            name="mood"
            value={mood}
            onChange={e => setMood(e.target.value)}
            style={{ width: '100%' }}
            required
          >
            <option value="">Select mood</option>
            <option value="happy">Happy</option>
            <option value="neutral">Neutral</option>
            <option value="sad">Sad</option>
            <option value="anxious">Anxious</option>
            <option value="energetic">Energetic</option>
            <option value="tired">Tired</option>
          </select>
        </label>
      </div>
      <div style={{ marginBottom: 16 }}>
        <label>Activity Level<br />
          <select
            name="activityLevel"
            value={activityLevel}
            onChange={e => setActivityLevel(e.target.value)}
            style={{ width: '100%' }}
            required
          >
            <option value="">Select activity level</option>
            <option value="sedentary">Sedentary</option>
            <option value="light">Light</option>
            <option value="moderate">Moderate</option>
            <option value="active">Active</option>
            <option value="very active">Very Active</option>
          </select>
        </label>
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default FoodIntakeForm; 