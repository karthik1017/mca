class StringReplace{
    public static void main(String[] args) {
        String str1 = "Santhosh is a good boy";
        String str2 = "teacher";
        str1 = str1.replace("boy",str2);
        System.out.println("the string after replacement:");
        System.out.print(str1);
    }
}