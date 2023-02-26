
#These should be set at top level.
define gomaStats = CharacterStats("Goma", 5)
define ensukeStats = CharacterStats("Ensuke", 5)
define ushiStats = CharacterStats("Ushi", 5)
define chikaStats = CharacterStats("Chika", 5)

define e = Character("Eileen")


label start:

    scene bg room1

    show eileen happy

    jump questions

label questions:
    
    show screen stattrack
    "Goma's values should be at 5 -> [gomaStats.amount]"
    #We can add values depending on the choices made.
    $ gomaStats.add(5)
    show screen stattrack
    "Goma's values should be at 10 -> [gomaStats.amount]"
    #We can subtract values depending on the choices made.
    $ gomaStats.subtract(5)
    show screen stattrack
    "Goma's values should be at 5 -> [gomaStats.amount]"


label test:
    
    


    menu:
        "Do you want to go to the image map?"
        "Yes":
            jump the_town_in_the_mountains
        "No":
            jump tracker
    return
