from re import I
from flask import Flask, session, redirect, url_for, render_template, request, escape
app = Flask(__name__)
app.secret_key = 'isinya password buat session'
app.static_folder = 'static'

daftarGejala = ['demam','batuk','kehilangan indera perasa','sesak nafas','sulit berpikir jernih','pusing','malaise','mual','kelelahan dan nyeri otot','batuk terus-menerus',
               'sakit perut','batuk kering','flu','muntah','gangguan pendengaran','hilang selera makan','mulut kering','ruam di sekujur tubuh','mata merah dan berair','suhu tinggi',
               'kehilangan atau perubahan indera pengecapan atau penciuman','kelelahan','keringan di malam hari','tenggorokan gatal','sakit kepala','hilangnya indera penciuman',
               'sakit tenggorokan','nyeri sendi','hilangnya indera pengecapan','pegal-pegal']
daftarVarian = ['alpha','beta','gamma','delta','lambda','kappa','eta','mu','omicron']
gejala = 0

def checkGejala():
    if request.form.get('pilihan') == 'ya':
        return True
    if request.form.get('pilihan') == 'tidak':
        return False
    else:
        return checkGejala()

@app.route('/')
def index():
   session.pop('namaPasien', None)
   session.pop('gejalaPasien', None)
   session.pop('logs', None)
   session.pop('logs2', None)
   session['gejalaPasien'] = 0
   session['logs'] = 0
   return render_template('index.html', link = url_for('index'))

@app.route('/welcome',methods = ['POST', 'GET'])
def welcome():
   if request.method == 'POST':
      name = request.form.get('Name')
      session['namaPasien'] = name
      gejalanya = session['gejalaPasien']
      pertanyaan = daftarGejala[gejalanya]
      return render_template("welcome.html", name = name,  pertanyaan = pertanyaan, link = url_for('index'))

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      #=============================================================Logs 0
      if session['logs'] == 0 and checkGejala():
         if session['gejalaPasien'] == 0: # Gejala 1
            session['gejalaPasien'] = 1
            session['logs'] = 0
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 1:
              session['gejalaPasien'] = 2
              session['logs'] = 0
              return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 2:
              session['gejalaPasien'] = 3
              session['logs'] = 0
              return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 3:
              session['gejalaPasien'] = 4
              session['logs'] = 0
              return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 4:
              session['gejalaPasien'] = 5
              session['logs'] = 0
              return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 5:
              session['gejalaPasien'] = 6
              session['logs'] = 0
              return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 6:
              session['gejalaPasien'] = 7
              session['logs'] = 0
              return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 7:
              session['gejalaPasien'] = 8
              session['logs'] = 0
              return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 8 and session['logs']==0:
              terjangkitVarian = daftarVarian[0]
              return render_template("result.html", terjangkitVarian = terjangkitVarian, awal = url_for('index'))
      #=============================================================Logs 1
      else :
          if session['gejalaPasien'] == 1 and session['logs']==0:
             session['gejalaPasien'] = 9
             session['logs'] = 1
             return redirect(url_for('diagnosa'))
          elif session['gejalaPasien'] == 9 and session['logs'] == 1:
               terjangkitVarian = daftarVarian[1]
               return render_template("result.html", terjangkitVarian=terjangkitVarian, awal = url_for('index'))
        

@app.route('/diagnosa',methods = ['POST', 'GET'])
def diagnosa():
   name = session['namaPasien']
   pertanyaan = daftarGejala[session['gejalaPasien']]
   return render_template("diagnosa.html", pertanyaan = pertanyaan, name = name, link = url_for('index'))
   
@app.route('/home')
def home():
   return render_template("home.html")

if __name__ == '__main__':
   app.run(debug = True)