async function calculate(operation) {
    const num1 = document.getElementById("num1").value;
    const num2 = document.getElementById("num2").value;
    const result = document.getElementById("result");

    if (num1 === "" || num2 === "") {
        result.innerText = "Please enter both numbers!";
        return;
    }

    try {
        const response = await fetch("/calculate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                num1: num1,
                num2: num2,
                operation: operation
            })
        });

        const data = await response.json();

        if (!response.ok) {
            result.innerText = data.error;
            return;
        }

        result.innerText = "Result: " + data.result;

    } catch (error) {
        result.innerText = "Error connecting to server!";
        console.error(error);
    }
}
function clearCalculator() {
    document.getElementById("num1").value = "";
    document.getElementById("num2").value = "";
    document.getElementById("result").innerText =
        "Your result will appear here";
}