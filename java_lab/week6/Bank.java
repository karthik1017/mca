	import java.io. *;
	import java.util. *;
	import java.util.Scanner; 

	class Bank{
		void displayBank(){
			System.out.println("welcome to KARTHIK BANKERS CO.");
			System.out.println("we provide loans");
			System.out.printf("\n Please enter your name:");
			Scanner sc = new Scanner(System.in);
			String name = sc.nextLine();
			System.out.printf("\n Please enter your acc no:");
			int acc_no = sc.nextInt();
		}

	}
	class Loan extends Bank{
		void displayLoan(){
			System.out.printf("1)loan\n2)HomeLoan\n3)PersonalLoan\n");
		}

	}

	class Vloan extends Loan{
		int interest = 10;
		void displayVloan(){
			System.out.println("the interest for vloan = "+interest);
		}

	}

	class HomeLoan extends Loan{
		int interest = 12;
		void displayHloan(){
			System.out.println("the interest for Hloan = "+interest);
		}
	}

	class PersonalLoan extends Loan{
		int interest = 11;
		void displayPloan(){
			System.out.println("the interest for Ploan = "+interest);
		}
	}

	class stat{
		public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
			Bank b = new Bank();
			b.displayBank();
			System.out.printf("\n 1)vehicle loan \n 2)personal loan \n 3)homeloan \n");
			System.out.println("enter ur choice");
			int choice = sc.nextInt();
			switch(choice) {
            case 1:
			       Vloan v = new Vloan();
			       v.displayLoan();
			       v.displayVloan();
                   break;
            case 2:
			       PersonalLoan P = new PersonalLoan();
			       P.displayLoan();
			       P.displayPloan();
                   break;
			case 3:
			       HomeLoan h = new HomeLoan();
			       h.displayLoan();
			       h.displayHloan();
			       break;
            default:
                 System.out.println("wrong choice");
		}
	}
}