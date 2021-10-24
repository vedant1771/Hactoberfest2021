#NAME:AMEY S. NAGMODE
#AIM:TO CALAULATE SIMPLE INTEREST AND COMPOUND INTEREST

#!/user/bin/ruby
puts"PROGRAM FOR SIMPLE INTEREST AND COMPOUND INTEREST"
puts"for simple interest.................."
puts"please enter principle amount,no of years and rate of intrest>>>"
p=gets.to_f
n=gets.to_f
r=gets.to_f
s=(p*n*r)/100
puts("simple interest is ")
puts(s)
puts"for compound interest................"
puts("please enter no of times in a year....t")
t=gets.to_f
c=(1+(r/n))
c=c**(n*t)
c=c*p
puts"compound interest is ............"
puts(c)
