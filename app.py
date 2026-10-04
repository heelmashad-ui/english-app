import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Learn English | تعلم الإنجليزية", page_icon="🎓", layout="wide")

# 2. Custom CSS for Bilingual Display and Styling
st.markdown("""
<style>
    .arabic-text { font-family: 'Arial', sans-serif; text-align: right; direction: rtl; color: #2E86C1; font-size: 1.2rem;}
    .english-text { font-family: 'sans-serif'; text-align: left; font-size: 1.2rem; font-weight: bold;}
    .vocab-card { background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);}
    .dialogue-box { background-color: #ffffff; padding: 15px; border-left: 5px solid #4CAF50; border-radius: 5px; margin-bottom: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
</style>
""", unsafe_allow_html=True)

# 3. Lesson Database (Curriculum)
# You can easily change the YouTube links to your own channel's videos!
curriculum = {
    "Beginner (مبتدئ)": {
        "Greetings & Introductions (التحيات والتعارف)": {
            "youtube_url": "https://www.youtube.com/watch?v=F_Riqjdh2oM", 
            "image": "https://images.unsplash.com/photo-1577563908411-5077b6dc7624?auto=format&fit=crop&w=600&q=80",
            "vocab": [
                {"eng": "Hello", "ar": "مرحباً / أهلاً"},
                {"eng": "How are you?", "ar": "كيف حالك؟"},
                {"eng": "Nice to meet you", "ar": "سعدت بلقائك"}
            ],
            "dialogue": [
                {"speaker": "Ahmed", "eng": "Hello! My name is Ahmed.", "ar": "مرحباً! اسمي أحمد."},
                {"speaker": "Sarah", "eng": "Hi Ahmed, I am Sarah. How are you?", "ar": "أهلاً أحمد، أنا سارة. كيف حالك؟"},
                {"speaker": "Ahmed", "eng": "I am fine, thank you. Nice to meet you.", "ar": "أنا بخير، شكراً لك. سعدت بلقائك."}
            ]
        },
        "At the Cafe (في المقهى)": {
            "youtube_url": "https://www.youtube.com/watch?v=BgJwGrmELv8",
            "image": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=600&q=80",
            "vocab": [
                {"eng": "Coffee", "ar": "قهوة"},
                {"eng": "Water", "ar": "ماء"},
                {"eng": "How much?", "ar": "بكم؟ (ما السعر؟)"}
            ],
            "dialogue": [
                {"speaker": "Customer", "eng": "I would like a coffee, please.", "ar": "أريد قهوة من فضلك."},
                {"speaker": "Barista", "eng": "Sure. That is 3 dollars.", "ar": "بالتأكيد. السعر 3 دولارات."}
            ]
        }
    },
    "Intermediate (متوسط)": {
        "Job Interview (مقابلة عمل)": {
            "youtube_url": "https://www.youtube.com/watch?v=HG68Ymazo18",
            "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=600&q=80",
            "vocab": [
                {"eng": "Experience", "ar": "خبرة"},
                {"eng": "Skills", "ar": "مهارات"},
                {"eng": "Strengths", "ar": "نقاط القوة"}
            ],
            "dialogue": [
                {"speaker": "Manager", "eng": "Tell me about your previous experience.", "ar": "أخبرني عن خبرتك السابقة."},
                {"speaker": "Applicant", "eng": "I worked as a teacher for three years.", "ar": "عملت كمعلم لمدة ثلاث سنوات."}
            ]
        }
    },
    "Advanced (متقدم)": {
        "Business Strategy (استراتيجية العمل)": {
            "youtube_url": "https://www.youtube.com/watch?v=1mHjMNZZvFo",
            "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=600&q=80",
            "vocab": [
                {"eng": "Revenue", "ar": "إيرادات"},
                {"eng": "Optimization", "ar": "تحسين / تطوير"},
                {"eng": "Stakeholders", "ar": "أصحاب المصلحة / المساهمين"}
            ],
            "dialogue": [
                {"speaker": "CEO", "eng": "We need to optimize our revenue streams.", "ar": "نحتاج إلى تحسين مصادر إيراداتنا."},
                {"speaker": "Director", "eng": "Agreed. I will brief the stakeholders tomorrow.", "ar": "أتفق معك. سأقوم بإطلاع أصحاب المصلحة غداً."}
            ]
        }
    }
}

# 4. Sidebar Navigation
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=600&q=80", caption="Keep Learning! استمر في التعلم")
    st.title("📚 Course Menu")
    
    # Select Level
    selected_level = st.radio("Choose your level (اختر مستواك):", list(curriculum.keys()))
    
    # Select Topic based on Level
    topics = list(curriculum[selected_level].keys())
    selected_topic = st.selectbox("Choose a lesson (اختر درساً):", topics)

# 5. Main App Content
lesson_data = curriculum[selected_level][selected_topic]

# Header
st.markdown(f"<h1 style='text-align: center; color: #2C3E50;'>{selected_topic}</h1>", unsafe_allow_html=True)
st.markdown("---")

# Video & Image Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📺 Watch & Listen (شاهد واستمع)")
    # Embed YouTube Video
    st.video(lesson_data["youtube_url"])
    st.caption("Watch the video above, then practice with the vocabulary and conversation below.")

with col2:
    st.subheader("🖼️ Visual Context (صورة توضيحية)")
    # Context Picture
    st.image(lesson_data["image"], use_container_width=True, caption="Lesson Context")
    
    # Vocabulary Section
    st.subheader("📖 Vocabulary (المفردات)")
    for word in lesson_data["vocab"]:
        st.markdown(f"""
        <div class="vocab-card">
            <span class="english-text">{word['eng']}</span> <br>
            <span class="arabic-text" style="display:block; margin-top:5px;">{word['ar']}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Conversation Practice Section
st.subheader("💬 Conversation Practice (ممارسة المحادثة)")
st.info("💡 **Tip:** Try reading the English part out loud, then check the Arabic translation to make sure you understand.")

for line in lesson_data["dialogue"]:
    st.markdown(f"""
    <div class="dialogue-box">
        <p style="color: gray; font-size: 0.9rem; margin-bottom: 2px;"><b>{line['speaker']}</b></p>
        <p class="english-text">{line['eng']}</p>
        <p class="arabic-text">{line['ar']}</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Designed for Arabic speakers learning English 🌍 مصمم للناطقين بالعربية لتعلم الإنجليزية</p>", unsafe_allow_html=True)
