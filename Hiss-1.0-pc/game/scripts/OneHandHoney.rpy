image glowing_bag:
    "glowing_bag.png"
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat 5

label TakeHoney:
    
    scene bg_idrisfriendhouse_without_honey_with_blood with dissolve

    show screen honey_screen with dissolve

    "You need to drag and drop this honey into your inventory."

    while not isHoneyTaken:
        "You need to drag and drop this honey to your inventory."
        show glowing_bag with dissolve:
            xysize(175,175)

    if isHoneyTaken == True:
        hide glowing_bag with dissolve
        hide screen honey_screen with dissolve
        stop music fadeout 5.0
        jump AfterTakingStuffs
