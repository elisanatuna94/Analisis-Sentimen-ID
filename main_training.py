from analiser import Analiser

# start analiser with set training data
an = Analiser(training_data='data/training_all_random.csv')

# train new model
an.train(filename='model')

test = "Kemarin jumpa tak sengaja @sahaL_AS. Masih ingat katakata dia: kalau RKUHP disahkan, tak akan bisa mundur lagi keadaan menjadi spt sebelumnya. Harus dicegah. Moral force harus bangkit. Mahasiswa yg bergerak perlu dikawal semua elemen. "
print test
print an.testFromTrained([an.tfidf_data.transform(test)])

test = "Ketika Habibie memimpin ICMI (Ikatan Cendekiawan Muslim Indonesia), banyak yg takut, atau sebaliknya berharap,   mereka akan memberi hak istimewa kpd elite Muslim. Ternyata tidak. Habibie dan banyak tokoh ICMI adalah pendukung kebhinekaan.#habibie"
print test
print an.testFromTrained([an.tfidf_data.transform(test)])
