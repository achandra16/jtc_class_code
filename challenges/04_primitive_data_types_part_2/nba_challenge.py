print("Challenge 2.1:")
jamal_murray_3pts_made = 46
fred_vanvleet_3pts_made = 43
james_harden_3pts_made = 37

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots")
print()

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
jamal_murray_3pts_shot_attempts = 93
fred_vanvleet_3pts_shot_attempts = 110
james_harden_3pts_shot_attempts = 109

print()

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3 point shots and Z 3 point shot attempts."
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3 point shots and made {jamal_murray_3pts_shot_attempts} attempts")
print(f"In the 2020 NBA playoffs, Fred VanVleet made {fred_vanvleet_3pts_made} 3 point shots and made {fred_vanvleet_3pts_shot_attempts} attempts")
print(f"In the 2020 NBA playoffs, James Harden made {james_harden_3pts_made} 3 point shots and made {james_harden_3pts_shot_attempts} attempts")
print()

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
jamal_murray_3pts_percentage = jamal_murray_3pts_made/jamal_murray_3pts_shot_attempts
fred_vanvleet_3pts_percentage = fred_vanvleet_3pts_made/fred_vanvleet_3pts_shot_attempts
james_harden_3pts_percentage = james_harden_3pts_made/james_harden_3pts_shot_attempts
print(jamal_murray_3pts_percentage)
print(fred_vanvleet_3pts_percentage)
print(james_harden_3pts_percentage)
print()


print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
one_sentence_per_line = "The Lakers went all in this offseason and swung a deal for former Pelicans forward Anthony Davis. \nThey sent a package of Brandon Ingram, Lonzo Ball, Josh Hart, and 3 first-round picks to New Orleans to land Davis. \nThose three have made good developments with the Pelicans, especially Brandon Ingram. \nBut, the deal is still a huge win for the Lakers as Lebron, Davis, and company have put together an incredible season. \nLos Angeles has ridden James and Davis, along with a supporting cast built around them, to the second-best record in the NBA. \nThe Lakers ended the season atop the Western Conference with a record of 49-14. \nThey were narrowly behind the Bucks for the best record in the league. \nDavis proved to the final piece necessary for the Lakers to rebound from missing the playoffís last year. \nLos Angeles was a dominant club on both sides of the ball and are in a position to have another successful year next season."
print(one_sentence_per_line)

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
print(one_sentence_per_line.upper())

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
# TODO: print out the variable in an f-string to convey your opinion on the lakers
lakers_are_best = False
print(f"The Lakers are the best team: {lakers_are_best}")

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out. 
# TODO: Convert your `lakers_are best` variable to a float, and print it out
print(int(lakers_are_best))
print(float(lakers_are_best))

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
print(str(jamal_murray_3pts_percentage))
print(str(fred_vanvleet_3pts_percentage))
print(str(james_harden_3pts_percentage))

print(int(jamal_murray_3pts_percentage))
print(int(fred_vanvleet_3pts_percentage))
print(int(james_harden_3pts_percentage))