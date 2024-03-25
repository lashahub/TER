class Category:
    def __init__(self, row):
        self.d1 = row['category_d1']
        self.d2 = row['category_d2']
        self.d3 = row['category_d3']
        self.d4 = row['category_d4']
        self.d5 = row['category_d5']
        self.d6 = row['category_d6']

    def __str__(self):
        return f"d1: {self.d1}, d2: {self.d2}, d3: {self.d3}, d4: {self.d4}, d5: {self.d5}, d6: {self.d6}"


class Original:
    def __init__(self, row):
        self.filename = row['filename']
        self.classname = row['classname']
        self.category = Category(row)
        self.is_reference = row['is_reference']
        self.multi_labeled = row['multi_labeled']

    def __str__(self):
        return f"Original: {self.filename}, {self.classname}, {self.category}, {self.is_reference}, {self.multi_labeled}"


class OriginalRecs:
    def __init__(self, df):
        self.originals = [Original(row) for index, row in df.iterrows()]

    def get_reference(self):
        return [original for original in self.originals if original.is_reference]

    def get_non_reference(self):
        return [original for original in self.originals if not original.is_reference]

    def __str__(self):
        return '\n'.join([str(original) for original in self.originals])


class Reference:
    def __init__(self, row):
        self.filename = row['reference_filename']

    def __str__(self):
        return f"Reference: {self.filename}"


class Imitation:
    def __init__(self, row):
        self.ID = row['imitation_id']
        self.imitation_filename = row['imitation_filename']
        self.category = Category(row)
        self.reference = Reference(row)
        self.participant = row['participant_id']
        self.satisfaction = row['satisfaction']
        self.description = row['participants_sound_recording_description']
        self.confidence = row['participants_sound_recording_description_confidence']
