init:
    $ timer_range = 0
    $ timer_jump = 0

label GiveSahmeranToKing:
    Idris "It looks like the only sensible thing for me to do is kill you and take your head to the king."

    show Sahmeran Angry at right

    Sahmeran "You believe you possess the strength or the audacity to do so? I shall claim your head first, you fool."

    stop music fadeout 5.0

    show screen countdown

    play music "heart.mp3" volume 10

    $ time = 5
    $ timer_range = 5
    $ timer_jump = 'nochoice_slow1'

    menu:
        "You think so?":
            hide screen countdown
            jump YouThinkSo

        "You wouldn't do that.":
            hide screen countdown
            jump YouWouldntDoThat

    label nochoice_slow1:
        jump YouWouldntDoThat