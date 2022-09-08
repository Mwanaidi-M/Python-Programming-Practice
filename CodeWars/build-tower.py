def tower_builder(num_floors):
    """
    Build a pyramid-shaped tower given a positive integer number of floors.
    A tower block is represented with "*" character.
    For example, a tower with 3 floors looks like this:
    [
      "  *  ",
      " *** ",
      "*****"
    ]
    """
    # list to hold the stars
    tower_list = []

    # calculation to determine the width of each star generated
    space_width = (num_floors*2)-1

    # Because each row of the tower is formed of an odd number of stars, we need to loop
    # oddly, Thus we set the loop max to the 2 * num_floors with step of 2 to ensure
    # that we are looping through odds.
    # Then we use center function to give the tower the final Pyramidal shape.
    for num in range(1, 2*num_floors, 2):
        star = "*" * num
        tower_list.append(star.center(space_width))

    print(tower_list)


tower_builder(3)
