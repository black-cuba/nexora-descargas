# nexora-descargas

Pagina publica de descargas de la **Suite NEXORA**. Solo **releases autorizados** de las aplicaciones NEXORA.

**URL publica (GitHub Pages):** https://black-cuba.github.io/nexora-descargas/

## Apps incluidas
| App | Plataforma | Prefijo de release | Repo de codigo (privado) |
|---|---|---|---|
| Sistema MultiAlmacen v3 | Windows EXE | `multialmacen-v3.0.*` | `SISTEMA-MULTIALMACEN-V3.0.0` |
| POS Movil v2 | Android APK | `pos-v2.0.*` | `Sistema-movil-multialmacen` |
| RRHH v1 | Windows EXE | `rrhh-v1.0.*` | `NEXORA_RRHH` |

## Como funciona

1. El cliente abre la pagina publica y consulta los releases de **este** repo via GitHub API (`/releases?per_page=100`).
2. El `index.html` agrupa los releases por prefijo (`multialmacen-`, `pos-`, `rrhh-`) y muestra la **ultima version de cada app** con boton de descarga directa.
3. Cuando el desarrollador hace un build, el workflow de cada repo **privado** genera el instalador y lo publica:
   - En su propio repo privado (como hasta ahora), y ademas
   - En **este** repo publico con el tag con el prefijo correspondiente.

> **El cliente NUNCA ve el codigo fuente** (los 3 repos de codigo son privados). Solo ve los releases subidos a este repo publico.

## Como subir un release manualmente (si no se configura el token)

```bash
# MultiAlmacen
gh release create multialmacen-v3.0.60 release/*.exe distribucioN/certificado-firmado.cer --repo black-cuba/nexora-descargas
# POS
gh release create pos-v2.0.31 app/build/outputs/apk/release/*.apk --repo black-cuba/nexora-descargas
# RRHH
gh release create rrhh-v1.0.1 release/*.exe --repo black-cuba/nexora-descargas
```

## Despliegue automatico (workflows)

Cada repo privado tiene un workflow que en cada build publica el release tambien en este repo, usando un secreto `NEXORA_DEPLOY_TOKEN` (PAT con permiso `repo` del owner `black-cuba`). Ver `build-windows-exe.yml` / `build.yml` de cada repo.

## Licencia

Suite NEXORA — descarga autorizada solo a licenciatarios. Ver `docs/CONTRATO-SUITE-NEXORA.md`.