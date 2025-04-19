image glowing_bag:
    "glowing_bag.png"
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat 5

label TakeOil:
    
    scene bg_idrisfriendhouse_without_oil_with_blood with dissolve

    show screen Oil_screen with dissolve

    "You need to drag and drop this oil into your inventory."

    while not isOilTaken:
        "You need to drag and drop this honey to your inventory."
        show glowing_bag with dissolve:
            xysize(175,175)

    if isOilTaken == True:
        hide glowing_bag with dissolve
        hide screen Oil_screen with dissolve
        stop music fadeout 5.0
        jump AfterTakingStuffs
