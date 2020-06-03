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



