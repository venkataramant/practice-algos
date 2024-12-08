package learn.j.concurrent;

import java.util.concurrent.Callable;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.ScheduledThreadPoolExecutor;
import java.util.concurrent.ThreadPoolExecutor;

public class CallablesMain {
	public static void main(String... args) {
		CompletableFuture<String> my;
		ThreadPoolExecutor tpe;
		ScheduledThreadPoolExecutor stpe;
		ExecutorService service = Executors.newSingleThreadExecutor();
		Future<String> future=service.submit(new MyCallable("MyName"));
		while(!future.isDone()) {
			try {
				Thread.currentThread().sleep(10);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		try {
			System.out.println(future+"..."+future.get());
		} catch (InterruptedException | ExecutionException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		service.shutdown();
	}
}

class MyCallable implements Callable<String> {

	String name;

	MyCallable(String name) {
		this.name = name;
	}

	@Override
	public String call() throws Exception {
		return "Hello " + this.name;
	}

}