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
    ""
    show unready at slightright with dissolve
    "ehem"
    hide unready
    show surprised at right with dissolve
    "Huy! (Charaught lang.)"
    hide surprised with dissolve
    "Teka okay na ba itsura ko?"
    show closeup with dissolve
    ""
    hide closeup with dissolve
    show smile
    "Orayt, lezgow!"
    hide smile with fade

    # change bg here
    show neutral2
    "Kumusta naman? It's been like what? 4 or 5 years since you received the initial version of this thingy?"
    "I'd love to call this DigiLet, btw."
    hide neutral2 with dissolve
    show c_ehe
    "Understandable, right?"
    hide c_ehe with dissolve
    show neutral2
    "I got a little tired of (but being stuck with) webdev stuffs and while checking-out what other options are available, I came across something that made me remember the very reason why I started programming."
    hide neutral2 with dissolve
    show smile
    ""
    hide smile
    show stare with dissolve
    "You."
    "I wanted to give you a digital, interactive love letter back then."
    hide stare
    show c_ehe with dissolve
    "And then...eto na yun!"
    "Hinanap ko ung sinend ko sa'yo noon (the very first one), and then inilagay ko dito."
    "Keep in mind na inalis ko na ung instructions on how to use it kasi heto na nga, may GUI na. Kaya mas maikli na siguro itey..."
    hide c_ehe with fade
    show neutral2
    "Today is April 19, 2022. (This also serves as a remembrance for me kaya may date.)"
    "I was able to create this part 1 Visual Novel (VN) in 2 days! ;)"
    hide neutral2
    show c_happy
    "Orayt! Let's go down the memory lane na."
    jump intro







    # This ends the game.

    return
