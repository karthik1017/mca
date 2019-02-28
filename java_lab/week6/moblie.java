import java.io. *;
import java.util. *;
class Phone{
	void displayCommon(){
		System.out.println("welcome to KARTHIK Mobile Showroom");
		System.out.printf("1)touchScreen\n2)camera\n3)andriod os\n4)water resistance\n");
	}

}

class Samsung extends Phone{
	void displaySamsung(){
        System.out.println("this are Samsung phones");
        System.out.printf("1)Samsung a8\n2)Samsung j7\n3)Samsung S9\n4)Samsung s10\n");
	}
}

class Micromax extends Phone{
	void displayMicromax(){
        System.out.println("this are Micromax phones");
        System.out.printf("1)Micromax a8\n2)Micromax j7\n3)Micromax S9\n4)MicromaxInfinity1\n");
	}
}

class SamsungS10 extends Samsung{
	int price = 100000;
	void displaySamsungS10(){
        System.out.println("this is Samsung s10");
        System.out.printf("1)water proof \n2)infinity display\n3)dual camera\n4)12gb ram 1tb storage\n");
	}
	void displaySamPrice(){
		System.out.println("SamsungS10 price = ");
		System.out.println(price);
	}
}

class MicromaxInfinity1 extends Micromax{
	int price = 80000;
	void displayMicromaxInfi(){
        System.out.println("this is Samsung s10");
        System.out.printf("1)no water proof \n2)infinity display\n3)dual camera\n4)8gb ram 128gb storage\n");
	}
	void displayMicromaxInfiPrice(){
		System.out.println("\nMicromaxInfinity1 price = ");
		System.out.println(price);
	}
}

class Mobile{
	public static void main(String[] args) {
		SamsungS10 s = new SamsungS10();

		MicromaxInfinity1 m = new MicromaxInfinity1();

		s.displayCommon();

		s.displaySamsung();
		m.displayMicromax();

		s.displaySamsungS10();
		m.displayMicromaxInfi();

		m.displayMicromaxInfiPrice();
		s.displaySamPrice();
	}
}