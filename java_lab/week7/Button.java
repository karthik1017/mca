import java.io. *;
import java.util. *;
abstract class Button{
    abstract void caption();
    void buttonProperty(){
        String b_color,b_font,b_edges,b_outline;
        int b_height,b_width,font_size;
        b_height = 1;
        b_width = 4;
        font_size = 11;
        b_color = "green color";
        b_font = "verdana";
        b_edges = "round edges";
        b_outline = "black"; 
        System.out.printf("color = "+ b_color + "\n" );
        System.out.printf("font = " + b_font + "\n" );
        System.out.printf("edges = " + b_edges + "\n" );
        System.out.printf("outline = " + b_outline + "\n" );
        System.out.printf("height = " + b_height + "\n" );
        System.out.printf("width = " + b_width + "\n" );
        System.out.printf("font = " + font_size + "\n" );
    }
}
class ButtonReservation extends Button{
    void caption(){
       String caption;
       caption = "reserve";
       System.out.println("caption = "+ caption);
    }
}
class ButtonCancelation extends Button{
    void caption(){
        String caption;
        caption = "cancel";
        System.out.println("caption = "+ caption);
     }
}

class Form{
    public static void main(String[] args) {
        ButtonReservation r = new ButtonReservation();
        System.out.println("reservation form ");
        r.buttonProperty();
        r.caption();

        ButtonCancelation c = new ButtonCancelation();
        System.out.println("cancelation form ");
        c.buttonProperty();;
        c.caption();



    }
}