#NAME:AMEY S. NAGMODE
#PRN:1841032
#CLASS:S.Y.COMPUTER
#BATCH:S2
#AIM:TO DISPLAY STUDENT'S ACADEMIC DATA USING CLASSES


class Student
  def initialize(name,id,gender,mobile,m1,m2,m3)

    @name=name
    @id=id
    @gender=gender
    @mobile=mobile
    @m1=m1
    @m2=m2
    @m3=m3

  end
  def accumulated_score
	m=0
	m=(@m1+@m2+@m3)/3
	puts("avarage score= #{m}")
  end
  def display
    puts("Student Name : #{@name}")
    puts("Student id : #{@id}")
    puts("Student Gender : #{@gender}")
    puts("Student mobile : #{@mobile}")

  end
end



  puts("Enter Name:")
  name=gets.to_s
  puts("Enter ID:")
  id=gets.to_i
  puts("Enter Gender:")
  gender=gets.to_s
  puts("Enter mobile:")
  mobile=gets.to_i
  puts("Enter M1:")
  m1=gets.to_i
  puts("Enter M2:")
  m2=gets.to_i
  puts("Enter M3:")
  m3=gets.to_i
  s=Student.new(name,id,gender,mobile,m1,m2,m3)
  s.display()
  s.accumulated_score

