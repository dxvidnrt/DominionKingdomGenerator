import pandas as pd
import random
from numpy.distutils.extension import Extension

path_pages = './src/Pages.xlsx'
path_cards = './src/Cards.csv'
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
    print(kingdom)
    return kingdom





#Promos!

def main():
    create_card_storage()
    generate_kingdom(current_expansions, [])

if __name__ == "__main__":
    main()
