package learn.jut.simple.dao;

import learn.jut.simple.model.User;

public interface UserDAO {
	public String getNameById(int id);
	public User getUserById(int id);

}
