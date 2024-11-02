import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Danh sách các URL cho các đội tuyển
urls = [
    'https://fbref.com/en/squads/822bd0ba/2023-2024/Liverpool-Stats',
    'https://fbref.com/en/squads/b8fd03ef/2023-2024/Manchester-City-Stats',
    'https://fbref.com/en/squads/18bb7c10/2023-2024/Arsenal-Stats',
    'https://fbref.com/en/squads/8602292d/2023-2024/Aston-Villa-Stats',
    'https://fbref.com/en/squads/4ba7cbea/2023-2024/Bournemouth-Stats',
    'https://fbref.com/en/squads/cd051869/2023-2024/Brentford-Stats',
    'https://fbref.com/en/squads/d07537b9/2023-2024/Brighton-and-Hove-Albion-Stats',
    'https://fbref.com/en/squads/943e8050/2023-2024/Burnley-Stats',
    'https://fbref.com/en/squads/cff3d9bb/2023-2024/Chelsea-Stats',
    'https://fbref.com/en/squads/47c64c55/2023-2024/Crystal-Palace-Stats',
    'https://fbref.com/en/squads/d3fd31cc/2023-2024/Everton-Stats',
    'https://fbref.com/en/squads/fd962109/2023-2024/Fulham-Stats',
    'https://fbref.com/en/squads/e297cd13/2023-2024/Luton-Town-Stats',
    'https://fbref.com/en/squads/19538871/2023-2024/Manchester-United-Stats',
    'https://fbref.com/en/squads/b2b47a98/2023-2024/Newcastle-United-Stats',
    'https://fbref.com/en/squads/e4a775cb/2023-2024/Nottingham-Forest-Stats',
    'https://fbref.com/en/squads/1df6b87e/2023-2024/Sheffield-United-Stats',
    'https://fbref.com/en/squads/361ca564/2023-2024/Tottenham-Hotspur-Stats',
    'https://fbref.com/en/squads/7c21e445/2023-2024/West-Ham-United-Stats',
    'https://fbref.com/en/squads/8cec06e1/2023-2024/Wolverhampton-Wanderers-Stats'

]

Tong_hop_team = []

for url in urls:
    # Gửi yêu cầu tới URL
    r = requests.get(url)

    soup = bs(r.text, 'html.parser')
    tables = soup.find_all('table')

    if tables: 

    #### Bảng cầu thủ
        bang = []

        # LẤY TÊN ĐỘI BÓNG
        team = tables[0].find('caption').find('span').text.strip()
        tmp = team.replace(":", "").split(" ")
        doi = ""
        for i in range(1,len(tmp)-2):
            doi += tmp[i]+" "

        rows0 = tables[0].find('tbody').find_all('tr')

        for im in rows0: 
            name = im.find('th').text.strip()
            cols = im.find_all('td')
            Play = []
            #### Nation
            Play.append(cols[0].text.strip())
            #### Team 
            Play.append(doi.strip())

            #### Position, Age, Playing time
            for i in range(1, 6):
                time = cols[i].text.strip()
                Play.append(time)

            # Performance
            non_Penalty = cols[10].text.strip()
            Play.append(non_Penalty)
            Penalty_Goalsy = cols[11].text.strip()
            Play.append(non_Penalty)
            Assists = cols[8].text.strip()
            Play.append(Assists)
            Yellow_Cards = cols[13].text.strip()
            Play.append(Yellow_Cards)
            Red_Cards  = cols[14].text.strip()
            Play.append(Red_Cards)

            # Expected
            for i in range(15, 18):
                tmp = cols[i].text.strip()
                Play.append(tmp)

            # Progression: PrgC, PrgP, PrgR
            Pro = []
            for i in range(19, 32):
                tmp = cols[i].text.strip()
                Pro.append(tmp)

            # Bảng tổng hợp thông tin
            bang.append([name] + Play + Pro)
        
        df1 = pd.DataFrame(bang, columns=['Name', 'Nation', 'Team', 'Position', 'Age', 'matches_played', 'starts', 'minutes', 
                                        'non_Penalty_Goals', 'Penalty Goals', 'Assists', 'Yellow_Cards', 'Red_Cards', 
                                        'xG', 'npxG', 'xAG', 'PrgC', 'PrgP', 'PrgR', 
                                        'Gls', 'Ast', 'G+A', 'G-PK', 'G+A-PK', 'xG_per_90', 'xAG_per_90', 
                                        'xG+xAG', 'npxG_per_90', 'npxG+xAG_per_90'])

    #### Bảng Goalkeeping
        bang2 = []
        rows1 = tables[2].find('tbody').find_all('tr')
        for im in rows1: 
            name2 = im.find('th').text.strip()
            cols1 = im.find_all('td')

            Goal = []
            for i in range(7, 17):
                tmp = cols1[i].text.strip()
                Goal.append(tmp)

            pen = []
            for i in range(17, 22):
                tmp = cols1[i].text.strip()
                pen.append(tmp)

            bang2.append([name2] + Goal + pen)

        
        df2 = pd.DataFrame(bang2, columns=['Name', 'GA', 'GA90', 'SoTA', 'Saves', 'Save%', 'W', 'D', 'L', 'CS', 'CS%', 
                                        'PKatt', 'PKA', 'PKsv', 'PKm', 'Save%_again'])

    
    
    #### Bảng Shooting
        bang3 = []
        rows3 = tables[4].find('tbody').find_all('tr')
        for im in rows3: 
            name3 = im.find('th').text.strip()
            cols3 = im.find_all('td')

            Sta = []
            for i in range(4, 16):
                tmp = cols3[i].text.strip()
                Sta.append(tmp)

            Exp = []
            for i in range(16, 21):
                tmp = cols3[i].text.strip()
                Exp.append(tmp)

            bang3.append([name3] + Sta + Exp)

        df3 = pd.DataFrame(bang3, columns=['Name', 'Gls', 'Sh', 'SoT', 'SoT%', 'Sh/90', 'SoT/90', 'G/Sh', 'G/SoT', 
                                        'Dist', 'FK', 'PK', 'PKatt', 'xG', 'npxG', 'npxG/Sh', 'G-xG', 'np:G-xG'])

    
    #### Bảng Passing
        bang4 = []
        rows4 = tables[5].find('tbody').find_all('tr')
        for im in rows4:
            name4 = im.find('th').text.strip()
            cols4 = im.find_all('td')

            bang_phu = []
            # Total: Cmp, Att, Cmp%, TotDist, PrgDist 
            for i in range(4, 9):
                tmp  = cols4[i].text.strip()
                bang_phu.append(tmp)
                
            # Short: Cmp, Att, Cmp% 
            for i in range(9,12):
                tmp  = cols4[i].text.strip()
                bang_phu.append(tmp)

            # Medium: Cmp, Att, Cmp% 
            for i in range(12,15):
                tmp  = cols4[i].text.strip()
                bang_phu.append(tmp)

            # Long: Cmp, Att, Cmp% 
            for i in range(15,18):
                tmp  = cols4[i].text.strip()
                bang_phu.append(tmp)
                

            # Expected: Ast, xAG, xA, A-xAG, KP, 1/3, PPA, CrsPA, PrgP 
            for i in range(18, 27):
                tmp  = cols4[i].text.strip()
                bang_phu.append(tmp)

            
            bang4.append([name4] + bang_phu)
            
        df4 = pd.DataFrame(bang4, columns =['Name', 'Total Cmp', 'Total Att', 'Total Cmp%', 'TotDist', 'PrgDist',
                                            'Short Cmp', 'Short Att', 'Short Cmp%',
                                            'Medium Cmp', 'Medium Att', 'Medium Cmp%',
                                            'Long Cmp', 'Long Att', 'Long Cmp%',
                                            'Ast', 'xAG', 'xA', 'A-xAG', 'Key Passes', 'Final Third Passes','PPA', 'CrsPA', 'PrgP'])



    #### Bảng Pass Types
        bang5 = []
        rows5 = tables[6].find('tbody').find_all('tr')
        for row in rows5:
            name5 = row.find('th').text.strip()
            cols5 = row.find_all('td')
            pass_types = []
            # Pass Types: Live, Dead, FK, TB, Sw, Crs, TI, CK
            for i in range(5, 13):  
                pass_types.append(cols5[i].text.strip())

            # Corner Kicks: In, Out, Str
            for i in range(13, 16): 
                pass_types.append(cols5[i].text.strip())

            # Outcomes: Cmp, Off, Blocks
            for i in range(16, 19): 
                pass_types.append(cols5[i].text.strip())

            
            bang5.append([name5] + pass_types)

        df5 = pd.DataFrame(bang5, columns=[ 'Name', 
                                            'Pass Types.Live', 'Pass Types.Dead', 'Pass Types.FK', 'Pass Types.TB', 'Pass Types.Sw', 
                                            'Pass Types.Crs', 'Pass Types.TI', 'Pass Types.CK', 
                                            'Corner Kicks.In', 'Corner Kicks.Out', 'Corner Kicks.Str', 
                                            'Outcomes.Cmp', 'Outcomes.Off', 'Outcomes.Blocks' ])
        
    
    #### Bảng Goal and Shot Creation 
        bang6 = []
        rows6 = tables[7].find('tbody').find_all('tr')
        for row in rows6:
            name6 = row.find('th').text.strip()
            cols6 = row.find_all('td')

            nap = []
            for i in range(4, 20): 
                nap.append(cols6[i].text.strip())
            
            bang6.append([name6] + nap)

        df6= pd.DataFrame(bang6,  columns=[
            'Name', 'SCA', 'SCA90', 'PassLive', 'PassDead', 'TO', 'Sh', 'Fld', 'Def',
            'GCA', 'GCA90', 'GCA PassLive', 'GCA PassDead', 'GCA TO', 'GCA Sh', 'GCA Fld', 'GCA Def'
        ])

  
    #### Bảng Defensive Actions:
        bang7 = []
        rows7 = tables[8].find('tbody').find_all('tr')
        for row in rows7:
            name7 = row.find('th').text.strip()
            cols7 = row.find_all('td')

            nap = []
            for i in range(4, 20): 
                nap.append(cols7[i].text.strip())
            
            bang6.append([name7] + nap)

        df7= pd.DataFrame(bang7,  columns=[
            'Name', 'Tkl', 'TklW', 'Def 3rd', 'Mid 3rd', 'Att 3rd', 
            'Tkl Att', 'Tkl%', 'Tkl Lost', 'Blocks', 'Sh', 'Pass', 'Int', 'Tkl+Int', 'Clr', 'Err'
        ])

    #### Bảng Possession
        bang8 = []
        rows8 = tables[9].find('tbody').find_all('tr')
        for row in rows8:
            name8 = row.find('th').text.strip()
            cols8= row.find_all('td')

            nap = []
            for i in range(4, 26): 
                nap.append(cols8[i].text.strip())
            
            bang8.append([name8] + nap)

        df8= pd.DataFrame(bang8, columns=[
            'Name', 'Touches', 'Def Pen', 'Def 3rd', 'Mid 3rd', 'Att 3rd', 'Att Pen', 'Live',
            'Att', 'Succ', 'Succ%', 'Tkld', 'Tkld% ',
            'Carries', 'TotDist', 'ProDist', 'ProgC', '1/3', 'CPA',  'Mis', 'Dis', 'Rec', 'PrgR'])

    #### Bảng Playing Time
        bang9 = []
        rows9 = tables[10].find('tbody').find_all('tr')
        for row in rows9:
            name9 = row.find('th').text.strip()
            cols9= row.find_all('td')

            nap = []
            for i in range(9, 18): 
                nap.append(cols9[i].text.strip())
            for i in range(21, 23): 
                nap.append(cols9[i].text.strip())
            
            bang9.append([name9] + nap)

        df9= pd.DataFrame(bang9, columns=[
            'Name', 'Starts', 'Mn/Start', 'Compl', 'Subs', 'Mn/Sub', 'unSub',
            'PPM', 'onG', 'onGA', 'onxG', 'onxGA'
        ])

    #### Bảng Miscellaneous Stats
        bang10 = []
        rows10= tables[11].find('tbody').find_all('tr')
        for row in rows10:
            name10 = row.find('th').text.strip()
            cols10= row.find_all('td')

            nap = []
            for i in range(7, 11): 
                nap.append(cols10[i].text.strip())

            for i in range(15, 20): 
                nap.append(cols10[i].text.strip())
            
            bang10.append([name10] + nap)

        df10= pd.DataFrame(bang10, columns=[
            'Name', 'Fls', 'Fld', 'Off', 'Crs', 'OG', 'Recov', 
            'Aerial Won', 'Aerial Lost', 'Aerial Won%'
        ])



    #### Chuẩn hóa cột Tên về cùng 1 dạng chữ
        df1['Name'] = df1['Name'].str.strip().str.upper()
        df2['Name'] = df2['Name'].str.strip().str.upper()
        df3['Name'] = df3['Name'].str.strip().str.upper()
        df4['Name'] = df4['Name'].str.strip().str.upper()
        df5['Name'] = df5['Name'].str.strip().str.upper()
        df6['Name'] = df6['Name'].str.strip().str.upper()
        df7['Name'] = df7['Name'].str.strip().str.upper()
        df8['Name'] = df8['Name'].str.strip().str.upper()
        df9['Name'] = df9['Name'].str.strip().str.upper()
        df10['Name'] = df10['Name'].str.strip().str.upper()

    #### Ghép các bảng dữ liệu dựa trên cột Tên
        merged_df = df1
        merged_df = pd.merge(merged_df, df2, on='Name', how='left')
        merged_df = pd.merge(merged_df, df3, on='Name', how='left')
        merged_df = pd.merge(merged_df, df4, on='Name', how='left')
        merged_df = pd.merge(merged_df, df5, on='Name', how='left')
        merged_df = pd.merge(merged_df, df6, on='Name', how='left')
        merged_df = pd.merge(merged_df, df7, on='Name', how='left')
        merged_df = pd.merge(merged_df, df8, on='Name', how='left')
        merged_df = pd.merge(merged_df, df9, on='Name', how='left')
        merged_df = pd.merge(merged_df, df10, on='Name', how='left')


    #### Chuyển cột minutes thành kiểu số nguyên 
        merged_df['minutes'] = pd.to_numeric(merged_df['minutes'].str.replace(',', ''), errors='coerce')

    #### Lọc cầu thủ có số phút thi nhiều hơn 90
        cau_thu = merged_df[merged_df['minutes'] > 90]

    #### In ra tất cả các thuộc tính của các cầu thủ này
        Tong_hop_team.append(cau_thu)
            

    

#### Gộp tất cả các DataFrame vào một DataFrame duy nhất
merged_dfx = pd.concat(Tong_hop_team, ignore_index=True)

#### Sắp xếp tên cầu thủ theo tên và tuổi
merged_dfx = merged_dfx.sort_values(by=['Name', 'Age'], ascending=[True, False])

#### Thay thế giá trị rỗng bằng 'N/a'
merged_dfx = merged_dfx.fillna('N/a')

#### Ghi kết quả ra file CSV
merged_dfx.to_csv('results.csv', index=False)

#### In ra DataFrame kết quả
print(merged_dfx)
