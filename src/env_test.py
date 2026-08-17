# Environment test script, verify Python environment and VSCode debugger
def test_env():
    a = 10
    b = 20
    result = a + b
    print(f"Environment test success! a+b = {result}")
    return result

if __name__ == "__main__":
    test_env()
