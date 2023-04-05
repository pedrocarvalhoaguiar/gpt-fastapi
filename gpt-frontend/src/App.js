import './App.css';
import ChatGPT from "./components/home/Index";
import ChatList from "./components/chatList/Index";
import {Route, Routes, BrowserRouter} from 'react-router-dom'


function App() {
    return (
        <div style={{backgroundColor: '#d9abab', display: 'flex', flexDirection: 'row'}}>
            <BrowserRouter>
                <Routes>
                    <Route path='/chat/:refId' element={<ChatGPT />}/>
                    <Route path='/' element={<ChatList />}/>
                </Routes>
            </BrowserRouter>
        </div>
    );
}

export default App;
