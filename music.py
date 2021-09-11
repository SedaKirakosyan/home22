import pywhatkit as kit
def music_(my_mood):
	if my_mood in mood_list:
		for i in range(len(mood_list)-1):
			if my_mood == mood_list[i]:
				kit.playonyt(music_list[i])
	else:
		print("This type of mood we dont't have!")
my_mood = input(" ")
mood_list = ["happy","sad","normal","drunk","crazy","excited"]
music_list = [ "The Ketchup Song (ZIGGY Remix)",
                "You Are The Reason",
				"Callin U",
				"Sirts Patrasta ft. Hak & Super Sako",
				"Bad Habits",
				"Shape of My Heart"]
music_(my_mood)