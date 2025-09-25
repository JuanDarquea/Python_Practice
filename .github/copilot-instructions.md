# Copilot Instructions for Python_Practice

## Project Overview
This repository is a personal practice space for Python programming, containing Jupyter notebooks and sample data files. It is organized for learning, experimentation, and code debugging.

## Structure & Key Files
- **Jupyter Notebooks**: Main work is in `Coursera_Practice.ipynb` and `Think_Python_Practice.ipynb`. These contain code, exercises, and notes from various learning modules.
- **Files/**: Contains sample datasets and files for practice, including CSV, JSON, XML, Excel, and image files. Example: `employee.csv`, `sample.json`, `sample.xlsx`.
- **README.md**: Explains the purpose of the repository.

## Developer Workflows
- **No build or test automation**: This project does not use automated build or test scripts. All code is run interactively in Jupyter notebooks.
- **Data Loading**: Use relative paths like `Files/employee.csv` when loading data in notebooks.
- **Experimentation**: Code cells are used for experimentation and learning. There is no strict module or package structure.

## Patterns & Conventions
- **Notebook-centric**: All logic and documentation are in notebooks. There are no standalone Python scripts or modules.
- **File Usage**: Data files are used for pandas, file I/O, and API practice. Example:
  ```python
  import pandas as pd
  df = pd.read_csv('Files/employee.csv')
  ```
- **No external dependencies listed**: Install packages as needed in the notebook environment (e.g., pandas, matplotlib).
- **Naming**: Filenames and variable names are descriptive and related to the learning topic.

## Integration Points
- **No external APIs or services integrated**: All code is local and self-contained.
- **Images and data files**: Used for exercises, not for production workflows.

## Guidance for AI Agents
- Focus on helping with Python code, Jupyter notebook cells, and data analysis tasks.
- Suggest improvements or refactoring only within the context of notebooks.
- When referencing files, use the `Files/` directory and relative paths.
- Do not assume the presence of tests, CI/CD, or production code.
- Prioritize clarity and educational value in code suggestions.

---
If any conventions or workflows are unclear, please ask for clarification or examples from the user.
