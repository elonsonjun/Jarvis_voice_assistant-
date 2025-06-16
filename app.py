
from flask import Flask, request, jsonify
import datetime
import wikipedia
import webbrowser
import pyttsx3
import requests
import random

app = Flask(__name__)
engine = pyttsx3.init()
WEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"  # Replace this

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    command = command.lower()

    if "hello" in command:
        return "Hello, I am Jarvis. How can I help you?"
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."
    elif "weather" in command:
        city = "New York"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        res = requests.get(url).json()
        if res["cod"] == 200:
            temp = res["main"]["temp"]
            desc = res["weather"][0]["description"]
            return f"It's {temp}°C with {desc} in {city}."
        else:
            return "I couldn't fetch weather info."
    elif "search wikipedia" in command:
        try:
            topic = command.replace("search wikipedia for", "").strip()
            summary = wikipedia.summary(topic, sentences=2)
            return summary
        except:
            return "Sorry, no result from Wikipedia."
    elif "joke" in command:
        jokes = [
            "Why do programmers hate nature? Too many bugs.",
            "Debugging is like being a detective in a crime movie.",
            "Why did the developer go broke? Because he used up all his cache."
        ]
        return random.choice(jokes)
    elif "your name" in command:
        return "I am Jarvis, your virtual assistant."
    else:
        return "Sorry, I didn’t understand that."

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    command = data.get("command", "")
    response = process_command(command)
    speak(response)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
