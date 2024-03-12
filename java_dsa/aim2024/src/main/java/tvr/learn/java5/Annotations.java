package tvr.learn.java5;

import static java.lang.System.out;

import java.lang.annotation.Annotation;
import java.lang.reflect.Method;

import tvr.learn.java5.annotations.MyClassAnnotated;
import tvr.learn.java5.annotations.MyRuntimeAnnotations;

/*
 * Annotation is Metadata to provide an intention to compile and compiler 
 * will check those intentions are followed or any violations.
 * Ex:
 *  @override(Method)
 *  @Depreciated(Class/Method)
 *  @Functional(Interface)
 * Retension
 */
public class Annotations {
	public static void main(String... args) {
		Annotations annotations = new Annotations();
		out.println(annotations);
		MyClassAnnotated mca = new MyClassAnnotated();
		Class mcaClass = mca.getClass();
		
		Annotation mra2 = mcaClass.getAnnotation(MyRuntimeAnnotations.class);
		out.println(mra2);
		if (mra2 != null) {
			out.printf("Class level name %s value %d\n", ((MyRuntimeAnnotations) mra2).myName(),
					((MyRuntimeAnnotations) mra2).myValue());
		}

		try {
			Method myMethod = mcaClass.getMethod("myMethod");
			mra2 = myMethod.getAnnotation(MyRuntimeAnnotations.class);
			
			
			out.println(mra2);
			if (mra2 != null) {
				out.printf("Method Level name %s value %d\n", ((MyRuntimeAnnotations) mra2).myName(),
						((MyRuntimeAnnotations) mra2).myValue());
			}
		} catch (NoSuchMethodException | SecurityException e) {
			out.println(e);
		}

	}

	@Override
	public String toString() {
		return "Annotation is introduced in Java5";
	}

}
