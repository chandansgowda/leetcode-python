class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image[i])):
                image[i][j]=1 if image[i][j]==0 else 0

        return image
