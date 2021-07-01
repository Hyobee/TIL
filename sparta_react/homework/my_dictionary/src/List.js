import React from 'react';
import styled from 'styled-components';

const List = () => {
    return(
        <Container>
            <Title>My Dictionary</Title>
            <Border>
                <Card>
                    <p>단어</p>
                    <div></div>
                    <p>설명</p>
                    <div></div>
                </Card>
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
`

const Title = styled.h1`
    text-align: center;
    font-size: 30px;
    margin: 0 0 30px;
`

const Card = styled.div`
    border-radius: 10px;
    background-color: rgba(255,255,255,.5);
    padding: 40px;

    & > p {
        font-size: 16px;
        font-weight: bold;
        margin-top: 0;
        margin-bottom: 5px;
    }
    & > input {
        width: 100%;
        border: 1px solid #e3e3e3;
        height: 40px;
        border-radius: 5px;
    }

    & > div {

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

export default List;