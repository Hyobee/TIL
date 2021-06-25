import React from 'react';
import img from './lion.gif'

const Start = (props) => {
    return (
        <div className="container">
            <div className="box-section">
                <img className="box-img" src={img}/>
                <h1 className="box-title">나는 <span className="highlight">{props.name}</span>에 대해 얼마나 알고있을까?</h1>
                <input className="box-input" type="text" placeholder="이름"/>
                <button className="box-btn">시작하기</button>
            </div>
        </div>
    )
}

export default Start;
