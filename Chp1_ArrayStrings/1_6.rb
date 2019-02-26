#String Compression
#basic string compression using counts of repeated characters
#eg aabcccccaaa is a2b1c5a3
#solution is O(n)

def stringCompress(fullString)

  result = []

  fullString.each_char do |c|

    if result[-2] != c
      result << c << 1
    else
      result[-1] += 1
    end
  end

  if result.length < fullString.length
    result.join("")
  else
    fullString
  end

end
