# Copyright (c) 2025 WangYibo <xtwyb@163.com>
# 本代码采用 CC BY-NC-SA 4.0 协议，禁止商业用途（作者授权除外）
# 详情参见项目根目录 LICENSE 文件
# 编写日期: 2025-04-04
# 代码描述: 归并排序

# 算法思想：
# 归并排序是一种典型的分而治之策略的排序算法。
# 基本思想是将序列不断二分拆分，直至每个子序列只含一个元素，然后再逐步合并，
# 合并过程中按照排序规则有序地归并成最终有序序列。

# 算法步骤：
# 1. 将待排序数组从中间划分成两半。
# 2. 递归地对左半部分进行归并排序。
# 3. 递归地对右半部分进行归并排序。
# 4. 将排好序的左右两部分归并为一个有序数组。

# 时间复杂度分析：
# - 每次划分数组的时间复杂度为 O(log n)，
# - 每一层合并的时间为 O(n)，
# - 所以总时间复杂度为 O(n log n)。

# 空间复杂度分析：
# - 合并过程中需要额外空间存放临时数组，空间复杂度为 O(n)。

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class MergeSortVisualizer:
    """
    归并排序可视化类，提供分治策略排序及动画演示功能。
    """
    def __init__(self, data):
        self.data = list(data)
        self.frames = []
        self._merge_sort(self.data, 0, len(self.data) - 1)

    def _merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            # 添加拆分前的状态
            self.frames.append((arr.copy(), left, mid, right, 'split'))
            self._merge_sort(arr, left, mid)
            self._merge_sort(arr, mid + 1, right)
            self._merge(arr, left, mid, right)

    def _merge(self, arr, left, mid, right):
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                self.frames.append((arr.copy(), k, left + i, 'merge'))
                i += 1
            else:
                arr[k] = R[j]
                self.frames.append((arr.copy(), k, mid + 1 + j, 'merge'))
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            self.frames.append((arr.copy(), k, left + i, 'merge'))
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            self.frames.append((arr.copy(), k, mid + 1 + j, 'merge'))
            j += 1
            k += 1

        # 添加合并后的状态
        self.frames.append((arr.copy(), left, mid, right, 'merged'))

    def _update(self, frame_data, ax):
        if len(frame_data) == 5:
            # 拆分或合并后的状态
            frame, left, mid, right, action = frame_data
            ax.clear()
            bars = ax.bar(range(len(frame)), frame, color=['blue'] * len(frame))
            for i in range(left, mid + 1):
                bars[i].set_color('green')  # 左子数组
            for i in range(mid + 1, right + 1):
                bars[i].set_color('orange')  # 右子数组
            ax.set_ylim(0, max(self.data) + 1)
            ax.set_title(f'Step: {len(self.frames)} - {action.upper()}')
        else:
            # 合并过程中的状态
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
        fig, ax = plt.subplots()
        ani = animation.FuncAnimation(fig, self._update, frames=self.frames, fargs=(ax,), interval=500, repeat=False)
        plt.show()

if __name__ == "__main__":
    data = np.random.randint(1, 20, 10)
    sorter = MergeSortVisualizer(data)
    sorter.animate()