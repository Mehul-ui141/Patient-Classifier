async function predict() {
    console.log("Button clicked ✅");

    const data = {
        temp: parseFloat(document.getElementById("temp").value),
        oxygen: parseFloat(document.getElementById("oxygen").value),
        bp: parseFloat(document.getElementById("bp").value),
        comfort: parseFloat(document.getElementById("comfort").value)
    };

    console.log("Sending:", data);

    const res = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await res.json();

    const resultDiv = document.getElementById("result");

    if (result.prediction === 1) {
        resultDiv.innerHTML = "✅ Sent Home";
        resultDiv.style.color = "#22c55e";
    } else {
        resultDiv.innerHTML = "⚠️ Keep Under Care";
        resultDiv.style.color = "#ef4444";
    }
}