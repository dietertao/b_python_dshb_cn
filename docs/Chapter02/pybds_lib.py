#coding:utf-8 

# import modules for data science 
import numpy as np


def describe_array(arr):
    """
    计算Numpy数组的基本统计信息
    输入：
    arr: Numpy数组
    输出：
    summary: dict, 一个包含导入Numpy数组的统计信息的字典
    """
    
    if not isinstance(arr, np.ndarray):
        raise ValueError("Input must be a numpy array.")
        return None
    
    #create a dict to store the statistical values
    summary = {}
    
    #下面的统计计算都使用针对有缺失值nan存在的数组的方法，如果没有缺失值，可以直接使用np.mean等方法 
    # 计算统计信息并存储在字典中
    
    summary["Size"] = arr.size
    summary['dtype'] = arr.dtype  # 数据类型
    summary['Shape'] = arr.shape  # 数组形状
    summary['Memory_usage'] = arr.nbytes  # 内存使用量（字节）
    
    # 计算数组元素的数值有效性：缺失值+非无限值  
    summary['NaN_count'] = np.isnan(arr).sum()  # 缺失值数量
    summary['finite_count'] = np.isfinite(arr).sum()  # 有效值数量 
    
    summary['Mean'] = np.nanmean(arr)  # 均值
    summary['Median'] = np.nanmedian(arr)  # 中值    
    summary['Min'] = np.nanmin(arr)  # 最小值
    summary['Max'] = np.nanmax(arr)  # 最大值
    summary['Range'] = np.nanmax(arr) - np.nanmin(arr)  # 极差 
    summary['Std'] = np.nanstd(arr)  # 标准差
    summary['Var'] = np.nanvar(arr)  # 方差
    summary['Skewness'] = np.nanmean((arr-np.nanmean(arr))**3 / (np.nanstd(arr)**3))  # 偏度
    summary['Kurtosis'] = np.nanmean((arr-np.nanmean(arr))**4 / (np.nanstd(arr)**4))  # 峰度
    

    return summary