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

Each case contains four suspects.

Every suspect has:

1. A statement describing where they were.
2. An independent record confirming their location.

For three suspects, the statement and record match.

For the culprit, they do not.

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

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Areej554-dev/infinite-case-files.git

Open your web browser and enter:

http://localhost:8000
