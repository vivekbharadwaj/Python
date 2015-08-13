import numpy as np
#help(np.random.seed)

np.random.seed(8)
#demo 1 - this will generate different numbers each time the randint is called. but the seed works in such a way that this combination of 3 random numbers will be consistent each time the 
#  		  program is compiled		
#	np.random.seed(8)
#	print np.random.randint(1,10)
#	print np.random.randint(1,10)
#	print np.random.randint(1,10)

#demo 2 - this will generate the same random number each time the randint is called.
#	np.random.seed(8)
#	print np.random.randint(1,10)
#	np.random.seed(8)
#	print np.random.randint(1,10)
#	np.random.seed(8)
#	print np.random.randint(1,10)

#function: simulate_prizedoor 
#purpose : door number that contains the actual prize
#howto   : random number between 0 and 2
#args    : sample_size which contains the number of doors
#help(np.random.choice)
def simulate_prizedoor(sample_size):
	return np.random.choice(3,size=sample_size)
#print simulate_prizedoor(200)


#function: simulate_guess 
#purpose : door number that the candidate guessed
#howto   : random number between 0 and 2
#args    : sample_size which contains the number of doors. should be same as the prize doors simulation
#help(np.random.choice)
def simulate_guess(sample_size):
	return np.random.choice(3,size=sample_size)
#print simulate_guess(200)

#function: simulate_goat_reveal 
#purpose : simulates the door number that the event show host opens AFTER the guess has been made
#howto   : picks door number that is neither the guess nor the prize 
#args    : actual arrays for guesses and prize doors
#help(np.random.choice)
#def simulate_goat_reveal(contestant_guesses,prize_doors):
#	goat_reveal = np.random.choice(3,size=len(contestant_guesses))
#	while np.any( goat_reveal == contestant_guesses ) or np.any( goat_reveal == prize_doors ):
#		goat_reveal = np.random.choice(3,size=len(contestant_guesses))
#	return goat_reveal
#print simulate_goat_reveal(np.array([1,1,2]),np.array([2,1,0]))
#this works but is extremely inefficient. modifying the code to randomise only the elements that are same, rather than the whole array.
def simulate_goat_reveal(contestant_guesses,prize_doors):
	goat_reveal = np.random.choice(3,size=len(contestant_guesses))
	while True:
		bad = ( goat_reveal == contestant_guesses ) | ( goat_reveal == prize_doors )
		if not bad.any():
			return goat_reveal
		goat_reveal[bad] = np.random.choice(3,size=bad.sum())
#got to admit - pretty smart solution in the online code	


#function: simulate_switch_guess 
#purpose : simulates the door number that the contestant switched to after the show host revealed one goat door
#howto   : picks door number that is neither the guess nor the revealed door 
#args    : actual arrays for guesses and revealed doors
#def simulate_switch_guess(contestant_guesses,goat_reveal):
#	switch_guess = np.random.choice(3,size=len(contestant_guesses))
#	while np.any( switch_guess == contestant_guesses ) or np.any( goat_reveal == switch_guess ):
#		switch_guess = np.random.choice(3,size=len(contestant_guesses))
#	return switch_guess
def simulate_switch_guess(contestant_guesses,goat_reveal):
	switch_guess = np.random.choice(3,size=len(contestant_guesses))
	while True:
		bad = ( switch_guess == contestant_guesses ) | ( goat_reveal == switch_guess )
		if not bad.any():
			return switch_guess
		switch_guess[bad] = np.random.choice(3,size=bad.sum())


#function: win_percentage_stay 
#purpose : % of times contestant would have won if she had stayed
def win_percentage_stay(guesses,prizedoors):
	return float(sum(guesses==prizedoors))/len(guesses)*100

#function: win_percentage_switch 
#purpose : % of times contestant would have won if she had switched
def win_percentage_switch(switch,prizedoors):
	return float(sum(switch==prizedoors))/len(switch)*100


#RUN THE PGM
prizes  = simulate_prizedoor(10000)
print "prize  is ", prizes
guesses = simulate_guess(10000)
print "guess  is ", guesses

print
print "if contestant stays, percentage is ", win_percentage_stay(guesses,prizes)
print

# quick performance until here - 4.4 seconds even for 2 million sample sizes

goat_revealed = simulate_goat_reveal(prizes,guesses)
print "reveal is ", goat_revealed

switches  = simulate_switch_guess(guesses,goat_revealed)
print "switch made" ,switches
print


print "if contestant switches, percentage is ", win_percentage_switch(switches,prizes)


#Test runs
#1. sample size : 10
#   results     : if contestant stays 20%, if switches 80%
#   time taken  : 0.7s

#2. sample size : 12
#   results     : if contestant stays 16.67%, if switches 83.33%
#   time taken  : 4.2s

#3. sample size : 20
#   results     : if contestant stays 40%, if switches **** (don't know. taking too long to execute)
#   time taken  : too long to wait.

#no good. 

#modified code to remove the performance constraint. how? randomising only those elements of the array that are same. so much fewer iterations.
#4. sample size : 200
#   results     : if contestant stays 35%, if switches 65%
#   time taken  : 0.3s

#5. sample size : 10000
#   results     : if contestant stays 33.83%, if switches 66.17%
#   time taken  : 0.3s

