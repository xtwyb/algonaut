# Copyright (c) 2025 WangYibo <xtwyb@163.com>
# 本代码采用 CC BY-NC-SA 4.0 协议，禁止商业用途（作者授权除外）
# 详情参见项目根目录 LICENSE 文件
# 编写日期: 2025-04-04
# 代码描述: 冒泡排序可视化类

# 算法思想：
# 冒泡排序是一种简单的排序算法，它通过重复遍历列表，逐步将最大元素移动到列表末尾。
# 每次遍历过程中，依次比较相邻元素，若顺序错误则交换，最终形成有序数组。
#
# 时间复杂度计算：
# 在最坏情况下（逆序排列），外层循环执行 n 次，内层循环执行 (n-1), (n-2), ..., 1 次，
# 因此总的比较次数为：
# (n-1) + (n-2) + ... + 1 = n(n-1)/2 ≈ O(n^2)
#
# 最好情况下（已排序），仍需执行 n 轮检查，因此最好时间复杂度仍然是 O(n^2)
#
# 空间复杂度计算：
# 仅使用了少量额外变量（如 `frames` 列表存储排序过程），但主排序过程是原地进行的，
# 空间复杂度为 O(n)（由于存储排序过程的多个状态，否则原算法的空间复杂度为 O(1)）。

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

class BubbleSort:
    '''
    冒泡排序可视化类，提供排序及动画演示功能
    '''
    def __init__(self, data):
        self.data = data
        self.frames=[] #存储每一帧的数据和高亮索引
        self._bubble_sort()
    
    def _bubble_sort(self):
        """
        执行冒泡排序，并记录排序过程。
        """
        arr = self.data.copy()
        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                self.frames.append((arr.copy(), j, j+1)) #记录当前状态和比较的索引
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j] #交换元素
                    self.frames.append((arr.copy(), j, j+1)) #记录交换后的状态

    def _update(self, frame_data,ax):
        '''
        更新动画帧，绘制当前排序状态
        '''
        frame,idx1,idx2 = frame_data
        ax.clear()
        bars=ax.bar(range(len(frame)), frame, color=['blue']*len(frame))

        #变色高亮当前比较的元素
        bars[idx1].set_color('red')
        bars[idx2].set_color('yellow')
        #在柱子顶部加星号标注
        ax.annotate('*',(idx1, frame[idx1]),ha='center', va='bottom',fontsize=12,color='red')
        ax.annotate('*',(idx2, frame[idx2]),ha='center', va='bottom',fontsize=12,color='red')

        ax.set_ylim(0, max(frame)+1)

    def animate(self):
        '''
        演示排序过程，并保存为gif动画
        '''
        fig, ax = plt.subplots()
        ani = animation.FuncAnimation(fig, self._update, frames=self.frames, fargs=(ax,), interval=500, repeat=False)
        # ani.save('bubble_sort.gif', writer='pillow', fps=2)
        plt.show()
        

# 示例用法：
if __name__ == "__main__":
    data = np.random.randint(1, 20, 10)  # 生成随机数组
    sorter = BubbleSort(data)
    sorter.animate()
