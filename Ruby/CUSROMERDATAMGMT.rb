#NAME:AMEY S. NAGMODE
#PRN:1841032
#CLASS:S.Y.COMPUTER
#BATCH:S2
#AIM:TO DISPLAY CUSTOMER DATA AND NUMBER OF CUSTOMERS USING CLASSES 

#!/user/bin/ruby
class Customer
   @@no_of_customer=0
  def initialize(id,name,address,phone)
    @id=id
    @name=name
    @address=address
    @phone=phone
  end
  def display()
    puts"id of Customer is #@id"
   # @id=gets
    puts"name of customer is #@name"
   # @name=gets
    puts"addess of customer is #@address"
   # @address=gets
    puts"phone of customer is #@phone"
   # @phone=gets
    puts"NO OF CUSTOMER IS--> #@@no_of_customer"

  end
  def no_of_customer()
     @@no_of_customer+=+1
    
  end
end
a=Customer.new(32,"AMEY","WARDHA",9175559003)
a.no_of_customer()
b=Customer.new(24,"VISHAL","BEED",9096858823)
b.no_of_customer()
c=Customer.new(28,"hrutik","WARDHA",9175554003)
c.no_of_customer()
a.display()
b.display()
c.display()
