# Main prints out hello world.
def main():
    print("Hello, World!")


# This function will test the output of the main function, capture the console output, and see if it matches the hello world output.
def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"

