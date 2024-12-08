package learn.jut.simple.service;

import learn.jut.simple.dao.UserDAO;
import lombok.Getter;
import lombok.Setter;

@Getter
public class UserService {
	private UserDAO userDAO;

	public UserService(UserDAO userDAO) {
		this.userDAO = userDAO;
	}

	public String getName(int id) {
		String name = userDAO.getNameById(id);
		return name.toUpperCase();
	}
}
