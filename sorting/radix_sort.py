# Copyright (c) 2025 WangYibo <xtwyb@163.com>
# 本代码采用 CC BY-NC-SA 4.0 协议，禁止商业用途（作者授权除外）
# 详情参见项目根目录 LICENSE 文件
# 编写日期: 2025-04-04
# 代码描述: 基数排序

# 算法思想：
# 基数排序是一种非比较型整数排序算法。
# 基本思想是通过逐位处理数字来进行排序。
# 它适用于整数排序，特别适用于数据范围较大的情况。
# 基数排序通常使用稳定排序算法（如计数排序）作为子过程。

# 算法步骤：
# 1. 找出最大值：确定数组中最大的元素，以便确定需要处理的最大位数。
# 2. 按位处理：从最低有效位（LSD）到最高有效位（MSD），依次对每一位进行排序。
# 3. 使用稳定排序算法：在每一步中使用稳定排序算法（如计数排序）对当前位进行排序。

# 时间复杂度分析：
# - 平均情况：O(d * (n + k))，其中 d 是数字的最大位数，n 是输入数组的大小，k 是基数（通常是 10）。
# - 最坏情况：O(d * (n + k))。
# - 最好情况：O(d * (n + k))。

# 空间复杂度分析：
# - 基数排序需要额外的空间来存储计数数组和输出数组，空间复杂度为 O(n + k)。

# 适用场景：
# - 数据是非负整数。
# - 数据范围较大但位数不是特别多。
# - 需要稳定的排序算法（即相同元素的相对顺序保持不变）。

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class RadixSortVisualizer:
    """
    基数排序可视化类，提供非比较型整数排序及动画演示功能。
    """
    def __init__(self, data):
        self.data = list(data)
        self.frames = []
        self._radix_sort(self.data)

    def _radix_sort(self, arr):
        """
        对数组进行基数排序，并记录排序过程中的状态。

        :param arr: 待排序的数组
        """
        if not arr:
            return

        # 找出数组中的最大值
        max_value = max(arr)
        exp = 1  # 从最低有效位开始

        while max_value // exp > 0:
            self._counting_sort(arr, exp)
            exp *= 10

    def _counting_sort(self, arr, exp):
        """
        对数组按指定位进行计数排序，并记录排序过程中的状态。

        :param arr: 待排序的数组
        :param exp: 当前处理的位数（1, 10, 100, ...）
        """
        n = len(arr)
        # 初始化计数数组
        count = [0] * 10
        # 初始化输出数组
        output = [0] * n

        # 统计每个元素在当前位上的数字出现的次数
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
            self.frames.append((arr.copy(), i, 'count'))

        # 累加计数数组
        for i in range(1, 10):
            count[i] += count[i - 1]
            self.frames.append((arr.copy(), i, 'accumulate'))

        # 构建输出数组
        for i in range(n - 1, -1, -1):
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            self.frames.append((output.copy(), i, 'build'))

        # 复制回原数组
        for i in range(n):
            arr[i] = output[i]
            self.frames.append((arr.copy(), i, 'copy'))

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
            if action == 'count':
                bars[idx].set_color('red')  # 标记当前操作的元素
            elif action == 'accumulate':
                bars[idx].set_color('orange')  # 标记累加计数的索引
            elif action == 'build':
                bars[idx].set_color('green')  # 标记构建输出数组的元素
            elif action == 'copy':
                bars[idx].set_color('purple')  # 标记复制回原数组的元素

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
    sorter = RadixSortVisualizer(data)
    sorter.animate()