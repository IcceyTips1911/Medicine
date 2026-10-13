def test_mental_2():
    return

mood = int(input("How are you feeling today? \nPlease rate on a scale of 1-10: "))
print(f"Your current mood is a {mood}")

while True:
    if 1 <= mood <= 5:
        print("What is wrong today?")
        print("Please enter the number that aligns with the topic: ")
        reason = int(input("1.Long Day \nYour Answer: "))
        if reason == 1:
            print("Would you like some music to help you relax?")
            relax_music_choice = int(input("1.Yes \n2.No \nYour Answer: "))
            if relax_music_choice == 1:
                print("What type of music would you like to listen to?")
                music_genre = int(input("1.Gospel \n2.Country \n3.Rap \n4.R&B \n5.Old Sckool \n6.Shuffle Play \nYour Answer: "))
                if music_genre == 1:
                    print("Now playing gospel music...")
                    from music import gospel
                    gospel()
                elif music_genre == 2:
                    print("Now playing country music...")
                    from music import country
                    country()
                elif music_genre == 3:
                    print("Now playing rap music...")
                    from music import rap
                    rap()
                elif music_genre == 4:
                    print("Now playing R&B music...")
                    from music import rythm_blues
                    rythm_blues()
                elif music_genre == 5:
                    print("Now playing old school music...")
                    from music import old_sckool
                    old_sckool()
                elif music_genre == 6:
                    print("Now playing today's hits...")
                    from music import top_hits
                    top_hits()
            elif relax_music_choice == 2:
                print("Let's what else would suit you. \nPlease choose one of the following that will help you in relaxing:")
                relax_choice = int(input("1.Soft Sounds \n2.Podcast \n3.Bible Sermon \nYour Answer: "))
                if relax_choice == 1:
                    print("What type of sound would you care to relax to?")
                    soft_sound_choice = int(input("1.White Noise \n2.Rain Sounds \n3.Ocean Waves \n4.Wind brustling against trees \n5.Camp Fire \nYour Answer: "))
                    if soft_sound_choice == 1:
                        print("Now playing some white noise...")
                        from soft_sounds import white_noise
                        white_noise()
                    elif soft_sound_choice == 2:
                        print("Now playing some rain noise...")
                        from soft_sounds import rain_noise
                        rain_noise()
                    elif soft_sound_choice == 3:
                        print("Now playing some ocean sounds...")
                        from soft_sounds import ocean_waves
                        ocean_waves()
                    elif soft_sound_choice == 4:
                        print("Now playing some wind brustling against tree branches...")
                        from soft_sounds import wind_trees
                        wind_trees()
                    elif soft_sound_choice == 5:
                        print("Now playing some camp fire sounds...")
                        from soft_sounds import camp_fire
                        camp_fire()
                break
        elif reason == 2:
            print("Something")
        break
    else:
        print("That is not a proper option")