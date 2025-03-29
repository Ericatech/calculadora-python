Calculadora Simples em Python
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
Uma calculadora simples que realiza operações básicas (soma, subtração, multiplicação e divisão) entre dois números fornecidos pelo usuário.

📝 Funcionalidades
Soma de dois números

Subtração entre dois números

Multiplicação de dois números

Divisão com tratamento para divisão por zero

Interface simples via linha de comando

⚙️ Como Usar
Certifique-se de ter o Python instalado (versão 3.x recomendada)

Clone este repositório ou copie o código

Execute o script:

bash
Copy
python calculadora.py
Siga as instruções no terminal:

Digite o primeiro número

Digite o segundo número

Veja os resultados das operações

🛠️ Estrutura do Código
python
Copy
# Solicita os números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Realiza as operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Verifica divisão por zero
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Erro: Divisão por zero!"

# Exibe os resultados
print("\nResultados:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
📌 Próximas Melhorias
Adicionar validação para entradas não numéricas

Implementar um menu de operações

Adicionar mais operações (potenciação, raiz quadrada)

Criar interface gráfica (GUI)

Adicionar histórico de operações

🤝 Como Contribuir
Contribuições são bem-vindas! Siga estes passos:

Faça um fork do projeto

Crie uma branch para sua feature (git checkout -b feature/nova-feature)

Commit suas mudanças (git commit -m 'Adiciona nova feature')

Push para a branch (git push origin feature/nova-feature)

Abra um Pull Request

📄 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

Feito com ❤️ por [Erica Lima]
