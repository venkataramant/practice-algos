package learn.j.java5.annotations;

import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
//@Target(ElementType.ANNOTATION_TYPE)
public @interface MyRuntimeAnnotations {
	String myName() default "me";

	int myValue() default 0;
}
