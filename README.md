# Password checker

Dada uma palavra contínua, e um conjunto de regras, verifica se a senha é válida
baseada nas regras:

    * minSize: ter pelo menos x caracteres.
    * minUppercase: ter pelo menos x caracteres maiúsculos
    * minLowercase: ter pelo menos x caracteres minúsculos
    * minDigit: ter pelo menos x dígitos (0-9)
    * minSpecialChars: ter pelo menos x caracteres especiaisda seguinte string: "!@#$%^&*()-+\/{}[]" )
    * noRepeted: não tenha nenhum caractere repetido em sequência

# Entrada

A API GraphQL possui uma única rota /graphql que recebe uma requisição contendo uma única query chamada verify.

URL: http://localhost:8080/graphql
Method: POST
```
query {
	verify(password: "TesteSenhaForte!12103&", rules: [
		{rule: "minSize",value: 100},
		{rule: "minSpecialChars",value: 2},
		{rule: "noRepeted",value: 0},
		{rule: "minDigit",value: 4},
	]) {
		verify
		noMatch
}
}
```
# Saida

A API retorna o resultado da Query:

    ● verify: que deve retornar um boolean dizendo se a senha foi validada por todas as regras
    ● noMatch: que deve retornar uma lista de strings que deve conter quais as regras a senha não passou ou uma lista vazia caso verify seja true.

Exemplo de saida:

```
{
  "data": {
    "verify": {
      "verify": true,
      "noMatch": [
        "minSize"
      ]
    }
  }
}
```

# Desenvolvimento e Execulção

### Tecnologias e suas versões:
    Foi utilizado:
        Python 3.11.1 64-bit
        Strawberry para definição do schema : [https://strawberry.rocks/docs]
        FastApi para a criação da API: [https://fastapi.tiangolo.com/]

# Execução:

    



