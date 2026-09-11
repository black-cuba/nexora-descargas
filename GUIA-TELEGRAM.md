# Guía de distribución por Telegram (internet nacional de Cuba)

Estrategia recomendada para que tus clientes descarguen la Suite NEXORA
desde la red nacional: **canal de Telegram** como fuente principal y la
**página de descargas** (`descargas/index.html`) como vitrina de enlaces.

Telegram es el método más rápido y confiable en Cuba: reanuda descargas,
no depende de VPN y casi todos los clientes ya lo tienen instalado.

---

## 1. Crear el canal

1. En Telegram pulsa el icono del **lápiz** (Android) o el **menú** (‏PC) → **Nuevo canal**.
2. Nombre sugerido: **NEXORA Suite** · Usuario/alias: `NEXORA_Suite`.
3. Tipo: **Canal público** (para que cualquiera lo encuentre). Privado también sirve, pero
   tendrás que enviar el enlace de invitación a cada cliente.
4. Al crearlo, ve a **Editar canal → Administradores** y agrega un bot o a un segundo dispositivo
   tuyo como respaldo (por si pierdes el acceso).

Quedará con enlace: `https://t.me/NEXORA_Suite`

---

## 2. Subir los instaladores (mensajes fijos / archivos)

Sube cada instalador como **archivo adjunto** en su propio mensaje para
que aparezca en la pestaña "Archivos" del canal:

| App | Archivo | Cómo apuntarlo |
|---|---|---|
| MultiAlmacen EXE | `NEXORA-SistemaMultiAlmacen-SETUP-V*.exe` | Descargar desde GitHub Release |
| POS Móvil APK | `Nexora-POS-v2.0.31.apk` | Descargar desde GitHub Release del repo móvil |
| RRHH EXE | `NexoraRRHH-v1.0.0-Setup.exe` | Descargar desde GitHub Release de NEXORA_RRHH |

Pasos por archivo:

1. Abre el canal y envía el archivo (arrastra o usa el clip 📎).
2. En el mensaje explica brevemente: qué app es, requisitos y versión.
3. Pulsa los **3 puntos del mensaje → Fijar** (pin) para que quede arriba.
4. Crea un mensaje de **bienvenida/índice** con las 3 apps y los pasos de
   instalación, y fíjalo también (así el cliente sabe qué hacer al entrar).

> Consejo: marca los archivos como **sin compresión** para que Telegram los
> suba tal cual y la descarga del cliente sea directa.

---

## 3. Preparar la página de descargas

Ya tienes `descargas/index.html` (autónoma, sin dependencias externas).
Antes de publicarla:

- Actualiza el enlace **Telegram** a tu canal real (`https://t.me/...`).
- Actualiza los enlaces **Descarga directa / Ver releases** con tus URLs reales de GitHub.
- Ajusta versiones si lanzas una nueva.

Dónde alojarla (opciones):

| Opción | Como funciona |
|---|---|
| **GitHub Pages** (repo público de solo docs) | Crear un repo público `nexora-descargas`, subir el `index.html` y activar Pages. Enlace tipo `https://usuario.github.io/nexora-descargas/`. |
| **Telegram "Fijado"** | Pegar el HTML no se ve bien; mejor compartir el enlace de GitHub Pages en un mensaje fijado. |
| **PC del cliente** | Enviar el `index.html` por WhatsApp; se abre en cualquier navegador (no necesita internet. Pero si lo abren en móvil, se ve bien). |

> GitHub puede ir lento en Cuba: siempre ofrece primero Telegram en la página.

---

## 4. Flujo recomendado para el cliente (texto para el canal)

> 📥 <b>NEXORA Suite — Descargas</b>
>
> 1️⃣ Entra aquí al canal y baja de la pestaña **Archivos**.
> 2️⃣ Descarga el que necesites:
>    • 🏢 MultiAlmacen v3 (Windows) — `...-Setup.exe`
>    • 📱 POS Móvil v2 (Android) — `...apk`
>    • 👥 RRHH v1 (Windows) — `...-Setup.exe`
> 3️⃣ Instala y abre. Al primer arranque solicita la **licencia**; contáctanos por
>    WhatsApp +53 50840302 para activarla.
> 💡 Si la descarga se corta, Telegram la reanuda sola.

---

## 5. Notas importantes para Cuba

- **La licencia es independiente por app** (ver `docs/CONTRATO-SUITE-NEXORA.md`,
  Anexo A): $15/mes, $50/trim, $75/sem, $100/año por aplicación.
- El APK requiere activar "Instalar apps de orígenes desconocidos" en Android.
- El EXE de Windows muestra "Publicador desconocido" hasta que el cliente
  instale el certificado (`INSTALAR-CERTIFICADO.bat` + `.cer`) incluido en el Release.
- No copies los instaladores a servicios como Mega/Drive: en Cuba suelen ir
  bloqueados o lentos. Telegram es la vía probada.