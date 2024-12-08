package learn.jut.service;

import static org.junit.Assert.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.Before;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.powermock.api.mockito.PowerMockito;

import learn.jut.simple.dao.UserDAO;
import learn.jut.simple.service.UserService;

public class UserServiceTest {
	UserService userService = null;

	@BeforeEach
	public void initalize() {

	}

	@ParameterizedTest
	@ValueSource(ints = { 1, 3 })
	public void getNameTest(int id) {
		assertTrue(id > 0);
	}

	@Test
	public void checkName() {
		String capitalName = "myName";
		int id = 101;
		UserDAO userDao = PowerMockito.mock(UserDAO.class);
		userService = new UserService(userDao);
		PowerMockito.when(userDao.getNameById(id)).thenReturn(capitalName);
		System.out.print(userDao.getNameById(id));
		assertEquals(userService.getName(id), capitalName.toUpperCase());
	}
}
