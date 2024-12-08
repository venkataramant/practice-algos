package learn.j.concurrent;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ExecutorsMain {
	public static void main(String... args) {
		System.out.println("Available Processors::"+Runtime.getRuntime().availableProcessors());
		ExecutorService executorService = Executors.newFixedThreadPool(10);
		for (int i = 0; i < 100; i++) {
			executorService.execute(new MyTask(i));
		}
		System.out.println("thread Name::" + Thread.currentThread().getName());
	}
}

class MyTask implements Runnable {
	int threadNumber;

	MyTask(int threadNumber) {

		this.threadNumber = threadNumber;
	}

	@Override()
	public void run() {
		System.out.println("Running my Task threadNumber:: " + threadNumber);
	}
}