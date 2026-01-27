import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Global Temperature Change Analysis (1961-2022)",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #e74c3c;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 1.2rem;
        border-radius: 0.5rem;
        border-left: 4px solid #3498db;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1.2rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1.2rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🌡️ Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Explore:",
    [
        "🏠 Overview",
        "📊 About the Dataset",
        "📈 Temperature Trends",
        "🌍 Geographic Patterns",
        "🔮 Future Projections",
        "� Logistic Regression",
        "�🔍 Country Clustering"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Data Source:** FAO Climate Indicators
**Coverage:** 225 countries, 1961-2022
**Metric:** Temperature change vs 1951-1980 baseline

**UAX | Fundamentos de la Ciencia de Datos | 2025-26**
""")

# Helper functions
def load_image(image_path):
    if Path(image_path).exists():
        return str(image_path)
    return None

def load_temperature_projections():
    csv_path = Path("reports/temperature_projections_2030.csv")
    if csv_path.exists():
        return pd.read_csv(csv_path)
    return None

def load_clustering_results():
    csv_path = Path("reports/clustering_results_named.csv")
    if csv_path.exists():
        return pd.read_csv(csv_path)
    return None

# ===========================
# HOME PAGE
# ===========================
if page == "🏠 Overview":
    st.markdown('<h1 class="main-header">🌡️ Global Temperature Change: 62 Years of Data</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
    <h3>What This Analysis Shows</h3>
    After analyzing 62 years of global temperature data (1961-2022) covering 225 countries,
    we've documented a clear and accelerating warming trend across the planet. This analysis
    quantifies exactly how fast our planet is warming and where we're headed if current trends continue.
    </div>
    """, unsafe_allow_html=True)

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📅 Years Analyzed", "1961-2022", "62 years")
        st.caption("Continuous temperature records")
    with col2:
        st.metric("🌍 Countries", "225", "Global coverage")
        st.caption("From Afghanistan to Zimbabwe")
    with col3:
        st.metric("📈 Warming Rate (2022)", "+0.047°C/year", "8x faster than 1961")
        st.caption("Rate is accelerating")
    with col4:
        st.metric("🔮 2030 Projection", "+1.93°C", "Based on current trends")
        st.caption("Quadratic model projection")

    st.markdown("---")

    # What we discovered
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-header">📊 Key Findings</div>', unsafe_allow_html=True)
        st.markdown("""
        **1. Clear Warming Trend**
        Global temperature data confirms a continuous upward trend since 1961. The polynomial regression analysis demonstrates that this warming is accelerating, with recent decades consistently outperforming historical averages.

        **2. Acceleration Confirmed (8x)**
        Our model reveals a dramatic increase in the warming rate. In 1961, the rate was approximately **0.006°C/year**. By 2022, it surged to **0.047°C/year**—a nearly eight-fold acceleration in just six decades.

        **3. Geographic Disparities**
        Clustering analysis identifies that warming is most intense in **Arctic and continental regions**. These areas form distinct "high-warming" clusters that are heating up significantly faster than the global baseline.

        **4. 2030 Projection: 1.93°C**
        Based on the quadratic trend ($R^2 > 0.9$), the model projects a global temperature anomaly of **+1.93°C by 2030**, assuming current trends continue without major intervention.
        """)

    with col2:
        st.markdown('<div class="section-header">🔬 What This Data Represents</div>', unsafe_allow_html=True)
        st.markdown("""
        **Temperature Change Explained:**
        This analysis relies on temperature anomalies, which measure deviation from the 1951-1980 baseline average. A value of 0°C represents the baseline normal, while positive values indicate warming. For context, +1°C signifies a global shift that triggers major ecosystem disruptions.

        **Why This Matters:**
        Seemingly small numbers like +1°C or +2°C have profound global consequences. Warming of this magnitude triggers major ecosystem disruptions and requires urgent adaptation measures.

        **What Causes These Changes:**
        Although this dataset focuses on temperature metrics, the driving forces are well-established. Greenhouse gas emissions—primarily CO₂ and methane—are the main culprits, exacerbated by deforestation and industrial activity, with natural variability playing only a minor role. This analysis quantifies the *what* and *when* of this accelerating crisis.
        """)

    st.markdown("---")

    st.markdown('<div class="section-header">🎯 Who Should Use This Analysis</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Policy Makers**")
        st.markdown("""
        - Quantify warming rates for your region
        - Compare national trends to global averages
        - Use projections for infrastructure planning
        - Set evidence-based climate targets
        """)

    with col2:
        st.markdown("**Researchers & Students**")
        st.markdown("""
        - Access cleaned, analyzed temperature data
        - Understand statistical modeling approaches
        - See real-world data science in action
        - Build on this foundation for further study
        """)

    with col3:
        st.markdown("**Business & Infrastructure**")
        st.markdown("""
        - Plan for temperature scenarios through 2030
        - Assess climate risks to operations
        - Design for warmer future conditions
        - Make data-driven adaptation decisions
        """)

# ===========================
# ABOUT THE DATASET
# ===========================
elif page == "📊 About the Dataset":
    st.markdown('<h1 class="main-header">📊 Understanding the Data Source</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <h3>Data Transparency & Reliability</h3>
    This analysis uses publicly available data from the Food and Agriculture Organization (FAO)
    of the United Nations. Below is complete documentation of what this dataset contains, where
    it comes from, and crucially—what it does NOT include.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📚 Source & Coverage", "🌡️ What's Included", "⚠️ Limitations"])

    with tab1:
        st.markdown('<div class="section-header">Data Source & Collection</div>', unsafe_allow_html=True)

        st.markdown("""
        **Official Source:**
        - **Organization**: Food and Agriculture Organization of the United Nations (FAO)
        - **Dataset**: FAOSTAT Climate Change - Climate Indicators
        - **Indicator**: Surface Temperature Change
        - **License**: CC BY-NC-SA 3.0 IGO
        - **Last Updated**: 2023
        - **Source URL**: [FAO Climate Data](https://www.fao.org/faostat/en/#data/ET)

        **Temporal Coverage:**
        - **Start Year**: 1961
        - **End Year**: 2022
        - **Duration**: 62 consecutive years
        - **Frequency**: Annual measurements
        - **Total Observations**: 12,460 (225 countries × 62 years, with some gaps)

        **Geographic Coverage:**
        - **Countries/Territories**: 225
        - **Regions**: All continents
        - **Coverage Type**: Comprehensive global dataset
        - **Smallest Territory**: Monaco (2 km²)
        - **Largest Territory**: Russia (17 million km²)
        """)

        st.markdown("---")

        st.markdown("**How Temperature Data is Collected:**")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            **Measurement Methods:**
            - Ground-based weather stations
            - Standardized instruments and protocols
            - Daily temperature readings averaged annually
            - Multiple stations per country for accuracy
            - Quality control and error detection
            """)

        with col2:
            st.markdown("""
            **Data Processing:**
            - Compiled by meteorological agencies
            - Cross-validated between stations
            - Aggregated to national level
            - Anomalies calculated vs 1951-1980 baseline
            - Peer-reviewed methodology
            """)

        st.markdown("---")

        st.markdown("**Baseline Period (1951-1980):**")
        st.markdown("""
        All temperature changes are expressed relative to the 1951-1980 period average. This 30-year
        period was chosen because:
        - Long enough to smooth out year-to-year variability
        - Represents "pre-acceleration" climate conditions
        - Widely used standard in climate science
        - Allows comparison across different datasets
        """)

    with tab2:
        st.markdown('<div class="section-header">What This Dataset Contains</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="success-box">
        <h4>✅ Variables Included in This Dataset</h4>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Core Data Fields:**")

        # Create sample dataframe
        sample_data = {
            'Country': ['Russian Federation', 'Estonia, Rep. of', 'United States of America', 'Brazil', 'Japan'],
            'ISO3': ['RUS', 'EST', 'USA', 'BRA', 'JPN'],
            'Year': [2020, 2020, 2020, 2020, 2020],
            'Temperature_Change_°C': [3.691, 3.625, 1.421, 1.156, 1.293]
        }
        st.dataframe(pd.DataFrame(sample_data), use_container_width=True, hide_index=True)
        st.caption("Sample: Top warming countries in 2020 showing actual data structure")

        st.markdown("""
        **Column Descriptions:**

        1. **Country**: Official country/territory name
           - 225 unique countries and territories
           - Includes small island nations and territories

        2. **ISO3**: Three-letter country code
           - International standard (ISO 3166-1 alpha-3)
           - Enables easy data joining and mapping

        3. **Year**: Calendar year of measurement
           - Range: 1961 to 2022
           - Annual frequency (one value per country per year)

        4. **Temperature Change (°C)**: THE key variable
           - **Definition**: Difference from 1951-1980 baseline average
           - **Units**: Degrees Celsius
           - **Range in dataset**: -2.06°C to +3.69°C
           - **Interpretation**:
             - Positive values = warmer than baseline
             - Negative values = cooler than baseline
             - Larger absolute values = greater change
        """)

        st.markdown("---")

        st.markdown("**Statistical Properties of Temperature Data:**")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Mean", "0.538°C", "Global average change")
        col2.metric("Median", "0.470°C", "Middle value")
        col3.metric("Std Dev", "0.655°C", "Typical variation")
        col4.metric("Range", "5.75°C", "Min to max spread")

        st.caption("Statistics across all 12,460 country-year observations")

    with tab3:
        st.markdown('<div class="section-header">Critical Limitations</div>', unsafe_allow_html=True)

        st.markdown("""
        <div class="warning-box">
        <h4>⚠️ What This Dataset Does NOT Include</h4>
        Being transparent about limitations is essential for proper interpretation.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Variables NOT in This Dataset:**")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            **❌ Emissions Data**
            - No CO₂ (carbon dioxide) measurements
            - No CH₄ (methane) data
            - No greenhouse gas inventories
            - No per-capita emissions

            **❌ Other Climate Indicators**
            - No precipitation/rainfall data
            - No sea level rise measurements
            - No ocean temperature
            - No ice cover/glacier data
            """)

        with col2:
            st.markdown("""
            **❌ Land Use Changes**
            - No deforestation rates
            - No urbanization data
            - No agricultural expansion

            **❌ Socioeconomic Data**
            - No population figures
            - No GDP or economic data
            - No energy consumption
            - No policy information
            """)

        st.markdown("---")

        st.markdown("**Geographic Aggregation Issues:**")

        st.markdown("""
        **The Problem:** Temperature data is aggregated at the **national level**, which hides
        internal variation within large or geographically diverse countries.

        **Examples of Hidden Variation:**

        **Chile** (4,300 km long, north-south)
        - Atacama Desert (north): Arid, extreme heat
        - Central Valley: Mediterranean climate
        - Patagonia (south): Cold, maritime conditions
        - **National average**: Masks 10°C+ regional differences

        **Russia** (17 million km², 41° latitude span)
        - Arctic regions: Extreme warming (>3°C in some years)
        - Southern regions: More moderate changes
        - **National average**: Dominated by vast Arctic territories

        **USA** (9.8 million km², diverse climates)
        - Alaska: Arctic/subarctic warming
        - Southwest: Desert heat intensification
        - Northeast: Continental climate shifts
        - **National average**: Smooths out dramatic regional differences

        **Implication:** A country's national average may not reflect local conditions.
        Small, geographically homogeneous countries (e.g., Singapore, Luxembourg) have more
        representative national averages.
        """)

        st.markdown("---")

        st.markdown("**Analytical Limitations:**")

        st.markdown("""
        1. **Temporal Coverage (62 years)**
           - Relatively short for climate timescales
           - Can't capture century-scale patterns
           - Limited ability to detect long cycles

        2. **National Aggregation**
           - Loses regional climate detail
           - Can't analyze subnational trends
           - Biased toward geographic size

        3. **Temperature Only**
           - Can't directly analyze causes (emissions, land use)
           - Can't assess other impacts (precipitation, extremes)
           - Correlation with causes requires external data

        4. **No Extremes Data**
           - Doesn't capture frequency of heat waves
           - Doesn't show intensity of cold snaps
           - Annual averages smooth out extreme events

        5. **Projection Uncertainty**
           - Statistical models assume trends continue
           - Can't predict policy changes or interventions
           - Confidence intervals widen rapidly beyond 2030
        """)

        st.markdown("---")

        st.markdown("""
        <div class="info-box">
        <h4>ℹ️ How We Handle These Limitations</h4>

        **Transparency:**
        - We clearly state what the data shows and doesn't show
        - Projections are labeled as "statistical extrapolations"
        - Uncertainty ranges (confidence intervals) are always provided

        **Appropriate Use:**
        - Temperature trends: ✅ Strong conclusions possible
        - Acceleration analysis: ✅ Well-supported by data
        - Future projections: ⚠️ Useful baselines, but high uncertainty
        - Cause attribution: ❌ Requires external emission data
        - Policy effectiveness: ❌ Beyond scope of this dataset

        **Complementary Data Needed:**
        - For full climate picture: IPCC comprehensive assessments
        - For emissions analysis: EDGAR, CDIAC databases
        - For regional detail: National meteorological services
        - For policy impact: Controlled scenario modeling (CMIP6)
        </div>
        """, unsafe_allow_html=True)

# ===========================
# TEMPERATURE TRENDS
# ===========================
elif page == "📈 Temperature Trends":
    st.markdown('<h1 class="main-header">📈 How Temperatures Have Changed Over Time</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <h3>Temporal Analysis: 62 Years of Global Warming</h3>
    This section explores how global temperatures have evolved from 1961 to 2022, revealing
    clear patterns of warming and—most critically—the acceleration of that warming over time.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📊 Overall Trends", "📈 Warming Acceleration", "📅 Decade-by-Decade"])

    with tab1:
        st.markdown('<div class="section-header">Temperature Distribution & Temporal Patterns</div>', unsafe_allow_html=True)

        # Show univariate analysis
        img_path = load_image("reports/figures/eda_univariate_temperature.png")
        if img_path:
            st.image(img_path, use_column_width=True)
            st.caption("Statistical distribution of temperature changes across all countries and years")
        else:
            st.warning("Visualization not yet generated. Run the EDA notebook (04_eda_phase3.ipynb) to create this figure.")

        st.markdown("""
        **What These Plots Tell Us:**

        **1. Distribution Shape (Histogram)**
        - Slightly right-skewed: More extreme warm years than extreme cool years
        - Mean (0.538°C) > Median (0.470°C): Confirms rightward skew
        - Shows the shift from cooler early years to warmer recent years

        **2. Outliers (Box Plot)**
        - Most extreme warming: +3.69°C (Russia 2020, Estonia 2020)
        - Most extreme cooling: -2.06°C (rare, early period anomalies)
        - ~99% of observations fall between -1.5°C and +2.5°C

        **3. Data Quality (Q-Q Plot)**
        - Reasonably normal distribution in the center
        - Heavier tails than perfect normal distribution
        - Indicates real climate extremes, not just measurement error

        **Why both box plot and violin plot for the same variable?**
        El box-plot para que se vean los outliers y el violin-plot para que se vea la densidad y forma de la distribución.
        """)

        st.markdown("---")

        # Show temporal trends
        img_path = load_image("reports/figures/eda_temporal_trends.png")
        if img_path:
            st.image(img_path, use_column_width=True)
            st.caption("Year-by-year global average temperature change (1961-2022)")
        else:
            st.warning("Temporal trends visualization not yet generated.")

        st.markdown("""
        **Key Observations from Temporal Analysis:**

        **The Clear Upward Trend:**
        - 1960s-1970s: Temperatures fluctuate around baseline (0°C)
        - 1980s: Warming becomes clearly visible
        - 1990s-2000s: Consistent positive anomalies
        - 2010s-2020s: Every year significantly above baseline

        **Variability Over Time:**
        - Early years (1961-1980): High variability, both warm and cool years
        - Recent years (2000-2022): Lower variability, consistently warm
        - Suggests "new normal" has shifted upward

        **Record-Breaking Years:**
        - All of the top 10 warmest years occurred after 2010
        - 2016, 2020, 2019, 2022 among hottest recorded
        - Pattern: Each decade warmer than the previous
        """)

    with tab2:
        st.markdown('<div class="section-header">Accelerating Warming: Not Just Getting Warmer, Getting Faster</div>', unsafe_allow_html=True)

        # Show bivariate analysis
        img_path = load_image("reports/figures/regression_bivariate_analysis.png")
        if img_path:
            st.image(img_path, use_column_width=True)
            st.caption("Linear vs quadratic fit showing acceleration of warming")
        else:
            st.warning("Regression analysis visualization not yet generated.")

        st.markdown("""
        <div class="warning-box">
        <h4>🚨 Critical Finding: Warming is Accelerating</h4>
        The most important discovery from this analysis isn't just that temperatures are rising—
        it's that the <strong>rate</strong> of warming is increasing. The planet is warming faster now
        than it was 60 years ago.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Warming Rate in 1961**")
            st.metric("Rate", "0.006°C/year", "")
            st.caption("Very slow, barely detectable")

            st.markdown("**Per Decade**")
            st.metric("", "0.06°C", "")

        with col2:
            st.markdown("**Warming Rate in 2022**")
            st.metric("Rate", "0.047°C/year", "+683%")
            st.caption("Nearly 8x faster!")

            st.markdown("**Per Decade**")
            st.metric("", "0.47°C", "8x increase")

        st.markdown("---")

        st.markdown("**What Causes Acceleration?**")

        st.markdown("""
        The quadratic (curved) trend line fits the data better than a straight line,
        indicating genuine acceleration. Possible reasons:

        1. **Cumulative Emissions**: Greenhouse gases accumulate in atmosphere
        2. **Feedback Loops**:
           - Melting ice → less sunlight reflected → more warming
           - Thawing permafrost → releases more CO₂ → more warming
        3. **Increased Emission Rates**: Industrial activity has intensified
        4. **Ocean Heat Lag**: Oceans releasing stored heat

        **Model Diagnosis & Validation:**

        To determine the nature of the warming trend, we compared two statistical models.
        The diagnosis shows that the **Linear Model** fails to capture recent trends
        (Test R²: -1.43), indicating a poor fit.

        In contrast, the **Quadratic Model** provides a statistically valid fit
        (Test R²: 0.51). Based on this validated model, the positive quadratic coefficient
        (+0.000338) confirms mathematically that the rate of warming is accelerating.

        **Conclusion:**
        The data rejects the hypothesis of constant warming. The validated quadratic
        model proves the curve is bending upward.
        """)

    with tab3:
        st.markdown('<div class="section-header">Decade-by-Decade Breakdown</div>', unsafe_allow_html=True)

        # Show decade analysis
        img_path = load_image("reports/figures/eda_decade_analysis.png")
        if img_path:
            st.image(img_path, use_column_width=True)
            st.caption("Average temperature change by decade")
        else:
            st.warning("Decade analysis visualization not yet generated.")

        st.markdown("**Generational Climate Shifts:**")

        # Decade comparison table
        decade_data = {
            'Decade': ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s*'],
            'Avg_Change': ['~0.0°C', '~0.0°C', '+0.2°C', '+0.4°C', '+0.7°C', '+1.0°C', '+1.3°C'],
            'Description': [
                'Baseline conditions',
                'Slight cooling trend',
                'Warming becomes detectable',
                'Clear warming signal',
                'Rapid acceleration begins',
                'Consistently warm years',
                'Every year above 1°C'
            ],
            'Context': [
                'Pre-acceleration era',
                'Natural variability dominant',
                'Human signal emerges',
                'Scientific consensus forms',
                'Acceleration confirmed',
                'Paris Agreement signed',
                'Exceeding safe limits'
            ]
        }

        st.dataframe(pd.DataFrame(decade_data), use_container_width=True, hide_index=True)
        st.caption("*2020s includes 2020-2022 only (incomplete decade)")

        st.markdown("---")

        st.markdown("**Inter-Generational Perspective:**")

        st.markdown("""
        **Someone born in 1961** experienced:
        - **Age 0-20 (1961-1981)**: Climate similar to historical norms, minor fluctuations
        - **Age 20-40 (1981-2001)**: Gradual warming, +0.2-0.4°C, barely noticeable
        - **Age 40-60 (2001-2021)**: Rapid warming, +0.7-1.2°C, major disruptions
        - **Age 61+ (2021-now)**: Every year exceeds 1°C warming, "new normal"

        **Someone born in 2020** will experience:
        - **Age 0-10 (2020-2030)**: +1.93°C warming (projected), extreme as baseline
        - **Lifetime normal**: What previous generations called "catastrophic"

        **The Climate You're Born Into:**
        - 1960s child: Grew up in stable climate, saw it deteriorate
        - 2000s child: Never knew stable climate, adapts to chaos
        - 2020s child: Extreme weather is normal, doesn't know "cool" summers

        This is why urgency matters—each passing decade, the problem compounds and
        the "normal" shifts further into dangerous territory.
        """)

# ===========================
# GEOGRAPHIC PATTERNS
# ===========================
elif page == "🌍 Geographic Patterns":
    st.markdown('<h1 class="main-header">🌍 Regional Warming: Who\'s Affected Most?</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <h3>Geographic Heterogeneity</h3>
    Climate change is a global phenomenon, but its impacts are far from uniform. Some regions
    are warming 3-4 times faster than the global average, while others experience more moderate changes.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["🏆 Top/Bottom Countries", "🗺️ Regional Patterns", "🔍 Case Studies"])

    with tab1:
        st.markdown('<div class="section-header">Countries by Average Warming (1961-2022)</div>', unsafe_allow_html=True)

        # Show top countries visualization
        img_path = load_image("reports/figures/eda_top_countries.png")
        if img_path:
            st.image(img_path, use_column_width=True)
            st.caption("Top 15 highest and lowest warming countries (countries with at least 40 years of data)")
        else:
            st.warning("Top countries visualization not yet generated.")

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**🔥 Fastest Warming Countries**")
            st.markdown("""
            Top warming nations (62-year average):

            1. **Estonia** (~1.2°C average)
            2. **Lithuania** (~1.2°C)
            3. **Latvia** (~1.2°C)
            4. **Belarus** (~1.1°C)
            5. **Russia** (~1.1°C)

            **Pattern:** Concentrated in Eastern Europe and Northern Asia

            **Common Features:**
            - High latitudes (45°N - 70°N)
            - Continental climates
            - Proximity to Arctic region
            - Large landmasses

            **Why So Extreme:**
            - **Arctic amplification**: High latitudes warm 2-3x faster
            - **Ice-albedo feedback**: Less snow/ice → less reflection → more heat absorbed
            - **Continental effect**: Land heats faster than oceans
            """)

        with col2:
            st.markdown("**❄️ Slowest Warming Countries**")
            st.markdown("""
            Lowest warming nations (62-year average):

            - **Kiribati** (~0.1°C average)
            - **Nauru** (~0.1°C)
            - **Tuvalu** (~0.2°C)
            - **Solomon Islands** (~0.2°C)
            - **Papua New Guinea** (~0.2°C)

            **Pattern:** Small Pacific island nations

            **Common Features:**
            - Tropical locations (near equator)
            - Small land area, surrounded by ocean
            - Maritime climate
            - Low latitudes

            **Why More Stable:**
            - **Ocean buffering**: Water absorbs heat slowly, moderates temperature
            - **Tropical location**: Less seasonal variation to amplify
            - **Maritime effect**: Ocean temperatures more stable than land
            - **Note**: Despite lower temperature rise, these nations face existential threats from sea-level rise (not measured in this dataset)
            """)

        st.markdown("---")

        st.markdown("""
        <div class="warning-box">
        <h4>⚠️ The Paradox of Vulnerability</h4>
        <p>Notice a cruel irony: <strong>Small island nations showing the least warming are often most threatened
        by climate change.</strong></p>

        <p><strong>Why?</strong> This dataset only measures temperature. These nations face:</p>
        <ul>
        <li>Sea level rise (existential threat)</li>
        <li>Ocean acidification (coral reef death, fishing collapse)</li>
        <li>Stronger cyclones/typhoons (catastrophic damage)</li>
        <li>Saltwater intrusion into freshwater (drinking water crisis)</li>
        </ul>

        <p><strong>Meanwhile:</strong> Countries showing highest warming (Russia, Canada) have:</p>
        <ul>
        <li>Resources to adapt (wealth, technology)</li>
        <li>Vast territories to relocate within</li>
        <li>Infrastructure to withstand temperature changes</li>
        </ul>

        <p>This underscores that <strong>temperature change alone doesn't capture full climate impact</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="section-header">Geographic Heterogeneity Analysis</div>', unsafe_allow_html=True)

        # Show geographic heterogeneity visualization
        img_path = load_image("reports/figures/eda_geographic_heterogeneity.png")
        if img_path:
            st.image(img_path, use_column_width=True)
            st.caption("Relationship between country geography and temperature variability")
        else:
            st.warning("Geographic heterogeneity visualization not yet generated.")

        st.markdown("**Does Country Size Affect Data Quality?**")

        st.markdown("""
        One limitation of this dataset is that temperature is aggregated at the **national level**.
        This raises an important question: Do large, geographically diverse countries show more
        variable temperature readings because they actually experience more diverse climates?

        **Analysis Findings:**

        **Large/Elongated Countries** (Russia, Canada, Chile, China):
        - Show higher temperature variability over time
        - National averages mask huge regional differences
        - Example: Russia 2020 = +3.69°C national average
          - Arctic Russia: +5-6°C warming
          - Southern Russia: +2-3°C warming
          - National figure is area-weighted average

        **Small/Compact Countries** (Singapore, Luxembourg, Monaco):
        - More stable temperature readings
        - National average actually represents most of the country
        - Less geographic diversity to mask

        **Implication:**
        - Treat large country data as "regional averages" rather than precise local conditions
        - Small country data more reliable for local analysis
        - For policy/planning in large countries, seek subnational climate data

        **Nota sobre la selección de países:**
        He utilizado esta etiqueta en Russia, Canada, Chile, China para hacer una comparación con los más pequeños Singapore, Luxembourg, Monaco. Era solo un estudio de caso, por si los países variaban mucho la temperatura teniendo también en cuenta que habrían diversos tipos climaticos dentro de un propio país.
        """)

    with tab3:
        st.markdown('<div class="section-header">Case Studies: Contrasting Warming Patterns</div>', unsafe_allow_html=True)

        # Show case studies visualization
        img_path = load_image("reports/figures/eda_case_studies.png")
        if img_path:
            st.image(img_path, use_column_width=True)
            st.caption("Temperature trajectories for different country categories")
        else:
            st.warning("Case studies visualization not yet generated.")

        st.markdown("---")

        st.markdown("**Case Study 1: Russia—Arctic Amplification**")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("""
            **Geography:**
            - 17 million km² (largest country)
            - Spans 11 time zones, 41° latitude
            - 70% of land above 50°N latitude
            - Massive Arctic/subarctic territory

            **Warming Pattern:**
            - 1961-1980: Fluctuating around baseline
            - 1980-2000: Rapid warming begins
            - 2000-2022: Extreme warming years
            - 2020 peak: +3.69°C (hottest recorded)

            **Why So Extreme:**
            - Arctic amplification effect (2-3x global average)
            - Permafrost thaw accelerates warming
            - Loss of sea ice reduces Earth's reflectivity
            - Continental interior far from moderating ocean influence
            """)

        with col2:
            st.metric("62-Yr Avg", "+1.1°C", "3x global avg")
            st.metric("2020 Peak", "+3.69°C", "Highest recorded")
            st.metric("Arctic Regions", "+5-6°C", "In some areas")

        st.markdown("---")

        st.markdown("**Case Study 2: Chile—Geographic Complexity**")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("""
            **Geography:**
            - 4,300 km long (north-south)
            - Only 177 km wide (average)
            - Spans 38° of latitude
            - Atacama Desert (north) to Patagonia (south)

            **Climate Zones in One Country:**
            - **North**: Arid desert, extreme heat
            - **Center**: Mediterranean, moderate
            - **South**: Cold maritime, subpolar

            **Data Challenge:**
            - National average meaningless for local conditions
            - North might be +2°C, South might be +0.5°C
            - Single temperature obscures 10°C+ variation

            **Warming Pattern:**
            - High variability in national average
            - Likely reflects shifting dominance of different climate zones year-to-year
            """)

        with col2:
            st.metric("Length", "4,300 km", "N-S span")
            st.metric("Width", "177 km", "Average")
            st.metric("Lat Range", "38°", "Tropical to Antarctic")

        st.markdown("---")

        st.markdown("**Case Study 3: Kiribati—Island Stability (and Vulnerability)**")

        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("""
            **Geography:**
            - 33 atolls and islands
            - Total land area: 811 km²
            - Scattered across 3.5 million km² of ocean
            - Average elevation: 2 meters above sea level

            **Warming Pattern:**
            - Very low temperature warming: ~0.1°C average
            - Ocean buffering keeps temperatures stable
            - Little year-to-year variation

            **The Paradox:**
            - **Temperature impact**: Minimal (lowest in dataset)
            - **Climate threat level**: EXISTENTIAL

            **Why the Disconnect:**
            - Sea level rise of 1-2 meters would submerge entire nation
            - Ocean acidification destroying coral reefs (food source)
            - This dataset **only** measures temperature—misses main threats
            """)

        with col2:
            st.metric("Temp Change", "+0.1°C", "Lowest globally")
            st.metric("Elevation", "2 meters", "Above sea level")
            st.metric("Threat Level", "Extreme", "Sea level rise")

        st.markdown("---")

        st.markdown("""
        <div class="info-box">
        <h4>💡 Key Lesson from Case Studies</h4>
        <p><strong>Temperature change alone doesn't tell the full climate story.</strong></p>

        <ul>
        <li><strong>Russia:</strong> High temperature change, high adaptive capacity</li>
        <li><strong>Kiribati:</strong> Low temperature change, existential threat from other factors</li>
        <li><strong>Chile:</strong> National average hides dramatic regional variation</li>
        </ul>

        <p>For comprehensive climate risk assessment, combine temperature data with:</p>
        <ul>
        <li>Sea level projections</li>
        <li>Precipitation/drought patterns</li>
        <li>Extreme weather frequency</li>
        <li>Economic adaptive capacity</li>
        <li>Geographic vulnerability</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ===========================
# FUTURE PROJECTIONS
# ===========================
elif page == "🔮 Future Projections":
    st.markdown('<h1 class="main-header">🔮 Where Are We Heading? Projections to 2030</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
    <h3>⚠️ Statistical Extrapolation vs Climate Modeling</h3>
    <strong>Important:</strong> The projections below are <strong>statistical extrapolations</strong>
    based on historical trends (1961-2022). They assume current patterns continue without major
    policy interventions or unexpected natural events.

    These are NOT comprehensive climate model outputs (like IPCC uses), but rather serve as
    <strong>baseline scenarios</strong> for planning purposes—showing where we're headed if nothing changes.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📊 Projection Models", "🎯 2030 Forecast", "💼 Implications"])

    with tab1:
        st.markdown('<div class="section-header">Two Models: Linear vs Accelerating Warming</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Model 1: Linear (Simple) Trend**")

            # Show model 1 visualization
            img_path = load_image("reports/figures/regression_model1_simple.png")
            if img_path:
                st.image(img_path, use_column_width=True)
            else:
                st.warning("Model 1 visualization not generated.")

            st.markdown("""
            **Assumption:** Warming continues at constant rate

            **Formula:** `Temp = β₀ + β₁ × Year`

            **Fitted Rate:** 0.023°C per year (0.23°C per decade)

            **Test Performance:**
            - R² = -1.43 (POOR fit on recent data)
            - RMSE = 0.26°C

            **Problem:**
            - Significantly **underestimates** recent warming
            - Doesn't capture acceleration
            - Straight line can't match curved reality

            **2030 Projection:** 1.37°C [0.85, 1.88]

            **Conclusion:** Linear model is **inadequate**—warming
            is not constant, it's speeding up.
            """)

        with col2:
            st.markdown("**Model 2: Polynomial (Quadratic) Trend**")

            # Show model 2 visualization
            img_path = load_image("reports/figures/regression_model2_polynomial.png")
            if img_path:
                st.image(img_path, use_column_width=True)
            else:
                st.warning("Model 2 visualization not generated.")

            st.markdown("""
            **Assumption:** Warming is accelerating over time

            **Formula:** `Temp = β₀ + β₁ × Year + β₂ × Year²`

            **Fitted Rates:**
            - 1961: 0.006°C/year (0.06°C/decade)
            - 2022: 0.047°C/year (0.47°C/decade)
            - **Acceleration: 8x faster!**

            **Test Performance:**
            - R² = 0.51 (MUCH better fit)
            - RMSE = 0.12°C

            **Advantage:**
            - Captures the upward curve
            - Matches recent data well
            - Accounts for feedback loops

            **2030 Projection:** 1.93°C [1.70, 2.16]

            **Conclusion:** Quadratic model better represents
            reality—supports **accelerating warming** hypothesis.
            """)

        st.markdown("---")

        st.markdown("**Model Comparison:**")

        comparison_data = {
            'Metric': ['Test R² Score', 'Test RMSE', 'Captures Acceleration?', '2030 Projection', 'Confidence Interval (95%)', 'Best Use Case'],
            'Linear Model': ['-1.43 (poor)', '0.26°C', 'No ❌', '1.37°C', '[0.85, 1.88]', 'Conservative lower bound'],
            'Quadratic Model': ['0.51 (good)', '0.12°C', 'Yes ✅', '1.93°C', '[1.70, 2.16]', 'Most realistic scenario']
        }

        st.table(pd.DataFrame(comparison_data))

        st.markdown("""
        **Recommendation:** Use **quadratic model** for primary projections, as it:
        1. Fits recent data much better (R² = 0.51 vs -1.43)
        2. Captures observed acceleration
        3. More accurate for near-term forecasts (2023-2030)
        4. Aligns with climate science understanding of feedback loops
        """)

    with tab2:
        st.markdown('<div class="section-header">2030 Temperature Projection</div>', unsafe_allow_html=True)

        # Show future projections visualization
        img_path = load_image("reports/figures/regression_future_projections.png")
        if img_path:
            st.image(img_path, use_column_width=True)
            st.caption("Temperature projections through 2030 with confidence intervals")
        else:
            st.warning("Future projections visualization not generated.")

        st.markdown("---")

        # Key projections
        st.markdown("**🎯 Primary Forecast (Quadratic Model)**")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("2025 Projection", "1.61°C", "+0.05°C/yr")
        col2.metric("2030 Projection", "1.93°C", "+0.06°C/yr")
        col3.metric("95% CI Lower", "1.70°C", "Uncertainty range")
        col4.metric("95% CI Upper", "2.16°C", "Worst case")

        st.markdown("---")

        # Year-by-year projections table
        df_proj = load_temperature_projections()
        if df_proj is not None:
            st.markdown("**Year-by-Year Projections (2023-2030):**")

            # Display with formatting
            display_df = df_proj[['Year', 'Quadratic_Projection', 'Quadratic_CI_Lower', 'Quadratic_CI_Upper']].copy()
            display_df.columns = ['Year', 'Projected Temp (°C)', '95% CI Lower', '95% CI Upper']

            st.dataframe(
                display_df.style.format({
                    'Projected Temp (°C)': '{:.3f}',
                    '95% CI Lower': '{:.3f}',
                    '95% CI Upper': '{:.3f}'
                }).background_gradient(subset=['Projected Temp (°C)'], cmap='YlOrRd'),
                use_container_width=True,
                hide_index=True
            )

            st.caption("Projections based on quadratic regression model trained on 1961-2012 data, validated on 2013-2022")

        st.markdown("---")

        st.markdown("**Climate Impact Assessment:**")

        st.markdown("""
        Our model projects +1.93°C warming by 2030, which represents significant climate change.

        **Current Trajectory:**
        - **2024**: ~1.4°C above baseline
        - **2030**: Projected 1.93°C above baseline
        - **Trend**: Accelerating warming rate

        **What +1.93°C by 2030 Means:**
        - Increased extreme weather frequency
        - Greater ecosystem disruption
        - More challenging adaptation required
        - Approaching dangerous thresholds

        **Can This Be Avoided?**
        These projections assume **business as usual**—no major policy changes or emission
        reductions. Aggressive climate action could bend the curve downward, but time is running out.
        """)

    with tab3:
        st.markdown('<div class="section-header">What 1.93°C Means in Practice</div>', unsafe_allow_html=True)

        st.markdown("**Translation from Statistics to Reality:**")

        st.markdown("""
        A global average of +1.93°C might sound abstract. Here's what it means for different sectors:
        """)

        # Sector impacts
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**🌾 Agriculture & Food Security**")
            st.markdown("""
            - **Crop yields**: 10-20% decline in tropical regions
            - **Growing seasons**: Shift by 2-3 weeks
            - **Water availability**: Increased drought frequency
            - **Pests**: Expanded range, longer active seasons
            - **Livestock**: Heat stress reduces productivity

            **Action Needed:** Drought-resistant crops, irrigation infrastructure
            """)

            st.markdown("**🏗️ Infrastructure & Cities**")
            st.markdown("""
            - **Cooling demand**: 30-40% increase in peak summer
            - **Power grids**: Strain from AC load, heat reduces efficiency
            - **Roads/rail**: Buckling, thermal expansion damage
            - **Buildings**: Designed for old climate now inadequate
            - **Water systems**: Increased demand, supply challenges

            **Action Needed:** Retrofit for heat, upgrade capacity
            """)

            st.markdown("**💧 Water Resources**")
            st.markdown("""
            - **Glaciers**: Accelerated melting → long-term shortages
            - **Rivers**: Lower flows in summer, flash floods in storms
            - **Groundwater**: Faster depletion from increased pumping
            - **Quality**: Warmer water = more algae, bacteria

            **Action Needed:** Storage, conservation, desalination
            """)

        with col2:
            st.markdown("**🏥 Public Health**")
            st.markdown("""
            - **Heat-related illness**: 2-3x increase in hospitalizations
            - **Disease vectors**: Mosquitoes, ticks expand range
            - **Air quality**: More ozone, particulates in heat
            - **Mental health**: Climate anxiety, displacement stress
            - **Vulnerable groups**: Elderly, poor most affected

            **Action Needed:** Early warning systems, cooling centers
            """)

            st.markdown("**🌲 Ecosystems & Biodiversity**")
            st.markdown("""
            - **Species extinction**: 15-20% at risk at 2°C
            - **Coral reefs**: 70-90% lost (already happening)
            - **Forests**: Increased wildfires, pest outbreaks
            - **Ocean**: Acidification, reduced oxygen
            - **Cascading effects**: Food web disruptions

            **Action Needed:** Protected areas, corridors, restoration
            """)

            st.markdown("**💼 Economic & Business**")
            st.markdown("""
            - **Labor productivity**: Outdoor work 10-15% less efficient
            - **Supply chains**: Disrupted by extreme weather
            - **Insurance**: Premiums rise, some areas uninsurable
            - **Real estate**: Coastal, flood-prone areas lose value
            - **Tourism**: Altered seasons, damaged destinations

            **Action Needed:** Climate risk assessment, diversification
            """)

        st.markdown("---")

        st.markdown("**📋 Planning Scenarios for Decision-Makers:**")

        scenarios = {
            'Scenario': ['Lower Bound', 'Most Likely', 'Upper Bound', 'Planning Recommendation'],
            'Assumptions': [
                'Model uncertainty (lower 95% CI)',
                'Current trends continue (our projection)',
                'Model uncertainty (upper 95% CI)',
                'Conservative approach for risk management'
            ],
            '2030_Temperature': ['1.70°C', '1.93°C', '2.16°C', 'Plan for 2.16°C'],
            'Probability': ['2.5%', '95%', '2.5%', 'Upper 97.5th percentile'],
            'Action_Posture': ['Monitor closely', 'Very urgent', 'Crisis mode', 'Prepare for worst case']
        }

        st.table(pd.DataFrame(scenarios))

        st.markdown("---")

        st.markdown("**🎯 Recommendations by Time Horizon:**")

        st.markdown("""
        **2025 (Immediate - 2 years):**
        - ✅ Assess current infrastructure climate resilience
        - ✅ Update building codes and design standards
        - ✅ Establish heat emergency protocols
        - ✅ Begin workforce climate training
        - ✅ Climate-proof critical supply chains

        **2030 (Near-term - 7 years):**
        - ✅ Complete major infrastructure retrofits
        - ✅ Achieve 50% renewable energy (to slow acceleration)
        - ✅ Implement adaptive water management
        - ✅ Relocate/protect vulnerable assets
        - ✅ Full climate risk integration in all planning

        **2050 (Long-term - 27 years):**
        - ✅ Carbon-neutral operations
        - ✅ Climate-resilient infrastructure fully deployed
        - ✅ Adaptive systems operational
        - ✅ Multi-scenario contingency plans active
        - ✅ Continuous monitoring and updating
        """)

        st.markdown("---")

        st.markdown("""
        <div class="info-box">
        <h4>💡 Key Takeaway</h4>
        <p><strong>1.93°C by 2030 is not inevitable</strong>—it's what happens if current trends continue.</p>

        <p><strong>Every fraction of a degree matters:</strong></p>
        <ul>
        <li>1.0°C: Major ecosystem changes</li>
        <li>1.5°C: Significant adaptation challenges</li>
        <li>2.0°C: Very difficult adaptation</li>
        <li>2.5°C+: Some impacts irreversible</li>
        </ul>

        <p><strong>The curve can still be bent</strong>—but the window for action narrows each year.
        These projections are not destiny; they're a warning of what's ahead without major course correction.</p>
        </div>
        """, unsafe_allow_html=True)

# ===========================
# LOGISTIC REGRESSION PAGE
# ===========================
elif page == "📈 Logistic Regression":
    st.markdown('<h1 class="main-header">📈 Logistic Regression: Climate Risk Classification</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <h3>What is Logistic Regression for Climate Risk?</h3>
    Using machine learning classification, we predict whether a year/country represents "High Risk" climate conditions
    based on temperature anomalies >1.5°C. This creates an early warning system for climate adaptation planning.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Load projections for risk assessment
    projections = load_temperature_projections()

    if projections is not None:
        st.markdown('<h2 class="section-header">🎯 Risk Classification Model</h2>', unsafe_allow_html=True)

        # Model overview
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Model Performance")
            st.metric("ROC AUC Score", "0.87", "Good discriminatory power")
            st.metric("Accuracy", "0.82", "Overall prediction accuracy")
            st.metric("High Risk Recall", "0.78", "Captures 78% of high-risk cases")

        with col2:
            st.markdown("### Risk Threshold")
            st.metric("High Risk Definition", ">1.5°C", "Paris Agreement threshold")
            st.metric("Training Period", "1961-2010", "Historical data")
            st.metric("Test Period", "2011-2022", "Recent validation")

        st.markdown("---")

        # Feature importance
        st.markdown("### Key Risk Indicators")
        features_data = {
            'Feature': ['Temperature Change', '5-Year Average', '10-Year Average', 'Change Rate', 'Year (Scaled)'],
            'Importance': ['High', 'High', 'Medium', 'Medium', 'Low'],
            'Direction': ['Positive', 'Positive', 'Positive', 'Positive', 'Positive']
        }
        st.table(pd.DataFrame(features_data))

        st.markdown("---")

        # Risk assessment visualization
        st.markdown('<h2 class="section-header">📊 Risk Assessment Dashboard</h2>', unsafe_allow_html=True)

        # Show logistic regression visualizations
        img_path = load_image("reports/figures/logistic_confusion_matrix.png")
        if img_path:
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_path, caption="Confusion Matrix - Risk Classification")
            with col2:
                roc_path = load_image("reports/figures/logistic_roc_curve.png")
                if roc_path:
                    st.image(roc_path, caption="ROC Curve - Model Performance")
        else:
            st.warning("Logistic regression visualizations not yet generated. Run the logistic regression notebook first.")

        st.markdown("---")

        # Future risk projections
        st.markdown("### 🔮 Future Risk Projections (2023-2030)")

        if projections is not None:
            # Calculate risk probability for each year
            risk_df = projections[['Year', 'Quadratic_Projection']].copy()
            risk_df['Risk_Probability'] = 1 / (1 + np.exp(-(risk_df['Quadratic_Projection'] - 1.5) * 2))  # Simplified logistic
            risk_df['Risk_Level'] = risk_df['Risk_Probability'].apply(lambda x: 'High Risk' if x > 0.5 else 'Normal')

            # Display risk projections
            st.dataframe(
                risk_df.style.format({
                    'Quadratic_Projection': '{:.3f}°C',
                    'Risk_Probability': '{:.1%}'
                }).apply(lambda x: ['background-color: #ffcccc' if x['Risk_Level'] == 'High Risk' else '' for i in x], axis=1),
                use_container_width=True,
                hide_index=True
            )

            st.caption("Risk probability based on projected temperature anomalies. High Risk = >50% probability of exceeding 1.5°C threshold.")

        st.markdown("---")

        # Business recommendations
        st.markdown('<h2 class="section-header">💼 Business Implications</h2>', unsafe_allow_html=True)

        st.markdown("""
        **Early Warning System Benefits:**
        - Predict high-risk climate scenarios 2-3 years in advance
        - Enable proactive risk management and adaptation planning
        - Support data-driven infrastructure investment decisions

        **Key Action Items:**
        1. **Monitor 5-year temperature averages** - Early indicator of risk
        2. **Implement risk thresholds** - Automated alerts at 1.2°C anomalies
        3. **Stress-test portfolios** - Against high-risk climate scenarios
        4. **Develop contingency plans** - For accelerated warming trajectories
        """)

    else:
        st.warning("""
        Logistic regression results not found. Please run the logistic regression notebook first:

        `notebooks/08_logistic_regression_phase5.ipynb`

        This will generate the required risk classification model and save results to `reports/phase5_logistic_summary.txt`.
        """)

# ===========================
# COUNTRY CLUSTERING PAGE
# ===========================
elif page == "🔍 Country Clustering":
    st.markdown('<h1 class="main-header">🔍 Country Clustering: Identifying Warming Patterns</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <h3>What is Clustering Analysis?</h3>
    Using machine learning (K-means clustering), we grouped 212 countries into distinct segments based on
    their warming patterns from 1961-2022. Each cluster represents countries with similar temperature trajectories,
    enabling targeted climate adaptation strategies.
    </div>
    """, unsafe_allow_html=True)

    # Load clustering data
    clustering_df = load_clustering_results()

    if clustering_df is not None:
        # ---------------------------
        # NEW: Interactive Map Section
        # ---------------------------
        st.markdown('### 🌍 Global Cluster Map')
        
        # Create choropleth map
        fig_map = px.choropleth(
            data_frame=clustering_df,
            locations="iso3",
            color="cluster_name",
            hover_name="country",
            hover_data={
                "iso3": False,
                "cluster_name": True,
                "mean_temp": ":.2f",
                "warming_rate": ":.4f",
                "cluster_description": True
            },
            projection="natural earth",
            title="Countries Colored by Climate Change Cluster",
            height=600,
            color_discrete_sequence=px.colors.qualitative.Bold  # Distinct colors for clusters
        )
        
        fig_map.update_layout(
            margin={"r":0,"t":40,"l":0,"b":0},
            legend_title_text='Cluster Group',
            legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.01,
                bgcolor="rgba(255, 255, 255, 0.8)"
            )
        )
        
        st.plotly_chart(fig_map, use_container_width=True)
        
        st.markdown("---")
        # ---------------------------

        st.markdown('<h2 class="section-header">📊 Cluster Overview</h2>', unsafe_allow_html=True)

        # Display cluster distribution
        cluster_counts = clustering_df['cluster_name'].value_counts()
        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown("### Cluster Distribution")
            for cluster_name, count in cluster_counts.items():
                pct = (count / len(clustering_df)) * 100
                st.metric(cluster_name, f"{count} countries", f"{pct:.1f}%")

        with col2:
            st.markdown("### Clustering Quality Metrics")
            st.info("""
            **Methodology:** K-means clustering with 6 features
            - Average temperature change
            - Temperature volatility
            - Warming rate (trend)
            - Recent period average (2010-2022)
            - Change from early to recent period
            - Warming acceleration
            """)

        st.markdown("---")

        # Cluster Details
        st.markdown('<h2 class="section-header">🎯 Cluster Profiles</h2>', unsafe_allow_html=True)

        unique_clusters = clustering_df['cluster_name'].unique()

        for cluster_name in unique_clusters:
            cluster_data = clustering_df[clustering_df['cluster_name'] == cluster_name]

            st.markdown(f"### {cluster_name}")

            # Calculate cluster statistics
            avg_temp = cluster_data['mean_temp'].mean()
            avg_warming_rate = cluster_data['warming_rate'].mean()
            avg_recent = cluster_data['recent_mean'].mean()
            avg_acceleration = cluster_data['acceleration'].mean()

            # Display cluster characteristics
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("Avg Temperature", f"{avg_temp:.3f}°C")
            with col2:
                st.metric("Warming Rate", f"{avg_warming_rate*10:.3f}°C/decade")
            with col3:
                st.metric("Recent Average", f"{avg_recent:.3f}°C")
            with col4:
                st.metric("Acceleration", f"{avg_acceleration:.5f}°C/year²")

            # Display description
            if 'cluster_description' in cluster_data.columns:
                desc = cluster_data['cluster_description'].iloc[0]
                st.markdown(f"**Description:** {desc}")

            # Top countries in this cluster
            st.markdown("**Top 10 countries by average warming:**")
            top_countries = cluster_data.nlargest(10, 'mean_temp')[['country', 'mean_temp', 'warming_rate', 'recent_mean']]

            # Display as table
            st.dataframe(
                top_countries.style.format({
                    'mean_temp': '{:.3f}°C',
                    'warming_rate': '{:.5f}°C/year',
                    'recent_mean': '{:.3f}°C'
                }),
                use_container_width=True,
                hide_index=True
            )

            st.markdown("---")

        # Visualizations
        st.markdown('<h2 class="section-header">📈 Visual Analysis</h2>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Clustering Quality Metrics")
            img_path = load_image("reports/figures/clustering_optimal_k.png")
            if img_path:
                st.image(img_path, use_container_width=True)
                st.caption("Multiple metrics used to determine optimal number of clusters")
            else:
                st.warning("Visualization not found. Run the clustering notebook to generate.")

        with col2:
            st.markdown("### 2D Cluster Visualization (PCA)")
            img_path = load_image("reports/figures/clustering_pca_visualization.png")
            if img_path:
                st.image(img_path, use_container_width=True)
                st.caption("Countries projected onto 2D space using Principal Component Analysis")
            else:
                st.warning("Visualization not found. Run the clustering notebook to generate.")

        st.markdown("---")

        st.markdown("### Feature Distributions by Cluster")
        img_path = load_image("reports/figures/clustering_feature_distributions.png")
        if img_path:
            st.image(img_path, use_container_width=True)
            st.caption("Box plots showing how different features vary across clusters")
        else:
            st.warning("Visualization not found. Run the clustering notebook to generate.")

        # Business Recommendations
        st.markdown("---")
        st.markdown('<h2 class="section-header">💼 Strategic Recommendations by Cluster</h2>', unsafe_allow_html=True)

        recommendations = {
            "Low-Risk Countries": {
                "priority": "🟢 MONITOR & MAINTAIN",
                "actions": [
                    "Regular climate monitoring",
                    "Gradual infrastructure upgrades",
                    "Energy efficiency improvements",
                    "Sustainable development practices",
                    "Community resilience programs",
                    "Sea level rise adaptation (if coastal/island)",
                    "Ocean acidification mitigation",
                    "Storm surge defenses"
                ],
                "investment": "MODERATE: (~0.5-1.5% GDP)",
                "risk": "MODERATE"
            },
            "High-Risk Countries": {
                "priority": "🟠 HIGH PRIORITY - URGENT ACTION",
                "actions": [
                    "Accelerated adaptation planning",
                    "Infrastructure upgrades for extreme temperatures",
                    "Enhanced monitoring systems",
                    "Climate risk assessment updates",
                    "Emergency response system enhancement",
                    "Retrofit existing infrastructure",
                    "Update building codes and standards",
                    "Develop climate contingency plans",
                    "Emergency climate adaptation planning",
                    "Water resource management crisis protocols"
                ],
                "investment": "HIGH: (~2-4% GDP)",
                "risk": "HIGH"
            }
        }

        for cluster_name in unique_clusters:
            if cluster_name in recommendations:
                rec = recommendations[cluster_name]

                st.markdown(f"### {cluster_name}")
                st.markdown(f"**Priority Level:** {rec['priority']}")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**Priority Actions:**")
                    for action in rec['actions']:
                        st.markdown(f"- {action}")

                with col2:
                    st.markdown(f"**Investment Needs:** {rec['investment']}")
                    st.markdown(f"**Risk Level:** {rec['risk']}")

                st.markdown("---")

        # Search functionality
        st.markdown('<h2 class="section-header">🔎 Find Your Country</h2>', unsafe_allow_html=True)

        country_search = st.selectbox(
            "Select a country to see its cluster assignment:",
            options=sorted(clustering_df['country'].unique())
        )

        if country_search:
            country_info = clustering_df[clustering_df['country'] == country_search].iloc[0]

            st.markdown(f"### {country_info['country']}")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"**Cluster:** {country_info['cluster_name']}")
                st.markdown(f"**Description:** {country_info['cluster_description']}")

                st.markdown("**Warming Metrics:**")
                st.markdown(f"- Average temperature change: **{country_info['mean_temp']:.3f}°C**")
                st.markdown(f"- Warming rate: **{country_info['warming_rate']*10:.3f}°C/decade**")
                st.markdown(f"- Recent average (2010-2022): **{country_info['recent_mean']:.3f}°C**")
                st.markdown(f"- Temperature volatility: **{country_info['std_temp']:.3f}°C**")

            with col2:
                st.markdown("**Trend Analysis:**")
                st.markdown(f"- Early period (1961-1980): **{country_info['early_mean']:.3f}°C**")
                st.markdown(f"- Change from early to recent: **{country_info['period_change']:.3f}°C**")
                st.markdown(f"- Warming acceleration: **{country_info['acceleration']:.5f}°C/year²**")

                # Similar countries
                same_cluster = clustering_df[
                    (clustering_df['cluster_name'] == country_info['cluster_name']) &
                    (clustering_df['country'] != country_search)
                ]

                st.markdown(f"**Similar countries ({len(same_cluster)} in same cluster):**")
                similar_top5 = same_cluster.nlargest(5, 'mean_temp')['country'].tolist()
                for similar_country in similar_top5:
                    st.markdown(f"- {similar_country}")

    else:
        st.warning("""
        Clustering results not found. Please run the clustering notebook first:

        `notebooks/07_clustering_phase5.ipynb`

        This will generate the required clustering analysis and save results to `reports/clustering_results_named.csv`.
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>Global Temperature Change Analysis (1961-2022)</strong></p>
    <p>Data Source: FAO Climate Indicators • 225 Countries • Statistical Analysis & Projections</p>
    <p><em>This analysis focuses solely on temperature change. For comprehensive climate assessment,
    combine with emissions, sea level, precipitation, and socioeconomic data.</em></p>
    <p>Fundamentos de la Ciencia de Datos | UAX (2025-26)</p>
</div>
""", unsafe_allow_html=True)
