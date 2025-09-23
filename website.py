import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

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
    .stat-box {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem;
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

# Create tabs
tab1, tab2, tab3 = st.tabs(["📊 Introduction", "👥 Team", "📋 Proposal Overview"])

with tab1:
    st.markdown('<h2 class="sub-header">Research Topic & Significance</h2>', unsafe_allow_html=True)
    
    st.write("""
    Urban crime represents one of the most pressing challenges facing modern cities, directly impacting public safety, economic development, and community well-being. This research focuses on analyzing comprehensive crime data from San Francisco to develop predictive models and identify actionable patterns that can enhance public safety strategies. The significance of this study lies in its potential to transform reactive policing into proactive, data-driven law enforcement that can prevent crimes before they occur. 
    
    By leveraging machine learning algorithms and advanced statistical analysis on over 500,000 crime incidents, this research aims to uncover temporal, spatial, and categorical patterns that have remained hidden in traditional crime analysis approaches. The importance of this work extends beyond academic interest—it directly addresses the critical need for evidence-based public safety policies that can save lives, reduce victimization, and optimize the allocation of limited municipal resources. 
    
    Who benefits from this research includes police departments seeking efficient resource deployment, city planners designing safer communities, businesses making location decisions, and ultimately, every citizen whose safety and quality of life depends on effective crime prevention strategies.
    """)
    
    st.markdown('<h2 class="sub-header">Stakeholders (Who is Affected?)</h2>', unsafe_allow_html=True)
    
    st.write("""
    The primary stakeholders impacted by this research span multiple sectors of urban society. Law enforcement agencies, particularly the San Francisco Police Department, represent the most direct beneficiaries, as predictive crime models can revolutionize patrol deployment strategies, shift scheduling, and tactical resource allocation. City government officials and urban planners will gain critical insights for policy development, budget allocation decisions, and infrastructure planning that considers public safety implications. 
    
    Local businesses and commercial districts are significantly affected, as crime patterns directly influence foot traffic, property values, insurance costs, and overall economic vitality. Residents and community organizations benefit from enhanced safety awareness, enabling informed decisions about housing, transportation, and daily activities. Tourism boards and hospitality industries have substantial stakes in crime reduction, as public safety perceptions directly impact San Francisco's reputation and visitor economy. 
    
    Insurance companies and real estate developers require accurate crime risk assessments for pricing and investment decisions. The real-world implications extend to emergency services, public health organizations, and social service agencies who must respond to crime's broader societal impacts. This research addresses the fundamental challenge of making cities safer while optimizing the use of public resources in an era of budget constraints and increasing urbanization.
    """)
    
    st.markdown('<h2 class="sub-header">Existing Solutions & Gaps</h2>', unsafe_allow_html=True)
    
    st.write("""
    Current crime analysis solutions primarily rely on retrospective statistical reports and basic geographic information systems that identify where crimes have already occurred. Traditional approaches include CompStat systems used by many police departments, which provide historical crime mapping and basic trend analysis, and hot spot policing strategies that deploy officers to areas with historically high crime rates. 
    
    However, these existing solutions face significant limitations and challenges that this research addresses. Most current systems lack predictive capabilities, operating reactively rather than proactively to prevent crimes. Limited temporal analysis represents another gap, as existing tools often fail to capture complex time-based patterns including seasonal variations, day-of-week effects, and hour-specific trends that could inform strategic planning. 
    
    Inadequate integration of multiple data sources prevents comprehensive analysis that could combine crime data with socioeconomic factors, weather patterns, and special events. Insufficient granularity in crime categorization limits the effectiveness of targeted interventions, as broad crime categories may obscure specific patterns that require different prevention strategies. Current solutions also struggle with scalability and real-time processing of large datasets, limiting their utility for dynamic resource allocation decisions. The challenge of translating analytical insights into actionable operational strategies remains largely unsolved in existing systems.
    """)
    
    st.markdown('<h2 class="sub-header">Blueprint for Your Project</h2>', unsafe_allow_html=True)
    
    st.write("""
    This comprehensive data science project will employ a multi-phase analytical approach to transform raw crime data into actionable intelligence for public safety optimization. The project team will explore temporal pattern analysis using time series decomposition and seasonal trend analysis to identify when different types of crimes are most likely to occur, enabling predictive patrol scheduling and resource allocation. 
    
    Spatial analysis techniques including geographic clustering algorithms, hotspot mapping, and geospatial correlation analysis will reveal crime concentration patterns and their relationship to urban infrastructure, demographic factors, and economic indicators. Machine learning classification models will be developed to predict crime types based on temporal, spatial, and contextual features, with particular focus on distinguishing between violent and property crimes to support risk-based policing strategies. 
    
    Predictive modeling approaches will include ensemble methods such as Random Forest and Gradient Boosting, as well as deep learning techniques for complex pattern recognition in high-dimensional crime data. The team will also implement clustering analysis to identify distinct crime patterns and criminal behavior profiles that may not be apparent through traditional analysis methods. 
    
    Feature engineering will create new variables combining temporal, geographical, and categorical data to enhance model performance and interpretability. The project will consider multiple datasets including the primary San Francisco Crime dataset (500K+ records), supplemented by weather data, economic indicators, and demographic information to create a comprehensive analytical framework. 
    
    Evaluation metrics will focus on both statistical accuracy and practical utility, ensuring that models not only perform well mathematically but also provide actionable insights for real-world implementation. The final deliverable will include interactive dashboards, predictive models, and strategic recommendations that can be directly implemented by law enforcement and city planning agencies.
    """)

with tab2:
    st.markdown('<h2 class="sub-header">👥 Meet Our Team</h2>', unsafe_allow_html=True)
    
    # Team Mission Statement
    st.info("🎯 **Team Mission Statement**\n\n*To leverage cutting-edge data science and machine learning techniques to transform public safety in San Francisco, creating predictive solutions that protect communities while optimizing resource allocation for maximum societal impact.*")
    
    st.markdown("---")
    
    # Team member 1
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image("formal.jpg", width=500)
    
    with col2:
        st.subheader("Siddhi Muni- Data Lead")
        st.write("**Brief Bio:** I'm a builder and a problem-solver, with a particular fascination for generative AI. My passion lies in taking a challenge and deconstructing it, then using AI to build a solution from the ground up. Whether it's developing a new algorithm to streamline a workflow or creating a model that can generate unique content, I am dedicated to crafting robust and effective tools. My goal is to not only solve the problem at hand but also to create scalable, intelligent systems that can adapt to future needs.")
    
        st.write("**Team Role/Responsibilities:**")
        st.write("• Data preprocessing and feature engineering")
        st.write("• Leading machine learning model development and validation")
       
        st.write("**Portfolio Links:**")
        st.write("📧 siddhimuni1302@gmail.com | 💼 [LinkedIn](www.linkedin.com/in/siddhimuni) | 🐙 [GitHub](https://github.com/siddhimuni) | 🌐 [Google Scholar](https://scholar.google.com/citations?user=pSDJxbQAAAAJ&hl=en)")
    
    st.markdown("---")
    
    # Team member 2
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown('<div class="team-card">', unsafe_allow_html=True)
        st.image("portfolio.jpg", caption="Sejal Hukare")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.subheader("Sejal Hukare - Pipeline and ML ")
        st.write("**Brief Bio:** I’m a passionate coding and tech enthusiast, always eager to dive into new challenges and explore the ever-evolving world of technology. My curiosity drives me to continuously learn and grow, while my love for connecting with people fuels my ability to collaborate and innovate. Whether it’s solving complex problems or exchanging ideas, I thrive in environments where creativity and learning intersect.")
        st.write("**Team Role/Responsibilities:**")
        st.write("• Machine learning model architecture and optimization")
        st.write("• Data pipeline development and deployment")
        st.write("**Portfolio Links:**")
        st.write("📧 sejal.hukare@colorado.edu | 💼 [LinkedIn](www.linkedin.com/in/sejal-hukare) | 🐙 [GitHub](https://github.com/sezol) ")
    
    st.markdown("---")
    
    # Team member 3
    col1, col2 = st.columns([1, 3])

with col1:
    st.markdown('<div class="team-card">', unsafe_allow_html=True)
    st.image("profile (2).jpg", caption="Mokshith")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("Mokshith - Data & Feature Engineer")
    st.write("**Brief Bio:** I’m passionate about uncovering hidden patterns in data and turning raw information into actionable insights. I enjoy getting hands-on with datasets—cleaning, preprocessing, and engineering features—to help predictive models perform at their best. Beyond the numbers, I love experimenting with creative solutions and seeing how data can make real-world decisions smarter and more efficient.")
    st.write("**Team Role/Responsibilities:**")
    st.write("• Data preprocessing and feature engineering")
    st.write("• Supporting machine learning model development")
    st.write("**Portfolio Links:**")
    st.write("📧 mokshit.Palleboina@colorado.edu | 💼 [LinkedIn](www.linkedin.com/in/mokshith-sreekar-915bb6249) | 🐙 [GitHub](https://github.com/mokshith9500) | 🌐 [IEEE Explore](https://ieeexplore.ieee.org/author/220685108923536)")

    
    st.markdown("---")

with tab3:
    st.markdown('<h2 class="sub-header">📋 Quick Reference Summary</h2>', unsafe_allow_html=True)
    
    # Research Topic
    st.markdown("""
    <div class="highlight-box">
        <h3>🔬 Research Topic</h3>
        <p><strong>Predicting Crime Patterns and Optimizing Public Safety Resource Allocation in San Francisco</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Scope
    st.markdown('<h3 class="sub-header">📊 Project Scope</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Dataset & Coverage:**
        • **Dataset:** San Francisco Crime Data  
        • **Volume:** 500,000+ incident records  
        • **Time Period:** Multi-year historical analysis  
        • **Geographic Focus:** All SF neighborhoods and police districts  
        """)
    
    with col2:
        st.markdown("""
        **Analysis Approach:**  
        • **Crime Categories:** Violent, property, quality-of-life violations  
        • **Methods:** Machine learning, statistical modeling  
        • **Techniques:** Geospatial analysis, predictive modeling  
        • **Output:** Interactive dashboards and recommendations  
        """)
    
    # Mock Data Generation
    # In a real project, you would load your data here
    np.random.seed(0)
    dates = pd.to_datetime(pd.date_range('2021-01-01', '2024-12-31', freq='D'))
    data_points = len(dates)
    
    crime_categories = ['Vehicle Theft', 'Robbery', 'Burglary', 'Assault', 'Vandalism']
    districts = ['Central', 'Southern', 'Northern', 'Bayview', 'Mission', 'Richmond', 'Ingleside', 'Park', 'Taraval', 'Tenderloin']
    
    df = pd.DataFrame({
        'Date': np.random.choice(dates, data_points * 5, replace=True),
        'Category': np.random.choice(crime_categories, data_points * 5, replace=True),
        'District': np.random.choice(districts, data_points * 5, replace=True),
        'Incidents': np.random.randint(1, 10, data_points * 5)
    })
    
    # Dynamic Filtering Sidebar
    st.markdown("### Interactive Crime Dashboard (Mock Data)")
    
    st.markdown('<div class="text-block">Use the sliders and filters below to explore how crime trends change over time, by category, and by district. This interactive dashboard demonstrates how we will present our project\'s findings.</div>', unsafe_allow_html=True)

    col_filters1, col_filters2 = st.columns(2)
    
    with col_filters1:
        selected_years = st.slider(
            "Select Year Range:",
            min_value=2021, max_value=2024, value=(2022, 2024)
        )
        selected_categories = st.multiselect(
            "Select Crime Categories:",
            options=crime_categories,
            default=crime_categories
        )

    with col_filters2:
        selected_districts = st.multiselect(
            "Select Districts:",
            options=districts,
            default=districts
        )
        
    filtered_df = df[
        (df['Date'].dt.year >= selected_years[0]) &
        (df['Date'].dt.year <= selected_years[1]) &
        (df['Category'].isin(selected_categories)) &
        (df['District'].isin(selected_districts))
    ]
    
    # Display statistics
    st.markdown('<h3 class="sub-header">Key Statistics</h3>', unsafe_allow_html=True)
    col_stats1, col_stats2, col_stats3 = st.columns(3)
    
    with col_stats1:
        st.metric(label="Total Incidents (in range)", value=f"{filtered_df['Incidents'].sum():,}")
    with col_stats2:
        st.metric(label="Average Daily Incidents", value=f"{filtered_df['Incidents'].sum() / (filtered_df['Date'].nunique()):.2f}")
    with col_stats3:
        st.metric(label="Most Common Crime", value=filtered_df['Category'].mode()[0] if not filtered_df.empty else "N/A")
    
    # Crime Trends Over Time
    st.markdown('<h3 class="sub-header">Crime Trends Over Time</h3>', unsafe_allow_html=True)
    trend_data = filtered_df.groupby(filtered_df['Date'].dt.to_period('M'))['Incidents'].sum().reset_index()
    trend_data['Date'] = trend_data['Date'].astype(str)
    
    fig_time = px.line(
        trend_data,
        x='Date',
        y='Incidents',
        title='Monthly Crime Incidents Trend'
    )
    st.plotly_chart(fig_time, use_container_width=True)
    
    # Crime Distribution by District
    st.markdown('<h3 class="sub-header">Crime Distribution by District</h3>', unsafe_allow_html=True)
    district_data = filtered_df.groupby('District')['Incidents'].sum().reset_index()
    
    fig_district = px.bar(
        district_data,
        x='District',
        y='Incidents',
        title='Total Incidents by District'
    )
    st.plotly_chart(fig_district, use_container_width=True)

    # Sample visualization of crime types
    st.markdown('<h3 class="sub-header">❓ Key Research Questions</h3>', unsafe_allow_html=True)
    
    questions = [
        "🕐 **Temporal Analysis:** When do specific crime types peak? (time of day, season, day of week)",
        "📍 **Spatial Analysis:** Where are crime hotspots located and why?",
        "🔮 **Predictive Modeling:** Can we predict crime type and likelihood by location/time?",
        "🚔 **Resource Optimization:** How should police allocate patrol resources?",
        "🏘️ **Comparative Analysis:** How do different neighborhoods compare in crime patterns?",
        "🔗 **Causal Relationships:** What factors drive crime rate fluctuations?"
    ]
    
    for i, question in enumerate(questions, 1):
        st.markdown(f"{i}. {question}")
    
# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🔒 <strong>Data Science for Public Safety</strong> | Transforming Crime Analysis Through Machine Learning</p>
    <p>San Francisco Crime Prediction Project • 2024</p>
</div>
""", unsafe_allow_html=True)
