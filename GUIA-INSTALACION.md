# 🚀 GUÍA DE INSTALACIÓN — El Multiverso de JULL
**Sin saber programar. Paso a paso. Costo: $0**

**Tu sitio quedará en → https://multiversoJULL.github.io**

---

## 📁 ARCHIVOS DEL SITIO

Tu sitio tiene 5 páginas:
| Archivo | Página |
|---------|--------|
| `index.html` | Hub Principal (página de inicio) |
| `gaming.html` | Canal Jullverse 🎮 |
| `suspenso.html` | Canal Bit de Suspenso 💾 |
| `futbol.html` | Canal Vinotinto Galáctico ⚽ |
| `comunidad.html` | Foro de la Comunidad 🌌 |

---

## PASO 1 — Obtén tu API Key de YouTube (GRATIS)

> Esto hace que los videos aparezcan automáticamente en tu sitio.

1. Ve a → https://console.cloud.google.com
2. Inicia sesión con tu cuenta de Google (Gmail)
3. Haz clic en **"Seleccionar proyecto"** → **"Nuevo proyecto"**
4. Nombre del proyecto: `multiverso-jull` → **Crear**
5. En el menú izquierdo: **"APIs y servicios"** → **"Biblioteca"**
6. Busca: `YouTube Data API v3` → clic en ella → **"Habilitar"**
7. Ve a **"Credenciales"** → **"+ Crear credencial"** → **"Clave de API"**
8. ¡Copia esa clave! Se ve así: `AIzaSyXXXXXXXXXXXXXXXXXXXX`

**Luego en cada archivo HTML**, abre el archivo con el Bloc de Notas, busca esta línea:
```
const YT_API_KEY = 'TU_API_KEY_AQUI';
```
Reemplaza `TU_API_KEY_AQUI` con tu clave. Repite en los 5 archivos.

---

## PASO 2 — Configura Firebase para el Foro (GRATIS)

> Esto activa el foro de comunidad tipo Reddit.

1. Ve a → https://console.firebase.google.com
2. Inicia sesión con tu Gmail → **"Agregar proyecto"**
3. Nombre: `multiverso-jull` → Continuar → **Crear proyecto**
4. En el panel, haz clic en **"</>"** (ícono web)
5. Apodo de la app: `jull-web` → **Registrar app**
6. Copia el bloque `firebaseConfig` que aparece. Se ve así:
```javascript
const firebaseConfig = {
  apiKey: "AIza...",
  authDomain: "multiverso-jull.firebaseapp.com",
  projectId: "multiverso-jull",
  storageBucket: "multiverso-jull.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abc123"
};
```
7. Abre `comunidad.html` con el Bloc de Notas, busca el bloque `firebaseConfig` y reemplaza todos los valores con los tuyos.
8. En Firebase, ve a **"Firestore Database"** → **"Crear base de datos"**
9. Elige **"Modo de prueba"** → Selecciona región `us-east1` → **Habilitar**
10. Ve a la pestaña **"Reglas"** y reemplaza todo el contenido con esto:
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /threads/{threadId} {
      allow read: if true;
      allow create: if request.resource.data.title.size() > 0;
      allow update: if true;
    }
  }
}
```
11. Haz clic en **"Publicar"**

---

## PASO 3 — Sube el sitio a GitHub Pages (GRATIS)

> Tu cuenta de GitHub ya existe: https://github.com/multiversoJULL

### 3a. Crea el repositorio
1. Entra a → https://github.com/multiversoJULL
2. Haz clic en el botón verde **"New"**
3. En "Repository name" escribe exactamente:
   ```
   multiversoJULL.github.io
   ```
   ⚠️ Debe ser idéntico a tu usuario, mayúsculas incluidas
4. Selecciona **"Public"**
5. Haz clic en **"Create repository"**

### 3b. Sube los archivos
1. Dentro del repositorio recién creado, haz clic en **"uploading an existing file"**
2. Arrastra los 5 archivos HTML al área de carga:
   - index.html
   - gaming.html
   - suspenso.html
   - futbol.html
   - comunidad.html
3. En la parte de abajo haz clic en **"Commit changes"**

### 3c. Activa GitHub Pages
1. Ve a la pestaña **"Settings"** de tu repositorio
2. En el menú izquierdo busca: **"Pages"**
3. En "Source": selecciona **"Deploy from a branch"**
4. Branch: **main** → carpeta: **/ (root)**
5. Haz clic en **"Save"**

✅ **En 2-5 minutos tu sitio estará en:**
# https://multiversoJULL.github.io

---

## PASO 4 — Verifica que todo funciona

Visita tu sitio y comprueba:
- [ ] La página principal carga con los 3 colores
- [ ] Los videos de cada canal aparecen (requiere API Key configurada)
- [ ] Los enlaces entre páginas funcionan
- [ ] El foro de comunidad carga
- [ ] En móvil se ve bien

---

## 🔧 CÓMO HACER CAMBIOS DESPUÉS

Para editar cualquier texto, color o sección:
1. Abre el archivo `.html` con el **Bloc de notas** (Windows) o **TextEdit** (Mac)
2. Edita lo que necesites
3. Guarda el archivo
4. Ve a tu repositorio en GitHub → arrastra el archivo actualizado → **Commit changes**
5. Los cambios se ven en ~2 minutos

---

## ❓ SOLUCIÓN DE PROBLEMAS

**Los videos no aparecen:**
→ Verifica que la API Key esté bien copiada (sin espacios extra) en los 5 archivos
→ Confirma que YouTube Data API v3 esté habilitada en Google Cloud Console

**El sitio no carga o da error 404:**
→ Confirma que el nombre del repositorio sea exactamente `multiversoJULL.github.io`
→ Espera 5-10 minutos después de activar GitHub Pages
→ Prueba entrar en modo incógnito del navegador

**El foro no guarda mensajes:**
→ Verifica que el `firebaseConfig` en comunidad.html tenga tus datos reales
→ Confirma que las reglas de Firestore estén publicadas correctamente

**La página se ve rara en el celular:**
→ El sitio es responsive, debería verse bien. Si no, avísale a Claude para ajustar.

---

## 📞 PARA PEDIR CAMBIOS

Comparte los archivos HTML con Claude y pide lo que necesites, por ejemplo:
- "Agrega mis redes sociales en el footer"
- "Cambia el texto de la descripción de Jullverse"
- "Agrega una sección de Twitch"
- "Pon mi foto de perfil en la página principal"

---

**🎉 Tu sitio: https://multiversoJULL.github.io**
