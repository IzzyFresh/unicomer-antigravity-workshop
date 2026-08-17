# 🧪 Laboratorio 1: Fundamentos de Antigravity y el Bucle Plan-Act-Verify

**Audiencia:** Desarrolladores e Ingenieros de Software de Unicomer  
**Tiempo estimado:** 25 - 30 minutos  
**Objetivo:** Familiarizarse con la interfaz de Antigravity (VS Code o CLI), comprender el ciclo `Plan → Act → Verify` y resolver un requerimiento real en el microservicio de crédito retail.

---

## 🎯 Escenario de Negocio

El equipo de negocio de **La Curacao** reporta que el cálculo del ratio de endeudamiento (*Debt-to-Income DTI*) en el microservicio `unicomer-sample-app` no está utilizando la fórmula formal de amortización financiera francesa, lo que produce ligeras discrepancias en las cuotas mensuales de financiamiento.

---

## 👣 Paso a Paso del Laboratorio

### Paso 1: Exploración del Proyecto y Contexto
1. Abre el proyecto en VS Code o en tu terminal:
   ```bash
   cd labs/unicomer-sample-app
   ```
2. Inicia una conversación con **Antigravity** pidiendo un análisis del proyecto:
   > *"Explica la estructura de este microservicio, qué librerías utiliza y cuáles son los endpoints principales expuestos."*
3. Observa cómo Antigravity lee los archivos relevantes (`main.py`, `requirements.txt`, `test_main.py`) sin requerir que copies y pegues código manualmente en una ventana de chat.

---

### Paso 2: Fase 1 - PLAN (Generación del Implementation Plan)
1. Envía el siguiente prompt a Antigravity:
   > *"Necesito corregir el cálculo de cuotas mensuales en `main.py` para usar la fórmula estándar de cuota fija nivelada: Cuota = P * [ r(1+r)^n ] / [ (1+r)^n - 1 ]. Por favor, genera un Implementation Plan detallando qué funciones modificarás y los riesgos potenciales."*
2. **Revisa el artefacto generado:**
   - Observa cómo Antigravity genera un archivo de plan interactivo (`implementation_plan.md`).
   - Revisa la lista de cambios propuestos y el análisis de impacto.
   - Haz clic en **"Proceed"** o responde *"Acepto el plan, procede con la implementación"*.

---

### Paso 3: Fase 2 - ACT (Aplicación Atómica de Cambios)
1. Antigravity aplicará las modificaciones necesarias en `main.py`.
2. Observa el visor de **Diffs**:
   - Nota que Antigravity realiza ediciones dirigidas conservando la documentación existente y comentarios de negocio.
   - Revisa la función modificada `evaluate_credit`.

---

### Paso 4: Fase 3 - VERIFY (Ejecución de Pruebas en Sandbox)
1. Pide a Antigravity que verifique los cambios:
   > *"Ejecuta la suite de pruebas con pytest para verificar que los cambios no hayan roto el comportamiento existente."*
2. Antigravity ejecutará el comando de consola de forma segura (respetando la política de revisión).
3. Si alguna prueba existente falla debido a los nuevos decimales calculados, pide al agente:
   > *"Ajusta las aserciones de `test_main.py` para reflejar la precisión de la nueva fórmula financiera y vuelve a correr los tests."*

---

## ✅ Criterios de Éxito
- [ ] Has generado y aprobado tu primer *Implementation Plan*.
- [ ] Los diffs de código fueron revisados visualmente.
- [ ] La suite de pruebas de `pytest` ejecutó exitosamente con 100% de tests pasando.
