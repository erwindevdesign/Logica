def quadratic_complexxity(matriz):
    for i in range (len(matriz)): # -------------------|
        for j in range (len(matriz[0])): # --|         |
            if num[i][j] !=0: #              |-->O(n)  |--> O(n)<--|--> O(n*n) == O
                print(num[i][j])# -----------|         |-----------|
                # -------------------------------------|



def three_sum(numbers: list[int]) -> List[List[int]]:
    if len[numbers] < 3:
        return[]
    numbers.sort()
    result = set()
    for i in range(len(numbers)-2):
        if numbers[1] <= 0:
            if i == 0 or numbers[i-1]<numbers[i]:
                map = {}
          