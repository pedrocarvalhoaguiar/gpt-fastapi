import logo from './logo.svg';
import './App.css';
import ChatGPT from "./components/home/Index";
import ChatList from "./components/chatList/Index";

function App() {
    return <div style={{backgroundColor: '#d9abab', display: 'flex', flexDirection: 'row'}}>
        <ChatList></ChatList>
        <ChatGPT></ChatGPT>
    </div>
}

export default App;
