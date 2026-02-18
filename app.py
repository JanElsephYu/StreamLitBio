import streamlit as st
import pandas as pd
import base64
from streamlit_searchbox import st_searchbox

# 1. Page Configuration
st.set_page_config(
    page_title="Jan Elseph Yu | Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="auto"
)

# --- BACKGROUND VIDEO LOGIC ---
def add_bg_from_local(image_file):
    try:
        with open(image_file, "rb") as file:
            encoded_string = base64.b64encode(file.read())
        st.markdown(
            f"""
            <style>
            #myVideo {{
                position: fixed;
                right: 0;
                bottom: 0;
                min-width: 100%; 
                min-height: 100%;
                z-index: -1;
                filter: blur(8px) brightness(0.5); 
                object-fit: cover;
            }}
            .stApp {{ background: transparent; }}
            div[data-testid="stExpander"], div[data-testid="stContainer"] {{
                background-color: rgba(255, 255, 255, 0.9);
                box-shadow: 0 10px 20px rgba(0,0,0,0.5);
                border-radius: 10px;
                border: 1px solid rgba(255,255,255,0.2);
            }}
            @media (prefers-color-scheme: dark) {{
                div[data-testid="stExpander"], div[data-testid="stContainer"] {{
                    background-color: rgba(30, 30, 30, 0.9);
                    box-shadow: 0 10px 20px rgba(0,0,0,0.8);
                }}
            }}
            </style>
            <video autoplay muted loop id="myVideo" playsinline>
                <source src="data:video/mp4;base64,{encoded_string.decode()}" type="video/mp4">
            </video>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("⚠️ 'background.mp4' not found.")

add_bg_from_local('background.mp4')

# 2. CSS Styling
st.markdown("""
<style>
    html, body, [class*="css"] { font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button {
        background: linear-gradient(45deg, #800000, #ffcc00);
        color: white !important;
        border: none;
        border-radius: 20px;
        font-weight: bold;
        transition: transform 0.2s;
        width: 100%;
    }
    .stButton>button:hover { transform: scale(1.02); }
    a { text-decoration: none; }
    
    /* Skill Badge Styling */
    .skill-badge {
        background-color: #800000;
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.85em;
        margin: 2px;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar (UPDATED WITH RESUME DETAILS)
with st.sidebar:
    st.image("profile.JPG", caption="Jan Elseph Yu | BSIT-4", use_container_width=True)
    
    st.title("Contact Info")
    st.markdown("📧 **Email:**")
    st.caption("janelsephyu@gmail.com")
    st.markdown("📍 **Location:**")
    st.caption("Cebu City, Philippines")
    st.markdown("🔗 **Socials:**")
    st.caption("[LinkedIn Profile](https://linkedin.com) | [GitHub Profile](https://github.com)")
    
    st.divider()
    
    st.subheader("🛠️ Tech Stack")
    st.markdown("""
    <div style="line-height: 2;">
        <span class="skill-badge">Python</span>
        <span class="skill-badge">Java</span>
        <span class="skill-badge">C++</span>
        <span class="skill-badge">React JS</span>
        <span class="skill-badge">Springboot</span>
        <span class="skill-badge">MySQL</span>
        <span class="skill-badge">AWS</span>
        <span class="skill-badge">Linux</span>
        <span class="skill-badge">Android Studio</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("🧩 Soft Skills")
    st.markdown("""
    - Leadership & Team Management
    - System Administration
    - Creative Problem Solving
    - Technical Documentation
    """)
    
    st.divider()
    st.caption("© 2026 Academic Portfolio")

# 4. Hero Section
col_hero, _ = st.columns([2, 1])
with col_hero:
    st.title("Jan Elseph Yu")
    st.subheader("Aspiring IT Professional & Systems Developer")
    st.write("**\"Innovating one line of code at a time.\"**")
    st.write("---")

# 5. DATA LOGIC: THE MASTER LIST (UNCHANGED)
ALL_GAMES = [
    # --- TOP 5 FAVORITES (Data for Logic) ---
    {"title": "Satisfactory", "genre": "Simulation", "tags": "Automation, Base Building, Co-op", "dev": "Coffee Stain", "date": "2020", "desc": "An open-world factory building game played from a first-person perspective. Construct multi-story factories, enter conveyor belt heaven, automate vehicles, and research new technologies.", "link": "https://store.steampowered.com/app/526870/Satisfactory/"},
    {"title": "Blood Brothers", "genre": "RPG", "tags": "Dark Fantasy, Vampire, Strategy", "dev": "DeNA", "date": "2012", "desc": "A dark fantasy RPG that tasked players with binding an army in a pact of blood to exact vengeance on a corrupt empire. Known for its distinct gothic art style and addicting creature evolution system.", "link": "https://bloodbrothers.fandom.com/wiki/Blood_Brothers_Wiki"},
    {"title": "Minecraft", "genre": "Sandbox", "tags": "Survival, Open World, Crafting", "dev": "Mojang", "date": "2011", "desc": "The ultimate sandbox game that allows players to build anything they can imagine with blocks. Features a survival mode with hunger and mobs, and a creative mode for limitless building.", "link": "https://www.minecraft.net/"},
    {"title": "Burger Shop", "genre": "Time Management", "tags": "Casual, Cooking, Fast-Paced", "dev": "GoBit Games", "date": "2007", "desc": "A fast-paced food making game where you must serve hungry customers by assembling burgers, shakes, and fries using a specialized conveyor belt machine.", "link": "https://store.steampowered.com/app/730840/Burger_Shop/"},
    {"title": "House Flipper", "genre": "Simulation", "tags": "Relaxing, Design, Realistic", "dev": "Empyrean", "date": "2018", "desc": "A unique chance to become a one-man renovation crew. Buy, repair, and remodel devastated houses. Give them a second life and sell them at a profit.", "link": "https://store.steampowered.com/app/613100/House_Flipper/"},

    # --- SANDBOX & SURVIVAL ---
    {"title": "Terraria", "genre": "Sandbox", "tags": "2D, Adventure, Crafting", "dev": "Re-Logic", "date": "2011", "desc": "Dig, fight, explore, build! Nothing is impossible in this action-packed adventure game. The world is your canvas and the ground itself is your paint.", "link": "https://store.steampowered.com/app/105600/Terraria/"},
    {"title": "Core Keeper", "genre": "Sandbox", "tags": "Pixel Graphics, Mining, Co-op", "dev": "Pugstorm", "date": "2022", "desc": "Explore an endless cavern of creatures, relics and resources in a mining sandbox adventure for 1-8 players. Mine, build, fight, craft and farm to unravel the mystery of the ancient Core.", "link": "https://store.steampowered.com/app/1621690/Core_Keeper/"},
    {"title": "Grounded", "genre": "Survival", "tags": "Co-op, Insects, Base Building", "dev": "Obsidian Ent.", "date": "2022", "desc": "The world is a vast, beautiful and dangerous place – especially when you have been shrunk to the size of an ant. Explore, build and survive together in this first-person multiplayer survival-adventure.", "link": "https://store.steampowered.com/app/962130/Grounded/"},
    {"title": "The Forest", "genre": "Survival Horror", "tags": "Open World, Crafting, Horror", "dev": "Endnight Games", "date": "2018", "desc": "As the lone survivor of a passenger jet crash, you find yourself in a mysterious forest battling to stay alive against a society of cannibalistic mutants.", "link": "https://store.steampowered.com/app/242760/The_Forest/"},
    {"title": "Necesse", "genre": "Sandbox", "tags": "Top-Down, Colony Sim, RPG", "dev": "Fair Games", "date": "2019", "desc": "A top-down sandbox action-adventure game in a procedurally generated infinite world. Fight bosses, recruit settlers, and build your settlement.", "link": "https://store.steampowered.com/app/1169040/Necesse/"},
    {"title": "Palworld", "genre": "Survival", "tags": "Creature Collector, Automation", "dev": "Pocketpair", "date": "2024", "desc": "A multiplayer open-world survival crafting game where you can fight, farm, build, and work alongside mysterious creatures called 'Pals'.", "link": "https://store.steampowered.com/app/1623730/Palworld/"},

    # --- ACTION & ADVENTURE ---
    {"title": "Ninja Gaiden Sigma", "genre": "Action", "tags": "Hack and Slash, Difficult, Ninja", "dev": "Team Ninja", "date": "2007", "desc": "The definitive version of the classic action game. assume the role of super ninja Ryu Hayabusa and seek vengeance against the Vigor Empire.", "link": "https://store.steampowered.com/app/1580780/NINJA_GAIDEN_Master_Collection_NINJA_GAIDEN_Sigma/"},
    {"title": "God of War", "genre": "Action", "tags": "Story Rich, Mythology, Combat", "dev": "Santa Monica", "date": "2018", "desc": "His vengeance against the Gods of Olympus years behind him, Kratos now lives as a man in the realm of Norse Gods and monsters. He must fight to survive... and teach his son to do the same.", "link": "https://store.steampowered.com/app/1593500/God_of_War/"},
    {"title": "Grand Theft Auto V", "genre": "Action", "tags": "Open World, Crime, Multiplayer", "dev": "Rockstar North", "date": "2013", "desc": "When a young street hustler, a retired bank robber and a terrifying psychopath find themselves entangled with some of the most frightening elements of the criminal underworld, they must pull off a series of dangerous heists.", "link": "https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/"},
    {"title": "Prototype", "genre": "Action", "tags": "Open World, Superpower, Gore", "dev": "Radical Ent.", "date": "2009", "desc": "You are the Prototype, Alex Mercer, a man without memory armed with amazing shape-shifting abilities, hunting your way to the heart of the conspiracy which created you.", "link": "https://store.steampowered.com/app/10150/Prototype/"},
    {"title": "Risk of Rain 2", "genre": "Roguelike", "tags": "Third-Person Shooter, Co-op, Loot", "dev": "Hopoo Games", "date": "2020", "desc": "Escape a chaotic alien planet by fighting through hordes of frenzied monsters – with your friends, or on your own. Combine loot in surprising ways and master each character.", "link": "https://store.steampowered.com/app/632360/Risk_of_Rain_2/"},

    # --- RPG & STRATEGY ---
    {"title": "Warframe", "genre": "RPG", "tags": "Looter Shooter, Ninja, Co-op", "dev": "Digital Extremes", "date": "2013", "desc": "Awaken as an unstoppable warrior and battle alongside your friends in this story-driven free-to-play online action game.", "link": "https://store.steampowered.com/app/230410/Warframe/"},
    {"title": "Fallout 4", "genre": "RPG", "tags": "Post-apocalyptic, Exploration", "dev": "Bethesda", "date": "2015", "desc": "Bethesda Game Studios, the award-winning creators of Fallout 3 and The Elder Scrolls V: Skyrim, welcome you to the world of Fallout 4 – their most ambitious game ever, and the next generation of open-world gaming.", "link": "https://store.steampowered.com/app/377160/Fallout_4/"},
    {"title": "Dislyte", "genre": "RPG", "tags": "Turn-Based, Urban Myth, Gacha", "dev": "Farlight Games", "date": "2022", "desc": "A stylish urban mythological RPG. Ordinary people become 'Espers' gaining powers from ancient gods to fight monsters in a neon-lit futuristic world.", "link": "https://dislyte.farlightgames.com/"},
    {"title": "Mobile Legends: Bang Bang", "genre": "MOBA", "tags": "5v5, Competitive, Strategy", "dev": "Moonton", "date": "2016", "desc": "Join your friends in a brand new 5v5 MOBA showdown against real human opponents. Choose your favorite heroes and build the perfect team with your comrades-in-arms.", "link": "https://m.mobilelegends.com/"},
    {"title": "Guardian Tales", "genre": "RPG", "tags": "Pixel Art, Puzzle, Adventure", "dev": "Kong Studios", "date": "2020", "desc": "A link to classic adventure RPGs! Solve challenging puzzles, battle strategic bosses, and explore a world filled with secrets and pop culture references.", "link": "https://guardiantales.com/"},
    {"title": "King God Castle", "genre": "Strategy", "tags": "Auto Battler, Defense, Pixel", "dev": "Awesomepiece", "date": "2020", "desc": "Threatened by powerful enemies, use heroes, the power of the gods, and your own strategy to defend your castle in this strategic defense game.", "link": "https://play.google.com/store/apps/details?id=com.awesomepiece.castle"},
    {"title": "Bloons TD 6", "genre": "Strategy", "tags": "Tower Defense, Co-op, Strategy", "dev": "Ninja Kiwi", "date": "2018", "desc": "The ultimate Tower Defense game. Craft your perfect defense from a combination of awesome Monkey Towers, upgrades, Heroes, and activated abilities.", "link": "https://store.steampowered.com/app/960090/Bloons_TD_6/"},
    {"title": "Pokemon", "genre": "RPG", "tags": "Creature Collector, Turn-Based", "dev": "Game Freak", "date": "1996", "desc": "The world-famous franchise about catching, training, and battling colorful creatures. A journey of exploration and friendship.", "link": "https://www.pokemon.com/"},
    {"title": "Dragon City", "genre": "Simulation", "tags": "Breeding, City Builder", "dev": "Socialpoint", "date": "2012", "desc": "Build a magical world in Dragon City! Gain hundreds of dragons, breed them and make them level up in order to become a Dragon Master.", "link": "https://play.google.com/store/apps/details?id=es.socialpoint.DragonCity"},
    {"title": "Adventure Quest Worlds", "genre": "MMORPG", "tags": "Browser, 2D, Fantasy", "dev": "Artix Ent.", "date": "2008", "desc": "A 2D browser-based fantasy MMORPG featuring real-time combat, distinct classes, and weekly story updates.", "link": "https://www.aq.com/"},
    {"title": "Miscrits", "genre": "RPG", "tags": "Creature Collector, Nostalgia", "dev": "Broken Bulb", "date": "2011", "desc": "A classic open-world creature collecting RPG played by millions on Facebook. Capture and train Miscrits to battle in the arena.", "link": "https://miscrits.fandom.com/wiki/Miscrits:_World_of_Creatures_Wiki"},

    # --- HORROR ---
    {"title": "Resident Evil 5", "genre": "Horror", "tags": "Co-op, Zombies, Action", "dev": "Capcom", "date": "2009", "desc": "The Umbrella Corporation and its crop of lethal viruses have been destroyed and contained. But a new, more dangerous threat has emerged. Features intense co-op gameplay.", "link": "https://store.steampowered.com/app/21690/Resident_Evil_5/"},
    {"title": "Left 4 Dead 2", "genre": "Horror", "tags": "Co-op, Shooter, Zombies", "dev": "Valve", "date": "2009", "desc": "Set in the zombie apocalypse, Left 4 Dead 2 (L4D2) is the highly anticipated sequel to the award-winning Left 4 Dead, the #1 co-op game of 2008.", "link": "https://store.steampowered.com/app/550/Left_4_Dead_2/"},

    # --- PLATFORMER & PUZZLE ---
    {"title": "Hollow Knight", "genre": "Metroidvania", "tags": "Souls-like, 2D, Difficult", "dev": "Team Cherry", "date": "2017", "desc": "Forge your own path in Hollow Knight! An epic action adventure through a vast ruined kingdom of insects and heroes. Explore twisting caverns, battle tainted creatures and befriend bizarre bugs.", "link": "https://store.steampowered.com/app/367520/Hollow_Knight/"},
    {"title": "Hollow Knight: Silksong", "genre": "Metroidvania", "tags": "Anticipated, Sequel, 2D", "dev": "Team Cherry", "date": "TBA", "desc": "Discover a vast, haunted kingdom in Hollow Knight: Silksong! The sequel to the award winning action-adventure. Explore, fight and survive as you ascend to the peak of a land ruled by silk and song.", "link": "https://store.steampowered.com/app/1030300/Hollow_Knight_Silksong/"},
    {"title": "Geometry Dash", "genre": "Platformer", "tags": "Rhythm, Difficult, Level Editor", "dev": "RobTop", "date": "2013", "desc": "Jump and fly your way through danger in this rhythm-based action platformer! Prepare for a near impossible challenge in the world of Geometry Dash.", "link": "https://store.steampowered.com/app/322170/Geometry_Dash/"},
    {"title": "Wordscapes", "genre": "Puzzle", "tags": "Word Game, Relaxing", "dev": "PeopleFun", "date": "2017", "desc": "This text twist of a word game is tremendous brain challenging fun. Enjoy modern word puzzles with the best of word searching, anagrams, and crosswords!", "link": "https://play.google.com/store/apps/details?id=com.peoplefun.wordcross"},
    {"title": "Piano Tiles 2", "genre": "Rhythm", "tags": "Music, Reflexes", "dev": "Cheetah Mobile", "date": "2015", "desc": "A popular music arcade game. Tap the black tiles according to the melody and don't tap the white tiles!", "link": "https://play.google.com/store/apps/details?id=com.kooapps.pianotiles2gp"},

    # --- RACING ---
    {"title": "Need for Speed: Most Wanted", "genre": "Racing", "tags": "Open World, Police, Classic", "dev": "EA Black Box", "date": "2005", "desc": "The original 2005 classic. Wake up to the smell of burnt asphalt as the thrill of illicit street racing permeates the air. Become the most notorious street racer.", "link": "https://en.wikipedia.org/wiki/Need_for_Speed:_Most_Wanted_(2005_video_game)"},
]

# Helper to display game card
def game_card(game):
    with st.expander(f"🎮 {game['title']} ({game['date']})", expanded=True):
        st.markdown(f"**Dev:** {game['dev']} | **Tags:** `{game['tags']}`")
        st.write(game['desc'])
        st.link_button(f"🔗 Visit {game['title']}", game['link'], use_container_width=True)

# Search Logic
def search_game_logic(searchterm: str):
    return [g["title"] for g in ALL_GAMES if searchterm.lower() in g["title"].lower()] if searchterm else []

# --- TAB LOGIC ---
tab1, tab2, tab3 = st.tabs(["👤 Personal Profile", "🚀 Featured Projects", "🎮 Hobbyist Zone"])

# --- TAB 1: UPDATED WITH RESUME CONTENT ---
with tab1:
    st.header("My Biography")
    
    # Professional Summary
    with st.container(border=True):
        st.subheader("🎯 Professional Summary")
        st.write("""
        A dedicated 4th-year **Bachelor of Science in Information Technology** student at **Cebu Institute of Technology - University**. 
        
        Passionate about bridging the gap between technical systems and creative expression. Specialized in **Systems Administration** and **Android Development**, with hands-on experience in building gamified e-learning platforms (SyntaxType), scholar management systems (SEMS/NASMS), and indoor positioning solutions (GIPS).
        
        Currently seeking OJT opportunities to leverage skills in **Java, Python, and Cloud Architecture** to solve real-world problems.
        """)

    # Personal Details & Education
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("📌 Personal Information")
            st.write("**Name:** Jan Elseph Yu")
            st.write("**Age:** 25 Years Old")
            st.write("**Birthdate:** January 11, 2001")
            st.write("**Nationality:** Filipino")
            st.write("**Address:** Cebu City, Philippines")
    
    with col2:
        with st.container(border=True):
            st.subheader("🎓 Education")
            st.write("**Bachelor of Science in Information Technology**")
            st.write("*Cebu Institute of Technology - University*")
            st.caption("📅 2022 - Present (Expected Graduation: 2026)")
            st.write("---")
            st.write("**Certifications:**")
            st.markdown("- ✅ **AWS Academy Cloud Architecting**")
            st.markdown("- ✅ **Introduction to Blockchain (CSIT360)**")

    # Key Competencies
    st.subheader("💡 Key Competencies")
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.write("**💻 Development**")
            st.markdown("- Android Dev (Java/Kotlin)")
            st.markdown("- Web Dev (React JS)")
            st.markdown("- Python Scripting")
    with c2:
        with st.container(border=True):
            st.write("**⚙️ Systems**")
            st.markdown("- Linux Administration")
            st.markdown("- RAID Configuration")
            st.markdown("- Cloud Architecture (AWS)")
    with c3:
        with st.container(border=True):
            st.write("**🛠️ Tools**")
            st.markdown("- Git & GitHub")
            st.markdown("- MySQL Database")
            st.markdown("- Visual Studio Code")

with tab2:
    st.header("Project Portfolio")
    c1, c2 = st.columns(2)
    with c1:
        with st.expander("⭐ GIPS (Grocery Indoor Positioning System)"):
            st.write("Android app for indoor grocery navigation.")
        with st.expander("🎓 SEMS (Scholarship System)"):
            st.write("Web/Mobile system for managing CIT-U scholarships.")
    with c2:
        with st.expander("📱 NASMS (Non-Academic Scholar System)"):
            st.write("Mobile app with PDF conversion for scholars.")
        with st.expander("⌨️ SyntaxType (Capstone)"):
            st.write("Gamified typing platform for BSIT freshmen.")

with tab3:
    st.header("Beyond the Code")
    
    # --- TOP 5 SECTION ---
    st.markdown("### 🏆 My Top 5 All-Time Favorites")
    st.info("These are the games that defined my gaming journey.")
    
    top5_cols = st.columns(5)
    
    # Top 1
    with top5_cols[0]:
        st.image("https://img.icons8.com/color/96/1-circle.png", width=50)
        st.write("**Satisfactory**")
        st.caption("*\"Building a factory has never been more satisfying, pun intended.\"*")
    
    # Top 2
    with top5_cols[1]:
        st.image("https://img.icons8.com/color/96/2-circle.png", width=50)
        st.write("**Blood Brothers**")
        st.caption("*\"I was devastated when this game got discontinued. My most grinded game as a kid.\"*")
        
    # Top 3
    with top5_cols[2]:
        st.image("https://img.icons8.com/color/96/3-circle.png", width=50)
        st.write("**Minecraft**")
        st.caption("*\"Who doesn't love Minecraft? Creativity, survival challenge, and playing with friends.\"*")
        
    # Top 4
    with top5_cols[3]:
        st.image("https://img.icons8.com/color/96/4-circle.png", width=50)
        st.write("**Burger Shop**")
        st.caption("*\"I don't know why, I just keep coming back to this game.\"*")
        
    # Top 5
    with top5_cols[4]:
        st.image("https://img.icons8.com/color/96/5-circle.png", width=50)
        st.write("**House Flipper**")
        st.caption("*\"Designing, cleaning, and organizing has never been more relaxing.\"*")

    st.divider()

    # --- SEARCH & GRAPH ---
    c_graph, c_search = st.columns([1, 1])
    with c_graph:
        st.write("### 📊 Genre Breakdown")
        df = pd.DataFrame(ALL_GAMES)
        # Simple count by Genre
        chart_data = df['genre'].value_counts()
        st.bar_chart(chart_data, color="#800000")
        
    with c_search:
        st.write("### 🔍 Search Collection")
        selected = st_searchbox(search_game_logic, key="search")
        if selected:
            res = next((g for g in ALL_GAMES if g["title"] == selected), None)
            if res:
                st.success(f"Found: {res['title']}")
                game_card(res)

    st.write("---")
    
    # --- CATEGORIZED TABS ---
    st.subheader("Browse Full Collection")
    g_tabs = st.tabs(["Strategy & Sim", "Action & Adventure", "RPG", "Survival & Horror", "Platformer & Others"])

    # 1. Strategy & Simulation
    with g_tabs[0]:
        st.caption("Building, Management, and Tactics")
        cols = st.columns(2)
        sim_games = [g for g in ALL_GAMES if g['genre'] in ['Simulation', 'Strategy', 'Time Management']]
        for i, game in enumerate(sim_games):
            with cols[i % 2]:
                game_card(game)

    # 2. Action & Adventure
    with g_tabs[1]:
        st.caption("High-octane Combat and Story")
        cols = st.columns(2)
        act_games = [g for g in ALL_GAMES if g['genre'] in ['Action', 'Roguelike', 'Racing']]
        for i, game in enumerate(act_games):
            with cols[i % 2]:
                game_card(game)

    # 3. RPG
    with g_tabs[2]:
        st.caption("Role-Playing, Looters, and MOBAs")
        cols = st.columns(2)
        rpg_games = [g for g in ALL_GAMES if g['genre'] in ['RPG', 'MOBA', 'MMORPG']]
        for i, game in enumerate(rpg_games):
            with cols[i % 2]:
                game_card(game)

    # 4. Survival & Horror
    with g_tabs[3]:
        st.caption("Survive the Elements and the Undead")
        cols = st.columns(2)
        surv_games = [g for g in ALL_GAMES if g['genre'] in ['Survival', 'Sandbox', 'Horror', 'Survival Horror']]
        for i, game in enumerate(surv_games):
            with cols[i % 2]:
                game_card(game)

    # 5. Platformer & Others
    with g_tabs[4]:
        st.caption("Jump, Solve, and Rhythm")
        cols = st.columns(2)
        other_games = [g for g in ALL_GAMES if g['genre'] in ['Metroidvania', 'Platformer', 'Puzzle', 'Rhythm']]
        for i, game in enumerate(other_games):
            with cols[i % 2]:
                game_card(game)

st.divider()
if st.button("Celebrate My Work! 🚀", use_container_width=True):
    st.balloons()