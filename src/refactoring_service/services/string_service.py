class StringService:
    def transform_string(self, text, to_uppercase):
        return text.upper() if to_uppercase else text.lower()

    def get_list_from_string(self, input_list_string, separator=","):
        return input_list_string.split(sep=separator)

    def capitalize_list(self, input_list):
        # iterate over list
        return list(map(str.upper, input_list))

    def convert_to_list_and_capitalize(self, input_list_string):
        input_list = self.get_list_from_string(input_list_string)
        return self.capitalize_list(input_list)
