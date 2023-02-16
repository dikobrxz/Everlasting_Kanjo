init:
  $ mods['EK_main_menu'] = u"{color=#000000}{size=48}{font=mods/Everlasting_Kanjo/fonts/18958.otf}БЕСКОНЕЧНОЕ КАНЖО."
label EK_dlc:
    $ renpy.block_rollback()
    show bg black with dissolve2
    stop music fadeout 3
    $ renpy.pause (3)
    $ new_chapter(0, u"Бесконечное Канжо. DLC.")
    $ prolog_time()
    avt "Сорямба, но эта часть ещё не доступна. Заходи позже!"
    jump EK_main_menu11