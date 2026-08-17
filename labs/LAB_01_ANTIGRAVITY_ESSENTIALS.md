# 🧪 Laboratorio 1: Fundamentos de Antigravity 2.0 y el Bucle Plan-Act-Verify

**Audiencia:** Desarrolladores e Ingenieros de Software de Unicomer  
**Tiempo estimado:** 25 - 30 minutos  
**Superficie de Trabajo:** **Antigravity 2.0 (GUI) + Extensión de Visual Studio Code**  
**Objetivo:** Familiarizarse con la interfaz visual de Antigravity 2.0, su integración nativa con VS Code, y ejecutar el ciclo `Plan → Act → Verify` para modernizar el microservicio de crédito retail.

---

## 🖥️ 1. Entorno de Trabajo: Antigravity 2.0 + VS Code

Durante este taller utilizaremos la combinación más productiva para desarrolladores:
* **Antigravity 2.0 (GUI):** Tu panel de control agéntico principal para orquestar planes, ver artefactos interactivos, disparar subagentes y monitorear tareas.
* **Visual Studio Code:** Tu editor de confianza donde se sincronizan automáticamente los archivos, diffs y reglas del repositorio.
  * 📦 **Instalar Extensión en VS Code:** [Marketplace Link](https://marketplace.visualstudio.com/items?itemName=Google.antigravity)
  * ⚡ **Instalación Directa:** [`vscode:extension/Google.antigravity`](vscode:extension/Google.antigravity)

```
+------------------------------------+------------------------------------+
|        Visual Studio Code          |         Antigravity 2.0 (GUI)      |
|  - Editor de código activo         |  - Panel conversacional            |
|  - Diffs interactivos integrados   |  - Planes interactivos (Artifacts) |
|  - Terminal / Extension Panel      |  - Bandeja de Subagentes           |
+------------------------------------+------------------------------------+
                   \                             /
                    \--- Antigravity Harness ---/
```

---

## 👣 Paso a Paso del Laboratorio

### Paso 1: Abrir el Proyecto en Antigravity 2.0 y VS Code
1. Abre la carpeta `unicomer-sample-app` en tu **Visual Studio Code**.
2. Abre **Antigravity 2.0** y selecciona el workspace del proyecto.
3. Envía tu primer mensaje conversacional en Antigravity 2.0:
   > *"Analiza la estructura de este microservicio: qué librerías utiliza, cuáles son los endpoints principales en `main.py` y qué cobertura de tests tenemos actualmente."*
4. Observa cómo Antigravity 2.0 inspecciona el workspace sin necesidad de que copies ni pegues código manualmente.

---

### Paso 2: Fase 1 - PLAN (Generación del Implementation Plan Interactivo)
1. En el panel de chat de Antigravity 2.0, ingresa el siguiente requerimiento técnico:
   > *"Necesito corregir el cálculo de cuotas mensuales en `main.py` para usar la fórmula formal de amortización francesa: Cuota = P * [ r(1+r)^n ] / [ (1+r)^n - 1 ]. Por favor, genera un Implementation Plan detallando las funciones afectadas, riesgos y la estrategia de verificación."*
2. **Revisa el artefacto visual generado:**
   - En el panel derecho de Antigravity 2.0 aparecerá un artefacto interactivo (`implementation_plan.md`).
   - Revisa la lista de verificación y haz clic en el botón azul **"Proceed"** (o escribe *"Acepto el plan, procede"*).

---

### Paso 3: Fase 2 - ACT (Revisión Visual de Diffs en Antigravity 2.0 y VS Code)
1. Antigravity 2.0 aplicará las modificaciones en `main.py`.
2. **Inspecciona los Diffs:**
   - En Antigravity 2.0 y en tu VS Code verás los bloques de diff resaltados en verde (adiciones) y rojo (eliminaciones).
   - Observa que las ediciones son atómicas y preservan la documentación previa y los tipos de Pydantic.

---

### Paso 4: Fase 3 - VERIFY (Ejecución en Sandbox y Feedback en Tiempo Real)
1. Solicita la verificación en el chat de Antigravity 2.0:
   > *"Ejecuta la suite de pruebas de pytest en el sandbox para verificar que los cambios financieros sean matemáticamente exactos y no rompan los endpoints existentes."*
2. Antigravity 2.0 correrá la suite de forma aislada y te mostrará el resultado de la ejecución.
3. Si los decimales de la nueva fórmula requieren ajustar las aserciones en `test_main.py`, pídele:
   > *"Ajusta las aserciones de `test_main.py` a la precisión de la nueva cuota francesa y vuelve a validar."*

---

## 🔌 2. Nota sobre la Integración con Visual Studio Code
* **Sincronización Bidireccional:** Todo cambio aceptado en Antigravity 2.0 se refleja al instante en los archivos abiertos en VS Code.
* **Extensión de VS Code:** Si prefieres no salir de tu editor, puedes abrir el panel lateral de **Antigravity en VS Code** usando tu sesión corporativa autenticada vía ADC (Google Cloud).

---

## ✅ Criterios de Éxito
- [ ] Conectaste tu workspace en Antigravity 2.0 y VS Code.
- [ ] Generaste e interactuaste con tu primer *Implementation Plan* visual.
- [ ] Inspeccionaste los diffs de código generados por el agente.
- [ ] Ejecutaste la verificación en el sandbox con 100% de tests pasando.
