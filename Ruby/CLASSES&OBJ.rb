#NAME:AMEY S. NAGMODE
#PRN:1841032
#CLASS:S.Y.COMPUTER
#BATCH:S2
#AIM:TO IMPLEMENT CLASSES AND OBJECTS

class Tv
def initialize(company,price,wireless)
@company=company
@price=price
@wireless=wireless
end
def display
  puts("####from tv")
  puts ("company name=#{@company}")
  puts ("price=#{@price}")
  puts ("wireless=#{@wireless}")
  end
end
class Speaker
def initialize(company,price,wireless)
@company=company
@price=price
@wireless=wireless
end
def display
  puts("from speaker")
  puts(" company name=#{@company}")
  puts("price=#{@price}")
  puts("wireless=#{@wireless}")
end
end

t1=Tv.new("sony",1500,"yes")
t1.display
s=Speaker.new("JBL",3500,"yes")
s.display
