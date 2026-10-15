#!/usr/bin/env python3
"""Genera las páginas HTML de la web pública (solo librería estándar).

Uso:   python3 build.py
Edite los textos aquí (o los DATOS de arriba) y vuelva a ejecutarlo.
Los textos marcados «POR VALIDAR» son borradores que debe aprobar el Comando.
"""
from pathlib import Path
from html import escape

AQUI = Path(__file__).parent

# ------------------------------------------------------------------ DATOS
NOMBRE = "Cuerpo de Bomberos Voluntarios de Santa Rosa de Cabal"
RAZON_SOCIAL = "Cuerpo de Bomberos Voluntarios del Municipio de Santa Rosa de Cabal, Risaralda"
NIT = "900.870.449-1"
MOVIL = "350 697 7228"            # llamada y WhatsApp
FIJOS = ["365 7239", "365 7247"]
CORREO = "cbvsantarosadec@gmail.com"
USUARIO_REDES = "bomberossantarosadecabal"   # POR VALIDAR: usuario exacto en cada red
URL_FACEBOOK = f"https://www.facebook.com/{USUARIO_REDES}"
URL_INSTAGRAM = f"https://www.instagram.com/{USUARIO_REDES}"
DIRECCION = "Carrera 15 con Calle 11, Santa Rosa de Cabal, Risaralda"
MAPA_BUSQUEDA = "https://www.google.com/maps/search/?api=1&query=Bomberos+Voluntarios+Santa+Rosa+de+Cabal"
MAPA_OSM = ("https://www.openstreetmap.org/export/embed.html?bbox=-75.6320%2C4.8600%2C-75.6110%2C4.8770"
            "&layer=mapnik&marker=4.8686%2C-75.6215")   # centro aproximado del municipio

def tel(n):  # "365 7239" -> enlace
    d = "".join(c for c in n if c.isdigit())
    return f"tel:+57{d}" if len(d) == 10 else f"tel:+576{d}"
MOVIL_D = "57" + "".join(c for c in MOVIL if c.isdigit())
WA = f"https://wa.me/{MOVIL_D}?text=" + "Hola%2C%20quisiera%20informaci%C3%B3n%20de%20los%20Bomberos%20de%20Santa%20Rosa%20de%20Cabal"

MENU = [("index.html", "Inicio"), ("donde-reportar.html", "Dónde reportar"), ("quienes-somos.html", "Quiénes somos"),
        ("servicios.html", "Servicios"), ("transparencia.html", "Transparencia"), ("prevencion.html", "Prevención"),
        ("ayudanos.html", "Ayúdanos"), ("contacto.html", "Contacto")]

# ------------------------------------------------------------------ PLANTILLA
def pagina(archivo, titulo, cuerpo, descripcion):
    menu = "".join(f'<a href="{h}"{" class=activo" if h == archivo else ""}>{t}</a>' for h, t in MENU)
    fijos = " · ".join(f'<a href="{tel(n)}">{n}</a>' for n in FIJOS)
    return f"""<!doctype html>
<html lang="es"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(titulo)} · Bomberos Voluntarios Santa Rosa de Cabal</title>
<meta name="description" content="{escape(descripcion)}">
<meta name="theme-color" content="#02192f">
<link rel="icon" href="assets/favicon.png"><link rel="stylesheet" href="assets/style.css">
</head><body>
<div class="sos"><div class="wrap"><span>🚨 EMERGENCIA:</span>
<a href="{tel(MOVIL)}">📞 {MOVIL}</a><a href="{tel(FIJOS[0])}">☎ {FIJOS[0]}</a><a href="{tel(FIJOS[1])}">☎ {FIJOS[1]}</a></div></div>
<header class="barra"><div class="wrap">
<a class="marca" href="index.html"><img src="assets/escudo.png" alt="Escudo de los Bomberos Voluntarios de Santa Rosa de Cabal">
<span>Bomberos Voluntarios<small>Santa Rosa de Cabal</small></span></a>
<button class="burger" aria-label="Abrir menú" onclick="document.getElementById('m').classList.toggle('abierto')">☰</button>
<nav class="menu" id="m">{menu}</nav></div></header>
<main>{cuerpo}</main>
<a class="wa" href="{WA}" target="_blank" rel="noopener">💬 WhatsApp</a>
<footer><div class="wrap"><div class="rejilla">
<div><h4>{NOMBRE}</h4><p>Valor · Abnegación · Disciplina</p><p>{RAZON_SOCIAL}</p><p>NIT {NIT} · Entidad sin ánimo de lucro</p><p>Personería jurídica N.º 055 del 17 de julio de 2015</p></div>
<div><h4>Contacto</h4><p>📞 <a href="{tel(MOVIL)}">{MOVIL}</a> (llamada y WhatsApp)</p><p>☎ {fijos}</p>
<p>✉ <a href="mailto:{CORREO}">{CORREO}</a></p><p>📍 {DIRECCION}</p></div>
<div><h4>Síguenos</h4><p><a href="{URL_FACEBOOK}" rel="noopener">Facebook</a></p><p><a href="{URL_INSTAGRAM}" rel="noopener">Instagram</a></p>
<p><a href="{WA}" rel="noopener">WhatsApp</a></p></div></div>
<p class="legal">Sitio informativo. Para reportar una emergencia llame directamente; esta página no recibe reportes.
Ley 1575 de 2012 · Decreto 014 de 2015.</p></div></footer>
</body></html>"""

def cabecera(titulo, sub):
    return f'<div class="page-head"><div class="wrap"><h1 class="titulo">{titulo}</h1><p class="sub">{sub}</p></div></div>'

def por_validar(txt="Borrador por validar por el Comando antes de publicar."):
    return f'<p class="nota">📝 <b>POR VALIDAR:</b> {txt}</p>'

PAGINAS = {}

# ------------------------------------------------------------------ INICIO
accesos = [
    ("donde-reportar.html", "🧭", "¿A quién llamo?", "Guía rápida: qué entidad atiende cada situación."),
    ("prevencion.html", "🛡️", "Prevención", "Consejos para evitar incendios y qué hacer en una emergencia."),
    ("transparencia.html", "📊", "Transparencia", "Cifras, informes y cómo usamos los recursos."),
    ("ayudanos.html", "🤝", "Ayúdanos", "Ser voluntario, donar o aliarse con nosotros."),
]
tarjetas = "".join(f'<a class="tarjeta" href="{h}"><div class="ico">{i}</div><h3>{t}</h3><p class="suave">{d}</p></a>' for h, i, t, d in accesos)
campanas = [("🎁", "Dona un regalo"), ("🎒", "Campaña escolar"), ("🧒", "Día del niño"), ("🎆", "Campaña contra la pólvora")]
camp = "".join(f'<div class="tarjeta"><div class="ico">{i}</div><h3>{t}</h3></div>' for i, t in campanas)
PAGINAS["index.html"] = ("Inicio", "Cuerpo de Bomberos Voluntarios de Santa Rosa de Cabal, Risaralda: emergencias, prevención, transparencia y cómo ayudar.", f"""
<section class="hero"><div class="wrap"><div>
<span class="lema">Valor · Abnegación · Disciplina</span>
<h1>Nuestra misión es salvar vidas</h1>
<p>Somos el Cuerpo de Bomberos Voluntarios de Santa Rosa de Cabal. En momentos críticos actuamos con valor y entrega. Aquí encuentras cómo pedir ayuda, cómo prevenir y cómo trabajamos.</p>
<div class="acciones"><a class="btn rojo" href="{tel(MOVIL)}">📞 Llamar: {MOVIL}</a>
<a class="btn verde" href="{WA}" target="_blank" rel="noopener">💬 WhatsApp</a>
<a class="btn sec" href="donde-reportar.html">🧭 ¿A quién llamo?</a></div></div>
<img class="escudo" src="assets/escudo.png" alt="Escudo de los Bomberos Voluntarios de Santa Rosa de Cabal"></div></section>

<section class="bloque"><div class="wrap"><h2>¿Qué necesitas?</h2><p class="sub">Todo lo que la comunidad necesita saber, en un solo lugar.</p>
<div class="rejilla">{tarjetas}</div></div></section>

<section class="bloque alt"><div class="wrap"><h2>Atención de emergencias</h2>
<p class="sub">Ante cualquier incidente, comunícate de inmediato. Esta página es informativa: <b>no recibe reportes</b>.</p>
<div class="rejilla">
<div class="tarjeta dest"><h3>📞 Llamada y WhatsApp</h3><p style="font-size:1.5rem;font-weight:700"><a href="{tel(MOVIL)}">{MOVIL}</a></p></div>
<div class="tarjeta dest"><h3>☎ Líneas fijas</h3><p style="font-size:1.3rem;font-weight:700"><a href="{tel(FIJOS[0])}">{FIJOS[0]}</a> · <a href="{tel(FIJOS[1])}">{FIJOS[1]}</a></p></div>
<div class="tarjeta"><h3>¿No sabes a quién llamar?</h3><p>Revisa la guía por tipo de situación.</p><a class="btn mini" href="donde-reportar.html">Ver guía</a></div></div></div></section>

<section class="bloque"><div class="wrap"><h2>Campañas con la comunidad</h2>
<p class="sub">Trabajamos con niños, familias y colegios del municipio.</p><div class="rejilla">{camp}</div>
<p style="margin-top:1rem">{por_validar("Falta la descripción y fotos de cada campaña.")}</p></div></section>
""")

# ------------------------------------------------------------------ DÓNDE REPORTAR
def num(txt, href):
    return f'<a class="btn mini" href="{href}">{txt}</a>'
BOMB = num(f"📞 {MOVIL}", tel(MOVIL)) + num(f"☎ {FIJOS[0]}", tel(FIJOS[0])) + num(f"☎ {FIJOS[1]}", tel(FIJOS[1]))
casos = [
    ("fuego", "🔥", "Incendio (casa, local, vehículo, lote)", "Bomberos", BOMB,
     "Salga del lugar y no regrese. Cierre puertas si puede. Si hay humo, agáchese y cúbrase nariz y boca. No use agua en incendios eléctricos ni de grasa."),
    ("fuego", "🌲", "Incendio forestal o quema de rastrojos", "Bomberos y Brigada Forestal", BOMB,
     "Aléjese en dirección contraria al viento. No intente apagarlo si crece. Indique la vereda, finca o punto de referencia."),
    ("rescate", "🚧", "Rescate: persona atrapada, accidente, alcantarilla, altura", "Bomberos", BOMB,
     "No mueva a la persona salvo peligro inminente. Señalice la zona y evite que se acumule gente."),
    ("rescate", "🐝", "Abejas, avispas o animales en riesgo", "Bomberos", BOMB,
     "Aléjese y mantenga a niños y mascotas lejos. No intente quitar el panal ni lo golpee."),
    ("rescate", "🌳", "Árbol o estructura a punto de caer", "Bomberos", BOMB,
     "Despeje el área y avise a vecinos. No pase por debajo."),
    ("quimico", "☣️", "Derrame o escape de sustancias peligrosas", "Bomberos", BOMB,
     "Aléjese contra el viento, no toque ni huela la sustancia y cierre el paso a otras personas."),
    ("salud", "🚑", "Herido, enfermo o urgencia médica", "Línea de emergencias / ambulancia", num("📞 123", "tel:123") + num("📞 132 Cruz Roja", "tel:132"),
     "Mantenga la calma, no mueva al herido y siga las indicaciones del operador. <b>POR VALIDAR</b> el número de ambulancia local."),
    ("seguridad", "🚓", "Delito o riesgo de seguridad", "Policía Nacional", num("📞 123", "tel:123"),
     "Llame a la línea de emergencias; los Bomberos no atienden delitos."),
    ("riesgo", "🌧️", "Inundación, deslizamiento, creciente de quebrada", "Gestión del Riesgo municipal y Bomberos", BOMB + num("📞 144 Defensa Civil", "tel:144"),
     "Aléjese de quebradas y laderas, evacúe a un lugar alto. <b>POR VALIDAR</b>: teléfono de la oficina de Gestión del Riesgo de la Alcaldía."),
    ("servicios", "💡", "Cable caído, corte de energía o fuga de gas", "Empresa de energía / gas", "",
     "No toque cables ni intente cortar una fuga. Avise a vecinos y llame a la empresa. Si hay fuego, a Bomberos. <b>POR VALIDAR</b>: línea de la empresa en Santa Rosa."),
]
filtros = [("todos", "Todos"), ("fuego", "Fuego"), ("rescate", "Rescate"), ("quimico", "Sustancias peligrosas"),
           ("salud", "Salud"), ("seguridad", "Seguridad"), ("riesgo", "Riesgo natural"), ("servicios", "Servicios públicos")]
btnf = "".join(f'<button data-f="{k}"{" class=on" if k == "todos" else ""}>{t}</button>' for k, t in filtros)
cards = "".join(f'''<div class="tarjeta caso" data-c="{c}"><div class="ico">{i}</div><h3>{t}</h3>
<div class="quien">→ {q}</div><div class="nums">{n or "<span class=suave>Número por confirmar</span>"}</div>
<details><summary>Mientras llega la ayuda</summary><p>{m}</p></details></div>''' for c, i, t, q, n, m in casos)
PAGINAS["donde-reportar.html"] = ("Dónde reportar cada situación", "Guía de cuál entidad llamar según la emergencia en Santa Rosa de Cabal.", f"""
{cabecera("¿A quién llamo?", "Centro de información: cada situación tiene una entidad. Esta página no recibe reportes, llama directamente.")}
<section class="bloque"><div class="wrap">
<div class="filtros" id="f">{btnf}</div><div class="rejilla" id="casos">{cards}</div>
<h2 style="margin-top:2.4rem">Qué decir al llamar</h2>
<ol class="pasos"><li><b>Qué pasa</b> (incendio, accidente, rescate…).</li><li><b>Dónde:</b> dirección, barrio, vereda y una referencia (tienda, iglesia, finca).</li>
<li><b>Si hay personas</b> en peligro, heridos o atrapados.</li><li><b>Su nombre y teléfono</b>, y no cuelgue hasta que se lo indiquen.</li></ol>
<p style="margin-top:1.2rem">{por_validar("Confirmar con el Comando los números de las demás entidades locales antes de publicar. 123 y 132 son nacionales.")}</p>
</div></section>
<script>
document.querySelectorAll('#f button').forEach(b=>b.onclick=()=>{{
 document.querySelectorAll('#f button').forEach(x=>x.classList.toggle('on',x===b));
 document.querySelectorAll('#casos .caso').forEach(c=>c.style.display=(b.dataset.f==='todos'||c.dataset.c===b.dataset.f)?'':'none');}});
</script>""")

# ------------------------------------------------------------------ QUIÉNES SOMOS
PAGINAS["quienes-somos.html"] = ("Quiénes somos", "Misión, visión y marco legal de los Bomberos Voluntarios de Santa Rosa de Cabal.", f"""
{cabecera("Quiénes somos", NOMBRE)}
<section class="bloque"><div class="wrap"><div class="rejilla">
<div class="tarjeta"><h3>🎯 Misión</h3><p>Salvar vidas y proteger los bienes y el ambiente de Santa Rosa de Cabal, atendiendo emergencias de incendio, rescate y materiales peligrosos con valor, abnegación y disciplina, y promoviendo la prevención en la comunidad.</p></div>
<div class="tarjeta"><h3>🔭 Visión</h3><p>Ser una institución reconocida por su capacidad de respuesta, su transparencia y su cercanía con la comunidad, con personal formado y equipos adecuados.</p></div>
<div class="tarjeta"><h3>🏛️ Datos de la organización</h3><p><b>{RAZON_SOCIAL}</b></p><p>NIT {NIT}</p><p>Entidad sin ánimo de lucro</p><p>📍 {DIRECCION}</p><p>Este es el sitio web oficial de la organización.</p></div>
<div class="tarjeta"><h3>⚖️ Marco legal</h3><p>Personería jurídica N.º 055 del 17 de julio de 2015. Actuamos bajo la Ley 1575 de 2012 (Ley General de Bomberos de Colombia) y el Decreto 014 de 2015.</p></div></div>
<p style="margin-top:1rem">{por_validar("La misión y la visión son un borrador; deben ser reemplazadas por el texto oficial del Cuerpo.")}</p></div></section>
<section class="bloque alt"><div class="wrap"><h2>Nuestros valores</h2><div class="rejilla">
<div class="tarjeta"><h3>Valor</h3><p>Enfrentamos el riesgo para proteger a los demás.</p></div>
<div class="tarjeta"><h3>Abnegación</h3><p>Servimos de forma voluntaria, sin esperar nada a cambio.</p></div>
<div class="tarjeta"><h3>Disciplina</h3><p>Nos formamos y entrenamos para actuar bien en cada emergencia.</p></div></div></div></section>
<section class="bloque"><div class="wrap"><h2>Historia y estructura</h2>
<p class="sub">Aquí irán la historia del Cuerpo, el Comandante y la estructura organizacional.</p>
{por_validar("Falta el texto de historia, nombre del Comandante y organigrama (sin datos personales de los bomberos).")}</div></section>""")

# ------------------------------------------------------------------ SERVICIOS
serv = [("📋", "Revisión de planes de emergencia y contingencia", "Evaluamos los planes de empresas y establecimientos."),
        ("🤲", "Apoyo a la comunidad", "Atención de incendios, rescates, árboles, abejas y otras emergencias."),
        ("🔎", "Inspecciones técnicas", "Revisión de seguridad humana y protección contra incendios en locales y edificaciones."),
        ("🚰", "Prueba de red contra incendios", "Verificamos el funcionamiento de las redes de agua contra incendios."),
        ("🧒", "Prevención a la primera infancia", "Charlas y actividades para enseñar a los niños a prevenir riesgos."),
        ("🌲", "Brigada Forestal", "Prevención y control de incendios forestales en el municipio.")]
sc = "".join(f'<div class="tarjeta"><div class="ico">{i}</div><h3>{t}</h3><p class="suave">{d}</p></div>' for i, t, d in serv)
PAGINAS["servicios.html"] = ("Servicios", "Servicios del Cuerpo de Bomberos Voluntarios de Santa Rosa de Cabal.", f"""
{cabecera("Servicios", "Lo que hacemos por la seguridad del municipio.")}
<section class="bloque"><div class="wrap"><div class="rejilla">{sc}</div>
<h2 style="margin-top:2.4rem">¿Necesitas una inspección técnica?</h2>
<p class="sub">Para solicitar una inspección o consultar tu trámite, comunícate con nosotros.</p>
<a class="btn" href="contacto.html">Cómo solicitarla</a>
<p style="margin-top:1rem">{por_validar("Cuando el formulario de solicitud de inspección esté disponible en internet, se enlaza aquí.")}</p></div></section>""")

# ------------------------------------------------------------------ TRANSPARENCIA
cifras = "".join(f'<div class="cifra"><b>—</b><span>{t}</span></div>' for t in
                 ["Emergencias atendidas este año", "Incendios", "Rescates", "Inspecciones realizadas"])
docs = ["Personería jurídica N.º 055 de 2015", "RUT", "Informe de gestión anual", "Rendición de cuentas", "Estados financieros",
        "Plan de acción y contratación"]
dl = "".join(f'<li>{d} <span class="etq aviso">Pendiente</span></li>' for d in docs)
PAGINAS["transparencia.html"] = ("Transparencia", "Cifras, documentos y recursos de los Bomberos Voluntarios de Santa Rosa de Cabal.", f"""
{cabecera("Transparencia", "Rendimos cuentas a la comunidad que nos apoya.")}
<section class="bloque"><div class="wrap"><h2>Cifras de emergencias</h2>
<p class="sub">Datos agregados y anónimos: no se publican nombres, direcciones ni datos de quienes reportan.</p>
<div class="cifras">{cifras}</div>
<p style="margin-top:1rem">{por_validar("Calcular las cifras desde el registro de emergencias y publicar solo con autorización del Comando.")}</p></div></section>
<section class="bloque alt"><div class="wrap"><h2>Documentos públicos</h2><ul>{dl}</ul>
{por_validar("Subir los PDF aprobados y enlazarlos aquí.")}</div></section>
<section class="bloque"><div class="wrap"><h2>Hidrantes del municipio</h2>
<p class="sub">Mapa de los puntos de hidrantes (barrio, conexión y diámetro).</p>
{por_validar("Se publica solo si el Comando lo autoriza. Nunca se publican viviendas de bomberos ni sitios con materiales peligrosos.")}</div></section>""")

# ------------------------------------------------------------------ PREVENCIÓN
prev = [("🏠", "En casa", "Revise instalaciones eléctricas y de gas. No sobrecargue tomas. Nunca deje comida cocinándose sola ni velas encendidas."),
        ("🎆", "Pólvora", "Evítela: causa quemaduras graves, sobre todo en niños. Si ve venta ilegal, repórtela a la Policía."),
        ("🌲", "Temporada seca", "No haga quemas de rastrojo, no tire colillas ni vidrios en el campo y reporte humo de inmediato."),
        ("🧯", "Extintor y salida", "Tenga un extintor vigente, conozca su uso y mantenga las salidas libres."),
        ("🚸", "Niños", "Mantenga fósforos y encendedores fuera de su alcance y enséñeles que no son juguetes."),
        ("🌧️", "Lluvias y crecientes", "No cruce corrientes de agua, aléjese de quebradas y tenga un plan de evacuación familiar.")]
pc = "".join(f'<div class="tarjeta"><div class="ico">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in prev)
PAGINAS["prevencion.html"] = ("Prevención", "Consejos de prevención de incendios y emergencias en Santa Rosa de Cabal.", f"""
{cabecera("Prevención", "Prevenir es la mejor forma de salvar vidas.")}
<section class="bloque"><div class="wrap"><div class="rejilla">{pc}</div>
<p style="margin-top:1rem">{por_validar("Consejos generales de seguridad; el Comando debe revisarlos y ampliarlos.")}</p></div></section>
<section class="bloque alt"><div class="wrap"><h2>Plan de emergencia familiar</h2>
<ol class="pasos"><li>Dibuje un croquis de su casa con dos salidas por habitación.</li><li>Acuerden un punto de encuentro afuera.</li>
<li>Tenga a la vista los números de emergencia.</li><li>Practiquen la evacuación con toda la familia.</li></ol></div></section>""")

# ------------------------------------------------------------------ AYÚDANOS
PAGINAS["ayudanos.html"] = ("Ayúdanos", "Cómo ser voluntario, donar o aliarte con los Bomberos de Santa Rosa de Cabal.", f"""
{cabecera("Ayúdanos", "Somos voluntarios: cada aporte se convierte en protección para la comunidad.")}
<section class="bloque"><div class="wrap"><div class="rejilla">
<div class="tarjeta"><div class="ico">🧑‍🚒</div><h3>Ser voluntario</h3><p>Si quieres servir a tu comunidad, escríbenos por WhatsApp y te contamos los requisitos y la formación.</p>
<a class="btn mini verde" href="{WA}" target="_blank" rel="noopener">💬 Quiero ser voluntario</a></div>
<div class="tarjeta"><div class="ico">💛</div><h3>Donar</h3><p>Tu aporte ayuda a dotar equipos y mantener los vehículos.</p><p class="etq aviso">Datos de cuenta: pendiente</p></div>
<div class="tarjeta"><div class="ico">🏢</div><h3>Empresas aliadas</h3><p>Las empresas pueden apoyar con equipos, formación o patrocinio de campañas.</p>
<a class="btn mini" href="contacto.html">Contáctanos</a></div></div>
<p style="margin-top:1rem">{por_validar("Publicar solo la cuenta bancaria oficial a nombre del Cuerpo de Bomberos, verificada por el Comando, para evitar fraudes.")}</p></div></section>""")

# ------------------------------------------------------------------ CONTACTO
PAGINAS["contacto.html"] = ("Contacto", "Teléfonos, WhatsApp, correo y ubicación de la estación de Bomberos de Santa Rosa de Cabal.", f"""
{cabecera("Contacto", "Estamos para servirte.")}
<section class="bloque"><div class="wrap"><div class="rejilla">
<div class="tarjeta dest"><h3>📞 Llamada y WhatsApp</h3><p style="font-size:1.4rem;font-weight:700">{MOVIL}</p>
<a class="btn mini rojo" href="{tel(MOVIL)}">Llamar</a> <a class="btn mini verde" href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div>
<div class="tarjeta"><h3>☎ Líneas fijas</h3><p><a href="{tel(FIJOS[0])}">{FIJOS[0]}</a><br><a href="{tel(FIJOS[1])}">{FIJOS[1]}</a></p></div>
<div class="tarjeta"><h3>✉ Correo</h3><p><a href="mailto:{CORREO}">{CORREO}</a></p><p class="suave">Para trámites e información. <b>No use el correo para emergencias.</b></p></div>
<div class="tarjeta"><h3>📲 Redes sociales</h3><p><a href="{URL_FACEBOOK}" rel="noopener">Facebook</a><br><a href="{URL_INSTAGRAM}" rel="noopener">Instagram</a></p><p class="suave">@{USUARIO_REDES}</p></div></div>
<h2 style="margin-top:2.4rem">Estación</h2><p class="sub">📍 {DIRECCION}</p>
<iframe class="mapa" src="{MAPA_OSM}" title="Mapa de Santa Rosa de Cabal" loading="lazy"></iframe>
<p><a class="btn mini" href="{MAPA_BUSQUEDA}" target="_blank" rel="noopener">Cómo llegar</a></p>
<p>{por_validar("El mapa muestra el centro del municipio; ajustar al punto exacto de la estación.")}</p></div></section>""")

# ------------------------------------------------------------------ ESCRIBIR
for archivo, (titulo, desc, cuerpo) in PAGINAS.items():
    (AQUI / archivo).write_text(pagina(archivo, titulo, cuerpo, desc), encoding="utf-8")
print("Generadas:", ", ".join(PAGINAS))
