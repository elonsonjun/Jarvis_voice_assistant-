
const btn = document.getElementById("speakBtn");
const responseEl = document.getElementById("response");

btn.addEventListener("click", () => {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";

  recognition.start();

  recognition.onresult = function (event) {
    const command = event.results[0][0].transcript;
    responseEl.innerText = `You said: "${command}"... thinking...`;

    fetch("http://127.0.0.1:5000/process", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command: command })
    })
    .then(res => res.json())
    .then(data => {
      responseEl.innerText = `Jarvis: ${data.reply}`;
      const utterance = new SpeechSynthesisUtterance(data.reply);
      speechSynthesis.speak(utterance);
    });
  };

  recognition.onerror = function (e) {
    responseEl.innerText = "Error recognizing speech.";
  };
});
