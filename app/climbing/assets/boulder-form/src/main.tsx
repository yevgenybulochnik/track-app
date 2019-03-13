import React from 'react';
import ReactDom from 'react-dom';
import './main.scss'

import {BoulderForm} from './components/boulderForm'

declare global {
  interface Window {
    props: any;
    react_mount: any;
  }
}


ReactDom.render(
  React.createElement(BoulderForm, window.props),
  window.react_mount
)
