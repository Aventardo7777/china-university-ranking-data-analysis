# China University Ranking Data Analysis
<div align="center">
<img src="https://img.shields.io/badge/Python-3.8+-blue" alt="Python Version">
<img src="https://img.shields.io/badge/Lib-Pandas%2FMatplotlib%2FSeaborn-orange" alt="Tech Stack">
<img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
<img src="https://img.shields.io/badge/Type-Course%20Data%20Analysis-purple" alt="Project Type">
</div>

### 🌐 仓库直达链接（新标签打开）
<a href="https://github.com/Aventardo7777/china-university-ranking-data-analysis" target="_blank">https://github.com/Aventardo7777/china-university-ranking-data-analysis</a>

## 📖 项目简介
本项目为Python数据分析课程完整大作业，基于软科中国大学排名公开数据，搭建完整「爬虫-数据整合-清洗-多维度统计-可视化」分析流程。
整合2022-2024三年高校综合榜单、各省市高校分布、院校类型、毕业生薪资多维度数据，输出标准化Excel数据集与6张专业分析图表，为高考志愿填报提供量化参考依据。

## ✨ 项目核心功能模块
1. **多年份榜单数据集内置**
内置连续三年全国百强高校综合评分、办学类型、所属省份数据，无需额外爬取即可直接分析；附带毕业生平均薪资关联数据集。
2. **标准化数据导出**
自动生成多工作表Excel文件，分年份存储排名数据、薪资数据，方便二次查阅。
3. **六大专业可视化图表自动生成**
- 各省上榜高校数量柱状图
- 东/中/西/东北四大区域占比饼图
- Top10高校三年排名变化折线图
- Top15高校总分变化横向柱状图
- 院校排名与薪资相关性散点拟合图
- 不同办学类型总分分布箱线图
4. **配套完整课程研究报告**
文档包含数据来源、缺失值处理、统计结果解读、报考参考建议、研究总结。

## 🧰 运行环境与启动方式
### 1. 依赖一键安装
pip install pandas numpy matplotlib seaborn openpyxl
### 2.本地运行命令
python 中国大学排行榜数据分析.py
#### 运行完根目录会自动生成EXCEL数据源＋6张高清PNG分析图表

## 📁 仓库标准文件结构
<img width="820" height="213" alt="image" src="https://github.com/user-attachments/assets/68bac1b0-ba93-4b9e-aee3-c9a9a9a3a342" />

## 📊 三大分析研究维度
### 地域维度：统计各省市高校数量、平均分，划分四大教育区域对比；
### 院校维度：综合分数分层、理工 / 综合 / 师范 / 农林类型分数分布对比；
### 就业维度：院校综合排名与毕业生平均薪资相关性量化分析。

## 📜 开源说明
本项目采用 MIT 开源协议，允许个人学习、课程作业、二次数据拓展分析，转载务必保留原仓库来源标注
