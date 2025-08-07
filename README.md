# Generating Data – Python Crash Course, Chapter 15

This repository contains my completed projects and exercises from **Chapter 15: Generating Data** in *Python Crash Course, 3rd Edition* by Eric Matthes. The chapter focuses on visualizing numerical data using Matplotlib and Plotly, with projects designed to build fluency in data generation, object-oriented programming (OOP), and graphical presentation.

Each section of this chapter demonstrates how to transform data into meaningful visuals using Python’s standard scientific libraries and structured code.

---

## 🧰 Libraries Used

- [Matplotlib](https://matplotlib.org/) – for static data visualizations
- [Plotly](https://plotly.com/python/) – for interactive data visualizations

---

## 📊 Projects and Exercises Completed

### 📈 **Project 1: Plotting a Simple Line Graph**
Topics practiced:
- Changing label type and line thickness
- Correcting misaligned data
- Using built-in style sheets
- Plotting individual points with `scatter()`
- Plotting and styling data series
- Calculating data automatically
- Customizing tick labels
- Defining custom colors
- Using colormaps for dynamic coloring
- Saving plots automatically with `savefig()`

---

### 🎲 **Project 2: Random Walks**
Topics practiced:
- Creating the `RandomWalk` class (OOP)
- Using `choice()` to pick directions
- Plotting random walks with Matplotlib
- Generating and styling multiple walks
- Highlighting start and end points
- Cleaning up axes for clarity
- Filling the screen and maximizing plot space
- Refactoring code for modularity and reuse

#### 🔧 Exercises:
- **15-1: Cubes** – plotting cubes from 1–5
- **15-2: Colored Cubes** – using colormaps with cube plots
- **15-3: Molecular Motion** – simulating particle movement
- **15-4: Modified Random Walk** – adjusting behavior and plot size
- **15-5: Refactoring** – moving logic into helper functions

---

### 📊 **Project 3: Rolling Dice with Plotly**
Topics practiced:
- Installing and using Plotly for browser-based visualizations
- Creating the `Die` class and simulating rolls
- Analyzing results and generating histograms
- Customizing axes and layout
- Rolling multiple dice (e.g., 2 D6, 3 D8, D6 × D10)
- Using comprehensions to roll and analyze data
- Saving interactive charts to HTML

#### 🔧 Exercises:
- **15-6: Two D8s**
- **15-7: Three Dice**
- **15-8: Multiplication**
- **15-9: Die Comprehensions**
- **15-10: Practicing with Both Libraries**

---

## 🗂️ Project Structure

```plaintext
chapter-15-generating-data/
│
├── .venv/              # Virtual environment (not committed to Git)
├── data/               # Source data files (if applicable)
├── html/               # Interactive HTML charts
│   └── dice_visual_d6d10.html
├── images/             # Saved plot images
├── notebooks/          # Jupyter Notebooks (currently empty)
├── src/                # Core Python scripts
├── tests/              # Unit tests (currently empty)
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

```

## 🚀 Getting Started

To run the code and view visualizations:

1. **Clone the repository:**
   ```bash
   <UPDATE WHEN PUBLIC>
    ```
2. **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate      # macOS/Linux
    venv\Scripts\activate.bat     # Windows
    pip install -r requirements.txt
   ```
3. **Run a project:**
    ```bash
    python src/dice_visual.py
    ```
3. **Open the generated chart:**
- Matplotlib plots saved to images/
- Plotly charts open in your browser or are saved as HTML files

## 📘 Attribution
This project is based on exercises and concepts from Python Crash Course, 3rd Edition by Eric Matthes. 
It is shared here for educational purposes only. 
All rights to the original content belong to Eric Matthes and No Starch Press.

## 📄 License
This project is open-source and available under the MIT License.




