import java.io. *;

class Student3{
	double cgpa;
	String name;
	public Student3(){
		this("karthik",9.36);
	}
	public Student3(String n,double c){
		cgpa = c;
		name = n;
	}
	public void display(){
	  System.out.println("name is: "+name);
      System.out.println("cgpa is: "+cgpa);
	}
	public static void main(String[] args) {
	  Student3 stu = new Student3();
	  stu.display();
	}
}

class Student4{
	double cgpa;
	String name;
	public Student4(String n,double c){
		cgpa = c;
		name = n;
	}
	public void display(){
	  System.out.println("name is: "+name);
      System.out.println("cgpa is: "+cgpa);
	}
	public static void main(String[] args) {
	  Student4 stu = new Student4("ramesh",9.36);
	  stu.display();
	}
}

