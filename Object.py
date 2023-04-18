class Object:
    def __init__(self, label, probability, xmin, ymin, xmax, ymax, image_data, education):
        self.label = label
        self.probability = probability
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        self.image_data = image_data
        self.education = education
