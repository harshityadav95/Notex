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

class Nurse extends HospitalEmployee {
  constructor(name, certifications) {
    super(name);
    this._certifications = certifications;
  } 
  get certifications()
  {
    return this._certifications;
  }
  addCertification(newCertification)
  {
    this._certifications.push(newCertification);
  }
}

const nurseOlynyk = new Nurse('Olynyk', ['Trauma','Pediatrics']);
nurseOlynyk.takeVacationDays(5);
console.log(nurseOlynyk.remainingVacationDays);
nurseOlynyk.addCertification('Genetics');
console.log(nurseOlynyk.certifications);
```

When we call `extends` in a class declaration, all of the parent methods are available to the child class.

## Static Methods

Sometimes you will want a class to have methods that aren’t available in individual instances, but that you can call directly from the class.

```js
class Animal {
  constructor(name) {
    this._name = name;
    this._behavior = 0;
  }

  static generateName() {
    const names = ['Angel', 'Spike', 'Buffy', 'Willow', 'Tara'];
    const randomNumber = Math.floor(Math.random()*5);
    return names[randomNumber];
  }
} 
//
static generatePassword()
  {
    return (Math.floor(Math.random() * 10000));
  }
```

### **BROWSER COMPATIBILITY AND TRANSPILATION**

- caniuse.com — A website that provides data on web browser compatibility for HTML, CSS, and JavaScript features. You will learn how to use it to look up ES6 feature support.
- Babel — A Javascript library that you can use to convert new, unsupported JavaScript (ES6), into an older version (ES5) that is recognized by most modern browsers.

# Transpilation With Babel

Although manual conversion only took you a few minutes, it is unsustainable as the size of the JavaScript file increases.

Because ES6 is predictably backwards compatible, a collection of JavaScript programmers developed a JavaScript library called Babel that *transpiles* ES6 JavaScript to ES5.

Transpilation is the process of converting one programming language to another

#### transpile ES6 code to ES5

In the instructions below, you will pass JavaScript ES6 code to Babel, which will transpile it to ES5 and write it to a file in the **lib** directory.

```shell
npm install babel-cli
npm install babel-preset-env

```

You can view the ES5 code in **./lib/main.js**.

You may need to refresh to see the newly created **lib** directory.

```shell
npm init
```

In the next five exercises you will learn how to setup a JavaScript project that transpiles code when you run `npm run build` from the root directory of a JavaScript project.

The first step is to place your ES6 JavaScript file in a directory called **src**. From your root directory, the path to the ES6 file is **./src/main.js**

```
project
|_ src
|___ main.js
```

- Before we install Babel, we need to setup our project to use the [node package manager (npm)](https://docs.npmjs.com/getting-started/what-is-npm). Developers use *npm* to access and manage Node packages. Node packages are directories that contain JavaScript code written by other developers. You can use these packages to reduce duplication of work and avoid bugs.
- Before we can add Babel to our project directory, we need to run `npm init`. The `npm init` command creates a **package.json** file in the root directory.
  - Metadata — This includes a project title, description, authors, and more.
  - A list of node packages required for the project — If another developer wants to run your project, npm looks inside **package.json** and downloads the packages in this list.
  - Key-value pairs for command line scripts — You can use npm to run these shorthand scripts to perform some process. In a later exercise, we will add a script that runs Babel and transpiles ES6 to ES5.

If you have Node installed on your computer, you can create a **package.json** file by typing `npm init` into the terminal.



The terminal prompts you to fill in fields for the project’s metadata (name, description, etc.)

You are not required to answer the prompts, though we recommend at minimum, you add your own title and description. If you don’t want to fill in a field, you can press enter. npm will leave fill these fields with default values or leave them empty when it creates the **package.json** file.

After you run `npm init` your directory structure will contain the following files and folders:

```js
project
|_ src
|___ main.js
|_ package.json
```

npm adds the **package.json** file to the same level as the **src** directory.

The `babel-cli` package includes command line Babel tools, and the `babel-preset-env` package has the code that maps any JavaScript feature, ES6 and above (ES6+), to ES5.

```js
$ npm install babel-cli -D
$ npm install babel-preset-env -D
```

The `-D` flag instructs npm to add each package to a property called `devDependencies` in **package.json**. Once the project’s dependencies are listed in `devDependencies`, other developers can run your project without installing each package separately. Instead, they can simply run `npm install` — it instructs npm to look inside **package.json** and download all of the packages listed in `devDependencies`.

Once you `npm install` packages, you can find the Babel packages and all their dependencies in the **node_modules** folder. The new directory structure contains the following:

```js
project
|_ node_modules
|___ .bin
|___ ...
|_ src
|___ main.js
|_ package.json
```

### .babelrc

Now that you’ve downloaded the Babel packages, you need to specify the version of the source JavaScript code.

You can specify the initial JavaScript version inside of a file named **.babelrc**. In your root directory, you can run `touch .babelrc` to create this file.

Your project directory contains the following folders and files:

```js
project
|_ node_modules
|___ .bin
|___ ...
|_ src
|___ main.js
|_ .babelrc
|_ package.json
```

Inside **.babelrc** you need to define the *preset* for your source JavaScript file. The preset specifies the version of your initial JavaScript file.

Usually, you want to transpile JavaScript code from versions ES6 and later (ES6+) to ES5. From this point on, we will refer to our source code as ES6+, because Ecma introduces new syntax with each new version of JavaScript.

To specify that we are transpiling code from an ES6+ source, we have to add the following JavaScript object into **.babelrc**:

```js
{
  "presets": ["env"]
}
```

When you run Babel, it looks in **.babelrc** to determine the version of the initial JavaScript file. In this case, `["env"]` instructs Babel to transpile any code from versions ES6 and later.

There’s one last step before we can transpile our code. We need to specify a script in **package.json** that initiates the ES6+ to ES5 transpilation.

Inside of the **package.json** file, there is a property named `"scripts"` that holds an object for specifying command line shortcuts. It looks like this:

```js
...
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1"
}, ...
```

In the code above, the `"scripts"` property contains an object with one property called `"test"`. Below the `"test"` property, we will add a script that runs Babel like this:

```
...
"scripts": {
  "test": "echo \"Error: no test specified\" && exit 1",
  "build": "babel src -d lib"
}
```

In the `"scripts"` object above, we add a property called `"build"`. The property’s value, `"babel src -d lib"`, is a command line method that transpiles ES6+ code to ES5. Let’s consider each argument in the method call:

- `babel` — The Babel command call responsible for transpiling code.
- `src` — Instructs Babel to transpile all JavaScript code inside the **src** directory.
- `-d` — Instructs Babel to write the transpiled code to a directory.
- `lib` — Babel writes the transpiled code to a directory called `lib`.

In the next exercise, we’ll run the `babel src -d lib` method to transpile our ES6+ code.

```js
{
  "name": "learning-babel",
  "version": "1.0.0",
  "description": "Use Babel to transpile JavaScript ES6 to ES5",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.7.0"
  }
  "build": "babel src -d lib"
}

```

### Build

We’re ready to transpile our code! In the last exercise, we wrote the following script in **package.json**:

```
"build": "babel src -d lib"
```

Now, we need to call `"build"` from the command line to transpile and write ES5 code to a directory called `lib`.

From the command line, we type:

```
npm run build
```

The command above runs the `build` script in **package.json**.

Babel writes the ES5 code to a file named **main.js** (it’s always the same name as the original file), inside of a folder called `lib`. The resulting directory structure is:

```js
project
|_ lib
|___ main.js
|_ node_modules
|___ .bin
|___ ...
|_ src
|___ main.js
|_ .babelrc
|_ package.json
```

Notice, the directory contains a new folder named **lib**, with one file, called **main.js**.

The `npm run build` command will transpile all JavaScript files inside of the **src** folder. This is helpful as you build larger JavaScript projects — regardless of the number of JavaScript files, you only need to run one command (`npm run build`) to transpile all of your code.



## **INTERMEDIATE JAVASCRIPT MODULES**

# module.exports

We can get started with modules by defining a module in one file and making the module available for use in another file with Node.js `module.exports` syntax. Every JavaScript file run in Node has a local `module` object with an `exports` property used to define what should be exported from the file

```js
let Menu = {};
Menu.specialty = "Roasted Beet Burger with Mint Sauce";

module.exports = Menu; 
```

Let’s consider what this code means.

1. `let Menu = {};` creates the object that represents the module `Menu`. The statement contains an uppercase variable named `Menu` which is set equal to an empty object.
2. `Menu.specialty` is defined as a property of the `Menu` module. We add data to the `Menu` object by setting properties on that object and giving the properties a value.
3. `"Roasted Beet Burger with Mint Sauce";` is the value stored in the `Menu.specialty` property.
4. `module.exports = Menu;` exports the `Menu` object as a module. `module` is a variable that represents the module, and `exports` exposes the module as an object.

The pattern we use to export modules is thus:

1. Create an object to represent the module.
2. Add properties or methods to the module object.
3. Export the module with `module.exports`.

# require()

To make use of the exported module and the behavior we define within it, we import the module into another file. In Node.js, use the `require()` function to import modules.

For instance, say we want the module to control the menu’s data and behavior, and we want a separate file to handle placing an order. We would create a separate file **order.js** and import the `Menu` module from **menu.js** to **order.js** using `require()`. `require()` takes a file path argument pointing to the original module file.

In **order.js** we would write:

```js
const Menu = require('./menu.js');

function placeOrder() {
  console.log('My order is: ' + Menu.specialty);
}

placeOrder();
```

We can also wrap any collection of data and functions in an object, and export the object using `module.exports`. In **menu.js**, we could write:

```js
module.exports = {
  specialty: "Roasted Beet Burger with Mint Sauce",
  getSpecialty: function() {
    return this.specialty;
  } 
}; 
```



# Export default

Node.js supports `require()`/`module.exports`, but as of ES6, JavaScript supports a new more readable and flexible syntax for exporting modules. These are usually broken down into one of two techniques, *default export* and *named exports*.

We’ll begin with the first syntax, default export. The default export syntax works similarly to the `module.exports` syntax, allowing us to export one module per file.

```
let Menu = {};

export default Menu;
```

1. `export default` uses the JavaScript `export` statement to export JavaScript objects, functions, and primitive data types.
2. `Menu` refers to the name of the `Menu` object, the object that we are setting the properties on within our modules.

When using ES6 syntax, we use `export default` in place of `module.exports`. Node.js doesn’t support `export default` by default, so `module.exports` is usually used for Node.js development and ES6 syntax is used for front-end development. As with most ES6 features, it is common to transpile code since ES6 is [not supported by all browsers](https://caniuse.com/#feat=es6).

```js
let Airplane = {};
Airplane.availableAirplanes = [
{ 
    name: 'AeroJet',
  fuelCapacity: 800
 }, 
 {name: 'SkyJet',
  fuelCapacity: 500
 }
];
export default Airplane;
```



# Import

ES6 module syntax also introduces the `import` keyword for importing objects. In our **order.js** example, we import an object like this

```
import Menu from './menu';
```

Within the body of the `displayFuelCapacity` function, use `forEach()` to iterate over the `Airplane.availableAirplanes` array.

The `forEach()` should take an anonymous function as a parameter. We’ll add more in the next step.

Pass the anonymous function you created in the last step a parameter of `element`.

```js
import Airplane from './airplane';
function displayFuelCapacity() {

  Airplane.availableAirplanes.forEach(function(element) {

    console.log('Fuel Capacity of ' + element.name + ': ' + element.fuelCapacity);
  });
}
displayFuelCapacity();
```



# Named Exports

ES6 introduced a second common approach to export modules. In addition to `export default`, *named exports* allow us to export data through the use of variables.

```js
let specialty = '';
function isVegetarian() {
}; 
function isLowSodium() {
}; 

export { specialty, isVegetarian };
```

Example  

```js
let availableAirplanes = [{
 name: 'AeroJet',
 fuelCapacity: 800,
 availableStaff: ['pilots', 'flightAttendants', 'engineers', 'medicalAssistance', 'sensorOperators'],
}, 
{name: 'SkyJet',
 fuelCapacity: 500,
 availableStaff: ['pilots', 'flightAttendants']
}];
let flightRequirements = {
  requiredStaff: 4,
};
function meetsStaffRequirements(availableStaff, requiredStaff) {
  if (availableStaff.length >= requiredStaff) {
    return true;
  } else {
    return false;
  }
}
export { availableAirplanes, flightRequirements, meetsStaffRequirements};
```

## Named Imports

To import objects stored in a variable, we use the `import` keyword and include the variables in a set of `{}`.

```js
import { specialty, isVegetarian } from './menu';

console.log(specialty);
```

```js
import {availableAirplanes, flightRequirements, meetsStaffRequirements} from './airplane';
function displayFuelCapacity() {

}
function displayStaffStatus() {
  availableAirplanes.forEach(function(element) {
   console.log(element.name + ' meets staff requirements: ' + meetsStaffRequirements(element.availableStaff, flightRequirements.requiredStaff) );
  });
}
displayStaffStatus();
```

## Export Named Exports

Named exports are also distinct in that they can be exported as soon as they are declared, by placing the keyword `export` in front of variable declarations.

```js
export let specialty = '';
export function isVegetarian() {
}; 
function isLowSodium() {
}; 
```

Example  : 

```js
export let availableAirplanes = [
{name: 'AeroJet',
 fuelCapacity: 800,
 availableStaff: ['pilots', 'flightAttendants', 'engineers', 'medicalAssistance', 'sensorOperators'],
 maxSpeed: 1200,
 minSpeed: 300
}, 
{name: 'SkyJet',
 fuelCapacity: 500,
 availableStaff: ['pilots', 'flightAttendants'],
 maxSpeed: 800,
 minSpeed: 200
}
];
 export let flightRequirements = {
  requiredStaff: 4,
  requiredSpeedRange: 700
};
export function meetsSpeedRangeRequirements(maxSpeed, minSpeed, requiredSpeedRange) {
  let range = maxSpeed - minSpeed;
  if (range > requiredSpeedRange) {
    return true;
    } else {
    return false;
  }
};
export function meetsStaffRequirements(availableStaff, requiredStaff) {
  if (availableStaff.length >= requiredStaff) {
    return true;
  } else {
    return false;
  }
}

```

### Import Named Imports

To import variables that are declared, we simply use the original syntax that describes the variable name. In other words, exporting upon declaration does not have an impact on how we import the variables.

```js
import { specialty, isVegetarian } from 'menu';
```

## Export as

Named exports also conveniently offer a way to change the name of variables when we export or import them. We can do this with the `as` keyword.

```js
let specialty = '';
let isVegetarian = function() {
}; 
let isLowSodium = function() {
}; 

export { specialty as chefsSpecial, isVegetarian as isVeg, isLowSodium };
```

## Import as

To import named export aliases with the `as` keyword, we add the aliased variable in our import statement.

```js
import { chefsSpecial, isVeg } from './menu';
```

In **orders.js**

1. We import `chefsSpecial` and `isVeg` from the `Menu` object.
2. Here, note that we have an option to alias an object that was not previously aliased when exported. For example, the `isLowSodium` object that we exported could be aliased with the `as` keyword when imported: `import {isLowSodium as saltFree} from 'Menu';`

Another way of using aliases is to import the entire module as an alias:

```js
import * as Carte from './menu';

Carte.chefsSpecial;
Carte.isVeg();
Carte.isLowSodium(); 
```

### Combining Export Statements

We can also use named exports and default exports together. In **menu.js**:

```js
let specialty = '';
function isVegetarian() {
}; 
function isLowSodium() {
}; 
function isGlutenFree() {
};

export { specialty as chefsSpecial, isVegetarian as isVeg };
export default isGlutenFree;
```

### Combining Import Statements

We can import the collection of objects and functions with the same data.

We can use an `import` keyword to import both types of variables as such:

```js
import { specialty, isVegetarian, isLowSodium } from './menu';

import GlutenFree from './menu';
```

# What is a Promise?

Promises are objects that represent the eventual outcome of an asynchronous operation. A `Promise` object can be in one of three states:

- Pending**: The initial state— the operation has not completed yet.
- **Fulfilled**: The operation has completed successfully and the promise now has a *resolved value*. For example, a request’s promise might resolve with a JSON object as its value.
- **Rejected**: The operation has failed and the promise has a reason for the failure. This reason is usually an `Error` of some kind.

### Constructing a Promise Object

Let’s construct a promise! To create a new `Promise` object, we use the `new` keyword and the `Promise` constructor method:

```js
const executorFunction = (resolve, reject) => { };
const myFirstPromise = new Promise(executorFunction);
```

The executor function has two function parameters, usually referred to as the `resolve()` and `reject()` functions. The `resolve()` and `reject()` functions aren’t defined by the programmer. When the `Promise` constructor runs, JavaScript will pass **its own** `resolve()` and `reject()` functions into the executor function.

- `resolve` is a function with one argument. Under the hood, if invoked, `resolve()` will change the promise’s status from `pending` to `fulfilled`, and the promise’s resolved value will be set to the argument passed into `resolve()`.
- `reject` is a function that takes a reason or error as an argument. Under the hood, if invoked, `reject()` will change the promise’s status from `pending` to `rejected`, and the promise’s rejection reason will be set to the argument passed into `reject()`.

Let’s look at an example executor function in a `Promise` constructor:

```js
const executorFunction = (resolve, reject) => {
  if (someCondition) {
      resolve('I resolved!');
  } else {
      reject('I rejected!'); 
  }
}
const myFirstPromise = new Promise(executorFunction);
```

Example  :  

```js
const inventory = {
  sunglasses: 1900,
  pants: 1088,
  bags: 1344
};

// Write your code below:
const myExecutor=(resolve,reject)=>{
  if(inventory.sunglasses>0)
  {
    resolve('Sunglasses order processed.');
  }
  else
  {
    reject('That item is sold out.');
  }
  
};
function orderSunglasses()
{

  return (new Promise(myExecutor));
}
const orderPromise=orderSunglasses();
console.log(orderPromise);
```

### The Node setTimeout() Function

Rather than constructing promises, you’ll be handling `Promise` objects returned to you as the result of an asynchronous operation. These promises will start off pending but settle eventually.

To accomplish this, we’ll be using `setTimeout()`. `setTimeout()` is a Node API (a comparable API is provided by web browsers) that uses callback functions to schedule tasks to be performed after a delay. `setTimeout()` has two parameters: a callback function and a delay in milliseconds.

```js
const delayedHello = () => {
  console.log('Hi! This is an asynchronous greeting!');
};

setTimeout(delayedHello, 2000);
```

Here, we invoke `setTimeout()` with the callback function `delayedHello()` and `2000`. In at least two seconds `delayedHello()` will be invoked. But why is it “at least” two seconds and not exactly two seconds?

This delay is performed asynchronously—the rest of our program won’t stop executing during the delay. Asynchronous JavaScript uses something called *the event-loop*. After two seconds, `delayedHello()` is added to a line of code waiting to be run. Before it can run, any synchronous code from the program will run. Next, any code in front of it in the line will run. This means it might be more than two seconds before `delayedHello()` is actually executed.

Let’s look at how we’ll be using `setTimeout()` to construct asynchronous promises:

```js
const returnPromiseFunction = () => {
  return new Promise((resolve, reject) => {
    setTimeout(( ) => {resolve('I resolved!')}, 1000);
  });
};

const prom = returnPromiseFunction();
```



In the example code, we invoked `returnPromiseFunction()` which returned a promise. We assigned that promise to the variable `prom`. Similar to the asynchronous promises you may encounter in production, `prom` will initially have a status of pending.

### Consuming Promises

- The initial state of an asynchronous promise is `pending`
-  but we have a guarantee that it will settle. How do we tell the computer what should happen then? Promise objects come with an aptly named `.then()` method. It allows us to say, “I have a promise, when it settles, **then** here’s what I want to happen…
- `.then()` is a higher-order function— it takes two callback functions as arguments. We refer to these callbacks as *handlers*. 



## The onFulfilled and onRejected Functions

To handle a “successful” promise, or a promise that resolved, we invoke `.then()` on the promise, passing in a success handler callback function:



```js
const prom = new Promise((resolve, reject) => {
  resolve('Yay!');
});

const handleSuccess = (resolvedValue) => {
  console.log(resolvedValue);
};

prom.then(handleSuccess); // Prints: 'Yay!'
```

With typical promise consumption, we won’t know whether a promise will resolve or reject, so we’ll need to provide the logic for either case. We can pass both an `onFulfilled` and `onRejected` callback to `.then()`.

```js
let prom = new Promise((resolve, reject) => {
  let num = Math.random();
  if (num < .5 ){
    resolve('Yay!');
  } else {
    reject('Ohhh noooo!');
  }
});

const handleSuccess = (resolvedValue) => {
  console.log(resolvedValue);
};

const handleFailure = (rejectionReason) => {
  console.log(rejectionReason);
};

prom.then(handleSuccess, handleFailure);
checkInventory(order).then(handleSuccess,handleFailure);
```

## Using catch() with Promises

One way to write cleaner code is to follow a principle called *separation of concerns*. Separation of concerns means organizing code into distinct sections each handling a specific task. It enables us to quickly navigate our code and know where to look if something isn’t working.

```js
prom
  .then((resolvedValue) => {
    console.log(resolvedValue);
  })
  .then(null, (rejectionReason) => {
    console.log(rejectionReason);
  });
```

-  Since JavaScript doesn’t mind whitespace, we follow a common convention of putting each part of this chain on a new line to make it easier to read. To create even more readable code, we can use a different promise function: `.catch()`.

  The `.catch()` function takes only one argument, `onRejected`. In the case of a rejected promise, this failure handler will be invoked with the reason for rejection. Using `.catch()` accomplishes the same thing as using a `.then()` with only a failure handler.

  Let’s look at an example using `.catch()`:

  ```js
  prom
    .then((resolvedValue) => {
      console.log(resolvedValue);
    })
    .catch((rejectionReason) => {
      console.log(rejectionReason);
    });
  ```

Example  :

```js
checkInventory(order).then(handleSuccess).catch(handleFailure);
```

# Chaining Multiple Promises

One common pattern we’ll see with asynchronous programming is multiple operations which depend on each other to execute or that must be executed in a certain order.*** We might make one request to a database and use the data returned to us to make another request and so on***

This process of chaining promises together is called *composition*. Promises are designed with composition in mind! Here’s a simple promise chain in code:

```js
firstPromiseFunction()
.then((firstResolveVal) => {
  return secondPromiseFunction(firstResolveVal);
})
.then((secondResolveVal) => {
  console.log(secondResolveVal);
});
```

Example  :

```js
checkInventory(order)
.then((resolvedValueArray) => {
  // Write the correct return statement here:
 return processPayment(resolvedValueArray);
})
.then((resolvedValueArray) => {
  // Write the correct return statement here:
  return shipOrder(resolvedValueArray);
})
.then((successMessage) => {
  console.log(successMessage);
})
.catch((errorMessage) => {
  console.log(errorMessage);
});
```

# Avoiding Common Mistakes

Promise composition allows for much more readable code than the nested callback syntax that preceded it. However, it can still be easy to make mistakes. In this exercise, we’ll go over two common mistakes with promise composition.

**Mistake 1:** Nesting promises instead of chaining them.

```js
returnsFirstPromise()
.then((firstResolveVal) => {
  return returnsSecondValue(firstResolveVal)
    .then((secondResolveVal) => {
      console.log(secondResolveVal);
    })
})
```

Instead of having a clean chain of promises, we’ve nested the logic for one inside the logic of the other. Imagine if we were handling five or ten promises!

**Mistake 2:** Forgetting to `return` a promise.

```js
returnsFirstPromise()
.then((firstResolveVal) => {
  returnsSecondValue(firstResolveVal)
})
.then((someVal) => {
  console.log(someVal);
})
```

# Using Promise.all()

When done correctly, promise composition is a great way to handle situations where asynchronous operations depend on each other or execution order matters. What if we’re dealing with multiple promises, but we don’t care about the order? Let’s think in terms of cleaning again.

To maximize efficiency we should use *concurrency*, multiple asynchronous operations happening together. With promises, we can do this with the function `Promise.all()`.

- If every promise in the argument array resolves, the single promise returned from `Promise.all()` will resolve with an array containing the resolve value from each promise in the argument array.
- If any promise from the argument array rejects, the single promise returned from `Promise.all()` will immediately reject with the reason that promise rejected. This behavior is sometimes referred to as *failing fast*.

```js
let myPromises = Promise.all([returnsPromOne(), returnsPromTwo(), returnsPromThree()]);

myPromises
  .then((arrayOfValues) => {
    console.log(arrayOfValues);
  })
  .catch((rejectionReason) => {
    console.log(rejectionReason);
  });
```

- We declare `myPromises` assigned to invoking `Promise.all()`.
- We invoke `Promise.all()` with an array of three promises— the returned values from functions.
- We invoke `.then()` with a success handler which will print the array of resolved values if each promise resolves successfully.
- We invoke `.catch()` with a failure handler which will print the first rejection message if any promise rejects.

# The async Keyword

The `async` keyword is used to write functions that handle asynchronous actions. We wrap our asynchronous logic inside a function prepended with the `async` keyword. Then, we invoke that function.

```js
const myFunc = async () => {
  // Function body here
};

myFunc();
```



`async` functions always return a promise. This means we can use traditional promise syntax, like `.then()` and `.catch` with our `async` functions. An `async` function will return in one of three ways:

- If there’s nothing returned from the function, it will return a promise with a resolved value of `undefined`.
- If there’s a non-promise value returned from the function, it will return a promise resolved to that value.
- If a promise is returned from the function, it will simply return that promise

```js
async function fivePromise() { 
  return 5;
}

fivePromise()
.then(resolvedValue => {
    console.log(resolvedValue);
  })  // Prints 5
```

# The await Operator

- `async` functions are almost always used with the additional keyword `await` inside the function body.

- The `await` keyword can only be used inside an `async` function

- `await` is an operator: it returns the resolved value of a promise

- Since promises resolve in an indeterminate amount of time, `await` halts, or pauses, the execution of our `async` function until a given promise is resolved.

  ```js
  async function asyncFuncExample(){
    let resolvedValue = await myPromise();
    console.log(resolvedValue);
  }
  
  asyncFuncExample(); // Prints: I am resolved now!
  ```

  Now we’ll write two `async` functions which invoke `myPromise()`:

  ```js
  async function noAwait() {
   let value = myPromise();
   console.log(value);
  }
  
  async function yesAwait() {
   let value = await myPromise();
   console.log(value);
  }
  
  noAwait(); // Prints: Promise { <pending> }
  yesAwait(); // Prints: Yay, I resolved!
  ```

  In the first `async` function, `noAwait()`, we left off the `await` keyword before `myPromise()`. In the second, `yesAwait()`, we included it. The `noAwait()` function logs `Promise {  }` to the console. Without the `await` keyword, the function execution wasn’t paused. The `console.log()` on the following line was executed before the promise had resolved.

  Remember that the `await` operator returns the resolved value of a promise. When used properly in `yesAwait()`, the variable `value` was assigned the resolved value of the `myPromise()` promise, whereas in `noAwait()`, `value` was assigned the promise object itself.

  

  #### Handling Dependent Promises

  The true beauty of `async...await` is when we have a series of asynchronous actions which depend on one another. For example, we may make a network request based on a query to a database. In that case, we would need to wait to make the network request until we had the results from the database. With native promise syntax, we use a chain of `.then()` functions making sure to return correctly each one:

  ```js
  function nativePromiseVersion() {
      returnsFirstPromise()
      .then((firstValue) => {
          console.log(firstValue);
          return returnsSecondPromise(firstValue);
      })
     .then((secondValue) => {
          console.log(secondValue);
      });
  }
  ```

  

  Let’s break down what’s happening in the `nativePromiseVersion()` function:

  - Within our function we use two functions which return promises: `returnsFirstPromise()` and `returnsSecondPromise()`.
  - We invoke `returnsFirstPromise()` and ensure that the first promise resolved by using `.then()`.
  - In the callback of our first `.then()`, we log the resolved value of the first promise, `firstValue`, and then return `returnsSecondPromise(firstValue)`.
  - We use another `.then()` to print the second promise’s resolved value to the console.

  Here’s how we’d write an `async` function to accomplish the same thing:

  

  ```js
  async function asyncAwaitVersion() {
   let firstValue = await returnsFirstPromise();
   console.log(firstValue);
   let secondValue = await returnsSecondPromise(firstValue);
   console.log(secondValue);
  }
  ```

  

# Handling Errors

With `async...await`, we use `try...catch` statements for error handling. By using this syntax, not only are we able to handle errors in the same way we do with synchronous code, but we can also catch both synchronous and asynchronous errors. This makes for easier debugging!

```js
async function usingTryCatch() {
 try {
   let resolveValue = await asyncFunction('thing that will fail');
   let secondValue = await secondAsyncFunction(resolveValue);
 } catch (err) {
   // Catches any errors in the try block
   console.log(err);
 }
}

usingTryCatch();
```

# Handling Independent Promises

Remember that `await` halts the execution of our `async` function. This allows us to conveniently write synchronous-style code to handle dependent promises. But what if our `async` function contains multiple promises which are not dependent on the results of one another to execute

```js
async function serveDinner()
{
 const vegetablePromise = steamBroccoli();
 const starchPromise = cookRice();
 const proteinPromise = bakeChicken();
 const sidePromise = cookBeans();
 console.log(`Dinner is served. We're having ${await vegetablePromise}, ${await starchPromise}, ${await proteinPromise}, and ${await sidePromise}.`);
}
serveDinner();
```

# Await Promise.all()

Another way to take advantage of concurrency when we have multiple promises which can be executed simultaneously is to `await` a `Promise.all()`

```js
async function asyncPromAll() {
  const resultArray = await Promise.all([asyncTask1(), asyncTask2(), asyncTask3(), asyncTask4()]);
  for (let i = 0; i<resultArray.length; i++){
    console.log(resultArray[i]); 
  }
}
```

`Promise.all()` allows us to take advantage of asynchronicity— each of the four asynchronous tasks can process concurrently. `Promise.all()` also has the benefit of *failing fast*, meaning it won’t wait for the rest of the asynchronous actions to complete once any one has rejected. As soon as the first promise in the array rejects, the promise returned from `Promise.all()` will reject with that reason. As it was when working with native promises, `Promise.all()` is a good choice if multiple asynchronous tasks are all required, but none must wait for any other before executing.

```js
async function serveDinnerAgain(){
  let foodArray = await Promise.all([steamBroccoli(), cookRice(), bakeChicken(), cookBeans()]); 
  
  console.log(`Dinner is served. We're having ${foodArray[0]}, ${foodArray[1]}, ${foodArray[2]}, and ${foodArray[3]}.`)
}

serveDinnerAgain()
```

# HTTP Requests

Web developers use the event loop to create a smoother browsing experience by deciding when to call functions and how to handle asynchronous events. We’ll be exploring one system of technologies called Asynchronous JavaScript and XML, or AJAX.

To read more about the event loop, read the MDN documentation:

- [MDN Documentation: Event Loop](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)

# XHR GET Requests I

Asynchronous JavaScript and XML (AJAX), enables requests to be made after the initial page load. Initially, AJAX was used only for XML formatted data, now it can be used to make requests that have many different formats.

[MDN Documentation: Extensible Markup Language (XML)](https://developer.mozilla.org/en-US/docs/XML_introduction).

Similarly, the XMLHttpRequest (XHR) API, named for XML, can be used to make many kinds of requests and supports other forms of data.

# XHR GET Requests II

We are going to reconstruct XHR GET request boilerplate code step-by-step until we have written a complete GET request.

Feel free to refer to the XHR GET diagram at any point while completing this exercise:

- [XHR GET diagram](https://s3.amazonaws.com/codecademy-content/courses/intermediate-javascript-requests/diagrams/XHR+GET+diagram.svg)

Example

```js
/*The XMLHttpRequest object is used in JavaScript to create and send requests. To create a new instance of an object, you would use the new keyword. Like so:*/

/*Make sure the URL is wrapped in quotes so that it is a string.*/

const xhr = new XMLHttpRequest(); 
const url =  'https://api-to-call.com/endpoint';
xhr.responseType = 'json';
xhr.onreadystatechange = () => {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    return xhr.response;
}
};
xhr.open('GET', url);
xhr.send();
```

