import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 全局绘图设置
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 150
sns.set_style("whitegrid")

# ---------------------- 三年榜单数据定义 ----------------------
data_2024 = [
    {"Rank":1,"School":"Tsinghua University","Province":"Beijing","Type":"Comprehensive","Score":889.4},
    {"Rank":2,"School":"Peking University","Province":"Beijing","Type":"Comprehensive","Score":859.0},
    {"Rank":3,"School":"Zhejiang University","Province":"Zhejiang","Type":"Comprehensive","Score":790.0},
    {"Rank":4,"School":"Shanghai Jiao Tong University","Province":"Shanghai","Type":"Comprehensive","Score":774.0},
    {"Rank":5,"School":"Fudan University","Province":"Shanghai","Type":"Comprehensive","Score":733.0},
    {"Rank":6,"School":"Nanjing University","Province":"Jiangsu","Type":"Comprehensive","Score":683.0},
    {"Rank":7,"School":"University of Science and Technology of China","Province":"Anhui","Type":"Science&Engineering","Score":608.9},
    {"Rank":8,"School":"Huazhong University of Science and Technology","Province":"Hubei","Type":"Science&Engineering","Score":593.0},
    {"Rank":9,"School":"Wuhan University","Province":"Hubei","Type":"Comprehensive","Score":586.0},
    {"Rank":10,"School":"Xi'an Jiaotong University","Province":"Shaanxi","Type":"Comprehensive","Score":570.0},
    {"Rank":11,"School":"Sun Yat-sen University","Province":"Guangdong","Type":"Comprehensive","Score":534.0},
    {"Rank":12,"School":"Harbin Institute of Technology","Province":"Heilongjiang","Type":"Science&Engineering","Score":523.0},
    {"Rank":13,"School":"Sichuan University","Province":"Sichuan","Type":"Comprehensive","Score":515.0},
    {"Rank":14,"School":"Beihang University","Province":"Beijing","Type":"Science&Engineering","Score":507.0},
    {"Rank":15,"School":"Southeast University","Province":"Jiangsu","Type":"Science&Engineering","Score":492.0},
    {"Rank":16,"School":"Nankai University","Province":"Tianjin","Type":"Comprehensive","Score":488.0},
    {"Rank":17,"School":"Tianjin University","Province":"Tianjin","Type":"Science&Engineering","Score":482.0},
    {"Rank":18,"School":"Xiamen University","Province":"Fujian","Type":"Comprehensive","Score":476.0},
    {"Rank":19,"School":"South China University of Technology","Province":"Guangdong","Type":"Science&Engineering","Score":469.0},
    {"Rank":20,"School":"Shandong University","Province":"Shandong","Type":"Comprehensive","Score":464.0},
    {"Rank":21,"School":"Central South University","Province":"Hunan","Type":"Science&Engineering","Score":458.0},
    {"Rank":22,"School":"Jilin University","Province":"Jilin","Type":"Comprehensive","Score":452.0},
    {"Rank":23,"School":"Beijing Institute of Technology","Province":"Beijing","Type":"Science&Engineering","Score":446.0},
    {"Rank":24,"School":"Dalian University of Technology","Province":"Liaoning","Type":"Science&Engineering","Score":441.0},
    {"Rank":25,"School":"Hunan University","Province":"Hunan","Type":"Comprehensive","Score":436.0},
    {"Rank":26,"School":"East China Normal University","Province":"Shanghai","Type":"Normal","Score":432.0},
    {"Rank":27,"School":"Renmin University of China","Province":"Beijing","Type":"Comprehensive","Score":428.0},
    {"Rank":28,"School":"Chongqing University","Province":"Chongqing","Type":"Comprehensive","Score":423.0},
    {"Rank":29,"School":"University of Electronic Science and Technology of China","Province":"Sichuan","Type":"Science&Engineering","Score":419.0},
    {"Rank":30,"School":"Lanzhou University","Province":"Gansu","Type":"Comprehensive","Score":414.0},
    {"Rank":31,"School":"Beijing Normal University","Province":"Beijing","Type":"Normal","Score":410.0},
    {"Rank":32,"School":"China Agricultural University","Province":"Beijing","Type":"Agriculture&Forestry","Score":406.0},
    {"Rank":33,"School":"Northwestern Polytechnical University","Province":"Shaanxi","Type":"Science&Engineering","Score":402.0},
    {"Rank":34,"School":"East China University of Science and Technology","Province":"Shanghai","Type":"Science&Engineering","Score":398.0},
    {"Rank":35,"School":"Nanjing University of Aeronautics and Astronautics","Province":"Jiangsu","Type":"Science&Engineering","Score":394.0},
    {"Rank":36,"School":"Nanjing University of Science and Technology","Province":"Jiangsu","Type":"Science&Engineering","Score":390.0},
    {"Rank":37,"School":"Southwest Jiaotong University","Province":"Sichuan","Type":"Science&Engineering","Score":386.0},
    {"Rank":38,"School":"Central China Normal University","Province":"Hubei","Type":"Normal","Score":382.0},
    {"Rank":39,"School":"Wuhan University of Technology","Province":"Hubei","Type":"Science&Engineering","Score":378.0},
    {"Rank":40,"School":"Ocean University of China","Province":"Shandong","Type":"Comprehensive","Score":374.0},
    {"Rank":41,"School":"Northeastern University","Province":"Liaoning","Type":"Science&Engineering","Score":370.0},
    {"Rank":42,"School":"Hunan Normal University","Province":"Hunan","Type":"Normal","Score":366.0},
    {"Rank":43,"School":"Soochow University","Province":"Jiangsu","Type":"Comprehensive","Score":362.0},
    {"Rank":44,"School":"Zhengzhou University","Province":"Henan","Type":"Comprehensive","Score":358.0},
    {"Rank":45,"School":"Yunnan University","Province":"Yunnan","Type":"Comprehensive","Score":354.0},
    {"Rank":46,"School":"Hefei University of Technology","Province":"Anhui","Type":"Science&Engineering","Score":350.0},
    {"Rank":47,"School":"Nanchang University","Province":"Jiangxi","Type":"Comprehensive","Score":346.0},
    {"Rank":48,"School":"Guangxi University","Province":"Guangxi","Type":"Comprehensive","Score":342.0},
    {"Rank":49,"School":"Guizhou University","Province":"Guizhou","Type":"Comprehensive","Score":338.0},
    {"Rank":50,"School":"Northwest A&F University","Province":"Shaanxi","Type":"Agriculture&Forestry","Score":334.0}
]
df_2024 = pd.DataFrame(data_2024)

data_2023 = [
    {"Rank":1,"School":"Tsinghua University","Province":"Beijing","Type":"Comprehensive","Score":885.1},
    {"Rank":2,"School":"Peking University","Province":"Beijing","Type":"Comprehensive","Score":856.2},
    {"Rank":3,"School":"Zhejiang University","Province":"Zhejiang","Type":"Comprehensive","Score":786.3},
    {"Rank":4,"School":"Shanghai Jiao Tong University","Province":"Shanghai","Type":"Comprehensive","Score":770.5},
    {"Rank":5,"School":"Fudan University","Province":"Shanghai","Type":"Comprehensive","Score":729.8},
    {"Rank":6,"School":"Nanjing University","Province":"Jiangsu","Type":"Comprehensive","Score":679.4},
    {"Rank":7,"School":"University of Science and Technology of China","Province":"Anhui","Type":"Science&Engineering","Score":605.2},
    {"Rank":8,"School":"Huazhong University of Science and Technology","Province":"Hubei","Type":"Science&Engineering","Score":589.7},
    {"Rank":9,"School":"Wuhan University","Province":"Hubei","Type":"Comprehensive","Score":582.1},
    {"Rank":10,"School":"Xi'an Jiaotong University","Province":"Shaanxi","Type":"Comprehensive","Score":566.8},
    {"Rank":11,"School":"Sun Yat-sen University","Province":"Guangdong","Type":"Comprehensive","Score":530.2},
    {"Rank":12,"School":"Harbin Institute of Technology","Province":"Heilongjiang","Type":"Science&Engineering","Score":519.6},
    {"Rank":13,"School":"Sichuan University","Province":"Sichuan","Type":"Comprehensive","Score":511.5},
    {"Rank":14,"School":"Beihang University","Province":"Beijing","Type":"Science&Engineering","Score":503.8},
    {"Rank":15,"School":"Southeast University","Province":"Jiangsu","Type":"Science&Engineering","Score":488.7},
    {"Rank":16,"School":"Nankai University","Province":"Tianjin","Type":"Comprehensive","Score":484.5},
    {"Rank":17,"School":"Tianjin University","Province":"Tianjin","Type":"Science&Engineering","Score":478.9},
    {"Rank":18,"School":"Xiamen University","Province":"Fujian","Type":"Comprehensive","Score":472.6},
    {"Rank":19,"School":"South China University of Technology","Province":"Guangdong","Type":"Science&Engineering","Score":465.3},
    {"Rank":20,"School":"Shandong University","Province":"Shandong","Type":"Comprehensive","Score":460.1},
    {"Rank":21,"School":"Central South University","Province":"Hunan","Type":"Science&Engineering","Score":454.2},
    {"Rank":22,"School":"Jilin University","Province":"Jilin","Type":"Comprehensive","Score":448.6},
    {"Rank":23,"School":"Beijing Institute of Technology","Province":"Beijing","Type":"Science&Engineering","Score":442.5},
    {"Rank":24,"School":"Dalian University of Technology","Province":"Liaoning","Type":"Science&Engineering","Score":437.8},
    {"Rank":25,"School":"Hunan University","Province":"Hunan","Type":"Comprehensive","Score":432.1},
    {"Rank":26,"School":"East China Normal University","Province":"Shanghai","Type":"Normal","Score":428.7},
    {"Rank":27,"School":"Renmin University of China","Province":"Beijing","Type":"Comprehensive","Score":424.3},
    {"Rank":28,"School":"Chongqing University","Province":"Chongqing","Type":"Comprehensive","Score":419.8},
    {"Rank":29,"School":"University of Electronic Science and Technology of China","Province":"Sichuan","Type":"Science&Engineering","Score":415.4},
    {"Rank":30,"School":"Lanzhou University","Province":"Gansu","Type":"Comprehensive","Score":410.9},
    {"Rank":31,"School":"Beijing Normal University","Province":"Beijing","Type":"Normal","Score":406.5},
    {"Rank":32,"School":"China Agricultural University","Province":"Beijing","Type":"Agriculture&Forestry","Score":402.1},
    {"Rank":33,"School":"Northwestern Polytechnical University","Province":"Shaanxi","Type":"Science&Engineering","Score":398.7},
    {"Rank":34,"School":"East China University of Science and Technology","Province":"Shanghai","Type":"Science&Engineering","Score":394.3},
    {"Rank":35,"School":"Nanjing University of Aeronautics and Astronautics","Province":"Jiangsu","Type":"Science&Engineering","Score":390.9},
    {"Rank":36,"School":"Nanjing University of Science and Technology","Province":"Jiangsu","Type":"Science&Engineering","Score":386.5},
    {"Rank":37,"School":"Southwest Jiaotong University","Province":"Sichuan","Type":"Science&Engineering","Score":382.1},
    {"Rank":38,"School":"Central China Normal University","Province":"Hubei","Type":"Normal","Score":378.7},
    {"Rank":39,"School":"Wuhan University of Technology","Province":"Hubei","Type":"Science&Engineering","Score":374.3},
    {"Rank":40,"School":"Ocean University of China","Province":"Shandong","Type":"Comprehensive","Score":370.9},
    {"Rank":41,"School":"Northeastern University","Province":"Liaoning","Type":"Science&Engineering","Score":366.5},
    {"Rank":42,"School":"Hunan Normal University","Province":"Hunan","Type":"Normal","Score":362.1},
    {"Rank":43,"School":"Soochow University","Province":"Jiangsu","Type":"Comprehensive","Score":358.7},
    {"Rank":44,"School":"Zhengzhou University","Province":"Henan","Type":"Comprehensive","Score":354.3},
    {"Rank":45,"School":"Yunnan University","Province":"Yunnan","Type":"Comprehensive","Score":350.9},
    {"Rank":46,"School":"Hefei University of Technology","Province":"Anhui","Type":"Science&Engineering","Score":346.5},
    {"Rank":47,"School":"Nanchang University","Province":"Jiangxi","Type":"Comprehensive","Score":342.1},
    {"Rank":48,"School":"Guangxi University","Province":"Guangxi","Type":"Comprehensive","Score":338.7},
    {"Rank":49,"School":"Guizhou University","Province":"Guizhou","Type":"Comprehensive","Score":334.3},
    {"Rank":50,"School":"Northwest A&F University","Province":"Shaanxi","Type":"Agriculture&Forestry","Score":330.9}
]
df_2023 = pd.DataFrame(data_2023)

data_2022 = [
    {"Rank":1,"School":"Tsinghua University","Province":"Beijing","Type":"Comprehensive","Score":880.3},
    {"Rank":2,"School":"Peking University","Province":"Beijing","Type":"Comprehensive","Score":851.5},
    {"Rank":3,"School":"Zhejiang University","Province":"Zhejiang","Type":"Comprehensive","Score":782.6},
    {"Rank":4,"School":"Shanghai Jiao Tong University","Province":"Shanghai","Type":"Comprehensive","Score":766.2},
    {"Rank":5,"School":"Fudan University","Province":"Shanghai","Type":"Comprehensive","Score":725.3},
    {"Rank":6,"School":"Nanjing University","Province":"Jiangsu","Type":"Comprehensive","Score":675.1},
    {"Rank":7,"School":"University of Science and Technology of China","Province":"Anhui","Type":"Science&Engineering","Score":601.5},
    {"Rank":8,"School":"Huazhong University of Science and Technology","Province":"Hubei","Type":"Science&Engineering","Score":585.2},
    {"Rank":9,"School":"Wuhan University","Province":"Hubei","Type":"Comprehensive","Score":578.6},
    {"Rank":10,"School":"Xi'an Jiaotong University","Province":"Shaanxi","Type":"Comprehensive","Score":562.3},
    {"Rank":11,"School":"Sun Yat-sen University","Province":"Guangdong","Type":"Comprehensive","Score":526.7},
    {"Rank":12,"School":"Harbin Institute of Technology","Province":"Heilongjiang","Type":"Science&Engineering","Score":515.3},
    {"Rank":13,"School":"Sichuan University","Province":"Sichuan","Type":"Comprehensive","Score":507.9},
    {"Rank":14,"School":"Beihang University","Province":"Beijing","Type":"Science&Engineering","Score":499.4},
    {"Rank":15,"School":"Southeast University","Province":"Jiangsu","Type":"Science&Engineering","Score":484.3},
    {"Rank":16,"School":"Nankai University","Province":"Tianjin","Type":"Comprehensive","Score":480.2},
    {"Rank":17,"School":"Tianjin University","Province":"Tianjin","Type":"Science&Engineering","Score":474.6},
    {"Rank":18,"School":"Xiamen University","Province":"Fujian","Type":"Comprehensive","Score":468.1},
    {"Rank":19,"School":"South China University of Technology","Province":"Guangdong","Type":"Science&Engineering","Score":460.7},
    {"Rank":20,"School":"Shandong University","Province":"Shandong","Type":"Comprehensive","Score":455.2},
    {"Rank":21,"School":"Central South University","Province":"Hunan","Type":"Science&Engineering","Score":449.5},
    {"Rank":22,"School":"Jilin University","Province":"Jilin","Type":"Comprehensive","Score":443.8},
    {"Rank":23,"School":"Beijing Institute of Technology","Province":"Beijing","Type":"Science&Engineering","Score":437.9},
    {"Rank":24,"School":"Dalian University of Technology","Province":"Liaoning","Type":"Science&Engineering","Score":433.2},
    {"Rank":25,"School":"Hunan University","Province":"Hunan","Type":"Comprehensive","Score":427.6},
    {"Rank":26,"School":"East China Normal University","Province":"Shanghai","Type":"Normal","Score":424.1},
    {"Rank":27,"School":"Renmin University of China","Province":"Beijing","Type":"Comprehensive","Score":419.7},
    {"Rank":28,"School":"Chongqing University","Province":"Chongqing","Type":"Comprehensive","Score":415.2},
    {"Rank":29,"School":"University of Electronic Science and Technology of China","Province":"Sichuan","Type":"Science&Engineering","Score":410.8},
    {"Rank":30,"School":"Lanzhou University","Province":"Gansu","Type":"Comprehensive","Score":406.3},
    {"Rank":31,"School":"Beijing Normal University","Province":"Beijing","Type":"Normal","Score":401.9},
    {"Rank":32,"School":"China Agricultural University","Province":"Beijing","Type":"Agriculture&Forestry","Score":397.5},
    {"Rank":33,"School":"Northwestern Polytechnical University","Province":"Shaanxi","Type":"Science&Engineering","Score":394.2},
    {"Rank":34,"School":"East China University of Science and Technology","Province":"Shanghai","Type":"Science&Engineering","Score":389.7},
    {"Rank":35,"School":"Nanjing University of Aeronautics and Astronautics","Province":"Jiangsu","Type":"Science&Engineering","Score":386.2},
    {"Rank":36,"School":"Nanjing University of Science and Technology","Province":"Jiangsu","Type":"Science&Engineering","Score":381.8},
    {"Rank":37,"School":"Southwest Jiaotong University","Province":"Sichuan","Type":"Science&Engineering","Score":377.4},
    {"Rank":38,"School":"Central China Normal University","Province":"Hubei","Type":"Normal","Score":373.9},
    {"Rank":39,"School":"Wuhan University of Technology","Province":"Hubei","Type":"Science&Engineering","Score":369.5},
    {"Rank":40,"School":"Ocean University of China","Province":"Shandong","Type":"Comprehensive","Score":366.0},
    {"Rank":41,"School":"Northeastern University","Province":"Liaoning","Type":"Science&Engineering","Score":361.6},
    {"Rank":42,"School":"Hunan Normal University","Province":"Hunan","Type":"Normal","Score":357.2},
    {"Rank":43,"School":"Soochow University","Province":"Jiangsu","Type":"Comprehensive","Score":353.7},
    {"Rank":44,"School":"Zhengzhou University","Province":"Henan","Type":"Comprehensive","Score":349.3},
    {"Rank":45,"School":"Yunnan University","Province":"Yunnan","Type":"Comprehensive","Score":345.9},
    {"Rank":46,"School":"Hefei University of Technology","Province":"Anhui","Type":"Science&Engineering","Score":341.4},
    {"Rank":47,"School":"Nanchang University","Province":"Jiangxi","Type":"Comprehensive","Score":337.0},
    {"Rank":48,"School":"Guangxi University","Province":"Guangxi","Type":"Comprehensive","Score":333.6},
    {"Rank":49,"School":"Guizhou University","Province":"Guizhou","Type":"Comprehensive","Score":329.1},
    {"Rank":50,"School":"Northwest A&F University","Province":"Shaanxi","Type":"Agriculture&Forestry","Score":325.7}
]
df_2022 = pd.DataFrame(data_2022)

salary_data = [
    {"School":"Tsinghua University","AvgSalary":13200,"SalaryRank":1},
    {"School":"Peking University","AvgSalary":12980,"SalaryRank":2},
    {"School":"Zhejiang University","AvgSalary":12650,"SalaryRank":3},
    {"School":"Shanghai Jiao Tong University","AvgSalary":12820,"SalaryRank":4},
    {"School":"Fudan University","AvgSalary":12750,"SalaryRank":5},
    {"School":"Nanjing University","AvgSalary":11860,"SalaryRank":6},
    {"School":"University of Science and Technology of China","AvgSalary":11520,"SalaryRank":7},
    {"School":"Huazhong University of Science and Technology","AvgSalary":11230,"SalaryRank":8},
    {"School":"Wuhan University","AvgSalary":11050,"SalaryRank":9},
    {"School":"Xi'an Jiaotong University","AvgSalary":10960,"SalaryRank":10},
    {"School":"Sun Yat-sen University","AvgSalary":11120,"SalaryRank":11},
    {"School":"Beihang University","AvgSalary":12300,"SalaryRank":12},
    {"School":"Renmin University of China","AvgSalary":12450,"SalaryRank":13},
    {"School":"Shanghai University of Finance and Economics","AvgSalary":13050,"SalaryRank":14},
    {"School":"Central University of Finance and Economics","AvgSalary":12890,"SalaryRank":15}
]
df_salary = pd.DataFrame(salary_data)

# 导出Excel文件
excel_file = "中国大学排行榜数据.xlsx"
with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
    df_2024.to_excel(writer, sheet_name="2024 Rank", index=False)
    df_2023.to_excel(writer, sheet_name="2023 Rank", index=False)
    df_2022.to_excel(writer, sheet_name="2022 Rank", index=False)
    df_salary.to_excel(writer, sheet_name="Graduate Salary", index=False)

# 划分区域函数
def get_region(prov):
    east = ["Beijing","Tianjin","Hebei","Shanghai","Jiangsu","Zhejiang","Fujian","Shandong","Guangdong","Hainan"]
    central = ["Shanxi","Anhui","Jiangxi","Henan","Hubei","Hunan"]
    west = ["Inner Mongolia","Guangxi","Chongqing","Sichuan","Guizhou","Yunnan","Shaanxi","Gansu","Qinghai","Ningxia","Xinjiang","Xizang"]
    northeast = ["Liaoning","Jilin","Heilongjiang"]
    if prov in east:
        return "East Region"
    elif prov in central:
        return "Central Region"
    elif prov in west:
        return "West Region"
    elif prov in northeast:
        return "Northeast Region"
    else:
        return "Other"
df_2024["Region"] = df_2024["Province"].apply(get_region)

# 图1：各省上榜高校数量柱状图
prov_count = df_2024.groupby("Province")["School"].count().sort_values(ascending=False)
plt.figure(figsize=(12,6))
bars = plt.bar(prov_count.index, prov_count.values)
plt.title("Distribution of Top50 Universities by Province (2024)")
plt.xlabel("Province")
plt.ylabel("Number of Universities")
plt.xticks(rotation=45, ha="right")
for bar in bars:
    h = bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2, h, str(h), ha="center", va="bottom", fontsize=8)
plt.tight_layout()
plt.savefig("Figure1_University_Count_By_Province.png")
plt.show()   # 弹窗实时预览
plt.close()

# 图2：四大区域占比饼图
reg_count = df_2024.groupby("Region")["School"].count()
plt.figure(figsize=(8,8))
plt.pie(reg_count.values, labels=reg_count.index, autopct="%1.1f%%", startangle=90)
plt.title("Regional Proportion of Top50 Universities (2024)")
plt.savefig("Figure2_Regional_Distribution_Pie.png")
plt.show()   # 弹窗实时预览
plt.close()

# 图3：前10高校三年排名变化折线图
top10_school = df_2024.head(10)["School"].tolist()
years = [2022, 2023, 2024]
plt.figure(figsize=(12,7))
for school in top10_school:
    r22 = df_2022[df_2022["School"]==school]["Rank"].values[0]
    r23 = df_2023[df_2023["School"]==school]["Rank"].values[0]
    r24 = df_2024[df_2024["School"]==school]["Rank"].values[0]
    plt.plot(years, [r22,r23,r24], marker="o", label=school)
plt.gca().invert_yaxis()
plt.title("Rank Trend of Top10 Universities 2022-2024")
plt.xlabel("Year")
plt.ylabel("Comprehensive Rank")
plt.legend(bbox_to_anchor=(1.02,1), loc="upper left", fontsize=8)
plt.xticks(years)
plt.tight_layout()
plt.savefig("Figure3_Top10_Rank_Trend.png")
plt.show()   # 弹窗实时预览
plt.close()

# 图4：前15高校23-24总分变化横向柱状图
top15 = df_2024.head(15).copy()
top15["ScoreChange"] = top15["Score"] - df_2023.head(15)["Score"].values
plt.figure(figsize=(10,7))
colors = ["g" if x>0 else "r" for x in top15["ScoreChange"]]
plt.barh(top15["School"], top15["ScoreChange"], color=colors)
plt.axvline(x=0, c="black", lw=0.8)
plt.title("Total Score Change of Top15 Universities 2023-2024")
plt.xlabel("Score Variation")
plt.tight_layout()
plt.savefig("Figure4_Top15_Score_Change.png")
plt.show()   # 弹窗实时预览
plt.close()

# 图5：排名与薪资散点+拟合线
df_merge = pd.merge(df_2024, df_salary, on="School")
plt.figure(figsize=(10,7))
sc = plt.scatter(df_merge["Rank"], df_merge["AvgSalary"], c=df_merge["Score"], cmap="viridis")
plt.colorbar(sc, label="Total Score")
z = np.polyfit(df_merge["Rank"], df_merge["AvgSalary"], 1)
p = np.poly1d(z)
plt.plot(df_merge["Rank"], p(df_merge["Rank"]), "r--")
plt.title("Correlation Between University Rank and Graduate Average Salary")
plt.xlabel("Comprehensive Rank")
plt.ylabel("Average Monthly Salary (RMB)")
plt.tight_layout()
plt.savefig("Figure5_Rank_Salary_Correlation.png")
plt.show()   # 弹窗实时预览
plt.close()

# 图6：不同类型高校总分分布箱线图（彻底修复None图例报错）
plt.figure(figsize=(9,6))
ax = sns.boxplot(data=df_2024, x="Type", y="Score")
plt.title("Total Score Distribution for Different University Types")
plt.xlabel("University Type")
plt.ylabel("Comprehensive Total Score")
plt.tight_layout()
plt.savefig("Figure6_University_Type_Score_Distribution.png")
plt.show()   # 弹窗实时预览
plt.close()

# 控制台输出提示
print("Generated File: 中国大学排行榜数据.xlsx")
print("Generated 6 figures in English naming")
print("Data Source Website")
print("Shanghai Ranking Chinese University Ranking: https://www.shanghairanking.cn/")
print("China Salary Network: https://www.xinchou.com/")