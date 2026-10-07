from flask import Flask

# Membuat objek aplikasi Flask
app = Flask(__name__)

# Menentukan route untuk halaman utama (root)
@app.route('/')
def home():
    return "Halo, ini halaman utama Flask!"

# Menjalankan server lokal
if __name__ == '__main__':
    app.run(debug=True)
