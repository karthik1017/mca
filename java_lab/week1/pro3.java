import java.io. *;
class Student1{
	double cgpa;
	String name;
	public Student1(String n,double c){
		cgpa = c;
		name = n;
	}
	public void display(){
	  System.out.println("name is: "+name);
      System.out.println("cgpa is: "+cgpa);
	}
	public static void main(String[] args) {
	  Student1 stu = new Student1("karthik",9.36);
	  stu.display();
	}
}