from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EduGenie - Learning Platform</title>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

body {
    background: #f4f7fb;
    color: #1f2937;
}

header {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: white;
    padding: 22px 35px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 27px;
    font-weight: bold;
}

.tagline {
    font-size: 14px;
    opacity: 0.9;
}

.theme-btn {
    background: white;
    color: #4f46e5;
    border: none;
    padding: 10px 15px;
    border-radius: 20px;
    cursor: pointer;
    font-weight: bold;
}

.container {
    display: flex;
    min-height: calc(100vh - 80px);
}

.sidebar {
    width: 220px;
    background: white;
    padding: 25px 15px;
    box-shadow: 2px 0 10px rgba(0,0,0,0.05);
}

.sidebar button {
    width: 100%;
    border: none;
    background: transparent;
    padding: 14px;
    margin: 5px 0;
    text-align: left;
    border-radius: 10px;
    cursor: pointer;
    font-size: 15px;
}

.sidebar button:hover,
.sidebar button.active {
    background: #eef2ff;
    color: #4f46e5;
    font-weight: bold;
}

.content {
    flex: 1;
    padding: 30px;
}.page {
    display: none;
}

.page.active {
    display: block;
}

.welcome {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    padding: 30px;
    border-radius: 18px;
    margin-bottom: 25px;
}

.welcome h1 {
    margin-bottom: 10px;
}

.stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    margin-bottom: 25px;
}

.stat {
    background: white;
    padding: 22px;
    border-radius: 15px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.06);
}

.stat h2 {
    color: #4f46e5;
    margin-bottom: 5px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.06);
}

.card h3 {
    margin-bottom: 10px;
}

.course-icon {
    font-size: 35px;
    margin-bottom: 10px;
}

.progress {
    height: 9px;
    background: #e5e7eb;
    border-radius: 10px;
    margin: 12px 0;
    overflow: hidden;
}

.progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #4f46e5, #8b5cf6);
    border-radius: 10px;
}

.primary-btn {
    background: #4f46e5;
    color: white;
    border: none;
    padding: 11px 18px;
    border-radius: 9px;
    cursor: pointer;
    margin-top: 10px;
}

.primary-btn:hover {
    background: #4338ca;
}

.quiz-box,
.planner-box,
.chat-box,
.notes-box {
    background: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.06);
    margin-top: 20px;
}

.option {
    display: block;
    padding: 12px;
    margin: 8px 0;
    border: 1px solid #ddd;
    border-radius: 9px;
    cursor: pointer;
}

.option:hover {
    background: #f3f4ff;
}

input, textarea {
    width: 100%;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 9px;
    margin: 8px 0;
}

textarea {
    height: 180px;
    resize: vertical;
}

.task {
    background: #f5f3ff;
    padding: 12px;
    margin: 8px 0;
    border-radius: 8px;
}

.chat-messages {
    height: 250px;
    overflow-y: auto;
    background: #f8fafc;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}

.message {
    padding: 10px;
    margin: 7px 0;
    border-radius: 9px;
}

.bot {
    background: #eef2ff;
}

.user {
    background: #dcfce7;
    text-align: right;
}

.dark {
    background: #111827;
    color: #f9fafb;
}

.dark .sidebar,
.dark .stat,
.dark .card,
.dark .quiz-box,
.dark .planner-box,
.dark .chat-box,
.dark .notes-box {
    background: #1f2937;
    color: white;
}

.dark input,
.dark textarea {
    background: #374151;
    color: white;
    border-color: #4b5563;
}

@media(max-width: 800px) {
    .sidebar {
        width: 70px;
    }

    .sidebar button {
        font-size: 0;
        text-align: center;
    }

    .sidebar button:first-letter {
        font-size: 20px;
    }

    .stats,
    .cards {
        grid-template-columns: 1fr;
    }

    .content {
        padding: 15px;
    }
}
</style>
</head>

<body>

<header>
    <div>
        <div class="logo">🎓 EduGenie</div>
        <div class="tagline">Learn smarter. Grow faster.</div>
    </div>
    <button class="theme-btn" onclick="toggleTheme()">🌙 Theme</button>
</header>

<div class="container">

<div class="sidebar">
    <button class="active" onclick="showPage('dashboard', this)">🏠 Dashboard</button>
    <button onclick="showPage('courses', this)">📚 Courses</button>
    <button onclick="showPage('quiz', this)">🧠 Quiz</button>
    <button onclick="showPage('planner', this)">📅 Planner</button>
    <button onclick="showPage('buddy', this)">🤖 Study Buddy</button>
    <button onclick="showPage('notes', this)">📝 Notes</button>
</div>

<div class="content">

<!-- DASHBOARD -->
<section id="dashboard" class="page active">

<div class="welcome">
    <h1>Welcome to EduGenie! 👋</h1>
    <p>Your personal learning space is ready.</p>
</div>

<div class="stats">
    <div class="stat">
        <h2>68%</h2>
        <p>Overall Progress</p>
    </div>

    <div class="stat">
        <h2>12</h2>
        <p>Lessons Completed</p>
    </div>

    <div class="stat">
        <h2>7</h2>
        <p>Day Streak 🔥</p>
    </div>

    <div class="stat">
        <h2>850</h2>
        <p>XP Points ⭐</p>
    </div>
</div>

<h2>Continue Learning</h2>

<div class="cards">

<div class="card">
    <div class="course-icon">🐍</div>
    <h3>Python Programming</h3>
    <p>Learn Python from basics to projects.</p>
    <div class="progress">
        <div class="progress-bar" style="width:75%"></div>
    </div>
    <small>75% completed</small>
</div>

<div class="card">
    <div class="course-icon">🔬</div>
    <h3>Science</h3>
    <p>Explore concepts with interactive learning.</p>
    <div class="progress">
        <div class="progress-bar" style="width:55%"></div>
    </div>
    <small>55% completed</small>
</div>

</div>

</section>


<!-- COURSES -->
<section id="courses" class="page">

<h1>📚 My Courses</h1>

<div class="cards">

<div class="card">
    <div class="course-icon">🐍</div>
    <h3>Python Programming</h3>
    <p>Variables, loops, functions and projects.</p>
    <div class="progress"><div class="progress-bar" style="width:75%"></div></div>
   <button class="primary-btn" onclick="showPage('python', this)">Continue</button>
</div><

<div class="card">
    <div class="course-icon">🔬</div>
    <h3>Science</h3>
    <p>Physics, Chemistry and Biology basics.</p>
    <div class="progress"><div class="progress-bar" style="width:55%"></div></div>
   <button class="primary-btn" onclick="showPage('science', this)">Continue</button>
</div>

<div class="card">
    <div class="course-icon">📐</div>
    <h3>Mathematics</h3>
    <p>Build strong mathematical thinking.</p>
    <div class="progress"><div class="progress-bar" style="width:42%"></div></div>
    <button class="primary-btn" onclick="showPage('mathematics', this)">Continue</button>
</div>

<div class="card">
    <div class="course-icon">📖</div>
    <h3>English</h3>
    <p>Improve grammar, vocabulary and writing.</p>
    <div class="progress"><div class="progress-bar" style="width:60%"></div></div>
    <button class="primary-btn" onclick="showPage('english', this)">Continue</button>
</div>

</div>

</section>


<!-- QUIZ -->
<section id="quiz" class="page">

<h1>🧠 Quick Quiz</h1>

<div class="quiz-box">

<h3 id="question">Which language are we using to build EduGenie?</h3>

<label class="option">
<input type="radio" name="answer" value="Python"> Python
</label>

<label class="option">
<input type="radio" name="answer" value="Java"> Java
</label>

<label class="option">
<input type="radio" name="answer" value="C++"> C++
</label>

<button class="primary-btn" onclick="checkQuiz()">Submit Answer</button>

<p id="quiz-result" style="margin-top:15px;"></p>

</div>

</section>


<section id="python" class="page">

    <h1>🐍 Python Programming</h1>

    <div class="card">
        <h2>Python Basics</h2>
        <p>Learn variables, loops, functions and projects.</p>

<h3>📘 Lesson 1: Python Basics</h3>

<p>
Python is a programming language used to create programs,
websites and useful applications.
</p>

<p>
A Python program can contain instructions that the computer
follows step by step.
</p>
   <h3>📗 Lesson 2: Variables</h3>
<p>
Variables are used to store data in Python.
</p>

<pre>
name = "Alex"
age = 15
</pre>

<p>
Here, <b>name</b> stores text and <b>age</b> stores a number.
</p>

<h3>📙 Lesson 3: Loops</h3>
<p>
Loops help us repeat instructions.
</p>

<pre>
for i in range(5):
    print(i)
</pre>

<p>
This loop prints numbers from 0 to 4.
</p>
 ← Back to Courses
</button>
    </div>

</section>
<!-- SCIENCE -->
<section id="science" class="page">
    <h1>🔬 Science</h1>

    <div class="card">
        <h2>Science Basics</h2>
        <p>Learn Physics, Chemistry and Biology basics.</p>

        <h3>📘 Lesson 1: Introduction to Science</h3>
        <p>
            Science helps us understand the world around us.
            Physics studies matter and energy, Chemistry studies substances,
            and Biology studies living things.
        </p>

        <button class="primary-btn" onclick="showPage('courses', this)">
            🔙 Back to Courses
        </button>
    </div>
</section>
<!-- MATHEMATICS -->
<section id="mathematics" class="page">
    <h1>📐 Mathematics</h1>

    <div class="card">
        <h2>Mathematics Basics</h2>
        <p>Build strong mathematical thinking.</p>

        <h3>📘 Lesson 1: Introduction to Mathematics</h3>
        <p>
            Mathematics helps us understand numbers, patterns,
            shapes and logical thinking.
        </p>

        <button class="primary-btn" onclick="showPage('courses', this)">
            🔙 Back to Courses
        </button>
    </div>
</section>
<!-- ENGLISH -->
<section id="english" class="page">
    <h1>📖 English</h1>

    <div class="card">
        <h2>English Basics</h2>
        <p>Improve grammar, vocabulary and writing.</p>

        <h3>📘 Lesson 1: Introduction to English</h3>
        <p>
            English helps us communicate clearly through speaking,
            reading and writing. Grammar and vocabulary help us
            express our ideas correctly.
        </p>

        <button class="primary-btn" onclick="showPage('courses', this)">
            🔙 Back to Courses
        </button>
    </div>
</section>
<!-- PLANNER -->
<section id="planner" class="page">

<h1>📅 Study Planner</h1>

<div class="planner-box">

<input id="taskInput" placeholder="Enter a study task...">

<button class="primary-btn" onclick="addTask()">Add Task</button>

<div id="tasks">
    <div class="task">📘 Complete Python lesson</div>
    <div class="task">🧠 Take today's quiz</div>
</div>

</div>

</section>


<!-- STUDY BUDDY -->
<section id="buddy" class="page">

<h1>🤖 EduGenie Study Buddy</h1>

<div class="chat-box">

<div class="chat-messages" id="chatMessages">

<div class="message bot">
👋 Hi! I'm your EduGenie Study Buddy. Ask me something!
</div>

</div>

<input id="chatInput" placeholder="Type your question...">

<button class="primary-btn" onclick="sendMessage()">Send</button>

</div>

</section>


<!-- NOTES -->
<section id="notes" class="page">

<h1>📝 My Notes</h1>

<div class="notes-box">

<p>Write your study notes here:</p>

<textarea id="notesArea" placeholder="Start writing your notes..."></textarea>

<button class="primary-btn" onclick="saveNotes()">Save Notes</button>

<p id="noteMessage"></p>

</div>

</section>

</div>
</div>


<script>

function showPage(pageId, button) {

    document.querySelectorAll('.page').forEach(function(page) {
        page.classList.remove('active');
    });

    document.getElementById(pageId).classList.add('active');

    document.querySelectorAll('.sidebar button').forEach(function(btn) {
        btn.classList.remove('active');
    });

    button.classList.add('active');
}


function toggleTheme() {
    document.body.classList.toggle('dark');
}


function checkQuiz() {

    let answer = document.querySelector('input[name="answer"]:checked');
    let result = document.getElementById('quiz-result');

    if (!answer) {
        result.innerHTML = "⚠️ Please select an answer.";
        return;
    }

    if (answer.value === "Python") {
        result.innerHTML = "🎉 Correct! Great job!";
    } else {
        result.innerHTML = "❌ Not quite. Try again!";
    }
}


function addTask() {

    let input = document.getElementById('taskInput');
    let tasks = document.getElementById('tasks');

    if (input.value.trim() === "") {
        return;
    }

    let task = document.createElement('div');
    task.className = "task";
    task.innerHTML = "📌 " + input.value;

    tasks.appendChild(task);

    input.value = "";
}


function sendMessage() {

    let input = document.getElementById('chatInput');
    let messages = document.getElementById('chatMessages');

    if (input.value.trim() === "") {
        return;
    }

    let userMessage = document.createElement('div');
    userMessage.className = "message user";
    userMessage.innerText = input.value;

    messages.appendChild(userMessage);

    let question = input.value.toLowerCase();

    let reply = "🤔 I'm still learning! Try asking me about Python, Science or study tips.";

    if (question.includes("python")) {
        reply = "🐍 Python is a beginner-friendly programming language. Start with variables, conditions, loops and functions.";
    }
    else if (question.includes("study")) {
        reply = "📚 Try studying for 25 minutes, take a short break, and then continue. Consistency is important!";
    }
    else if (question.includes("science")) {
        reply = "🔬 Science becomes easier when you understand concepts instead of memorizing everything.";
    }

    let botMessage = document.createElement('div');
    botMessage.className = "message bot";
    botMessage.innerText = reply;

    messages.appendChild(botMessage);

    input.value = "";
    messages.scrollTop = messages.scrollHeight;
}


function saveNotes() {

    let notes = document.getElementById('notesArea').value;

    localStorage.setItem("edugenie_notes", notes);

    document.getElementById('noteMessage').innerHTML =
        "✅ Notes saved on this browser!";
}


window.onload = function() {

    let savedNotes = localStorage.getItem("edugenie_notes");

    if (savedNotes) {
        document.getElementById('notesArea').value = savedNotes;
    }

};

</script>
</body>
</html>
"""




@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)