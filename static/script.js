function toggleChat() {
    const chatPopup = document.getElementById("chatPopup");
    chatPopup.style.display = chatPopup.style.display === "flex" ? "none" : "flex";
}

function sendMessage() {
    const input = document.getElementById("userInput");
    const msg = input.value.trim();
    if (!msg) return;

    const chatBox = document.getElementById("chatMessages");
    const userBubble = document.createElement("div");
    userBubble.textContent = "You: " + msg;
    chatBox.appendChild(userBubble);

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        const botBubble = document.createElement("div");
        botBubble.textContent = "Meta AI: " + data.reply;
        chatBox.appendChild(botBubble);
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    input.value = "";
}
