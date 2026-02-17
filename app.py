import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Jan Elseph Yu | Professional Portfolio",
    page_icon="🎓",
    layout="wide",
)

# 2. Custom CSS for Animations (The "Aesthetic" Secret Sauce)
st.markdown("""
<style>
    /* Targeting all Streamlit buttons */
    .stButton>button {
        transition: all 0.3s ease; /* Smooth transition */
        border-radius: 10px;
        border: 2px solid #800000; /* CIT-U Maroon */
        background-color: white;
        color: #800000;
        font-weight: bold;
    }

    /* Hover Animation: Button grows and changes color */
    .stButton>button:hover {
        transform: scale(1.1); /* Grow 10% */
        background-color: #800000; /* Fill with Maroon */
        color: white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }

    /* Click Animation: Button shrinks slightly */
    .stButton>button:active {
        transform: scale(0.95);
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar for Quick Facts
with st.sidebar:
    # Use your profile image from GitHub
    st.image("profile.JPG", caption="Jan Elseph Yu")
    st.title("Contact Details")
    st.write("📧 janelsephyu@gmail.com")
    st.write("📍 Cebu City, Philippines")
    st.divider()
    st.write("**Course:** BSIT-4 @ CIT-U")

# 4. Hero Section
st.title("👨‍💻 Jan Elseph Yu")
st.subheader("BSIT Senior Student | Mobile Developer")
st.divider()

# 5. Navigation Tabs
tab1, tab2, tab3 = st.tabs(["👤 Personal Profile", "🚀 Featured Projects", "🎨 Skills & Hobbies"])

with tab1:
    col_text, col_metrics = st.columns([2, 1])
    
    with col_text:
        st.header("Autobiography")
        st.write(f"**Full Name:** Jan Elseph Yu")
        st.write(f"**Birthday:** January 11, 2001")
        st.write(f"**Age:** 25")
        st.write("""
        I am a 4th-year IT student at the Cebu Institute of Technology - University. 
        My academic focus is on developing mobile and web systems that solve real-world 
        problems, ranging from indoor positioning to scholarship management.
        """)
        
    with col_metrics:
        st.metric(label="Graduation Year", value="2026")
        st.metric(label="OJT Status", value="In Progress")

with tab2:
    st.header("Technical Projects")
    
    # GIPS Project
    with st.expander("⭐ GIPS (Grocery Indoor Positioning System)"):
        st.write("""
        An Android application designed to streamline the grocery shopping experience. 
        - **Indoor Positioning:** Locate items specifically within a store.
        - **Shopping Management:** Manage a digital cart and check item availability.
        """)
    
    # NASMS/SEMS Project
    with st.expander("🎓 NASMS (Non-Academic Scholar Management System)"):
        st.write("""
        A mobile solution for Cebu Institute of Technology - University scholarship applicants.
        - **Documentation:** In-app PDF conversion and document uploading for Grades and School IDs.
        - **User Portal:** Features landing pages, account creation, and profile displays.
        """)

with tab3:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Hobbies")
        st.info("🎨 Drawing")
        st.success("✍️ Writing Stories")
    
    with c2:
        st.subheader("Proficiency")
        st.progress(85, text="Android Development (Java)")
        st.progress(70, text="System Admin (Linux)")

# 6. Interactive Button with Animation
st.divider()
st.write("### Interactive Experience")
st.write("Try hovering over the button below to see the animation!")

if st.button("Celebrate My Journey!"):
    st.balloons()
    st.snow()
    st.toast("Submission Ready!", icon='🎉')

st.caption("© 2026 | Built for CIT-U IT Portfolio Assignment")