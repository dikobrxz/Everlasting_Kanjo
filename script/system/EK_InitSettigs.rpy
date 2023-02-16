
init:
  $ mods['EK_main_menu'] = u"{color=#000000}{size=48}{font=mods/Everlasting_Kanjo/fonts/18958.otf}БЕСКОНЕЧНОЕ КАНЖО."
  
  #НОВЫЕ ГЕРОИ
  $ go = Character (u'Тимофей', color="#DC143C", what_color="#E2C778") #Тимофей Хаккинен, гг, русский с финскими корнями.
  $ avt = Character (u'Автор', color="#5caaaf", what_color="#E2C778")
  $ uvg = Character (u'Голос', color="#00FF00", what_color="#E2C778")
  $ mes = Character (u'Сообщение', color="#E0FFFF", what_color="#E2C778")
  # ФОНЫ
  image logo1 = "mods/Everlasting_Kanjo/images/main_menu/logo1.png"
  image bg prolog_cruise = "mods/Everlasting_Kanjo/images/bg/bg_prolog_cruise.png"
  image bg prolog_corner_1 = "mods/Everlasting_Kanjo/images/bg/bg_prolog_corner1.png"
  image bg prolog_corner_2 = "mods/Everlasting_Kanjo/images/bg/bg_prolog_corner2.png"
  image bg prolog_corner_3 = "mods/Everlasting_Kanjo/images/bg/bg_prolog_corner3.png"
  image bg prolog_corner_4 = "mods/Everlasting_Kanjo/images/bg/bg_prolog_corner4.png"
  image bg prolog_corner_5 = "mods/Everlasting_Kanjo/images/bg/bg_prolog_corner5.png"
  image bg prolog_corner_5_hit = "mods/Everlasting_Kanjo/images/bg/bg_prolog_corner5_hit.png"
  image bg prolog_underwater = "mods/Everlasting_Kanjo/images/bg/prolog_underwater.jpg"
  image bg ext_entrance_civic_day = "mods/Everlasting_Kanjo/images/bg/ext_entrance_civic_day.png"
  image bg ext_entrance_inside_camp = "mods/Everlasting_Kanjo/images/bg/ext_entrance_inside_camp.png"
  image bg ext_ssdc_club_day = "mods/Everlasting_Kanjo/images/bg/ext_ssdc_club_day.png"
  image bg ext_house_of_mt_day_civic = "mods/Everlasting_Kanjo/images/bg/ext_house_of_mt_day_civic.png"
  image bg home_evening = "mods/Everlasting_Kanjo/images/bg/home_evening.jpg"
  image bg EK_kitchen = "mods/Everlasting_Kanjo/images/bg/EK_kitchen.png"
  image bg home_evening_laptop = "mods/Everlasting_Kanjo/images/bg/home_evening_laptop.png"
  #CГШКИ
  image cg volga_valit_bokom = "mods/Everlasting_Kanjo/images/сg/volga_valit_bokom.png"
  #ДНЕВНЫЕ ИНТРО
  image cg EK_prolog = "mods/Everlasting_Kanjo/images/day_intros/EK_prolog.png"
  image cg EK_day_1 = "mods/Everlasting_Kanjo/images/day_intros/EK_day_1.png"
  #МЕМЫ
  image cg EK_blatnoy_muzon = "mods/Everlasting_Kanjo/images/сg/EK_blatnoy_muzon.png"
  #СПРАЙТЫ
    #САЛОНЫ ТАЧЕК
        #HONDA CIVIC
  image civ civic_int_night_cruise = "mods/Everlasting_Kanjo/images/interiors/int_civic/civic_int_night_cruise.png"
  image civ civic_int_deep_night_cruise = "mods/Everlasting_Kanjo/images/interiors/int_civic/civic_int_deep_night_cruise.png"
  image civ civic_int_night_vtec_on = "mods/Everlasting_Kanjo/images/interiors/int_civic/civic_int_night_vtec_on.png"
  image civ civic_int_day_cruise = "mods/Everlasting_Kanjo/images/interiors/int_civic/civic_int_day_cruise.png"
  image civ civic_int_day_holost = "mods/Everlasting_Kanjo/images/interiors/int_civic/civic_int_day_holost.png"
  image civ civic_int_day_vtec_on = "mods/Everlasting_Kanjo/images/interiors/int_civic/civic_int_day_vtec_on.png"
    #ЗЕРКАЛО ЗАДНЕГО ВИДА
  image back sky_close = "mods/Everlasting_Kanjo/images/backside_mirror/sky_close.png"
  image back sky_far = "mods/Everlasting_Kanjo/images/backside_mirror/sky_far.png"
  #ТАЧКИ
  image sky sky_rush = "mods/Everlasting_Kanjo/images/car_sprites/Skyline_GTR32/sky_rush.png"
  #ЗВУКИ
  $ use_enter_sound = "mods/Everlasting_Kanjo/sounds/sfx/use_enter_sound.ogg"
  $ enter_waterhit = "mods/Everlasting_Kanjo/sounds/sfx/enter_waterhit.ogg"
  $ prolog_crash = "mods/Everlasting_Kanjo/sounds/sfx/prolog_crash.ogg"
  $ car_enter = "mods/Everlasting_Kanjo/sounds/sfx/car_enter.ogg"
  $ car_exit = "mods/Everlasting_Kanjo/sounds/sfx/car_exit.ogg"
  $ engine_start = "mods/Everlasting_Kanjo/sounds/sfx/engine_start.ogg"
  $ engine_stop = "mods/Everlasting_Kanjo/sounds/sfx/engine_stop.ogg"
  $ hood_close = "mods/Everlasting_Kanjo/sounds/sfx/hood_close.ogg"
  $ hood_open = "mods/Everlasting_Kanjo/sounds/sfx/hood_open.ogg"
  $ holost_b16a = "mods/Everlasting_Kanjo/sounds/sfx/holost_b16a.ogg"
  $ paper = "mods/Everlasting_Kanjo/sounds/sfx/paper.ogg"
  $ sfx_dudos_EK = "mods/Everlasting_Kanjo/sounds/sfx/sfx_dudos_EK.mp3"
  $ blyadskiy_chainik = "mods/Everlasting_Kanjo/sounds/sfx/blyadskiy_chainik.ogg"
  #ЭМБИЕНСЫ
  $ amb_underwater_EK = "mods/Everlasting_Kanjo/sounds/ambience/amb_underwater_EK.ogg"
  $ amb_car_cruise_EK = "mods/Everlasting_Kanjo/sounds/ambience/amb_car_cruise_EK.mp3"
  $ amb_holodos = "mods/Everlasting_Kanjo/sounds/ambience/amb_holodos.ogg"
  $ amb_car_vtec_on_EK = "mods/Everlasting_Kanjo/sounds/ambience/amb_car_vtec_on_EK.mp3"
  #МУЗЫКА
  $ DEVILISH_TRIO_MAIN = "mods/Everlasting_Kanjo/sounds/music/DEVILISH_TRIO_MAIN.mp3"
  $ dj_sacred_hit_da_gas = "mods/Everlasting_Kanjo/sounds/music/dj_sacred_hit_da_gas.mp3"
  $ hand_of_blood = "mods/Everlasting_Kanjo/sounds/music/hand_of_blood.mp3"
  $ sensy_affect_destiny = "mods/Everlasting_Kanjo/sounds/music/sensy_affect_destiny.mp3"
  $ bigson_talking = "mods/Everlasting_Kanjo/sounds/music/bigson_talking.mp3"
  $ krovostok_sniper = "mods/Everlasting_Kanjo/sounds/music/krovostok_sniper.mp3"
  $ dj_sacred_grim_house = "mods/Everlasting_Kanjo/sounds/music/dj_sacred_grim_house.mp3"
  #МУЗЫКАЛЬНЫЕ АЛЕРТЫ
  image bigson_talking = "mods/Everlasting_Kanjo/images/music_alerts/bigson_talking.png"
  image hand_of_blood = "mods/Everlasting_Kanjo/images/music_alerts/hand_of_blood.png"
  image krovostok_sniper = "mods/Everlasting_Kanjo/images/music_alerts/krovostok_sniper.png"
  image dj_sacred_grim_house = "mods/Everlasting_Kanjo/images/music_alerts/dj_sacred_grim_house.png"
  #ВИДЕО
  #image intro = Movie(play="mods/Everlasting_Kanjo/videos/intro.webm", mask="intro.webm", size=(1920,1080))
  image EK_main_menu = Movie(play="mods/Everlasting_Kanjo/videos/EK_main_menu.webm", mask="EK_main_menu.webm", size=(1920,1080))
  #ТРАНСФОРМЫ И ПРОЧАЯ СРАНЬ
  transform gas_gas_gas:
    anchor (0.0, 0.0) pos (0.0, 0.0)
    ease (0.1) pos (-5, -3)
    ease (0.1) pos (0, 0)
    ease (0.1) pos (5, -3)
    ease (0.1) pos (0, 0)
    ease (0.1) pos (-5, 3)
    ease (0.1) pos (0, 0)
    ease (0.1) pos (5, 3)
    repeat
  transform music_alert:
    xcenter -1.50 ycenter 0.50
    pause (5)
    linear 1.0 pos(0.50, 0.50)
    pause (10)
    linear 1.0 pos(-1.50, 0.50)
  transform car_enter:      
    xcenter 1.50 ycenter 0.50
    linear 0.5 pos(0.50, 0.50)
  transform car_exit:
    xcenter 0.50 ycenter 0.50
    linear 0.5 pos(1.50, 0.50)