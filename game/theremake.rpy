# the remake part, obviously...duh?

label theRemake:
    # scene bg ricefields
    scene black
    with fade
    show neutral
    with dissolve
    "Okaaaaaaaaaay! So eto na nga! haha Ayos na ha? TheRemake na to. \nAndito yung effort ko talaga e."
    show ehe
    "Yung bracelet na tig-20, humanap na lang tayo some other time. \nWorth 30 na ung bibilhin ko for you para mas okay. Hehe JK!"
    hide ehe
    "Game na! Q&A! ;)"
    "Do you remember when we first held hands?"

    show neutral at left

    menu:
        "Syempre naman!":
            jump q1_yes

        "Uhhh... (\"Hindi\" in Pinky's tone)":
            jump q1_no

    label q1_yes:
        $ menu_flag = True
        # user input placed here
        python:
            date1 = renpy.input("Kailan? (mmddyyyy)")
            date1 = date1 # "07122018"
        if str(date1) == ("07122018"):
            jump date1_done
        else:
            "Awwwwww. Mahirap ba to? Need a clue? \n2nd week of July. ;)"
            jump q1_yes

    label q1_no:
        $ menu_flag = False
        show c_haist
        "Bat mo nga naman tatandaan di ba?"
        "Sagutin ko na rin para hindi naman ako mapahiya. \n07122018"
        hide c_haist
        jump date1_done


    label date1_done:
        hide neutral
        if menu_flag:
            show c_ha
            with flashbulb
            "Haneeeeppp! So, tinandaan mo rin? I'm... touched."
            hide c_ha
            show c_happy
            "Or hinulaan mo na lang ung dates sa 2nd week? haha!"
            hide c_happy
            screen busScreen
            with dissolve
            "Well, anyway, hindi naman yun mahalaga. What's important is now you know. ;P \nTechnically, that was 13 kase madaling araw na..."

            "...sa bus. di ba? \nI would love to remember as much details as I could kaso di ko matandaan ung name ng bus. LOL"
        else:
            "asdfasdfasdfasdfasdfasdf"
