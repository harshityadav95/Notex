### # Javascript ES6 Notes: 

###  JavaScript Versions: ES6 and Before 

Take for example pre-ES6 syntax for function expressions:

```
var greeting = function() {
  console.log('Hello World!');  
};
```



With ES6 arrow functions, we can transform the expression above into:

````
let writingUtensil=tool || 'pen'const greeting = () => console.log('Hello World'); 
````



### Progate + Codeacademy Lesson 1:

1. *Null*: This data type represents the intentional absence of a value, and is represented by the keyword `null` (without quotes).

2. *Undefined*: This data type is denoted by the keyword `undefined` (without quotes). It also represents the absence of a value though it has a different use than `null`.

   ```js
   let price;
   console.log(price); // Output: undefined
   ```

   

3. *Symbol*: A newer feature to the language, symbols are unique identifiers, useful in more complex coding. No need to worry about these for now.

4. *Object*: Collections of related data.

The first 1-2 of those types are considered *primitive data types*. They are the most basic data types in the language.

```javascript
// Prinitng the Hello World
console.log("Hello World");
// Output the result of 24 divided by 4
console.log(24/4);
//Using the variable
let name="Harshit Yadav";
console.log("My Name is "+name);
//dont use let again  
name=4;
console.log(name);
//Short hand works in JS
name+=2;
console.log(name);
//Constants in JS
const ne="this is constant";
// Templeate Literals
console.log(`My name is ${ne} :) `);
// if condition
if(name>1)
{
  console.log("check");
  console.log(name>1);
}

const password = "kentheninja";

// When the value of password is "kentheninja", output "Signed in successfully"
if(password==="kentheninja")
{
  switch (password){
    case "kentheninja":
      console.log("check mate");
      break;
      default:
      console.log("fail");
      break;

  }
  

  console.log("Signed in successfully");
}
else
{
  console.log("nope");
}


// Short Circuit using and Operator
let writingUtensil=tool || 'pen'

// Ternary operator  
let isLocked = false;
isLocked ?
  console.log('You will need a key to open the door.') :
  console.log('You will not need a key to open the door.');

let favoritePhrase = 'Love That!';

favoritePhrase === 'Love That!' ?
  console.log('I love that!'):
  console.log("I don't love that!");

```



### Progate Lesson 2  

```

```

### CodeAcdemy Lesson 1:

```js
//calculating the length of the string 
console.log("hello".length);

console.log('hello'.toUpperCase()); // Prints 'HELLO'
console.log('Hey'.startsWith('H')); // Prints true
console.log('    Remove whitespace   '.trim());// Remove the WhiteSpace
console.log(Math.random()); // Prints a random number between 0 and 1
console.math(Math.random()*50);//to generate number between 1 to 50
console.log(Math.floor(Math.random() * 50));// Floor the decimal values to whole number

```

#### Maths  In [Javascript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)

#### Number in [Javascript Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number)

### Variable in JS  

There were a lot of changes introduced in the ES6 version of JavaScript in 2015. One of the biggest changes was two new keywords, `let` and `const`, to create, or *declare*, variables. Prior to the ES6, programmers could only use the `var` keyword to declare variables

 The `let` keyword signals that the variable can be reassigned a different value. 

```js
//var myName = 'Arya';
let myName = 'Arya';
console.log(myName);
```

`myName` is the variable’s name. Capitalizing in this way is a standard convention in JavaScript called *camel casing*. In camel casing you group words into one, the first word is lowercase, then every word that follows will have its first letter uppercased. (e.g. camelCaseEverything) 

#### String Interpolation

In the ES6 version of JavaScript, we can insert, or *interpolate*, variables into strings using *template literals*

```js
const myPet = 'armadillo';
console.log(`I own a pet ${myPet}.`);
```



### Typeof Operator 

```js
let newVariable = 'Playing around with typeof.';

console.log(typeof newVariable);
```

# Functions in Javascript 



One way to create a function is by using a *function declaration*. Just like how a variable declaration binds a value to a variable name, a function declaration binds a function to a name, or an *identifier*.

```javascript
function getReminder()
{
  console.log('Water the plants.');
}
```

#### Default Parameters

```javascript
function makeShoppingList(item1='milk', item2='bread', item3='eggs'){
  console.log(`Remember to buy ${item1}`);
  console.log(`Remember to buy ${item2}`);
  console.log(`Remember to buy ${item3}`);
}
```



### Return Function 

```javascript
function rectangleArea(width, height) {
  if (width < 0 || height < 0) {
    return 'You need positive integers to calculate area!';
  }
  return width * height;

```

# Arrow Functions

ES6 introduced *arrow function syntax*, a shorter way to write functions by

using the special “fat arrow” `() =>` notation.

```js
const rectangleArea = (width, height) => {
  let area = width * height;
  return area;
};
```

### Concise Body Arrow Functions

```js
const squareNum = num => num * num;
```








