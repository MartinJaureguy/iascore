### Las 5 preguntas fijas del cuestionario

1. ¿Qué es un LLM y cómo funciona a alto nivel?
2. ¿Qué diferencia hay entre fine-tuning y prompt engineering?
3. Dame un ejemplo de alucinación y cómo mitigarla.
4. ¿Qué es RAG y cuándo usarlo?
5. ¿Qué riesgos éticos ves en el uso de IA generativa en tu industria?

---

## 2. Prompt detallado para Stitch (diseño de la web)

```
Diseñá una landing page + aplicación web de una sola página para un producto llamado "IAScore", un evaluador de conocimientos en Inteligencia Artificial Generativa potenciado por IA. El diseño debe sentirse moderno, premium y "vendible", como un producto SaaS de 2026, no como un formulario académico aburrido.

ESTILO VISUAL GENERAL:
- Estética: dark mode como base, minimalista pero con personalidad, inspirado en productos como Linear, Vercel o Perplexity.
- Paleta de colores: fondo casi negro (#0A0A0F o similar), con un color de acento vibrante tipo violeta-eléctrico o cian-neón (#7C3AED o #00D9FF) usado con moderación en botones, bordes activos y elementos de datos. Textos en blanco roto (#F5F5F7) y grises (#9CA3AF) para jerarquía.
- Tipografía: sans-serif moderna y geométrica (estilo Inter, Space Grotesk o Satoshi) para títulos grandes y bold; cuerpo de texto más liviano y legible.
- Usar gradientes sutiles (violeta a azul) en fondos de secciones o detrás de elementos clave, nunca saturando toda la pantalla.
- Bordes redondeados suaves (12-16px) en cards y botones, con sombras suaves tipo "glow" en elementos interactivos.
- Micro-interacciones sugeridas: hover states con leve elevación y brillo, transiciones suaves.

ESTRUCTURA DE LA PÁGINA (en este orden):

1. HEADER
   - Logo/nombre del proyecto a la izquierda (tipografía bold)
   - Badge pequeño tipo "Powered by Groq" o "AI-Powered" a la derecha

2. HERO SECTION
   - Título grande e impactante (ej: "Descubrí qué tan preparado estás en IA Generativa")
   - Subtítulo corto explicando el valor: evaluación instantánea con feedback personalizado
   - Botón principal grande con el acento de color: "Comenzar evaluación"
   - Elemento visual decorativo: podría ser un mockup abstracto de un gráfico radar o barras flotando con glow, sugiriendo "análisis de datos"

3. SECCIÓN DE PREGUNTAS (vista tipo "quiz card")
   - Una card central, ancha pero no full-width, centrada en la pantalla
   - Indicador de progreso arriba (ej: "Pregunta 2 de 5") con barra de progreso delgada usando el color de acento
   - Número de pregunta destacado, texto de la pregunta en tamaño grande y legible
   - Textarea grande, con bordes redondeados, fondo ligeramente más claro que el fondo general, placeholder tipo "Escribí tu respuesta acá..."
   - Botones de navegación "Anterior" (secundario, outline) y "Siguiente" / "Finalizar" (primario, con el color de acento) alineados abajo a la derecha

4. PANTALLA DE RESULTADOS (después de enviar el cuestionario)
   - Puntaje final destacado en el centro, tipografía enorme (ej: "7.2/10"), con un anillo de progreso circular animado alrededor usando el color de acento
   - Nivel del usuario debajo del puntaje como badge (Principiante / Intermedio / Avanzado) con colores diferenciados (ej: ámbar, violeta, verde neón)
   - Gráfico tipo radar chart mostrando los 4 criterios (Precisión, Profundidad, Contexto, Claridad) promediados
   - Dos columnas debajo: "Fortalezas" (con ícono de check verde) y "A mejorar" (con ícono de flecha o alerta ámbar), cada una con bullets cortos
   - Sección de "Recomendaciones" al final, presentada como cards individuales pequeñas, una por recomendación
   - Botón secundario abajo: "Volver a intentar" o "Compartir resultado"

5. FOOTER
   - Minimalista, con nombre del proyecto y un texto pequeño tipo "Hecho con IA para evaluar IA"

REQUISITOS TÉCNICOS DE DISEÑO:
- Totalmente responsive, priorizando que se vea excelente en desktop (se va a mostrar en una demo de clase en pantalla grande) pero funcional en mobile.
- Buen uso de espacio en blanco (o "espacio en negro" en este caso), sin saturar la pantalla.
- Contraste alto para legibilidad (texto siempre legible sobre los fondos oscuros).
- Evitar íconos genéricos de stock; preferir un lenguaje visual coherente y minimalista (líneas finas, geometría simple).

TONO GENERAL: el diseño debe transmitir confianza y precisión (como una herramienta analítica seria) pero sin perder calidez ni volverse intimidante — el usuario tiene que sentir ganas de completar el cuestionario, no percibirlo como un examen estresante.
```
