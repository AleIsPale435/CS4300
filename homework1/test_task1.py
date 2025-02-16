# test_task1.py
import task1

def test_main_output(capsys):
    task1.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"