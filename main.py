import pandas as pd
import os

path_pages = './src/Pages.xlsx'
path_cards = './src/Cards.csv'
path_kingdoms = './src/Kingdoms.csv'
columns = ['Extension', 'Name']

# Generate List of card names with Pages.xlsx
def create_card_storage():


    df = pd.read_excel(path_pages)

    new_df = pd.DataFrame(columns=columns)
    condition = df.iloc[:, 0].str.startswith('cards', na=False)

    for index, row in df[condition].iterrows():
        # Extract specific parts of the row (e.g., columns 1 and 2)
        selected_data = row[1:3].values  # Adjust based on your desired columns
        clean_data = [selected_data[0].split('_')[0], selected_data[1]]
        # Append data to the new DataFrame
        new_df.loc[len(new_df)] = clean_data

    new_df.to_csv(path_cards, index=False)

expansions = ['baseset', 'baseset2', 'intrigue', 'intrigue2', 'seaside', 'seaside2', 'alchemy', 'prosperity',
              'prosperity2', 'cornucopia', 'hinterlands', 'hinterlands2', 'darkages', 'guilds', 'adventures', 'empires',
              'nocturne', 'renaissance', 'menagerie', 'allies', 'plunder', 'risingsun', 'guildscornucopia',
              'guildscornucopia2']

current_expansions = ['baseset', 'baseset2', 'intrigue', 'intrigue2', 'seaside', 'seaside2', 'alchemy', 'prosperity',
              'prosperity2', 'cornucopia', 'hinterlands', 'hinterlands2', 'darkages', 'guilds', 'adventures', 'empires',
              'nocturne', 'renaissance', 'menagerie', 'risingsun']

fixed_cards = []


def generate_kingdom(expansion, fixed_cards):
    generate_number = 10 - len(fixed_cards)
    cards = pd.read_csv(path_cards)
    cards = cards[cards['Extension'].isin(expansion)]
    random_cards = cards.sample(n=generate_number, random_state=42)['Name'].tolist()

    kingdom = fixed_cards + random_cards
    return kingdom

players = ["David", "Julian", "Jojo"]


def start_game():
    pass


def new_round():
    """
    This method takes care of initiating a new round. It lets you generate multiple kingdoms and choose one,
    then it asks for the names of the players and stores the value in a csv.
    """
    global players
    choice = input(f"Starting a new round of Dominion... \nThe current selected players are: {players}\nPress Enter to start a new "
          "round or enter 'c' to change the players.")

    if choice == "c":
        players = []
        while True:
            player_name = input("Enter a player name or press enter when all players are named.")
            if player_name == "":
                break
            else:
                players.append(player_name)
        if len(players) == 0:
            raise ValueError("There are no selected players.")
        if len(players) > 6:
            raise ValueError("There are too many players.")
        new_round()

    if choice != "":
        print(f"Unknown command {choice}")
        new_round()

    players.sort()
    kingdom_cards = []

    while True:
        print(f"Generating Kingdoms with expansions:\n{current_expansions}\nand fixed cards:\n{fixed_cards}")
        kingdom_cards = generate_kingdom(current_expansions, fixed_cards)

        choice = input(f"Generated kingdom:\n{kingdom_cards}\n press enter to play the kingdom or 'r' to generate a different "
                       f"kingdom.")
        if choice == "":
            break

        if choice != "r":
            raise ValueError(f"Unknown command {choice}")

    write_new_kingdom(players, kingdom_cards)


def write_new_kingdom(players, kingdom_cards):
    kingdom_columns = ["Player1", "Player2", "Player3", "Player4", "Player5", "Player6",
                       "Card1", "Card2", "Card3", "Card4", "Card5", "Card6", "Card7", "Card8", "Card9", "Card10",
                       "1. Place", "2. Place", "3. Place", "4. Place", "5. Place", "6. Place",
                       "Player1VP", "Player2VP", "Player3VP", "Player4VP", "Player5VP", "Player6VP"]

    if not os.path.exists(path_kingdoms):
        df = pd.DataFrame(columns=kingdom_columns)
        df.to_csv(path_kingdoms, index=False)

    cur_columns = kingdom_columns[:len(players)] + kingdom_columns[6:16]
    print(cur_columns)
    cur_row = players + kingdom_cards
    print(cur_row)
    new_kingdom_line = pd.DataFrame([cur_row], columns=cur_columns)
    print(f"New Kingdom Line: {new_kingdom_line}")
    kingdoms_csv = pd.read_csv(path_kingdoms)
    kingdoms_csv = pd.concat([kingdoms_csv, new_kingdom_line], ignore_index=True)
    kingdoms_csv.to_csv(path_kingdoms, index=False, header=kingdom_columns)


def add_scores():
    pass

#TODO Promos!

def main():
    create_card_storage()
    new_round()

if __name__ == "__main__":
    main()
