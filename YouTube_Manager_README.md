
# YouTube Manager

**YouTube Manager** is a command-line application that allows users to manage a database of YouTube videos. 
Built with **Python** and **SQLite**, this project demonstrates how to perform basic CRUD (Create, Read, Update, Delete) operations through a simple menu-driven interface.

![YouTube Manager Screenshot](./image.png)

---

## Features

1. **List Videos**: View all video entries stored in the SQLite database.
2. **Add Video**: Add a new video by providing its name and duration.
3. **Update Video**: Modify the details of an existing video using its unique ID.
4. **Delete Video**: Remove a video entry from the database using its unique ID.

---

## Built With

- **Python**: The core programming language used.
- **SQLite**: A lightweight and embedded database.
- **Command-Line Interface (CLI)**: Enables easy interaction via terminal.

---

## How to Download and Run the Project

### Step 1: Clone the Repository

1. Visit the GitHub repository link: **[GitHub Repository Link](https://github.com/YourGitHubUsername/youtube-manager)**.
2. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/YourGitHubUsername/youtube-manager.git
   ```
3. Navigate into the project directory:
   ```bash
   cd youtube-manager
   ```

---

### Step 2: Install Python

Ensure Python 3.10+ is installed. Download it from [Python's official website](https://www.python.org/).

---

### Step 3: Run the Application

1. Open a terminal/command prompt in the project directory.
2. Run the main Python script:
   ```bash
   python youtube_manager_db.py
   ```
3. Use the on-screen menu options to manage videos:
   - Press `1` to list videos.
   - Press `2` to add a video.
   - Press `3` to update a video.
   - Press `4` to delete a video.
   - Press `5` to exit the program.

---

## How to Rebuild This Project from Scratch

If you'd like to build the project on your own, here’s how you can do it:

1. **Set Up a Python Environment**:
   ```bash
   python -m venv env
   source env/bin/activate   # For macOS/Linux
   env\Scripts\activate    # For Windows
   ```

2. **Create a SQLite Database**:
   Use Python's `sqlite3` library to initialize the database:
   ```python
   import sqlite3
   con = sqlite3.connect("youtube_videos.db")
   cur = con.cursor()
   cur.execute('''CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, name TEXT NOT NULL, time TEXT NOT NULL)''')
   con.commit()
   con.close()
   ```

3. **Build the Python Script**:
   Implement CRUD operations using Python functions like `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.

4. **Create a Menu-Driven Interface**:
   Use Python’s `input()` and `match-case` syntax for user interaction.

---

## How to Improve This Project

Here are some ways to enhance the functionality:

1. **Convert CLI to GUI**:
   - Use libraries like `Tkinter` or `PyQt` to build a user-friendly graphical interface.

2. **Web-Based Interface**:
   - Build a web application using Flask or FastAPI and deploy it online.

3. **Error Handling**:
   - Add validation checks for user inputs and handle invalid entries gracefully.

4. **Cloud Database Integration**:
   - Replace SQLite with a cloud-based database like PostgreSQL or Firebase for scalability.

5. **Search and Filter**:
   - Add advanced search capabilities to filter videos based on duration or name.

6. **Export Data**:
   - Include functionality to export video details to a CSV or JSON file.

7. **Analytics Dashboard**:
   - Create an analytics dashboard showing statistics like total video duration.

---

## Repository Link

**GitHub Link**: [Your GitHub Repository](https://github.com/YourGitHubUsername/youtube-manager)

1. Clone the repository:
   ```bash
   git clone https://github.com/YourGitHubUsername/youtube-manager.git
   ```
2. Navigate to the directory:
   ```bash
   cd youtube-manager
   ```

---

## Download README

You can download the README file here: [Download README.md](./YouTube_Manager_README.md)

---

Let me know if you need additional help with any of these steps or further improvements!
