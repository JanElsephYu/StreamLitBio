import streamlit as st

# 1. Professional Page Setup
st.set_page_config(
    page_title="Jan Elseph Yu | Academic Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Sidebar Profile
with st.sidebar:
    # This assumes you have uploaded 'profile.jpg' to your GitHub repo
    st.image("profile.JPG", caption="Jan Elseph Yu")
    st.title("At a Glance")
    st.write("📍 **Location:** Cebu City, PH")
    st.write("🏫 **University:** CIT-University")
    st.write("🎯 **Course:** BSIT-4")
    st.divider()
    st.write("**Direct Contact:**")
    st.caption("janelsephyu@gmail.com")

# 3. Main Header
st.title("👨‍💻 The Digital Autobiography of Jan Elseph Yu")
st.subheader("BSIT Senior Student | Aspiring IT Professional")
st.divider()

# 4. Multi-Component Tabs (Full Utilization)
tab1, tab2, tab3 = st.tabs(["👤 Personal Profile", "🚀 Academic Projects", "🛠 Skills & Hobbies"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Basic Information")
        st.write(f"**Full Name:** Jan Elseph Yu")
        st.write(f"**Birthday:** January 11, 2001")
        st.write(f"**Age:** 25 Years Old")
        st.write(f"**Current Year:** 4th Year (Senior)")
        
    with col2:
        st.header("Brief Bio")
        st.write("""
        I am a dedicated Information Technology student at the Cebu Institute of Technology - University. 
        As I near the completion of my BSIT degree, I am focused on bridging the gap between 
        technical system administration and creative digital expression.
        """)
        st.info("Currently focused on completing OJT requirements for graduation.")

with tab2:
    st.header("Academic Highlights")
    # Using metrics for a dashboard aesthetic
    m1, m2, m3 = st.columns(3)
    m1.metric("Degree", "BSIT")
    m2.metric("Specialization", "SysAdmin")
    m3.metric("University", "CIT-U")
    
    st.write("### Featured Projects")
    with st.expander("⭐ SyntaxType: E-Learning Platform"):
        st.write("A gamified typing platform designed for first-year BSIT students to master technical typing.")
        
    with st.expander("🛡️ CloudFour: Systems Administration"):
        st.write("A project focused on RAID configurations and storage management solutions.")

with tab3:
    st.header("Beyond the Classroom")
    
    col_hobbies, col_skills = st.columns(2)
    
    with col_hobbies:
        st.subheader("My Hobbies")
        # Displaying hobbies with different status boxes for variety
        st.success("🎨 **Drawing:** Digital and traditional art.")
        st.info("✍️ **Writing Stories:** A passion for world-building and narrative.")
        st.warning("🎮 **Gaming:** Exploring mechanics and immersive worlds.")
        
    with col_skills:
        st.subheader("Technical Proficiency")
        st.progress(85, text="Java & C++")
        st.progress(75, text="Web Development (React/MySQL)")
        st.progress(65, text="Blockchain & Cloud Architecture")

# 5. Interactive Grade Bonus Components
st.divider()
st.write("### Interaction Section")
if st.button("Celebrate My Journey!"):
    st.balloons()
    st.snow()
    st.toast("Portfolio Successfully Displayed!", icon='🎉')

st.caption("© 2026 | Developed by Jan Elseph Yu for CIT-U IT Assignment")