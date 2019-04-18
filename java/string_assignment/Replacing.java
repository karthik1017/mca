class Replacing{
    public static void main(String[] args){
        String name = "santhosh";
        char[] nameChars = name.toCharArray();
        nameChars[0] = 'k';
        name = String.valueOf(nameChars);
        System.out.println("the string after replacement:");
        System.out.println(name);
    }
}