import streamlit as st

st.set_page_config(
    page_title="Portafolio Multimodal",
    page_icon="✨",
    layout="wide"
)

# CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f3d9ff, #d0ebff);
}

.main {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 1rem;
    max-width: 95%;
}

.titulo {
    text-align: center;
    font-size: 70px;
    font-weight: 800;
    color: #2d1457;
    margin-bottom: 10px;
}

.subtitulo {
    text-align: center;
    font-size: 22px;
    color: #2d1457;
    margin-bottom: 50px;
}

.card {
    background-color: rgba(255,255,255,0.65);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    min-height: 480px;
}

.card-title {
    font-size: 26px;
    font-weight: bold;
    color: #6a00ff;
    margin-bottom: 20px;
}

.card-text {
    font-size: 17px;
    color: #311b5b;
    margin-bottom: 25px;
}

.link-btn {
    display: block;
    text-align: center;
    background: linear-gradient(90deg, #9d4edd, #9747ff);
    color: white !important;
    padding: 14px;
    border-radius: 16px;
    margin-top: 14px;
    text-decoration: none;
    font-size: 16px;
    font-weight: bold;
    transition: 0.3s;
}

.link-btn:hover {
    transform: scale(1.03);
    background: linear-gradient(90deg, #7b2cbf, #9d4edd);
}

.footer {
    text-align: center;
    margin-top: 35px;
    margin-bottom: 10px;
    color: #4b296b;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# TITULO
st.markdown("""
<div class='titulo'>
✨ Portafolio Multimodal ✨
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='subtitulo'>
Sobrevivimos a Streamlit, OCR, NLP y crisis emocionales con GitHub.
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

# CLASE 6
with col1:
    st.markdown("""
    <div class='card'>
        <div class='card-title'>📚 Clase 6</div>
        <div class='card-text'>
        Primer contacto con Streamlit. Mucho café y errores existenciales.
        </div>

        <a class="link-btn" href="https://introo-zfwazup7wrvjuqbqbmczfl.streamlit.app/" target="_blank">
        🚀 Introducción
        </a>

        <a class="link-btn" href="https://texto-a-audio-ale-ppvwbaurnr3mep2zh8anqn.streamlit.app/" target="_blank">
        🔊 Texto a Audio
        </a>

    </div>
    """, unsafe_allow_html=True)

# CLASE 7
with col2:
    st.markdown("""
    <div class='card'>
        <div class='card-title'>🌎 Clase 7</div>
        <div class='card-text'>
        OCR, traducción y magia tecnológica sospechosamente poderosa.
        </div>

        <a class="link-btn" href="https://traductoor-q4rqcerg82tfgk2ghmahpu.streamlit.app/" target="_blank">
        🌐 Traductor
        </a>

        <a class="link-btn" href="https://ocr-audio-avfn8jneonbdegm2mvipto.streamlit.app/" target="_blank">
        🎧 OCR + Audio
        </a>

        <a class="link-btn" href="https://jwrh4nyycm8pwyqjl3pddg.streamlit.app/" target="_blank">
        📸 VisionScan OCR
        </a>

    </div>
    """, unsafe_allow_html=True)

# CLASE 8
with col3:
    st.markdown("""
    <div class='card'>
        <div class='card-title'>🧠 Clase 8</div>
        <div class='card-text'>
        NLP, sentimientos y análisis emocional. TextBlob leyendo traumas desde temprano.
        </div>

        <a class="link-btn" href="https://wordcloud-ale-79ksrpzluvjdajhoveyqqm.streamlit.app/" target="_blank">
        ☁️ WordCloud
        </a>

        <a class="link-btn" href="https://tfidf-demo-espanol-thhzrhhzhrvpx7fhyq5zcm.streamlit.app/" target="_blank">
        📊 TF-IDF
        </a>

        <a class="link-btn" href="https://sentimenta-fw2zmndnyesdczxhsvygze.streamlit.app/" target="_blank">
        💜 Sentimenta
        </a>

        <a class="link-btn" href="https://dpaudyyodkunjmeg6rpcex.streamlit.app/" target="_blank">
        🤖 NLP Dashboard
        </a>

    </div>
    """, unsafe_allow_html=True)

# CLASE 9
with col4:
    st.markdown("""
    <div class='card'>
        <div class='card-title'>🎯 Clase 9</div>
        <div class='card-text'>
        Computer Vision entrando como protagonista del semestre.
        </div>

        <a class="link-btn" href="https://yolov5-8hzpgrleyaixfoygjfwxvz.streamlit.app/" target="_blank">
        👁️ YOLOv5
        </a>

        <a class="link-btn" href="https://yrhoftz8g3zqnca6elyu22.streamlit.app/" target="_blank">
        📦 Object Detection
        </a>

    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class='footer'>
✨ Desarrollado por Ale • Interfaces Multimodales • Streamlit Survivor ✨
</div>
""", unsafe_allow_html=True)
