init:
  $ mods['EK_main_menu'] = u"{color=#000000}{size=48}{font=mods/Everlasting_Kanjo/fonts/18958.otf}БЕСКОНЕЧНОЕ КАНЖО."
label EK_main_menu:
    $ renpy.movie_cutscene("mods/Everlasting_Kanjo/videos/intro.webm")
    $ renpy.block_rollback()
    scene EK_main_menu with dissolve2
    play music dj_sacred_hit_da_gas fadein 3
    $ renpy.pause (3.5, hard=True)
    show logo1
    call screen EK_buttons with dissolve
    screen EK_buttons:
        tag test
        imagemap:
                idle "mods/Everlasting_Kanjo/images/main_menu/EK_buttons.png"
                hover "mods/Everlasting_Kanjo/images/main_menu/EK_buttons_hover.png"
            
                hotspot(200,490,340,75) action (Hide("EK_main_menu"), Jump ("EK_part_pick")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))
                hotspot(190,660,625,75) action (Hide("EK_main_menu"), Jump ("EK_menu_gamedev")) hovered (Play("sound","mods/Everlasting_Kanjo/sfx/sfx/use_enter_sound.mp3"))
                hotspot(200,840,300,75) action (Hide("EK_main_menu"), Jump ("EK_menu_exit")) hovered (Play("sound","mods/Everlasting_Kanjo/sfx/sfx/use_enter_sound.mp3"))
    label EK_menu_gamedev:
        play sound use_enter_sound
        $ renpy.block_rollback()
        call screen EK_buttons_gamedev with dissolve
        screen EK_buttons_gamedev:
          tag test
          imagemap:
              idle"mods/Everlasting_Kanjo/images/main_menu/EK_buttons_gamedev.png"
              hover"mods/Everlasting_Kanjo/images/main_menu/EK_buttons_gamedev_hover.png"

              hotspot(200,480,560,100) action (Hide("EK_menu_gamedev"), OpenURL ("https://vk.com/dikobrxz_inc")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))
              hotspot(195,655,410,90) action (Hide("EK_menu_gamedev"), OpenURL ("https://steamcommunity.com/id/dikobrxz/")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))
              hotspot(200,840,290,75) action (Hide("EK_menu_gamedev"), Jump ("EK_main_menu1")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))
    label EK_menu_exit:
        play sound use_enter_sound
        $ renpy.block_rollback()
        scene bg black with dissolve2
        stop music fadeout 3
        $ renpy.pause (3, hard=True)
        return
    label EK_main_menu1:
    play sound use_enter_sound
    $ renpy.block_rollback()
    call screen EK_buttons with dissolve
    screen EK_buttons:
        tag test
        imagemap:
                idle "mods/Everlasting_Kanjo/images/main_menu/EK_buttons.png"
                hover "mods/Everlasting_Kanjo/images/main_menu/EK_buttons_hover.png"
            
                hotspot(200,490,340,75) action (Hide("EK_main_menu"), Jump ("EK_part_pick")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))
                hotspot(190,660,625,75) action (Hide("EK_main_menu"), Jump ("EK_menu_gamedev")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))
                hotspot(200,840,300,75) action (Hide("EK_main_menu"), Jump ("EK_menu_exit")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))
    label EK_main_menu11:
    scene EK_main_menu with dissolve2
    show logo1
    $ renpy.block_rollback()
    call screen EK_buttons with dissolve
    screen EK_buttons:
        tag test
        imagemap:
                idle "mods/Everlasting_Kanjo/images/main_menu/EK_buttons.png"
                hover "mods/Everlasting_Kanjo/images/main_menu/EK_buttons_hover.png"
            
                hotspot(200,490,340,75) action (Hide("EK_main_menu"), Jump ("EK_part_pick")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))
                hotspot(190,660,625,75) action (Hide("EK_main_menu"), Jump ("EK_menu_gamedev")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))
                hotspot(200,840,300,75) action (Hide("EK_main_menu"), Jump ("EK_menu_exit")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))
    label EK_part_pick:
    show bg black with dissolve2
    $ renpy.block_rollback ()
    call screen EK_buttons_part with dissolve
    screen EK_buttons_part:
        tag test
        imagemap:
                idle "mods/Everlasting_Kanjo/images/main_menu/EK_buttons_part.png"
                hover "mods/Everlasting_Kanjo/images/main_menu/EK_buttons_part_hover.png"
            
                hotspot(0,0,960,1080) action (Hide("EK_main_menu"), Jump ("EK_prolog")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))
                hotspot(960,0,960,1080) action (Hide("EK_main_menu"), Jump ("EK_dlc")) hovered (Play("sound","mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.mp3"))