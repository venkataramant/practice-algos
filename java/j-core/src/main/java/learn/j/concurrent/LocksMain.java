package learn.j.concurrent;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.stream.IntStream;

public class LocksMain {
	private int i;
	private int j;
	Lock lock1 = new ReentrantLock();
	Lock lock2 = new ReentrantLock();

	public void incrementI() {
		System.out.println("inside incrementI " + i);
		lock1.lock();
		i++;
		lock1.unlock();
		System.out.println("After incrementI " + i);
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
		System.out.println("inside incrementJ " + j);
		lock2.lock();
		j++;
		lock2.unlock();
		System.out.println("After incrementJ " + j);
	}

	public Integer fetchI() {
		return i;
	}

	public Integer fetchJ() {
		return j;
	}

	public static void main(String[] args) throws InterruptedException {
		LocksMain obj = new LocksMain();
		ExecutorService service = Executors.newFixedThreadPool(4);
		IntStream.range(0, 10).forEach(x -> service.submit(() -> obj.increment(x)));
		Thread.sleep(2000);
		System.out.println(obj.fetchI() + "..." + obj.fetchJ());
	}

}
