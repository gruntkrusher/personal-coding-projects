import math

class Matrix():
    
    # Constructor (initialize zero)
    def __init__(self, blockDim):
        
        self.matrix = [];
        self.numCols = blockDim * blockDim;
        self.blockDim = blockDim;
        
        # initialize to 0
        for i in range(self.numCols):
            self.matrix.append([]);
            for j in range(self.numCols):
                self.matrix[i].append(0);
                            
    
    # Display the current state of the board 
    def display(self):
        
        # top line
        print(" ",end="")
        for i in range(2 * self.blockDim * self.blockDim + 2 * self.blockDim - 1):
            print("-",end="")
        print()
        
        for i in range(self.numCols):
            
            # left hand edge
            print("|", end=" ");
            
            for j in range(self.numCols):
                
                if self.matrix[i][j] == 0 :
                    print(" ", end=" ")
                else:
                    print(self.matrix[i][j], end=" ");
                
                # insert vertical separator
                if j % self.blockDim == self.blockDim - 1 :
                    print("|", end=" ");
            
            print();
            
            # insert horizontal separator
            if i % self.blockDim == self.blockDim - 1 :
                print(" ",end="")
                for i in range(2 * self.blockDim * self.blockDim + 2 * self.blockDim - 1):
                    print("-",end="")
                print()
    
    # use solution stored on disk
    def readFromFile(self, fileName):
        
        # open file
        inFile = open(fileName, 'r');
        # put file contents in string
        read_data = inFile.read();
        # split string by end of line
        l = read_data.split("\n");
        
        # split into individual integers
        broken_list = [];
        for i in range(len(l)):
            broken_list.append(l[i].split(" "));
        
        # put integers from broken_list in matrix
        for i in range(self.numCols):
            for j in range(self.numCols):
                if(i < len(broken_list) and j < len(broken_list[i])):
                    self.matrix[i][j] = int(broken_list[i][j]) ;
    
    
     
    ### MATRIX OPERATIONS ###
    
    def swapSmallRow(self, a, b):
        
        for i in range(self.numCols):
            temp = self.matrix[a][i]
            self.matrix[a][i] = self.matrix[b][i]
            self.matrix[b][i] = temp
            
    def swapSmallCol(self, a, b):
        
        self.rotateClockWise()
        self.swapSmallRow(a, b)
        self.rotateCounterClockWise()
        
    def swapLargeRow(self, a, b):
        
        for i in range(self.blockDim):
            self.swapSmallRow(a * self.blockDim + i, b * self.blockDim + i)
            
    def swapLargeCol(self, a, b):
        
        self.rotateClockWise()
        self.swapLargeRow(a, b)
        self.rotateCounterClockWise()
            
    def swapValues(self, a, b):
        
        for i in range(self.numCols):
            for j in range(self.numCols):
                if(self.matrix[i][j] == a):
                    self.matrix[i][j] = b;
                elif(self.matrix[i][j] == b):
                    self.matrix[i][j] = a;
                     
    def rotateCounterClockWise(self):
        N = self.numCols
        x = 0
        while(x < N/2 ):
            
            y = x
            while(y < N - x - 1):
                temp = self.matrix[x][y]
                self.matrix[x][y] = self.matrix[y][N-1-x]
                self.matrix[y][N-1-x] = self.matrix[N-1-x][N-1-y]
                self.matrix[N-1-x][N-1-y] = self.matrix[N-1-y][x]
                self.matrix[N-1-y][x] = temp
                
                y += 1
                
            x += 1
            
    def rotateClockWise(self):
        for i in range(3):
            self.rotateCounterClockWise()
                
        
        
        
        
        
        