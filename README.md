# 🚀 Tool Spam Tin Nhắn Tự Động bằng Python

---

## 📄 Mô tả

Tool giúp bạn **tự động gửi tin nhắn** nhiều lần vào cửa sổ chat đang mở (Zalo, Messenger, Discord, ...). Bạn nhập nội dung, số lần gửi, thời gian delay — tool sẽ giả lập gõ phím và gửi tin nhắn tự động.

---

## ⚠️ Lưu ý quan trọng

- **Chỉ dùng hợp pháp, có sự đồng ý người nhận.**
- Tránh gửi tin nhắn quá nhanh, dễ bị khóa tài khoản.
- Nên test trước với “Cloud của tôi” trên Zalo hoặc chat với chính bạn.
- Delay khuyến nghị: **≥ 0.5 giây**.

---

## 🛠️ Yêu cầu

- Python 3.x
- Thư viện `pyautogui`

---


## 📥 Clone dự án

Mở terminal hoặc command prompt và chạy lệnh sau để tải project về máy:

```bash
git clone https://github.com/haivoDA22TTD/Spam_Message.git
cd Spam_Message
```
### 🪟 Windows

 Cài thư viện pyautogui:  
   ```bash
   pip install pyautogui
  ```
Chạy tool:

```bash
python spam_message.py
```
### 🍎 macOS

Cài Python (nếu chưa có):
https://www.python.org/downloads/mac-osx/

Mở Terminal (Cmd + Space, gõ Terminal).

Cài pyautogui:
```bash
pip3 install pyautogui
```

Chạy tool:
```bash
python3 spam_message.py
```
### 🐧 Linux (Ubuntu/Debian)

Cài Python 3 và pip (nếu chưa có):
```bash
sudo apt update
sudo apt install python3 python3-pip git
```
Cài pyautogui:
```bash
pip3 install pyautogui
```

Chạy tool:
```bash
python3 spam_message.py
```
