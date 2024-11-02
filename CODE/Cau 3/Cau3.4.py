import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Đọc dữ liệu từ file CSV
data = pd.read_csv('results.csv')

# Chọn các chỉ số cần so sánh
attributes = [
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

# Kiểm tra xem các thuộc tính có trong dữ liệu không
attributes = [attr for attr in attributes if attr in data.columns]

# Tạo thư mục để lưu hình ảnh
luu = 'radarChartPlot'
os.makedirs(luu, exist_ok=True)

# So sánh tất cả các cầu thủ
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        player1 = data.iloc[i]
        player2 = data.iloc[j]

        # Số lượng các chỉ số
        num_vars = len(attributes)

        # Thiết lập góc cho mỗi chỉ số
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

        # Đưa điểm đầu tiên về để khép kín hình
        values1 = player1[attributes].values.flatten().tolist()
        values1 += values1[:1]
        values2 = player2[attributes].values.flatten().tolist()
        values2 += values2[:1]
        angles += angles[:1]

        # Tạo hình radar
        fig, ax = plt.subplots(figsize=(12, 6), subplot_kw=dict(polar=True))
        ax.fill(angles, values1, color='red', alpha=0.3)  
        ax.fill(angles, values2, color='blue', alpha=0.3) 
        
        # Đường viền cho cầu thủ
        ax.plot(angles, values1, color='red', linewidth=1, label=player1["Name"])  
        ax.plot(angles, values2, color='blue', linewidth=1, label=player2["Name"]) 

        # Trục và chỉ số
        ax.set_yticklabels([], fontsize=5)  
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(attributes, fontsize=5)  
        
        # Tiêu đề
        plt.title(f'{player1["Name"]} và {player2["Name"]}', size=20, color='black', weight='bold')  
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1)) 

        # Lưu biểu đồ vào thư mục với đường dẫn đầy đủ
        file_name = f'{player1["Name"].replace("/", "_")}_vs_{player2["Name"].replace("/", "_")}.png'
        plt.savefig(os.path.join(luu, file_name))
        plt.close()

print("Tất cả hình ảnh đã được lưu vào thư mục:", luu)
