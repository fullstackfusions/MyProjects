import axios from "axios";

export const fetchGreeting = async (name: string) => {
    try {
        const response = await axios.get(`http://localhost/greet?name=${name}`);
        return response.data;
    } catch (error) {
        console.error("Error fetching greeting:", error);
        return "Error fetching greeting.";
    }
};
