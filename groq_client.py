"""
Cliente para la API de Groq — IAScore
Evalúa las respuestas del usuario usando el modelo LLM de Groq.
"""

import json
import re
from groq import Groq
from rubric import SYSTEM_PROMPT


def evaluate_answers(questions: list[str], answers: list[str], api_key: str) -> dict:
    """
    Envía las preguntas y respuestas del usuario a Groq para evaluación.

    Args:
        questions: Lista de 5 preguntas.
        answers: Lista de 5 respuestas del usuario.
        api_key: API key de Groq.

    Returns:
        dict con el resultado parseado, o dict con {"error": True, "message": "..."}.
    """
    # Construir el mensaje del usuario
    user_message_parts = []
    for i, (question, answer) in enumerate(zip(questions, answers), 1):
        user_message_parts.append(f"Pregunta {i}: {question}\nRespuesta: {answer}")

    user_message = "\n\n".join(user_message_parts)
    user_message += "\n\nResponde ÚNICAMENTE con el JSON de evaluación, sin texto adicional."

    # Modelos a intentar (en orden de preferencia)
    models = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant"]

    client = Groq(api_key=api_key)

    for model in models:
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_message},
                ],
                model=model,
                temperature=0.3,
                max_tokens=4096,
            )

            response_text = chat_completion.choices[0].message.content

            # Intentar parsear directamente
            try:
                result = json.loads(response_text)
                return result
            except json.JSONDecodeError:
                # Intentar extraer JSON con regex (primer '{' al último '}')
                json_match = re.search(r"\{.*\}", response_text, re.DOTALL)
                if json_match:
                    try:
                        result = json.loads(json_match.group())
                        return result
                    except json.JSONDecodeError:
                        pass

                return {
                    "error": True,
                    "message": "La IA devolvió una respuesta que no pude interpretar. Por favor, intentá de nuevo.",
                }

        except Exception as e:
            error_str = str(e)

            # Verificar si es un error del modelo (404) para intentar el siguiente
            if "404" in error_str or "model" in error_str.lower():
                continue

            # Errores específicos
            if "401" in error_str or "authentication" in error_str.lower():
                return {
                    "error": True,
                    "message": "❌ Error de autenticación: La API key de Groq es inválida. "
                    "Verificá que esté correctamente configurada en `.streamlit/secrets.toml`.",
                }

            if "429" in error_str or "rate" in error_str.lower():
                return {
                    "error": True,
                    "message": "⏳ Límite de solicitudes alcanzado (rate limit). "
                    "Esperá unos segundos e intentá de nuevo.",
                }

            return {
                "error": True,
                "message": f"Error al conectar con la API de Groq: {error_str}",
            }

    return {
        "error": True,
        "message": "No se pudo conectar con ningún modelo disponible de Groq. Intentá de nuevo más tarde.",
    }
