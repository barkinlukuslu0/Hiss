default honey = ['honey']
default DevilArm = ['DevilArm']
default DevilLeg = ['DevilLeg']
default WomanFeet = ['WomanFeet']
default WomanHand = ['WomanHand']
default Oil = ['Oil']
default SahmeranItems = ['Sahmeran_Body_1', 'Sahmeran_Body_2', 'Sahmeran_Body_3']

default isHoneyTaken = False
default isOilTaken = False
default isHandTaken = False
default isFeetTaken = False
default isLegTaken = False
default isArmTaken = False
default isBody1Taken = False
default isBody2Taken = False
default isBody3Taken = False

init:
    $ config.mouse = {
        'default':[('gui/cursor/mouse_idle.png', 0, 0)],
        'pressed_default': [('gui/cursor/mouse_drag.png', 0, 0)],
        "button": [('gui/cursor/mouse_hover.png', 0, 0)],
        'pressed_button': [('gui/cursor/mouse_drag.png', 0, 0)],
    }


init python:
    def add_item(player_inv, dragged_item):
        global isHoneyTaken
        global isOilTaken
        global isHandTaken
        global isFeetTaken
        global isLegTaken
        global isArmTaken
        global isBody1Taken
        global isBody2Taken
        global isBody3Taken
        
        item_name = dragged_item[0].drag_name
        print(f"{item_name} was added to your inventory.")
        player_inventory.append(item_name)

        if item_name == "honey":
            isHoneyTaken = True
            print(isHoneyTaken)
        
        elif item_name == "Oil":
            isOilTaken = True
            print(isOilTaken)
        
        elif item_name == "DevilLeg":
            isLegTaken = True
            print(isLegTaken)
        
        elif item_name == "DevilArm":
            isArmTaken = True
            print(isArmTaken)
        
        elif item_name == "WomanFeet":
            isFeetTaken = True
            print(isFeetTaken)
        
        elif item_name == "WomanHand":
            isHandTaken = True
            print(isHandTaken)

        elif item_name == "Sahmeran_Body_1":
            isBody1Taken = True
            print(isBody1Taken)

        elif item_name == "Sahmeran_Body_2":
            isBody2Taken = True
            print(isBody2Taken)

        elif item_name == "Sahmeran_Body_3":
            isBody3Taken = True
            print(isBody3Taken)
        
        dragged_item[0].set_child(Null())

screen honey_screen():

    draggroup:
        drag:
            align(0.0, 0.0)
            drag_raise False
            draggable False
            droppable True
            dropped add_item

            imagebutton:
                align(0.0, 0.0)
                auto "/images/bag %s.png"
                action [ToggleScreen("player_hud"), Show("player_inventory")]
                at transform:
                    xysize(175,175)

        for item in honey:
            drag:
                align((0.5, 0.5))
                drag_name item
                drag_raise True
                add f"/images/honey.png" xysize (300, 300)

screen Oil_screen():

    draggroup:
        drag:
            align(0.0, 0.0)
            drag_raise False
            draggable False
            droppable True
            dropped add_item

            imagebutton:
                align(0.0, 0.0)
                auto "/images/bag %s.png"
                action [ToggleScreen("player_hud"), Show("player_inventory")]
                at transform:
                    xysize(175,175)

        for item in Oil:
            drag:
                align((0.5, 0.5))
                drag_name item
                drag_raise True
                add f"/images/Oil.png":
                    xysize (300, 300)
                    zoom 1.5

screen WomanFeet_screen():

    draggroup:
        drag:
            align(0.0, 0.0)
            drag_raise False
            draggable False
            droppable True
            dropped add_item

            imagebutton:
                align(0.0, 0.0)
                auto "/images/bag %s.png"
                action [ToggleScreen("player_hud"), Show("player_inventory")]
                at transform:
                    xysize(175,175)

        for item in WomanFeet:
            drag:
                align((0.5, 0.5))
                drag_name item
                drag_raise True
                add f"/images/WomanFeet.png" xysize (300, 300)

screen WomanHand_screen():

    draggroup:
        drag:
            align(0.0, 0.0)
            drag_raise False
            draggable False
            droppable True
            dropped add_item

            imagebutton:
                align(0.0, 0.0)
                auto "/images/bag %s.png"
                action [ToggleScreen("player_hud"), Show("player_inventory")]
                at transform:
                    xysize(175,175)

        for item in WomanHand:
            drag:
                align((0.5, 0.5))
                drag_name item
                drag_raise True
                add f"/images/WomanHand.png" xysize (300, 300)

screen DevilLeg_screen():

    draggroup:
        drag:
            align(0.0, 0.0)
            drag_raise False
            draggable False
            droppable True
            dropped add_item

            imagebutton:
                align(0.0, 0.0)
                auto "/images/bag %s.png"
                action [ToggleScreen("player_hud"), Show("player_inventory")]
                at transform:
                    xysize(175,175)

        for item in DevilLeg:
            drag:
                xalign 1.0
                yalign 0.5
                drag_name item
                drag_raise True
                add f"/images/DevilLeg.png":
                    xysize (300, 300)
                    zoom 1.5

screen DevilArm_screen():

    draggroup:
        drag:
            align(0.0, 0.0)
            drag_raise False
            draggable False
            droppable True
            dropped add_item

            imagebutton:
                align(0.0, 0.0)
                auto "/images/bag %s.png"
                action [ToggleScreen("player_hud"), Show("player_inventory")]
                at transform:
                    xysize(175,175)

        for item in DevilArm:
            drag:
                xalign 1.0
                yalign 0.5
                drag_name item
                drag_raise True
                add f"/images/DevilArm.png":
                    xysize (300, 300)
                    zoom 1.5

screen SahmeranBody_screen():

    draggroup:
        drag:
            align(0.0, 0.0)
            drag_raise False
            draggable False
            droppable True
            dropped add_item

            imagebutton:
                align(0.0, 0.0)
                auto "/images/bag %s.png"
                action [ToggleScreen("player_hud"), Show("player_inventory")]
                at transform:
                    xysize(175, 175)

        $ item_positions = [(0.05, 0.5), (0.5, 0.5), (0.95, 0.5)]
        
        for i, item in enumerate(SahmeranItems):
            drag:
                align item_positions[i]
                drag_name item
                drag_raise True
                add f"/images/{item}.png":
                    xysize (300, 300)
                    zoom 1.5