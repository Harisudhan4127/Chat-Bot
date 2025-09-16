function sendMessage() {
    let input = document.getElementById("userInput");
    let message = input.value.trim();
    if (message === "") return;

    let chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<div class="message user">${message}</div>`;

    fetch("/get", {
        method: "POST",
        body: JSON.stringify({ msg: message }),
        headers: { "Content-Type": "application/json" }
    })
    .then(res => res.json())
    .then(data => {
        chatbox.innerHTML += `<div class="message bot">${data.text}</div>`;

        if (data.images.length > 0) {
            let imgHtml = data.images.map(src => `<img src="${src}" onclick="showImage(this.src)">`).join("");
            chatbox.innerHTML += `<div class="message bot">${imgHtml}</div>`;
        }
        chatbox.scrollTop = chatbox.scrollHeight;
    });

    input.value = "";
}

function showImage(src) {
    let modal = document.getElementById("imageModal");
    let modalImg = document.getElementById("modalImg");
    modal.style.display = "block";
    modalImg.src = src;
}

document.querySelector(".close").onclick = function() {
    document.getElementById("imageModal").style.display = "none";
};
