def test_mental_2():
    return

mood = int(input("How are oyu feeling today? \nPlease rate on a scale of 1-10: "))
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
                music_genre = int(input("1.Gospel \n2.Country \n3.Rap \n4.R&B \n5.Old Sckool \n6.Shuffle Play"))
                if music_genre == 1:
                    print("Now playing gospel music")
                    from play import gospel
                    gospel()
                elif music_genre == 2:
                    print("Now playing country music")
                    from play import country
                    country()
                elif music_genre == 3:
                    print("Now playing rap music")
                    from play import rap
                    rap()
                elif music_genre == 4:
                    print("Now playing R&B music")
                    from play import rythm_blues
                    rythm_blues()
                elif music_genre == 5:
                    print("Now playing old school music")
                    from play import old_sckool
                    old_sckool()
                elif music_genre == 6:
                    print("Now playing today's hits")
                    from play import top_hits
                    top_hits()
            elif relax_music_choice == 2:
                print("Let's what else would suit you.")
                break
        break
    else:
        print("That is not a proper option")