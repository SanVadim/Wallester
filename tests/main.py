import pytest

def run_all_tests():
    # Здесь args - это аргументы, которые вы бы передали pytest в командной строке.
    # Например, '.' указывает pytest запустить все тесты в текущем каталоге
    args = ['C:\\Users\\vadja\\Wallester\\tests\\api_1.py']
    
    pytest.main(args)

if __name__ == "__main__":
    run_all_tests()