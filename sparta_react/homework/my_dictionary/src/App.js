import React from 'react';
import { Route } from 'react-router';
import {BrowserRouter} from "react-router-dom";

import styled from "styled-components";

import { firestore } from "./firebase";

import List from "./List";
import Create from "./Create";


const App = () => {
  return (
    <React.Fragment>
        <BrowserRouter>
          <Route path="/" exact component={List} />
          <Route path="/create" exact component={Create} />
        </BrowserRouter>
    </React.Fragment>
  );
}

export default App;