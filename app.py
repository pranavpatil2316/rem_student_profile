import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Renewable Energy Dashboard", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Full page background */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1509395176047-4a66953fd231");
    background-size: cover;
    background-attachment: fixed;
}

/* Overlay for readability */
.main {
    background-color: rgba(255, 255, 255, 0.9);
    padding: 20px;
    border-radius: 15px;
}

/* Title */
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #1b5e20;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.95);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    transition: 0.3s;
}
.card:hover {
    transform: scale(1.05);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #e8f5e9;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<p class="title">🌱 Renewable Energy Management</p>', unsafe_allow_html=True)

st.markdown("### 🌍 Clean Energy | Sustainable Future | Smart Solutions")

# ---------------- SIDEBAR ----------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=120)

st.sidebar.header("👤 Student Profile")
st.sidebar.write("**Name:** Pranav Patil")
st.sidebar.write("**Roll No:** 22108A0038")
st.sidebar.write("**Subject:** Renewable Energy Management")

st.sidebar.markdown("---")

st.sidebar.header("👨‍🏫 Professor")
st.sidebar.write("Prof. XYZ")
st.sidebar.write("Department of Energy Engineering")

# ---------------- HERO IMAGE ----------------
st.image("https://images.unsplash.com/photo-1466611653911-95081537e5b7", use_container_width=True)

# ---------------- ASSIGNMENTS ----------------
st.subheader("📂 Assignments")

assignments = {
    "🌞 Solar Energy Basics": "https://your-link-1",
    "🌬️ Wind Energy Analysis": "https://your-link-2",
    "💧 Hydropower Study": "https://your-link-3",
    "🌿 Biomass Energy": "https://your-link-4",
    "⚡ Energy Storage": "https://your-link-5",
    "🌍 Sustainability Report": "https://your-link-6",
    "🔋 Smart Grid": "https://your-link-7",
    "🏭 Energy Audit": "https://your-link-8",
    "📊 Final Report": "https://your-link-9",
}

cols = st.columns(3)

for i, (title, link) in enumerate(assignments.items()):
    with cols[i % 3]:
        st.markdown(f"<div class='card'><h4>{title}</h4></div>", unsafe_allow_html=True)
        if st.button("View Assignment", key=i):
            st.session_state["pdf"] = link

# ---------------- PDF VIEWER ----------------
if "pdf" in st.session_state:
    st.markdown("### 📄 Assignment Viewer")
    st.components.v1.iframe(st.session_state["pdf"], height=650)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("### 🌱 Designed for Renewable Energy Management")