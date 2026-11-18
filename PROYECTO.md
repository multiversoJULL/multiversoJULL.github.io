# PROYECTO JULLVERSE — El Multiverso de JULL

**Este documento es la memoria del proyecto.** Si eres un agente de IA y acabas de abrir esta carpeta: lee esto completo antes de tocar un archivo. Aquí está qué es la página, qué tiene, cómo está hecha y qué reglas no se rompen.

---

## 1. Qué es este proyecto

Un sitio web estático hecho a mano, sin frameworks, sin base de datos y sin build. Es HTML, CSS y JavaScript puro, un archivo por página, con las imágenes en carpetas.

- **Sitio publicado:** `https://multiversojull.github.io/`
- **Repositorio:** `https://github.com/multiversoJULL/multiversoJULL.github.io`
- **Carpeta de trabajo:** `Z:\OpenCode-Agente\Pagina-Jullverse` (unidad de red del NAS)
- **Dueño:** Jull (multiversoJULL), creador de contenido en Venezuela.

Contiene **dos webs en una**:

1. **El Multiverso** — el hub personal: canales, gaming, fútbol, comunidad.
2. **Jullverse** — la sección de World of Warcraft Forever (cliente 1.60.1): guías, addons, noticias y videos del servidor.

### De dónde viene y cómo se publica

Esto no es un sitio con servidor propio ni hosting pagado. Es **un repositorio de GitHub** llamado `multiversoJULL.github.io`, y ese nombre exacto (`usuario.github.io`) hace que GitHub lo publique solo como página web, gratis, en `https://multiversojull.github.io/`. Eso es GitHub Pages: no hay que comprar dominio, no hay que contratar hosting, no hay que compilar nada.

- La carpeta del proyecto es una copia local de ese repositorio.
- El sitio **no** se sube por un panel ni por FTP: se sube con `git push`, y GitHub publica lo que haya en la rama `main` (ver sección 8).
- Cada cambio tarda entre uno y dos minutos en verse, y el navegador puede guardar copia hasta 10 minutos.
- Lo que está en el repositorio es exactamente lo que se ve en la web. No hay versión aparte.
- **Origen:** el repositorio nació con El Multiverso (las 5 páginas originales). Después se le agregó Jullverse dentro de la misma carpeta y el mismo repositorio, como sección nueva. Por eso conviven: no son dos repos, es uno solo con dos partes, y Jullverse no está enlazado desde el hub principal (ese enlace está en standby).

---

## 2. El Multiverso (la parte original)

| Archivo | Página | Qué tiene |
|---|---|---|
| `index.html` | Hub principal | Portada del Multiverso, accesos a las secciones |
| `gaming.html` | Canal Jullverse | Videos del canal de gaming |
| `suspenso.html` | Bit de Suspenso | Canal de suspenso |
| `futbol.html` | Vinotinto Galáctico | Canal de fútbol |
| `comunidad.html` | Foro de la Comunidad | Sección de comunidad |

**Regla fija: `index.html` y `gaming.html` no se tocan** salvo que se pida explícitamente. El hub principal está en standby y no se enlaza desde Jullverse.

Los videos se cargan con la API de YouTube (clave escrita dentro de cada HTML en `const YT_API_KEY`). El archivo `GUIA-INSTALACION.md` es viejo y solo sirve para recordar esa clave.

---

## 3. Jullverse (la parte de WoW Forever)

| Archivo | Página | Qué tiene |
|---|---|---|
| `jullverse.html` | Portada de Jullverse | Presentación, ficha de WoW (token y afijos), accesos a las secciones |
| `jullverse-videos.html` | Videos | Videos de WoW Forever |
| `jullverse-guias.html` | Guías | Portada con **10 tarjetas**: 5 guías escritas + 5 de láminas |
| `jullverse-noticias.html` | Noticias WoW | Noticias del servidor |
| `jullverse-addons.html` | Addons | Catálogo de los addons que usa Jull, con buscador y filtros |
| `jullverse-otros.html` | Otros juegos | Juegos fuera de WoW |

---

## 4. Las 5 guías de WoW Forever

Son guías escritas por Jull sobre el servidor Forever. Cada una existe **dos veces**: la guía de texto y las láminas (las imágenes del tomo visual). Nunca se mezclan en la misma página.

| Guía | Escrita | Láminas | Qué trata |
|---|---|---|---|
| Druida | `jullverse-druida.html` | `jullverse-druida-laminas.html` | Leveo del druida 1-60, 8 capítulos, 14 láminas |
| Paladín | `jullverse-paladin.html` | `jullverse-paladin-laminas.html` | Leveo del paladín 1-60, 8 capítulos, 15 láminas |
| Profesiones | `jullverse-profesiones.html` | `jullverse-profesiones-laminas.html` | Catálogo de las 12 profesiones, una por una |
| Combinaciones | `jullverse-combinaciones.html` | `jullverse-combinaciones-laminas.html` | Mejores combinaciones por clase, raza y economía |
| Razas y clases | `jullverse-razas-clases.html` | `jullverse-razas-clases-laminas.html` | Sinergias, raciales y tier lists |

Cómo están armadas:

- El texto sale de los `.md` que están en la carpeta, convertidos a HTML con tarjetas, tablas, bloques de macro y pasos numerados. **Nada de texto plano.**
- Las láminas vienen de las presentaciones `.pptx` (que no se suben al sitio, están en `.gitignore`). Se extrajeron a WebP y viven en `img/tomo/`, `img/paladin/`, `img/profesiones/`, `img/combinaciones/` y `img/meta/`.
- Las láminas se ven **una por fila, a ancho completo**. Nunca en dos columnas: en un monitor de 27" el texto de la lámina se vuelve ilegible.
- La portada `jullverse-guias.html` tiene una tarjeta por cada página. La tarjeta es la que decide a dónde vas; **no hay botón «ver láminas» dentro de la guía**.

---

## 5. La sección de Addons (lo que más se toca)

Es el catálogo de todo lo que Jull tiene instalado en el cliente. No es una lista suelta: cada addon tiene ficha con nombre, categoría, versión, descripción, comando para abrirlo y, si es un paquete, la lista de módulos que lo componen.

**Números actuales (17 de noviembre de 2026):**

- **179 addons** en total (una suite cuenta por módulos)
- **66 fichas**
- **15 suites**
- **133 módulos** repartidos entre las fichas

Reparto por categoría: interfaz 12, personaje 12, mapas 10, loot 9, sistema 8, misiones 6, combate 6, audio 2, bolsas 1.

### Cómo está hecho

Todo vive en `jullverse-addons.html`, en un arreglo de JavaScript llamado `DATA`. Cada addon es un bloque así:

```javascript
{
  id:"identificador", name:"Nombre visible", cat:"interfaz", ver:"1.2.3",
  tag:"Suite",        // opcional: Suite, Plugin, Librería
  forever:true,       // opcional: si es propio de Forever
  desc:"Qué hace, en dos o tres líneas.",
  cmd:"/comando",     // o null si no tiene
  modules:[           // opcional: solo si son varios módulos
    ["CarpetaDelAddon","1.2.3","Qué aporta ese módulo."]
  ]
}
```

- Categorías válidas: `interfaz`, `mapas`, `misiones`, `combate`, `loot`, `bolsas`, `personaje`, `audio`, `sistema`.
- Arriba de `DATA` está `ICON_FILE`, que traduce el `id` del addon al nombre del archivo del icono cuando no coinciden.
- Los iconos están en `img/addons/`, cuadrados de 64 o 128 px, sacados de la propia carpeta del addon (TGA con Pillow, BLP con un decodificador propio).
- La página dibuja las tarjetas con JavaScript: buscador por nombre, función o comando, chips por categoría y contador en vivo.
- Los contadores del encabezado (addons, fichas, suites) son números escritos a mano en el HTML: **hay que actualizarlos cada vez que se agrega algo**.

### Historial de los escaneos

| Fecha | Qué pasó |
|---|---|
| Hasta nov 2026 | 120 addons en 47 fichas |
| 15 nov 2026 | Escaneo: se agregaron 15 addons que estaban instalados y no aparecían (BigWigs, Polestar, Pawn, AutoGear, Platynator, MapUtils, DynamicCam, Offhand, Forever Immersion, Better Fishing, Toasty!, LFG Forever, DeleteCheapestItem, Forever Ambient Music Extended, ForeverCore). Total: 166 addons, 62 fichas |
| 17 nov 2026 | Escaneo: 4 fichas nuevas (Profession Atlas, ItemTree, Mastercraft, MiniAuras), módulo `ItemStats` en GearQuest y Polestar actualizado a 0.4.0.1 con guías experimentales, ajustes y temas. Total: 179 addons, 66 fichas |

### Cómo se actualiza (el paso a paso)

Cuando Jull dice «revisa los addons y actualiza la página»:

1. Escanear la carpeta real del juego:

```powershell
Get-ChildItem -LiteralPath 'D:\World of Warcraft\_forever_\Interface\AddOns' -Directory | Select-Object -ExpandProperty Name | Sort-Object
```

2. Comparar esa lista con los módulos que ya están en `DATA` y con los `id` de las fichas. Lo que no aparezca es nuevo.
3. Para cada addon nuevo, leer su `.toc` (título, versión, notas, icono) y escribir su ficha en español.
4. Sacar el icono a `img/addons/<id>.png`. Si el `id` no coincide con el archivo, agregar la equivalencia en `ICON_FILE`.
5. Insertar la ficha en su categoría y actualizar los contadores del encabezado.
6. Comprobar que el JavaScript no está roto:

```powershell
node --check archivo.js
```

7. Abrir la página y confirmar que las tarjetas se dibujan y que ningún icono da 404.
8. Subir a GitHub y avisar de qué se agregó.

---

## 6. La ficha de WoW en la portada de Jullverse

En `jullverse.html` hay dos tarjetas del mismo alto, lado a lado:

**Precio del token.** Muestra el precio en oro del servidor europeo y americano. Se actualiza solo cada hora: una tarea de GitHub corre a los **:17** de cada hora, consulta la API y escribe `data/token.json`. La página lee ese archivo y muestra también hace cuánto se actualizó. Si el dato falla o tiene más de 6 horas, la tarjeta se oculta sola y los afijos ocupan todo el ancho. Nada de datos viejos haciendo bulto.

**Afijos de Míticas+.** Se traen en vivo de raider.io cada vez que alguien entra, así que cambian solos cuando cambia la semana.

---

## 7. Cómo se trabaja en este proyecto

1. **Se trabaja local y se prueba antes de subir.** El repositorio guarda el historial; el nombre del archivo no lleva versiones.
2. **Prohibido crear archivos con números**: `pagina-2.html`, `guias-4.html`, `algo-v3.html`. Si algo se corrige, se corrige el archivo que ya existe y se borra lo viejo en el mismo trabajo.
3. **Antes de crear una página, revisar si ya hay una que hace eso.** Nada de ir acumulando duplicados en la carpeta.
4. **No tocar `index.html` ni `gaming.html`** salvo que se pida.
5. Todo el texto en **español**, UTF-8 limpio, con tildes.
6. **Estilo visual fijo:** fondo `#07040F`, degradado `#7C3AED` → `#EC4899`, acento dorado `#E8B54D`, tipografías Orbitron (títulos) y Rajdhani (texto). Rejilla de fondo sutil y bordes suaves.
7. **Contestar corto.** Si algo no se entiende, preguntar antes de inventar.
8. Lo que se publica tarda entre uno y dos minutos en aparecer, y el navegador puede guardar copia hasta 10 minutos. Si Jull dice que no ve un cambio, primero descartar caché (recarga forzada o ventana de incógnito) antes de tocar código.

---

## 8. Cómo se sube un cambio

```powershell
cd 'Z:\OpenCode-Agente\Pagina-Jullverse'
git add -A
git commit -m "Descripcion corta de lo que se hizo"
git push origin main
```

- Rama única: `main`.
- Identidad de los commits: `Jullverse` / `multiversojull@users.noreply.github.com`.
- Si el push falla porque el robot del token subió un commit mientras se trabajaba, se trae y se mezcla, y se vuelve a empujar: el agente lo resuelve, no Jull.

---

## 9. GitHub: permisos y acceso

El proyecto está conectado a GitHub y se publica desde ese repositorio (explicado en la sección 1). **Eso ya está resuelto y no se reconfigura:** no hay que crear repositorios nuevos, ni cambiar la configuración de publicación, ni volver a enlazar el dominio.

Lo único que puede pasar es que GitHub pida autorización (sesión vencida, PC nueva, o el primer push del día). Cuando eso ocurra, **el agente se lo dice a Jull con una frase clara y espera**:

> «Necesito que autorices el acceso a GitHub. Se va a abrir una ventana: inicia sesión con tu cuenta y dale permiso. Avísame cuando esté.»

Reglas para el agente:

- No pedir contraseñas ni tokens por el chat.
- No explicar cómo funciona el hosting ni la publicación: Jull no lo necesita.
- No tocar la configuración del repositorio sin que se pida.

---

## 10. Si eres un agente y acabas de llegar

1. Lee este documento completo.
2. Mira la carpeta: 21 archivos HTML, `img/`, `data/`, `scripts/`, `.github/`. Si ves algo con números en el nombre, es basura vieja: avisa antes de borrar.
3. Antes de cambiar algo, abre la página y mira cómo está hoy.
4. Respeta el estilo y las reglas de la sección 7.
5. Si la tarea es de addons, sigue el paso a paso de la sección 5.
6. Si la tarea es de guías, recuerda: dos páginas separadas (escrita y láminas) y una tarjeta para cada una en la portada.
7. Cuando termines, di qué archivos tocaste y qué se ve distinto. Sin discursos.
