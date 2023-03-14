---
tags: ['react', 'bootstrap', 'material']
title: Using UI Frameworks with React
description: How to use UI frameworks with react
pubDate: Fri, 29 November 2024
layout: "@/templates/BasePost.astro"
imgSrc: /imgs/2023/148139817.png
---

# Chapter 7 UI Frameworks with React
Bootstrap 5 is a popular front-end web development framework that provides a collection of HTML, CSS, and JavaScript tools and components for building responsive and mobile-first websites and web applications. It was released in May 2021 and is the latest version of the Bootstrap framework.

Bootstrap 5 comes with several new features and improvements compared to its previous versions, including a reduced file size, updated CSS utilities, new layout options, improved form controls, and a new icon set. It also includes improvements to its existing components, such as the navbar, card, modal, and carousel components.

Bootstrap 5 is designed to help developers quickly create responsive and accessible websites that work well on all devices and screen sizes. It provides a flexible grid system and a range of pre-built components that can be easily customized and extended to meet the specific needs of a project.


Reactstrap is a library of Bootstrap 4 components for React.js. It provides pre-built components like modals, navbar, forms, and more, that you can use in your React.js applications.

To get started with reactstrap, follow these steps:

1. Install React and reactstrap:


```tsx
npm install react react-dom reactstrap
```
2. Import required reactstrap components into your component:


```tsx
import { Button, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
```
3. Use the components in your JSX code:


```tsx
const Example = (props) => {
 const {
 buttonLabel,
 className
 } = props;

 const [modal, setModal] = useState(false);

 const toggle = () => setModal(!modal);

 return (
 <div>
 <Button color="danger" onClick={toggle}>{buttonLabel}</Button>
 <Modal isOpen={modal} toggle={toggle} className={className}>
 <ModalHeader toggle={toggle}>Modal title</ModalHeader>
 <ModalBody>
 Modal body text goes here.
 </ModalBody>
 <ModalFooter>
 <Button color="primary" onClick={toggle}>Do Something</Button>{' '}
 <Button color="secondary" onClick={toggle}>Cancel</Button>
 </ModalFooter>
 </Modal>
 </div>
 );
}

export default Example;
```
4. You can also add custom styles to the components using standard CSS classes or CSS-in-JS libraries like styled-components.

Reactstrap is a simple and easy-to-use library that can help you save a lot of time when building responsive and mobile-friendly web applications.


Bootstrap is a popular front-end development framework that helps developers create responsive and mobile-friendly websites and web applications. Some of the core concepts of Bootstrap include:

1. Grid system: Bootstrap uses a responsive grid system to create layouts for web pages. The grid system divides the screen into 12 columns and allows developers to create different column configurations for different screen sizes.
2. Components: Bootstrap provides a set of pre-built UI components that developers can use to create user interfaces quickly and easily. These components include forms, buttons, dropdowns, navbars, modals, and more.
3. Typography: Bootstrap includes a set of typography styles that developers can use to style text on their web pages. This includes headings, paragraphs, lists, and more.
4. Utilities: Bootstrap includes a set of utility classes that developers can use to quickly add spacing, alignment, and other styles to their web pages. These utility classes can help speed up the development process by eliminating the need for custom CSS.
5. JavaScript plugins: Bootstrap includes a set of JavaScript plugins that developers can use to add interactive features to their web pages. These plugins include carousels, modals, tooltips, and more.

By leveraging these core concepts, developers can create modern, responsive, and mobile-friendly web applications with minimal effort.


Sure, here's an example of how to create a basic landing page component using Reactstrap:


```tsx
import React from 'react';
import { Container, Row, Col, Button } from 'reactstrap';

const LandingPage = () => {
 return (
 <div className="landing-page">
 <Container>
 <Row>
 <Col md={6}>
 <h1>Welcome to My Landing Page</h1>
 <p>Thanks for visiting my landing page. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ut odio ac justo ultrices mollis. Nulla facilisi.</p>
 <Button color="primary">Learn More</Button>
 </Col>
 <Col md={6}>
 <img src="https://via.placeholder.com/500x500" alt="placeholder" />
 </Col>
 </Row>
 </Container>
 </div>
 );
};

export default LandingPage;
```
In this example, we're using the `Container`, `Row`, `Col`, and `Button` components from Reactstrap to create a simple landing page layout. The `Container` component provides a fixed-width container for our content, while the `Row` and `Col` components allow us to create a responsive grid layout. The `Button` component provides a styled button that we can use to link to other pages or sections of our site.

We're also using some basic HTML markup to create a heading, paragraph, and image. You can customize the content and styling of your landing page as needed.


In Reactstrap, you can use built-in classes to style components. Reactstrap follows the Bootstrap CSS framework, so it uses the same class names as Bootstrap. Here are some examples of how to use built-in classes to style Reactstrap components:


```tsx
import React from 'react';
import { Button } from 'reactstrap';

const StyledButton = () => {
 return (
 <div>
 <Button color="primary" className="btn-lg">Large Button</Button>
 <Button color="secondary" className="btn-sm">Small Button</Button>
 <Button color="danger" className="btn-block">Full-Width Button</Button>
 </div>
 );
};

export default StyledButton;
```
In this example, we're using the `Button` component from Reactstrap to create three different buttons. We're also using the `className` prop to add custom classes to each button:

* The first button uses the `btn-lg` class to make it a large button.
* The second button uses the `btn-sm` class to make it a small button.
* The third button uses the `btn-block` class to make it a full-width button.

You can also use other Bootstrap classes to style your components, such as `text-center` to center text or `bg-primary` to set a background color. Simply add the class name as a string to the `className` prop on the component you want to style.


Using SCSS mixins in Reactstrap is a great way to implement responsive design and style components in a modular and efficient way. Here's an example of how to use SCSS mixins to style a component in Reactstrap:


```tsx
s$primary-color: #007bff;
$secondary-color: #6c757d;

.btn {
 @include border-radius(0);
 @include box-shadow(none);

 &.btn-primary {
 @include background-image(linear-gradient($primary-color, darken($primary-color, 7.5%)));
 @include border-color($primary-color);

 &:hover {
 @include background-color(darken($primary-color, 7.5%));
 @include border-color(darken($primary-color, 7.5%));
 }
 }

 &.btn-secondary {
 @include background-image(linear-gradient($secondary-color, darken($secondary-color, 7.5%)));
 @include border-color($secondary-color);

 &:hover {
 @include background-color(darken($secondary-color, 7.5%));
 @include border-color(darken($secondary-color, 7.5%));
 }
 }
}
```
In this example, we define two variables for our primary and secondary colors. We then use SCSS mixins to style the `.btn` class and its child classes `.btn-primary` and `.btn-secondary`. We use the `border-radius` and `box-shadow` mixins to remove the default styles for all buttons, and then we use the `background-image`, `border-color`, and `background-color` mixins to style the primary and secondary buttons with gradients and hover effects.

To make this responsive, we can use Bootstrap's grid system and mixins to adjust the styles based on screen size. For example, we can use the `@include media-breakpoint-up` mixin to change the styles for larger screens:


```tsx
s.btn {
 @include border-radius(0);
 @include box-shadow(none);

 &.btn-primary {
 @include background-image(linear-gradient($primary-color, darken($primary-color, 7.5%)));
 @include border-color($primary-color);

 &:hover {
 @include background-color(darken($primary-color, 7.5%));
 @include border-color(darken($primary-color, 7.5%));
 }

 @include media-breakpoint-up(md) {
 @include background-image(linear-gradient($primary-color, darken($primary-color, 15%)));
 @include border-color($primary-color);

 &:hover {
 @include background-color(darken($primary-color, 15%));
 @include border-color(darken($primary-color, 15%));
 }
 }
 }

 // Same for .btn-secondary
}
```
In this example, we use the `@include media-breakpoint-up` mixin to change the styles for medium-sized screens and up. We double the gradient and hover effects for the primary button to make it more pronounced on larger screens. You can adjust the styles based on your own needs and use the built-in SCSS mixins to keep your styles modular and efficient.


Material UI is a popular React UI library that provides pre-built and customizable React components based on Google's Material Design guidelines. It is designed to help developers build high-quality, responsive, and mobile-friendly user interfaces quickly and easily. Material UI offers a wide range of components, including buttons, forms, navigation menus, sliders, and much more. It also provides various tools and utilities to make the development process more efficient, such as a responsive grid system, theme customization, and support for server-side rendering. Material UI is widely used by developers and companies to create visually appealing and functional web applications with minimal effort.


To get started with Material UI, you can follow these steps:

1. Create a new React project or use an existing one.
2. Install Material UI by running the following command in your project directory:


```tsx
java`npm install @material-ui/core
```
3. Once Material UI is installed, you can import any of the available components into your React components like this:


```tsx
import { Button } from '@material-ui/core';
```
4. You can then use the imported component like any other React component in your code:


```tsx
function MyButton() {
 return (
 <Button variant="contained" color="primary">
 Click Me!
 </Button>
 );
}
```
5. Customize the component's styles and behavior by passing props or using the provided classes and theme.
6. You can also explore the Material UI documentation and examples to learn more about the available components and features.

That's it! With these basic steps, you can start using Material UI in your React projects and take advantage of its powerful and flexible components to create beautiful and responsive user interfaces.


Here are some core concepts in Material UI:

1. Components: Material UI provides a large number of pre-built and customizable React components that follow the Material Design guidelines, including buttons, inputs, cards, dialogs, and many more.
2. Theme: Material UI allows you to define a global theme for your application, which includes typography, colors, spacing, and other design-related properties. This theme can be easily customized and applied to all components in your app.
3. Styling: Material UI provides a flexible and powerful styling system based on CSS-in-JS, which allows you to customize the look and feel of your components using a combination of inline styles, global styles, and theme-based styles.
4. Icons: Material UI includes a large collection of customizable icons that can be easily added to your components using the Icon component or the IconButton component.
5. Layout: Material UI provides several layout components that can help you structure your app, including Grid, Box, and Container.
6. Accessibility: Material UI is designed to be accessible and follows the Web Content Accessibility Guidelines (WCAG). It includes features such as keyboard navigation, focus management, and support for screen readers.

By understanding these core concepts, you can use Material UI to create beautiful, accessible, and responsive user interfaces in your React applications.


```tsx
import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { AppBar, Button, Toolbar, Typography } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
 root: {
 flexGrow: 1,
 },
 title: {
 flexGrow: 1,
 textAlign: 'center',
 },
 button: {
 margin: theme.spacing(1),
 },
}));

function LandingPage() {
 const classes = useStyles();

 return (
 <div className={classes.root}>
 <AppBar position="static">
 <Toolbar>
 <Typography variant="h6" className={classes.title}>
 Welcome to My App
 </Typography>
 <Button variant="contained" color="secondary" className={classes.button}>
 Sign In
 </Button>
 <Button variant="contained" color="primary" className={classes.button}>
 Sign Up
 </Button>
 </Toolbar>
 </AppBar>
 <div style={{ padding: '2rem' }}>
 <Typography variant="h4" gutterBottom>
 Our Awesome Features
 </Typography>
 <Typography variant="body1" gutterBottom>
 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec auctor velit sit amet erat luctus, non feugiat
 nisi vulputate. Nam elementum risus at purus cursus, non blandit leo bibendum.
 </Typography>
 <Typography variant="body1" gutterBottom>
 Phasellus dictum felis vel dui rutrum, nec consequat augue consequat. Duis vel sapien ultrices, commodo justo
 vel, aliquet neque. Proin lacinia nisl vel mi sagittis, eu fringilla enim mattis.
 </Typography>
 <Typography variant="body1" gutterBottom>
 In non dui ac quam blandit hendrerit. Nulla facilisi. Pellentesque quis orci at magna consectetur gravida.
 </Typography>
 <Typography variant="body1" gutterBottom>
 Suspendisse tincidunt odio eget mauris vehicula, vel imperdiet nunc consectetur. Nunc ac placerat eros, ut
 tristique metus. Nulla facilisi. Maecenas quis risus ultricies, tempor purus quis, ultrices diam.
 </Typography>
 <Typography variant="body1" gutterBottom>
 Fusce vulputate metus vel nisl tincidunt, nec fringilla sem vulputate. In hac habitasse platea dictumst.
 </Typography>
 </div>
 </div>
 );
}

export default LandingPage;
```
This landing page includes a Material UI AppBar at the top with a centered title and sign in/sign up buttons on the right side. It also includes some example content with typography components in a responsive layout. The `makeStyles` function is used to define custom styles for the component using Material UI's built-in style props and SCSS-like syntax.



Material UI provides two ways to style your components: using JavaScript and using CSS. Here's a brief overview of each approach:

Styling with JavaScript: Material UI's approach to styling with JavaScript is called JSS (JavaScript Style Sheets). JSS is a CSS-in-JS solution that allows you to write styles in JavaScript and attach them to your components. With JSS, you can easily create dynamic styles by accessing component props and state. You can also create global styles that apply to your entire application by using the createGlobalStyle API. Here's an example of using JSS to style a Button component:

```jsx
import { Button } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.contrastText,
    borderRadius: theme.shape.borderRadius,
    '&:hover': {
      backgroundColor: theme.palette.primary.dark,
    },
  },
}));

function MyButton(props) {
  const classes = useStyles();
  return <Button className={classes.root} {...props} />;
}
```

In this example, we define a makeStyles hook that creates a styles object for our Button component. The styles object defines the backgroundColor, color, borderRadius, and hover styles for our button. We then apply these styles to our Button component by passing the classes.root prop.

Styling with CSS: Material UI also allows you to style your components using CSS. To use CSS to style your components, you can create a separate CSS file and import it into your component. Material UI provides a class naming convention that makes it easy to target Material UI components with CSS. Here's an example of using CSS to style a Button component:

```jsx
import { Button } from '@material-ui/core';
import './MyButton.css';

function MyButton(props) {
  return <Button className="my-button" {...props} />;
}
```

In this example, we define a my-button class in a separate CSS file and import it into our component. We then apply the my-button class to our Button component by passing the className prop.

By using either the JSS or CSS approach to styling, you can customize the look and feel of your Material UI components in your React application.