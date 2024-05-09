import game, engine

while True:
    play = engine.menu()
    running = True
    if play and running:
        game.reset()
        running = True
        while running:
            running = game.update()


# nichts   = 0
# w bauer  = 1
# s bauer  = 2
# w turm   = 3
# s turm   = 4
# w pferd  = 5
# s pferd  = 6
# w läufer = 7
# s läufer = 8
# w dame   = 9
# s dame   = 10
# w könig  = 11
# s könig  = 12