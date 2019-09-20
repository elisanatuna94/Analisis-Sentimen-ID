from analiser import Analiser

# start analiser with set training data
an = Analiser(training_data='data/training_all_random.csv')

# train new model
an.train(filename='model')

test = "Kemarin jumpa tak sengaja @sahaL_AS. Masih ingat katakata dia: kalau RKUHP disahkan, tak akan bisa mundur lagi keadaan menjadi spt sebelumnya. Harus dicegah. Moral force harus bangkit. Mahasiswa yg bergerak perlu dikawal semua elemen. "
print test
print an.testFromTrained([an.tfidf_data.transform(test)])

test = "Tempo pantas dikritik tiap kali ia bias atau keliru. Tapi ingat: pers tak sekuasa politisi di Senayan.  Apalagi di zaman ini. Di Senayan “wakil rakyat”— dgn gaji besar meskipun malas —bisa membuat undang2 yg mengatur kehidupan bangsa, meskipun tak adil.#bela"
print test
print an.testFromTrained([an.tfidf_data.transform(test)])
