# Reinstalar Windows y volver a trabajar en el sitio

**Cómo se usa:** cuando reinstales Windows, dile al agente:

> «Lee `REINSTALAR-WINDOWS.md` del repo y seguimos.»

---

## 1. Antes de formatear

1. El sitio no se pierde: está en GitHub y en el NAS.
2. Copia a un pendrive `C:\Users\julis\.config\opencode\` (ahí están las reglas del agente).
3. Si no quieres volver a bajar addons, copia `D:\World of Warcraft\_forever_\Interface\AddOns` y `WTF`.

---

## 2. Qué instalar

- **Chrome**
- **Git para Windows**
- **Python 3** (marcar «Add to PATH») y luego `pip install pillow`
- **Node.js**
- **OpenCode**
- **VS Code**, solo si vas a editar a mano

Después devuelve la carpeta `.config\opencode` a su sitio.

---

## 3. Dónde está el proyecto

Está en el NAS, en la unidad de red:

```
Z:\OpenCode-Agente\Pagina-Jullverse
```

El repo es `https://github.com/multiversoJULL/multiversoJULL.github.io` y la rama es `main`.

Si algún día la carpeta no está, se baja así:

```powershell
cd 'Z:\OpenCode-Agente'
git clone https://github.com/multiversoJULL/multiversoJULL.github.io.git Pagina-Jullverse
```

---

## 4. Lo único que tiene que hacer el usuario

**Iniciar sesión en GitHub cuando salga la ventana.**

Eso es todo. La primera vez que el agente suba un cambio, Git abre el navegador y pide la cuenta. Se inicia sesión con la cuenta de siempre y ya no vuelve a preguntar.

Si el agente no puede subir y pide ayuda, la respuesta del usuario es: «me falta iniciar sesión en GitHub» y se resuelve en esa ventana.

---

## 5. Reglas de trabajo

1. Se trabaja local, se prueba, y después se sube.
2. Nada de archivos con números en el nombre (`algo-2.html`, `guias-4.html`). Si algo se corrige, se corrige el archivo que ya existe.
3. Antes de crear una página, mirar si ya hay una que haga eso, y borrar la vieja en el mismo trabajo.
4. No tocar `index.html` ni `gaming.html` sin que se pida.
5. Todo en español, con tildes bien puestas.
6. Colores del sitio: fondo `#07040F`, degradado `#7C3AED` → `#EC4899`, dorado `#E8B54D`, letras Orbitron y Rajdhani.
7. Las guías van en dos páginas: la escrita y la de láminas. La portada `jullverse-guias.html` tiene una tarjeta para cada una.
8. Contestar corto. Si algo no se entiende, preguntar antes de inventar.

---

## 6. Páginas del sitio

| Archivo | Qué es |
|---|---|
| `index.html` | Hub principal del Multiverso (no tocar) |
| `gaming.html`, `futbol.html`, `suspenso.html`, `comunidad.html` | Secciones del Multiverso (no tocar) |
| `jullverse.html` | Portada de Jullverse |
| `jullverse-videos.html`, `-noticias.html`, `-addons.html`, `-otros.html` | Secciones de Jullverse |
| `jullverse-guias.html` | Portada de las 5 guías |
| `jullverse-druida.html`, `-paladin`, `-profesiones`, `-combinaciones`, `-razas-clases` | Guías escritas |
| Las mismas con `-laminas` | Solo las láminas |

Carpetas: `img/` (imágenes, y `img/addons/` con los iconos), `data/token.json` (precio del token, lo escribe un robot cada hora), `scripts/` y `.github/workflows/`.

---

## 7. Actualizar los addons

1. Escanear la carpeta del juego:

```powershell
Get-ChildItem -LiteralPath 'D:\World of Warcraft\_forever_\Interface\AddOns' -Directory | Select-Object -ExpandProperty Name | Sort-Object
```

2. Comparar con lo que ya está en `jullverse-addons.html`. Cada addon es un bloque así:

```javascript
{
  id:"identificador", name:"Nombre visible", cat:"interfaz", ver:"1.2.3", forever:true,
  desc:"Qué hace, en dos o tres líneas.",
  cmd:"/comando",
  modules:[
    ["CarpetaDelAddon","1.2.3","Qué aporta ese módulo."]
  ]
}
```

3. Categorías: `interfaz`, `mapas`, `misiones`, `combate`, `loot`, `bolsas`, `personaje`, `audio`, `sistema`.
4. Cada addon lleva icono en `img/addons/<id>.png`, sacado de la propia carpeta del addon.
5. Actualizar los contadores del encabezado.
6. Comprobar que el JavaScript no está roto antes de subir:

```powershell
node --check archivo.js
```

---

## 8. Subir un cambio

```powershell
cd 'Z:\OpenCode-Agente\Pagina-Jullverse'
git add -A
git commit -m "Descripcion corta"
git push origin main
```

Si el push falla porque alguien más subió algo mientras trabajabas, se pide al agente que lo resuelva. No hace falta que el usuario toque comandos.

---

## 9. Para el agente

1. Comprobar `git`, `python` y `node` antes de tocar nada.
2. Confirmar que existe `Z:\OpenCode-Agente\Pagina-Jullverse` y que es el repo correcto.
3. Si falta autenticación, pedirle al usuario que inicie sesión en la ventana de GitHub. No pedir tokens ni contraseñas por el chat.
4. Si algo del documento no coincide con lo que hay en el repo, avisar de que el documento quedó viejo.
