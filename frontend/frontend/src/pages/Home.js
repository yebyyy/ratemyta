import React from 'react';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const [schools, setSchools] = useState([]);
  const [searchTerm, setSearchTerm] = useState('')

  useEffect(() => {
    // Fetch the list of schools from the backend or static JSON file
    fetch('/api/schools')
      .then(response => response.json())
      .then(data => setSchools(data))
      .catch(error => console.error('Error fetching schools:', error));
  }, []);
  const navigate = useNavigate();

  const handleSearch = () => {
    // Assuming you have a route for search results
    navigate('/search-results');
  };
  const handleSignIn = () => {
    navigate('/sign-in');
  };

  const handleRegister = () => {
    navigate('/register');
  };
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gradient-to-br from-primary to-secondary">
      <h1 className="text-5xl text-black tracking-wide leading-tight font-suse mb-6">Rate My TA</h1>
      <header className="w-full flex justify-end items-center px-8 py-4 absolute top-0 right-0">
        <div className="flex space-x-4">
          <button
            onClick={handleSignIn}
            className="text-black font-semibold text-lg hover:underline"
          >
            Log in
          </button>
          <button
            onClick={handleRegister}
            className="bg-yellow-300 text-black font-semibold hover:text-white text-lg rounded-full px-6 py-2 hover:bg-gray-800 transition duration-300"
          >
            Sign up
          </button>
        </div>
      </header>
      <div className="mt-4 flex items-center">
      <div className="relative w-96">
      <input 
            type="text" 
            placeholder="Your TA Here" 
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            onKeyPress={handleKeyPress}
            className="border-none rounded-full p-4 w-full shadow-lg text-lg text-gray-700 focus:outline-none focus:ring-4 focus:ring-black transition duration-300 ease-in-out"
          />
          <div className="absolute top-1/2 transform -translate-y-1/2 right-4 cursor-pointer" onClick={handleSearch}>
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth="2">
              <path strokeLinecap="round" strokeLinejoin="round" d="M21 21l-4.35-4.35M16.65 16.65A7.5 7.5 0 1116.65 2a7.5 7.5 0 010 14.65z" />
            </svg>
          </div>
        </div>
        <select 
          value={schools}
          onChange={(e) => setSchools(e.target.value)}
          className="ml-4 border-none rounded-full p-4 text-md text-gray-700 shadow-lg focus:outline-none focus:ring-4 focus:ring-black transition duration-300 ease-in-out"
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
      </div>
    </div>
  );
}
