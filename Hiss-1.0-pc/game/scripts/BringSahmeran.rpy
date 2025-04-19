init:
    $ timer_range = 0
    $ timer_jump = 0

label BringSahmeran:

    show Vizier Idle at right

    Vizier "That's what I thought."

    stop music fadeout 5.0

    hide screen player_hud with dissolve

    hide Idris Idle with dissolve

    hide Vizier Idle with dissolve

    play music "sahmeran_cave.mp3" fadein 2.0

    scene bg_sahmerancave with dissolve

    show screen player_hud with dissolve

    show Idris Idle at left with dissolve

    show Sahmeran Idle at right with dissolve

    Sahmeran "What brings you back here again, you pitiful mortal? I thought you had chosen to go home."

    Idris "Vallahi I couldn't keep myself away from you. There's a magical aura around it as if it's drawing me in."

    Sahmeran "You're aware of who I am, aren't you? Or shall I refresh your memory once more?!"

    Idris "Yeahh. I'm just messin' with ya."

    Sahmeran "So, what brings thee back to my den?"

    Idris "I came here for what I intended in the first place. Making money. You think you're something, don't you?"

    Sahmeran "What nonsense do you think you're spouting? How do you plan to profit by returning here?"

    Idris "I've come to take your head."

    show Sahmeran Angry at right

    Sahmeran "You believe you possess the strength or the audacity to do so? I shall claim your head first, you fool."

    stop music fadeout 5.0

    show screen countdown

    play music "heart.mp3" volume 10

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'nochoice_slow'

    menu:
        "You think so?":
            hide screen countdown
            jump YouThinkSo

        "You wouldn't do that.":
            hide screen countdown
            jump YouWouldntDoThat

    label nochoice_slow:
        jump YouWouldntDoThat