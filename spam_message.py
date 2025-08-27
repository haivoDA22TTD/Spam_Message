import pyautogui
import time

def main():
    print("===== TOOL SPAM TIN NHẮN =====")
    message = input("Nhập nội dung tin nhắn: ")
    count = int(input("Nhập số lần gửi: "))
    delay = float(input("Nhập thời gian delay giữa mỗi lần gửi (giây): "))

    print("\nBạn có 5 giây để mở cửa sổ chat (Zalo, Messenger, Discord...)")
    time.sleep(5)

    for i in range(count):
        pyautogui.write(message)
        pyautogui.press("enter")
        time.sleep(delay)

    print("✅ Gửi xong!")

if __name__ == "__main__":
    main()
