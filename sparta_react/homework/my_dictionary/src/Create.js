import React from "react";
import styled from "styled-components";

import { useDispatch } from "react-redux";
import { createWord } from "./redux/modules/word";

const Create = (props) => {
    const dispatch = useDispatch();

    const word_ref = React.useRef(null);
    const desc_ref = React.useRef(null);
    const example_ref = React.useRef(null);

    const addWord = () => {
        //   가짜 데이터가 어떻게 생겨야 할까? 미리 생김새부터 떠올려봅니다.
        //  1. {} <- 이런 딕셔너리 안에,
        //  2. id, word, desc, example이 들어간다!
        //     - 그럼 생김새는? {id: ~~~, word: ~~~, desc: ~~~, example: ~~~} 이렇게 생겨야죠!
        //  3. 그럼 word, desc, example은 어디에서 가져올까요? -> ref에서 가져와야겠죠!
        //     - useRef를 먼저 잡아주고, input의 ref에 넣어줍니다. 그리고 ref담고 있는 변수명.currect로 가져오면 끝!
    
        const word = {
            id: 'word_11111', // id는 임시로 아무거나 넣어요
            word: word_ref.current.value, // input에서 text값에 접근하려면 ~~.value로 접근해요. (word_ref.current가 input이에요.)
            desc: desc_ref.current.value,
            example: example_ref.current.value
        }
    
        // 리덕스에 가짜 데이터를 넣어볼게요!
        dispatch(createWord(word));
        // 데이터를 넣고 나면 목록 페이지로 이동합시다.
        props.history.replace('/');
    }

    return(
        <React.Fragment>
            <Container>
                <Title>단어 추가하기</Title>
                <Border>
                    <Card>
                        <FormGroup>
                            <CardLabel>단어</CardLabel>
                            <CardValue><input ref={word_ref} /></CardValue>
                        </FormGroup>
                        <FormGroup>
                            <CardLabel>설명</CardLabel>
                            <CardValue><input ref={desc_ref} /></CardValue>
                        </FormGroup>
                        <FormGroup>
                            <CardLabel>예시</CardLabel>
                            <CardValue><input ref={example_ref} /></CardValue>
                        </FormGroup>
                    </Card>
                    <Button onClick={addWord}>추가하기</Button>
                </Border>
            </Container>
        </React.Fragment>
    );
}


// = 콘테이너
const Container = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    min-height: 100vh;
    margin: 0 auto;
    padding: 20px;
    background-color: #a5c5d5;
`

// = 레이아웃
const Border = styled.div`
    max-width: 400px;
    width: 100%;
    padding: 40px;
    border-radius: 10px;
    background-color: rgba(255,255,255,.5);
`

// = 제목
const Title = styled.h1`
    text-align: center;
    font-size: 30px;
    margin: 0 0 30px;
`

// = 카드
const Card = styled.div`
    font-size: 20px;

    & > p {
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    & + div {
        margin-top: 30px;
    }
`
const FormGroup = styled.div`
    & + div {
        margin-top: 30px;
    }
`

// = 카드 레이블
const CardLabel = styled.p`
    font-size: 16px;
    font-weight: bold;
    margin-top: 0;
    margin-bottom: 5px;
`

// = 카드 데이터
const CardValue = styled.div`
    font-size: 16px;

    & > input {
        width: 100%;
        border: 1px solid #e3e3e3;
        height: 40px;
        border-radius: 5px;
    }
`

// = 버튼
const Button = styled.button`
    width: 100%;
    height: 45px;
    font-size: 18px;
    color: #fff;
    background-color: #0d6efd;
    border-radius: 5px;
    border: 0;
    margin-top: 30px;
    cursor: pointer;
`


export default Create;