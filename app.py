import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(
    page_title="Jan Elseph Yu | Professional Portfolio",
    page_icon="🎓",
    layout="wide",
)

# 2. Minimalist CSS (Enhancements only, no color forcing)
st.markdown("""
<style>
    /* This CSS adds a nice gradient to your buttons but leaves the 
       backgrounds alone so they adapt to Light/Dark mode automatically.
    */
    
    /* Global Font Adjustment */
    html, body, [class*="css"] {
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* CIT-U Maroon & Gold Gradient Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #800000, #ffcc00);
        color: white !important; /* Force white text on the colored button */
        border: none;
        border-radius: 20px;
        font-weight: bold;
        transition: transform 0.2s;
    }
    
    /* Button Hover Effect */
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    
    /* Wattpad Link specific styling */
    a[href*="wattpad.com"] {
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Profile
with st.sidebar:
    # Ensure profile.JPG is uploaded to GitHub
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
    
    # Use st.container with border=True for the "Card" look that supports Dark Mode
    with st.container(border=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("📌 **Personal Details**")
            st.write("**Full Name:** Jan Elseph Yu")
            st.write("**Birthday:** January 11, 2001") 
            st.write("**Age:** 25 Years Old") 
            st.write("**Address:** Cebu City, Philippines")
        
        with col2:
            st.success("🎓 **Education**")
            st.write("**Course:** BS Information Technology")
            st.write("**Year Level:** 4th Year (Senior)")
            st.write("**University:** CIT-University")
            st.write("**Status:** Regular Student / OJT Intern")

    st.write("### About Me")
    st.write("""
    My journey in technology started with a love for storytelling in the 3rd grade. 
    That creativity evolved into a passion for building digital worlds. Today, I specialize 
    in creating systems that help people—whether it's navigating a grocery store or 
    managing scholarship applications.
    """)

# --- TAB 2: FEATURED PROJECTS ---
with tab2:
    st.header("Project Portfolio")
    st.caption("Hover over the cards below to see details.")

    col_proj1, col_proj2 = st.columns(2)
    
    with col_proj1:
        # Using expanded=True makes them look like cards immediately
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

# --- TAB 3: SKILLS & HOBBIES (Updated) ---
with tab3:
    st.header("Beyond the Code")
    
    # 1. CREATIVE WRITING SECTION
    st.subheader("✍️ Creative Writing")
    st.write("I have been writing stories since the 3rd grade. My latest featured work:")
    
    # Using container(border=True) creates a nice visible box in any theme
    with st.container(border=True):
        c_img, c_text = st.columns([1, 4])
        with c_img:
            st.markdown("# 📖")
        with c_text:
            st.write("### Mysterious Adventures Season 1: The New Beginning")
            st.write("_A story about new beginnings, unfolding mysteries, and the adventures that await._")
            st.link_button("Read on Wattpad", "https://www.wattpad.com/story/44610822-mysterious-adventures-season-1-the-new-beginning")

    st.divider()

    # 2. GAMING PORTFOLIO SECTION
    st.subheader("🎮 Gaming Portfolio")
    st.write("I enjoy exploring complex mechanics and lore in various genres.")

    col_games_1, col_games_2 = st.columns(2)

    with col_games_1:
        with st.expander("🏰 Metroidvania & Platformers", expanded=True):
            st.markdown("""
            * **Hollow Knight:** Deep lore exploration and challenging combat.
            * **Hollow Knight: Silksong:** (Anticipated)
            * **Geometry Dash:** Focused on completing the Top 5 most difficult levels.
            """)
            
        with st.expander("⚔️ Action & Tactical RPG", expanded=True):
            st.markdown("""
            * **Warhammer: Vermintide 2:** Co-op survival and combat mechanics.
            * **Dislyte:** Mobile turn-based RPG strategy and team building.
            """)

    with col_games_2:
        with st.expander("🏗️ Simulation & Sandbox", expanded=True):
            st.markdown("""
            * **Satisfactory:** Factory building and efficiency calculation.
            * **Core Keeper:** Mining sandbox, boss battles, and item collection.
            """)
            
        # Placeholder for future games
        with st.expander("🕹️ More Games Coming Soon...", expanded=True):
             st.write("Currently exploring new titles to add to this list!")

    st.divider()
    
    # 3. TECHNICAL SKILLS PROGRESS
    st.subheader("Technical Proficiency")
    c1, c2 = st.columns(2)
    with c1:
        st.write("Android Development (Java/Kotlin)")
        st.progress(85)
        st.write("Web Development (React/Python)")
        st.progress(75)
    with c2:
        st.write("Systems Administration")
        st.progress(70)
        st.write("Creative Arts (Drawing/Writing)")
        st.progress(90)

# 6. Interactive Footer
st.divider()
st.write("### Interactive Feedback")

b1, b2, b3 = st.columns([1, 2, 1])
with b2:
    if st.button("Click to Celebrate My Work! 🚀", use_container_width=True):
        st.balloons()
        st.snow()
        time.sleep(1)
        st.toast("Thank you for visiting my portfolio!", icon="🎉")

st.markdown("<center>Developed by Jan Elseph Yu | CIT-U Output</center>", unsafe_allow_html=True)