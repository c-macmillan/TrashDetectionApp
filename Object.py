id2label = {
    0: 'cardboard',
    1: 'compost',
    2: 'glass',
    3:'metal',
    4: 'paper',
    5: 'plastic',
    6: 'trash'
}

id2bin = {
    0: 'recycle',
    1: 'compost',
    2: 'recycle',
    3:'recycle',
    4: 'recycle',
    5: 'recycle',
    6: 'landfill'
}

class Object:
    def __init__(self, class_id, probability, education=""):
        self.label = id2label[class_id]
        self.bin = id2bin[class_id]
        self.probability = str(round(float(probability), 2) * 100) + "%"
        self.education = education
