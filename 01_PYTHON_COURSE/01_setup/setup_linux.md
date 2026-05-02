# Manual de Instalación: Python y Visual Studio Code en Linux

> **Guía completa, paso a paso, para instalar Python y Visual Studio Code en distribuciones Linux basadas en Debian/Ubuntu.**

---

## Tabla de Contenidos

1. [Requisitos Previos](#1-requisitos-previos)
2. [Actualizar el Sistema](#2-actualizar-el-sistema)
3. [Instalación de Python](#3-instalación-de-python)
   - 3.1 [Verificar si Python ya está instalado](#31-verificar-si-python-ya-está-instalado)
   - 3.2 [Instalar Python desde el repositorio oficial](#32-instalar-python-desde-el-repositorio-oficial)
   - 3.3 [Instalar una versión específica de Python con deadsnakes PPA](#33-instalar-una-versión-específica-de-python-con-deadsnakes-ppa)
   - 3.4 [Configurar Python como versión predeterminada](#34-configurar-python-como-versión-predeterminada)
   - 3.5 [Instalar pip](#35-instalar-pip)
   - 3.6 [Instalar y usar entornos virtuales](#36-instalar-y-usar-entornos-virtuales)
   - 3.7 [Verificar instalación completa de Python](#37-verificar-instalación-completa-de-python)
4. [Instalación de Visual Studio Code](#4-instalación-de-visual-studio-code)
   - 4.1 [Método 1: Instalar con el repositorio oficial de Microsoft (Recomendado)](#41-método-1-instalar-con-el-repositorio-oficial-de-microsoft-recomendado)
   - 4.2 [Método 2: Instalar con Snap](#42-método-2-instalar-con-snap)
   - 4.3 [Método 3: Descargar el paquete .deb manualmente](#43-método-3-descargar-el-paquete-deb-manualmente)
5. [Configurar VS Code para Desarrollo Backend con Python](#5-configurar-vs-code-para-desarrollo-backend-con-python)
   - 5.1 [Extensiones esenciales](#51-extensiones-esenciales)
   - 5.2 [Configurar el intérprete de Python en VS Code](#52-configurar-el-intérprete-de-python-en-vs-code)
   - 5.3 [Configuración recomendada (settings.json)](#53-configuración-recomendada-settingsjson)
6. [Solución de Problemas Comunes](#6-solución-de-problemas-comunes)
7. [Comandos de Referencia Rápida](#7-comandos-de-referencia-rápida)

---

## 1. Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente:

| Requisito | Descripción |
|---|---|
| **Sistema operativo** | Ubuntu 20.04 / 22.04 / 24.04 o Debian 10/11/12 |
| **Acceso sudo** | Tu usuario debe tener permisos de administrador |
| **Conexión a internet** | Necesaria para descargar paquetes |
| **Terminal** | Puedes usar cualquier emulador de terminal |

Para abrir la terminal en Ubuntu puedes presionar:

```
Ctrl + Alt + T
```

---

## 2. Actualizar el Sistema

Antes de instalar cualquier cosa, es una buena práctica actualizar los repositorios y paquetes del sistema.

```bash
sudo apt update && sudo apt upgrade -y
```

- `apt update` — Actualiza la lista de paquetes disponibles.
- `apt upgrade -y` — Instala las actualizaciones disponibles sin pedir confirmación.

---

## 3. Instalación de Python

### 3.1 Verificar si Python ya está instalado

Muchas distribuciones Linux ya incluyen Python. Verifica con:

```bash
python3 --version
```

Si obtienes una respuesta como `Python 3.x.x`, ya tienes Python instalado. Si no, continúa con los siguientes pasos.

También puedes verificar si `python` (versión 2) está instalado:

```bash
python --version
```

> ⚠️ **Nota:** Python 2 está oficialmente obsoleto desde enero de 2020. Se recomienda usar únicamente Python 3.

---

### 3.2 Instalar Python desde el repositorio oficial

Para instalar la versión de Python disponible en los repositorios de Ubuntu/Debian:

```bash
sudo apt install python3 -y
```

Verifica la instalación:

```bash
python3 --version
```

---

### 3.3 Instalar una versión específica de Python con deadsnakes PPA

Si necesitas una versión específica de Python (por ejemplo, 3.11 o 3.12), usa el PPA de deadsnakes:

**Paso 1: Agregar el repositorio deadsnakes**

```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
```

**Paso 2: Actualizar la lista de paquetes**

```bash
sudo apt update
```

**Paso 3: Instalar la versión deseada**

Reemplaza `3.12` con la versión que necesites:

```bash
sudo apt install python3.12 -y
```

**Paso 4: Verificar la instalación**

```bash
python3.12 --version
```

---

### 3.4 Configurar Python como versión predeterminada

Si tienes varias versiones de Python instaladas y quieres definir cuál es la predeterminada:

**Paso 1: Listar las versiones instaladas**

```bash
ls /usr/bin/python*
```

**Paso 2: Configurar alternativas**

```bash
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 2
```

**Paso 3: Seleccionar la versión predeterminada**

```bash
sudo update-alternatives --config python3
```

Se mostrará un menú. Escribe el número correspondiente a la versión que deseas usar y presiona `Enter`.

**Paso 4 (Opcional): Hacer que `python` apunte a `python3`**

```bash
sudo ln -sf /usr/bin/python3 /usr/bin/python
```

Verifica:

```bash
python --version
```

---

### 3.5 Instalar pip

`pip` es el gestor de paquetes de Python. Es fundamental para instalar librerías.

**Instalar pip para Python 3:**

```bash
sudo apt install python3-pip -y
```

**Verificar la instalación:**

```bash
pip3 --version
```

**Actualizar pip a la última versión:**

```bash
pip3 install --upgrade pip
```

**Instalar pip para una versión específica:**

```bash
python3.12 -m ensurepip --upgrade
```

---

### 3.6 Instalar y usar entornos virtuales

Los entornos virtuales son esenciales para aislar dependencias entre proyectos. Es una buena práctica usarlos siempre.

**Instalar el módulo venv:**

```bash
sudo apt install python3-venv -y
```

**Crear un entorno virtual:**

```bash
python3 -m venv nombre_del_entorno
```

Por ejemplo:

```bash
python3 -m venv .venv
```

**Activar el entorno virtual:**

```bash
source .venv/bin/activate
```

Cuando el entorno esté activo, verás el nombre del entorno al inicio de tu prompt:

```
(.venv) usuario@maquina:~/mi_proyecto$
```

**Instalar paquetes dentro del entorno:**

```bash
pip install nombre_paquete
```

**Desactivar el entorno virtual:**

```bash
deactivate
```

**Ver los paquetes instalados en el entorno:**

```bash
pip list
```

**Exportar dependencias a un archivo:**

```bash
pip freeze > requirements.txt
```

**Instalar dependencias desde un archivo:**

```bash
pip install -r requirements.txt
```

---

### 3.7 Verificar instalación completa de Python

Ejecuta los siguientes comandos para confirmar que todo está correctamente instalado:

```bash
python3 --version
pip3 --version
python3 -c "import sys; print(sys.path)"
```

Si todos devuelven resultados sin errores, ¡Python está listo!

---

## 4. Instalación de Visual Studio Code

Hay tres métodos para instalar VS Code en Linux. Se recomienda el **Método 1** por ser el más estable y permitir actualizaciones automáticas.

---

### 4.1 Método 1: Instalar con el repositorio oficial de Microsoft (Recomendado)

Este método agrega el repositorio oficial de Microsoft, lo que permite recibir actualizaciones automáticas con `apt`.

**Paso 1: Instalar dependencias necesarias**

```bash
sudo apt install wget gpg apt-transport-https -y
```

**Paso 2: Importar la clave GPG de Microsoft**

```bash
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
```

**Paso 3: Agregar el repositorio de VS Code**

```bash
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
```

**Paso 4: Actualizar la lista de paquetes**

```bash
sudo apt update
```

**Paso 5: Instalar VS Code**

```bash
sudo apt install code -y
```

**Paso 6: Verificar la instalación**

```bash
code --version
```

**Paso 7: Abrir VS Code**

```bash
code
```

O búscalo en el menú de aplicaciones de tu escritorio.

---

### 4.2 Método 2: Instalar con Snap

Snap es un sistema de paquetes universal disponible en Ubuntu. Es más sencillo pero puede ser un poco más lento al iniciar.

**Paso 1: Asegurarte de que Snap está instalado**

```bash
sudo apt install snapd -y
```

**Paso 2: Instalar VS Code con Snap**

```bash
sudo snap install code --classic
```

La flag `--classic` es necesaria porque VS Code necesita acceso completo al sistema.

**Paso 3: Verificar la instalación**

```bash
code --version
```

---

### 4.3 Método 3: Descargar el paquete .deb manualmente

Este método es útil si no tienes acceso a internet en el servidor o prefieres control total.

**Paso 1: Descargar el paquete .deb**

Ve a la página oficial de VS Code:

```
https://code.visualstudio.com/Download
```

Descarga el archivo `.deb` para Linux x64.

O descárgalo directamente desde la terminal:

```bash
wget "https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64" -O vscode.deb
```

**Paso 2: Instalar el paquete descargado**

```bash
sudo apt install ./vscode.deb -y
```

O con dpkg:

```bash
sudo dpkg -i vscode.deb
sudo apt --fix-broken install -y
```

**Paso 3: Verificar la instalación**

```bash
code --version
```

---

## 5. Configurar VS Code para Desarrollo Backend con Python

### 5.1 Extensiones esenciales

Abre VS Code y ve a la sección de extensiones con:

```
Ctrl + Shift + X
```

Busca e instala las siguientes extensiones:

| Extensión | ID | Descripción |
|---|---|---|
| **Python** | `ms-python.python` | Soporte completo para Python (linting, debugging, IntelliSense) |
| **Pylance** | `ms-python.vscode-pylance` | Motor de análisis estático avanzado para Python |
| **Python Debugger** | `ms-python.debugpy` | Depurador oficial para Python |
| **GitLens** | `eamodio.gitlens` | Mejora la integración con Git |
| **REST Client** | `humao.rest-client` | Probar APIs directamente desde VS Code |
| **Docker** | `ms-azuretools.vscode-docker` | Gestión de contenedores Docker |
| **Thunder Client** | `rangav.vscode-thunder-client` | Cliente HTTP alternativo a Postman |
| **Error Lens** | `usernamehw.errorlens` | Muestra errores en línea dentro del código |
| **indent-rainbow** | `oderwat.indent-rainbow` | Colorea los niveles de indentación |
| **Better Comments** | `aaron-bond.better-comments` | Colorea comentarios por tipo |

**También puedes instalarlas desde la terminal:**

```bash
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
code --install-extension ms-python.debugpy
code --install-extension eamodio.gitlens
code --install-extension humao.rest-client
code --install-extension ms-azuretools.vscode-docker
code --install-extension rangav.vscode-thunder-client
code --install-extension usernamehw.errorlens
code --install-extension oderwat.indent-rainbow
code --install-extension aaron-bond.better-comments
```

---

### 5.2 Configurar el intérprete de Python en VS Code

Cuando abras un proyecto con Python, debes seleccionar el intérprete correcto:

**Paso 1:** Abre la paleta de comandos:

```
Ctrl + Shift + P
```

**Paso 2:** Escribe y selecciona:

```
Python: Select Interpreter
```

**Paso 3:** Selecciona el intérprete de tu entorno virtual (aparecerá con la ruta `.venv/bin/python`) o la versión global de Python que desees usar.

> ✅ **Tip:** Si estás dentro de una carpeta con un entorno virtual activo, VS Code lo detectará automáticamente.

---

### 5.3 Configuración recomendada (settings.json)

Abre el archivo de configuración de VS Code:

```
Ctrl + Shift + P → "Open User Settings (JSON)"
```

Agrega o fusiona la siguiente configuración:

```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 4,
  "editor.formatOnSave": true,
  "editor.rulers": [79, 120],
  "editor.wordWrap": "on",
  "files.autoSave": "onFocusChange",
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "terminal.integrated.defaultProfile.linux": "bash",
  "workbench.colorTheme": "Default Dark+",
  "editor.minimap.enabled": false,
  "breadcrumbs.enabled": true
}
```

---

## 6. Solución de Problemas Comunes

### ❌ Error: `command not found: python`

**Causa:** El alias `python` no está configurado.

**Solución:**

```bash
sudo ln -sf /usr/bin/python3 /usr/bin/python
```

---

### ❌ Error: `pip: command not found`

**Causa:** pip no está instalado.

**Solución:**

```bash
sudo apt install python3-pip -y
```

---

### ❌ Error al abrir VS Code: `SUID sandbox helper binary...`

**Causa:** Problema de permisos con el sandbox de Chromium.

**Solución:**

```bash
sudo chown root:root /usr/share/code/chrome-sandbox
sudo chmod 4755 /usr/share/code/chrome-sandbox
```

---

### ❌ VS Code no detecta el entorno virtual

**Solución:**

1. Asegúrate de haber activado el entorno con `source .venv/bin/activate`.
2. Abre VS Code desde la misma terminal: `code .`
3. Selecciona el intérprete manualmente con `Ctrl + Shift + P → Python: Select Interpreter`.

---

### ❌ Error: `externally-managed-environment` al usar pip

**Causa:** En Ubuntu 23.04+ y Debian 12+, pip no puede instalar paquetes globalmente por defecto.

**Solución recomendada (usar entorno virtual):**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install nombre_paquete
```

**Solución alternativa (no recomendada para producción):**

```bash
pip install nombre_paquete --break-system-packages
```

---

## 7. Comandos de Referencia Rápida

### Python

| Comando | Descripción |
|---|---|
| `python3 --version` | Ver versión de Python instalada |
| `pip3 --version` | Ver versión de pip |
| `pip3 install paquete` | Instalar un paquete |
| `pip3 uninstall paquete` | Desinstalar un paquete |
| `pip3 list` | Listar paquetes instalados |
| `pip3 freeze > requirements.txt` | Exportar dependencias |
| `pip3 install -r requirements.txt` | Instalar desde requirements.txt |
| `python3 -m venv .venv` | Crear entorno virtual |
| `source .venv/bin/activate` | Activar entorno virtual |
| `deactivate` | Desactivar entorno virtual |
| `python3 script.py` | Ejecutar un script |
| `python3 -i` | Iniciar el intérprete interactivo |

### Visual Studio Code

| Atajo | Descripción |
|---|---|
| `Ctrl + Shift + P` | Paleta de comandos |
| `Ctrl + Shift + X` | Gestor de extensiones |
| `Ctrl + `` ` `` ` | Abrir terminal integrada |
| `Ctrl + Shift + E` | Explorador de archivos |
| `Ctrl + Shift + G` | Control de versiones Git |
| `Ctrl + B` | Mostrar/ocultar barra lateral |
| `Ctrl + /` | Comentar/descomentar línea |
| `Alt + Shift + F` | Formatear documento |
| `F5` | Iniciar depuración |
| `F9` | Agregar/quitar breakpoint |
| `Ctrl + Shift + `` ` `` ` | Nueva terminal integrada |
| `Ctrl + P` | Búsqueda rápida de archivos |
| `Ctrl + Shift + F` | Buscar en todos los archivos |

---

> 📌 **Nota final:** Este manual fue creado para distribuciones basadas en **Debian/Ubuntu**. Si usas Fedora, Arch, o cualquier otra distribución, algunos comandos varían (por ejemplo, `dnf` en lugar de `apt` en Fedora, o `pacman` en Arch Linux).

---

*Manual generado para desarrolladores backend — Python + VS Code en Linux.*
