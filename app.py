<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Portafolio Interfaces Multimodales</title>

  <style>

    *{
      margin:0;
      padding:0;
      box-sizing:border-box;
      font-family: 'Poppins', sans-serif;
    }

    body{
      background: linear-gradient(135deg,#f8e8ff,#e0c3fc,#c2e9fb);
      min-height:100vh;
      padding:40px;
      color:#2d1b4e;
    }

    h1{
      text-align:center;
      font-size:3rem;
      margin-bottom:10px;
    }

    .subtitle{
      text-align:center;
      margin-bottom:40px;
      font-size:1.1rem;
    }

    .container{
      display:grid;
      grid-template-columns:repeat(auto-fit,minmax(320px,1fr));
      gap:25px;
    }

    .card{
      background:rgba(255,255,255,0.75);
      backdrop-filter:blur(12px);
      border-radius:25px;
      padding:25px;
      box-shadow:0 8px 20px rgba(0,0,0,0.1);
      transition:0.3s;
    }

    .card:hover{
      transform:translateY(-5px) scale(1.01);
    }

    .card h2{
      margin-bottom:15px;
      color:#6a00f4;
    }

    .card p{
      margin-bottom:20px;
      color:#4b3f72;
    }

    .links{
      display:flex;
      flex-direction:column;
      gap:12px;
    }

    .links a{
      text-decoration:none;
      background:#9d4edd;
      color:white;
      padding:12px;
      border-radius:12px;
      text-align:center;
      transition:0.3s;
      font-weight:600;
    }

    .links a:hover{
      background:#7b2cbf;
    }

    footer{
      text-align:center;
      margin-top:50px;
      color:#5a4a75;
      font-size:0.95rem;
    }

  </style>
</head>

<body>

  <h1>✨ Portafolio Multimodal ✨</h1>

  <p class="subtitle">
    Sobrevivimos a Streamlit, OCR, NLP, MediaPipe y crisis emocionales con GitHub.
  </p>

  <div class="container">

    <!-- CLASE 6 -->
    <div class="card">

      <h2>📚 Clase 6</h2>

      <p>
        Primer contacto con Streamlit. 
        Hubo café, errores y probablemente lágrimas.
      </p>

      <div class="links">

        <a href="https://introo-zfwazup7wrvjuqbqbmczfl.streamlit.app/" target="_blank">
          🚀 Introducción
        </a>

        <a href="https://texto-a-audio-ale-ppvwbaurnr3mep2zh8anqn.streamlit.app/" target="_blank">
          🔊 Texto a Audio
        </a>

      </div>

    </div>

    <!-- CLASE 7 -->
    <div class="card">

      <h2>🌎 Clase 7</h2>

      <p>
        OCR, traducción y magia tecnológica digna de película sci-fi low budget.
      </p>

      <div class="links">

        <a href="https://traductoor-q4rqcerg82tfgk2ghmahpu.streamlit.app/" target="_blank">
          🌐 Traductor
        </a>

        <a href="https://ocr-audio-avfn8jneonbdegm2mvipto.streamlit.app/" target="_blank">
          🎧 OCR + Audio
        </a>

        <a href="https://jwrh4nyycm8pwyqjl3pddg.streamlit.app/" target="_blank">
          📸 VisionScan OCR
        </a>

      </div>

    </div>

    <!-- CLASE 8 -->
    <div class="card">

      <h2>🧠 Clase 8</h2>

      <p>
        NLP, sentimientos y análisis emocional.
        TextBlob leyendo traumas desde 2025.
      </p>

      <div class="links">

        <a href="https://wordcloud-ale-79ksrpzluvjdajhoveyqqm.streamlit.app/" target="_blank">
          ☁️ WordCloud
        </a>

        <a href="https://tfidf-demo-espanol-thhzrhhzhrvpx7fhyq5zcm.streamlit.app/" target="_blank">
          📊 TF-IDF
        </a>

        <a href="https://sentimenta-fw2zmndnyesdczxhsvygze.streamlit.app/" target="_blank">
          💜 Sentimenta
        </a>

        <a href="https://dpaudyyodkunjmeg6rpcex.streamlit.app/" target="_blank">
          🤖 NLP Dashboard
        </a>

      </div>

    </div>

    <!-- CLASE 9 -->
    <div class="card">

      <h2>👁️ Clase 9</h2>

      <p>
        Visión por computador porque claramente sufrir con Python no era suficiente.
      </p>

      <div class="links">

        <a href="https://yolov5-8hzpgrleyaixfoygjfwxvz.streamlit.app/" target="_blank">
          🎯 YOLOv5 Detector
        </a>

        <a href="https://yrhoftz8g3zqnca6elyu22.streamlit.app/" target="_blank">
          🧿 Computer Vision App
        </a>

      </div>

    </div>

  </div>

  <footer>
    ✨ Desarrollado por Ale • Interfaces Multimodales • Streamlit Survivor ✨
  </footer>

</body>
</html>
