import {useEffect, useState} from "react";
import axios from "axios";
import {Link} from "react-router-dom";

function ChatList() {
    const [chats, setChats] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://localhost:8666/v1/chats?skip=0&limit=50&sort_field=created_at&sort_order=desc');
                if (response.status === 200) {
                    setChats(response.data.data);
                }
            } catch (error) {
                console.error(error);
            }
        };

        fetchData();
    }, []);
    console.log(chats)
    return (
        <div style={{width: '30%', display: 'flex'}}>
            <h1>Chat List</h1>
            <ul>
                {chats.map((chat) => (
                    <div key={chat.id} style={{minHeight: '30px'}}>
                        <Link to={`chat/${chat.ref_id}`}
                              style={{textDecoration: 'none', color: 'white'}}>{chat.id}</Link>
                    </div>
                ))}
            </ul>
        </div>
    );
}

export default ChatList