def joystickInit():
    pygame.init()# Inicializar el joystick
    pygame.joystick.init()
    while(pygame.joystick.get_count()==0):
        print("Conecte un joystick")
        time.sleep(2)
    joystick = pygame.joystick.Joystick(0)  # Selecciona el primer joystick
    joystick.init()
    return joystick

def joystickRead():
    joystickInit()

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    button = event.button
                    print(button)
                elif event.type == pygame.JOYAXISMOTION:
                    axis = event.axis
                    value = round((event.value)*100)
                    data = f"A{axis}:{value}"
                    print(data)
        except KeyboardInterrupt:
            pass
    