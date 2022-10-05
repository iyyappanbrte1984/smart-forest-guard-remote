def on_button_pressed_a():
    global Reading
    pins.analog_write_pin(AnalogPin.P1, 1023)
    Reading = pins.analog_read_pin(AnalogPin.P0)
    basic.show_number(Reading)
    pins.analog_write_pin(AnalogPin.P1, 0)
    led.plot_bar_graph(Reading, 1023)
    if Reading < 1000:
        basic.show_icon(IconNames.YES)
        pins.servo_write_pin(AnalogPin.P1, 180)
        basic.pause(2000)
        pins.servo_write_pin(AnalogPin.P1, 0)
        basic.pause(2000)
        pins.servo_write_pin(AnalogPin.P1, 180)
        basic.pause(2000)
        pins.servo_write_pin(AnalogPin.P1, 0)
        basic.pause(2000)
    else:
        basic.show_icon(IconNames.NO)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(TEMP)
    led.plot_bar_graph(TEMP, 50)
    if TEMP >= 30:
        radio.send_number(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

Reading = 0
TEMP = 0
led.set_brightness(64)
radio.set_group(77)
TEMP = input.temperature()
datalogger.set_column_titles("moisture", "Temperatue")

def on_every_interval():
    datalogger.log(datalogger.create_cv("moisture", Reading),
        datalogger.create_cv("Temperatue", TEMP))
loops.every_interval(1000, on_every_interval)
