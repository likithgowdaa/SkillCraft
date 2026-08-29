# SkillCraft — Software Development Tasks

This repository contains the solutions developed as part of the **SkillCraft Technology Software Development Internship**.

The tasks demonstrate fundamental programming concepts, problem-solving, algorithms, and practical Python development.

## Tasks

| Task    | Project                | Concepts Used                                  |
| ------- | ---------------------- | ---------------------------------------------- |
| Task 01 | Temperature Converter  | Functions, conditionals, user input            |
| Task 02 | Number Guessing Game   | Random numbers, loops, conditionals            |
| Task 03 | Sudoku Solver          | Recursion, backtracking, algorithms            |
| Task 04 | E-commerce Web Scraper | Web scraping, HTTP requests, HTML parsing, CSV |

---

## Task 01 — Temperature Converter

A Python program that converts temperatures between:

* Celsius
* Fahrenheit
* Kelvin

### Concepts

* Functions
* Conditional statements
* User input
* Mathematical operations
* Exception handling

### File

`temperature_converter.py`

---

## Task 02 — Number Guessing Game

A Python game where the computer generates a random number between 1 and 100, and the user attempts to guess it.

The program provides hints such as **"Too high"** or **"Too low"** until the correct number is guessed.

### Concepts

* Python `random` module
* Loops
* Conditional statements
* User input
* Exception handling
* Functions

### File

`number_guessing_game.py`

---

## Task 03 — Sudoku Solver

A Python program that solves a Sudoku puzzle using the **backtracking algorithm**.

The program checks whether a number can be placed in a particular cell and recursively attempts to solve the remaining puzzle. If a choice leads to an invalid solution, the program backtracks and tries another possibility.

### Concepts

* 2D lists
* Functions
* Recursion
* Backtracking
* Nested loops
* Constraint checking

### File

`sudoku_solver.py`

---

## Task 04 — E-commerce Web Scraper

A Python web scraper that extracts product information from an e-commerce practice website.

The scraper collects:

* Product name
* Price
* Rating
* Availability

The extracted information can be stored in a CSV file for further analysis.

### Technologies

* Python
* Requests
* BeautifulSoup
* CSV

### Concepts

* HTTP requests
* HTML parsing
* Web scraping
* Data extraction
* CSV file handling
* Exception handling

### File

`ecommerce_web_scraper.py`

---

## Technologies Used

* **Python 3**
* Requests
* BeautifulSoup
* CSV
* Git
* GitHub

## Installation

For Task 04, install the required Python libraries:

```bash
pip install requests beautifulsoup4
```

Or, if a `requirements.txt` file is provided:

```bash
pip install -r requirements.txt
```

## How to Run

Navigate to the directory containing the required Python file and run:

```bash
python filename.py
```

For example:

```bash
python temperature_converter.py
```

## Repository Structure

```text
SkillCraft/
│
├── Task-01/
│   └── temperature_converter.py
│
├── Task-02/
│   └── number_guessing_game.py
│
├── Task-03/
│   └── sudoku_solver.py
│
├── Task-04/
│   └── ecommerce_web_scraper.py
│
└── README.md
```

## Learning Outcomes

Through these tasks, the following skills were practiced:

* Python programming fundamentals
* Problem-solving and logical thinking
* Functions and modular programming
* Loops and conditional statements
* Exception handling
* Recursion and backtracking
* Working with external Python libraries
* Web scraping and HTML parsing
* File and CSV handling
* Git and GitHub version control

## Author

**Likith R**

Software Development Intern
SkillCraft Technology
SDI
