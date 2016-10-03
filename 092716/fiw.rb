
def in_words(int)
  is_negative=false
  
  if(int<0)
    is_negative=true
  end
  int=int.abs
  
  numbers_to_name = {
    
    #Lookup table unique numbers
      1000000 => "million",
      1000 => "thousand",
      100 => "hundred",
      90 => "ninety",
      80 => "eighty",
      70 => "seventy",
      60 => "sixty",
      50 => "fifty",
      40 => "forty",
      30 => "thirty",
      20 => "twenty",
      19=>"nineteen",
      18=>"eighteen",
      17=>"seventeen", 
      16=>"sixteen",
      15=>"fifteen",
      14=>"fourteen",
      13=>"thirteen",              
      12=>"twelve",
      11 => "eleven",
      10 => "ten",
      9 => "nine",
      8 => "eight",
      7 => "seven",
      6 => "six",
      5 => "five",
      4 => "four",
      3 => "three",
      2 => "two",
      1 => "one"
      
    }
  str = ""
  numbers_to_name.each do |num, name|
    if int == 0
      return str
    elsif int.to_s.length == 1 && int/num > 0
      return "Negative "+str + "#{name}" if is_negative 
      return str + "#{name}" if !is_negative 
    elsif int < 100 && int/num > 0
      return "Negative " + str + "#{name}" if int%num == 0 && is_negative 
      return str + "#{name}" if int%num == 0 && !is_negative
      return "Negative " + str + "#{name} " + in_words(int%num) if is_negative
      return str + "#{name} " + in_words(int%num) if !is_negative
    elsif int/num > 0
      return "Negative " + str + in_words(int/num) + " #{name} " + in_words(int%num) if is_negative
       return str + in_words(int/num) + " #{name} " + in_words(int%num) if !is_negative
    end
  end
end

puts in_words(-34)
