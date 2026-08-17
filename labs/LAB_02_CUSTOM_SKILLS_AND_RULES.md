# 🧪 Laboratorio 2: Creación Rápida de Habilidades (Skills) Mediante Prompts en Antigravity 2.0

**Audiencia:** Desarrolladores e Ingenieros de Software de Unicomer (con experiencia en Claude Code / VS Code)  
**Tiempo estimado:** 25 - 30 minutos  
**Superficie de Trabajo:** **Antigravity 2.0 (GUI / Web)**  
**Objetivo:** Aprender a crear, extraer, probar y versionar **Habilidades Empresariales (Gemini Skills)** en segundos usando lenguaje natural en Antigravity 2.0, sin escribir plantillas YAML ni estructuras de carpetas a mano.

---

## 🎯 ¿Por qué Antigravity 2.0 para la Creación de Habilidades?

Si tu equipo hoy utiliza herramientas como Claude Code o editores manuales de prompts, Antigravity 2.0 lleva la personalización al siguiente nivel:

| Flujo Tradicional / Claude Code | Flujo Agéntico en Antigravity 2.0 |
| :--- | :--- |
| ❌ Crear carpetas y archivos markdown a mano | ✅ **Creación conversacional:** Pides la habilidad por prompt y Antigravity la estructura |
| ❌ Redactar encabezados YAML y reglas manualmente | ✅ **Extracción inteligente de patrones:** Antigravity analiza tu código y genera la skill |
| ❌ Probar la regla manualmente con prueba y error | ✅ **Auto-verificación:** El agente valida la habilidad contra el código activo de inmediato |
| ❌ Configuraciones aisladas en cada máquina | ✅ **Git-Native Team Sync:** Al guardar en `.agents/skills/`, todo el equipo hereda la habilidad con un `git pull` |

---

## 👣 Ejercicios Prácticos del Laboratorio

### Ejercicio 1: Crear una Habilidad desde Cero con un Solo Prompt

En lugar de crear archivos a mano, pídele a **Antigravity 2.0** que cree la habilidad por ti:

#### 📋 Prompt para Antigravity 2.0:
```text
Crea una nueva habilidad personalizada llamada 'unicomer-scoring-engine' en '.agents/skills/unicomer-scoring-engine'.
La habilidad debe establecer que:
1. Todo cliente de La Curacao, Gollo o Emma debe ser evaluado con un puntaje crediticio entre 300 y 850.
2. Si el score es >= 700 (Tier Gold/Platinum), la tasa de interés anual tiene un descuento del 4%.
3. Si el score está entre 600 y 699 (Tier Silver), la tasa tiene un descuento del 2%.
4. Si el score es < 600, requiere un fiador o rechazo automático si el DTI supera 35%.
Genera el SKILL.md con su YAML frontmatter, reglas detalladas y ejemplos de entrada/salida.
```

#### 👁️ Lo que verás en Antigravity 2.0:
1. Antigravity creará automáticamente la carpeta `.agents/skills/unicomer-scoring-engine/` y el archivo `SKILL.md`.
2. Estructura el YAML (`name: unicomer-scoring-engine`, `description: ...`) y las reglas de negocio en markdown limpio.
3. La habilidad queda **inmediatamente registrada** y lista para usarse en el proyecto.

---

### Ejercicio 2: Extraer una Habilidad a partir de Código Existente (*Pattern Extraction*)

Una de las funciones más potentes de Antigravity 2.0 es convertir buenas prácticas existentes en tu repositorio en habilidades corporativas reutilizables:

#### 📋 Prompt para Antigravity 2.0:
```text
Analiza cómo implementamos el enmascaramiento de DUI/NIT y la estructura de logs en 'main.py'. 
Extrae ese patrón y conviértelo en una habilidad corporativa llamada 'unicomer-pii-masking' dentro de '.agents/skills/unicomer-pii-masking'. 
Asegúrate de documentar las expresiones regulares para DUI salvadoreño (00000000-0) y teléfonos (+503), y cómo deben registrarse en los logs de Cloud Logging.
```

#### 👁️ Lo que verás en Antigravity 2.0:
- Antigravity inspecciona `main.py`, detecta el algoritmo de sanitización y crea una skill formal con especificaciones de seguridad y ejemplos de código.

---

### Ejercicio 3: Ejecutar y Probar la Nueva Habilidad en el Microservicio

Ahora pondremos a prueba la habilidad recién creada para refactorizar el código real:

#### 📋 Prompt para Antigravity 2.0:
```text
Utiliza nuestra nueva habilidad 'unicomer-scoring-engine' para agregar una función 'calculate_credit_score()' en 'main.py' y exponer un nuevo endpoint 'POST /api/v1/credit/score-and-evaluate'. 
Luego genera los tests correspondientes en 'test_main.py' y ejecuta pytest en el sandbox.
```

#### 👁️ Lo que verás en Antigravity 2.0:
1. El agente carga la habilidad `unicomer-scoring-engine`.
2. Aplica exactamente la matriz de descuentos (4% para Gold/Platinum, 2% para Silver).
3. Escribe las pruebas unitarias y las ejecuta en el sandbox validando que pasen al 100%.

---

### Ejercicio 4: Sincronización con el Equipo en GitHub

Para que todos los desarrolladores de Unicomer tengan acceso a estas habilidades en sus entornos locales o en VS Code:

```bash
# Guardar las nuevas habilidades en el repositorio compartido
git add .agents/skills/
git commit -m "feat(skills): add unicomer-scoring-engine and pii-masking skills"
git push origin main
```

Cualquier compañero de equipo que haga `git pull` en su rama tendrá las habilidades activas inmediatamente en su Antigravity 2.0, CLI o extensión de VS Code.

---

## ✅ Criterios de Éxito del Laboratorio
- [ ] Creaste una habilidad en Antigravity 2.0 usando únicamente un prompt en lenguaje natural.
- [ ] Extrajiste un patrón de seguridad desde código existente hacia una nueva habilidad.
- [ ] Ejecutaste la habilidad sobre `main.py` y verificaste las pruebas en el sandbox.
- [ ] Comprobaste cómo el versionado en Git (`.agents/skills/`) distribuye las habilidades a todo el equipo.
