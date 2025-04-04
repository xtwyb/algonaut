# Copyright (c) 2025 WangYibo <xtwyb@163.com>
# 本代码采用 CC BY-NC-SA 4.0 协议，禁止商业用途（作者授权除外）
# 详情参见项目根目录 LICENSE 文件
# 编写日期: 2025-04-04
# 代码描述: 快速排序

# 算法思想：
# 快速排序是一种分而治之的排序算法。
# 基本思想是通过一个“基准”元素将数组分成两部分，使得左边部分的所有元素都小于基准元素，
# 右边部分的所有元素都大于基准元素，然后递归地对这两部分进行排序。

# 算法步骤：
# 1. 从数组中选择一个基准元素（pivot）。
# 2. 重新排列数组，所有比基准元素小的元素摆放在基准前面，所有比基准元素大的元素摆放在基准后面。
# 3. 递归地对基准前后的子数组进行快速排序。

# 时间复杂度分析：
# - 平均情况下，时间复杂度为 O(n log n)。
# - 最坏情况下（例如，每次选择的基准都是最大或最小元素），时间复杂度为 O(n^2)。

# 空间复杂度分析：
# - 快速排序是原地排序算法，空间复杂度为 O(log n)（递归调用栈的空间）。

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class QuickSortVisualizer:
    """
    快速排序可视化类，提供分治策略排序及动画演示功能。
    """
    def __init__(self, data):
        self.data = list(data)
        self.frames = []
        self._quick_sort(self.data, 0, len(self.data) - 1)

    def _quick_sort(self, arr, low, high):
        """
        递归地对数组进行快速排序，并记录排序过程中的状态。

        :param arr: 待排序的数组
        :param low: 数组的起始索引
        :param high: 数组的结束索引
        """
        if low < high:
            # 获取分区点
            pi = self._partition(arr, low, high)
            # 添加分区后的状态
            self.frames.append((arr.copy(), low, high, pi, 'partitioned'))
            # 递归地对左子数组进行快速排序
            self._quick_sort(arr, low, pi - 1)
            # 递归地对右子数组进行快速排序
            self._quick_sort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        """
        对数组进行分区，并记录交换过程中的状态。

        :param arr: 待分区的数组
        :param low: 数组的起始索引
        :param high: 数组的结束索引
        :return: 分区点的索引
        """
        pivot = arr[high]  # 选择最后一个元素作为基准
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                # 添加交换后的状态
                self.frames.append((arr.copy(), i, j, 'swap'))
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        # 添加交换后的状态
        self.frames.append((arr.copy(), i + 1, high, 'swap'))
        return i + 1

    def _update(self, frame_data, ax):
        """
        更新动画帧，绘制当前排序状态。

        :param frame_data: 当前帧的数据
        :param ax: Matplotlib 的 Axes 对象
        """
        if len(frame_data) == 5:
            # 分区后的状态
            frame, low, high, pi, action = frame_data
            ax.clear()
            bars = ax.bar(range(len(frame)), frame, color=['blue'] * len(frame))
            for i in range(low, high + 1):
                bars[i].set_color('green')  # 分区范围
            bars[pi].set_color('red')  # 分区点
            # 添加星号标记
            ax.annotate('*', (pi, frame[pi]), ha='center', va='bottom', fontsize=12, color='brown')
            ax.set_ylim(0, max(self.data) + 1)
            ax.set_title(f'Step: {len(self.frames)} - {action.upper()}')
        else:
            # 交换过程中的状态
            frame, idx1, idx2, action = frame_data
            ax.clear()
            bars = ax.bar(range(len(frame)), frame, color=['blue'] * len(frame))
            bars[idx1].set_color('red')
            bars[idx2].set_color('yellow')
            ax.annotate('⬆', (idx1, frame[idx1]), ha='center', va='bottom', fontsize=12, color='red')
            ax.annotate('⬆', (idx2, frame[idx2]), ha='center', va='bottom', fontsize=12, color='red')
            ax.set_ylim(0, max(self.data) + 1)
            ax.set_title(f'Step: {len(self.frames)} - {action.upper()}')

    def animate(self):
        """
        运行动画，展示排序过程。
        """
        fig, ax = plt.subplots()
        ani = animation.FuncAnimation(fig, self._update, frames=self.frames, fargs=(ax,), interval=500, repeat=False)
        plt.show()

if __name__ == "__main__":
    data = np.random.randint(1, 20, 10)
    sorter = QuickSortVisualizer(data)
    sorter.animate()