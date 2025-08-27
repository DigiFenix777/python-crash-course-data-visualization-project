# 📊 Data Visualization with Matplotlib and Plotly  

<!-- 📛 Project Badges -->
![Last Commit](https://img.shields.io/github/last-commit/DigiFenix777/python-crash-course-data-visualization-project)
![Top Language](https://img.shields.io/github/languages/top/DigiFenix777/python-crash-course-data-visualization-project)
![Repo Size](https://img.shields.io/github/repo-size/DigiFenix777/python-crash-course-data-visualization-project)
![Issues](https://img.shields.io/github/issues/DigiFenix777/python-crash-course-data-visualization-project)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)


## 🔑 Executive Summary  
This project explores **Python-powered data visualization** through Matplotlib and Plotly, focusing on both **static and interactive charts**. While the examples center on mathematics and simulations (cubes, random walks, dice rolls), the same visualization techniques directly apply to **cybersecurity workflows**, such as:  

- Charting **attack frequency trends** over time.  
- Mapping **geographic spread of incidents**.  
- Creating interactive **dashboards for SOC and compliance reporting**.  
- Communicating **risk insights to executives and auditors** with clarity.  

👉 For recruiters and hiring managers: this project demonstrates my ability to transform raw data into **meaningful, visual insights**—a critical competency for cybersecurity analysis, reporting, and decision-making.  

---

## 📌 Overview  

This project covers end-to-end **data visualization practices** using Matplotlib (static plots) and Plotly (interactive plots). Key topics include:  

- Plotting simple line and scatter graphs.  
- Customizing styles, labels, colors, and tick marks.  
- Using **colormaps** for clarity in large datasets.  
- Saving plots automatically for portfolio inclusion.  
- Simulating and visualizing **random walks**.  
- Building **interactive dice roll simulations** with Plotly.  

---

## 🧠 Skills & Concepts  

- **Matplotlib basics** (line plots, scatter plots, colormaps).  
- **Plotly Express** for interactive charting.  
- Styling and scaling plots for readability.  
- Object-oriented design with custom classes (`RandomWalk`, `Die`).  
- Automating workflows with refactoring and list comprehensions.  
- Professional Git/GitHub practices (branching, version control, repo hygiene).  

---

## 🗂️ Repository Structure  

```plaintext
data-visualization-project/
│
├── data/                 # Input datasets or simulation outputs (empty)
│ 
├── html/                 # Exported Die Roll plots in HTML format
│   ├── dice_visual_2d8.html
│   └── dice_visual_d6d10.html
│
├── images/portfolio/     # Exported static and interactive plots
│   ├── cubes_plot.png
│   ├── mod_random_walk_inferno.png
│   ├── mod_random_walk_purples.png
│   ├── random_walk_magma.png
│   ├── squares_plot.png
│   └── dice_multiplication.png
│
├── src/                  # Python scripts for lessons & exercises
│   ├── dice_visual.py
│   ├── dice_visual_2d8.py
│   ├── dice_visual_3d6.py
│   ├── dice_visual_d6d10.py
│   ├── dice_visual_multiply_2d6.py
│   ├── die.py
│   ├── die_visual.py
│   ├── main.py
│   ├── mod_rw_visual.py
│   ├── modified_random_walk.py
│   ├── molecular_motion.py
│   ├── molecular_visual.py
│   ├── mpl_squares.py
│   ├── random_walk.py
│   ├── rw_plotly.py
│   ├── rw_visual.py
│   ├── scatter_cubes.py
│   ├── scatter_squares.py
│   └── main.py
│
├── tests/
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
## 🚀 How to Run

Clone this repo and move into the folder:
```bash
git clone git@github.com:your-username/project-data-visualization.git
cd project-data-visualization
```

(Optional) Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run any exercise script, for example:
```bash
python src/scatter_cubes.py
```
## 🔎 Skills Spotlight


This project highlights:
- Python scripting for data visualization.
- Matplotlib & Plotly for both static and interactive charts.
- Designing simulations with object-oriented programming.
- Applying clean repo structure and GitHub portfolio practices.
- Building transferable skills for cybersecurity dashboards and incident reports.


---


## 📝 Lessons Learned

- Importance of styling and scaling plots for readability and accuracy.
- How random walks simulate unpredictable patterns (mirroring attacker behavior in networks).
- How dice simulations parallel probability and risk assessment in cybersecurity.
- Why reproducibility (requirements, clear structure, README) matters for collaboration and audits.
- How visualization bridges raw technical data and executive decision-making.

---


## 📊 Exercises Implemented

- **15-1: Cubes** → Plotted cubic numbers (5 & 5,000 points).
- **15-2: Colored Cubes** → Applied a colormap to cubes plot.
- **15-3: Molecular Motion** → Simulated pollen grain motion with line plots.
- **15-4: Modified Random Walks** → Adjusted parameters to explore behavior.
- **15-5: Refactoring** → Simplified fill_walk() for readability and maintainability.
- **15-6: Two D8s** → Simulated and plotted results of rolling two 8-sided dice.
- **15-7: Three Dice** → Simulated rolling three D6 dice (min=3, max=18).
- **15-8: Multiplication** → Visualized results of multiplying two dice rolls.
- **15-9: Die Comprehensions** → Used list comprehensions to simplify dice simulations.

---


## 🌍 Data Sources

Synthetic datasets generated in exercises (random walks, dice rolls).

Exercises and examples adapted from Python Crash Course, 3rd Edition by Eric Matthes (No Starch Press).


---


## 📚 Attribution

Based on exercises from:
Matthes, E. (2023). Python Crash Course (3rd ed.). No Starch Press.
[Book website](https://nostarch.com/python-crash-course-3rd-edition)

---


## 🧩 License

Distributed under the MIT License.
See LICENSE for details.

---
