import React, {useState, useEffect} from 'react';
import axios from 'axios';
import {useParams} from "react-router-dom";

function ChatGPT() {
    const [textInput, setTextInput] = useState('');
    const [answer, setAnswer] = useState('');
    const [question, setQuestion] = useState('')
    const [chatId, setChatId] = useState(null);
    const [messages, setMessages] = useState([])

    let params = useParams();

    useEffect(() => {
        const loadChat = async () => {
            try {
                const response = await axios.get(`http://localhost:8666/v1/chats/${params.refId}`);
                setChatId(response.data.data.id);
            } catch (error) {
                console.error(error);
            }
        };

        loadChat();
        const loadMessages = async () => {
            console.log(1)
            try {
                const response = await axios.get(`http://localhost:8666/v1/messages/${chatId}`);
                setMessages(response.data.id);
            } catch (error) {
                console.error(error);
            }
        };
        if (chatId) {
            loadMessages();
        }
    });

    const handleClick = async () => {
        try {
            const response = await axios.post('http://localhost:8666/v1/gpt-answer', {
                'input_text': textInput
            }, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            if (response.status === 200) {
                setAnswer(response.data.answer);
                setQuestion(textInput);

                await axios.post('http://localhost:8666/v1/messages', {
                    'type': 'input',
                    'text': textInput,
                    'chat': chatId
                });

                await axios.post('http://localhost:8666/v1/messages', {
                    'type': 'output',
                    'text': response.data.answer,
                    'chat': chatId
                });
            } else {
                setAnswer('Error: Could not get answer from server');
            }
        } catch (error) {
            console.error(error);
        }
    };


    return (
        <div style={{width: '70%'}}>
            {question && <div style={{display: "block"}}>Your question: {question}</div>}
            {answer && <div style={{display: 'block'}}>Answer: {answer}</div>}
            <input
                type="text"
                value={textInput}
                onChange={(e) => setTextInput(e.target.value)}
            />
            <button onClick={handleClick}>{chatId}</button>

        </div>
    );
}

export default ChatGPT;
