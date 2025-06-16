
# Jarvis - Local Voice Assistant

This is a basic local voice assistant named **Jarvis**. It includes a simple frontend and a Flask-based backend.

## Features
- Voice input (using Web Speech API)
- Flask backend to process commands
- Speech output
- Supports: time, weather, Wikipedia, jokes, basic web navigation

## Setup Instructions

1. Clone or unzip the folder.
2. Install Python packages:
    ```bash
    pip install flask pyttsx3 wikipedia requests
    ```

3. Replace `"YOUR_OPENWEATHER_API_KEY"` in `app.py` with your OpenWeatherMap API key.

4. Run the backend:
    ```bash
    python app.py
    ```

5. Open `index.html` in your browser.
6. Click "Speak" and try commands like:
    - "What time is it?"
    - "Search Wikipedia for Python"
    - "Tell me a joke"
    - "Open Google"
    - "What's the weather?"

Enjoy using your local Jarvis assistant!

---

Built by ChatGPT
