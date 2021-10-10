public class SampleBank {
    public static void main(String[] args) {
        Bank B1 = new Bank("01634001300000452","Biman Sen", "S", "55000.67");
        B1.display();
        System.out.println("After Deposit ...");
        B1.deposit("45987.59");
        B1.display();
        System.out.println("After With draw ...");
        B1.withDraw("10000");
        B1.display();
    }
}

class Bank{
    private String accountNumber, customerName, accountType, amount;

    public Bank(String accountNumber, String customerName, String accountType, String amount){
        this.accountNumber = accountNumber;
        this.customerName = customerName;
        this.accountType = accountType;
        this.amount = amount;
    }

    public void deposit(String amount) {
        this.amount = Double.toString(Double.parseDouble(amount) + Double.parseDouble(this.amount));
        System.out.println("Deposit Successful.");
    }
    public void withDraw(String amount) {
        if(Double.parseDouble(amount) > Double.parseDouble(this.amount)){
            System.out.println("withdrawal amount is not available");
        }
        else if(Double.parseDouble(this.amount) < 5000){
            System.out.println("Balance is less than 5000. Can't withdraw money!");
        }
        else {
            this.amount = Double.toString(Double.parseDouble(this.amount) - Double.parseDouble(amount));
            System.out.println("Withdrawal Successful");
        }
    }
    public void display(){
        System.out.println("Customer Name: " + this.customerName);
        System.out.println("Account Number: " + this.accountNumber);
        System.out.println("Account Type: " + this.accountType);
        System.out.println("Account Balance: " + this.amount);
        System.out.println();
    }
}
