# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    print("      [ Movies currently showing ]")
    for i in movie_list:
        print(i['movie_name'], ':', i['ticket_price'])

# # ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
# def check_age(user_age, age_restriction):
#     if age_restriction == 'G':


# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    for movie in movies:
        if movie['genre'] == 'Sci-Fi':
            ticket_price = base_price + 50

# # ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
# def buy_ticket(movie_list):
#     # TODO: 
#     # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
#     # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
#     # 3. รับอายุผู้ใช้
#     # 4. ตรวจสอบอายุผ่าน check_age
#     #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
#     # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
#     # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
#     # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว

def main():
    while True:
        movies = [
            {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
            {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
            {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
            {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
            {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
        ]

        print("      ------ Main Menu ------")
        print("1) Movies Available")
        print("2) Purchase tickets")
        menuChoice = int(input("Awaiting input...: "))

        if menuChoice == 1:
            show_movies(movies)
        elif menuChoice == 2:
            buy_ticket(movies)
        else:
            print("Error: Invalid Input")

# เรียก main เพื่อเริ่มโปรแกรม
main()