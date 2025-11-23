# 🌍 Climate Change Indicators - Streamlit App Guide

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit App

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

## App Features

### Navigation Menu
The app includes a sidebar menu to navigate through all project phases:

- **🏠 Home**: Project overview, key metrics, and technology stack
- **📊 Phase 1: Database Setup**: SQL queries and database schema
- **🔍 Phase 2: Exploratory Data Analysis**: Univariate analysis, temporal trends, and correlations
- **📈 Phase 3: Linear Regression**: Temperature prediction models and future projections
- **🎯 Phase 4: Logistic Regression**: High-risk climate year classification
- **🔬 Phase 5: Clustering Analysis**: Country segmentation by climate profiles

### Key Metrics Dashboard

The home page displays:
- 62 years of climate data analyzed (1961-2022)
- +1.2°C temperature increase since 1961
- 92% classification accuracy
- R² score of 0.87 for regression models

### Interactive Visualizations

Each phase includes:
- Statistical analysis results
- Interactive charts and graphs (when available)
- Model performance metrics
- Key insights and recommendations

## Customization

### Adding Your Own Visualizations

If you've generated additional figures in the `reports/figures/` directory, they will automatically appear in the relevant sections.

### Modifying Content

Edit `app.py` to:
- Add new sections or tabs
- Update metrics and findings
- Include additional visualizations
- Customize styling and layout

### Theme Customization

Create a `.streamlit/config.toml` file to customize the app theme:

```toml
[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"
```

## Project Structure

```
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── reports/
│   ├── figures/               # Generated visualizations
│   ├── temperature_projections_2030.csv
│   └── phase4_regression_summary.txt
└── notebooks/                 # Jupyter notebooks
```

## Troubleshooting

### Port Already in Use

If port 8501 is already in use:

```bash
streamlit run app.py --server.port 8502
```

### Missing Visualizations

If images don't appear:
1. Run the corresponding Jupyter notebooks to generate figures
2. Ensure figures are saved in `reports/figures/`
3. Check that file paths in `app.py` match your saved figures

### Package Conflicts

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Deployment

### Streamlit Cloud (Free)

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### Docker Deployment

Add this to your `docker-compose.yml`:

```yaml
streamlit:
  build: .
  ports:
    - "8501:8501"
  command: streamlit run app.py --server.port=8501 --server.address=0.0.0.0
  volumes:
    - ./reports:/app/reports
```

## Support

For issues or questions:
- Check the [Streamlit documentation](https://docs.streamlit.io)
- Review the project README.md
- Examine the Jupyter notebooks for data generation

---

**Built with Streamlit** 🎈 | Climate Change Indicators Analysis
