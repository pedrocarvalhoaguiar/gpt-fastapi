import React, {useState} from 'react';
import axios from 'axios';

function GptAnswer() {
    const [textInput, setTextInput] = useState('');
    const [answer, setAnswer] = useState('');
    const [question, setQuestion] = useState('')
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

                const chatResponse = await axios.post('http://localhost:8666/v1/chats', {});
                const chatId = chatResponse.data.id;
                console.log(chatId)
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
        <div style={{width: '70%', display: "flex"}}>
            <input
                type="text"
                value={textInput}
                onChange={(e) => setTextInput(e.target.value)}
            />
            <button onClick={handleClick}>Submit</button>
            {question && <div>Your question: {question}</div>}
            {answer && <div>{answer}</div>}
        </div>
    );
}

export default GptAnswer;
