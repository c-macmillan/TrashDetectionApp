id2label = {
    0: 'cardboard',
    1: 'compost',
    2: 'glass',
    3: 'metal',
    4: 'paper',
    5: 'plastic',
    6: 'trash'
}

id2bin = {
    0: 'recycle',
    1: 'compost',
    2: 'recycle',
    3: 'recycle',
    4: 'recycle',
    5: 'recycle',
    6: 'landfill'
}

id2instruction = {
    'cardboard': 'Flatten cardboard boxes and separate from other paper products.',
    'compost': 'Separate/Rinse Food/Liquid before composting.',
    'glass': 'Separate by color and remove caps and lids.',
    'metal': 'Remove food residue and flatten cans to save space.',
    'paper': 'Recycle mixed paper products together.',
    'plastic': 'Check for local recycling regulations for specific types of plastic.',
    'trash': 'This item should be placed in the trash.'
}

class Object:
    def __init__(self, class_id, probability, education=""):
        self.label = id2label[class_id]
        self.bin = id2bin[class_id]
        self.probability = str(round(float(probability), 2) * 100) + "%"
        self.education = education
        self.instruction = id2instruction[self.label]
