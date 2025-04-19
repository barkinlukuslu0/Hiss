label splashscreen:
    scene black 
    with Pause(1)

    show text "{font=BerkshireSwash-Regular.ttf}{size=*1}From Uhm Ackshually\n\n\nBarkın Ali Lüküslü\n\nPeri Güven\n\nNazlı Şimal Kumcu{/size}{/font}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text "{font=BerkshireSwash-Regular.ttf}{size=*7}Hiss{/size}{/font}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return


label start:

    jump cutscenes

    return
