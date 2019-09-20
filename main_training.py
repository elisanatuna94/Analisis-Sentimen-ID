from analiser import Analiser

# start analiser with set training data
an = Analiser(training_data='data/training_all_random.csv')

# train new model
an.train(filename='model')

test = "Tai lu"
print test
print an.testFromTrained([an.tfidf_data.transform(test)])

test = "Ketika Habibie memimpin ICMI (Ikatan Cendekiawan Muslim Indonesia), banyak yg takut, atau sebaliknya berharap,   mereka akan memberi hak istimewa kpd elite Muslim. Ternyata tidak. Habibie dan banyak tokoh ICMI adalah pendukung kebhinekaan.#habibie"
print test
print an.testFromTrained([an.tfidf_data.transform(test)])
