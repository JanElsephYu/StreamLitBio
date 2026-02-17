import streamlit as st

# 1. Page Setup for Professionalism
st.set_page_config(
    page_title="Jan Elseph Yu | Academic Portfolio",
    page_icon="🎓",
    layout="wide",
)

# 2. Hero Section: Header & Branding
# Using columns to create a clean, modern header
col1, col2 = st.columns([3, 1])

with col1:
    st.title("Jan Elseph Yu")
    st.subheader("Bachelor of Science in Information Technology")
    st.write("📍 **Cebu Institute of Technology - University**")
    st.write("Focus: Systems Administration & Blockchain Technology")

with col2:
    # A professional metric to show academic standing
    st.metric(label="Current Status", value="4th Year Student")

st.divider()

# 3. Main Navigation using Tabs (Aesthetic & Organized)
tab1, tab2, tab3 = st.tabs(["📖 Autobiography", "🚀 Technical Projects", "🛠 Skills & Certifications"])

with tab1:
    st.header("My Academic Journey")
    # Using columns for a more visual layout than just text
    left_co, right_co = st.columns(2)
    
    with left_co:
        st.write("### Background")
        # [Placeholder: Add your specific personal background story here]
        st.write("""
        I am currently a senior IT student in Cebu City, balancing rigorous academic 
        coursework with hands-on technical training. My interest in technology 
        stems from a lifelong passion for creating and building systems.
        """)
        
    with right_co:
        st.write("### Current Focus")
        st.info("Currently undergoing **On-the-Job Training (OJT)** to bridge the gap between classroom theory and industry practice.")
        st.write("Projected Graduation: 2026")

with tab2:
    st.header("Academic Portfolio")
    # Using Expanders for "Full Utilization" of components
    with st.expander("⭐ SyntaxType: Gamified E-Learning"):
        st.write("A specialized platform developed for first-year BSIT students to improve typing proficiency within a technical context.")
        st.write("**Tech Stack:** [Add specific technologies used]")
        
    with st.expander("🛡️ CloudFour: Systems Admin Project"):
        st.write("A group project focused on managing storage solutions and RAID configurations for enterprise-level systems.")
        
    with st.expander("🔗 Blockchain Research & Development"):
        st.write("Handwritten research and practical node setup involving the Linux environment and Cardano blockchain.")

with tab3:
    st.header("Competencies")
    
    # Progress bars add a nice visual touch to represent skill levels
    st.write("Programming Proficiency")
    st.progress(85, text="Java & C++")
    st.progress(70, text="React JS & Web Development")
    st.progress(60, text="Cloud Architecting (AWS Academy)")
    
    st.divider()
    
    # Using a professional-looking 'Success' box for certifications
    st.subheader("Certifications & Courses")
    st.success("✅ AWS Academy Cloud Architecting")
    st.success("✅ Introduction to Blockchain (CSIT360)")

# 4. Footer Interactivity
st.divider()
if st.button("Celebrate Completion!"):
    st.balloons()
    st.toast("Portfolio Successfully Loaded!", icon='🎉')

# Footer text
st.caption("Developed by Jan Elseph Yu | © 2026 Academic Portfolio Assignment")