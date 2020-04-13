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



# Arrays

Arrays are JavaScript’s way of making lists. Arrays can store any data types (including strings, numbers, and booleans). Like lists, arrays are ordered, meaning each item has a numbered position

```js
let newYearsResolutions = ['Keep a journal', 'Take a falconry class', 'Learn to juggle'];

console.log(newYearsResolutions);
console.log(newYearsResolutions.length);

```

- Variables declared with the `const` keyword cannot be reassigned. However, elements in an array declared with `const` remain mutable. Meaning that we can change the contents of a `const` array, but cannot reassign a new array or a different value

  ###  The .push() .pop()Method

  `.push()` can take a single argument or multiple arguments separated by commas

  [Mozilla Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

  Some arrays methods that are available to JavaScript developers include: `.join()`, `.slice()`, `.splice()`, `.shift()`, `.unshift()`, and `.concat()` amongst many others.

  ```js
  const itemTracker = ['item 0', 'item 1', 'item 2'];
  
  itemTracker.push('item 3', 'item 4');
  chores.pop();
  
  console.log(itemTracker); 
  
  const array1 = [1, 2, 3];
  
  const firstElement = array1.shift();
  
  const animals = ['ant', 'bison', 'camel', 'duck', 'elephant'];
  
  console.log(animals.slice(2));
  // expected output: Array ["camel", "duck", "elephant"]
  
  console.log(animals.slice(2, 4));
  ```

###  Arrays and Functions

```js
const concept = ['arrays', 'can', 'be', 'mutated'];

function changeArr(arr){
  arr[3] = 'MUTATED';
 
}
changeArr(concept);
function removeElement(newArr)
{
  newArr.pop();
}
removeElement(concept);
 console.log(concept);

```

# Nested Arrays

```js
let numberClusters=[[1,2],[3,4],[5,6]];
const target=numberClusters[2][1];
```

# HIGHER-ORDER FUNCTIONS 

### Functions as Data

- [mozilla documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)

  

```js
const announceThatIAmDoingImportantWork = () => {
    console.log("I’m doing very important work!");
};
const busy = announceThatIAmDoingImportantWork;

busy(); // This function call barely takes any space!
```

### Functions as Parameters

of data in JavaScript, it might not surprise you to learn that we can also pass functions (into other functions) as parameters. A *higher-order function* is a function that either accepts functions as parameters, returns a function, or both! We call the functions that get passed in as parameters and invoked *callback functions* because they get called during the execution of the higher-order function.

When we pass a function in as an argument to another function, we don’t invoke it. Invoking the function would evaluate to the return value of that function call. With callbacks, we pass in the function itself by typing the function name *without* the parentheses (that would evaluate to the result of calling the function):

```js
const timeFuncRuntime = funcParameter => {
   let t1 = Date.now();
   funcParameter();
   let t2 = Date.now();
   return t2 - t1;
}

const addOneToOne = () => 1 + 1;

timeFuncRuntime(addOneToOne);
```

We wrote a higher-order function, `timeFuncRuntime()`. It takes in a function as an argument, saves a starting time, invokes the callback function, records the time after the function was called, and returns the time the function took to run by subtracting the starting time from the ending time.

Example :

```js
const checkThatTwoPlusTwoEqualsFourAMillionTimes = () => {
  for(let i = 1; i <= 1000000; i++) {
    if ( (2 + 2) != 4) {
      console.log('Something has gone very wrong :( ');
    }
  }
};

const addTwo = num => num + 2;

const timeFuncRuntime = funcParameter => {
  let t1 = Date.now();
  funcParameter();
  let t2 = Date.now();
  return t2 - t1;
};

// Write your code below

const time2p2 = timeFuncRuntime(checkThatTwoPlusTwoEqualsFourAMillionTimes);

const checkConsistentOutput = (func, val) => {
    let firstTry = func(val);
    let secondTry = func(val);
    if (firstTry === secondTry) {
        return firstTry
    } else {
        return 'This function returned inconsistent results'
    }
};

checkConsistentOutput(addTwo, 10);
```



# Iterators 

#### The .forEach() Method

Aptly named, `.forEach()` will execute the same code for each element of an array.

```js
const fruits = ['mango', 'papaya', 'pineapple', 'apple'];

fruits.forEach(groceryItem => console.log(fruits));

function printer(arr)
{
  console.log('I want to eat a' + arr);
}
fruits.forEach(printer);

fruits.forEach(fruit => console.log(`I want to eat a ${fruit}.`))
```



### The .map() Method

The second iterator we’re going to cover is `.map()`. When `.map()` is called on an array, it takes an argument of a callback function and returns a new array! Take a look at an example of calling `.map()`:

```js
const numbers = [1, 2, 3, 4, 5]; 

const bigNumbers = numbers.map(number => {
  return number * 10;
});

```

`.map()` works in a similar manner to `.forEach()`— the major difference is that `.map()` returns a new array.

Example  

```js
const animals = ['Hen', 'elephant', 'llama', 'leopard', 'ostrich', 'Whale', 'octopus', 'rabbit', 'lion', 'dog'];

// Create the secretMessage array below
const secretMessage=animals.map( world =>
{
  return world[0];
}
  );
```



# The .filter() Method

`.filter()` returns an array of elements after filtering out certain elements from the original array. The callback function for the `.filter()` method should return `true` or `false` depending on the element that is passed to it. The elements that cause the callback function to return `true` are added to the new array. Take a look at the following example:

```js
const words = ['chair', 'music', 'pillow', 'brick', 'pen', 'door']; 

const shortWords = words.filter(word => {
  return word.length < 6;
});
```

Example  :  

```js
const randomNumbers = [375, 200, 3.14, 7, 13, 852];

// Call .filter() on randomNumbers below

const smallNumbers=randomNumbers.filter( digit =>
{
  return digit<250;
})

console.log(smallNumbers);
const favoriteWords = ['nostalgia', 'hyperbole', 'fervent', 'esoteric', 'serene'];


// Call .filter() on favoriteWords below

const longFavoriteWords=favoriteWords.filter( word => {
  return word.length>7;
});

console.log(longFavoriteWords);
```

# The .findIndex() Method

We sometimes want to find the location of an element in an array. That’s where the `.findIndex()` method comes in! Calling `.findIndex()` on an array will return the index of the first element that evaluates to `true` in the callback function

```js
const jumbledNums = [123, 25, 78, 5, 9]; 

const lessThanTen = jumbledNums.findIndex(num => {
  return num < 10;
});

```

Example  

```js
const animals = ['hippo', 'tiger', 'lion', 'seal', 'cheetah', 'monkey', 'salamander', 'elephant'];



const foundAnimal=animals.findIndex( word =>
{
  return  word==='elephant';
});
console.log(foundAnimal);
const startsWithS=animals.findIndex(
  word =>
  {
    return word[0]==='s';
  }
);
console.log(startsWithS);
```

# The .reduce() Method

Another widely used iteration method is `.reduce()`. The `.reduce()` method returns a single value after iterating through the elements of an array, thereby *reducing* the array. 

```js
const numbers = [1, 2, 4, 10];

const summedNums = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue
})

console.log(summedNums) // Output: 17
```

The `.reduce()` method can also take an optional second parameter to set an initial value for `accumulator` (remember, the first argument is the callback function!). For instance:

```js
const numbers = [1, 2, 4, 10];

const summedNums = numbers.reduce((accumulator, currentValue) => {
  return accumulator + currentValue
}, 100)  // <- Second argument for .reduce()

console.log(summedNums); // Output: 117
```

Example :

```js
const newNumbers = [1, 3, 5, 7];

const newSum=newNumbers.reduce(function (accumulator,currentValue)
{
   console.log('The value of accumulator: ', accumulator);
  console.log('The value of currentValue: ', currentValue);
  return accumulator + currentValue;
},10);

console.log(newSum);
```

