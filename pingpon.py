from pygame import*

back = (145, 145, 146)
win_width = 750
win_height = 500
mw = display.set_mode((win_width,win_height))
mw.fill(back)

clock = time.Clock()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        display.update()
    clock.tick(40)


