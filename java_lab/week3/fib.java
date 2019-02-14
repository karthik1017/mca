import java.io. *;
class Fib{
	int first = 0,second = 1,n = 5,third;
	void display(){
	   for(int i = 2; i <= n; i++){
           third = first + second;
           System.out.print(third+',');
           first = second;
           second = third;
	   }
	}
	public static void main(String[] args) {
		Fib f = new Fib();
		f.display();
	}
}