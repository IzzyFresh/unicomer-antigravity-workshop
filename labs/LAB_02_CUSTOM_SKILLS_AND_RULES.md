# 🧪 Laboratorio 2: Creación de Habilidades de Ingeniería de Software (Coding Skills) en Antigravity 2.0

**Audiencia:** Desarrolladores Backend, Arquitectos de Software e Ingenieros DevOps de Unicomer  
**Tiempo estimado:** 25 - 30 minutos  
**Superficie de Trabajo:** **Antigravity 2.0 (GUI / Web)**  
**Objetivo:** Aprender a crear **Habilidades de Codificación y Arquitectura de Software** mediante prompts en Antigravity 2.0 para automatizar el scaffolding de Clean Architecture, la generación exhaustiva de pruebas con mocks en Pytest y la refactorización asíncrona.

---

## 🎯 ¿Por qué Habilidades de Codificación (Coding Skills)?

Las habilidades en Antigravity no son solo para reglas de negocio; su mayor valor para los desarrolladores es **automatizar tareas repetitivas de arquitectura, calidad de código y patrones de diseño corporativos**:

1. 🏗️ **Architectural Scaffolding:** Forzar que todo nuevo microservicio o endpoint se estructure en capas limpias (Routers ➔ Services ➔ Repositories ➔ Schemas).
2. 🧪 **Test-Driven Automation:** Generar suites completas de Pytest con fixtures, mocks de clientes HTTP y pruebas parametrizadas de borde.
3. ⚡ **Async/Performance Standards:** Garantizar que todo I/O sea no bloqueante (`async`/`await`) y con manejo estricto de concurrencia.

---

## 👣 Ejercicios de Codificación del Laboratorio

### Ejercicio 1: Crear una Habilidad de Arquitectura Limpia (*FastAPI Clean Architecture*)

En lugar de explicarle a la IA en cada prompt cómo estructurar tu código, creamos una habilidad de ingeniería con un solo prompt:

#### 📋 Prompt para Antigravity 2.0:
```text
Crea una habilidad de ingeniería de software llamada 'fastapi-clean-architecture' en '.agents/skills/fastapi-clean-architecture/SKILL.md'.
La habilidad debe establecer que todo nuevo módulo o refactorización en Python FastAPI debe seguir:
1. Separación estricta en 4 capas: Routers (FastAPI Depends), Services (Lógica pura y excepciones tipadas), Repositories (Acceso a datos async), y Schemas (Pydantic v2 con tipado estricto).
2. Prohibido hacer llamadas directas a base de datos o lógica de negocio pesada dentro de los Routers.
3. Todo endpoint I/O debe ser asíncrono (async def).
4. Manejo centralizado de excepciones con HTTP Status Codes semánticos (400, 404, 422, 500).
Genera el archivo SKILL.md con YAML frontmatter y ejemplos de código completos.
```

#### 👁️ Lo que verás en Antigravity 2.0:
- Antigravity crea la carpeta y el `SKILL.md` estructurado.
- El agente ahora "sabe" cómo estructurar cualquier backend de Unicomer según este patrón de arquitectura limpia.

---

### Ejercicio 2: Probar la Habilidad Scaffolding un Nuevo Módulo de Código

Ahora le pedimos a Antigravity que use la habilidad recién creada para refactorizar `main.py` hacia una arquitectura limpia en capas:

#### 📋 Prompt para Antigravity 2.0:
```text
Aplica nuestra habilidad 'fastapi-clean-architecture' para refactorizar este proyecto monolítico:
1. Extrae los schemas a un archivo 'schemas.py'.
2. Mueve la lógica de cálculo y evaluación a 'services/credit_service.py'.
3. Deja los endpoints en 'routers/credit_router.py' usando inyección de dependencias con Depends().
4. Mantén 'main.py' como punto de entrada limpio que monte el router.
Muestra el plan de refactorización antes de proceder.
```

#### 👁️ Lo que verás en Antigravity 2.0:
- Antigravity genera un plan modular y divide el código limpio en capas sin romper la funcionalidad existente.

---

### Ejercicio 3: Crear una Habilidad de Generación Automatizada de Tests con Mocks

Creemos una segunda habilidad orientada a testing avanzado:

#### 📋 Prompt para Antigravity 2.0:
```text
Crea una habilidad llamada 'pytest-mock-generator' en '.agents/skills/pytest-mock-generator/SKILL.md'.
La habilidad debe instruir al agente a:
1. Crear fixtures reusables en 'conftest.py' usando TestClient de FastAPI.
2. Generar pruebas unitarias parametrizadas con '@pytest.mark.parametrize' para cubrir casos de borde (valores 0, negativos, strings vacíos, payloads malformados).
3. Mockear dependencias externas usando 'unittest.mock' o 'respx' sin hacer llamadas de red reales.
4. Apuntar a un mínimo de 90% de cobertura de ramas (branch coverage).
```

---

### Ejercicio 4: Ejecutar la Habilidad de Testing y Validar Cobertura en Sandbox

#### 📋 Prompt para Antigravity 2.0:
```text
Usa la habilidad 'pytest-mock-generator' para generar una suite de pruebas exhaustiva en 'tests/test_credit_service.py' que cubra todos los métodos de 'services/credit_service.py' con pruebas parametrizadas. 
Luego ejecuta pytest con reporte de cobertura en el sandbox de ejecución.
```

#### 👁️ Lo que verás en Antigravity 2.0:
- El agente genera pruebas parametrizadas profesionales con fixtures y asserts limpios.
- Ejecuta `pytest` en el sandbox y reporta los resultados de cobertura al 100%.

---

### Ejercicio 5: Compartir las Habilidades con el Equipo Vía Git

```bash
git add .agents/skills/
git commit -m "feat(engineering-skills): add clean-architecture and pytest-generator skills"
git push origin main
```

Todo el equipo de desarrollo de Unicomer que haga `git pull` dispondrá de estas dos herramientas de productividad de forma instantánea.

---

## ✅ Criterios de Éxito del Laboratorio
- [ ] Creaste una habilidad de arquitectura limpia para Python/FastAPI con un prompt.
- [ ] Refactorizaste código monolítico hacia una arquitectura modular en capas usando la habilidad.
- [ ] Creaste una habilidad de testing avanzado y generaste pruebas parametrizadas con fixtures.
- [ ] Ejecutaste y verificaste la suite de pruebas en el sandbox de Antigravity.
