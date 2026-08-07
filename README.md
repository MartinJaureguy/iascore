# 🧠 IAScore — Evaluador de Conocimientos en IA Generativa

IAScore es una aplicación web que evalúa tus conocimientos en Inteligencia Artificial Generativa mediante un cuestionario de 5 preguntas abiertas. Utiliza un modelo LLM (via [Groq](https://groq.com/)) para analizar tus respuestas y brindarte feedback personalizado con puntaje, fortalezas, debilidades y recomendaciones.

## ✨ Características

- **Quiz interactivo** de 5 preguntas, mostradas de a una por vez con barra de progreso
- **Evaluación con IA** usando el modelo Llama 3.3 70B via Groq (ultrarrápido)
- **Puntaje detallado** con desglose por 4 criterios: Precisión, Profundidad, Contexto y Claridad
- **Gráfico radar interactivo** (Plotly) para visualizar competencias
- **Feedback personalizado**: fortalezas, debilidades y recomendaciones accionables
- **Diseño dark mode premium** inspirado en productos como Linear y Vercel

## 🚀 Instalación Local

### 1. Clonar el repositorio

```bash
git clone <url-del-repo>
cd iascore
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar la API Key de Groq

Creá el archivo `.streamlit/secrets.toml` (este archivo **NO se sube a Git**):

```bash
# En Windows (PowerShell):
copy .streamlit\secrets.toml.example .streamlit\secrets.toml

# En Mac/Linux:
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

Luego editá `.streamlit/secrets.toml` y reemplazá con tu API key real:

```toml
GROQ_API_KEY = "gsk_tu_api_key_real_aca"
```

> 💡 Podés obtener una API key gratuita en [console.groq.com](https://console.groq.com/)

### 4. Correr la app

```bash
streamlit run app.py
```

La app se abrirá automáticamente en `http://localhost:8501`.

## ☁️ Deploy en Streamlit Community Cloud

### 1. Subir el código a GitHub

Asegurate de que el repositorio incluya todos los archivos **excepto** `.streamlit/secrets.toml` (ya está en `.gitignore`).

### 2. Conectar con Streamlit Community Cloud

1. Andá a [share.streamlit.io](https://share.streamlit.io/)
2. Conectá tu cuenta de GitHub
3. Seleccioná el repositorio y el archivo `app.py`

### 3. Configurar el Secret

1. En el panel de tu app desplegada, hacé clic en **⚙️ Settings** (el engranaje)
2. Andá a la pestaña **Secrets**
3. Pegá el contenido del secret:

```toml
GROQ_API_KEY = "gsk_tu_api_key_real_aca"
```

4. Hacé clic en **Save**. La app se va a reiniciar automáticamente.

## 📁 Estructura de Archivos

```
iascore/
├── app.py                        # App principal de Streamlit
├── rubric.py                     # Rúbrica de evaluación (SYSTEM_PROMPT)
├── groq_client.py                # Cliente para la API de Groq
├── requirements.txt              # Dependencias (streamlit, groq, plotly)
├── .streamlit/
│   ├── config.toml               # Tema visual (dark mode + colores)
│   └── secrets.toml.example      # Ejemplo de configuración de secrets
├── .gitignore                    # Excluye secrets.toml y archivos temporales
└── README.md                     # Este archivo
```

## 🛠️ Tecnologías

| Tecnología | Uso |
|---|---|
| [Streamlit](https://streamlit.io/) | Framework de la UI |
| [Groq](https://groq.com/) | API de inferencia LLM (Llama 3.3 70B) |
| [Plotly](https://plotly.com/) | Gráfico radar interactivo |

## 📝 Licencia

Proyecto educativo desarrollado para CoderHouse.
