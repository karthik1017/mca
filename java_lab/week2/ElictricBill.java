import java.io. *;
class ElectricBill{
	double slab1 = 1.20,slab2 = 2.10,slab3 = 4.20,slab4 = 5;
	int prevUnit = 5000;
	int presUnit = 5150;
	int unit = 0,min = 50;
	double total;
	public void calculate(){
		unit = presUnit - prevUnit;
	}
	public void bill(){
		if(unit <= 99 && unit >= 1){
          total = unit * slab1 + min;
          System.out.println("the bill is: "+total);
		}
		else if(unit <= 199 && unit >= 100){
			total = unit * slab2 + min;
			System.out.println("the bill is: "+total);
		}
		else if(unit <= 299 && unit >= 200){
			total = unit * slab3 + min;
			System.out.println("the bill is: "+total);
		}
		else{
			total = unit * slab4 + min;
			System.out.println("the bill is: "+total);
		}
	}
	public static void main(String[] args) {
		ElectricBill el = new ElectricBill();
		el.calculate();
		el.bill();
	}
}