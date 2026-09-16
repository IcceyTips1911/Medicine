name = input("Please tell me your name: ")


if name == "Landon":
	print("Greetings sir")
	mood = int(input("How are you feeling today? Please rate your mood a scale from 1-10: "))
	print(f"Mood scale rating: {mood}")

	if 1 <= mood <=5:
		print("What is wrong today?")
		print("Please choose a number to use:")
		reason = int(input("1.Long Day \n2.Work was not all that \n3.Missing my lady \n4.Not motivated \nYour Answer: "))
		if reason == 1:
			print("Would you like to have some soft sounds,  music, podcast, or Bible Sermon to help calm you down?")
			ld_choice = int(input("1.Soft Sounds \n2.General Music \n3.Tech Podcast \n4.Bible Sermon \nYour Answer: "))
			if ld_choice == 1:
				print("Is there a specific type of sound you would like for me to play sir?")
				yon = input("Yes or No \nYour Answer: ")
				if yon == "yes":
					sounds = int(input("1.Rain \n2.White Noise \n3.Black Noise \nYour Answer: "))
					if sounds == 1:
						print("Now playing Rain sounds")
					elif sounds == 2:
						print("Now playing White Noise")
					elif sounds == 3:
						print("Now playing Black Noise")
				else:
					print("Now shuffling to find the right sounds for you.")
			elif ld_choice == 2:
				print("Please select the type of music:")
				music = int(input("1.Country \n2.Gospel \n3.Rap \n4.R&B \n5.Old School \n6.Shuffle Play \nYour Answer: "))
				if music == 1:
					print("Now shuffling Country Music.")
				elif music == 2:
					print("Now shuffling Gospel Music.")
				elif music == 3:
					print("Now shuffling Rap Music.")
				elif music == 4:
					print("Now shuffling R&B Music.")
				elif music == 5:
					print("Now shuffling Old School Music.")
				else:
					print("Now shuffling music at random.")
	elif  6 <= mood <= 10:
		print("That's good.")
		print("Please choose something you would like for me to help you with:")
		topics = input("1.Sports \n2.Weather \nYour answer: ")
else:
	print("Not valid")
