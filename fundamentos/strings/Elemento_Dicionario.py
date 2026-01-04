#Criando um dicionario com alguns pares chave-valor
dicionario = {
    "nome" : "Anderson",
    "idade" : "45",
    "cidade" : "São Paulo"
}

#Acessando e imprimindo valores individuais chave-valor
nome = dicionario["nome"]
idade = dicionario["idade"]
cidade = dicionario["cidade"]

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Cidade: {cidade}")

#Adicionando uma nova chave-valor ao dicionairo
dicionario ["Profissão"] = ["Desenvolvedor Full Stack"]
print(f"Dicionário após adicionar uma profissão, {dicionario}")
#Modificando valor associado a uma chave existente
dicionario["idade"] = "45"
print(f"Após modificar a idade, {dicionario}")

#Removendo um par chave-valor do dicionário
del dicionario["cidade"]
print(f"Diconário após remover cidade: {dicionario}")

#Acessando todas as chaves e valores ao dicionário
chaves = dicionario.keys()
valores = dicionario.values()

print(f"Chaves: {list(chaves)}")
print(f"Valores: {list(valores)}")

#Iterando sobre os pares chave valor do dicionário
print(f"Iterando sobre o dicionário: ")
for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

#Verificando se uma chave existe no dicionario
if "nome" in dicionario:
    print(f"O nome do dicionário é: {dicionario["nome"]}")

else:
    print(f"A chave 'nome' não esta no dicionário.")

#Usando o metodo get() para acessar valores de forma segura
profissão = dicionario.get("profissão", "Desconhecido")
print(f"Profissão: {profissão}")

#Limpando todos os elementos do dicionário
dicionario.clear()
print(f"Dicioário após limpar todos os elementos: {dicionario} ")





