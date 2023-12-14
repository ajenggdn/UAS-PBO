from flask import Flask, render_template, request, redirect, url_for 
# mengimport libary dari flask agar dapat menggunakan service web menggunakan bahasa python disini saya butuh render template untuk menampilkan file html, 
# request untuk menampung input dari html, dan url_for untuk mengarahkan form ke routing yang diinginkan

from flask_socketio import SocketIO, join_room, leave_room 
# mengimport libary socket untuk dapat menggunakan service realtime chat atau realtime notification, disini saya mengambil fungsi join room untuk mengakses room, 
# leave_room untuk meninggalkan room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ajengduarrr!'
socketio = SocketIO(app)
# Ini menciptakan objek aplikasi Flask (app) dan objek SocketIO (socketio). 
# SECRET_KEY digunakan untuk melindungi sesi aplikasi Flask. 

chat_rooms = {}
# membuat sebuah variabel berbentuk objek yang dapat menampung data room dari aplikasi chat

@app.route('/')
def index():
    return render_template('index.html')

# Ini fungsi route utama yang merender template 'index.html' saat pengguna mengakses halaman utama aplikasi.

@app.route('/chat', methods=['POST'])
def chat():
    username = request.form.get('username')
    room = request.form.get('room')
    return render_template('chat.html', username=username, room=room)

# Ini adalah route yang merespons data form yang disubmit oleh pengguna saat mereka masuk ke ruang obrol. 
# Data ini kemudian digunakan untuk merender template 'chat.html' dengan informasi username dan room.

@socketio.on('joined')
def handle_joined(data):
    username = data['username']
    room = data['room']
    join_room(room)
    socketio.emit('status', {'msg': username + ' has entered the room.'}, room=room)

# Event handler ini menangani peristiwa ketika pengguna bergabung ke dalam ruangan obrol. 
# user akan bergabung ke ruangan menggunakan join_room dan mengirim pesan ke semua pengguna di ruangan melalui socketio.emit.

@socketio.on('send_message')
def handle_send_message(data):
    username = data['username']
    message = data['message']
    room = data['room']
    socketio.emit('receive_message', {'username': username, 'message': message}, room=room)

# Event handler ini menangani peristiwa ketika pengguna mengirim pesan. 
# Pesan tersebut kemudian disiarkan ke semua pengguna di ruangan dengan menggunakan socketio.emit.

@socketio.on('left')
def handle_left(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    socketio.emit('status', {'msg': username + ' has left the room.'}, room=room)

# Event handler ini menangani peristiwa ketika pengguna keluar dari ruangan obrol. 
# Mereka meninggalkan ruangan menggunakan leave_room dan mengirim pesan ke semua pengguna di ruangan melalui socketio.emit.

if __name__ == '__main__':
    socketio.run(app, debug=True)

# Ini menjalankan aplikasi Flask menggunakan SocketIO. 
# Jika aplikasi dijalankan langsung (bukan diimpor sebagai modul), maka mode debug akan diaktifkan.