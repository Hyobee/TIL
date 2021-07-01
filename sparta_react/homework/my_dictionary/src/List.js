import React from 'react';
import styled from 'styled-components';

// 임시데이터
// 주의) "" 안에서 또 ""를 쓸 수 없어요! ''를 대신 써주세요. :)
const _word_list = [
    {
        id: "list_0",
        word: "ㅎ1ㅎ1",
        desc: "히히를 변형한 단어. 숫자 1을 'ㅣ'로 쓴다.",
        example: "저 친구가 초콜릿을 줬어. ㅎ1ㅎ1",
    },
    {
        id: "list_1",
        word: "ㅎ1ㅎ1",
        desc: "히히를 변형한 단어. 숫자 1을 'ㅣ'로 쓴다.",
        example: "저 친구가 초콜릿을 줬어. ㅎ1ㅎ1",
    },
    {
        id: "list_2",
        word: "ㅎ1ㅎ1",
        desc: "히히를 변형한 단어. 숫자 1을 'ㅣ'로 쓴다.",
        example: "저 친구가 초콜릿을 줬어. ㅎ1ㅎ1",
    },
    {
        id: "list_3",
        word: "ㅎ1ㅎ1",
        desc: "히히를 변형한 단어. 숫자 1을 'ㅣ'로 쓴다.",
        example: "저 친구가 초콜릿을 줬어. ㅎ1ㅎ1",
    },
];

const List = (props) => {
    const [word_list, setWordList] = React.useState(_word_list);

    //   state에 가짜 데이터 하나를 넣는 함수예요.
    const addWord = () => {
        // 넣을 가짜 데이터
        const word_item = {
            id: 'word_11111123132',
            word: "ㅎ2ㅎ2",
            desc: "안녕이라는 뜻",
            example: "펄이 ㅎ2ㅎ2!"
        };

        //   스프레드 문법을 써서 word_list에 있던 값을 전부 넣어주고, 추가할 데이터도 뒤에 넣어서 추가합니다.
        setWordList([...word_list, word_item]);
    };

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
                    {/* state에 값을 추가하기 위해 임시 추가 버튼을 하나 만들어줬어요. 누르면 가짜 데이터 하나가 바로 추가되게 해줄거예요. */}
                    <button onClick={addWord}>임시 추가 버튼</button>
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