Q:
3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
给定一个由整数组成的 N × N 矩阵，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。
A:
遍历矩阵， 判断每个元素为首的3 x 3单元是否为幻方。判断依据就是题中的条件。
另外也可以观察幻方得出其他的限定条件：
幻方的中心必须是5。
其他8个数字：偶数必须在角落，奇数必须在边缘。
它必须按“43816729”（顺时针或逆时针）的顺序排列
这样可以用下面代码解决：
def numMagicSquaresInside(self, grid):
        def isMagic(i, j):
		#s是表示取方阵中的按照顺时针取边缘数据。
            s = "".join(str(g[i + x // 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return g[i][j] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)
        return sum(isMagic(i, j) for i in range(len(g) - 2) for j in range(len(g[0]) - 2) if g[i + 1][j + 1] == 5)