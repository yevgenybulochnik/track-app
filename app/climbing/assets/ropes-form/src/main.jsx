import React from 'react';
import ReactDOM from 'react-dom';
import './main.scss'

import {RopesForm} from './components/ropesForm'

ReactDOM.render(
  React.createElement(RopesForm, window.props),
  window.react_mount
)
