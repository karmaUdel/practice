package com.lynda.javatraining.threads;

public class MyThread extends Thread {

	@Override
	public void run() {

		try {
			sleep(2000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}

	}

}
