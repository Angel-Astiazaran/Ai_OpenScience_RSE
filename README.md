# Ai_OpenScience_RSE

This project is part of the course *Artificial Intelligence and Open Science in Research Software Engineering* at UPM.

---

## ✨ Features
- Extracts and analyzes text from 10 open-access research papers.
- Generates a keyword cloud from abstracts.
- Counts and visualizes figures per paper.
- Extracts and lists URLs from the papers.
- Fully dockerized for reproducibility.

---

## 📦 Installation

### Prerequisites
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution)
- [Poetry](https://python-poetry.org/docs/#installation) (installed via Conda)
- [Docker](https://docs.docker.com/get-docker/) (optional, for containerized execution)


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

## 🐳 Running with Docker (Optional)
If you prefer running the project inside a containerized environment, you can use Docker.

### 1. Build the Docker Image
docker build -t ai_openscience_rse:latest .

### 2. Run the Docker Container
docker run --rm -it ai_openscience_rse:latest


## 🧪 Running Tests
To run the tests, make sure you are in the Poetry shell and execute:
pytest tests/


## 📚 Documentation

This document contains all the necessary information to install, run, and contribute to this project.  
For specific details on:
- **Installation**, see [📦 Installation](#installation).
- **Usage**, see [🚀 Usage](#usage).
- **Docker Execution**, see [🐳 Running with Docker](#running-with-docker-optional).
- **Validation Methodology**, see [📊 Result Validation](#result-validation).
- **Project Structure**, see [📂 Project Structure](#project-structure).
- **Contributing**, see [🤝 Contributing](#contributing).

## 📊 Result Validation  
The methodology used to validate the results is detailed in [rationale.md](rationale.md).

## 🤝 Contributing

Contributions are welcome! To contribute:
    1. Fork the repository.
    2. Create a new branch (git checkout -b feature-new-feature).
    3. Make your changes and commit them (git commit -m "Added a new feature").
    4. Push to your branch (git push origin feature-new-feature).
    5. Open a pull request.

## 📄 License
This project is licensed under the [Apache 2.0](LICENSE) License.

## 📑 Citation
Zenodo:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14962748.svg)](https://doi.org/10.5281/zenodo.14962748)