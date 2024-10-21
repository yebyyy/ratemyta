import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const navigate = useNavigate();

  const handleSearch = () => {
    // Assuming you have a route for search results
    navigate('/search-results');
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gradient-to-br from-primary to-secondary">
      <h1 className="text-4xl font-bold text-foreground">Rate My TA</h1>
      <div className="mt-4 flex items-center">
        <input 
          type="text" 
          placeholder="Your TA Here" 
          className="border placeholder:text-lg border-gray-300 rounded-l-lg p-3 w-96 focus:outline-none focus:ring-4 focus:ring-black text-lg"
        />
        <select 
          className="ml-2 border border-gray-300 rounded-lg p-4 text-base text-gray-700 focus:outline-none focus:ring-4 focus:ring-black transition duration-300 ease-in-out"
        >
          <option value="">Select School</option>
          <option value="school1">School 1</option>
          <option value="school2">School 2</option>
          <option value="school3">School 3</option>
          {/* <option value="">Select School</option>
          {schools.map((school) => (
            <option key={school.id} value={school.id}>{school.name}</option>
          ))} */}
        </select>
        <button 
          onClick={handleSearch} 
          className="bg-yellow-500 text-white font-semibold text-lg rounded-r-lg px-8 py-3 ml-2 hover:bg-yellow-400 transition duration-300 transform hover:scale-105 shadow-lg"
        >
          Search
        </button>
      </div>
    </div>
  );
}
