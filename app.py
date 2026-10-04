import streamlit as st

# 1. Page Configuration & Channel Branding
st.set_page_config(
    page_title="Learn Arabic English Channel", 
    page_icon="📺", 
    layout="wide"
)

# 2. Custom CSS for Bilingual Display
st.markdown("""
<style>
    .arabic-text { font-family: 'Arial', sans-serif; text-align: right; direction: rtl; color: #D32F2F; font-size: 1.3rem; font-weight: bold;}
    .english-text { font-family: 'sans-serif'; text-align: left; font-size: 1.2rem; font-weight: bold; color: #1E88E5;}
    .vocab-card { background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 4px solid #1E88E5; border-right: 4px solid #D32F2F; box-shadow: 0 2px 4px rgba(0,0,0,0.05);}
    .dialogue-box { background-color: #ffffff; padding: 15px; border-radius: 5px; margin-bottom: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
    .speaker-name { color: gray; font-size: 0.9rem; margin-bottom: 2px; font-weight: bold; text-transform: uppercase;}
</style>
""", unsafe_allow_html=True)

# 3. Channel Curriculum Database
# REPLACE the 'youtube_url' links below with the links to your own channel's videos!
# Make sure your YouTube videos have "Allow embedding" turned ON in YouTube Studio.
curriculum = {
    "Level 1: Beginners (المستوى الأول: مبتدئ)": {
        "Lesson 1: Greetings (الدرس الأول: التحيات)": {
            "youtube_url": "https://www.youtube.com/watch?v=juKd26qkNAw", # Replace with YOUR video link
            "image": "https://images.unsplash.com/photo-1577563908411-5077b6dc7624?auto=format&fit=crop&w=600&q=80",
            "vocab": [
                {"eng": "Good morning", "ar": "صباح الخير"},
                {"eng": "How are you doing?", "ar": "كيف حالك؟"},
                {"eng": "See you later", "ar": "أراك لاحقاً"}
            ],
            "dialogue": [
                {"speaker": "Teacher (المعلم)", "eng": "Good morning! Welcome to the Learn Arabic English channel.", "ar": "صباح الخير! مرحباً بكم في قناة تعلم العربية والإنجليزية."},
                {"speaker": "Student (الطالب)", "eng": "Good morning! I am ready to learn.", "ar": "صباح الخير! أنا مستعد للتعلم."}
            ]
        },
        "Lesson 2: At the Restaurant (في المطعم)": {
            "youtube_url": "https://www.youtube.com/watch?v=BgJwGrmELv8", # Replace with YOUR video link
            "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=600&q=80",
            "vocab": [
                {"eng": "Menu", "ar": "قائمة الطعام"},
                {"eng": "Delicious", "ar": "لذيذ"},
                {"eng": "The bill, please", "ar": "الفاتورة من فضلك"}
            ],
            "dialogue": [
                {"speaker": "Waiter", "eng": "Are you ready to order?", "ar": "هل أنت مستعد لطلب الطعام؟"},
                {"speaker": "Customer", "eng": "Yes, I would like chicken and rice, please.", "ar": "نعم، أريد دجاج وأرز من فضلك."}
            ]
        }
    },
    "Level 2: Intermediate (المستوى الثاني: متوسط)": {
        "Lesson 3: Travel & Airport (السفر والمطار)": {
            "youtube_url": "https://www.youtube.com/watch?v=HG68Ymazo18", # Replace with YOUR video link
            "image": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=600&q=80",
            "vocab": [
                {"eng": "Passport", "ar": "جواز سفر"},
                {"eng": "Flight", "ar": "رحلة طيران"},
                {"eng": "Luggage", "ar": "أمتعة / حقائب"}
            ],
            "dialogue": [
                {"speaker": "Officer", "eng": "Can I see your passport and ticket, please?", "ar": "هل يمكنني رؤية جواز سفرك وتذكرتك من فضلك؟"},
                {"speaker": "Traveler", "eng": "Here you go. I have two bags to check in.", "ar": "تفضل. لدي حقيبتان لتسجيلهما."}
            ]
        }
    }
}

# 4. Sidebar: Channel Branding & Navigation
with st.sidebar:
    # Official Channel Header
    st.markdown("<h1 style='text-align: center; color: #D32F2F;'>📺 Learn Arabic English</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px;'>The official companion app for our YouTube Channel!</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.title("📚 Select a Lesson")
    
    # Navigation Menus
    selected_level = st.radio("Choose Level (اختر المستوى):", list(curriculum.keys()))
    
    topics = list(curriculum[selected_level].keys())
    selected_topic = st.selectbox("Choose Lesson (اختر الدرس):", topics)
    
    st.markdown("---")
    st.info("🔔 **Don't forget to subscribe** to 'Learn Arabic English' on YouTube for weekly lessons!")

# 5. Main Content Area
lesson_data = curriculum[selected_level][selected_topic]

# Lesson Title
st.markdown(f"<h1 style='text-align: center; color: #2C3E50;'>{selected_topic}</h1>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([2, 1])

# Left Column: YouTube Video
with col1:
    st.subheader("📺 Watch the Channel Lesson (شاهد درس القناة)")
    
    # This safely embeds your YouTube video
    st.video(lesson_data["youtube_url"])
    st.caption(f"If the video doesn't load, [click here to watch it on YouTube]({lesson_data['youtube_url']})")

# Right Column: Visuals & Vocabulary
with col2:
    st.image(lesson_data["image"], use_container_width=True, caption="Lesson Context")
    
    st.subheader("📖 Key Vocabulary (أهم المفردات)")
    for word in lesson_data["vocab"]:
        st.markdown(f"""
        <div class="vocab-card">
            <span class="english-text">{word['eng']}</span> <br>
            <span class="arabic-text" style="display:block; margin-top:5px;">{word['ar']}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Bottom Section: Conversation Practice
st.subheader("💬 Practice the Conversation (تدرب على المحادثة)")
st.write("Read the English out loud, then check the Arabic translation below it.")

for line in lesson_data["dialogue"]:
    st.markdown(f"""
    <div class="dialogue-box">
        <p class="speaker-name">{line['speaker']}</p>
        <p class="english-text">{line['eng']}</p>
        <p class="arabic-text">{line['ar']}</p>
    </div>
    """, unsafe_allow_html=True)

# App Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 Learn Arabic English YouTube Channel. Keep practicing! استمر في التدريب!</p>", unsafe_allow_html=True)
