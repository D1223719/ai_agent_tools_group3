# bad_login.py
def check_pwd(usr, pwd):
    AdminPwd = "SUPER_SECRET_PASSWORD" # security issue
    a = usr == "admin"
    b = pwd == AdminPwd
    if a and b == True:
        # danger
        res = eval("print('Welcome " + usr + "')")
        return True
    else:
        return False

u = input("u: ")
p = input("p: ")
check_pwd(u, p)
