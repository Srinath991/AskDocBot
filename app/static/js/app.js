document.getElementById("uploadForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    const fileInput = document.getElementById("file");
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("/upload/", {
        method: "POST",
        body: formData,
    });

    const result = await response.json();
    alert(result.message);
});

document.getElementById("askBtn").addEventListener("click", async function () {
    const questionInput = document.getElementById("question");
    const question = questionInput.value.trim();
    const chatWindow = document.getElementById("chatWindow");
    const loading = document.getElementById("loading");

    if (!question) {
        alert("Please enter a question!");
        return;
    }

    // Append user's question
    const userMessage = document.createElement("div");
    userMessage.className = "chat-bubble user-message";
    userMessage.textContent = question;
    chatWindow.appendChild(userMessage);
    questionInput.value = "";

    // Scroll chat window
    chatWindow.scrollTop = chatWindow.scrollHeight;

    // Show loading dots
    loading.style.display = "flex";

    try {
        const response = await fetch(`/query/?question=${encodeURIComponent(question)}`);
        const result = await response.json();

        // Append bot's response
        const botMessage = document.createElement("div");
        botMessage.className = "chat-bubble bot-message";
        botMessage.textContent = result.answer || "Sorry, I couldn't find an answer.";
        chatWindow.appendChild(botMessage);
    } catch (error) {
        alert("An error occurred. Please try again.");
    } finally {
        loading.style.display = "none";
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
});
