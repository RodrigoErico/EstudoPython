# codigo iperativo
email = 'rodrigo@gmail.com'
servidor = email[7:]
print(servidor)


'''Orientado a objeto''' 

# objeto Email
class Email():
    # Atributos da classe Email = caracteristicas
    def init():
        nome= 'Rodrigo'
        email = 'rodrigo2@gmail.com'
    
    def pegar_servidor():
        return email[7:]

retorna_email = Email()    
print(retorna_email.pegar_servidor)