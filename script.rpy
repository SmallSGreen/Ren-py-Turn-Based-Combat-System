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

# Shake when hurt

transform shake:
    xoffset -20
    linear 0.05 xoffset 20
    linear 0.05 xoffset -10
    linear 0.05 xoffset 10
    linear 0.05 xoffset 0

# HP and HP Bar

init python:
        player_hp = 40
        player_max_hp = 40
        enemy_hp = 40
        enemy_max_hp = 40
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

    t "測試模板"

    $ enemy_name = t
    $ enemy_max_hp = 40

    jump battle

label battle:

    show enemy at right
    show player at left
    play music "audio/Glorious_Morning.mp3" volume 0.4 fadein 1.0 fadeout 1.0 loop
    $ player_hp = player_max_hp
    $ enemy_hp = enemy_max_hp
    $ anger = 0

    show screen hp_bars_1v1
    
    while player_hp > 0:

        call dice_roll from _call_dice_roll

        menu:
            "重低音攻擊":
                $ enemy_hp -= d6
                play sound "audio/vine_boom.mp3" volume 1.1
                show enemy at shake
                "你對 [enemy_name] 造成了 [d6] 點傷害!"

                if enemy_hp <= 0:
                    play music "audio/Victory.mp3" volume 0.5 fadein 1.0 fadeout 1.0 loop
                    "你擊敗了 [enemy_name]!"
                    jump options

            "嘲諷":
                $ anger += d4
                "你告訴 [enemy_name] 去死一死..."
                "[enemy_name] 被激怒了!"
                "[enemy_name] 傷害加[d4]點!"

        $ player_hp -= (d4+anger) 
        show player at shake
        play sound "audio/metal_pipe.mp3" volume 0.8
        "[enemy_name] 對你造成了 [d4+anger] 傷害!"

    play music "audio/Sisyphus.mp3" volume 0.5 fadein 1.0 fadeout 1.0 loop
    "你被擊敗了..."

    hide screen hp_bars_1v1
    menu options:
        "再玩一次":
            jump battle

        "結束":
            return

    return