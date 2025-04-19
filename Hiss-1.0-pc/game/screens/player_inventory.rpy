default slot_count = 4
default player_inventory = []

init python:
    def remove_items_from_inventory(inventory, num_items):
        del inventory[:num_items]

screen player_inventory:
    modal True

    imagebutton:
        align(0.0, 0.0)
        auto "/images/bag %s.png"
        action [Hide(), ToggleScreen('player_hud')]
        at transform:
            xysize(175,175)

    frame:
        background "#030003d3"
        xysize(1920, 1080)
        align(0.5, 0.5)

        vpgrid cols 2:
            spacing 30
            align(0.5, 0.5)

            for slot in range(slot_count):
                frame:
                    maximum(200, 200)
                    if slot < len(player_inventory):
                        add Image("/images/" + player_inventory[slot] + ".png") align((0.5, 0.5)) xysize(200,200)
                        $ inv_item_name = player_inventory[slot].replace("_", ' ')
                    else:
                        pass
