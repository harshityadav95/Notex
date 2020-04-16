# Javascript ES6 Notes: 

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

- [Mozilla Documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#Iteration_methods)

  

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

### More Example  : 

```js
const words = ['unique', 'uncanny', 'pique', 'oxymoron', 'guise'];



console.log(words.some(word => {
  return word.length < 6;
}));

// Use filter to create a new array
const interestingWords = words.filter((word) => {return word.length > 5});

console.log(interestingWords.every((word) => {return word.length > 5}));

```

Revision  :

```js
const cities = ['Orlando', 'Dubai', 'Edinburgh', 'Chennai', 'Accra', 'Denver', 'Eskisehir', 'Medellin', 'Yokohama'];

const nums = [1, 50, 75, 200, 350, 525, 1000];

//  Choose a method that will return undefined
cities.forEach(city => console.log('Have you visited ' + city + '?'));

// Choose a method that will return a new array
const longCities = cities.filter(city => city.length > 7);

// Choose a method that will return a single value
const word = cities.reduce((acc, currVal) => {
  return acc + currVal[0]
}, "C");

console.log(word)

// Choose a method that will return a new array
const smallerNums = nums.map(num => num - 5);

// Choose a method that will return a boolean value
nums.some(num => num < 0);

```

# Introduction to Objects 

### Creating Object Literals

Objects can be assigned to variables just like any JavaScript type. We use curly braces, `{}`, to designate an *object literal*:

```js
let spaceship = {}; // spaceship is an empty object
```

We fill an object with unordered data. This data is organized into *key-value pairs*.

```js
// An object literal with two key-value pairs
let spaceship = {
  'Fuel Type': 'diesel',
  color: 'silver'
};
```

### Accessing Properties

```js
let spaceship = {
  homePlanet: 'Earth',
  color: 'silver'
};
spaceship.homePlanet; // Returns 'Earth',
spaceship.color; // Returns 'silver',
```

If we try to access a property that does not exist on that object, `undefined` will be returned.

```js
spaceship.favoriteIcecream; // Returns undefined
```

### Using Bracket [ ] notation

The second way to access a key’s value is by using bracket notation, `[ ]`.

```js
let spaceship = {
  'Fuel Type': 'Turbo Fuel',
  'Active Duty': true,
  homePlanet: 'Earth',
  numCrew: 5
};
spaceship['Active Duty'];   // Returns true
spaceship['Fuel Type'];   // Returns  'Turbo Fuel'
spaceship['numCrew'];   // Returns 5
spaceship['!!!!!!!!!!!!!!!'];   // Returns undefined
```

Example  :

```js
let spaceship = {
  'Fuel Type' : 'Turbo Fuel',
  'Active Mission' : true,
  homePlanet : 'Earth', 
  numCrew: 5
 };

let propName =  'Active Mission';

// Write your code below
let isActive=spaceship['Active Mission'];
console.log(spaceship[propName]);
```

### Property Assignment

It’s important to know that although we can’t reassign an object declared with `const`, we can still mutate it, meaning we can add new properties and change the properties that are there.

```js
const spaceship = {type: 'shuttle'};
spaceship = {type: 'alien'}; // TypeError: Assignment to constant variable.
spaceship.type = 'alien'; // Changes the value of the type property
spaceship.speed = 'Mach 5'; // Creates a new key of 'speed' with a value of 'Mach 5'

```

You can delete a property from an object with the `delete` operator.

```js
const spaceship = {
  'Fuel Type': 'Turbo Fuel',
  homePlanet: 'Earth',
  mission: 'Explore the universe' 
};

delete spaceship.mission;  // Removes the mission property
```

### Methods

When the data stored on an object is a function we call that a *method*. A property is what an object has, while a method is what an object does.

```js
let retreatMessage = 'We no longer wish to conquer your planet. It is full of dogs, which we do not care for.';

// Write your code below
let alienShip={
  retreat : function ()
  {
    console.log(retreatMessage);
  },
  takeOff : function()
  {
    console.log('Spim... Borp... Glix... Blastoff!');
  }
}
alienShip.retreat();
alienShip.takeOff();
```

### Nested Objects

```js
spaceship.nanoelectronics['back-up'].battery; // Returns 'Lithium'
```

### Pass By Reference

Objects are *passed by reference*. This means when we pass a variable assigned to an object into a function as an argument, the computer interprets the parameter name as pointing to the space in memory holding that object. As a result, functions which change object properties actually mutate the object permanently (even when the object is assigned to a `const` variable)

```js
const spaceship = {
  homePlanet : 'Earth',
  color : 'silver'
};

let paintIt = obj => {
  obj.color = 'glorious gold'
};

paintIt(spaceship);

spaceship.color // Returns 'glorious gold'
```

Example  :  

```js
let spaceship = {
  'Fuel Type' : 'Turbo Fuel',
  homePlanet : 'Earth'
};
greenEnergy(obj)
{
  obj['Fuel Type'] ='avocado oil';
}
function remotelyDisable(obj)
{
  obj.disabled=true;
}
greenEnergy(spaceship);
remotelyDisable(spaceship);
console.log(spaceship);

```

### Looping Through Objects

`for...in` will execute a given block of code for each property in an object.

```js
let spaceship = {
    crew: {
    captain: { 
        name: 'Lily', 
        degree: 'Computer Engineering', 
        cheerTeam() { console.log('You got this!') } 
        },
    'chief officer': { 
        name: 'Dan', 
        degree: 'Aerospace Engineering', 
        agree() { console.log('I agree, captain!') } 
        },
    medic: { 
        name: 'Clementine', 
        degree: 'Physics', 
        announce() { console.log(`Jets on!`) } },
    translator: {
        name: 'Shauna', 
        degree: 'Conservation Science', 
        powerFuel() { console.log('The tank is full!') } 
        }
    }
}; 

// Write your code below

for (let crewMember in spaceship.crew) {
  console.log(`${crewMember}: ${spaceship.crew[crewMember].name}`)
};

for (let crewMember in spaceship.crew) {
  console.log(`${spaceship.crew[crewMember].name}: ${spaceship.crew[crewMember].degree}`)
};
```

# Advanced Objects Introduction

# The this Keyword

Objects are collections of related data and functionality. We store that functionality in methods on our objects:

```js
const goat = {
  dietType: 'herbivore',
  makeSound() {
    console.log('baaa');
  }
};
```

In our `goat` object we have a `.makeSound()` method. We can invoke the `.makeSound()` method on `goat`.

```js
goat.makeSound(); // Prints baaa
```

ice, we have a `goat` object that can print `baaa` to the console. Everything seems to be working fine. What if we wanted to add a new method to our `goat` object called `.diet()` that prints the `goat`‘s `dietType`?

```js
const goat = {
  dietType: 'herbivore',
  makeSound() {
    console.log('baaa');
  },
  diet() {
    console.log(dietType);
  }
};
goat.diet(); 
// Output will be "ReferenceError: dietType is not defined"
```

That’s strange, why is `dietType` not defined even though it’s a property of `goat`? That’s because inside the scope of the `.diet()` method, we don’t automatically have access to other properties of the `goat` object.

Here’s where the `this` keyword comes to the rescue. If we change the `.diet()` method to use the `this`, the `.diet()` works! 

```js
const goat = {
  dietType: 'herbivore',
  makeSound() {
    console.log('baaa');
  },
  diet() {
    console.log(this.dietType);
  }
};

goat.diet(); 
// Output: herbivore
```

The `this` keyword references the *calling object* which provides access to the calling object’s properties. In the example above, the calling object is `goat` and by using `this` we’re accessing the `goat` object itself, and then the `dietType` property of `goat` by using property dot notation.

Example  : 

```js
const robot = {
  model:'1E78V2',
  energyLevel:100,
  provideInfo(){
  return(`I am ${this.model} and my current energy level is ${this.energyLevel}`);
  }

};
console.log(robot.provideInfo());
```

### Arrow Functions and this

We saw in the previous exercise that for a method, the calling object is the object the method belongs to. If we use the `this` keyword in a method then the value of `this` is the calling object. However, it becomes a bit more complicated when we start using arrow functions for methods. Take a look at the example below:

```js
const goat = {
  dietType: 'herbivore',
  makeSound() {
    console.log('baaa');
  },
  diet: () => {
    console.log(this.dietType);
  }
};

goat.diet(); // Prints undefined
```

In the comment, you can see that `goat.diet()` would log `undefined`. So what happened? Notice that in the `.diet()` is defined using an arrow function.

Arrow functions inherently *bind*, or tie, an already defined `this` value to the function itself that is NOT the calling object. In the code snippet above, the value of `this` is the *global object*, or an object that exists in the global scope, which doesn’t have a `dietType` property and therefore returns `undefined`.

To read more about either arrow functions or the global object check out the MDN documentation of [the global object](https://developer.mozilla.org/en-US/docs/Glossary/Global_object) and [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).

Example : 

This would work  

```js
const robot = {
  energyLevel: 100,
  checkEnergy()  {
    console.log(`Energy is currently at ${this.energyLevel}%.`)
  }
}

robot.checkEnergy();
```

but this wont work  :  

```js
const robot = {
  energyLevel: 100,
  checkEnergy: () => {
    console.log(`Energy is currently at ${this.energyLevel}%.`)
  }
}

robot.checkEnergy();
```

## Privacy

Accessing and updating properties is fundamental in working with objects. However, there are cases in which we don’t want other code simply accessing and updating an object’s properties. When discussing *privacy* in objects, we define it as the idea that only certain properties should be mutable or able to change in value.

Certain languages have privacy built-in for objects, but JavaScript does not have this feature. Rather, JavaScript developers follow naming conventions that signal to other developers how to interact with a property. One common convention is to place an underscore `_` before the name of a property to mean that the property should not be altered. Here’s an example of using `_` to prepend a property.

```js
const bankAccount = {
  _amount: 1000
}
```

In the example above, the `_amount` is not intended to be directly manipulated

#### Getters

*Getters* are methods that get and return the internal properties of an object. But they can do more than just retrieve the value of a property

```js
onst person = {
  _firstName: 'John',
  _lastName: 'Doe',
  get fullName() {
    if (this._firstName && this._lastName){
      return `${this._firstName} ${this._lastName}`;
    } else {
      return 'Missing a first name or a last name.';
    }
  }
}

// To call the getter method: 
person.fullName; // 'John Doe'
```

### Setters

Along with getter methods, we can also create *setter* methods which reassign values of existing properties within an object. Let’s see an example of a setter method:

```js
const person = {
  _age: 37,
  set age(newAge){
    if (typeof newAge === 'number'){
      this._age = newAge;
    } else {
      console.log('You must assign a number to age');
    }
  }
};
```

Example :

```js
const robot = {
  _model: '1E78V2',
  _energyLevel: 100,
  _numOfSensors: 15,
  get numOfSensors(){
    if(typeof this._numOfSensors === 'number'){
      return this._numOfSensors;
    } else {
      return 'Sensors are currently down.'
    }
  },
  set numOfSensors(num) {
    if (typeof num === 'number' && num >= 0){
      this._numOfSensors = num;
    }
    else
    {
      console.log(`Pass in a number that is greater than or equal to 0`);
    }
  }

};
robot.numOfSensors=100;
console.log(robot.numOfSensors);

```



### Factory Functions

- So far we’ve been creating objects individually, but there are times where we want to create many instances of an object quickly. Here’s where *factory functions* come in

- A factory function is a function that returns an object and can be reused to make multiple object instances. Factory functions can also have parameters allowing us to customize the object that gets returned.

- Let’s say we wanted to create an object to represent monsters in JavaScript. There are many different types of monsters and we could go about making each monster individually but we can also use a factory function to make our lives easier. To achieve this diabolical plan of creating multiple monsters objects, we can use a factory function that has parameters:

  ```js
  const monsterFactory = (name, age, energySource, catchPhrase) => {
    return { 
      name: name,
      age: age, 
      energySource: energySource,
      scare() {
        console.log(catchPhrase);
      } 
    }
  };
  ```

  

- To make an object that represents a specific monster like a ghost, we can call `monsterFactory` with the necessary arguments and assign the return value to a variable:

  ```js
  const ghost = monsterFactory('Ghouly', 251, 'ectoplasm', 'BOO!');
  ghost.scare(); // 'BOO!'
  ```

  ## Property Value Shorthand

  ES6 introduced some new shortcuts for assigning properties to variables known as *destructuring*.

  In the previous exercise, we created a factory function that helped us create objects. We had to assign each property a key and value even though the key name was the same as the parameter name we assigned to it. To remind ourselves, here’s a truncated version of the factory function:

  ```js
  const monsterFactory = (name, age) => {
    return { 
      name: name,
      age: age
    }
  };
  ```

  But we can use a destructuring technique, called *property value shorthand*, to save ourselves some keystrokes.

  ```js
  const monsterFactory = (name, age) => {
    return { 
      name,
      age 
    }
  };
  ```

  ### Destructured Assignment

  We often want to extract key-value pairs from objects and save them as variables.

  ```js
  const vampire = {
    name: 'Dracula',
    residence: 'Transylvania',
    preferences: {
      day: 'stay inside',
      night: 'satisfy appetite'
    }
  };
  ```

  If we wanted to extract the `residence` property as a variable,

  ```js
  const residence = vampire.residence;
  ```

   we can also take advantage of a destructuring technique called *destructured assignment* to save ourselves some keystrokes. In destructured assignment we create a variable with the name of an object’s key that is wrapped in curly braces `{ }` and assign to it the object. Take a look at the example below:

  ```js
  const { residence } = vampire; 
  console.log(residence); // Prints 'Transylvania'
  ```

  

Look back at the `vampire` object’s properties in the first code example. Then, in the example above, we declare a new variable `residence` that extracts the value of the `residence` property of `vampire`. When we log the value of `residence` to the console, `'Transylvania'` is printed.

```js
const { day } = vampire.preferences; 
console.log(day); // Prints 'stay inside'
```

Example  :  

```js
const robot = {
  model: '1E78V2',
  energyLevel: 100,
  functionality: {
    beep() {
      console.log('Beep Boop');
    },
    fireLaser() {
      console.log('Pew Pew');
    },
  }
};
const {functionality }=robot;
functionality.beep();

```

# Built-in Object Methods

For example, we have access to object instance methods like: `.hasOwnProperty()`, `.valueOf()`, and many more! Practice your documentation reading skills and check out: [MDN’s object instance documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#Methods).

There are also useful Object class methods such as `Object.assign()`, `Object.entries()`, and `Object.keys()` just to name a few. For a comprehensive list, browse: [MDN’s object instance documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#Methods_of_the_Object_constructor).

- Find out what we have to include by reading [MDN’s `Object.keys()` documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys).
- To find how to use `Object.entries()`, read [the documentation at MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries).
- we should check [Object.assign() documentation at MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign).

Example  :  

```js
const robot = {
	model: 'SAL-1000',
  mobile: true,
  sentient: false,
  armor: 'Steel-plated',
  energyLevel: 75
};

// What is missing in the following method call?
const robotKeys = Object.keys(robot);

console.log(robotKeys);

// Declare robotEntries below this line:

const robotEntries=Object.entries(robot);
console.log(robotEntries);

// Declare newRobot below this line:

const newRobot=Object.assign({laserBlaster: true, voiceRecognition: true}, robot);
console.log(newRobot);
```

# Introduction to Classes

JavaScript is an *object-oriented programming* (OOP) language we can use to model real-world items. In this lesson, you will learn how to make *classes*. 

Take, for example, an object representing a dog named `halley`. This dog’s `name` (a key) is `"Halley"` (a value) and has an `age` (another key) of `3` (another value). We create the `halley` object below:

```js
let halley = {
  _name: 'Halley',
  _behavior: 0,

  get name() {
    return this._name;
  },

  get behavior() {
    return this._behavior;
  },

  incrementBehavior() {
    this._behavior++;
  }
}
```

class instantiation, method

```js
const halley = new Dog('Halley');
console.log(halley.name); // Print name value to console
console.log(halley.behavior); // Print behavior value to console
halley.incrementBehavior(); // Add one to behavior
console.log(halley.name); // Print name value to console
console.log(halley.behavior); // Print behavior value to console
```

### Constructor

Although you may see similarities between class and object syntax, there is one important method that sets them apart. It’s called the *constructor* method. JavaScript calls the `constructor()` method every time it creates a new *instance* of a class.

```js
class Dog {
  constructor(name) {
    this.name = name;
    this.behavior = 0;
  }
}

```

### Instance  

n *instance* is an object that contains the property names and methods of a class, but with unique property values.

```js
class Surgeon {
  constructor(name, department) {
    this.name = name;
    this.department = department;
  }
}
const surgeonCurry=new Surgeon('Curry','Cardiovascular');

const surgeonDurant=new Surgeon('Durant','Orthopedics');

```

### Methods

Example 

```js
class Surgeon {
  constructor(name, department) {
    this._name = name;
    this._department = department;
    this._remainingVacationDays = 20;
  }
  
  get name() {
    return this._name;
  }
  
  get department() {
    return this._department;
  }
  
  get remainingVacationDays() {
    return this._remainingVacationDays; 
  
  takeVacationDays(daysOff) {
    this._remainingVacationDays -= daysOff;
  }
}

const surgeonCurry = new Surgeon('Curry', 'Cardiovascular');
const surgeonDurant = new Surgeon('Durant', 'Orthopedics');
```

### Method Calls

Example  : 

```js
class Surgeon {
  constructor(name, department) {
    this._name = name;
    this._department = department;
    this._remainingVacationDays = 20;
  }
  
  get name() {
    return this._name;
  }
  
  get department() {
    return this._department;
  }
  
  get remainingVacationDays() {
    return this._remainingVacationDays;
  }
  
  takeVacationDays(daysOff) {
    this._remainingVacationDays -= daysOff;
  }
}

const surgeonCurry = new Surgeon('Curry', 'Cardiovascular');
const surgeonDurant = new Surgeon('Durant', 'Orthopedics');

console.log(surgeonCurry.name);
surgeonCurry.takeVacationDays(3);
console.log(surgeonCurry.remainingVacationDays);
```

### Inheritance I

We’ve abstracted the shared properties and methods of our `Cat` and `Dog` classes into a parent class called `Animal` (See below)

```js
class Animal {
  constructor(name) {
    this._name = name;
    this._behavior = 0;
  }

  get name() {
    return this._name;
  }

  get behavior() {
    return this._behavior;
  }

  incrementBehavior() {
    this._behavior++;
  }
} 
```

Now that we have these shared properties and methods in the parent `Animal` class, we can extend them to the subclass, `Cat`

```js
class Cat extends Animal {
  constructor(name, usesLitter) {
    super(name);
    this._usesLitter = usesLitter;
  }
}
```

- The `super` keyword calls the constructor of the parent class. In this case, `super(name)` passes the name argument of the `Cat` class to the constructor of the `Animal` class. When the `Animal` constructor runs, it sets `this._name = name;` for new `Cat` instances


Example :

```js
class HospitalEmployee {
  constructor(name) {
    this._name = name;
    this._remainingVacationDays = 20;
  }
  
  get name() {
    return this._name;
  }
  
  get remainingVacationDays() {
    return this._remainingVacationDays;
  }
  
  takeVacationDays(daysOff) {
    this._remainingVacationDays -= daysOff;
  }
}
class Nurse extends HospitalEmployee{
  constructor(name,certifications) {
    this._name=name;

    super(name);
        this._certifications=certifications;
  }

}

const nurseOlynyk=new Nurse('Olynyk',['Trauma', 'Pediatrics']);
```

