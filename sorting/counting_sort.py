# Copyright (c) 2025 WangYibo <xtwyb@163.com>
# 本代码采用 CC BY-NC-SA 4.0 协议，禁止商业用途（作者授权除外）
# 详情参见项目根目录 LICENSE 文件
# 编写日期: 2025-04-04
# 代码描述: 计数排序

# 算法思想：
# 计数排序是一种非比较型整数排序算法。
# 基本思想是通过计算每个元素在数组中出现的次数来确定每个元素在排序后数组中的位置。
# 计数排序适用于已知数据范围且数据范围不是特别大的情况。

# 算法步骤：
# 1. 找出最大值：确定数组中最大的元素，以便确定计数数组的大小。
# 2. 初始化计数数组：创建一个大小为 max_value + 1 的计数数组，初始值为 0。
# 3. 统计频率：遍历输入数组，统计每个元素出现的次数，并存储在计数数组中。
# 4. 累加计数：将计数数组转换为累加计数数组，这样每个元素的值表示该元素在排序后数组中的位置。
# 5. 构建输出数组：根据累加计数数组，将输入数组中的元素放到正确的位置上。
# 6. 复制回原数组：将排序后的结果复制回原数组。

# 时间复杂度分析：
# - 平均情况：O(n + k)，其中 n 是输入数组的大小，k 是数据范围。
# - 最坏情况：O(n + k)。
# - 最好情况：O(n + k)。

# 空间复杂度分析：
# - 计数排序需要额外的空间来存储计数数组，空间复杂度为 O(k)。

# 适用场景：
# - 数据范围较小且已知。
# - 数据是非负整数。
# - 需要稳定的排序算法（即相同元素的相对顺序保持不变）。
# - 对时间复杂度要求较高，且数据范围不是特别大。

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class CountingSortVisualizer:
    """
    计数排序可视化类，提供非比较型整数排序及动画演示功能。
    """
    def __init__(self, data):
        self.data = list(data)
        self.frames = []
        self._counting_sort(self.data)

    def _counting_sort(self, arr):
        """
        对数组进行计数排序，并记录排序过程中的状态。

        :param arr: 待排序的数组
        """
        if not arr:
            return

        # 找出数组中的最大值
        max_value = max(arr)
        # 初始化计数数组
        count = [0] * (max_value + 1)
        # 初始化输出数组
        output = [0] * len(arr)

        # 统计每个元素出现的次数
        for i, num in enumerate(arr):
            count[num] += 1
            self.frames.append((arr.copy(), i, 'count'))  # 传索引 i，而不是数值 num

        # 累加计数数组
        for i in range(1, len(count)):
            count[i] += count[i - 1]
            self.frames.append((arr.copy(), i, 'accumulate'))

        # 构建输出数组
        for i in range(len(arr) - 1, -1, -1):  # 逆序遍历以保持稳定性
            num = arr[i]
            output[count[num] - 1] = num
            count[num] -= 1
            self.frames.append((output.copy(), i, 'build'))  # 传索引 i，而不是数值 num

        # 复制回原数组
        for i in range(len(arr)):
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
    data = np.random.randint(1, 20, 10)  # 生成 10 个随机整数
    sorter = CountingSortVisualizer(data)
    sorter.animate()
