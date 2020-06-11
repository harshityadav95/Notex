### Keyframe Animation change color

```
<style>
  div {
    height: 50px;
    width: 70%;
    background: black;
    margin: 50px auto;
    border-radius: 5px;
  }

  #rect {
  animation-name: rainbow;
  animation-duration: 4s;
  }
  @keyframes rainbow
  {
    0% {
        background-color: blue;
    }
    50% {
      background-color: green
    }
    100% {
      background-color: yellow;

    }
  }




</style>
<div id="rect"></div>


```

### Change button color with hover using animation 

```
<style>
  button {
    border-radius: 5px;
    color: white;
    background-color: #0F5897;
    padding: 5px 10px 8px 10px;
  }

  button:hover {
    animation-name: background-color;
    animation-duration: 500ms;
  }
  @keyframes background-color
  {
    100% {
      background-color:#4791d0;
    }

  }

</style>

<button>Register</button>
```

## Change the color of the button on Hover and remain that way 

```
<style>
  button {
    border-radius: 5px;
    color: white;
    background-color: #0F5897;
    padding: 5px 10px 8px 10px;
  }
  button:hover {
    animation-name: background-color;
    animation-duration: 500ms;
    /* Only change code below this line */
    animation-fill-mode:forwards;

    /* Only change code above this line */
  }
  @keyframes background-color {
    100% {
      background-color: #4791d0;
    }
  }
</style>
<button>Register</button>

```

## Create Movement Animation using CSS Animation

```
<style>
  div {
    height: 40px;
    width: 70%;
    background: black;
    margin: 50px auto;
    border-radius: 5px;
    position: relative;
  }

  #rect {
    animation-name: rainbow;
    animation-duration: 4s;
  }

  @keyframes rainbow {
    0% {
      background-color: blue;
      top: 0px;
      left:0px;

    }
    50% {
      background-color: green;
      top: 50px;
      left:25px;

    }
    100% {
      background-color: yellow;
      top: 0px;
      left:-25px;

    }
  }
</style>

<div id="rect"></div>
```



##  Fade the element as it moves 

```
<style>

  #ball {
    width: 70px;
    height: 70px;
    margin: 50px auto;
    position: fixed;
    left: 20%;
    border-radius: 50%;
    background: linear-gradient(
      35deg,
      #ccffff,
      #ffcccc
    );
    animation-name: fade;
    animation-duration: 3s;

  }

  @keyframes fade {
    50% {
      left: 60%;
      opacity:0.1;

    }
  }

</style>

<div id="ball"></div>

```



## Iterating animation in a loop 

```
<style>

  #ball {
    width: 100px;
    height: 100px;
    margin: 50px auto;
    position: relative;
    border-radius: 50%;
    background: linear-gradient(
      35deg,
      #ccffff,
      #ffcccc
    );
    animation-name: bounce;
    animation-duration: 1s;
    animation-iteration-count: infinite;
  }

  @keyframes bounce{
    0% {
      top: 0px;
    }
    50% {
      top: 249px;
      width: 130px;
      height: 70px;
    }
    100% {
      top: 0px;
    }
  }
</style>
<div id="ball"></div>

```

## Make a growing and shrinking animation by scaling 

```
<style>
  .back {
    position: fixed;
    padding: 0;
    margin: 0;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: white;
    animation-name: backdiv;
    animation-duration: 1s;
    animation-iteration-count: infinite;

  }

  .heart {
    position: absolute;
    margin: auto;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-color: pink;
    height: 50px;
    width: 50px;
    transform: rotate(-45deg);
    animation-name: beat;
    animation-duration: 1s;
    animation-iteration-count: infinite;


  }
  .heart:after {
    background-color: pink;
    content: "";
    border-radius: 50%;
    position: absolute;
    width: 50px;
    height: 50px;
    top: 0px;
    left: 25px;
  }
  .heart:before {
    background-color: pink;
    content: "";
    border-radius: 50%;
    position: absolute;
    width: 50px;
    height: 50px;
    top: -25px;
    left: 0px;
  }

  @keyframes backdiv {
    50% {
      background: #ffe6f2;
    }
  }

  @keyframes beat {
    0% {
      transform: scale(1) rotate(-45deg);
    }
    50% {
      transform: scale(0.6) rotate(-45deg);
    }
  }

</style>
<div class="back"></div>
<div class="heart"></div>

```

## Animate elements of CSS at different rate

```
<style>
  .stars {
    background-color: white;
    height: 30px;
    width: 30px;
    border-radius: 50%;
    animation-iteration-count: infinite;
  }

  .star-1 {
    margin-top: 15%;
    margin-left: 60%;
    animation-name: twinkle-1;
    animation-duration: 1s;
  }

  .star-2 {
    margin-top: 25%;
    margin-left: 25%;
    animation-name: twinkle-2;
    animation-duration: 1s;
  }

  @keyframes twinkle-1 {
    50% {
      transform: scale(0.5);
      opacity: 0.5;
    }
  }

  @keyframes twinkle-2 {
    20% {
      transform: scale(0.5);
      opacity: 0.5;
    }
  }


  #back {
    position: fixed;
    padding: 0;
    margin: 0;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(black, #000099, #66c2ff, #ffcccc, #ffeee6);
  }
</style>

<div id="back"></div>
<div class="star-1 stars"></div>
<div class="star-2 stars"></div>
```

## Animate Multiple Elements at Variable Rate

```
<style>
  .stars {
    background-color: white;
    height: 30px;
    width: 30px;
    border-radius: 50%;
    animation-iteration-count: infinite;
  }

  .star-1 {
    margin-top: 15%;
    margin-left: 60%;
    animation-duration: 1s;
    animation-name: twinkle;
  }

  .star-2 {
    margin-top: 25%;
    margin-left: 25%;
    animation-duration: 0.9s;
    animation-name: twinkle;
  }

  .star-3 {
    margin-top: 10%;
    margin-left: 50%;
    animation-duration: 1.1s;
    animation-name: twinkle;
  }

  @keyframes twinkle {
    20% {
      transform: scale(0.5);
      opacity: 0.5;
    }
  }

  #back {
    position: fixed;
    padding: 0;
    margin: 0;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(black, #000099, #66c2ff, #ffcccc, #ffeee6);
  }
</style>

<div id="back"></div>
<div class="star-1 stars"></div>
<div class="star-2 stars"></div>
<div class="star-3 stars"></div>

```

## Change Animation  speed with keyword

```
<style>

  .balls {
    border-radius: 50%;
    background: linear-gradient(
      35deg,
      #ccffff,
      #ffcccc
    );
    position: fixed;
    width: 50px;
    height: 50px;
    margin-top: 50px;
    animation-name: bounce;
    animation-duration: 2s;
    animation-iteration-count: infinite;
  }
  #ball1 {
    left:27%;
    animation-timing-function: linear;

  }
  #ball2 {
    left:56%;
    animation-timing-function: ease-out;

  }


  @keyframes bounce {
    0% {
      top: 0px;
    }
    100% {a
      top: 249px;
    }
  }

</style>

<div class="balls" id="ball1"></div>
<div class="balls" id="ball2"></div>

```

##  Curve Animation using Bezier Curves

```
cubic-bezier(0.25, 0.25, 0.75, 0.75);
```

## The viewport is a user's visible area of a web page, and is different depending on the device used to access the site.

Here's an example of a media query that returns the content when the device's width is less than or equal to 100px:

```
@media (max-width: 100px) { /* CSS Rules */ }
```

and the following media query returns the content when the device's height is more than or equal to 350px:

```
@media (min-height: 350px) { /* CSS Rules */ }
```

Remember, the CSS inside the media query is applied only if the media type matches that of the device being used.

```
<style>
  p {
    font-size: 20px;
  }

  /* Only change code below this line */
@media (max-height: 800px) { p {
    font-size: 10px;
  } }
  /* Only change code above this line */
</style>
```

## Make an Responsive Images using 

The `max-width` of `100%` will make sure the image is never wider than the container it is in, and the `height` of `auto` will make the image keep its original aspect ratio.

```
<style>
.responsive-img {
    max-width: 100%;
  height: auto;


}

img {
  width: 600px;
}
</style>
```

## Make Typography Responsive

The four different viewport units are:



- `vw` (viewport width): `10vw` would be 10% of the viewport's width.
- `vh` (viewport height): `3vh` would be 3% of the viewport's height.
- `vmin` (viewport minimum): `70vmin` would be 70% of the viewport's smaller dimension (height or width).
- `vmax` (viewport maximum): `100vmax` would be 100% of the viewport's bigger dimension (height or width).



Here is an example that sets a body tag to 30% of the viewport's width.

```
body { width: 30vw; }
```

```
<style>
h2 {width:80vw;}
p {width:75vmin}
</style>
```

