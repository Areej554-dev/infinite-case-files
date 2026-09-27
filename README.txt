# 🕵️ Infinite Case Files

> A procedural detective game built with Python, HTML, CSS, and JavaScript.

## 📌 About the Project

**Infinite Case Files** is a browser-based detective game where every case is generated automatically.

The player investigates a collection of suspects, statements, and independent records to identify the culprit. Instead of using a fixed set of cases, the Python program generates new combinations of suspects, locations, items, motives, and evidence.

The goal is simple:

**Find the suspect whose statement contradicts the independent evidence.**

---

## 🎮 Features

- 🔍 Procedurally generated detective cases
- 👥 4 suspects in every case
- 📋 Randomized statements and evidence
- 🎲 Random suspects, locations, items, and motives
- 🔀 Shuffled evidence for every case
- 🧠 Logic-based culprit identification
- ♾️ Replayable cases
- 🌐 Browser-based interface
- 🎨 Custom HTML/CSS interface
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
