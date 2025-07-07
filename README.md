#  Django User Management System

This is a Django project in progress. It will allow users to register, log in, verify their accounts, manage their profiles, and be managed by an admin.

---

##  Project Status

🛠 Work in progress — started on **July 7, 2025**  
✅ Deadline: **Today, 6PM**

---

##  Planned Features

- User Registration & Login
- Email Verification 
- Profile View & Edit
- Change Password
- Admin Panel
- Unit Tests (models and views)

---

## 1. Project Setup 

so i started by by setting up my project by by the name user-mgmt and create an app and named it account. to ensure that django recognises the app, i added it in the installed apps in the user-mgmt/setting.py.


![Screenshot (10)](https://github.com/user-attachments/assets/fb03a423-b552-40e1-8773-f2859e15f3d7)



---
## 2. User Registration & Login

This project includes a simple user authentication system using Django's built-in tools.

### it What’s Implemented

- **User Registration**
  - Uses Django’s `UserCreationForm`
  - Allows users to register with a username, email, and password
  - Accessible at: `/accounts/register/`
   
![Screenshot (11)](https://github.com/user-attachments/assets/06c59fed-ba87-4d7b-b1e1-f938f68cbcb4)

- **User Login**
  - Uses Django’s built-in `LoginView`
  - Allows registered users to log in securely
  - Accessible at: `/accounts/login/`
 
    ![Screenshot (12)](https://github.com/user-attachments/assets/d142d04c-e623-4f4e-a1d1-e48020dd53ef)


- **Redirection**
  - Upon successful login, users are redirected to the home page (`/`)



---



---
## 📃 License

For educational use only.
