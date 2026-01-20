# 🌍 Climate Change Indicators Analysis

> Interactive web app analyzing 62 years of global temperature data (1961-2022) across 225 countries using advanced data science techniques.

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-FF4B4B.svg)](https://streamlit.io)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://docker.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791.svg)](https://postgresql.org)

## 🎯 Project Overview

This project analyzes global temperature change data from the [FAO Climate Indicators Dataset](https://www.kaggle.com/datasets/tarunrm09/climate-change-indicators) to:

- 📈 Analyze temperature trends and warming acceleration (1961-2022)
- 🗺️ Compare geographic patterns across 225 countries
- 🔮 Project future temperatures using polynomial regression
- 🔍 Segment countries by warming patterns using K-means clustering

**🌐 Live Demo**: [Streamlit App](https://ccanalysis.streamlit.app/)

**Academic Context**: Final project for *Fundamentos de la Ciencia de Datos* @ UAX (2025-26)

---

## 🚀 Quick Start

### Option 1: Run Streamlit App Locally

```bash
# 1. Clone repository
git clone https://github.com/tu-usuario/Climate_Change_-Indicador.git
cd Climate_Change_-Indicador

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py

# 4. Open browser to http://localhost:8501
```

### Option 2: Docker (Full Development Environment)

```bash
# 1. Download dataset (see data/README.md for instructions)

# 2. Start services (includes PostgreSQL + Jupyter)
docker-compose up -d

# 3. Access services:
# - Jupyter Lab: http://localhost:8888
# - Streamlit App: Run 'streamlit run app.py' in container
```

### Stop Services

```bash
docker-compose down
```

---

## 📱 Interactive Streamlit App Features

The web app provides an intuitive interface to explore 62 years of global temperature data:

### 🏠 **Overview**

- Executive summary of global warming trends
- Key statistics: +0.57°C average warming, acceleration from 0.006°C/year (1961) to 0.047°C/year (2022)
- Visual summary of warming acceleration

### 📊 **About the Dataset**

- **Source**: FAO Climate Indicators (FAOSTAT)
- **Coverage**: 225 countries, 62 years (1961-2022)
- **Metric**: Temperature change vs 1951-1980 baseline
- Interactive data sample viewer
- Clear documentation of data limitations

### 📈 **Temperature Trends**

- **Global trends** with polynomial regression analysis
- **Regional comparison** across continents
- Warming acceleration visualizations
- Interactive time series explorer
- Statistical insights (R² = 0.924, warming rate doubling)

### 🌍 **Geographic Patterns**

- **Top 20 warmest countries** with comparative analysis
- Regional warming rankings
- Country-level temperature change exploration
- Geographic distribution insights
- Interactive country search

### 🔮 **Future Projections**

- **2030 temperature forecasts** based on polynomial regression
- Scenario analysis showing acceleration impact
- Risk timeline (2025, 2030, 2050 milestones)
- Strategic recommendations by timeframe
- Confidence intervals and model limitations

### 🔍 **Country Clustering** *(NEW)*

- **K-means clustering** analysis grouping 212 countries
- **3-4 distinct warming patterns** identified
- Cluster profiles with detailed statistics
- Strategic recommendations by cluster:
  - 🔴 High-Impact Rapid Warmers (urgent action needed)
  - 🟠 Fast-Accelerating Warmers (high priority)
  - 🟢 Moderate/Stable Warming Groups (steady adaptation)
- Interactive country search to find cluster assignments
- Visual analysis: PCA projections, feature distributions
- Investment guidance (% GDP) and risk assessments

---

## 📊 Project Phases & Analysis Pipeline

### Phase 1: Data Loading & Database Setup

- PostgreSQL database with temperature indicators
- Data ingestion from FAO Climate Indicators dataset
- 4 analytical SQL queries for data validation
- 📓 [Notebook: 01_data_loading.ipynb](notebooks/01_data_loading.ipynb)

### Phase 2: Exploratory Data Analysis (EDA)

- Univariate analysis of temperature change distributions
- Temporal trends analysis (1961-2022)
- Geographic patterns exploration
- Data quality assessment and handling missing values
- 📓 [Notebook: 02_eda.ipynb](notebooks/02_eda.ipynb)

### Phase 3: Polynomial Regression Analysis

To address the core question of how global temperature is evolving, we applied a 2nd-degree polynomial regression model. The analysis yielded an excellent fit (R² = 0.924) and revealed a critical insight: the warming rate has accelerated eightfold from 0.006°C/year in 1961 to 0.047°C/year in 2022, confirming a significant non-linear trajectory of acceleration.

- 📓 [Notebook: 03_regression_phase3.ipynb](notebooks/03_regression_phase3.ipynb)

### Phase 4: Future Projections

This phase focused on projecting temperature changes out to 2030 using polynomial extrapolation with confidence intervals. The primary finding indicates that if current trends persist, the global average temperature will reach +1.93°C by 2030. This projection serves as a baseline for risk assessment and adaptation timelines.

- 📓 [Notebook: 04_projections.ipynb](notebooks/04_projections.ipynb)

### Phase 5: Clustering Analysis

We utilized K-Means clustering to segment countries into actionable groups based on distinct warming patterns. By analyzing six engineered features—including warming rate, acceleration, and volatility—we identified three optimal segments for business interpretability. These clusters range from "High-Impact Rapid Warmers" requiring critical intervention to "Moderate/Stable Warming Groups" suitable for steady adaptation, enabling a more nuanced approach to climate policy.

- 📓 [Notebook: 07_clustering_phase5.ipynb](notebooks/07_clustering_phase5.ipynb)

### Phase 6: Interactive Web Application

- **Streamlit app** with 6 interactive pages
- Real-time data exploration and visualization
- Country-level analysis and cluster assignment lookup
- Strategic recommendations engine
- 💻 [App: app.py](app.py)

---

## 🛠️ Tech Stack

### Frontend & Visualization

- **Streamlit 1.29+**: Interactive web application framework
- **Matplotlib & Seaborn**: Statistical visualizations
- **Plotly**: Interactive charts

### Data Processing & Analysis

- **Python 3.11**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning (K-means clustering)
- **SciPy & Statsmodels**: Statistical analysis

### Database & Infrastructure

- **PostgreSQL 15**: Data warehouse
- **Docker Compose**: Containerized environment
- **Jupyter Lab**: Interactive notebooks

### Deployment

- **Streamlit Cloud**: App hosting
- **Git & GitHub**: Version control

---

## 📁 Repository Structure

```text
Climate_Change_-Indicador/
├── app.py                      # 🌐 Streamlit web application (main entry point)
├── requirements.txt            # Python dependencies for Streamlit app
├── notebooks/                  # 📓 Jupyter notebooks (analysis pipeline)
│   ├── 01_data_loading.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_regression_phase3.ipynb
│   ├── 04_projections.ipynb
│   └── 07_clustering_phase5.ipynb
├── data/                       # 📊 Dataset directory (gitignored)
│   └── README.md              # Dataset download instructions
├── reports/                    # 📈 Generated outputs
│   ├── figures/               # Visualizations from notebooks
│   ├── clustering_results_named.csv
│   └── temperature_projections_2030.csv
├── jupyter/                    # Jupyter-specific configs
│   └── requirements.txt
├── docker-compose.yml          # 🐳 Container orchestration
└── README.md                   # This file
```

---

## 📈 Key Findings

### 🌡️ Temperature Trends

Analysis of global temperature data from 1961 to 2022 reveals a statistically significant and accelerating warming trend. The global average temperature has increased by 0.57°C over this period, but the rate of change provides deeper insight than the absolute rise. Polynomial regression analysis (R² = 0.924) highlights a dramatic acceleration in warming: the rate has intensified eightfold, surging from a negligible 0.006°C/year in 1961 to a concerning 0.047°C/year by 2022. This acceleration is not distributed evenly; Eastern Europe and Russia are warming at nearly three times the global average (+1.5°C), while persistent ocean effects moderate the rise in Pacific island nations to approximately +0.4°C.

### 🔮 Future Projections

If current acceleration trends continue, our models project a global temperature increase of +1.93°C by 2030. This trajectory suggests we are approaching the critical 2°C threshold significantly faster than previous linear estimates indicated. The 95% confidence interval for this projection ranges from 1.7°C to 2.1°C, indicating a high probability of exceeding safe climate limits within the next decade unless drastic mitigation strategies are implemented.

### 🔍 Country Clustering

Data segmentation identifies three distinct warming patterns across 212 countries, offering a framework for targeted adaptation. A group of **High-Impact Rapid Warmers**, primarily in the Arctic and Eastern Europe, faces the most urgent risk with an average rise of +1.27°C and a warming rate of 0.54°C/decade. A larger cluster of **Fast-Accelerating Warmers** (+0.62°C avg) shows strong recent acceleration, warranting high-priority intervention. Meanwhile, the majority of nations fall into **Moderate Warming Groups** (+0.43°C avg), where steady adaptation strategies are more appropriate. This segmentation underscores that effective climate policy must be tailored to specific warming behaviors rather than applied uniformly.

---

## 🔗 Links & Resources

- **Live App**: [Streamlit Cloud](https://ccanalysis.streamlit.app/)
- **Dataset Source**: [FAO Climate Indicators on Kaggle](https://www.kaggle.com/datasets/tarunrm09/climate-change-indicators)
- **Repository**: [GitHub](https://github.com/GabrielFersPin/Climate_Change_-Indicador)

---

## 📝 How to Reproduce

All analysis is fully reproducible:

1. **Clone repository** and follow [Quick Start](#-quick-start)
2. **Download dataset** from Kaggle (see `data/README.md`)
3. **Run notebooks** in sequence: 01 → 02 → 03 → 04 → 07
4. **Launch Streamlit app**: `streamlit run app.py`
5. Notebooks automatically generate all figures in `reports/figures/`
6. Clustering results saved to `reports/clustering_results_named.csv`

### Data Pipeline

```text
Raw Dataset → PostgreSQL → EDA → Regression → Projections → Clustering → Streamlit App
```

---

## 🏗️ Features & Best Practices

This project demonstrates:

- ✅ **Interactive data apps** with Streamlit
- ✅ **Containerized workflows** with Docker
- ✅ **SQL database integration** for data management
- ✅ **Advanced statistical modeling** (polynomial regression, K-means)
- ✅ **Feature engineering** from time series data
- ✅ **Business-driven analysis** (interpretability > metrics)
- ✅ **Clean, documented code** following best practices
- ✅ **Reproducible research** with Jupyter notebooks
- ✅ **Cloud deployment** ready for Streamlit Cloud

---

## ⚠️ Important Notes

- **Dataset scope**: This analysis focuses solely on temperature change data
- **Limitations**: Does not include CO₂ emissions, sea level, precipitation, or other climate variables
- **Projections**: Based on historical trends; actual outcomes depend on climate action taken

---

## 📄 License

MIT License - Free to use for educational purposes with attribution.
