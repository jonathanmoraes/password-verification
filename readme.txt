para rodar : python -m uvicorn main:app --rel

Query inicial de teste para rodar no graphql:


query {
	verify(password: "TesteSenhaForte!12103&", rules: [
		{rule: "minSize",value: 100},
		{rule: "minSpecialChars",value: 3},
		{rule: "noRepeted",value: 0},
		{rule: "minDigit",value: 4}
	]) {
		verify
		noMatch
}
}