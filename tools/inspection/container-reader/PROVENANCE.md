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

## Declaración del solicitante y alcance autorizado — 25/10/2026

El usuario responsable de este proyecto confirmó: «se creo para mi al ordenar
la creacion del port del juego a C++». Se registra como declaración de que
encargó el lector y fue creado para él; no se atribuye titularidad a la
herramienta Codex ni se presenta una determinación jurídica independiente.

Esta aclaración se lee junto con sus órdenes previas de usar/trasladar el
lector a este repositorio, «doy permisos» y «publica general». Se conserva
como autorización específica documentada para incorporar y publicar la
contribución en este proyecto y efectuar las adaptaciones de integración
solicitadas. No se inventa una licencia estándar, una cesión de terceros
ni un permiso universal de sublicencia o reutilización ajena al proyecto.
La licencia pública general continúa sin especificarse.

El bloqueo de identificar a Codex como supuesto titular queda corregido:
Codex figura como herramienta/autor Git; el solicitante humano declara haber
encargado y recibido el trabajo y autoriza la incorporación/publicación.
Esta revisión acepta esa declaración para el alcance concreto solicitado,
sin garantizar derechos sobre materiales de terceros no declarados.

| Componente | Procedencia / autorización | Condiciones conservadas |
|---|---|---|
| Código, suite y CMake del lector | STT PR39 en el commit fijado; trabajo encargado por el usuario para él y traslado/publicación autorizados en este proyecto | Mantener procedencia; no asignar licencia general unilateralmente |
| README adaptado e integración del destino | Modificaciones necesarias para la integración solicitada | Identificar adaptaciones y preservar atribuciones originales |
| zlib1.3.2 | Gailly/Adler; licencia zlib independiente | Conservar aviso y origen; marcar modificaciones de la biblioteca si las hubiera |
| OpenSSL Linux / BCrypt Windows | Dependencias del sistema, no vendorizadas | Aplicar términos de la versión realmente distribuida si en el futuro se empaquetan |

Se conserva la atribución factual a STT PR39 y a su historial Git. No se añade
un copyright nominal no declarado por el usuario. Las autorizaciones del
proyecto no alcanzan ROM, claves, recursos comerciales, código derivado del
juego ni implementaciones ajenas. La fuente declarada en RESEARCH del origen
indica consulta de formatos sin copia; no equivale a garantía exhaustiva.

La aclaración sustituye el bloqueo documental anterior para esta incorporación.
La revisión técnica y la CI deben corresponder al commit final. PR39 y PR4
permanecen intactas; no fusionar PR5 automáticamente.
