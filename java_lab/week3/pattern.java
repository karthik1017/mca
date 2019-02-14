import java.io. *;
class Pattern{
	int total,start = 1; 
	void display(){
		for(int i = 0; i < 9;i++){
            total = start * start;
            System.out.println(total);
            start = start * 10 + 1;
		}
	}
	public static void main(String[] args) {
		Pattern p = new Pattern();
		p.display();
	}
}