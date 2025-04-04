# Copyright (c) 2025 WangYibo <xtwyb@163.com>
# 本代码采用 CC BY-NC-SA 4.0 协议，禁止商业用途（作者授权除外）
# 详情参见项目根目录 LICENSE 文件
# 编写日期: 2025-04-04
# 代码描述: 插入排序

# 算法思想：
# 插入排序是一种构建有序序列的方法，通过逐步将未排序元素插入到已排序部分。
# 每次迭代，从未排序部分取出一个元素，在已排序部分找到合适位置并插入。
#
# 算法步骤：
# 1. 从第二个元素（索引1）开始，将其视为当前待插入元素。
# 2. 向前遍历已排序部分，找到合适的位置，将待插入元素插入。
# 3. 如果前一个元素比当前元素大，则向右移动前一个元素。
# 4. 重复此过程，直到找到适当位置或遍历结束。
# 5. 插入当前元素，继续下一轮迭代，直到所有元素排序完成。
#
# 时间复杂度计算：
# 在最坏情况下（逆序排列），外层循环执行 n-1 次，内层循环执行 1+2+...+(n-1) 次，
# 因此总的比较次数为：
# (n-1) + (n-2) + ... + 1 = n(n-1)/2 ≈ O(n^2)
#
# 最好情况下（已排序），每个元素仅比较一次，因此最好时间复杂度为 O(n)
#
# 平均情况下，时间复杂度约为 O(n^2)
#
# 空间复杂度计算：
# 插入排序是原地排序，仅使用少量额外变量，空间复杂度为 O(1)。

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class InsertionSortVisualizer:
    """
    插入排序可视化类，提供排序及动画演示功能。
    """
    def __init__(self, data):
        self.data = list(data)  # 复制数据，避免修改原始数据
        self.frames = []  # 存储每一帧的数据和高亮索引
        self._insertion_sort()
    
    def _insertion_sort(self):
        """
        执行插入排序，并记录排序过程。
        """
        arr = self.data.copy()
        n = len(arr)
        
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]  # 向右移动元素
                self.frames.append((arr.copy(), j, j + 1))  # 记录当前状态
                j -= 1
            
            arr[j + 1] = key  # 插入当前元素
            self.frames.append((arr.copy(), j + 1, i))  # 记录插入后的状态
    
    def _update(self, frame_data, ax):
        """
        更新动画帧，绘制当前排序状态。
        """
        frame, idx1, idx2 = frame_data
        ax.clear()
        bars = ax.bar(range(len(frame)), frame, color=['blue'] * len(frame))
        
        # 变色高亮当前比较的元素
        bars[idx1].set_color('red')
        bars[idx2].set_color('yellow')
        
        # 在柱子顶部加箭头标注
        ax.annotate('⬆', (idx1, frame[idx1]), ha='center', va='bottom', fontsize=12, color='red')
        ax.annotate('⬆', (idx2, frame[idx2]), ha='center', va='bottom', fontsize=12, color='red')
        
        ax.set_ylim(0, max(self.data) + 1)
    
    def animate(self):
        """
        运行动画，展示排序过程。
        """
        fig, ax = plt.subplots()
        ani = animation.FuncAnimation(fig, self._update, frames=self.frames, fargs=(ax,), interval=500, repeat=False)
        plt.show()

# 示例用法：
if __name__ == "__main__":
    data = np.random.randint(1, 20, 10)  # 生成随机数组
    sorter = InsertionSortVisualizer(data)
    sorter.animate()

