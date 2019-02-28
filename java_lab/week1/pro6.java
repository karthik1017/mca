import java.io. *;
class Student5{
	double cgpa;
	String name;
	public Student5(String n,double c){
		cgpa = c;
		name = n;
	}
	public void display(){
	  System.out.println("name is: "+name);
      System.out.println("cgpa is: "+cgpa);
	}
	public static void main(String[] args) {
	  Student5 stu = new Student5("karthik",9.36);
	  stu.display();
	}
	public static void main() {
	  System.out.println("hello world");
    }
}

