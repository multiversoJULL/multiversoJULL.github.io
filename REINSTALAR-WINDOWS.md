# Reinstalar Windows y volver a conectar el agente con GitHub

**Para qué sirve este documento:** cuando reinstales Windows, ábrele este archivo al agente y dile:

> «Lee `REINSTALAR-WINDOWS.md` del repo y hazlo paso a paso.»

Contiene todo lo que el agente necesita saber: qué instalar, dónde está el proyecto, cómo autenticarse en GitHub, cómo se publica el sitio y qué reglas no se rompen.

---

## 1. Los datos duros del proyecto

| Dato | Valor |
|---|---|
| Repositorio | `https://github.com/multiversoJULL/multiversoJULL.github.io.git` |
| Cuenta de GitHub | `multiversoJULL` |
| Correo para commits | `multiversojull@users.noreply.github.com` |
| Rama | `main` (única, sin ramas de trabajo) |
| Sitio publicado | `https://multiversojull.github.io/` |
| Carpeta del proyecto (en el NAS) | `Z:\OpenCode-Agente\Pagina-Jullverse` |
| Misma carpeta por red | `\\Nass-jull\servidor-nass\OpenCode-Agente\Pagina-Jullverse` |
| Addons del juego | `D:\World of Warcraft\_forever_\Interface\AddOns` |
| Config del agente | `C:\Users\julis\.config\opencode\` (ahí vive `AGENTS.md`) |

**Importante:** el proyecto NO vive en el disco del PC, vive en el NAS. Si el NAS está apagado o la VPN está prendida, la unidad `Z:` desaparece y todo falla. Eso no es un error del agente: es la unidad de red.

---

## 2. Antes de formatear (si todavía puedes)

1. **El código ya está a salvo** en GitHub. No hay que copiar el repo.
2. Copia la carpeta `C:\Users\julis\.config\opencode\` a un pendrive (tiene `AGENTS.md` y la configuración del agente). Si no la copias, hay que reescribir las reglas a mano (están resumidas en la sección 8).
3. Copia `D:\World of Warcraft\_forever_\Interface\AddOns` y `WTF` si no quieres volver a bajar addons y perfiles.
4. Anota tu usuario y contraseña de GitHub. No hace falta token a mano: el agente usa el administrador de credenciales de Windows.

---

## 3. Programas que hay que instalar

| Programa | Para qué | Cómo |
|---|---|---|
| **Chrome** (o Edge) | Ver el sitio y dejar que el agente maneje el navegador | normal |
| **Git para Windows** | Clonar y subir cambios | git-scm.com, todo por defecto |
| **Python 3** | Scripts del proyecto (token, iconos) | python.org, marcar «Add to PATH» |
| **Pillow** | Convertir iconos de addons | `pip install pillow` |
| **Node.js** | Comprobar que el JavaScript de las páginas no tiene errores | nodejs.org LTS |
| **VS Code** (opcional) | Editar a mano | code.visualstudio.com |
| **OpenCode** | El agente | opencode.ai (o `npm i -g opencode-ai`) |

Comprobación rápida en PowerShell:

```powershell
git --version
python --version
node -v
```

Si los tres contestan, vas bien.

---

## 4. Volver a montar la unidad de red

1. Abre el Explorador de Windows.
2. `Este equipo` → botón derecho → **Conectar a una unidad de red**.
3. Unidad: `Z:`
4. Carpeta: `\\Nass-jull\servidor-nass`
5. Marca **Conectar de nuevo al iniciar sesión**.

Si el NAS pide usuario y contraseña, son las del servidor (no las de GitHub).

Prueba:

```powershell
Test-Path 'Z:\OpenCode-Agente\Pagina-Jullverse'
```

Tiene que decir `True`.

---

## 5. Traer el proyecto

Si la carpeta `Z:\OpenCode-Agente\Pagina-Jullverse` ya existe en el NAS, **no clones nada**: solo entra ahí y comprueba que es un repo.

```powershell
cd 'Z:\OpenCode-Agente\Pagina-Jullverse'
git remote -v
git status
```

Si la carpeta no existe:

```powershell
cd 'Z:\OpenCode-Agente'
git clone https://github.com/multiversoJULL/multiversoJULL.github.io.git Pagina-Jullverse
cd Pagina-Jullverse
```

---

## 6. Autenticarse en GitHub (esto es lo que más se traba)

Git en Windows no guarda la contraseña: usa el **Administrador de credenciales**. La primera vez que hagas `git push`, se abre una ventana del navegador para iniciar sesión en GitHub. Eso es normal.

Pasos:

1. Abre PowerShell **en la carpeta del proyecto**.
2. Configura la identidad (una sola vez):

```powershell
git config --global user.name "Jullverse"
git config --global user.email "multiversojull@users.noreply.github.com"
```

3. Autoriza la carpeta aunque esté en red (Windows marca las rutas UNC como inseguras):

```powershell
git config --global --add safe.directory '%(prefix)///Nass-jull/servidor-nass/OpenCode-Agente/Pagina-Jullverse'
```

4. Fuerza un primer contacto con GitHub:

```powershell
cd 'Z:\OpenCode-Agente\Pagina-Jullverse'
git fetch origin main
```

5. Si pide credenciales, inicia sesión en la ventana que se abre. Si en vez de ventana pide usuario y contraseña en la consola, la contraseña **no** es la de GitHub: hay que crear un **token personal**:
   - GitHub → foto de perfil → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)** → **Generate new token**.
   - Nombre: `PC-Julisa`. Caducidad: la que quieras. Permisos: **`repo`** (y `workflow` si vas a tocar `.github/`).
   - Copia el token y úsalo como contraseña en la consola.
   - El Administrador de credenciales lo guarda y no vuelve a preguntar.

6. Prueba real de escritura:

```powershell
git commit --allow-empty -m "prueba de conexion"
git push origin main
```

Si sube, ya estás conectado. Borra ese commit de prueba si quieres, o déjalo: no hace daño.

**Nunca** escribas el token dentro de un archivo del proyecto ni en el chat.

---

## 7. Comprobar que el sitio sigue publicándose

El sitio es GitHub Pages y se sirve desde la raíz de la rama `main`. No hay build ni nada que ejecutar: lo que subes es lo que se ve.

1. GitHub → repo `multiversoJULL.github.io` → **Settings** → **Pages**.
2. Debe decir: **Source: Deploy from a branch**, rama `main`, carpeta `/ (root)`.
3. Abre `https://multiversojull.github.io/` y comprueba que carga.

Detalles que engañan:

- Tarda entre **60 y 120 segundos** en publicar.
- GitHub sirve copia en caché hasta **10 minutos**. Si cambiaste algo y no lo ves, abre la dirección con `?v=2` al final o usa una ventana de incógnito.
- Si algo da **404** justo después de subirlo, espera y recarga: casi siempre es la caché, no un archivo faltante.

---

## 8. Cómo se trabaja en este proyecto (reglas que no se rompen)

Estas reglas están en `AGENTS.md` y son las que evitan repetir errores ya cometidos:

1. **Se trabaja local, se prueba, y solo entonces se sube.** Nada de publicar versiones a medias.
2. **Prohibido crear archivos con números**: `pagina-2.html`, `guias-4.html`, `algo-v3.html`. Las versiones viven en el repositorio (el historial de git), no en el nombre del archivo. Si algo se corrige, se corrige el archivo que ya existe.
3. Antes de crear una página nueva, **mirar si ya hay una que hace eso** y limpiar la vieja en el mismo trabajo.
4. **No tocar `index.html` ni `gaming.html`** salvo que se pida explícitamente. El hub principal del Multiverso sigue en standby: no se enlaza.
5. Todo el texto en **español**, UTF-8 sin caracteres roñosos.
6. Estilo visual fijo: fondo `#07040F`, degradado `#7C3AED` → `#EC4899`, acento dorado `#E8B54D`, tipografías Orbitron y Rajdhani.
7. Las guías de Jullverse van en **dos páginas separadas**: una escrita (`jullverse-<tema>.html`) y una solo de láminas (`jullverse-<tema>-laminas.html`). La portada `jullverse-guias.html` tiene una tarjeta para cada una.
8. Responder corto. Si algo no se entiende, preguntar antes de inventar.

### Las páginas que existen hoy

| Archivo | Qué es |
|---|---|
| `index.html` | Hub principal del Multiverso (no tocar) |
| `gaming.html`, `futbol.html`, `suspenso.html`, `comunidad.html` | Secciones del Multiverso (no tocar) |
| `jullverse.html` | Portada de Jullverse |
| `jullverse-videos.html`, `-noticias.html`, `-addons.html`, `-otros.html` | Secciones de Jullverse |
| `jullverse-guias.html` | Portada de las 5 guías, 10 tarjetas |
| `jullverse-druida.html` / `-paladin` / `-profesiones` / `-combinaciones` / `-razas-clases` | Guías escritas |
| Las mismas con `-laminas` | Solo las láminas |

Carpetas:

- `img/` → todas las imágenes (`img/addons/` son los iconos de addons, cuadrado 64 o 128 px).
- `data/token.json` → precio del token, lo escribe un robot.
- `scripts/update_token.py` → script que consulta la API del token.
- `.github/workflows/token.yml` → tarea que corre cada hora a los **:17** y actualiza `data/token.json`.

---

## 9. Actualizar la página de addons (la tarea más repetida)

Cuando instales addons nuevos:

1. Escanear la carpeta real del juego:

```powershell
Get-ChildItem -LiteralPath 'D:\World of Warcraft\_forever_\Interface\AddOns' -Directory | Select-Object -ExpandProperty Name | Sort-Object
```

2. Comparar con lo que ya está en `jullverse-addons.html`. Los addons viven en un arreglo de JavaScript llamado `DATA`, cada uno con esta forma:

```javascript
{
  id:"identificador", name:"Nombre visible", cat:"interfaz", ver:"1.2.3", forever:true,
  desc:"Qué hace, en dos o tres líneas, en español.",
  cmd:"/comando",
  modules:[
    ["CarpetaDelAddon","1.2.3","Qué aporta ese módulo."]
  ]
}
```

Categorías válidas: `interfaz`, `mapas`, `misiones`, `combate`, `loot`, `bolsas`, `personaje`, `audio`, `sistema`.

3. Cada addon necesita su icono en `img/addons/<id>.png`. Se saca de la propia carpeta del addon: los `.tga` se abren con Pillow, y los `.blp` con un decodificador propio (está documentado en el historial: BLP2 paletizado y DXT5).
4. Si el `id` no coincide con el nombre del archivo del icono, se agrega la equivalencia en el objeto `ICON_FILE`.
5. Actualizar los números del encabezado: total de addons, fichas y suites.
6. Verificar antes de subir que el JavaScript no está roto:

```powershell
node --check archivo.js
```

7. Subir y esperar un minuto. Luego comprobar que las tarjetas se dibujan y que ningún icono da 404.

---

## 10. Publicar un cambio (el ciclo completo)

```powershell
cd 'Z:\OpenCode-Agente\Pagina-Jullverse'
git add -A
git -c user.name="Jullverse" -c user.email="multiversojull@users.noreply.github.com" commit -m "Descripcion corta y clara"
git push origin main
```

Notas:

- Si `git push` se queja de **non-fast-forward**, es porque el robot del token subió un commit mientras trabajabas:

```powershell
git fetch origin main
git -c user.name="Jullverse" -c user.email="multiversojull@users.noreply.github.com" merge --no-edit origin/main
git push origin main
```

- Si el repo queda en **detached HEAD** (pasa tras un rebase interrumpido), se arregla así:

```powershell
git checkout -B main
git push origin main
```

- PowerShell muestra el progreso del `push` en rojo aunque haya funcionado. No es un error.

---

## 11. Checklist final para decir «ya está todo»

- [ ] `git --version`, `python --version`, `node -v` responden.
- [ ] `Z:` montada y `Test-Path 'Z:\OpenCode-Agente\Pagina-Jullverse'` da `True`.
- [ ] `git remote -v` muestra el repo de `multiversoJULL`.
- [ ] `git push` funciona sin pedir credenciales cada vez.
- [ ] `https://multiversojull.github.io/` carga.
- [ ] `https://multiversojull.github.io/jullverse.html` carga.
- [ ] `https://multiversojull.github.io/jullverse-addons.html` dibuja las tarjetas de addons.
- [ ] `https://multiversojull.github.io/data/token.json` devuelve el JSON con precios.
- [ ] En GitHub → Actions, la tarea «Actualizar precio del token» aparece en verde.

---

## 12. Lo que el agente debería hacer al leer este documento

1. Comprobar los tres programas y la unidad `Z:` antes de tocar nada.
2. Verificar `git remote -v` y `git status` en la carpeta del proyecto.
3. Resolver la autenticación con el usuario en pantalla: no inventar tokens ni pedirlos en el chat.
4. Hacer un commit vacío de prueba y empujarlo, para confirmar que hay escritura real.
5. Abrir el sitio publicado y confirmar que responde.
6. A partir de ahí, trabajar con las reglas de la sección 8: local primero, nombres limpios, sin duplicados.

Si algo de este documento no coincide con lo que hay en el repositorio, **manda el repositorio** y avisa que el documento quedó viejo.
