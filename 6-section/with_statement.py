# o with permite alterações ao ficheiro sem a necessidade
# de o fechar, pois isso acontece quando o bloco with é
# terminado
with open("6-section/files/example2.txt", 'a+') as file:
    # 'a+' coloca o read() pointer no ultimo caracter
    # logo, no caso de leitura, é necessário coloca-lo
    # de volta no inicio do ficheiro
    file.seek(0)
    # ler o ficheiro
    content=file.read()
    print(content)
    # append "Line 5"
    file.write("Line 5\n")
