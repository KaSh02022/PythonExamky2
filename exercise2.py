
import os
import pandas as pd

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.csv")

def main():
    df = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5, 6],
            "name": ["Quach Loan", "Quach Ngoc", "Cao Son", "Tuan Kiet", "Ngo Lam", "Duy Khanh"],
            "age": [19, 20, 21, 19, 22, 20],
            "score": [8.5, 4.0, 7.5, 9.0, 5.0, 3.5],
        }
    )

    df.to_csv(CSV_PATH, index=False)
    print(f"Đã lưu dữ liệu vào {CSV_PATH}")

    data = pd.read_csv(CSV_PATH)

    print("\n=== Tất cả sinh viên ===")
    print(data.to_string(index=False))

    print("\n=== Sinh viên có score >= 8 ===")
    print(data[data["score"] >= 8].to_string(index=False))

    print(f"\n=== Điểm trung bình: {data['score'].mean():.2f} ===")

    data["result"] = data["score"].apply(lambda s: "Pass" if s >= 5 else "Fail")
    print("\n=== Dữ liệu sau khi thêm cột result ===")
    print(data.to_string(index=False))


if __name__ == "__main__":
    main()
