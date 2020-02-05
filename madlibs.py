def main():
	# write your code here
	print("Mad lips the game where lips get mad -you will see why")
	print (" ")
	print ("lets start")
	time = input ("enter a time:(e.g. :12pm) ")
	item = input ("enter an item:(e.g. : pen) ")
	name = input ("enter your name (e.g.: reallly?!) ")
	scream = input ("how will your enemy scream sound like ? ")
	action = input ("enter a continuous action:(e.g.:flying) ")

	name = name.title()
	scream = scream.upper()

	print ("\n once upon a time, " + str(time) +" to be exact.")
	print ("I woke up from a realy weird dream")
	print ("I saw " + str(name) + " fighting with a " + str(item) +" a realy HUGE "+ str(item.upper()))
	print ("It was a scary fight.And just when i thought " + str(name) + " was getting defeted,")
	print ("a realy shiny cat came with the biggest sward i have ever seen in my life. ")
	print ("And when the " + str(item) + " saw the sward it ran away screaming : " + str(scream))
	print ("then the cat said : excuse me i have some " + str(action) +" to do")
	print ("then my alarm clock woke me up and i never saw the shiny cat again :(")






if __name__ == '__main__':
	main()
