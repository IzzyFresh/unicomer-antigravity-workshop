# 🧪 Laboratorio 2: Creación y Uso de Habilidades Empresariales (Gemini Skills)

**Audiencia:** Desarrolladores y Líderes Técnicos de Unicomer  
**Tiempo estimado:** 25 - 30 minutos  
**Objetivo:** Aprender a codificar las reglas de arquitectura y negocio de Unicomer en habilidades modulares (`SKILL.md`), registrar reglas de repositorio (`GEMINI.md` / `AGENTS.md`) y dispararlas automáticamente o mediante comandos slash.

---

## 🎯 Escenario de Negocio

El área de Riesgo y Crédito de Unicomer ha establecido topes de financiamiento automatizado según la marca:
- **La Curacao:** Máximo \$3,500 USD
- **Gollo:** Máximo \$2,500 USD
- **Emma (Fintech):** Máximo \$1,500 USD
- **RadioShack:** Máximo \$1,000 USD

Además, la gerencia de Arquitectura exige que todo microservicio nuevo o modificado cumpla con la convención de URLs en kebab-case y un sobre estándar de respuesta de error (`unicomer-api-standards`).

---

## 👣 Paso a Paso del Laboratorio

### Paso 1: Instalación de la Skill en el Repositorio
1. Crea la carpeta de habilidades locales en el proyecto o cópiala desde `custom-skills/`:
   ```bash
   mkdir -p .agents/skills/unicomer-credit-policy
   cp ../../custom-skills/unicomer-credit-policy/SKILL.md .agents/skills/unicomer-credit-policy/
   ```
2. Revisa la estructura de `SKILL.md`:
   - Observa el encabezado YAML (`name`, `description`).
   - Revisa las reglas de DTI, topes por marca y protección de datos PII (DUI/NIT).

---

### Paso 2: Configuración de Reglas del Proyecto (`GEMINI.md`)
1. Crea o actualiza el archivo `GEMINI.md` en la raíz de tu proyecto para establecer lineamientos obligatorios:
   ```markdown
   # Reglas del Proyecto: Unicomer Retail APIs
   - Todos los endpoints deben seguir la habilidad `unicomer-api-standards`.
   - Toda lógica de evaluación crediticia debe validar las restricciones de `unicomer-credit-policy`.
   - Nunca dejar datos de identificación ciudadana (DUI/NIT) en logs planos.
   ```

---

### Paso 3: Aplicación de la Skill con Antigravity
1. Pide a Antigravity que aplique las políticas de crédito corporativas:
   > *"Por favor revisa `main.py` y aplica las restricciones de financiamiento máximo por marca y techos de DTI especificadas en nuestra habilidad `unicomer-credit-policy`. Si una solicitud supera el tope de la marca, debe ser rechazada o ajustada al tope máximo permitido."*
2. **Observa el comportamiento del agente:**
   - Antigravity detecta automáticamente la habilidad registrada.
   - Aplica los topes de \$3,500 para La Curacao, \$2,500 para Gollo, \$1,500 para Emma y \$1,000 para RadioShack.
   - Ajusta los mensajes de `decision_reason` con la justificación formal de negocio.

---

### Paso 4: Validación con Nuevas Pruebas
1. Pide a Antigravity:
   > *"Escribe nuevos tests en `test_main.py` que verifiquen los topes máximos para solicitudes de Emma ($1,500) y RadioShack ($1,000) asegurando que no se aprueben montos superiores, y ejecuta pytest."*
2. Verifica que las nuevas pruebas pasen con éxito.

---

## ✅ Criterios de Éxito
- [ ] La habilidad `unicomer-credit-policy` fue reconocida por Antigravity.
- [ ] Las reglas de negocio de Unicomer fueron implementadas sin ambigüedades.
- [ ] Se generaron pruebas específicas que validan los límites por marca.
