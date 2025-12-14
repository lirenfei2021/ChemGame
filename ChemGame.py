#
# 文件名: ChemGame.py
# 项目: 化学离子风暴卡牌游戏
# 功能: 作为库, 包含程序所需函数
# 作者: @lirenfei2021
# 创建日期: 2025/11/28
# 最后修改日期: 2025/12/14
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
    def add(self, card, num=1):
        if num < 0 or num % 1 != 0:
            raise ValueError("Enter a positive integer.")
        try:
            if self.cards[card] + num > t.initCard[card]:
                raise ValueError(f"Not enough \"{card}\".")
            self.cards[card] += num
        except KeyError:
            raise KeyError(f"No card called \"{card}\".")
        return self.cards[card]
    def subtract(self, card, num=1):
        if num < 0 or num % 1 != 0:
            raise ValueError("Enter a positive integer.")
        try:
            if self.cards[card] - num < 0:
                raise ValueError(f"Not enough \"{card}\".")
            self.cards[card] -= num
        except KeyError:
            raise KeyError(f"No card called \"{card}\".")
        return self.cards[card]
    @property
    def randomCard(self):
        tmp = []
        for i in dict(self.cards):
            for j in range(self.cards[i]):
                tmp.append(i)
        return random.choice(tmp)
        

class Table(Card):
    sod = {}
    gas = {}
    we = {}
    def __init__(self):
        for i in list(t.Ion):
            self.cards[i] = 0
    def reaction(self, card, enough=False):
        if enough:
            ic = self.cards[card]
            self.cards[card] = 114514
        tmp = 0
        if card in list(t.Cation):
            re = t.Anion
            cat = True
        elif card in list(t.Anion):
            re = t.Cation
            cat = False
        elif card in list(t.initCard):
            raise TypeError(f"\"{card}\" is not an ion.")
            return 0
        else:
            raise KeyError(f"￼No card called \"{card}\".")
            return 0
        for i in t.toS[card]:
            while (self.cards[i] >= t.Balance[card][i][1]
                and self.cards[card] >= t.Balance[card][i][0]):
                self.cards[i] -= t.Balance[card][i][1]
                self.cards[card] -= t.Balance[card][i][0]
                if cat:
                    try:
                        self.sod[(card, i)] += 1
                    except KeyError:
                        self.sod[(card, i)] = 1
                else:
                    try:
                        self.sod[(i, card)] += 1
                    except KeyError:
                        self.sod[(i, card)] = 1
                tmp += 1
        for i in t.toG[card]:
            while (self.cards[i] >= t.Balance[card][i][1]
                and self.cards[card] >= t.Balance[card][i][0]):
                self.cards[i] -= t.Balance[card][i][1]
                self.cards[card] -= t.Balance[card][i][0]
                if cat:
                    try:
                        self.gas[(card, i)] += 1
                    except:
                        self.gas[(card, i)] = 1
                else:
                    try:
                        self.gas[(i, card)] += 1
                    except:
                        self.gas[(i, card)] = 1
                tmp += 1
        for i in t.toWE[card]:
            while (self.cards[i] >= t.Balance[card][i][1]
                and self.cards[card] >= t.Balance[card][i][0]):
                self.cards[i] -= t.Balance[card][i][1]
                self.cards[card] -= t.Balance[card][i][0]
                if cat:
                    try:
                        self.we[(card, i)] += 1
                    except KeyError:
                        self.we[(card, i)] = 1
                else:
                    try:
                        self.we[(i, card)] += 1
                    except KeyError:
                        self.we[(i, card)] = 1
                tmp += 1
        for i in t.toSS[card]:
            while (self.cards[i] >= 2 * t.Balance[card][i][1]
                and self.cards[card] >= 2 * t.Balance[card][i][0]):
                self.cards[i] -= t.Balance[card][i][1]
                self.cards[card] -= t.Balance[card][i][0]
                if cat:
                    try:
                        self.sod[(card, i)] += 1
                    except KeyError:
                        self.sod[(card, i)] = 1
                else:
                    try:
                        self.sod[(i, card)] += 1
                    except KeyError:
                        self.sod[(i, card)] = 1
                tmp += 1
        for i in t.toNE[card]:
            while (self.cards[i] >= t.Balance[card][i][1]
                and self.cards[card] >= t.Balance[card][i][0]):
                self.cards[i] -= t.Balance[card][i][1]
                self.cards[card] -= t.Balance[card][i][0]
                tmp += 1
        if enough:
            self.cards[card] = ic
        return (tmp + 1) // 2
