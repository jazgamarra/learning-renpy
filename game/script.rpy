# Crear personajes
define jaz = Character('Jamin', color='#C92C6D')
define jose = Character('Josek', color='#609EA2')
define sofi = Character('Sofia', color='#F2C94C')

# Definimos las imagenes 
image fondo_lapacho = 'bg_lapacho.jpg'
image img_jaz:
    'bellota.png'
    zoom 0.20 
    pos (1500, 900)

image img_jose:
    'mojojojo.png'
    zoom 1.2 

image img_sofi:
    'demon.png'
    zoom 0.5
    pos (1000, 800)

# Indicar en donde inicia el juego
label start:

    # Imagen de fondo 
    scene fondo_lapacho
    with fade 

    # Conversacion 
    'En un reino muy lejano en la ciudad del pinguino'
    show img_jose at left # Mostrar imagen a la izquierda 
    jose 'Buenos dias'
    hide jose 

    show img_jaz
    jaz 'Que se desayuna en esta casa? '
    menu: 
        'Cafe':
            jump jose_cafe
        'Sandia':
            jump sofia_sandia

    jump terminar

label sofia_sandia: 
    show img_sofi 
    with fade
    sofi 'Sin mi?'
    return 

label jose_cafe: 
    hide img_jose
    show img_jose at center
    with fade
    jose 'se eleva majestuosamente'
    return 

label terminar: 
    'Fin'
    