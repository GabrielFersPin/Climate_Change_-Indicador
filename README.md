# 🌍 Climate Change Indicators Analysis

> Data Science project analyzing global climate indicators using regression, classification, and clustering techniques.

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://docker.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791.svg)](https://postgresql.org)

## 🎯 Project Overview

This project analyzes climate change indicators from [Kaggle Dataset](https://www.kaggle.com/datasets/tarunrm09/climate-change-indicators) to:
- Predict global temperature trends using regression models
- Classify high-risk climate scenarios with logistic regression
- Segment countries by emission profiles using clustering

**Academic Context**: Final project for *Fundamentos de la Ciencia de Datos* @ UAX (2025-26)

---

## 🚀 Quick Start with Docker

### Prerequisites
- Docker & Docker Compose installed
- 4GB RAM available
- Dataset downloaded (see [Data Setup](#data-setup))

### Run the Project
```bash
# 1. Clone repository
git clone https://github.com/tu-usuario/climate-change-analysis.git
cd climate-change-analysis

# 2. Download dataset (see data/README.md for instructions)

# 3. Start services
docker-compose up -d

# 4. Access Jupyter Lab
# Open http://localhost:8888
# Token: check terminal output or logs
```

### Stop Services
```bash
docker-compose down
```

---

## 📊 Project Phases

### Phase 1: Database Setup
- PostgreSQL database with climate indicators
- 4 analytical SQL queries ([see notebook](notebooks/01_data_loading.ipynb))

### Phase 2: Exploratory Data Analysis
- Univariate analysis of key variables
- Correlation heatmaps and temporal trends
- Data quality assessment

### Phase 3: Linear Regression
- **Question**: Can CO2 emissions predict global temperature?
- **Variables**: CO2, deforestation, methane → Temperature
- **Results**: R² = 0.87, significant positive relationship

### Phase 4: Logistic Regression
- **Question**: Which factors predict "high-risk" climate years?
- **Target**: Binary classification (temp > 1.5°C baseline)
- **Accuracy**: 92%

### Phase 5: Clustering Analysis
- **Objective**: Segment countries by climate profile
- **Method**: K-Means (k=4 optimal)
- **Clusters**: High emitters, Vulnerable nations, Green leaders, Developing

---

## 🛠️ Tech Stack

- **Database**: PostgreSQL 15
- **Analysis**: Python 3.11 (pandas, scikit-learn, statsmodels)
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Infrastructure**: Docker Compose
- **Version Control**: Git & GitHub

---

## 📁 Repository Structure
```
├── notebooks/          # Jupyter notebooks (reproducible)
├── src/               # Reusable Python modules
├── data/              # Data directory (gitignored)
├── reports/           # Final outputs and figures
└── docker-compose.yml # Infrastructure as code
```

---

## 📈 Key Findings

1. **Strong correlation** (r=0.93) between CO2 emissions and global temperature
2. **Logistic model** identifies 2015-2020 as critical high-risk period
3. **Clustering reveals** 4 distinct country profiles for targeted policy

[View Full Report](reports/final_report.pdf)

---

## 🔗 Links

- **Dataset Source**: [Kaggle - Climate Change Indicators](link)
- **Live Analysis**: [GitHub Pages](https://tu-usuario.github.io/climate-change-analysis)
- **Author**: Gabriel - [LinkedIn](link) | [Portfolio](link)

---

## 📝 How to Reproduce

All analysis is fully reproducible:

1. Follow [Quick Start](#quick-start-with-docker)
2. Run notebooks in order (01 → 05)
3. Notebooks generate all figures in `reports/figures/`
4. Final report compiled from notebook outputs

---

## 🏗️ Development Notes

This project demonstrates:
- ✅ Containerized data science workflows
- ✅ SQL database integration
- ✅ Statistical modeling and interpretation
- ✅ Clean, documented code
- ✅ Reproducible research practices

**Academic Integrity**: This is an original work for UAX coursework.

---

## 📄 License

MIT License - Free to use for educational purposes with attribution.