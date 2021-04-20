// Program illustrating garbage collection in Java



class Student{
    int a;
    int b;

    public void setData(int c, int d){
	a=c;
	b=d;
    }
    public void showData(){
	System.out.println("Value of a = "+a);
	System.out.println("value of b = "+b);
    }
    public static void main(String args[]){
	Student s1 = new Student();
	Student s2 = new Student();
	s1.setData(1,2);
	s2.setData(3,4);
	s1.showData();
	s2.showData();

	Student s3;
	//values of s2 assigned to s3
	s3=s2;
	// now s3 references the memory referenced by s2
	// it can display that memory
	s3.showData();
	// s2 set to null but there's still on variable referencing (pointing to) the memory once references by s2
	s2=null;
	// So you can still see that data after s2 is set to null
	s3.showData();
	// now s3 Student object is set to null and the data becomes eligible for garbage collection
	//s3=null;
	// Now you cannot display that data as it has been deleting at/before runtime
	s3.showData();
    }
}


// If you want to make an object eligible for garbage collection assign its reference variable to null







