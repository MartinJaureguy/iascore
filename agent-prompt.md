# Prompt para Antigravity — Conversión a Streamlit + integración Groq

## Contexto para el agente (pegar tal cual)

```
Tengo en esta carpeta el resultado exportado de Stitch (Google): archivos HTML/CSS/JS de un diseño de landing + quiz + pantalla de resultados para un proyecto llamado "IAScore" (evaluador de conocimientos en IA Generativa). También hay un archivo master_prompt.txt con el prompt original usado para generar ese diseño y la rúbrica de evaluación.

Tu tarea es convertir este proyecto en una aplicación funcional en Python usando el framework Streamlit, manteniendo la identidad visual del diseño original (colores, tipografía, estructura de secciones) lo más fielmente posible dentro de las limitaciones de Streamlit. No uses Flask, FastAPI ni ningún otro framework: el despliegue final va a ser en Streamlit Community Cloud.

REQUISITOS FUNCIONALES:

1. FLUJO DE LA APP (usar st.session_state para manejar el estado):
   - Pantalla 1: Hero/bienvenida con el título y botón "Comenzar evaluación".
   - Pantalla 2: Quiz de 5 preguntas abiertas, mostradas de a una por vez (no todas juntas), con barra de progreso ("Pregunta X de 5") y botones "Anterior" / "Siguiente". Las respuestas se van guardando en st.session_state a medida que el usuario avanza, para no perderlas si retrocede.
   - Pantalla 3: Al finalizar la pregunta 5, mostrar un estado de carga (spinner con st.spinner) mientras se llama a la API de Groq, y luego la pantalla de resultados.
   - Pantalla de resultados: puntaje final grande, badge de nivel (Principiante/Intermedio/Avanzado), gráfico radar con los 4 criterios (usar plotly, no matplotlib, para que se vea moderno e interactivo), columnas de "Fortalezas" y "A mejorar", cards de "Recomendaciones", y un botón para reiniciar el cuestionario (que resetee el session_state).

2. INTEGRACIÓN CON GROQ:
   - Usar el SDK oficial de Groq para Python (paquete `groq`), no requests crudo, salvo que no esté disponible.
   - La API key NO debe estar hardcodeada en ningún lado. Debe leerse desde una variable llamada GROQ_API_KEY, obtenida así:
     ```python
     import streamlit as st
     import os

     GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", os.environ.get("GROQ_API_KEY"))
     ```
     Esto permite que funcione tanto en local (con un archivo .streamlit/secrets.toml que vos vas a crear manualmente y NO debe subirse a git) como en Streamlit Community Cloud (configurando el secret desde el panel de la app).
   - Crear un archivo .streamlit/secrets.toml.example (de ejemplo, sin la key real) con el formato:
     ```toml
     GROQ_API_KEY = "tu-api-key-aca"
     ```
   - Agregar .streamlit/secrets.toml al .gitignore (crear el .gitignore si no existe) para que nunca se suba la key real al repositorio.
   - Si GROQ_API_KEY no está configurada, la app debe mostrar un st.error claro explicando que falta configurar el secret, en vez de crashear con una excepción fea.
   - Usar el modelo "llama-3.3-70b-versatile" de Groq (o el que esté disponible en el free tier al momento de correr el código; si ese modelo da error, probar con "llama-3.1-8b-instant" como alternativa).
   - Configurar temperature baja (0.2-0.3) para esta tarea de evaluación, ya que buscamos consistencia y no creatividad.

3. LÓGICA DE EVALUACIÓN:
   - Usar como system prompt el contenido completo de la rúbrica que está en master_prompt.txt (la sección de rúbrica, no el prompt de diseño de Stitch). Copiala tal cual al código, en una variable SYSTEM_PROMPT o en un archivo aparte rubric.py que se importe.
   - El mensaje del usuario a Groq debe incluir las 5 preguntas junto con las 5 respuestas del usuario, claramente identificadas (Pregunta 1: ... / Respuesta: ... etc.).
   - Pedir explícitamente al modelo que responda solo con el JSON (esto ya está indicado en la rúbrica, pero reforzalo en el código).
   - Parsear la respuesta con json.loads() dentro de un try/except. Si falla el parseo (el modelo devolvió texto extra antes/después del JSON), intentar extraer el bloque JSON con una expresión regular simple (buscar desde el primer '{' hasta el último '}') antes de fallar. Si aun así falla, mostrar un mensaje de error amigable al usuario y un botón para reintentar.

4. VALIDACIONES:
   - No permitir avanzar de pregunta si el campo de respuesta está vacío (mostrar un st.warning).
   - Manejar errores de la API de Groq (timeout, rate limit, key inválida) con mensajes claros usando try/except alrededor del llamado, diferenciando si es un error de autenticación (401) vs. rate limit (429) vs. otro error, y mostrando un mensaje distinto para cada caso.

5. ESTRUCTURA DE ARCHIVOS que espero como resultado:
   ```
   /
   ├── app.py                    # app principal de Streamlit
   ├── rubric.py                 # contiene el SYSTEM_PROMPT con la rúbrica
   ├── groq_client.py            # función que llama a la API de Groq y devuelve el JSON parseado
   ├── requirements.txt          # streamlit, groq, plotly
   ├── .streamlit/
   │   ├── config.toml           # tema de Streamlit ajustado a los colores del diseño (dark mode, color de acento)
   │   └── secrets.toml.example
   ├── .gitignore
   └── README.md                 # instrucciones de instalación local y deploy en Streamlit Community Cloud
   ```

6. ESTILO VISUAL EN STREAMLIT:
   - Usar .streamlit/config.toml para configurar el theme (backgroundColor, primaryColor, textColor, font) acorde a la paleta oscura + acento violeta/cian del diseño original.
   - Donde Streamlit no permita replicar el diseño exacto de Stitch (Streamlit tiene limitaciones de layout), usar st.markdown con HTML/CSS embebido (unsafe_allow_html=True) para lograr cards, badges y el radar chart styling lo más parecido posible al mockup original.
   - Mantené el proyecto simple de mantener: no uses componentes de terceros que requieran instalación compleja, salvo plotly.

7. README.md debe incluir:
   - Cómo instalar dependencias (pip install -r requirements.txt)
   - Cómo crear el archivo .streamlit/secrets.toml local con la GROQ_API_KEY
   - Cómo correr localmente (streamlit run app.py)
   - Pasos para desplegar en Streamlit Community Cloud, incluyendo dónde configurar el secret GROQ_API_KEY en el panel de la app desplegada

Antes de escribir código, hacé un resumen breve del plan de archivos y la lógica que vas a implementar, y esperá mi confirmación antes de generar todo el código.
```

