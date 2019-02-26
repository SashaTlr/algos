def contains_no_dupes(string)
  if len(string) <= 1:
    return True
  if len(string) > 256:
    return False
    
  letters = {}
  for letter in string:
    if letter in letters:
      return False
    letters[letter] = True
  return True
 
      
