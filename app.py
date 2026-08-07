"""
IAScore — Evaluador de conocimientos en IA Generativa
App principal de Streamlit
"""

import streamlit as st
import os
import plotly.graph_objects as go

from rubric import QUESTIONS
from groq_client import evaluate_answers

# ─── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="IAScore — Evaluador de IA Generativa",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── API Key ──────────────────────────────────────────────────────────────────
try:
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY"))
except Exception:
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# ─── CSS Global ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    /* Reset Streamlit defaults */
    .stApp {
        background-color: #0A0A0F !important;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Global typography */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #e4e1e9;
    }

    h1, h2, h3, h4 {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #e4e1e9 !important;
    }

    /* ── Hero Section ── */
    .hero-container {
        text-align: center;
        padding: 80px 20px 60px;
        position: relative;
    }

    .hero-glow {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(124,58,237,0.08) 0%, transparent 70%);
        pointer-events: none;
        z-index: 0;
    }

    .hero-badge {
        display: inline-block;
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: #ccc3d8;
        background: rgba(124,58,237,0.1);
        border: 1px solid rgba(124,58,237,0.2);
        padding: 6px 16px;
        border-radius: 9999px;
        margin-bottom: 24px;
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 52px;
        font-weight: 700;
        line-height: 1.15;
        letter-spacing: -0.02em;
        color: #e4e1e9;
        margin-bottom: 20px;
        position: relative;
        z-index: 1;
    }

    .hero-title .gradient-text {
        background: linear-gradient(135deg, #d2bbff 0%, #00d9ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        line-height: 28px;
        color: #9CA3AF;
        max-width: 560px;
        margin: 0 auto 40px;
        position: relative;
        z-index: 1;
    }

    /* ── Cards & Panels ── */
    .glass-card {
        background: rgba(18, 18, 26, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid #26262E;
        border-radius: 16px;
        padding: 32px;
        margin-bottom: 24px;
    }

    .glass-card:hover {
        border-color: rgba(124,58,237,0.3);
        box-shadow: 0 0 20px rgba(124,58,237,0.08);
    }

    /* ── Buttons ── */
    .btn-primary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        background: linear-gradient(135deg, #7c3aed 0%, #00d9ff 100%);
        color: white !important;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 16px;
        padding: 14px 32px;
        border-radius: 12px;
        border: none;
        cursor: pointer;
        text-decoration: none;
        transition: all 0.3s ease;
        position: relative;
        z-index: 1;
    }

    .btn-primary:hover {
        box-shadow: 0 0 30px rgba(124,58,237,0.3);
        transform: translateY(-2px);
    }

    .btn-ghost {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        background: transparent;
        color: #9CA3AF !important;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        font-size: 14px;
        padding: 12px 24px;
        border-radius: 10px;
        border: 1px solid #26262E;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .btn-ghost:hover {
        color: white !important;
        border-color: #4a4455;
        background: rgba(255,255,255,0.05);
    }

    /* ── Quiz ── */
    .quiz-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
    }

    .quiz-label {
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        color: #ccc3d8;
    }

    .quiz-percent {
        font-family: 'Inter', sans-serif;
        font-size: 12px;
        font-weight: 700;
        color: #d2bbff;
    }

    .progress-bar-container {
        width: 100%;
        height: 8px;
        background: #26262E;
        border-radius: 9999px;
        overflow: hidden;
        margin-bottom: 32px;
    }

    .progress-bar-fill {
        height: 100%;
        background: linear-gradient(135deg, #7c3aed 0%, #00d9ff 100%);
        border-radius: 9999px;
        box-shadow: 0 0 12px rgba(124,58,237,0.5);
        transition: width 0.5s ease;
    }

    .question-text {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 24px;
        font-weight: 600;
        line-height: 32px;
        color: #e4e1e9;
        margin-bottom: 24px;
    }

    /* ── Results ── */
    .score-ring-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 32px 0;
        position: relative;
    }

    .score-ring-glow {
        position: absolute;
        width: 280px;
        height: 280px;
        background: radial-gradient(circle, rgba(124,58,237,0.12) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
    }

    .score-display {
        position: relative;
        z-index: 1;
        text-align: center;
    }

    .score-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 72px;
        font-weight: 700;
        color: #e4e1e9;
        line-height: 1;
    }

    .score-denominator {
        font-family: 'Inter', sans-serif;
        font-size: 20px;
        color: #9CA3AF;
    }

    .level-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 20px;
        border-radius: 9999px;
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-top: 16px;
    }

    .level-principiante {
        background: rgba(245,158,11,0.15);
        border: 1px solid rgba(245,158,11,0.3);
        color: #f59e0b;
    }

    .level-intermedio {
        background: rgba(124,58,237,0.15);
        border: 1px solid rgba(124,58,237,0.3);
        color: #d2bbff;
    }

    .level-avanzado {
        background: rgba(0,217,255,0.15);
        border: 1px solid rgba(0,217,255,0.3);
        color: #00d9ff;
    }

    /* ── Feedback Lists ── */
    .feedback-card {
        background: rgba(18, 18, 26, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid #26262E;
        border-radius: 16px;
        padding: 24px;
    }

    .feedback-card.strengths {
        border-left: 3px solid #aeecff;
    }

    .feedback-card.weaknesses {
        border-left: 3px solid #ffb4ab;
    }

    .feedback-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 20px;
        font-weight: 600;
        color: #e4e1e9;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .feedback-item {
        display: flex;
        align-items: flex-start;
        gap: 10px;
        padding: 8px 0;
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        color: #ccc3d8;
        line-height: 1.5;
    }

    .feedback-icon-ok {
        color: #aeecff;
        font-size: 18px;
        margin-top: 2px;
    }

    .feedback-icon-warn {
        color: #ffb4ab;
        font-size: 18px;
        margin-top: 2px;
    }

    /* ── Recommendation cards ── */
    .rec-card {
        background: rgba(18, 18, 26, 0.4);
        border: 1px solid #26262E;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 12px;
        transition: all 0.3s ease;
    }

    .rec-card:hover {
        border-color: rgba(124,58,237,0.3);
        background: rgba(18, 18, 26, 0.7);
    }

    .rec-text {
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        color: #ccc3d8;
        line-height: 1.6;
    }

    .rec-icon {
        color: #00d9ff;
        margin-right: 8px;
    }

    /* ── Section titles ── */
    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 24px;
        font-weight: 600;
        color: #e4e1e9;
        margin-bottom: 8px;
    }

    .section-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        color: #9CA3AF;
        margin-bottom: 24px;
    }

    /* ── Justification expander ── */
    .justification-card {
        background: rgba(18, 18, 26, 0.4);
        border: 1px solid #26262E;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 12px;
    }

    .justification-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }

    .justification-q {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 16px;
        font-weight: 600;
        color: #e4e1e9;
    }

    .justification-score {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 20px;
        font-weight: 700;
        color: #d2bbff;
    }

    .justification-text {
        font-family: 'Inter', sans-serif;
        font-size: 14px;
        color: #9CA3AF;
        line-height: 1.6;
    }

    .criteria-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 8px;
        margin-top: 12px;
    }

    .criteria-item {
        text-align: center;
        padding: 8px;
        background: rgba(26,26,36,0.5);
        border-radius: 8px;
    }

    .criteria-label {
        font-size: 11px;
        color: #9CA3AF;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .criteria-value {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 18px;
        font-weight: 600;
        color: #d2bbff;
    }

    /* ── Footer ── */
    .app-footer {
        text-align: center;
        padding: 40px 20px;
        border-top: 1px solid rgba(74,68,85,0.3);
        margin-top: 60px;
    }

    .footer-brand {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 20px;
        font-weight: 700;
        color: #e4e1e9;
        margin-bottom: 8px;
    }

    .footer-text {
        font-family: 'Inter', sans-serif;
        font-size: 13px;
        color: #656769;
    }

    /* ── Streamlit overrides ── */
    .stTextArea textarea {
        background-color: #12121A !important;
        border: 1px solid #26262E !important;
        border-radius: 16px !important;
        color: #e4e1e9 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        padding: 16px !important;
        min-height: 180px !important;
        transition: all 0.3s ease !important;
    }

    .stTextArea textarea:focus {
        border-color: #7c3aed !important;
        box-shadow: 0 0 0 2px rgba(124,58,237,0.2) !important;
    }

    .stTextArea textarea::placeholder {
        color: rgba(204,195,216,0.4) !important;
    }

    .stTextArea label {
        display: none !important;
    }

    /* Button overrides */
    .stButton > button {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        padding: 10px 28px !important;
        transition: all 0.3s ease !important;
    }

    div[data-testid="stHorizontalBlock"] .stButton > button {
        width: 100%;
    }

    /* Plotly chart background */
    .js-plotly-plot .plotly .bg {
        fill: transparent !important;
    }

    /* Warning/error styling */
    .stAlert {
        border-radius: 12px !important;
    }
</style>
""", unsafe_allow_html=True)


# ─── Session State Initialization ─────────────────────────────────────────────
if "screen" not in st.session_state:
    st.session_state.screen = "hero"

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = [""] * len(QUESTIONS)

if "results" not in st.session_state:
    st.session_state.results = None

if "evaluation_done" not in st.session_state:
    st.session_state.evaluation_done = False


# ─── Helper Functions ─────────────────────────────────────────────────────────
def go_to_screen(screen_name):
    st.session_state.screen = screen_name


def next_question():
    if st.session_state.current_question < len(QUESTIONS) - 1:
        st.session_state.current_question += 1


def prev_question():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1


def reset_quiz():
    st.session_state.screen = "hero"
    st.session_state.current_question = 0
    st.session_state.answers = [""] * len(QUESTIONS)
    st.session_state.results = None
    st.session_state.evaluation_done = False


def create_radar_chart(results_data):
    """Crea un gráfico radar con Plotly usando los promedios de los 4 criterios."""
    preguntas = results_data.get("preguntas", [])

    if not preguntas:
        return None

    # Promediar cada criterio
    avg_precision = sum(p.get("precision", 0) for p in preguntas) / len(preguntas)
    avg_profundidad = sum(p.get("profundidad", 0) for p in preguntas) / len(preguntas)
    avg_contexto = sum(p.get("contexto", 0) for p in preguntas) / len(preguntas)
    avg_claridad = sum(p.get("claridad", 0) for p in preguntas) / len(preguntas)

    categories = ["Precisión", "Profundidad", "Contexto", "Claridad"]
    values = [avg_precision, avg_profundidad, avg_contexto, avg_claridad]

    fig = go.Figure()

    # Área de datos
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],  # Cerrar el polígono
        theta=categories + [categories[0]],
        fill="toself",
        fillcolor="rgba(124, 58, 237, 0.15)",
        line=dict(color="#7c3aed", width=2),
        marker=dict(size=8, color="#d2bbff"),
        name="Tu rendimiento",
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                showticklabels=True,
                tickfont=dict(size=10, color="#656769"),
                gridcolor="rgba(74,68,85,0.3)",
                linecolor="rgba(74,68,85,0.3)",
            ),
            angularaxis=dict(
                tickfont=dict(size=13, color="#ccc3d8", family="Space Grotesk"),
                gridcolor="rgba(74,68,85,0.3)",
                linecolor="rgba(74,68,85,0.3)",
            ),
        ),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=60, r=60, t=40, b=40),
        height=380,
    )

    return fig


# ═══════════════════════════════════════════════════════════════════════════════
# PANTALLA 1: HERO / BIENVENIDA
# ═══════════════════════════════════════════════════════════════════════════════
if st.session_state.screen == "hero":

    st.markdown("""
    <div class="hero-container">
        <div class="hero-glow"></div>
        <div class="hero-badge">🧠 Powered by Groq</div>
        <h1 class="hero-title">
            Descubrí qué tan preparado<br>estás en <span class="gradient-text">IA Generativa</span>
        </h1>
        <p class="hero-subtitle">
            Evaluación instantánea con feedback personalizado de nivel experto.
            Diseñado para líderes técnicos y equipos vanguardistas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Botón centrado
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🚀  Comenzar evaluación", use_container_width=True, type="primary"):
            go_to_screen("quiz")
            st.rerun()

    # Footer
    st.markdown("""
    <div class="app-footer">
        <div class="footer-brand">IAScore</div>
        <div class="footer-text">Hecho con IA para evaluar IA · © 2024 IAScore</div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════════════
# PANTALLA 2: QUIZ
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == "quiz":

    q_idx = st.session_state.current_question
    q_num = q_idx + 1
    total = len(QUESTIONS)
    progress = q_num / total

    # ─── Progress Header ──────────────────────────────────────────────────
    st.markdown(f"""
    <div class="glass-card">
        <div class="quiz-header">
            <span class="quiz-label">Pregunta {q_num} de {total}</span>
            <span class="quiz-percent">{int(progress * 100)}%</span>
        </div>
        <div class="progress-bar-container">
            <div class="progress-bar-fill" style="width: {int(progress * 100)}%"></div>
        </div>
        <div class="question-text">{QUESTIONS[q_idx]}</div>
    </div>
    """, unsafe_allow_html=True)

    # ─── Text Area ────────────────────────────────────────────────────────
    answer = st.text_area(
        label="Respuesta",
        value=st.session_state.answers[q_idx],
        placeholder="Escribí tu respuesta acá...",
        height=180,
        key=f"answer_{q_idx}",
    )
    st.session_state.answers[q_idx] = answer

    # ─── Navigation ───────────────────────────────────────────────────────
    col_prev, col_spacer, col_next = st.columns([1, 2, 1])

    with col_prev:
        if q_idx > 0:
            if st.button("← Anterior", use_container_width=True):
                prev_question()
                st.rerun()

    with col_next:
        if q_idx < total - 1:
            if st.button("Siguiente →", use_container_width=True, type="primary"):
                if not answer.strip():
                    st.warning("⚠️ Escribí una respuesta antes de continuar.")
                else:
                    next_question()
                    st.rerun()
        else:
            if st.button("🎯 Finalizar evaluación", use_container_width=True, type="primary"):
                if not answer.strip():
                    st.warning("⚠️ Escribí una respuesta antes de finalizar.")
                else:
                    # Verificar que todas las respuestas estén completas
                    empty_answers = [i + 1 for i, a in enumerate(st.session_state.answers) if not a.strip()]
                    if empty_answers:
                        st.warning(f"⚠️ Falta completar la(s) pregunta(s): {', '.join(map(str, empty_answers))}")
                    else:
                        go_to_screen("results")
                        st.rerun()


# ═══════════════════════════════════════════════════════════════════════════════
# PANTALLA 3: RESULTADOS
# ═══════════════════════════════════════════════════════════════════════════════
elif st.session_state.screen == "results":

    # ─── Verificar API Key ────────────────────────────────────────────────
    if not GROQ_API_KEY:
        st.error(
            "🔑 **Falta configurar la API key de Groq.**\n\n"
            "Para correr en local:\n"
            "1. Creá el archivo `.streamlit/secrets.toml`\n"
            "2. Agregá la línea: `GROQ_API_KEY = \"tu-api-key-aca\"`\n\n"
            "Para Streamlit Community Cloud:\n"
            "- Configurá el secret `GROQ_API_KEY` desde el panel de la app desplegada."
        )
        if st.button("← Volver al cuestionario"):
            go_to_screen("quiz")
            st.rerun()
        st.stop()

    # ─── Llamar a Groq (solo una vez) ─────────────────────────────────────
    if not st.session_state.evaluation_done:
        with st.spinner("🧠 Analizando tus respuestas con IA..."):
            results = evaluate_answers(QUESTIONS, st.session_state.answers, GROQ_API_KEY)

        if results.get("error"):
            st.error(results["message"])
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 Reintentar", use_container_width=True, type="primary"):
                    st.rerun()
            with col2:
                if st.button("← Volver al cuestionario", use_container_width=True):
                    go_to_screen("quiz")
                    st.rerun()
            st.stop()

        st.session_state.results = results
        st.session_state.evaluation_done = True

    results = st.session_state.results

    # ─── Score + Radar ────────────────────────────────────────────────────
    puntaje = results.get("puntaje_final", 0)
    nivel = results.get("nivel", "Intermedio")

    level_class = {
        "Principiante": "level-principiante",
        "Intermedio": "level-intermedio",
        "Avanzado": "level-avanzado",
    }.get(nivel, "level-intermedio")

    level_icon = {
        "Principiante": "🌱",
        "Intermedio": "⚡",
        "Avanzado": "🏆",
    }.get(nivel, "⚡")

    col_score, col_radar = st.columns(2)

    with col_score:
        st.markdown(f"""
        <div class="glass-card">
            <div class="section-title" style="text-align:center; margin-bottom:16px;">Evaluación Completada</div>
            <div class="score-ring-container">
                <div class="score-ring-glow"></div>
                <div class="score-display">
                    <div class="score-number">{puntaje}</div>
                    <div class="score-denominator">/ 10</div>
                </div>
            </div>
            <div style="text-align:center;">
                <span class="level-badge {level_class}">{level_icon} Nivel {nivel}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_radar:
        st.markdown("""
        <div class="glass-card" style="padding-bottom:16px;">
            <div class="section-title">Análisis de Competencias</div>
            <div class="section-subtitle">Desglose multidimensional de tu rendimiento.</div>
        </div>
        """, unsafe_allow_html=True)

        radar_fig = create_radar_chart(results)
        if radar_fig:
            st.plotly_chart(radar_fig, use_container_width=True, config={"displayModeBar": False})

    # ─── Fortalezas y Debilidades ─────────────────────────────────────────
    col_str, col_weak = st.columns(2)

    with col_str:
        fortalezas_html = ""
        for f in results.get("fortalezas", []):
            fortalezas_html += f'<div class="feedback-item"><span class="feedback-icon-ok">✓</span><span>{f}</span></div>'

        st.markdown(f"""
        <div class="feedback-card strengths">
            <div class="feedback-title">✅ Fortalezas</div>
            {fortalezas_html}
        </div>
        """, unsafe_allow_html=True)

    with col_weak:
        debilidades_html = ""
        for d in results.get("debilidades", []):
            debilidades_html += f'<div class="feedback-item"><span class="feedback-icon-warn">→</span><span>{d}</span></div>'

        st.markdown(f"""
        <div class="feedback-card weaknesses">
            <div class="feedback-title">⚠️ A Mejorar</div>
            {debilidades_html}
        </div>
        """, unsafe_allow_html=True)

    # ─── Recomendaciones ──────────────────────────────────────────────────
    st.markdown("""
    <div style="margin-top:32px;">
        <div class="section-title">💡 Recomendaciones</div>
        <div class="section-subtitle">Pasos concretos para mejorar tu conocimiento.</div>
    </div>
    """, unsafe_allow_html=True)

    for rec in results.get("recomendaciones", []):
        st.markdown(f"""
        <div class="rec-card">
            <div class="rec-text"><span class="rec-icon">→</span> {rec}</div>
        </div>
        """, unsafe_allow_html=True)

    # ─── Detalle por pregunta ─────────────────────────────────────────────
    st.markdown("""
    <div style="margin-top:32px;">
        <div class="section-title">📋 Detalle por Pregunta</div>
        <div class="section-subtitle">Justificación y desglose de criterios para cada respuesta.</div>
    </div>
    """, unsafe_allow_html=True)

    for p in results.get("preguntas", []):
        with st.expander(f"Pregunta {p.get('numero', '?')} — Puntaje: {p.get('puntaje', 0)}"):
            st.markdown(f"""
            <div class="justification-card">
                <div class="justification-header">
                    <span class="justification-q">{QUESTIONS[p.get('numero', 1) - 1]}</span>
                    <span class="justification-score">{p.get('puntaje', 0)}/10</span>
                </div>
                <div class="justification-text">{p.get('justificacion', '')}</div>
                <div class="criteria-grid">
                    <div class="criteria-item">
                        <div class="criteria-label">Precisión</div>
                        <div class="criteria-value">{p.get('precision', 0)}</div>
                    </div>
                    <div class="criteria-item">
                        <div class="criteria-label">Profundidad</div>
                        <div class="criteria-value">{p.get('profundidad', 0)}</div>
                    </div>
                    <div class="criteria-item">
                        <div class="criteria-label">Contexto</div>
                        <div class="criteria-value">{p.get('contexto', 0)}</div>
                    </div>
                    <div class="criteria-item">
                        <div class="criteria-label">Claridad</div>
                        <div class="criteria-value">{p.get('claridad', 0)}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ─── Acciones finales ─────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    col_retry, col_spacer2 = st.columns([1, 2])

    with col_retry:
        if st.button("🔄 Reiniciar cuestionario", use_container_width=True, type="primary"):
            reset_quiz()
            st.rerun()

    # ─── Footer ───────────────────────────────────────────────────────────
    st.markdown("""
    <div class="app-footer">
        <div class="footer-brand">IAScore</div>
        <div class="footer-text">Hecho con IA para evaluar IA · © 2024 IAScore</div>
    </div>
    """, unsafe_allow_html=True)
