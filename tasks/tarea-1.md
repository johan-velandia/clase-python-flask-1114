# Tarea 1 - Levantar una aplicacion Flask desde cero

## Objetivo tecnico

Poner en marcha el proyecto en tu entorno local, entender para que sirve cada pieza minima del setup y verificar que la aplicacion responde en el navegador.

En esta primera clase no alcanza con "hacerlo andar". Tienes que empezar a distinguir que problema resuelve cada paso: aislamiento del entorno, instalacion de dependencias, arranque del servidor y renderizado de una plantilla HTML.

## Preparacion

Para instalar dependencias y ejecutar el proyecto, sigue el `README.md`.

## Consigna

1. Instala las dependencias y levanta la aplicacion siguiendo el `README.md`.

2. Abre la aplicacion en el navegador y comprueba que responde correctamente.

3. Modifica la vista base y verifica el cambio:

   Edita `templates/index.html`, cambia al menos el `<title>` y el `<h1>`, guarda y recarga la pagina.

   Este paso existe para que veas la relacion concreta entre archivo fuente, servidor y resultado en navegador. Codigo que no observas, no lo entendes.

## Preguntas de reflexion tecnica

1. Que problema concreto resuelve el entorno virtual en un proyecto Python?
El entorno virtual resuelve el problema de que distintos proyectos pueden necesitar diferentes versiones de las mismas librerías.

Sin entorno virtual, todas las librerías se instalan en el Python global del sistema. Eso provoca conflictos cuando un proyecto requiere una versión específica y otro necesita otra distinta.

Por ejemplo:

Un proyecto puede necesitar Flask 2.x
Otro proyecto puede necesitar Flask 3.x

Si ambas versiones se instalan globalmente, una termina reemplazando a la otra.

El entorno virtual crea un espacio aislado para cada proyecto donde se instalan únicamente las dependencias que ese proyecto necesita. Así:

cada proyecto tiene sus propias librerías
no hay conflictos de versiones
el Python del sistema no se modifica
el entorno puede reproducirse fácilmente en otra máquina

En resumen, el entorno virtual sirve para aislar dependencias y mantener proyectos independientes entre sí.
2. Que diferencia hay entre instalar `Flask` globalmente y hacerlo dentro de `.venv`?
La diferencia está en el alcance de la instalación.

Instalación global

Cuando Flask se instala globalmente:

queda disponible para todo el sistema
todos los proyectos usan esa misma instalación
todos comparten la misma versión
pueden aparecer conflictos entre proyectos

Además, modificar paquetes globales puede afectar herramientas del sistema o otros desarrollos.

Instalación dentro de .venv

Cuando Flask se instala dentro de .venv:

solo está disponible para ese proyecto
las librerías quedan aisladas
cada proyecto puede tener versiones distintas
no se altera el Python global del sistema

Eso permite que dos proyectos usen versiones diferentes de Flask sin interferirse entre sí.

3. Por que `requirements.txt` forma parte del proyecto y no de tu maquina personal?
forma parte del proyecto porque describe las dependencias que el proyecto necesita para funcionar correctamente, no las preferencias o configuraciones personales de una máquina.

Ese archivo pertenece al proyecto ya que define:

qué librerías utiliza
qué versiones requiere
qué entorno necesita para ejecutarse

Por ejemplo, si un proyecto usa:

Flask
SQLAlchemy
Requests

esas dependencias deben ser iguales para cualquier persona que trabaje en el proyecto.

Por eso requirements.txt se comparte junto al código fuente.

Si el archivo perteneciera solo a tu máquina personal:

otro desarrollador no sabría qué instalar
el proyecto podría fallar en otra computadora
aparecerían diferencias entre entornos
el servidor de producción no tendría las mismas librerías

La función de requirements.txt es garantizar que todos trabajen con el mismo entorno de dependencias:

desarrolladores
servidores
contenedores Docker
sistemas de despliegue continuo
4. Cuando ejecutas `python app.py`, que archivo actua como punto de entrada y por que?
el archivo app.py actúa como punto de entrada del programa porque es el archivo que Python recibe directamente para comenzar la ejecución.

Python interpreta ese archivo primero y ejecuta su contenido de arriba hacia abajo.

Se le llama “punto de entrada” porque desde allí inicia el flujo principal de la aplicación:

se crean objetos
se importan módulos
se configura la aplicación
se inicia el servidor
se ejecuta la lógica principal

Por ejemplo, en un proyecto con Flask, app.py normalmente contiene:

la creación de la aplicación Flask
las rutas
el arranque del servidor

Por eso Python empieza desde ese archivo.
5. Que relacion hay entre la ruta `/`, la funcion `inicio()` y el archivo `templates/index.html`?
La relación es que cada elemento cumple una función distinta dentro del flujo de una aplicación web hecha con Flask.

La ruta / representa la URL principal del sitio.
La función inicio() procesa la petición asociada a esa ruta.
El archivo templates/index.html contiene la página HTML que se mostrará al usuario.
6. Que evidencia te da la terminal de que el servidor arranco correctamente?
La terminal da varias evidencias de que el servidor de Flask inició correctamente.

Las señales más comunes son:

aparece un mensaje indicando que la aplicación está corriendo
se muestra una dirección URL local
la terminal queda “escuchando” solicitudes sin cerrarse
no aparecen errores de ejecución

Por ejemplo, normalmente Flask muestra algo similar a:
7. Si cambias el HTML y el navegador muestra otra cosa, que te demuestra eso sobre el flujo entre backend y frontend en este proyecto?
Si cambias el archivo HTML y el navegador muestra el cambio, eso demuestra que existe una conexión directa entre el backend y el frontend dentro del proyecto.

En este flujo:

el backend construido con Flask entrega la plantilla HTML
el frontend es el contenido visual que el navegador renderiza

Eso significa que:

El navegador hace una petición al servidor.
Flask recibe la petición mediante una ruta.
Flask ejecuta una función del backend.
Esa función devuelve un archivo HTML.
El navegador renderiza ese HTML y muestra el resultado visual.

## Entregable

La tarea se considera completa si puedes demostrar estas cuatro cosas:

1. El entorno virtual esta creado y activado.
2. Las dependencias se instalaron desde `requirements.txt`.
3. La aplicacion corre en tu maquina y responde en el navegador.
4. Modificaste `templates/index.html` y podes señalar exactamente donde se refleja ese cambio.

## Cierre

No estas aprendiendo a tipear comandos. Estas empezando a construir criterio tecnico. Si hoy entiendes que levanta el servidor, de donde salen las dependencias y por que Flask encuentra esa plantilla, entonces arrancaste bien. Simple no significa superficial.
