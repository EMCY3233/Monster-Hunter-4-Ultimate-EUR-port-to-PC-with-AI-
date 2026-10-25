# Evaluación del lector de contenedores — 25/10/2026

Origen evaluado: [STT PR39](https://github.com/EMCY3233/STT-Monster-Hunter-Project/pull/39), commit `9174a7cac52ca6b51af7aafe5a70ac66c72f6be1`.

## Resultado reproducido

En un laboratorio Windows x64 aislado se compilaron Release y Debug y pasaron las 68 pruebas sintéticas en cada configuración. CTest Release pasó 1/1: ejecuta la misma suite, no añade cobertura independiente. Se comprobó el archivo oficial zlib 1.3.2 contra el SHA-256 fijado por CMake. Linux y sanitizadores no se ejecutaron localmente.

El alcance evaluado comprende NCSD/NCCH, ExeFS, índices RomFS/IVFC y validación acotada ARC19/zlib. No se incorporan código externo, binarios, entradas comerciales, capturas ni resultados privados en esta contribución.

## Decisión

Integración de código aplazada: el árbol completo del commit solo contiene `container-inspector/THIRD_PARTY_NOTICES.md`, con licencia y atribución de zlib. No se localizó una licencia explícita del código propio del lector. Antes de importarlo hay que registrar los términos aplicables del titular y la atribución compatible con las instrucciones de colaboración del destino. No inferir una licencia del carácter público del repositorio ni extender la licencia de zlib al código propio.

Una vez resuelto, preparar una contribución mínima en una rama y PR independientes; no modificar ni fusionar automáticamente la PR de origen. `verify_profile.py` permanece separado para perfiles del ejecutable/AOT.

## Límites y continuidad

La inspección no ofrece extracción, descifrado, reconstrucción, autenticación con ancla confiada ni decodificación semántica general TEX/MOD/MRL/LMT. Un retorno cero no prueba autenticidad, gameplay ni AOT completo. La evidencia comercial y sus hashes se conservan exclusivamente en el laboratorio privado.

Inspector ROM Python v2: **NO LOCALIZADO — RECUPERACIÓN PENDIENTE** dentro del ámbito ya documentado. No repetir búsquedas ni reconstruirlo; reactivar solo ante nuevas rutas, adjuntos o evidencias. Esta recuperación y la licencia del lector no detienen el tutorial original ni la ampliación AOT en los chats existentes.
