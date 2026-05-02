# 🐍 Manual instalación de Python y VS Code (Windows)

Este manual contiene absolutamente todo lo necesario para preparar tu entorno de desarrollo en Windows desde cero.

---

## 🛠️ PARTE 1: Instalación de Python en Windows

1. **Descarga:** 
   - Ve al sitio oficial [python.org/downloads](https://www.python.org/downloads/)[cite: 2].
   - Haz clic en el botón amarillo que dice **"Download Python 3.x.x"** (siempre descarga la versión más reciente).

2. **Ejecución del Instalador (PASO CRÍTICO):**
   - Abre el archivo `.exe` que acabas de descargar.
   - **¡IMPORTANTE!:** Antes de hacer clic en cualquier otro botón, busca en la parte inferior la casilla que dice **"Add Python 3.x to PATH"** y **MÁRCALA**. Si olvidas este paso, la terminal no reconocerá tus comandos de Python más adelante.
   - Ahora sí, haz clic en **"Install Now"**.

3. **Verificación:** 
   - Presiona la tecla Windows en tu teclado, escribe `cmd` (Símbolo del sistema) y presiona Enter[cite: 2].
   - En la ventana negra que aparece, escribe el siguiente comando y pulsa Enter:
     ```cmd
     python --version
     ```
   - Si el sistema te responde con algo como `Python 3.12.x`, la instalación fue exitosa[cite: 2].

---

## 💻 PARTE 2: Instalación de Visual Studio Code (VS Code)

VS Code es el editor (bloc de notas inteligente) donde escribirás tus programas.

1. **Descarga:** Ve a [code.visualstudio.com](https://code.visualstudio.com/) y haz clic en el botón **"Download for Windows"**[cite: 2].
2. **Instalación:** Ejecuta el instalador descargado y sigue los pasos por defecto (puedes darle a "Siguiente" en todo)[cite: 2].
3. **Configuración para Python:**
   - Abre el programa VS Code una vez instalado[cite: 2].
   - En la barra lateral izquierda, busca el icono que parece cuatro cuadritos (Extensiones) o presiona `Ctrl + Shift + X`[cite: 2].
   - En la barra de búsqueda, escribe **"Python"**[cite: 2].
   - Selecciona la extensión creada por **Microsoft** y haz clic en el botón azul de **"Install"**[cite: 2].

---

## 🚀 PARTE 3: Tu Primer Programa (La Prueba de Fuego)

1. Abre VS Code y ve al menú superior: `Archivo > Nuevo archivo de texto`[cite: 2].
2. Guárdalo inmediatamente (`Ctrl + S`) con el nombre `hola.py` (es fundamental que el nombre termine en **.py**)[cite: 2].
3. Escribe el siguiente código dentro del archivo:
   ```python
   print("¡Felicidades! Ya tengo Python y VS Code configurados.")
