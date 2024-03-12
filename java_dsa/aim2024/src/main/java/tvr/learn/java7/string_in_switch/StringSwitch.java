package tvr.learn.java7.string_in_switch;

enum Day {
	Monday("mon");

	final String val;

	Day(String val) {
		this.val = val;
	}

}

public interface StringSwitch {
	public static final String DAY1="moon";
	static void testStringSwitch(String day) {
		String myvalue = "moon";
		switch (day.toLowerCase()) {
		case "mon":
		case DAY1:
		case "monday":
			System.out.println("This is Monday");
			break;
		case "tue":
		case "tues":
		case "tuesday":
			System.out.println("This is Tuesday");
			break;
		case "wed":
		case "wednes":
		case "wednesday":
			System.out.println("This is Wednesday");
			break;
		case "thur":
		case "thurs":
		case "thursday":
			System.out.println("This is Thursday");
			break;
		case "fri":
		case "friday":
			System.out.println("This is Friday");
			break;
		case "sat":
		case "satur":
		case "saturday":
			System.out.println("This is Saturday");
			break;
		default:
			System.out.println("Wow, is it Sunday or None");

		}
	}
}