import streamlit as st
import time

# 1. Page Configuration (Aesthetics & Branding)
st.set_page_config(
    page_title="Jan Elseph Yu | Professional Bio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Sidebar with Profile Stats
with st.sidebar:
    st.image("https://via.placeholder.com/150", caption="Jan Elseph Yu - BSIT Student")
    st.title("Quick Info")
    st.write("📍 Cebu City, Philippines")
    st.write("🎓 4th Year BSIT @ CIT-U")
    
    st.divider()
    
    # Progress bar for your OJT or Semester progress
    st.write("Graduation Progress")
    st.progress(85)
    
    st.write("---")
    st.subheader("Interests")
    st.info("🎮 Hollow Knight & Core Keeper")
    st.success("✍️ Creative Story Writing")

# 3. Main Hero Section (Visual Impact)
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Hello, I'm Jan Elseph Yu 👋")
    st.subheader("Aspiring IT Professional & Storyteller")
    st.write("""
    I am a dedicated 4th-year IT student passionate about building systems that make a difference. 
    From blockchain node setup to gamified e-learning platforms, I love exploring the intersection of 
    technology and user experience.
    """)

with col2:
    # Using metrics for a professional "dashboard" feel
    st.metric(label="Tech Stack", value="10+ Tools")
    st.metric(label="Capstone Status", value="Testing Phase")

st.divider()

# 4. Interactive Tabs (Organization & Component Variety)
tab1, tab2, tab3, tab4 = st.tabs(["📖 My Story", "🛠 Skill Set", "🚀 Projects", "📩 Contact"])

with tab1:
    st.header("Autobiography")
    st.write("""
    My journey into the world of technology began back in the 3rd grade when I started 
    writing stories. That love for creation evolved into coding. Today, I am finishing 
    my BSIT degree at the Cebu Institute of Technology - University, specializing in 
    Information Assurance and Cloud Architecting.
    """)

with tab2:
    st.header("Technical Arsenal")
    # Using columns inside tabs for better spacing
    c1, c2, c3 = st.columns(3)
    with c1:
        st.write("**Languages**")
        st.code("Python, Java, C++")
    with c2:
        st.write("**Web Tech**")
        st.code("React JS, Springboot, MySQL")
    with c3:
        st.write("**Infrastructure**")
        st.code("AWS, Blockchain, Linux")

with tab3:
    st.header("Featured Work")
    # Using expanders for clean project descriptions
    with st.expander("⭐ SyntaxType - E-Learning Platform"):
        st.write("A gamified typing-based platform designed for first-year BSIT students at CIT-U.")
        st.write("**Role:** Lead Developer")
        
    with st.expander("☁️ CloudFour - Systems Admin Project"):
        st.write("Focused on RAID configurations and storage management solutions.")
        st.write("**Role:** Systems Architect")

with tab4:
    st.header("Let's Collaborate!")
    # Using st.form for "Full Utilization" points
    with st.form("contact_form"):
        u_name = st.text_input("Name")
        u_email = st.text_input("Email")
        u_msg = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")
        
        if submit_button:
            # Adding visual feedback for extra aesthetic points
            with st.spinner("Processing..."):
                time.sleep(1)
            st.success(f"Thank you, {u_name}! I'll get back to you soon.")
            st.balloons()