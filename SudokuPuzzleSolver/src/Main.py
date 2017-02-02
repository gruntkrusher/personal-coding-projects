from Matrix import Matrix

print("\n\n unfilled");
matrix = Matrix(3);
matrix.display();

print("\n\n filled");
matrix.readFromFile("sol.txt");
matrix.display();

print("\n\n swapped")
matrix.swapSmallRow(0, 2)
matrix.display()

print("\n\n swapped Large")
matrix.swapLargeRow( 0, 1)
matrix.display()

print("\n\n swap Values")
matrix.swapValues(4, 5)
matrix.display()

print("\n\n rotate")
matrix.rotateCounterClockWise()
matrix.display()

print("\n\n swap col")
matrix.swapSmallCol(1, 3)
matrix.display()

print("\n\n swap col")
matrix.swapLargeCol(1, 2)
matrix.display()