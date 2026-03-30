const input = document.getElementById("input");
const messages = document.getElementById("messages");

let dark = false;

function addMessage(text, type) {
  const div = document.createElement("div");

  if (type === "user") {
    div.className =
      "self-end bg-blue-500 text-white px-4 py-2 rounded-xl max-w-[75%]";
  } else {
    div.className =
      "self-start bg-green-500 text-white px-4 py-2 rounded-xl max-w-[75%]";
  }

  div.innerText = text;
  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

function showTyping() {
  const div = document.createElement("div");
  div.id = "typing";
  div.className = "self-start bg-gray-400 text-white px-4 py-2 rounded-xl";
  div.innerText = "Digitando...";
  messages.appendChild(div);
}

function removeTyping() {
  const typing = document.getElementById("typing");
  if (typing) typing.remove();
}

function sendMessage(textParam = null) {
  const text = textParam || input.value;
  if (!text) return;

  addMessage(text, "user");
  showTyping();

  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: text }),
  })
    .then((res) => res.json())
    .then((data) => {
      removeTyping();
      addMessage(data.response, "bot");
    });

  input.value = "";
}

function quick(option) {
  sendMessage(option.toString());
}

input.addEventListener("keypress", function (e) {
  if (e.key === "Enter") sendMessage();
});

function toggleTheme() {
  const body = document.getElementById("body");
  dark = !dark;

  if (dark) {
    body.classList.remove("bg-white");
    body.classList.add("bg-gray-900");
  } else {
    body.classList.remove("bg-gray-900");
    body.classList.add("bg-white");
  }
}

window.onload = () => {
  addMessage(
    `Olá! 👋

O que você quer saber?

1 - O que é Fórmula 1?
2 - O que é DRS?
3 - O que é Pit Stop?
4 - Quem é Lewis Hamilton?
5 - Quem é Max Verstappen?`,
    "bot"
  );
};
