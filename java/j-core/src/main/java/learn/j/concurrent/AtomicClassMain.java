package learn.j.concurrent;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.stream.IntStream;

public class AtomicClassMain {
	private AtomicInteger aI = new AtomicInteger(0);
	private AtomicInteger aJ = new AtomicInteger(0);

	public void incrementI() {
		System.out.println("inside incrementI " + aI);

		System.out.println("After incrementI " + aI.incrementAndGet());
	}

	public void increment(int index) {
		System.out.println("started_thread::" + index);
		if (index % 2 == 0) {
			incrementI();
		} else {
			incrementJ();
		}
		System.out.println("completed_thread::" + index);
	}

	public void incrementJ() {
		System.out.println("inside incrementJ " + aJ);

		System.out.println("After incrementJ " + aJ.incrementAndGet());
	}

	public Integer fetchI() {
		return aI.get();
	}

	public Integer fetchJ() {
		return aJ.get();
	}

	public static void main(String[] args) throws InterruptedException {
		AtomicClassMain obj = new AtomicClassMain();
		ExecutorService service = Executors.newFixedThreadPool(4);
		IntStream.range(0, 10).forEach(x -> service.submit(() -> obj.increment(x)));
		Thread.sleep(2000);
		System.out.println(obj.fetchI() + "..." + obj.fetchJ());
	}

}
