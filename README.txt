# 🕵️ Infinite Case Files

> A procedurally generated detective game built with Python, HTML, CSS, and JavaScript.

## 📌 About the Project

**Infinite Case Files** is a browser-based detective game where every case is generated automatically.

The player investigates a group of suspects, their statements, and independent records to identify the culprit. Instead of relying on a fixed set of cases, the Python program generates new combinations of suspects, locations, items, motives, and evidence every time.

**The goal is simple:** find the suspect whose statement contradicts the independent evidence.

---

## 🎮 Features

- 🔍 Procedurally generated detective cases
- 👥 4 suspects in every case
- 📋 Randomized statements and evidence
- 🎲 Random suspects, locations, items, and motives
- 🔀 Shuffled evidence for every case
- 🧠 Logic-based culprit identification
- ♾️ Endlessly replayable
- 🌐 Browser-based interface
- 🎨 Custom HTML/CSS design
- ⚡ JavaScript-powered interaction
- 🐍 Python-powered case generation
- 📦 No external Python packages required

---

## 🧩 How It Works

Each case contains four suspects. Every suspect has:

1. **A statement** describing where they claim to have been.
2. **An independent record** confirming where they actually were.

For three suspects, the statement and the record match. For the culprit, they do not.

### Example

```text
Alex
Statement: Hotel
Record:    Hotel

Sara
Statement: Museum
Record:    Museum

Daniel
Statement: Cafe
Record:    Office   ← Contradiction

Emma
Statement: Gallery
Record:    Gallery
```

In this case, **Daniel** is the culprit: he said he was at the cafe, but the record places him at the office.

---

## 🚀 How to Run

### Requirements

- Python 3.8 or newer
- Any modern web browser

### 1. Clone the repository

```bash
git clone https://github.com/Areej554-dev/infinite-case-files.git
cd infinite-case-files
```

### 2. Start the game

```bash
python app.py
```

> Replace `app.py` with the name of your main Python file if it is different.

### 3. Open it in your browser

Go to:

```text
http://localhost:8000
```

---
