from app.processor import compute_mean

if __name__ == "__main__":
    path = "data.csv"
    result = compute_mean(path)
    print("Column means:", result)
