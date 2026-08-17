# 🧪 Laboratorio 3: Subagentes Autónomos en Paralelo y Auditoría de Seguridad

**Audiencia:** Desarrolladores, Ingenieros de Seguridad y DevOps de Unicomer  
**Tiempo estimado:** 30 - 35 minutos  
**Objetivo:** Utilizar la capacidad de **Subagentes** de Antigravity para delegar múltiples tareas complejas en paralelo (auditoría de seguridad de PII, generación de cobertura de pruebas y documentación de entrega).

---

## 🎯 Escenario de Negocio

Antes de liberar el microservicio a producción en el clúster de Google Cloud / Cloud Run de Unicomer, el equipo de Ciberseguridad y QA exige:
1. **Auditoría de PII (Información Personal Identificable):** Eliminar o enmascarar los números de DUI/NIT y teléfonos en los logs de la aplicación.
2. **Cobertura de Pruebas de Borde (Edge Cases):** Pruebas para valores extremos (ingreso cero, cuotas máximas, términos de 60 meses, clientes Platinum).
3. **Reporte de Auditoría y Walkthrough:** Un documento consolidado que detalle todos los cambios realizados para el pase a producción.

---

## 👣 Paso a Paso del Laboratorio

### Paso 1: Delegación a Subagentes en Paralelo
1. Envía el siguiente prompt al Lead Agent de Antigravity:
   > *"Por favor lanza subagentes especializados en paralelo para preparar este servicio para producción:*
   > *1. Un subagente 'Security Auditor' que identifique fugas de PII en `main.py` y enmascare los identificadores en los logs.*
   > *2. Un subagente 'QA Test Engineer' que cree una suite exhaustiva de casos de borde en `test_main.py`.*
   > *3. Consolidar los resultados y verificar que todas las pruebas pasen al 100%."*

---

### Paso 2: Observación de la Ejecución de Subagentes
1. Observa cómo Antigravity:
   - Crea subagentes con roles dinámicos y prompts especializados.
   - Ejecuta las tareas en paralelo sin bloquear tu terminal o conversación principal.
   - Recibe los reportes y diffs generados por cada subagente.

---

### Paso 3: Revisión de Cambios de Seguridad
1. El subagente de Seguridad habrá reemplazado:
   ```python
   # Antes (Inseguro):
   logger.info(f"Evaluating credit for customer_id={request.customer_id}, name={request.customer_name}, phone={request.phone_number}")
   
   # Después (Seguro / Enmascarado):
   masked_id = request.customer_id[:4] + "****" + request.customer_id[-2:] if len(request.customer_id) >= 6 else "****"
   logger.info(f"Evaluating credit for customer_id={masked_id}, brand={request.brand}, tier={request.tier}")
   ```

---

### Paso 4: Verificación Final y Creación del Walkthrough
1. Pide a Antigravity:
   > *"Ejecuta la suite completa de pruebas en el sandbox y genera un artefacto `walkthrough.md` resumiendo las mejoras aplicadas, las vulnerabilidades mitigadas y las métricas de cobertura."*
2. Revisa el artefacto de cierre generado.

---

## ✅ Criterios de Éxito
- [ ] Se ejecutaron subagentes en paralelo de forma autónoma.
- [ ] La vulnerabilidad de PII en logs fue remediada con éxito.
- [ ] La suite de pruebas cubre casos de borde y ejecuta con 100% de éxito.
- [ ] Se generó un artefacto de walkthrough listo para revisión por el Tech Lead.
