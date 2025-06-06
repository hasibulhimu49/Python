# Python Learning Roadmap 🐍

A structured, project‑oriented guide from absolute beginner to practical machine‑learning developer.

---

## How to Use This Roadmap

1. **One milestone per week** (≈ 7–10 hrs).
2. Work through the resources, then complete the **mini‑project** before ticking the box.
3. Keep notes and commit code to GitHub to track progress.

Legend ⬜ Not started ▣ In progress ✅ Completed

---

## 0 Environment & Tooling (Day 0–1)

* ⬜ Install Python 3.12+
* ⬜ Set up a virtual environment (`python -m venv venv`)
* ⬜ Pick an IDE (VS Code / PyCharm / JupyterLab)
* ⬜ Run **Hello World**

**Resources** Python Downloads • [VS Code Docs](https://code.visualstudio.com/docs)

Mini‑project Create a CLI app that greets users by name.

---

## 1 Fundamentals (Week 1)

* ⬜ Syntax & indentation
* ⬜ Comments
* ⬜ Variables & data types (`int`, `float`, `str`, `bool`, `list`, `tuple`, `dict`, `set`)
* ⬜ Type conversion & casting
* ⬜ Input/Output (`input()`, `print()`)
* ⬜ Operators (arithmetic, comparison, logical, assignment, bitwise)

Mini‑project Simple calculator that supports + – × ÷ and keeps a history.

Resources [Python Tutorial §3‑5](https://docs.python.org/3/tutorial/) • W3Schools Python Basics

---

## 2 Control Flow (Week 2)

* ⬜ Conditionals (`if … elif … else`)
* ⬜ Loops (`for`, `while`)
* ⬜ Loop control (`break`, `continue`, `pass`)
* ⬜ List comprehensions

Mini‑project Number‑guessing game with unlimited tries and replay option.

---

## 3 Functions & Modules (Week 3)

* ⬜ Define & call functions (`def`, `return`)
* ⬜ Arguments (positional, keyword, default, `*args`, `**kwargs`)
* ⬜ Lambda expressions
* ⬜ `import` built‑in modules (`math`, `datetime`)
* ⬜ Create a custom module & package

Mini‑project Tiny **utility library** (e.g., string helpers) published on GitHub.

---

## 4 Core Data Structures (Week 4)

* ⬜ Lists ‑ operations, slicing, mutating, methods
* ⬜ Tuples ‑ immutability, unpacking
* ⬜ Sets ‑ uniqueness, set algebra
* ⬜ Dictionaries ‑ key/value ops, comprehension
* ⬜ Strings ‑ methods, f‑strings, formatting

Mini‑project Contact‑book CLI that stores, searches, and sorts contacts in memory.

---

## 5 File & Error Handling (Week 5)

* ⬜ File I/O (`open`, `with` context manager)
* ⬜ Read & write text, JSON, and CSV
* ⬜ Exception handling (`try`, `except`, `else`, `finally`, `raise`)

Mini‑project CSV‑based todo‑list manager with persistent storage.

---

## 6 Object‑Oriented Programming (Weeks 6‑7)

* ⬜ Classes & objects
* ⬜ Constructors (`__init__`)
* ⬜ Instance vs class variables & methods (`@classmethod`)
* ⬜ Inheritance & polymorphism
* ⬜ Method overriding & MRO
* ⬜ Encapsulation & abstraction (properties, `@staticmethod`)

Mini‑project Text‑based RPG with character subclasses and inventory system.

---

## 7 Intermediate Language Features (Week 8)

* ⬜ Decorators
* ⬜ Generators & `yield`
* ⬜ Iterators & iterables (`__iter__`, `__next__`)
* ⬜ Context managers (`with`, `__enter__`, `__exit__`)

Mini‑project URL crawler that lazily fetches pages using generators.

---

## 8 Popular Libraries & Frameworks (Weeks 9‑12)

* ⬜ NumPy arrays & broadcasting
* ⬜ Pandas Series, DataFrames, groupby
* ⬜ Matplotlib basic plots • (bonus: Seaborn aesthetics)
* ⬜ Scikit‑Learn train/test split, pipelines
* ⬜ Flask micro‑web‑app with REST endpoints (bonus: Django overview)
* ⬜ TensorFlow *or* PyTorch build a simple neural network

Mini‑project End‑to‑end ML notebook: load data → clean → train → evaluate → serve via Flask.

---

## 9 Databases & APIs (Week 13)

* ⬜ SQLite CRUD with `sqlite3`
* ⬜ Connect to MySQL/PostgreSQL via `sqlalchemy`
* ⬜ Consume REST APIs with `requests`
* ⬜ Design & document your own JSON API

Mini‑project Blog backend storing posts in SQLite and exposing a REST API.

---

## 10 Automation & Scripting (Week 14)

* ⬜ Web scraping BeautifulSoup / Scrapy
* ⬜ Selenium browser automation
* ⬜ `os` & `pathlib` for file ops

Mini‑project Automated script that downloads daily currency rates and appends them to a CSV.

---

## 11 Concurrency & Parallelism (Week 15)

* ⬜ `threading` threads vs GIL
* ⬜ `multiprocessing` CPU‑bound tasks
* ⬜ Async IO `async`, `await`, `asyncio`

Mini‑project Concurrent image‑downloader using both threads and async IO.

---

## 12 Testing, Packaging & Deployment (Week 16)

* ⬜ Unit testing with `unittest` / `pytest`
* ⬜ Virtual environments & `pip`
* ⬜ Build a wheel & publish to PyPI (test index)
* ⬜ Dockerize your Flask app

Mini‑project CI workflow (GitHub Actions) that runs tests and builds a Docker image.

---

### 🎯 Capstone Project (Weeks 17‑18)

Pick a real‑world problem (e.g., heart‑disease classification) and deliver:

1. Data acquisition & EDA
2. ML model with Scikit‑Learn / PyTorch
3. REST API or Streamlit dashboard
4. Docker + GitHub Actions deployment

---

## Additional Resources

* **Python Docs** [https://docs.python.org/3](https://docs.python.org/3)
* **Real Python** [https://realpython.com](https://realpython.com)
* **FreeCodeCamp YouTube Python Course**
* **Automate the Boring Stuff** by A. Sweigart
* **DataCamp Python Tracks**

