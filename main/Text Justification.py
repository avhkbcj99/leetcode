"""
给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

注意:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。


示例 1:

输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


提示:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] 由小写英文字母和符号组成
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []  # 当前行的单词列表
        curr_width = 0  # 当前行的宽度（不包括单词之间的空格）

        for word in words:
            # 如果加上当前单词的宽度超过了maxWidth，则将当前行的单词进行排版
            if curr_width + len(line) + len(word) > maxWidth:
                # 计算当前行的空格总数和单词之间的平均空格数
                total_spaces = maxWidth - curr_width
                num_words = len(line)

                # 特殊情况处理：当前行只有一个单词，或者是最后一行（左对齐）
                if num_words == 1 or len(line) == 0:
                    result.append(line[0] + ' ' * (maxWidth - curr_width))
                else:
                    # 计算单词之间的额外空格数和左边的空格数
                    spaces_between_words = total_spaces // (num_words - 1)
                    extra_spaces = total_spaces % (num_words - 1)

                    # 构造当前行的文本
                    curr_line = ''
                    for i in range(num_words - 1):
                        curr_line += line[i] + ' ' * spaces_between_words
                        if i < extra_spaces:
                            curr_line += ' '
                    curr_line += line[-1]  # 添加最后一个单词

                    result.append(curr_line)

                # 重置当前行的变量
                line = [word]
                curr_width = len(word)
            else:
                line.append(word)
                curr_width += len(word)

        # 处理最后一行（左对齐）
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result