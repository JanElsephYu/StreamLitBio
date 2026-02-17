import streamlit as st

# Aesthetic setup for bonus points
st.set_page_config(page_title="Jan Elseph Yu | Portfolio", page_icon="🎓", layout="wide")

# Sidebar for personal touches
with st.sidebar:
    st.title("Jan Elseph Yu")
    st.info("4th Year BSIT Student @ CIT-U")
    st.write("---")
    st.subheader("Interests")
    st.write("🎮 Hollow Knight & Core Keeper")
    st.write("✍️ Creative Writing")

# Tabs to organize content cleanly
tab1, tab2, tab3 = st.tabs(["📖 Autobiography", "🛠 Projects", "✉️ Contact"])

with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/200", caption="Jan Elseph Yu")
    with col2:
        st.header("My Story")
        st.write("I am a 4th-year BSIT student at the Cebu Institute of Technology - University. I have a passion for blockchain and systems administration.")

with tab2:
    st.header("Academic Projects")
    st.write("**SyntaxType:** A gamified typing platform for IT students.")
    st.write("**CloudFour:** Systems administration project on RAID storage.")
    st.write("---")
    st.subheader("Skills")
    st.write("`Python` `Java` `C++` `React JS` `MySQL` `Blockchain`")

with tab3:
    st.header("Get in Touch")
    with st.form("contact"):
        st.text_input("Name")
        st.text_area("Message")
        if st.form_submit_button("Submit"):
            st.balloons() # Interactive flair!
            st.success("Message 'sent'!")