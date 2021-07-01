import React from 'react';
import styled from 'styled-components';

const Create = (props) => {
    return(
        <Container>
            <Title>단어 추가하기</Title>
            <Border>
                <Card>
                    <p>단어</p>
                    <input type="text"/>
                </Card>
                <Card>
                    <p>설명</p>
                    <input type="text"/>
                </Card>
                <Card>
                    <p>예시</p>
                    <input type="text"/>
                </Card>
                <Button type="button">추가하기</Button>
            </Border>
        </Container>
    );
}

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
const Border = styled.div`
    max-width: 400px;
    width: 100%;
    padding: 40px;
    border-radius: 10px;
    background-color: rgba(255,255,255,.5);
`

const Title = styled.h1`
    text-align: center;
    font-size: 30px;
    margin: 0 0 30px;
`

const Card = styled.div`
    font-size: 20px;

    & > p {
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 5px;
    }
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