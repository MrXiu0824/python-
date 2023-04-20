"""
exec-1
给出两个有序的链表L1,L2 .
在不创建新的链表的基础上将两个链表合并为一个
要求合并后的链表仍为有序
"""

from num_tow.shujujiegou.link_list import *
from num_tow.shujujiegou.link_sstack import *
from num_tow.shujujiegou.link_queue import *


class Exex1:
    # 创建两个链表,初始化数值
    L1 = LinkList()
    L2 = LinkList()

    L1.init_list([1, 5, 7, 8, 10, 12, 13, 19])
    L2.init_list([0, 3, 4, 8, 14, 21, 22])

    L1.show()
    print("=========================")
    L2.show()

    def merge(L1, L2):
        # 将L2向L1中合并
        p = L1.head
        q = L2.head.next
        while p.next is not None:
            if p.next.val < q.val:
                p = p.next
            else:
                tmp = p.next
                p.next = q
                p = p.next
                q = tmp

        p.next = q

    merge(L1, L2)
    print("=================================")
    L1.show()


"""
exec-2
逆波兰表达式实现
"""


class Exec2:
    st = LinkSstack()

    while True:
        exp = input()
        tmp = exp.split(' ')  # 按照空格切割字符串
        for i in tmp:
            if i not in ['+', '-', '*', '/', 'p']:
                st.push(float(i))
            elif i == '+':
                y = st.pop()
                x = st.pop()
                st.push(x + y)
            elif i == '-':
                y = st.pop()
                x = st.pop()
                st.push(x - y)
            elif i == '*':
                y = st.pop()
                x = st.pop()
                st.push(x * y)
            elif i == '/':
                y = st.pop()
                x = st.pop()
                st.push(x / y)
            elif i == 'p':
                print(st.top())


"""
exec-3
创建一个顺序队列, 队列中入队一组值
将队列中的值反转过来(值的个数不确定).
比如:[1,2,3,4,5]-->[5,4,3,2,1]
"""


class Exec3:
    sq = LinkQueue()
    for i in range(8):
        sq.enqueue(i)

    # 完成队列反转
    ls = LinkSstack()
    # 出队 入栈
    while not sq.is_empty():
        ls.push(sq.dequeue())

    # 出栈 入队
    while not ls.is_empty():
        sq.enqueue(ls.pop())

    while not sq.is_empty():
        print(sq.dequeue())


"""
exec-4
编写一个接口程序,要求判断一段文字中括号匹配是否正确,
如果正确则打印"匹配正确",如果不正确则打印出哪里出错(只需要找出第一个错误即可)

出错情况 : 少前括号,少后括号,括号不匹配
"""
from link_sstack import *


class Exec4:

    # 先定义好验证条件
    def __init__(self):
        self.text = "When an Open Data (standard) is created and promoted, it’s [important ]to think why - what change is th=is {trying (to] drive}? What will people do with this data that they couldn’t do before?"
        self.ls = LinkSstack()  # 初始化一个栈 用来存储左括号
        self.parens = "()[]{}"  # 关注字符
        self.left_parens = "([{"  # 入栈的字符
        self.opposite = {')': '(', ']': '[', '}': '{'}  # 匹配原则

    # 编写生成器,用来遍历字符串,不断的提供括号及位置
    def parent(self):
        # 通过开两个变量记录字符和字符位置
        i, text_len = 0, len(self.text)

        # 开始遍历字符串
        while True:
            while i < text_len and self.text[i] not in self.parens:
                i += 1

            # 判定因为什么结束上一个循环
            if i >= text_len:
                return
            else:
                yield i, self.text[i]  # 提供位置和括号字符
                i += 1

    # 验证过程封装位函数
    def ver(self):
        for i, c in self.parent(self.text):
            if c in self.left_parens:
                self.ls.push((i, c))  # 入栈一个元组
            # 遇到了右括号
            elif self.ls.is_empty() or self.ls.pop()[1] != self.opposite[c]:
                print("Unmatch is found at %d for %s" % (i, c))
                break
        else:
            if self.ls.is_empty():
                print("All parens is matched")
            else:
                # 左括号多了 (i,c)
                print("Unmatch is found at %d for %s" % self.ls.pop())

    ver()

"""
从终端输入一个单词,
可以打印出单词及其解释,
如果没有这个单词则打印 "没有该单词
"""

# word = input("Word:")  # 要查找的单词
#
# # 打开文件 'r'
# f = open('dict.txt')
#
# # 每次获取一行
# for line in f:
#     w = line.split(' ')[0]
#     # 如果遍历到的单词已经大于目标,就结束查找
#     if w > word:
#         print("没有找到该单词")
#         break
#     elif w == word:
#         print(line)
#         break
# else:
#     print("没有找到单词")
#
# f.close()

