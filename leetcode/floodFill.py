def print_image(new_image):
    M = len(new_image)
    N = len(new_image[0])
    print (f"Updated screen after call to floodFill: {M} X {N}")
    for i in range(M):
        for j in range(N):
            print(new_image[i][j], end = ' ')
        print()

class Solution(object):
    def floodFillHelper(self, image, sr, sc, newColor, oldColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        print(f"Visiting {sr} {sc}\n------------------------")
        print_image(image)
        if(not(0 <= sr and sr < len(image) ) or not (0 <= sc and sc < len(image[0])) or (image[sr][sc] != oldColor) ):
            print(f"outside the matrix {sr} {sc}")
            return
        else:
            print(f"inside the matrix {sr} {sc} and {image[sr][sc]}")
            image[sr][sc] = newColor
            print(f"inside the matrix {sr} {sc} and {image[sr][sc]}")
            self.floodFillHelper(image, sr -1, sc, newColor, oldColor)#UP
            self.floodFillHelper(image, sr +1, sc, newColor, oldColor)#DOWN
            self.floodFillHelper(image, sr, sc -1, newColor, oldColor)#LEFT
            self.floodFillHelper(image, sr, sc +1, newColor, oldColor)#RIGHT



    def floodFill(self, image, sr, sc, newColor):
        color_to_replace = image[sr][sc]
        if color_to_replace != newColor:
            self.floodFillHelper(image, sr, sc, newColor, color_to_replace)
        return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
# image =  [[0,0,0],[0,0,0]]
# sr = 0
# sc = 0
# newColor = 2
# image = [[0,0,0],[0,1,1]]
# sr=1
# sc=1
# newColor=1
new_image = Solution().floodFill(image, sr, sc, newColor)

print_image(new_image)