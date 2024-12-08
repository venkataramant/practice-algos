package learn.j.concurrent;

import java.util.concurrent.Callable;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;

public class CompletableFutureMain {
	public static void main(String... args) {
		CompletableFuture<ByeTask> results = CompletableFuture.supplyAsync(() -> new HelloTask("MyName"))
				.thenApply(name -> new ByeTask(name));
		try {
			while (!results.isDone()) {

				Thread.sleep(30);

			}
			System.out.println(results.get());
		} catch (ExecutionException | InterruptedException e) {
			System.out.println(e);
		}
	}
}

class HelloTask implements Callable<String> {

	String name;

	HelloTask(String name) {
		this.name = name;
	}

	@Override
	public String call() throws Exception {
		System.out.println("execuitng hello");
		return "Hello " + this.name;
	}

}

class ByeTask implements Callable<String> {

	HelloTask name;

	ByeTask(HelloTask name2) {
		System.out.println("execuitng bye");
		this.name = name2;
	}

	@Override
	public String call() throws Exception {
		return "Bye " + this.name;
	}

}