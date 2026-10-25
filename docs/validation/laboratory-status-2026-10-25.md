# Resultados de laboratorio — 25 de octubre de 2026

Este resumen original comunica resultados revisados por el coordinador. No incorpora el laboratorio privado al repositorio ni proporciona un ejecutable del juego. La base pública y los experimentos privados son entregables distintos.

## Estado comprobado

| Trabajo | Estado | Evidencia revisada y límite |
|---|---|---|
| Función real EUR recompilada | Completado con pruebas acotadas | Comparación ARM/nativo de una función y sus dependencias, con entradas controladas y comprobaciones de estado. No certifica todas las funciones ni todos los estados ARM/VFP. |
| Menú original en runtime híbrido | Completado con pruebas | Capturas del menú y respuesta a selección; contador confirma ejecución de una función nativa durante el arranque. El resto puede ejecutarse mediante ARM_DynCom. |
| Options en híbrido restringido | Completado con pruebas | Abre Game Settings y vuelve al menú sin editar ajustes. Ejecución de 40 segundos emulados, salida 0, sin timeout; imágenes clave iguales a la referencia anterior. |
| New Game en el mismo híbrido | Completado con pruebas | Editor abierto y cancelación completa al menú, sin completar personaje. Hashes de entradas y binarios invariables; una llamada a la función nativa observada. |
| Continue en el mismo híbrido | Completado con pruebas | Tres ranuras vacías y regreso al menú. No se probó cargar una partida real. |
| DLC en el mismo híbrido | Completado con pruebas acotadas | Aviso de conexión y cancelación con regreso al menú. No se aceptó conexión ni descarga. |
| Language en el mismo híbrido | En curso | Último caso de la cola; falta aceptación visual final de apertura y regreso. |
| Cinco entradas del menú en JIT | Completado con pruebas acotadas | Ocho ejecuciones con perfiles aislados: cada entrada abre su pantalla y tiene al menos un regreso observado. No certifica todas las operaciones interiores. |
| Circle Pad Pro en JIT | Completado con pruebas | On → Off → On y regreso al menú. Las confirmaciones de la pantalla superior explican el resultado parcial inicial. No demuestra calibración ni hardware físico. |
| Idioma en JIT | Completado con pruebas acotadas | Francés aplicado y visible tras reiniciar el mismo perfil aislado. Pulsaciones sobrantes avanzaron al editor; este reinicio no certifica una ruta limpia hasta el menú. |

Las verificaciones híbridas no son AOT puro ni un port completamente independiente de emulación. Los resultados JIT no se extienden automáticamente al híbrido.

## Evidencia y reproducción

Responsables: validación diferencial/integración híbrida, laboratorio de runtime/JIT y coordinador de revisión. El laboratorio conserva recibos de cada caso con argumentos, perfiles aislados, hashes antes/después, salida y timeout, capturas de ambas pantallas y contadores cuando corresponde. El coordinador revisó las capturas de los hitos indicados.

Esta publicación contiene una síntesis de conclusiones; los recibos y materiales privados no se adjuntan. Por tanto, el lector público no puede reproducir de extremo a extremo los experimentos con este repositorio ni verificarlos de forma independiente solamente a partir de este documento. Tampoco existe aquí un commit público del runtime privado al que atribuir estos resultados. Los commits de esta documentación no son commits de implementación del juego.

Las pruebas automatizadas de infraestructura de la PR #1 son sintéticas y separadas de estas ejecuciones. Su CI no certifica el juego.

## Pendientes y dependencias

- Cerrar la aceptación visual de Language en el híbrido ya fijado, conservando los casos aprobados.
- Mantener pendientes la carga de partidas reales, descargas, calibración, gameplay y arranque AOT puro.
- La revisión comercial exacta y las correspondencias semánticas EUR/USA requieren evidencia adicional; direcciones coincidentes no bastan.
- Una incorporación pública del runtime requiere revisión técnica, procedencia, licencias y selección explícita de código redistribuible. No se incorporan implementaciones externas mediante este resumen.
- No inferir cobertura global ni porcentajes a partir de campañas que pueden solaparse.

## Corrección del diagnóstico

Los aparentes bloqueos de Circle Pad Pro e idioma se habían juzgado atendiendo solo a la pantalla inferior. La revisión de la pantalla superior identificó avisos y confirmaciones pendientes. Las secuencias corregidas resolvieron los casos JIT sin modificar servicios HLE. Los mensajes de infrarrojos no demostraban la causa de un fallo.

Este cambio publica documentación original de resultados y límites. No contiene ROM, recursos comerciales, capturas, claves, volcados, pseudocódigo, código derivado, direcciones internas ni rutas personales.
