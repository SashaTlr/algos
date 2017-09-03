#rotate matrix
#given NxN matrix, rotate image 90 degrees

def RotateMatrix (squareImg)
  r = squareImg.size - 1
  c = squareImg[0].size - 1

  (0..r/2).each do |row|
    (0..c/2).each do |col|

squareImg[row][col], squareImg[r - row][col], squareImg[r-row][c-col], squareImg[row][c-col] = squareImg[r - row][col], squareImg[r-row][c-col], squareImg[row][c-col], squareImg[row][col]


    end
   end
squareImg
end

