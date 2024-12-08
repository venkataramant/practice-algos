package learn.j.collectoins;

class Student implements Comparable<Student> {
	private String name;
	private int id;
	private int age;

	public Student(int id, String name, int age) {

		this.setId(id);
		this.setName(name);
		this.setAge(age);
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	@Override
	public String toString() {
		return "Id:: " + id + " Name:: " + name + " Age::" + age + "\n";
	}

	@Override
	public int compareTo(Student o) {
		if (o != null) {
			return Integer.compare(this.getId(), o.getId());
		}
		return this.getId();
	}

}