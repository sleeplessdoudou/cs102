import time

t0 = time.time()


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.available = []
        self.value = 0


def initPoint(sudoku):
    pointList = []
    length = len(sudoku)
    for i in range(length):
        if sudoku[i] == 0:
            p = point(i % 9, i // 9)
            for j in range(1, 10):
                if j not in getRow(p, sudoku) and j not in getCol(p, sudoku) and j not in getBlock(p, sudoku):
                    p.available.append(j)
            pointList.append(p)
    print(pointList)
    return pointList


#找出该行已存在的数字
def getRow(p, sudoku):
    row = set(sudoku[p.y * 9:(p.y + 1) * 9]) #这里将列表转为无序不重复的集合 该函数可返回整行，也可返回集合
    row.remove(0) #如果返回集合，将集合中的0去掉
    # row = sudoku[p.y * 9:(p.y + 1) * 9]
    # print("row:::::", row)
    # print("row1:::::", row1)
    return row


#找出该列已存在的数字
def getCol(p, sudoku):
    col = []
    length = len(sudoku)
    for i in range(p.x, length, 9):
        col.append(sudoku[i])
    col = set(col) #这里将列表转为无序不重复的集合 该函数可返回整列，也可返回集合
    col.remove(0)#如果返回集合，将集合中的0去掉
    # print(col)
    return col


#找出小九宫格内已存在的数字
def getBlock(p, sudoku):
    block_x = p.x // 3
    block_y = p.y // 3
    block = []
    start = block_y * 3 * 9 + block_x * 3  #计算小九宫格内三行的第一行的起始点
    for i in range(start, start + 3): #第一行
        block.append(sudoku[i])
    for i in range(start + 9, start + 9 + 3): #第二行
        block.append(sudoku[i])
    for i in range(start + 9 + 9, start + 9 + 9 + 3): #第三行
        block.append(sudoku[i])
    block = set(block) #将列表转为无序不重复的集合
    block.remove(0) #去掉0
    return block





def solveSudoku(p, sudoku):
    availNum = p.available
    for v in availNum:
        p.value = v
        if check(p, sudoku):
            sudoku[p.y * 9 + p.x] = p.value #将一个可能值赋予该格
            if len(pointList) <= 0:
                t1 = time.time()
                useTime = t1 - t0
                showSudoku(sudoku)
                print('\nuse Time: %f s' % (useTime))
                exit()
            p2 = pointList.pop()
            solveSudoku(p2, sudoku) #递归
            sudoku[p2.y * 9 + p2.x] = 0
            sudoku[p.y * 9 + p.x] = 0
            p2.value = 0
            pointList.append(p2)
        else:
            pass
        # showSudoku(sudoku)
        # print("")


def check(p, sudoku):
    if p.value == 0:
        print('not assign value to point p!!')
        return False
    if p.value not in getRow(p, sudoku) and p.value not in getCol(p, sudoku) and p.value not in getBlock(p, sudoku):
        return True
    else:
        return False


def showSudoku(sudoku):
    for j in range(9):
        for i in range(9):
            print('%d ' % (sudoku[j * 9 + i]), end='')
        print('')


if __name__ == '__main__':
    sudoku = [
        8, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 3, 6, 0, 0, 0, 0, 0,
        0, 7, 0, 0, 9, 0, 2, 0, 0,
        0, 5, 0, 0, 0, 7, 0, 0, 0,
        0, 0, 0, 0, 4, 5, 7, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 3, 0,
        0, 0, 1, 0, 0, 0, 0, 6, 8,
        0, 0, 8, 5, 0, 0, 0, 1, 0,
        0, 9, 0, 0, 0, 0, 4, 0, 0,
    ]
    pointList = initPoint(sudoku)
    showSudoku(sudoku)
    print('\n')
    p = pointList.pop()
    solveSudoku(p, sudoku)

