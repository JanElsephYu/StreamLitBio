import streamlit as st
import pandas as pd
import time
from streamlit_searchbox import st_searchbox

# 1. Page Configuration
st.set_page_config(
    page_title="Jan Elseph Yu | Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="auto"
)

# 2. Universal CSS (Mobile-Responsive & Adaptive)
st.markdown("""
<style>
    html, body, [class*="css"] {
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background: linear-gradient(45deg, #800000, #ffcc00);
        color: white !important;
        border: none;
        border-radius: 20px;
        font-weight: bold;
        transition: transform 0.2s;
        width: 100%;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    a[href*="wattpad.com"] {
        text-decoration: none;
    }
    @media (max-width: 768px) {
        .main .block-container {
            padding-top: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
        h1 {
            font-size: 2rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Profile
with st.sidebar:
    st.image("profile.JPG", caption="Jan Elseph Yu | BSIT-4", use_container_width=True)
    st.title("Connect")
    st.write("📧 janelsephyu@gmail.com")
    st.write("📍 Cebu City, Philippines")
    st.write("🏫 CIT-University")
    st.divider()
    st.caption("© 2026 Academic Portfolio")

# 4. Hero Section
col_hero_text, col_hero_empty = st.columns([2, 1])
with col_hero_text:
    st.title("Jan Elseph Yu")
    st.subheader("Aspiring IT Professional & Systems Developer")
    st.write("""
    **"Innovating one line of code at a time."**
    
    I am a 4th-year BSIT student focused on mobile development, systems administration, 
    and gamified e-learning solutions.
    """)
    st.write("---")

# 5. DATA LOGIC (GAMES LIST)
ALL_GAMES = [
    {"title": "Minecraft", "genre": "Sandbox", "desc": "The ultimate voxel sandbox for creativity and survival.", "link": "https://www.minecraft.net/"},
    {"title": "Terraria", "genre": "Sandbox", "desc": "2D action-adventure sandbox with deep progression.", "link": "https://store.steampowered.com/app/105600/Terraria/"},
    {"title": "Core Keeper", "genre": "Sandbox", "desc": "Mining sandbox adventure with bosses and relics.", "link": "https://store.steampowered.com/app/1621690/Core_Keeper/"},
    {"title": "Grounded", "genre": "Survival", "desc": "Survival adventure shrunk down in a backyard environment.", "link": "https://store.steampowered.com/app/962130/Grounded/"},
    {"title": "The Forest", "genre": "Horror Survival", "desc": "Intense survival horror against cannibals.", "link": "https://store.steampowered.com/app/242760/The_Forest/"},
    {"title": "Necesse", "genre": "Sandbox", "desc": "Top-down procedural sandbox action-adventure.", "link": "https://store.steampowered.com/app/1169040/Necesse/"},
    {"title": "Palworld", "genre": "Survival", "desc": "Monster-collecting survival game with automation elements.", "link": "https://store.steampowered.com/app/1623730/Palworld/"},
    {"title": "Satisfactory", "genre": "Simulation", "desc": "First-person open-world factory building.", "link": "https://store.steampowered.com/app/526870/Satisfactory/"},
    {"title": "House Flipper", "genre": "Simulation", "desc": "Renovation simulation (flipping houses for profit).", "link": "https://store.steampowered.com/app/613100/House_Flipper/"},
    {"title": "Burger Shop", "genre": "Time Management", "desc": "Fast-paced food making time-management sim.", "link": "https://store.steampowered.com/app/730840/Burger_Shop/"},
    {"title": "Dragon City", "genre": "Strategy", "desc": "Breeding and battling strategy game with dragons.", "link": "https://play.google.com/store/apps/details?id=es.socialpoint.DragonCity"},
    {"title": "God of War", "genre": "Action-Adventure", "desc": "Mythological action focused on combat and fatherhood.", "link": "https://store.steampowered.com/app/1593500/God_of_War/"},
    {"title": "Ninja Gaiden", "genre": "Action", "desc": "High-difficulty hack-and-slash action.", "link": "https://store.steampowered.com/app/1580780/NINJA_GAIDEN_Master_Collection_NINJA_GAIDEN_Sigma/"},
    {"title": "Prototype", "genre": "Action", "desc": "Open-world action featuring a shapeshifting anti-hero.", "link": "https://store.steampowered.com/app/10150/Prototype/"},
    {"title": "Grand Theft Auto V", "genre": "Action", "desc": "Open-world crime and action-adventure.", "link": "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/"},
    {"title": "Warframe", "genre": "Shooter", "desc": "High-speed space ninja looter shooter.", "link": "https://store.steampowered.com/app/230410/Warframe/"},
    {"title": "Fallout 4", "genre": "RPG", "desc": "Post-apocalyptic RPG exploring the wasteland.", "link": "https://store.steampowered.com/app/377160/Fallout_4/"},
    {"title": "Dislyte", "genre": "RPG", "desc": "Urban mythological turn-based RPG.", "link": "https://dislyte.farlightgames.com/"},
    {"title": "Resident Evil Village", "genre": "Horror", "desc": "The premier survival horror franchise.", "link": "https://store.steampowered.com/app/1196590/Resident_Evil_Village/"},
    {"title": "Left 4 Dead 2", "genre": "Shooter", "desc": "Classic co-op zombie apocalypse shooter.", "link": "https://store.steampowered.com/app/550/Left_4_Dead_2/"},
    {"title": "Miscrits", "genre": "Classic RPG", "desc": "Open-world monster battling RPG (Facebook Classic).", "link": "https://miscrits.fandom.com/wiki/Miscrits:_World_of_Creatures_Wiki"},
    {"title": "Blood Brothers", "genre": "Classic RPG", "desc": "Dark fantasy vampire RPG by DeNA (Classic).", "link": "https://bloodbrothers.fandom.com/wiki/Blood_Brothers_Wiki"},
    {"title": "Hollow Knight", "genre": "Metroidvania", "desc": "Deep lore exploration and challenging combat.", "link": "https://store.steampowered.com/app/367520/Hollow_Knight/"},
    {"title": "Geometry Dash", "genre": "Rhythm", "desc": "Rhythm-based platformer focused on difficulty.", "link": "https://store.steampowered.com/app/322170/Geometry_Dash/"},
    {"title": "Need for Speed Heat", "genre": "Racing", "desc": "Street racing and police chases.", "link": "https://store.steampowered.com/app/1222680/Need_for_Speed_Heat/"},
    {"title": "Piano Tiles 2", "genre": "Rhythm", "desc": "Reflex-based music rhythm game.", "link": "https://play.google.com/store/apps/details?id=com.kooapps.pianotiles2gp"}
]

def search_game_logic(searchterm: str):
    return [g["title"] for g in ALL_GAMES if searchterm.lower() in g["title"].lower()] if searchterm else []

def display_game_link(title):
    game = next((g for g in ALL_GAMES if g["title"] == title), None)
    if game:
        st.markdown(f"- **[{game['title']}]({game['link']})**: {game['desc']}")

# 6. Main Navigation Tabs
tab1, tab2, tab3 = st.tabs(["👤 Personal Profile", "🚀 Featured Projects", "🎮 Hobbyist Zone"])

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

with tab3:
    st.header("Beyond the Code")
    st.subheader("✍️ Creative Writing")
    with st.container(border=True):
        c_img, c_text = st.columns([1, 4])
        with c_img:
            st.markdown("# 📖")
        with c_text:
            st.write("### Mysterious Adventures")
            st.write("_A story about new beginnings, unfolding mysteries, and adventures._")
            st.link_button("Read on Wattpad", "https://www.wattpad.com/story/44610822-mysterious-adventures-season-1-the-new-beginning", use_container_width=True)

    st.divider()
    st.subheader("🎮 Gaming Collection")
    col_graph, col_search = st.columns([1, 1])
    with col_graph:
        st.write("### 📊 Gaming Stats")
        game_data = pd.DataFrame({
            'Genre': ['Sandbox & Sim', 'Action & RPG', 'Horror & Classics', 'Rhythm & Others'],
            'Games Played': [11, 7, 4, 4] 
        })
        st.bar_chart(game_data, x="Genre", y="Games Played", color="#800000", use_container_width=True)
    with col_search:
        st.write("### 🔍 Search Library")
        st.caption("Type a game name (e.g., 'Terraria') to see details.")
        selected_game = st_searchbox(
            search_game_logic,
            placeholder="Search game titles...",
            key="game_searchbox"
        )
        if selected_game:
            result = next((g for g in ALL_GAMES if g["title"] == selected_game), None)
            if result:
                st.success(f"**Found:** {result['title']}")
                st.write(f"**Genre:** {result['genre']}")
                st.info(f"📝 {result['desc']}")
                st.link_button(f"🔗 Go to {result['title']} Page", result['link'], use_container_width=True)

    st.write("---")
    st.write("A curated list of games I have enjoyed over the years, organized by genre.")
    g_tab1, g_tab2, g_tab3, g_tab4 = st.tabs(["🏗️ Sandbox & Sim", "⚔️ Action & RPG", "👻 Horror & Classics", "🎵 Rhythm & Others"])

    with g_tab1:
        st.caption("Building, surviving, and managing worlds.")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            with st.expander("🌲 Survival Sandbox", expanded=True):
                for g in ["Minecraft", "Terraria", "Core Keeper", "Grounded", "The Forest", "Necesse", "Palworld"]:
                    display_game_link(g)
        with col_s2:
             with st.expander("🏭 Simulation & Management", expanded=True):
                for g in ["Satisfactory", "House Flipper", "Burger Shop", "Dragon City"]:
                    display_game_link(g)
    with g_tab2:
        st.caption("High-octane combat and deep storytelling.")
        col_a1, col_a2 = st.columns(2)
        with col_a1:
            with st.expander("⚔️ Action-Adventure", expanded=True):
                for g in ["God of War", "Ninja Gaiden", "Prototype", "Grand Theft Auto V"]:
                    display_game_link(g)
        with col_a2:
             with st.expander("🚀 RPG & Shooters", expanded=True):
                for g in ["Warframe", "Fallout 4", "Dislyte"]:
                    display_game_link(g)
    with g_tab3:
        st.caption("Scary moments and nostalgic memories.")
        col_h1, col_h2 = st.columns(2)
        with col_h1:
            with st.expander("🧟 Horror & Zombies", expanded=True):
                for g in ["Resident Evil Village", "Left 4 Dead 2"]:
                    display_game_link(g)
        with col_h2:
             with st.expander("💾 Classics & Nostalgia", expanded=True):
                for g in ["Miscrits", "Blood Brothers"]:
                    display_game_link(g)
    with g_tab4:
        st.caption("Platforming, speed, and rhythm.")
        col_o1, col_o2 = st.columns(2)
        with col_o1:
            with st.expander("🏰 Metroidvania & Platformers", expanded=True):
                for g in ["Hollow Knight", "Geometry Dash"]:
                    display_game_link(g)
        with col_o2:
             with st.expander("🏎️ Racing & Rhythm", expanded=True):
                for g in ["Need for Speed Heat", "Piano Tiles 2"]:
                    display_game_link(g)

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