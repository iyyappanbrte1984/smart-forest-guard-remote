basic.showLeds(`
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    `)
basic.showLeds(`
    . . . . .
    . # # # .
    . # # # .
    . # # # .
    . . . . .
    `)
basic.showLeds(`
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    # # # # #
    `)
basic.clearScreen()
led.setBrightness(64)
radio.setGroup(77)
let TEMP = input.temperature()
basic.forever(function () {
    basic.showNumber(TEMP)
    led.plotBarGraph(
    TEMP,
    50
    )
    if (TEMP >= 30) {
        radio.sendNumber(1)
    }
})
