<h1><b>Proyecto MAW</b></h1>

<p>Este es un proyecto para la materia Taller de Proyecto I de la carrera de Ingenieria en Computación de la Universidad Nacional de La Plata. Consiste en un vehiculo con cuatro motores, el cual es controlado mediante un joystick. Además, esta compuesto de una cámara con la que realiza una transmisión de video para poder facilitar el control del vehiculo.</p>
<p>Para facilitar el control del vehiculo se diseño un software de control mediante pyhton con el cual recivir video, y el envio y recepcion de mensajes.</p>

<h2><b>Software de Control</b></h2>
<p>Este repositorio contiene el codigo del Software de Control para poder comunicarse y controlar el vehiculo.</p>
<p>El programa consta de una ventan unica donde se visualiza el video y una consola donde puede ver los mensajes salientes y entrantes. Mientras que 2do plano mantiene 3 threads, uno que recive la transmision de video, otro consultando si hay algun mensaje que recivir, y por ultimo uno que lee continuamente el mando conectado, procesa los inputs y envia el mensaje corespondiete al vehiculo.</p>

<h2><b>Requerimientos</b></h2>
El programa solo requiere estar conectado a la red generada por el vehiculo, tener un mando conectado y las bibliotecas correspondiendes instaladas:
<li>Tkinter</li>
<li>Pygame</li>
<li>cv2</li>
<li>PIL</li>
<li>urllib</li>
<li>numpy</li>

<h2><b>Requerimientos</b></h2>
<p>El programa surge de la necesidad de tener un software que permita controlar el vehiculo, mas no era un objetivo del proyecto, por tanto se opto por la simplicidad y funcionalidad. Este software puede presentar errores sino se usa de la manera y contexto adecuado.</p>

<h2><b>Controles</b></h2>

<h3>Adevertencia:</h3> el programa se diseño basado en un mando generico disponible, y no fue testeado en otro, por tanto no se asegura que las teclas correspondan con otros mandos.
-Adevertencia: no precione el boton MODE conectado al vehiculo, puede generar un error que requiera un reinicio del vehiculo.
