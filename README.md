# SCT_CT_3
Strength of a Password


Here is the **GitHub-styled, polished, professional README.md** — ready to upload directly to your repository.

---

# 🔐 Password Strength Checker

A simple and interactive **Python-based tool** that evaluates the strength of a password based on essential cybersecurity criteria.
This project helps users understand and improve password quality through clear feedback and scoring.

---

## ✨ Features

This tool evaluates a password using **five key criteria**:

| Criterion              | Description                      |
| ---------------------- | -------------------------------- |
| **Length**             | At least 8 characters            |
| **Uppercase Letters**  | Contains A–Z                     |
| **Lowercase Letters**  | Contains a–z                     |
| **Digits**             | Contains numbers 0–9             |
| **Special Characters** | Contains symbols like !@#$%^&*() |

Each satisfied condition adds **1 point** (maximum score: 5).

### 🏆 Strength Levels

| Score   | Strength       |
| ------- | -------------- |
| **5**   | 🟢 Very Strong |
| **4**   | 🟩 Strong      |
| **3**   | 🟨 Moderate    |
| **2**   | 🟧 Weak        |
| **0–1** | 🔴 Very Weak   |

---

## 📁 Project Structure

```
password-strength-checker/
│
├── password_checker.py     # Main program
└── README.md               # Documentation
```

---

## ▶️ How to Run

### **1. Clone the repository**

```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
```

### **2. Run the script**

```bash
python password_checker.py
```

---

## 🖥️ Sample Output

```
===================================
=== P Y T H O N   P A S S W O R D   C H E C K E R ===
===================================
Enter a password to check: Hello@123

--- Password Strength Report ---
Password: Hello@123
----------------------------------
| Criterion             | Met? |
----------------------------------
| Length (>=8)          | ✅    |
| Uppercase Letter (A-Z)| ✅    |
| Lowercase Letter (a-z)| ✅    |
| Digit (0-9)           | ✅    |
| Special Char (!@#$...)| ✅    |
----------------------------------
Total Score: 5 / 5

Overall Strength: Very Strong
Tip: Aim for 'Strong' or 'Very Strong'!
```

---


## 💡 Why This Tool?

* ✔ Beginner-friendly example of conditional logic
* ✔ Helpful for teaching password security basics
* ✔ Works instantly — no external libraries needed
* ✔ Can be integrated into signup forms or security modules
