number = 0

def on_button_pressed_a():
    global number
    music.play_melody("C E E F F - - - ", 0)
    while True:
        number += 1
        basic.show_string("" + str((number)))
        basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)
