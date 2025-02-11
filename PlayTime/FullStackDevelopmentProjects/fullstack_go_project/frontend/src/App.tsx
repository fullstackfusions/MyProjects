import { useState } from "react";
import { fetchGreeting } from "./api";

function App() {
  const [name, setName] = useState("");
  const [greeting, setGreeting] = useState("");

  const handleGreet = async () => {
    if (!name.trim()) return;
    const response = await fetchGreeting(name);
    setGreeting(response);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">Enter Your Name</h1>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        className="px-4 py-2 border border-gray-400 rounded-md text-lg"
        placeholder="Your name..."
      />
      <button
        onClick={handleGreet}
        className="mt-4 px-6 py-3 bg-blue-500 hover:bg-blue-600 text-white rounded-lg text-lg font-semibold"
      >
        Greet Me
      </button>
      {greeting && <p className="mt-4 text-xl font-medium">{greeting}</p>}
    </div>
  );
}

export default App;
