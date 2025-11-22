import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import os

# Page configuration
st.set_page_config(
    page_title="SF Crime Analysis Project",
    page_icon="🚔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .highlight-box {
        background-color: #f8f9fa;
        color:black;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .team-card {
        background-color: #f5f5f5;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">🚔 Predicting Crime Patterns in San Francisco</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Optimizing Public Safety Resource Allocation Through Data Science</p>', unsafe_allow_html=True)

# Tabs (shorter labels so they fit better)
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Intro",
    "👥 Team",
    "📋 Proposal",
    "🔍 Phase 2 EDA",
    "🧠 Models"
])

# =========================
# TAB 1 – INTRODUCTION
# =========================
with tab1:
    st.markdown('<h2 class="sub-header">Research Topic & Significance</h2>', unsafe_allow_html=True)
    st.write("""
    Urban crime represents one of the most pressing challenges facing modern cities. This project analyzes 
    San Francisco crime data to build predictive models and uncover patterns that can support proactive, 
    data-driven public safety decision-making.
    """)

    st.markdown('<h2 class="sub-header">Stakeholders</h2>', unsafe_allow_html=True)
    st.write("""
    Key stakeholders include the San Francisco Police Department, city planners, local businesses, residents, 
    and policymakers. All benefit from understanding where, when, and which types of crimes occur.
    """)

    st.markdown('<h2 class="sub-header">Existing Solutions & Gaps</h2>', unsafe_allow_html=True)
    st.write("""
    Traditional tools like CompStat mainly focus on historical mapping and basic trend analysis. They often 
    lack predictive capabilities, struggle to integrate multiple data sources, and rarely provide real-time, 
    actionable guidance for resource allocation.
    """)

    st.markdown('<h2 class="sub-header">Project Blueprint</h2>', unsafe_allow_html=True)
    st.write("""
    This project uses a multi-phase pipeline:
    - **Phase 1 & 2**: Data cleaning and exploratory analysis (temporal, spatial, categorical).
    - **Phase 3**: Modeling using classification, clustering, regression, and frequent pattern mining.
    - **Final**: Interactive dashboards and a public-facing website summarizing insights for non-technical stakeholders.
    """)

# =========================
# TAB 2 – TEAM
# =========================
with tab2:
    st.markdown('<h2 class="sub-header">👥 Meet Our Team</h2>', unsafe_allow_html=True)
    st.info("🎯 **Team Mission:** Use data science and machine learning to support safer, smarter policing in San Francisco.")

    st.markdown("---")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("formal.jpg", width=500)
    with col2:
        st.subheader("Siddhi Muni – Data Lead")
        st.write("Leads data preprocessing, feature engineering, and core ML model development.")
        st.write("📧 siddhimuni1302@gmail.com | 💼 LinkedIn / GitHub / Google Scholar")

    st.markdown("---")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="team-card">', unsafe_allow_html=True)
        st.image("portfolio.jpg", caption="Sejal Hukare")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.subheader("Sejal Hukare – Pipeline & ML")
        st.write("Focuses on ML pipeline design, model optimization, and deployment.")
        st.write("📧 sejal.hukare@colorado.edu | 💼 LinkedIn / GitHub")

    st.markdown("---")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="team-card">', unsafe_allow_html=True)
        st.image("profile (2).jpg", caption="Mokshith")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.subheader("Mokshith – Data & Feature Engineer")
        st.write("Works on data cleaning, feature engineering, and supporting model experimentation.")
        st.write("📧 mokshit.Palleboina@colorado.edu | 💼 LinkedIn / GitHub / IEEE Xplore")

# =========================
# TAB 3 – PROPOSAL / OVERVIEW
# =========================
with tab3:
    st.markdown('<h2 class="sub-header">📋 Project Overview</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="highlight-box">
        <h3>🔬 Research Topic</h3>
        <p><strong>Predicting Crime Patterns and Optimizing Public Safety Resource Allocation in San Francisco</strong></p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Dataset & Coverage:**  
        • San Francisco Crime Data (historical)  
        • 500,000+ incident records  
        • Multiple years, all SF districts and neighborhoods  
        """)
    with col2:
        st.markdown("""
        **Analysis Approach:**  
        • Temporal and spatial pattern analysis  
        • Classification, clustering, regression models  
        • Frequent pattern mining for co-occurring crime types  
        """)

    # Mock data for interactive demo (does not depend on real SF dataset here)
    np.random.seed(0)
    dates = pd.to_datetime(pd.date_range('2021-01-01', '2024-12-31', freq='D'))
    data_points = len(dates)
    crime_categories = ['Vehicle Theft', 'Robbery', 'Burglary', 'Assault', 'Vandalism']
    districts = ['Central', 'Southern', 'Northern', 'Bayview', 'Mission',
                 'Richmond', 'Ingleside', 'Park', 'Taraval', 'Tenderloin']
    df = pd.DataFrame({
        'Date': np.random.choice(dates, data_points * 5, replace=True),
        'Category': np.random.choice(crime_categories, data_points * 5, replace=True),
        'District': np.random.choice(districts, data_points * 5, replace=True),
        'Incidents': np.random.randint(1, 10, data_points * 5)
    })

    st.markdown("### Interactive Crime Dashboard (Mock Data)")
    col_filters1, col_filters2 = st.columns(2)
    with col_filters1:
        selected_years = st.slider("Select Year Range:", 2021, 2024, (2022, 2024))
        selected_categories = st.multiselect("Select Crime Categories:",
                                             options=crime_categories,
                                             default=crime_categories)
    with col_filters2:
        selected_districts = st.multiselect("Select Districts:",
                                            options=districts,
                                            default=districts)

    filtered_df = df[
        (df['Date'].dt.year >= selected_years[0]) &
        (df['Date'].dt.year <= selected_years[1]) &
        (df['Category'].isin(selected_categories)) &
        (df['District'].isin(selected_districts))
    ]

    col_stats1, col_stats2, col_stats3 = st.columns(3)
    with col_stats1:
        st.metric("Total Incidents", f"{filtered_df['Incidents'].sum():,}")
    with col_stats2:
        denom = max(1, filtered_df['Date'].nunique())
        st.metric("Avg Daily Incidents", f"{filtered_df['Incidents'].sum() / denom:.2f}")
    with col_stats3:
        common = filtered_df['Category'].mode()[0] if not filtered_df.empty else "N/A"
        st.metric("Most Common Crime", common)

    trend_data = filtered_df.groupby(filtered_df['Date'].dt.to_period('M'))['Incidents'].sum().reset_index()
    trend_data['Date'] = trend_data['Date'].astype(str)
    fig_time = px.line(trend_data, x='Date', y='Incidents', title='Monthly Crime Incidents Trend')
    st.plotly_chart(fig_time, use_container_width=True)

# =========================
# TAB 4 – PHASE 2 EDA
# =========================
with tab4:
    st.markdown('<h2 class="sub-header">🔍 Phase 2 – Exploratory Data Analysis (EDA)</h2>', unsafe_allow_html=True)
    st.write("""
    Phase 2 focuses on cleaning, transforming, and exploring the SF crime dataset to understand key patterns
    before modeling.
    """)

    st.markdown('<h3 class="sub-header">🧹 Data Cleaning & Transformation</h3>', unsafe_allow_html=True)
    st.write("""
    Main preprocessing steps included:
    - Handling missing values and duplicate records  
    - Dropping irrelevant columns and encoding categorical features  
    - Outlier detection for extreme incident counts or rare categories  
    - Extracting date-time features such as year, month, weekday, and hour  
    """)

    st.markdown('<h3 class="sub-header">📊 Correlation Analysis</h3>', unsafe_allow_html=True)
    for img_name, caption in [
        ("coorelation_heatmap.png", "Correlation Heatmap (Before Cleaning)"),
        ("coorelation_heatmap_cleaned.png", "Correlation Heatmap (After Cleaning)")
    ]:
        if os.path.exists(img_name):
            st.image(img_name, caption=caption)
        else:
            st.warning(f"⚠️ {img_name} not found in directory.")

    st.write("""
    These heatmaps were used to identify redundant or highly correlated variables to avoid multicollinearity
    and simplify downstream models.
    """)

    st.markdown('<h3 class="sub-header">📈 Key Visual Insights</h3>', unsafe_allow_html=True)
    visualizations = [
        ("crime_type_distribution.png", "Crime Type Distribution",
         "Shows which crime categories dominate overall incident counts."),
        ("monthly_trend.png", "Monthly Crime Trend",
         "Reveals seasonal variations and long-term trends in crime volume."),
        ("day_of_week.png", "Crimes by Day of Week",
         "Highlights which days see more activity (e.g., mid-week vs weekends)."),
        ("hourly_pattern.png", "Hourly Crime Pattern",
         "Shows time-of-day effects, with peaks in afternoon/early evening."),
        ("neighborhood_hotspots.png", "Neighborhood Crime Hotspots",
         "Maps high-density crime areas such as Mission, Tenderloin, and SoMa."),
        ("district_comparison.png", "Incidents by District",
         "Compares total incidents across SF police districts."),
        ("wordcloud.png", "Crime Wordcloud",
         "Visual emphasizes the most frequent incident descriptions/categories.")
    ]

    for img_name, title, desc in visualizations:
        st.markdown(f"#### {title}")
        if os.path.exists(img_name):
            st.image(img_name, caption=title)
        else:
            st.warning(f"⚠️ {img_name} not found.")
        st.write(desc)
        st.markdown("---")

    st.markdown("**Summary:** Mission, Tenderloin, and SoMa emerge as persistent hotspots; larceny/theft and vehicle-related incidents dominate; and crime activity is highest in afternoon and early evening hours.")

# =========================
# TAB 5 – MODELS IMPLEMENTED
# =========================
with tab5:
    st.markdown('<h2 class="sub-header">🧠 Models Implemented</h2>', unsafe_allow_html=True)
    st.markdown("""
    This section summarizes the models used in Phase 3, grouped by requirement category:
    - Frequent Pattern Mining: **Apriori**  
    - Clustering: **K-Means**  
    - Classification: **Support Vector Machine (SVM)**  
    - Regression: **XGBoost** and **LightGBM**  
    """, unsafe_allow_html=True)

    # APRIORI
    st.markdown("### 1️⃣ Frequent Pattern Mining – Apriori")
    st.write("""
    **Why chosen:** To discover which crime types tend to co-occur within the same district and day 
    (e.g., Theft + Vehicle-related crimes).

    **Data formatting:**  
    - Created a `transaction_id` by combining police district and incident date.  
    - Grouped incidents by transaction and crime category, then pivoted to a binary matrix
      (1 = crime type occurred that day in that district, 0 = did not).  

    **Hyperparameters:**  
    - `min_support = 0.01`  
    - Generated rules using `metric="lift"` with `min_threshold = 1.2`  
    - Filtered to keep rules with `confidence ≥ 0.30` and ≤ 2 items per side.

    **Metrics:**  
    - **Support:** how often the pattern occurs.  
    - **Confidence:** how reliable the rule is.  
    - **Lift:** how much more often the pattern occurs than random chance (lift > 1 = positive association).

    **Insight:** Property crime combinations occur together more often than expected in certain districts, suggesting 
    opportunities for joint prevention strategies.
    """)

    if os.path.exists("apriori_scatter_plot.png"):
        st.image("apriori_scatter_plot.png",
                 caption="Apriori Association Rules – Confidence vs Lift")

    st.markdown("---")

    # K-MEANS
    st.markdown("### 2️⃣ Clustering – K-Means")
    st.write("""
    **Why chosen:** To segment neighborhoods or districts into groups with similar crime intensity and patterns.

    **Data formatting:**  
    - Aggregated features such as incident counts and category mix per spatial unit.  
    - Scaled all numeric features so that each contributes fairly to the distance metric.

    **Hyperparameters (conceptual):**  
    - `n_clusters = k` chosen using the elbow method (within-cluster sum of squares).  
    - `init = "k-means++"` for stable centroid initialization.

    **Insight:** Clusters roughly correspond to high-crime cores, moderate-risk mixed areas, and lower-risk residential zones,
    which helps prioritize patrol coverage and resource allocation.
    """)

    colk1, colk2 = st.columns(2)
    with colk1:
        if os.path.exists("kmeans_elbow_plot.png"):
            st.image("kmeans_elbow_plot.png", caption="K-Means Elbow Plot")
    with colk2:
        if os.path.exists("kmeans_cluster_map.png"):
            st.image("kmeans_cluster_map.png", caption="K-Means Cluster Map")

    st.markdown("---")

    # SVM
    st.markdown("### 3️⃣ Classification – Support Vector Machine (SVM)")
    st.write("""
    **Why chosen:** SVM with an RBF kernel handles high-dimensional feature spaces and can model non-linear 
    decision boundaries. We used it to classify police districts (or simplified crime categories) using
    spatial and temporal features.

    **Data preparation:**  
    - Standardized numeric features (coordinates, time features).  
    - Applied PCA to reduce dimensionality while preserving most variance.  
    - Encoded target labels and used a stratified train–test split.

    **Hyperparameters (conceptual):**  
    - `kernel = "rbf"`  
    - `C` (controls margin vs misclassification)  
    - `gamma = "scale"`  

    **Evaluation:**  
    - Accuracy and per-class precision/recall (via classification report).  
    - Performance is moderate: common districts are predicted better than rare ones, showing overlapping patterns
      between some districts.
    """)

    if os.path.exists("svm_decision_boundary.png"):
        st.image("svm_decision_boundary.png",
                 caption="SVM Decision Boundary in PCA Space (PC1 vs PC2)")

    st.markdown("---")

    # XGBOOST
    st.markdown("### 4️⃣ Regression – XGBoost (Response Time Prediction)")
    st.write("""
    **Goal:** Predict police response time (in minutes) based on spatial, temporal, and incident features.

    **Why chosen:** XGBoost is strong on tabular data, captures non-linear interactions, and includes regularization.

    **Features:**  
    - Numeric: latitude, longitude, incident hour, weekday, month  
    - Target-encoded categorical: police district, neighborhood, incident category  

    **Target engineering:**  
    - Computed response time in minutes from incident and report timestamps  
    - Filtered out invalid/negative values  
    - Capped extreme values at the 95th percentile  
    - Applied `log1p` transform to reduce skewness  

    **Best hyperparameters (RandomizedSearchCV, 3-fold):**  
    - `n_estimators = 400`, `learning_rate = 0.01`, `max_depth = 4`  
    - `subsample = 0.8`, `colsample_bytree = 0.8`, `reg_lambda = 5`  

    **Performance (original scale, capped target):**  
    - **Train:** RMSE ≈ 3432, MAE ≈ 1218, R² ≈ 0.54  
    - **Test:**  RMSE ≈ 4592, MAE ≈ 1729, R² ≈ 0.22  

    **Interpretation:** XGBoost captures some structure in response time but is limited by missing external factors 
    (traffic, staffing, concurrent calls). It is still the best-performing regression model in our pipeline.
    """)

    st.markdown("---")

    # LIGHTGBM
    st.markdown("### 5️⃣ Regression – LightGBM (Comparison Model)")
    st.write("""
    **Why chosen:** LightGBM is a fast and memory-efficient gradient boosting framework; we used it as a 
    comparison model to XGBoost on the same regression task.

    **Setup:**  
    - Same features and target as XGBoost (shared preprocessing pipeline).  

    **Best hyperparameters (RandomizedSearchCV, 3-fold):**  
    - `learning_rate = 0.03`, `n_estimators = 100`, `max_depth = 3`, `num_leaves = 31`  
    - `reg_alpha = 1.0`, `reg_lambda = 1.0`  
    - `min_child_samples = 10`, `min_split_gain = 0.1`, `subsample = 0.8`, `colsample_bytree = 1.0`  

    **Performance (original scale, capped target):**  
    - **Train:** RMSE ≈ 3627, MAE ≈ 1309, R² ≈ 0.48  
    - **Test:**  RMSE ≈ 4672, MAE ≈ 1760, R² ≈ 0.19  

    **Comparison:** XGBoost slightly outperforms LightGBM on both R² and RMSE, but both confirm that response time 
    is noisy and only partially predictable from the available features.
    """)

    st.markdown("#### 📌 Overall Model Summary")
    st.write("""
    | Category               | Model        | Main Goal                                    | Key Outcome                                  |
    |------------------------|-------------|----------------------------------------------|---------------------------------------------|
    | Frequent Pattern Mining| Apriori     | Discover co-occurring crime patterns         | Support, Confidence, Lift-based rules       |
    | Clustering             | K-Means     | Group areas by similar crime behavior        | Hotspot vs moderate vs low-risk clusters    |
    | Classification         | SVM (+ PCA) | Classify districts / crime types             | Moderate accuracy, overlapping patterns     |
    | Regression             | XGBoost     | Predict police response time                 | Best Test R² ≈ 0.22                         |
    | Regression             | LightGBM    | Validate and compare regression performance  | Test R² ≈ 0.19                              |

    Together, these models give a multi-faceted view of SF crime:
    - **Apriori** uncovers crime co-occurrence structures.  
    - **K-Means** reveals spatial risk clusters.  
    - **SVM** explores how separable crime patterns are across districts.  
    - **XGBoost** and **LightGBM** attempt to forecast response time and highlight the limits of prediction with 
      the current data.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🔒 <strong>Data Science for Public Safety</strong> | Transforming Crime Analysis Through Machine Learning</p>
    <p>San Francisco Crime Prediction Project • 2024</p>
</div>
""", unsafe_allow_html=True)
