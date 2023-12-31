# Import thư viện CustomTkinter
import customtkinter as ctk
import tkinter.messagebox
from PIL import Image, ImageTk
import smtplib
import random
import string
import os
from datetime import datetime

login_lock = False
WINDOW_SIZES = [(1280,720),(768,432)]
WINDOW_SIZES_INDEX = 0
ratio = WINDOW_SIZES[WINDOW_SIZES_INDEX][0]/1536
email = None
code = None
# Các khai báo cho biến toàn cục
login_lock = False
# img = fp.find_images('assets/player') # Kiểm tra file được tìm thấy không
img_label = None
# confirm_button = None Nút xác nhận được gắn hàm kiểm tra trong FindPicture.py (hiện bị disable)
bg_color = "#2b95d1"
image_load_path = None
user_id, user_money = None, None

def fileread(username):
    global user_id, user_money
    with open(f"assets/player/{username}/{username}.txt") as f:
        lines = f.readlines()
        user_id = username
        user_money = lines[1]
        return user_id, user_money
class LoginMenu:
    def __init__(self,root):
        # Tạo một cửa sổ mới với kích thước 1536x864 px và màu nền trắng
        self.window = root
        self.window.geometry(f'1280x720+128+72')
        # Tạo hình ảnh 
        self.background = Image.open("./main/image.png")
        self.photo_background = ImageTk.PhotoImage(self.background)
        self.background_label = ctk.CTkLabel(self.window, image=self.photo_background,width=1173*ratio, height=864*ratio, text='')
        self.background_label.place(x=363*ratio, y=0)
        
        # Tạo một khung CTKFrame với màu nền là màu hex #2b95d1 và đặt ở vị trí x = 0, y = 0
        self.frame = ctk.CTkFrame(self.window,width=512*ratio, height=864*ratio, fg_color="#2b95d1")
        self.frame.place(x=0, y=0)

        # Tạo nhãn "Username/Email" và đặt ở tọa độ (92,334)
        self.username_label = ctk.CTkLabel(self.frame, text="Username/Email", font=("default", 20*ratio, "bold"))
        self.username_label.place(x=92*ratio, y=334*ratio)

        # Tạo nhãn "Password" và đặt ở tọa độ (92,443)
        self.password_label = ctk.CTkLabel(self.frame, text="Password", font=("default", 20*ratio, "bold"))
        self.password_label.place(x=92*ratio, y=443*ratio)

        # Tạo hộp nhập liệu thứ nhất và đặt ở tọa độ (92,370)
        self.username_entry = ctk.CTkEntry(self.frame, width=343*ratio, height=54*ratio, fg_color="white", border_width=1, border_color="black", corner_radius=20, font=("default", 20))
        self.username_entry.configure(text_color="black")
        self.username_entry.place(x=92*ratio, y=370*ratio)

        # Tạo hộp nhập liệu thứ hai và đặt ở tọa độ (92,478)
        self.password_entry = ctk.CTkEntry(self.frame, width=343*ratio, height=54*ratio, fg_color="white", border_width=1, border_color="black", corner_radius=20, font=("default", 20), show='•')
        self.password_entry.configure(text_color="black")
        self.password_entry.place(x=92*ratio, y=478*ratio)

        # Tạo nhãn "Don't have an account?" và đặt ở tọa độ (158,728)
        self.account_label = ctk.CTkLabel(self.frame, text="Don't have an account?", font=("default", 12*ratio, "bold"), fg_color="transparent", width=145*ratio, height=20*ratio)
        self.account_label.place(x=158*ratio, y=728*ratio)

        # Tạo nút "Sign up" và đặt ở tọa độ (303,728)
        self.signup_button = ctk.CTkButton(self.frame, text="Sign up", font=("default", 12*ratio, "bold"), fg_color="transparent", width=51*ratio, height=20*ratio, command=self.create_account)
        self.signup_button.place(x=303*ratio, y=728*ratio)

        # Tạo nút "Login" và đặt ở tọa độ (213,608)
        self.login_button = ctk.CTkButton(self.frame, text="Login", font=("default", 20*ratio, "bold"), fg_color="#F7B104", width=169*ratio, height=47*ratio, corner_radius=30, command=self.login)
        self.login_button.place(x=179*ratio, y=575*ratio)

        # self.open_image_label = ctk.CTkLabel(self.frame, text="Other choice? ", font=("default", 12*ratio, "bold"), fg_color="transparent", width=145*ratio, height=20*ratio)
        # self.open_image_label.place(x= 158*ratio, y= 758*ratio)

        # self.open_image_button = ctk.CTkButton(self.frame, text="Open image", font=("default", 12*ratio, "bold"), fg_color="transparent", width= 78*ratio, height=20*ratio, command=self.open_image)
        # self.open_image_button.place(x=303*ratio, y= 758*ratio)

        # Tạo nút đăng kí bằng email
        self.email_register = ctk.CTkButton(self.frame, text="Sign up by email", font=("default",12*ratio,"bold"),fg_color="transparent",width=145*ratio, height=20*ratio,command=self.switch_to_register)
        # Tạo hình ảnh và đặt ở tọa độ (156,71)
        self.image = Image.open("./main/image_transparent.png")
        self.image = self.image.resize((int(200*ratio), int(200*ratio)))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = ctk.CTkLabel(self.frame, image=self.photo, width=int(200*ratio), height=int(200*ratio), text='')
        self.image_label.place(x=156*ratio, y=71*ratio)

        # Tạo nhãn "Login" và đặt ở tọa độ (167,271)
        self.login_label = ctk.CTkLabel(self.frame, text="Login", font=("default", 32*ratio, "bold"), fg_color="transparent", width=177*ratio, height=45*ratio)
        self.login_label.place(x=167*ratio, y=271*ratio)

        self.confirm_password_label = ctk.CTkLabel(self.frame, text="Confirm Password", font=("default", 20*ratio, "bold"))
        self.confirm_password_entry = ctk.CTkEntry(self.frame, width=343*ratio, height=54*ratio, fg_color="white", border_width=1, border_color="black", corner_radius=20, font=("default", 20*ratio),show='•')
        self.confirm_password_entry.configure(text_color="black")

        self.back_button = ctk.CTkButton(master=self.frame, text="Back", font=("default",12*ratio,"bold"),fg_color="transparent",width=65*ratio, height=20*ratio,command=self.switch_to_register)

    def open_image(self):
        pass
    def draw(self):
        # Lặp vô tận để hiển thị cửa sổ
        self.window.mainloop()
    
    # Đăng kí bằng email
    def switch_to_register(self):
        global ratio
        self.login_label.configure(text="Register")
        clear_entry(self.username_entry)
        clear_entry(self.password_entry)
        clear_entry(self.confirm_password_entry)
        self.login_label.configure(text="Register")
        self.username_label.configure(text="Email")
        self.password_label.place_forget()
        self.password_entry.place_forget()
        self.confirm_password_entry.place_forget()
        self.confirm_password_label.place_forget()
        self.email_register.place_forget()
        # Chuyển đổi text trên nút "Login" thành "Register"
        self.login_button.configure(text="Confirm Email", command= self.confirm_email)
        # Thay đổi chữ trong label "Don't have an account?" thành "Already have one?"
        self.account_label.configure(text="Already have one?")
        # Thay đổi chữ trên nút "Sign up" thành "Sign in"
        self.signup_button.configure(text="Sign in", command=self.switch_to_login)
        self.back_button.configure(command=self.create_account)
        self.back_button.place(x = 233*ratio, y = 788*ratio)

    def switch_to_login(self):
        self.email_register.place_forget()
        self.login_label.configure(text="Login")
        self.username_label.configure(text="Username/Email")
        self.login_button.configure(text="Login")
        self.confirm_password_entry.place_forget()
        self.confirm_password_label.place_forget()
        self.login_button.place_forget()
        self.password_label.place_forget()
        self.password_entry.place_forget()
        self.back_button.place_forget()
        clear_entry(self.username_entry)
        clear_entry(self.password_entry)
        clear_entry(self.confirm_password_entry)
        self.login_button.configure(command=self.login)
        self.login_button.place(x = 179*ratio, y = 575*ratio)
        self.password_label.place(x = 92*ratio, y = 443*ratio)
        self.password_entry.place(x = 92*ratio, y = 478*ratio)
        self.account_label.configure(text="Don't have an account?")
        self.signup_button.configure(text="Sign up", command=self.create_account)

    def confirm_email(self):
        global code, email
        email_input = self.username_entry.get()
        if email_input == '':
            tkinter.messagebox.showerror('Empty email', 'Email must be filled!')
        else:
            if check_gmail_in_string(email_input) == True:
                code = send_verification_code(email_input)
                clear_entry(self.username_entry)
                email = email_input
                self.login_button.configure(text="Confirm", command= self.veri_confirm)
                self.login_label.configure(text="Confirmation")
                self.username_label.configure(text="Enter the code")
                self.username_entry.place_forget()
                self.username_entry.place(x=92*ratio, y = 370*ratio)
                self.back_button.configure(command=self.switch_to_register)
                self.back_button.place(x = 233*ratio, y = 788*ratio)

            else:
                code = send_verification_code(email_input + "@gmail.com")
                email = email_input
                self.login_button.configure(text="Confirm", command= self.veri_confirm)
                clear_entry(self.username_entry)
                self.login_label.configure(text="Confirmation")
                self.username_label.configure(text="Enter the code")
                self.username_entry.place_forget()
                self.username_entry.place(x=92*ratio, y = 370*ratio)
                self.back_button.configure(command=self.switch_to_register)
                self.back_button.place(x = 233*ratio, y = 788*ratio)
        return code
    
    def veri_confirm(self):
        global code, email

        veri_code = self.username_entry.get()
        if veri_code == '':
            tkinter.messagebox.showinfo("Check","Empty code. Try again.")
        else:
            if veri_code == code:
                tkinter.messagebox.showinfo("Success!","Confirm success!")
                self.create_account()
            else:
                tkinter.messagebox.showerror("Invalid!","Invalid code!")

    def create_account(self):
        clear_entry(self.username_entry)
        clear_entry(self.password_entry)
        clear_entry(self.confirm_password_entry)
        self.login_label.configure(text="Create account")
        self.username_label.place_forget()
        self.username_label.configure(text="Username")
        self.password_entry.place_forget()
        self.password_entry.place_forget()
        self.login_button.place_forget()
        self.back_button.place_forget()
        self.username_label.place(x=92*ratio, y=334*ratio)
        self.password_label.place(x=92*ratio, y=443*ratio)
        self.password_entry.place(x=92*ratio, y=478*ratio)
        self.account_label.configure(text="Already have account?")
        self.signup_button.configure(text="Sign in", command=self.switch_to_login)
        self.email_register.place(x=159*ratio, y=758*ratio)
        # Tạo nhãn "Password" và đặt ở tọa độ (92,443)
        self.confirm_password_label.place(x=92*ratio, y=549*ratio)
        # Tạo hộp nhập liệu thứ nhất và đặt ở tọa độ (92,370)
        self.confirm_password_entry.place(x=92*ratio, y=584*ratio)
        self.login_button.configure(text="Register", command=self.register)
        self.login_button.place(x = 179*ratio, y = 651*ratio)

    # Hàm xử lý sự kiện đăng nhập
    def login(self):
        global email, login_lock, user_id, user_money
        username = self.username_entry.get()  # Lấy tên người dùng từ trường nhập liệu
        password = self.password_entry.get()  # Lấy mật khẩu từ trường nhập liệu
        emails = find_file_in_subdirectories('./assets/player',f'{username}.txt')
        if len(emails) == 0:
                if os.path.exists(f"assets/player/{username}/{username}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
                    with open(f"assets/player/{username}/{username}.txt", "r") as file:  # Mở file tương ứng với tên người dùng
                        if password == file.readline().strip():  # Kiểm tra xem mật khẩu có khớp không
                            tkinter.messagebox.showinfo("Login successful!", "Login successful!")  # Hiển thị thông báo thành công
                            global login_lock
                            login_lock = True
                            user_id, user_money = fileread(username)
                            self.window.quit()  # Thoát chương trình
                            self.window.destroy()
                        else:
                            tkinter.messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi
                else:
                    tkinter.messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi        else: 
        else:
            if check_first_line_in_files(emails,password):
                tkinter.messagebox.showinfo("Success!", "Login successful!")  # Hiển thị thông báo 
                login_lock = True
                self.window.quit()
            else:
                tkinter.messagebox.showerror("Invalid username or password!", "Invalid username or password!")  # Hiển thị thông báo lỗi
        
    # Hàm xử lí sự kiện đăng nhập bằng khuôn mặt
    
    # Hàm xử lí sự kiện đăng kí bằng khuôn mặt

    # Hàm xử lý sự kiện đăng ký
    def register(self):
        global email
        username = self.username_entry.get()  # Lấy tên người dùng từ trường nhập liệu
        password = self.password_entry.get()  # Lấy mật khẩu từ trường nhập liệu
        repeat_password = self.confirm_password_entry.get()  # Lấy mật khẩu nhập lại từ trường nhập liệu
        if username == "" or password == "" or repeat_password == "":
            tkinter.messagebox.showerror("Have blank emulation!", "Have blank emulation!")
        else:
            if os.path.exists(f"assets/player/{username}/{username}.txt"):  # Kiểm tra xem tên người dùng có tồn tại không
                tkinter.messagebox.showerror("Username existed!", "Username existed!")  # Hiển thị thông báo lỗi
            elif password == repeat_password:  # Kiểm tra xem mật khẩu và mật khẩu nhập lại có khớp không
                os.makedirs(f"assets/player/{username}",exist_ok=True)
                with open(f"assets/player/{username}/{username}.txt", "w") as file:  # Tạo một file mới với tên người dùng
                    file.write(password + "\n")  # Ghi mật khẩu vào dòng đầu tiên của file
                    file.write("500" + "\n")  # Ghi "500" vào dòng thứ hai của file
                '''with open(f"assets/player/{username}/{email}.txt",'w') as file:
                    file.write(email + '\n')'''
                tkinter.messagebox.showinfo("Register successful!", "Register successful!")  # Hiển thị thông báo thành công
                self.switch_to_login()  # Chuyển về chế độ đăng nhập
            else:
                tkinter.messagebox.showerror("Passwords do not match!", "Passwords do not match!")  # Hiển thị thông báo lỗi
def check_gmail_in_string(s):
    return "@gmail.com" in s
def send_verification_code(receiver_email):
    # Tạo mã xác minh ngẫu nhiên
    global code
    now = datetime.now()
    now = now.replace(microsecond=0)
    now = now.strftime("%d/%m%Y, %H:%M:%S")
    veri_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    code = veri_code
    # Thông tin tài khoản Gmail của bạn
    sender_email = "devteam.animalracetrack@gmail.com"
    password = "dzlh mowf obyr bfei"
    # Tạo nội dung email
    subject = "Your verification code confirm the email to login/signup into Animal RaceTrack"
    body = f"""Hello {receiver_email}.
    We have received requests to authenticate your email used to login or signup into our Animal RaceTrack game.
    We have sent a verificaion code to verify your login or registration.
    Your verification code is: {veri_code}

    Please secure the encrypted OTP and follow the next steps to complete your login or registration to our Animal RaceTrack game.

    You have sent this email because you requested the registration or login into your account.

    If not, you can ignore this.

    If you have any questions or other service requests, please contact us via:
    Email: {sender_email}
    """
    message = f"Subject: {subject}\n\n{body}"



    # Gửi email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    print(f"Verification code sent to {receiver_email}.")
    return code
def clear_entry(entry):
    entry.delete(0,'end')
def find_file_in_subdirectories(relative_path, filename):
    # Chuyển đổi đường dẫn phụ thuộc thành đường dẫn tuyệt đối
    directory = os.path.abspath(relative_path)
    
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == filename + '.txt':
                # Chuyển đổi đường dẫn tuyệt đối thành đường dẫn phụ thuộc
                matching_files.append(os.path.relpath(os.path.join(root, file), directory))
    return matching_files
def check_first_line_in_files(file_list, target_string):
    for file_path in file_list:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            if first_line == target_string:
                return True
    return False
# Tạo một đối tượng LoginMenu và vẽ nó
window = ctk.CTk()
window.title("Login")
app = LoginMenu(window)
window.mainloop()
