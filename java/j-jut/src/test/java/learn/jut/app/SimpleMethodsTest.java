package learn.jut.app;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.Optional;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.RepeatedTest;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.TestInstance.Lifecycle;
import org.junit.jupiter.api.extension.ExtensionContext;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.ArgumentsProvider;
import org.junit.jupiter.params.provider.ArgumentsSource;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.ValueSource;

import learn.jut.simple.SimpleMethods;

/**
 * Unit test for simple App.
 */
@TestInstance(value = Lifecycle.PER_CLASS)
public class SimpleMethodsTest {
	SimpleMethods sm;

	@BeforeAll
	public void initialize() {
		sm = new SimpleMethods();
	}

	@ParameterizedTest
	@CsvSource(value = { "10,10", "10,10" })
	public void addTest() {
		Integer i1 = 4;
		Integer i2 = 5;
		Integer iNull = null;
		assertTrue(i1 + i2 == sm.add(Optional.of(i1), Optional.of(i2)));
		assertEquals(Integer.valueOf(i1 + i2), sm.add(Optional.of(i1), Optional.of(i2)));
	}

	public void addTestFail(Integer i1, Integer i2) {
		assertTrue(i1 + i2 == sm.add(Optional.of(i1), Optional.of(i2)));
		assertEquals(Integer.valueOf(i1 + i2), sm.add(Optional.of(i1), Optional.of(i2)));
	}

	@ParameterizedTest
	@ValueSource(ints = { 1, 4, 3 })
	public void addTestNPE(int iValue) {
		Integer i1 = null;
		Integer i2 = Integer.valueOf(iValue);
		assertThrows(NullPointerException.class, () -> sm.add(Optional.of(i1), Optional.of(i2)));
	}

	@ParameterizedTest
	@MethodSource("methodSource1")
	public void addTestNPE(Integer i2) {
		Integer i1 = null;
		assertThrows(NullPointerException.class, () -> sm.add(Optional.of(i1), Optional.of(i2)));
	}

	@ParameterizedTest
	@ArgumentsSource(MyArgumentProvider.class)
	public void addTestNPE2(Integer i1, Integer i2) {
		assertThrows(NullPointerException.class, () -> sm.add(Optional.of(i1), Optional.of(i2)));
	}

	@RepeatedTest(name = "test", value = 4)
	public void shouldAnswerWithTrue() {
		assertTrue(true);
	}

	public IntStream methodSource1() {
		return IntStream.builder().add(new Integer(4)).build();
	}

	static class MyArgumentProvider implements ArgumentsProvider {

		@Override
		public Stream<? extends Arguments> provideArguments(ExtensionContext context) throws Exception {
			return Stream.of(Arguments.of(2, null), Arguments.of(null, 2), Arguments.of(null, null));
		}

	}
}
