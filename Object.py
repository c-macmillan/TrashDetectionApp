id2label = {
    0: 'cardboard',
    1: 'compost',
    2: 'glass',
    3:'metal',
    4: 'plastic'
}

class Object:
    def __init__(self, class_id, probability, education=""):
        self.label = id2label[class_id]
        self.probability = str(round(float(probability), 2) * 100) + "%"
        self.education = education
