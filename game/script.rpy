# The script of the game goes in this file.
# teppy's Note: This script only contains the intro.
# Other parts of the letter (originals) will be on other chopped-scripts.rpy files


# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define s = Character('You', color="#c8ffc8")
# define m = Character('Me', color="#c8c8ff")

# Sprite positioning and Transitiondefinitions

transform slightleft:
    xalign 0.25
    yalign 1.0
transform slightright:
    xalign 0.75
    yalign 1.0

# Default transition options:
# fade, dissolve, pixellate, vpunch/hpunch (use with 'play audio "punch.opus"'),
# move (brings the character to the right then back to the center)
    # show eileen happy at right
    # with move
    # show eileen happy at center
    # with move

define slowdissolve = Dissolve(1.0)
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff') # flashbang!



################################################ The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg pathway1
    play music "audio/farm-birds.ogg" fadeout 1.0 fadein 1.0
    ""
    show unready at slightright with dissolve
    "ehem"
    hide unready
    show surprised at right with dissolve
    "Huy! (Charaught. Gulat epek lang.)"
    hide surprised with dissolve
    "Teka okay na ba itsura ko?"
    show closeup with dissolve
    ""
    hide closeup with dissolve
    show smile
    "Pogi ng avatar ko no? Hehe"
    hide smile with fade

    # change bg here
    show neutral2
    "So, kumusta naman? It's been like what? 4 or 5 years since you received the initial version of this DigiLet thingy?"
    show neutral2
    "I got a little tired of (but also being stuck with) webdev stuffs and while checking-out what other options are available, I came across something that made me remember the very reason why I started programming."
    hide neutral2 with dissolve
    show c_happy with dissolve
    pause 1.0
    hide c_happy with dissolve
    show stare with dissolve
    pause 1.0
    "You."
    "I wanted to give you a digital, interactive love letter back then."
    hide stare
    show c_ehe
    "And then...eto na yun!"
    "Hinanap ko ung sinend ko sa'yo noon (the very first one), and then inilagay ko dito."
    hide c_ehe
    show closeup
    "Keep in mind na inalis ko na ung instructions on how to use it kasi heto na nga, may GUI na. Kaya mas maikli na siguro itey..."
    hide closeup
    pause 1.0
    stop music fadeout 1.0
    scene black
    show c_happy at right with fade
    "Orayt! Tama na ang intro. \nLet's go down the memory lane na."
    jump intro







    # This ends the game.

    return
