class ED:
    def edit_distance(self, s1, s2):
        array = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]

        for i in range(len(array)):
            for j in range(len(array[i])):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    if '' != s2[j - 1]:
                        array[i][j] = array[i][j - 1] + 1
                elif j == 0:
                    if s1[i - 1] != '':
                        array[i][j] = array[i - 1][j] + 1
                else:
                    if s1[i - 1] == s2[j - 1]:
                        array[i][j] = array[i - 1][j - 1]
                    else:
                        array[i][j] = min(array[i - 1][j - 1], array[i - 1][j], array[i][j - 1]) + 1
        return array[-1][-1]

