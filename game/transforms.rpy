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

transform move_jump:
    # moving the image from right to left, left to right
    xalign 1.0 yalign 0.0
    pause 1.0
    xalign 0.0
    pause 1.0
    repeat

### for sample/side images (showing beside the main character)
# left
transform slightleft1:
        xysize (350, 300)
        xalign 0.2
        yalign 0.2
transform slightleft2:
        xysize (350, 300)
        xalign 0.2
        yalign 0.4
transform slightleft3:
        xysize (350, 300)
        xalign 0.2
        yalign 0.6
transform leftmost1:
        xysize (350, 300)
        xalign 0.0
        yalign 0.2
transform leftmost2:
        xysize (350, 300)
        xalign 0.0
        yalign 0.4
transform leftmost3:
        xysize (350, 300)
        xalign 0.0
        yalign 0.6
# right
transform slightright1:
        xysize (350, 300)
        xalign 0.8
        yalign 0.2
transform slightright2:
        xysize (350, 300)
        xalign 0.8
        yalign 0.4
transform slightright3:
        xysize (350, 300)
        xalign 0.8
        yalign 0.6
transform rightmost1:
        xysize (350, 300)
        xalign 1.0
        yalign 0.2
transform rightmost2:
        xysize (350, 300)
        xalign 1.0
        yalign 0.4
transform rightmost3:
        xysize (350, 300)
        xalign 1.0
        yalign 0.6
