import pywhatkit as kit
def music_(my_mood):
	if my_mood in mood_dict.keys():
		kit.playonyt(mood_dict[my_mood])
	else:
		print("This type of mood we dont't have!")
my_mood = input(" ")
mood_dict = {"happy":"The Ketchup Song (ZIGGY Remix)","sad":"You Are The Reason","normal":"Callin U",
			"drunk":"Sirts Patrasta ft. Hak & Super Sako",
			"crazy":"Bad Habits","excited":"Shape of My Heart"}
music_(my_mood)