import React from 'react';
import ReactDOM from 'react-dom';


const TestComponent = ({users}) =>
  <div class='jumbotron'>
    <h1 class='display-4'>{ users[0].username }</h1>
    <a class="btn btn-primary" href="">Test button</a>
  </div>

ReactDOM.render(
  React.createElement(TestComponent, window.props),
  window.react_mount
)
