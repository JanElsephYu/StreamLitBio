import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Jan Elseph Yu | Professional Portfolio",
    page_icon="🎓",
    layout="wide",
)

# 2. Advanced CSS for "Glassmorphism" Cards & Animations
st.markdown("""
<style>
    /* Global Styles */
    .main {
        background-color: #f5f5f5;
    }
    
    /* Custom Card Style */
    .st-emotion-cache-1r6slb0, .css-1r6slb0 {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    /* Hover Effect for Cards */
    div[data-testid="stMetric"], div[data-testid="stExpander"] {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 15px;
        transition: all 0.3s ease;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    
    div[data-testid="stMetric"]:hover, div[data-testid="stExpander"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border-color: #800000; /* CIT-U Maroon Accent */
    }

    /* Button Styling */
    .stButton>button {
        border-radius: 25px;
        background: linear-gradient(45deg, #800000, #ffcc00); /* Maroon & Gold */
        color: white;
        border: none;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(128, 0, 0, 0.4);
        color: white;
    }
    
    /* Header Typography */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Profile
with st.sidebar:
    # Ensure profile.JPG is uploaded to GitHub with capital JPG
    st.image("profile.JPG", caption="Jan Elseph Yu | BSIT-4")
    st.title("Connect")
    st.write("📧 janelsephyu@gmail.com")
    st.write("📍 Cebu City, Philippines")
    st.write("🏫 CIT-University")
    st.divider()
    st.caption("© 2026 Academic Portfolio")

# 4. Hero Section
col_hero_text, col_hero_img = st.columns([2, 1])
with col_hero_text:
    st.title("Jan Elseph Yu")
    st.subheader("Aspiring IT Professional & Systems Developer")
    st.write("""
    **"Innovating one line of code at a time."**
    
    I am a 4th-year BSIT student focused on mobile development, systems administration, 
    and gamified e-learning solutions.
    """)
    st.write("---")

# 5. Main Navigation Tabs
tab1, tab2, tab3 = st.tabs(["👤 Personal Profile", "🚀 Featured Projects", "🎨 Skills & Hobbies"])

# --- TAB 1: PERSONAL PROFILE ---
with tab1:
    st.header("My Biography")
    
    # Using columns to organize data neatly
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("📌 **Personal Details**")
        st.write(f"**Full Name:** Jan Elseph Yu")
        st.write(f"**Birthday:** January 11, 2001") # Restored
        st.write(f"**Age:** 25 Years Old") # Restored
        st.write(f"**Address:** Cebu City, Philippines")
    
    with col2:
        st.success("🎓 **Education**")
        st.write("**Course:** Bachelor of Science in Information Technology")
        st.write("**Year Level:** 4th Year (Senior)")
        st.write("**University:** Cebu Institute of Technology - University")
        st.write("**Status:** Regular Student / OJT Intern")

    st.write("### About Me")
    st.write("""
    My journey in technology started with a love for storytelling in the 3rd grade. 
    That creativity evolved into a passion for building digital worlds. Today, I specialize 
    in creating systems that help people—whether it's navigating a grocery store or 
    managing scholarship applications.
    """)

# --- TAB 2: FEATURED PROJECTS (Restored GIPS, SEMS, NASMS) ---
with tab2:
    st.header("Project Portfolio")
    st.caption("Hover over the cards below to see details.")

    col_proj1, col_proj2 = st.columns(2)
    
    with col_proj1:
        with st.expander("⭐ GIPS (Grocery Indoor Positioning System)", expanded=True):
            st.write("**Platform:** Android Application")
            st.write("""
            An indoor navigation tool designed to help users locate items in a grocery store.
            - 🗺️ **Indoor Mapping:** Locates specific aisles and shelves.
            - 🛒 **Smart Cart:** Manages shopping lists and availability.
            """)
            
        with st.expander("🎓 SEMS (Scholarship & Enrollment Management System)", expanded=True):
            st.write("**Platform:** Web & Mobile System")
            st.write("""
            A comprehensive system for managing student scholarships and enrollment data.
            - 📂 **Data Management:** Handles student records and scholarship requirements.
            - 📊 **Reporting:** Generates automated reports for the OAS.
            """)

    with col_proj2:
        with st.expander("📱 NASMS (Non-Academic Scholar Management System)", expanded=True):
            st.write("**Platform:** Mobile Application (CIT-U)")
            st.write("""
            The mobile counterpart for managing non-academic scholars.
            - 📄 **PDF Conversion:** In-app document processing.
            - ☁️ **Cloud Upload:** Direct upload for Grades and School IDs.
            """)
            
        with st.expander("⌨️ SyntaxType (Capstone Project)", expanded=True):
            st.write("**Platform:** Web Application")
            st.write("""
            A gamified typing e-learning platform built for BSIT freshmen.
            - 🎮 **Gamification:** Makes learning syntax fun and interactive.
            - 📈 **Analytics:** Tracks typing speed and accuracy improvements.
            """)

# --- TAB 3: SKILLS & HOBBIES ---
with tab3:
    c1, c2 = st.columns(2)
    
    with c1:
        st.subheader("My Hobbies")
        st.markdown("""
        * 🎨 **Drawing:** Digital art and sketching.
        * ✍️ **Writing Stories:** Creative writing and lore building.
        * 🎮 **Gaming:** Strategy and RPGs.
        """)
    
    with c2:
        st.subheader("Technical Skills")
        st.write("Android Development (Java/Kotlin)")
        st.progress(85)
        st.write("Web Development (React/Python)")
        st.progress(75)
        st.write("Systems Administration")
        st.progress(70)

# 6. Interactive Footer
st.divider()
st.write("### Interactive Feedback")

# Using columns to center the button
b1, b2, b3 = st.columns([1, 2, 1])
with b2:
    if st.button("Click to Celebrate My Work! 🚀", use_container_width=True):
        st.balloons()
        st.snow()
        time.sleep(1)
        st.toast("Thank you for visiting my portfolio!", icon="🎉")

st.markdown("<center>Developed by Jan Elseph Yu | CIT-U Output</center>", unsafe_allow_html=True)