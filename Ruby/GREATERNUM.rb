#NAME:AMEY S. NAGMODE
#PRN:1841032
#CLASS:S.Y.COMPUTER
#BATCH:S2
#AIM:TO GET LARGER NUMBER USING CLASSES

#!/user/bin/rubyclass Greater
#!/user/bin/ruby
class Greater
        def get
	  puts"Enter first number:"
	  a=gets.to_i
	  puts"Enter second number:"
	  b=gets.to_i
	  if(a>b)
	    puts"Greater number is #{a}"
	  else
	    puts"Greater number is #{b}"
	  end
	end
end
g=Greater.new()
g.get

