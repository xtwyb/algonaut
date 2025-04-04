# Copyright (c) 2025 WangYibo <xtwyb@163.com>
# 本代码采用 CC BY-NC-SA 4.0 协议，禁止商业用途（作者授权除外）
# 详情参见项目根目录 LICENSE 文件
# 编写日期: 2025-04-04
# 代码描述: 桶排序

# 算法思想：
# 桶排序是一种分而治之的排序算法，适用于数据均匀分布的情况。
# 基本思想是将数据分配到不同的桶中，然后对每个桶分别进行排序（通常使用插入排序），最后合并所有桶中的元素。

# 算法步骤：
# 1. 确定桶的数量：根据数据范围和数据量确定桶的数量。
# 2. 分配到桶中：将数据分配到相应的桶中。
# 3. 排序每个桶：对每个桶中的元素进行排序（通常使用插入排序）。
# 4. 合并桶：将所有桶中的元素合并成一个有序数组。

# 时间复杂度分析：
# - 平均情况：O(n + k)，其中 n 是输入数组的大小，k 是桶的数量。
# - 最坏情况：O(n^2)（当所有元素分配到同一个桶中时）。
# - 最好情况：O(n + k)。

# 空间复杂度分析：
# - 桶排序需要额外的空间来存储桶，空间复杂度为 O(n + k)。

# 适用场景：
# - 数据均匀分布。
# - 数据是非负整数或浮点数。
# - 对时间复杂度要求较高，且数据范围不是特别大。

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class BucketSortVisualizer:
    """
    桶排序可视化类，提供分而治之排序及动画演示功能。
    """
    def __init__(self, data):
        self.data = list(data)
        self.frames = []
        self._bucket_sort(self.data)

    def _bucket_sort(self, arr):
        """
        对数组进行桶排序，并记录排序过程中的状态。

        :param arr: 待排序的数组
        """
        if not arr:
            return

        # 找出数组中的最大值和最小值
        min_value = min(arr)
        max_value = max(arr)
        n = len(arr)

        # 确定桶的数量
        num_buckets = int(np.sqrt(n))
        buckets = [[] for _ in range(num_buckets)]

        # 分配到桶中
        for num in arr:
            index = int((num - min_value) / (max_value - min_value) * (num_buckets - 1))
            buckets[index].append(num)
            self.frames.append((arr.copy(), num, 'bucket'))

        # 对每个桶进行插入排序
        for i in range(num_buckets):
            self._insertion_sort(buckets[i])
            for num in buckets[i]:
                self.frames.append((arr.copy(), num, 'sort'))

        # 合并桶
        sorted_index = 0
        for bucket in buckets:
            for num in bucket:
                arr[sorted_index] = num
                sorted_index += 1
                self.frames.append((arr.copy(), sorted_index - 1, 'merge'))

    def _insertion_sort(self, arr):
        """
        对数组进行插入排序，并记录排序过程中的状态。

        :param arr: 待排序的数组
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def _update(self, frame_data, ax):
        """
        更新动画帧，绘制当前排序状态。

        :param frame_data: 当前帧的数据
        :param ax: Matplotlib 的 Axes 对象
        """
        frame, idx, action = frame_data
        ax.clear()
        bars = ax.bar(range(len(frame)), frame, color=['blue'] * len(frame))

        if 0 <= idx < len(bars):  # 确保 idx 在 bars 可访问范围内
            if action == 'bucket':
                bars[idx].set_color('red')  # 标记分配到桶中的元素
            elif action == 'sort':
                bars[idx].set_color('orange')  # 标记桶内排序的元素
            elif action == 'merge':
                bars[idx].set_color('green')  # 标记合并桶中的元素

        ax.set_ylim(0, max(self.data) + 1)
        ax.set_title(f'Step: {len(self.frames)} - {action.upper()}')

    def _init_draw(self, ax):
        """
        初始化动画帧。

        :param ax: Matplotlib 的 Axes 对象
        """
        ax.clear()
        bars = ax.bar(range(len(self.data)), self.data, color=['blue'] * len(self.data))
        ax.set_ylim(0, max(self.data) + 1)
        ax.set_title('Step: 0 - INIT')
        return bars

    def animate(self):
        """
        运行动画，展示排序过程。
        """
        fig, ax = plt.subplots()
        ani = animation.FuncAnimation(fig, self._update, frames=self.frames, 
                                      init_func=lambda: self._init_draw(ax), 
                                      fargs=(ax,), interval=500, repeat=False)
        plt.show()

if __name__ == "__main__":
    data = np.random.randint(1, 200, 10)  # 生成 10 个随机整数，范围在 1 到 200 之间
    sorter = BucketSortVisualizer(data)
    sorter.animate()