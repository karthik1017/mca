import java.io. *;
import java.util. *;
import java.util.Scanner;
import java.lang.String;

interface Amma{
   final int plane_cake=100,cold_coffee=150,juice=30,ice_cake=200;
   int displayMenu();
}

abstract class Counter implements Amma{
   String userName = "karthik";
   String password = "karthik123" ;
   int total=0,count = 0; 
   abstract boolean authen();
   abstract void calcualte();
   abstract void showMenu();
   void displayCounter(){

   }
}

class Authenticate extends Counter{
   Boolean authen(){
     System.out.println("Enter your username: ");
     Scanner scanner = new Scanner(System.in);
     String user = scanner.nextLine();
     System.out.println("Enter your username: ");
     String pass = scanner.nextLine();
     if(user.equals(userName) && pass.equals(password)){
        return true;
     }
     else{
        return false;
     }
   }
}

class Menu extends Counter{
    void showMenu(){
       Scanner input = new Scanner(System.in);
        boolean quit= false;
        int sum=0;
        String order="";
        
        do{
            System.out.println("ITEM"+"\t\tPrice");
            System.out.println("1.plane_cake"+"\t\t"+"100");
            System.out.println("2.cold_coffee"+"\t"+"150");
            System.out.println("3.juice"+"\t\t"+"30");
            System.out.println("4.ice_cake"+"\t\t"+"200");
            System.out.println("5.Quit");
            
            int choice=input.nextInt();
            
            switch(choice){
                case 1:System.out.println("plane_cake"+"\n");
                        sum=sum+plane_cake;
                        order=order.concat("plane_cake"+"\n");
                        
                    break;
                case 2:
                    System.out.println("cold_coffee");
                    sum=sum+cold_coffee;
                    order=order.concat("cold_coffee"+"\n");
                    
                    break;
                case 3:
                    System.out.println("juice");
                    sum=sum+juice;
                    order=order.concat("juice"+"\n");
                    break;

                case 4:
                    System.out.println("ice_cake");
                    sum=sum+ice_cake;
                    order=order.concat("ice_cake"+"\n");
                    break;
                case 5:
                    quit=true;
                     
                    break;
                default:
                    System.out.println("Wrong input");
            }
        
        }while(!quit);
       
        System.out.println("Your Orders are:\n"+order);
        System.out.println("Your total bill="+sum);
        System.out.println("Thank you");
    }
}


