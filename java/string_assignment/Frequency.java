class Frequency{
    public static void main(String[] args) {
        String str = "Santosh and Anand are sanskrit terms meaning happiness. The difference is Santosh is the happiness that spreads and Anand is the happiness that is felt by one-self.  Santosh enhances by giving and Anand enhances by involving. Anology: A person eats a chocolate and relishes its taste, and this is Anand, a feeling when you involve. You gift chocolate to your friend who likes it and when you see the joy on your friends face, you feel Santosh, a feeling of spreading happiness.";
        String[] splitStr = str.split("\\s+");
        String findStr = "Anand";
        int count = 0;
        for(int i = 0;i < splitStr.length; i++){
            if(splitStr[i].equals(findStr)){
                count++;
            }
        }
        System.out.println("the frequency of the given word is: "+ count);
    }
}