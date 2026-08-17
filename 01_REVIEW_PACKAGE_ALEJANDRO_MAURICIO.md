# 📑 Paquete de Revisión: Taller Hands-On Antigravity 2.0 & Gemini Skills
## Documento de Alineación Técnica para Alejandro y Mauricio

**Fecha de Entrega para Revisión:** Viernes  
**Facilitador:** Israel Castillo (Google Cloud)  
**Destinatarios:** Alejandro, Mauricio  
**Enfoque del Repositorio:** **100% Práctico / Hands-On para Desarrolladores** *(La presentación ejecutiva de apoyo se gestionará en Google Slides por separado)*.

---

## 🎯 1. Resumen Ejecutivo y Propósito

Este paquete técnico prepara el **Taller Práctico (Hands-On Lab)** para el equipo de desarrollo de **Grupo Unicomer en El Salvador**. 

El objetivo es demostrar en código vivo la transición de herramientas de autocompletado tradicionales a **Ingeniería de Software Agéntica Autónoma** utilizando **Google Antigravity 2.0** y el modelo **Gemini 3.7 Flash** (con soporte integrado para VS Code).

### 🔑 Pilares del Taller Práctico:
1. **Flujo de Ingeniería de 3 Fases (*Plan → Act → Verify*):** Dejar que el agente analice el repositorio, genere planes de implementación interactivos (`implementation_plan.md`), aplique diffs atómicos y valide pruebas en sandbox.
2. **Creación de Habilidades de Código por Prompt:** Enseñar a los desarrolladores a estandarizar Clean Architecture y generación de pruebas Pytest usando lenguaje natural en Antigravity 2.0 (comparándolo con Claude Code).
3. **Subagentes en Paralelo (*Worktrees* Aislados):** Lanzar múltiples agentes concurrentes (Arquitecto, Auditor de Seguridad/PII y QA Engineer) que trabajan al mismo tiempo sin bloquear el editor.
4. **Integración Nativa con VS Code:** Cero fricción de adopción; los desarrolladores mantienen su editor habitual sincronizado en tiempo real con el harness de Antigravity 2.0.

---

## 🛠️ 2. Estructura de los Laboratorios Prácticos

| Módulo | Enfoque Técnico | Dinámica para los Desarrolladores de Unicomer |
| :--- | :--- | :--- |
| **Lab 1: Fundamentos y Plan-Act-Verify** | *Interfaz y Flujo Autónomo* | Conexión Antigravity 2.0 + VS Code. Diagnóstico del microservicio `unicomer-sample-app`, corrección de fórmulas financieras mediante *Implementation Plans* y verificación en sandbox. |
| **Lab 2: Habilidades de Ingeniería (Skills)** | *Arquitectura y Automatización* | Creación conversacional de habilidades (`fastapi-clean-architecture` y `pytest-mock-generator`), refactorización hacia capas modulares y sincronización con el equipo vía Git (`.agents/skills/`). |
| **Lab 3: Agentes Locales y Subagentes** | *Escalabilidad Multi-Agente* | Despliegue de 3 subagentes en paralelo con ramas/worktrees aislados (Arquitectura, Sanitización de PII y QA), configuración de un sidecar de calidad y generación del artefacto `walkthrough.md`. |

---

## 🔍 3. Integración con Visual Studio Code y Entorno de Desarrollo

- **Disponibilidad:** **General Availability (GA)** en el roadmap de Agosto.
- **Autenticación Corporativa:** Soporte nativo para *Application Default Credentials (ADC)* y *Workload Identity Federation (WIF)* sin requerir API keys manuales.
- **Sincronización Git-Native:** Las habilidades y reglas guardadas en `.agents/` en el repositorio se distribuyen a todos los desarrolladores automáticamente con un simple `git pull`.

---

## 📝 4. Rúbrica de Validación para la Sesión del Viernes

Por favor validar los siguientes puntos:
- [ ] **Enfoque 100% de Desarrollo:** ¿Los ejercicios de refactorización hacia Clean Architecture, generación de Pytest y auditoría de PII son representativos para los desarrolladores de Unicomer?
- [ ] **Herramientas:** ¿Se confirma el uso de **Antigravity 2.0 (GUI)** + **VS Code** para todos los participantes?
- [ ] **Repositorio de Trabajo:** El repositorio público de GitHub está listo para ser clonado por los desarrolladores:  
  👉 `https://github.com/IzzyFresh/unicomer-antigravity-workshop`
