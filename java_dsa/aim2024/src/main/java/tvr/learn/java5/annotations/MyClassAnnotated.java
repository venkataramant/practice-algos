package tvr.learn.java5.annotations;

@MyRuntimeAnnotations(myName = "myAnnotationExample", myValue = 99)
public class MyClassAnnotated{

	@MyRuntimeAnnotations(myName ="myMethodName",myValue = 200 )
	public void myMethod() {
		
	}
}