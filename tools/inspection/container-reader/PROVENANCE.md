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
