import React from "react";
import styled from "styled-components";
import { useSelector } from "react-redux";


const List = (props) => {
    // const [word_list, setWordList] = React.useState(_word_list);

    //   리덕스에 있는 데이터를 가져와요!
    const word_list = useSelector((state) => state.word.word_list);

    return(
        <React.Fragment>
            <Container>
                <Title>My Dictionary</Title>
                <Border>
                    {word_list.map((w) => {
                        return(
                            <Card key={w.id}>
                                <CardLabel>단어</CardLabel>
                                <CardValue>{w.word}</CardValue>
                                <CardLabel>설명</CardLabel>
                                <CardValue>{w.desc}</CardValue>
                                <CardLabel>예시</CardLabel>
                                <CardValue>{w.example}</CardValue>
                            </Card>
                        );
                    })}
                    <AddButton
                        onClick={() => {
                        props.history.push("/create");
                        }}
                    >
                        +
                    </AddButton>
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
    height: 100vh;
    margin: 0 auto;
    padding: 20px;
    background-color: #a5c5d5;
`

// = 레이아웃
const Border = styled.div`
    max-width: 400px;
    width: 100%;
`

// = 제목
const Title = styled.h1`
    text-align: center;
    font-size: 30px;
    margin: 0 0 30px;
`

// = 카드
const Card = styled.div`
    border-radius: 10px;
    background-color: rgba(255,255,255);
    padding: 30px;

    & > input {
        width: 100%;
        border: 1px solid #e3e3e3;
        height: 40px;
        border-radius: 5px;
    }

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
`

// = 버튼
const AddButton = styled.button`
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 50px;
    height: 50px;
    border-radius: 50px;
    background-color: #6100ff;
    color: #ffffff;
    font-size: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
`;

export default List;