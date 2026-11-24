// Dados do estudante
const nomeEstudante = "Mariana";
const nota1 = 8;
const nota2 = 7;
const nota3 = 9;
// Cálculo da média
const media = (nota1 + nota2 + nota3) / 3;
// Apresentação dos resultados
console.log("Estudante:", nomeEstudante);
console.log("Nota 1:", nota1);
console.log("Nota 2:", nota2);
console.log("Nota 3:", nota3);
console.log("Média:", media.toFixed(1));

const nomeEstudante = prompt(
 "Informe o nome do estudante:"
);
const nota1 = Number(prompt("Informe a primeira nota:"));
const nota2 = Number(prompt("Informe a segunda nota:"));
const nota3 = Number(prompt("Informe a terceira nota:"));
const media = (nota1 + nota2 + nota3) / 3;
console.log("Estudante:", nomeEstudante);
console.log("Média:", media.toFixed(1));