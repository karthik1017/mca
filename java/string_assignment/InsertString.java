import java.util.Scanner;
class InsertString{
    public static void main(String[] args) {
        String str1 = "Santosh is a good Teacher";
        String[] splitStr = str1.split("\\s+");
        String str2 = "very";
        Scanner s = new Scanner(System.in);
        System.out.println("Enter index you need to insert:");
        int n;
        n = s.nextInt();
        for(int i = (n-1); i >= (n-1); i--)
        {
            splitStr[i+1] = splitStr[i];
        }
        splitStr[n-1] = str2;
        System.out.print("After inserting:");
        str1 = String.join(" ",splitStr);
        System.out.println(str1);
    }
}