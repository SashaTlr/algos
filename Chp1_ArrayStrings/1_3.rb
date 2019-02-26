#replace all spaces in string with %20
#e.g. "Mr John Smith     " --> "Mr%20John%20Smith"

#split sentence into character array
#join with %20

#explicit solution
#for loop starting with last element of string length
#iterating backwards from stringLength, array[index] = array[stringLength]
#if string length index is a space, array index, i-1, i-2 is %20

#ruby solution
def splitString(example)
  example.split(" ").join("%20")
end

void splitstring (string example, int truelength)
{
  var numSpaces= 0;

  for (int i = 0; i <= truelength; i++)
    {
      if (example[i] ==" ")
        {
          numSpaces += 1;
        }
    }

    var index = truelength + numSpaces * 2;
  for (int i = truelength - 1; i >= 0; i--)
    {
      if(example[i] == " ")
        {
          example[index] = "0";
          example[index-1] = "2";
          example[index-2] = "%";
          index -= 3;
        }
      else
        {
          example[index] = example[i];
          index -= 1;
        }
    }
}
