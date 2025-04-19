image glowing_bag:
    "glowing_bag.png"
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat 5

image beforeWomanHand:
    "WomanHand.png"
    align((0.5, 0.5))
    xysize(300,300)

label WomanHand:

    scene black with dissolve

    play sound "chopping_meat.mp3" volume 1.0

    pause(3)

    stop sound

    scene bg_womanroomwithouthand with dissolve:
        zoom 0.5

    show Idris Blood1 at right with dissolve

    show screen WomanHand_screen with dissolve

    show glowing_bag with dissolve:
        xysize(175,175)

    "You need to drag and drop this old woman's hand into your inventory."

    while not isHandTaken:
        "You need to drag and drop this old woman's hand into your inventory."
        show glowing_bag with dissolve:
            xysize(175,175)

    if isHandTaken == True:

        hide glowing_bag with dissolve

        hide Idris Blood1 with dissolve
        
        jump WomanHandContinue

    label WomanHandContinue:

        scene bg_villagenight with dissolve

        show Idris Blood1 at left with dissolve

        show Devil Idle at right with dissolve

        Devil "Çüüüüş. Even I wouldn't torture such an old lady! What are you thinking, you filthy peasant? Are you thirsty for death?"

        Idris "Oooh I was thinking about where the hell am I going to find a devil in this god-forsaken village." 
        Idris "Now there you are right in front of me."

        Devil "What do you want with me?"

        hide Idris Blood1 with dissolve

        show Devil Idle at center with moveinleft

    menu:
        "Break his leg.":
            hide screen WomanHand_screen with dissolve
            hide screen WomanFeet_screen with dissolve
            jump DevilLeg

        "Break his arm.":
            hide screen WomanHand_screen with dissolve
            hide screen WomanFeet_screen with dissolve
            jump DevilArm
            