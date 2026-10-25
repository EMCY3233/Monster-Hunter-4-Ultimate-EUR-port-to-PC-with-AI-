# Procedencia y permiso de traslado

Origen: EMCY3233/STT-Monster-Hunter-Project, PR39, commit
9174a7cac52ca6b51af7aafe5a70ac66c72f6be1, revisado el25/10/2026.
Historial Git: doce commits con autor registrado Codex; esa etiqueta no identifica
por sí sola al titular legal. No se atribuye automáticamente al propietario del
repositorio la titularidad de contribuciones de terceros.

El25/10/2026 el usuario de este proyecto autorizó expresamente:
«utiliza el lector estructural c++17 y fusiona o traslada el pr en el que se
encuentra al repositorio de este proyecto. doy permisos».
Esta integración registra ese permiso específico de traslado entre proyectos.
No constituye una licencia general nueva, ni una afirmación de titularidad
verificada, ni una concesión de derechos sobre componentes de terceros.
La licencia general del código propio sigue sin estar especificada; no atribuirle
MIT, zlib u otros términos. Para reutilizaciones posteriores debe aclararse el
alcance de derechos con el responsable del proyecto.

Archivos seleccionados: main.cpp, decompression.hpp, signature_resource.hpp,
test_inspector.py, CMakeLists.txt, README.md y THIRD_PARTY_NOTICES.md.
Código funcional, suite y CMake del componente conservados desde el commit.
README adaptado a las rutas del destino; CMake raíz y CI añadidos para integración.
No se importa RESEARCH.md ni otras propuestas STT. La PR39 original no se modifica.

zlib1.3.2 conserva su licencia y atribución en THIRD_PARTY_NOTICES.md.
Su descarga oficial tiene SHA256
bb329a0a2cd0274d05519d61c667c062e06990d72e125ee2dfa8de64f0119d16.
Windows utiliza BCrypt del sistema; Linux requiere OpenSSL::Crypto del sistema.
Registrar versiones y avisos aplicables si se distribuyen esas dependencias.

El lector abre la imagen en solo lectura. No incluye ROM, claves, recursos,
capturas, partidas, ejecutables comerciales ni código derivado del juego.
verify_profile.py permanece separado y no interpreta estos contenedores.

## Cierre de revisión de permisos — 25/10/2026

Estado: **borrador; no listo para fusión por autorización incompleta**.

La orden del usuario acredita permiso operativo para el traslado a este
repositorio y su PR pública. No acredita por sí sola la titularidad o facultad
para conceder derechos de todos los componentes. No se ha localizado una
declaración que concrete modificación y redistribución previstas en fuente
y binario, atribución, condiciones o excepciones de terceros. No presentar
el permiso de traslado como licencia general ni como revisión jurídica cerrada.

| Componente | Evidencia de autoría/titularidad | Términos y estado |
|---|---|---|
| Código, suite y CMake originales del lector | Doce commits Git con autor/committer Codex; PR presentada por EMCY3233. Titular humano/entidad no identificado mediante esos datos | Licencia explícita propia no localizada. Modificación y redistribución requieren aclaración del titular/representante |
| Documentación propia de origen seleccionada | Misma cadena Git; README adaptado en destino | Conservar procedencia; no extender licencia de zlib al texto propio |
| Integración CMake raíz y CI del destino | Cambio preparado para este proyecto con autorización humana | No sustituye permisos sobre el código importado |
| zlib1.3.2 | Aviso Jean-loup Gailly y Mark Adler y archivo oficial fijado | Licencia zlib independiente; conservar aviso y marcar modificaciones de esa biblioteca si las hubiera |
| OpenSSL Linux / BCrypt Windows | Dependencias del sistema, no vendorizadas | Registrar versión y términos del artefacto si se distribuyen; consultar THIRD_PARTY_NOTICES.md |

La revisión de historial fijado no halló LICENSE/COPYING general, encabezados
de licencia propia ni trailers de coautoría. Eso no prueba ausencia de derechos
o colaboradores. RESEARCH del origen declara consulta de formatos sin copia;
se conserva como declaración de procedencia, no certificación exhaustiva.

### Declaración concreta pendiente

El contacto inicial de procedencia es la persona responsable de la cuenta
EMCY3233 que encargó/publicó la PR39; no se la declara titular verificado.
Debe identificar al titular o representante facultado. Se solicita:

- Identidad de persona/entidad y facultad para autorizar los archivos propios
  de PR39 fijados en9174a7cac52ca6b51af7aafe5a70ac66c72f6be1.
- Confirmación del alcance para publicación, copia, modificación y
  redistribución en fuente/binario en este proyecto.
- Licencia o permiso específico con condiciones, atribución y avisos;
  indicar contribuciones o acuerdos de terceros que queden excluidos.

No se añadirá una licencia unilateralmente ni se inferirán facultades del
control de ambos repositorios. La consulta se dirige al usuario responsable
del proyecto; no se han enviado mensajes a terceros no identificados.
PR39 y PR4 permanecen intactas. No fusionar PR5 automáticamente.
