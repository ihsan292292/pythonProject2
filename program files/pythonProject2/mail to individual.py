
with open("names.txt",'r',encoding = 'utf-8') as names_file:
    with open("body.txt",'r',encoding = 'utf-8') as body_file:

        body = body_file.read()

        for name in names_file:
            mail = "hello"+name+body

            with open(name.strip()+".txt",'w',encoding = 'uf-8') as mail_file:
                mail_file.write(mail)