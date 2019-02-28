import java.io. *;
class Student{
	String name = "karthik";
	double cgpa = 9.36;
	public void diplay(){
	  System.out.println("name is: "+name);
      System.out.println("cgpa is: "+cgpa);
	}
	public static void main(String args[]){
		Student stu = new Student();
		stu.diplay();
	}
}