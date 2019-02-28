import java.io. *;
class Student2{
	double cgpa;
	String name;
	public Student2(){
		this("karthik",9.36);
	}
	public Student2(String n,double c){
		cgpa = c;
		name = n;
	}
	public void display(){
	  System.out.println("name is: "+name);
      System.out.println("cgpa is: "+cgpa);
	}
	public static void main(String[] args) {
	  Student2 stu = new Student2();
	  stu.display();
	}
}