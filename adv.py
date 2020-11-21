from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# backwards path...
returnPath = []
revDirections = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# create a set for the rooms that were already visited...
visited = set()

# if the length of the room_graph -1 is less than the length of the visited -1 continue..
while len(room_graph) - 1 > len(visited) - 1:
    # set what upcoming move as a variable
    # default it to 0 or None to init the start of the variable...
    # This will be helpful when writting my if else statement...
    upcoming_move = 0

    # for loop player to continue after exiting the current room...
    for continuing in player.current_room.get_exits():
        # checking...
        if player.current_room.get_room_in_direction(continuing) not in visited:
            # re-update the variable upcoming_move to continuing...
            upcoming_move = continuing

    # checks if the variable upcoming_move has initiated...
    if upcoming_move is not 0:
        # add the upcoming move to the traversal path at the end...
        traversal_path.append(upcoming_move)

        # more appending done...
        returnPath.append(revDirections[upcoming_move])

        # make the player travel with the upcoming moves...
        player.travel(upcoming_move)

        # adds the visited places the player has gone through...
        visited.add(player.current_room)

    # else if no more moves left...
    else:

        # pop of the returnPath and set it to the upcoming move...
        upcoming_move = returnPath.pop()

        # append what was pop from the return path to the traversal_path...
        traversal_path.append(upcoming_move)

        # make the player travel with the upcoming moves...
        player.travel(upcoming_move)

# Uncomment to see where the player visited while the while loop occurs...
#     print(player.current_room)

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
