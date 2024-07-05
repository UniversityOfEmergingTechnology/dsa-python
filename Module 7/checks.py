for i in range(9):
    # row = 5 col = 5
    rowIndex = 3 * (5 // 3) + i // 3
    colIndex = 3 * (5 // 3) + i % 3
    print("Printing for  " , i , " " , rowIndex , " " , colIndex)