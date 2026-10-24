# Selección de componentes STT

Revalidación por API GitHub: 24-10-2026. Fuente secundaria: EMCY3233/STT-Monster-Hunter-Project, main f199bd07b4e05ee4f7e56ed616840518374f3300. Todas las PR siguientes continúan abiertas y sin fusionar. No se incorpora su implementación en esta base.

| PR | Head revisado | Candidato reutilizable | Evidencia disponible y dependencia |
|---|---|---|---|
| [39](https://github.com/EMCY3233/STT-Monster-Hunter-Project/pull/39) | 9174a7cac52ca6b51af7aafe5a70ac66c72f6be1 | Inspección estructural de contenedores | CI Container inspector satisfactoria; autor declara 68 pruebas Debug/Release. No ejecuta el juego. zlib es dependencia externa con licencia propia. |
| [45](https://github.com/EMCY3233/STT-Monster-Hunter-Project/pull/45) | d91eb729647cea45dbd099a3fd03e4bded75796d | Banco acotado de equivalencia A32/C++17 | CI de equivalencia satisfactoria; 21 fixtures y 5376 estados sintéticos declarados. No recompilador general. |
| [48](https://github.com/EMCY3233/STT-Monster-Hunter-Project/pull/48) | 0c65b13b98bd3bb52c454fa3df0587cb0d0e44db | Contrato del decodificador | Depende de #45, cuya rama es su base. CI específica satisfactoria; 4096 inmediatos sintéticos. |
| [50](https://github.com/EMCY3233/STT-Monster-Hunter-Project/pull/50) | 7bf782de498bb55160d3b51b960b8f72f0e428da | Auditoría de MH4UltimateDC | Documentación; CI genérica no valida un port. |
| [51](https://github.com/EMCY3233/STT-Monster-Hunter-Project/pull/51) | 5afb59a4934b6b950fec4fec9f88d6fce56e8de1 | Matriz regional y etapas R0–R7 | Documentación sin ensayos ejecutados por la contribución. Revisión regional pendiente. |
| [52](https://github.com/EMCY3233/STT-Monster-Hunter-Project/pull/52) | 784b17ea109fcbc6b09f3231bc2f086915ce570c | Propuesta de perfiles | JSON sintético comprobado; selector normativo todavía propuesto. Conciliar con #50/#51 antes de adoptar contrato definitivo. |

Los resultados de las PR se atribuyen a sus autores y a CI remota; no son nuevas ejecuciones locales de este proyecto. Las ramas ajenas permanecen intactas. La revisión del árbol raíz STT no encontró LICENSE: antes de importar cualquier archivo deben aclararse sus permisos, avisos por archivo y dependencias, además de obtener revisión del cambio concreto. La propiedad del repositorio no sustituye esa comprobación.

MH4UltimateDC en e06b0ca30b9b2d66ec7785f277ead4bb35374b28 incluye GPL-3.0; su incorporación requiere revisar obligaciones del componente y combinación elegidos. REA, Azahar y 3dsrecomp se mantienen como referencias: fijar commit y revisar su licencia y subdependencias antes de copiar o enlazar código. Ninguna implementación externa está vendorizada aquí.

Ruta técnica: MH4UltimateDC + REA/Ghidra + Azahar. Evaluar 3dsrecomp/Zakuro solamente ante impedimento concreto del candidato principal. Este validador original de manifiestos es infraestructura local de inspección y no reemplaza sus recompiladores.

## Siguiente integración revisable

El responsable regional debe conciliar identidad/representación, mapa, modos, entradas, hooks y parámetros entre #50/#51/#52. Para cada correspondencia registrar ambos artefactos fijados, método, evidencia y discrepancia; una dirección coincidente no prueba equivalencia. Mantener perfiles reales en el laboratorio privado. Solicitar revisión antes de importar código STT; conservar #48 después de #45 si finalmente se selecciona su banco.
