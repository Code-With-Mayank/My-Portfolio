from pathlib import Path
import  json
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie


#----- PATH SETINGS ----------------#
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Mayank_Jha_Resume.pdf"
profile_pic = current_dir / "assets" / "Profile Photo.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "MY-PORTFOLIO"
PAGE_ICON = ":computer:"
DESCRIPTION = """
“An enthusiastic young mind and a hard-working individual with knowledge in Full Stack Web Development and Data Analysis from India.
My passion for software lies with dreaming up ideas and making them come true with elegant interfaces.
I take great care in the performance, architecture, and code quality of the things I build.
I am also an open-source enthusiast and maintainer.
I learned a lot from the open-source community and I love how collaboration and knowledge sharing happened through open-source.
"""
EMAIL = "jhamayank043@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mayank-jha-9132b8214/",
    "GitHub": "https://github.com/Code-With-Mayank",
    "FaceBook": "https://www.facebook.com/profile.php?id=100024163296583",
    "Instagram": "https://www.instagram.com/mj_mayankjha/",
}
PROJECTS = {
    "🗂️ Agro_Sense - A cutting-edge agricultural technology platform powered by state-of-the-art machine learning algorithms. Our mission? To empower farmers worldwide with data-driven insights and recommendations, revolutionizing the way crops are grown.": "https://agro-sense-ml-cza4.onrender.com/",
    "🗂️ NIGHT_OWL - Movies and TV Series Searching App. An Entertainment Hub Website designed using React to fetch all movie details": "https://night-owl-movie-series-searching.vercel.app/",
    "🗂️ SMART-SALES - The Website is a comprehensive online platform designed to empower businesses with powerful insights and data-driven decision-making capabilities. This project aims to provide a user-friendly interface for analysing sales data, identifying trends, and making informed business choices.":"https://smart-sales-eda-application.streamlit.app/",
    "🗂️ VEGAN_BRO’S- An Online E-Commerce website where user can buy fresh vegetables and all products of their choice. Technologies used: MERN STACK, Html, CSS, Bootstrap ": "https://github.com/sayokghosh/VeganBros/tree/main",
    "🗂️ HOTEL MANGEMENT SYSTEM - A GUI Application.This is a User Interface project with Tkinter module of Python. It can be used by any Hotel Chain Owners to track and manage of their Customers and Booking Status of their Hotel.Technologies used: Python, Tkinter, Pillow, MySQL ": "https://www.linkedin.com/posts/mayank-jha-9132b8214_python-tkinter-mysql-activity-7086039198490607616-RaOS?utm_source=share&utm_medium=member_desktop",
    "🗂️ FOOD SERVER - A Simple Python's Tkinter GUI Interface for ordering foods and displaying related price details.": "https://www.linkedin.com/posts/mayank-jha-9132b8214_1stproject-tkinter-foodorderingsystem-activity-6964563005153914880-v5U0?utm_source=share&utm_medium=member_desktop",
    "🗂️ POWER-BI DASHBOARD- It is a beautiful dashboard created using Power BI of Microsoft for the Sales analysis of an potential Ecommerce Shop Owner.": "https://github.com/Code-With-Mayank/MJ_Sales_Analysis_Dashboard",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# ------------- Animations ----------
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return  json.load(f)

# --- Main SECTION ---
col1, col2, col3 = st.columns(3, gap="small")
with col1:
    st.image(profile_pic, width=260)
with col3:
    lottie_hello = load_lottiefile("lottiefiles/Hello animation.json")
    st_lottie(
        lottie_hello,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height =None,
        width=None,
        key=None,
    )
    lottie_hi = load_lottiefile("lottiefiles/Robo Hi.json")
    st_lottie(
        lottie_hi,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height =None,
        width=None,
        key=None,
    )
with col2:
    st.title(":red[MAYANK JHA]")
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫 :red[**EMAIL** :] ", EMAIL)

# --- SOCIAL LINKS ---
st.write('📲:red[Connect With Me :]👇\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# --- EDUCATION & QUALIFICATIONS ---
st.write('\n')
st.subheader(":green[EDUCATION AND QUALIFICATIONS]")
st.write("---")
col21, col22 = st.columns(2, gap="small")
with col21:
    st.write(
    """
- 🔭 I’m currently studying Computer Science and Engineering from :red[B.P. PODDAR INSTITUTE OF MANGEMENT AND TECHNOLOGY.]
- ⚡ I have completed my schooling from :red[SWAMI PRANABANANDA VIDYAPITH.]
- 🌱 Learning MERN STACK in JAVASCRIPT, STREAMLIT, PANDAS, BOOTSTRAP AND DJANGO.
- 💬 Good understanding of TKINTER, PYTHON, HTML, CSS, OOPS, DBMS along with WEB DEVELOPMENT and EXPLORATORY DATA ANALYSIS.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)
with col22:
    lottie_hello = load_lottiefile("lottiefiles/Education.json")
    st_lottie(
        lottie_hello,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height = 350,
        width= 600,
        key=None,
    )

# --- SKILLS ---
st.write('\n')
st.subheader(":green[SKILLS]")
st.write("---")
col11, col12 = st.columns(2, gap="small")
with col11:
    st.write(
    """
- 🌐 WEB TECHNOLOGIES :   React, Node, Express, Html, CSS, Bootstrap, Tkinter, Streamlit. 
 
 
- 👩‍💻 PROGRAMMING LANGUAGES :    Python (Moderate, Pandas), SQL, C, JAVASCRIPT


- 📊 DATA VISUALIZATION :   PowerBi, MS Excel, Plotly, Matplotlib


- 📚 CONCEPTS : DSA, OOPS, DBMS, git, GitHub 


- 🗄️ DATABASES :   PostgreSQL, MongoDB, MySQL

"""
)

with col12:
    lottie_hello = load_lottiefile("lottiefiles/Skills.json")
    st_lottie(
        lottie_hello,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height = 350,
        width= 600,
        key=None,
    )

# ------ CERTIFICATES AND ACCOMPLISHMENTS ----------
st.write('\n')
st.subheader(":green[CERTIFICATES AND ACCOMPLISHMENTS]")
st.write("---")
col31, col32 = st.columns(2, gap="small")
with col31:
        # --- Certifications
    st.write("🚧", "CERTIFICATIONS : ")
    st.write(
        """
    - ► FS-Web Development (MERN) Certificate from :red[**ARDENT**]
    - ► Summer Industrial Training Certificate from :red[**ARDENT**]
    - ► JavaScript with HTML and CSS from :red[**UDEMY**]
    - ► Organiser Certificate of College Tech-Fest :red[**TECHSTORM**]
    - ► Basic Python Programming from :red[**COURSERA**]
    """
    )

    # --- ACCOMPLISHMENTS
    st.write('\n')
    st.write("🚧", "ACCOMPLISHMENTS : ")
    st.write(
        """
    - ► Runner Up at Intra college Quiz Competition :red[**AbhiGyaan**], of BPPIMT Literary Forum
    - ► Been Campus Ambassador for :red[**Ardent Infotech Pvt. Ltd**] and :red[**TechLearn Education Platform**].
    - ► Tech-Fest Coordinator and PR | Sponsor Lead for the College Fest -- :red[**Elixir'23**] and :red[**Techstorm 2.23**].
    """
    )
with col32:
    lottie_hello = load_lottiefile("lottiefiles/Certifiactions.json")
    st_lottie(
        lottie_hello,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height = 350,
        width= 600,
        key=None,
    )

# --- Projects  ---
st.write('\n')
st.subheader(":green[PROJECTS]")
st.write("---")
col41, col42 = st.columns(2, gap="small")
with col41:
    for project, link in PROJECTS.items():
        st.write(f"[{project}]({link})")
with col42:
    lottie_hello = load_lottiefile("lottiefiles/Projects.json")
    st_lottie(
        lottie_hello,
        speed = 1,
        reverse=False,
        loop=True,
        quality="high",
        height = 550,
        width= 600,
        key=None,
    )



    
