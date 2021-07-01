import React from 'react';
import { Route } from 'react-router';
import {BrowserRouter} from "react-router-dom";

import styled from "styled-components";

import List from "./List";
import Create from "./Create";


class App extends React.Component {

  constructor(props) {
    super(props);
    // App 컴포넌트의 state를 정의해줍니다.
    this.state = {
      list: ["영화관 가기", "매일 책읽기", "수영 배우기"],
    };
  }

  // constructor(props){
  //   super(props);
  //   this.state={
  //     word: '단어',
  //     page: 'create',
  //     desc: '단어설명',
  //   };
  // }
  
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