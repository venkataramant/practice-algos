package tvr.learn.design_pattern.solid.open_closed;

public class NewNotificationService extends NotificationService {
	@Override
	public void notify(String notee, String message,String type) throws Exception {
		if (type=="3") {
			System.out.println("Doing it in NewWay 3rd");
		}else {
			super.notify(notee, message, type);
		}
	}
}