package tvr.learn.java8.annotations;

@FunctionalInterface
public interface MyFunctionalInterface<T> {
	boolean isBigger(T t1, T t2);
}
