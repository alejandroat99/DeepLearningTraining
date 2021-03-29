# Desarrollo de Herramientas Formativas sobre Redes Neuronales aplicadas a la Visión por Computador

Este proyecto tiene como objetivo proporcionar una labor formativa en el ámbito del Deep Learning enfocándose
en el área de la Visión por Computador. En este repositorio se encuentran los cuadernos de trabajo desarrollados
que contienen todos los conceptos y fundamentos teóricos necesarios para comprender esta área, así como actividades
prácticas planteadas para aplicar los conocimientos obtenidos.

## Estructura
Los cuadernos se encuentran clasificados en tres grandes bloques:
1. Bloque de Fundamentos
2. Bloque de Aplicaciones Prácticas
3. Bloque de Proyectos

### Bloque de Fundamentos
Este bloque está centrado en explicar los conceptos y fundamentos teóricos de las redes neuronales y el Deep Learning,
se realizarán activades sencillas para mostrar ilustrar los conocimientos proporcionados y se desarrollarán redes
neuronales básicas para solucionar los problemas genéricos de esta área: clasificación binaria, clasificación multiclase
y regresión.

### Bloque de Aplicaciones Prácticas
Este bloque se centrará más en el uso de las redes neuronales en la resolución de problemas de Visión por Computador. Los
problemas a resolver estarán basados en redes neuronales convolucionales y aplicados desde el procesamiento de la imagen
hasta la detección de objetos.

### Bloque de Proyectos
Este bloque propone algunos proyectos interesantes a realizar que aplican todo lo aprendido en los bloque anteriores,
centrándose en el encadenamiento de técnicas para resolver los problemas planteados.

## Requisitos Técnicos
- Docker

## Ejecución
1. Descargar el contenido del repositorio
2. Construir la imagen docker: `docker build -t <image-name> `.
3. Ejecutar la imagen docker: `docker run -p <port>:8888 <image-name>`.
4. Acceder a la dirección: `127.0.0.1:<port>`.