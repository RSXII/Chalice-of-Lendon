
#These should be set at top level.
define gomaStats = CharacterStats("Goma", 5)
define ensukeStats = CharacterStats("Ensuke", 5)
define ushiStats = CharacterStats("Ushi", 5)
define chikaStats = CharacterStats("Chika", 5)

define e = Character("Eileen")


label start:

    scene bg room1


    show eileen happy

    "This value should be 5 -> [gomaStats.amount]"
    #We can add values depending on the choices made.
    $ gomaStats.add(5)
    "This value should be 10 -> [gomaStats.amount]"
    #We can subtract values depending on the choices made.
    $ gomaStats.subtract(5)
    "This value should be 5 -> [gomaStats.amount]"


    menu:
        "Do you want to go to the image map?"
        "Yes":
            jump imagemap_demo
        "No":
            jump the_town_in_the_mountains
    return
