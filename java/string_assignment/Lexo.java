import java.util.Arrays;
class Lexo{
    public static void main(String[] args) {
        String[] str = {"Santosh", "Suraj", "Sudhanva", "Shreedhar", "Sushma", "Smita"};
        Arrays.sort(str);
        System.out.println("sorted array is as follows");
        for(int i = 0; i < str.length; i++){
            System.out.println(str[i]);
        }
    }
}