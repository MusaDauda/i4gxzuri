// Simple calculator in javaScript

// Ask for operator input
var operator = prompt("Enter an operator: +, -, *, /, %(modulo)");

//Take operand input
var operarand1 = parseFloat(prompt("Enter first operand"));
var operarand2 = parseFloat(prompt("Enter second operand"));

// find addition, subtraction, division and multiplication using a variable: result
var result;
// using if...else expression
if (operator == "+") {
    result = operarand1 + operarand2;
}
else if (operator == "-") {
    result = operarand1 - operarand2;
}
else if (operator == "*") {
    result = operarand1 * operarand2;
}
else if (operator  == "/") {
    result = operarand1 / operarand2;
}
else if (operator == "%") {
    result = operarand1 % operarand2;
}
else {
    alert("Invalid operation");
}

// Display the result
console.log(`${operarand1} ${operator} ${operarand2} = ${result}`);
alert(`${operarand1} ${operator} ${operarand2} = ${result}`);