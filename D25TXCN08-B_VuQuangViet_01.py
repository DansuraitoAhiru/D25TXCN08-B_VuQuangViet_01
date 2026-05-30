import json

student_list = []

with open("data.json", "r", encoding="utf-8") as file:
    student_list = json.load(file)

while True:
    choice = input("""\n===== QUẢN LÝ SINH VIÊN =====
1. Hiển thị danh sách sinh viên
2. Thêm mới sinh viên
3. Cập nhật sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên
6. Sắp xếp danh sách sinh viên
7. Thống kê điểm TB
8. Liệt kê sinh viên điểm cao nhất/thấp nhất
9. Phân loại học lực sinh viên
10. Thoát 
Nhập lựa chọn: """).strip()

    match choice:
        case "1":
            if len(student_list) == 0:
                print("Danh sách đang trống")
                continue

            print(f"\n{'Mã SV':<10} | {'Tên':<25} | {'Toán':<6} | {'Lý':<6} | {'Hóa':<6} | {'TB':<10} | {'Xếp loại'}")
            print("-" * 96)
            for student in student_list:
                print(f"{student['id']:<10} | {student['ten']:<25} | {student['diem_toan']:<6} | {student['diem_ly']:<6} | {student['diem_hoa']:<6} | {student['diem_tb']:<10} | {student['xep_loai']}")

        case "2":
            while True:
                student_id = input("Nhập mã sinh viên mới: ").upper().strip()
                
                if student_id == "":
                    print("Ko được để trống")
                    continue

                if any(student["id"] == student_id for student in student_list):
                    print("Mã sinh viên đã tồn tại!")
                    continue
                break

            while True:
                name = input("Nhập tên: ").title().strip()
                if name == "":
                    print("Ko được để trống")
                    continue
                break

            while True:
                math_score = input("Nhập điểm Toán: ").strip()

                if not math_score.lstrip("-").replace(".", "", 1).isdigit():
                    print("Vui lòng nhập số!")
                    continue

                math_score = float(math_score)

                if math_score < 0 or math_score > 10:
                    print("Điểm phải nằm trong khoảng 0-10")
                    continue
                break

            while True:
                physic_score = input("Nhập điểm Lý: ").strip()

                if not physic_score.lstrip("-").replace(".", "", 1).isdigit():
                    print("Vui lòng nhập số!")
                    continue

                physic_score = float(physic_score)
                if 0 > physic_score or physic_score > 10:
                    print("Điểm phải nằm trong khoảng 0-10")
                    continue
                break

            while True:
                chemistry_score = input("Nhập điểm Hóa: ").strip()

                if not chemistry_score.lstrip("-").replace(".", "", 1).isdigit():
                    print("Vui lòng nhập số!")
                    continue

                chemistry_score = float(chemistry_score)

                if 0 > chemistry_score or chemistry_score > 10:
                    print("Điểm phải nằm trong khoảng 0-10")
                    continue
                break

            avg_score = round((math_score + physic_score + chemistry_score) / 3, 2)

            if avg_score < 5:
                ranking = "Yếu"
            elif avg_score < 7:
                ranking = "Trung Bình"
            elif avg_score < 8:
                ranking = "Khá"
            else:
                ranking = "Giỏi"

            student_list.append({
                "id": student_id,
                "ten": name,
                "diem_toan": math_score,
                "diem_ly": physic_score,
                "diem_hoa": chemistry_score,
                "diem_tb": avg_score,
                "xep_loai": ranking
            })

            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(student_list, file, ensure_ascii=False, indent=4)

            print("Thêm thành công!")

        case "3":
            while True:
                update_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()

                if update_id == "":
                    print("Ko được để trống")
                    continue
                break

            for student in student_list:
                if student["id"] == update_id:
                    while True:
                        new_math_score = input("Nhập điểm Toán: ").strip()

                        if not new_math_score.lstrip("-").replace(".", "", 1).isdigit():
                            print("Vui lòng nhập số!")
                            continue

                        new_math_score = float(new_math_score)

                        if new_math_score < 0 or new_math_score > 10:
                            print("Điểm phải nằm trong khoảng 0-10")
                            continue
                        break

                    while True:
                        new_physic_score = input("Nhập điểm Lý: ").strip()

                        if not new_physic_score.lstrip("-").replace(".", "", 1).isdigit():
                            print("Vui lòng nhập số!")
                            continue

                        new_physic_score = float(new_physic_score)
                        if 0 > new_physic_score or new_physic_score > 10:
                            print("Điểm phải nằm trong khoảng 0-10")
                            continue
                        break

                    while True:
                        new_chemistry_score = input("Nhập điểm Hóa: ").strip()

                        if not new_chemistry_score.lstrip("-").replace(".", "", 1).isdigit():
                            print("Vui lòng nhập số!")
                            continue

                        new_chemistry_score = float(new_chemistry_score)

                        if 0 > new_chemistry_score or new_chemistry_score > 10:
                            print("Điểm phải nằm trong khoảng 0-10")
                            continue
                        break

                    student["diem_toan"] = new_math_score
                    student["diem_ly"] = new_physic_score
                    student["diem_hoa"] = new_chemistry_score

                    student["diem_tb"] = round((student["diem_toan"] + student["diem_ly"] + student["diem_hoa"]) / 3, 2)

                    if student["diem_tb"] < 5:
                        student["xep_loai"] = "Yếu"
                    elif student["diem_tb"] < 7:
                        student["xep_loai"] = "Trung Bình"
                    elif student["diem_tb"] < 8:
                        student["xep_loai"] = "Khá"
                    else:
                        student["xep_loai"] = "Giỏi"

                    with open("data.json", "w", encoding="utf-8") as file:
                        json.dump(student_list, file, ensure_ascii=False, indent=4)

                    print("Cập nhật thành công!")
                    break
            else: 
                print("Ko tìm thấy mã sinh viên cần cập nhật")

        case "4":
            while True:
                delete_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()

                if delete_id == "":
                    print("Ko được để trống")
                    continue
                break

            for student in student_list:
                if student["id"] == delete_id:
                    while True:
                        confirm = input("Bạn có chắc muốn xóa? (Y/N): ").upper().strip()

                        if confirm == "Y":
                            student_list.remove(student)

                            with open("data.json", "w", encoding="utf-8") as file:
                                json.dump(student_list, file, ensure_ascii=False, indent=4)

                            print("Đã xóa!")
                            break

                        elif confirm == "N":
                            print("Đã hủy thao tác xóa!")
                            break

                        else:
                            print("Lựa chọn không hợp lệ! Vui lòng nhập Y hoặc N.")
                    break
            else:
                print("Ko tìm thấy mã sinh viên cần xóa")

        case "5":
            while True:
                keyword = input("Nhập tên hoặc mã student: ").strip()

                if keyword == "":
                    print("Ko được để trống")
                    continue
                break

            found = False

            print(f"\n{'Mã SV':<10} | {'Tên':<25} | {'Toán':<6} | {'Lý':<6} | {'Hóa':<6} | {'TB':<10} | {'Xếp loại'}")
            print("-" * 96)
            for student in student_list:
                if keyword.lower() == student["id"].strip().lower() or keyword.lower() in student["ten"].lower():
                    print(f"{student['id']:<10} | {student['ten']:<25} | {student['diem_tb']:<10} | {student['xep_loai']}")
                    found = True

            if not found:
                print("Ko tìm thấy sinh viên")

        case "6":
            sub_choice = input('''\n1. Điểm TB giảm dần
2. Tên tăng dần (A-Z)
Nhập lựa chọn: ''').strip()

            match sub_choice:
                case "1":
                    student_list.sort(key=lambda x: x["diem_tb"], reverse=True)
                    print("Đã sắp xếp theo điểm giảm dần! Chọn 1 để xem")

                case "2":
                    student_list.sort(key=lambda x: x["ten"])
                    print("Đã sắp xếp theo tên tăng dần (A-Z)! Chọn 1 để xem")

                case _:
                    print("Lựa chọn ko hợp lệ! Vui lòng nhập 1 hoặc 2")

        case "7":
            good = enough = mid = poor = 0

            for student in student_list:
                match student["xep_loai"]:
                    case "Giỏi":
                        good += 1

                    case "Khá":
                        enough += 1

                    case "Trung Bình":
                        mid += 1

                    case "Yếu":
                        poor += 1

            print(f"Số lượng sinh viên giỏi: {good}")
            print(f"Số lượng sinh viên khá: {enough}")
            print(f"Số lượng sinh viên TB: {mid}")
            print(f"Số lượng sinh viên yếu: {poor}")

        case "8":
            if len(student_list) == 0:
                print("Danh sách trống!")

            else:
                max_student = student_list[0]
                min_student = student_list[0]

                for student in student_list:

                    if student["diem_tb"] > max_student["diem_tb"]:
                        max_student = student

                    if student["diem_tb"] < min_student["diem_tb"]:
                        min_student = student

                print(f"Sinh viên có điểm TB cao nhất: {max_student}")
                print(f"Sinh viên có điểm TB thấp nhất: {min_student}")

        case "9":
            for student in student_list:
                if student["diem_tb"] < 5:
                    student["xep_loai"] = "Yếu"

                elif student["diem_tb"] < 7:
                    student["xep_loai"] = "Trung Bình"

                elif student["diem_tb"] < 8:
                    student["xep_loai"] = "Khá"

                else:
                    student["xep_loai"] = "Giỏi"

            print("Đã phân loại lại học lực!")

        case "10":
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ!")