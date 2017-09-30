#string rotation
#concatenate the string to itself and check if string 1 is a substring of s2

def isRotation (s1, s2)



  if s2.length > s1.length
    return false

  s2 = s2 << s2

  s2.include?(s1)

end