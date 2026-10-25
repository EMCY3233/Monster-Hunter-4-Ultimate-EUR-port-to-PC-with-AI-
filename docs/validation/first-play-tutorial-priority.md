# Prioridad: tutorial original y llegada a Val Habar

Orden del propietario recibida el 25-10-2026. Ruta principal: New Game → creación del cazador y Palico → tutorial introductorio de Dah'ren Mohran completo → Val Habar → guardado y Continue. No se exige AOT puro para comprobar esta primera secuencia; se conserva la ampliación AOT en paralelo.

## Estado revisado al establecer la prioridad

- Cinco selecciones del menú híbrido, incluido Language, ya verificadas: no repetir campañas aprobadas.
- Ensayo híbrido de creación activo: nombre MH4UPC observado y confirmación de finalizar cazador aceptada; falta terminar Palico.
- No hay evidencia revisada de inicio o superación del tutorial, llegada a Val Habar, guardado persistente o carga real de ese personaje.
- La salida de audio del runner es nula: sonido no verificado.
- El observador para seleccionar otra función EUR está preparado; todavía depende de una llamada real observada tras la creación o al comenzar el tutorial.

La confirmación del cazador no significa creación completa, guardado ni tutorial superado. Los resultados JIT, híbridos y AOT se registran por separado.

## Hitos y aceptación

| Hito | Cierre exigido | Estado inicial |
|---|---|---|
| T0 — Creación | Cazador y Palico confirmados mediante pantallas y respuestas del juego; perfil nuevo de laboratorio | En curso |
| T1 — Inicio original | Transición desde creación e inicio de la introducción, conservando eventos originales | Pendiente |
| T2 — Control del tutorial | Instrucciones y objetivos realmente mostrados, acciones enviadas y respuesta observable; registrar cada bloqueo | Pendiente |
| T3 — Encuentro | Encuentro con Dah'ren Mohran y cumplimiento de las condiciones que el juego exija, sin forzar progreso | Pendiente |
| T4 — Val Habar | Final original del tutorial y llegada visible a Val Habar, con respuesta a controles | Pendiente |
| T5 — Persistencia | Guardado normal, cierre y reinicio del proceso, Continue y mismo personaje/estado cargados | Pendiente |

No sustituir objetivos por suposiciones sobre mecánicas no observadas. Una cinemática, ausencia de errores o archivo existente no certifican superación ni persistencia. Si el juego ofrece guardar antes de Val Habar, conservar ese punto sin alterar la secuencia exigida ni dar T4/T5 por cumplidos.

## Responsables e interfaces de trabajo

- Runtime/Azahar: dueño exclusivo del ensayo activo, perfiles, entradas adaptativas y evidencia T0–T5. Continuar el proceso existente; no reiniciarlo para aplicar esta prioridad.
- REA/Ghidra: contratos y dependencias del punto observado; candidato AOT ligado a una llamada real de creación o tutorial. El análisis estático no demuestra ejecución.
- Diferencial/AOT: captura mínima de caller, destino y argumentos en copia propia; comparación ARM/nativo de funciones EUR reales y versión aislada. No sustituir la DLL del ensayo activo.
- Compatibilidad: revisión independiente de hitos y reproducciones mínimas de incompatibilidades concretas, sin campañas paralelas duplicadas.
- Coordinación: dependencias, revisión de resultados y contribuciones mediante ramas/PR. Utilizar los chats actuales.

Cada hito conserva responsable, identidad de artefactos, entradas/tiempos, evidencia visual de ambas pantallas, salida/timeout y límites. Para AOT, registrar también registros, banderas, memoria y retorno comparados. La llamada nativa ya validada debe conservarse; el éxito híbrido no demuestra AOT completo.

## Protección y siguiente acción

Continuar T0 en el ensayo activo y observar la transición a T1. Ante fallo, conservar el estado, registrar causa comprobada o incertidumbre y asignar una reproducción mínima antes de cambiar código.

No omitir eventos, forzar flags, introducir partidas ajenas o sustituir la secuencia por estados prefabricados. Preservar originales, baselines aceptados, instalaciones activas, ramas ajenas y PS Vita. Guardados, ROM, claves, capturas y código derivado permanecen privados. Publicar solo documentación original sanitizada o código redistribuible revisado; no fusionar automáticamente.

Después de T5: misiones y combate progresivos, con pruebas específicas de movimiento, interacción, ataques, impactos, IA y finalización.
