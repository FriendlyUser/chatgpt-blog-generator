---
tags: ['react']
title: React Basics
description: How to use JSX and the components lifecycle
pubDate: Fri, 29 November 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/430118953.png
---

# Chapter 2 React Basics

JSX (JavaScript XML) is a syntax extension for JavaScript. It allows you to write HTML-like code in your JavaScript files. JSX code is compiled to JavaScript code at runtime, allowing you to use HTML-like syntax to define the structure and content of your components.

To use JSX in your Next.js application, you can create a file with the `.jsx` extension, and then use JSX syntax in your code. Here's an example of a basic JSX component:


```tsx
import React from 'react';

function MyComponent() {
 return (
 <div>
 <h1>Hello, world!</h1>
 </div>
 );
}
```
In this example, we're importing the `React` library, which is required to use JSX. We're then defining a functional component called `MyComponent`, which returns a JSX element. The JSX element is a `<div>` element containing an `<h1>` element with the text "Hello, world!".

When this component is rendered, the JSX code is compiled to JavaScript code that creates the corresponding HTML elements.

JSX supports all HTML attributes, as well as custom attributes and event handlers. Here's an example of a button element with a custom `onClick` event handler:


```tsx
import React from 'react';

function MyComponent() {
 function handleClick() {
 console.log('Button clicked');
 }

 return (
 <button onClick={handleClick}>
 Click me
 </button>
 );
}
```
In this example, we're defining a function called `handleClick` that logs a message to the console when the button is clicked. We're then defining a button element with an `onClick` attribute that calls the `handleClick` function when the button is clicked.

JSX is a powerful tool that makes it easy to create dynamic and interactive user interfaces in your Next.js application. By using JSX syntax in your components, you can define the structure and content of your UI in a clear and concise way.


In React and Next.js, components are the building blocks of your application's user interface. They are reusable pieces of code that can be composed together to create more complex UI elements.

A component can be defined as a function or a class. Here's an example of a functional component that takes a prop called `name` and uses it to display a greeting:


```tsx
function Greeting(props) {
 return <h1>Hello, {props.name}!</h1>;
}
```
In this example, we're defining a functional component called `Greeting`. The component takes a single prop called `name`, which is used to display a greeting message. The `{props.name}` expression inside the JSX code is used to interpolate the `name` prop value into the HTML output.

Props are a way to pass data from a parent component to a child component. They are like function arguments, but for React components. Here's an example of how to use the `Greeting` component from above:


```tsx
function App() {
 return <Greeting name="Alice" />;
}
```
In this example, we're defining a functional component called `App`. The `App` component renders the `Greeting` component and passes it a prop called `name` with the value "Alice". When the `Greeting` component is rendered, it will display the message "Hello, Alice!".

Props can be used to pass any kind of data to a component, including primitive values like strings and numbers, objects, arrays, and functions. Here's an example of a component that takes an array of items as a prop and uses it to render a list:


```tsx
function List(props) {
 const items = props.items.map(item => <li>{item}</li>);
 return <ul>{items}</ul>;
}
```
In this example, we're defining a functional component called `List`. The component takes a prop called `items`, which is an array of strings. The component uses the `map` method to create an array of `<li>` elements, one for each item in the `items` prop array. The resulting array of `<li>` elements is then rendered inside a `<ul>` element.

Components and props are key concepts in React and Next.js development. By using components and props, you can create reusable, composable UI elements that make your application more maintainable and easier to develop.


In React and Next.js, there are two ways to define components: class components and functional components. Both types of components have their own syntax and use cases.

Class components are defined as ES6 classes that extend the `React.Component` base class. Here's an example of a class component that takes a prop called `name` and uses it to display a greeting:


```tsx
class Greeting extends React.Component {
 render() {
 return <h1>Hello, {this.props.name}!</h1>;
 }
}
```
In this example, we're defining a class component called `Greeting`. The component defines a `render` method that returns a JSX element. The JSX element uses the `this.props.name` expression to interpolate the `name` prop value into the HTML output.

Functional components are defined as functions that take props as their input and return a JSX element. Here's an example of a functional component that takes a prop called `name` and uses it to display a greeting:


```tsx
function Greeting(props) {
 return <h1>Hello, {props.name}!</h1>;
}
```
In this example, we're defining a functional component called `Greeting`. The component takes a single prop called `name`, which is used to display a greeting message. The `{props.name}` expression inside the JSX code is used to interpolate the `name` prop value into the HTML output.

Functional components are simpler and more lightweight than class components. They don't have their own state or lifecycle methods, which makes them easier to reason about and test. However, they can't be used for more advanced features like managing component state or using lifecycle methods.

In general, it's recommended to use functional components whenever possible, as they are easier to read and write. However, there are still some cases where class components are necessary, such as when managing component state or using lifecycle methods.


In React and Next.js, state and lifecycle methods are important concepts for managing the dynamic behavior of your application.

State is an object that contains data that can change over time. It's usually used to represent user input, server responses, or other dynamic data. You can define state in a class component by setting a `state` property in the component's constructor:


```tsx
class Counter extends React.Component {
 constructor(props) {
 super(props);
 this.state = { count: 0 };
 }

 render() {
 return (
 <div>
 <p>Count: {this.state.count}</p>
 <button onClick={() => this.setState({ count: this.state.count + 1 })}>
 Increment
 </button>
 </div>
 );
 }
}
```
In this example, we're defining a class component called `Counter`. The component defines a `constructor` method that initializes the `state` property with a `count` property set to 0. The component's `render` method displays the current value of the `count` state property and a button that updates the `count` state when clicked.

Lifecycle methods are methods that are called at different stages of a component's life cycle. They're used to perform actions like initializing state, updating the DOM, or fetching data from a server. Here's an example of a component that uses the `componentDidMount` lifecycle method to fetch data from an API:


```tsx
class DataViewer extends React.Component {
 constructor(props) {
 super(props);
 this.state = { data: null };
 }

 componentDidMount() {
 fetch('https://api.example.com/data')
 .then(response => response.json())
 .then(data => this.setState({ data }));
 }

 render() {
 if (this.state.data === null) {
 return <p>Loading data...</p>;
 }
 return <p>Data: {this.state.data}</p>;
 }
}
```
In this example, we're defining a class component called `DataViewer`. The component defines a `constructor` method that initializes the `state` property with a `data` property set to `null`. The component's `componentDidMount` lifecycle method fetches data from an API and updates the `data` state property when the response is received. The `render` method displays a loading message while the data is being fetched, and the data itself once it's available.

State and lifecycle methods are powerful tools for building dynamic, responsive user interfaces in React and Next.js. By using state and lifecycle methods, you can create components that respond to user input, fetch data from servers, and update the DOM in real time.


To install React packages in your project, you can use either npm or yarn package managers. Both tools are commonly used in the React and Next.js ecosystem and offer similar functionality.

To install a React package using npm, you can run the following command in your project's root directory:


```tsx
npm install <package-name>
```
For example, to install the `react-router-dom` package, you can run:


```tsx
npm install react-router-dom
```
To install a React package using yarn, you can run the following command in your project's root directory:


```tsx
yarn add <package-name>
```
For example, to install the `react-router-dom` package, you can run:


```tsx
yarn add react-router-dom
```
Both npm and yarn will automatically download the package and its dependencies and add them to your project's `node_modules` directory. Once the package is installed, you can import it into your code using a `import` statement.

For example, to use the `BrowserRouter` component from the `react-router-dom` package in your code, you can import it like this:


```tsx
import { BrowserRouter } from 'react-router-dom';
```
By using either npm or yarn to install React packages, you can easily add powerful and useful functionality to your React and Next.js applications.


To install React packages in your project, you can use either npm or yarn package managers. Both tools are commonly used in the React and Next.js ecosystem and offer similar functionality.

To install a React package using npm, you can run the following command in your project's root directory:


```tsx
npm install <package-name>
```
For example, to install the `react-router-dom` package, you can run:


```tsx
npm install react-router-dom
```
To install a React package using yarn, you can run the following command in your project's root directory:


```tsx
yarn add <package-name>
```
For example, to install the `react-router-dom` package, you can run:


```tsx
yarn add react-router-dom
```
Both npm and yarn will automatically download the package and its dependencies and add them to your project's `node_modules` directory. Once the package is installed, you can import it into your code using a `import` statement.

For example, to use the `BrowserRouter` component from the `react-router-dom` package in your code, you can import it like this:


```tsx
import { BrowserRouter } from 'react-router-dom';
```
By using either npm or yarn to install React packages, you can easily add powerful and useful functionality to your React and Next.js applications.

### React spring

React-spring is a popular animation library for React applications. It allows developers to create smooth and natural animations using physics-based models. The library provides a wide range of animation options and can be used to animate various elements such as text, images, and even entire components.

One of the key features of react-spring is its ability to create complex animations with ease. The library provides a simple API that allows developers to define animations using intuitive spring-based models. This makes it easy to create realistic animations that mimic real-world physics.

Another advantage of react-spring is its performance. The library uses efficient algorithms and techniques to ensure that animations run smoothly even on low-end devices. This makes it an ideal choice for developers looking to create high-performance applications.

In conclusion, react-spring is a powerful animation library that offers a wide range of features and benefits. Its intuitive API and efficient performance make it an excellent choice for developers looking to add smooth and natural animations to their React applications.


```js
import {useSpring, animated} from 'react-spring'

function FadeIn() {
  const props = useSpring({opacity: 1, from: {opacity: 0}})
  return <animated.div style={props}>I will fade in</animated.div>
}
```


In this example, we use the useSpring hook to define an animation that transitions the opacity of an element from 0 to 1. We then apply this animation to a div element using the animated.div component provided by react-spring.

This is just one simple example of what you can do with react-spring. The library provides many other hooks and components that allow you to create complex animations with ease.

```js
import {useSpring, animated} from 'react-spring'

function SpringAnimation() {
  const props = useSpring({x: 100, from: {x: 0}})
  return (
    <animated.div
      style={{
        transform: props.x.interpolate(x => `translate3d(${x}px,0,0)`)
      }}
    >
      I will move to the right
    </animated.div>
  )
}
```

In this example, we use the useSpring hook to define an animation that transitions the x property of an element from 0 to 100. We then apply this animation to a div element using the animated.div component and the transform CSS property.

This is another simple example of what you can do with react-spring. The library provides many other hooks and components that allow you to create complex animations with ease.


```js
import {useTrail, animated} from 'react-spring'

const items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
const config = {mass: 5, tension: 2000, friction: 200}

function TrailAnimation() {
  const [toggle, set] = useState(true)
  const trail = useTrail(items.length, {
    config,
    opacity: toggle ? 1 : 0,
    x: toggle ? 0 : 20,
    height: toggle ? 80 : 0,
    from: {opacity: 0, x: 20, height: 0},
  })

return (
    <div>
      <button onClick={() => set(state => !state)}>Toggle</button>
      <div>
        {trail.map(({x, height, ...rest}, index) => (
          <animated.div
            key={items[index]}
            className="trails-text"
            style={{...rest}}
          >
            <animated.div style={{transform: x.interpolate(x => `translate3d(0,${x}px,0)`)}}>
              {items[index]}
            </animated.div>
          </animated.div>
        ))}
      </div>
    </div>
   )
}
```

In this example we use the useTrail hook to create a trail animation that animates multiple elements at once. We define an array of items and pass it to the useTrail hook along with a configuration object that specifies the mass, tension and friction of the animation.

We then use the trail array returned by the useTrail hook to render each item in our list. We apply the animation to each item using the animated.div component and various CSS properties such as opacity, height, and transform.

This is a more complex example that shows some of the advanced features of react-spring. The library provides many other hooks and components that allow you to create even more complex animations with ease.

<iframe src="https://codesandbox.io/embed/youthful-chatelet-9tyow5?fontsize=14&hidenavigation=1&theme=dark"
     style="width:100%; height:500px; border:0; border-radius: 4px; overflow:hidden;"
     title="youthful-chatelet-9tyow5"
     allow="accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking"
     sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"
   ></iframe>

### References

- https://codesandbox.io/s/youthful-chatelet-9tyow5?file=/src/App.js