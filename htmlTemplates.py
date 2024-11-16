css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
}

.chat-message.user {
    background-color: #2b313e;
    margin-left: 25%;
}

.chat-message.bot {
    background-color: #475063;
    margin-right: 25%;
}

.chat-message .avatar {
    width: 20%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.chat-message .avatar img {
    width: 100px;
    height: 100px;
    object-fit: cover;
}

.chat-message .message {
    width: 80%;
    color: #fff;
    padding-left: 1rem;
}

.chat-message user{
    margin-right: 25%;
}

.chat-message bot{
    margin-left: 25%;
}
</style>
'''

bot_template = '''
<div class="chat-message bot" style="margin-right: 25%;">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712126.png" alt="Bot Image">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''



user_template = '''
<div class="chat-message user" style="margin-left: 25%;">
    <div class="avatar">
        <img src="https://miro.medium.com/v2/resize:fit:1024/1*kS0_6KSm5mqfwsTqy6uz4A.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
