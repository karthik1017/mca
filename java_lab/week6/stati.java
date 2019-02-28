import java.io. *;
import java.util. *;
class Bank{
	static int bal = 3500;
	static void display(){
		System.out.println(Bank.bal);
	}
}

class Loan extends Bank{
	public static void main(String[] args) {
		Bank.display();
		System.out.println(A.num);
	}
	
}

class A{
	static int num = 3;
}

