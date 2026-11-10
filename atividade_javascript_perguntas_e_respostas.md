# Atividade Prática de JavaScript — Perguntas e Respostas

**Instituição:** CEUB  
**Disciplina:** Desenvolvimento de Interface  
**Conteúdo:** Introdução, variáveis e operadores — JavaScript  
**Aluno:** Arthur Parente Cabral  
**Curso:** Análise e Desenvolvimento de Sistemas (ADS)

---

## Parte A — Primeiros comandos e variáveis

### Questão 01 — Minha primeira mensagem

**Enunciado:** Exiba no console seu nome, o curso ADS e a frase “Estou aprendendo JavaScript”, em três mensagens.

**Resposta:**
```javascript
console.log("Meu nome é Arthur Parente Cabral.");
console.log("Curso: Análise e Desenvolvimento de Sistemas (ADS).");
console.log("Estou aprendendo JavaScript.");
```

### Questão 02 — Apresentação pessoal

**Enunciado:** Crie variáveis para nome, idade e curso. Atribua valores e mostre as três informações no console.

**Resposta:**
```javascript
const nome = "Arthur Parente Cabral";
const idade = 20; // Substitua pela sua idade, se necessário.
const curso = "Análise e Desenvolvimento de Sistemas (ADS)";

console.log("Nome:", nome);
console.log("Idade:", idade, "anos");
console.log("Curso:", curso);
```

### Questão 03 — Alterando uma variável

**Enunciado:** Declare uma variável `pontos` com valor inicial 10. Altere o valor para 25 e mostre o resultado.

**Resposta:**
```javascript
let pontos = 10;
console.log("Pontos iniciais:", pontos);

pontos = 25;
console.log("Pontos após a alteração:", pontos);
```

### Questão 04 — Tipos de dados

**Enunciado:** Crie quatro variáveis contendo texto, número inteiro, número decimal e booleano. Identifique os tipos usando `typeof`.

**Resposta:**
```javascript
const texto = "JavaScript";
const numeroInteiro = 25;
const numeroDecimal = 19.99;
const valorBooleano = true;

console.log("Tipo de texto:", typeof texto); // string
console.log("Tipo de número inteiro:", typeof numeroInteiro); // number
console.log("Tipo de número decimal:", typeof numeroDecimal); // number
console.log("Tipo booleano:", typeof valorBooleano); // boolean
```

---

## Parte B — Operadores aritméticos

### Questão 05 — Soma de dois números

**Enunciado:** Crie duas variáveis com os valores 15 e 8. Calcule e exiba a soma.

**Resposta:**
```javascript
const numero1 = 15;
const numero2 = 8;
const soma = numero1 + numero2;

console.log("Soma de 15 + 8 =", soma); // 23
```

### Questão 06 — Quatro operações

**Enunciado:** Com os números 20 e 4, calcule adição, subtração, multiplicação e divisão. Identifique cada resultado no console.

**Resposta:**
```javascript
const numero1 = 20;
const numero2 = 4;

console.log("Adição:", numero1 + numero2); // 24
console.log("Subtração:", numero1 - numero2); // 16
console.log("Multiplicação:", numero1 * numero2); // 80
console.log("Divisão:", numero1 / numero2); // 5
```

### Questão 07 — Preço total de uma compra

**Enunciado:** Um produto custa R$ 35,00 e o cliente comprou 4 unidades. Calcule o total da compra.

**Resposta:**
```javascript
const precoUnitario = 35;
const quantidade = 4;
const total = precoUnitario * quantidade;

console.log("Preço unitário: R$", precoUnitario.toFixed(2));
console.log("Quantidade:", quantidade);
console.log("Total da compra: R$", total.toFixed(2)); // R$ 140,00
```

### Questão 08 — Calculando um desconto

**Enunciado:** Um produto custa R$ 200,00 e tem desconto de 10%. Calcule o valor do desconto e o preço final.

**Resposta:**
```javascript
const preco = 200;
const percentualDesconto = 10;
const valorDesconto = preco * percentualDesconto / 100;
const precoFinal = preco - valorDesconto;

console.log("Preço original: R$", preco.toFixed(2));
console.log("Desconto:", percentualDesconto + "%");
console.log("Valor do desconto: R$", valorDesconto.toFixed(2)); // R$ 20,00
console.log("Preço final: R$", precoFinal.toFixed(2)); // R$ 180,00
```

### Questão 09 — Média de três notas

**Enunciado:** Um estudante obteve notas 7, 8 e 9. Calcule e exiba a média aritmética.

**Resposta:**
```javascript
const nota1 = 7;
const nota2 = 8;
const nota3 = 9;
const media = (nota1 + nota2 + nota3) / 3;

console.log("Média das notas:", media); // 8
```

### Questão 10 — Resto da divisão

**Enunciado:** Descubra o resto de 10 dividido por 3, de 15 dividido por 4 e de 20 dividido por 5.

**Resposta:**
```javascript
console.log("Resto de 10 dividido por 3:", 10 % 3); // 1
console.log("Resto de 15 dividido por 4:", 15 % 4); // 3
console.log("Resto de 20 dividido por 5:", 20 % 5); // 0
```

---

## Parte C — Atribuição, comparação e lógica

### Questão 11 — Atualização de saldo

**Enunciado:** Uma conta tem saldo de R$ 500,00. Adicione R$ 150,00 e retire R$ 80,00. Exiba o saldo final.

**Resposta:**
```javascript
let saldo = 500;
console.log("Saldo inicial: R$", saldo.toFixed(2));

saldo += 150;
saldo -= 80;

console.log("Saldo final: R$", saldo.toFixed(2)); // R$ 570,00
```

### Questão 12 — Comparando idades

**Enunciado:** Crie uma variável `idade` com valor 17. Teste as expressões `idade >= 18`, `idade < 18` e `idade === 17`.

**Resposta:**
```javascript
const idade = 17;

console.log("Idade >= 18:", idade >= 18); // false
console.log("Idade < 18:", idade < 18); // true
console.log("Idade === 17:", idade === 17); // true
```

### Questão 13 — Igualdade de valor e tipo

**Enunciado:** Compare o número 10 com o texto "10" usando `==` e `===`. Explique a diferença entre os resultados.

**Resposta:**
```javascript
console.log('10 == "10":', 10 == "10"); // true
console.log('10 === "10":', 10 === "10"); // false
```

**Explicação:** O operador `==` compara os valores e permite a conversão de tipos antes da comparação. Por isso, o número `10` e o texto `"10"` são considerados iguais nesse caso. Já o operador `===` compara o valor e também o tipo de dado, sem conversão. Como um é `number` e o outro é `string`, o resultado é `false`.

### Questão 14 — Acesso ao sistema

**Enunciado:** Uma pessoa pode acessar o sistema se tiver 18 anos ou mais E cadastro ativo. Considere idade 20 e cadastro ativo. Mostre a expressão lógica no console.

**Resposta:**
```javascript
const idade = 20;
const cadastroAtivo = true;
const podeAcessar = idade >= 18 && cadastroAtivo;

console.log("Pode acessar o sistema?", podeAcessar); // true
```

**Explicação:** O operador `&&` representa o E lógico. As duas condições precisam ser verdadeiras para permitir o acesso.

### Questão 15 — Frete gratuito

**Enunciado:** Uma loja oferece frete gratuito para compras de pelo menos R$ 150,00 OU clientes VIP. Considere compra de R$ 100,00 e cliente VIP.

**Resposta:**
```javascript
const valorCompra = 100;
const clienteVIP = true;
const freteGratis = valorCompra >= 150 || clienteVIP;

console.log("Compra: R$", valorCompra.toFixed(2));
console.log("Cliente VIP?", clienteVIP);
console.log("Tem direito a frete grátis?", freteGratis); // true
```

**Explicação:** O operador `||` representa o OU lógico. Basta uma das condições ser verdadeira. Neste exemplo, a compra é inferior a R$ 150,00, mas o cliente é VIP; portanto, tem direito ao frete gratuito.

---

## Parte D — Desafio integrador

### Questão 16 — Compra com desconto

**Enunciado:** Crie variáveis para nome do produto, preço unitário, quantidade e percentual de desconto. Calcule subtotal, desconto e valor final; exiba os valores com rótulos. Teste com teclado, R$ 80,00, 3 unidades e 10% de desconto.

**Resposta:**
```javascript
const nomeProduto = "Teclado";
const precoUnitario = 80;
const quantidade = 3;
const percentualDesconto = 10;

const subtotal = precoUnitario * quantidade;
const valorDesconto = subtotal * percentualDesconto / 100;
const valorFinal = subtotal - valorDesconto;

console.log("===== RESUMO DA COMPRA =====");
console.log("Produto:", nomeProduto);
console.log("Preço unitário: R$", precoUnitario.toFixed(2));
console.log("Quantidade:", quantidade);
console.log("Percentual de desconto:", percentualDesconto + "%");
console.log("Subtotal: R$", subtotal.toFixed(2));
console.log("Valor do desconto: R$", valorDesconto.toFixed(2));
console.log("Valor final: R$", valorFinal.toFixed(2));
```

**Resultado esperado:**

| Descrição | Valor |
|---|---:|
| Produto | Teclado |
| Preço unitário | R$ 80,00 |
| Quantidade | 3 |
| Subtotal | R$ 240,00 |
| Desconto (10%) | R$ 24,00 |
| **Valor final** | **R$ 216,00** |

---

## Orientações para execução

1. Abra o Google Chrome ou Microsoft Edge.
2. Pressione `F12` ou `Ctrl + Shift + J`.
3. Selecione a aba **Console**.
4. Copie o código de cada questão e cole no Console.
5. Pressione `Enter` e confira os resultados.

**Observação:** Os trechos de código foram separados por questão. Assim, podem ser executados individualmente no Console sem conflito entre declarações de variáveis. Se optar por executar todos os trechos em um único arquivo, mantenha cada questão dentro de seu próprio bloco `{ }`.

## Conclusão

A atividade permite praticar os fundamentos iniciais da linguagem JavaScript: exibição de mensagens, declaração e alteração de variáveis, identificação de tipos, operações matemáticas, operadores de atribuição, comparações e expressões lógicas. O desafio integrador reúne esses conceitos em uma situação prática de cálculo de compra com desconto.
