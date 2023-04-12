class Card:
    def __init__(self, text, is_face_up=False, action=None, is_outside=False):
        self.text = text
        self.is_face_up = is_face_up
        self.action = action
        self.is_outside = is_outside