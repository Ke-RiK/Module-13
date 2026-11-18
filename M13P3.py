# Kirill Kaminskyi M13P3.py 11/18/2026

players = {}

file = open("M12P4", "r")

count = 0

for line in file:
    line = line.strip()

    if line == "":
        continue

    if count % 2 == 0:
        last_name = line
    else:
        players[last_name] = float(line)

    count += 1

def display_players():
    print(f"{"Last name:":<20} {"Batting average:":<20}")

    for last_name, batting_average in players.items():
        print(f"{last_name:<20} {batting_average:<20,.3f}")

display_players()