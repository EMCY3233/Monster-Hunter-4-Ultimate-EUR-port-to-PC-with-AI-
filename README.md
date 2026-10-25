# Monster Hunter 4 Ultimate EUR — Port to PC with AI

Proyecto de investigación y desarrollo para llevar Monster Hunter 4 Ultimate, edición europea, a PC con ayuda de herramientas de inteligencia artificial.

Repositorio principal: [MH4U-PC](https://github.com/EMCY3233/Monster-Hunter-4-Ultimate-EUR-port-to-PC-with-AI-), rama main. STT es fuente secundaria; sus propuestas requieren selección y revisión antes de incorporarse.

## Estado y objetivo

Esta base proporciona inspección local de perfiles, pruebas sintéticas y un punto de entrada CMake/CTest. No contiene el juego ni un runtime integrado. La aceptación técnica exige primero una función EUR real recompilada con comparación ARM/nativo reproducible y después inicialización y menú original interactivo mediante el runtime elegido. Las pruebas sintéticas de esta base no satisfacen esos hitos.

Ruta principal: MH4UltimateDC + REA/Ghidra + Azahar. 3dsrecomp/Zakuro es alternativa ante un bloqueo demostrado. Consultar [selección STT y licencias](docs/research/stt-inventory.md) antes de reutilizar implementaciones.

## Resultados revisados

Consultar el [estado de laboratorio del 25-10-2026](docs/validation/laboratory-status-2026-10-25.md): función EUR real validada de forma acotada, menú original y varias selecciones comprobadas en runtime híbrido. Son experimentos privados revisados; este repositorio no distribuye el runtime ni un port jugable. Se distinguen los resultados JIT, híbridos y los objetivos AOT pendientes.

## Organización

- tools/inspection: validación original de manifiestos y artefactos locales.
- tests: casos reproducibles sin archivos comerciales.
- docs: arquitectura, compatibilidad, investigación y validación.
- CMakeLists.txt y .github/workflows: ejecución de las comprobaciones.

src/include y herramientas de recompilación se añadirán cuando exista código original o una integración revisada que alojar. No se crean componentes vacíos ni otro recompilador general.

## Pruebas

Requiere Python 3.11 o posterior; para CTest, CMake 3.20 o posterior.

```sh
python -B -m unittest discover -s tests -v
cmake -S . -B build
ctest --test-dir build -C Debug --output-on-failure
```

Los comandos solo validan infraestructura y ejemplos sintéticos. Los perfiles reales y los resultados del juego se conservan fuera del árbol público. Consulta la [guía experimental de validación local](docs/validation/local-profiles.md) antes de invocar el inspector; su formato no constituye el contrato regional definitivo.

## Colaboración y protección

El propietario autoriza a los chats REA PC MH4U + Others a colaborar. Leer AGENTS.md, coordinar propietarios de archivos, trabajar en ramas y solicitar revisión mediante PR; no fusionar automáticamente. Conservar procedencia, commits, dependencias, pruebas y bloqueos. Distinguir completado con pruebas, en curso, pendiente, bloqueado y experimental.

No incorporar ROM, claves, recursos comerciales, volcados, pseudocódigo ni código recompilado derivado del juego. Usar copias privadas aisladas; mantener originales, REA activa, ramas ajenas y PS Vita intactos. .gitignore es una ayuda y requiere revisar el contenido concreto de cada publicación.

No se concede aquí una licencia nueva para código ajeno. Resolver licencias y atribución antes de cada importación. [CHANGELOG.md](CHANGELOG.md) registra los cambios incorporados en la rama correspondiente.
