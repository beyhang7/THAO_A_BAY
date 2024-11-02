import pandas as pd

# Tải dữ liệu từ tệp CSV
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


results = []

# Tính toán cho toàn giải
for attribute in attributes:
    median_value = data[attribute].median()
    mean_value = data[attribute].mean()
    std_value = data[attribute].std()
    results.append({'Đội': 'all', 'Trung vị': median_value, 'Giá trị trung bình ': mean_value, 'Độ lệch chuẩn': std_value})

# Tính toán cho từng đội
teams = data['Team'].unique()
for team in teams:
    team_data = data[data['Team'] == team]
    for attribute in attributes:
        median_value = team_data[attribute].median()
        mean_value = team_data[attribute].mean()
        std_value = team_data[attribute].std()
        results.append({'Đội': team, 'Trung vị': median_value, 'Giá trị trung bình': mean_value, 'Độ lệch chuẩn': std_value})


results_df = pd.DataFrame(results)

results_df.to_csv('results2.csv', index=False)