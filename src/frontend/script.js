const button = document.getElementById("ask");
const questionInput = document.getElementById("question");
const chat = document.getElementById("chat");

button.addEventListener("click", async () => {

    const question = questionInput.value.trim();

    if (!question)
        return;

    questionInput.value = "";

    chat.innerHTML += `
        <div class="message user">
            ${question}
        </div>
    `;

    const aiMessage = document.createElement("div");

    aiMessage.className = "message ai";

    chat.appendChild(aiMessage);

    chat.scrollTop = chat.scrollHeight;

    const response = await fetch("/ask/stream", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            question,

            top_k:5

        })

    });

    const reader = response.body.getReader();

    const decoder = new TextDecoder();

    while(true){

        const {done,value}=await reader.read();

        if(done)
            break;

        aiMessage.textContent += decoder.decode(value, { stream: true } );

        chat.scrollTop = chat.scrollHeight;
    }

    // Flush any remaining buffered bytes.
    aiMessage.textContent += decoder.decode();
});