from utils import read_csv, print_table

def test_read_csv(tmp_path):
    csv_content = "name,age\nAlice,30\nBob,25\n"
    file = tmp_path / "test.csv"
    file.write_text(csv_content, encoding="utf-8")

    data = read_csv(str(file))
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["name"] == "Alice"
    assert data[1]["age"] == "25"

def test_print_table_with_data(capsys):
    data = [
        {"name": "Alice", "age": "30"},
        {"name": "Bob", "age": "25"}
    ]
    print_table(data)

    captured = capsys.readouterr()
    assert "name" in captured.out
    assert "Alice" in captured.out
    assert "Bob" in captured.out
    assert "age" in captured.out

def test_print_table_no_data(capsys):
    print_table([])

    captured = capsys.readouterr()
    assert captured.out.strip() == "Нет данных для отображения."