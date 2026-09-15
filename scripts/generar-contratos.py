import os
from docx import Document
from docx.shared import Pt, RGBColor, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION

DARK = RGBColor(0x0B, 0x12, 0x22)     # azul noche
CYAN = RGBColor(0x0E, 0x7B, 0x8F)     # cian
AMBER = RGBColor(0xB4, 0x5F, 0x04)
GRAY = RGBColor(0x66, 0x6E, 0x7B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

NEXORA = "NEXORA"
DEV = "Miguel Angel Piñeiro"
WHATS = "+53 50840302"
MAIL = "miguel290876@gmail.com"
COUNTRY = "Cuba"
DATE = "15 de septiembre de 2026"

APP_AGUA = {
    "multialmacen": {
        "nombre": "NEXORA Sistema MultiAlmacen v3",
        "plataforma": "Windows (EXE) — 64 bits",
        "desc": "Gestión comercial integral: inventario multi-almacén, facturación POS con validación de stock, vales de entrada y salida, transferencias entre almacenes, ajustes tipificados (mermas, devoluciones, vencidos), integración IPV con POS móvil, Modelo D-01 ONAT y reportes/auditoría.",
    },
    "pos": {
        "nombre": "NEXORA POS Móvil v2",
        "plataforma": "Android (APK)",
        "desc": "Punto de venta móvil que importa el inventario del almacén central mediante archivos IPV, vende de forma 100% offline y devuelve el cierre de turno para reconciliación con el almacén central.",
    },
    "rrhh": {
        "nombre": "NEXORA RRHH v1",
        "plataforma": "Windows (EXE) — 64 bits",
        "desc": "Gestión integral de Recursos Humanos: expediente del personal, puestos de trabajo, control de asistencia, permisos y ausencias, nómina con cálculo de impuestos y vacaciones.",
    },
    "cubapos": {
        "nombre": "NEXORA CubaPOS",
        "plataforma": "Windows (EXE) y Android (APK)",
        "desc": "Punto de venta multimoneda (CUP/USD/EUR) e inventario en tiempo real para restaurantes y bares: 7 métodos de pago, cierre de turno, transferencias entre locales, ajustes tipificados, Modelo D-01 ONAT e integración WhatsApp Studio.",
    },
}

def set_cell(cell, text, bold=False, size=10.5, color=None, align=None):
    cell.text = ""
    p = cell.paragraphs[0]
    r = p.add_run(text)
    r.bold = bold
    r.font.size = Pt(size)
    r.font.name = "Calibri"
    if color:
        r.font.color.rgb = color
    if align:
        p.alignment = align
    for para in cell.paragraphs:
        para.paragraph_format.space_after = Pt(0)
        para.paragraph_format.space_before = Pt(0)

def estilo_docs(doc):
    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(11)
    st.paragraph_format.space_after = Pt(6)

def portada(doc, app):
    for _ in range(3):
        doc.add_paragraph()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(NEXORA); r.bold = True; r.font.size = Pt(44); r.font.color.rgb = DARK; r.font.name = "Calibri"
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("S O F T W A R E   S U I T E"); r.font.size = Pt(14); r.font.color.rgb = CYAN; r.font.name = "Calibri"
    doc.add_paragraph()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(app["nombre"]); r.bold = True; r.font.size = Pt(22); r.font.color.rgb = DARK
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(app["plataforma"]); r.font.size = Pt(13); r.font.color.rgb = GRAY
    for _ in range(2):
        doc.add_paragraph()
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("CONTRATO DE LICENCIA DE USO DE SOFTWARE"); r.bold = True; r.font.size = Pt(16); r.font.color.rgb = DARK
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Versión 1.0 · " + DATE); r.font.size = Pt(12); r.font.color.rgb = GRAY
    for _ in range(3):
        doc.add_paragraph()
    tbl = doc.add_table(rows=2, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell(tbl.cell(0,0), "Entre:", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(tbl.cell(0,1), "y:", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(tbl.cell(1,0), "LICENCIANTE\n" + DEV, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(tbl.cell(1,1), "LICENCIATARIO\n______________________", align=WD_ALIGN_PARAGRAPH.CENTER)
    doc.add_page_break()

def partes(doc):
    doc.add_heading("Identificación de las Partes", level=1)
    tbl = doc.add_table(rows=0, cols=2)
    tbl.style = "Table Grid"
    lic = [
        ("Nombre / Razón social", DEV),
        ("Marca comercial", NEXORA),
        ("Rol", "Desarrollador y titular de los derechos del software"),
        ("WhatsApp", WHATS),
        ("Correo electrónico", MAIL),
        ("País", COUNTRY),
    ]
    licat = [
        ("Nombre / Razón social", "__________________________________"),
        ("Tipo de entidad", "MIPYME / OTPC / SRL / TCP / Cooperativa / Estatal"),
        ("NIT / REEUP", "__________________________________"),
        ("Representante legal", "__________________________________"),
        ("Teléfono / WhatsApp", "__________________________________"),
        ("Correo electrónico", "__________________________________"),
        ("Dirección", "__________________________________"),
    ]
    h = tbl.add_row().cells
    set_cell(h[0], "LICENCIANTE", bold=True, color=WHITE, align=WD_ALIGN_PARAGRAPH.CENTER)
    set_cell(h[1], "LICENCIATARIO", bold=True, color=WHITE, align=WD_ALIGN_PARAGRAPH.CENTER)
    for c in h:
        for p in c.paragraphs:
            p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(2)
        tcPr = c._tc.get_or_add_tcPr()
        from docx.oxml.ns import qn
        shd = tcPr.makeelement(qn('w:shd'), {qn('w:val'):'clear', qn('w:color'):'auto', qn('w:fill'):'0B1222'})
        tcPr.append(shd)
    n = max(len(lic), len(licat))
    for i in range(n):
        row = tbl.add_row().cells
        if i < len(lic):
            set_cell(row[0], lic[i][0], bold=True)
            set_cell(row[1], lic[i][1])
        if i < len(licat):
            set_cell(row[0], licat[i][0] if i >= len(lic) else lic[i][0], bold=(i >= len(lic)))
            set_cell(row[1], licat[i][1])
    doc.add_paragraph()

def clausula(doc, num, titulo, items):
    doc.add_heading(f"{num}. {titulo}", level=2)
    for it in items:
        if isinstance(it, tuple):
            lead, rest = it
            p = doc.add_paragraph(style="List Number")
            r = p.add_run(lead + " ")
            r.bold = True
            p.add_run(rest)
        else:
            doc.add_paragraph(it, style="List Bullet")

def app_section(doc, app):
    doc.add_heading("1. Objeto del Contrato", level=2)
    p = doc.add_paragraph()
    r = p.add_run(f"El presente contrato regula la concesión de uso del programa de computación {app['nombre']} ")
    r = p.add_run(f"({app['plataforma']})")
    r.font.color.rgb = CYAN
    r2 = p.add_run(", desarrollado y licenciado por el Licenciante bajo la marca comercial NEXORA, entregado en formato de instalador y que funciona de forma 100% offline en el equipo del Licenciatario.")
    doc.add_paragraph().add_run("Descripción de la aplicación:").bold = True
    doc.add_paragraph(app["desc"])
    p = doc.add_paragraph()
    r = p.add_run("Quedan excluidos de este contrato el generador de licencias (herramienta interna del Licenciante) y cualquier otro programa no identificado expresamente, que no se entregan ni se licencian al Licenciatario.")
    doc.add_paragraph()

def genero(doc, app, tarifas, notas_tarifa, archivo):
    estilo_docs(doc)
    portada(doc, app)
    partes(doc)
    app_section(doc, app)

    clausula(doc, 2, "Concesión de Licencia", [
        ("Sujeto al pago acordado y al cumplimiento de este Contrato,","el Licenciante otorga al Licenciatario una licencia de uso no exclusiva, intransferible y no cedible."),
        ("Vínculo a un equipo:","la licencia queda ligada a una máquina específica (Machine ID) en la que se activa, durante el período activo del plan adquirido (mensual, trimestral, semestral o anual)."),
        ("Una licencia por equipo:","se concede una licencia por cada instalación de la aplicación que se haga en un equipo distinto."),
        ("Activación:","mediante archivo .lic o clave de licencia generada y firmada electrónicamente (firma RSA) por el Licenciante para el Machine ID del equipo."),
        ("Prueba gratuita:","la aplicación incluye un período de prueba de 15 días con acceso a todos los módulos antes de requerir activación."),
    ])

    clausula(doc, 3, "Restricciones", [
        ("(a)","No copiar, distribuir, revender, sublicenciar, alquilar, prestar o ceder el Software o la Licencia a terceros sin autorización escrita del Licenciante."),
        ("(b)","No descompilar, aplicar ingeniería inversa, modificar o extraer el código del Software."),
        ("(c)","No manipular la fecha/hora del sistema para extender la validez de la Licencia. La aplicación detecta retrocesos de reloj y se bloquea automáticamente."),
        ("(d)","No intentar evadir, alterar o adulterar el mecanismo de licenciamiento ni los datos fiscales sellados."),
        ("(e)","No instalar la aplicación en más equipos de los licenciados."),
    ])

    clausula(doc, 4, "Pago y Renovación", [
        ("Uso con licencia válida:","el uso continuado de la aplicación requiere una Licencia válida."),
        ("Medios de pago:","según el mecanismo comunicado por el Licenciante (actualmente: ONAT D-01 / transferencia / efectivo, coordinado por WhatsApp)."),
        ("Tarifas vigentes:","se detallan en el Anexo A — Tarifas, por cada equipo en el que se instale la aplicación."),
        ("Renovación:","al expirar la Licencia, el Licenciatario debe renovarla para continuar usando la aplicación con todas sus funciones."),
        ("Cambio de precios:","el Licenciante se reserva el derecho de modificar precios y planes con aviso previo; las renovaciones durante la vigencia se ajustan a lo aquí pactado."),
    ])

    clausula(doc, 5, "Soporte y Actualizaciones", [
        ("Soporte:","se brinda por WhatsApp al número oficial del Licenciante dentro del horario acordado y sujeto a disponibilidad."),
        ("Actualizaciones:","se distribuyen como nueva instalación (EXE/APK); los datos del Licenciatario (bases de datos locales) se conservan durante el proceso."),
        ("Responsabilidad del Licenciatario:","usar la versión vigente para el respaldo del fabricante y de las normativas fiscales aplicables."),
    ])

    clausula(doc, 6, "Datos y Privacidad", [
        ("100% offline:","la aplicación funciona sin conexión a internet. Los datos comerciales residen exclusivamente en el equipo del Licenciatario."),
        ("Sin acceso:","el Licenciante no accede, almacena ni transmite los datos del Licenciatario."),
        ("Respaldos:","es responsabilidad del Licenciatario realizar sus propios respaldos (.db). Los datos sobreviven a reinstalaciones porque se guardan en la carpeta de datos del usuario."),
    ])

    clausula(doc, 7, "Garantía y Responsabilidad", [
        ("“Tal cual”:","el Software se entrega sin garantía de funcionamiento ininterrumpido o libre de errores."),
        ("Limitación:","en la máxima medida permitida por la ley, el Licenciante no será responsable por daños directos, indirectos, incidentales o consecuentes, incluyendo pérdida de datos, pérdida de beneficios o interrupción del negocio."),
        ("Uso de reportes:","el Licenciatario asume la responsabilidad del uso de los datos y reportes generados (incluidos los fiscales/ONAT)."),
    ])

    clausula(doc, 8, "Terminación", [
        ("Automática:","el Contrato termina si el Licenciatario incumple cualquiera de las restricciones o si la Licencia expira sin renovación."),
        ("Revocación:","el Licenciante podrá revocar la Licencia si detecta manipulación, distribución no autorizada o uso indebido del Software."),
    ])

    clausula(doc, 9, "Propiedad Intelectual", [
        "El Software, incluyendo código, diseño, iconos, nombres y la tecnología de licenciamiento (firma RSA), es propiedad intelectual del Licenciante. Este Contrato no transfiere ninguna propiedad; solo concede el derecho limitado de uso descrito.",
    ])

    clausula(doc, 10, "Ley Aplicable y Jurisdicción", [
        f"Este Contrato se rige por las leyes de la República de {COUNTRY}. Cualquier controversia que no pueda resolverse de mutuo acuerdo se someterá a la jurisdicción correspondiente.",
    ])

    doc.add_heading("11. Aceptación", level=2)
    p = doc.add_paragraph()
    r = p.add_run(f"Al instalar, usar o activar la aplicación {app['nombre']}, el Licenciatario acepta todos los términos de este Contrato.")
    r.bold = True

    doc.add_heading("Firmas", level=1)
    p = doc.add_paragraph()
    p.add_run(f"En {COUNTRY}, a los ____ días del mes de ______________ de 20____.")
    tbl = doc.add_table(rows=4, cols=2)
    tbl.style = "Table Grid"
    set_cell(tbl.cell(0,0), "Por el Licenciante:", bold=True)
    set_cell(tbl.cell(0,1), "Por el Licenciatario:", bold=True)
    set_cell(tbl.cell(1,0), "Nombre: " + DEV)
    set_cell(tbl.cell(1,1), "Nombre / Razón social:")
    set_cell(tbl.cell(2,0), "Marca: " + NEXORA)
    set_cell(tbl.cell(2,1), "Cargo / Representante:")
    set_cell(tbl.cell(3,0), "Firma: ______________________")
    set_cell(tbl.cell(3,1), "Firma: ______________________")
    doc.add_page_break()

    doc.add_heading("Anexo A — Tarifas", level=1)
    p = doc.add_paragraph()
    p.add_run("Tarifas vigentes por cada equipo en el que se instale la aplicación.")
    tbl = doc.add_table(rows=1, cols=3)
    tbl.style = "Table Grid"
    headers = ("Plan", "Período", "Precio (USD)")
    for i, htxt in enumerate(headers):
        set_cell(tbl.cell(0, i), htxt, bold=True, color=WHITE, align=WD_ALIGN_PARAGRAPH.CENTER)
    for plan, per, precio in tarifas:
        row = tbl.add_row().cells
        set_cell(row[0], plan, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell(row[1], per, align=WD_ALIGN_PARAGRAPH.CENTER)
        set_cell(row[2], precio, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    doc.add_paragraph()
    for nota in notas_tarifa:
        doc.add_paragraph(nota, style="List Bullet")

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("— Fin del documento —")
    r.font.color.rgb = GRAY
    r.italic = True

    doc.save(archivo)
    print(f"OK: {archivo}")

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")

def base_tarifas():
    return [
        ("Mensual", "30 días", "$15"),
        ("Trimestral", "90 días", "$50"),
        ("Semestral", "180 días", "$75"),
        ("Anual", "365 días", "$100"),
    ]

def notas_base():
    return [
        "Cada aplicación de la Suite NEXORA se licencia de forma independiente.",
        "El precio de paquetes multi-app o de licencias para varios equipos se pacta por escrito con el Licenciante.",
        "Métodos de pago: ONAT D-01 / transferencia / efectivo, coordinados por WhatsApp (" + WHATS + ").",
    ]

def main():
    os.makedirs(OUT, exist_ok=True)
    for key, app in APP_AGUA.items():
        doc = Document()
        tarifas = base_tarifas()
        notas = notas_base()
        if key == "cubapos":
            tarifas = [
                ("1 Mes", "30 días", "$15"),
                ("6 Meses", "180 días", "$50"),
                ("1 Año", "365 días", "$100"),
            ]
        shortcut = {
            "multialmacen": "Sistema-MultiAlmacen-v3",
            "pos": "POS-Movil-v2",
            "rrhh": "RRHH-v1",
            "cubapos": "CubaPOS",
        }
        archivo = os.path.join(OUT, f"NEXORA-Contrato-{shortcut[key]}.docx")
        genero(doc, app, tarifas, notas, archivo)

if __name__ == "__main__":
    main()