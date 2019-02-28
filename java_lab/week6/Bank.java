	import java.io. *;
	import java.util. *;
	class Bank{
		void displayBank(){
			System.out.println("welcome to KARTHIK BANKERS CO.");
			System.out.println("we provide loans");
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
			Vloan v = new Vloan();
			v.displayBank();
			v.displayLoan();
			v.displayVloan();

			HomeLoan h = new HomeLoan();
			h.displayBank();
			h.displayLoan();
			h.displayHloan();

			PersonalLoan P = new PersonalLoan();
			P.displayBank();
			P.displayLoan();
			P.displayPloan();
		}
	}