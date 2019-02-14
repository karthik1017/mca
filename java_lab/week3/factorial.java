import java.io. *;
class Factorial{
	int fact = 1;
	int n;
	Factorial(int number){
		n = number;
	}
	int factorial(){
		for(int i = 1; i <= n; i++){
           fact = fact * i;
		}
		return fact;
	}
	public static void main(String[] args) {
        Factorial fact = new Factorial(4);
        System.out.println(fact.factorial());
	}
}