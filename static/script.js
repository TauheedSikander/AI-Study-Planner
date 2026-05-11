async function generateSchedule() {
  const exam_date = document.getElementById("exam_date").value;

  const subjects = document.getElementById("subjects").value.split(",");

  const hours = document.getElementById("hours").value;

  const response = await fetch("/generate_schedule", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      exam_date: exam_date,
      subjects: subjects,
      hours_per_day: Number(hours),
    }),
  });

  const data = await response.json();

  document.getElementById("scheduleResult").innerText = JSON.stringify(
    data.schedule,
    null,
    2,
  );

  document.getElementById("aiSuggestions").innerText = data.suggestions;
}

let time = 1500;
let timerInterval;

function startTimer() {
  timerInterval = setInterval(() => {
    time--;

    let minutes = Math.floor(time / 60);
    let seconds = time % 60;

    document.getElementById("timer").innerText =
      `${minutes}:${seconds.toString().padStart(2, "0")}`;

    updateProgress();

    if (time <= 0) {
      clearInterval(timerInterval);
      alert("Session complete!");
    }
  }, 1000);
}

function resetTimer() {
  clearInterval(timerInterval);

  time = 1500;

  document.getElementById("timer").innerText = "25:00";
}

let studiedMinutes = 0;
let dailyGoal = 120;

function updateProgress() {
  studiedMinutes++;

  let percent = (studiedMinutes / dailyGoal) * 100;

  if (percent > 100) percent = 100;

  document.getElementById("progress").style.width = percent + "%";

  document.getElementById("progressText").innerText = Math.floor(percent) + "%";
}
