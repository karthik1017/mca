import java.io. *;
import java.util. *;
abstract class Computer{
    void create(){

    }
    void delete(){

    }
    void retrive(){

    }
    void update(){

    }
    abstract specialfeatures();
}
class HomePC extends Computer{
    void specialfeatures(){

    }
}
class WebServer extends Computer{
    void specialfeatures(){

    }
}
class SmartPhones extends Computer{
    void specialfeatures(){

    }
}
class System{
    public static void main(String[] args) {
        HomePC h = new HomePC();
        
        WebServer w = new WebServer();
        SmartPhones s = new SmartPhones();

    }
}