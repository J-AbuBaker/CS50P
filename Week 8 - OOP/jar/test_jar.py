from jar import Jar
import pytest

def test_init():
    cookies_jar = Jar(30)
    assert cookies_jar.capacity == 30

    cookies_jar = Jar()
    assert cookies_jar.capacity == 12

    with pytest.raises(ValueError):
        cookies_jar = Jar(-12)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    cookies_jar = Jar()
    cookies_jar.deposit(5)
    assert cookies_jar.size == 5
    cookies_jar.deposit(5)
    assert cookies_jar.size == 10

    with pytest.raises(ValueError):
        cookies_jar.deposit(5)

def test_withdraw():
    cookies_jar = Jar()
    cookies_jar.deposit(10)
    cookies_jar.withdraw(5)
    assert cookies_jar.size == 5

    with pytest.raises(ValueError):
        cookies_jar.withdraw(7)
