import os


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

    def discard_non_existing(self, ref_dir, non_ref_dir):
        print("Size before discarding non existing: ", len(self.originals))

        self.originals = [original for original in self.originals if
                          (original.is_reference and os.path.exists(f"{ref_dir}/{original.filename}")) or
                          (not original.is_reference and os.path.exists(
                              f"{non_ref_dir}/{original.classname}/{original.filename}"))]

        print("Size after discarding non existing: ", len(self.originals))
