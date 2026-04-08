import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Renewable Energy Dashboard", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Background Image */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1508791290064-c27cc1ef7a9a?q=80&w=1174&auto=format&fit=crop");
    background-size: cover;
    background-attachment: fixed;
}

/* Dark overlay for readability */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.35);
    z-index: -1;
}

/* Title */
.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #ffffff;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
}

/* Glass Cards */
.card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);

    padding: 20px;
    border-radius: 20px;
    text-align: center;

    border: 1px solid rgba(255, 255, 255, 0.3);

    box-shadow: 0 8px 32px rgba(0,0,0,0.2);

    transition: 0.3s ease;
}

/* Hover effect */
.card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 12px 40px rgba(0,0,0,0.4);
}

/* Link styling */
.card h4 a {
    color: #ffffff !important;
    text-decoration: none;
    text-shadow: 1px 1px 6px rgba(0,0,0,0.7);
}

.card h4 a:hover {
    text-decoration: underline;
}

/* Subtitle text */
.card p {
    color: #f1f1f1;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: rgba(232, 245, 233, 0.95);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<p class="title">🌱 Renewable Energy Management</p>', unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:white;'>🌍 Clean Energy | Sustainable Future | Smart Solutions</h3>", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=120)

st.sidebar.header("👤 Student Profile")
st.sidebar.write("**Name:** Pranav Patil")
st.sidebar.write("**Roll No:** 22108A0038")
st.sidebar.write("**Subject:** Renewable Energy Management")

st.sidebar.markdown("---")

st.sidebar.header("👨‍🏫 Professor")
st.sidebar.write("Prof. Rakshak Sood")
st.sidebar.write("Department of Electronics and Computer Science")

# ---------------- ASSIGNMENTS ----------------
st.markdown("<h2 style='color:white;'>📂 Assignments</h2>", unsafe_allow_html=True)

assignments = {
    "🌍 1. National Energy Scenario": "https://viteduin59337-my.sharepoint.com/:b:/g/personal/pranav_patil22_vit_edu_in/IQAqPWjrZvYLR4k0LpUhYjJNAdsIHbg6zZVINvlzi-baTew?e=U1tfFQ",
    "🌬️ 2. Types of Renewable Energy": "https://viteduin59337-my.sharepoint.com/:b:/g/personal/pranav_patil22_vit_edu_in/IQAh9DRWICUpT5Jb69RPAmL8AYWeGR4AMQR4mvPXfzBOsWc?e=4EG3Mt",
    "🌞 3. Solar Thermal Energy": "https://viteduin59337-my.sharepoint.com/:b:/g/personal/pranav_patil22_vit_edu_in/IQD8YvLLKvXIQ7ZA_GkAlWajAQRJQTnRLl_E6bGsPfrYFp4?e=mwS1DS",
    "🏭 4. Energy Utility Dashboard": "https://vit-spark-harmony.lovable.app/",
    "💧 5. Biomass, Hydro & Geothermal": "https://viteduin59337-my.sharepoint.com/:b:/g/personal/pranav_patil22_vit_edu_in/IQD9QLg76dhpSbEZQkUxvWNoAc2QuJ5axRcOydnCFr6U6e0?e=Kdpwai",
    "🌍 6. Smart Poster - Solar Plant": "https://viteduin59337-my.sharepoint.com/:b:/g/personal/pranav_patil22_vit_edu_in/IQAfXmDIT18RQ6lcmi3NrQ73ASzkj0xss8giWiS_HWTRQu8?e=Gq0fMo",
    "🔋 7. Era of Energy Disruption": "https://notebooklm.google.com/notebook/6c17b708-bee3-4cd7-816c-3e9ec21c7609?artifactId=8c84318b-ddff-4eb5-87d6-8a3e22e6bddf&classId=29f5a994-116f-44ab-a2a2-f2f4bc03067a&assignmentId=c34ee5fb-fa17-4645-9d3d-bd1faabdb96e&submissionId=01ac8c41-5d74-8a0f-0339-2a0257cd8590&pli=1&authuser=1&pageId=none",
    "🌿 8. IEEE Research Paper": "https://viteduin59337-my.sharepoint.com/:b:/g/personal/pranav_patil22_vit_edu_in/IQCLbIlq8JafQ5Q5tCBmkaYiAV1bSMJ0Wd50Ghs-0LFE9lQ?e=o0z6Nn",
    "📊 Report": "https://viteduin59337-my.sharepoint.com/:i:/g/personal/pranav_patil22_vit_edu_in/IQBdWCDlpGNgQLFM30yBMogtAd4eHrJYqyMP7G1_DaCq2-0?e=hyzHTW",
}

cols = st.columns(3)

for i, (title, link) in enumerate(assignments.items()):
    with cols[i % 3]:
        st.markdown(f"""
        <div class='card'>
            <h4>
                <a href="{link}" target="_blank">
                    {title}
                </a>
            </h4>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("<h4 style='text-align:center; color:white;'>🌱 Designed for Renewable Energy Management</h4>", unsafe_allow_html=True)