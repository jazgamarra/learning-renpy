
# Crear personajes
define jaz = Character('Jamin', color='#C92C6D')
define jose = Character('Josek', color='#609EA2')

# Definimos las imagenes 
image fondo_lapacho = 'bg_lapacho.jpg'
image img_jaz:
    'bellota.png'
    zoom 0.25 
    pos (1000, 900)
    
image img_jose:
    'mojojojo.png'
    zoom 1.2 

# Indicar en donde inicia el juego
label start:

    # Imagen de fondo 
    scene fondo_lapacho
    
    # Conversacion 
    'En un reino muy lejano en la ciudad del pinguino'
    show img_jose
    jose 'Buenos dias'
    hide img_jose
    show img_jaz
    jaz 'Malos dias'
    
