<h1><b>Proyecto MAW</b></h1>

<p>Este es un proyecto para la materia Taller de Proyecto I de la carrera de Ingenieria en Computación de la Universidad Nacional de La Plata. Consiste en un vehiculo con cuatro motores, el cual es controlado mediante un joystick. Además, esta compuesto de una cámara con la que realiza una transmisión de video para poder facilitar el control del vehiculo.</p>
<p>Para facilitar el control del vehiculo se diseño un software de control mediante pyhton con el cual recivir video, y el envio y recepcion de mensajes.</p>

<h2><b>Software de Control</b></h2>
<p>Este repositorio contiene el codigo del Software de Control para poder comunicarse y controlar el vehiculo.</p>
<p>El programa consta de una ventan unica donde se visualiza el video y una consola donde puede ver los mensajes salientes y entrantes. Mientras que 2do plano mantiene 3 threads, uno que recive la transmision de video, otro consultando si hay algun mensaje que recivir, y por ultimo uno que lee continuamente el mando conectado, procesa los inputs y envia el mensaje corespondiete al vehiculo.</p>
