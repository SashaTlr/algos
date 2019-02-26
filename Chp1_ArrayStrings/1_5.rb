#write a function to determine if two strings are one edit from being identical

#psuedocode
#if length of two stings differ by more then one, then return false
#if one string is smaller, iterate through each, if there is a difference, insert new letter. if rest is true, return true
#if strings are identical in length, swap first mismatch to match, if rest identical, return true
require "pry"

def oneAway(str1, str2)


  oneAwayDiff = false
  equalStringLength = false
  longstring = ""
  shortstring = ""

  if (str1.length - str2.length).abs > 1
    return oneAwayDiff
  end

  if str1.length > str2.length
    longstring = str1
    shortstring = str2
  elsif str1.length == str2.length
    equalStringLength = true
    longstring = str1
    shortstring = str2
  else
    longstring = str2
    shortstring = str1
  end

  shortstringpointer = 0

  longstring.each_char.with_index{|e, i|
    if e != shortstring[shortstringpointer]
      if oneAwayDiff
        return false;
      end

      if !equalStringLength
        shortstringpointer -=1
      end
      oneAwayDiff = true
    end
    shortstringpointer +=1
  }

  true
end
