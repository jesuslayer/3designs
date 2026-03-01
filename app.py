import streamlit as st

# ==============================
# Configuración principal
# ==============================
st.set_page_config(
    page_title="Portafolio de Jesús",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estado para animación simple de typing
if "typing_index" not in st.session_state:
    st.session_state.typing_index = 0

# Datos editables del portafolio
PROFILE = {
    "name": "Jesús",
    "profession": "Desarrollador Python & Creador de Experiencias Web",
    "bio": (
        "Soy Jesús, apasionado por construir productos digitales útiles y visualmente atractivos.\n"
        "Me enfoco en Python, automatización y desarrollo de interfaces modernas.\n"
        "Disfruto transformar ideas en aplicaciones reales con buen rendimiento.\n"
        "Actualmente estoy creando proyectos que combinan IA, datos y diseño interactivo."
    ),
    "email": "jesus@email.com",
    "github": "https://github.com/jesus38168195",
    "linkedin": "https://www.linkedin.com/in/jesus-dev/",
    "twitter": "https://x.com/jesus38168195",
    "instagram": "https://instagram.com/jesus.dev",
    "avatar": "https://images.unsplash.com/photo-1607746882042-944635dfe10e?q=80&w=800&auto=format&fit=crop",
}

PROJECTS = [
    {
        "title": "InsightBoard AI",
        "description": "Dashboard inteligente para analizar métricas de negocio con recomendaciones automáticas impulsadas por IA.",
        "tech": ["Python", "Streamlit", "Pandas", "OpenAI API"],
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200&auto=format&fit=crop",
        "demo": "https://example.com/demo-insightboard",
        "code": "https://github.com/jesus38168195/insightboard-ai",
    },
    {
        "title": "TaskFlow Pro",
        "description": "App de productividad colaborativa con tableros Kanban, recordatorios y reportes visuales en tiempo real.",
        "tech": ["FastAPI", "Streamlit", "PostgreSQL", "Docker"],
        "image": "https://images.unsplash.com/photo-1611224923853-80b023f02d71?q=80&w=1200&auto=format&fit=crop",
        "demo": "https://example.com/demo-taskflow",
        "code": "https://github.com/jesus38168195/taskflow-pro",
    },
    {
        "title": "VisionRetail",
        "description": "Sistema de visión por computadora para conteo de inventario y alertas de stock bajo para tiendas minoristas.",
        "tech": ["Python", "OpenCV", "YOLO", "SQLAlchemy"],
        "image": "https://images.unsplash.com/photo-1556740738-b6a63e27c4df?q=80&w=1200&auto=format&fit=crop",
        "demo": "https://example.com/demo-visionretail",
        "code": "https://github.com/jesus38168195/visionretail",
    },
    {
        "title": "CreatorPulse",
        "description": "Herramienta para creadores de contenido que consolida estadísticas de redes y sugiere mejores horarios de publicación.",
        "tech": ["Python", "APIs", "Plotly", "Streamlit"],
        "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1200&auto=format&fit=crop",
        "demo": "https://example.com/demo-creatorpulse",
        "code": "https://github.com/jesus38168195/creatorpulse",
    },
    {
        "title": "CodeMentor Bot",
        "description": "Asistente educativo que explica errores de código y propone rutas de aprendizaje personalizadas.",
        "tech": ["Python", "LLMs", "Streamlit", "SQLite"],
        "image": "https://images.unsplash.com/photo-1518773553398-650c184e0bb3?q=80&w=1200&auto=format&fit=crop",
        "demo": "https://example.com/demo-codementor",
        "code": "https://github.com/jesus38168195/codementor-bot",
    },
    {
        "title": "TravelLens",
        "description": "Galería interactiva de viajes con geolocalización y storytelling visual para compartir experiencias.",
        "tech": ["Streamlit", "Mapbox", "Pillow", "Pandas"],
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1200&auto=format&fit=crop",
        "demo": "https://example.com/demo-travellens",
        "code": "https://github.com/jesus38168195/travellens",
    },
]

GALLERY = [
    ("Ciudad nocturna", "https://images.unsplash.com/photo-1519501025264-65ba15a82390?q=80&w=900&auto=format&fit=crop"),
    ("Setup de trabajo", "https://images.unsplash.com/photo-1487014679447-9f8336841d58?q=80&w=900&auto=format&fit=crop"),
    ("Naturaleza", "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?q=80&w=900&auto=format&fit=crop"),
    ("Laptop & café", "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=900&auto=format&fit=crop"),
    ("Equipo creativo", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=900&auto=format&fit=crop"),
    ("Viaje", "https://images.unsplash.com/photo-1501785888041-af3ef285b470?q=80&w=900&auto=format&fit=crop"),
    ("Productividad", "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=900&auto=format&fit=crop"),
    ("Cámara", "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=900&auto=format&fit=crop"),
]

# ==============================
# Estilos CSS custom (hover + gradientes + responsive)
# ==============================
st.markdown(
    """
    <style>
    :root {
        --brand1: #7c3aed;
        --brand2: #06b6d4;
        --card-bg: rgba(255,255,255,.75);
    }

    @media (prefers-color-scheme: dark) {
        :root { --card-bg: rgba(20,20,24,.85); }
    }

    html { scroll-behavior: smooth; }

    .hero-wrap {
        padding: 2rem;
        border-radius: 24px;
        background: linear-gradient(130deg, rgba(124,58,237,.18), rgba(6,182,212,.16));
        backdrop-filter: blur(4px);
    }

    .hero-title {
        font-size: clamp(2rem, 4vw, 4rem);
        font-weight: 800;
        margin-bottom: .2rem;
    }

    .hero-sub {
        font-size: clamp(1rem, 2vw, 1.5rem);
        color: #94a3b8;
        min-height: 2rem;
    }

    .project-card {
        background: var(--card-bg);
        border: 1px solid rgba(148,163,184,.25);
        border-radius: 18px;
        padding: 1rem;
        margin-bottom: 1rem;
        transition: transform .25s ease, box-shadow .25s ease;
    }

    .project-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 18px 32px rgba(2,6,23,.15);
    }

    .chip {
        display: inline-block;
        padding: .25rem .6rem;
        margin: .2rem .25rem .2rem 0;
        border-radius: 999px;
        font-size: .8rem;
        background: linear-gradient(120deg, rgba(124,58,237,.18), rgba(6,182,212,.18));
        border: 1px solid rgba(148,163,184,.25);
    }

    .skill-tag {
        display: inline-block;
        margin: .2rem;
        padding: .35rem .65rem;
        border-radius: .7rem;
        background: rgba(124,58,237,.14);
        border: 1px solid rgba(124,58,237,.35);
        font-size: .85rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.title("🧭 Navegación")
    st.caption("Tema: automático según tu sistema (claro/oscuro)")
    st.markdown("- [Hero](#hero)\n- [Sobre mí](#sobre-mi)\n- [Proyectos](#proyectos-destacados)\n- [Galería](#galeria-de-imagenes)\n- [Snippets](#snippets-de-codigo)\n- [Skills](#skills)\n- [Contacto](#contacto)")
    st.divider()
    st.write("**Conecta conmigo**")
    st.link_button("GitHub", PROFILE["github"], use_container_width=True)
    st.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)
    st.link_button("X / Twitter", PROFILE["twitter"], use_container_width=True)
    st.link_button("Instagram", PROFILE["instagram"], use_container_width=True)

# ==============================
# 1) HERO
# ==============================
st.markdown("<a id='hero'></a>", unsafe_allow_html=True)
left, right = st.columns([1.3, 1], vertical_alignment="center")

with left:
    st.markdown("<div class='hero-wrap'>", unsafe_allow_html=True)
    st.markdown(f"<div class='hero-title'>Hola, soy {PROFILE['name']} 👋</div>", unsafe_allow_html=True)

    full_prof = PROFILE["profession"]
    idx = st.session_state.typing_index
    typed = full_prof[: idx + 1]
    st.markdown(f"<div class='hero-sub'>{typed}</div>", unsafe_allow_html=True)

    if st.session_state.typing_index < len(full_prof) - 1:
        st.session_state.typing_index += 1

    cta1, cta2, cta3 = st.columns(3)
    cta1.link_button("GitHub", PROFILE["github"], use_container_width=True)
    cta2.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)
    cta3.link_button("Contáctame", f"mailto:{PROFILE['email']}", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.image(PROFILE["avatar"], caption="Jesús - Perfil", use_container_width=True)

# ==============================
# 2) SOBRE MÍ
# ==============================
st.markdown("<a id='sobre-mi'></a>", unsafe_allow_html=True)
st.subheader("🙋‍♂️ Sobre mí")
a1, a2 = st.columns([2, 1], vertical_alignment="center")
with a1:
    st.write(PROFILE["bio"])
with a2:
    st.image(PROFILE["avatar"], caption="Avatar profesional", use_container_width=True)

# ==============================
# 3) PROYECTOS DESTACADOS
# ==============================
st.markdown("<a id='proyectos-destacados'></a>", unsafe_allow_html=True)
st.subheader("🚀 Proyectos destacados")

for i in range(0, len(PROJECTS), 3):
    cols = st.columns(3)
    for col, project in zip(cols, PROJECTS[i : i + 3]):
        with col:
            st.markdown("<div class='project-card'>", unsafe_allow_html=True)
            st.image(project["image"], use_container_width=True)
            st.markdown(f"### {project['title']}")
            st.write(project["description"])
            chips = "".join([f"<span class='chip'>{t}</span>" for t in project["tech"]])
            st.markdown(chips, unsafe_allow_html=True)
            b1, b2 = st.columns(2)
            b1.link_button("Ver demo", project["demo"], use_container_width=True)
            b2.link_button("Ver código", project["code"], use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# 4) GALERÍA
# ==============================
st.markdown("<a id='galeria-de-imagenes'></a>", unsafe_allow_html=True)
st.subheader("🖼️ Galería de imágenes")
st.caption("Haz click en cualquier botón para abrir una vista ampliada en modal.")

for j in range(0, len(GALLERY), 4):
    row = st.columns(4)
    for col, (caption, url) in zip(row, GALLERY[j : j + 4]):
        with col:
            st.image(url, caption=caption, use_container_width=True)
            # Botón para abrir modal por imagen usando st.dialog
            if st.button(f"Ampliar: {caption}", key=f"open_{caption}_{j}"):
                st.session_state["selected_img"] = (caption, url)

if "selected_img" in st.session_state:
    cap, img = st.session_state["selected_img"]

    @st.dialog(f"Vista ampliada · {cap}")
    def show_modal():
        st.image(img, caption=cap, use_container_width=True)
        st.write("Tip: reemplaza esta imagen por fotos reales tuyas o de tu trabajo.")

    show_modal()

# ==============================
# 5) SNIPPETS DE CÓDIGO
# ==============================
st.markdown("<a id='snippets-de-codigo'></a>", unsafe_allow_html=True)
st.subheader("💻 Snippets de código")

snippets = [
    (
        "1) Limpieza rápida de datos",
        """import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    df = df.drop_duplicates().dropna(how='all')
    return df
""",
    ),
    (
        "2) Cache inteligente en Streamlit",
        """import streamlit as st
import requests

@st.cache_data(ttl=3600)
def get_json(url: str):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
""",
    ),
    (
        "3) Decorador para medir tiempo",
        """from time import perf_counter
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {perf_counter() - start:.4f}s")
        return result
    return wrapper
""",
    ),
    (
        "4) API simple con FastAPI",
        """from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
def health():
    return {'status': 'ok'}
""",
    ),
]

for title, code in snippets:
    with st.expander(title, expanded=False):
        st.code(code, language="python", line_numbers=True)

# ==============================
# 6) SKILLS
# ==============================
st.markdown("<a id='skills'></a>", unsafe_allow_html=True)
st.subheader("🛠️ Skills")

skills_progress = {
    "Python": 95,
    "Streamlit": 90,
    "FastAPI": 85,
    "SQL": 80,
    "Docker": 75,
    "Data Visualization": 88,
    "UI/UX Thinking": 82,
}

for skill, value in skills_progress.items():
    c1, c2 = st.columns([2.5, 1])
    with c1:
        st.write(skill)
        st.progress(value / 100)
    with c2:
        st.metric("Nivel", f"{value}%")

st.markdown("### Tags")
tags = ["Automatización", "IA aplicada", "Dashboards", "Web Apps", "APIs", "Data Science", "Scraping", "DevOps básico"]
st.markdown("".join([f"<span class='skill-tag'>{t}</span>" for t in tags]), unsafe_allow_html=True)

# ==============================
# 7) CONTACTO
# ==============================
st.markdown("<a id='contacto'></a>", unsafe_allow_html=True)
st.subheader("📬 Contacto")

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Tu nombre")
    email = st.text_input("Tu email")
    message = st.text_area("Tu mensaje", height=130)
    send = st.form_submit_button("Enviar mensaje")

if send:
    if name and email and message:
        st.success("¡Mensaje enviado correctamente! Te responderé muy pronto.")
    else:
        st.warning("Por favor completa todos los campos antes de enviar.")

st.divider()
st.caption("Hecho con ❤️ usando Streamlit · Diseño moderno y responsive 2025/2026")
