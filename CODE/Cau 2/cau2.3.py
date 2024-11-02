import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Đọc dữ liệu từ tệp CSV
data = pd.read_csv('results.csv')

# Danh sách các chỉ số
attributes = [
    'matches_played', 'starts', 'minutes', 'non_Penalty_Goals', 
    'Penalty Goals', 'Assists', 'Yellow_Cards', 'Red_Cards',
    'xG_x', 'npxG_x', 'xAG_x', 'PrgC', 'PrgP_x', 'PrgR_x', 
    'Gls_x', 'Ast_x', 'G+A', 'G-PK', 'G+A-PK', 'xG_per_90', 
    'xAG_per_90', 'xG+xAG', 'npxG_per_90', 'npxG+xAG_per_90',
    'Gls_y', 'Sh_x', 'SoT', 'SoT%', 'Sh/90', 'SoT/90', 
    'G/Sh', 'G/SoT', 'Dist', 'FK', 'PK', 'PKatt_y', 
    'xG_y', 'npxG_y', 'npxG/Sh', 'G-xG', 'np:G-xG', 
    'Total Cmp', 'Total Att', 'Total Cmp%', 'TotDist_x', 
    'PrgDist', 'Short Cmp', 'Short Att', 'Short Cmp%', 
    'Medium Cmp', 'Medium Att', 'Medium Cmp%', 'Long Cmp', 
    'Long Att', 'Long Cmp%', 'Ast_y', 'xAG_y', 'xA', 
    'A-xAG', 'Key Passes', 'Final Third Passes', 'PPA', 
    'CrsPA', 'PrgP_y', 'Pass Types.Live', 'Pass Types.Dead', 
    'Pass Types.FK', 'Pass Types.TB', 'Pass Types.Sw', 
    'Pass Types.Crs', 'Pass Types.TI', 'Pass Types.CK', 
    'Corner Kicks.In', 'Corner Kicks.Out', 'Corner Kicks.Str', 
    'Outcomes.Cmp', 'Outcomes.Off', 'Outcomes.Blocks', 
    'SCA', 'SCA90', 'PassLive', 'PassDead', 'TO', 
    'Sh_y', 'Fld_x', 'Def', 'GCA', 'GCA90', 
    'GCA PassLive', 'GCA PassDead', 'GCA TO', 'GCA Sh', 
    'GCA Fld', 'GCA Def', 'Touches', 'Def Pen', 
    'Def 3rd_y', 'Mid 3rd_y', 'Att 3rd_y', 'Att Pen', 
    'Live', 'Att', 'Succ', 'Succ%', 'Tkld', 'Tkld% ', 
    'Carries', 'TotDist_y', 'ProDist', 'ProgC', 
    '1/3', 'CPA', 'Mis', 'Dis', 'Rec', 'PrgR_y', 
    'Starts', 'Mn/Start', 'Compl', 'Subs', 'Mn/Sub', 
    'unSub', 'PPM', 'onG', 'onGA', 'onxG', 
    'onxGA', 'Fls', 'Fld_y', 'Off', 'Crs', 
    'OG', 'Recov', 'Aerial Won', 'Aerial Lost', 
    'Aerial Won%'
]

#### Toàn giải
output_folder_all = 'Toàn giải'
os.makedirs(output_folder_all, exist_ok=True)

for attribute in attributes:
    plt.figure(figsize=(10, 5))
    sns.histplot(data[attribute], bins=40, kde=True, color='red')
    plt.title(f'Bảng phân bố của chỉ số {attribute} trong toàn giải đấu')
    plt.xlabel(attribute)
    plt.ylabel('Tần suất')
    plt.grid()

    safe_attribute = attribute.replace("/", "_").replace(" ", "_")
    plt.savefig(f'{output_folder_all}/{safe_attribute}_league_histogram.png')
    plt.close()  


#### Từng đội
output_folder_teams = 'Từng đội'
os.makedirs(output_folder_teams, exist_ok=True)

teams = data['Team'].unique()

for team in teams:
    team_folder = f'{output_folder_teams}/{team}'
    os.makedirs(team_folder, exist_ok=True)

    team_data = data[data['Team'] == team]
    for attribute in attributes:
        plt.figure(figsize=(10, 5))
        sns.histplot(team_data[attribute], bins=40, kde=True, color='orange')
        plt.title(f'Bảng phân bố chỉ số {attribute} của đội tuyển {team}')
        plt.xlabel(attribute)
        plt.ylabel('Tần suất')
        plt.grid()

        safe_attribute = attribute.replace("/", "_").replace(" ", "_")
        plt.savefig(f'{team_folder}/{safe_attribute}_{team}_histogram.png')
        plt.close()  
