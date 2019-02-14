import java.io. *;
class Rto{
	int n = 9,r = 3;
	long fact = 1,total;
	public long calculate(){
		total = (n * (findFact(n)/findFact(n-r)));
        return total;
	}
	public long findFact(int n){
		if(n <= 1){
			return 1;
		}
		else{
            return findFact(n) * findFact(n-1);
		}
	}
	public static void main(String[] args) {
		Rto r = new Rto();
		System.out.println(r.calculate());
	}
}