import java.io. *;
import java.util. *;
class Island{
	Island i;
	public static void main(String[] args) {
		Island i1 = new Island();
		Island i2 = new Island();
		i1.i = i2;
		i2.i = i1;
		System.out.println("now none of objects is eligible for garbage collection");
		i1 = null;
		i2 = null;
		System.out.println("now both the object is eleigible for garbage collection");
		System.out.println("now calling garbage collector Function");
		System.gc();
	}
}