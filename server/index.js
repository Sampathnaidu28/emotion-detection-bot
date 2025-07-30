const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// POST route to send message to FastAPI and return emotion
app.post("/api/emotion", async (req, res) => {
  const { message } = req.body;

  try {
    const response = await axios.post("http://127.0.0.1:8000/predict", {
      text: message,
    });

    res.json(response.data);
  } catch (error) {
    console.error("Error from FastAPI:", error.message);
    res.status(500).json({ error: "Failed to get emotion" });
  }
});

// Start the server
const PORT = 5000;
app.listen(PORT, () => {
  console.log(`Node.js server running at http://localhost:${PORT}`);
});
