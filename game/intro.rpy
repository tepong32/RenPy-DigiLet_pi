# script containing the actual messages from the original, python-only-based digilet

label intro:
    scene bg afgbmts
    with pixellate

    show c_ehe at left with dissolve
    "(O di ba, nakakuha ako ng picture ng Trade?)"
    hide c_ehe with dissolve
    show neutral2 at left with dissolve
    "A few years back...(uhh..err..?) MANY years ago, at AFGBMTS, I met you."
    ""
    "The end."
    hide neutral2
    scene black with pixellate
    show c_ehe at left with dissolve
    "Hehe! Joke lang. So ayon...yeah I met you...along with everyone else."
    hide c_ehe
    show closeup at left
    "It's not unknown naman na hindi tayo close / masyadong close nung high school.The Pinky I know was someone so...nag-aaral lang. Ganern. Kasama sa top students? Tropa ni Angelique at Llabora? haha"
    hide closeup
    show c_ehe at left
    "Bakit ko ba ipinasok to e wala naman akong maisip. Tinatype ko lang on the spot."
    "Well, let's jump forward to where things got a little crazy na lang...para may masabi ako."
    hide c_ehe
    show c_happy at left
    "SI BRUUUU! :) We became close when 'we' (me and her) became close. Yun yata yun di ba? (Textmates kami.)"
    hide c_happy with dissolve
    show bru at right with dissolve
    pause 1.0
    show closeup at left with dissolve
    hide bru with dissolve
    ""
    "I cannot really recall na how things started. Basta alam ko na you were fond / very fond of me back then. NYAHAHAHAHA!"
    hide closeup
    show c_haist with dissolve
    "Kokontra?"
    hide c_haist with dissolve
    show c_happy with dissolve
    "Good!"
    hide c_happy with dissolve
    show unready at left with dissolve
    "Errr...Wala talaga akong masabi sa part na 'to."
    "I'll skip the little details. The fun part is the latter part, anyways."
    "Lemme just ask you this here na lang:"
    ""
    hide unready

    show poker at left
    "Okay na ba tayo?"
    "Have you forgiven me already?"
    pause 1.0
    hide poker
    show c_poker at left with dissolve
    "Sincerely? As in wala nang nakatanim jan na galit for me?"
    hide c_poker
    show poker at left with move
    menu:
        "Oo... siguro?":
            hide poker
            jump choice1_yes

        "Hindi...hindi rin ako sigurado.":
            hide poker
            jump choice1_no

    label choice1_yes:
        $ menu_flag = True
        hide c_poker
        show c_happy
        "Well, sana nga. (Trust issues!?) Pero thank you. ;)"
        jump choice1_done
        hide c_happy

    label choice1_no:
        $ menu_flag = False
        hide c_poker
        show c_haist
        "Sabi ko na nga ba e. Anywaaaay..."
        hide c_haist
        jump choice1_done
        hide c_haist

#### This block can be used somewhere else...I guess
# a block in relation to menu_flag on choice1 labels
    # label choice1_done:
    #     if menu_flag:
    #         e "For example, I remember that you plan to use menus in your game."
    #     else:
    #         e "For example, I remember that you're planning to make a kinetic novel, without menus."

    label choice1_done:
        show c_poker
        ""
        "Naisip mo bang mabuti bago ka sumagot?"
        "If anything, di ko sigurado if I apologized enough or even properly for what I did way back...10 years ago?"
        "This is where I'll do so."
        hide c_poker
        # change scene here
        scene bg sorry with slowdissolve
        show unready at right with dissolve
        "Pinky, I really want to apologize, make-up for what I did back then and uh...maybe repay you for the kindness you've shown me throughout all the years I've known you."
        "I know this is will not be enough. This will never be enough. Kahit nasabi mo na sakin na okay na...na wala ka namang itinanim na galit sakin (samin), it really did bother me to this day..."
        hide unready
        show ehe at slightright with dissolve
        "Wait...hindi naman to this day, actually. HAHA but the whole time we were not talking to each other; the whole time we're not as close as how we used to be before THAT happened."
        hide ehe
        show poker with dissolve
        "I know apologies will never be enough. \nSabi nga ni Dao Ming Zi: \"Para saan pa ang pulis?\" di ba?"
        hide poker
        show ehe
        "I would like to get into more details pero I think I better not. Baka maalala mo pang lalo e...mahirap na. Saka Birthday present mo to tapos ganern?"
        hide ehe
        show neutral
        "But even so, I would like to re-iterate that I really wanted to, and I am apologizing sincerely for what I did."
        "That was the whole point of this intro, actually."
        hide neutral
        show ha
        "(Intro pa lang 'to!?)"
        hide ha
        show smile
        "Yep. I made the last part before this kase so andun na almost everything. Look forward to it na lang."
        "And always bear the caution of hitting Enter carefully, ha? Mahaba-haba na to para ulitin pag may nalagpasan ka. ;) "
        hide smile

        jump theRemake
