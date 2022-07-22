<p align="center">
  <img alt="SAEP logo" src="https://i.ibb.co/gFJkDmc/filename.png" width=100  >
</p>
<h1 align="center">
  <a href="#">
    Sistema de Administración Escolar de Posgrado
  </a>
</h1>

<p align="center">
  <strong>El Sistema de Administración Escolar de Posgrado será un sistema de información intensivo y extensivo para poder controlar toda la información académica de cada estudiante de posgrado. </strong><br>
  @ESFM-X
</p>


<p align="center">
    <img src="https://img.shields.io/github/license/JoulesCH/juegos_del_hambre.svg" alt="MIT License" />

  <a href="#">
    <img src="https://img.shields.io/github/issues/JoulesCH/juegos_del_hambre.svg" alt="No issues." />
  </a>

  <a href="#">
    <img src="https://img.shields.io/github/watchers/JoulesCH/juegos_del_hambre.svg" alt="Current npm package version." />
  </a>

  <a href="#">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="Watchers" />
  </a>
</p>

<p align="center">
    <a href="#">
        <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E" alt="Javascript" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D" alt="VueJS" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/SASS-hotpink.svg?style=for-the-badge&logo=SASS&logoColor=white" alt="SaSS" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" alt="Postgres" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white" alt="Redis" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
    </a>
    <a href="#">
        <img src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white" alt="Heroku" />
    </a>
</p>

## Alcance

☑️ **Visualización de Constancias** 

- El sistema debe ser capaz de generar dos tipos de constancias por default:
    - Constancia de inscripción con historial
    - Constancia de seguimiento académico para CONACyT
- Las constancias pueden o no llevar el espacio para firma autógrafa del Jefe de la SEPI de acuerdo a la solicitud que se haga
- Las constancias deben de contar con un QR que permita su validación a través de una app o un portal web

☑️ **Captura de información**

- Subir de forma masiva e individual el historial académico del alumno (administradores SEPI)
- Que sea posible subir la lista de calificaciones (docentes)

☑️ **Catálogos que deben contar con módulo de administración para ABC simples**

- Programa Académico
- Institución Procedencia

## Observaciones Técnicas

- Contemplar que un mismo alumno puede tener varios números de boleta, pues se le asigna uno diferente cada vez que se inscriben a un posgrado (de Maestría a Doctorado o de Maestría Trunca a Maestría).
- El diseño de la página deberá tener coherencia visual con la *[Guía de Diseño Web del IPN](https://www.ipn.mx/assets/files/cenac/docs/Web/GuiaDeDisenoWeb.pdf).*

# Despliegue Local 🎸

Somos un **equipo ágil**, por lo que necesitamos desarrollar Software de forma rápida y sencilla, sin  que exista intervención humana a la hora de mandar nuestro Software a producción. 

Para trabajar sería necesario que todos los desarrolladores:

- Tengan el mismo sistema que el de producción (linux)
- Tengan exactamente la misma versión del lenguaje backend
- Instalen las dependencias (librerías) con la misma versión
- Instalen la RDBMS (base de datos) y la tengan ejecutando

y un par de cosas más. 

Como te puedes imaginar **no es factible** cumplir con muchos de de esos puntos. A continuación te presentamos la tecnología que nos simplifica el desarrollo, haciendo que no nos tengamos que preocupar por lo anterior.  

## 1️⃣ **Docker**

Esta tecnología permite instalar e iniciar en un **contenedor** (un entorno cerrado) aquellas cosas que la aplicación necesita para ser ejecutada (lenguaje backend, dependencias, etc.) y la propia aplicación. Dicho contenedor puede iniciarse en **cualquier** máquina que tenga instalado Docker, sin importar su sistema operativo. También se encarga de instalar las dependencias en las versiones indicadas, haciendo que todos veamos el mismo producto.

## 2️⃣**Docker Compose**

Con **Compose** podemos definir varios contenedores Docker y la configuración de la aplicación en cuestión. De esta manera con un solo comando podemos crear e iniciar los servicios configurados.

## 3️⃣ WSL

Windows Subsystem for Linux es una capa de compatibilidad desarrollada por Microsoft para correr Linux nativamente en Windows 10; **simula** un [kernel de Linux](https://es.wikipedia.org/wiki/Nucleo_Linux) (sin contener código de Linux propiamente dicho).

# Instalar Docker 🎛️

## 📃**Guía Oficial**

Puedes revisar la guía oficial entrando al siguiente link: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

## 📑Guía rápida

### **Windows 10**

- Necesitas tener **WSL** (Windows Subsystem For Linux). Puedes instalarlo y activarlo entrando a [este enlace](https://www.wikiversus.com/informatica/windows/como-instalar-wsl-windows-subsystem-for-linux-windows-10/); no es necesario que instales alguna versión de Linux en específico.
- Activar la **virtualización desde la BIOS**. Para ver si tienes la virtualización activa puedes abrir el *administrador de tareas,* ir a *Rendimiento -> CPU* y buscar el parámetro *Virtualización.* Si no está habilitado entonces:
    1. **Acceder a la BIOS de tu computadora**, deberás apagar tu computadora y cuando se esté prendiendo presionar una tecla especial (depende de cada computadora, googlea el modelo de computadora seguido de "tecla BIOS")
    2. Buscar alguna opción que diga Virtual Technology o Virtualization Technology y **activarla** (igual cambia por cada computadora, googlea tu modelo)
- Instalar [Docker Desktop for Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)

### **Mac**

- Instalar [Docker Desktop for Mac](https://docs.docker.com/docker-for-mac/install/)

Si utilizas **Linux** muy probablemente no estás leyendo esta guía para instalar Docker.

# Correr la aplicación 💻

## 🏗️ Construir los contenedores

Deberás descargar y construir los contenedores, ejecutar:

```jsx
$ docker-compose build
```

este comando se debe ejecutar cada vez que las dependencias (librerías) cambien, normalmente se recomienda que lo hagas cada vez que sincronices tu repositorio con el remoto.

## 🆙Iniciar los contendores

Una vez que hayas construido, debes ejecutar el siguiente comando para iniciar todo:

```jsx
$ docker-compose up
```

**Tip** puedes utilizar el siguiente comando para construir y después iniciar los contenedores:

```jsx
$ docker-compose up --build
```

Para acceder a la aplicación debes ingresar a la url: **http://localhost:8080**