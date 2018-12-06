import React from 'react';
import ReactDOM from 'react-dom';
//import App from "./components/App";
import './screen.css';
import {App} from './components/App';

import '!style-loader!css-loader!./css/bootstrap.min.css';

ReactDOM.render(<App />, document.getElementById('content'));