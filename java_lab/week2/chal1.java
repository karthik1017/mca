import java.io. *;
class Last{
	int num = 67;
	int digit = 67%10;
    public void display(){
    	if(digit == 0){
           System.out.println("zero");
    	}
    	else if(digit == 1){
    	   System.out.println("one");
    	}
    	else if(digit == 2){
           System.out.println("two");
    	}
    	else if(digit == 3){
           System.out.println("three");    		
    	}
    	else if(digit == 4){
           System.out.println("four");
    	}
    	else if(digit == 5){
           System.out.println("five");
    	}
    	else if(digit == 6){
           System.out.println("six");
    	}
    	else if(digit == 7){
           System.out.println("seven");   		
    	}
    	else if(digit == 8){
           System.out.println("eight");   		
    	}
    	else if(digit == 9){
           System.out.println("nine");    		
    	}
    }
    public static void main(String[] args) {
        Last l = new Last();
        l.display();	
    }
}