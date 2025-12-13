#
# 文件名: ChemGame.py
# 项目: 化学离子风暴卡牌游戏
# 功能: 作为库, 包含程序所需函数
# 作者: @lirenfei2021
# 创建日期: 2025/11/28
# 最后修改日期: 2025/12/13. 
#

import random
import table as t

# table.py 使用说明
# initCard: 初始牌数
# cardType: 卡牌类型, 阳离子为1, 阴离子为2, 特殊物质为0, 功能牌为3
# 气体 toG: toG[A] 为所有与 A 离子反应生成气体物质的离子组成的列表
# 沉淀 toS: toS[A] 为所有与 A 离子反应生成沉淀物质的离子组成的列表
# 微溶 toSS: toSS[A] 为所有与 A 离子反应生成微溶物质的离子组成的列表
# 弱电解质 toWE: toWE[A] 为所有与 A 离子反应生成弱电解质的离子组成的列表
# 不存在 toNE: toNE[A] 为所有与 A 离子反应生成不存在物质的离子组成的列表
# 电荷 Ele: Ele[A] 为 A 离子所带电荷 (带符号)
# 配平 Balance: 若 AB 组成的物质为 A_{a} B_{b}, 则 Balance[A][B] == [a, b]

class Card:
    cards = {}
    def __init__(self, init=False):
        self.cards = dict(t.initCard)
        if not init:
            for i in self.cards:
                self.cards[i] = 0
    def add(self, card, numbers=1):
        if numbers < 0 or numbers % 1 != 0:
            raise ValueError("Enter a positive integer.")
        try:
            self.cards[card] += numbers
            print(self.cards[card])
            print(t.initCard[card])
            if self.cards[card] > t.initCard[card]:
                raise ValueError
        except KeyError:
            raise KeyError(f"No card called \"{card}\".")
        except ValueError:
            raise ValueError(f"Not enough \"{card}\".")
        return self.cards[card]
    def subtract(self, card, numbers=1):
        if numbers < 0 or numbers % 1 != 0:
            raise ValueError("Enter a positive integer.")
        try:
            self.cards[card] -= numbers
            print(self.cards[card])
            print(t.initCard[card])
            if self.cards[card] > t.initCard[card]:
                raise ValueError
        except KeyError:
            raise KeyError(f"No card called \"{card}\".")
        except ValueError:
            raise ValueError(f"Not enough \"{card}\".")
        return self.cards[card]
    @property
    def randomCard(self):
        tmp = []
        for i in self.cards:
            for j in range(self.cards[i]):
                tmp.append(i)
        return random.choice(tmp)
