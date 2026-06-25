# Student Information Database

A comprehensive Python desktop application built with Tkinter for managing student records, including viewing, adding, removing, and modifying student information, as well as visualizing data through plots.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [File Structure](#file-structure)
- [Data Storage](#data-storage)
- [Dependencies](#dependencies)
- [GUI Overview](#gui-overview)
- [Code Organization](#code-organization)
- [Known Issues & Limitations](#known-issues--limitations)
- [Future Improvements](#future-improvements)
- [Acknowledgments](#acknowledgments)

---

## 📖 Overview

This project was developed as the **final project for the Python course** at **Jahad Daneshgahi of Tehran University**. 

This project is a **Student Information Database** application built using Python's Tkinter library. It allows users to manage student records through a graphical user interface (GUI). The application supports five main functionalities:

1. **View the list of students**
2. **Add a new student**
3. **Remove a student**
4. **Change a student's information**
5. **Visualize student data on plots**

The data is stored locally in text files, making it lightweight and portable.

---

## ✨ Features

### 1️⃣ View Student List
- Displays a complete list of all students with their:
  - Student Number
  - Name
  - Entry Year
  - Midterm Score
  - Final Score
- Data is presented in a clean, tabular format with separators.

### 2️⃣ Add a Student
- Input fields for:
  - Student Number (numeric, range: 1350-1430)
  - Full Name
  - Entry Year (numeric, range: 1350-1430)
  - Midterm Score (numeric, range: 0-20)
  - Final Score (numeric, range: 0-20)
- Validation for numeric ranges and data types.
- Confirmation pop-up before saving.

### 3️⃣ Remove a Student
- Search for a student by **Student Number**.
- Display the student's full information.
- Remove the student after confirmation.

### 4️⃣ Change Student Information
- Search for a student by **Student Number**.
- Choose what to change from a dropdown menu:
  - Name
  - Entry Year
  - Midterm Score
  - Final Score
  - All of the above
- Input new data with validation.
- Confirm changes before saving.

### 5️⃣ Visualize Data on Plots
Two types of visualizations:
- **Histograms**: Show the distribution of students by:
  - Entry Year
  - Midterm Scores
  - Final Scores
- **Line Plots**: Show annual averages of:
  - Midterm Scores
  - Final Scores

---

## 🛠️ Installation

### Prerequisites
- Python 3.x installed on your system
- Required Python libraries (see [Dependencies](#dependencies))

### Steps

1. **Clone or download the project files** to your local machine.

2. **Ensure all files are in the same directory:**
   - `aaProject_C_F.py` (main logic and GUI windows)
   - `aaaProject.py` (main menu entry point)
   - `Final Project.pdf` (project documentation - optional)
   - `logo.png` (application icon - optional)

3. **Install the required dependencies:**

```bash
pip install numpy matplotlib
```

4. **Run the application:**

```bash
python aaaProject.py
```

---

## 🚀 Usage Guide

### Starting the Application
Run `aaaProject.py` to launch the main menu window.

### Main Menu Options
The main menu displays five buttons corresponding to the application's core features. Click any button to open a new window.

### Adding a Student
1. Click **"2. Add a student"**.
2. Fill in all fields (Student Number, Name, Entry Year, Midterm, Final).
3. Click **"Add"**.
4. Confirm your entry in the pop-up window.

### Removing a Student
1. Click **"3. Remove a student"**.
2. Enter the student's number in the search field.
3. Click **"Search"** to display the student's information.
4. Click **"Remove"** and confirm the deletion.

### Changing Student Information
1. Click **"4. Change a student's info"**.
2. Enter the student's number and click **"Search"**.
3. Select what you want to change from the dropdown menu.
4. Enter the new value(s) in the provided fields.
5. Click **"Change"** and confirm.

### Viewing Plots
1. Click **"5. See the student's information on plot"**.
2. **Histogram Section**:
   - Choose between **Year**, **Midterm**, or **Final**.
   - Click **"Show"** to display the histogram.
3. **Line Plot Section**:
   - Choose between **Midterm** or **Final** annual averages.
   - Click **"Show"** to display the line plot.

---

## 📁 File Structure

```
project_root/
├── aaProject_C_F.py        # Core application logic and GUI functions
├── aaaProject.py           # Main menu entry point
├── Final Project.pdf       # Persian project documentation
├── logo.png                # Application icon
├── Number.txt              # Student numbers (auto-generated)
├── Name.txt                # Student names (auto-generated)
├── Year.txt                # Entry years (auto-generated)
├── Midterm.txt             # Midterm scores (auto-generated)
├── Final.txt               # Final scores (auto-generated)
└── README.md               # This file
```

> **Note:** The `.txt` files are automatically created when the application runs for the first time.

---

## 💾 Data Storage

All data is stored in simple text files, one per attribute:

| File | Format | Description |
|------|--------|-------------|
| `Number.txt` | Integer | Student numbers (e.g., 14001234) |
| `Name.txt` | String | Student full names |
| `Year.txt` | Integer | Entry year (1350-1430) |
| `Midterm.txt` | Float | Midterm score (0-20) |
| `Final.txt` | Float | Final score (0-20) |

Each file stores one record per line. The first line is empty (reserved for headers).

---

## 📦 Dependencies

| Library | Purpose |
|---------|---------|
| **Tkinter** | GUI framework (built-in with Python) |
| **NumPy** | Numerical operations for data processing |
| **Matplotlib** | Plotting and data visualization |

---

## 🖥️ GUI Overview

### Design
- **Color Scheme**: Light green background (`#F0FFF0`) with color-coded elements:
  - Pink (`#C71585`) for titles
  - Blue (`#0000CD`) for labels and text
  - Green (`#006400`) for data display
- **Responsive**: Windows are fixed-size (500x500) with disabled resizing.
- **Icon**: Uses `logo.png` if available.

### Windows
1. **Main Menu** - Central hub with five action buttons.
2. **View List** - Displays all student records in a table format.
3. **Add Student** - Input form with validation and confirmation.
4. **Remove Student** - Search, display, and delete functionality.
5. **Change Info** - Search, select attribute, modify, and confirm.
6. **Plots** - Two visualization sections with radio button selection.

---

## 🧩 Code Organization

### `aaProject_C_F.py` (Core Logic)
- **File Handling Functions**: `number()`, `name()`, `year()`, etc.
- **Utility Classes**:
  - `FileToList`: Converts file content to a list of strings.
  - `TxttoFloatList`: Converts file content to a list of floats.
  - `ListSearch`: Searches for items in a list and returns indices.
- **Utility Functions**: `getitem()`, `error2()`
- **Window Creation Functions**: `creat1()` through `creat5()`

### `aaaProject.py` (Main Menu)
- Sets up the main application window.
- Imports functions from `aaProject_C_F.py`.
- Creates buttons for each feature.

---

## ⚠️ Known Issues & Limitations

1. **Data Validation**:
   - Midterm and Final scores are validated as integers, but the system accepts floats.
   - The search function displays an error message but doesn't clear it automatically.

2. **File Handling**:
   - Files are opened and closed repeatedly, which can be inefficient.
   - No file locking mechanism for concurrent access.

3. **GUI Limitations**:
   - Windows are fixed-size (500x500), which may cut off longer names.
   - No scrollbar for the student list view.

4. **Data Integrity**:
   - No unique constraint for student numbers (duplicates are allowed).
   - Deleting a student doesn't reindex the student numbers.

5. **Error Handling**:
   - `error2()` pop-up doesn't specify which field has invalid data.
   - Some exceptions are caught with `pass` (silent failure).

---

## 🚧 Future Improvements

- [ ] **Database Integration**: Replace text files with SQLite for better data management.
- [ ] **Search Enhancements**: Allow searching by name, year, or score ranges.
- [ ] **Export/Import**: Support CSV or Excel file export/import.
- [ ] **Data Validation**: Improve validation with detailed error messages.
- [ ] **Responsive UI**: Make windows resizable and add scrollbars.
- [ ] **Data Visualization**: Add more plot types (scatter plots, box plots).
- [ ] **Logging**: Add logging for debugging and user actions.
- [ ] **Unit Tests**: Implement tests for core functions.
- [ ] **Theme Support**: Allow users to switch between color themes.
- [ ] **Keyboard Shortcuts**: Add keyboard shortcuts for common actions.

---

## 📝 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- This project was created as the final project for the Python course at **Jahad Daneshgahi of Tehran University**.
- Thanks to the **Matplotlib** and **NumPy** communities for their excellent libraries.
- Thanks to the **Tkinter** documentation for GUI development.
  
---

**Happy Coding!** 🎓
