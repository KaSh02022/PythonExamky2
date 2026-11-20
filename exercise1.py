
def input_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Giá trị phải lớn hơn 0.")
        except ValueError:
            print("Nhập một số nguyên.")

def input_salary(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Lương không được âm.")
        except ValueError:
            print("Nhập một số hợp lệ.")

def input_employees(n):
    employees = []
    for i in range(1, n + 1):
        print(f"\n--- Nhân viên {i} ---")
        while True:
            emp_id = input("Employee ID: ").strip()
            if not emp_id:
                print("ID không được để trống.")
            elif any(e["id"] == emp_id for e in employees):
                print("ID đã tồn tại, nhập ID khác.")
            else:
                break
        while True:
            name = input("Full name: ").strip()
            if name:
                break
            print("Tên không được để trống.")
        salary = input_salary("Salary: ")
        employees.append({"id": emp_id, "name": name, "salary": salary})
    return employees

def display_employees(employees, title):
    print(f"\n=== {title} ===")
    if not employees:
        print("(Không có nhân viên nào)")
        return
    print(f"{'ID':<10}{'Full name':<25}{'Salary':>15}")
    for e in employees:
        print(f"{e['id']:<10}{e['name']:<25}{e['salary']:>15,.2f}")

def main():
    n = input_positive_int("Nhập số lượng nhân viên: ")
    employees = input_employees(n)

    display_employees(employees, "Tất cả nhân viên")

    max_salary = max(e["salary"] for e in employees)
    top = [e for e in employees if e["salary"] == max_salary]
    display_employees(top, "Nhân viên có lương cao nhất")

    average = sum(e["salary"] for e in employees) / len(employees)
    print(f"\n=== Lương trung bình: {average:,.2f} ===")

    rich = [e for e in employees if e["salary"] > 10000]
    display_employees(rich, "Nhân viên có lương > 10,000")

if __name__ == "__main__":
    main()
