class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m=len(box)
        n=len(box[0])
        for row in range(m):
            down_empty_pos=n-1
            for col in range(n-1,-1,-1):
                if box[row][col]=='#':
                    # move the small box to next empty positon
                    # empty this place
                    box[row][col]='.'
                    box[row][down_empty_pos]='#'
                    down_empty_pos-=1
                elif box[row][col]=='*':
                    # obstacles
                    down_empty_pos=col-1

        # now rotate and return the new matrix
        # number of rows becomes number of columns and vice versa
        returnMatrix=[[None]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                # clockwise 90 degree rotation
                returnMatrix[i][j]=box[m-1-j][i]
        return returnMatrix