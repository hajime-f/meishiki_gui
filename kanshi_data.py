kan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸',]
shi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥',]

setsuiri = [6, 4, 6, 5, 6, 6, 7, 8, 8, 9, 8, 7]

sixty_kanshi = [
    [0, 0,],
    [1, 1,],
    [2, 2,],
    [3, 3,],
    [4, 4,],
    [5, 5,],
    [6, 6,],
    [7, 7,],
    [8, 8,],
    [9, 9,],
    [0, 10,],
    [1, 11,],
    [2, 0,],
    [3, 1,],
    [4, 2,],
    [5, 3,],
    [6, 4,],
    [7, 5,],
    [8, 6,],
    [9, 7,],
    [0, 8,],
    [1, 9,],
    [2, 10,],
    [3, 11,],
    [4, 0,],
    [5, 1,],
    [6, 2,],
    [7, 3,],
    [8, 4,],
    [9, 5,],
    [0, 6,],
    [1, 7,],
    [2, 8,],
    [3, 9,],
    [4, 10,],
    [5, 11,],
    [6, 0,],
    [7, 1,],
    [8, 2,],
    [9, 3,],
    [0, 4,],
    [1, 5,],
    [2, 6,],
    [3, 7,],
    [4, 8,],
    [5, 9,],
    [6, 10,],
    [7, 11,],
    [8, 0,],
    [9, 1,],
    [0, 2,],
    [1, 3,],
    [2, 4,],
    [3, 5,],
    [4, 6,],
    [5, 7,],
    [6, 8,],
    [7, 9,],
    [8, 10,],
    [9, 11,],
]

month_kanshi = [
    [ [3, 1,],  # 甲
      [2, 2,],
      [3, 3,],
      [4, 4,],
      [5, 5,],
      [6, 6,],
      [7, 7,],
      [8, 8,],
      [9, 9,],
      [0, 10,],
      [1, 11,],
      [2, 0,], ],
    [ [5, 1,],  # 乙
      [4, 2,],
      [5, 3,],
      [6, 4,],
      [7, 5,],
      [8, 6,],
      [9, 7,],
      [0, 8,],
      [1, 9,],
      [2, 10,],
      [3, 11,],
      [4, 0,], ],
    [ [7, 1,],  # 丙
      [6, 2,],
      [7, 3,],
      [8, 4,],
      [9, 5,],
      [0, 6,],
      [1, 7,],
      [2, 8,],
      [3, 9,],
      [4, 10,],
      [5, 11,],
      [6, 0,], ],
    [ [9, 1,],  # 丁
      [8, 2,],
      [9, 3,],
      [0, 4,],
      [1, 5,],
      [2, 6,],
      [3, 7,],
      [4, 8,],
      [5, 9,],
      [6, 10,],
      [7, 11,],
      [8, 0,], ],
    [ [1, 1,],  # 戊
      [0, 2,],
      [1, 3,],
      [2, 4,],
      [3, 5,],
      [4, 6,],
      [5, 7,],
      [6, 8,],
      [7, 9,],
      [8, 10,],
      [9, 11,],
      [0, 0,], ],
    [ [3, 1,],  # 己
      [2, 2,],
      [3, 3,],
      [4, 4,],
      [5, 5,],
      [6, 6,],
      [7, 7,],
      [8, 8,],
      [9, 9,],
      [0, 10,],
      [1, 11,],
      [2, 0,], ],
    [ [5, 1,],  # 庚
      [4, 2,],
      [5, 3,],
      [6, 4,],
      [7, 5,],
      [8, 6,],
      [9, 7,],
      [0, 8,],
      [1, 9,],
      [2, 10,],
      [3, 11,],
      [4, 0,], ],
    [ [7, 1,],  # 辛
      [6, 2,],
      [7, 3,],
      [8, 4,],
      [9, 5,],
      [0, 6,],
      [1, 7,],
      [2, 8,],
      [3, 9,],
      [4, 10,],
      [5, 11,],
      [6, 0,], ],
    [ [9, 1,],  # 壬
      [8, 2,],
      [9, 3,],
      [0, 4,],
      [1, 5,],
      [2, 6,],
      [3, 7,],
      [4, 8,],
      [5, 9,],
      [6, 10,],
      [7, 11,],
      [8, 0,], ],
    [ [1, 1,],  # 癸
      [0, 2,],
      [1, 3,],
      [2, 4,],
      [3, 5,],
      [4, 6,],
      [5, 7,],
      [6, 8,],
      [7, 9,],
      [8, 10,],
      [9, 11,],
      [0, 0,], ],
]

kisu_table = [
    [26, 57, 25, 56, 26, 57, 27, 58, 29, 59, 30,  0], # 昭和1(1926年)
    [31,  2, 30,  1, 31,  2, 32,  3, 34,  4, 35,  5], # 昭和2
    [36,  7, 36,  7, 37,  8, 38,  9, 40, 10, 41, 11], # 昭和3
    [42, 13, 41, 12, 42, 13, 43, 14, 45, 15, 46, 16], # 昭和4
    [47, 18, 46, 17, 47, 18, 48, 19, 50, 20, 51, 21], # 昭和5
    [52, 23, 51, 22, 52, 23, 53, 24, 55, 25, 56, 26], # 昭和6
    [57, 28, 57, 28, 58, 29, 59, 30,  1, 31,  2, 32], # 昭和7
    [ 3, 34,  2, 33,  3, 34,  4, 35,  6, 36,  7, 37], # 昭和8
    [ 8, 39,  7, 38,  8, 39,  9, 40, 11, 41, 12, 42], # 昭和9
    [13, 44, 12, 43, 13, 44, 14, 45, 16, 46, 17, 47], # 昭和10
    [18, 49, 18, 49, 19, 50, 20, 51, 22, 52, 23, 53], # 昭和11
    [24, 55, 23, 54, 24, 55, 25, 56, 27, 57, 28, 58], # 昭和12
    [29,  0, 28, 59, 29,  0, 30,  1, 32,  2, 33,  3], # 昭和13
    [34,  5, 33,  4, 34,  5, 35,  6, 37,  7, 38,  8], # 昭和14
    [39, 10, 39, 10, 40, 11, 41, 12, 43, 13, 44, 14], # 昭和15
    [45, 16, 44, 15, 45, 16, 46, 17, 48, 18, 49, 19], # 昭和16
    [50, 21, 49, 20, 50, 21, 51, 22, 53, 23, 54, 24], # 昭和17
    [55, 26, 54, 25, 55, 26, 56, 27, 58, 28, 59, 29], # 昭和18
    [ 0, 31,  0, 31,  1, 32,  2, 33,  4, 34,  5, 35], # 昭和19
    [ 6, 37,  5, 36,  6, 37,  7, 38,  9, 39, 10, 40], # 昭和20
    [11, 42, 10, 41, 11, 42, 12, 43, 14, 44, 15, 45], # 昭和21
    [16, 47, 15, 46, 16, 47, 17, 48, 19, 49, 20, 50], # 昭和22
    [21, 52, 21, 52, 22, 53, 23, 54, 25, 55, 26, 56], # 昭和23(1948)
    [27, 58, 26, 57, 27, 58, 28, 59, 30,  0, 31,  1], # 昭和24
    [32,  3, 31,  2, 32,  3, 33,  4, 35,  5, 36,  6], # 昭和25
    [37,  8, 36,  7, 37,  8, 38,  9, 40, 10, 41, 11], # 昭和26
    [42, 13, 42, 13, 43, 14, 44, 15, 46, 16, 47, 17], # 昭和27
    [48, 19, 47, 18, 48, 19, 49, 20, 51, 21, 52, 22], # 昭和28
    [53, 24, 52, 23, 53, 24, 54, 25, 56, 26, 57, 27], # 昭和29
    [58, 29, 57, 28, 58, 29, 59, 30,  1, 31,  2, 32], # 昭和30
    [ 3, 34,  3, 34,  4, 35,  5, 36,  7, 37,  8, 38], # 昭和31
    [ 9, 40,  8, 39,  9, 40, 10, 41, 12, 42, 13, 43], # 昭和32
    [14, 45, 13, 44, 14, 45, 15, 46, 17, 47, 18, 48], # 昭和33
    [19, 50, 18, 49, 19, 50, 20, 51, 22, 52, 23, 53], # 昭和34
    [24, 55, 24, 55, 25, 56, 26, 57, 28, 58, 29, 59], # 昭和35
    [30,  1, 29,  0, 30,  1, 31,  2, 33,  3, 34,  4], # 昭和36
    [35,  6, 34,  5, 35,  6, 36,  7, 38,  8, 39,  9], # 昭和37
    [40, 11, 39, 10, 40, 11, 41, 12, 43, 13, 44, 14], # 昭和38
    [45, 16, 45, 16, 46, 17, 47, 18, 49, 19, 50, 20], # 昭和39
    [51, 22, 50, 21, 51, 22, 52, 23, 54, 24, 55, 25], # 昭和40
    [56, 27, 55, 26, 56, 27, 57, 28, 59, 29,  0, 30], # 昭和41
    [ 1, 32,  0, 31,  1, 32,  2, 33,  4, 34,  5, 35], # 昭和42
    [ 6, 37,  6, 37,  7, 38,  8, 39, 10, 40, 11, 41], # 昭和43
    [12, 43, 11, 42, 12, 43, 13, 44, 15, 45, 16, 46], # 昭和44
    [17, 48, 16, 47, 17, 48, 18, 49, 20, 50, 21, 51], # 昭和45
    [22, 53, 21, 52, 22, 53, 23, 54, 25, 55, 26, 56], # 昭和46
    [27, 58, 27, 58, 28, 59, 29,  0, 31,  1, 32,  2], # 昭和47
    [33,  4, 32,  3, 33,  4, 34,  5, 36,  6, 37,  7], # 昭和48
    [38,  9, 37,  8, 38,  9, 39, 10, 41, 11, 42, 12], # 昭和49
    [43, 14, 42, 13, 43, 14, 44, 15, 46, 16, 47, 17], # 昭和50
    [48, 19, 48, 19, 49, 20, 50, 21, 52, 22, 53, 23], # 昭和51
    [54, 25, 53, 24, 54, 25, 55, 26, 57, 27, 58, 28], # 昭和52
    [59, 30, 58, 29, 59, 30,  0, 31,  2, 32,  3, 33], # 昭和53
    [ 4, 35,  3, 34,  4, 35,  5, 36,  7, 37,  8, 38], # 昭和54
    [ 9, 40,  9, 40, 10, 41, 11, 42, 13, 43, 14, 44], # 昭和55
    [15, 46, 14, 45, 15, 46, 16, 47, 18, 48, 19, 49], # 昭和56
    [20, 51, 19, 50, 20, 51, 21, 52, 23, 53, 24, 54], # 昭和57
    [25, 56, 24, 55, 25, 56, 26, 57, 28, 58, 29, 59], # 昭和58
    [30,  1, 30,  1, 31,  2, 32,  3, 34,  4, 35,  5], # 昭和59
    [36,  7, 35,  6, 36,  7, 37,  8, 39,  9, 40, 10], # 昭和60
    [41, 12, 40, 11, 41, 12, 42, 13, 44, 14, 45, 15], # 昭和61
    [46, 17, 45, 16, 46, 17, 47, 18, 49, 19, 50, 20], # 昭和62
    [51, 22, 51, 22, 52, 23, 53, 24, 55, 25, 56, 26], # 昭和63
    [57, 28, 56, 27, 57, 28, 58, 29,  0, 30,  1, 31], # 平成1(64)
    [ 2, 33,  1, 32,  2, 33,  3, 34,  5, 35,  6, 36], # 平成2(65)
    [ 7, 38,  6, 37,  7, 38,  8, 39, 10, 40, 11, 41], # 平成3(66)
    [12, 43, 12, 43, 13, 44, 14, 45, 16, 46, 17, 47], # 平成4(67)
    [18, 49, 17, 48, 18, 49, 19, 50, 21, 51, 22, 52], # 平成5(68)
    [23, 54, 22, 53, 23, 54, 24, 55, 26, 56, 27, 57], # 平成6(69)
    [28, 59, 27, 58, 28, 59, 29,  0, 31,  1, 32,  2], # 平成7(70)
    [33,  4, 33,  4, 34,  5, 35,  6, 37,  7, 38,  8], # 平成8(71)
    [39, 10, 38,  9, 39, 10, 40, 11, 42, 12, 43, 13], # 平成9(72)
    [44, 15, 43, 14, 44, 15, 45, 16, 47, 17, 48, 18], # 平成10(73)
    [49, 20, 48, 19, 49, 20, 50, 21, 52, 22, 53, 23], # 平成11(74)
    [54, 25, 54, 25, 55, 26, 56, 27, 58, 28, 59, 29], # 平成12(75)
    [ 0, 31, 59, 30,  0, 31,  1, 32,  3, 33,  4, 34], # 平成13(76)
    [ 5, 36,  4, 35,  5, 36,  6, 37,  8, 38,  9, 39], # 平成14(77)
    [10, 41,  9, 40, 10, 41, 11, 42, 13, 43, 14, 44], # 平成15(78)
    [15, 46, 15, 46, 16, 47, 17, 48, 19, 49, 20, 50], # 平成16(79)
    [21, 52, 20, 51, 21, 52, 22, 53, 24, 54, 25, 55], # 平成17（80, 2005年）
]

time_kanshi = [
    [ [0, 0],    # 甲
      [1, 1],
      [2, 2],
      [3, 3],
      [4, 4],
      [5, 5],
      [6, 6],
      [7, 7],
      [8, 8],
      [9, 9],
      [0, 10],
      [1, 11],
      [2, 0], ],
    [ [2, 0],    # 乙
      [3, 1],
      [4, 2],
      [5, 3],
      [6, 4],
      [7, 5],
      [8, 6],
      [9, 7],
      [0, 8],
      [1, 9],
      [2, 10],
      [3, 11],
      [4, 0], ],
    [ [4, 0],    # 丙
      [5, 1],
      [6, 2],
      [7, 3],
      [8, 4],
      [9, 5],
      [0, 6],
      [1, 7],
      [2, 8],
      [3, 9],
      [4, 10],
      [5, 11],
      [6, 0], ],
    [ [6, 0],   # 丁
      [7, 1],
      [8, 2],
      [9, 3],
      [0, 4],
      [1, 5],
      [2, 6],
      [3, 7],
      [4, 8],
      [5, 9],
      [6, 10],
      [7, 11],
      [8, 0], ],
    [ [8, 0],   # 戊
      [9, 1],
      [0, 2],
      [1, 3],
      [2, 4],
      [3, 5],
      [4, 6],
      [5, 7],
      [6, 8],
      [7, 9],
      [8, 10],
      [9, 11],
      [0, 0], ],
    [ [0, 0],    # 己
      [1, 1],
      [2, 2],
      [3, 3],
      [4, 4],
      [5, 5],
      [6, 6],
      [7, 7],
      [8, 8],
      [9, 9],
      [0, 10],
      [1, 11],
      [2, 0], ],
    [ [2, 0],    # 庚
      [3, 1],
      [4, 2],
      [5, 3],
      [6, 4],
      [7, 5],
      [8, 6],
      [9, 7],
      [0, 8],
      [1, 9],
      [2, 10],
      [3, 11],
      [4, 0], ],
    [ [4, 0],    # 辛
      [5, 1],
      [6, 2],
      [7, 3],
      [8, 4],
      [9, 5],
      [0, 6],
      [1, 7],
      [2, 8],
      [3, 9],
      [4, 10],
      [5, 11],
      [6, 0], ],
    [ [6, 0],   # 壬
      [7, 1],
      [8, 2],
      [9, 3],
      [0, 4],
      [1, 5],
      [2, 6],
      [3, 7],
      [4, 8],
      [5, 9],
      [6, 10],
      [7, 11],
      [8, 0], ],
    [ [8, 0],   # 癸
      [9, 1],
      [0, 2],
      [1, 3],
      [2, 4],
      [3, 5],
      [4, 6],
      [5, 7],
      [6, 8],
      [7, 9],
      [8, 10],
      [9, 11],
      [0, 0], ],
]

zokan_time = [
    [10, 1],
    [9, 3],
    [7, 2],
    [10, 3],
    [9, 3],
    [7, 2],
    [[10, 0], [20, 1]],
    [9, 3],
    [7, 2],
    [10, 3],
    [9, 3],
    [7, 2],
]

zokan = [
    [8, 9,],  # 子
    [9, 5,],  # 丑
    [4, 0,],  # 寅
    [0, 1,],  # 卯
    [1, 4,],  # 辰
    [4, 2,],  # 巳
    [2, 5, 3,],  # 午
    [3, 5,],  # 未
    [4, 6,],  # 申
    [6, 7,],  # 酉
    [7, 4,],  # 戌
    [4, 8,],  # 亥
]

gogyo = ['木', '火', '土', '金', '水',]
gogyo_kan = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4,]
gogyo_shi = [4, 2, 0, 0, 2, 1, 1, 2, 3, 3, 2, 4,]

tsuhen = ['比肩', '劫財', '食神', '傷官', '偏財', '正財', '偏官', '正官', '偏印', '印綬',]

kan_tsuhen = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,],  # 甲
    [1, 0, 3, 2, 5, 4, 7, 6, 9, 8,],  # 乙
    [2, 3, 4, 5, 6, 7, 8, 9, 0, 1,],  # 丙
    [3, 2, 5, 4, 7, 6, 9, 8, 1, 0,],  # 丁
    [4, 5, 6, 7, 8, 9, 0, 1, 2, 3,],  # 戊
    [5, 4, 7, 6, 9, 8, 1, 0, 3, 2,],  # 己
    [6, 7, 8, 9, 0, 1, 2, 3, 4, 5,],  # 庚
    [7, 6, 9, 8, 1, 0, 3, 2, 5, 4,],  # 辛
    [8, 9, 0, 1, 2, 3, 4, 5, 6, 7,],  # 壬
    [9, 8, 1, 0, 3, 2, 5, 4, 7, 6,],  # 癸
]

twelve_fortune = [
    '長', '沐', '冠', '建', '帝', 'ス', 'ビ', 'シ', 'ボ', 'ゼ', '胎', '養', 
]

twelve_table = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0,],  # 甲
    [6, 5, 4, 3, 2, 1, 0, 11, 10, 9, 8, 7,],  # 乙
    [10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,],  # 丙
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 10,],  # 丁
    [10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,],  # 戊    
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 10,],  # 己
    [7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6,],  # 庚
    [0, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1,],  # 辛
    [4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3,],  # 壬
    [3, 2, 1, 0, 11, 10, 9, 8, 7, 6, 5, 4,],  # 癸
]

choko = [
    ['火土', '火土', '火水', '水', '水', '水', '土水', '土水', '火', '火土', '火土', '土',],  # 甲
    ['火土', '火土', '火水', '水', '水', '水', '土水', '土水', '火', '火土', '火土', '土',],  # 乙
    ['木火', '火', '金土', '水金', '水金', '水', '金水', '水', '木火', '木火', '木火', '木火',],  # 丙
    ['木火', '火', '金土', '水金', '水金', '水', '金水', '水', '木火', '木火', '木火', '木火',],  # 丁
    ['火土', '火金', '土火', '金', '金水', '水金', '水金', '水', '火', '土火', '土火', '火',],  # 戊
    ['火土', '火金', '土火', '金', '金水', '水金', '水金', '水', '火', '土火', '土火', '火',],  # 己
    ['土火', '火金', '土金', '土金', '土金', '土金', '金土', '水', '水火木', '火木', '火土', '火土',],  # 庚
    ['土火', '火金', '土金', '土金', '土金', '土金', '金土', '水', '水火木', '火木', '火土', '火土',],  # 庚
    ['火土', '土火', '金水', '水金', '水', '金', '金', '木火', '木土', '土木・火', '火土', '火土',],  # 壬
    ['火土', '土火', '金水', '水金', '水', '金', '金', '木火', '木土', '土木・火', '火土', '火土',],  # 癸
]

kubo = [
    [10, 11,],
    [8, 9,],
    [6, 7,],
    [4, 5,],
    [2, 3,],
    [0, 1,],
]

from datetime import datetime as dt

WAREKI_START = {
    '令和': dt(2019, 5, 1),
    '平成': dt(1989, 1, 8),
    '昭和': dt(1926, 12, 25)
}

def convert_to_wareki(y_m_d):
    """西暦の年月日を和暦の年に変換する."""
    try:
        if WAREKI_START['令和'] <= y_m_d:
            reiwa_year = WAREKI_START['令和'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '令和'
        elif WAREKI_START['平成'] <= y_m_d:
            reiwa_year = WAREKI_START['平成'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '平成'
        elif WAREKI_START['昭和'] <= y_m_d:
            reiwa_year = WAREKI_START['昭和'].year
            era_year = y_m_d.year
            year = (era_year - reiwa_year) + 1
            era_str = '昭和'
        else:
            return '昭和以前'
        
        if len(str(year)) == 1:
            year = ' ' + str(year)
        else:
            year = str(year)
            
        if year == ' 1':
            year = '元'
            
        return era_str + year + '年'
    except ValueError as e:
        raise e


