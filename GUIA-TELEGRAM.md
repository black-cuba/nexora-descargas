# Guía de distribución de la Suite NEXORA (internet nacional de Cuba)

Estrategia para que tus clientes descarguen la Suite NEXORA desde la red
nacional: **canal de Telegram** como fuente principal y **página web pública**
(`nexora-descargas` en GitHub Pages) como vitrina de instaladores.

Telegram es el método más rápido y confiable en Cuba: reanuda descargas,
no depende de VPN y casi todos los clientes ya lo tienen instalado.

> **Importante**: el cliente **nunca accede a tus repositorios de código**.
> Todos los repos de código (MultiAlmacen, POS, RRHH) son **privados**. La
> página pública solo muestra los **releases autorizados** que se publican en
> el repo público `nexora-descargas`, y el cliente descarga desde esa página
> o desde Telegram.

---

## 1. Página pública de descargas (ya montada)

| Dato | Valor |
|---|---|
| Repo público | `black-cuba/nexora-descargas` |
| URL de la página | https://black-cuba.github.io/nexora-descargas/ |
| Contenido | `index.html` (auto-actualizable) + `GUIA-TELEGRAM.md` + `docs/CONTRATO-SUITE-NEXORA.md` |

### Cómo se actualiza sola

1. `index.html` consulta la API pública de releases de `nexora-descargas`
   (`/releases?per_page=100`) al abrirse.
2. Agrupa los releases por prefijo y muestra la **última versión** de cada app:
   - `multialmacen-*` → MultiAlmacen (Windows EXE)
   - `pos-*` → POS Móvil (Android APK)
   - `rrhh-*` → RRHH (Windows EXE)
3. Cada build que publica un release en el repo privado publica **también** un
   release con ese prefijo en `nexora-descargas` → la página refleja la nueva
   versión automáticamente. No hay que editar la página a mano.

### Cómo se publica un release del código → repo público

Cada repo privado tiene su workflow con un paso extra que publica el instalador
en `nexora-descargas` (usa el secreto `NEXORA_DEPLOY_TOKEN`):
- MultiAlmacen: `.github/workflows/build-windows-exe.yml` → `multialmacen-v3.0.N`
- RRHH: `.github/workflows/build-windows-exe.yml` → `rrhh-v1.0.N`
- POS: `.github/workflows/build.yml` → `pos-v2.0.N`

Si el secreto no existe, el paso se omite sin romper el build (puedes publicar
a mano con `gh release create <tag> <archivo> --repo black-cuba/nexora-descargas`).

---

## 2. Crear el canal de Telegram

1. En Telegram pulsa el icono del **lápiz** (Android) o el **menú** (PC) → **Nuevo canal**.
2. Nombre sugerido: **NEXORA Suite** · Usuario/alias: `NEXORA_Suite`.
3. Tipo: **Canal público** (para que cualquiera lo encuentre).
4. Al crearlo: **Editar canal → Administradores** y agrega un bot o segundo
   dispositivo tuyo como respaldo.

Quedará con enlace: `https://t.me/NEXORA_Suite`

---

## 3. Subir los instaladores al canal

Sube cada instalador como **archivo adjunto** en su propio mensaje:

| App | Archivo |
|---|---|
| MultiAlmacen EXE | `NEXORA-SistemaMultiAlmacen-SETUP-V3.0.N.exe` |
| POS Móvil APK | `Nexora-POS-v2.0.N.apk` |
| RRHH EXE | `NexoraRRHH-v1.0.N-Setup.exe` |

Pasos: enviar archivo → explicar app/versión → **fijar** el mensaje. Crea un
mensaje de bienvenida/índice con las 3 apps y fíjalo también.

---

## 4. Flujo recomendado para el cliente (texto para el canal)

> 📥 <b>NEXORA Suite — Descargas</b>
>
> 1️⃣ Página web: <code>https://black-cuba.github.io/nexora-descargas/</code>
> 2️⃣ O baja de la pestaña **Archivos** del canal el que necesites:
>    • 🏢 MultiAlmacen v3 (Windows) — `...-Setup.exe`
>    • 📱 POS Móvil v2 (Android) — `...apk`
>    • 👥 RRHH v1 (Windows) — `...-Setup.exe`
> 3️⃣ Instala y abre. Al primer arranque solicita la **licencia**; contáctanos
>    por WhatsApp +53 50840302 para activarla.
> 💡 Si la descarga se corta, Telegram la reanuda sola.

---

## 5. Notas importantes para Cuba

- **Licencia independiente por app** (`docs/CONTRATO-SUITE-NEXORA.md`, Anexo A):
  $15/mes, $50/trim, $75/sem, $100/año por aplicación.
- El APK requiere activar "Instalar apps de orígenes desconocidos" en Android.
- El EXE de Windows muestra "Publicador desconocido" hasta que se instale el
  certificado (`INSTALAR-CERTIFICADO.bat` + `.cer`) incluido en el Release.
- No copies instaladores a Mega/Drive: en Cuba suelen ir bloqueados o lentos.
  Telegram es la vía probada.