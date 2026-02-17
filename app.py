import streamlit as st
import pandas as pd
import time
from streamlit_searchbox import st_searchbox  # New Component for the Search Feature

# 1. Page Configuration
st.set_page_config(
    page_title="Jan Elseph Yu | Professional Portfolio",
    page_icon="🎓",
    layout="wide",
)

# 2. Universal CSS (Theme-Adaptive & Clean)
st.markdown("""
<style>
    /* Global Font */
    html, body, [class*="css"] {
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* CIT-U Maroon & Gold Gradient Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #800000, #ffcc00);
        color: white !important;
        border: none;
        border-radius: 20px;
        font-weight: bold;
        transition: transform 0.2s;
    }
    
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

# 5. DATA LOGIC FOR SEARCHBOX (The "Backend" for your game list)
# We list all your games here so the search component can find them.
ALL_GAMES = [
    {"title": "Minecraft", "genre": "Sandbox", "desc": "The ultimate voxel sandbox for creativity and survival."},
    {"title": "Terraria", "genre": "Sandbox", "desc": "2D action-adventure sandbox with deep progression."},
    {"title": "Core Keeper", "genre": "Sandbox", "desc": "Mining sandbox adventure with bosses and relics."},
    {"title": "Grounded", "genre": "Survival", "desc": "Survival adventure shrunk down in a backyard environment."},
    {"title": "The Forest", "genre": "Horror Survival", "desc": "Intense survival horror against cannibals."},
    {"title": "Necesse", "genre": "Sandbox", "desc": "Top-down procedural sandbox action-adventure."},
    {"title": "Palworld", "genre": "Survival", "desc": "Monster-collecting survival game with automation elements."},
    {"title": "Satisfactory", "genre": "Simulation", "desc": "First-person open-world factory building."},
    {"title": "House Flipper", "genre": "Simulation", "desc": "Renovation simulation (flipping houses for profit)."},
    {"title": "Burger Shop", "genre": "Time Management", "desc": "Fast-paced food making time-management sim."},
    {"title": "Dragon City", "genre": "Strategy", "desc": "Breeding and battling strategy game with dragons."},
    {"title": "God of War", "genre": "Action-Adventure", "desc": "Mythological action focused on combat and fatherhood."},
    {"title": "Ninja Gaiden", "genre": "Action", "desc": "High-difficulty hack-and-slash action."},
    {"title": "Prototype", "genre": "Action", "desc": "Open-world action featuring a shapeshifting anti-hero."},
    {"title": "Grand Theft Auto", "genre": "Action", "desc": "Open-world crime and action-adventure."},
    {"title": "Warframe", "genre": "Shooter", "desc": "High-speed space ninja looter shooter."},
    {"title": "Fallout", "genre": "RPG", "desc": "Post-apocalyptic RPG exploring the wasteland."},
    {"title": "Dislyte", "genre": "RPG", "desc": "Urban mythological turn-based RPG."},
    {"title": "Resident Evil", "genre": "Horror", "desc": "The premier survival horror franchise."},
    {"title": "Left 4 Dead 2", "genre": "Shooter", "desc": "Classic co-op zombie apocalypse shooter."},
    {"title": "Miscrits", "genre": "Classic RPG", "desc": "Open-world monster battling RPG (Facebook Classic)."},
    {"title": "Blood Brothers", "genre": "Classic RPG", "desc": "Dark fantasy vampire RPG by DeNA (Classic)."},
    {"title": "Hollow Knight", "genre": "Metroidvania", "desc": "Deep lore exploration and challenging combat."},
    {"title": "Geometry Dash", "genre": "Rhythm", "desc": "Rhythm-based platformer focused on difficulty."},
    {"title": "Need for Speed", "genre": "Racing", "desc": "Street racing and police chases."},
    {"title": "Piano Tiles 2", "genre": "Rhythm", "desc": "Reflex-based music rhythm game."}
]

# Function required by streamlit-searchbox to filter results
def search_game_logic(searchterm: str):
    return [g["title"] for g in ALL_GAMES if searchterm.lower() in g["title"].lower()] if searchterm else []

# 6. Main Navigation Tabs
tab1, tab2, tab3 = st.tabs(["👤 Personal Profile", "🚀 Featured Projects", "🎮 Hobbyist Zone"])

# --- TAB 1: PERSONAL PROFILE ---
with tab1:
    st.header("My Biography")
    
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

# --- TAB 3: HOBBIES & GAMES (With Graph + Searchbox) ---
with tab3:
    st.header("Beyond the Code")
    
    # 1. CREATIVE WRITING
    st.subheader("✍️ Creative Writing")
    with st.container(border=True):
        c_img, c_text = st.columns([1, 4])
        with c_img:
            st.markdown("# 📖")
        with c_text:
            st.write("### Mysterious Adventures Season 1: The New Beginning")
            st.write("_A story about new beginnings, unfolding mysteries, and the adventures that await._")
            st.link_button("Read on Wattpad", "https://www.wattpad.com/story/44610822-mysterious-adventures-season-1-the-new-beginning")

    st.divider()

    # 2. GAMING PORTFOLIO - ANALYTICS & SEARCH
    st.subheader("🎮 Gaming Collection")
    
    # --- SPLIT LAYOUT: GRAPH on Left, SEARCH on Right ---
    col_graph, col_search = st.columns([1, 1])

    with col_graph:
        st.write("### 📊 Gaming Stats")
        # Creating a simple DataFrame for the graph
        game_data = pd.DataFrame({
            'Genre': ['Sandbox & Sim', 'Action & RPG', 'Horror & Classics', 'Rhythm & Others'],
            'Games Played': [11, 7, 4, 5] 
        })
        # Displaying the Bar Chart
        st.bar_chart(game_data, x="Genre", y="Games Played", color="#800000")
        
    with col_search:
        st.write("### 🔍 Search Library")
        st.caption("Type a game name (e.g., 'Terraria') to see details.")
        
        # THE SEARCHBOX COMPONENT
        selected_game = st_searchbox(
            search_game_logic,
            placeholder="Search game titles...",
            key="game_searchbox"
        )
        
        # Display Result if something is selected
        if selected_game:
            # Find the game details in our list
            result = next((g for g in ALL_GAMES if g["title"] == selected_game), None)
            if result:
                st.success(f"**Found:** {result['title']}")
                st.write(f"**Genre:** {result['genre']}")
                st.info(f"📝 {result['desc']}")

    st.write("---")
    st.write("A curated list of games I have enjoyed over the years, organized by genre.")

    # Organized into 4 Tabs for better readability
    g_tab1, g_tab2, g_tab3, g_tab4 = st.tabs(["🏗️ Sandbox & Sim", "⚔️ Action & RPG", "👻 Horror & Classics", "🎵 Rhythm & Others"])

    # TAB 1: SANDBOX & SIMULATION
    with g_tab1:
        st.caption("Building, surviving, and managing worlds.")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            with st.expander("🌲 Survival Sandbox", expanded=True):
                st.markdown("""
                * **Minecraft:** The ultimate voxel sandbox for creativity and survival.
                * **Terraria:** 2D action-adventure sandbox with deep progression.
                * **Core Keeper:** Mining sandbox adventure with bosses and relics.
                * **Grounded:** Survival adventure shrunk down in a backyard environment.
                * **The Forest / Sons of The Forest:** Intense survival horror against cannibals.
                * **Necesse:** Top-down procedural sandbox action-adventure.
                * **Palworld:** Monster-collecting survival game with automation elements.
                """)
        with col_s2:
             with st.expander("🏭 Simulation & Management", expanded=True):
                st.markdown("""
                * **Satisfactory:** First-person open-world factory building.
                * **House Flipper:** Renovation simulation (flipping houses for profit).
                * **Burger Shop:** Fast-paced food making time-management sim.
                * **Dragon City:** Breeding and battling strategy game with dragons.
                """)

    # TAB 2: ACTION & RPG
    with g_tab2:
        st.caption("High-octane combat and deep storytelling.")
        col_a1, col_a2 = st.columns(2)
        with col_a1:
            with st.expander("⚔️ Action-Adventure", expanded=True):
                st.markdown("""
                * **God of War:** Mythological action-adventure focused on combat and fatherhood.
                * **Ninja Gaiden:** High-difficulty hack-and-slash action.
                * **Prototype:** Open-world action featuring a shapeshifting anti-hero.
                * **Grand Theft Auto (Series):** Open-world crime and action-adventure.
                """)
        with col_a2:
             with st.expander("🚀 RPG & Shooters", expanded=True):
                st.markdown("""
                * **Warframe:** High-speed space ninja looter shooter.
                * **Fallout (Series):** Post-apocalyptic RPG exploring the wasteland.
                * **Dislyte:** Urban mythological turn-based RPG.
                """)

    # TAB 3: HORROR & CLASSICS
    with g_tab3:
        st.caption("Scary moments and nostalgic memories.")
        col_h1, col_h2 = st.columns(2)
        with col_h1:
            with st.expander("🧟 Horror & Zombies", expanded=True):
                st.markdown("""
                * **Resident Evil (Series):** The premier survival horror franchise.
                * **Left 4 Dead 2:** Classic co-op zombie apocalypse shooter.
                """)
        with col_h2:
             with st.expander("💾 Classics & Nostalgia", expanded=True):
                st.markdown("""
                * **Miscrits:** Open-world monster battling RPG (Facebook Classic).
                * **Blood Brothers:** Dark fantasy vampire RPG by DeNA (Classic).
                """)

    # TAB 4: PLATFORMERS & OTHERS
    with g_tab4:
        st.caption("Platforming, speed, and rhythm.")
        col_o1, col_o2 = st.columns(2)
        with col_o1:
            with st.expander("🏰 Metroidvania & Platformers", expanded=True):
                st.markdown("""
                * **Hollow Knight:** Deep lore exploration and challenging combat.
                * **Hollow Knight: Silksong:** (Anticipated sequel).
                * **Geometry Dash:** Rhythm-based platformer focused on difficulty.
                """)
        with col_o2:
             with st.expander("🏎️ Racing & Rhythm", expanded=True):
                st.markdown("""
                * **Need for Speed (Series):** Street racing and police chases.
                * **Piano Tiles 2:** Reflex-based music rhythm game.
                """)

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