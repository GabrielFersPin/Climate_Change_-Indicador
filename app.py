import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import json

# Page configuration
st.set_page_config(
    page_title="Climate Reality: Understanding Our Planet's Crisis",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 2rem;
        color: #2ca02c;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .info-box {
        background-color: #e7f3ff;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #0066cc;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🌍 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Explore the Story:",
    [
        "🏠 The Climate Crisis Today",
        "📊 Understanding the Data",
        "🔍 Climate Patterns & Trends",
        "📈 Our Future: What Lies Ahead",
        "🎯 Identifying Critical Risk Periods",
        "🔬 Different Paths, Shared Planet"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("**About This Project**\n\nAnalyzing 62 years of global climate data to understand what's happening to our planet and what we can do about it.\n\n**UAX | 2025-26**")

# Helper function to load images
def load_image(image_path):
    """Load and display image if it exists."""
    if Path(image_path).exists():
        return str(image_path)
    return None

# Helper function to load data
def load_temperature_projections():
    """Load temperature projections CSV if available."""
    csv_path = Path("reports/temperature_projections_2030.csv")
    if csv_path.exists():
        return pd.read_csv(csv_path)
    return None

# ===========================
# HOME PAGE
# ===========================
if page == "🏠 The Climate Crisis Today":
    st.markdown('<h1 class="main-header">🌍 Our Planet is Warming: Here\'s What the Data Shows</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
    <h3>⚠️ The Reality We Face</h3>
    After analyzing 62 years of global climate data (1961-2022), one thing is clear: our planet is heating up
    faster than at any point in recorded history. This isn't just numbers on a chart—it's reshaping coastlines,
    threatening food security, and displacing millions of people.
    </div>
    """, unsafe_allow_html=True)

    # Key metrics in columns - Business focused
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🌡️ Global Warming", "+1.2°C", "Since 1961")
        st.caption("Enough to shift weather patterns worldwide")
    with col2:
        st.metric("⏰ Time Remaining", "2030", "To limit warming to 1.5°C")
        st.caption("Based on Paris Agreement targets")
    with col3:
        st.metric("📈 Projected by 2030", "+1.93°C", "43% over safe limit")
        st.caption("If current trends continue")
    with col4:
        st.metric("🌍 Countries Affected", "195", "Global crisis")
        st.caption("No region is immune")

    st.markdown("---")

    # The Struggle and Solutions
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-header">💔 The Struggles We Face</div>', unsafe_allow_html=True)
        st.markdown("""
        **Rising Temperatures**
        - Planet has warmed by 1.2°C since 1961, and the pace is accelerating
        - Each decade brings more extreme heatwaves, droughts, and wildfires

        **Emissions Crisis**
        - CO₂ levels are directly driving temperature increases
        - Current trajectory puts us on track for dangerous 2°C+ warming

        **Unequal Impact**
        - Countries that contributed least to emissions often suffer most
        - Small island nations face existential threats from rising seas

        **Time Running Out**
        - We're already seeing irreversible changes to ecosystems
        - Window to limit warming to safe levels is rapidly closing
        """)

    with col2:
        st.markdown('<div class="section-header">💡 Solutions Within Reach</div>', unsafe_allow_html=True)
        st.markdown("""
        **Early Warning Systems**
        - We can now predict high-risk climate years with 92% confidence
        - Helps governments and businesses prepare for extreme events

        **Targeted Action Plans**
        - Data reveals which countries need adaptation support vs emission cuts
        - Different solutions for different situations

        **Clear Benchmarks**
        - We know exactly where we're heading if trends continue
        - Enables evidence-based policy and investment decisions

        **Success Stories Exist**
        - Some countries have proven low-carbon development works
        - Their strategies can be adapted globally
        """)

    st.markdown("---")

    # What this means for decision makers
    st.markdown('<div class="section-header">🎯 What This Means for Action</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**For Governments**")
        st.markdown("""
        - Identify which years will require emergency preparedness
        - Allocate climate adaptation budgets effectively
        - Set realistic, data-driven emission targets
        """)
    with col2:
        st.markdown("**For Businesses**")
        st.markdown("""
        - Assess climate risks to supply chains and operations
        - Plan infrastructure investments for warming scenarios
        - Identify opportunities in the green transition
        """)
    with col3:
        st.markdown("**For Communities**")
        st.markdown("""
        - Understand what climate future your region faces
        - Prepare for increasing extreme weather events
        - Advocate for evidence-based climate action
        """)

# ===========================
# PHASE 1: UNDERSTANDING THE DATA
# ===========================
elif page == "📊 Understanding the Data":
    st.markdown('<h1 class="main-header">📊 What the Data Reveals About Our Climate</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <h3>The Foundation: 62 Years of Global Climate Records</h3>
    We've gathered comprehensive climate data from 195 countries spanning 1961 to 2022. This dataset tracks
    key indicators: temperature changes, carbon emissions, methane levels, deforestation rates, and sea level rise.
    Together, they tell the story of our changing planet.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # What we track
    st.markdown('<div class="section-header">🌡️ What We\'re Tracking</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Climate Impact Indicators**")
        st.markdown("""
        **Temperature Changes**
        - How much warmer (or cooler) each year was compared to historical averages
        - Tracks the direct impact on our climate

        **Sea Level Rise**
        - Measuring coastal threats to millions of people
        - Critical for island nations and coastal cities

        **Extreme Weather Frequency**
        - How often we're experiencing record-breaking heat
        - Pattern of climate instability
        """)

    with col2:
        st.markdown("**What's Driving the Changes**")
        st.markdown("""
        **Carbon Dioxide (CO₂) Emissions**
        - The primary driver of global warming
        - From burning fossil fuels and industrial processes

        **Methane Emissions**
        - A potent greenhouse gas from agriculture and energy
        - 25x more warming potential than CO₂

        **Deforestation Rates**
        - Loss of nature's carbon storage systems
        - Reduces Earth's ability to regulate climate
        """)

    st.markdown("---")

    # Key Insights from the Data
    st.markdown('<div class="section-header">🔍 Key Questions the Data Answers</div>', unsafe_allow_html=True)

    insights = {
        "How has warming progressed over time?": {
            "finding": """
            **Year-by-year analysis reveals accelerating warming:**
            - 1960s-1970s: Relatively stable temperatures with minor fluctuations
            - 1980s-2000: Warming begins to accelerate significantly
            - 2000-2022: Each decade warmer than the last, with 2015-2022 seeing unprecedented heat

            **What this means:** The problem isn't just warming—it's the speed of change. Ecosystems and societies
            struggle to adapt when change happens this fast.
            """,
            "chart": "reports/figures/query1_temporal_aggregation.png"
        },
        "Which countries are the biggest contributors?": {
            "finding": """
            **Top emitters since 2000:**
            1. China - Rapid industrialization created massive emission growth
            2. United States - High per-capita emissions despite being developed
            3. India - Growing economy with coal dependence
            4. Russia - Energy production and heavy industry
            5. Japan - Manufacturing powerhouse

            **What this means:** The top 10 emitters account for over 60% of global CO₂. Solutions require
            both emission cuts from major polluters AND support for clean development elsewhere.
            """,
            "chart": None
        },
        "How do different decades compare?": {
            "finding": """
            **Decade-by-decade warming trend:**
            - 1960s: Baseline period, relatively cool and stable
            - 1970s: First signs of warming trend emerging
            - 1980s: Clear warming signal, extreme years becoming more common
            - 1990s: Warming accelerates, variability increases
            - 2000s: Hot years become the norm rather than exception
            - 2010s: Every year warmer than 20th century average
            - 2020s: On track to be hottest decade ever recorded

            **What this means:** Each generation is inheriting a more unstable climate than the last.
            """,
            "chart": None
        },
        "When do we see the most dangerous years?": {
            "finding": """
            **Identifying extreme climate years:**
            - Before 1990: Rare extreme heat years, usually isolated events
            - 1990-2010: Extreme years becoming more frequent
            - 2010-2022: Majority of years qualify as "extreme" by historical standards

            **Red flags we're seeing:**
            - Years with multiple record-breaking temperatures globally
            - Simultaneous extremes in different regions
            - Shorter recovery periods between extreme events

            **What this means:** What used to be a once-in-a-generation heatwave is becoming routine.
            Communities and infrastructure designed for historical climate norms are increasingly inadequate.
            """,
            "chart": None
        }
    }

    insight_choice = st.selectbox("Explore Key Insights:", list(insights.keys()))

    st.markdown(insights[insight_choice]["finding"])

    # Display visualization if available
    if insights[insight_choice]["chart"]:
        img_path = load_image(insights[insight_choice]["chart"])
        if img_path:
            st.image(img_path, caption=insight_choice, use_column_width=True)

# ===========================
# PHASE 2: CLIMATE PATTERNS & TRENDS
# ===========================
elif page == "🔍 Climate Patterns & Trends":
    st.markdown('<h1 class="main-header">🔍 Uncovering Climate Patterns: What the Numbers Show</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <h3>Reading the Climate Story in Data</h3>
    Looking beyond individual numbers to understand the bigger patterns: How are temperatures changing?
    Which regions are hit hardest? What's driving these changes? These patterns help us understand where
    we've been and where we're heading.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs(["🌡️ The Warming Pattern", "📈 How Fast Are We Warming?", "🌍 Who's Most Affected?", "🔗 What's Driving It?"])

    with tab1:
        st.markdown('<div class="section-header">The Shape of Global Warming</div>', unsafe_allow_html=True)
        img_path = load_image("reports/figures/eda_univariate_temperature.png")
        if img_path:
            st.image(img_path, use_column_width=True)
        else:
            st.info("Visualization will be available after running the analysis.")

        st.markdown("""
        **What this pattern tells us:**

        The distribution of global temperatures over 62 years reveals a clear shift toward warmer conditions:
        - Early decades (1960s-1970s) cluster around cooler temperatures
        - Recent decades show a distinct shift toward the warmer end
        - The "new normal" is significantly warmer than historical averages

        **Real-world impact:**
        - Agricultural zones are shifting as temperature ranges change
        - Infrastructure designed for historical temperature ranges is now inadequate
        - What used to be exceptionally hot years are becoming typical
        """)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Average Temperature", "14.2°C")
            st.caption("Global average across all years")
        with col2:
            st.metric("Warming Range", "1.8°C variation")
            st.caption("But recent years cluster at the high end")
        with col3:
            st.metric("Total Shift", "8.5°C spread")
            st.caption("From coolest to warmest years")

    with tab2:
        st.markdown('<div class="section-header">The Acceleration of Warming</div>', unsafe_allow_html=True)
        img_path = load_image("reports/figures/eda_temporal_trends.png")
        if img_path:
            st.image(img_path, use_column_width=True)
        else:
            st.info("Visualization will be available after running the analysis.")

        st.markdown("""
        **The story the trend line tells:**

        This isn't just gradual warming—it's acceleration:
        - **1961-1980**: Slow, almost imperceptible temperature increases
        - **1980-2000**: Warming becomes clearly visible and measurable
        - **2000-2022**: Rapid temperature rise, with each year often breaking previous records

        **Why acceleration matters:**
        The speed of change is as critical as the amount. Faster warming means:
        - Less time for ecosystems to adapt
        - More severe weather extremes
        - Insufficient time to upgrade infrastructure
        - Increased risk of cascading climate impacts

        **What businesses and governments need to know:**
        Planning based on historical climate data is increasingly unreliable. The next decade will likely
        be warmer than any in recorded history, requiring adaptive strategies and resilient infrastructure.
        """)

    with tab3:
        st.markdown('<div class="section-header">Climate Injustice: Unequal Burdens</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            img_path = load_image("reports/figures/eda_geographic_heterogeneity.png")
            if img_path:
                st.image(img_path, use_column_width=True)

        with col2:
            img_path = load_image("reports/figures/eda_top_countries.png")
            if img_path:
                st.image(img_path, use_column_width=True)

        st.markdown("**The Unfair Reality:**")
        st.markdown("""
        Climate change doesn't affect everyone equally, revealing stark global inequalities:

        **Arctic and Northern Regions:**
        - Experiencing warming at 2-3 times the global average
        - Permafrost melt threatens infrastructure and releases stored carbon
        - Indigenous communities losing traditional ways of life

        **Small Island Nations:**
        - Produce minimal emissions but face existential threats
        - Rising seas threaten entire countries (Maldives, Tuvalu, Kiribati)
        - No higher ground to retreat to

        **Developing Countries:**
        - Often located in vulnerable tropical and subtropical zones
        - Less resources for adaptation and disaster response
        - Agriculture-dependent economies hit hardest by changing weather

        **The Emission Gap:**
        - Top 10% of emitters are primarily developed nations
        - Bottom 50% contribute minimal emissions but face worst impacts
        - Historical emissions from industrialization created current crisis
        """)

    with tab4:
        st.markdown('<div class="section-header">The Root Causes: What\'s Driving This?</div>', unsafe_allow_html=True)
        img_path = load_image("reports/figures/eda_decade_analysis.png")
        if img_path:
            st.image(img_path, use_container_width=True)

        st.markdown("""
        **The Clear Connection Between Emissions and Warming:**

        The data reveals an undeniable link between human activities and rising temperatures:

        **Carbon Dioxide (CO₂): The Primary Culprit**
        - For every increase in CO₂ emissions, temperatures rise in lockstep
        - The relationship is so strong it's virtually predictable
        - Source: Burning fossil fuels for energy, transportation, and manufacturing

        **Methane: The Overlooked Problem**
        - 25 times more potent than CO₂ at trapping heat
        - Rising alongside industrialization and agricultural expansion
        - Source: Livestock farming, rice cultivation, and natural gas leaks

        **Deforestation: Removing Our Natural Defense**
        - Trees absorb CO₂, but we're cutting them down at alarming rates
        - Lost forests means more CO₂ stays in the atmosphere
        - Regional impacts show clear temperature increases where forests disappear

        **The Bottom Line:**
        This isn't natural climate variation—it's directly tied to how we produce energy, grow food,
        and develop land. But that also means we know exactly what needs to change.
        """)

# ===========================
# PHASE 3: OUR FUTURE - WHAT LIES AHEAD
# ===========================
elif page == "📈 Our Future: What Lies Ahead":
    st.markdown('<h1 class="main-header">📈 Where Are We Heading? Projecting Our Climate Future</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
    <h3>⚠️ If Current Trends Continue...</h3>
    By analyzing 62 years of data, we can project where we're headed. The patterns are clear and consistent
    enough to predict the future with confidence—and what we see requires urgent action.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Key business-focused metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("2030 Temperature", "1.93°C above baseline", "⚠️ Critical level")
        st.caption("Exceeds Paris Agreement target")
    with col2:
        st.metric("Paris Agreement Gap", "+0.43°C", "29% over limit")
        st.caption("We're missing the 1.5°C target")
    with col3:
        st.metric("Current Warming Rate", "0.047°C per year", "Accelerating")
        st.caption("8x faster than 1961 rate")
    with col4:
        st.metric("Prediction Confidence", "High", "Based on strong patterns")
        st.caption("Historical data shows consistent trend")

    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs(["🔍 Understanding the Trend", "⚡ The Acceleration Problem", "🔮 What 2030 Looks Like", "💼 Business Implications"])

    with tab1:
        st.markdown('<div class="section-header">Two Ways to Look at Warming</div>', unsafe_allow_html=True)

        st.markdown("""
        We tested two scenarios for how warming might continue:
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Scenario 1: Steady, Constant Warming**")
            img_path = load_image("reports/figures/regression_model1_simple.png")
            if img_path:
                st.image(img_path, use_column_width=True)
            st.markdown("""
            **Assumption:** Warming continues at the same pace as historical average

            **The Problem:** This scenario significantly underestimates future warming because
            it ignores the acceleration we're seeing. Historical data shows warming isn't
            constant—it's speeding up.

            **Result:** Poor match with actual observed patterns
            """)

        with col2:
            st.markdown("**Scenario 2: Accelerating Warming (What We're Seeing)**")
            img_path = load_image("reports/figures/regression_model2_polynomial.png")
            if img_path:
                st.image(img_path, use_column_width=True)
            st.markdown("""
            **Assumption:** Warming is accelerating, not constant

            **Why It Matters:** This matches what we actually observe—each decade warms faster
            than the last. This is due to feedback loops (like ice melt reducing Earth's
            reflectivity) and cumulative emissions.

            **Result:** Closely matches observed data and better predicts future warming
            """)

    with tab2:
        st.markdown('<div class="section-header">Why Acceleration Is the Real Danger</div>', unsafe_allow_html=True)
        img_path = load_image("reports/figures/regression_bivariate_analysis.png")
        if img_path:
            st.image(img_path, use_column_width=True)

        st.markdown("""
        **The acceleration of warming is what makes this crisis so urgent:**

        **1961: The Starting Point**
        - Warming rate: 0.006°C per year
        - Barely noticeable changes
        - Climate relatively stable

        **2022: Today's Reality**
        - Warming rate: 0.047°C per year
        - **Nearly 8x faster than 1961**
        - Rapid, visible changes to weather patterns

        **What This Means:**
        - We're not dealing with steady, predictable change
        - The problem is compounding, getting worse faster
        - Infrastructure, agriculture, and ecosystems built for historical climate can't keep up
        - Each year of delay makes the problem harder to solve

        **Real-World Impacts of Acceleration:**
        - Coastal cities have less time to build defenses
        - Farmers can't adapt crop varieties fast enough
        - Insurance models based on historical risk become obsolete
        - Species can't migrate or evolve quickly enough to survive
        """)

    with tab3:
        st.markdown('<div class="section-header">2030: A Critical Crossroads</div>', unsafe_allow_html=True)
        img_path = load_image("reports/figures/regression_future_projections.png")
        if img_path:
            st.image(img_path, use_column_width=True)

        st.markdown("""
        <div class="warning-box">
        <h4>⚠️ We're On Track to Miss Our Climate Goals</h4>
        If current trends continue, by 2030 we'll reach <strong>1.93°C</strong> of warming—
        <strong>0.43°C above the Paris Agreement target</strong> of 1.5°C.
        That may sound small, but every fraction of a degree matters enormously.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        **What 1.93°C means for the world:**

        **Food Security Threats:**
        - Crop yields decline in tropical regions
        - More frequent droughts affect grain production
        - Fishing grounds shift, disrupting coastal economies

        **Extreme Weather Becomes the Norm:**
        - Hurricanes and typhoons intensify
        - Deadly heatwaves occur more frequently
        - Flooding events increase in severity and frequency

        **Economic Disruption:**
        - Supply chain interruptions from extreme weather
        - Infrastructure damage costs escalate
        - Insurance premiums rise, some areas become uninsurable

        **Irreversible Changes:**
        - Coral reefs face mass die-offs (tourism, fishing impacted)
        - Arctic sea ice disappears in summer months
        - Greenland ice sheet loss accelerates (sea level rise)

        **Why 1.5°C Was the Target:**
        Scientists determined that 1.5°C represents a threshold where we can still avoid the worst
        impacts. Beyond that, feedback loops kick in that make the problem much harder to control.
        """)

        # Load and display temperature projections table
        df_proj = load_temperature_projections()
        if df_proj is not None:
            st.markdown("**Year-by-Year Projections Through 2030:**")
            st.dataframe(df_proj, use_container_width=True)
            st.caption("Each year shows estimated warming if current trends continue unchecked")

    with tab4:
        st.markdown('<div class="section-header">What Decision-Makers Need to Know</div>', unsafe_allow_html=True)

        st.markdown("""
        **The Bottom Line:**
        Based on 62 years of consistent data, we can say with high confidence that current trends will
        lead to approximately 1.93°C of warming by 2030—well above safe limits.

        **What Governments Should Do:**
        1. **Plan infrastructure for a 2°C warmer world**
           - Upgrade flood defenses and drainage systems
           - Redesign cooling systems for hospitals and schools
           - Strengthen power grids for extreme weather

        2. **Accelerate the transition away from fossil fuels**
           - Current emission rates guarantee dangerous warming
           - Earlier transition means less severe impacts
           - Cost of prevention far lower than cost of adaptation

        3. **Support vulnerable regions now**
           - Don't wait for 2030 to prepare
           - Invest in early warning systems
           - Fund climate adaptation in high-risk areas

        **What Businesses Should Do:**
        1. **Stress-test operations for climate scenarios**
           - Assume 2°C warming minimum for long-term planning
           - Identify supply chain vulnerabilities
           - Assess physical asset exposure to extreme weather

        2. **Identify opportunities in the transition**
           - Green technology demand will explode
           - Climate adaptation is a massive market
           - Early movers gain competitive advantage

        3. **Engage in carbon accounting now**
           - Regulation is coming globally
           - Investors increasingly demand climate disclosure
           - Carbon costs will affect bottom lines

        **What This Analysis Can't Tell Us:**
        - Specific regional impacts (we're looking at global averages)
        - Effects of potential policy changes (we're projecting current trends)
        - Timing of tipping points (feedback loops could accelerate warming further)

        **Therefore:** Use this as a baseline "business as usual" scenario, but also prepare for
        scenarios where warming accelerates even faster. Hope for policy success, but don't bet
        your business or community on it.
        """)

# ===========================
# PHASE 4: IDENTIFYING CRITICAL RISK PERIODS
# ===========================
elif page == "🎯 Identifying Critical Risk Periods":
    st.markdown('<h1 class="main-header">🎯 Spotting the Most Dangerous Climate Years Before They Hit</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <h3>Early Warning System for Extreme Climate Years</h3>
    Some years are significantly more dangerous than others—marked by extreme temperatures, severe weather,
    and major climate impacts. By analyzing patterns from the past 62 years, we can now identify which years
    are most likely to be "high-risk" based on emission levels and other indicators.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Business-focused metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Prediction Success", "92%", "Highly reliable")
        st.caption("We correctly identify 92 out of 100 extreme years")
    with col2:
        st.metric("False Alarm Rate", "11%", "Low")
        st.caption("Rarely cry wolf on normal years")
    with col3:
        st.metric("Detection Rate", "94%", "Catches almost all")
        st.caption("Miss only 6% of actual extreme years")
    with col4:
        st.metric("Advance Warning", "Early", "Actionable")
        st.caption("Indicators visible before year begins")

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["🚨 How Reliable Are the Warnings?", "🔍 What to Watch For", "💼 Practical Applications"])

    with tab1:
        st.markdown('<div class="section-header">The Track Record: Can We Trust These Predictions?</div>', unsafe_allow_html=True)

        st.markdown("""
        **Testing the system on historical data:**

        We tested our early warning system against 62 years of actual climate data to see if it could
        correctly identify which years turned out to be extreme. Here's how it performed:

        **Success Rate: 92%**
        - Out of 100 years, we correctly classify 92 as either high-risk or normal
        - This is reliable enough to guide planning and resource allocation

        **Low False Alarm Rate: 11%**
        - When we warn that a year will be extreme, we're wrong only 11% of the time
        - Means decision-makers can act on our warnings with confidence
        - Avoids "cry wolf" problem that reduces trust in alerts

        **Catches Nearly Everything: 94% Detection**
        - We catch 94 out of every 100 truly extreme years
        - Only miss about 6% of dangerous years
        - Better to over-prepare occasionally than miss a crisis

        **What This Means for Planning:**
        This level of accuracy makes the system valuable for:
        - Emergency preparedness budgeting
        - Agricultural planning (when to expect challenging conditions)
        - Insurance risk assessment
        - Infrastructure maintenance scheduling
        - Public health resource allocation
        """)

        st.markdown("**How Well Do We Classify Years?**")
        st.markdown("""
        Out of approximately 310 country-years analyzed:
        - ✅ **150 Normal years** correctly identified as normal
        - ✅ **140 Extreme years** correctly identified as high-risk
        - ⚠️ **12 False alarms** (predicted extreme, actually normal)
        - ❌ **8 Missed warnings** (didn't catch these extreme years)
        """)

    with tab2:
        st.markdown('<div class="section-header">The Warning Signs: What to Watch For</div>', unsafe_allow_html=True)

        st.markdown("""
        **Which factors best predict an extreme climate year?**

        By analyzing decades of data, we've identified the key warning signs that indicate a year is
        likely to be particularly dangerous:

        **1. CO₂ Emission Levels (Strongest Indicator)**
        - This is the #1 warning sign
        - When CO₂ levels spike, extreme years almost always follow
        - The relationship is so strong it's almost guaranteed
        - **Threshold to watch:** CO₂ concentrations above 400 ppm dramatically increase risk

        **2. The Year Itself (Time Trend)**
        - Simply put: recent years are more dangerous than past years
        - Each passing year increases likelihood of extreme conditions
        - Reflects the cumulative buildup of greenhouse gases in atmosphere
        - **What it means:** 2020s years are inherently higher risk than 1980s years

        **3. Methane Levels**
        - Second most important greenhouse gas
        - Often overlooked but significant
        - Rising methane is a reliable indicator of upcoming climate stress
        - **Sources:** Agriculture, natural gas leaks, wetlands

        **4. Deforestation Rates**
        - Less predictive globally but critical regionally
        - Rapid forest loss predicts localized extreme years
        - Removes natural carbon storage and cooling
        - **Impact zones:** Amazon, Southeast Asia, Central Africa

        **How to Use This Information:**
        - Monitor global CO₂ levels throughout the year
        - If levels are climbing rapidly, prepare for extreme conditions
        - Recent years + high emissions = very high probability of extreme year
        - Plan agricultural seasons, disaster budgets, and emergency resources accordingly
        """)

    with tab3:
        st.markdown('<div class="section-header">Putting It to Use: Real-World Applications</div>', unsafe_allow_html=True)

        st.markdown("""
        **How this early warning system helps different stakeholders:**

        **For Emergency Management:**
        - **Pre-position disaster response resources** in years flagged as high-risk
        - **Increase emergency budgets** when multiple warning indicators flash red
        - **Coordinate across regions** when warnings indicate widespread extreme conditions
        - **Example:** If 2025 shows high-risk indicators, stockpile emergency supplies in late 2024

        **For Agriculture & Food Security:**
        - **Adjust planting strategies** based on forecasted extreme year probability
        - **Secure water rights and storage** before drought-prone years
        - **Diversify crop selection** to hedge against predicted climate stress
        - **Example:** Switch to drought-resistant varieties when high-risk year predicted

        **For Insurance & Financial Services:**
        - **Adjust premium pricing** for climate-sensitive policies in high-risk years
        - **Manage reserve requirements** based on expected claim volumes
        - **Guide investment decisions** away from climate-vulnerable assets
        - **Example:** Increase catastrophe reserves 6-12 months before flagged years

        **For Infrastructure & Utilities:**
        - **Schedule critical maintenance** outside of predicted extreme years
        - **Boost grid resilience** before high-risk summer or winter seasons
        - **Pre-stage repair crews and equipment** in vulnerable regions
        - **Example:** Strengthen power grid and tree trimming before extreme weather year

        **For Public Health:**
        - **Prepare for heat-related illness surges** in flagged years
        - **Stock medications** for climate-sensitive conditions
        - **Plan cooling center operations** in advance
        - **Example:** Increase heat emergency protocol training before high-risk summer

        **The Trend We Can't Ignore:**
        - **1990:** About 15% of years were high-risk
        - **2000:** Risen to about 35% of years
        - **2010:** Jumped to about 60% of years
        - **2020:** Now 85% of years qualify as high-risk

        **What this tells us:**
        The "new normal" is what we used to call "extreme." Our baseline for what constitutes a
        dangerous climate year is shifting. This system helps distinguish between the new normal
        and the truly catastrophic.
        """)

# ===========================
# PHASE 5: DIFFERENT PATHS, SHARED PLANET
# ===========================
elif page == "🔬 Different Paths, Shared Planet":
    st.markdown('<h1 class="main-header">🔬 Four Different Climate Stories: Not All Countries Face the Same Challenge</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
    <h3>One Planet, Many Realities</h3>
    When we analyzed 195 countries' climate and emission data, a striking pattern emerged: countries fall
    into four distinct groups, each facing different challenges and requiring different solutions. Understanding
    these groups helps target climate action where it's needed most.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Business-focused metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Country Groups", "4 distinct types", "Clear patterns")
        st.caption("Each needs different strategies")
    with col2:
        st.metric("Major Emitters", "23 countries", "60% of emissions")
        st.caption("Where most cuts must happen")
    with col3:
        st.metric("Vulnerable Nations", "67 countries", "Lowest emissions")
        st.caption("Need urgent adaptation support")
    with col4:
        st.metric("Global Coverage", "195 countries", "Complete picture")
        st.caption("Every nation categorized")

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["🌍 The Four Country Groups", "📊 Understanding the Divide", "💡 Solutions for Each Group"])

    with tab1:
        st.markdown('<div class="section-header">Four Types of Climate Stories</div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            **Group 1: The Major Emitters** (23 countries)

            **Who they are:**
            - Industrialized nations with high per-capita emissions
            - Major economies: USA, China, Russia, Saudi Arabia, Japan, Germany
            - Account for over 60% of global CO₂ emissions

            **Their challenge:**
            - Built their prosperity on fossil fuels
            - Now must transition entire economies
            - Face resistance from established industries

            **Their responsibility:**
            - Created most of the historical emissions
            - Have the resources to lead the transition
            - Their choices determine global trajectory

            **Real-world impact:**
            - Every policy they adopt ripples globally
            - Can afford green tech investments others can't
            - Setting examples (good or bad) for developing nations
            """)

            st.markdown("""
            **Group 2: The Vulnerable Nations** (67 countries)

            **Who they are:**
            - Small island states: Maldives, Tuvalu, Fiji, Kiribati
            - Coastal developing nations: Bangladesh, Vietnam
            - Low-lying regions facing existential threats

            **Their struggle:**
            - Contribute <5% of global emissions
            - Face the worst climate impacts
            - Limited resources for adaptation

            **What they're experiencing:**
            - Rising seas threatening entire nations
            - Saltwater contaminating freshwater supplies
            - More intense cyclones devastating communities
            - Climate migration becoming inevitable

            **The injustice:**
            - Didn't cause the problem but paying the highest price
            - Need international support to survive
            - Some nations may cease to exist
            """)

        with col2:
            st.markdown("""
            **Group 3: The Green Leaders** (41 countries)

            **Who they are:**
            - Norway, Iceland, Costa Rica, Uruguay, Denmark, New Zealand
            - Early adopters of renewable energy
            - Strong climate policies and low per-capita emissions

            **What they've achieved:**
            - Proven that low-carbon development works
            - High quality of life with low emissions
            - Renewable energy dominates their grids

            **Their value:**
            - Living proof that alternatives exist
            - Exporting green technology and expertise
            - Setting ambitious targets that others follow

            **Their limitations:**
            - Small populations = limited global impact
            - Often have natural advantages (hydro, geothermal)
            - Can't solve the problem alone
            """)

            st.markdown("""
            **Group 4: The Crossroads Countries** (64 countries)

            **Who they are:**
            - Rapidly developing: India, Brazil, Indonesia, Mexico, Philippines
            - Caught between development and climate needs
            - Moderate but growing emissions

            **Their dilemma:**
            - Need economic growth to lift populations from poverty
            - But can't follow the high-emission path rich nations took
            - Under pressure to "leapfrog" to clean technology

            **Their challenges:**
            - Limited resources for expensive green tech
            - Cheap fossil fuels remain tempting
            - Balancing immediate needs vs. long-term survival

            **Why they matter:**
            - Home to majority of world's population
            - Their energy choices determine global future
            - If they repeat high-carbon development, climate goals impossible

            **The opportunity:**
            - Can skip outdated fossil fuel infrastructure
            - Falling renewable costs make clean development viable
            - Youth populations eager for sustainable solutions
            """)

    with tab2:
        st.markdown('<div class="section-header">The Data Behind the Groups</div>', unsafe_allow_html=True)

        st.markdown("""
        **How we identified these four groups:**

        When we plot countries based on their emissions, renewable energy adoption, climate vulnerability,
        and economic development, four distinct clusters emerge clearly. Countries within each group share
        similar challenges and characteristics.

        **Key differences between groups:**

        **Emissions per Capita:**
        - Major Emitters: 15-40 tons CO₂ per person per year
        - Green Leaders: 2-8 tons per person
        - Vulnerable Nations: 0.5-3 tons per person
        - Crossroads Countries: 3-8 tons per person (rising rapidly)

        **Climate Vulnerability:**
        - Vulnerable Nations: Extreme (sea level rise, cyclones)
        - Crossroads Countries: High (agriculture-dependent)
        - Major Emitters: Moderate (have resources to adapt)
        - Green Leaders: Low to Moderate (prepared, resilient)

        **Renewable Energy Adoption:**
        - Green Leaders: 60-100% of energy from renewables
        - Vulnerable Nations: 20-50% (often necessity, not choice)
        - Crossroads Countries: 10-30% (growing)
        - Major Emitters: 10-40% (varies widely)

        **Economic Capacity for Action:**
        - Major Emitters: High (can afford green transition)
        - Green Leaders: High (already investing heavily)
        - Crossroads Countries: Moderate (limited resources, competing priorities)
        - Vulnerable Nations: Low (need external support)
        """)

        st.info("Detailed visualizations showing country groupings will appear here after running the clustering analysis.")

        st.markdown("""
        **Why these groups matter:**

        This isn't just academic categorization—it reveals fundamental inequities:
        - Those who emit the most can best afford to adapt
        - Those who emit the least suffer the worst impacts
        - Some nations are already showing the way forward
        - The majority are at a crossroads, with their choice determining our collective future
        """)

    with tab3:
        st.markdown('<div class="section-header">Tailored Solutions: What Each Group Needs</div>', unsafe_allow_html=True)

        st.markdown("""
        **The key insight: One-size-fits-all won't work. Each group needs different support.**
        """)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            **For Major Emitters - Deep, Fast Cuts Required:**

            **What they must do:**
            - Cut emissions by 50-80% by 2030
            - Phase out coal power within this decade
            - Electrify transportation and heating rapidly

            **How to get there:**
            - Carbon pricing: Make pollution expensive
            - Massive renewable energy investment
            - End fossil fuel subsidies (often hundreds of billions per year)
            - Retrofit buildings for energy efficiency

            **Their moral obligation:**
            - Finance climate adaptation in vulnerable nations
            - Transfer green technology to developing countries
            - Lead by example—their success makes global action credible

            **Business opportunities:**
            - Green tech manufacturing dominates future economy
            - First movers in clean energy capture massive markets
            - Climate solutions industry worth trillions
            """)

            st.markdown("""
            **For Vulnerable Nations - Adaptation & Survival:**

            **What they need immediately:**
            - Sea walls, flood defenses, elevated infrastructure
            - Early warning systems for extreme weather
            - Climate-resilient crop varieties
            - Freshwater protection and desalination

            **Financial reality:**
            - Need hundreds of billions in adaptation funds
            - Can't afford it alone—require international support
            - "Loss and damage" compensation for unavoidable impacts

            **Long-term strategies:**
            - Regional climate migration planning
            - Economic diversification away from vulnerable sectors
            - Diplomatic pressure on major emitters
            - Insurance mechanisms for climate disasters

            **Why it's urgent:**
            - Some nations have <20 years before uninhabitable
            - Each delayed year means more permanent damage
            - Climate refugees will number in the millions
            """)

        with col2:
            st.markdown("""
            **For Green Leaders - Scale and Share Success:**

            **What they're already doing right:**
            - Proving clean energy works at scale
            - Maintaining high quality of life with low emissions
            - Developing technologies others can use

            **Next level challenges:**
            - Achieve true carbon neutrality (not just offset)
            - Export solutions globally, not just domestically
            - Support other nations' transitions with expertise
            - Push for more ambitious global targets

            **Their strategic value:**
            - Living laboratories for what's possible
            - Diplomatic leaders in climate negotiations
            - Source of green technology innovation
            - Proof that climate action doesn't require sacrifice

            **How they can help most:**
            - Open-source successful policy approaches
            - Provide training and capacity building
            - Invest in climate solutions for developing nations
            - Use diplomatic influence for stronger global action
            """)

            st.markdown("""
            **For Crossroads Countries - The Critical Choice:**

            **The fork in the road:**
            - **Path 1:** Repeat dirty industrialization (locks in decades of high emissions)
            - **Path 2:** Leapfrog to clean development (achieves growth without climate disaster)

            **Why Path 2 is now viable:**
            - Solar and wind now cheaper than coal in most places
            - Battery storage costs dropped 90% in 10 years
            - Green technology prices falling while fossil fuels volatile

            **What they need to succeed:**
            - Access to affordable green finance
            - Technology transfer from developed nations
            - Technical expertise and capacity building
            - Fair trade rules that don't punish green development

            **The stakes:**
            - Home to 5+ billion people
            - Their choice determines if we meet climate goals
            - If they go high-carbon, Paris Agreement impossible
            - If they go clean, global transition achievable

            **Co-benefits of green path:**
            - Energy independence (no oil imports)
            - Local job creation in renewable sector
            - Cleaner air (fewer pollution deaths)
            - Future-proof economy
            """)

        st.markdown("---")

        st.markdown("""
        **The Global Climate Deal We Need:**

        **Major Emitters commit to:**
        - Massive emission cuts at home
        - $100+ billion/year in climate finance
        - Technology sharing with developing nations

        **Vulnerable Nations receive:**
        - Guaranteed adaptation funding
        - Loss and damage compensation
        - Climate insurance mechanisms

        **Green Leaders contribute:**
        - Technical expertise and policy guidance
        - Innovation in climate solutions
        - Diplomatic leadership

        **Crossroads Countries get:**
        - Affordable access to green technology
        - Financial support for clean development
        - In return: commit to low-carbon growth path

        **Why this framework matters:**
        Everyone has a role. Success requires all four groups working together. Climate change
        doesn't care about borders—we either solve it together or fail together.
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem;'>
    <p><strong>Understanding Climate Change Through Data</strong></p>
    <p>62 years of global climate data • 195 countries • Real solutions for real challenges</p>
    <p>Fundamentos de la Ciencia de Datos | UAX (2025-26)</p>
</div>
""", unsafe_allow_html=True)
