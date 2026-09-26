const goal = 10000;

function calculateSteps() {

    const input = document.getElementById("stepsInput");
    const steps = Number(input.value);

    if (steps < 0 || input.value === "") {
        alert("Please enter a valid number of steps.");
        return;
    }

    const progress = Math.min((steps / goal) * 100, 100);

    const distance = (steps * 0.75) / 1000;

    const calories = steps * 0.04;

    const remaining = Math.max(goal - steps, 0);

    document.getElementById("stepCount").textContent =
        steps.toLocaleString();

    document.getElementById("progressText").textContent =
        progress.toFixed(1) + "%";

    document.getElementById("progress").style.width =
        progress + "%";

    document.getElementById("distance").textContent =
        distance.toFixed(2) + " km";

    document.getElementById("calories").textContent =
        Math.round(calories) + " kcal";

    if (steps >= goal) {

        document.getElementById("message").textContent =
            "🎉 Excellent! You reached your daily goal!";

    } else {

        document.getElementById("message").textContent =
            `🚶 You need ${remaining.toLocaleString()} more steps.`;

    }
}