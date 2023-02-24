screen track():
    hbox:
        text "Goma "
        align (0.99, 0)
        spacing 10
        vbox:
            bar:
                xsize 200
                value gomaStats.amount
                range 20
    hbox:
        text "Ensuke "
        align (0.7, 0)
        spacing 10
        vbox:
            bar:
                xsize 200
                value ensukeStats.amount
                range 20
    hbox:
        text "Ushi "
        align (0.4, 0)
        spacing 10
        vbox:
            bar:
                xsize 200
                value ushiStats.amount
                range 20
    hbox:
        text "Chika "
        align (0.09, 0)
        spacing 10
        vbox:
            bar:
                xsize 200
                value chikaStats.amount
                range 20
                
        
    
label tracker:
    show screen track
    jump questions