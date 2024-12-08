package tvr.learn.design_pattern.solid.open_closed;

public class NotificationService {

	public void notify(String notee,String message,String type) throws Exception {
		if (type=="1") {
			System.out.println("doing it 1st way");
		}else if (type=="2") {
			System.out.println("doing it in 2nd way");
		}else {
			String errorMsg="Unknown way";
			System.out.println(errorMsg);
			throw new Exception (errorMsg);
		}
	}
}