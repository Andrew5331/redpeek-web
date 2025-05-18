import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Red Peek", layout="centered", page_icon="🕹️")

# Cargar y mostrar la imagen de portada
portada = Image.open("Portada.jpg")
st.image(portada, use_column_width=True)

# Título y tagline
st.title("Red Peek")
st.markdown("### *La princesa ha caído, ¿caerás tú también?*")

# Secciones de contenido
st.header("🎮 Sinopsis")
st.write("""
En las tierras olvidadas de Red Peek, donde la niebla cubre las montañas y las leyendas se murmuran en las tabernas, un antiguo mal ha despertado...

Solo un caballero, armado con valor y una voluntad templada por el sufrimiento, se atreve a descender. Las criptas están vivas, los pasajes cambian y las bestias acechan.
""")

st.header("🕹️ Mecánicas del Juego")
st.markdown("""
- RPG lineal en 2D con estética pixel art medieval  
- Modo campaña narrativo y modo arcade tipo survival  
- Hack & Slash con evolución del personaje  
- Controles táctiles optimizados para móviles
""")

st.header("👥 Personajes")
st.markdown("""
- **🛡️ El Caballero**: campesino con pasado humilde, ahora caballero. Sus emociones se revelan a través de páginas ocultas.  
- **👑 El Rey de las Profundidades**: antagonista solitario que busca un rival digno.  
- **👸 Olivia, la Princesa**: figura que guía con notas y recuerdos durante la aventura.
""")

st.header("👾 Enemigos")
st.markdown("""
- **No-muertos**: algunos conservan humanidad.  
- **Duendes**: cobardes y escurridizos.  
- **Trolls**: grandes, salvajes y poderosos.
""")

st.header("🌍 Mundo del Juego")
st.write("""
Ambientado en el Monte Coladi. Las mazmorras varían entre piedra, agua, veneno y fuego, hasta llegar al trono del Rey, un coliseo oscuro y solemne.
""")

st.header("📱 Público y Plataforma")
st.markdown("""
- Público: mayores de 10 años  
- Plataformas: Android e iOS  
- Ideal para partidas cortas o competitivas
""")

st.header("💰 Monetización")
st.markdown("""
- Microtransacciones opcionales (armas, vidas)  
- Todo también obtenible con oro dentro del juego
""")

# Footer
st.markdown("---")
st.markdown("Red Peek © 2025 | Andrés Ramos, Jorge Perico, Daniela Mayorga")
