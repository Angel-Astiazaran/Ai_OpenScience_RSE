# Ai_OpenScience_RSE

This project is part of the course *Artificial Intelligence and Open Science in Research Software Engineering* at UPM.

---

## ✨ Features
- Extracts and analyzes text from 10 open-access research papers.
- Generates a keyword cloud from abstracts.
- Counts and visualizes figures per paper.
- Extracts and lists URLs from the papers.

---

## 📦 Installation

### Prerequisites
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution)
- [Poetry](https://python-poetry.org/docs/#installation) (instalaremos con Conda)

### 1. Clone the Repository
bash
git clone https://github.com/Angel-Astiazaran/Ai_OpenScience_RSE.git
cd Ai_OpenScience_RSE


### 2. Create and Activate the Conda Environment
conda create -n ai_openscience python=3.10
conda activate ai_openscience

### 3. Install Poetry
conda install -c conda-forge poetry
Verifica la instalación con:
poetry --version

### 4. Install Project Dependencies
poetry install 

### 5. Activate the Poetry Shell
poetry shell

## 🚀 Usage
Once inside the Poetry shell, you can run the main script:
python main.py

## 🧪 Running Tests
To run the tests, make sure you are in the Poetry shell and execute:
pytest tests/

## 📚 Documentation

The full documentation will be available at ReadTheDocs (to be created).

## 📄 License
This project is licensed under the [Apache 2.0](LICENSE) License.

## 📊 Result Validation  
The methodology used to validate the results is detailed in [rationale.md](rationale.md).

## 📑 Citation
Zenodo:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14962748.svg)](https://doi.org/10.5281/zenodo.14962748)