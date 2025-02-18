import task1

# This function will test the output of the main function, capture the console output, and see if it matches the hello world output.
def test_main_output(capsys):
    task1.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"