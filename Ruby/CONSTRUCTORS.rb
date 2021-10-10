$num=20
class D
 def initialize()
	puts"the original no is#{$num}"
 end
end
class B
 def initialize()
	puts"increment by 10:#{$num+10}"
 end
end
d=D.new()
b=B.new()
