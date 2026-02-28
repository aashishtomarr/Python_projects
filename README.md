# 🐍 Python Mini-Projects Collection
Welcome to my collection of Python-based applications! This repository showcases a variety of projects, from CLI-based games to functional utility tools, focusing on logic, user experience, and clean code.

---

## 🚀 Projects Overview

| Project | Description | Key Features |
| :--- | :--- | :--- |
| **[Typing Speed Tool](./Typing-Speed-Calculator)** | A WPM (Words Per Minute) calculator. | Word-wrap formatting, Accuracy %, Net vs Gross WPM. |
| **[RPS Game](./Stone-Paper-Scissors)** | Classic Rock, Paper, Scissors vs CPU. | Score tracking, Randomization logic. |
| **[QR Generator](./QR-Code-Generator)** | Utility to create QR codes from URLs. | External library integration, Image exporting. |
| **[Calculator](./Calculator)** | A clean, logic-based math tool. | Input handling, Arithmetic operations. |
| **[Number Guessing](./Number-Guessing)** | A "Hot or Cold" logic game. | Difficulty levels, Iteration tracking. |

---

## 🛠️ Deep Dive: Typing Speed Calculator
The **Typing Speed Calculator** was built to help users measure their typing efficiency directly from the terminal.

### 📊 How the Math Works
The script calculates speed using the standard **Net WPM** formula:

$$WPM = \frac{\text{Correct Words}}{\text{Time in Seconds} / 60}$$

### ✨ Key Technical Features
* **Intelligent Word Wrap:** Uses the `textwrap` module to ensure the text fits any terminal window width, preventing horizontal scrolling.
* **Accuracy Engine:** Compares the user's input against the target text word-by-word to penalize typos.
* **Performance Tracking:** Distinguishes between "Gross WPM" (raw speed) and "Net WPM" (speed after errors).

---

## 💻 How to Run These Projects

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/aashishtomarr/Python-Projects-Hub.git](https://github.com/aashishtomarr/Python-Projects-Hub.git)
2. Navigate to a project folder:

   Bash
   cd Typing-Speed-Calculator
3. Run the script:

   Bash
   python typing_test.py
   Note: For the QR Code Generator, you will need to install dependencies:
   pip install qrcode[pil]

📈 Learning Journey
This repository tracks my progress in Python. Through these projects, I have mastered:

Standard library modules (time, textwrap, random, datetime).

Data structures (Lists, Dictionaries).

Error handling and input validation.

Git workflow and project organization.

Contact: Aashish - aashishtomar102@gmail.com - https://www.linkedin.com/in/tomaraashish
