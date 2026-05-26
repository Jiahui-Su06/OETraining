import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import time
from sklearn.metrics import mean_squared_error
import os


def load_data():
    """加载原始数据"""
    df = pd.read_excel('data/m5spec.xlsx', sheet_name='Sheet1', index_col=0)
    return df


def evaluate_preprocessing():
    """评估三种预处理方法的性能"""
    # 加载数据
    df = load_data()
    wavelengths = df.columns.astype(float)
    
    # 创建结果存储字典
    results = {
        '指数平滑': {'snr': [], 'smoothness': [], 'feature_preservation': [], 'time': []},
        'SNV标准化': {'snr': [], 'smoothness': [], 'feature_preservation': [], 'time': []},
        'Savitzky-Golay': {'snr': [], 'smoothness': [], 'feature_preservation': [], 'time': []}
    }
    
    # 对每个样本进行评估
    for sample_number, row in df.iterrows():
        original_data = row.values
        
        # 1. 指数平滑评估
        start_time = time.time()
        smoothed_data = exponential_smoothing(row, alpha=0.24)
        results['指数平滑']['time'].append(time.time() - start_time)
        results['指数平滑']['snr'].append(calculate_snr(smoothed_data, original_data - smoothed_data))
        results['指数平滑']['smoothness'].append(calculate_smoothness(smoothed_data))
        results['指数平滑']['feature_preservation'].append(calculate_feature_preservation(original_data, smoothed_data))
        
        # 2. SNV评估
        start_time = time.time()
        snv_data = snv_normalize(original_data)
        results['SNV标准化']['time'].append(time.time() - start_time)
        results['SNV标准化']['snr'].append(calculate_snr(snv_data, original_data - snv_data))
        results['SNV标准化']['smoothness'].append(calculate_smoothness(snv_data))
        results['SNV标准化']['feature_preservation'].append(calculate_feature_preservation(original_data, snv_data))
        
        # 3. Savitzky-Golay评估
        start_time = time.time()
        sg_data = savgol_filter(original_data, window_length=65, polyorder=3, deriv=1)
        results['Savitzky-Golay']['time'].append(time.time() - start_time)
        results['Savitzky-Golay']['snr'].append(calculate_snr(sg_data, original_data - sg_data))
        results['Savitzky-Golay']['smoothness'].append(calculate_smoothness(sg_data))
        results['Savitzky-Golay']['feature_preservation'].append(calculate_feature_preservation(original_data, sg_data))
    
    # 计算平均结果
    summary = {}
    for method in results:
        summary[method] = {
            '平均信噪比(dB)': np.mean(results[method]['snr']),
            '平均平滑度': np.mean(results[method]['smoothness']),
            '平均特征保持度': np.mean(results[method]['feature_preservation']),
            '平均处理时间(秒)': np.mean(results[method]['time'])
        }
    
    # 创建比较图表
    metrics = ['平均信噪比(dB)', '平均平滑度', '平均特征保持度', '平均处理时间(秒)']
    methods = list(summary.keys())
    
    plt.figure(figsize=(15, 10))
    for i, metric in enumerate(metrics, 1):
        plt.subplot(2, 2, i)
        values = [summary[method][metric] for method in methods]
        plt.bar(methods, values)
        plt.title(metric)
        plt.xticks(rotation=45)
        plt.tight_layout()
    
    # 保存结果
    output_dir = 'preprocessing_evaluation'
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, '预处理方法比较.png'))
    plt.close()
    
    # 保存数值结果到CSV
    summary_df = pd.DataFrame(summary).T
    summary_df.to_csv(os.path.join(output_dir, '预处理评估指标.csv'))
    
    # 打印结果
    print("\n预处理方法性能比较：")
    print("=" * 80)
    for method in summary:
        print(f"\n{method}:")
        for metric, value in summary[method].items():
            print(f"{metric}: {value:.4f}")
    
    return summary

if __name__ == "__main__":
    evaluate_preprocessing()