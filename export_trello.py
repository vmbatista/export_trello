import datetime
import pandas as pd
from trello import TrelloClient

client = TrelloClient(
    api_key     = 'keykeykeykeykeykeykeykeykey',
    token       = 'tokentokentokentokentokentokentokentokentoken',
    )

df_open = []
boards = client.list_boards()
for board in boards:
    i_board = client.get_board(board.id)
    
    lists = i_board.all_lists()
    for list in lists:
        i_list = i_board.get_list(list.id)

        cards  = i_list.list_cards()
        for card in cards:
            df_open.append((board.name, list.name, card.name, card.card_created_date, card.desc))

df_closed = []
for board in boards:
    cards  = board.closed_cards()
    for card in cards:
        df_closed.append((board.name, list.name, card.name, card.card_created_date, card.desc))



df_trello_open = pd.DataFrame(df_open, columns = ['Board', 'List', 'Card Name', 'Created Date', 'Description'])
df_trello_closed = pd.DataFrame(df_closed, columns = ['Board', 'List', 'Card Name', 'Created Date', 'Description'])

now = datetime.datetime.now()
file_name = 'output_' + now.strftime('%Y%m%d_%H%M%S') + '.xlsx'

writer = pd.ExcelWriter(file_name, engine='xlsxwriter')

dfs = {'Open': df_trello_open, 'Closed': df_trello_closed}

for sheet, df in dfs.items():
    df.to_excel(writer, sheet_name = sheet)

writer.save()
