from flask import Flask
import random
app = Flask(__name__)
facts_list = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
              "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
              "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
              "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
              "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
              "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
              "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
              "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]
yazi_tura = ["yazı","tura"]
@app.route("/")
def hello_world():
    return '''<h1>Hello, World!</h1>
    <html>
    <a href="abc">Link Text</a>
    <a href="cbc">Rastgele gerçek</a>
    <a href="yazi_tura">Yazı Tura</a>
    <html>
    '''
@app.route("/abc")
def hello_world2():
    return '<h1>Diğer Site!</h1>'
@app.route("/cbc")
def helloworld3():
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/yazi_tura")
def helloworld4():
    return f"<p>{random.choice(yazi_tura)}</p>"




app.run(debug=True)

