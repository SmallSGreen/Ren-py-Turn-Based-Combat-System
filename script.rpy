# Chinese Support

init: 
    $ style.default.font = "font.ttf"
    $ style.default.language = "font"

# Character Definitions

define t = Character(_("我是人偶"), color= "#ffffffff")

# Random Number Generator

label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

# HP and HP Bar

init python:
        player_hp = 10
        player_max_hp = 10
        enemy_hp = 10
        enemy_max_hp = 10
        enemy_name = "人偶"

screen hp_bars_1v1:

    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "Player"
        bar value player_hp range player_max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "[enemy_name]"
        bar value enemy_hp range enemy_max_hp

label start:

    t "hi"

    $ enemy_name = t
    $ enemy_max_hp = 69

    jump battle

label battle:

    
    $ player_hp = player_max_hp
    $ enemy_hp = enemy_max_hp
    $ anger = 0

    "test"
    show screen hp_bars_1v1
    
    while player_hp > 0:

        call dice_roll

        menu:
            "Punch":
                $ enemy_hp -= d4
                "You punched [enemy_name] for [d4] damage!"

                if enemy_hp <= 0:
                    "You defeated the [enemy_name]!"
                    jump options

            "Mock":
                "You tell the [enemy_name] to kill himself..."
                "The [enemy_name] is enraged!"
                $ anger += 1

        $ player_hp -= (2+anger) 
        "The [enemy_name] punched you for [2+anger] damage!"


    "You are defeated!"

    hide screen hp_bars_1v1
    menu options:
        "Try Again":
            jump battle

        "Quit":
            return

    return