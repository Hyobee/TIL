import React from 'react';
import './App.css';

import Start from './Start';
import Quiz from './Quiz';
import Score from './Score';

class App extends React.Component {
  constructor(props){
    super(props)

    this.state = {
      name: '춘식이',
      page: 'quiz',
      list: [
        {question: '춘식이는 1살이다', answer: 'O'},
        {question: '춘식이는 2살이다', answer: 'O'},
        {question: '춘식이는 3살이다', answer: 'O'},
        {question: '춘식이는 4살이다', answer: 'O'}
      ],
      scoreMsg: "이 정도면 찐친 사이! 앞으로도 우리 우정 영원히",
    };
  }

  render (){
    return (
      <div className="App">
        {/* <Start name={this.state.name}/> */}
        {this.state.page === "quiz" && <Quiz list={this.state.list}/>}
        {this.state.page === "start" && <Start name={this.state.name}/>}
        {this.state.page === "score" && <Score name={this.state.name} scoreMsg={this.state.scoreMsg}/>}
      </div>
    );
  }
}

export default App;
