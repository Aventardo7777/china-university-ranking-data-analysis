# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:20:39 2026

@author: avent
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 10:15:43 2026

@author: avent
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2023软科排名数据探索性分析（修复版）
作者: Claude Data Analysis Assistant
日期: 2025-10-02
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from scipy import stats
from scipy.stats import pearsonr, spearmanr
import warnings
import os
warnings.filterwarnings('ignore')

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# ==============================================
# 【核心修复】自动获取当前脚本所在路径
# ==============================================
# 固定桌面路径
data_file = r"C:\Users\avent\Desktop\data.csv"
output_dir = r"C:\Users\avent\Desktop\analysis_reports"

# 自动创建输出文件夹
import os
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 提前校验文件是否存在，给出清晰提示
if not os.path.exists(data_file):
    print(f"❌ 找不到文件：{data_file}")
    print("请确认桌面上确实存在 data.csv 文件，文件名不要多空格、后缀不要隐藏")
    exit()

def load_and_inspect_data(file_path):
    """
    加载数据并进行初始检查
    """
    print("=" * 50)
    print("1. 数据加载与初始检查")
    print("=" * 50)

    # 读取数据
    df = pd.read_csv(file_path, encoding='utf-8')

    # 基本信息
    print(f"数据集形状: {df.shape}")
    print(f"列数: {df.shape[1]}")
    print(f"行数: {df.shape[0]}")
    print("\n列名:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i:2d}. {col}")

    # 数据类型
    print("\n数据类型:")
    print(df.dtypes)

    # 前5行和后5行
    print("\n前5行数据:")
    print(df.head())

    print("\n后5行数据:")
    print(df.tail())

    return df

def check_data_quality(df):
    """
    检查数据质量
    """
    print("\n" + "=" * 50)
    print("2. 数据质量检查")
    print("=" * 50)

    quality_report = {}

    # 缺失值检查
    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / len(df)) * 100

    print("缺失值统计:")
    missing_data = []
    for col in df.columns:
        if missing_values[col] > 0:
            missing_data.append({
                'column': col,
                'missing_count': int(missing_values[col]),
                'missing_percentage': round(float(missing_percentage[col]), 2)
            })

    missing_data.sort(key=lambda x: x['missing_count'], reverse=True)

    for item in missing_data:
        print(f"{item['column']}: {item['missing_count']}个缺失值 ({item['missing_percentage']}%)")

    quality_report['missing_values'] = missing_data

    # 重复值检查
    duplicates = df.duplicated().sum()
    print(f"\n重复行数: {duplicates}")
    quality_report['duplicate_rows'] = int(duplicates)

    # 数据类型一致性检查
    print("\n数据类型检查:")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

    print(f"数值型列 ({len(numeric_cols)}): {numeric_cols}")
    print(f"分类型列 ({len(categorical_cols)}): {categorical_cols}")

    quality_report['numeric_columns'] = numeric_cols
    quality_report['categorical_columns'] = categorical_cols

    # 检查数值列的范围
    print("\n数值列基本统计:")
    numeric_stats = df[numeric_cols].describe()
    print(numeric_stats)

    quality_report['numeric_statistics'] = numeric_stats.to_dict()

    return quality_report

def descriptive_statistics(df):
    """
    描述性统计分析
    """
    print("\n" + "=" * 50)
    print("3. 描述性统计分析")
    print("=" * 50)

    # 获取数值列
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    # 基本统计信息
    print("基本统计信息:")
    stats_summary = df[numeric_cols].describe()
    print(stats_summary)

    # 分布特征
    print("\n分布特征分析:")
    distribution_stats = {}

    for col in numeric_cols:
        if col != '排名':  # 排名列不需要分析分布
            try:
                data = df[col].dropna()
                if len(data) > 0:
                    skewness = stats.skew(data)
                    kurtosis = stats.kurtosis(data)

                    distribution_stats[col] = {
                        '偏度': round(skewness, 3),
                        '峰度': round(kurtosis, 3),
                        '最小值': float(data.min()),
                        '最大值': float(data.max()),
                        '中位数': float(data.median()),
                        '标准差': round(float(data.std()), 3)
                    }

                    print(f"{col}: 偏度={skewness:.3f}, 峰度={kurtosis:.3f}")
            except:
                continue

    # 分类变量统计
    print("\n分类变量统计:")
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

    categorical_stats = {}
    for col in categorical_cols:
        value_counts = df[col].value_counts()
        print(f"\n{col} 分布:")
        print(value_counts.head(10))
        categorical_stats[col] = value_counts.to_dict()

    return {
        'basic_statistics': stats_summary.to_dict(),
        'distribution_statistics': distribution_stats,
        'categorical_statistics': categorical_stats
    }

def correlation_analysis(df):
    """
    相关性分析
    """
    print("\n" + "=" * 50)
    print("4. 相关性分析")
    print("=" * 50)

    # 获取数值列
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if len(numeric_cols) < 2:
        print("数值列不足2列，无法进行相关性分析")
        return {}

    # Pearson相关系数
    print("Pearson相关系数矩阵:")
    correlation_matrix = df[numeric_cols].corr()
    print(correlation_matrix.round(3))

    # 找出强相关关系（绝对值 > 0.7）
    print("\n强相关关系（|r| > 0.7）:")
    strong_correlations = []

    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            corr_value = correlation_matrix.iloc[i, j]
            if abs(corr_value) > 0.7 and not pd.isna(corr_value):
                col1 = correlation_matrix.columns[i]
                col2 = correlation_matrix.columns[j]
                strong_correlations.append({
                    'variable1': col1,
                    'variable2': col2,
                    'correlation': round(corr_value, 3)
                })
                print(f"{col1} - {col2}: {corr_value:.3f}")

    return {
        'correlation_matrix': correlation_matrix.to_dict(),
        'strong_correlations': strong_correlations
    }

def outlier_detection(df):
    """
    异常值检测
    """
    print("\n" + "=" * 50)
    print("5. 异常值检测")
    print("=" * 50)

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    outlier_summary = {}

    for col in numeric_cols:
        if col != '排名':  # 排名列不检测异常值
            data = df[col].dropna()
            if len(data) > 0:
                # IQR方法
                Q1 = data.quantile(0.25)
                Q3 = data.quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                outliers_iqr = data[(data < lower_bound) | (data > upper_bound)]

                # Z-score方法
                z_scores = np.abs(stats.zscore(data))
                outliers_zscore = data[z_scores > 3]

                outlier_summary[col] = {
                    'iqr_outliers_count': len(outliers_iqr),
                    'iqr_outliers_percentage': round(len(outliers_iqr) / len(data) * 100, 2),
                    'zscore_outliers_count': len(outliers_zscore),
                    'zscore_outliers_percentage': round(len(outliers_zscore) / len(data) * 100, 2),
                    'lower_bound': round(lower_bound, 2),
                    'upper_bound': round(upper_bound, 2)
                }

                if len(outliers_iqr) > 0:
                    print(f"{col}: IQR异常值 {len(outliers_iqr)}个 ({len(outliers_iqr)/len(data)*100:.1f}%)")

    return outlier_summary

def pattern_discovery(df):
    """
    模式发现
    """
    print("\n" + "=" * 50)
    print("6. 模式发现")
    print("=" * 50)

    patterns = {}

    # 1. 省市分布分析
    if '省市' in df.columns:
        print("省市分布分析:")
        province_stats = df['省市'].value_counts()
        print(province_stats.head(10))
        patterns['province_distribution'] = province_stats.to_dict()

    # 2. 学校类型分析
    if '学校类型' in df.columns:
        print("\n学校类型分析:")
        school_type_stats = df['学校类型'].value_counts()
        print(school_type_stats)
        patterns['school_type_distribution'] = school_type_stats.to_dict()

        # 按学校类型的平均总分
        if '总分' in df.columns:
            print("\n各学校类型平均总分:")
            avg_score_by_type = df.groupby('学校类型')['总分'].agg(['mean', 'count', 'std']).round(2)
            print(avg_score_by_type)
            patterns['avg_score_by_type'] = avg_score_by_type.to_dict()

    # 3. 双一流/985/211分析
    elite_columns = ['是否双一流', '是否985', '是否211']
    for col in elite_columns:
        if col in df.columns:
            print(f"\n{col}分析:")
            elite_stats = df[col].value_counts()
            print(elite_stats)
            patterns[f'{col}_distribution'] = elite_stats.to_dict()

            # 与总分的关系
            if '总分' in df.columns:
                avg_scores = df.groupby(col)['总分'].agg(['mean', 'count', 'std']).round(2)
                print(f"{col}与总分关系:")
                print(avg_scores)
                patterns[f'{col}_score_relation'] = avg_scores.to_dict()

    # 4. 排名区间分析
    if '排名' in df.columns:
        print("\n排名区间分析:")
        # 创建排名区间
        df['排名区间'] = pd.cut(df['排名'], bins=[0, 10, 50, 100, 200, float('inf')],
                               labels=['前10', '11-50', '51-100', '101-200', '200+'])
        ranking_distribution = df['排名区间'].value_counts()
        print(ranking_distribution)
        patterns['ranking_distribution'] = ranking_distribution.to_dict()

    return patterns

def generate_insights(df, quality_report, stats_summary, correlation_results, outlier_results, patterns):
    """
    生成洞察和建议
    """
    print("\n" + "=" * 50)
    print("7. 关键洞察和建议")
    print("=" * 50)

    insights = []

    # 数据质量洞察
    if quality_report['missing_values']:
        missing_count = len(quality_report['missing_values'])
        insights.append({
            'type': '数据质量',
            'finding': f"发现{missing_count}个列存在缺失值",
            'detail': f"缺失值最多的列: {quality_report['missing_values'][0]['column']}({quality_report['missing_values'][0]['missing_count']}个)",
            'recommendation': "建议对缺失值进行处理：删除、填充或标记"
        })

    # 相关性洞察
    if correlation_results and 'strong_correlations' in correlation_results:
        strong_corrs = correlation_results['strong_correlations']
        if strong_corrs:
            insights.append({
                'type': '相关性分析',
                'finding': f"发现{len(strong_corrs)}对强相关变量",
                'detail': f"最强相关: {strong_corrs[0]['variable1']} 与 {strong_corrs[0]['variable2']} (r={strong_corrs[0]['correlation']})",
                'recommendation': "建议在建模时考虑多重共线性问题"
            })

    # 异常值洞察
    if outlier_results:
        outlier_cols = [col for col, data in outlier_results.items() if data['iqr_outliers_count'] > 0]
        if outlier_cols:
            insights.append({
                'type': '异常值分析',
                'finding': f"发现{len(outlier_cols)}个变量存在异常值",
                'detail': f"异常值最多的变量: {outlier_cols[0]}",
                'recommendation': "建议深入调查异常值的产生原因"
            })

    # 分布模式洞察
    if patterns:
        if 'school_type_distribution' in patterns:
            top_type = max(patterns['school_type_distribution'].items(), key=lambda x: x[1])
            insights.append({
                'type': '学校类型分布',
                'finding': f"学校类型分布不均，{top_type[0]}类学校最多",
                'detail': f"{top_type[0]}类学校占比{top_type[1]/sum(patterns['school_type_distribution'].values())*100:.1f}%",
                'recommendation': "在分析时需要考虑学校类型的不平衡"
            })

    # 输出洞察
    for i, insight in enumerate(insights, 1):
        print(f"\n洞察 {i}: {insight['type']}")
        print(f"发现: {insight['finding']}")
        print(f"详情: {insight['detail']}")
        print(f"建议: {insight['recommendation']}")

    return insights

def main():
    """
    主函数
    """
    # 1. 加载和检查数据
    df = load_and_inspect_data(data_file)

    # 2. 数据质量检查
    quality_report = check_data_quality(df)

    # 3. 描述性统计
    stats_summary = descriptive_statistics(df)

    # 4. 相关性分析
    correlation_results = correlation_analysis(df)

    # 5. 异常值检测
    outlier_results = outlier_detection(df)

    # 6. 模式发现
    patterns = pattern_discovery(df)

    # 7. 生成洞察
    insights = generate_insights(df, quality_report, stats_summary, correlation_results, outlier_results, patterns)

    # 保存结果
    print("\n" + "=" * 50)
    print("8. 保存分析结果")
    print("=" * 50)

    # 保存数据质量报告
    quality_file = os.path.join(output_dir, "data_quality.json")
    with open(quality_file, 'w', encoding='utf-8') as f:
        json.dump(quality_report, f, ensure_ascii=False, indent=2)
    print(f"数据质量报告已保存: {quality_file}")

    # 保存统计摘要
    stats_file = os.path.join(output_dir, "statistical_summary.csv")
    if 'basic_statistics' in stats_summary:
        stats_df = pd.DataFrame(stats_summary['basic_statistics'])
        stats_df.to_csv(stats_file, encoding='utf-8-sig')
        print(f"统计摘要已保存: {stats_file}")

    # 生成详细分析报告
    report_file = os.path.join(output_dir, "analysis_summary.md")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# 2023软科排名数据探索性数据分析报告\n\n")
        f.write("## 执行摘要\n\n")
        f.write(f"本报告对{df.shape[0]}所大学的{df.shape[1]}个指标进行了全面的探索性数据分析。\n\n")

        f.write("## 数据概况\n\n")
        f.write(f"- 数据集大小: {df.shape[0]}行 × {df.shape[1]}列\n")
        f.write(f"- 数值型变量: {len(quality_report['numeric_columns'])}个\n")
        f.write(f"- 分类型变量: {len(quality_report['categorical_columns'])}个\n")
        f.write(f"- 缺失值: {len(quality_report.get('missing_values', []))}个变量存在缺失值\n\n")

        f.write("## 主要发现\n\n")
        for i, insight in enumerate(insights, 1):
            f.write(f"### {i}. {insight['type']}\n")
            f.write(f"**发现**: {insight['finding']}\n\n")
            f.write(f"**详情**: {insight['detail']}\n\n")
            f.write(f"**建议**: {insight['recommendation']}\n\n")

        f.write("## 数据质量评估\n\n")
        if quality_report.get('missing_values'):
            f.write("### 缺失值分析\n")
            for item in quality_report['missing_values']:
                f.write(f"- {item['column']}: {item['missing_count']}个缺失值 ({item['missing_percentage']}%)\n")

        f.write(f"\n### 重复值\n")
        f.write(f"发现 {quality_report['duplicate_rows']} 行重复数据\n\n")

        f.write("## 统计分析结果\n\n")
        if correlation_results and 'strong_correlations' in correlation_results:
            f.write("### 强相关关系\n")
            for corr in correlation_results['strong_correlations']:
                f.write(f"- {corr['variable1']} ↔ {corr['variable2']}: r = {corr['correlation']}\n")

        f.write("\n## 模式发现\n\n")
        if patterns:
            if 'school_type_distribution' in patterns:
                f.write("### 学校类型分布\n")
                for school_type, count in patterns['school_type_distribution'].items():
                    f.write(f"- {school_type}: {count}所\n")

            if 'province_distribution' in patterns:
                f.write("\n### 省市分布（前10）\n")
                province_items = list(patterns['province_distribution'].items())[:10]
                for province, count in province_items:
                    f.write(f"- {province}: {count}所\n")

        f.write("\n## 下一步建议\n\n")
        f.write("1. **数据预处理**: 处理缺失值和异常值\n")
        f.write("2. **深度分析**: 基于发现的模式进行更深入的统计测试\n")
        f.write("3. **可视化**: 创建图表以更好地展示数据模式\n")
        f.write("4. **建模准备**: 基于相关性分析结果准备特征工程\n")
        f.write("5. **业务洞察**: 将统计发现转化为实际的教育政策建议\n\n")

        f.write("---\n")
        f.write("*报告生成时间: 2025-10-02*\n")
        f.write("*分析工具: Python pandas, numpy, scipy*\n")

    print(f"详细分析报告已保存: {report_file}")
    print("\n分析完成！所有结果已保存到 analysis_reports 目录。")

if __name__ == "__main__":
    main()