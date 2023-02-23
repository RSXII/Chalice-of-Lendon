label imagemap_demo:
    call screen myimagemap
    return

screen myimagemap:
    imagemap:
        #This is the image we want to display.
        ground "bg room1.jpg"
        #This is our hotspot marker on the image location and the action we want when they click it, here it jumps to the label "the_town_in_the_mountains"
        hotspot (0, 0, 200, 307) action Jump("the_town_in_the_mountains")