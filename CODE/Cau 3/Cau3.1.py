import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Bước 1: Đọc dữ liệu từ file CSV
merged_dfx = pd.read_csv('results.csv')

# Bước 2: Lựa chọn các cột mà bạn muốn sử dụng để phân nhóm
features = [
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
    'Live', 'Att', 'Succ', 'Succ%', 'Tkld', 
    'Tkld% ', 'Carries', 'TotDist_y', 'ProDist', 
    'ProgC', '1/3', 'CPA', 'Mis', 'Dis', 
    'Rec', 'PrgR_y', 'Starts', 'Mn/Start', 'Compl', 
    'Subs', 'Mn/Sub', 'unSub', 'PPM', 'onG', 
    'onGA', 'onxG', 'onxGA', 'Fls', 'Fld_y', 
    'Off', 'Crs', 'OG', 'Recov', 'Aerial Won', 
    'Aerial Lost', 'Aerial Won%'
]

# Chọn các cột dữ liệu
X = merged_dfx[features]

# Chuyển đổi các giá trị không hợp lệ thành NaN và sau đó loại bỏ
X = X.apply(pd.to_numeric, errors='coerce')
X = X.fillna(0)  

#Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  #


#Tìm số lượng cluster tối ưu
inertia = []  
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled) 
    inertia.append(kmeans.inertia_)

# Vẽ đồ thị để xác định số lượng cluster
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Phương pháp Elbow để xác định k tối ưu')
plt.xlabel('Số lượng cluster')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()

# Áp dụng K-means với số lượng cluster đã chọn
optimal_k = 3  
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
merged_dfx['Cluster'] = kmeans.fit_predict(X_scaled)  

#Gán tên cho từng nhóm
cluster_names = {
    0: "Nhóm A - Cầu thủ tấn công",
    1: "Nhóm B - Cầu thủ phòng ngự",
    2: "Nhóm C - Cầu thủ Toàn Diện"
}

# Gán tên nhóm vào cột mới trong DataFrame
merged_dfx['Cluster_Name'] = merged_dfx['Cluster'].map(cluster_names)

# In ra tên cầu thủ theo từng nhóm
for cluster in range(optimal_k):
    print(f"\n{cluster_names[cluster]}:")
    print(merged_dfx[merged_dfx['Cluster'] == cluster][['Name'] + features])