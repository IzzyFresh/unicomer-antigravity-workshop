# 💳 Microservicio de Evaluación de Crédito y Lealtad Retail (Unicomer)

Este proyecto sirve como base práctica para los laboratorios del **Google Antigravity & Gemini Skills Deep Dive**.

---

## 🏗️ Requisitos Previos

- Python 3.10 o superior
- `pip` o entorno virtual (`venv`)
- Antigravity CLI o Extensión de VS Code con modelo **Gemini 3.7 Flash**

---

## 🚀 Instalación y Ejecución Local

```bash
# 1. Crear entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar suite de pruebas
pytest -v

# 4. Iniciar servidor FastAPI local
uvicorn main:app --reload --port 8000
```

---

## 🎯 Retos Prácticos en el Taller

Durante los laboratorios utilizaremos **Antigravity** para:
1. **Lab 1:** Implementar el cálculo formal de DTI y amortización financiera bajo el ciclo `Plan → Act → Verify`.
2. **Lab 2:** Inyectar y aplicar la habilidad corporativa `unicomer-credit-policy` para validar reglas de negocio en El Salvador y la región (límites por marca *La Curacao, Gollo, RadioShack, Emma*).
3. **Lab 3:** Desplegar subagentes en paralelo para auditar el manejo de PII (eliminando DUI/Teléfono de logs) y generar una suite completa de pruebas unitarias que cubra casos de borde.
