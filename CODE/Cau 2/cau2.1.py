import pandas as pd

# Đọc dữ liệu từ tệp CSV 
data = pd.read_csv('results.csv')

# Danh sách các chỉ số 
attributes = [
    'Team', 'Name',
    'matches_played', 'starts', 'minutes', 'non_Penalty_Goals', 'Penalty Goals', 'Assists', 
    'Yellow_Cards', 'Red_Cards', 'xG_x', 'npxG_x', 'xAG_x', 'PrgC', 'PrgP_x', 'PrgR_x', 
    'Gls_x', 'Ast_x', 'G+A', 'G-PK', 'G+A-PK', 'xG_per_90', 'xAG_per_90', 'xG+xAG', 
    'npxG_per_90', 'npxG+xAG_per_90', 'Gls_y', 'Sh_x', 'SoT', 'SoT%', 'Sh/90', 'SoT/90', 
    'G/Sh', 'G/SoT', 'Dist', 'FK', 'PK', 'PKatt_y', 'xG_y', 'npxG_y', 'npxG/Sh', 
    'G-xG', 'np:G-xG', 'Total Cmp', 'Total Att', 'Total Cmp%', 'TotDist_x', 'PrgDist', 
    'Short Cmp', 'Short Att', 'Short Cmp%', 'Medium Cmp', 'Medium Att', 'Medium Cmp%', 
    'Long Cmp', 'Long Att', 'Long Cmp%', 'Ast_y', 'xAG_y', 'xA', 'A-xAG', 'Key Passes', 
    'Final Third Passes', 'PPA', 'CrsPA', 'PrgP_y', 'Pass Types.Live', 'Pass Types.Dead', 
    'Pass Types.FK', 'Pass Types.TB', 'Pass Types.Sw', 'Pass Types.Crs', 'Pass Types.TI', 
    'Pass Types.CK', 'Corner Kicks.In', 'Corner Kicks.Out', 'Corner Kicks.Str', 
    'Outcomes.Cmp', 'Outcomes.Off', 'Outcomes.Blocks', 'SCA', 'SCA90', 'PassLive', 
    'PassDead', 'TO', 'Sh_y', 'Fld_x', 'Def', 'GCA', 'GCA90', 'GCA PassLive', 
    'GCA PassDead', 'GCA TO', 'GCA Sh', 'GCA Fld', 'GCA Def', 'Touches', 'Def Pen', 
    'Def 3rd_y', 'Mid 3rd_y', 'Att 3rd_y', 'Att Pen', 'Live', 'Att', 'Succ', 'Succ%', 
    'Tkld', 'Tkld% ', 'Carries', 'TotDist_y', 'ProDist', 'ProgC', '1/3', 'CPA', 'Mis', 
    'Dis', 'Rec', 'PrgR_y', 'Starts', 'Mn/Start', 'Compl', 'Subs', 'Mn/Sub', 'unSub', 
    'PPM', 'onG', 'onGA', 'onxG', 'onxGA', 'Fls', 'Fld_y', 'Off', 'Crs', 'OG', 
    'Recov', 'Aerial Won', 'Aerial Lost', 'Aerial Won%'
]

# Chuyển đổi các cột số liệu sang kiểu số
for attribute in attributes[2:]:
    if attribute in data.columns:
        data[attribute] = pd.to_numeric(data[attribute], errors='coerce')


result = {   
    'Chỉ số': [],
    'Top 3 cầu thủ có điểm cao nhất': [],
    'Tên đội của cầu thủ có điểm cao nhất': [],
    'Điểm cao nhất': [],
    'Top 3 cầu thủ có điểm thấp nhất': [],
    'Tên đội của cầu thủ có điểm thấp nhất': [],
    'Điểm thấp nhất': []
}

# Tìm top 3 cầu thủ có điểm cao nhất và thấp nhất cho mỗi chỉ số
for attribute in attributes:
    if attribute in data.columns and pd.api.types.is_numeric_dtype(data[attribute]):
        # Lấy 3 cầu thủ có điểm cao nhất
        top_3 = data.nlargest(3, attribute)[['Name', 'Team', attribute]].dropna()
        
        # Lấy 3 cầu thủ có điểm thấp nhất
        bottom_3 = data.nsmallest(3, attribute)[['Name', 'Team', attribute]].dropna()

        result['Chỉ số'].append(attribute)
        result['Top 3 cầu thủ có điểm cao nhất'].append(", ".join(top_3['Name']))
        result['Tên đội của cầu thủ có điểm cao nhất'].append(", ".join(top_3['Team']))
        result['Điểm cao nhất'].append(", ".join(top_3[attribute].astype(str)))
        result['Top 3 cầu thủ có điểm thấp nhất'].append(", ".join(bottom_3['Name']))
        result['Tên đội của cầu thủ có điểm thấp nhất'].append(", ".join(bottom_3['Team']))
        result['Điểm thấp nhất'].append(", ".join(bottom_3[attribute].astype(str)))


result_df = pd.DataFrame(result)

print(result_df)