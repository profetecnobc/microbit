basic.show_string("Com et sents avui?")
basic.pause(500)
basic.show_icon(IconNames.HAPPY)
basic.pause(500)
basic.show_icon(IconNames.SAD)

def on_forever():
    pass
basic.forever(on_forever)
