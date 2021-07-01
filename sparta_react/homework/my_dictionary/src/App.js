import React from 'react';
import { Route } from 'react-router';
import {BrowserRouter} from "react-router-dom";

import styled from "styled-components";

import List from "./List";
import Create from "./Create";


class App extends React.Component {

  constructor(props){
    super(props);
    this.state={
      word: '단어',
      page: 'create',
      desc: '단어설명',
    };
  }
  
  render(){
    return (
      <div className="App">
        {/* 실제로 연결해볼까요! */}
        <Route path="/" exact component={List} />
        <Route path="/create" component={Create} />
      </div>
    );
  }
}

export default App;