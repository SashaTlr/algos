
def contains_no_dupes(str):
    if len(str) <= 1:
      return True
    if len(str) > 256:
      return False
    
    letters = {}
    for letter in str:
      if letter in letters:
        return False
      letters[letter] = True
    return True

if __name__ == "__main__":
    import sys
    print(contains_no_dupes(sys.argv[-1]))

#last section lets you use 'python A_unique_chars_01.py hello' in terminal to run function

