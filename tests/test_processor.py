import pandas as pd
from app.processor import compute_mean

def test_compute_mean(tmp_path):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    file_path = tmp_path / "test.csv"
    df.to_csv(file_path, index=False)

    result = compute_mean(file_path)
    assert result["a"] == 2
    assert result["b"] == 5
