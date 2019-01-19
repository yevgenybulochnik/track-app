import React from 'react';
import ReactDOM from 'react-dom';
import './main.scss'

import {SessionForm} from './components/sessionForm'

ReactDOM.render(
  React.createElement(SessionForm, window.props),
  window.react_mount
)
