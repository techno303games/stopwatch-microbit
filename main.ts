let number = 0
input.onButtonPressed(Button.A, function () {
    music.playMelody("C E E F F - - - ", 0)
    while (true) {
        number += 1
        basic.showString("" + (number))
        basic.pause(1000)
    }
})
